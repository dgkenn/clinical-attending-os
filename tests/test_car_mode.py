"""Tests for car-mode study support.

Covers:
  - _kp_car_safe helper: 1 for short recall fact, 0 for long answer / 3-item
    enumeration / "which of the following" stem.
  - seed_kp_catalog populates car_safe correctly.
  - get_kp_to_study(format="car") returns ONLY car_safe rows, still priority-ordered.
  - get_due_knowledge_points(car=True) excludes long/enumerated points.
"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Fixture: isolated SQLite DB (same pattern as test_kp_catalog.py)
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def fresh_db():
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
# Tests: _kp_car_safe logic
# ---------------------------------------------------------------------------

def test_car_safe_short_recall_fact():
    """A concise single-fact Q&A should be car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="What is the first-line vasopressor in septic shock?",
        answer="Norepinephrine.",
        rationale="Alpha-1 dominant, less arrhythmogenic than dopamine.",
    ) == 1


def test_car_safe_long_answer():
    """An answer > 180 chars should NOT be car-safe."""
    from src.student_model import _kp_car_safe
    long_answer = "A" * 181
    assert _kp_car_safe(
        stem="Name the drug.",
        answer=long_answer,
        rationale="Short rationale.",
    ) == 0


def test_car_safe_long_stem():
    """A stem > 120 chars should NOT be car-safe."""
    from src.student_model import _kp_car_safe
    long_stem = "What is the " + "very " * 25 + "answer?"
    assert len(long_stem) > 120
    assert _kp_car_safe(
        stem=long_stem,
        answer="X.",
        rationale="Short.",
    ) == 0


def test_car_safe_long_rationale():
    """A rationale > 200 chars should NOT be car-safe."""
    from src.student_model import _kp_car_safe
    long_rat = "Because " + "of this " * 30
    assert len(long_rat) > 200
    assert _kp_car_safe(
        stem="Short stem?",
        answer="Short answer.",
        rationale=long_rat,
    ) == 0


def test_car_safe_enumeration_three_commas():
    """An answer with 3+ comma/semicolon/' and ' tokens should NOT be car-safe."""
    from src.student_model import _kp_car_safe
    # 3 commas → enum_count = 3 → unsafe
    assert _kp_car_safe(
        stem="List the shock types.",
        answer="Distributive, hypovolemic, cardiogenic, obstructive.",
        rationale="Four types.",
    ) == 0


def test_car_safe_enumeration_semicolons():
    """Semicolons count toward the enumeration threshold (need >=3 total separators)."""
    from src.student_model import _kp_car_safe
    # 3 semicolons → total=3 → unsafe
    assert _kp_car_safe(
        stem="Name the findings.",
        answer="Fever; tachycardia; hypotension; confusion.",
        rationale="SIRS criteria.",
    ) == 0
    # 2 semicolons only → total=2 < 3 → still car-safe by spec
    assert _kp_car_safe(
        stem="Name the findings.",
        answer="Fever; tachycardia; hypotension.",
        rationale="SIRS criteria.",
    ) == 1


def test_car_safe_enumeration_and_keyword():
    """' and ' occurrences count toward the enumeration threshold."""
    from src.student_model import _kp_car_safe
    # "and" appears 3 times → enum_count >= 3
    assert _kp_car_safe(
        stem="What do you give?",
        answer="Drug A and drug B and drug C and drug D.",
        rationale="All four.",
    ) == 0


def test_car_safe_which_of_the_following():
    """'which of the following' in stem → NOT car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="Which of the following is the first-line vasopressor?",
        answer="Norepinephrine.",
        rationale="Alpha-1 dominant.",
    ) == 0


def test_car_safe_list_phrase_in_stem():
    """'list ' in stem → NOT car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="List the causes of hyponatremia.",
        answer="SIADH, hypothyroidism.",
        rationale="Common causes.",
    ) == 0


def test_car_safe_name_all_phrase():
    """'name all' in stem → NOT car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="Name all the components of SIRS.",
        answer="Fever, tachycardia.",
        rationale="Classic SIRS.",
    ) == 0


def test_car_safe_image_phrase():
    """'image' in stem → NOT car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="What does this ECG image show?",
        answer="ST elevation in V1-V4.",
        rationale="STEMI pattern.",
    ) == 0


