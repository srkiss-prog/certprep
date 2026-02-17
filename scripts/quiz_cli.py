#!/usr/bin/env python3
"""Interactive practice/exam CLI backed by data/questions.db."""

from __future__ import annotations

import argparse
import math
import random
import signal
import sqlite3
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path


class InputTimeout(Exception):
    pass


class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"


@dataclass
class Question:
    id: int
    subtopic: str
    q_number: int
    q_type: str
    prompt: str
    correct_tf: int | None
    justification: str | None


@dataclass
class AnswerResult:
    question_id: int
    subtopic: str
    is_correct: bool
    elapsed_seconds: float


@dataclass
class PracticeSelection:
    question_count: int
    q_start: int | None
    q_end: int | None


def colors_enabled() -> bool:
    return sys.stdout.isatty() and "NO_COLOR" not in __import__("os").environ


USE_COLOR = colors_enabled()


def paint(text: str, *styles: str) -> str:
    if not USE_COLOR or not styles:
        return text
    return "".join(styles) + text + C.RESET


def hr(char: str = "=", width: int = 72) -> str:
    return char * width


def panel(title: str) -> None:
    print()
    print(paint(hr("=", 72), C.GRAY))
    print(paint(f"  {title}", C.BOLD, C.CYAN))
    print(paint(hr("=", 72), C.GRAY))


def splash() -> None:
    print()
    print(paint("  ____ ____  ____    ____        _      ____  _   _ ___ _____ ", C.CYAN, C.BOLD))
    print(paint(" / ___| __ )|  _ \\  |  _ \\ _   _(_)____/ ___|| | | |_ _|_   _|", C.CYAN, C.BOLD))
    print(paint("| |   |  _ \\| |_) | | |_) | | | | |_  /\\___ \\| | | || |  | |  ", C.CYAN, C.BOLD))
    print(paint("| |___| |_) |  __/  |  __/| |_| | |/ /  ___) | |_| || |  | |  ", C.CYAN, C.BOLD))
    print(paint(" \\____|____/|_|     |_|    \\__,_|_/___||____/ \\___/|___| |_|  ", C.CYAN, C.BOLD))
    print(paint("                      Command Line Trainer", C.DIM))


def timeout_handler(_signum: int, _frame: object) -> None:
    raise InputTimeout


def input_with_timeout(prompt: str, timeout_seconds: float | None) -> str:
    if timeout_seconds is None:
        return input(prompt)
    if timeout_seconds <= 0:
        raise InputTimeout

    has_sigalrm = hasattr(signal, "SIGALRM") and hasattr(signal, "setitimer")
    if not has_sigalrm:
        return input(prompt)

    previous_handler = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout_seconds)
    try:
        return input(prompt)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


def fmt_seconds(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    minutes, secs = divmod(total, 60)
    return f"{minutes:02d}:{secs:02d}"


class CountdownTicker:
    """Simple live countdown renderer for exam mode while waiting for input."""

    def __init__(self, deadline: float) -> None:
        self.deadline = deadline
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._last_remaining: int | None = None

    def start(self) -> None:
        if not sys.stdout.isatty():
            return
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self) -> None:
        while not self._stop.is_set():
            remaining = max(0, int(self.deadline - time.monotonic()))
            if remaining != self._last_remaining:
                self._last_remaining = remaining
                msg = paint(f"Live timer: {fmt_seconds(remaining)}", C.YELLOW, C.BOLD)
                # Save cursor, draw timer on the first terminal row, then restore.
                sys.stdout.write("\033[s\033[1;1H\033[2K" + msg + "\033[u")
                sys.stdout.flush()
            if remaining <= 0:
                break
            self._stop.wait(0.2)

    def stop(self) -> None:
        if self._thread is None:
            return
        self._stop.set()
        self._thread.join(timeout=1.0)
        # Clear the pinned timer line when question input ends.
        sys.stdout.write("\033[s\033[1;1H\033[2K\033[u")
        sys.stdout.flush()


def progress_bar(current: int, total: int, width: int = 30) -> str:
    if total <= 0:
        return "[" + ("-" * width) + "]"
    filled = int((current / total) * width)
    return "[" + ("#" * filled) + ("-" * (width - filled)) + "]"


