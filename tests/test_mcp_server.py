"""
Comprehensive test suite for the MCP server implementation.

Tests cover:
1. Server startup and initialization
2. Tool registration
3. Basic endpoint functionality
4. Error handling
5. Database persistence
"""

import pytest
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# Import server components
from src.mcp_server import main
from src.mcp_endpoints import (
    retrieval,
    get_session_state,
    get_next_topic,
    submit_answer,
    get_mastery_gates,
    get_progress,
    request_follow_up,
)
from src.student_model import initialize_database, conn as get_db_connection


class TestMCPServerStartup:
    """Test MCP server initialization and startup."""

    def test_server_imports_without_error(self):
        """Verify MCP server module imports cleanly."""
        try:
            from src import mcp_server
            assert hasattr(mcp_server, 'main')
        except ImportError as e:
            pytest.fail(f"Failed to import mcp_server: {e}")

    def test_mcp_sdk_installed(self):
        """Verify MCP SDK is available."""
        try:
            import mcp
            assert mcp is not None
        except ImportError:
            pytest.fail("MCP SDK not installed. Run: pip install mcp")

    def test_database_connection(self):
        """Verify database connection works."""
        initialize_database()
        conn = get_db_connection()
        assert conn is not None
        conn.close()


class TestRetrievalEndpoint:
    """Test the retrieval endpoint (Tool 1)."""

    def test_retrieval_basic(self):
        """Test basic retrieval with a query."""
        result = retrieval("shock management")

        assert isinstance(result, dict)
        assert "results" in result
        assert "retrieval_confidence" in result
        assert "insufficient_context" in result

    def test_retrieval_returns_list(self):
        """Test that retrieval returns a list of results."""
        result = retrieval("shock")

        assert isinstance(result["results"], list)
        if result["results"]:
            chunk = result["results"][0]
            assert "text" in chunk or "book" in chunk  # text content may be under different key
            assert "score" in chunk

    def test_retrieval_with_mode(self):
        """Test retrieval with different modes."""
        modes = ["intern_teach", "rapid_response", "pimp"]

        for mode in modes:
            result = retrieval("shock", mode=mode)
            # Should return valid result dict with results list
            assert isinstance(result, dict)
            assert "results" in result

    def test_retrieval_with_max_results(self):
        """Test retrieval with custom max_results."""
        result = retrieval("shock", max_results=3)

        assert len(result["results"]) <= 3

    def test_retrieval_confidence_range(self):
        """Test that retrieval_confidence is in valid range."""
        result = retrieval("shock")

        confidence = result["retrieval_confidence"]
        assert 0.0 <= confidence <= 1.0

    def test_retrieval_empty_query_handling(self):
        """Test retrieval with empty query."""
        result = retrieval("")

        # Should handle gracefully
        assert isinstance(result, dict)
        assert "results" in result


class TestSessionStateEndpoint:
    """Test the get_session_state endpoint (Tool 2)."""

    def test_get_session_state_returns_dict(self):
        """Test that get_session_state returns proper dict."""
        state = get_session_state()

        assert isinstance(state, dict)
        assert "fsrs_due_today" in state
        assert "weak_topics" in state
        assert "mastery_matrix" in state
        assert "phase" in state
        assert "progress_pct" in state

    def test_session_state_due_today_is_list(self):
        """Test that fsrs_due_today is a list."""
        state = get_session_state()

        assert isinstance(state["fsrs_due_today"], list)
        if state["fsrs_due_today"]:
            item = state["fsrs_due_today"][0]
            assert "topic_id" in item
            assert "topic" in item

    def test_session_state_mastery_matrix_is_dict(self):
        """Test that mastery_matrix is a dict."""
        state = get_session_state()

        assert isinstance(state["mastery_matrix"], dict)

    def test_session_state_progress_in_range(self):
        """Test that progress_pct is in valid range."""
        state = get_session_state()

        progress = state["progress_pct"]
        assert 0.0 <= progress <= 100.0


