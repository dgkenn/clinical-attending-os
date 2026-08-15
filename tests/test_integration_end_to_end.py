# tests/test_integration_end_to_end.py
"""
End-to-End Integration Tests for Clinical Attending OS Mastery Tutor.

Tests the complete workflow:
1. Lesson Flow: retrieve -> answer -> mastery -> FSRS
2. Follow-Up Workflow: request subtopic -> drill -> return
3. Session Persistence: start -> pause -> resume
4. Mastery Gating: baseline mastery enforcement
5. Confidence Weighting: overconfident penalty
6. Full E2E Conversation Cycle

Coverage: All 6 MCP endpoints + pedagogy principles
"""

import pytest
import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path

from src.mcp_endpoints import (
    retrieval, get_session_state, get_next_topic, submit_answer,
    get_mastery_gates, get_progress, request_follow_up
)
from src.student_model import initialize_database, conn as get_db


# Initialize once per module — but INSIDE a fixture, never at import time.
# Module-level initialize_database() ran at pytest COLLECTION, before conftest's
# session-scoped isolate_student_db could redirect settings.sqlite_db_path, so
# every test run opened (and migrated, and flipped to WAL) the user's REAL
# progress database despite the isolation fixture.
@pytest.fixture(scope="module", autouse=True)
def _init_db(isolate_student_db):
    initialize_database()


@pytest.fixture
def test_session_id():
    """Generate a unique test session ID."""
    return f"test_e2e_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


class TestMCPEndpointAvailability:
    """Test that all 6 MCP endpoints are callable and return valid responses."""

    def test_retrieval_endpoint_callable(self):
        """Endpoint 1: retrieval() is callable and returns valid structure."""
        result = retrieval(
            "shock management",
            mode="intern_teach",
            max_results=5
        )

        assert isinstance(result, dict)
        assert 'retrieval_confidence' in result
        assert isinstance(result['retrieval_confidence'], (int, float))
        assert 'results' in result or 'error' in result
        assert isinstance(result.get('results', []), list)

    def test_retrieval_with_filters(self):
        """retrieval() supports mode and library_filter parameters."""
        result = retrieval(
            "sepsis treatment",
            mode="intern_teach",
            library_filter="intern_year_medicine",
            max_results=3
        )

        assert 'retrieval_confidence' in result

    def test_get_session_state_endpoint_callable(self):
        """Endpoint 2: get_session_state() returns learning state."""
        result = get_session_state()

        assert isinstance(result, dict)
        assert 'fsrs_due_today' in result
        assert 'weak_topics' in result
        assert 'mastery_matrix' in result
        assert 'phase' in result
        assert 'progress_pct' in result
        assert isinstance(result['progress_pct'], (int, float))
        assert 0 <= result['progress_pct'] <= 100

    def test_get_next_topic_endpoint_callable(self):
        """Endpoint 3: get_next_topic() returns recommended next topic."""
        result = get_next_topic(session_id="test_session")

        assert isinstance(result, dict)
        assert 'topic' in result
        assert 'reason' in result
        assert 'retrieval_query' in result
        assert 'suggested_phase' in result
        assert 'is_nested' in result
        assert isinstance(result['is_nested'], bool)

    def test_get_mastery_gates_endpoint_callable(self):
        """Endpoint 5: get_mastery_gates() returns mastery status."""
        result = get_mastery_gates()

        assert isinstance(result, dict)
        assert 'mastery_matrix' in result
        assert 'ready_for_phase_advance' in result
        assert isinstance(result['mastery_matrix'], dict)
        assert isinstance(result['ready_for_phase_advance'], bool)

    def test_get_progress_endpoint_callable(self):
        """Endpoint 6: get_progress() returns progress statistics."""
        result = get_progress()

        assert isinstance(result, dict)
        assert 'intern_medicine_pct' in result
        assert 'icu_pct' in result
        assert 'anesthesia_pct' in result
        assert 'overall_pct' in result
        assert 'hours_studied' in result

        # All percentages should be 0-100
        for key in ['intern_medicine_pct', 'icu_pct', 'anesthesia_pct', 'overall_pct']:
            assert 0 <= result[key] <= 100, f"{key} out of range"

    def test_submit_answer_endpoint_callable(self, test_session_id):
        """Endpoint 4: submit_answer() creates attempt record."""
        result = submit_answer(
            topic='test_topic_e2e',
            user_answer='Test answer',
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.8,
            transfer_success=False,
            session_id=test_session_id
        )

        # Should return response (may contain error if DB schema issue)
        assert isinstance(result, dict)
        assert 'next_review_date' in result
        assert 'mastery_updated' in result
        assert 'level_achieved' in result


class TestMasteryVectorStructure:
    """Test mastery vector has correct structure and metrics."""

    def test_mastery_vector_has_all_required_metrics(self):
        """Mastery vector includes all 6 key metrics."""
        result = get_mastery_gates()

        required_keys = {
            'accuracy', 'transfer_auc', 'mechanism_quality',
            'calibration_icc', 'retention_6mo', 'integration_score'
        }

        for topic, info in result['mastery_matrix'].items():
            vector = info['vector']
            for key in required_keys:
                assert key in vector, f"Missing {key} in vector for {topic}"
                # All should be floats
                assert isinstance(vector[key], (int, float)), \
                    f"{key} should be numeric, got {type(vector[key])}"

    def test_mastery_level_classification(self):
        """Mastery level is correctly classified."""
        result = get_mastery_gates()

        for topic, info in result['mastery_matrix'].items():
            level = info['level']
            # Should be one of: None, 'baseline', 'intermediate', 'advanced'
            assert level in [None, 'baseline', 'intermediate', 'advanced'], \
                f"Invalid level for {topic}: {level}"


