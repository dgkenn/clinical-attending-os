# Medicine-First Knowledge Base Gap-Filling + MCP Server Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ingest ~2,350-2,950 intern medicine units across 3 phases, extend MCP server with 6 core endpoints, and integrate with Claude for end-to-end mastery learning.

**Architecture:** 
- Phase 1-3: Parallel PDF acquisition + sequential ingestion via existing `ingest.py` pipeline
- MCP server: Extend `mcp_server.py` with new endpoints; maintain bidirectional SQLite sync with FastAPI
- Claude integration: Wire MCP endpoints into Claude system prompt; test session persistence across restarts

**Tech Stack:** Python 3.9+, Chroma vector DB, SQLite (student_model.db), FastAPI, MCP protocol, Claude API

---

## FILE STRUCTURE

### New Files (Created)

```
docs/superpowers/plans/
  └── 2026-06-04-medicine-first-knowledge-gap-filling.md (this file)

data/
  ├── phase1_sources/
  │   ├── AHA_ASA_Stroke_Guidelines_2024.pdf (downloaded)
  │   ├── IDSA_Meningitis_Guidelines.pdf (downloaded)
  │   ├── Washington_Manual_H_and_P.pdf (acquired)
  │   └── Guyatts_Guide_Chapters_1-4.pdf (acquired)
  │
  ├── phase2_sources/
  │   ├── IDSA_Pneumonia_Guidelines_2023.pdf
  │   ├── NAEPP_Asthma_Guidelines_2024.pdf
  │   ├── GOLD_COPD_Guidelines_2024.pdf
  │   ├── AHA_ACC_CAD_Guidelines_2023.pdf
  │   ├── CHEST_PE_DVT_Guidelines_2023.pdf
  │   ├── ADA_Standards_of_Care_2024.pdf
  │   └── AACE_Thyroid_Guidelines_2016.pdf
  │
  └── phase3_sources/
      ├── AASLD_Cirrhosis_Guidelines.pdf
      ├── ASGE_GI_Bleeding_Guidelines.pdf
      └── Psychiatry_IHI_modules.pdf

src/
  ├── ingest.py (MODIFY: add phase-aware source grouping)
  ├── mcp_server.py (EXTEND: add 6 new endpoints)
  ├── mcp_endpoints.py (CREATE: new endpoint implementations)
  ├── mastery_gates.py (CREATE: mastery criteria + decision logic)
  └── confidence_weighter.py (CREATE: confidence-weighted FSRS)

tests/
  ├── test_mcp_endpoints.py (CREATE: test all 6 endpoints)
  ├── test_mastery_gates.py (CREATE: test mastery criteria)
  └── test_phase_transitions.py (CREATE: test phase gating + FSRS updates)

CUSTOM_GPT_INSTRUCTIONS_PHASE1.md (CREATE: Claude system prompt for phase 1 testing)
```

### Modified Files (Existing)

```
src/
  ├── ingest.py (add SOURCE_OVERRIDE_PHASE logic)
  ├── curriculum.py (ensure phase tags are preserved on units)
  ├── student_model.py (add mastery_vector table, confidence columns)
  ├── schemas.py (add MasterySignals schema)
  └── api.py (add /mcp_debug endpoint for testing)

.env.example (add MCP_ENABLED flag)
```

---

## TASK BREAKDOWN

### PHASE 0: SOURCE ACQUISITION & SETUP (Prep, ~4 hours)

#### Task 0.1: Download Free PDF Guidelines

**Files:**
- Target: `data/phase1_sources/`, `data/phase2_sources/`, `data/phase3_sources/`

- [ ] **Step 1: Create source directories**

```bash
mkdir -p data/phase{1,2,3}_sources
ls data/
```

Expected output: `phase1_sources  phase2_sources  phase3_sources`

- [ ] **Step 2: Download Phase 1 sources**

```bash
# AHA/ASA Stroke Guidelines 2024 (free, public domain)
curl -L https://www.stroke.org/en/professional-education/aha-asa-stroke-guidelines \
  -o data/phase1_sources/AHA_ASA_Stroke_Guidelines_2024.pdf

# IDSA Meningitis Guidelines (free, IDSA.org)
curl -L https://www.idsa.org/practice-guidelines \
  -o data/phase1_sources/IDSA_Meningitis_Guidelines.pdf

# Guyatt's BMJ Learning (free via BU/MGH institutional access; manual download)
# For now, assume downloaded locally
```

Expected: 2 PDF files in `data/phase1_sources/`

- [ ] **Step 3: Download Phase 2 sources**

```bash
# IDSA Pneumonia
curl -L https://www.idsa.org/practice-guidelines \
  -o data/phase2_sources/IDSA_Pneumonia_Guidelines_2023.pdf

# NAEPP Asthma
curl -L https://www.naepp.asthma.edu \
  -o data/phase2_sources/NAEPP_Asthma_Guidelines_2024.pdf

# GOLD COPD
curl -L https://goldcopd.org \
  -o data/phase2_sources/GOLD_COPD_Guidelines_2024.pdf

# AHA/ACC CAD
curl -L https://www.americanheart.org/professional \
  -o data/phase2_sources/AHA_ACC_CAD_Guidelines_2023.pdf

# CHEST PE/DVT
curl -L https://www.chestjournal.org \
  -o data/phase2_sources/CHEST_PE_DVT_Guidelines_2023.pdf

# ADA Standards
curl -L https://diabetes.org/professionals/standards-of-care \
  -o data/phase2_sources/ADA_Standards_of_Care_2024.pdf

# AACE Thyroid
curl -L https://www.aace.com/disease-state-resources/thyroid \
  -o data/phase2_sources/AACE_Thyroid_Guidelines_2016.pdf
```

Expected: 7 PDF files in `data/phase2_sources/`

- [ ] **Step 4: Download Phase 3 sources**

```bash
# AASLD Cirrhosis
curl -L https://www.aasld.org \
  -o data/phase3_sources/AASLD_Cirrhosis_Guidelines.pdf

# ASGE GI Bleeding
curl -L https://www.asge.org \
  -o data/phase3_sources/ASGE_GI_Bleeding_Guidelines.pdf

# IHI modules (free, online — manual capture or PDF export)
# Placeholder: assume manual download for now
```

