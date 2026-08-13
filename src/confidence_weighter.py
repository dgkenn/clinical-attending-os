# src/confidence_weighter.py

def apply_confidence_weight_to_interval(
    base_interval: float,
    is_correct: bool,
    confidence_reported: int  # 1-5 scale
) -> float:
    """
    Apply confidence-based multiplier to FSRS interval.

    Logic:
    - Confident (4-5) + wrong: ×0.7 penalty (Dunning-Kruger risk)
    - Confident (4-5) + correct: ×1.0 normal
    - Uncertain (1-2) + correct: ×1.2 bonus (well-calibrated)
    - Uncertain (1-2) + wrong: ×1.0 normal
    - Medium (3) + any: ×1.0 normal

    Args:
        base_interval: FSRS-computed interval (days)
        is_correct: whether answer was correct
        confidence_reported: 1-5 scale from student

    Returns:
        float: weighted interval in days
    """
    multiplier = 1.0

    if confidence_reported >= 4:  # High confidence
        if not is_correct:
            multiplier = 0.7  # Overconfident error: return sooner
    elif confidence_reported <= 2:  # Low confidence
        if is_correct:
            multiplier = 1.2  # Well-calibrated: push out slightly

    return base_interval * multiplier