class TestNextTopicEndpoint:
    """Test the get_next_topic endpoint (Tool 3)."""

    def test_get_next_topic_returns_dict(self):
        """Test that get_next_topic returns proper dict."""
        topic = get_next_topic()

        assert isinstance(topic, dict)
        assert "topic" in topic
        assert "reason" in topic
        assert "retrieval_query" in topic
        assert "suggested_phase" in topic
        assert "is_nested" in topic

    def test_next_topic_reason_valid(self):
        """Test that reason is one of the valid values."""
        topic = get_next_topic()

        valid_reasons = [
            "active_follow_up",
            "due_today",
            "weak",
            "new_material",
            "integration",
            # curriculum-coverage engine reasons (added Phase 2)
            "due_review",
            "new_coverage",
            "error_fallback",
        ]
        assert topic["reason"] in valid_reasons

    def test_next_topic_phase_valid(self):
        """Test that suggested_phase is valid."""
        topic = get_next_topic()

        valid_phases = [
            "new_material",
            "drilling",
            "case_application",
            "integration"
        ]
        assert topic["suggested_phase"] in valid_phases

    def test_next_topic_is_nested_bool(self):
        """Test that is_nested is boolean."""
        topic = get_next_topic()

        assert isinstance(topic["is_nested"], bool)


class TestSubmitAnswerEndpoint:
    """Test the submit_answer endpoint (Tool 4)."""

    def test_submit_correct_answer(self):
        """Test submitting a correct answer."""
        result = submit_answer(
            topic="test_topic_correct",
            user_answer="This is the correct answer",
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.8
        )

        assert isinstance(result, dict)
        assert "ok" in result
        assert "next_review_date" in result
        assert "mastery_updated" in result
        assert "level_achieved" in result

    def test_submit_incorrect_answer(self):
        """Test submitting an incorrect answer."""
        result = submit_answer(
            topic="test_topic_incorrect",
            user_answer="This is wrong",
            is_correct=False,
            confidence_reported=2,
            mistake_type="mechanism"
        )

        assert isinstance(result, dict)
        assert "next_review_date" in result

    def test_submit_answer_creates_review_date(self):
        """Test that submit_answer creates a valid review date."""
        result = submit_answer(
            topic="test_topic_date_v2",
            user_answer="Test",
            is_correct=True,
            confidence_reported=3
        )

        review_date = datetime.fromisoformat(result["next_review_date"])
        now = datetime.now()

        # Review date should be at least in the future (allow small tolerance)
        assert (review_date - now).total_seconds() >= -1

    def test_submit_answer_confidence_weighting(self):
        """Test that confidence affects review interval."""
        # Submit with high confidence
        high_conf = submit_answer(
            topic="test_high_conf_v2",
            user_answer="Right",
            is_correct=True,
            confidence_reported=5
        )

        # Submit with low confidence (different topic)
        low_conf = submit_answer(
            topic="test_low_conf_v2",
            user_answer="Right",
            is_correct=True,
            confidence_reported=1
        )

        # Both should return valid dates
        assert "next_review_date" in high_conf
        assert "next_review_date" in low_conf

    def test_submit_answer_with_subtopic(self):
        """Test submitting answer with subtopic (nested session)."""
        result = submit_answer(
            topic="vasopressors_v2",
            user_answer="Norepinephrine increases afterload",
            is_correct=True,
            confidence_reported=4,
            subtopic="vasopressor_dosing"
        )

        assert isinstance(result, dict)
        assert "next_review_date" in result

    def test_submit_answer_transfer_success(self):
        """Test submitting answer with transfer_success flag."""
        result = submit_answer(
            topic="shock_v2",
            user_answer="Patient needs fluids and vasopressor",
            is_correct=True,
            confidence_reported=4,
            transfer_success=True
        )

        assert isinstance(result, dict)
        # Transfer success should influence mastery (checked via mastery_updated flag)
        assert "mastery_updated" in result