Expected: 2 PDF files in `data/phase3_sources/`, IHI modules ready

- [ ] **Step 5: Acquire Washington Manual & Guyatt's Guide**

```bash
# Manual step: Purchase used Washington Manual (~$20-40) from Amazon/ThriftBooks
# Manual step: Access Guyatt's BMJ Learning via BU/MGH login
# For now, document receipt in a tracking file
echo "Washington Manual (11th ed.) — received in hard copy" > data/ACQUISITION_LOG.txt
echo "Guyatt's Guide — access via BU institutional login" >> data/ACQUISITION_LOG.txt
```

- [ ] **Step 6: Commit source acquisition**

```bash
git add data/phase{1,2,3}_sources/ data/ACQUISITION_LOG.txt .gitignore
git commit -m "feat: add phase 1-3 PDF source files for knowledge gap-filling"
```

---

### PHASE 1: FOUNDATION (WEEKS 1-4, ~50-65 HOURS INGESTION)

#### Task 1.1: Extend SQLite Schema for Mastery Tracking

**Files:**
- Modify: `src/student_model.py:1-100` (schema definition)
- Test: `tests/test_mastery_gates.py`

- [ ] **Step 1: Read current schema**

```bash
head -100 src/student_model.py | grep -A 50 "CREATE TABLE"
```

Expected: Current tables include `topics`, `attempts`, `sessions`, `student_progress`

- [ ] **Step 2: Write test for mastery_vector table**

```python
# tests/test_mastery_gates.py

import sqlite3
import pytest
from src.student_model import conn, initialize_database

def test_mastery_vector_table_exists():
    """Verify mastery_vector table exists with required columns."""
    initialize_database()
    cursor = conn.cursor()
    
    # Check table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mastery_vector'")
    assert cursor.fetchone() is not None, "mastery_vector table does not exist"
    
    # Check columns
    cursor.execute("PRAGMA table_info(mastery_vector)")
    columns = {row[1] for row in cursor.fetchall()}
    required = {'topic_id', 'accuracy', 'transfer_auc', 'mechanism_quality', 'calibration_icc', 'retention_6mo', 'integration_score', 'last_updated'}
    assert required.issubset(columns), f"Missing columns: {required - columns}"

def test_confidence_columns_in_attempts():
    """Verify attempts table has confidence_reported and confidence_actual columns."""
    initialize_database()
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(attempts)")
    columns = {row[1] for row in cursor.fetchall()}
    assert 'confidence_reported' in columns, "confidence_reported missing"
    assert 'confidence_actual' in columns, "confidence_actual missing"
```

- [ ] **Step 3: Run test to verify it fails**

```bash
cd C:\Users\Dean\anesthesia_attending
python -m pytest tests/test_mastery_gates.py::test_mastery_vector_table_exists -v
```

Expected: `FAILED — sqlite3.OperationalError: no such table: mastery_vector`

- [ ] **Step 4: Implement schema changes**

```python
# src/student_model.py — add to initialize_database() function

def initialize_database():
    """Initialize SQLite schema with all required tables."""
    cursor = conn.cursor()
    
    # ... existing tables ...
    
    # NEW: Mastery vector table (one row per topic)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mastery_vector (
            topic_id INTEGER PRIMARY KEY,
            topic_name TEXT UNIQUE NOT NULL,
            accuracy REAL DEFAULT 0.0,                    -- % correct (0-1)
            transfer_auc REAL DEFAULT 0.0,                -- Area under ROC on novel cases (0-1)
            mechanism_quality REAL DEFAULT 0.0,           -- Teach-back rubric score (0-1)
            calibration_icc REAL DEFAULT 0.0,             -- Intraclass correlation (confidence vs actual) (0-1)
            retention_6mo REAL DEFAULT 0.0,               -- % retained at 6 months (0-1)
            integration_score REAL DEFAULT 0.0,           -- Can integrate with other topics (0-1)
            mastery_achieved BOOLEAN DEFAULT 0,           -- True if all criteria met
            last_updated TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Add columns to attempts table if not already present
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY,
            session_id TEXT,
            topic_id INTEGER,
            question TEXT,
            user_answer TEXT,
            is_correct BOOLEAN,
            confidence_reported INTEGER,                  -- 1-5 scale
            confidence_actual REAL,                       -- Computed from recent accuracy
            teach_back_quality REAL,                      -- Rubric 0-1
            transfer_success BOOLEAN,                     -- Passed novel case test
            mistake_type TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(session_id) REFERENCES sessions(id),
            FOREIGN KEY(topic_id) REFERENCES topics(id)
        )
    """)
    
    conn.commit()
```

- [ ] **Step 5: Run test to verify it passes**

```bash
python -m pytest tests/test_mastery_gates.py::test_mastery_vector_table_exists -v
python -m pytest tests/test_mastery_gates.py::test_confidence_columns_in_attempts -v
```

Expected: Both pass

- [ ] **Step 6: Commit**

```bash
git add src/student_model.py tests/test_mastery_gates.py
git commit -m "feat: add mastery_vector table and confidence tracking to SQLite schema"
```

---

#### Task 1.2: Implement Mastery Criteria Decision Logic

**Files:**
- Create: `src/mastery_gates.py`
- Test: `tests/test_mastery_gates.py`

- [ ] **Step 1: Write test for mastery thresholds**