def connect_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def list_subtopics(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return list(
        conn.execute(
            """
            SELECT s.id, s.name, COUNT(q.id) AS question_count
            FROM subtopics s
            LEFT JOIN questions q ON q.subtopic_id = s.id
            GROUP BY s.id, s.name
            ORDER BY s.name
            """
        )
    )


def count_questions_in_scope(
    conn: sqlite3.Connection,
    *,
    subtopic_id: int,
    q_start: int | None,
    q_end: int | None,
) -> int:
    sql = "SELECT COUNT(*) FROM questions WHERE subtopic_id = ?"
    params: list[int] = [subtopic_id]
    if q_start is not None:
        sql += " AND q_number >= ?"
        params.append(q_start)
    if q_end is not None:
        sql += " AND q_number <= ?"
        params.append(q_end)
    row = conn.execute(sql, tuple(params)).fetchone()
    return int(row[0]) if row else 0


def fetch_questions(
    conn: sqlite3.Connection,
    *,
    mode: str,
    question_count: int,
    subtopic_id: int | None = None,
    q_start: int | None = None,
    q_end: int | None = None,
) -> list[Question]:
    base_select = """
        SELECT q.id, s.name AS subtopic, q.q_number, q.q_type, q.prompt, q.correct_tf, q.justification
        FROM questions q
        JOIN subtopics s ON s.id = q.subtopic_id
    """

    if mode == "practice":
        if subtopic_id is None:
            raise ValueError("subtopic_id is required in practice mode")

        where_clauses = ["s.id = ?"]
        params: list[int] = [subtopic_id]
        if q_start is not None:
            where_clauses.append("q.q_number >= ?")
            params.append(q_start)
        if q_end is not None:
            where_clauses.append("q.q_number <= ?")
            params.append(q_end)

        sql = base_select + " WHERE " + " AND ".join(where_clauses) + " ORDER BY RANDOM() LIMIT ?"
        params.append(question_count)
        rows = conn.execute(sql, tuple(params)).fetchall()
    else:
        rows = conn.execute(base_select + " ORDER BY RANDOM() LIMIT ?", (question_count,)).fetchall()

    return [
        Question(
            id=row["id"],
            subtopic=row["subtopic"],
            q_number=row["q_number"],
            q_type=row["q_type"],
            prompt=row["prompt"],
            correct_tf=row["correct_tf"],
            justification=row["justification"],
        )
        for row in rows
    ]


def fetch_options(conn: sqlite3.Connection, question_id: int) -> list[tuple[str, int]]:
    rows = conn.execute(
        "SELECT option_text, is_correct FROM question_options WHERE question_id = ?",
        (question_id,),
    ).fetchall()
    return [(row["option_text"], row["is_correct"]) for row in rows]


def choose_mode(args_mode: str | None) -> str:
    if args_mode in {"practice", "exam"}:
        return args_mode

    panel("Select Mode")
    print("  1) Practice")
    print("  2) Exam")
    while True:
        choice = input("\n  Enter choice [1-2]: ").strip()
        if choice == "1":
            return "practice"
        if choice == "2":
            return "exam"
        print(paint("  Invalid choice.", C.YELLOW))


def choose_subtopic(conn: sqlite3.Connection, requested_name: str | None) -> sqlite3.Row:
    subtopics = list_subtopics(conn)
    if not subtopics:
        raise SystemExit("No subtopics found. Run migration first.")

    if requested_name:
        for subtopic in subtopics:
            if subtopic["name"].lower() == requested_name.lower():
                return subtopic
        available = ", ".join(s["name"] for s in subtopics)
        raise SystemExit(f"Subtopic '{requested_name}' not found. Available: {available}")

    panel("Select Subtopic")
    for idx, row in enumerate(subtopics, start=1):
        print(f"  {idx:>2}) {row['name']} {paint(f'({row['question_count']} questions)', C.DIM)}")

    while True:
        raw = input(f"\n  Enter choice [1-{len(subtopics)}]: ").strip()
        if raw.isdigit():
            index = int(raw)
            if 1 <= index <= len(subtopics):
                return subtopics[index - 1]
        print(paint("  Invalid choice.", C.YELLOW))


def choose_integer(prompt: str, *, default: int, minimum: int, maximum: int | None = None) -> int:
    while True:
        limit_hint = f"{minimum}+" if maximum is None else f"{minimum}-{maximum}"
        raw = input(f"{prompt} [{default}, {limit_hint}]: ").strip()
        if not raw:
            return default
        if raw.isdigit():
            value = int(raw)
            if value >= minimum and (maximum is None or value <= maximum):
                return value
        print(paint("  Invalid number.", C.YELLOW))


def resolve_range(
    *,
    min_q: int,
    max_q: int,
    requested_start: int | None,
    requested_end: int | None,
) -> tuple[int | None, int | None]:
    if requested_start is None and requested_end is None:
        return None, None

    q_start = requested_start if requested_start is not None else min_q
    q_end = requested_end if requested_end is not None else max_q

    if q_start > q_end:
        raise SystemExit("Question range is invalid: start must be <= end.")
    if q_start < min_q or q_end > max_q:
        raise SystemExit(
            f"Question range must stay inside available subtopic bounds Q{min_q}..Q{max_q}."
        )

    return q_start, q_end


def choose_practice_selection(
    conn: sqlite3.Connection,
    *,
    subtopic: sqlite3.Row,
    requested_count: int | None,
    requested_q_start: int | None,
    requested_q_end: int | None,
) -> PracticeSelection:
    min_row = conn.execute(
        "SELECT MIN(q_number) AS min_q, MAX(q_number) AS max_q FROM questions WHERE subtopic_id = ?",
        (subtopic["id"],),
    ).fetchone()
    if min_row is None or min_row["min_q"] is None or min_row["max_q"] is None:
        raise SystemExit(f"Subtopic '{subtopic['name']}' has no questions.")

    min_q = int(min_row["min_q"])
    max_q = int(min_row["max_q"])

    q_start, q_end = resolve_range(
        min_q=min_q,
        max_q=max_q,
        requested_start=requested_q_start,
        requested_end=requested_q_end,
    )

    needs_prompt = requested_count is None and requested_q_start is None and requested_q_end is None
    if needs_prompt:
        panel("Practice Question Scope")
        print(f"  Subtopic: {paint(subtopic['name'], C.CYAN)}")
        print(f"  Available q_number span: Q{min_q} to Q{max_q}")
        print("  1) Random questions")
        print("  2) Question number range")

        while True:
            mode_choice = input("\n  Enter choice [1-2] (default 1): ").strip()
            if mode_choice in {"", "1", "2"}:
                break
            print(paint("  Invalid choice.", C.YELLOW))

        if mode_choice == "2":
            q_start = choose_integer("  Start at question number", default=min_q, minimum=min_q, maximum=max_q)
            q_end = choose_integer("  End at question number", default=max_q, minimum=q_start, maximum=max_q)

    available = count_questions_in_scope(conn, subtopic_id=subtopic["id"], q_start=q_start, q_end=q_end)
    if available == 0:
        if q_start is not None and q_end is not None:
            raise SystemExit(f"No questions found in '{subtopic['name']}' for range Q{q_start}..Q{q_end}.")
        raise SystemExit(f"No questions found in '{subtopic['name']}'.")

    if requested_count is not None:
        if requested_count <= 0:
            raise SystemExit("Question count must be greater than 0.")
        question_count = requested_count
    else:
        default_count = min(25, available)
        if needs_prompt:
            question_count = choose_integer(
                "\n  How many questions",
                default=default_count,
                minimum=1,
                maximum=available,
            )
        else:
            question_count = default_count

    return PracticeSelection(question_count=question_count, q_start=q_start, q_end=q_end)


def ask_tf(question: Question, timeout_seconds: float | None) -> bool:
    while True:
        raw = input_with_timeout(paint("\n  Your answer [T/F]: ", C.BOLD), timeout_seconds).strip().lower()
        if raw in {"t", "true"}:
            return question.correct_tf == 1
        if raw in {"f", "false"}:
            return question.correct_tf == 0
        print(paint("  Please answer with T or F.", C.YELLOW))


def ask_mcq(
    conn: sqlite3.Connection,
    question: Question,
    timeout_seconds: float | None,
) -> tuple[bool, str]:
    options = fetch_options(conn, question.id)
    if not options:
        raise SystemExit(f"Question {question.id} has no options.")

    random.shuffle(options)
    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(options) > len(labels):
        raise SystemExit(f"Question {question.id} has too many options.")

    labeled: list[tuple[str, str, int]] = []
    for idx, (text, is_correct) in enumerate(options):
        labeled.append((labels[idx], text, is_correct))

    print()
    for label, text, _ in labeled:
        print(f"  {paint(label + ')', C.BOLD, C.BLUE)} {paint(text, C.BOLD)}")

    while True:
        raw = input_with_timeout(paint("\n  Your answer: ", C.BOLD), timeout_seconds).strip().upper()
        if not raw:
            print(paint("  Please enter an option letter.", C.YELLOW))
            continue
        letter = raw[0]
        for label, text, is_correct in labeled:
            if letter == label:
                correct_text = next(t for _, t, c in labeled if c == 1)
                return is_correct == 1, correct_text
        print(paint("  Invalid option.", C.YELLOW))


def run_session(
    conn: sqlite3.Connection,
    *,
    mode: str,
    questions: list[Question],
    justification_mode: str,
    timer_minutes: int,
) -> None:
    total_questions = len(questions)
    if total_questions == 0:
        raise SystemExit("No questions found for the selected configuration.")

    panel("Session Start")
    if mode == "practice":
        print(f"  Mode: {paint('Practice', C.GREEN, C.BOLD)}")
        print(f"  Questions: {total_questions}")
        print(f"  Justification mode: {justification_mode}")
    else:
        print(f"  Mode: {paint('Exam', C.CYAN, C.BOLD)}")
        print(f"  Questions: {total_questions}")
        print(f"  Timer: {timer_minutes} minutes")

    exam_seconds = timer_minutes * 60
    exam_started_at = time.monotonic()
    deadline = exam_started_at + exam_seconds if mode == "exam" else None

    results: list[AnswerResult] = []
    result_by_qid: dict[int, bool] = {}

    for idx, question in enumerate(questions, start=1):
        now = time.monotonic()
        if deadline is not None and now >= deadline:
            print("\n" + paint("Time is up. Auto-submitting exam.", C.RED, C.BOLD))
            break

        print()
        print(paint(hr("-", 72), C.GRAY))
        print(
            f"  {paint(progress_bar(idx - 1, total_questions), C.BLUE)} "
            f"{paint(f'Question {idx}/{total_questions}', C.BOLD)}"
        )
        print(f"  Subtopic: {paint(question.subtopic, C.CYAN)}")
        print()
        print(paint("  QUESTION", C.BOLD, C.CYAN))
        print(paint(f"  {question.prompt}", C.BOLD))

        started = time.monotonic()
        ticker: CountdownTicker | None = None
        timed_out = False
        try:
            if deadline is not None:
                ticker = CountdownTicker(deadline)
                ticker.start()

            if question.q_type == "TF":
                timeout = (deadline - time.monotonic()) if deadline is not None else None
                is_correct = ask_tf(question, timeout)
                correct_text = "TRUE" if question.correct_tf == 1 else "FALSE"
            else:
                timeout = (deadline - time.monotonic()) if deadline is not None else None
                is_correct, correct_text = ask_mcq(conn, question, timeout)
        except InputTimeout:
            timed_out = True
        finally:
            if ticker is not None:
                ticker.stop()
                print()

        if timed_out:
            print(paint("  Time is up during input. Auto-submitting exam.", C.RED, C.BOLD))
            break

        elapsed = time.monotonic() - started
        results.append(
            AnswerResult(
                question_id=question.id,
                subtopic=question.subtopic,
                is_correct=is_correct,
                elapsed_seconds=elapsed,
            )
        )
        result_by_qid[question.id] = is_correct

        if mode == "practice":
            print()
            if is_correct:
                print(paint("  >>> CORRECT <<<", C.GREEN, C.BOLD))
            else:
                print(paint("  >>> INCORRECT <<<", C.RED, C.BOLD))
                print(f"  Correct answer: {paint(correct_text, C.BOLD)}")

            if question.justification:
                show_just = (
                    justification_mode == "always"
                    or (justification_mode == "incorrect" and not is_correct)
                )
                if show_just:
                    print(f"\n  {paint('Justification:', C.BOLD)} {question.justification}")

    if mode == "practice":
        correct = sum(1 for r in results if r.is_correct)
        attempted = len(results)
        panel("Practice Complete")
        print(f"  Answered: {attempted}/{total_questions}")
        print(f"  Correct: {paint(str(correct), C.GREEN, C.BOLD)}")
        print(f"  Incorrect: {paint(str(attempted - correct), C.RED, C.BOLD)}")
        if attempted:
            print(f"  Accuracy: {paint(f'{(correct / attempted) * 100:.1f}%', C.CYAN, C.BOLD)}")
            avg = sum(r.elapsed_seconds for r in results) / attempted
            print(f"  Average answer time: {avg:.1f}s")
        return

    total_correct = sum(1 for r in results if r.is_correct)
    attempted = len(results)
    required_correct = math.ceil(total_questions * 0.70)
    passed = total_correct >= required_correct

    end_time = time.monotonic()
    if deadline is not None:
        time_used = min(exam_seconds, end_time - exam_started_at)
    else:
        time_used = end_time - exam_started_at

    avg_answer_time = (sum(r.elapsed_seconds for r in results) / attempted) if attempted else 0.0

    per_subtopic: dict[str, dict[str, int]] = {}
    for q in questions:
        bucket = per_subtopic.setdefault(q.subtopic, {"total": 0, "correct": 0})
        bucket["total"] += 1

    for q in questions:
        if result_by_qid.get(q.id):
            per_subtopic[q.subtopic]["correct"] += 1

    panel("Exam Assessment")
    score_pct = (total_correct / total_questions) * 100 if total_questions else 0
    print(f"  Score: {paint(f'{total_correct}/{total_questions} ({score_pct:.1f}%)', C.BOLD)}")
    result_text = "PASS" if passed else "FAIL"
    result_style = (C.GREEN, C.BOLD) if passed else (C.RED, C.BOLD)
    print(f"  Result: {paint(result_text, *result_style)} (need at least {required_correct} correct)")
    print(f"  Answered: {attempted}/{total_questions}")
    print(f"  Time used: {fmt_seconds(time_used)}")
    print(f"  Average answer time: {avg_answer_time:.1f}s")
    print()
    print(paint("  Right/Missed by subtopic", C.BOLD, C.CYAN))
    print(paint("  " + hr("-", 56), C.GRAY))
    for subtopic in sorted(per_subtopic):
        total = per_subtopic[subtopic]["total"]
        correct = per_subtopic[subtopic]["correct"]
        missed = total - correct
        print(
            f"  {subtopic:<38} "
            f"right {paint(str(correct), C.GREEN)}   "
            f"missed {paint(str(missed), C.RED)}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CBP practice/exam CLI")
    parser.add_argument(
        "--mode",
        choices=["practice", "exam"],
        help="Mode to run. If omitted, you will be prompted.",
    )
    parser.add_argument(
        "--db",
        default="data/questions.db",
        help="Path to SQLite DB (default: data/questions.db)",
    )
    parser.add_argument(
        "--subtopic",
        help="Subtopic name for practice mode (default: prompt selector)",
    )
    parser.add_argument(
        "--question-count",
        type=int,
        help="Practice default is 25 (random). Exam default is 75.",
    )
    parser.add_argument(
        "--q-start",
        type=int,
        help="Practice only: lower q_number bound (inclusive).",
    )
    parser.add_argument(
        "--q-end",
        type=int,
        help="Practice only: upper q_number bound (inclusive).",
    )
    parser.add_argument(
        "--justification",
        choices=["always", "never", "incorrect"],
        default="incorrect",
        help="Practice mode: when to show justifications (default: incorrect)",
    )
    parser.add_argument(
        "--timer-minutes",
        type=int,
        default=20,
        help="Exam mode timer in minutes (default: 20)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    db_path = (repo_root / args.db).resolve()
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}. Run migration first.")

    splash()
    mode = choose_mode(args.mode)

    if mode == "exam":
        question_count = args.question_count if args.question_count is not None else 75
        if question_count <= 0:
            raise SystemExit("Question count must be greater than 0.")
    else:
        question_count = args.question_count if args.question_count is not None else 25

    with connect_db(db_path) as conn:
        if mode == "practice":
            subtopic = choose_subtopic(conn, args.subtopic)
            selection = choose_practice_selection(
                conn,
                subtopic=subtopic,
                requested_count=args.question_count,
                requested_q_start=args.q_start,
                requested_q_end=args.q_end,
            )
            questions = fetch_questions(
                conn,
                mode="practice",
                question_count=selection.question_count,
                subtopic_id=subtopic["id"],
                q_start=selection.q_start,
                q_end=selection.q_end,
            )
            if len(questions) < selection.question_count:
                scope_text = (
                    f" in range Q{selection.q_start}..Q{selection.q_end}"
                    if selection.q_start is not None and selection.q_end is not None
                    else ""
                )
                print(
                    paint(
                        (
                            f"Requested {selection.question_count} questions but only found "
                            f"{len(questions)} in '{subtopic['name']}'{scope_text}."
                        ),
                        C.YELLOW,
                    )
                )

            run_session(
                conn,
                mode="practice",
                questions=questions,
                justification_mode=args.justification,
                timer_minutes=args.timer_minutes,
            )
        else:
            questions = fetch_questions(conn, mode="exam", question_count=question_count)
            if len(questions) < question_count:
                print(paint(f"Requested {question_count} questions but only found {len(questions)} total.", C.YELLOW))

            run_session(
                conn,
                mode="exam",
                questions=questions,
                justification_mode=args.justification,
                timer_minutes=args.timer_minutes,
            )


if __name__ == "__main__":
    main()