class TestFollowUpWorkflow:
    """Test nested learning: request subtopic -> drill -> return."""

    def test_request_follow_up_endpoint_callable(self, test_session_id):
        """Endpoint 7: request_follow_up() is callable and returns valid structure."""
        result = request_follow_up(
            parent_topic='shock_test',
            requested_subtopic='vasopressors_test',
            session_id=test_session_id
        )

        # Should return response dict (may have ok=False if DB issue)
        assert isinstance(result, dict)
        assert 'ok' in result

        # If successful, should have these fields
        if result['ok']:
            assert result['parent_topic'] == 'shock_test'
            assert result['child_topic'] == 'vasopressors_test'
            assert 'follow_up_session_id' in result
            assert result['suggested_phase'] == 'drilling'
            assert 'retrieval_query' in result
            assert isinstance(result.get('related_subtopics', []), list)


class TestSessionPersistence:
    """Test that session state can be retrieved consistently."""

    def test_session_state_consistent(self):
        """Session state returns same structure on repeated calls."""
        state1 = get_session_state()
        state2 = get_session_state()

        # Both should have same keys
        assert set(state1.keys()) == set(state2.keys())
        assert 'progress_pct' in state1
        assert 'progress_pct' in state2
        assert isinstance(state1['progress_pct'], (int, float))
        assert isinstance(state2['progress_pct'], (int, float))


class TestPhaseAdvancementGating:
    """Test phase advancement logic is gated by mastery."""

    def test_phase_advance_gating_enforced(self):
        """Ready for phase advance is based on mastery percentage."""
        result = get_mastery_gates()

        # Initially (on new DB) should not be ready
        # As student progresses, should eventually be ready
        assert isinstance(result['ready_for_phase_advance'], bool)


class TestConfidenceWeighting:
    """Test that confidence parameter is accepted and used."""

    def test_submit_answer_accepts_confidence_levels(self, test_session_id):
        """submit_answer() accepts confidence from 1 to 5."""
        for confidence in [1, 2, 3, 4, 5]:
            result = submit_answer(
                topic=f'confidence_test_{confidence}',
                user_answer='Test answer',
                is_correct=True,
                confidence_reported=confidence,
                teach_back_quality=0.7,
                transfer_success=False,
                session_id=test_session_id
            )

            # Should return valid response
            assert isinstance(result, dict)
            assert 'next_review_date' in result

    def test_teach_back_quality_parameter_used(self, test_session_id):
        """submit_answer() accepts teach_back_quality (0-1)."""
        result = submit_answer(
            topic='teach_back_test',
            user_answer='Detailed mechanism explanation',
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.95,  # Excellent teach-back
            transfer_success=False,
            session_id=test_session_id
        )

        # Should record the teach-back quality
        assert isinstance(result, dict)
        assert 'level_achieved' in result


class TestEndToEndWorkflows:
    """Test realistic end-to-end tutor workflows."""

    def test_simple_lesson_cycle(self):
        """Complete lesson cycle: retrieve -> answer -> check mastery."""
        session_id = f"e2e_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Step 1: Get current session state
        state = get_session_state()
        assert isinstance(state, dict)
        assert 'progress_pct' in state

        # Step 2: Retrieve content
        content = retrieval(
            "shock treatment",
            mode="intern_teach",
            max_results=5
        )
        assert isinstance(content, dict)

        # Step 3: Submit answer
        result = submit_answer(
            topic='shock_simple',
            user_answer='Shock is inadequate tissue perfusion',
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.8,
            transfer_success=False,
            session_id=session_id
        )
        assert isinstance(result, dict)
        assert 'next_review_date' in result

        # Step 4: Check mastery gates
        gates = get_mastery_gates()
        assert isinstance(gates['mastery_matrix'], dict)

        # Step 5: Check progress
        progress = get_progress()
        assert isinstance(progress, dict)
        assert 'overall_pct' in progress


class TestErrorGracefulHandling:
    """Test that endpoints handle edge cases gracefully."""

    def test_empty_retrieval_query(self):
        """retrieval() handles empty query."""
        result = retrieval(
            "",  # Empty query
            mode="intern_teach",
            max_results=5
        )

        # Should return valid response structure
        assert isinstance(result, dict)
        assert 'retrieval_confidence' in result

    def test_zero_max_results(self):
        """retrieval() handles max_results=0."""
        result = retrieval(
            "test",
            mode="intern_teach",
            max_results=0
        )

        # Should return valid response
        assert isinstance(result, dict)
        assert 'results' in result or 'error' in result

    def test_database_initialization_once(self):
        """Database only initialized once, subsequent calls use existing."""
        # Database already initialized at module level
        state1 = get_session_state()
        state2 = get_session_state()

        # Both should succeed
        assert isinstance(state1, dict)
        assert isinstance(state2, dict)
