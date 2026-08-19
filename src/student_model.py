from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Optional

from .config import settings
from .fact_extraction import clean_fact_text as shared_clean_fact_text
from .fact_extraction import fact_subtopic, fact_target_id
from .fact_extraction import is_testable_chunk as shared_is_testable_chunk
from .fact_extraction import split_fact_units as shared_split_fact_units
from .fsrs import (
    deserialize as fsrs_deserialize,
    fsrs_init,
    fsrs_review,
    mastery_proxy as fsrs_mastery_proxy,
    next_review_date_from_state,
    serialize as fsrs_serialize,
)
from .spaced_repetition import next_review_date, status_for_mastery
from .source_classifier import ANESTHESIA_LIBRARY, ICU_LIBRARY, INTERN_LIBRARY
from .topic_taxonomy import TOPICS


BASICS_TERMS = ("basic", "basics", "ca-1", "ca1")
ANESTHESIA_MODE_TERMS = BASICS_TERMS + ("anesthesia", "anesthesiology", "boards")
ICU_MODE_TERMS = ("icu", "critical care", "marino", "ventilator", "pressor")
CA1_FACT_MIN_WORDS = 5
CA1_FACT_MAX_CHARS = 180
SKIP_SECTION_TERMS = (
    "table of contents",
    "acknowledg",
    "contributors",
    "suggested checklist",
    "goals of the ca-1",
    "key points and expectations",
    "references",
    "suggested readings",
    "index",
)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


_WAL_INIT_PATHS: set[str] = set()


def conn() -> sqlite3.Connection:
    db_path = str(settings.sqlite_db_path)
    if db_path not in _WAL_INIT_PATHS:
        settings.ensure_dirs()
    c = sqlite3.connect(db_path)
    c.row_factory = sqlite3.Row
    if db_path not in _WAL_INIT_PATHS:
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA synchronous=NORMAL")
        _WAL_INIT_PATHS.add(db_path)
    return c


def _table_columns(db: sqlite3.Connection, table: str) -> set[str]:
    return {row["name"] for row in db.execute(f"PRAGMA table_info({table})").fetchall()}


def _ensure_column(db: sqlite3.Connection, table: str, column: str, definition: str) -> None:
    # PRAGMA table_info on a table that does not exist returns no rows rather
    # than raising, so a missing table used to surface here as a confusing
    # "no such table" from the ALTER. Tables are created in a specific order
    # inside initialize_database and the migration loop does not run last, so
    # skipping is the correct behaviour: the CREATE will include the column.
    if not _table_columns(db, table):
        return
    if column not in _table_columns(db, table):
        db.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def initialize_database() -> None:
    with conn() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS topics (
              topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
              library TEXT DEFAULT '',
              training_phase TEXT DEFAULT '',
              topic TEXT NOT NULL,
              subtopic TEXT DEFAULT '',
              source TEXT DEFAULT '',
              mastery_score REAL DEFAULT 0.25,
              confidence_score REAL DEFAULT 0.0,
              status TEXT DEFAULT 'new',
              last_seen TEXT, last_correct TEXT, last_partial TEXT, last_incorrect TEXT,
              times_seen INTEGER DEFAULT 0, times_correct INTEGER DEFAULT 0,
              times_partial INTEGER DEFAULT 0, times_incorrect INTEGER DEFAULT 0,
              next_review_date TEXT, forgetting_risk REAL DEFAULT 1.0,
              created_at TEXT, updated_at TEXT,
              UNIQUE(topic, subtopic)
            );
            CREATE TABLE IF NOT EXISTS question_attempts (
              attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT, session_id TEXT, topic_id INTEGER,
              library TEXT DEFAULT '', training_phase TEXT DEFAULT '',
              topic TEXT, subtopic TEXT,
              question TEXT, user_answer TEXT, ideal_answer TEXT, result TEXT,
              mistake_type TEXT, difficulty TEXT, hints_used INTEGER DEFAULT 0,
              confidence_reported REAL, retrieval_sources TEXT, source_citations TEXT, notes TEXT
            );
            CREATE TABLE IF NOT EXISTS sessions (
              session_id TEXT PRIMARY KEY, date TEXT, requested_mode TEXT, mode TEXT,
              training_phase TEXT DEFAULT '',
              duration_minutes INTEGER, selected_topics TEXT, rationale TEXT,
              summary TEXT, created_at TEXT
            );
            CREATE TABLE IF NOT EXISTS learned_facts (
              fact_id INTEGER PRIMARY KEY AUTOINCREMENT,
              topic_id INTEGER, fact TEXT, source TEXT, first_learned TEXT,
              last_demonstrated TEXT, confidence_score REAL DEFAULT 0.0,
              review_interval_days INTEGER DEFAULT 1, next_review_date TEXT
            );
            CREATE TABLE IF NOT EXISTS settings (
              key TEXT PRIMARY KEY,
              value TEXT,
              updated_at TEXT
            );
            """
        )
        for table, columns in {
            "topics": {
                "library": "TEXT DEFAULT ''",
                "training_phase": "TEXT DEFAULT ''",
                "last_partial": "TEXT",
                "fsrs_state": "TEXT",
            },
            "question_attempts": {
                "library": "TEXT DEFAULT ''",
                "training_phase": "TEXT DEFAULT ''",
                "source_citations": "TEXT",
                "confidence_actual": "REAL DEFAULT 0.0",
                "teach_back_quality": "REAL DEFAULT 0.0",
                "transfer_success": "BOOLEAN DEFAULT 0",
                "bloom_level": "TEXT DEFAULT ''",  # recall|apply|analyze|evaluate|transfer
                # Verbatim exchange, for auditing what was actually said.
                # `user_answer` holds the tutor's GRADED SUMMARY ("correctly
                # identified lactulose, wrong mechanism") — useful for grading,
                # useless for auditing, because it is the tutor's account of
                # the user rather than the user's own words. Repeated audits
                # stalled on exactly this: the user asked whether their stated
                # reason for declining a topic was recorded anywhere, and it
                # was not, because prose never reaches the backend at all.
                "user_answer_verbatim": "TEXT DEFAULT ''",
                "tutor_response": "TEXT DEFAULT ''",
                # The source passage the question was built from. Previously
                # accepted by submit_answer and written only to the tool log,
                # never to the row — so an audit that selected it as a column
                # died with "no such column: grounded_in". Grounding belongs
                # next to the answer it grounds.
                "grounded_in": "TEXT DEFAULT ''",
                # Set when the answer was scored as exposure rather than recall
                # (a restatement of what the tutor had just said).
                "graded_as_exposure": "INTEGER DEFAULT 0",
            },
            "knowledge_points": {
                # The user's own words that demonstrate this fact. Stored, not
                # just checked, so "why am I seeing this again?" is answerable.
                "evidence": "TEXT DEFAULT ''",
                # NULL means never actually put to the user. Bulk ingestion
                # previously wrote facts through the same path an answered
                # question uses, so 253 facts looked asked-and-failed when they
                # had never been shown — inflating coverage to 6.6% against a
                # true 2.4%, poisoning every accuracy figure, and queueing the
                # lot for the next morning in the top-priority bucket.
                "first_presented_at": "TEXT",
                # Provenance for the fact itself. Without it the tutor has
                # nothing to cite when it serves a stored fact, and grounding
                # degrades into naming the fact table it came from.
                "source": "TEXT DEFAULT ''",
            },
            "sessions": {
                "mode": "TEXT",
                "training_phase": "TEXT DEFAULT ''",
            },
        }.items():
            for column, definition in columns.items():
                _ensure_column(db, table, column, definition)

        # NEW: Mastery vector table (one row per topic)
        db.execute("""
            CREATE TABLE IF NOT EXISTS mastery_vector (
                topic_id INTEGER PRIMARY KEY,
                topic_name TEXT UNIQUE NOT NULL,
                accuracy REAL DEFAULT 0.0,                    -- % correct (0-1)
                transfer_auc REAL DEFAULT 0.0,                -- Area under ROC on novel cases (0-1)
                mechanism_quality REAL DEFAULT 0.0,           -- Teach-back rubric score (0-1)
                calibration_icc REAL DEFAULT 0.0,             -- Intraclass correlation (confidence vs actual) (0-1)
                retention_6mo REAL DEFAULT 0.0,               -- % retained at 6 months (0-1)
                integration_score REAL DEFAULT 0.0,           -- Can integrate with other topics (0-1)
                mastery_achieved BOOLEAN DEFAULT 0,           -- True if all criteria met
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # NEW: Topic hierarchy for subtopic relationships (for follow-up learning)
        db.execute("""
            CREATE TABLE IF NOT EXISTS topic_hierarchy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                relationship_type TEXT DEFAULT 'subtopic',  -- 'subtopic', 'prerequisite', 'related'
                order_priority INTEGER DEFAULT 0,  -- for ordering follow-up suggestions
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(parent_topic_id, child_topic_id, relationship_type)
            )
        """)

        # NEW: Track active follow-up sessions (nested learning)
        db.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                parent_session_state TEXT,  -- JSON: {lesson_phase, progress, last_answer_timestamp}
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)

        # NEW: Fine-grained subtopic weakness tracking
        db.execute("""
            CREATE TABLE IF NOT EXISTS subtopic_weaknesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                subtopic_id INTEGER NOT NULL,
                weakness_type TEXT NOT NULL,  -- 'mechanism', 'dosing', 'monitoring', 'indications', 'side_effects'
                failure_count INTEGER DEFAULT 0,
                last_seen TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(topic_id, subtopic_id, weakness_type)
            )
        """)

        # Atomic KNOWLEDGE POINTS — the finest grain of tracking: one testable fact
        # (e.g. "ARDS: low tidal volume 6 mL/kg IBW is the mortality move, not PEEP").
        # Each point carries its OWN correctness history, per-point confidence +
        # calibration, and an INDEPENDENT spaced-repetition schedule, so a weak fact
        # resurfaces on its own timeline and graduates to 'mastered' after repeated
        # correct recalls — regardless of its parent topic's schedule. This is the
        # unit that powers granular error tracking AND per-point confidence on
        # compound questions. Distinct from the topics table (topic-level FSRS).
        db.execute("""
            CREATE TABLE IF NOT EXISTS knowledge_points (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                point TEXT NOT NULL,                 -- atomic canonical fact
                status TEXT DEFAULT 'weak',          -- 'weak'|'learning'|'mastered'|'new'
                times_seen INTEGER DEFAULT 0,
                times_correct INTEGER DEFAULT 0,
                consecutive_correct INTEGER DEFAULT 0,
                last_correct INTEGER,                -- 0/1 of last attempt
                last_confidence INTEGER,             -- 1-5 of last attempt
                confidence_sum INTEGER DEFAULT 0,    -- for avg confidence (calibration)
                confidence_n INTEGER DEFAULT 0,
                mistake_type TEXT DEFAULT 'other',
                interval_days REAL DEFAULT 0,        -- current spacing interval (days)
                fsrs_state TEXT,                     -- per-point FSRS-4 state (JSON)
                next_review_date TEXT,
                created_at TEXT,
                updated_at TEXT,
                -- The user's own words demonstrating this fact. Stored so that
                -- "why am I being asked this again?" is answerable from the
                -- row itself rather than by diffing session transcripts.
                evidence TEXT DEFAULT '',
                -- NULL = never actually put to the user. Bulk ingestion once
                -- wrote facts through the same path an answered question uses,
                -- so 253 facts read as asked-and-failed without ever being
                -- shown: coverage reported 6.6% against a true 2.4%, accuracy
                -- was dragged toward zero by questions never asked, and the
                -- whole batch queued for the next morning as 'weak'.
                first_presented_at TEXT,
                -- Where this fact came from: book/guideline and location.
                -- Its absence was mistaken for tutor laziness. Reviewing a
                -- stored fact the tutor had nothing to cite, and honestly wrote
                -- "<Topic> knowledge point bank" on 11 of 17 answers — which
                -- reads as a rubber stamp but accurately described a fact table
                -- that recorded no provenance. A fact you cannot trace is a
                -- fact you cannot check, which is how an invented vasopressor
                -- threshold survived being drilled five times.
                source TEXT DEFAULT '',
                UNIQUE(topic, point)
            )
        """)
        for col, defn in [("fsrs_state", "TEXT")]:
            _ensure_column(db, "knowledge_points", col, defn)

        # Illness scripts — the expert's mental model of a diagnosis (5 fields).
        # Drilled by reconstruction, not recited as a fact list.
        db.execute("""
            CREATE TABLE IF NOT EXISTS illness_scripts (
                topic TEXT PRIMARY KEY,
                enabling_conditions TEXT DEFAULT '',
                pathophysiology TEXT DEFAULT '',
                time_course TEXT DEFAULT '',
                key_features TEXT DEFAULT '',
                consequence_if_missed TEXT DEFAULT '',
                discipline TEXT DEFAULT '',
                source TEXT DEFAULT '',
                created_at TEXT,
                updated_at TEXT
            )
        """)

        # Confusable pairs — diagnoses/entities that mimic each other. Drive
        # contrastive cases ("what's the discriminating feature, and why?").
        db.execute("""
            CREATE TABLE IF NOT EXISTS confusable_pairs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_a TEXT NOT NULL,
                topic_b TEXT NOT NULL,
                discriminator TEXT DEFAULT '',
                created_at TEXT,
                UNIQUE(topic_a, topic_b)
            )
        """)

        # Curriculum blueprint table — full universe of topics to master
        db.execute("""
            CREATE TABLE IF NOT EXISTS curriculum (
                topic TEXT PRIMARY KEY,
                domain TEXT DEFAULT '',
                discipline TEXT DEFAULT '',
                is_critical_care INTEGER DEFAULT 0,
                subtopics TEXT DEFAULT '',
                high_yield INTEGER DEFAULT 1,
                priority_tier INTEGER DEFAULT 2,
                category TEXT DEFAULT 'topic',
                added_at TEXT
            )
        """)
        # Backfill columns for existing DBs that predate this schema version
        # (ALTER TABLE is idempotent via helper).
        for col, defn in [
            ("discipline", "TEXT DEFAULT ''"),
            ("is_critical_care", "INTEGER DEFAULT 0"),
            ("priority_tier", "INTEGER DEFAULT 2"),
            ("category", "TEXT DEFAULT 'topic'"),
        ]:
            _ensure_column(db, "curriculum", col, defn)

        db.execute(
            "INSERT OR IGNORE INTO settings(key, value, updated_at) VALUES('default_training_phase', ?, ?)",
            (settings.default_training_phase, now()),
        )

        # Dosing-drill rules table (populated by seed_dosing_rules)
        db.execute("""
            CREATE TABLE IF NOT EXISTS dosing_rules (
                id TEXT PRIMARY KEY,
                drug TEXT NOT NULL,
                context TEXT NOT NULL,
                calc_type TEXT NOT NULL,
                params_json TEXT NOT NULL,
                randomize_json TEXT NOT NULL,
                units TEXT NOT NULL,
                discipline TEXT DEFAULT '',
                is_critical_care INTEGER DEFAULT 0,
                source TEXT DEFAULT '',
                explanation TEXT DEFAULT '',
                created_at TEXT
            )
        """)

        # KP Catalog — generated knowledge points from the catalog JSON.
        # Priority columns (tier/category/is_critical_care) are denormalized here so
        # get_kp_to_study can ORDER without joining curriculum at query time.
        db.execute("""
            CREATE TABLE IF NOT EXISTS kp_catalog (
                id TEXT PRIMARY KEY,
                topic TEXT NOT NULL,
                domain TEXT DEFAULT '',
                discipline TEXT DEFAULT '',
                stem TEXT NOT NULL,
                answer TEXT DEFAULT '',
                rationale TEXT DEFAULT '',
                bloom TEXT DEFAULT '',
                source TEXT DEFAULT '',        -- JSON array
                confusable_with TEXT DEFAULT '',
                tier INTEGER DEFAULT 2,
                category TEXT DEFAULT 'topic',
                is_critical_care INTEGER DEFAULT 0,
                car_safe INTEGER DEFAULT 0,    -- 1 = short/ear-friendly for car-mode study
                times_seen INTEGER DEFAULT 0,  -- times served by get_kp_to_study (advance, don't repeat)
                added_at TEXT
            )
        """)
        _ensure_column(db, "kp_catalog", "car_safe", "INTEGER DEFAULT 0")
        _ensure_column(db, "kp_catalog", "times_seen", "INTEGER DEFAULT 0")
        # Corpus-verification status from the two-pass grounding audit:
        #   1 = fact's content confirmed against the corpus (open retrieval OR
        #       its own cited page)  0 = no supporting page found anywhere.
        # Tutors surface unverified facts with a caveat instead of teaching
        # them as sourced truth.
        _ensure_column(db, "kp_catalog", "verified", "INTEGER DEFAULT 1")


