"""End-to-end diagnostic battery for the right/wrong answer logging pipeline.

Layers covered:
  1. HTTP entry + Pydantic validation (/submit_answer)
  2. Routing (api -> tutor_engine.record_evaluated_answer -> log_attempt)
  3. DB persistence (question_attempts row matches input field-by-field)
  4. Auto-tagging (overconfident_wrong fires when conf>=4 + incorrect)
  5. FSRS state evolution (stability/difficulty/lapses/reps + next_due)
  6. Aggregations (/weak_patterns reflects everything correctly)
  7. Concurrency (parallel submits, no lost rows)
  8. Source snippets (record_evaluated_answer populates them)

These tests use isolated tmp DBs so they don't pollute Dean's real data.
"""

from __future__ import annotations

import json
import sqlite3
import threading
from itertools import product

import pytest
from fastapi.testclient import TestClient

from src.api import app
from src.config import settings


API_KEY = settings.api_key


def _isolated_db(tmp_path, monkeypatch):
    """Reset per-test SQLite + clear any cached connections."""
    from src import student_model
    db_path = tmp_path / "diagnostic.db"
    monkeypatch.setattr(student_model.settings, "sqlite_db_path", db_path)
    student_model._WAL_INIT_PATHS.clear()
    student_model.initialize_database()
    return db_path


def _client():
    return TestClient(app)


def _h():
    return {"X-API-Key": API_KEY}


# ===== Layer 1: HTTP entry + validation =====

def test_submit_rejects_missing_required_field():
    r = _client().post("/submit_answer", json={"question": "q"}, headers=_h())
    assert r.status_code == 422


def test_submit_rejects_invalid_result_enum():
    r = _client().post(
        "/submit_answer",
        json={"question": "q", "user_answer": "a", "topic": "t", "result": "kinda right"},
        headers=_h(),
    )
    assert r.status_code == 422


def test_submit_rejects_invalid_mistake_type_enum():
    r = _client().post(
        "/submit_answer",
        json={
            "question": "q",
            "user_answer": "a",
            "topic": "t",
            "result": "correct",
            "mistake_type": "invented_mistake",
        },
        headers=_h(),
    )
    assert r.status_code == 422


def test_submit_accepts_without_session_id():
    """Confirms session_id default 'voice' so GPT can omit it."""
    r = _client().post(
        "/submit_answer",
        json={
            "question": "q",
            "user_answer": "a",
            "topic": "DiagnosticProbe",
            "result": "correct",
            "mistake_type": "other",
        },
        headers=_h(),
    )
    assert r.status_code == 200
    body = r.json()
    assert body["evaluation"] == "correct"


def test_submit_requires_api_key():
    r = _client().post("/submit_answer", json={"question": "q"})
    assert r.status_code == 401


# ===== Layer 2 + 3: routing + DB persistence + Layer 4: auto-tag =====

@pytest.mark.parametrize("result,conf,mistake,expected_tag", [
    ("correct",   None, "other",          "other"),
    ("correct",   1.0,  "other",          "other"),
    ("correct",   3.0,  "other",          "other"),
    ("correct",   5.0,  "other",          "other"),
    ("partial",   None, "incomplete_answer", "incomplete_answer"),
    ("partial",   2.0,  "mechanism",      "mechanism"),
    ("partial",   4.0,  "drug_dosing",    "drug_dosing"),  # partial doesn't trigger overconfident
    ("incorrect", None, "recall",         "recall"),
    ("incorrect", 1.0,  "recall",         "recall"),
    ("incorrect", 3.0,  "recall",         "recall"),
    ("incorrect", 4.0,  "recall",         "overconfident_wrong"),  # auto-tag fires
    ("incorrect", 5.0,  "recall",         "overconfident_wrong"),  # auto-tag fires
])
def test_persist_every_combination(tmp_path, monkeypatch, result, conf, mistake, expected_tag):
    _isolated_db(tmp_path, monkeypatch)
    body = {
        "question": "q",
        "user_answer": "a",
        "topic": f"Diag_{result}_{conf}_{mistake}",
        "result": result,
        "mistake_type": mistake,
    }
    if conf is not None:
        body["confidence_reported"] = conf
    r = _client().post("/submit_answer", json=body, headers=_h())
    assert r.status_code == 200, r.text
    # Inspect DB
    from src.student_model import conn
    with conn() as db:
        db.row_factory = sqlite3.Row
        row = db.execute(
            "SELECT result, mistake_type, confidence_reported FROM question_attempts ORDER BY attempt_id DESC LIMIT 1"
        ).fetchone()
    assert row["result"] == result
    assert row["mistake_type"] == expected_tag
    assert row["confidence_reported"] == conf