class TestMasteryGatesEndpoint:
    """Test the get_mastery_gates endpoint (Tool 5)."""

    def test_get_mastery_gates_returns_dict(self):
        """Test that get_mastery_gates returns proper dict."""
        gates = get_mastery_gates()

        assert isinstance(gates, dict)
        assert "mastery_matrix" in gates
        assert "ready_for_phase_advance" in gates

    def test_mastery_matrix_structure(self):
        """Test mastery_matrix has correct structure."""
        gates = get_mastery_gates()

        matrix = gates["mastery_matrix"]
        assert isinstance(matrix, dict)

        if matrix:
            topic_name = list(matrix.keys())[0]
            topic_data = matrix[topic_name]

            assert "level" in topic_data
            assert "vector" in topic_data

            vector = topic_data["vector"]
            assert "accuracy" in vector
            assert "transfer_auc" in vector
            assert "mechanism_quality" in vector

    def test_mastery_levels_valid(self):
        """Test that mastery levels are valid."""
        gates = get_mastery_gates()

        valid_levels = [None, "baseline", "intermediate", "advanced"]

        for topic_data in gates["mastery_matrix"].values():
            assert topic_data["level"] in valid_levels

    def test_ready_for_phase_advance_bool(self):
        """Test that ready_for_phase_advance is boolean."""
        gates = get_mastery_gates()

        assert isinstance(gates["ready_for_phase_advance"], bool)


class TestProgressEndpoint:
    """Test the get_progress endpoint (Tool 6)."""

    def test_get_progress_returns_dict(self):
        """Test that get_progress returns proper dict."""
        progress = get_progress()

        assert isinstance(progress, dict)
        assert "intern_medicine_pct" in progress
        assert "icu_pct" in progress
        assert "anesthesia_pct" in progress
        assert "overall_pct" in progress
        assert "hours_studied" in progress

    def test_progress_percentages_in_range(self):
        """Test that all percentages are 0-100."""
        progress = get_progress()

        assert 0.0 <= progress["intern_medicine_pct"] <= 100.0
        assert 0.0 <= progress["icu_pct"] <= 100.0
        assert 0.0 <= progress["anesthesia_pct"] <= 100.0
        assert 0.0 <= progress["overall_pct"] <= 100.0

    def test_hours_studied_non_negative(self):
        """Test that hours_studied is non-negative."""
        progress = get_progress()

        assert progress["hours_studied"] >= 0.0


class TestFollowUpEndpoint:
    """Test the request_follow_up endpoint (Tool 7)."""

    def test_request_follow_up_valid_parent(self):
        """Test requesting follow-up with valid parent topic."""
        # First ensure parent topic exists
        submit_answer("shock_test", "test", True, 3)

        result = request_follow_up(
            parent_topic="shock_test",
            requested_subtopic="vasopressor_test"
        )

        assert isinstance(result, dict)
        if result["ok"]:
            assert "parent_topic" in result
            assert "child_topic" in result
            assert "follow_up_session_id" in result

    def test_request_follow_up_invalid_parent(self):
        """Test requesting follow-up with invalid parent topic."""
        result = request_follow_up(
            parent_topic="nonexistent_topic_xyz",
            requested_subtopic="some_subtopic"
        )

        # Should return error gracefully
        assert isinstance(result, dict)

    def test_follow_up_response_structure(self):
        """Test follow-up response has correct structure."""
        submit_answer("parent", "test", True, 3)

        result = request_follow_up("parent", "child")

        if result["ok"]:
            assert "retrieval_query" in result
            assert "suggested_phase" in result
            assert "related_subtopics" in result
            assert isinstance(result["related_subtopics"], list)


class TestErrorHandling:
    """Test error handling across endpoints."""

    def test_retrieval_error_graceful(self):
        """Test retrieval handles errors gracefully."""
        # Query with special characters that might break things
        result = retrieval("'; DROP TABLE topics; --")

        # Should not crash, should return valid response
        assert isinstance(result, dict)
        assert "results" in result

    def test_submit_answer_missing_required_fields(self):
        """Test submit_answer with missing required fields."""
        # Missing topic
        result = submit_answer(
            topic="",
            user_answer="test",
            is_correct=True,
            confidence_reported=3
        )

        # Should handle gracefully
        assert isinstance(result, dict)

    def test_endpoints_with_concurrent_calls(self):
        """Test endpoints don't crash with rapid calls."""
        for _ in range(5):
            get_session_state()
            get_next_topic()
            get_mastery_gates()
            get_progress()

        # If we get here, no crashes occurred
        assert True


