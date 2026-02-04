#!/usr/bin/env python3
"""Create and populate an SQLite question bank from practice/sessions/*.md."""

from __future__ import annotations

import argparse
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

QUESTION_RE = re.compile(r"^Q(\d+)\)\s*(.*)$")
CORRECT_RE = re.compile(r"^- Correct answer:\s*(.+?)\s*$")
JUSTIFICATION_RE = re.compile(r"^- Justification:\s*(.+?)\s*$")
OPTION_RE = re.compile(r"^([A-Z])\)\s*(.+)$")


@dataclass
class ParsedQuestion:
    subtopic_name: str
    q_number: int
    q_type: str
    prompt: str
    correct_tf: int | None
    justification: str | None
    options: list[tuple[str, int]]


def load_schema(schema_path: Path) -> str:
    return schema_path.read_text(encoding="utf-8")


def create_tables(conn: sqlite3.Connection, schema_sql: str) -> None:
    conn.executescript(schema_sql)


def clear_tables(conn: sqlite3.Connection) -> None:
    conn.execute("DELETE FROM question_options")
    conn.execute("DELETE FROM questions")
    conn.execute("DELETE FROM subtopics")


def parse_question_block(question_lines: list[str], correct_answer: str) -> tuple[str, list[tuple[str, int]]]:
    prompt_lines: list[str] = []
    options: list[tuple[str, int]] = []
    correct_key = correct_answer.strip().upper()

    for line in question_lines:
        stripped = line.strip()
        if not stripped:
            continue

        option_match = OPTION_RE.match(stripped)
        if option_match:
            option_key = option_match.group(1)
            option_text = option_match.group(2).strip()
            is_correct = 1 if option_key == correct_key else 0
            options.append((option_text, is_correct))
            continue

        prompt_lines.append(stripped)

    prompt = "\n".join(prompt_lines).strip()
    return prompt, options


def parse_markdown_file(md_path: Path) -> list[ParsedQuestion]:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    parsed: list[ParsedQuestion] = []

    i = 0
    while i < len(lines):
        q_match = QUESTION_RE.match(lines[i].strip())
        if not q_match:
            i += 1
            continue

        q_number = int(q_match.group(1))
        first_line = q_match.group(2).strip()

        i += 1
        question_lines = [first_line] if first_line else []

        while i < len(lines):
            candidate = lines[i].strip()
            if CORRECT_RE.match(candidate):
                break
            if QUESTION_RE.match(candidate):
                break
            question_lines.append(lines[i])
            i += 1

        if i >= len(lines):
            break

        correct_match = CORRECT_RE.match(lines[i].strip())
        if not correct_match:
            continue

        correct_answer = correct_match.group(1).strip()
        i += 1

        justification: str | None = None
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines):
            just_match = JUSTIFICATION_RE.match(lines[i].strip())
            if just_match:
                justification = just_match.group(1).strip()
                i += 1

        answer_upper = correct_answer.upper()
        if answer_upper in {"TRUE", "FALSE"}:
            q_type = "TF"
            correct_tf = 1 if answer_upper == "TRUE" else 0
            prompt, _ = parse_question_block(question_lines, correct_answer)
            options: list[tuple[str, int]] = []
        else:
            q_type = "MCQ"
            correct_tf = None
            prompt, options = parse_question_block(question_lines, correct_answer)

        if not prompt:
            continue

        parsed.append(
            ParsedQuestion(
                subtopic_name=md_path.stem,
                q_number=q_number,
                q_type=q_type,
                prompt=prompt,
                correct_tf=correct_tf,
                justification=justification,
                options=options,
            )
        )

    return parsed


def get_or_create_subtopic_id(
    conn: sqlite3.Connection, subtopic_name: str, cache: dict[str, int]
) -> int:
    existing = cache.get(subtopic_name)
    if existing is not None:
        return existing

    conn.execute("INSERT OR IGNORE INTO subtopics (name) VALUES (?)", (subtopic_name,))
    row = conn.execute("SELECT id FROM subtopics WHERE name = ?", (subtopic_name,)).fetchone()
    if row is None:
        raise RuntimeError(f"Failed to resolve subtopic id for: {subtopic_name}")

    subtopic_id = int(row[0])
    cache[subtopic_name] = subtopic_id
    return subtopic_id


def insert_questions(conn: sqlite3.Connection, questions: list[ParsedQuestion]) -> int:
    inserted = 0
    subtopic_cache: dict[str, int] = {}

    for q in questions:
        subtopic_id = get_or_create_subtopic_id(conn, q.subtopic_name, subtopic_cache)

        cursor = conn.execute(
            """
            INSERT INTO questions (subtopic_id, q_number, q_type, prompt, correct_tf, justification)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (subtopic_id, q.q_number, q.q_type, q.prompt, q.correct_tf, q.justification),
        )
        question_id = cursor.lastrowid

        for option_text, is_correct in q.options:
            conn.execute(
                """
                INSERT INTO question_options (question_id, option_text, is_correct)
                VALUES (?, ?, ?)
                """,
                (question_id, option_text, is_correct),
            )

        inserted += 1

    return inserted


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate practice session markdown to SQLite.")
    parser.add_argument(
        "--db",
        default="data/questions.db",
        help="SQLite db file path (default: data/questions.db)",
    )
    parser.add_argument(
        "--sessions-glob",
        default="practice/sessions/*.md",
        help="Glob for source markdown files (default: practice/sessions/*.md)",
    )
    parser.add_argument(
        "--schema",
        default="scripts/schema.sql",
        help="SQL schema path (default: scripts/schema.sql)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    db_path = repo_root / args.db
    schema_path = repo_root / args.schema
    sessions = sorted(repo_root.glob(args.sessions_glob))

    if not sessions:
        raise SystemExit(f"No session files found for glob: {args.sessions_glob}")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    schema_sql = load_schema(schema_path)

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        create_tables(conn, schema_sql)
        clear_tables(conn)

        total_inserted = 0
        for session_file in sessions:
            parsed_questions = parse_markdown_file(session_file)
            total_inserted += insert_questions(conn, parsed_questions)

        conn.commit()

    print(f"Migrated {total_inserted} questions into {db_path}")


if __name__ == "__main__":
    main()
