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
from exam.flashcards_loader import build_flashcard_session, has_deck, load_cards
from exam.grading import grade_exam, grade_one
from exam.flashcards_loader import build_flashcard_session, has_deck, load_cards
from exam.acronyms_loader import (
    build_acronym_session,
    has_deck as acronyms_has_deck,
    load_acronyms,
)
from exam.diagnostic import analyze_diagnostic, build_diagnostic
from exam.models import is_pbq
from exam.notes_loader import load_notes, notes_by_domain
from exam.study import build_attempt_guide
from exam.traps import CATEGORIES, build_traps_session, category_counts, get_category

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


# --------------------------------------------------------------------------- #
# Exam Traps: curated hands-on practice categories with instant feedback and   #
# optional visual aids (ports reference, risk calculator, network-zone diagram)#
# --------------------------------------------------------------------------- #
@app.route("/traps")
@app.route("/traps/<exam_key>")
def traps_setup(exam_key: str | None = None):
    """Pick a hands-on practice category. Traps are Security+ only for now."""
    profile = get_exam("secplus")
    bank = _bank_for(profile)
    counts = category_counts(bank)
    cats = [dict(c, count=counts.get(c["key"], 0)) for c in CATEGORIES]
    return render_template("traps_setup.html", profile=profile, categories=cats)


@app.route("/traps/start", methods=["POST"])
def traps_start():
    profile = get_exam("secplus")
    bank = _bank_for(profile)
    cat = get_category(request.form.get("category", ""))
    if cat is None:
        return redirect(url_for("traps_setup"))
    num = int(request.form.get("num_questions", 15))
    session_qs = build_traps_session(cat, bank, num_questions=num)
    if not session_qs:
        return redirect(url_for("traps_setup"))

    sid = secrets.token_hex(8)
    _EXAMS[sid] = {
        "profile_key": profile.key,
        "questions": session_qs,
        "mode": "traps",
        "category": cat["key"],
    }
    session["traps_id"] = sid
    return redirect(url_for("traps_session"))


@app.route("/traps/session")
def traps_session():
    entry = _EXAMS.get(session.get("traps_id"))
    if not entry:
        return redirect(url_for("traps_setup"))
    profile = get_exam(entry["profile_key"])
    cat = get_category(entry.get("category", ""))
    questions = [
        _public_question(profile, q, i, study_hints=True)
        for i, q in enumerate(entry["questions"])
    ]
    return render_template(
        "traps_session.html",
        questions=questions,
        exam_name=profile.name,
        category=cat,
    )


@app.route("/traps/grade", methods=["POST"])
def traps_grade():
    """Grade ONE question for immediate Exam-Traps feedback."""
    entry = _EXAMS.get(session.get("traps_id"))
    if not entry:
        return jsonify({"error": "no active traps session"}), 400
    data = request.get_json(force=True)
    qid = data.get("id")
    answer = data.get("answer")
    question = next((q for q in entry["questions"] if q["id"] == qid), None)
    if question is None:
        return jsonify({"error": "unknown question"}), 400
    return jsonify(grade_one(question, answer))


# --------------------------------------------------------------------------- #
# Flashcards: definition -> term, in multiple-choice or open-ended mode        #
# --------------------------------------------------------------------------- #
@app.route("/flashcards")
@app.route("/flashcards/<exam_key>")
def flashcards_setup(exam_key: str | None = None):
    profile = get_exam(exam_key)
    exams = [e for e in EXAMS.values() if has_deck(e.key)]
    return render_template(
        "flashcards_setup.html",
        profile=profile,
        exams=exams,
        has_deck=has_deck(profile.key),
        deck_size=len(load_cards(profile.key)),
    )


@app.route("/flashcards/start", methods=["POST"])
def flashcards_start():
    profile = get_exam(request.form.get("exam"))
    mode = request.form.get("mode", "multiple_choice")
    if mode not in ("multiple_choice", "open_ended"):
        mode = "multiple_choice"
    num = int(request.form.get("num_cards", 15))
    session_cards = build_flashcard_session(profile.key, mode=mode, num_cards=num)
    if not session_cards:
        return redirect(url_for("flashcards_setup", exam_key=profile.key))
    return render_template(
        "flashcards.html",
        cards=session_cards,
        mode=mode,
        exam_name=profile.name,
    )


