"""Tests for the CATALOG→SCHEDULER wiring:
  - kp_catalog table creation
  - seed_kp_catalog (incremental / idempotent)
  - get_kp_to_study priority ordering + mastered-KP exclusion
  - illness_script and confusable_pair pass-through
"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def fresh_db():
    """Give every test a brand-new, fully isolated SQLite file (same pattern as
    test_curriculum_coverage.py)."""
    import src.student_model as _sm
    from src.config import settings

    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    new_path = tmp.name

    original_path = settings.sqlite_db_path
    settings.sqlite_db_path = Path(new_path)
    os.environ["SQLITE_DB_PATH"] = new_path
    _sm._WAL_INIT_PATHS.clear()

    from src.student_model import initialize_database
    initialize_database()
    yield

    settings.sqlite_db_path = original_path
    os.environ.pop("SQLITE_DB_PATH", None)
    _sm._WAL_INIT_PATHS.clear()
    try:
        os.unlink(new_path)
    except OSError:
        pass


# ---------------------------------------------------------------------------
# Mock catalog fixture
# ---------------------------------------------------------------------------

MOCK_CATALOG = [
    # KP 1 — presentation category (highest priority)
    {
        "id": "approach-chest-pain-01",
        "topic": "Approach to Chest Pain",
        "domain": "Internal medicine: cardiology",
        "discipline": "medicine",
        "stem": "What are the can't-miss diagnoses in acute chest pain?",
        "answer": "ACS, aortic dissection, PE, tension pneumothorax, esophageal rupture.",
        "rationale": "Life threats first.",
        "bloom": "recall",
        "source": [{"book": "MGH Housestaff Manual", "page": 1}],
        "confusable_with": "",
        "category": "presentation",
        "tier": 1,
    },
    # KP 2 — critical care, tier 1
    {
        "id": "septic-shock-cc-01",
        "topic": "Septic Shock",
        "domain": "Internal medicine: ICU & critical care",
        "discipline": "medicine",
        "stem": "What is the first-line vasopressor in septic shock?",
        "answer": "Norepinephrine.",
        "rationale": "Alpha-1 dominant, less arrhythmogenic than dopamine.",
        "bloom": "recall",
        "source": [{"book": "Marino ICU Book", "page": 543}],
        "confusable_with": "Dopamine",
        "tier": 1,
    },
    # KP 3 — regular medicine topic, tier 2
    {
        "id": "hyperkalemia-ecg-01",
        "topic": "Hyperkalemia",
        "domain": "Internal medicine: nephrology, fluids & electrolytes",
        "discipline": "medicine",
        "stem": "What is the first ECG change in hyperkalemia?",
        "answer": "Peaked T waves.",
        "rationale": "K+ accelerates repolarization.",
        "bloom": "recall",
        "source": [{"book": "Morgan & Mikhail", "page": 1886}],
        "confusable_with": "Hyperacute T waves of STEMI",
        "tier": 2,
    },
    # Illness script entry
    {
        "_type": "illness_script",
        "topic": "Septic Shock",
        "enabling_conditions": "Immunocompromised, elderly, invasive devices",
        "pathophysiology": "Cytokine storm → vasodilation → distributive shock",
        "time_course": "Hours to days",
        "key_features": "Fever, hypotension MAP<65, elevated lactate, warm extremities",
        "consequence_if_missed": "MODS, death",
        "discipline": "medicine",
    },
    # Confusable pair entry
    {
        "_type": "confusable_pair",
        "topic_a": "Septic Shock",
        "topic_b": "Adrenal Crisis",
        "discriminator": "Adrenal crisis has hyponatremia/hyperkalemia; septic shock has elevated lactate",
    },
]


@pytest.fixture
def mock_catalog_file(tmp_path):
    """Write MOCK_CATALOG to a temp JSON file; return the path."""
    p = tmp_path / "mock_kp_catalog.json"
    p.write_text(json.dumps(MOCK_CATALOG), encoding="utf-8")
    return str(p)


# ---------------------------------------------------------------------------
# Seed a minimal curriculum so priority lookup works for at least one topic
# ---------------------------------------------------------------------------

def _seed_minimal_curriculum():
    """Seed the curriculum table with entries matching MOCK_CATALOG topics."""
    from src.student_model import conn, initialize_database, now
    initialize_database()
    with conn() as db:
        db.execute(
            """INSERT OR IGNORE INTO curriculum(topic, domain, discipline,
               is_critical_care, priority_tier, category, subtopics, high_yield, added_at)
               VALUES(?,?,?,?,?,?,?,?,?)""",
            ("Approach to Chest Pain", "Internal medicine: cardiology",
             "medicine", 0, 1, "presentation", "[]", 1, now()),
        )
        db.execute(
            """INSERT OR IGNORE INTO curriculum(topic, domain, discipline,
               is_critical_care, priority_tier, category, subtopics, high_yield, added_at)
               VALUES(?,?,?,?,?,?,?,?,?)""",
            ("Septic Shock", "Internal medicine: ICU & critical care",
             "medicine", 1, 1, "topic", "[]", 1, now()),
        )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_kp_catalog_table_created(fresh_db):
    """kp_catalog table should exist after initialize_database."""
    from src.student_model import conn
    with conn() as db:
        cols = {r["name"] for r in db.execute("PRAGMA table_info(kp_catalog)").fetchall()}
    assert "id" in cols
    assert "stem" in cols
    assert "tier" in cols
    assert "category" in cols
    assert "is_critical_care" in cols
    assert "added_at" in cols


def test_seed_creates_kp_rows(fresh_db, mock_catalog_file):
    """seed_kp_catalog inserts the plain KP rows."""
    from src.student_model import seed_kp_catalog, conn
    counts = seed_kp_catalog(mock_catalog_file)
    assert counts["kps"] == 3
    with conn() as db:
        n = db.execute("SELECT COUNT(*) FROM kp_catalog").fetchone()[0]
    assert n == 3


def test_seed_creates_illness_script(fresh_db, mock_catalog_file):
    """seed_kp_catalog routes illness_script entries to illness_scripts table."""
    from src.student_model import seed_kp_catalog, get_illness_script
    counts = seed_kp_catalog(mock_catalog_file)
    assert counts["illness_scripts"] == 1
    script = get_illness_script("Septic Shock")
    assert script is not None
    assert "distributive" in script["pathophysiology"]


def test_seed_creates_confusable_pair(fresh_db, mock_catalog_file):
    """seed_kp_catalog routes confusable_pair entries to confusable_pairs table."""
    from src.student_model import seed_kp_catalog, get_confusable_pairs
    counts = seed_kp_catalog(mock_catalog_file)
    assert counts["confusable_pairs"] == 1
    pairs = get_confusable_pairs("Septic Shock")
    assert len(pairs) == 1
    assert pairs[0]["confused_with"] == "Adrenal Crisis"


def test_seed_derives_priority_from_curriculum(fresh_db, mock_catalog_file):
    """Rows whose topic is in curriculum should inherit curriculum priority."""
    _seed_minimal_curriculum()
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mock_catalog_file)
    with conn() as db:
        row = db.execute(
            "SELECT category, tier, is_critical_care FROM kp_catalog WHERE id=?",
            ("approach-chest-pain-01",),
        ).fetchone()
    assert row["category"] == "presentation"   # from curriculum
    assert row["tier"] == 1
    assert row["is_critical_care"] == 0


def test_seed_derives_cc_from_curriculum(fresh_db, mock_catalog_file):
    """Septic Shock entry should inherit is_critical_care=1 from curriculum."""
    _seed_minimal_curriculum()
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mock_catalog_file)
    with conn() as db:
        row = db.execute(
            "SELECT is_critical_care FROM kp_catalog WHERE id=?",
            ("septic-shock-cc-01",),
        ).fetchone()
    assert row["is_critical_care"] == 1


def test_seed_fallback_when_topic_not_in_curriculum(fresh_db, mock_catalog_file):
    """Hyperkalemia is NOT in curriculum; fallback to entry-level values."""
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mock_catalog_file)
    with conn() as db:
        row = db.execute(
            "SELECT tier, category, discipline FROM kp_catalog WHERE id=?",
            ("hyperkalemia-ecg-01",),
        ).fetchone()
    assert row["tier"] == 2
    assert row["category"] == "topic"
    assert row["discipline"] == "medicine"


def test_get_kp_to_study_priority_order(fresh_db, mock_catalog_file):
    """get_kp_to_study returns items in correct priority order:
       presentation → CC/tier-1 → tier-2 medicine."""
    _seed_minimal_curriculum()
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(mock_catalog_file)
    results = get_kp_to_study(limit=10)
    assert len(results) == 3
    # First must be the presentation KP
    assert results[0]["id"] == "approach-chest-pain-01"
    assert results[0]["category"] == "presentation"
    # Second must be the CC/tier-1 KP
    assert results[1]["id"] == "septic-shock-cc-01"
    assert results[1]["is_critical_care"] is True
    # Third is the regular tier-2 KP
    assert results[2]["id"] == "hyperkalemia-ecg-01"


def test_get_kp_to_study_excludes_mastered(fresh_db, mock_catalog_file):
    """After mastering a KP (2 correct records), it drops out of get_kp_to_study."""
    _seed_minimal_curriculum()
    from src.student_model import seed_kp_catalog, record_knowledge_point
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(mock_catalog_file)

    stem = "What is the first ECG change in hyperkalemia?"
    # Two consecutive correct answers → status='mastered'
    record_knowledge_point("Hyperkalemia", stem, is_correct=True, confidence=4)
    record_knowledge_point("Hyperkalemia", stem, is_correct=True, confidence=4)

    results = get_kp_to_study(limit=10)
    returned_ids = {r["id"] for r in results}
    assert "hyperkalemia-ecg-01" not in returned_ids
    # Other two KPs still present
    assert "approach-chest-pain-01" in returned_ids
    assert "septic-shock-cc-01" in returned_ids


def test_seed_idempotent(fresh_db, mock_catalog_file):
    """Re-seeding the same file must not create duplicate rows."""
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mock_catalog_file)
    seed_kp_catalog(mock_catalog_file)
    with conn() as db:
        n_kps = db.execute("SELECT COUNT(*) FROM kp_catalog").fetchone()[0]
        n_scripts = db.execute("SELECT COUNT(*) FROM illness_scripts").fetchone()[0]
        n_pairs = db.execute("SELECT COUNT(*) FROM confusable_pairs").fetchone()[0]
    assert n_kps == 3
    assert n_scripts == 1
    assert n_pairs == 1


def test_get_kp_to_study_discipline_filter(fresh_db, mock_catalog_file):
    """discipline filter restricts results to that discipline."""
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(mock_catalog_file)
    results = get_kp_to_study(limit=10, discipline="medicine")
    assert len(results) == 3
    assert all(r["discipline"] == "medicine" for r in results)


def test_get_kp_to_study_topic_filter(fresh_db, mock_catalog_file):
    """topic filter restricts results to that topic."""
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(mock_catalog_file)
    results = get_kp_to_study(limit=10, topic="Hyperkalemia")
    assert len(results) == 1
    assert results[0]["id"] == "hyperkalemia-ecg-01"


def test_get_kp_to_study_returns_required_fields(fresh_db, mock_catalog_file):
    """Every result dict must contain the required content fields."""
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(mock_catalog_file)
    results = get_kp_to_study(limit=10)
    required_keys = {"id", "topic", "stem", "answer", "rationale", "bloom",
                     "source", "discipline", "tier", "category", "is_critical_care"}
    for r in results:
        assert required_keys <= set(r.keys()), f"Missing keys in {r}"


def test_get_kp_to_study_empty_catalog(fresh_db):
    """When kp_catalog is empty, returns empty list (no error)."""
    from src.mcp_endpoints import get_kp_to_study
    results = get_kp_to_study(limit=10)
    assert results == []
