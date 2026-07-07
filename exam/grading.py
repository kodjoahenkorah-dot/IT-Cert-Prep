"""Grading, per-question explanations, and the end-of-exam study plan.

A "response" maps a question id to the candidate's answer. The shape of the
answer depends on the question type:

    multiple_choice    -> option id (str)             e.g. "b"
    multiple_response  -> list of option ids          e.g. ["a", "c"]
    pbq_matching       -> {prompt_id: target_id}
    pbq_ordering       -> [item_id, ...]  (the order the candidate chose)
    pbq_categorize     -> {item_id: category_id}
"""

from __future__ import annotations

from .models import correct_option_ids


def _grade_choice(q: dict, answer) -> bool:
    correct = set(correct_option_ids(q))
    if q["type"] == "multiple_choice":
        return answer in correct
    given = set(answer or [])
    return given == correct


def _grade_matching(q: dict, answer) -> bool:
    answer = answer or {}
    return all(answer.get(pid) == tid for pid, tid in q["answer"].items())


def _grade_ordering(q: dict, answer) -> bool:
    return list(answer or []) == list(q["answer"])


def _grade_categorize(q: dict, answer) -> bool:
    answer = answer or {}
    return all(answer.get(iid) == cid for iid, cid in q["answer"].items())


_GRADERS = {
    "multiple_choice": _grade_choice,
    "multiple_response": _grade_choice,
    "pbq_matching": _grade_matching,
    "pbq_ordering": _grade_ordering,
    "pbq_categorize": _grade_categorize,
}


def _option_text(q: dict, oid: str) -> str:
    for o in q.get("options", []):
        if o["id"] == oid:
            return o["text"]
    return oid


def _explain_choice(q: dict, answer) -> dict:
    """Build the why-right / why-wrong breakdown for MC and MR questions."""
    correct = set(correct_option_ids(q))
    given = {answer} if q["type"] == "multiple_choice" else set(answer or [])
    breakdown = []
    for o in q["options"]:
        breakdown.append(
            {
                "text": o["text"],
                "correct": bool(o.get("correct")),
                "chosen": o["id"] in given,
                "rationale": o.get("rationale", ""),
            }
        )
    return {
        "correct_answers": [_option_text(q, oid) for oid in correct],
        "your_answers": [_option_text(q, oid) for oid in given] or ["(left blank)"],
        "options": breakdown,
    }


def _explain_matching(q: dict, answer) -> dict:
    answer = answer or {}
    prompt_text = {p["id"]: p["text"] for p in q["prompts"]}
    target_text = {t["id"]: t["text"] for t in q["targets"]}
    rows = []
    for pid, correct_tid in q["answer"].items():
        chosen_tid = answer.get(pid)
        rows.append(
            {
                "prompt": prompt_text.get(pid, pid),
                "correct": target_text.get(correct_tid, correct_tid),
                "yours": target_text.get(chosen_tid, "(left blank)"),
                "ok": chosen_tid == correct_tid,
                "rationale": q.get("rationales", {}).get(pid, ""),
            }
        )
    return {"rows": rows}


def _explain_ordering(q: dict, answer) -> dict:
    answer = list(answer or [])
    item_text = {i["id"]: i["text"] for i in q["items"]}
    rows = []
    for pos, correct_iid in enumerate(q["answer"]):
        yours_iid = answer[pos] if pos < len(answer) else None
        rows.append(
            {
                "position": pos + 1,
                "correct": item_text.get(correct_iid, correct_iid),
                "yours": item_text.get(yours_iid, "(blank)"),
                "ok": yours_iid == correct_iid,
                "rationale": q.get("rationales", {}).get(correct_iid, ""),
            }
        )
    return {"rows": rows}


def _explain_categorize(q: dict, answer) -> dict:
    answer = answer or {}
    item_text = {i["id"]: i["text"] for i in q["items"]}
    cat_text = {c["id"]: c["text"] for c in q["categories"]}
    rows = []
    for iid, correct_cid in q["answer"].items():
        chosen_cid = answer.get(iid)
        rows.append(
            {
                "item": item_text.get(iid, iid),
                "correct": cat_text.get(correct_cid, correct_cid),
                "yours": cat_text.get(chosen_cid, "(left blank)"),
                "ok": chosen_cid == correct_cid,
                "rationale": q.get("rationales", {}).get(iid, ""),
            }
        )
    return {"rows": rows}


_EXPLAINERS = {
    "multiple_choice": _explain_choice,
    "multiple_response": _explain_choice,
    "pbq_matching": _explain_matching,
    "pbq_ordering": _explain_ordering,
    "pbq_categorize": _explain_categorize,
}


