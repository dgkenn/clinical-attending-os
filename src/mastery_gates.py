# src/mastery_gates.py

from typing import Dict, List
import statistics

def compute_mastery_vector(attempts: List[Dict]) -> Dict[str, float]:
    """
    Compute 6-dimensional mastery vector from attempt history.

    Returns:
        {
            'accuracy': float (0-1),
            'transfer_auc': float (0-1),
            'mechanism_quality': float (0-1),
            'calibration_icc': float (0-1),
            'retention_6mo': float (0-1),
            'integration_score': float (0-1),
            'overconfident_rate': float (0-1),
        }
    """
    if not attempts:
        return {
            'accuracy': 0.0,
            'transfer_auc': 0.0,
            'mechanism_quality': 0.0,
            'calibration_icc': 0.0,
            'retention_6mo': 0.0,
            'integration_score': 0.0,
            'overconfident_rate': 0.0,
        }

    # Accuracy: % correct
    correct = sum(1 for a in attempts if a.get('correct'))
    accuracy = correct / len(attempts)

    # Overconfident rate: confident + wrong / total
    overconfident = sum(1 for a in attempts if a.get('confidence_reported', 0) >= 4 and not a.get('correct'))
    overconfident_rate = overconfident / len(attempts) if attempts else 0.0

    # Transfer AUC: % of attempts marked transfer_success (novel case test).
    #
    # `transfer_assessed` distinguishes "was tested on a novel case and failed"
    # from "was never tested on one". Without it a 0.0 meaning UNMEASURED was
    # indistinguishable from a 0.0 meaning FAILED, and since transfer has been
    # assessed on 1 of 171 real attempts, every topic scored 0.0 and the
    # intermediate and advanced gates were unreachable by construction.
    # Identical in shape to the bug that once pinned mechanism_quality at 0.0
    # and made mastery impossible for topics sitting at 100% accuracy.
    transfer_attempts = [a for a in attempts if 'transfer_success' in a]
    transfer_assessed = bool(transfer_attempts)
    if transfer_attempts:
        transfer_success = sum(1 for a in transfer_attempts if a.get('transfer_success'))
        transfer_auc = transfer_success / len(transfer_attempts)
    else:
        transfer_auc = 0.0

    # Mechanism quality: % of teach-back attempts with rubric >= 0.75
    mechanism_attempts = [a for a in attempts if 'mechanism_quality' in a]
    if mechanism_attempts:
        mechanism_quality = sum(1 for a in mechanism_attempts if a.get('mechanism_quality', 0) >= 0.75) / len(mechanism_attempts)
    else:
        # If no explicit mechanism_quality, assume 1.0 if mechanism_articulated
        mechanism_attempts = [a for a in attempts if 'mechanism_articulated' in a]
        if mechanism_attempts:
            mechanism_quality = sum(1 for a in mechanism_attempts if a.get('mechanism_articulated')) / len(mechanism_attempts)
        else:
            mechanism_quality = 0.0

    # Calibration ICC: correlation between reported confidence and actual correctness
    confidence_reported = [a.get('confidence_reported', 3) / 5.0 for a in attempts]  # Normalize 1-5 to 0-1
    correctness = [1.0 if a.get('correct') else 0.0 for a in attempts]
    calibration_icc = _compute_icc(confidence_reported, correctness)

    # Retention 6mo: assume 0.0 for now (no 6-month data yet); will be populated on follow-up quiz
    retention_6mo = 0.0

    # Integration score: assume 0.0 for now (no cross-topic tests yet)
    integration_score = 0.0

    return {
        'accuracy': accuracy,
        'transfer_auc': transfer_auc,
        'transfer_assessed': transfer_assessed,
        'mechanism_quality': mechanism_quality,
        'calibration_icc': calibration_icc,
        'retention_6mo': retention_6mo,
        'integration_score': integration_score,
        'overconfident_rate': overconfident_rate,
    }


def mastery_level(vector: Dict[str, float]) -> str:
    """Highest tier this vector satisfies: 'none'|'baseline'|'intermediate'|'advanced'.

    The database previously stored only `mastery_achieved`, hard-wired to
    check_mastery(..., level='advanced'). Advanced demands transfer_auc >= 0.80
    and mechanism_quality >= 0.95, so with transfer effectively never assessed
    the column was 0 for every topic forever and carried no information — the
    tutor could not tell a topic answered correctly a dozen times from one never
    seen. Recording the tier that was actually reached makes the field mean
    something, and lets a genuinely solid topic stop being drilled like a new one.
    """
    for level in ('advanced', 'intermediate', 'baseline'):
        if check_mastery(vector, level=level):
            return level
    return 'none'