@app.route("/acronyms")
@app.route("/acronyms/<exam_key>")
def acronyms_setup(exam_key: str | None = None):
    profile = get_exam(exam_key)
    exams = [e for e in EXAMS.values() if acronyms_has_deck(e.key)]
    return render_template(
        "acronyms_setup.html",
        profile=profile,
        exams=exams,
        has_deck=acronyms_has_deck(profile.key),
        deck_size=len(load_acronyms(profile.key)),
    )


@app.route("/acronyms/start", methods=["POST"])
def acronyms_start():
    profile = get_exam(request.form.get("exam"))
    mode = request.form.get("mode", "multiple_choice")
    if mode not in ("multiple_choice", "typed"):
        mode = "multiple_choice"
    num = int(request.form.get("num_cards", 15))
    cards = build_acronym_session(profile.key, mode=mode, num_cards=num)
    if not cards:
        return redirect(url_for("acronyms_setup", exam_key=profile.key))
    return render_template(
        "acronyms.html", cards=cards, mode=mode, exam_name=profile.name
    )


# --------------------------------------------------------------------------- #
# Diagnostic test: short assessment + pass-readiness / behaviour analysis      #
# --------------------------------------------------------------------------- #
@app.route("/diagnostic")
@app.route("/diagnostic/<exam_key>")
def diagnostic_setup(exam_key: str | None = None):
    profile = get_exam(exam_key)
    return render_template("diagnostic_setup.html", profile=profile, exams=list(EXAMS.values()))


@app.route("/diagnostic/start", methods=["POST"])
def diagnostic_start():
    profile = get_exam(request.form.get("exam"))
    bank = _bank_for(profile)
    num = int(request.form.get("num_questions", 15))
    quiz = build_diagnostic(profile, bank, num)
    diag_id = secrets.token_hex(8)
    _EXAMS[diag_id] = {"profile_key": profile.key, "questions": quiz, "mode": "diagnostic"}
    session["diag_id"] = diag_id
    questions = [_public_question(profile, q, i) for i, q in enumerate(quiz)]
    return render_template("diagnostic.html", questions=questions, exam_name=profile.name)


@app.route("/diagnostic/submit", methods=["POST"])
def diagnostic_submit():
    entry = _EXAMS.get(session.get("diag_id"))
    if not entry:
        return jsonify({"error": "no active diagnostic"}), 400
    profile = get_exam(entry["profile_key"])
    data = request.get_json(force=True)
    responses = data.get("responses", {})
    times = data.get("times", {})
    report = analyze_diagnostic(profile, entry["questions"], responses, times)
    report_id = secrets.token_hex(8)
    report["profile_key"] = profile.key
    _REPORTS[report_id] = report
    session["diag_report_id"] = report_id
    _EXAMS.pop(session.get("diag_id"), None)
    session.pop("diag_id", None)
    return jsonify({"redirect": url_for("diagnostic_results")})


@app.route("/diagnostic/results")
def diagnostic_results():
    report = _REPORTS.get(session.get("diag_report_id"))
    if not report:
        return redirect(url_for("diagnostic_setup"))
    return render_template("diagnostic_results.html", r=report)


@app.route("/diagnostic/study-weak", methods=["POST"])
def diagnostic_study_weak():
    """Start a Study-Mode session focused on the diagnostic's weak topics."""
    report = _REPORTS.get(session.get("diag_report_id"))
    if not report:
        return redirect(url_for("diagnostic_setup"))
    profile = get_exam(report.get("profile_key"))
    weak = report.get("weak_topic_labels", [])
    if not weak:
        return redirect(url_for("diagnostic_results"))
    bank = _bank_for(profile)
    quiz = build_study_session(profile, bank, topics=weak, num_questions=20)
    sid = secrets.token_hex(8)
    _EXAMS[sid] = {"profile_key": profile.key, "questions": quiz, "mode": "study"}
    session["study_id"] = sid
    return redirect(url_for("study_session"))


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
