"""Grading tests across all question types.

Verifies that the server-side grader accepts correct answers, rejects wrong
ones, and returns the explanation payload the UI depends on.
"""

import pytest

from exam.grading import grade_one
from exam.models import correct_option_ids


def _first(bank, qtype):
    return next((q for q in bank if q["type"] == qtype), None)


def test_multiple_choice_correct_and_incorrect(banks, exam_key):
    q = _first(banks[exam_key], "multiple_choice")
    assert q is not None
    right = correct_option_ids(q)[0]
    wrong = next(o["id"] for o in q["options"] if o["id"] != right)
    assert grade_one(q, right)["is_correct"] is True
    assert grade_one(q, wrong)["is_correct"] is False


def test_multiple_response_requires_exact_set(banks, exam_key):
    q = _first(banks[exam_key], "multiple_response")
    if q is None:
        pytest.skip(f"{exam_key} has no multiple_response questions")
    correct = correct_option_ids(q)
    assert grade_one(q, list(correct))["is_correct"] is True
    # a partial answer (drop one correct option) must not count as correct
    assert grade_one(q, list(correct)[:-1])["is_correct"] is False


def test_grade_one_payload_shape(banks, exam_key):
    q = _first(banks[exam_key], "multiple_choice")
    result = grade_one(q, correct_option_ids(q)[0])
    for key in ("id", "is_correct", "type", "study_topic", "explanation", "detail"):
        assert key in result, f"grade_one missing '{key}'"
    assert result["is_correct"] is True


def test_pbq_ordering_grades_correct_permutation(banks):
    """Find any ordering PBQ and confirm its own answer key grades correct."""
    for key, bank in banks.items():
        q = _first(bank, "pbq_ordering")
        if q:
            assert grade_one(q, q["answer"])["is_correct"] is True
            return
    pytest.skip("no ordering PBQs in any bank")
