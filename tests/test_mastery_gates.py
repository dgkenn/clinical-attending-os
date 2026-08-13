# tests/test_mastery_gates.py

import sqlite3
import pytest
from src.student_model import conn, initialize_database

def test_mastery_vector_table_exists():
    """Verify mastery_vector table exists with required columns."""
    initialize_database()
    database = conn()
    cursor = database.cursor()

    # Check table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mastery_vector'")
    assert cursor.fetchone() is not None, "mastery_vector table does not exist"

    # Check columns
    cursor.execute("PRAGMA table_info(mastery_vector)")
    columns = {row[1] for row in cursor.fetchall()}
    required = {'topic_id', 'accuracy', 'transfer_auc', 'mechanism_quality', 'calibration_icc', 'retention_6mo', 'integration_score', 'last_updated'}
    assert required.issubset(columns), f"Missing columns: {required - columns}"
    database.close()

def test_confidence_columns_in_attempts():
    """Verify question_attempts table has confidence_reported and confidence_actual columns."""
    initialize_database()
    database = conn()
    cursor = database.cursor()

    cursor.execute("PRAGMA table_info(question_attempts)")
    columns = {row[1] for row in cursor.fetchall()}
    assert 'confidence_reported' in columns, "confidence_reported missing"
    assert 'confidence_actual' in columns, "confidence_actual missing"
    database.close()

from src.mastery_gates import check_mastery, compute_mastery_vector

def test_baseline_mastery_achieved():
    """Verify baseline mastery criteria: 70% accuracy, 3 attempts, confidence >= 0.60."""
    # Simulate 3 correct attempts with confidence 4/5
    attempts = [
        {'correct': True, 'confidence_reported': 4, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'mechanism_articulated': True},
    ]

    vector = compute_mastery_vector(attempts)
    assert vector['accuracy'] == 1.0
    assert vector['calibration_icc'] >= 0.60, f"calibration_icc too low: {vector['calibration_icc']}"
    assert vector['mechanism_quality'] == 1.0

    mastered = check_mastery(vector, level='baseline')
    assert mastered == True

def test_intermediate_mastery_not_achieved():
    """Verify intermediate criteria: 80% accuracy, 5+ attempts, <2 overconfident errors."""
    attempts = [
        {'correct': True, 'confidence_reported': 5, 'overconfident': False},
        {'correct': True, 'confidence_reported': 5, 'overconfident': False},
        {'correct': False, 'confidence_reported': 5, 'overconfident': True},  # Overconfident error
        {'correct': False, 'confidence_reported': 5, 'overconfident': True},  # 2nd overconfident error
        {'correct': True, 'confidence_reported': 3, 'overconfident': False},
    ]

    vector = compute_mastery_vector(attempts)
    assert vector['accuracy'] == 0.6  # 3/5 correct
    assert vector['overconfident_rate'] == 0.4  # 2/5 errors with high confidence

    mastered = check_mastery(vector, level='intermediate')
    assert mastered == False  # Accuracy too low (0.6 < 0.80)

def test_advanced_mastery_achieved():
    """Verify advanced criteria: 90% accuracy, 10+ attempts, overconf <0.15, transfer AUC >=0.80."""
    attempts = [
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': True, 'confidence_reported': 4, 'overconfident': False, 'transfer_success': True, 'mechanism_articulated': True},
        {'correct': False, 'confidence_reported': 3, 'overconfident': False, 'transfer_success': False, 'mechanism_articulated': True},
    ]

    vector = compute_mastery_vector(attempts)
    assert vector['accuracy'] >= 0.90  # 9/10 correct
    assert vector['overconfident_rate'] < 0.15
    assert vector['transfer_auc'] >= 0.80

    mastered = check_mastery(vector, level='advanced')
    assert mastered == True


from src.confidence_weighter import apply_confidence_weight_to_interval

def test_overconfident_error_reduces_interval():
    """Confident + wrong should have 0.7x multiplier on interval."""
    base_interval = 10  # days
    is_correct = False
    confidence_reported = 5  # High confidence (1-5 scale)

    weighted_interval = apply_confidence_weight_to_interval(
        base_interval, is_correct, confidence_reported
    )

    # Overconfident penalty: ×0.7
    expected = base_interval * 0.7
    assert weighted_interval == expected

def test_high_confidence_correct_normal_interval():
    """Confident + correct should have normal interval (×1.0)."""
    base_interval = 10
    is_correct = True
    confidence_reported = 5

    weighted_interval = apply_confidence_weight_to_interval(
        base_interval, is_correct, confidence_reported
    )

    assert weighted_interval == base_interval

def test_calibrated_low_confidence_correct_bonus():
    """Uncertain + correct should have 1.2x bonus (well-calibrated learner)."""
    base_interval = 10
    is_correct = True
    confidence_reported = 2  # Low confidence

    weighted_interval = apply_confidence_weight_to_interval(
        base_interval, is_correct, confidence_reported
    )

    expected = base_interval * 1.2
    assert weighted_interval == expected
