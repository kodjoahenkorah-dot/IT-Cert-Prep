"""Optional AI question generation via the Claude API.

This module is entirely optional. When an ``ANTHROPIC_API_KEY`` is present and
the ``anthropic`` package is installed, the web app can generate brand-new,
never-before-seen questions on demand for whichever exam is selected. When it
isn't, the app silently falls back to the large offline bank.

Generated questions follow the exact schema in :mod:`exam.models` and are run
through :func:`validate_question` before use, so a malformed model response is
discarded rather than shown to the candidate.
"""

from __future__ import annotations

import json
import os
import uuid

from .models import validate_question

MODEL = os.environ.get("SECPLUS_MODEL", "claude-opus-4-8")

# Exam-agnostic schema instructions. The exam-specific framing (which exam,
# which domains) is supplied by the ExamProfile's ai_system_prompt.
SCHEMA_INSTRUCTIONS = """\
Output rules:
- Return ONLY a JSON array of question objects. No prose, no markdown fences.
- Each object MUST match one of these schemas exactly.

multiple_choice / multiple_response:
{"id": str, "domain": int 1-5, "objective": str e.g. "2.4", "type": "multiple_choice" or "multiple_response", "difficulty": "hard" or "expert", "study_topic": short label, "stem": scenario question, "options": [{"id": "a", "text": str, "correct": bool, "rationale": "why this option is right or WRONG — be specific"}, ... 4 options], "explanation": overall teaching explanation}

multiple_choice has exactly ONE correct option; multiple_response has TWO OR MORE and the stem must say how many to choose.

pbq_matching (drag prompts to targets):
{"id": str, "domain": int, "objective": str, "type": "pbq_matching", "difficulty": "hard", "study_topic": str, "stem": str, "prompts": [{"id": str, "text": str}], "targets": [{"id": str, "text": str}], "answer": {prompt_id: target_id}, "rationales": {prompt_id: "why this pairing"}, "explanation": str}

pbq_ordering (put items in correct sequence):
{"id": str, "domain": int, "objective": str, "type": "pbq_ordering", "difficulty": "hard", "study_topic": str, "stem": str, "items": [{"id": str, "text": str}], "answer": [item_id in correct order], "rationales": {item_id: "why it sits here"}, "explanation": str}

pbq_categorize (sort items into categories):
{"id": str, "domain": int, "objective": str, "type": "pbq_categorize", "difficulty": "hard", "study_topic": str, "stem": str, "categories": [{"id": str, "text": str}], "items": [{"id": str, "text": str}], "answer": {item_id: category_id}, "rationales": {item_id: "why it belongs there"}, "explanation": str}

Every distractor rationale must explain the specific misconception it targets. \
Make the questions genuinely hard."""


def ai_available() -> bool:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return False
    return True


def _extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.rsplit("```", 1)[0]
    start = text.find("[")
    end = text.rfind("]")
    if start != -1 and end != -1:
        text = text[start : end + 1]
    return json.loads(text)


def generate_questions(
    profile,
    domain_counts: dict[int, int],
    num_pbqs: int = 3,
    avoid_topics: list[str] | None = None,
) -> list[dict]:
    """Generate fresh questions for ``profile`` via the Claude API.

    ``domain_counts`` maps domain number -> how many MC/MR questions to make.
    Raises if the API is unavailable; callers should check ``ai_available()``.
    """
    import anthropic

    client = anthropic.Anthropic()
    system_prompt = profile.ai_system_prompt + "\n\n" + SCHEMA_INSTRUCTIONS

    avoid = ""
    if avoid_topics:
        avoid = (
            "\n\nAvoid re-using these exact scenarios from earlier exams: "
            + "; ".join(avoid_topics[:40])
        )

    plan_lines = [
        f"- Domain {d} ({profile.domains[d]['name']}): {n} multiple_choice/multiple_response questions"
        for d, n in domain_counts.items()
        if n
    ]
    if num_pbqs:
        plan_lines.append(
            f"- {num_pbqs} performance-based questions (mix of pbq_matching, "
            "pbq_ordering, pbq_categorize), spread across domains"
        )

    user_msg = (
        f"Generate a complete set of brand-new {profile.name} practice questions "
        "with this composition:\n" + "\n".join(plan_lines) + avoid +
        "\n\nMake every id unique. Return the single JSON array now."
    )

    resp = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = "".join(block.text for block in resp.content if block.type == "text")
    questions = _extract_json(raw)

    valid: list[dict] = []
    for q in questions:
        q["id"] = f"ai-{uuid.uuid4().hex[:10]}"
        if not validate_question(q):
            valid.append(q)
    return valid