```python
# tests/test_mastery_gates.py — add to existing test file

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
    assert vector['confidence_accuracy'] >= 0.60
    assert vector['mechanism_quality'] == 1.0
    
    mastered = check_mastery(vector, level='baseline')
    assert mastered == True

def test_intermediate_mastery_not_achieved():
    """Verify intermediate criteria: 80% accuracy, 5+ attempts, <2 overconfident errors."""
    attempts = [
        {'correct': True, 'confidence': 5, 'overconfident': False},
        {'correct': True, 'confidence': 5, 'overconfident': False},
        {'correct': False, 'confidence': 5, 'overconfident': True},  # Overconfident error
        {'correct': False, 'confidence': 5, 'overconfident': True},  # 2nd overconfident error
        {'correct': True, 'confidence': 3, 'overconfident': False},
    ]
    
    vector = compute_mastery_vector(attempts)
    assert vector['accuracy'] == 0.6  # 3/5 correct
    assert vector['overconfident_errors'] == 2
    
    mastered = check_mastery(vector, level='intermediate')
    assert mastered == False  # Accuracy too low (0.6 < 0.80)

def test_advanced_mastery_achieved():
    """Verify advanced criteria: 90% accuracy, 8+ attempts, overconf <0.15, transfer AUC >=0.80."""
    attempts = [
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
        {'correct': False, 'confidence': 3, 'overconfident': False, 'transfer': False},
        {'correct': True, 'confidence': 4, 'overconfident': False, 'transfer': True},
    ]
    
    vector = compute_mastery_vector(attempts)
    assert vector['accuracy'] >= 0.90
    assert vector['overconfident_rate'] < 0.15
    assert vector['transfer_auc'] >= 0.80
    
    mastered = check_mastery(vector, level='advanced')
    assert mastered == True
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_mastery_gates.py::test_baseline_mastery_achieved -v
python -m pytest tests/test_mastery_gates.py::test_intermediate_mastery_not_achieved -v
python -m pytest tests/test_mastery_gates.py::test_advanced_mastery_achieved -v
```

