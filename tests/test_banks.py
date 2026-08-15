"""Question-bank integrity tests.

These guard the content itself: every question in every exam must be
schema-valid, IDs must be globally unique, and the multiple-choice /
multiple-response correctness rules must hold. A bad question can't reach a
candidate if these pass.
"""

from collections import Counter

from exam.models import correct_option_ids, validate_question


def test_bank_loads_and_is_nonempty(banks, exam_key):
    assert banks[exam_key], f"{exam_key} bank is empty"


def test_every_question_is_schema_valid(banks, exam_key):
    errors = []
    for q in banks[exam_key]:
        errors.extend(validate_question(q))
    assert not errors, f"{exam_key}: {errors[:5]}"


def test_question_ids_are_unique(banks, exam_key):
    ids = [q["id"] for q in banks[exam_key]]
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    assert not dupes, f"{exam_key} duplicate ids: {dupes[:5]}"


def test_domains_are_within_the_profile(banks, profiles, exam_key):
    valid = set(profiles[exam_key].domains)
    bad = {q["id"]: q["domain"] for q in banks[exam_key] if q["domain"] not in valid}
    assert not bad, f"{exam_key} questions outside declared domains: {list(bad.items())[:5]}"


def test_multiple_choice_has_exactly_one_correct(banks, exam_key):
    offenders = [
        q["id"] for q in banks[exam_key]
        if q["type"] == "multiple_choice" and len(correct_option_ids(q)) != 1
    ]
    assert not offenders, f"{exam_key} MC with !=1 correct: {offenders[:5]}"


def test_multiple_response_has_at_least_two_correct(banks, exam_key):
    offenders = [
        q["id"] for q in banks[exam_key]
        if q["type"] == "multiple_response" and len(correct_option_ids(q)) < 2
    ]
    assert not offenders, f"{exam_key} MR with <2 correct: {offenders[:5]}"


def test_every_option_has_text_and_rationale(banks, exam_key):
    bad = []
    for q in banks[exam_key]:
        for o in q.get("options", []):
            if not o.get("text") or not o.get("rationale"):
                bad.append(f"{q['id']}:{o.get('id')}")
    assert not bad, f"{exam_key} options missing text/rationale: {bad[:5]}"
