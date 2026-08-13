"""
Regression tests for submit_answer mastery crediting.

Guards against the bugs fixed in mcp_endpoints.py:
  1. mastery_vector table never written after submit_answer
  2. level_achieved always returned "baseline" (used wrong column name)
  3. Double FSRS advance (second fsrs_review call on already-advanced state)
"""

import os
import sqlite3
from pathlib import Path
import pytest


@pytest.fixture()
def isolated_db(tmp_path, monkeypatch):
    """
    Redirect the SQLite backend to a per-test temp file.

    Settings is a dataclass whose field defaults are evaluated once at class
    parse time via os.getenv(), so env-var monkeypatching after import has no
    effect on the already-constructed module-level `settings` singleton.
    We therefore patch the *attribute* on the live singleton directly.
    """
    db_file = tmp_path / "test_student.db"

    import src.config as cfg_mod
    import src.student_model as sm_mod

    # Patch the live singleton's attribute (dataclasses allow attribute assignment)
    monkeypatch.setattr(cfg_mod.settings, "sqlite_db_path", Path(db_file))
    monkeypatch.setattr(sm_mod.settings, "sqlite_db_path", Path(db_file))

    # Clear WAL init cache so the new path gets PRAGMA journal_mode=WAL applied
    sm_mod._WAL_INIT_PATHS.clear()
    sm_mod.initialize_database()

    yield db_file

    sm_mod._WAL_INIT_PATHS.discard(str(db_file))


def _raw_db(db_file):
    c = sqlite3.connect(str(db_file))
    c.row_factory = sqlite3.Row
    return c


def test_submit_answer_writes_mastery_vector(isolated_db):
    """After a correct submit_answer, mastery_vector row must exist with accuracy > 0."""
    import src.mcp_endpoints as ep
    import src.student_model as sm
    ep.conn = sm.conn  # ensure mcp_endpoints uses the patched conn()

    result = ep.submit_answer(
        topic="Sepsis",
        user_answer="Norepinephrine first-line; 30 mL/kg crystalloid; cultures before abx.",
        is_correct=True,
        confidence_reported=4,
        teach_back_quality=0.9,
        transfer_success=True,
    )

    assert result["ok"] is True, f"submit_answer failed: {result}"

    db = _raw_db(isolated_db)
    mv = db.execute(
        "SELECT accuracy, mechanism_quality FROM mastery_vector WHERE topic_name='Sepsis'"
    ).fetchone()
    db.close()

    assert mv is not None, "mastery_vector row not written after submit_answer"
    assert mv["accuracy"] == 1.0, f"Expected accuracy 1.0, got {mv['accuracy']}"


def test_submit_answer_level_achieved_not_always_baseline(isolated_db):
    """
    level_achieved must reflect the actual status from the topics table,
    not always the default 'baseline' string (old bug: wrong column name).

    We drive the topic to 'learning' status by doing many correct answers
    so FSRS raises mastery above 0.6 and status_for_mastery() returns 'learning'.
    Then we confirm the API returns 'intermediate', not 'baseline'.
    """
    import src.mcp_endpoints as ep
    import src.student_model as sm
    from src.fsrs import fsrs_init, fsrs_review, serialize
    ep.conn = sm.conn

    # Seed a high-stability FSRS state directly so FSRS proxy returns mastery >= 0.6.
    # mastery_proxy = log1p(s)/log1p(180) >= 0.6  →  s >= exp(0.6*log1p(180))-1 ≈ 34.
    # We can't easily achieve this via rapid same-instant reviews (elapsed≈0 prevents
    # stability growth), so we directly inject a state with stability=40.
    import json
    from datetime import datetime, timedelta, timezone
    topic_id = sm.get_or_create_topic("Hyperkalemia", "")
    # Build a synthetic FSRS state with stability=40 reviewed 2 days ago
    last_review = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
    next_due = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()  # overdue
    high_stability_state = json.dumps({
        "stability": 40.0, "difficulty": 4.0, "lapses": 0,
        "reps": 5, "last_review": last_review, "next_due": next_due, "state": "review",
    })
    with sm.conn() as db:
        db.execute(
            "UPDATE topics SET fsrs_state=?, mastery_score=0.62, status='learning' "
            "WHERE topic='Hyperkalemia'",
            (high_stability_state,),
        )

    result = ep.submit_answer(
        topic="Hyperkalemia",
        user_answer="Stop potassium, calcium gluconate, insulin+glucose, kayexalate.",
        is_correct=True,
        confidence_reported=4,
        teach_back_quality=0.85,
        transfer_success=True,
    )

    assert result["ok"] is True
    # With high stability pre-seeded, status_for_mastery should return 'learning'
    # or better, and level_achieved must NOT be 'baseline'.
    assert result["level_achieved"] in ("intermediate", "advanced"), (
        f"level_achieved should be 'intermediate' or 'advanced' for a well-trained topic, "
        f"got {result['level_achieved']!r} (status now: {result.get('status')}, "
        f"mastery: {result.get('mastery_score')})"
    )


