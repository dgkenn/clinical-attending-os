"""Tests for curriculum-coverage engine: seeding, discipline/CC tagging,
get_mastery_map(), get_next_topic(), and set_medicine_weight().

Uses a temp SQLite DB to avoid polluting the real student model.
"""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import pytest

# now safe to import src modules (DB path is set per-fixture below)
from src.student_model import (  # noqa: E402
    initialize_database,
    seed_curriculum,
    get_medicine_weight,
    set_medicine_weight,
    _derive_discipline,
    _derive_is_critical_care,
    get_or_create_topic,
    record_knowledge_gap,
    record_knowledge_point,
    get_knowledge_gaps,
    get_knowledge_points,
    get_due_knowledge_points,
    resolve_knowledge_gaps,
    mark_topic_weak,
    mark_topic_mastered,
    conn,
)
from src.student_model import get_due_reviews as _due_reviews  # noqa: E402
from src.mcp_endpoints import (  # noqa: E402
    get_mastery_map,
    get_next_topic,
    get_session_state,
    get_kp_to_study,
    set_medicine_weight_tool,
)
from src.mcp_server import (  # noqa: E402
    log_missed_topic,
    get_knowledge_gaps as get_knowledge_gaps_tool,
    submit_knowledge_points,
    get_knowledge_points as get_knowledge_points_tool,
    get_due_knowledge_points as get_due_knowledge_points_tool,
)

MOCK_PATH = str(Path(__file__).parent.parent / "data" / "_mock_curriculum.json")


@pytest.fixture(autouse=True)
def fresh_db():
    """Give every test a brand-new, fully isolated SQLite file."""
    import sqlite3
    import src.student_model as _sm
    from src.config import settings

    # Create a unique temp file for this test
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    new_path = tmp.name

    # Patch the settings object and the module-level WAL cache
    original_path = settings.sqlite_db_path
    settings.sqlite_db_path = Path(new_path)
    os.environ["SQLITE_DB_PATH"] = new_path
    _sm._WAL_INIT_PATHS.clear()

    initialize_database()
    yield

    # Teardown: restore settings and remove temp file
    settings.sqlite_db_path = original_path
    os.environ.pop("SQLITE_DB_PATH", None)
    _sm._WAL_INIT_PATHS.clear()
    try:
        os.unlink(new_path)
    except OSError:
        pass


# ---------------------------------------------------------------------------
# 1. seed_curriculum — count and column derivation
# ---------------------------------------------------------------------------

class TestSeedCurriculum:
    def test_seeded_count_matches_json(self):
        data = json.loads(Path(MOCK_PATH).read_text())
        n = seed_curriculum(MOCK_PATH)
        assert n == len(data), f"Expected {len(data)} rows, got {n}"

    def test_idempotent(self):
        n1 = seed_curriculum(MOCK_PATH)
        n2 = seed_curriculum(MOCK_PATH)
        assert n1 == n2

    def test_discipline_anesthesia(self):
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            rows = db.execute(
                "SELECT discipline FROM curriculum WHERE domain LIKE '%Anesth%'"
            ).fetchall()
        assert rows, "No anesthesia rows found"
        for r in rows:
            assert r["discipline"] == "anesthesia", f"Expected 'anesthesia', got {r['discipline']}"

    def test_discipline_medicine(self):
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            rows = db.execute(
                "SELECT discipline FROM curriculum WHERE domain LIKE '%Internal Medicine%'"
            ).fetchall()
        assert rows, "No internal medicine rows found"
        for r in rows:
            assert r["discipline"] == "medicine", f"Expected 'medicine', got {r['discipline']}"

    def test_icu_domain_is_critical_care(self):
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            rows = db.execute(
                "SELECT topic, is_critical_care FROM curriculum WHERE domain LIKE '%ICU%' OR domain LIKE '%Critical%'"
            ).fetchall()
        assert rows, "No ICU/Critical Care rows found"
        for r in rows:
            assert r["is_critical_care"] == 1, f"{r['topic']} should be critical_care=1"

    def test_sepsis_is_critical_care(self):
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            row = db.execute(
                "SELECT is_critical_care FROM curriculum WHERE topic LIKE '%Sepsis%'"
            ).fetchone()
        assert row is not None, "Sepsis topic not found"
        assert row["is_critical_care"] == 1

    def test_airway_is_critical_care(self):
        """Airway Management contains 'airway' keyword."""
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            row = db.execute(
                "SELECT is_critical_care FROM curriculum WHERE topic = 'Airway Management'"
            ).fetchone()
        assert row is not None
        assert row["is_critical_care"] == 1

    def test_atrial_fibrillation_not_critical_care(self):
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            row = db.execute(
                "SELECT is_critical_care FROM curriculum WHERE topic = 'Atrial Fibrillation'"
            ).fetchone()
        assert row is not None
        assert row["is_critical_care"] == 0


