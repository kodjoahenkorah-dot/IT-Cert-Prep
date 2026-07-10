"""Diagnostic test: builds a short assessment and analyses the result to
estimate pass readiness and diagnose *why* the candidate misses questions.

The analysis produces:
  * an estimated percentage chance of passing the real exam (clearly an
    estimate, with a confidence note that scales with sample size),
  * strongest and weakest domains,
  * weakest subtopics,
  * a behavioural read — whether misses look like missing knowledge,
    misreading/distractor-traps, or guessing/rushing — inferred from answer
    correctness, per-question time, and how clustered the misses are,
  * a recommended study path.
"""

from __future__ import annotations

import math

from .grading import _GRADERS


def build_diagnostic(profile, bank, num_questions, seed=None):
    """Build a diagnostic of MC/MR questions weighted across domains.

    PBQs are excluded so per-question timing is clean and comparable.
    """
    from .generator import build_exam
    # Reuse the weighted assembler but force zero PBQs; don't burn seen-history
    # so a diagnostic never eats into fresh practice questions.
    return build_exam(profile, bank, num_questions=num_questions, num_pbqs=0,
                      track_seen=False, seed=seed)


def _pass_probability(percent: float) -> float:
    """Map a diagnostic score to an estimated pass probability.

    The diagnostic is deliberately harder than the live exam, so the curve is
    centred a little below the real ~83% pass line. Logistic, clamped 3-98%.
    """
    p = 1.0 / (1.0 + math.exp(-(percent - 68.0) / 8.0))
    return max(0.03, min(0.98, p))


def analyze_diagnostic(profile, questions, responses, times_ms):
    """Grade the diagnostic and produce the full analysis payload.

    ``questions`` are the full (answer-key) question dicts; ``responses`` maps
    question id -> answer; ``times_ms`` maps question id -> milliseconds spent.
    """
    domains = profile.domains
    per_domain = {d: {"correct": 0, "total": 0} for d in domains}
    per_topic: dict[str, dict] = {}
    rows = []
    correct = 0

    for q in questions:
        ans = responses.get(q["id"])
        is_correct = _GRADERS[q["type"]](q, ans)
        correct += int(is_correct)
        d = q["domain"]
        per_domain[d]["total"] += 1
        per_domain[d]["correct"] += int(is_correct)
        t = per_topic.setdefault(q["study_topic"], {"correct": 0, "total": 0, "domain": d})
        t["total"] += 1
        t["correct"] += int(is_correct)
        rows.append({
            "id": q["id"], "domain": d, "study_topic": q["study_topic"],
            "is_correct": is_correct, "time_ms": int(times_ms.get(q["id"], 0) or 0),
        })

    total = len(questions)
    percent = round(100 * correct / total, 1) if total else 0.0
    pass_prob = round(100 * _pass_probability(percent))

    # ---- domains ranked ----
    dom_scored = [
        {"domain": d, "name": domains[d]["name"],
         "correct": per_domain[d]["correct"], "total": per_domain[d]["total"],
         "percent": round(100 * per_domain[d]["correct"] / per_domain[d]["total"], 1)}
        for d in domains if per_domain[d]["total"]
    ]
    dom_by_score = sorted(dom_scored, key=lambda x: x["percent"])
    weakest_domains = [x for x in dom_by_score if x["percent"] < 100][:3]
    strongest_domains = sorted(dom_scored, key=lambda x: -x["percent"])[:2]

    # ---- weakest subtopics (missed at least once) ----
    weak_topics = sorted(
        ({"topic": name, "domain": info["domain"],
          "domain_name": domains[info["domain"]]["name"],
          "correct": info["correct"], "total": info["total"],
          "percent": round(100 * info["correct"] / info["total"], 1)}
         for name, info in per_topic.items() if info["correct"] < info["total"]),
        key=lambda x: (x["percent"], -x["total"]),
    )[:8]

    behavior = _behavioral_read(rows)
    plan = _study_path(profile, percent, weakest_domains, weak_topics, behavior)

    # Confidence scales with how many questions were asked.
    if total >= 20:
        confidence = "This is a reasonably reliable read for a short test."
    elif total >= 10:
        confidence = "Treat this as a rough indicator — a longer diagnostic (20 questions) gives a firmer estimate."
    else:
        confidence = "Only a few questions were asked, so this is a very rough snapshot. Run a 15–20 question diagnostic for a firmer estimate."

    return {
        "exam_name": profile.name,
        "total": total, "correct": correct, "percent": percent,
        "pass_probability": pass_prob,
        "pass_percent": profile.pass_percent,
        "confidence": confidence,
        "strongest_domains": strongest_domains,
        "weakest_domains": weakest_domains,
        "weak_topics": weak_topics,
        "behavior": behavior,
        "study_path": plan,
        "weak_topic_labels": [t["topic"] for t in weak_topics],
    }