_CRITICAL_CARE_KEYWORDS = (
    "icu",
    "critical care",
    "crises",
    "crisis",
    "resuscitation",
    "shock",
    "sepsis",
    "ards",
    "ventilat",
    "vasopressor",
    "acls",
    "code",
    "emergency",
    "airway",
    "anaphylaxis",
)


def _derive_discipline(domain: str) -> str:
    """Map a domain string to 'anesthesia' or 'medicine'. In this curriculum the
    medicine domains are labeled 'Internal medicine: ...' / 'General internal
    medicine ...'; every other domain is anesthesia (incl. Airway, Pain, Preop,
    Crises, Safety, which don't contain the word 'anesthesia')."""
    d = domain.lower().strip()
    if d.startswith("internal medicine") or d.startswith("general internal medicine"):
        return "medicine"
    return "anesthesia"


def _derive_is_critical_care(domain: str, topic: str) -> int:
    """Return 1 if domain or topic matches any critical-care keyword."""
    text = (domain + " " + topic).lower()
    return 1 if any(kw in text for kw in _CRITICAL_CARE_KEYWORDS) else 0


def seed_curriculum(path: str) -> int:
    """Load curriculum blueprint JSON and UPSERT into the curriculum table.

    Each entry: {"domain": str, "topic": str, "subtopics": [str], "high_yield": bool}.
    Returns the number of rows processed. Idempotent.
    """
    initialize_database()
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    ts = now()
    count = 0
    with conn() as db:
        for item in data:
            topic = str(item.get("topic", "")).strip()
            if not topic:
                continue
            domain = str(item.get("domain", ""))
            discipline = str(item.get("discipline", "")).strip() or _derive_discipline(domain)
            # Allow the blueprint to set is_critical_care explicitly; otherwise derive
            # it from keyword matching on the domain/topic.
            if "is_critical_care" in item:
                is_critical_care = 1 if item.get("is_critical_care") else 0
            else:
                is_critical_care = _derive_is_critical_care(domain, topic)
            category = str(item.get("category", "topic")).strip() or "topic"
            subtopics = json.dumps(item.get("subtopics", []))
            high_yield = 1 if item.get("high_yield", True) else 0
            try:
                priority_tier = int(item.get("priority_tier", 2))
                priority_tier = max(1, min(3, priority_tier))
            except (TypeError, ValueError):
                priority_tier = 2
            db.execute(
                """INSERT INTO curriculum(topic, domain, discipline, is_critical_care, subtopics, high_yield, priority_tier, category, added_at)
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(topic) DO UPDATE SET
                       domain=excluded.domain,
                       discipline=excluded.discipline,
                       is_critical_care=excluded.is_critical_care,
                       subtopics=excluded.subtopics,
                       high_yield=excluded.high_yield,
                       priority_tier=excluded.priority_tier,
                       category=excluded.category""",
                (topic, domain, discipline, is_critical_care, subtopics, high_yield, priority_tier, category, ts),
            )
            count += 1
    return count


_CAR_UNSAFE_STEM_PHRASES = (
    "which of the following",
    "list ",
    "name all",
    "label",
    "shown",
    "figure",
    "image",
)

_CAR_ENUMERATION_THRESHOLD = 3  # answer.count(',') + count(';') + count(' and ') >= this → unsafe


def _kp_car_safe(stem: str, answer: str, rationale: str | None) -> int:
    """Return 1 if this KP is safe to study in car/voice mode, else 0.

    A KP is car-safe when ALL of the following hold:
      - stem   ≤ 120 chars  (short enough to speak)
      - answer ≤ 180 chars  (short enough to hear)
      - rationale ≤ 200 chars  (brief enough for a spoken 1-sentence teach)
      - answer is NOT a long enumeration:
          (answer.count(',') + answer.count(';') + answer.lower().count(' and ')) < 3
      - stem (lowercased) contains none of the unsafe visual/list phrases:
          "which of the following", "list ", "name all", "label", "shown",
          "figure", "image"
    """
    rat = rationale or ""
    if len(stem) > 120:
        return 0
    if len(answer) > 180:
        return 0
    if len(rat) > 200:
        return 0
    enum_count = answer.count(",") + answer.count(";") + answer.lower().count(" and ")
    if enum_count >= _CAR_ENUMERATION_THRESHOLD:
        return 0
    stem_lower = stem.lower()
    if any(phrase in stem_lower for phrase in _CAR_UNSAFE_STEM_PHRASES):
        return 0
    return 1


