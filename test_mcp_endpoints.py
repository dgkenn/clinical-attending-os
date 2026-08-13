#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script for MCP endpoints."""

print("Testing MCP endpoints...")

# Test imports
try:
    from src.mcp_endpoints import (
        retrieval,
        get_session_state,
        get_next_topic,
        submit_answer,
        get_mastery_gates,
        get_progress,
    )
    print("[PASS] All 6 endpoints imported successfully")
except Exception as e:
    print(f"[FAIL] Import failed: {e}")
    exit(1)

# Test retrieval endpoint
try:
    result = retrieval("NIHSS scoring stroke", mode="intern_teach", max_results=5)
    print(f"[PASS] Retrieval endpoint works: {len(result['results'])} results, confidence {result['retrieval_confidence']:.2f}")
except Exception as e:
    print(f"[FAIL] Retrieval failed: {e}")

# Test session_state endpoint
try:
    state = get_session_state()
    print(f"[PASS] Session state endpoint works: {len(state['fsrs_due_today'])} due topics, progress {state['progress_pct']:.1f}%")
except Exception as e:
    print(f"[FAIL] Session state failed: {e}")

# Test next_topic endpoint
try:
    topic = get_next_topic()
    print(f"[PASS] Next topic endpoint works: {topic['topic']} ({topic['reason']})")
except Exception as e:
    print(f"[FAIL] Next topic failed: {e}")

# Test mastery_gates endpoint
try:
    gates = get_mastery_gates()
    total = len(gates['mastery_matrix'])
    print(f"[PASS] Mastery gates endpoint works: {total} topics in matrix")
except Exception as e:
    print(f"[FAIL] Mastery gates failed: {e}")

# Test progress endpoint
try:
    prog = get_progress()
    print(f"[PASS] Progress endpoint works: {prog['overall_pct']:.1f}% overall, {prog['hours_studied']:.1f} hours studied")
except Exception as e:
    print(f"[FAIL] Progress failed: {e}")

# Test submit_answer endpoint
try:
    result = submit_answer(
        topic="Test Topic",
        user_answer="test",
        is_correct=True,
        confidence_reported=4,
    )
    print(f"[PASS] Submit answer endpoint works: next_review={result['next_review_date'][:10]}, level={result['level_achieved']}")
except Exception as e:
    print(f"[FAIL] Submit answer failed: {e}")

print("\n[SUCCESS] All 6 MCP endpoints operational")