# ---------------------------------------------------------------------------
# 2. Derivation helpers
# ---------------------------------------------------------------------------

class TestDerivationHelpers:
    def test_derive_discipline_anesthesia(self):
        assert _derive_discipline("Anesthesia") == "anesthesia"
        assert _derive_discipline("ANESTHESIOLOGY Boards") == "anesthesia"

    def test_derive_discipline_medicine(self):
        assert _derive_discipline("Internal medicine: cardiology") == "medicine"
        assert _derive_discipline("General internal medicine, preventive care") == "medicine"

    def test_derive_discipline_unknown_defaults_anesthesia(self):
        # Anything not labeled 'Internal/General internal medicine' is anesthesia here
        # (Airway, Pain, Preop, Crises, Safety domains don't contain 'anesthesia').
        assert _derive_discipline("Airway management") == "anesthesia"
        assert _derive_discipline("Pain medicine") == "anesthesia"
        assert _derive_discipline("") == "anesthesia"

    def test_derive_is_cc_from_domain(self):
        assert _derive_is_critical_care("ICU Critical Care", "Something") == 1
        assert _derive_is_critical_care("Something", "Sepsis") == 1
        assert _derive_is_critical_care("Something", "ARDS") == 1
        assert _derive_is_critical_care("Something", "Vasopressor dosing") == 1

    def test_derive_is_cc_false_for_regular(self):
        assert _derive_is_critical_care("Internal Medicine", "Atrial Fibrillation") == 0
        assert _derive_is_critical_care("Anesthesia", "Regional Anesthesia") == 0


# ---------------------------------------------------------------------------
# 3. get_mastery_map — empty curriculum, then after seeding, then after study
# ---------------------------------------------------------------------------

class TestGetMasteryMap:
    def test_empty_curriculum_returns_zeros(self):
        result = get_mastery_map()
        assert result["total_curriculum_topics"] == 0
        assert result["topics_studied"] == 0
        assert result["coverage_pct"] == 0.0
        assert result["by_discipline"] == {
            "medicine": {"total": 0, "studied": 0, "coverage_pct": 0.0},
            "anesthesia": {"total": 0, "studied": 0, "coverage_pct": 0.0},
        }
        assert result["critical_care"] == {"total": 0, "studied": 0, "coverage_pct": 0.0}
        assert "error" not in result

    def test_seeded_coverage_zero_before_study(self):
        seed_curriculum(MOCK_PATH)
        result = get_mastery_map()
        data = json.loads(Path(MOCK_PATH).read_text())
        assert result["total_curriculum_topics"] == len(data)
        assert result["topics_studied"] == 0
        assert result["coverage_pct"] == 0.0
        assert result["untouched_count"] == len(data)

    def test_by_discipline_totals_populated(self):
        seed_curriculum(MOCK_PATH)
        result = get_mastery_map()
        data = json.loads(Path(MOCK_PATH).read_text())
        total_all = result["by_discipline"]["medicine"]["total"] + result["by_discipline"]["anesthesia"]["total"]
        assert total_all == len(data)

    def test_critical_care_total_nonzero(self):
        seed_curriculum(MOCK_PATH)
        result = get_mastery_map()
        assert result["critical_care"]["total"] > 0, "Expected some CC topics in mock"

    def test_coverage_rises_after_study(self):
        seed_curriculum(MOCK_PATH)
        before = get_mastery_map()
        assert before["coverage_pct"] == 0.0

        # Mark one topic as studied (times_seen > 0) by inserting directly
        with conn() as db:
            db.execute(
                "INSERT OR IGNORE INTO topics(topic, subtopic, times_seen, status, mastery_score, "
                "next_review_date, created_at, updated_at) VALUES(?, '', 1, 'learning', 0.7, '2099-01-01', datetime('now'), datetime('now'))",
                ("Sepsis and Septic Shock",),
            )

        after = get_mastery_map()
        assert after["topics_studied"] == 1
        assert after["coverage_pct"] > 0.0
        assert after["critical_care"]["studied"] == 1

    def test_by_domain_sorted_weakest_first(self):
        seed_curriculum(MOCK_PATH)
        # Partially study one domain
        with conn() as db:
            db.execute(
                "INSERT OR IGNORE INTO topics(topic, subtopic, times_seen, status, mastery_score, "
                "next_review_date, created_at, updated_at) VALUES(?, '', 2, 'maintenance', 0.9, '2099-01-01', datetime('now'), datetime('now'))",
                ("Malignant Hyperthermia",),
            )
        result = get_mastery_map()
        coverages = [d["coverage_pct"] for d in result["by_domain"]]
        assert coverages == sorted(coverages), "by_domain should be sorted weakest-coverage first"

    def test_weakest_domains_top_3(self):
        seed_curriculum(MOCK_PATH)
        result = get_mastery_map()
        assert isinstance(result["weakest_domains"], list)
        assert len(result["weakest_domains"]) <= 3