def test_submit_answer_mastery_score_increases(isolated_db):
    """mastery_score in the topics table must increase after correct answers."""
    import src.mcp_endpoints as ep
    import src.student_model as sm
    ep.conn = sm.conn

    sm.get_or_create_topic("Sepsis", "")
    before = sm.get_topic_summary("Sepsis").get("mastery_score", 0.25)

    for _ in range(3):
        ep.submit_answer(
            topic="Sepsis",
            user_answer="Norepinephrine is first-line vasopressor in septic shock.",
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.9,
            transfer_success=True,
        )

    after = sm.get_topic_summary("Sepsis").get("mastery_score", 0.25)
    assert after > before, (
        f"mastery_score should increase after 3 correct answers; was {before}, now {after}"
    )


def test_submit_answer_no_double_fsrs_advance(isolated_db):
    """
    submit_answer must advance FSRS exactly once per call.

    First review with rating 2 (teach_back_quality<0.5 → mechanism path) gives
    stability ~1.18 → 1-day interval.  Rating 3 gives ~3.13 → 3 days.
    Double-advance compounding from a fresh card would yield 30+ days.
    Allow up to 15 days to absorb any confidence-weighting headroom.
    """
    import src.mcp_endpoints as ep
    import src.student_model as sm
    from datetime import date
    ep.conn = sm.conn

    result = ep.submit_answer(
        topic="Afib with RVR",
        user_answer="Rate control with metoprolol or diltiazem.",
        is_correct=True,
        confidence_reported=3,
        teach_back_quality=0.7,
        transfer_success=False,
    )

    assert result["ok"] is True
    next_review = result["next_review_date"]
    today = date.today()
    next_date = date.fromisoformat(next_review[:10])
    days_out = (next_date - today).days
    assert days_out <= 15, (
        f"next_review_date is {days_out} days out ({next_review!r}); "
        f"expected <=15 for a first-review card (double-FSRS-advance would be 30+)"
    )


def test_get_mastery_gates_reads_mastery_vector_after_submit(isolated_db):
    """get_mastery_gates must show non-zero accuracy for Sepsis after submit_answer."""
    import src.mcp_endpoints as ep
    import src.student_model as sm
    ep.conn = sm.conn

    ep.submit_answer(
        topic="Sepsis",
        user_answer="Norepinephrine first-line; 30 mL/kg crystalloid.",
        is_correct=True,
        confidence_reported=4,
        teach_back_quality=0.9,
        transfer_success=True,
    )

    gates = ep.get_mastery_gates()
    assert "mastery_matrix" in gates
    sepsis = gates["mastery_matrix"].get("Sepsis")
    assert sepsis is not None, "Sepsis missing from mastery_matrix"
    accuracy = sepsis["vector"]["accuracy"]
    assert accuracy > 0.0, (
        f"Sepsis vector accuracy should be > 0 after a correct answer, got {accuracy}"
    )