def test_car_safe_figure_phrase():
    """'figure' in stem → NOT car-safe."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="Based on the figure, what is the diagnosis?",
        answer="Tension pneumothorax.",
        rationale="Tracheal deviation.",
    ) == 0


def test_car_safe_none_rationale():
    """None rationale should be treated as empty (0 chars) — still safe if other fields OK."""
    from src.student_model import _kp_car_safe
    assert _kp_car_safe(
        stem="What is the MAP target in septic shock?",
        answer="Greater than or equal to 65 mmHg.",
        rationale=None,
    ) == 1


def test_car_safe_exactly_at_boundary():
    """Items exactly at the boundary (120/180/200 chars) should be car-safe."""
    from src.student_model import _kp_car_safe
    stem = "S" * 120
    answer = "A" * 180
    rationale = "R" * 200
    assert _kp_car_safe(stem=stem, answer=answer, rationale=rationale) == 1


# ---------------------------------------------------------------------------
# Tests: seed_kp_catalog populates car_safe
# ---------------------------------------------------------------------------

# Mini catalog: two KPs — one car-safe, one not
_MINI_CATALOG = [
    {
        "id": "safe-kp-01",
        "topic": "Septic Shock",
        "domain": "Internal medicine: ICU & critical care",
        "discipline": "medicine",
        "stem": "What is the first-line vasopressor in septic shock?",
        "answer": "Norepinephrine.",
        "rationale": "Alpha-1 dominant, less arrhythmogenic than dopamine.",
        "bloom": "recall",
        "source": [],
        "tier": 1,
    },
    {
        "id": "unsafe-kp-01",
        "topic": "Shock Types",
        "domain": "Internal medicine: ICU & critical care",
        "discipline": "medicine",
        "stem": "Which of the following correctly describes the four shock categories?",
        "answer": "Distributive, hypovolemic, cardiogenic, obstructive — each with different hemodynamics.",
        "rationale": "Classic four-category framework from Marino.",
        "bloom": "recall",
        "source": [],
        "tier": 1,
    },
]


@pytest.fixture
def mini_catalog_file(tmp_path):
    p = tmp_path / "mini_kp_catalog.json"
    p.write_text(json.dumps(_MINI_CATALOG), encoding="utf-8")
    return str(p)


def test_seed_populates_car_safe(fresh_db, mini_catalog_file):
    """seed_kp_catalog should compute and store car_safe for each KP."""
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mini_catalog_file)
    with conn() as db:
        rows = {
            r["id"]: r["car_safe"]
            for r in db.execute("SELECT id, car_safe FROM kp_catalog").fetchall()
        }
    assert rows["safe-kp-01"] == 1
    assert rows["unsafe-kp-01"] == 0


def test_seed_car_safe_idempotent(fresh_db, mini_catalog_file):
    """Re-seeding the same catalog should NOT flip car_safe values."""
    from src.student_model import seed_kp_catalog, conn
    seed_kp_catalog(mini_catalog_file)
    seed_kp_catalog(mini_catalog_file)
    with conn() as db:
        rows = {
            r["id"]: r["car_safe"]
            for r in db.execute("SELECT id, car_safe FROM kp_catalog").fetchall()
        }
    assert rows["safe-kp-01"] == 1
    assert rows["unsafe-kp-01"] == 0


# ---------------------------------------------------------------------------
# Tests: get_kp_to_study(format="car")
# ---------------------------------------------------------------------------

# Richer catalog for priority-order tests
_PRIORITY_CATALOG = [
    {
        "id": "pres-safe-01",
        "topic": "Approach to Chest Pain",
        "domain": "Internal medicine: cardiology",
        "discipline": "medicine",
        "stem": "What is the single most urgent can't-miss cause of chest pain?",
        "answer": "Aortic dissection — immediate CT angiogram if suspected.",
        "rationale": "Rapidly fatal if missed; D-dimer is not reliable.",
        "bloom": "recall",
        "source": [],
        "category": "presentation",
        "tier": 1,
    },
    {
        "id": "cc-safe-01",
        "topic": "Septic Shock",
        "domain": "Internal medicine: ICU & critical care",
        "discipline": "medicine",
        "stem": "What is the first-line vasopressor in septic shock?",
        "answer": "Norepinephrine.",
        "rationale": "Alpha-1 dominant, less arrhythmogenic.",
        "bloom": "recall",
        "source": [],
        "tier": 1,
    },
    {
        "id": "unsafe-visual-01",
        "topic": "ECG Interpretation",
        "domain": "Internal medicine: cardiology",
        "discipline": "medicine",
        "stem": "Looking at this ECG image, what rhythm is shown?",
        "answer": "Atrial fibrillation with rapid ventricular response.",
        "rationale": "Irregularly irregular, no P waves.",
        "bloom": "apply",
        "source": [],
        "tier": 1,
    },
    {
        "id": "tier2-safe-01",
        "topic": "Hyperkalemia",
        "domain": "Internal medicine: nephrology",
        "discipline": "medicine",
        "stem": "What is the first ECG change in hyperkalemia?",
        "answer": "Peaked T waves.",
        "rationale": "K+ accelerates repolarization.",
        "bloom": "recall",
        "source": [],
        "tier": 2,
    },
]


@pytest.fixture
def priority_catalog_file(tmp_path):
    p = tmp_path / "priority_kp_catalog.json"
    p.write_text(json.dumps(_PRIORITY_CATALOG), encoding="utf-8")
    return str(p)


def _seed_priority_curriculum():
    """Seed curriculum entries so priority derivation works."""
    from src.student_model import conn, initialize_database, now
    initialize_database()
    with conn() as db:
        for topic, domain, discipline, is_cc, tier, category in [
            ("Approach to Chest Pain", "Internal medicine: cardiology", "medicine", 0, 1, "presentation"),
            ("Septic Shock", "Internal medicine: ICU & critical care", "medicine", 1, 1, "topic"),
        ]:
            db.execute(
                """INSERT OR IGNORE INTO curriculum(topic, domain, discipline,
                   is_critical_care, priority_tier, category, subtopics, high_yield, added_at)
                   VALUES(?,?,?,?,?,?,?,?,?)""",
                (topic, domain, discipline, is_cc, tier, category, "[]", 1, now()),
            )


def test_get_kp_to_study_car_format_excludes_unsafe(fresh_db, priority_catalog_file):
    """get_kp_to_study(format='car') should return ONLY car_safe=1 rows."""
    _seed_priority_curriculum()
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(priority_catalog_file)
    results = get_kp_to_study(limit=10, format="car")
    ids = {r["id"] for r in results}
    assert "unsafe-visual-01" not in ids, "Visual/image item should be excluded"
    assert "pres-safe-01" in ids
    assert "cc-safe-01" in ids
    assert "tier2-safe-01" in ids


def test_get_kp_to_study_car_format_priority_order(fresh_db, priority_catalog_file):
    """Car-format results should still be in priority order (presentation→CC→tier-2)."""
    _seed_priority_curriculum()
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(priority_catalog_file)
    results = get_kp_to_study(limit=10, format="car")
    # Only car-safe items should be present
    assert all(r["car_safe"] is True for r in results)
    # Priority: presentation first
    assert results[0]["id"] == "pres-safe-01"
    # CC/tier-1 second
    assert results[1]["id"] == "cc-safe-01"
    # Tier-2 last
    assert results[2]["id"] == "tier2-safe-01"


def test_get_kp_to_study_default_format_unchanged(fresh_db, priority_catalog_file):
    """format='' (default) should still return ALL non-mastered rows including unsafe ones."""
    _seed_priority_curriculum()
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(priority_catalog_file)
    results = get_kp_to_study(limit=10)
    ids = {r["id"] for r in results}
    assert "unsafe-visual-01" in ids, "Default format should include all rows"


def test_get_kp_to_study_car_format_returns_car_safe_field(fresh_db, priority_catalog_file):
    """Results from get_kp_to_study should include car_safe field."""
    from src.student_model import seed_kp_catalog
    from src.mcp_endpoints import get_kp_to_study
    seed_kp_catalog(priority_catalog_file)
    results = get_kp_to_study(limit=10)
    for r in results:
        assert "car_safe" in r, f"car_safe missing from result {r['id']}"


# ---------------------------------------------------------------------------
# Tests: get_due_knowledge_points(car=True)
# ---------------------------------------------------------------------------

def _backdate_knowledge_points(db_conn):
    """Force all knowledge_points into "due yesterday" state.

    Both dates must move: next_review_date puts the fact in the due window, and
    updated_at must leave TODAY because a fact touched today is deliberately
    not re-served today (the same-local-day guard — the user was seeing the
    same cards several times a day)."""
    db_conn.execute("UPDATE knowledge_points SET next_review_date='2000-01-01', "
                    "updated_at=datetime(updated_at, '-2 days')")


def test_get_due_knowledge_points_car_excludes_long_points(fresh_db):
    """car=True should exclude knowledge points longer than 120 chars."""
    from src.student_model import record_knowledge_point, get_due_knowledge_points, conn

    short_point = "Norepinephrine is the first-line vasopressor in septic shock."
    long_point = "The mechanism of action involves " + "alpha-1 receptor activation " * 5
    assert len(long_point) > 120

    record_knowledge_point("Septic Shock", short_point, is_correct=False)
    record_knowledge_point("Septic Shock", long_point, is_correct=False)
    with conn() as db:
        _backdate_knowledge_points(db)

    due_car = get_due_knowledge_points(limit=50, car=True)
    car_points = {p["point"] for p in due_car}
    assert short_point in car_points
    assert long_point not in car_points, "Long point should be excluded in car mode"


def test_get_due_knowledge_points_car_excludes_enumerated_points(fresh_db):
    """car=True should exclude points with 3+ total comma/semicolon separators."""
    from src.student_model import record_knowledge_point, get_due_knowledge_points, conn

    clean_point = "First-line vasopressor is norepinephrine."
    # 1 comma + 2 semicolons = 3 total separators → should be excluded
    enum_point = "SIRS criteria: fever, tachycardia; hypotension; altered mental status."

    record_knowledge_point("SIRS", clean_point, is_correct=False)
    record_knowledge_point("SIRS", enum_point, is_correct=False)
    with conn() as db:
        _backdate_knowledge_points(db)

    due_car = get_due_knowledge_points(limit=50, car=True)
    car_points = {p["point"] for p in due_car}
    assert clean_point in car_points
    assert enum_point not in car_points, "Enumeration-heavy point should be excluded in car mode"


def test_get_due_knowledge_points_default_unchanged(fresh_db):
    """car=False (default) should return long/enumerated points as before."""
    from src.student_model import record_knowledge_point, get_due_knowledge_points, conn

    long_point = "The mechanism involves " + "repeated " * 20 + "steps."
    assert len(long_point) > 120

    record_knowledge_point("Pharmacology", long_point, is_correct=False)
    with conn() as db:
        _backdate_knowledge_points(db)

    due_all = get_due_knowledge_points(limit=50)
    assert any(p["point"] == long_point for p in due_all), (
        "Default (car=False) should include long points"
    )


def test_get_due_knowledge_points_car_via_mcp_server(fresh_db):
    """mcp_server.get_due_knowledge_points(car=True) should wire through correctly."""
    from src.student_model import record_knowledge_point, conn
    from src.mcp_server import get_due_knowledge_points as server_get_due

    short = "MAP target in septic shock is 65 mmHg."
    long_p = "X" * 130  # > 120 chars → excluded

    record_knowledge_point("Septic Shock", short, is_correct=False)
    record_knowledge_point("Septic Shock", long_p, is_correct=False)
    with conn() as db:
        _backdate_knowledge_points(db)

    result = server_get_due(limit=50, car=True)
    points = {p["point"] for p in result["due_points"]}
    assert short in points
    assert long_p not in points