# ---------------------------------------------------------------------------
# 4. get_next_topic — untouched curriculum topic with new_coverage reason
# ---------------------------------------------------------------------------

class TestGetNextTopic:
    def test_returns_new_coverage_reason_from_curriculum(self):
        seed_curriculum(MOCK_PATH)
        result = get_next_topic()
        assert result.get("reason") == "new_coverage", (
            f"Expected 'new_coverage', got {result.get('reason')}: {result}"
        )

    def test_critical_care_topic_preferred(self):
        """With no studied topics, a CC topic should be picked first."""
        seed_curriculum(MOCK_PATH)
        result = get_next_topic()
        assert result.get("is_critical_care") is True, (
            f"Expected a critical-care topic first, got: {result.get('topic')}"
        )

    def test_returned_topic_is_in_curriculum(self):
        seed_curriculum(MOCK_PATH)
        result = get_next_topic()
        with conn() as db:
            row = db.execute(
                "SELECT topic FROM curriculum WHERE topic = ?", (result["topic"],)
            ).fetchone()
        assert row is not None, f"Topic '{result['topic']}' not in curriculum"

    def test_next_topic_has_discipline_field(self):
        seed_curriculum(MOCK_PATH)
        result = get_next_topic()
        assert "discipline" in result

    def test_due_review_takes_priority(self):
        """If a topic is due for review, it beats new_coverage."""
        seed_curriculum(MOCK_PATH)
        # Insert a topic in 'topics' table that is overdue
        with conn() as db:
            db.execute(
                "INSERT OR IGNORE INTO topics(topic, subtopic, times_seen, status, mastery_score, "
                "next_review_date, created_at, updated_at) VALUES(?, '', 3, 'weak', 0.2, '2000-01-01', datetime('now'), datetime('now'))",
                ("Hyperkalemia",),
            )
        result = get_next_topic()
        assert result.get("reason") == "due_review", (
            f"Overdue topic should take priority, got: {result}"
        )

    def test_after_all_cc_studied_falls_back_to_medicine(self):
        """Once all CC topics are studied, medicine topics should be preferred."""
        seed_curriculum(MOCK_PATH)
        # Mark all CC topics as studied
        with conn() as db:
            cc_topics = db.execute(
                "SELECT topic FROM curriculum WHERE is_critical_care = 1"
            ).fetchall()
            for (t,) in cc_topics:
                db.execute(
                    "INSERT OR IGNORE INTO topics(topic, subtopic, times_seen, status, mastery_score, "
                    "next_review_date, created_at, updated_at) "
                    "VALUES(?, '', 1, 'learning', 0.7, '2099-01-01', datetime('now'), datetime('now'))",
                    (t,),
                )
        result = get_next_topic()
        # Should still return new_coverage, and discipline should be medicine (default weight 0.8)
        assert result.get("reason") == "new_coverage"
        assert result.get("discipline") == "medicine"


# ---------------------------------------------------------------------------
# 5. set_medicine_weight / get_medicine_weight
# ---------------------------------------------------------------------------

class TestMedicineWeight:
    def test_default_weight(self):
        assert get_medicine_weight() == 0.8

    def test_set_and_get(self):
        set_medicine_weight(0.6)
        assert get_medicine_weight() == 0.6

    def test_clamp_above_1(self):
        set_medicine_weight(1.5)
        assert get_medicine_weight() == 1.0

    def test_clamp_below_0(self):
        set_medicine_weight(-0.3)
        assert get_medicine_weight() == 0.0

    def test_tool_wrapper_returns_ok(self):
        result = set_medicine_weight_tool(0.7)
        assert result["ok"] is True
        assert result["medicine_weight"] == 0.7
        assert abs(result["anesthesia_weight"] - 0.3) < 0.001
        assert get_medicine_weight() == 0.7

    def test_100_percent_medicine_no_anesthesia_slots(self):
        """With weight=1.0 and no CC topics, should always prefer medicine."""
        seed_curriculum(MOCK_PATH)
        set_medicine_weight(1.0)
        # Mark all CC topics as studied to force the non-CC path
        with conn() as db:
            cc_topics = db.execute(
                "SELECT topic FROM curriculum WHERE is_critical_care = 1"
            ).fetchall()
            for (t,) in cc_topics:
                db.execute(
                    "INSERT OR IGNORE INTO topics(topic, subtopic, times_seen, status, mastery_score, "
                    "next_review_date, created_at, updated_at) "
                    "VALUES(?, '', 1, 'learning', 0.7, '2099-01-01', datetime('now'), datetime('now'))",
                    (t,),
                )
        result = get_next_topic()
        assert result["reason"] == "new_coverage"
        assert result["discipline"] == "medicine"