def seed_kp_catalog(path: str) -> dict[str, int]:
    """Load a KP catalog JSON and UPSERT entries into the database.

    Handles three entry types:
      - plain KP (no _type field): UPSERTs into kp_catalog.
        Priority columns (tier/category/is_critical_care/discipline) are derived
        from the curriculum table keyed on topic; falls back to entry-level values
        or safe defaults when the topic is not in the curriculum.
      - _type == 'illness_script': calls upsert_illness_script.
      - _type == 'confusable_pair': calls add_confusable_pair.

    Idempotent: re-running on the same file produces the same DB state.
    Returns {"kps": n, "illness_scripts": n, "confusable_pairs": n}.
    """
    initialize_database()
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    ts = now()
    kps_count = 0
    scripts_count = 0
    pairs_count = 0

    with conn() as db:
        # Build a lookup map from curriculum so we can derive priority fields.
        curr_rows = db.execute(
            "SELECT topic, discipline, is_critical_care, priority_tier, category FROM curriculum"
        ).fetchall()
        curr_map: dict[str, sqlite3.Row] = {r["topic"]: r for r in curr_rows}

    for entry in data:
        entry_type = entry.get("_type", "")

        if entry_type == "illness_script":
            upsert_illness_script(
                topic=str(entry.get("topic", "")).strip(),
                enabling_conditions=str(entry.get("enabling_conditions", "")),
                pathophysiology=str(entry.get("pathophysiology", "")),
                time_course=str(entry.get("time_course", "")),
                key_features=str(entry.get("key_features", "")),
                consequence_if_missed=str(entry.get("consequence_if_missed", "")),
                discipline=str(entry.get("discipline", "")),
            )
            scripts_count += 1
            continue

        if entry_type == "confusable_pair":
            add_confusable_pair(
                topic_a=str(entry.get("topic_a", "")).strip(),
                topic_b=str(entry.get("topic_b", "")).strip(),
                discriminator=str(entry.get("discriminator", "")),
            )
            pairs_count += 1
            continue

        # Plain KP entry
        kp_id = str(entry.get("id", "")).strip()
        topic = str(entry.get("topic", "")).strip()
        stem = str(entry.get("stem", "")).strip()
        if not kp_id or not topic or not stem:
            continue  # skip malformed entries

        domain = str(entry.get("domain", ""))
        # Derive priority columns from curriculum if the topic is present there;
        # otherwise fall back to whatever the entry provides or safe defaults.
        curr = curr_map.get(topic)
        if curr:
            discipline = curr["discipline"] or str(entry.get("discipline", "")) or _derive_discipline(domain)
            is_critical_care = int(curr["is_critical_care"])
            tier = int(curr["priority_tier"] or 2)
            category = str(curr["category"] or "topic")
        else:
            discipline = str(entry.get("discipline", "")) or _derive_discipline(domain)
            is_critical_care = _derive_is_critical_care(domain, topic)
            try:
                tier = max(1, min(3, int(entry.get("tier", 2))))
            except (TypeError, ValueError):
                tier = 2
            category = str(entry.get("category", "topic")).strip() or "topic"

        source_val = entry.get("source", [])
        source_json = json.dumps(source_val) if not isinstance(source_val, str) else source_val

        answer_str = str(entry.get("answer", ""))
        rationale_str = str(entry.get("rationale", ""))
        car_safe = _kp_car_safe(stem, answer_str, rationale_str)

        with conn() as db:
            db.execute(
                """INSERT INTO kp_catalog(id, topic, domain, discipline, stem, answer,
                       rationale, bloom, source, confusable_with,
                       tier, category, is_critical_care, car_safe, verified, added_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                   ON CONFLICT(id) DO UPDATE SET
                       topic=excluded.topic,
                       domain=excluded.domain,
                       discipline=excluded.discipline,
                       stem=excluded.stem,
                       answer=excluded.answer,
                       rationale=excluded.rationale,
                       bloom=excluded.bloom,
                       source=excluded.source,
                       confusable_with=excluded.confusable_with,
                       tier=excluded.tier,
                       category=excluded.category,
                       is_critical_care=excluded.is_critical_care,
                       car_safe=excluded.car_safe,
                       verified=excluded.verified""",
                (
                    kp_id, topic, domain, discipline, stem,
                    answer_str,
                    rationale_str,
                    str(entry.get("bloom", "")),
                    source_json,
                    str(entry.get("confusable_with", "")),
                    tier, category, is_critical_care, car_safe,
                    int(entry.get("verified", 1)), ts,
                ),
            )
        kps_count += 1

    return {"kps": kps_count, "illness_scripts": scripts_count, "confusable_pairs": pairs_count}


def get_medicine_weight() -> float:
    """Return the stored medicine_weight setting (default 0.8)."""
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT value FROM settings WHERE key='medicine_weight'").fetchone()
    try:
        return float(row["value"]) if row and row["value"] else 0.8
    except (TypeError, ValueError):
        return 0.8


def set_medicine_weight(weight: float) -> None:
    """Store the medicine_weight setting (0.0–1.0). Flippable at runtime."""
    initialize_database()
    clamped = max(0.0, min(1.0, float(weight)))
    with conn() as db:
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('medicine_weight', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (str(clamped), now()),
        )


# --- Daily load economics (spaced-repetition needs a bounded daily intake) ---

def get_current_rotation() -> str:
    """The rotation the student is currently on ('' = none set). New-topic
    selection biases toward matching curriculum domains so study lands the
    same week the patients do — the strongest encoding context available."""
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT value FROM settings WHERE key='current_rotation'").fetchone()
    return (row["value"] or "") if row else ""


def set_current_rotation(rotation: str) -> None:
    initialize_database()
    with conn() as db:
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('current_rotation', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            ((rotation or "").strip(), now()),
        )


def get_int_setting(key: str, default: int) -> int:
    """Read an integer setting, falling back to default."""
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    try:
        return int(row["value"]) if row and row["value"] is not None else default
    except (TypeError, ValueError):
        return default


def set_int_setting(key: str, value: int) -> None:
    initialize_database()
    with conn() as db:
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES(?, ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (key, str(int(value)), now()),
        )


def get_daily_new_item_cap() -> int:
    """Max NEW topics to introduce per day (default 20). Bounds the future review
    pile so the schedule never collapses."""
    return get_int_setting("daily_new_item_cap", 20)


# Measured on this user's own history, not assumed:
#   - a fact's review schedule compounds 3 -> 14 -> 50 -> 154 -> 427 days, so it
#     costs about 6 reviews in its first year, heavily front-loaded
#   - a review takes ~1.4 minutes
#   - answers mint ~1.0 new fact each
# Which makes the steady-state daily review load roughly
#   new_facts_per_day x 3.4 reviews/day  (at the 90-day mark)
# So the daily review burden is CHOSEN when the new-material rate is chosen; it
# is not a backlog that clears. At the observed 15 new facts per study day the
# steady state is ~51 reviews/day, about 70 minutes EVERY day, forever — which
# is exactly the "drowning in reviews, never reach new material" experience.
_REVIEWS_PER_NEW_FACT_PER_DAY = 3.4
_MINUTES_PER_REVIEW = 1.4


def get_daily_review_minutes_target() -> int:
    """How many minutes a day the user is willing to spend on REVIEWS."""
    return get_int_setting("daily_review_minutes_target", 30)


def sustainable_new_facts_per_day() -> int:
    """New facts per day whose steady-state review load fits the time budget.

    This is the honest version of "how much new material can I take on?" — the
    answer is fixed by arithmetic once the daily review budget is chosen, and
    getting it wrong is invisible for weeks because the review debt arrives
    later than the learning does.
    """
    target = max(5, get_daily_review_minutes_target())
    reviews = target / _MINUTES_PER_REVIEW
    return max(1, int(reviews / _REVIEWS_PER_NEW_FACT_PER_DAY))


def count_new_facts_today() -> int:
    """Facts first presented today — the number the cap actually governs."""
    initialize_database()
    with conn() as db:
        return db.execute(
            "SELECT COUNT(*) FROM knowledge_points "
            "WHERE date(COALESCE(first_presented_at, created_at), 'localtime') "
            "      = date('now','localtime')").fetchone()[0]


def get_daily_review_budget() -> int:
    """Target max reviews per day (default 200). Advisory load signal for the tutor."""
    return get_int_setting("daily_review_budget", 200)


def local_day_start_utc_iso() -> str:
    """Start of the STUDENT'S current local day, expressed as a UTC ISO string
    (attempt timestamps are stored in UTC). Day-boundary counters must use
    this: comparing against the UTC date string made "today" begin at 8pm the
    previous evening for a US-Eastern user — the daily new-item cap reset
    mid-evening and one evening session was split across two "days"."""
    local_midnight = datetime.now().astimezone().replace(hour=0, minute=0, second=0, microsecond=0)
    return local_midnight.astimezone(timezone.utc).isoformat()


def count_new_topics_today() -> int:
    """Distinct curriculum topics introduced (first-ever attempt) in the
    student's current LOCAL day."""
    initialize_database()
    today = local_day_start_utc_iso()
    with conn() as db:
        row = db.execute(
            """SELECT COUNT(*) FROM (
                   SELECT topic FROM question_attempts
                   GROUP BY topic
                   HAVING MIN(date) >= ?
               )""",
            (today,),
        ).fetchone()
    return int(row[0]) if row else 0


def _is_basics_context(mode: str = "", focus_topic: str | None = None) -> bool:
    text = f"{mode} {focus_topic or ''}".lower()
    return any(term in text for term in BASICS_TERMS)


def get_default_training_phase() -> str:
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT value FROM settings WHERE key='default_training_phase'").fetchone()
    return row["value"] if row and row["value"] else settings.default_training_phase


def set_default_training_phase(phase: str) -> None:
    initialize_database()
    with conn() as db:
        db.execute(
            "INSERT INTO settings(key, value, updated_at) VALUES('default_training_phase', ?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
            (phase, now()),
        )


def training_phase_for_mode(mode: str = "default", focus_topic: str | None = None, requested_phase: str | None = None) -> str:
    if requested_phase:
        return requested_phase
    text = f"{mode} {focus_topic or ''}".lower()
    if any(term in text for term in ANESTHESIA_MODE_TERMS):
        return "anesthesia_boards" if not "transition" in text else "anesthesia_transition"
    if any(term in text for term in ICU_MODE_TERMS):
        return "ICU"
    if mode in {"default", "mixed", ""}:
        return get_default_training_phase()
    if mode in {"intern_teach", "cross_cover", "admission_plan", "wards_rounding", "rapid_response"}:
        return "intern_year"
    return get_default_training_phase()


def get_ca1_topic_catalog() -> list[str]:
    path = settings.chroma_dir / "chunks.jsonl"
    counts: dict[str, int] = {}
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    row = json.loads(line)
                except Exception:
                    continue
                meta = row.get("metadata", {})
                if meta.get("book") != "Stanford CA-1":
                    continue
                for tag in meta.get("topic_tags", "").split(","):
                    tag = tag.strip()
                    if tag:
                        counts[tag] = counts.get(tag, 0) + 1
    if counts:
        return [topic for topic, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))]
    return list(TOPICS.keys())


def _clean_fact_text(text: str) -> str:
    return shared_clean_fact_text(text)


def _split_fact_units(text: str) -> list[str]:
    return shared_split_fact_units(text, max_chars=CA1_FACT_MAX_CHARS)


def _is_testable_chunk(meta: dict[str, Any], text: str) -> bool:
    return shared_is_testable_chunk(meta, text)


_FACT_CATALOG_CACHE: dict[tuple, list[dict[str, Any]]] = {}
_FACT_CATALOG_MTIME: int | None = None


