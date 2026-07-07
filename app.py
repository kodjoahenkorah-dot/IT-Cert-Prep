"""Multi-exam CompTIA practice exam — Flask web app.

Supports CompTIA Security+ (SY0-701) and A+ Core 1 (220-1201). Pick an exam on
the home page; each gets weighted assembly, per-option explanations, a study
plan, fresh-question tracking, and an optional AI mode.

Run:
    pip install -r requirements.txt
    python app.py
    # open http://127.0.0.1:5000

Optional AI mode (unlimited brand-new questions):
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic
"""

from __future__ import annotations

import secrets

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from exam.ai_generator import ai_available, generate_questions
from exam.bank import bank_stats, load_bank
from exam.catalog import EXAMS, get_exam
from exam.generator import (
    _weighted_domain_counts,
    build_adaptive_quiz,
    build_exam,
    build_study_session,
    reset_seen,
    topics_by_domain,
)
from exam.grading import grade_exam, grade_one
from exam.models import is_pbq
from exam.notes_loader import load_notes, notes_by_domain
from exam.study import build_attempt_guide

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Exams and graded reports in flight, kept server-side (the answer key never
# reaches the browser before grading, and reports are too big for a cookie).
_EXAMS: dict[str, dict] = {}      # exam_id -> {"profile_key":..., "questions":[...]}
_REPORTS: dict[str, dict] = {}    # report_id -> report payload


def _bank_for(profile) -> list[dict]:
    return load_bank(profile.questions_package)


def _public_question(profile, q: dict, index: int, study_hints: bool = False) -> dict:
    """Strip the answer key out of a question for the browser.

    With ``study_hints=True`` (Study Mode only), include the number of correct
    options for multiple_response questions so the client can auto-grade the
    moment the required number of selections is made.
    """
    pub = {
        "id": q["id"],
        "index": index,
        "number": index + 1,
        "type": q["type"],
        "domain": q["domain"],
        "domain_name": profile.domains[q["domain"]]["name"],
        "objective": q["objective"],
        "is_pbq": is_pbq(q),
        "stem": q.get("stem", ""),
    }
    if q["type"] in ("multiple_choice", "multiple_response"):
        pub["options"] = [{"id": o["id"], "text": o["text"]} for o in q["options"]]
        pub["multi"] = q["type"] == "multiple_response"
        if study_hints and pub["multi"]:
            pub["n_correct"] = sum(1 for o in q["options"] if o.get("correct"))
    elif q["type"] == "pbq_matching":
        pub["prompts"] = q["prompts"]
        pub["targets"] = q["targets"]
    elif q["type"] == "pbq_ordering":
        pub["items"] = q["items"]
    elif q["type"] == "pbq_categorize":
        pub["categories"] = q["categories"]
        pub["items"] = q["items"]
    return pub


@app.route("/")
def index():
    cards = []
    for profile in EXAMS.values():
        stats = bank_stats(_bank_for(profile))
        cards.append({"profile": profile, "stats": stats})
    return render_template("index.html", cards=cards, ai_on=ai_available())


@app.route("/start", methods=["POST"])
def start():
    profile = get_exam(request.form.get("exam"))
    bank = _bank_for(profile)
    num_questions = int(request.form.get("num_questions", profile.default_num_questions))
    num_pbqs = int(request.form.get("num_pbqs", profile.default_pbqs))
    use_ai = request.form.get("use_ai") == "on" and ai_available()

    if use_ai:
        num_mc = max(0, num_questions - num_pbqs)
        counts = _weighted_domain_counts(profile.domains, num_mc)
        try:
            exam = generate_questions(profile, counts, num_pbqs=num_pbqs)
            import random

            random.shuffle(exam)
        except Exception as exc:  # fall back to offline bank on any AI failure
            app.logger.warning("AI generation failed (%s); using offline bank", exc)
            exam = build_exam(profile, bank, num_questions, num_pbqs)
    else:
        exam = build_exam(profile, bank, num_questions, num_pbqs)

    exam_id = secrets.token_hex(8)
    _EXAMS[exam_id] = {"profile_key": profile.key, "questions": exam}
    session["exam_id"] = exam_id
    return redirect(url_for("take"))


@app.route("/exam")
def take():
    entry = _EXAMS.get(session.get("exam_id"))
    if not entry:
        return redirect(url_for("index"))
    profile = get_exam(entry["profile_key"])
    questions = [_public_question(profile, q, i) for i, q in enumerate(entry["questions"])]
    return render_template(
        "exam.html",
        questions=questions,
        exam_name=profile.name,
        time_limit_min=profile.time_limit_min,
    )


# --------------------------------------------------------------------------- #
# Study Mode: untimed, immediate per-question feedback, topic-by-topic drills  #
# --------------------------------------------------------------------------- #
@app.route("/study")
@app.route("/study/<exam_key>")
def study_setup(exam_key: str | None = None):
    """Pick an exam, a domain, and (optionally) specific topics to drill."""
    profile = get_exam(exam_key)
    bank = _bank_for(profile)
    return render_template(
        "study_setup.html",
        profile=profile,
        exams=list(EXAMS.values()),
        topics_by_domain=topics_by_domain(bank),
        domains=profile.domains,
    )


@app.route("/study/start", methods=["POST"])
def study_start():
    profile = get_exam(request.form.get("exam"))
    bank = _bank_for(profile)
    domain = request.form.get("domain")
    domain = int(domain) if domain and domain != "all" else None
    topics = request.form.getlist("topics") or None
    num = int(request.form.get("num_questions", 20))

    session_qs = build_study_session(
        profile, bank, domain=domain, topics=topics, num_questions=num
    )
    if not session_qs:
        return redirect(url_for("study_setup", exam_key=profile.key))

    sid = secrets.token_hex(8)
    _EXAMS[sid] = {"profile_key": profile.key, "questions": session_qs, "mode": "study"}
    session["study_id"] = sid
    return redirect(url_for("study_session"))


@app.route("/study/session")
def study_session():
    entry = _EXAMS.get(session.get("study_id"))
    if not entry:
        return redirect(url_for("study_setup"))
    profile = get_exam(entry["profile_key"])
    questions = [
        _public_question(profile, q, i, study_hints=True)
        for i, q in enumerate(entry["questions"])
    ]
    return render_template(
        "study_session.html", questions=questions, exam_name=profile.name
    )


@app.route("/study/grade", methods=["POST"])
def study_grade():
    """Grade ONE question for immediate Study-Mode feedback."""
    entry = _EXAMS.get(session.get("study_id"))
    if not entry:
        return jsonify({"error": "no active study session"}), 400
    data = request.get_json(force=True)
    qid = data.get("id")
    answer = data.get("answer")
    question = next((q for q in entry["questions"] if q["id"] == qid), None)
    if question is None:
        return jsonify({"error": "unknown question"}), 400
    return jsonify(grade_one(question, answer))


@app.route("/submit", methods=["POST"])
def submit():
    exam_id = session.get("exam_id")
    entry = _EXAMS.get(exam_id)
    if not entry:
        return jsonify({"error": "no active exam"}), 400
    profile = get_exam(entry["profile_key"])
    responses = request.get_json(force=True).get("responses", {})
    report = grade_exam(profile, entry["questions"], responses)

    report_id = secrets.token_hex(8)
    # Keep the exam this report belongs to, so the per-attempt guide and the
    # weakness-focused quiz know which profile/bank to use.
    report["profile_key"] = profile.key
    _REPORTS[report_id] = report
    session["report_id"] = report_id
    _EXAMS.pop(exam_id, None)
    session.pop("exam_id", None)
    return jsonify({"redirect": url_for("results")})


@app.route("/results")
def results():
    report = _REPORTS.get(session.get("report_id"))
    if not report:
        return redirect(url_for("index"))
    return render_template("results.html", report=report)


@app.route("/attempt-guide")
def attempt_guide():
    """Per-attempt study guide: notes + focused plan for the last attempt."""
    report = _REPORTS.get(session.get("report_id"))
    if not report:
        return redirect(url_for("index"))
    profile = get_exam(report.get("profile_key"))
    guide = build_attempt_guide(profile, report)
    return render_template("attempt_guide.html", guide=guide)


@app.route("/study-weak", methods=["POST"])
def study_weak():
    """Build and start a quiz focused on the last attempt's weak topics."""
    report = _REPORTS.get(session.get("report_id"))
    if not report:
        return redirect(url_for("index"))
    profile = get_exam(report.get("profile_key"))
    weak_labels = report["study_plan"].get("weak_topic_labels", [])
    if not weak_labels:
        return redirect(url_for("results"))
    bank = _bank_for(profile)
    num = int(request.form.get("num_questions", 20))
    quiz = build_adaptive_quiz(profile, bank, weak_labels, num_questions=num)

    exam_id = secrets.token_hex(8)
    _EXAMS[exam_id] = {"profile_key": profile.key, "questions": quiz}
    session["exam_id"] = exam_id
    return redirect(url_for("take"))


@app.route("/notes")
@app.route("/notes/<exam_key>")
def notes(exam_key: str | None = None):
    """Browse the study notes for an exam, organised by domain."""
    profile = get_exam(exam_key)
    grouped = notes_by_domain(profile)
    total = len(load_notes(profile))
    return render_template(
        "notes.html",
        profile=profile,
        grouped=grouped,
        total=total,
        exams=list(EXAMS.values()),
    )


@app.route("/fresh-start", methods=["POST"])
def fresh_start():
    """Forget the seen-question history for one exam so its bank is reusable."""
    profile = get_exam(request.form.get("exam"))
    reset_seen(profile.key)
    return redirect(url_for("index"))


if __name__ == "__main__":
    for profile in EXAMS.values():
        s = bank_stats(_bank_for(profile))
        print(f"[exams] {profile.name}: {s['total']} questions {s['by_domain']}")
    print(f"[exams] AI mode: {'ON' if ai_available() else 'off (offline bank only)'}")
    app.run(debug=True, port=5000)