# ---------------------------------------------------------------------------
# 6. priority_tier — tier 1 preferred over tier 3 in new-material selection
# ---------------------------------------------------------------------------

class TestPriorityTier:
    def test_tier1_preferred_over_tier3_medicine(self, tmp_path):
        """Tier-1 medicine topic is picked before tier-3 medicine topic when both uncovered."""
        blueprint = [
            {
                "domain": "Internal Medicine",
                "topic": "Tier3 Topic",
                "subtopics": [],
                "high_yield": True,
                "priority_tier": 3,
            },
            {
                "domain": "Internal Medicine",
                "topic": "Tier1 Topic",
                "subtopics": [],
                "high_yield": True,
                "priority_tier": 1,
            },
        ]
        bp_path = tmp_path / "tier_test_curriculum.json"
        bp_path.write_text(json.dumps(blueprint), encoding="utf-8")

        seed_curriculum(str(bp_path))

        # No due reviews, no CC topics — should fall to 2b non-CC discipline path.
        # Default medicine_weight=0.8 picks medicine first; studied_curriculum=0
        # so it's not an anesthesia slot (0 % 5 != 4).
        result = get_next_topic()

        assert result.get("reason") == "new_coverage"
        assert result.get("topic") == "Tier1 Topic", (
            f"Expected 'Tier1 Topic' (tier 1) to be picked first, got: {result.get('topic')}"
        )
        assert result.get("priority_tier") == 1

    def test_priority_tier_in_returned_dict(self, tmp_path):
        """priority_tier key is present in get_next_topic result for new_coverage."""
        blueprint = [
            {
                "domain": "Internal Medicine",
                "topic": "Some Medicine Topic",
                "subtopics": [],
                "high_yield": True,
                "priority_tier": 2,
            },
        ]
        bp_path = tmp_path / "tier_field_test.json"
        bp_path.write_text(json.dumps(blueprint), encoding="utf-8")
        seed_curriculum(str(bp_path))
        result = get_next_topic()
        assert "priority_tier" in result, "priority_tier should be in get_next_topic result"
        assert result["priority_tier"] == 2

    def test_seed_clamps_priority_tier(self, tmp_path):
        """Invalid or out-of-range priority_tier values are clamped to 1-3 or default to 2."""
        blueprint = [
            {"domain": "Internal Medicine", "topic": "Clamped High", "subtopics": [], "high_yield": True, "priority_tier": 99},
            {"domain": "Internal Medicine", "topic": "Clamped Low", "subtopics": [], "high_yield": True, "priority_tier": -5},
            {"domain": "Internal Medicine", "topic": "Default Missing", "subtopics": [], "high_yield": True},
            {"domain": "Internal Medicine", "topic": "Bad String", "subtopics": [], "high_yield": True, "priority_tier": "bad"},
        ]
        bp_path = tmp_path / "clamp_test.json"
        bp_path.write_text(json.dumps(blueprint), encoding="utf-8")
        seed_curriculum(str(bp_path))
        with conn() as db:
            rows = {
                r["topic"]: r["priority_tier"]
                for r in db.execute("SELECT topic, priority_tier FROM curriculum").fetchall()
            }
        assert rows["Clamped High"] == 3
        assert rows["Clamped Low"] == 1
        assert rows["Default Missing"] == 2
        assert rows["Bad String"] == 2


# ---------------------------------------------------------------------------
# 7. category — on-call "Approach to X" presentation topics
# ---------------------------------------------------------------------------