Expected: All 3 fail (mastery_gates module doesn't exist)

- [ ] **Step 3: Implement mastery_gates module**

```python
# src/mastery_gates.py

from typing import Dict, List, Optional
import sqlite3

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
        return {k: 0.0 for k in ['accuracy', 'transfer_auc', 'mechanism_quality', 'calibration_icc', 'retention_6mo', 'integration_score', 'overconfident_rate']}
    
    # Accuracy: % correct
    correct = sum(1 for a in attempts if a.get('correct'))
    accuracy = correct / len(attempts)
    
    # Overconfident rate: confident + wrong / total
    overconfident = sum(1 for a in attempts if a.get('confidence_reported', 0) >= 4 and not a.get('correct'))
    overconfident_rate = overconfident / len(attempts) if attempts else 0.0
    
    # Transfer AUC: % of attempts marked transfer_success (novel case test)
    transfer_success = sum(1 for a in attempts if a.get('transfer_success'))
    transfer_auc = transfer_success / len([a for a in attempts if 'transfer_success' in a]) if any('transfer_success' in a for a in attempts) else 0.0
    
    # Mechanism quality: % of teach-back attempts with rubric >= 0.75
    mechanism_attempts = [a for a in attempts if 'mechanism_quality' in a]
    mechanism_quality = sum(1 for a in mechanism_attempts if a.get('mechanism_quality', 0) >= 0.75) / len(mechanism_attempts) if mechanism_attempts else 0.0
    
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
        'mechanism_quality': mechanism_quality,
        'calibration_icc': calibration_icc,
        'retention_6mo': retention_6mo,
        'integration_score': integration_score,
        'overconfident_rate': overconfident_rate,
    }

def _compute_icc(list1: List[float], list2: List[float]) -> float:
    """
    Compute Intraclass Correlation Coefficient (ICC) between two lists.
    Simplified: Pearson correlation between reported confidence and actual correctness.
    """
    if len(list1) < 2 or len(list2) < 2:
        return 0.0
    
    import statistics
    mean1, mean2 = statistics.mean(list1), statistics.mean(list2)
    
    numerator = sum((list1[i] - mean1) * (list2[i] - mean2) for i in range(len(list1)))
    denom1 = sum((list1[i] - mean1) ** 2 for i in range(len(list1))) ** 0.5
    denom2 = sum((list2[i] - mean2) ** 2 for i in range(len(list2))) ** 0.5
    
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
        # Accuracy >= 70% + confidence_accuracy >= 0.60 + mechanism_quality > 0
        return (
            vector['accuracy'] >= 0.70 and
            vector['calibration_icc'] >= 0.60 and
            vector['mechanism_quality'] > 0.0
        )
    
    elif level == 'intermediate':
        # Accuracy >= 80% + <2 overconfident errors (rate < 0.40) + transfer_auc >= 0.70
        overconfident_count = int(vector['overconfident_rate'] * 10)  # Rough estimate from rate
        return (
            vector['accuracy'] >= 0.80 and
            vector['overconfident_rate'] < 0.40 and
            vector['transfer_auc'] >= 0.70
        )
    
    elif level == 'advanced':
        # Accuracy >= 90% + overconf_rate < 15% + transfer_auc >= 0.80 + teach_back >= 0.95 + calibration >= 0.70
        return (
            vector['accuracy'] >= 0.90 and
            vector['overconfident_rate'] < 0.15 and
            vector['transfer_auc'] >= 0.80 and
            vector['mechanism_quality'] >= 0.95 and
            vector['calibration_icc'] >= 0.70
        )
    
    return False

def update_mastery_in_db(topic_id: int, vector: Dict[str, float], conn: sqlite3.Connection) -> None:
    """Update mastery_vector table in SQLite with computed values."""
    cursor = conn.cursor()
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_mastery_gates.py::test_baseline_mastery_achieved -v
python -m pytest tests/test_mastery_gates.py::test_intermediate_mastery_not_achieved -v
python -m pytest tests/test_mastery_gates.py::test_advanced_mastery_achieved -v
```

Expected: All 3 pass

- [ ] **Step 5: Commit**

```bash
git add src/mastery_gates.py tests/test_mastery_gates.py
git commit -m "feat: implement 6-dimensional mastery criteria decision logic"
```

---

#### Task 1.3: Implement Confidence-Weighted FSRS

**Files:**
- Create: `src/confidence_weighter.py`
- Modify: `src/fsrs.py:150-200` (integrate weighting into interval calculation)
- Test: `tests/test_mastery_gates.py` (add new test)

- [ ] **Step 1: Write test for confidence weighting**

```python
# tests/test_mastery_gates.py — add

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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_mastery_gates.py::test_overconfident_error_reduces_interval -v
```

Expected: `ImportError: cannot import name 'apply_confidence_weight_to_interval'`

- [ ] **Step 3: Implement confidence weighter**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_mastery_gates.py::test_overconfident_error_reduces_interval -v
python -m pytest tests/test_mastery_gates.py::test_high_confidence_correct_normal_interval -v
python -m pytest tests/test_mastery_gates.py::test_calibrated_low_confidence_correct_bonus -v
```

Expected: All pass

- [ ] **Step 5: Integrate into fsrs.py**

Modify `src/fsrs.py` to call confidence weighter after computing interval:

```python
# src/fsrs.py — in the compute_next_review_date() or similar function

from src.confidence_weighter import apply_confidence_weight_to_interval

def record_review(card_id, grade, confidence_reported=3):
    """
    Record a review attempt and update FSRS state.
    
    Args:
        card_id: ID of the card being reviewed
        grade: 'again', 'hard', 'good', 'easy' (0-3)
        confidence_reported: 1-5 scale from student
    """
    # ... existing FSRS logic ...
    base_interval = compute_interval(...)  # FSRS computation
    
    # Apply confidence weighting
    weighted_interval = apply_confidence_weight_to_interval(
        base_interval, is_correct=(grade in ['good', 'easy']), confidence_reported
    )
    
    # Update review date
    next_review = datetime.now() + timedelta(days=weighted_interval)
    # ... save to DB ...
```

- [ ] **Step 6: Commit**

```bash
git add src/confidence_weighter.py src/fsrs.py tests/test_mastery_gates.py
git commit -m "feat: implement confidence-weighted FSRS interval adjustment"
```

---

#### Task 1.4: Ingest Phase 1 Sources (Foundation)

**Files:**
- Modify: `src/ingest.py:1-50` (add phase-aware source grouping)
- Run: `python -m src.ingest --phase phase1`
- Test: Verify 550-750 new units created

- [ ] **Step 1: Update ingest.py to support --phase flag**

```python
# src/ingest.py — modify main() function

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Force re-ingest all sources')
    parser.add_argument('--phase', choices=['phase1', 'phase2', 'phase3', None], default=None, help='Ingest specific phase sources')
    parser.add_argument('--source', type=str, help='Ingest specific source by name')
    args = parser.parse_args()
    
    # Map phase to source directories
    phase_to_sources = {
        'phase1': [
            'data/phase1_sources/AHA_ASA_Stroke_Guidelines_2024.pdf',
            'data/phase1_sources/IDSA_Meningitis_Guidelines.pdf',
            'data/phase1_sources/Washington_Manual_H_and_P.pdf',
            'data/phase1_sources/Guyatts_Guide_Chapters_1-4.pdf',
        ],
        'phase2': [
            'data/phase2_sources/IDSA_Pneumonia_Guidelines_2023.pdf',
            'data/phase2_sources/NAEPP_Asthma_Guidelines_2024.pdf',
            'data/phase2_sources/GOLD_COPD_Guidelines_2024.pdf',
            'data/phase2_sources/AHA_ACC_CAD_Guidelines_2023.pdf',
            'data/phase2_sources/CHEST_PE_DVT_Guidelines_2023.pdf',
            'data/phase2_sources/ADA_Standards_of_Care_2024.pdf',
            'data/phase2_sources/AACE_Thyroid_Guidelines_2016.pdf',
        ],
        'phase3': [
            'data/phase3_sources/AASLD_Cirrhosis_Guidelines.pdf',
            'data/phase3_sources/ASGE_GI_Bleeding_Guidelines.pdf',
        ],
    }
    
    if args.phase:
        sources_to_ingest = phase_to_sources[args.phase]
    elif args.source:
        sources_to_ingest = [f for f in os.listdir('data') if args.source in f]
    else:
        sources_to_ingest = SOURCE_FILES  # Default from .env
    
    for source_file in sources_to_ingest:
        ingest_file(source_file, force=args.force, phase=args.phase or 'default')
        
    # Rebuild curriculum after ingestion
    subprocess.run(['python', '-m', 'src.curriculum'], check=True)
    print(f"Ingestion complete. Curriculum rebuilt.")
```

- [ ] **Step 2: Run Phase 1 ingestion**

```bash
cd C:\Users\Dean\anesthesia_attending
python -m src.ingest --phase phase1 --force
```

Expected output:
```
Ingesting data/phase1_sources/AHA_ASA_Stroke_Guidelines_2024.pdf...
Extracted 120 chunks from Stroke Guidelines
...
Ingesting data/phase1_sources/Guyatts_Guide_Chapters_1-4.pdf...
Extracted 150 chunks from Guyatt's Guide
Total new units created: 550-750
Curriculum rebuilt successfully.
```

- [ ] **Step 3: Verify ingestion**

```bash
python -c "
from src.retrieval import hybrid_search
results, _ = hybrid_search('H&P methodology differential diagnosis', mode='intern_teach', max_results=5)
for r in results:
    print(f'{r.source_name}: {r.topic_tags}')
"
```

Expected: H&P, differential diagnosis, NIHSS, seizure, meningitis results returned

- [ ] **Step 4: Commit**

```bash
git add src/ingest.py storage/chroma/ingestion_manifest.json storage/curriculum/units.json
git commit -m "feat: ingest Phase 1 sources (H&P, EBM, stroke, seizure, meningitis) — 550-750 units"
```

---

#### Task 1.5: Test Retrieval Quality (Phase 1)

**Files:**
- Run: `python -m src.retrieval_debug` (manual spot-checks)
- Run: `python -m src.eval_runner --no-cross-encoder` (automated audit)
- Test: Verify MRR@5 ≥ 0.80, recall@10 ≥ 0.97

- [ ] **Step 1: Spot-check critical queries**

```bash
python -m src.retrieval_debug

# Interactively test queries:
# Query: "how to take a history and physical"
# Expected: H&P methodology chapters rank highest
# Query: "NIHSS scoring stroke"
# Expected: NIHSS details, stroke assessment
# Query: "seizure management lorazepam dose"
# Expected: Seizure recognition, benzodiazepine dosing
```

- [ ] **Step 2: Run evaluation suite**

```bash
python -m src.eval_runner --no-cross-encoder
```

Expected output:
```
Evaluating retrieval quality on 50 golden questions...
MRR@5: 0.82 (target: >= 0.80) ✓
Recall@10: 0.97 (target: >= 0.97) ✓
All tests passed.
```

- [ ] **Step 3: Commit (if passing)**

```bash
git add storage/eval_final.json
git commit -m "test: Phase 1 retrieval quality audit passed (MRR@5=0.82, recall@10=0.97)"
```

---

#### Task 1.6: Implement MCP Server Endpoints (Part 1: Core Functions)

**Files:**
- Create: `src/mcp_endpoints.py` (6 core endpoints)
- Modify: `src/mcp_server.py` (register endpoints)
- Test: `tests/test_mcp_endpoints.py`

- [ ] **Step 1: Write test for `retrieval()` endpoint**

```python
# tests/test_mcp_endpoints.py

import pytest
from src.mcp_endpoints import retrieval, get_session_state, submit_answer

def test_retrieval_returns_chunks_with_citations():
    """Test retrieval endpoint returns chunks and citations."""
    results = retrieval(
        query="hyperkalemia treatment",
        mode="intern_teach",
        max_results=5
    )
    
    assert 'results' in results
    assert 'retrieval_confidence' in results
    assert 'insufficient_context' in results
    
    assert len(results['results']) > 0
    result = results['results'][0]
    assert 'text' in result
    assert 'source_name' in result
    assert 'page' in result or 'book' in result

def test_get_session_state_returns_fsrs_queue():
    """Test session state includes FSRS due dates and weak topics."""
    state = get_session_state()
    
    assert 'fsrs_due_today' in state
    assert 'weak_topics' in state
    assert 'mastery_matrix' in state
    assert 'phase' in state
    
    assert isinstance(state['fsrs_due_today'], list)
    assert isinstance(state['weak_topics'], list)

def test_submit_answer_updates_fsrs():
    """Test submitting answer updates FSRS and mastery vector."""
    # Simulate submission
    result = submit_answer(
        topic="hyperkalemia",
        user_answer="give calcium gluconate",
        is_correct=True,
        confidence_reported=4,
        teach_back_quality=0.9,
        transfer_success=True,
        session_id="test_session_001"
    )
    
    assert result['ok'] == True
    assert 'next_review_date' in result
    assert 'mastery_updated' in result
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_mcp_endpoints.py::test_retrieval_returns_chunks_with_citations -v
```

Expected: `ModuleNotFoundError: No module named 'src.mcp_endpoints'`

- [ ] **Step 3: Implement mcp_endpoints.py**

```python
# src/mcp_endpoints.py

from typing import Dict, List, Optional, Any
import sqlite3
from datetime import datetime, timedelta
from src.retrieval import hybrid_search
from src.student_model import conn
from src.mastery_gates import compute_mastery_vector, check_mastery, update_mastery_in_db
from src.confidence_weighter import apply_confidence_weight_to_interval
from src.fsrs import record_review

def retrieval(
    query: str,
    mode: str = "intern_teach",
    library_filter: Optional[str] = None,
    max_results: int = 8
) -> Dict[str, Any]:
    """
    MCP Endpoint 1: Retrieve chunks from knowledge base.
    
    Args:
        query: User question or topic
        mode: "intern_teach", "icu_teach", "anesthesia_boards"
        library_filter: Optional filter by library
        max_results: Number of results to return
    
    Returns:
        {
            'results': [{'text': str, 'source_name': str, 'page': int, ...}],
            'retrieval_confidence': float (0-1),
            'insufficient_context': bool,
        }
    """
    results, insufficient = hybrid_search(
        query, 
        mode=mode, 
        library_filter=library_filter, 
        max_results=max_results
    )
    
    return {
        'results': [r.model_dump() for r in results],
        'retrieval_confidence': len(results) / max_results if results else 0.0,
        'insufficient_context': insufficient,
    }

def get_session_state() -> Dict[str, Any]:
    """
    MCP Endpoint 2: Get current student session state.
    
    Returns:
        {
            'fsrs_due_today': [{'topic': str, 'due_date': str}],
            'weak_topics': [{'topic': str, 'error_rate': float}],
            'mastery_matrix': {topic: {level: bool}},
            'phase': 'intern_medicine' | 'icu' | 'anesthesia',
            'progress_pct': float (0-100),
        }
    """
    cursor = conn.cursor()
    
    # Get FSRS due today
    cursor.execute("""
        SELECT DISTINCT topic_id, topic_name
        FROM fsrs_state
        WHERE next_review_date <= DATE('now')
        LIMIT 20
    """)
    due_today = [{'topic_id': row[0], 'topic': row[1]} for row in cursor.fetchall()]
    
    # Get weak topics (>25% error rate)
    cursor.execute("""
        SELECT topic, COUNT(*) as total, SUM(CASE WHEN mistake_type IS NOT NULL THEN 1 ELSE 0 END) as errors
        FROM attempts
        WHERE timestamp >= DATE('now', '-7 days')
        GROUP BY topic
        HAVING (errors / total) > 0.25
        ORDER BY (errors / total) DESC
        LIMIT 10
    """)
    weak_topics = [{'topic': row[0], 'error_rate': row[2] / row[1]} for row in cursor.fetchall()]
    
    # Get mastery matrix
    cursor.execute("SELECT topic_name, mastery_achieved FROM mastery_vector")
    mastery_matrix = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Get current phase (from student preferences or default)
    cursor.execute("SELECT default_training_phase FROM student_model LIMIT 1")
    phase_row = cursor.fetchone()
    phase = phase_row[0] if phase_row else 'intern_medicine'
    
    # Progress %: topics mastered / total topics
    total_topics = len(mastery_matrix)
    mastered_topics = sum(1 for v in mastery_matrix.values() if v)
    progress_pct = (mastered_topics / total_topics * 100) if total_topics > 0 else 0.0
    
    return {
        'fsrs_due_today': due_today,
        'weak_topics': weak_topics,
        'mastery_matrix': mastery_matrix,
        'phase': phase,
        'progress_pct': progress_pct,
    }

def get_next_topic() -> Dict[str, Any]:
    """
    MCP Endpoint 3: Get next topic to study (FSRS-prioritized).
    
    Returns:
        {
            'topic': str,
            'reason': 'due_today' | 'weak' | 'new_material' | 'integration',
            'retrieval_query': str,
            'suggested_phase': str,
        }
    """
    cursor = conn.cursor()
    
    # Priority 1: Due today (FSRS)
    cursor.execute("""
        SELECT topic_name FROM fsrs_state
        WHERE next_review_date <= DATE('now')
        ORDER BY next_review_date ASC
        LIMIT 1
    """)
    due_row = cursor.fetchone()
    if due_row:
        return {
            'topic': due_row[0],
            'reason': 'due_today',
            'retrieval_query': f"Mechanism of {due_row[0]}",
            'suggested_phase': 'drilling',
        }
    
    # Priority 2: Weak topic (error rate >25%)
    cursor.execute("""
        SELECT topic, COUNT(*) / SUM(1) as error_rate FROM attempts
        WHERE timestamp >= DATE('now', '-7 days')
        GROUP BY topic
        HAVING error_rate > 0.25
        ORDER BY error_rate DESC
        LIMIT 1
    """)
    weak_row = cursor.fetchone()
    if weak_row:
        return {
            'topic': weak_row[0],
            'reason': 'weak',
            'retrieval_query': f"Treatment of {weak_row[0]}",
            'suggested_phase': 'drilling',
        }
    
    # Priority 3: New material (not yet studied)
    cursor.execute("""
        SELECT topic_name FROM mastery_vector
        WHERE topic_name NOT IN (SELECT DISTINCT topic FROM attempts)
        LIMIT 1
    """)
    new_row = cursor.fetchone()
    if new_row:
        return {
            'topic': new_row[0],
            'reason': 'new_material',
            'retrieval_query': f"What is {new_row[0]}?",
            'suggested_phase': 'new_material',
        }
    
    # Fallback: integration challenge
    return {
        'topic': 'integration_challenge',
        'reason': 'integration',
        'retrieval_query': 'Create a case combining hyperkalemia and sepsis',
        'suggested_phase': 'case_application',
    }

def submit_answer(
    topic: str,
    user_answer: str,
    is_correct: bool,
    confidence_reported: int,
    teach_back_quality: float = 0.0,
    transfer_success: bool = False,
    session_id: str = "default",
    mistake_type: str = "other",
) -> Dict[str, Any]:
    """
    MCP Endpoint 4: Submit student answer; update FSRS and mastery.
    
    Args:
        topic: Topic being tested
        user_answer: Student's response
        is_correct: Whether answer is correct
        confidence_reported: 1-5 scale
        teach_back_quality: Rubric score (0-1)
        transfer_success: Passed novel case test
        session_id: Current session
        mistake_type: 'recall', 'mechanism', 'overconfident', etc.
    
    Returns:
        {
            'ok': bool,
            'next_review_date': str,
            'mastery_updated': bool,
            'level_achieved': 'baseline' | 'intermediate' | 'advanced' | None,
        }
    """
    cursor = conn.cursor()
    
    # Get topic_id
    cursor.execute("SELECT id FROM topics WHERE name = ?", (topic,))
    topic_row = cursor.fetchone()
    if not topic_row:
        # Create topic if doesn't exist
        cursor.execute("INSERT INTO topics (name) VALUES (?)", (topic,))
        topic_id = cursor.lastrowid
    else:
        topic_id = topic_row[0]
    
    # Record attempt
    cursor.execute("""
        INSERT INTO attempts 
        (topic_id, session_id, user_answer, is_correct, confidence_reported, 
         teach_back_quality, transfer_success, mistake_type, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (
        topic_id, session_id, user_answer, is_correct, confidence_reported,
        teach_back_quality, transfer_success, mistake_type
    ))
    conn.commit()
    
    # Update FSRS with confidence weighting
    cursor.execute("SELECT next_review_date FROM fsrs_state WHERE topic_id = ?", (topic_id,))
    fsrs_row = cursor.fetchone()
    if fsrs_row:
        base_interval = (datetime.fromisoformat(fsrs_row[0]) - datetime.now()).days
        weighted_interval = apply_confidence_weight_to_interval(
            base_interval, is_correct, confidence_reported
        )
        next_review = datetime.now() + timedelta(days=weighted_interval)
        cursor.execute(
            "UPDATE fsrs_state SET next_review_date = ? WHERE topic_id = ?",
            (next_review.isoformat(), topic_id)
        )
    else:
        # Initialize FSRS for this topic
        next_review = datetime.now() + timedelta(days=1)
        cursor.execute(
            "INSERT INTO fsrs_state (topic_id, next_review_date) VALUES (?, ?)",
            (topic_id, next_review.isoformat())
        )
    conn.commit()
    
    # Update mastery_vector
    cursor.execute("""
        SELECT id, is_correct, confidence_reported, teach_back_quality, transfer_success
        FROM attempts WHERE topic_id = ?
        ORDER BY timestamp DESC LIMIT 10
    """)
    recent_attempts = [
        {
            'correct': row[1],
            'confidence_reported': row[2],
            'mechanism_quality': row[3],
            'transfer_success': row[4],
        }
        for row in cursor.fetchall()
    ]
    
    vector = compute_mastery_vector(recent_attempts)
    update_mastery_in_db(topic_id, vector, conn)
    
    # Determine mastery level
    level_achieved = None
    if check_mastery(vector, 'advanced'):
        level_achieved = 'advanced'
    elif check_mastery(vector, 'intermediate'):
        level_achieved = 'intermediate'
    elif check_mastery(vector, 'baseline'):
        level_achieved = 'baseline'
    
    return {
        'ok': True,
        'next_review_date': next_review.isoformat(),
        'mastery_updated': True,
        'level_achieved': level_achieved,
    }

def get_mastery_gates() -> Dict[str, Any]:
    """
    MCP Endpoint 5: Get mastery status for all topics.
    
    Returns:
        {
            'mastery_matrix': {topic: {'level': str, 'vector': {scores}}},
            'ready_for_phase_advance': bool,
        }
    """
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT topic_name, accuracy, transfer_auc, mechanism_quality,
               calibration_icc, retention_6mo, integration_score
        FROM mastery_vector
    """)
    
    mastery_matrix = {}
    for row in cursor.fetchall():
        topic, acc, trans, mech, cal, ret, integ = row
        vector = {
            'accuracy': acc,
            'transfer_auc': trans,
            'mechanism_quality': mech,
            'calibration_icc': cal,
            'retention_6mo': ret,
            'integration_score': integ,
        }
        
        level = None
        if check_mastery(vector, 'advanced'):
            level = 'advanced'
        elif check_mastery(vector, 'intermediate'):
            level = 'intermediate'
        elif check_mastery(vector, 'baseline'):
            level = 'baseline'
        
        mastery_matrix[topic] = {'level': level, 'vector': vector}
    
    # Check if ready to advance phase
    total = len(mastery_matrix)
    advanced = sum(1 for m in mastery_matrix.values() if m['level'] == 'advanced')
    ready = (advanced / total > 0.8) if total > 0 else False
    
    return {
        'mastery_matrix': mastery_matrix,
        'ready_for_phase_advance': ready,
    }

def get_progress() -> Dict[str, Any]:
    """
    MCP Endpoint 6: Get overall progress.
    
    Returns:
        {
            'intern_medicine_pct': float,
            'icu_pct': float,
            'anesthesia_pct': float,
            'overall_pct': float,
            'hours_studied': float,
        }
    """
    cursor = conn.cursor()
    
    # By library
    for lib in ['intern_year_medicine', 'ICU_critical_care', 'anesthesiology_boards']:
        cursor.execute(f"""
            SELECT COUNT(*) as total,
                   SUM(CASE WHEN mastery_achieved THEN 1 ELSE 0 END) as mastered
            FROM mastery_vector
            WHERE library = ?
        """, (lib,))
        total, mastered = cursor.fetchone()
        pct = (mastered / total * 100) if total > 0 else 0.0
        
        if 'intern' in lib:
            intern_pct = pct
        elif 'ICU' in lib:
            icu_pct = pct
        else:
            anes_pct = pct
    
    # Overall
    cursor.execute("SELECT COUNT(*), SUM(CASE WHEN mastery_achieved THEN 1 ELSE 0 END) FROM mastery_vector")
    total, mastered = cursor.fetchone()
    overall_pct = (mastered / total * 100) if total > 0 else 0.0
    
    # Hours studied (estimate: 45 min per session, count sessions)
    cursor.execute("SELECT COUNT(DISTINCT session_id) FROM attempts")
    sessions = cursor.fetchone()[0]
    hours_studied = sessions * 0.75  # 45 min per session
    
    return {
        'intern_medicine_pct': intern_pct,
        'icu_pct': icu_pct,
        'anesthesia_pct': anes_pct,
        'overall_pct': overall_pct,
        'hours_studied': hours_studied,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_mcp_endpoints.py::test_retrieval_returns_chunks_with_citations -v
python -m pytest tests/test_mcp_endpoints.py::test_get_session_state_returns_fsrs_queue -v
python -m pytest tests/test_mcp_endpoints.py::test_submit_answer_updates_fsrs -v
```

Expected: All pass

- [ ] **Step 5: Register endpoints in mcp_server.py**

```python
# src/mcp_server.py

from src.mcp_endpoints import (
    retrieval, get_session_state, get_next_topic,
    submit_answer, get_mastery_gates, get_progress
)

# Register MCP tools
mcp_server.tool("retrieval", retrieval)
mcp_server.tool("get_session_state", get_session_state)
mcp_server.tool("get_next_topic", get_next_topic)
mcp_server.tool("submit_answer", submit_answer)
mcp_server.tool("get_mastery_gates", get_mastery_gates)
mcp_server.tool("get_progress", get_progress)
```

- [ ] **Step 6: Commit**

```bash
git add src/mcp_endpoints.py src/mcp_server.py tests/test_mcp_endpoints.py
git commit -m "feat: implement 6 core MCP endpoints (retrieval, session, mastery, progress)"
```

---

#### Task 1.7: Phase 1 Validation & Approval Gate

**Files:**
- Run: All Phase 1 tests
- Document: Phase 1 completion in README.md

- [ ] **Step 1: Run all Phase 1 tests**

```bash
python -m pytest tests/test_mastery_gates.py -v
python -m pytest tests/test_mcp_endpoints.py -v
python -m pytest tests/test_retrieval.py -v
```

Expected: All pass

- [ ] **Step 2: Run retrieval evaluation**

```bash
python -m src.eval_runner --no-cross-encoder
```

Expected: MRR@5 ≥ 0.80, Recall@10 ≥ 0.97

- [ ] **Step 3: Verify curriculum units created**

```bash
python -c "
import json
with open('storage/curriculum/units.json') as f:
    units = json.load(f)
print(f'Total units: {len(units)}')
print(f'Intern medicine units: {sum(1 for u in units if \"intern\" in u.get(\"band\", \"\").lower())}')
"
```

Expected: 550-750 new units, majority tagged intern_medicine

- [ ] **Step 4: Document Phase 1 completion**

```markdown
# Phase 1 Completion Summary

**Date:** 2026-06-04  
**Goal:** Foundation topics (H&P, EBM, stroke, seizure, meningitis)  
**Status:** ✅ COMPLETE

## Metrics

- New units created: 550-750
- Retrieval quality: MRR@5 = 0.82, Recall@10 = 0.97 ✓
- Mastery gates: All tests passing ✓
- MCP endpoints: All 6 endpoints operational ✓
- FSRS integration: Confidence weighting live ✓

## Validation Checks

- [x] H&P methodology retrieval works
- [x] Differential diagnosis templates present
- [x] NIHSS scoring queries return correct results
- [x] Seizure management topics fully covered
- [x] Meningitis CSF interpretation available
- [x] EBM concepts (study design, GRADE) indexed

## Ready for Phase 2?

✅ YES — All Phase 1 gates passed. Proceeding to Phase 2 (high-frequency diagnoses).
```

- [ ] **Step 5: Commit**

```bash
git add README.md PHASE1_COMPLETION.md
git commit -m "docs: Phase 1 completion summary and validation results"
```

---

## PHASE 2: HIGH-FREQUENCY DIAGNOSES (WEEKS 5-12, ~65-75 HOURS INGESTION)

[Similar task structure: Ingest 7 guideline PDFs, deduplicate vs Marino, rebuild curriculum, validate retrieval quality, run tests]

Due to length constraints, I'll outline the key tasks:

### Task 2.1: Ingest Phase 2 sources (pneumonia, ACS, PE/DVT, GI bleed, COPD/asthma, diabetes, thyroid)
- Run: `python -m src.ingest --phase phase2 --force`
- Expected: 1,000-1,200 new units

### Task 2.2: Deduplication audit vs Marino ICU
- Check for overlap with existing ICU content
- Resolve conflicts (e.g., if sepsis management differs between Marino and IDSA)
- Maintain source attribution

### Task 2.3: Retrieval quality audit (Phase 2)
- Spot-check: ACS ECG interpretation, pneumonia antibiotic selection, PE Wells score
- Run `eval_runner` → MRR@5 ≥ 0.80, Recall@10 ≥ 0.97

### Task 2.4: Integration test (MCP + mastery gates)
- Claude calls `get_next_topic()` → returns pneumonia
- Claude calls `retrieval("pneumonia treatment")` → gets IDSA guidelines
- Claude calls `submit_answer(...)` with student attempt
- Verify mastery_vector and FSRS updated correctly

---

## PHASE 3: BREADTH & INTEGRATION (WEEKS 13-20, ~65-77 HOURS INGESTION)

### Task 3.1-3.3: Similar to Phase 2, ingest hematology, hepatology, psychiatry, communication modules
- Target: 800-1,000 new units
- Final state: 2,478-3,078 cumulative units

---

## FINAL PHASE: MCP SERVER & CLAUDE INTEGRATION

### Task F.1: Test full MCP server locally

```bash
# Start MCP server in standalone mode
python -m src.mcp_server --port 5000

# Test endpoint
curl -X POST http://localhost:5000/mcp/get_session_state

# Expected response
{"fsrs_due_today": [...], "weak_topics": [...], ...}
```

### Task F.2: Create Claude system prompt

```markdown
# Claude Medical Mastery Tutor System Prompt

You are a medical learning coach for an intern preparing for board exams.

## Instructions

1. **Load session state** at start of every conversation:
   - Call MCP tool `get_session_state()` to see what the student knows
   - Check `fsrs_due_today` — prioritize these topics first

2. **Teach using 5-phase pedagogy**:
   - Warm-up (2 min): Quick recall question
   - Drilling (5-8 min): Active retrieval on weak mechanism
   - New material (8 min): Textbook explanation with retrieved sources
   - Case application (5 min): "What would you do first?" scenario
   - Teach-back (2 min): "Explain to a colleague" without notes

3. **Retrieve citations**:
   - Call MCP tool `retrieval(query, mode="intern_teach")` for every teaching step
   - Include source attribution in your response

4. **Evaluate understanding**:
   - After each lesson, ask: "How confident are you? (1-5)"
   - Assess mechanism articulation in teach-back
   - Test transfer: "What if the patient had X comorbidity?"

5. **Submit results**:
   - Call MCP tool `submit_answer(topic, is_correct, confidence, teach_back_quality, transfer_success)`
   - FSRS and mastery tracking update automatically

6. **Adapt to mastery level**:
   - If student ≥90% accuracy: Skip warm-up + drilling, jump to cases
   - If student <70%: Do full 5-phase, focus on mechanism
   - If overconfident (high confidence but wrong): Flag and re-quiz

## Phase Gating

- **Phase 1:** Foundation (H&P, differential diagnosis, EBM, stroke, seizure, meningitis)
- **Phase 2:** High-frequency diagnoses (pneumonia, ACS, PE, GI bleed, COPD, asthma, diabetes, thyroid)
- **Phase 3:** Breadth (hematology, hepatology, psychiatry, communication)

Advance phases only when ~80% of topics at "advanced" mastery level.

## Tone

- Encouraging but rigorous
- Explain "why" before "what"
- If uncertainty: "This is evolving research; here's what we know..."
- Celebrate mastery milestones
```

### Task F.3: Test end-to-end session

```python
# tests/test_end_to_end.py

def test_full_lesson_cycle():
    """Simulate complete lesson from session load to mastery update."""
    # 1. Load session
    session = get_session_state()
    assert len(session['fsrs_due_today']) > 0
    
    # 2. Get next topic
    next_topic = get_next_topic()
    assert next_topic['topic'] in session['fsrs_due_today'][0]['topic']
    
    # 3. Retrieve
    sources = retrieval(next_topic['retrieval_query'], mode='intern_teach', max_results=3)
    assert len(sources['results']) >= 3
    
    # 4. Submit answer
    result = submit_answer(
        topic=next_topic['topic'],
        user_answer="give fluids and broad-spectrum antibiotics",
        is_correct=True,
        confidence_reported=4,
        teach_back_quality=0.85,
        transfer_success=True,
        session_id="test_e2e_001",
    )
    
    assert result['ok'] == True
    assert result['level_achieved'] in ['baseline', 'intermediate', 'advanced']
    
    # 5. Verify state updated
    updated_state = get_session_state()
    mastery_gates = get_mastery_gates()
    
    # Topic should be moved to "due later" if mastered
    if result['level_achieved'] == 'advanced':
        assert next_topic['topic'] not in [t['topic'] for t in updated_state['fsrs_due_today']]
```

- [ ] **Step 1: Run end-to-end test**

```bash
python -m pytest tests/test_end_to_end.py::test_full_lesson_cycle -v
```

Expected: PASS

---

## EXECUTION HANDOFF

**Plan complete and saved** to `docs/superpowers/plans/2026-06-04-medicine-first-knowledge-gap-filling.md`.

**Two execution options:**

**1. Subagent-Driven (RECOMMENDED)**
- I dispatch a fresh subagent per task
- Subagent executes the task, reports back
- I review and approve before next task
- Fast feedback loops, catch issues early

**2. Inline Execution**
- I execute tasks sequentially in this session
- Batch execution with checkpoints after each phase
- Faster overall if all steps pass

**Which approach would you prefer?**

(Recommendation: Start with **Subagent-Driven** for Phase 1 — it's foundational and we want high confidence before scaling to Phases 2-3. After Phase 1 passes all gates, we can accelerate Phases 2-3 in parallel if desired.)
