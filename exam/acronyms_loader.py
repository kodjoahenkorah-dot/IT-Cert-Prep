"""Acronym-drill loading and session assembly.

Deck module: ``exam/acronyms/<key>.py`` exposing ``ACRONYMS`` — a list of
``{"acronym", "expansion", "domain"}`` dicts.

Two study modes (both graded instantly, client-side):
  * multiple_choice — show the acronym, pick its correct expansion from 4.
  * typed           — show the acronym, type the expansion; graded leniently
                      (case/punctuation-insensitive significant-word match),
                      with the canonical expansion always revealed.
"""

from __future__ import annotations

import importlib
import random
import re

_CACHE: dict[str, list[dict]] = {}

# Words ignored when leniently grading a typed expansion.
_STOP = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or",
         "the", "to", "with"}


def load_acronyms(exam_key: str) -> list[dict]:
    if exam_key in _CACHE:
        return _CACHE[exam_key]
    try:
        mod = importlib.import_module(f"exam.acronyms.{exam_key}")
    except ModuleNotFoundError:
        _CACHE[exam_key] = []
        return []
    cards = [
        a for a in getattr(mod, "ACRONYMS", [])
        if a.get("acronym") and a.get("expansion")
    ]
    _CACHE[exam_key] = cards
    return cards


def has_deck(exam_key: str) -> bool:
    return bool(load_acronyms(exam_key))


def significant_tokens(text: str) -> list[str]:
    """Normalized significant words for lenient typed grading."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w for w in words if w not in _STOP]


def build_acronym_session(
    exam_key: str,
    mode: str = "multiple_choice",
    num_cards: int = 15,
    seed: int | None = None,
) -> list[dict]:
    rng = random.Random(seed)
    deck = load_acronyms(exam_key)
    if not deck:
        return []
    rng.shuffle(deck)
    chosen = deck[: min(num_cards, len(deck))]

    all_expansions = list({a["expansion"] for a in deck})
    session = []
    for a in chosen:
        item = {
            "acronym": a["acronym"],
            "expansion": a["expansion"],
            "domain": a.get("domain"),
            # significant-word set used by the client to grade typed answers
            "accept_tokens": significant_tokens(a["expansion"]),
        }
        if mode == "multiple_choice":
            distractors = [e for e in all_expansions if e != a["expansion"]]
            rng.shuffle(distractors)
            opts = distractors[:3] + [a["expansion"]]
            rng.shuffle(opts)
            item["options"] = opts
            item["answer_index"] = opts.index(a["expansion"])
        session.append(item)
    return session