def get_fact_catalog(
    source: str | None = None,
    max_facts_per_chunk: int = 32,
    library: str | None = None,
    training_phase: str | None = None,
) -> list[dict[str, Any]]:
    path = settings.chroma_dir / "chunks.jsonl"
    facts: list[dict[str, Any]] = []
    if not path.exists():
        return []
    # Cache by (source, library, training_phase, max_facts_per_chunk) + jsonl mtime.
    global _FACT_CATALOG_MTIME, _FACT_CATALOG_CACHE
    mtime_ns = path.stat().st_mtime_ns
    if _FACT_CATALOG_MTIME != mtime_ns:
        _FACT_CATALOG_CACHE = {}
        _FACT_CATALOG_MTIME = mtime_ns
    cache_key = (source, library, training_phase, max_facts_per_chunk)
    if cache_key in _FACT_CATALOG_CACHE:
        return list(_FACT_CATALOG_CACHE[cache_key])
    # Reuse the retrieval-layer cached chunk index instead of re-reading + re-parsing.
    from .retrieval import load_json_chunks
    rows = load_json_chunks()
    use_fact_rows = any(row.get("metadata", {}).get("chunk_type") == "fact" for row in rows)
    for row in rows:
            meta = row.get("metadata", {})
            source_name = meta.get("source_name") or meta.get("book", "")
            if source and source_name != source:
                continue
            if library and meta.get("library") != library:
                continue
            if training_phase and meta.get("training_phase") != training_phase:
                continue
            text = row.get("search_text") or row.get("text", "")
            if use_fact_rows:
                if meta.get("chunk_type") != "fact":
                    continue
                fact = meta.get("fact_text") or row.get("text", "")
                page = meta.get("page")
                tags = [tag for tag in meta.get("topic_tags", "").split(",") if tag]
                topic = tags[0] if tags else (meta.get("section") or source_name or "Source")
                facts.append(
                    {
                        "target_id": meta.get("chunk_id") or fact_target_id(source_name, page, fact, int(meta.get("fact_index") or 1)),
                        "topic": topic,
                        "subtopic": meta.get("subtopic") or fact_subtopic(source_name, page, fact),
                        "fact": fact,
                        "page": page,
                        "section": meta.get("section", ""),
                        "source": source_name,
                        "library": meta.get("library", ""),
                        "training_phase": meta.get("training_phase", ""),
                        "clinical_context": meta.get("clinical_context", ""),
                    }
                )
                continue
            if not _is_testable_chunk(meta, text):
                continue
            tags = [tag for tag in meta.get("topic_tags", "").split(",") if tag]
            topic = tags[0] if tags else (meta.get("section") or source_name or "Source")
            page = meta.get("page")
            display_source = "CA-1" if source_name == "Stanford CA-1" else source_name
            for idx, fact in enumerate(_split_fact_units(text)[:max_facts_per_chunk], start=1):
                facts.append(
                    {
                        "target_id": fact_target_id(source_name, page, fact, idx),
                        "topic": topic,
                        "subtopic": fact_subtopic(source_name, page, fact),
                        "fact": fact,
                        "page": page,
                        "section": meta.get("section", ""),
                        "source": source_name,
                        "library": meta.get("library", ""),
                        "training_phase": meta.get("training_phase", ""),
                        "clinical_context": meta.get("clinical_context", ""),
                    }
                )
    _FACT_CATALOG_CACHE[cache_key] = facts
    return facts


def get_ca1_fact_catalog(max_facts_per_chunk: int = 32) -> list[dict[str, Any]]:
    return get_fact_catalog("Stanford CA-1", max_facts_per_chunk)


def get_supporting_fact_catalog(max_facts_per_chunk: int = 32) -> list[dict[str, Any]]:
    facts = []
    for book in ["Morgan & Mikhail", "Miller/Baby Miller"]:
        facts.extend(get_fact_catalog(book, max_facts_per_chunk))
    return facts


def get_library_fact_catalog(library: str, max_facts_per_chunk: int = 32) -> list[dict[str, Any]]:
    return get_fact_catalog(None, max_facts_per_chunk, library=library)


def get_intern_fact_catalog(max_facts_per_chunk: int = 32) -> list[dict[str, Any]]:
    return get_library_fact_catalog(INTERN_LIBRARY, max_facts_per_chunk)


def get_icu_fact_catalog(max_facts_per_chunk: int = 32) -> list[dict[str, Any]]:
    return get_library_fact_catalog(ICU_LIBRARY, max_facts_per_chunk)


def get_or_create_topic(topic: str, subtopic: str = "", source: str = "", library: str = "", training_phase: str = "") -> int:
    """Atomic upsert. Race-safe under WAL with multiple concurrent writers."""
    initialize_database()
    sub = subtopic or ""
    ts = now()
    with conn() as db:
        # Atomic insert; collisions are silently ignored by the UNIQUE
        # constraint, leaving any existing row untouched.
        db.execute(
            """INSERT OR IGNORE INTO topics
               (library, training_phase, topic, subtopic, source, status,
                next_review_date, created_at, updated_at)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (library, training_phase, topic, sub, source, "new",
             next_review_date(0.25), ts, ts),
        )
        # Existing row (or freshly inserted): top up missing source/library/training_phase
        db.execute(
            """UPDATE topics
               SET source=COALESCE(NULLIF(source,''), ?),
                   library=COALESCE(NULLIF(library,''), ?),
                   training_phase=COALESCE(NULLIF(training_phase,''), ?),
                   updated_at=?
               WHERE topic=? AND subtopic=?""",
            (source, library, training_phase, ts, topic, sub),
        )
        row = db.execute(
            "SELECT topic_id FROM topics WHERE topic=? AND subtopic=?",
            (topic, sub),
        ).fetchone()
        return int(row["topic_id"])


CRITICAL_MISTAKES = {
    "crisis_algorithm",
    "drug_dosing",
    "failure_to_escalate",
    "overconfident_wrong",
}


def _result_to_fsrs_rating(
    result: str,
    mistake_type: str,
    hints_used: int,
    confidence_reported: float | None = None,
) -> int:
    """Map a graded attempt to an FSRS 1-4 rating.

    Confidence calibration (Bjork): confident-wrong is the dangerous case —
    keep at rating 1 (the FSRS lapse path) and the caller still tags
    `mistake_type='overconfident_wrong'` to bump difficulty further. Unsure-
    right earns the easy-rating bonus because that confidence-correct
    increment is genuine learning, not pattern-matching.
    """
    conf = confidence_reported if confidence_reported is not None else None
    if result == "incorrect":
        return 1
    if result == "partial":
        return 2
    if result == "correct":
        if mistake_type in CRITICAL_MISTAKES:
            return 2
        if hints_used:
            return 3
        # Unsure-right maps to Good (3), NOT Easy (4): the confidence weighter
        # already applies the x1.2 well-calibrated interval bonus for
        # correct+conf<=2 (confidence_weighter.py), so rating it Easy as well
        # would compound the same signal twice. Confident-right also stays
        # Good — don't over-space possible pattern recognition. The KP-level
        # _kp_rating mirrors this mapping; the two layers must agree, since
        # they grade the identical (correctness, confidence) event.
        return 3
    return 2


def _confident_wrong(result: str, confidence_reported: float | None) -> bool:
    return result == "incorrect" and confidence_reported is not None and confidence_reported >= 4


def _two_question_mastery_satisfied(
    db: sqlite3.Connection, topic_id: int, current_result: str
) -> bool:
    """Return True if THIS attempt (counting the in-flight current_result)
    plus prior question_attempts for this topic constitute ≥2 corrects
    spaced ≥24h apart.

    Called from update_mastery_score, which runs BEFORE the row is inserted
    into question_attempts — so we account for the current attempt manually.
    """
    rows = db.execute(
        """SELECT date FROM question_attempts
           WHERE topic_id=? AND result='correct'
           ORDER BY date""",
        (topic_id,),
    ).fetchall()
    dates = [r["date"] for r in rows]
    if current_result == "correct":
        dates.append(now())
    if len(dates) < 2:
        return False
    try:
        from datetime import datetime
        d1 = datetime.fromisoformat(dates[0].replace("Z", "+00:00"))
        d2 = datetime.fromisoformat(dates[-1].replace("Z", "+00:00"))
        return (d2 - d1).total_seconds() >= 24 * 3600
    except Exception:
        return False


def update_mastery_score(
    topic_id: int,
    result: str,
    mistake_type: str = "other",
    hints_used: int = 0,
    confidence_reported: float | None = None,
) -> float:
    # Normalize/validate result HERE, before any dict lookup. The MCP path
    # accepts arbitrary strings; "Correct" (capitalized) previously sailed past
    # _result_to_fsrs_rating (which tolerates unknowns) and then crashed the
    # counters-update dict lookup with a bare KeyError mid-transaction.
    result = (result or "").strip().lower()
    if result not in ("correct", "partial", "incorrect"):
        raise ValueError(
            f"invalid result {result!r}: must be 'correct', 'partial' or 'incorrect'"
        )
    if _confident_wrong(result, confidence_reported):
        mistake_type = "overconfident_wrong"
    rating = _result_to_fsrs_rating(result, mistake_type, hints_used, confidence_reported)
    with conn() as db:
        row = db.execute("SELECT * FROM topics WHERE topic_id=?", (topic_id,)).fetchone()
        prior = fsrs_deserialize(row["fsrs_state"] if row and "fsrs_state" in row.keys() else None)
        # confidence_reported is ALREADY on the 1-5 scale everywhere in this
        # codebase: mcp_endpoints.submit_answer clamps to 1..5 before log_attempt,
        # and _result_to_fsrs_rating/_confident_wrong in this very function use
        # raw thresholds of <=2 / >=4. The old `round(conf * 5)` here assumed
        # 0-1 input, so every real value (1-5) clamped to 5 — the interval
        # weighter saw maximum confidence on every answer: the x0.7 overconfident
        # penalty fired on ALL wrong answers and the x1.2 well-calibrated bonus
        # was unreachable. Clamp only; do not rescale.
        conf_1_to_5 = None
        if confidence_reported is not None:
            conf_1_to_5 = max(1, min(5, round(confidence_reported)))
        new_state, _next_due = fsrs_review(prior, rating=rating, confidence_reported=conf_1_to_5)
        mastery = fsrs_mastery_proxy(new_state)
        status = status_for_mastery(mastery)
        # Two-question mastery rule: even if FSRS proxy would say "maintenance",
        # require 2 corrects ≥24h apart before we let a topic claim that
        # status. Otherwise demote to 'learning' so the topic stays in active
        # rotation. This makes "mastered" mean genuine retention.
        demoted_pending_respacing = False
        if status == "maintenance" and not _two_question_mastery_satisfied(db, topic_id, result):
            status = "learning"
            demoted_pending_respacing = True
        if result == "incorrect" and mastery < 0.4:
            review_date = _study_today().isoformat()
        else:
            review_date = next_review_date_from_state(new_state)
            # The demotion's stated purpose is keeping the topic in active
            # rotation, but both due queues filter on next_review_date, not
            # status — so a demotion whose FSRS date is 60+ days out was purely
            # cosmetic (one lucky 'Easy' pushed the topic months away anyway).
            # Cap the interval so the confirming 24h-spaced second pass can
            # actually happen soon.
            if demoted_pending_respacing:
                cap = (_study_today() + timedelta(days=3)).isoformat()
                review_date = min(review_date, cap)
        fields = {
            "correct": "times_correct=times_correct+1, last_correct=?",
            "partial": "times_partial=times_partial+1, last_partial=?",
            "incorrect": "times_incorrect=times_incorrect+1, last_incorrect=?",
        }[result]
        db.execute(
            f"""UPDATE topics SET mastery_score=?, status=?, times_seen=times_seen+1, last_seen=?,
            {fields}, next_review_date=?, forgetting_risk=?, fsrs_state=?, updated_at=? WHERE topic_id=?""",
            (
                mastery,
                status,
                now(),
                now(),
                review_date,
                1.0 - mastery,
                fsrs_serialize(new_state),
                now(),
                topic_id,
            ),
        )
        return mastery


def log_attempt(
    session_id: str,
    topic: str,
    subtopic: str,
    question: str,
    user_answer: str,
    ideal_answer: str,
    result: str,
    mistake_type: str = "other",
    difficulty: str = "medium",
    hints_used: int = 0,
    confidence_reported: float | None = None,
    retrieval_sources: str = "",
    source_citations: str = "",
    notes: str = "",
    library: str = "",
    training_phase: str = "",
    bloom_level: str = "",
    teach_back_quality: float | None = None,
    transfer_success: bool = False,
    user_answer_verbatim: str = "",
    tutor_response: str = "",
    grounded_in: str = "",
    graded_as_exposure: bool = False,
) -> int:
    # These two columns existed and were never written. submit_answer accepted
    # both from the tutor, used them transiently to pick the next strategy, and
    # dropped them here — so compute_mastery_vector, which reads them back out
    # of this table, saw 0.0 forever. mechanism_quality and transfer_auc were
    # therefore pinned at zero for every topic, and since the mastery gate
    # requires mechanism_quality > 0, mastery was unreachable by construction:
    # topics sitting at 100% accuracy still reported mastery_achieved = 0.
    topic_id = get_or_create_topic(topic, subtopic, library=library, training_phase=training_phase)
    if _confident_wrong(result, confidence_reported):
        mistake_type = "overconfident_wrong"
    update_mastery_score(topic_id, result, mistake_type, hints_used, confidence_reported)
    with conn() as db:
        cur = db.execute(
            """INSERT INTO question_attempts(date, session_id, topic_id, library, training_phase, topic, subtopic, question, user_answer, ideal_answer,
            result, mistake_type, difficulty, hints_used, confidence_reported, retrieval_sources, source_citations, notes, bloom_level,
            teach_back_quality, transfer_success, user_answer_verbatim, tutor_response,
            grounded_in, graded_as_exposure)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                now(),
                session_id,
                topic_id,
                library,
                training_phase,
                topic,
                subtopic,
                question,
                user_answer,
                ideal_answer,
                result,
                mistake_type,
                difficulty,
                hints_used,
                confidence_reported,
                retrieval_sources,
                source_citations or retrieval_sources,
                notes,
                (bloom_level or "").strip().lower(),
                # NULL, not 0.0, when the caller said nothing: "not assessed"
                # and "explained the mechanism badly" are different facts, and
                # storing 0.0 for the first would drag the mechanism average
                # down for every question that simply never asked for one.
                (None if teach_back_quality is None
                 else max(0.0, min(1.0, float(teach_back_quality)))),
                1 if transfer_success else 0,
                (user_answer_verbatim or "")[:4000],
                (tutor_response or "")[:8000],
                (grounded_in or "")[:500],
                1 if graded_as_exposure else 0,
            ),
        )
        return int(cur.lastrowid)


