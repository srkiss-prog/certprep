# CBP Preparation Workspace

This repository is a structured workspace for preparing the **Certified Bitcoin Professional (CBP)** exam.

The focus is **speed-based recognition under time pressure** (~16 seconds per question), aligned with the official CBP study guide.  
The workflow favors *active recall, trap awareness, and semantic precision* over passive reading.

No score tracking is implemented initially by design.

---

## Exam Constraints (Design Assumptions)

- 75 questions total
- Mix of True/False and Multiple Choice
- 20 minutes total (~16 seconds per question)
- One-pass thinking (no revisiting questions)
- No partial credit

All practice material and structure in this repo is optimized for these constraints.

---

## Repository Structure

```
cbp-prep/
  README.md
  codex/
    commands/              # Canonical prompt commands
    templates/             # Optional prompt/output templates
  knowledge/
    glossary.md            # Global Bitcoin / CBP terminology
    fast-fail-patterns.md  # Global recurring mistake patterns
    domains/
      01-history-of-money/
      02-digital-economy/
      03-cryptography-basics/
      04-bitcoin-basics/
      05-consensus-mining-bips/
      06-wallets-key-management/
      07-bitcoin-commerce/
  practice/
    queue.md               # What to generate next
    sessions/              # Legacy markdown session exports (optional)
  data/
    questions.db           # Primary question bank (SQLite)
  scripts/
    quiz_cli.py            # Practice/exam CLI from SQLite
  sources/
    cbp-study-guide.pdf
```

---

## Core Concepts

### Knowledge vs Practice (Separation of Concerns)

- **knowledge/**  
  Persistent, curated material:
  - Mini recaps
  - Key terms
  - Common fast-fail patterns  
  This evolves slowly and is refined over time.

- **practice + data/**  
  SQLite-first drill storage:
  - Fresh questions are inserted into `data/questions.db`
  - Existing markdown session files are optional/legacy exports
  - Repetition and variation are generated from the DB

---

## Topic-Level Workflow

Each CBP subtopic is represented in SQLite and can still have domain notes:

```
knowledge/domains/03-cryptography-basics/hash-functions/
  topic.md        # Canonical summary for this subtopic

data/questions.db
  subtopics
  questions
  question_options
```

### `topic.md` contains:
- The exact CBP study guide bullet
- A refined mini recap
- Curated key terms
- Known fast-fail patterns

### `data/questions.db` contains:
- Generated TF/MCQ question bank
- Justifications for review
- MCQ options with correctness flags
- Source for practice/exam sessions in `scripts/quiz_cli.py`

---

## Primary Practice Command

The main prompt used to generate drills is:

**`speed_recognition_v1`**

This command:
- Mixes True/False and Multiple Choice
- Enforces fast-recognition design
- Injects realistic CBP-style traps
- Avoids math-heavy or obscure trivia

Canonical versions of all commands live in:

```
codex/commands/
```

Only commands in this folder should be reused verbatim.

---

## Practice Queue

The file:

```
practice/queue.md
```

acts as the single source of truth for:
- What to study next
- What has already been covered
- What to revisit later

Think of it as a lightweight Kanban board.

---

## Initial Usage Pattern

1. Pick one CBP bullet from the study guide
2. Create the topic folder (if it doesn’t exist)
3. Run `speed_recognition_v1`
4. Insert generated questions directly into `data/questions.db`
5. Optionally refine `topic.md` with insights

No analytics, no scoring, no dashboards — just reps.

---

## Quick Start

```bash
# 1) Generate and ingest new questions
# Use: codex/commands/speed_recognition_v1.md

# 2) Launch interactive practice mode
scripts/.venv/bin/python scripts/quiz_cli.py --mode practice

# 3) Launch full exam mode (75 questions, 20 min)
scripts/.venv/bin/python scripts/quiz_cli.py --mode exam
```

---

## Design Philosophy

- Precision beats breadth
- Recognition beats reasoning
- Traps are more valuable than facts
- If you need to reread the question, it’s already too slow

---

## Future Extensions (Not Implemented Yet)

- Quick drills (5-question bursts)
- Difficulty flags
- Miss / hesitation tracking
- Tag-based weak-area heatmaps

These are intentionally deferred.

---

## Status

This repo is a **working prep environment**, not a static knowledge base.
Expect frequent small additions and refinements.