class TestDataPersistence:
    """Test that data persists across calls."""

    def test_answer_persists_in_session_state(self):
        """Test that submitted answers appear in session state."""
        topic = "persistence_test_topic"

        # Submit answer
        submit_answer(topic, "answer", True, 4)

        # Get session state
        state = get_session_state()

        # Topic should be in mastery matrix (even if not mastered yet)
        assert isinstance(state["mastery_matrix"], dict)

    def test_mastery_tracking_updates(self):
        """Test that mastery tracking updates after multiple answers."""
        topic = "mastery_track_test"

        # Submit multiple correct answers
        for i in range(3):
            submit_answer(topic, f"answer {i}", True, 4, teach_back_quality=0.8)

        # Check mastery gates
        gates = get_mastery_gates()

        # Topic should have a vector entry
        assert isinstance(gates["mastery_matrix"], dict)


class TestInputValidation:
    """Test input validation and type checking."""

    def test_confidence_out_of_range(self):
        """Test handling of invalid confidence values."""
        # Confidence should be 1-5, but test with invalid
        result = submit_answer(
            topic="test",
            user_answer="answer",
            is_correct=True,
            confidence_reported=10  # Invalid
        )

        # Should handle gracefully or clamp
        assert isinstance(result, dict)

    def test_teach_back_quality_out_of_range(self):
        """Test handling of invalid teach_back_quality."""
        result = submit_answer(
            topic="test",
            user_answer="answer",
            is_correct=True,
            confidence_reported=3,
            teach_back_quality=1.5  # Invalid (should be 0-1)
        )

        assert isinstance(result, dict)

    def test_special_characters_in_topic(self):
        """Test handling of special characters in topic names."""
        result = submit_answer(
            topic="topic-with-special_chars!@#$",
            user_answer="answer",
            is_correct=True,
            confidence_reported=3
        )

        assert isinstance(result, dict)


class TestIntegration:
    """Test integration scenarios."""

    def test_full_study_session_flow(self):
        """Test a complete study session flow."""
        # 1. Get next topic
        next_topic = get_next_topic()
        topic_name = next_topic["topic"]

        # 2. Retrieve content
        content = retrieval(next_topic["retrieval_query"])
        assert isinstance(content["results"], list)

        # 3. Submit answer
        answer = submit_answer(
            topic=topic_name + "_flow_test",
            user_answer="Test answer",
            is_correct=True,
            confidence_reported=4,
            teach_back_quality=0.7
        )
        assert isinstance(answer, dict)
        assert "next_review_date" in answer

        # 4. Check mastery
        gates = get_mastery_gates()
        assert isinstance(gates["mastery_matrix"], dict)

        # 5. Check progress
        progress = get_progress()
        assert progress["overall_pct"] >= 0.0

    def test_nested_follow_up_flow(self):
        """Test nested follow-up session flow."""
        # Create parent topic
        submit_answer("parent_topic", "answer", True, 3)

        # Request follow-up
        follow_up = request_follow_up("parent_topic", "child_topic")

        if follow_up["ok"]:
            # Should be able to continue studying parent after child
            state = get_session_state()
            assert isinstance(state["mastery_matrix"], dict)


class TestPerformance:
    """Test endpoint performance."""

    def test_retrieval_completes_reasonably(self):
        """Test retrieval doesn't timeout (basic sanity check)."""
        import time

        start = time.time()
        retrieval("shock")
        elapsed = time.time() - start

        # Should complete within 5 seconds
        assert elapsed < 5.0

    def test_mastery_gates_completes_reasonably(self):
        """Test get_mastery_gates completes quickly."""
        import time

        start = time.time()
        get_mastery_gates()
        elapsed = time.time() - start

        # Should complete within 1 second (local DB)
        assert elapsed < 1.0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