# Document-structure artifacts that ingest turned into "topics". "Disclaimer"
# reached the due queue with five subtopics, all of them the Intern Notes p.2
# boilerplate, and was offered as study material. These are excluded by NAME
# rather than by "never answered", because a genuinely new clinical topic
# (Consults, Respiratory physiology) also has no attempts yet and must stay.
_NON_TOPICS = (
    "disclaimer", "table of contents", "contents", "index", "references",
    "bibliography", "acknowledgments", "acknowledgements", "preface",
    "foreword", "copyright", "about the authors", "appendix", "abbreviations",
    "introduction", "title page", "colophon",
    # Named clinical-sounding topics whose actual source content is
    # administrative/logistical, not testable clinical reasoning. Verified by
    # checking what a bare-name retrieval query for EACH one actually returns
    # before excluding it, precisely so this stays evidence-based and does not
    # sweep in real clinical topics that just happen to share a category
    # (Shock, Respiratory physiology, IV anesthetics, and Monitoring all
    # checked out as genuine clinical content and are NOT excluded).
    #
    # "Consults" -> MGH Housestaff Manual "Calling Consults": "TIPS FOR
    #   CALLING CONSULTS: To do BEFORE you call: place order in Epic...".
    #   Served three times in one session, answered zero — the user named the
    #   reason directly: "it's just a checklist, not clinical knowledge."
    # "Cross-cover pages" -> pager numbers and who-to-call logistics
    #   ("page MGH needlestick consultant, pager #36222"), same defect.
    "consults", "cross-cover pages",
)


def get_due_reviews(limit: int = 20) -> list[dict[str, Any]]:
    initialize_database()
    today = _study_today()
    with conn() as db:
        # Exclude topics that are now tracked at the fact (knowledge_point) level —
        # their review lives in the knowledge-point queue (get_due_knowledge_points),
        # so surfacing the old topic-level card too would double-count and produce the
        # "stale card that never clears" problem. Also skip empty subtopic-only rows.
        # `topic NOT LIKE 'unit:%'`: those rows are voice-session bookkeeping
        # (_mark_unit_served), created with default mastery 0.25 / risk 1.0 and
        # never rescheduled — without the filter they become permanently-due
        # phantom "topics" that outrank every real review and get served to the
        # tutor as literal retrieval queries like 'unit:ch05-...'.
        # `topic != ''`: get_or_create_topic accepts a blank name, and a blank
        # row otherwise surfaces as a due review with an empty retrieval query.
        # Over-fetch, because the dedupe below collapses many rows per topic and
        # we still want `limit` distinct topics back.
        # DUENESS IS DECIDED BY THE PARENT ROW, not by "any row of this topic".
        #
        # The earlier fix made the parent the schedule REPRESENTATIVE, but a
        # topic still qualified as due when any of its rows was overdue. When
        # the parent was NOT due, it was absent from the candidate set entirely
        # and a stale legacy subtopic row represented the topic instead —
        # "Electrolytes" surfaced as 55 days overdue while its parent was
        # scheduled three days in the FUTURE and it had been answered five
        # times that same day. The contradiction check caught it.
        #
        # A topic with no parent row at all (legacy data) still qualifies on
        # its subtopic rows, so nothing becomes permanently unreachable.
        rows = db.execute(
            """SELECT * FROM topics
               WHERE topic IN (
                     SELECT topic FROM topics
                      WHERE (subtopic = '' OR subtopic IS NULL)
                        AND (next_review_date IS NULL OR next_review_date <= ?)
                     UNION
                     SELECT topic FROM topics
                      GROUP BY topic
                      HAVING SUM(CASE WHEN subtopic = '' OR subtopic IS NULL
                                      THEN 1 ELSE 0 END) = 0
                        AND MIN(COALESCE(next_review_date, '0000')) <= ?
                 )
                 AND topic NOT IN (SELECT DISTINCT topic FROM knowledge_points)
                 AND topic NOT LIKE 'unit:%'
                 AND topic != ''
                 AND lower(topic) NOT IN ({placeholders})
               ORDER BY mastery_score ASC, forgetting_risk DESC LIMIT ?""".format(
                placeholders=",".join("?" * len(_NON_TOPICS))
            ),
            (today.isoformat(), today.isoformat(), *_NON_TOPICS, max(limit * 12, 200)),
        ).fetchall()

        # Collapse to ONE entry per topic NAME.
        #
        # `topics` holds a row per (topic, subtopic), so a single topic owns many
        # rows — "Electrolytes" has 15, "PE" 7. Returning them all made the tutor
        # report 32 due reviews for 12 real topics, and 112 "overdue topics" when
        # only 28 names existed. The user correctly recognised they had never
        # studied that many; the backlog was mostly the same handful of topics
        # counted repeatedly, which both misrepresents progress and wastes the
        # session on duplicates.
        #
        # The PARENT row (no subtopic) represents the topic, because that is the
        # row the topic-level FSRS schedule actually lives on — it is what
        # advances when the topic is reviewed.
        #
        # Ranking by "most overdue row" instead was wrong in a way that made the
        # queue permanently stuck. 45 of 119 rows are phantoms: fact-level notes
        # ("Wells PE score: D-dimer only useful if...") written as pseudo-topic
        # rows by the old log_missed_topic, with times_seen=0, last_seen NULL and
        # a next_review_date frozen in June. Nothing can ever review them,
        # because the tutor reviews "PE" — not "Wells PE score: ...". So they sit
        # overdue forever and drag their parent topic's figure with them: PE
        # showed 56 days overdue the day after it was studied. The user spotted
        # this ("I already did PE today"), and left alone it would mean studying
        # a topic never visibly clears it.
        #
        # Those notes are still listed under subtopics_due as useful context for
        # what the topic covers; they just no longer drive the schedule.
        best: dict[str, dict[str, Any]] = {}
        subs: dict[str, list[str]] = {}
        for r in rows:
            d = dict(r)
            nrd = d.get("next_review_date")
            try:
                d["days_overdue"] = max(0, (today - datetime.fromisoformat(nrd).date()).days) if nrd else 0
            except Exception:
                d["days_overdue"] = 0
            name = d.get("topic") or ""
            sub = (d.get("subtopic") or "").strip()
            if sub:
                subs.setdefault(name, [])
                if sub not in subs[name]:
                    subs[name].append(sub)
            prior = best.get(name)
            if prior is None:
                best[name] = d
                continue
            prior_is_parent = not (prior.get("subtopic") or "").strip()
            this_is_parent = not sub
            if this_is_parent and not prior_is_parent:
                best[name] = d                      # parent always wins
            elif this_is_parent == prior_is_parent and d["days_overdue"] > prior["days_overdue"]:
                best[name] = d                      # tie-break within the same kind
        for name, d in best.items():
            d["subtopics_due"] = subs.get(name, [])

        result = sorted(
            best.values(),
            key=lambda d: (-d["days_overdue"], d.get("mastery_score") or 0.0),
        )
        for d in result:
            d["subtopic_count"] = len(d.get("subtopics_due", []))
        return result[:limit]


def _library_for_phase(phase: str) -> str:
    return {
        "intern_year": INTERN_LIBRARY,
        "ICU": ICU_LIBRARY,
        "anesthesia_transition": ANESTHESIA_LIBRARY,
        "anesthesia_boards": ANESTHESIA_LIBRARY,
    }.get(phase, INTERN_LIBRARY)


def _new_fact_targets_for_phase(phase: str, basics_context: bool) -> list[dict[str, Any]]:
    if basics_context or phase == "anesthesia_boards":
        return get_ca1_fact_catalog()
    if phase == "ICU":
        return get_icu_fact_catalog()
    if phase == "anesthesia_transition":
        targets = get_icu_fact_catalog(4)
        targets.extend(get_ca1_fact_catalog(3)[:100])
        return targets
    return get_intern_fact_catalog()


