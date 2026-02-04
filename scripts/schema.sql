PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS subtopics (
  id    INTEGER PRIMARY KEY,
  name  TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS questions (
  id            INTEGER PRIMARY KEY,
  subtopic_id   INTEGER NOT NULL REFERENCES subtopics(id) ON DELETE RESTRICT,
  q_number      INTEGER NOT NULL,
  q_type        TEXT NOT NULL CHECK (q_type IN ('TF', 'MCQ')),
  prompt        TEXT NOT NULL,
  correct_tf    INTEGER CHECK (correct_tf IN (0,1)),
  justification TEXT
);

CREATE TABLE IF NOT EXISTS question_options (
  id            INTEGER PRIMARY KEY,
  question_id   INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  option_text   TEXT NOT NULL,
  is_correct    INTEGER NOT NULL CHECK (is_correct IN (0,1))
);

CREATE INDEX IF NOT EXISTS idx_questions_subtopic_id ON questions(subtopic_id);
CREATE INDEX IF NOT EXISTS idx_questions_type ON questions(q_type);
