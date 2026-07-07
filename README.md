# CompTIA Practice Exam Generator

A web app that generates full-length CompTIA practice exams written to be **as hard or harder than
the live exam** — scenario-based "best answer" questions where you can't reverse-engineer the answer
just by reading the options, plus interactive **performance-based questions (PBQs)**.

**Three exams are included** (pick one on the home page):

- **CompTIA Security+ (SY0-701)** — 5 domains, pass line ≈ 83%
- **CompTIA A+ Core 1 (220-1201)** — 5 domains, pass line ≈ 75%
- **Cisco CCNA (200-301)** — 6 domains, 120-minute timer, pass line ≈ 82%

Every time you start an exam you get a **different mix of questions**, so you can keep retesting.
After grading, the app explains **every question you missed** — including **why each wrong option
is wrong** — and builds a **personalised study plan** that ranks your weakest domains and topics.

## Features

- **Weighted, exam-accurate composition** — questions are sampled to match each exam's official
  domain percentages (Security+ 12/22/18/28/20; A+ Core 1 13/23/25/11/28).
- **Performance-based questions** — matching, categorisation, and ordering PBQs, just like the real exam.
- **Fresh exams every time** — the app tracks which questions you've already seen and pulls new ones
  until the bank is exhausted. (Reset that history any time from the home page.)
- **90-minute countdown timer**, like the real exam.
- **Deep explanations** — for every question, the correct answer *and* a specific rationale for why
  each distractor is wrong, plus an overall teaching explanation.
- **Study plan** — score by domain, weakest topics ranked worst-first, and concrete advice on what
  to study next.
- **Optional AI mode** — with an Anthropic API key, generate *unlimited* brand-new questions.

## Quick start

```bash
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```

Pick the number of questions and PBQs, then start. Submit any time (or let the timer run out) to see
your score, explanations, and study plan. Click **Generate another exam** for a fresh set.

## Optional: unlimited AI-generated questions

The offline bank ships with 200+ hand-written questions and works with zero setup. To generate
brand-new questions on demand:

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python app.py
```

A new **"Generate brand-new questions with AI"** checkbox appears on the home page. Each AI exam is
freshly written and validated against the same schema. (Costs a few cents per exam; falls back to
the offline bank automatically if the API is unavailable.)

## How it's organised

```
app.py                       Flask web app (routes, session, serving)
requirements.txt
exam/
  models.py                  Question schema + validation (single source of truth)
  bank.py                    Loads & validates the offline question bank
  generator.py               Weighted exam assembly, answer shuffling, "seen" tracking
  grading.py                 Scoring, per-option explanations, study-plan builder
  ai_generator.py            Optional Claude API question generation
  catalog.py                 Exam profiles (domains, weights, pass mark, AI prompt)
  questions/
    secplus/                 Security+ SY0-701 bank (one module per domain + PBQs)
    aplus_core1/             A+ Core 1 220-1201 bank (one module per domain + PBQs)
    ccna_200_301/            Cisco CCNA 200-301 bank (one module per domain + PBQs)
templates/                   index / exam / results pages
static/                      style.css, exam.js
data/seen_<exam>.json        Tracks seen questions per exam (auto-created, gitignored)
```

## Adding your own questions

Drop a new `QUESTIONS = [...]` list into any module under `exam/questions/` (or add to an existing
one). Each question is a dict following the schema documented at the top of `exam/models.py`. The
loader validates every question on startup and skips malformed ones, so a typo can't crash the app.

## Scoring note

The real SY0-701 is scored on a 100–900 scale with a 750 pass mark. This app reports raw percentage,
an approximate scaled score, and pass/fail against the equivalent (~83%). Treat the scaled number as
an estimate for self-assessment, not an official prediction.

## Disclaimer

These are original practice questions for study purposes and are **not** real exam items. CompTIA and
Security+ are trademarks of CompTIA, Inc.; this project is not affiliated with or endorsed by CompTIA.