def generate_session_plan(
    duration_minutes: int = 20,
    mode: str = "default",
    focus_topic: str | None = None,
    training_phase: str | None = None,
) -> dict[str, Any]:
    initialize_database()
    session_id = str(uuid.uuid4())
    phase = training_phase_for_mode(mode, focus_topic, training_phase)
    library = _library_for_phase(phase)
    due = [r for r in get_due_reviews(30) if not r.get("library") or r.get("library") == library][:10]
    plan: list[dict[str, str]] = []
    basics_context = _is_basics_context(mode, focus_topic)
    if focus_topic:
        plan.append({"topic": focus_topic, "library": library, "training_phase": phase, "reason": "requested focus"})
    for r in due[:3]:
        plan.append(
            {
                "topic": r["topic"],
                "subtopic": r.get("subtopic", ""),
                "library": r.get("library") or library,
                "training_phase": r.get("training_phase") or phase,
                "reason": f"due review; mastery {r['mastery_score']:.2f}",
            }
        )
    primary_facts = _new_fact_targets_for_phase(phase, basics_context)
    supporting_facts = get_supporting_fact_catalog() if basics_context or phase == "anesthesia_boards" else []
    with conn() as db:
        seen_targets = {
            (row["topic"], row["subtopic"])
            for row in db.execute("SELECT topic, subtopic FROM topics WHERE times_seen > 0 AND mastery_score >= 0.6").fetchall()
        }
    if primary_facts:
        primary_remaining = 0
        for target in primary_facts:
            if len(plan) >= 10:
                break
            key = (target["topic"], target["subtopic"])
            if key in seen_targets or key in {(p["topic"], p.get("subtopic", "")) for p in plan}:
                continue
            primary_remaining += 1
            plan.append(
                {
                    "topic": target["topic"],
                    "subtopic": target["subtopic"],
                    "fact": target["fact"],
                    "page": str(target["page"]),
                    "target_id": target["target_id"],
                    "source": target["source"],
                    "library": target.get("library", library),
                    "training_phase": target.get("training_phase", phase),
                    "reason": (
                        "uncovered granular Stanford CA-1 fact target"
                        if target.get("source") == "Stanford CA-1"
                        else f"uncovered granular {target.get('source', 'source')} fact target"
                    ),
                }
            )
            get_or_create_topic(
                target["topic"],
                target["subtopic"],
                target.get("source", ""),
                target.get("library", library),
                target.get("training_phase", phase),
            )
        supporting_slots = 1 if primary_remaining and phase == "anesthesia_boards" else 2
        for target in supporting_facts:
            if supporting_slots <= 0 or len(plan) >= 12:
                break
            key = (target["topic"], target["subtopic"])
            if key in seen_targets or key in {(p["topic"], p.get("subtopic", "")) for p in plan}:
                continue
            plan.append(
                {
                    "topic": target["topic"],
                    "subtopic": target["subtopic"],
                    "fact": target["fact"],
                    "page": str(target["page"]),
                    "target_id": target["target_id"],
                    "source": target["source"],
                    "library": target.get("library", ""),
                    "training_phase": target.get("training_phase", ""),
                    "reason": "supporting textbook color after Stanford CA-1 priority",
                }
            )
            get_or_create_topic(target["topic"], target["subtopic"], target["source"], target.get("library", ""), target.get("training_phase", ""))
            supporting_slots -= 1
    else:
        defaults = (
            ["Hyperkalemia", "Afib with RVR", "Sepsis", "Hypoxemia", "AKI"]
            if phase == "intern_year"
            else ["Shock", "Mechanical ventilation", "ARDS", "Vasopressors"]
            if phase == "ICU"
            else ["Airway", "Respiratory physiology", "IV anesthetics", "Malignant hyperthermia"]
        )
        for topic in defaults:
            if len(plan) >= 5:
                break
            if topic not in [p["topic"] for p in plan]:
                plan.append({"topic": topic, "library": library, "training_phase": phase, "reason": "new or maintenance topic"})
                get_or_create_topic(topic, library=library, training_phase=phase)
    rationale = (
        "BASICS mode: keep cycling through due weak targets plus granular Stanford CA-1 fact targets until the CA-1 guide is covered at fact level; Morgan/Mikhail and Miller remain lower-priority supporting color until then."
        if basics_context
        else (
            "Default intern-year session: 50% due weak topics, 25% new intern-note fact targets, 15% unstable material, 10% maintenance; ICU/anesthesia crossover is included only when relevant."
            if phase == "intern_year"
            else "50% due weak topics, 25% new material, 15% unstable material, 10% maintenance checks."
        )
    )
    with conn() as db:
        db.execute(
            "INSERT INTO sessions(session_id, date, requested_mode, mode, training_phase, duration_minutes, selected_topics, rationale, created_at) VALUES(?,?,?,?,?,?,?,?,?)",
            (session_id, now(), mode, mode, phase, duration_minutes, json.dumps(plan), rationale, now()),
        )
    return {"session_id": session_id, "training_phase": phase, "plan": plan, "rationale": rationale}


def select_next_question(topic: str | None = None) -> str:
    topic = topic or (get_due_reviews(1)[0]["topic"] if get_due_reviews(1) else "Airway")
    return f"What is the first thing you worry about with {topic}, and what would you do next?"


# ---------------------------------------------------------------------------
# Illness scripts + confusable pairs (clinical-reasoning structure)
# ---------------------------------------------------------------------------

def upsert_illness_script(topic: str, enabling_conditions: str = "", pathophysiology: str = "",
                          time_course: str = "", key_features: str = "",
                          consequence_if_missed: str = "", discipline: str = "",
                          source: str = "") -> None:
    topic = (topic or "").strip()
    if not topic:
        return
    initialize_database()
    ts = now()
    with conn() as db:
        db.execute(
            """INSERT INTO illness_scripts(topic, enabling_conditions, pathophysiology,
                   time_course, key_features, consequence_if_missed, discipline, source,
                   created_at, updated_at)
               VALUES(?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(topic) DO UPDATE SET
                   enabling_conditions=excluded.enabling_conditions,
                   pathophysiology=excluded.pathophysiology,
                   time_course=excluded.time_course,
                   key_features=excluded.key_features,
                   consequence_if_missed=excluded.consequence_if_missed,
                   discipline=excluded.discipline,
                   source=excluded.source,
                   updated_at=excluded.updated_at""",
            (topic, enabling_conditions, pathophysiology, time_course, key_features,
             consequence_if_missed, discipline, source, ts, ts),
        )


def get_illness_script(topic: str) -> Optional[dict[str, Any]]:
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT * FROM illness_scripts WHERE topic=?", ((topic or "").strip(),)).fetchone()
    return dict(row) if row else None


def add_confusable_pair(topic_a: str, topic_b: str, discriminator: str = "") -> None:
    a, b = (topic_a or "").strip(), (topic_b or "").strip()
    if not a or not b or a == b:
        return
    # canonical order so (A,B) and (B,A) dedup
    if a > b:
        a, b = b, a
    initialize_database()
    with conn() as db:
        db.execute(
            """INSERT INTO confusable_pairs(topic_a, topic_b, discriminator, created_at)
               VALUES(?,?,?,?)
               ON CONFLICT(topic_a, topic_b) DO UPDATE SET
                   discriminator=CASE WHEN excluded.discriminator != '' THEN excluded.discriminator
                                      ELSE confusable_pairs.discriminator END""",
            (a, b, discriminator, now()),
        )


def get_confusable_pairs(topic: str) -> list[dict[str, Any]]:
    """All entities a topic is commonly confused with, + the discriminating feature."""
    t = (topic or "").strip()
    initialize_database()
    with conn() as db:
        rows = db.execute(
            "SELECT topic_a, topic_b, discriminator FROM confusable_pairs WHERE topic_a=? OR topic_b=?",
            (t, t),
        ).fetchall()
    out = []
    for r in rows:
        other = r["topic_b"] if r["topic_a"] == t else r["topic_a"]
        out.append({"topic": t, "confused_with": other, "discriminator": r["discriminator"] or ""})
    return out


def _override_fsrs_stability(db, topic_id: int, stability: float) -> None:
    """Force a topic's FSRS stability to match a manual mastered/weak override.

    mark_topic_mastered/weak used to write mastery_score/status/next_review_date
    but leave fsrs_state untouched — and update_mastery_score recomputes mastery
    purely from FSRS state on the next attempt, so the override evaporated: a
    topic marked weak with stability 90 snapped back to 'strong' after one
    correct answer, and the manual flag had zero effect on scheduling."""
    row = db.execute("SELECT fsrs_state FROM topics WHERE topic_id=?", (topic_id,)).fetchone()
    state = fsrs_deserialize(row["fsrs_state"] if row else None)
    state["stability"] = stability
    db.execute("UPDATE topics SET fsrs_state=? WHERE topic_id=?",
               (fsrs_serialize(state), topic_id))


def mark_topic_mastered(topic: str, subtopic: str = "") -> None:
    topic_id = get_or_create_topic(topic, subtopic)
    with conn() as db:
        db.execute("UPDATE topics SET mastery_score=.92, status='maintenance', next_review_date=?, updated_at=? WHERE topic_id=?", (next_review_date(.92), now(), topic_id))
        _override_fsrs_stability(db, topic_id, 90.0)
    # Demonstrated mastery closes the open granular gaps on this topic.
    resolve_knowledge_gaps(topic)


def mark_topic_weak(topic: str, subtopic: str = "") -> None:
    topic_id = get_or_create_topic(topic, subtopic)
    with conn() as db:
        db.execute("UPDATE topics SET mastery_score=.2, status='weak', next_review_date=?, updated_at=? WHERE topic_id=?", (next_review_date(.2), now(), topic_id))
        _override_fsrs_stability(db, topic_id, 1.0)


# ---------------------------------------------------------------------------
# Atomic knowledge points — granular fact tracking with per-point confidence
# and an independent spaced-repetition schedule.
# ---------------------------------------------------------------------------

# Knowledge points are scheduled by the SAME per-item FSRS-4 engine used for topics
# (per-item stability/difficulty/retrievability) — ~20-30% fewer reviews than a fixed
# ladder for the same retention. A learner's (is_correct, confidence) maps to an FSRS
# rating 1-4. _KP_LADDER retained only for the legacy resolve helper's far-future date.
_KP_LADDER = [1, 3, 7, 16, 35, 75, 150]


def _study_today():
    """The user's study day, in THEIR timezone — never UTC.

    All scheduling used _study_today(). The user is in
    Eastern time, so from 8pm EDT the "day" had already flipped: facts
    answered in an afternoon session were scheduled "+1 day" from tomorrow's
    UTC date, and the evening's due query — also running on the new UTC day —
    served cards back the same evening. The user noticed as "I'm reviewing the
    same cards multiple times a day". A spaced-repetition day is a human day;
    the machine runs in the user's local timezone, which is authoritative here.
    """
    return datetime.now().astimezone().date()


def _kp_rating(is_correct: bool, confidence: Optional[int]) -> int:
    """Map (correctness, 1-5 confidence) to an FSRS rating: 1=again, 3=good.

    Correct answers rate Good regardless of stated confidence — confidence is
    handled ONCE, by apply_confidence_weight_to_interval inside fsrs_review
    (x1.2 for unsure-right, x0.7 for confident-wrong). The old mapping here
    (unsure-right -> 2=hard, confident-right -> 4=easy) was the exact OPPOSITE
    of the topic layer's for the same event, and rating unsure-right as 'hard'
    made fsrs_review classify a genuinely correct answer as wrong
    (is_correct = rating in (3,4)), so the well-calibrated bonus was
    unreachable at the KP level. Mirrors _result_to_fsrs_rating."""
    if is_correct == "partial":
        # FSRS "Hard": a success with a smaller stability gain and a difficulty
        # bump — NOT a lapse. Grading partials as full misses (the old binary
        # behaviour) treated "named lactulose, wrong mechanism" identically to
        # "don't know this one at all", which resets the streak, increments
        # lapses, and collapses the interval to a day. In one 30-question
        # session 20 answers were recorded incorrect and most were substantially
        # right; that both buries the user in false repeats and destroys the
        # signal that says which facts are actually fragile.
        return 2
    if not is_correct:
        return 1
    return 3


