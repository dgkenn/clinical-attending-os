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
                status TEXT DEFAULT 'weak',          -- 'weak' | 'learning' | 'mastered'
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
                       tier, category, is_critical_care, car_safe, added_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
                       car_safe=excluded.car_safe""",
                (
                    kp_id, topic, domain, discipline, stem,
                    answer_str,
                    rationale_str,
                    str(entry.get("bloom", "")),
                    source_json,
                    str(entry.get("confusable_with", "")),
                    tier, category, is_critical_care, car_safe, ts,
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


def get_daily_review_budget() -> int:
    """Target max reviews per day (default 200). Advisory load signal for the tutor."""
    return get_int_setting("daily_review_budget", 200)


def count_new_topics_today() -> int:
    """Distinct curriculum topics introduced (first-ever attempt) today (UTC)."""
    initialize_database()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
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
        if conf is not None and conf <= 2:
            return 4  # unsure-right: real learning, reinforce strongly
        if conf is not None and conf >= 4:
            return 3  # confident-right: don't over-space, may be pattern recognition
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
    if _confident_wrong(result, confidence_reported):
        mistake_type = "overconfident_wrong"
    rating = _result_to_fsrs_rating(result, mistake_type, hints_used, confidence_reported)
    with conn() as db:
        row = db.execute("SELECT * FROM topics WHERE topic_id=?", (topic_id,)).fetchone()
        prior = fsrs_deserialize(row["fsrs_state"] if row and "fsrs_state" in row.keys() else None)
        # Convert confidence_reported (0-1 scale) to 1-5 scale for FSRS weighting
        conf_1_to_5 = None
        if confidence_reported is not None:
            conf_1_to_5 = max(1, min(5, round(confidence_reported * 5)))
        new_state, _next_due = fsrs_review(prior, rating=rating, confidence_reported=conf_1_to_5)
        mastery = fsrs_mastery_proxy(new_state)
        status = status_for_mastery(mastery)
        # Two-question mastery rule: even if FSRS proxy would say "maintenance",
        # require 2 corrects ≥24h apart before we let a topic claim that
        # status. Otherwise demote to 'learning' so the topic stays in active
        # rotation. This makes "mastered" mean genuine retention.
        if status == "maintenance" and not _two_question_mastery_satisfied(db, topic_id, result):
            status = "learning"
        if result == "incorrect" and mastery < 0.4:
            review_date = datetime.now(timezone.utc).date().isoformat()
        else:
            review_date = next_review_date_from_state(new_state)
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
) -> int:
    topic_id = get_or_create_topic(topic, subtopic, library=library, training_phase=training_phase)
    if _confident_wrong(result, confidence_reported):
        mistake_type = "overconfident_wrong"
    update_mastery_score(topic_id, result, mistake_type, hints_used, confidence_reported)
    with conn() as db:
        cur = db.execute(
            """INSERT INTO question_attempts(date, session_id, topic_id, library, training_phase, topic, subtopic, question, user_answer, ideal_answer,
            result, mistake_type, difficulty, hints_used, confidence_reported, retrieval_sources, source_citations, notes, bloom_level)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
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
            ),
        )
        return int(cur.lastrowid)


def get_due_reviews(limit: int = 20) -> list[dict[str, Any]]:
    initialize_database()
    today = datetime.now(timezone.utc).date()
    with conn() as db:
        # Exclude topics that are now tracked at the fact (knowledge_point) level —
        # their review lives in the knowledge-point queue (get_due_knowledge_points),
        # so surfacing the old topic-level card too would double-count and produce the
        # "stale card that never clears" problem. Also skip empty subtopic-only rows.
        rows = db.execute(
            """SELECT * FROM topics
               WHERE (next_review_date IS NULL OR next_review_date <= ?)
                 AND topic NOT IN (SELECT DISTINCT topic FROM knowledge_points)
               ORDER BY mastery_score ASC, forgetting_risk DESC LIMIT ?""",
            (today.isoformat(), limit),
        ).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            nrd = d.get("next_review_date")
            try:
                d["days_overdue"] = max(0, (today - datetime.fromisoformat(nrd).date()).days) if nrd else 0
            except Exception:
                d["days_overdue"] = 0
            result.append(d)
        return result


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