class TestPresentationCategory:
    def test_category_column_seeded(self):
        """Presentation topics in the mock seed with category='presentation';
        ordinary topics default to category='topic'."""
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            pres = db.execute(
                "SELECT topic FROM curriculum WHERE category = 'presentation'"
            ).fetchall()
            pres_topics = {r["topic"] for r in pres}
            ordinary = db.execute(
                "SELECT category FROM curriculum WHERE topic = 'Hyperkalemia'"
            ).fetchone()
        assert "Approach to Hypotension" in pres_topics
        assert "Approach to Fever" in pres_topics
        assert "Approach to Constipation" in pres_topics
        assert ordinary["category"] == "topic"

    def test_explicit_is_critical_care_respected(self):
        """A presentation topic with no CC keyword but explicit is_critical_care=1
        (Approach to Hypotension) is stored as CC; explicit 0 (Approach to Fever)
        stays non-CC even though 'fever' would not trigger the keyword path anyway."""
        seed_curriculum(MOCK_PATH)
        with conn() as db:
            hypo = db.execute(
                "SELECT is_critical_care FROM curriculum WHERE topic='Approach to Hypotension'"
            ).fetchone()["is_critical_care"]
            constip = db.execute(
                "SELECT is_critical_care FROM curriculum WHERE topic='Approach to Constipation'"
            ).fetchone()["is_critical_care"]
        assert hypo == 1
        assert constip == 0

    def test_mastery_map_has_on_call_approaches(self):
        seed_curriculum(MOCK_PATH)
        mm = get_mastery_map()
        assert "on_call_approaches" in mm
        assert mm["on_call_approaches"]["total"] == 3
        assert mm["on_call_approaches"]["studied"] == 0
        assert mm["on_call_approaches"]["coverage_pct"] == 0.0

    def test_on_call_coverage_rises_after_study(self):
        seed_curriculum(MOCK_PATH)
        get_or_create_topic("Approach to Hypotension", "")
        with conn() as db:
            db.execute(
                "UPDATE topics SET times_seen = 2 WHERE topic = 'Approach to Hypotension'"
            )
        mm = get_mastery_map()
        assert mm["on_call_approaches"]["studied"] == 1
        assert mm["on_call_approaches"]["coverage_pct"] == round(1 / 3 * 100, 1)

    def test_get_next_topic_surfaces_category(self):
        seed_curriculum(MOCK_PATH)
        result = get_next_topic()
        assert "category" in result
        assert result["category"] in ("topic", "presentation")

    def test_presentation_interleaved_on_third_slot(self):
        """The presentation interleave fires on slots where studied_curriculum % 3 == 1.
        With one topic already studied, the next new-coverage pick is a presentation
        topic, and the most acute (is_critical_care=1) one comes first."""
        seed_curriculum(MOCK_PATH)
        # Mark exactly one curriculum topic as studied -> studied_curriculum == 1
        get_or_create_topic("Hyperkalemia", "")
        with conn() as db:
            db.execute("UPDATE topics SET times_seen = 1 WHERE topic = 'Hyperkalemia'")
        result = get_next_topic()
        assert result.get("reason") == "new_coverage"
        assert result.get("category") == "presentation", (
            f"Expected a presentation topic on the interleave slot, got: {result.get('topic')}"
        )
        # Acute approach (is_critical_care=1) ordered first within the set
        assert result.get("topic") == "Approach to Hypotension"

    def test_non_cc_presentation_not_starved_by_cc(self):
        """Non-CC presentation topics (Fever, Constipation) must be reachable even
        while CC disease topics remain unstudied — they surface via the interleave
        ahead of the CC pass, not only after CC is exhausted."""
        seed_curriculum(MOCK_PATH)
        seen_presentation = set()
        # Walk new-coverage picks, marking each seen, for enough iterations to
        # exhaust the 3 presentation topics while CC disease topics still remain.
        for _ in range(12):
            r = get_next_topic()
            if r.get("category") == "presentation":
                seen_presentation.add(r["topic"])
            get_or_create_topic(r["topic"], "")
            with conn() as db:
                db.execute("UPDATE topics SET times_seen = 1 WHERE topic = ?", (r["topic"],))
        # All 3 presentation topics (incl. the 2 non-CC) surfaced within 12 picks,
        # well before all CC disease topics were exhausted.
        assert {"Approach to Hypotension", "Approach to Fever", "Approach to Constipation"} <= seen_presentation


# ---------------------------------------------------------------------------
# 8. knowledge_gaps — granular missed-fact persistence + resurfacing + resolve
# ---------------------------------------------------------------------------

