"""Flashcard loading and quiz-mode assembly.

Each exam can have a deck module under ``exam/flashcards/<key>.py`` exposing a
module-level list ``CARDS``. A card is a dict:

    {
        "term": "Zero Trust",
        "definition": "A security model that assumes no implicit trust ...",
        "domain": 1,                 # optional, for filtering/labels
        "study_topic": "Zero Trust architecture",  # optional
    }

Two study modes are served from the same deck:
  * multiple_choice — show the definition, pick the matching term from 4
    options (3 distractors are other terms from the same deck).
  * open_ended      — show the definition, recall the term, then reveal it.
"""

from __future__ import annotations

import importlib
import random


def _deck_module(exam_key: str):
    try:
        return importlib.import_module(f"exam.flashcards.{exam_key}")
    except ModuleNotFoundError:
        return None


def load_cards(exam_key: str) -> list[dict]:
    mod = _deck_module(exam_key)
    if mod is None:
        return []
    return [c for c in getattr(mod, "CARDS", []) if c.get("term") and c.get("definition")]


def has_deck(exam_key: str) -> bool:
    return bool(load_cards(exam_key))


def build_flashcard_session(
    exam_key: str,
    mode: str = "multiple_choice",
    num_cards: int = 15,
    seed: int | None = None,
) -> list[dict]:
    """Return a shuffled flashcard session.

    For ``multiple_choice`` each card gets 4 options (its own term plus 3
    distractor terms drawn from the rest of the deck), with the correct index.
    For ``open_ended`` the client shows the definition and reveals the term.
    """
    rng = random.Random(seed)
    cards = load_cards(exam_key)
    if not cards:
        return []
    rng.shuffle(cards)
    chosen = cards[: min(num_cards, len(cards))]

    all_terms = list({c["term"] for c in cards})
    session = []
    for c in chosen:
        item = {
            "term": c["term"],
            "definition": c["definition"],
            "domain": c.get("domain"),
            "study_topic": c.get("study_topic", ""),
        }
        if mode == "multiple_choice":
            distractors = [t for t in all_terms if t != c["term"]]
            rng.shuffle(distractors)
            opts = distractors[:3] + [c["term"]]
            rng.shuffle(opts)
            item["options"] = opts
            item["answer_index"] = opts.index(c["term"])
        session.append(item)
    return session