def mark_topic_mastered(topic: str, subtopic: str = "") -> None:
    topic_id = get_or_create_topic(topic, subtopic)
    with conn() as db:
        db.execute("UPDATE topics SET mastery_score=.92, status='maintenance', next_review_date=?, updated_at=? WHERE topic_id=?", (next_review_date(.92), now(), topic_id))
    # Demonstrated mastery closes the open granular gaps on this topic.
    resolve_knowledge_gaps(topic)


def mark_topic_weak(topic: str, subtopic: str = "") -> None:
    topic_id = get_or_create_topic(topic, subtopic)
    with conn() as db:
        db.execute("UPDATE topics SET mastery_score=.2, status='weak', next_review_date=?, updated_at=? WHERE topic_id=?", (next_review_date(.2), now(), topic_id))


# ---------------------------------------------------------------------------
# Atomic knowledge points — granular fact tracking with per-point confidence
# and an independent spaced-repetition schedule.
# ---------------------------------------------------------------------------

# Knowledge points are scheduled by the SAME per-item FSRS-4 engine used for topics
# (per-item stability/difficulty/retrievability) — ~20-30% fewer reviews than a fixed
# ladder for the same retention. A learner's (is_correct, confidence) maps to an FSRS
# rating 1-4. _KP_LADDER retained only for the legacy resolve helper's far-future date.
_KP_LADDER = [1, 3, 7, 16, 35, 75, 150]


def _kp_rating(is_correct: bool, confidence: Optional[int]) -> int:
    """Map (correctness, 1-5 confidence) to an FSRS rating: 1=again, 2=hard, 3=good,
    4=easy. A miss is always 'again'; a correct answer's grade scales with confidence."""
    if not is_correct:
        return 1
    if confidence is None:
        return 3
    if confidence <= 2:
        return 2
    if confidence >= 4:
        return 4
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
    is_correct: bool,
    confidence: Optional[int] = None,
    mistake_type: str = "other",
) -> Optional[dict[str, Any]]:
    """Record one attempt on an atomic knowledge point: updates correctness history,
    per-point confidence, mastery status, and the independent SRS schedule. Deduped
    on (topic, point). No-op (returns None) if topic or point is blank."""
    topic = (topic or "").strip()
    point = (point or "").strip()
    if not topic or not point:
        return None
    initialize_database()
    ts = now()
    today = datetime.now(timezone.utc).date()
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
        prev_consec = row["consecutive_correct"] if row else 0
        consec = (prev_consec + 1) if is_correct else 0
        times_seen = (row["times_seen"] if row else 0) + 1
        times_correct = (row["times_correct"] if row else 0) + (1 if is_correct else 0)
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
            except Exception:
                interval = 1.0
        except Exception:
            # Fallback: never let a scheduling error drop the attempt.
            fsrs_state_json = row["fsrs_state"] if row else None
            interval = 0.0 if not is_correct else 1.0
            nrd = (today + timedelta(days=int(round(interval)))).isoformat()
        if not is_correct:
            status = "weak"
        elif consec >= 2:
            status = "mastered"
        else:
            status = "learning"
        created = row["created_at"] if row else ts
        db.execute(
            """INSERT INTO knowledge_points
                   (topic, point, status, times_seen, times_correct, consecutive_correct,
                    last_correct, last_confidence, confidence_sum, confidence_n,
                    mistake_type, interval_days, fsrs_state, next_review_date, created_at, updated_at)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
                   updated_at=excluded.updated_at""",
            (topic, point, status, times_seen, times_correct, consec,
             1 if is_correct else 0, conf, confidence_sum, confidence_n,
             (mistake_type or "other").strip() or "other", interval, fsrs_state_json, nrd, created, ts),
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
    today = datetime.now(timezone.utc).date()
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
    today = datetime.now(timezone.utc).date()
    with conn() as db:
        rows = db.execute(
            """SELECT * FROM knowledge_points
               WHERE (next_review_date IS NULL OR next_review_date <= ?)
                 AND status != 'mastered'
               ORDER BY CASE status WHEN 'weak' THEN 0 WHEN 'learning' THEN 1 ELSE 2 END,
                        next_review_date ASC
               LIMIT ?""",
            (today.isoformat(), limit),
        ).fetchall()
    results = [_kp_row_to_dict(r, today) for r in rows]
    if car:
        results = [
            p for p in results
            if len(p.get("point", "")) <= 120
            and (p.get("point", "").count(",") + p.get("point", "").count(";")) < 3
        ]
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
    today = datetime.now(timezone.utc).date()
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
