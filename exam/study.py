"""Per-attempt study guide builder.

After a quiz is graded, this assembles a study guide tailored to THAT attempt:
- the headline/score context,
- the weak topics ranked worst-first,
- the specific notes that cover those weak topics (so the candidate reads
  exactly what they need), and
- a focused action plan.

It reuses the grade report's ``study_plan`` (which already ranks weak topics)
and the notes linkage in :mod:`exam.notes`.
"""

from __future__ import annotations

from .notes_loader import notes_for_topics


def build_attempt_guide(profile, report: dict) -> dict:
    """Build a study guide specific to one graded attempt.

    Returns a dict consumed by the results/guide templates.
    """
    plan = report["study_plan"]
    summary = report["summary"]
    weak_labels = plan.get("weak_topic_labels", [])

    # Notes that cover the missed topics, in domain/topic order.
    relevant_notes = notes_for_topics(profile, weak_labels)

    # A focused, ordered action plan: tackle weakest topics first, naming the
    # note section to read for each.
    note_topics = {n["topic"] for n in relevant_notes}
    actions = []
    for t in plan.get("weak_topics", []):
        label = t["topic"]
        has_note = label in note_topics or any(
            label in n.get("study_topics", []) for n in relevant_notes
        )
        line = (
            f"Review '{label}' (Domain {t['domain']} — {t['domain_name']}): "
            f"you scored {t['correct']}/{t['total']} ({t['percent']}%)."
        )
        if has_note:
            line += " See the matching notes section below."
        actions.append(line)

    if summary["passed"]:
        intro = (
            f"You passed this attempt ({summary['percent']}%). This guide targets the "
            "specific topics you still missed so you can lock them down before exam day."
        )
    else:
        intro = (
            f"This guide is built from your {summary['percent']}% attempt. Work through the "
            "topics below (weakest first), read the linked notes, then take a "
            "weakness-focused quiz to confirm improvement."
        )

    return {
        "exam_name": summary["exam_name"],
        "intro": intro,
        "weak_topics": plan.get("weak_topics", []),
        "actions": actions,
        "notes": relevant_notes,
        "has_weak_topics": bool(weak_labels),
        "weak_topic_labels": weak_labels,
    }
