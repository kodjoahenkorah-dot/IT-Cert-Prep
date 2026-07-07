"""Exam assembly.

Builds a fresh practice exam by sampling the question bank according to the
exam's official domain weightings, mixing in a few PBQs, shuffling answer
order, and tracking which questions a candidate has already seen so repeated
exams pull different questions for as long as the bank allows.

All exam-specific knowledge (domain weights, "seen" history namespace) comes
from an :class:`exam.catalog.ExamProfile` passed in by the caller.
"""

from __future__ import annotations

import copy
import json
import os
import random

from .models import PBQ_TYPES

_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


# --------------------------------------------------------------------------- #
# "Seen question" persistence (namespaced per exam)                            #
# --------------------------------------------------------------------------- #
def _seen_path(exam_key: str) -> str:
    return os.path.join(_DATA_DIR, f"seen_{exam_key}.json")


def _load_seen(exam_key: str) -> set[str]:
    try:
        with open(_seen_path(exam_key), "r", encoding="utf-8") as fh:
            return set(json.load(fh))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()


def _save_seen(exam_key: str, seen: set[str]) -> None:
    os.makedirs(_DATA_DIR, exist_ok=True)
    with open(_seen_path(exam_key), "w", encoding="utf-8") as fh:
        json.dump(sorted(seen), fh)


def reset_seen(exam_key: str) -> None:
    """Forget the history of seen questions for one exam (a 'fresh start')."""
    path = _seen_path(exam_key)
    if os.path.exists(path):
        os.remove(path)


# --------------------------------------------------------------------------- #
# Sampling helpers                                                             #
# --------------------------------------------------------------------------- #
def _weighted_domain_counts(domains: dict, total: int) -> dict[int, int]:
    """Distribute ``total`` non-PBQ questions across domains by exam weight."""
    counts: dict[int, int] = {}
    # Largest-remainder method so the counts sum exactly to ``total``.
    raw = {d: domains[d]["weight"] * total for d in domains}
    for d in domains:
        counts[d] = int(raw[d])
    remainder = total - sum(counts.values())
    leftovers = sorted(domains, key=lambda d: raw[d] - int(raw[d]), reverse=True)
    for d in leftovers[:remainder]:
        counts[d] += 1
    return counts


def _pick(pool: list[dict], n: int, seen: set[str], rng: random.Random) -> list[dict]:
    """Pick ``n`` questions from ``pool`` with strict rotation.

    Guarantee: a question is never shown again until every OTHER question in
    the same pool has been shown. ``seen`` is mutated in place to record the
    new cycle state, and is persisted by the caller.

    How rotation works: we draw from the unseen portion first. If the unseen
    portion can't satisfy ``n``, the current cycle is complete — we take what
    unseen remains, then reset the cycle for this pool (clear its seen marks)
    and draw the rest from the freshly-reset pool, deliberately excluding the
    questions just shown so none repeats across the cycle boundary.
    """
    pool_ids = {q["id"] for q in pool}
    unseen = [q for q in pool if q["id"] not in seen]
    rng.shuffle(unseen)
    chosen = unseen[:n]

    if len(chosen) < n:
        # Cycle complete: everything in this pool has now been shown. Start a
        # fresh cycle, but don't immediately repeat the boundary questions.
        seen -= pool_ids  # reset this pool's history
        already = {q["id"] for q in chosen}
        fresh = [q for q in pool if q["id"] not in already]
        rng.shuffle(fresh)
        chosen.extend(fresh[: n - len(chosen)])

    for q in chosen:
        seen.add(q["id"])
    return chosen


# --------------------------------------------------------------------------- #
# Answer-order shuffling                                                        #
# --------------------------------------------------------------------------- #
def _shuffle_question(q: dict, rng: random.Random) -> dict:
    """Return a deep copy with option / item order randomised.

    Correctness is encoded on the option objects (or in answer maps), so
    shuffling presentation order never breaks grading.
    """
    q = copy.deepcopy(q)
    if q["type"] in ("multiple_choice", "multiple_response"):
        rng.shuffle(q["options"])
    elif q["type"] == "pbq_matching":
        rng.shuffle(q["prompts"])
        rng.shuffle(q["targets"])
    elif q["type"] == "pbq_ordering":
        rng.shuffle(q["items"])
    elif q["type"] == "pbq_categorize":
        rng.shuffle(q["items"])
        rng.shuffle(q["categories"])
    return q


