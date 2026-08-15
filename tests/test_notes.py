"""Study-notes linkage tests.

The "missed question -> relevant note" feature only works if every question's
``study_topic`` resolves to a note. For any exam that ships notes, this test
enforces 100% coverage so the linkage can't silently rot.
"""

from exam.notes_loader import _study_topic_index, load_notes


def test_notes_cover_every_quiz_topic(profiles, banks, exam_key):
    profile = profiles[exam_key]
    notes = load_notes(profile)
    if not notes:
        # Not every exam ships notes yet; only enforce coverage where they exist.
        import pytest
        pytest.skip(f"{exam_key} has no study notes")

    covered = set(_study_topic_index(profile).keys())
    quiz_topics = {q["study_topic"] for q in banks[exam_key]}
    missing = quiz_topics - covered
    assert not missing, f"{exam_key} topics with no note: {sorted(missing)}"


def test_note_study_topics_reference_real_labels(profiles, banks, exam_key):
    """A note shouldn't point at a study_topic that no question uses."""
    profile = profiles[exam_key]
    notes = load_notes(profile)
    if not notes:
        import pytest
        pytest.skip(f"{exam_key} has no study notes")

    quiz_topics = {q["study_topic"] for q in banks[exam_key]}
    orphans = []
    for n in notes:
        for st in n.get("study_topics", []):
            if st not in quiz_topics:
                orphans.append((n.get("topic"), st))
    assert not orphans, f"{exam_key} notes referencing unused topics: {orphans[:5]}"