class TestKnowledgeGaps:
    """Backward-compat 'gap' surface (a gap = a not-yet-mastered knowledge point)."""

    def test_record_and_get(self):
        record_knowledge_gap("ARDS", "low TV 6 mL/kg IBW is the mortality move, not PEEP", "recall")
        gaps = get_knowledge_gaps(topic="ARDS")
        assert len(gaps) == 1
        assert gaps[0]["gap_note"].startswith("low TV")
        assert gaps[0]["status"] == "open"

    def test_blank_note_is_noop(self):
        record_knowledge_gap("Sepsis", "")
        record_knowledge_gap("", "something")
        assert get_knowledge_gaps(status="all") == []

    def test_resolve_by_topic_masters_points(self):
        record_knowledge_gap("DKA", "hold insulin if K<3.3")
        record_knowledge_gap("DKA", "goal is closing the anion gap, not glucose")
        n = resolve_knowledge_gaps("DKA")
        assert n == 2
        assert get_knowledge_gaps(topic="DKA", status="open") == []
        assert len(get_knowledge_gaps(topic="DKA", status="resolved")) == 2

    def test_relogging_reopens_resolved_gap(self):
        record_knowledge_gap("PE", "massive PE = tPA; submassive = anticoag + monitor")
        resolve_knowledge_gaps("PE")
        assert get_knowledge_gaps(topic="PE", status="open") == []
        record_knowledge_gap("PE", "massive PE = tPA; submassive = anticoag + monitor")
        assert len(get_knowledge_gaps(topic="PE", status="open")) == 1

    def test_log_missed_topic_tool_persists_gap_and_weak(self):
        res = log_missed_topic("Hyponatremia", "ODS risk: correct <=12 mEq/L per 24h")
        assert res["ok"] is True and res["gap_logged"] is True
        gaps = get_knowledge_gaps_tool(topic="Hyponatremia")
        assert gaps["open_count"] == 1
        # Parent topic flagged weak (no junk pseudo-topic row from the long gap text)
        with conn() as db:
            rows = db.execute("SELECT subtopic, status FROM topics WHERE topic='Hyponatremia'").fetchall()
        assert all(r["subtopic"] == "" for r in rows)
        assert any(r["status"] == "weak" for r in rows)

    def test_mark_mastered_resolves_gaps(self):
        record_knowledge_gap("Shock", "obstructive: JVD + hypotension; tension PTX vs tamponade")
        mark_topic_mastered("Shock")
        assert get_knowledge_gaps(topic="Shock", status="open") == []

    def test_fact_tracked_topic_not_served_as_stale_topic_review(self):
        """Once a topic is tracked at the fact level, its old topic-level card is
        retired from the topic-review queue (handled by the knowledge-point queue),
        so get_next_topic won't keep re-serving it as a stale 'due_review'."""
        seed_curriculum(MOCK_PATH)
        get_or_create_topic("Hyperkalemia", "")
        with conn() as db:
            db.execute(
                "UPDATE topics SET times_seen=2, status='weak', mastery_score=0.2, "
                "next_review_date='2000-01-01' WHERE topic='Hyperkalemia'"
            )
        # Before fact-tracking: it IS a due topic review.
        assert any(r["topic"] == "Hyperkalemia" for r in _due_reviews(limit=50))
        # After fact-tracking: retired from the topic queue.
        record_knowledge_gap("Hyperkalemia", "calcium stabilizes membrane, does NOT lower K")
        assert not any(r["topic"] == "Hyperkalemia" for r in _due_reviews(limit=50))


# ---------------------------------------------------------------------------
# 9. knowledge_points — atomic facts, per-point confidence, independent SRS
# ---------------------------------------------------------------------------

class TestKnowledgePoints:
    def test_record_incorrect_is_weak_and_overconfident(self):
        r = record_knowledge_point("ARDS", "low TV 6 mL/kg IBW", is_correct=False, confidence=4)
        assert r["status"] == "weak"
        # FSRS schedules a missed item soon (confident-wrong gets the shortest interval)
        assert r["interval_days"] <= 1
        pts = get_knowledge_points(topic="ARDS")
        assert pts[0]["calibration"] == "overconfident"
        assert "fsrs_state" in pts[0] and pts[0]["fsrs_state"]  # per-item FSRS persisted

    def test_two_consecutive_correct_graduates_to_mastered(self):
        record_knowledge_point("AF", "3-4 wk anticoag pre-cardioversion", is_correct=True, confidence=3)
        r2 = record_knowledge_point("AF", "3-4 wk anticoag pre-cardioversion", is_correct=True, confidence=4)
        assert r2["status"] == "mastered"
        assert r2["consecutive_correct"] == 2
        assert r2["interval_days"] >= 1

    def test_miss_resets_consecutive(self):
        record_knowledge_point("Sepsis", "lactate first, cultures before abx", is_correct=True, confidence=4)
        r = record_knowledge_point("Sepsis", "lactate first, cultures before abx", is_correct=False, confidence=2)
        assert r["consecutive_correct"] == 0
        assert r["status"] == "weak"

    def test_confidence_modulates_interval(self):
        # First-exposure correct: higher confidence -> higher FSRS rating -> longer interval
        low = record_knowledge_point("T1", "fact-low", is_correct=True, confidence=1)
        high = record_knowledge_point("T2", "fact-high", is_correct=True, confidence=5)
        assert high["interval_days"] >= low["interval_days"]

    def test_submit_knowledge_points_compound(self):
        res = submit_knowledge_points("Hyperkalemia", [
            {"point": "calcium stabilizes membrane, does NOT lower K", "correct": True, "confidence": 4},
            {"point": "insulin+D50 shifts K intracellularly", "correct": True, "confidence": 5},
            {"point": "kayexalate/dialysis eliminates K", "correct": False, "confidence": 4, "mistake_type": "recall"},
        ])
        assert res["recorded"] == 3
        assert "kayexalate/dialysis eliminates K" in res["weak_or_learning"]
        oc = get_knowledge_points_tool()["overconfident"]
        assert any("kayexalate" in p for p in oc)

    def test_weak_point_surfaces_and_due_query_works(self):
        # A missed point is 'weak' (surfaces same-session via status) and, once its
        # scheduled date arrives, appears in the due queue.
        record_knowledge_point("Airway", "subacute SCI: sux -> K surge; use roc", is_correct=False, confidence=3)
        weak = get_knowledge_points_tool(status="weak")
        assert any(p["point"].startswith("subacute SCI") for p in weak["points"])
        # Force the schedule into the past to exercise the due query mechanism.
        with conn() as db:
            db.execute("UPDATE knowledge_points SET next_review_date='2000-01-01' "
                       "WHERE point LIKE 'subacute SCI%'")
        due = get_due_knowledge_points_tool()
        assert due["count"] >= 1
        assert any(p["point"].startswith("subacute SCI") for p in due["due_points"])

    def test_mastered_point_not_due(self):
        record_knowledge_point("DKA", "hold insulin if K<3.3", is_correct=True, confidence=4)
        record_knowledge_point("DKA", "hold insulin if K<3.3", is_correct=True, confidence=4)
        due_points = get_due_knowledge_points()
        assert not any(p["point"] == "hold insulin if K<3.3" for p in due_points)

    def test_session_state_surfaces_weak_points(self):
        record_knowledge_point("Airway", "CICO -> cricothyrotomy, declare early", is_correct=False, confidence=2)
        ss = get_session_state()
        # weak points surface via open_knowledge_gaps (status-based, same-session)
        assert any(g["topic"] == "Airway" for g in ss["open_knowledge_gaps"])
        assert "load" in ss and ss["load"]["daily_new_item_cap"] >= 1

    def test_blank_point_is_noop(self):
        assert record_knowledge_point("X", "", is_correct=True) is None
        assert record_knowledge_point("", "y", is_correct=True) is None