# ===== Layer 5: FSRS state evolution =====

def test_consecutive_correct_grows_stability(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    from src.student_model import conn

    stabilities = []
    for _ in range(5):
        _client().post(
            "/submit_answer",
            json={
                "question": "q",
                "user_answer": "a",
                "topic": "DiagnosticGrowth",
                "result": "correct",
                "mistake_type": "other",
                "confidence_reported": 3.0,
            },
            headers=_h(),
        )
        with conn() as db:
            db.row_factory = sqlite3.Row
            row = db.execute("SELECT fsrs_state FROM topics WHERE topic='DiagnosticGrowth'").fetchone()
        state = json.loads(row["fsrs_state"])
        stabilities.append(state["stability"])
    # Stability must be monotonically non-decreasing across consecutive successes
    for i in range(1, len(stabilities)):
        assert stabilities[i] >= stabilities[i - 1], f"stability regressed at step {i}: {stabilities}"
    # Final stability should be substantially > initial
    assert stabilities[-1] > stabilities[0]


def test_incorrect_low_mastery_forces_today_review(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    from datetime import datetime, timezone
    _client().post(
        "/submit_answer",
        json={
            "question": "q",
            "user_answer": "wrong",
            "topic": "DiagnosticLapse",
            "result": "incorrect",
            "mistake_type": "recall",
            "confidence_reported": 5.0,
        },
        headers=_h(),
    )
    from src.student_model import conn
    with conn() as db:
        db.row_factory = sqlite3.Row
        row = db.execute("SELECT next_review_date, mastery_score FROM topics WHERE topic='DiagnosticLapse'").fetchone()
    # Backend uses UTC date; assert review is scheduled for today UTC
    assert row["next_review_date"] == datetime.now(timezone.utc).date().isoformat()
    assert row["mastery_score"] < 0.4  # weak mastery threshold


def test_fsrs_lapses_increment_on_wrong(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    from src.student_model import conn
    for _ in range(3):
        _client().post(
            "/submit_answer",
            json={
                "question": "q",
                "user_answer": "wrong",
                "topic": "DiagnosticLapses",
                "result": "incorrect",
                "mistake_type": "recall",
            },
            headers=_h(),
        )
    with conn() as db:
        db.row_factory = sqlite3.Row
        row = db.execute("SELECT fsrs_state, times_incorrect FROM topics WHERE topic='DiagnosticLapses'").fetchone()
    state = json.loads(row["fsrs_state"])
    assert state["lapses"] >= 2, f"lapses didn't increment: {state}"
    assert row["times_incorrect"] == 3


def test_topic_upsert_no_duplicate_rows(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    for _ in range(4):
        _client().post(
            "/submit_answer",
            json={
                "question": "q",
                "user_answer": "a",
                "topic": "DiagnosticDedupe",
                "result": "correct",
                "mistake_type": "other",
            },
            headers=_h(),
        )
    from src.student_model import conn
    with conn() as db:
        n = db.execute("SELECT COUNT(*) FROM topics WHERE topic='DiagnosticDedupe'").fetchone()[0]
    assert n == 1


# ===== Layer 6: aggregations =====

def test_weak_patterns_reflects_attempts(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    cases = [
        ("DiagAgg_A", "correct",   3.0, "other"),
        ("DiagAgg_A", "incorrect", 5.0, "recall"),       # confident-wrong
        ("DiagAgg_A", "incorrect", 5.0, "recall"),       # confident-wrong (repeat offender)
        ("DiagAgg_B", "correct",   5.0, "other"),
        ("DiagAgg_B", "incorrect", 4.0, "prioritization"),  # confident-wrong
        ("DiagAgg_C", "partial",   2.0, "mechanism"),
        ("DiagAgg_C", "partial",   1.0, "mechanism"),
    ]
    for topic, result, conf, mistake in cases:
        _client().post(
            "/submit_answer",
            json={
                "question": "q", "user_answer": "a",
                "topic": topic, "result": result,
                "mistake_type": mistake, "confidence_reported": conf,
            },
            headers=_h(),
        )
    r = _client().get("/weak_patterns", headers=_h())
    assert r.status_code == 200
    body = r.json()
    assert body["rolling_30d_attempts"] >= len(cases)
    # 3 confident attempts, 2 of them wrong, 1 right → overconfidence_rate = 2/3 ≈ 0.67
    assert 0.4 <= body["overconfidence_rate"] <= 0.8
    assert body["by_mistake_type"].get("overconfident_wrong", 0) >= 2
    # DiagAgg_A repeated overconfident_wrong twice → repeat offender
    repeat_topics = {(e["topic"], e["mistake_type"]) for e in body["repeat_offenders"]}
    assert ("DiagAgg_A", "overconfident_wrong") in repeat_topics


def test_due_reviews_surfaces_lapsed_topic(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    _client().post(
        "/submit_answer",
        json={
            "question": "q", "user_answer": "wrong",
            "topic": "DiagDueReview", "result": "incorrect",
            "mistake_type": "recall",
        },
        headers=_h(),
    )
    r = _client().get("/due_reviews", headers=_h())
    assert r.status_code == 200
    body = r.json()
    assert any(row["topic"] == "DiagDueReview" for row in body)


def test_student_dashboard_summarizes(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    for i in range(3):
        _client().post(
            "/submit_answer",
            json={
                "question": "q", "user_answer": "a",
                "topic": f"DiagDash_{i}", "result": "correct",
                "mistake_type": "other",
            },
            headers=_h(),
        )
    r = _client().get("/student_dashboard", headers=_h())
    assert r.status_code == 200
    body = r.json()
    assert "summary" in body
    assert "weakest_topics" in body


# ===== Layer 7: concurrency =====

def test_parallel_submits_no_lost_rows(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    n_threads = 4
    n_per_thread = 5

    def submit():
        for _ in range(n_per_thread):
            _client().post(
                "/submit_answer",
                json={
                    "question": "q", "user_answer": "a",
                    "topic": "DiagConcurrency", "result": "correct",
                    "mistake_type": "other",
                },
                headers=_h(),
            )

    threads = [threading.Thread(target=submit) for _ in range(n_threads)]
    for t in threads: t.start()
    for t in threads: t.join()

    from src.student_model import conn
    with conn() as db:
        db.row_factory = sqlite3.Row
        n_attempts = db.execute("SELECT COUNT(*) FROM question_attempts WHERE topic='DiagConcurrency'").fetchone()[0]
        topic_row = db.execute("SELECT times_seen, times_correct FROM topics WHERE topic='DiagConcurrency'").fetchone()
    assert n_attempts == n_threads * n_per_thread, f"lost rows: {n_attempts}/{n_threads * n_per_thread}"
    assert topic_row["times_seen"] == n_threads * n_per_thread


# ===== Layer 8: source snippets =====

@pytest.mark.skipif(not (settings.chroma_dir / "chunks.jsonl").exists(), reason="corpus not ingested")
def test_source_snippets_populated_for_known_topic(tmp_path, monkeypatch):
    _isolated_db(tmp_path, monkeypatch)
    r = _client().post(
        "/submit_answer",
        json={
            "question": "hyperkalemia treatment first move",
            "user_answer": "calcium",
            "topic": "Hyperkalemia",
            "result": "correct",
            "mistake_type": "other",
        },
        headers=_h(),
    )
    assert r.status_code == 200
    body = r.json()
    snippets = body.get("source_snippets") or []
    assert len(snippets) > 0, "no source_snippets returned for known-corpus topic"
    blob = " ".join((s.get("text") or "").lower() for s in snippets)
    # Any of these indicates we hit the right area of the corpus
    assert any(t in blob for t in ("calcium", "insulin", "ecg", "potassium", "hyperk")), \
        f"snippets present but none on hyperkalemia treatment; got: {[s.get('text','')[:60] for s in snippets]}"


# ===== Confidence calibration deeper checks =====

def test_unsure_correct_rates_higher_than_confident_correct(tmp_path, monkeypatch):
    """Bjork's calibration: getting it right WHILE unsure means real learning."""
    _isolated_db(tmp_path, monkeypatch)
    for topic, conf in [("DiagConfident", 5.0), ("DiagUnsure", 1.0)]:
        _client().post(
            "/submit_answer",
            json={
                "question": "q", "user_answer": "a", "topic": topic,
                "result": "correct", "mistake_type": "other", "confidence_reported": conf,
            },
            headers=_h(),
        )
    from src.student_model import conn
    with conn() as db:
        db.row_factory = sqlite3.Row
        confident = db.execute("SELECT fsrs_state FROM topics WHERE topic='DiagConfident'").fetchone()
        unsure = db.execute("SELECT fsrs_state FROM topics WHERE topic='DiagUnsure'").fetchone()
    s_confident = json.loads(confident["fsrs_state"])["stability"]
    s_unsure = json.loads(unsure["fsrs_state"])["stability"]
    # Unsure-correct should have GREATER stability (FSRS rating 4 = Easy)
    assert s_unsure > s_confident, f"unsure={s_unsure}, confident={s_confident} — calibration not applied"