def _behavioral_read(rows):
    """Infer whether misses look like missing knowledge, misreading, or guessing.

    Signals (no perfect ground truth, so this is an estimate):
      * fast-wrong: wrong answers given very quickly => rushing/guessing.
      * clustering: are the misses concentrated in a few topics (=> knowledge
        gaps) or scattered across many (=> misreading / distractor traps)?
      * slow-wrong: wrong answers where real time was spent => engaged but
        tripped up, consistent with misreading the 'best answer' nuance.
    """
    wrong = [r for r in rows if not r["is_correct"]]
    n_wrong = len(wrong)
    result = {"primary": None, "signals": [], "detail": ""}
    if n_wrong == 0:
        result["primary"] = "none"
        result["detail"] = "You didn't miss anything on this diagnostic — no error pattern to diagnose."
        return result

    # timing signals (only meaningful if we captured times)
    timed = [r for r in wrong if r["time_ms"] > 0]
    fast_wrong = [r for r in timed if r["time_ms"] < 15000]     # < 15s on a scenario Q
    slow_wrong = [r for r in timed if r["time_ms"] >= 45000]    # > 45s and still wrong
    fast_frac = (len(fast_wrong) / len(timed)) if timed else 0.0

    # clustering of misses by topic: share taken by the single worst topic
    from collections import Counter
    topic_counts = Counter(r["study_topic"] for r in wrong)
    top_share = (topic_counts.most_common(1)[0][1] / n_wrong) if n_wrong else 0
    distinct_topics = len(topic_counts)
    clustered = distinct_topics <= max(1, n_wrong // 2) and top_share >= 0.4

    if timed and fast_frac >= 0.5:
        result["primary"] = "guessing"
        result["detail"] = (
            f"{len(fast_wrong)} of your {len(timed)} timed misses were answered in under 15 seconds. "
            "That pattern usually means rushing or guessing rather than a knowledge gap. Slow down, "
            "read every option, and eliminate deliberately before choosing.")
        result["signals"].append("Many wrong answers were very fast.")
    elif clustered:
        result["primary"] = "knowledge"
        worst = topic_counts.most_common(1)[0][0]
        result["detail"] = (
            f"Your misses cluster in a small number of topics (heaviest: '{worst}'). "
            "That points to specific knowledge gaps rather than test-taking technique — targeted "
            "study of those topics should move your score the most.")
        result["signals"].append("Misses are concentrated in a few topics.")
    else:
        result["primary"] = "misreading"
        base = ("Your misses are spread across many topics")
        if slow_wrong:
            base += f", and {len(slow_wrong)} were slow answers you still got wrong"
        result["detail"] = (
            base + ". With this bank's deliberately close 'best answer' distractors, that usually "
            "means you're understanding the material but misreading the question or getting pulled "
            "to a plausible-but-not-best option. Watch for qualifiers (BEST, FIRST, NOT, MOST likely) "
            "and re-read the exact ask before answering.")
        result["signals"].append("Misses are scattered across many topics.")

    if slow_wrong and result["primary"] != "misreading":
        result["signals"].append(f"{len(slow_wrong)} slow answers were still wrong.")
    return result


def _study_path(profile, percent, weak_domains, weak_topics, behavior):
    """Produce an ordered, concrete recommended study path."""
    steps = []
    prim = behavior.get("primary")
    if prim == "guessing":
        steps.append("Technique first: on your next sessions, force yourself to read all four options "
                     "and eliminate two before answering — the goal is accuracy, not speed.")
    elif prim == "misreading":
        steps.append("Technique first: practice spotting the qualifier in each stem (BEST / FIRST / NOT / "
                     "MOST likely) and restate what the question is actually asking before you answer.")

    if weak_domains:
        names = ", ".join(f"Domain {d['domain']} ({d['name']})" for d in weak_domains[:2])
        steps.append(f"Study your weakest domains next: {names}. Read the Study Notes for these, then "
                     "run Study Mode filtered to each domain.")
    if weak_topics:
        tnames = ", ".join(f"'{t['topic']}'" for t in weak_topics[:4])
        steps.append(f"Drill your weakest subtopics with Study Mode topic filters: {tnames}.")
    steps.append("Use Flashcards and the Acronym drill for quick daily reinforcement of the terms in "
                 "your weak areas.")
    if percent < profile.pass_percent:
        steps.append("Re-take a diagnostic after a few study sessions to confirm the estimate is moving up, "
                     "then sit a full timed practice exam.")
    else:
        steps.append("You're near or above the bar — sit full timed practice exams to build stamina and "
                     "lock in consistency.")
    return steps