# ---------------------------------------------------------------------------
# 10. Daily load economics — new-item cap bounds intake
# ---------------------------------------------------------------------------

class TestDailyLoad:
    def test_new_item_cap_stops_new_topics(self):
        from src.student_model import set_int_setting, log_attempt
        seed_curriculum(MOCK_PATH)
        set_int_setting("daily_new_item_cap", 2)
        introduced = 0
        for _ in range(6):
            nt = get_next_topic()
            if nt.get("reason") == "daily_new_limit_reached":
                break
            introduced += 1
            log_attempt(session_id="s", topic=nt["topic"], subtopic="", question="q",
                        user_answer="a", ideal_answer="", result="correct", mistake_type="other",
                        difficulty="medium", hints_used=0, confidence_reported=3,
                        retrieval_sources="", source_citations="", notes="", library="",
                        training_phase="intern_year")
        assert introduced == 2
        nt = get_next_topic()
        assert nt["reason"] == "daily_new_limit_reached"
        assert nt["new_items_today"] >= 2

    def test_due_reviews_not_capped(self):
        """A due review must still be served even after the new-item cap is hit."""
        from src.student_model import set_int_setting
        seed_curriculum(MOCK_PATH)
        set_int_setting("daily_new_item_cap", 0)  # no new items allowed
        get_or_create_topic("Hyperkalemia", "")
        with conn() as db:
            db.execute("UPDATE topics SET times_seen=2, status='weak', mastery_score=0.2, "
                       "next_review_date='2000-01-01' WHERE topic='Hyperkalemia'")
        nt = get_next_topic()
        assert nt["reason"] == "due_review"
        assert nt["topic"] == "Hyperkalemia"

    def test_load_surfaced_in_session_state(self):
        ss = get_session_state()
        assert "load" in ss
        assert ss["load"]["daily_new_item_cap"] == 20  # default
        assert ss["load"]["new_items_remaining_today"] <= 20


# ---------------------------------------------------------------------------
# 11. Clinical-reasoning structures: illness scripts, confusable pairs, bloom
# ---------------------------------------------------------------------------