def _kp_calibration(avg_conf: Optional[float], accuracy: Optional[float]) -> str:
    """Label a point's confidence calibration from its history."""
    if avg_conf is None or accuracy is None:
        return "unknown"
    if avg_conf >= 3.5 and accuracy < 0.5:
        return "overconfident"
    if avg_conf <= 2.5 and accuracy >= 0.75:
        return "underconfident"
    return "calibrated"


def record_knowledge_point(
    topic: str,
    point: str,
    is_correct,
    confidence: Optional[int] = None,
    mistake_type: str = "other",
    triage: bool = False,
    evidence: str = "",
    source: str = "",
) -> Optional[dict[str, Any]]:
    """Record one attempt on an atomic knowledge point: updates correctness history,
    per-point confidence, mastery status, and the independent SRS schedule. Deduped
    on (topic, point). No-op (returns None) if topic or point is blank.

    `is_correct` is True / False / the string "partial". Partial means the user
    had the substance but missed a component — it earns FSRS "Hard" (a smaller
    stability gain, not a lapse) and holds the point at `learning` rather than
    knocking it back to `weak`.

    `evidence` is the user's own words that demonstrate the fact. It is stored,
    not merely validated, so that a repeat can always answer "why am I being
    asked this again?" — the question the maintainer has had to chase by
    diffing transcripts by hand. A fact marked known with no evidence behind it
    is exactly the state that produced both failure directions: demonstrated
    knowledge going unrecorded, and unearned credit accruing from parroting."""
    topic = (topic or "").strip()
    point = (point or "").strip()
    if not topic or not point:
        return None
    initialize_database()
    ts = now()
    today = _study_today()
    conf = None
    if confidence is not None:
        try:
            conf = max(1, min(5, int(confidence)))
        except (TypeError, ValueError):
            conf = None
    with conn() as db:
        row = db.execute(
            "SELECT * FROM knowledge_points WHERE topic=? AND point=?", (topic, point)
        ).fetchone()
        if row is None:
            # No EXACT match. Before creating a new row, check whether this is
            # the same fact under different phrasing — the derived-knowledge-
            # point fallback keys text off the QUESTION asked, and two
            # different questions routinely probe the same fact ("STEMI:
            # oxygen only if SpO2 <90%" from one session, "SpO2 less than 90"
            # from another). This path (submit_answer's normal recording) is
            # what creates the vast majority of knowledge points, and until
            # now the fuzzy matcher only ran inside log_tangent — a sweep
            # found 2 such duplicates had already formed from ordinary graded
            # answers, not tangents.
            #
            # Confident match -> redirect the write onto that row instead of
            # forking a second history for the same fact. UNCERTAIN is
            # deliberately NOT blocked here (unlike log_tangent): this path
            # must always succeed, since a graded answer can never be left
            # half-recorded waiting on a judgement call. Ambiguous cases
            # create a new point; the periodic merge script (which asks a
            # human before merging anything gray) is the backstop.
            #
            # O(N) against all existing points per call — fine at today's
            # scale (~180), worth revisiting if the catalog grows to
            # thousands of studied points.
            try:
                from .fact_matcher import find_matching_point
                candidates = db.execute(
                    "SELECT id, topic, point, status, times_seen FROM knowledge_points"
                ).fetchall()
                match, _unc = find_matching_point(topic, point, candidates)
                if match:
                    row = db.execute(
                        "SELECT * FROM knowledge_points WHERE topic=? AND point=?",
                        (match["topic"], match["point"])).fetchone()
                    topic, point = match["topic"], match["point"]
            except Exception:
                pass  # dedupe is best-effort; never block a real answer on it
        is_partial = (is_correct == "partial")
        full_correct = bool(is_correct) and not is_partial
        prev_consec = row["consecutive_correct"] if row else 0
        # A partial holds the streak rather than advancing or resetting it:
        # the user did not demonstrate mastery, but they did not fail either.
        consec = (prev_consec + 1) if full_correct else (prev_consec if is_partial else 0)
        times_seen = (row["times_seen"] if row else 0) + 1
        times_correct = (row["times_correct"] if row else 0) + (1 if full_correct else 0)
        confidence_sum = (row["confidence_sum"] if row else 0) + (conf or 0)
        confidence_n = (row["confidence_n"] if row else 0) + (1 if conf is not None else 0)
        # Advance this point's own FSRS-4 state.
        try:
            prior_state = fsrs_deserialize(row["fsrs_state"]) if (row and row["fsrs_state"]) else fsrs_init()
            new_state, next_due_iso = fsrs_review(
                prior_state, rating=_kp_rating(is_correct, conf),
                confidence_reported=conf,
            )
            fsrs_state_json = fsrs_serialize(new_state)
            nrd = next_due_iso[:10]
            try:
                interval = max(0.0, (datetime.fromisoformat(nrd).date() - today).days)
                # Load smoothing: ±10% deterministic jitter on week-plus
                # intervals. Facts cleared in one sitting otherwise re-arrive
                # in one sitting — a bulk-cleared backlog reconverged into a
                # single-day wave that read as "2-3 hours of reviews today".
                # Seeded by the fact text so the shift is stable per fact
                # (no retest churn), and centred so it averages out. A ±10%
                # shift is far inside FSRS's tolerance — the same fact
                # reviewed a day early or late earns almost identical
                # stability, so this costs nothing in retention.
                if interval >= 7:
                    import hashlib
                    h = int(hashlib.sha1(point.encode()).hexdigest()[:8], 16)
                    shift = (h % 21 - 10) / 100.0        # -0.10 .. +0.10
                    interval = max(1.0, interval * (1 + shift))
                    nrd = (today + timedelta(days=int(round(interval)))).isoformat()
            except Exception:
                interval = 1.0
        except Exception:
            # Fallback: never let a scheduling error drop the attempt.
            fsrs_state_json = row["fsrs_state"] if row else None
            interval = 0.0 if not is_correct else 1.0
            nrd = (today + timedelta(days=int(round(interval)))).isoformat()
        if is_partial:
            status = "learning"
        elif not is_correct:
            status = "weak"
        elif triage and (confidence or 0) >= 4 and consec >= 1:
            # Gap-triage mode: ONE confident correct classifies the fact as
            # known and parks it on a long verification interval (it resurfaces
            # when due — mastered-but-due points are served). Without this, a
            # fact the student already knew cold still cost 2-3 touches to exit
            # the queue, which makes triaging a 6,200-fact catalog ~3x slower
            # than it needs to be. A hesitant correct (conf <= 3) stays in the
            # normal ladder — hesitation IS information about fragility.
            status = "mastered"
            try:
                nrd = (today + timedelta(days=60)).isoformat()
                interval = 60.0
            except Exception:
                pass
        elif full_correct and consec >= 2:
            status = "mastered"
        else:
            status = "learning"
        created = row["created_at"] if row else ts
        # This call IS a presentation — the fact was put to the user and
        # answered. Stamped once and never overwritten, so it stays the honest
        # answer to "has he actually seen this?" (see the ghost-fact note on
        # the column definition). COALESCE keeps the first presentation.
        first_presented = (
            (row["first_presented_at"] if row and "first_presented_at" in row.keys() else None)
            or ts)
        # Keep the most recent non-empty evidence: a later attempt that
        # demonstrates the fact should replace an earlier blank, but a blank
        # must never erase evidence already earned.
        prior_ev = (row["evidence"] if row and "evidence" in row.keys() else "") or ""
        ev = (evidence or "").strip() or prior_ev
        # Provenance is sticky: once a fact knows which book and page it came
        # from, a later answer that omits the citation must not erase it.
        prior_src = (row["source"] if row and "source" in row.keys() else "") or ""
        src_val = prior_src or (source or "").strip()
        db.execute(
            """INSERT INTO knowledge_points
                   (topic, point, status, times_seen, times_correct, consecutive_correct,
                    last_correct, last_confidence, confidence_sum, confidence_n,
                    mistake_type, interval_days, fsrs_state, next_review_date, created_at, updated_at,
                    evidence, first_presented_at, source)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(topic, point) DO UPDATE SET
                   status=excluded.status,
                   times_seen=excluded.times_seen,
                   times_correct=excluded.times_correct,
                   consecutive_correct=excluded.consecutive_correct,
                   last_correct=excluded.last_correct,
                   last_confidence=excluded.last_confidence,
                   confidence_sum=excluded.confidence_sum,
                   confidence_n=excluded.confidence_n,
                   mistake_type=excluded.mistake_type,
                   interval_days=excluded.interval_days,
                   fsrs_state=excluded.fsrs_state,
                   next_review_date=excluded.next_review_date,
                   updated_at=excluded.updated_at,
                   evidence=excluded.evidence,
                   first_presented_at=COALESCE(knowledge_points.first_presented_at,
                                               excluded.first_presented_at),
                   source=CASE WHEN COALESCE(knowledge_points.source,'')=''
                               THEN excluded.source ELSE knowledge_points.source END""",
            (topic, point, status, times_seen, times_correct, consec,
             1 if is_correct else 0, conf, confidence_sum, confidence_n,
             (mistake_type or "other").strip() or "other", interval, fsrs_state_json, nrd, created, ts,
             ev, first_presented, src_val),
        )
    return {"topic": topic, "point": point, "status": status,
            "consecutive_correct": consec, "interval_days": interval,
            "next_review_date": nrd}


def _kp_row_to_dict(r: sqlite3.Row, today=None) -> dict[str, Any]:
    d = dict(r)
    avg_conf = (d["confidence_sum"] / d["confidence_n"]) if d.get("confidence_n") else None
    acc = (d["times_correct"] / d["times_seen"]) if d.get("times_seen") else None
    d["avg_confidence"] = round(avg_conf, 2) if avg_conf is not None else None
    d["accuracy"] = round(acc, 2) if acc is not None else None
    d["calibration"] = _kp_calibration(avg_conf, acc)
    # Transfer scheduling: after 3+ consecutive corrects, straight recall stops
    # discriminating functional from inert knowledge — the tutor should reframe
    # this point as a NOVEL presentation (different patient/context) instead of
    # re-asking it verbatim. Computed, not stored, so no migration.
    d["serve_as_transfer"] = bool(
        (d.get("consecutive_correct") or 0) >= 3 and d.get("status") != "weak"
    )
    if today is not None:
        nrd = d.get("next_review_date")
        try:
            d["days_overdue"] = max(0, (today - datetime.fromisoformat(nrd).date()).days) if nrd else 0
        except Exception:
            d["days_overdue"] = 0
    return d


