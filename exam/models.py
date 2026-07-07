"""Core data structures for the Security+ SY0-701 practice exam engine.

Question schema (the single source of truth used by the offline bank, the AI
generator, the exam assembler, and the grader):

A question is a plain ``dict`` with the following keys:

Common keys (every question):
    id          str   - unique stable id, e.g. "d1-001" or "pbq-acl-001"
    domain      int   - 1..5 (SY0-701 exam domain)
    objective   str   - exam objective number, e.g. "1.2"
    type        str   - one of QUESTION_TYPES
    difficulty  str   - "medium" | "hard" | "expert"
    study_topic str   - short label used to build the study plan, e.g.
                        "Cryptographic concepts"
    explanation str   - overall teaching explanation shown after grading

Type-specific keys:

  multiple_choice / multiple_response:
    stem        str
    options     list[dict]   each: {id, text, correct: bool, rationale: str}
                "rationale" explains why that option is right or wrong.
    (multiple_choice has exactly one correct option; multiple_response has
     two or more and the candidate must pick all of them.)

  pbq_matching:  (drag each prompt onto its single best target)
    stem        str
    prompts     list[dict]   each: {id, text}
    targets     list[dict]   each: {id, text}
    answer      dict         {prompt_id: target_id, ...}
    rationales  dict         {prompt_id: "why this pairing is correct"}

  pbq_ordering:  (arrange items into the correct sequence)
    stem        str
    items       list[dict]   each: {id, text}   (presented shuffled)
    answer      list[str]    item ids in correct order
    rationales  dict         {item_id: "why it sits here in the order"}

  pbq_categorize:  (sort each item into exactly one category/bucket)
    stem        str
    categories  list[dict]   each: {id, text}
    items       list[dict]   each: {id, text}
    answer      dict         {item_id: category_id, ...}
    rationales  dict         {item_id: "why it belongs in that category"}
"""

from __future__ import annotations

QUESTION_TYPES = {
    "multiple_choice",
    "multiple_response",
    "pbq_matching",
    "pbq_ordering",
    "pbq_categorize",
}

PBQ_TYPES = {"pbq_matching", "pbq_ordering", "pbq_categorize"}

# Exams in this app use a 1..N domain layout (CompTIA exams have 5 domains,
# Cisco CCNA has 6). The human-readable names and per-exam weightings live in
# exam.catalog; here we only need the set of structurally valid domain numbers.
VALID_DOMAINS = {1, 2, 3, 4, 5, 6}


def is_pbq(question: dict) -> bool:
    return question.get("type") in PBQ_TYPES


def correct_option_ids(question: dict) -> list[str]:
    """Return the set of correct option ids for MC / MR questions."""
    return [o["id"] for o in question.get("options", []) if o.get("correct")]


def validate_question(q: dict) -> list[str]:
    """Return a list of human-readable problems with a question dict.

    An empty list means the question is structurally valid. This is used by
    the bank loader and the AI generator to reject malformed questions before
    they ever reach a candidate.
    """
    errs: list[str] = []
    qid = q.get("id", "<no id>")

    for key in ("id", "domain", "objective", "type", "study_topic", "explanation"):
        if not q.get(key):
            errs.append(f"{qid}: missing required key '{key}'")

    qtype = q.get("type")
    if qtype not in QUESTION_TYPES:
        errs.append(f"{qid}: unknown type '{qtype}'")
        return errs

    if q.get("domain") not in VALID_DOMAINS:
        errs.append(f"{qid}: domain must be 1..6, got {q.get('domain')!r}")

    if qtype in ("multiple_choice", "multiple_response"):
        if not q.get("stem"):
            errs.append(f"{qid}: missing 'stem'")
        opts = q.get("options") or []
        if len(opts) < 3:
            errs.append(f"{qid}: needs at least 3 options")
        ids = [o.get("id") for o in opts]
        if len(set(ids)) != len(ids):
            errs.append(f"{qid}: duplicate option ids {ids}")
        for o in opts:
            if not o.get("text"):
                errs.append(f"{qid}: option {o.get('id')} missing text")
            if not o.get("rationale"):
                errs.append(f"{qid}: option {o.get('id')} missing rationale")
        n_correct = len(correct_option_ids(q))
        if qtype == "multiple_choice" and n_correct != 1:
            errs.append(f"{qid}: multiple_choice must have exactly 1 correct, has {n_correct}")
        if qtype == "multiple_response" and n_correct < 2:
            errs.append(f"{qid}: multiple_response must have >=2 correct, has {n_correct}")

    elif qtype == "pbq_matching":
        prompts = q.get("prompts") or []
        targets = q.get("targets") or []
        answer = q.get("answer") or {}
        if not prompts or not targets:
            errs.append(f"{qid}: matching needs prompts and targets")
        target_ids = {t.get("id") for t in targets}
        for p in prompts:
            pid = p.get("id")
            if pid not in answer:
                errs.append(f"{qid}: prompt {pid} has no answer mapping")
            elif answer[pid] not in target_ids:
                errs.append(f"{qid}: prompt {pid} maps to unknown target {answer[pid]}")

    elif qtype == "pbq_ordering":
        items = q.get("items") or []
        answer = q.get("answer") or []
        item_ids = {i.get("id") for i in items}
        if sorted(answer) != sorted(item_ids):
            errs.append(f"{qid}: ordering answer must be a permutation of item ids")

    elif qtype == "pbq_categorize":
        cats = q.get("categories") or []
        items = q.get("items") or []
        answer = q.get("answer") or {}
        cat_ids = {c.get("id") for c in cats}
        for it in items:
            iid = it.get("id")
            if iid not in answer:
                errs.append(f"{qid}: item {iid} not assigned to a category")
            elif answer[iid] not in cat_ids:
                errs.append(f"{qid}: item {iid} assigned to unknown category {answer[iid]}")

    return errs