class TestClinicalReasoning:
    def test_illness_script_roundtrip(self):
        from src.student_model import upsert_illness_script, get_illness_script
        upsert_illness_script("PE", enabling_conditions="post-op, immobility",
                              pathophysiology="clot -> V/Q mismatch", time_course="acute",
                              key_features="pleuritic CP, hypoxia", consequence_if_missed="arrest")
        s = get_illness_script("PE")
        assert s and s["key_features"] == "pleuritic CP, hypoxia"
        # update is idempotent
        upsert_illness_script("PE", key_features="updated features")
        assert get_illness_script("PE")["key_features"] == "updated features"

    def test_confusable_pair_canonical_dedup(self):
        from src.student_model import add_confusable_pair, get_confusable_pairs
        add_confusable_pair("Tension PTX", "Tamponade", "breath sounds vs heart tones")
        add_confusable_pair("Tamponade", "Tension PTX", "")  # reversed order -> same row
        pairs_a = get_confusable_pairs("Tension PTX")
        assert len(pairs_a) == 1
        assert pairs_a[0]["confused_with"] == "Tamponade"
        assert "breath sounds" in pairs_a[0]["discriminator"]
        # queryable from either side
        assert get_confusable_pairs("Tamponade")[0]["confused_with"] == "Tension PTX"

    def test_get_contrastive_case_tool(self):
        from src.mcp_server import add_confusable_pair as add_tool, get_contrastive_case
        add_tool("SIADH", "Cerebral Salt Wasting", "volume status: euvolemic vs hypovolemic")
        cc = get_contrastive_case("SIADH")
        assert cc["count"] == 1
        assert cc["confusables"][0]["confused_with"] == "Cerebral Salt Wasting"

    def test_bloom_level_recorded(self):
        from src.student_model import log_attempt
        log_attempt(session_id="s", topic="Sepsis", subtopic="", question="q", user_answer="a",
                    ideal_answer="", result="correct", bloom_level="apply")
        with conn() as db:
            bl = db.execute("SELECT bloom_level FROM question_attempts WHERE topic='Sepsis'").fetchone()[0]
        assert bl == "apply"

    def test_get_progress_real_discipline_metrics(self):
        from src.student_model import get_or_create_topic
        seed_curriculum(MOCK_PATH)
        # study one medicine + one anesthesia curriculum topic
        for t in ("Hyperkalemia", "Airway Management"):
            get_or_create_topic(t, "")
            with conn() as db:
                db.execute("UPDATE topics SET times_seen=2 WHERE topic=?", (t,))
        from src.mcp_endpoints import get_progress
        pr = get_progress()
        # real per-discipline coverage (not fixed multipliers of overall)
        assert pr["intern_medicine_pct"] > 0
        assert pr["anesthesia_pct"] > 0


# ---------------------------------------------------------------------------
# 10. Backend fixes from session review: kp advancement, stale-card retire,
#     KP-aware coverage
# ---------------------------------------------------------------------------

class TestBackendFixes:
    def _seed_catalog(self, n=6):
        from src.student_model import now
        with conn() as db:
            for i in range(n):
                db.execute(
                    "INSERT OR REPLACE INTO kp_catalog(id, topic, discipline, stem, answer, "
                    "tier, category, is_critical_care, car_safe, times_seen, added_at) "
                    "VALUES(?,?,?,?,?,?,?,?,?,0,?)",
                    (f"kp-{i}", "Anemia", "medicine", f"stem {i}", f"ans {i}",
                     1, "topic", 0, 0, now()),
                )

    def test_get_kp_to_study_advances_not_repeats(self):
        self._seed_catalog(6)
        a = [k["id"] for k in get_kp_to_study(limit=3)]
        b = [k["id"] for k in get_kp_to_study(limit=3)]
        assert len(a) == 3 and len(b) == 3
        assert set(a).isdisjoint(b), f"get_kp_to_study repeated: {a} then {b}"

    def test_due_reviews_excludes_fact_tracked_topics(self):
        # A topic that is overdue at the topic level...
        get_or_create_topic("Sepsis", "")
        with conn() as db:
            db.execute(
                "UPDATE topics SET times_seen=3, status='weak', mastery_score=0.2, "
                "next_review_date='2000-01-01' WHERE topic='Sepsis'"
            )
        assert any(r["topic"] == "Sepsis" for r in _due_reviews(limit=50))
        # ...becomes fact-tracked -> its stale topic card drops out of the queue
        record_knowledge_point("Sepsis", "lactate first", is_correct=False)
        assert not any(r["topic"] == "Sepsis" for r in _due_reviews(limit=50))

    def test_mastery_map_reports_knowledge_points(self):
        record_knowledge_point("DKA", "hold insulin if K<3.5", is_correct=True, confidence=4)
        mm = get_mastery_map()
        assert "knowledge_points" in mm
        assert mm["knowledge_points"]["facts_tracked"] >= 1

    def test_mastery_map_coverage_counts_fact_tracked_topics(self):
        seed_curriculum(MOCK_PATH)
        before = get_mastery_map()["topics_studied"]
        # Study a curriculum topic purely at the fact level (no topics.times_seen)
        record_knowledge_point("Hyperkalemia", "calcium stabilizes membrane", is_correct=True)
        after = get_mastery_map()["topics_studied"]
        assert after >= before + 1