def grade_one(question: dict, answer) -> dict:
    """Grade a single question and return its correctness + full explanation.

    Used by Study Mode for immediate per-question feedback. ``question`` here is
    the full (answer-key-bearing) question dict, not the public one.
    """
    is_correct = _GRADERS[question["type"]](question, answer)
    return {
        "id": question["id"],
        "is_correct": is_correct,
        "type": question["type"],
        "study_topic": question["study_topic"],
        "explanation": question["explanation"],
        "detail": _EXPLAINERS[question["type"]](question, answer),
    }


def grade_exam(profile, exam: list[dict], responses: dict) -> dict:
    """Grade a completed exam and produce a full results payload."""
    domains = profile.domains
    pass_percent = profile.pass_percent
    results = []
    correct_count = 0
    per_domain = {d: {"correct": 0, "total": 0} for d in domains}
    per_topic: dict[str, dict] = {}

    for q in exam:
        answer = responses.get(q["id"])
        is_correct = _GRADERS[q["type"]](q, answer)
        correct_count += int(is_correct)

        d = q["domain"]
        per_domain[d]["total"] += 1
        per_domain[d]["correct"] += int(is_correct)

        topic = q["study_topic"]
        bucket = per_topic.setdefault(topic, {"correct": 0, "total": 0, "domain": d})
        bucket["total"] += 1
        bucket["correct"] += int(is_correct)

        results.append(
            {
                "id": q["id"],
                "domain": d,
                "domain_name": domains[d]["name"],
                "objective": q["objective"],
                "type": q["type"],
                "study_topic": topic,
                "stem": q.get("stem", ""),
                "is_correct": is_correct,
                "explanation": q["explanation"],
                "detail": _EXPLAINERS[q["type"]](q, answer),
            }
        )

    total = len(exam)
    percent = round(100 * correct_count / total, 1) if total else 0.0
    scaled = round(100 + (percent / 100) * 800)  # 100..900 scale approximation

    summary = {
        "total": total,
        "correct": correct_count,
        "percent": percent,
        "scaled_score": scaled,
        "passed": percent >= pass_percent,
        "pass_percent": pass_percent,
        "exam_name": profile.name,
        "per_domain": {
            d: {
                "name": domains[d]["name"],
                "weight": domains[d]["weight"],
                **per_domain[d],
                "percent": round(100 * per_domain[d]["correct"] / per_domain[d]["total"], 1)
                if per_domain[d]["total"]
                else None,
            }
            for d in domains
        },
    }

    return {
        "summary": summary,
        "results": results,
        "study_plan": build_study_plan(profile, summary, per_topic),
    }


def build_study_plan(profile, summary: dict, per_topic: dict) -> dict:
    """Turn the score breakdown into concrete, prioritised study advice."""
    domains = profile.domains
    # Rank domains worst-first (only those that had questions).
    domains_ranked = sorted(
        (
            (d, info)
            for d, info in summary["per_domain"].items()
            if info["total"] and info["percent"] is not None
        ),
        key=lambda kv: kv[1]["percent"],
    )

    # Rank specific topics worst-first, requiring at least one miss.
    topics_ranked = sorted(
        (
            {
                "topic": t,
                "domain": info["domain"],
                "domain_name": domains[info["domain"]]["name"],
                "correct": info["correct"],
                "total": info["total"],
                "percent": round(100 * info["correct"] / info["total"], 1),
            }
            for t, info in per_topic.items()
            if info["correct"] < info["total"]
        ),
        key=lambda x: (x["percent"], -x["total"]),
    )

    if summary["passed"]:
        headline = (
            f"You scored {summary['percent']}% (~{summary['scaled_score']}/900) — that's a "
            f"PASS against the {profile.short_name} bar. Keep these weak spots tight before exam day."
        )
    else:
        gap = round(summary["pass_percent"] - summary["percent"], 1)
        headline = (
            f"You scored {summary['percent']}% (~{summary['scaled_score']}/900). You're "
            f"{gap} points under the ~{summary['pass_percent']}% pass line. Focus your "
            "study on the areas below, then generate a fresh exam and retest."
        )

    advice = []
    for d, info in domains_ranked[:3]:
        if info["percent"] >= 85:
            continue
        advice.append(
            f"Domain {d} — {info['name']}: {info['correct']}/{info['total']} "
            f"({info['percent']}%). This domain is {int(info['weight'] * 100)}% of the "
            "real exam, so improvement here moves your score the most."
        )

    return {
        "headline": headline,
        "weak_domains": advice,
        "weak_topics": topics_ranked[:8],
        "all_topics": topics_ranked,
        # Bare list of every missed study_topic label, worst-first. Drives the
        # weakness-focused adaptive quiz and the per-attempt notes linkage.
        "weak_topic_labels": [t["topic"] for t in topics_ranked],
    }
