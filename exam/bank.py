"""Loads and validates a per-exam offline question bank.

Each exam has its own subpackage under ``exam/questions/`` (e.g.
``exam.questions.secplus``). Every module in that subpackage exposes a
module-level list called ``QUESTIONS``. This loader imports them all,
validates each question against the schema in :mod:`exam.models`, and exposes
the combined, de-duplicated bank for one exam.
"""

from __future__ import annotations

import importlib
import pkgutil

from .models import validate_question

# Cache loaded banks by package name so we don't re-import on every request.
_CACHE: dict[str, list[dict]] = {}


def _iter_question_modules(package_name: str):
    package = importlib.import_module(package_name)
    for modinfo in pkgutil.iter_modules(package.__path__):
        if modinfo.name.startswith("_"):
            continue
        yield importlib.import_module(f"{package_name}.{modinfo.name}")


def load_bank(package_name: str, strict: bool = False) -> list[dict]:
    """Return the validated question bank for one exam's question package.

    With ``strict=True`` a malformed question raises ``ValueError``; otherwise
    malformed questions are skipped with a printed warning so one bad question
    can't take down the whole app.
    """
    if not strict and package_name in _CACHE:
        return _CACHE[package_name]

    bank: list[dict] = []
    seen_ids: set[str] = set()

    for module in _iter_question_modules(package_name):
        for q in getattr(module, "QUESTIONS", []):
            errs = validate_question(q)
            if errs:
                msg = "; ".join(errs)
                if strict:
                    raise ValueError(f"Invalid question in {module.__name__}: {msg}")
                print(f"[bank] skipping invalid question: {msg}")
                continue
            qid = q["id"]
            if qid in seen_ids:
                if strict:
                    raise ValueError(f"Duplicate question id: {qid}")
                print(f"[bank] skipping duplicate id: {qid}")
                continue
            seen_ids.add(qid)
            bank.append(q)

    _CACHE[package_name] = bank
    return bank


def bank_stats(bank: list[dict]) -> dict:
    """Summarise how many questions exist per domain and per type."""
    by_domain: dict[int, int] = {}
    by_type: dict[str, int] = {}
    for q in bank:
        by_domain[q["domain"]] = by_domain.get(q["domain"], 0) + 1
        by_type[q["type"]] = by_type.get(q["type"], 0) + 1
    return {"total": len(bank), "by_domain": by_domain, "by_type": by_type}