def get_knowledge_points(
    topic: Optional[str] = None,
    status: str = "",
    due_only: bool = False,
    limit: int = 200,
) -> list[dict[str, Any]]:
    """Return atomic knowledge points (with calibration + overdue info).

    Filter by topic, status ('weak'|'learning'|'mastered', or '' for all not-mastered
    by default-friendly callers should pass explicitly), and/or due_only (next_review
    <= today). Weakest/most-overdue first."""
    initialize_database()
    today = _study_today()
    with conn() as db:
        q = "SELECT * FROM knowledge_points"
        clauses, params = [], []
        if topic:
            clauses.append("topic = ?")
            params.append(topic)
        if status and status != "all":
            clauses.append("status = ?")
            params.append(status)
        if due_only:
            clauses.append("(next_review_date IS NULL OR next_review_date <= ?)")
            params.append(today.isoformat())
        if clauses:
            q += " WHERE " + " AND ".join(clauses)
        # weak first, then most overdue, then least-mastered
        q += (" ORDER BY CASE status WHEN 'weak' THEN 0 WHEN 'learning' THEN 1 ELSE 2 END,"
              " next_review_date ASC, times_correct ASC LIMIT ?")
        params.append(limit)
        return [_kp_row_to_dict(r, today) for r in db.execute(q, params).fetchall()]


def get_due_knowledge_points(limit: int = 25, car: bool = False) -> list[dict[str, Any]]:
    """Knowledge points due for review on their own schedule (not yet mastered-and-future).

    When car=True, the returned list is filtered to 'hearable' points only:
      len(point) <= 120 AND (point.count(',') + point.count(';')) < 3.
    This keeps car-mode sessions free of long/enumeration-heavy facts that need reading.
    """
    initialize_database()
    today = _study_today()
    # The car filter runs in Python, so the SQL LIMIT must not be the caller's
    # limit when car=True: taking the top N and *then* discarding the long ones
    # returns fewer than N — and returns ZERO whenever the N most-overdue points
    # all happen to be long, which is exactly what happened in practice
    # (limit=5 -> 0 results while 65 car-safe points were due). Over-fetch, then
    # filter, then truncate.
    fetch_limit = max(limit * 20, 200) if car else limit
    with conn() as db:
        # Mastered points MUST still surface once their FSRS date passes —
        # that overdue re-test is the only path by which retention gets
        # re-checked and a decayed 'mastered' can revert to 'weak'. The old
        # blanket `status != 'mastered'` retired them permanently: two corrects
        # in one evening and the fact never appeared in any queue again
        # (get_due_reviews also excludes the whole topic once it has KP rows,
        # so the topic card never came back either — a scheduling black hole).
        # Mastered points with NO date are still excluded: those are bulk
        # mark-as-mastered rows that were deliberately retired.
        #
        # `date(updated_at,'localtime') < today`: a fact touched today is DONE
        # for today, whatever its schedule says. This is the hard guard behind
        # the user's report of seeing the same cards several times a day —
        # same-day re-review adds nearly nothing to FSRS stability, so a
        # repeat costs time and teaches nothing. Tomorrow it is eligible again.
        rows = db.execute(
            # `julianday('now') - julianday(updated_at) >= 0.8` is a ROLLING
            # guard, replacing a calendar-day one. The old rule let a fact
            # missed at 8pm return at 7am the next morning — eleven hours later
            # — and the maintainer reported exactly that: "constantly reviewing
            # information I very recently just reviewed". Measured on his queue,
            # 11 of the 20 facts about to be served had been touched within the
            # last 24 hours and 8 more the day before.
            #
            # 0.8 days rather than a full 1.0 so an evening session still
            # follows a morning one on the next day without slipping a day each
            # time; the point is to stop the same-night and next-dawn repeat,
            # not to punish studying twice in one day.
            """SELECT * FROM knowledge_points
               WHERE ((next_review_date IS NOT NULL AND next_review_date <= ?)
                  OR (next_review_date IS NULL AND status != 'mastered'))
                 AND date(updated_at, 'localtime') < ?
                 AND (julianday('now') - julianday(updated_at)) >= 0.8
               ORDER BY CASE status WHEN 'weak' THEN 0 WHEN 'learning' THEN 1 ELSE 2 END,
                        next_review_date ASC
               LIMIT ?""",
            (today.isoformat(), today.isoformat(), fetch_limit),
        ).fetchall()
    results = [_kp_row_to_dict(r, today) for r in rows]
    if car:
        results = [
            p for p in results
            if len(p.get("point", "")) <= 120
            and (p.get("point", "").count(",") + p.get("point", "").count(";")) < 3
        ][:limit]
    return results


# --- Backward-compatible "gap" wrappers (a gap = a knowledge point you missed) ---

def record_knowledge_gap(topic: str, gap_note: str, mistake_type: str = "other") -> None:
    """Compat shim: logging a missed micro-fact == recording a knowledge point as
    incorrect (confidence unknown)."""
    record_knowledge_point(topic, gap_note, is_correct=False, confidence=None, mistake_type=mistake_type)


def get_knowledge_gaps(topic: Optional[str] = None, status: str = "open", limit: int = 200) -> list[dict[str, Any]]:
    """Compat shim: 'gaps' are the not-yet-mastered knowledge points. Maps the old
    'open'/'resolved' status vocabulary onto the new model."""
    if status == "resolved":
        pts = get_knowledge_points(topic=topic, status="mastered", limit=limit)
    elif status in ("open", "weak", "learning"):
        # not-mastered points
        pts = [p for p in get_knowledge_points(topic=topic, status="", limit=limit)
               if p["status"] != "mastered"]
    else:  # 'all'
        pts = get_knowledge_points(topic=topic, status="", limit=limit)
    # expose under the legacy 'gap_note'/'status' shape too
    out = []
    for p in pts:
        q = dict(p)
        q["gap_note"] = p["point"]
        q["status"] = "resolved" if p["status"] == "mastered" else "open"
        out.append(q)
    return out


def resolve_knowledge_gaps(topic: str, gap_id: Optional[int] = None) -> int:
    """Mark a topic's not-yet-mastered points as mastered (or one point by id).
    Returns count promoted."""
    topic = (topic or "").strip()
    initialize_database()
    today = _study_today()
    far = (today + timedelta(days=_KP_LADDER[-1])).isoformat()
    with conn() as db:
        if gap_id is not None:
            cur = db.execute(
                "UPDATE knowledge_points SET status='mastered', consecutive_correct=MAX(consecutive_correct,2), "
                "next_review_date=?, updated_at=? WHERE id=? AND status!='mastered'",
                (far, now(), gap_id),
            )
        elif topic:
            cur = db.execute(
                "UPDATE knowledge_points SET status='mastered', consecutive_correct=MAX(consecutive_correct,2), "
                "next_review_date=?, updated_at=? WHERE topic=? AND status!='mastered'",
                (far, now(), topic),
            )
        else:
            return 0
        return cur.rowcount or 0


def get_topic_summary(topic: str) -> dict[str, Any]:
    initialize_database()
    with conn() as db:
        row = db.execute("SELECT * FROM topics WHERE topic=? ORDER BY updated_at DESC LIMIT 1", (topic,)).fetchone()
        return dict(row) if row else {}


def get_student_dashboard() -> dict[str, Any]:
    initialize_database()
    with conn() as db:
        rows = db.execute("SELECT status, COUNT(*) n, AVG(mastery_score) avg_mastery FROM topics GROUP BY status").fetchall()
        weak = db.execute("SELECT topic, subtopic, mastery_score, next_review_date FROM topics ORDER BY mastery_score ASC LIMIT 10").fetchall()
        return {"summary": [dict(r) for r in rows], "weakest_topics": [dict(r) for r in weak]}


def get_ca1_coverage() -> dict[str, Any]:
    initialize_database()
    catalog = get_ca1_fact_catalog()
    with conn() as db:
        rows = db.execute("SELECT topic, subtopic, mastery_score, status, times_seen, next_review_date FROM topics").fetchall()
    by_target = {(row["topic"], row["subtopic"]): dict(row) for row in rows}
    targets = []
    for target in catalog:
        row = by_target.get((target["topic"], target["subtopic"]))
        targets.append(
            {
                "target_id": target["target_id"],
                "topic": target["topic"],
                "subtopic": target["subtopic"],
                "fact": target["fact"],
                "page": target["page"],
                "status": row["status"] if row else "new",
                "mastery_score": row["mastery_score"] if row else 0.0,
                "times_seen": row["times_seen"] if row else 0,
                "next_review_date": row["next_review_date"] if row else None,
                "covered": bool(row and row["times_seen"] > 0 and row["mastery_score"] >= 0.6),
            }
        )
    covered = sum(1 for item in targets if item["covered"])
    weak_or_new = [item for item in targets if not item["covered"]]
    topic_count = len({item["topic"] for item in targets})
    return {
        "source": "Stanford CA-1",
        "granularity": "fact",
        "total_topics": topic_count,
        "total_facts": len(targets),
        "covered_topics": covered,
        "remaining_topics": len(targets) - covered,
        "covered_facts": covered,
        "remaining_facts": len(targets) - covered,
        "coverage_percent": round((covered / len(targets)) * 100, 1) if targets else 0.0,
        "next_targets": weak_or_new[:10],
        "targets": targets,
    }


def _known_sources() -> list[str]:
    from .retrieval import load_json_chunks
    sources: set[str] = set()
    for row in load_json_chunks():
        meta = row.get("metadata", {})
        source = meta.get("source_name") or meta.get("book")
        if source:
            sources.add(source)
    preferred = [
        "Intern Notes / Survival Guide",
        "MGH Housestaff Manual",
        "OnlineMedEd Intern Guide",
        "Marino ICU Book",
        "Stanford CA-1",
        "Morgan & Mikhail",
        "Miller/Baby Miller",
    ]
    ordered = [source for source in preferred if source in sources]
    ordered.extend(sorted(sources - set(ordered)))
    return ordered or ["Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller"]


def get_source_coverage() -> dict[str, Any]:
    initialize_database()
    sources = _known_sources()
    with conn() as db:
        rows = db.execute("SELECT topic, subtopic, mastery_score, status, times_seen, next_review_date FROM topics").fetchall()
    by_target = {(row["topic"], row["subtopic"]): dict(row) for row in rows}
    summaries = []
    next_targets = []
    for source in sources:
        catalog = get_fact_catalog(source)
        covered = 0
        remaining_for_source = []
        for target in catalog:
            row = by_target.get((target["topic"], target["subtopic"]))
            is_covered = bool(row and row["times_seen"] > 0 and row["mastery_score"] >= 0.6)
            if is_covered:
                covered += 1
            else:
                remaining_for_source.append({**target, "status": row["status"] if row else "new", "mastery_score": row["mastery_score"] if row else 0.0})
        summaries.append(
            {
                "source": source,
                "priority": "primary" if source in {"Intern Notes / Survival Guide", "Stanford CA-1", "Marino ICU Book"} else "supporting",
                "total_facts": len(catalog),
                "covered_facts": covered,
                "remaining_facts": len(catalog) - covered,
                "coverage_percent": round((covered / len(catalog)) * 100, 1) if catalog else 0.0,
            }
        )
        next_targets.extend(remaining_for_source[:5])
    return {"granularity": "fact", "source_summaries": summaries, "next_targets": next_targets[:15]}


def export_student_model_csv(out_dir: str | Path | None = None) -> dict[str, str]:
    initialize_database()
    out = Path(out_dir or settings.log_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths = {}
    with conn() as db:
        for table in ["topics", "question_attempts", "sessions", "learned_facts"]:
            rows = db.execute(f"SELECT * FROM {table}").fetchall()
            path = out / f"{table}.csv"
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if rows:
                    writer.writerow(rows[0].keys())
                    writer.writerows([tuple(r) for r in rows])
            paths[table] = str(path)
    return paths