# --------------------------------------------------------------------------- #
# Public API                                                                   #
# --------------------------------------------------------------------------- #
def build_exam(
    profile,
    bank: list[dict],
    num_questions: int | None = None,
    num_pbqs: int | None = None,
    track_seen: bool = True,
    seed: int | None = None,
) -> list[dict]:
    """Assemble a fresh exam for ``profile`` from its ``bank``.

    Returns a list of (deep-copied, answer-shuffled) question dicts ready to
    serve. Marks the chosen questions as seen so the next call pulls different
    ones until the bank is exhausted.
    """
    if num_questions is None:
        num_questions = profile.default_num_questions
    if num_pbqs is None:
        num_pbqs = profile.default_pbqs

    rng = random.Random(seed)
    seen = _load_seen(profile.key) if track_seen else set()

    pbq_pool = [q for q in bank if q["type"] in PBQ_TYPES]
    mc_pool = [q for q in bank if q["type"] not in PBQ_TYPES]

    num_pbqs = min(num_pbqs, len(pbq_pool))
    num_mc = max(0, num_questions - num_pbqs)

    domain_counts = _weighted_domain_counts(profile.domains, num_mc)
    chosen: list[dict] = []
    for domain, n in domain_counts.items():
        pool = [q for q in mc_pool if q["domain"] == domain]
        chosen.extend(_pick(pool, n, seen, rng))

    # Top up if some domain pool was too small to hit its quota.
    if len(chosen) < num_mc:
        chosen_ids = {q["id"] for q in chosen}
        rest = [q for q in mc_pool if q["id"] not in chosen_ids]
        chosen.extend(_pick(rest, num_mc - len(chosen), seen, rng))

    chosen.extend(_pick(pbq_pool, num_pbqs, seen, rng))

    # _pick already recorded the chosen ids in `seen` (and reset cycles as
    # needed); just persist the updated rotation state.
    if track_seen:
        _save_seen(profile.key, seen)

    rng.shuffle(chosen)
    return [_shuffle_question(q, rng) for q in chosen]


def build_study_session(
    profile,
    bank: list[dict],
    domain: int | None = None,
    topics: list[str] | None = None,
    num_questions: int = 20,
    include_pbqs: bool = True,
    track_seen: bool = True,
    seed: int | None = None,
) -> list[dict]:
    """Build an untimed Study-Mode session, optionally scoped to a domain/topics.

    Unlike ``build_exam`` this does not weight by domain; it simply draws from
    the requested slice (a whole domain, specific topics, or the whole bank),
    preferring unseen questions. Used by Study Mode's topic drills.
    """
    rng = random.Random(seed)
    seen = _load_seen(profile.key) if track_seen else set()

    pool = bank
    if domain is not None:
        pool = [q for q in pool if q["domain"] == domain]
    if topics:
        wanted = set(topics)
        pool = [q for q in pool if q.get("study_topic") in wanted]
    if not include_pbqs:
        pool = [q for q in pool if q["type"] not in PBQ_TYPES]

    if not pool:
        return []

    # Same strict rotation as exam mode: no repeat until the chosen slice is
    # exhausted, then a clean cycle.
    chosen = _pick(pool, num_questions, seen, rng)
    if track_seen:
        _save_seen(profile.key, seen)

    rng.shuffle(chosen)
    return [_shuffle_question(q, rng) for q in chosen]


def topics_by_domain(bank: list[dict]) -> dict[int, list[str]]:
    """Return the sorted distinct study_topics available per domain in a bank."""
    out: dict[int, set] = {}
    for q in bank:
        out.setdefault(q["domain"], set()).add(q.get("study_topic", ""))
    return {d: sorted(t for t in ts if t) for d, ts in sorted(out.items())}


def build_adaptive_quiz(
    profile,
    bank: list[dict],
    weak_topics: list[str],
    num_questions: int = 20,
    track_seen: bool = True,
    seed: int | None = None,
) -> list[dict]:
    """Assemble a quiz that focuses on the candidate's weak ``study_topic``s.

    Questions are drawn ONLY from the missed topics, using the same strict
    rotation as the other modes: no question repeats until the weak-topic pool
    is exhausted, then a clean cycle begins.
    """
    rng = random.Random(seed)
    seen = _load_seen(profile.key) if track_seen else set()
    weak = set(weak_topics)

    pool = [q for q in bank if q.get("study_topic") in weak]
    if not pool:
        # Nothing matched (shouldn't happen) -> fall back to a normal short quiz.
        return build_exam(profile, bank, num_questions, num_pbqs=0,
                          track_seen=track_seen, seed=seed)

    chosen = _pick(pool, num_questions, seen, rng)
    if track_seen:
        _save_seen(profile.key, seen)

    rng.shuffle(chosen)
    return [_shuffle_question(q, rng) for q in chosen]