def _compute_icc(list1: List[float], list2: List[float]) -> float:
    """
    Compute Intraclass Correlation Coefficient (ICC) between two lists.
    Simplified: Pearson correlation between reported confidence and actual correctness.

    Special case: if both lists are constant, check if they represent perfect calibration
    (high confidence + all correct) = 1.0, otherwise 0.0.
    """
    if len(list1) < 2 or len(list2) < 2:
        return 0.0

    mean1, mean2 = statistics.mean(list1), statistics.mean(list2)

    numerator = sum((list1[i] - mean1) * (list2[i] - mean2) for i in range(len(list1)))
    denom1 = sum((list1[i] - mean1) ** 2 for i in range(len(list1))) ** 0.5
    denom2 = sum((list2[i] - mean2) ** 2 for i in range(len(list2))) ** 0.5

    # Special case: no variance in one or both lists
    if denom1 == 0 and denom2 == 0:
        # Both constant: if all correct and high confidence, perfect calibration
        if mean2 == 1.0 and mean1 >= 0.6:
            return 1.0
        else:
            return 0.0

    if denom1 == 0 or denom2 == 0:
        return 0.0

    return numerator / (denom1 * denom2)

def check_mastery(vector: Dict[str, float], level: str = 'baseline') -> bool:
    """
    Determine if mastery criteria are met at the specified level.

    Args:
        vector: mastery_vector dict from compute_mastery_vector()
        level: 'baseline' | 'intermediate' | 'advanced'

    Returns:
        bool: True if all criteria met for this level
    """
    if level == 'baseline':
        # Accuracy >= 70% + calibration_icc >= 0.60 + mechanism_quality > 0
        return (
            vector['accuracy'] >= 0.70 and
            vector['calibration_icc'] >= 0.60 and
            vector['mechanism_quality'] > 0.0
        )

    elif level == 'intermediate':
        # Accuracy >= 80% + overconf_rate < 0.40 + transfer_auc >= 0.70.
        #
        # Transfer only gates once it has been ASSESSED. An unmeasured
        # dimension must not read as a failed one: transfer has been assessed on
        # 1 of 171 real attempts, so requiring it unconditionally made this tier
        # unreachable no matter how well the topic was actually known. Advanced
        # still demands it outright — that is the tier where demonstrating
        # transfer to a novel case is the whole point.
        if vector.get('transfer_assessed', True) and vector['transfer_auc'] < 0.70:
            return False
        return (
            vector['accuracy'] >= 0.80 and
            vector['overconfident_rate'] < 0.40
        )

    elif level == 'advanced':
        # Accuracy >= 90% + overconf_rate < 15% + transfer_auc >= 0.80 + mechanism >= 0.95 + calibration >= 0.70
        return (
            vector['accuracy'] >= 0.90 and
            vector['overconfident_rate'] < 0.15 and
            vector['transfer_auc'] >= 0.80 and
            vector['mechanism_quality'] >= 0.95 and
            vector['calibration_icc'] >= 0.70
        )

    return False

def update_mastery_in_db(topic_id: int, vector: Dict[str, float], conn) -> None:
    """Update mastery_vector table in SQLite with computed values.

    Stores the tier actually reached alongside the boolean. `mastery_achieved`
    was pinned to the ADVANCED gate, which requires transfer_auc >= 0.80 and
    mechanism_quality >= 0.95 — so with transfer effectively never assessed the
    column read 0 for every topic regardless of performance, and could not
    distinguish a topic answered correctly a dozen times from one never seen.
    """
    cursor = conn.cursor()
    try:
        cols = {r[1] for r in cursor.execute("PRAGMA table_info(mastery_vector)")}
        if "mastery_level" not in cols:
            cursor.execute("ALTER TABLE mastery_vector ADD COLUMN mastery_level TEXT DEFAULT 'none'")
    except Exception:
        pass  # a missing column must not lose the rest of the update
    try:
        cursor.execute("UPDATE mastery_vector SET mastery_level = ? WHERE topic_id = ?",
                       (mastery_level(vector), topic_id))
    except Exception:
        pass
    cursor.execute("""
        UPDATE mastery_vector
        SET accuracy = ?,
            transfer_auc = ?,
            mechanism_quality = ?,
            calibration_icc = ?,
            retention_6mo = ?,
            integration_score = ?,
            mastery_achieved = ?,
            last_updated = CURRENT_TIMESTAMP
        WHERE topic_id = ?
    """, (
        vector['accuracy'],
        vector['transfer_auc'],
        vector['mechanism_quality'],
        vector['calibration_icc'],
        vector['retention_6mo'],
        vector['integration_score'],
        check_mastery(vector, level='advanced'),  # Mark as mastered if advanced level met
        topic_id,
    ))
    conn.commit()
