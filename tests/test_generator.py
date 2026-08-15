"""Exam-assembly and rotation tests.

Covers the two properties that make the practice exams useful: they are
composed to the exam's official domain weighting, and repeated exams don't
recycle a question until the relevant pool is exhausted.
"""

from exam import generator
from exam.generator import build_exam


def test_build_exam_returns_requested_count(profiles, banks, exam_key):
    profile, bank = profiles[exam_key], banks[exam_key]
    exam = build_exam(profile, bank, num_questions=40, num_pbqs=2, track_seen=False, seed=1)
    assert len(exam) == 40


def test_pbq_count_is_respected(profiles, banks, exam_key):
    profile, bank = profiles[exam_key], banks[exam_key]
    exam = build_exam(profile, bank, num_questions=40, num_pbqs=5, track_seen=False, seed=2)
    pbqs = [q for q in exam if q["type"].startswith("pbq")]
    # The bank may not have 5 PBQs for a given exam, so allow up to the request.
    assert len(pbqs) <= 5
    non_pbq = [q for q in exam if not q["type"].startswith("pbq")]
    assert len(non_pbq) >= 35


def test_no_duplicate_questions_within_one_exam(profiles, banks, exam_key):
    profile, bank = profiles[exam_key], banks[exam_key]
    exam = build_exam(profile, bank, num_questions=40, num_pbqs=2, track_seen=False, seed=3)
    ids = [q["id"] for q in exam]
    assert len(set(ids)) == len(ids)


def test_composition_approximates_domain_weights(profiles, banks):
    """A large single-domain-weighted draw should land near the blueprint."""
    profile, bank = profiles["secplus"], banks["secplus"]
    exam = build_exam(profile, bank, num_questions=90, num_pbqs=0, track_seen=False, seed=7)
    from collections import Counter
    counts = Counter(q["domain"] for q in exam)
    for d, info in profile.domains.items():
        expected = info["weight"] * 90
        # within +/- 4 questions of the target is plenty for this bank size
        assert abs(counts.get(d, 0) - expected) <= 4, (
            f"domain {d}: got {counts.get(d, 0)}, expected ~{expected:.0f}")


def test_rotation_serves_fresh_questions(profiles, banks, monkeypatch, tmp_path):
    """Consecutive exams shouldn't repeat non-PBQ questions until the pool
    is exhausted. We redirect the seen-state to a temp dir so the test is
    hermetic and leaves no files behind."""
    monkeypatch.setattr(generator, "_DATA_DIR", str(tmp_path))
    profile, bank = profiles["secplus"], banks["secplus"]

    seen = set()
    repeats = 0
    for _ in range(5):
        exam = build_exam(profile, bank, num_questions=90, num_pbqs=0, track_seen=True)
        ids = [q["id"] for q in exam]
        repeats += sum(1 for i in ids if i in seen)
        seen.update(ids)
    # 5 x 90 = 450 unique draws from a 1,800+ MC pool => zero repeats expected.
    assert repeats == 0, f"{repeats} questions repeated before the pool was exhausted"
