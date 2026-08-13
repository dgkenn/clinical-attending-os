# Clinical Attending OS — Testing Guide

## Pre-Launch Validation

### 1. MCP Server Functionality

Test each of the 7 tools:

```bash
# Terminal 1: Start MCP server
cd C:\Users\Dean\anesthesia_attending
python -m src.mcp_server

# Terminal 2: Run tests
pytest tests/test_mcp_server.py -v
```

Expected output:
```
test_retrieval_tool PASSED
test_session_state_tool PASSED
test_next_topic_tool PASSED
test_submit_answer_tool PASSED
test_mastery_gates_tool PASSED
test_get_progress_tool PASSED
test_request_follow_up_tool PASSED

======================== 7 passed in 3.2s ========================
```

### 2. Database Integrity

Verify database structure is correct:

```bash
# Windows PowerShell
sqlite3 student.db ".tables"
sqlite3 student.db ".schema mastery_vector"
```

Expected output:
```
attempts          follow_up_sessions  mastery_vector    sessions          
student_model     subtopic_weaknesses topic_hierarchy   topics            fsrs_state

CREATE TABLE mastery_vector (
    topic TEXT PRIMARY KEY,
    baseline_score REAL DEFAULT 0.0,
    intermediate_score REAL DEFAULT 0.0,
    advanced_score REAL DEFAULT 0.0,
    fsrs_interval INT DEFAULT 1,
    last_review TEXT,
    created_at TEXT
);
```

### 3. Chroma Vector Index

Verify knowledge base is indexed:

```bash
python -c "
from src.retrieval import get_chroma_db
db = get_chroma_db()
collection = db.get_or_create_collection('medical_knowledge')
print(f'Total documents indexed: {collection.count()}')
"
```

Expected:
```
Total documents indexed: 813
```

### 4. Curriculum Structure

Verify curriculum was built:

```bash
python -c "
import json
from pathlib import Path
units = json.load(open('storage/curriculum/units.json'))
print(f'Curriculum units: {len(units)}')
libs = {}
for u in units:
    lib = u.get('library', 'unknown')
    libs[lib] = libs.get(lib, 0) + 1
for lib, count in sorted(libs.items(), key=lambda x: -x[1]):
    print(f'  {lib}: {count}')
"
```

Expected:
```
Curriculum units: 2507
  intern_year_medicine: 2300
  anesthesia_related: 207
```

## User Testing Workflow

### Test 1: Basic Lesson Cycle (15 minutes)

**Objective:** Verify end-to-end learning loop works

1. MCP server running in background terminal
2. Open Claude Desktop
3. Verify tools available: "What tools do you have?"
4. Open a new medical chat
5. Ask: "Let's study NIHSS scoring for stroke severity assessment"
6. Claude retrieves content, teaches, asks question
7. You answer: "NIHSS is 11-item scale, scores 0-42, higher = more severe"
8. Provide confidence: "4/5"
9. Claude evaluates answer, asks mechanism question
10. You explain: "Higher NIHSS predicts worse outcomes and need for intervention"
11. Claude calls submit_answer tool
12. Check result: "You've achieved baseline mastery" or "Good progress, continue practicing"

**Success Criteria:**
- ✓ Claude retrieved relevant NIHSS content
- ✓ Question was appropriate difficulty
- ✓ Your answer was evaluated correctly
- ✓ Mastery was recorded (can query database)
- ✓ No errors in terminal where MCP server runs

**Verification:**
```bash
sqlite3 student.db "SELECT * FROM attempts WHERE topic LIKE '%NIHSS%';"
```
Should return your answer record.

---

### Test 2: Follow-Up Drilling (10 minutes)

**Objective:** Verify nested learning sessions work

1. Same session as Test 1
2. After NIHSS mastery, ask: "Tell me more about the motor subscore"
3. Claude calls request_follow_up tool
4. Claude teaches motor score components (arm drift, leg strength)
5. Answer 3-4 follow-up questions on motor subscale
6. Claude: "You've mastered motor subscale components"
7. Ask: "Ready to go back to full stroke management?"
8. Claude resumes main stroke lesson with motor knowledge integrated

**Success Criteria:**
- ✓ Follow-up session created separately from main session
- ✓ Questions specific to motor subscale
- ✓ Main session context restored smoothly
- ✓ Both sessions tracked in database

**Verification:**
```bash
sqlite3 student.db "SELECT * FROM follow_up_sessions ORDER BY created_at DESC LIMIT 1;"
```
Should show recent follow-up on motor subscale.

---

### Test 3: Session Persistence (10 minutes)

**Objective:** Verify learning carries across conversations

1. Complete Test 1 & 2 successfully
2. Close Claude chat entirely (quit the application)
3. Close MCP server terminal
4. Wait 10 seconds
5. Start MCP server again: `python -m src.mcp_server`
6. Reopen Claude Desktop
7. Ask: "What's my progress so far?"
8. Claude calls get_progress tool
9. Claude reports: "You've studied X topics, mastered NIHSS, weak on hyponatremia"
10. Ask: "What should I study next?"
11. Claude recommends next due topic based on FSRS schedule

**Success Criteria:**
- ✓ Claude remembered prior learning without reminder
- ✓ FSRS dates preserved
- ✓ Mastery status accurate
- ✓ Progress calculation correct
- ✓ Next topic recommendation aligned with schedule

**Verification:**
```bash
sqlite3 student.db "SELECT topic, baseline_score, last_review FROM mastery_vector WHERE baseline_score > 0;"
```
Should show multiple topics with scores and review dates.

---

### Test 4: Mastery Gating (15 minutes)

**Objective:** Verify mastery gates enforce progression

1. Start new topic: "Let's learn about vasopressors"
2. Claude retrieves vasopressor content
3. Claude asks: "What's the difference between dopamine at 5 mcg/kg/min vs 15 mcg/kg/min?"
4. You answer incorrectly: "Both work the same, dosing doesn't matter"
5. Provide confidence: "2/5"
6. Claude evaluates: "That's not quite right. The dose determines the effect..."
7. Claude asks another vasopressor question (doesn't mark mastered yet)
8. Answer correctly with high confidence (4/5)
9. Claude asks one more: "When would you use epinephrine over norepinephrine?"
10. Answer demonstrates good mechanism understanding
11. Claude: "You've achieved baseline mastery on vasopressors"

**Success Criteria:**
- ✓ Incorrect answer didn't gate progression
- ✓ Multiple questions required for mastery
- ✓ Mastery gate enforced (required 3+ correct)
- ✓ Can now progress to more advanced vasopressor topics

**Verification:**
```bash
sqlite3 student.db "SELECT topic, baseline_score FROM mastery_vector WHERE topic LIKE '%vasopr%';"
```
Should show baseline_score >= 70 (mastery threshold).

---

### Test 5: Confidence Weighting (10 minutes)

**Objective:** Verify calibration affects scheduling

1. Study two different topics in same session
2. Topic A: Answer correctly, confidence 5/5 (well-calibrated)
3. Topic B: Answer correctly, confidence 1/5 (underconfident)
4. Topic C: Answer correctly, confidence 5/5 but WRONG (overconfident)
5. Ask: "When will I review each topic?"
6. Claude reports next review dates

**Expected behavior:**
- Topic A: Long interval (well-calibrated correct)
- Topic B: Shorter interval (penalized for underconfidence)
- Topic C: Much shorter interval (penalized for overconfidence with error)

**Success Criteria:**
- ✓ Well-calibrated answer scheduled furthest out
- ✓ Underconfident answer penalized
- ✓ Overconfident wrong answer heavily penalized
- ✓ Calibration ICC tracked in database

**Verification:**
```bash
sqlite3 student.db "SELECT topic, fsrs_interval FROM mastery_vector WHERE topic IN ('TopicA', 'TopicB', 'TopicC') ORDER BY fsrs_interval DESC;"
```
Should show TopicA > TopicB, and TopicC very short.

---

### Test 6: Knowledge Base Completeness (5 minutes)

**Objective:** Verify all 813 units are accessible

Run retrieval test for diverse queries:

```bash
python -c "
from src.retrieval import hybrid_search

queries = [
    'shock management cardiogenic',
    'sepsis qSOFA criteria',
    'acetaminophen overdose NAC',
    'preeclampsia magnesium',
    'pediatric CPR compression',
    'breaking bad news SPIKES',
]

for q in queries:
    hits, _ = hybrid_search(q, max_results=1)
    if hits:
        print(f'[OK] {q}: found')
    else:
        print(f'[FAIL] {q}: NOT found')
"
```

**Expected:** All 6 should find results

---

## Performance Testing

### Latency Benchmarks

Measure tool call latencies:

```bash
python -c "
import time
from src.retrieval import hybrid_search
from src.session_runner import get_session_state

# Test 1: Retrieval
start = time.time()
for _ in range(5):
    hybrid_search('shock', max_results=3)
latency = (time.time() - start) / 5 * 1000
print(f'Retrieval latency: {latency:.0f}ms (target: <500ms)')

# Test 2: Database query
start = time.time()
for _ in range(10):
    get_session_state()
latency = (time.time() - start) / 10 * 1000
print(f'Session state latency: {latency:.0f}ms (target: <50ms)')
"
```

**Expected:**
- Retrieval: 200-500ms (depends on index size)
- Database: 10-30ms

---

## Sign-Off Checklist

Before marking system production-ready:

### Pre-Launch Checks
- [ ] MCP server starts without errors
- [ ] Claude Desktop config file valid JSON
- [ ] All 7 tools appear in Claude
- [ ] Chroma vector DB has 813 units indexed
- [ ] SQLite database has 9 tables
- [ ] Curriculum built with 2,507 units

### Functional Tests
- [ ] Test 1: Basic lesson cycle works end-to-end
- [ ] Test 2: Follow-up drilling creates nested session
- [ ] Test 3: Session persistence works across restarts
- [ ] Test 4: Mastery gating enforces progression
- [ ] Test 5: Confidence weighting affects scheduling
- [ ] Test 6: All major topics retrievable

### Performance Tests
- [ ] Retrieval latency <500ms
- [ ] Database latency <50ms
- [ ] Tool call overhead minimal (0 MCP tokens)
- [ ] No timeouts on typical queries

### Data Integrity
- [ ] Database backup created
- [ ] Export functionality works
- [ ] Records persist across server restarts
- [ ] No data corruption on normal use

### Documentation
- [ ] Deployment guide complete
- [ ] Testing guide complete (this file)
- [ ] Troubleshooting guide accessible
- [ ] All 7 tools documented with examples

### User Acceptance
- [ ] Medical content accurate (spot-check 20 units)
- [ ] Teaching explanations clear
- [ ] Questions appropriate difficulty
- [ ] Progress tracking intuitive
- [ ] No user-facing errors

---

## Regression Testing

After any code changes, run:

```bash
# Full test suite
pytest tests/ -v

# Specific test file
pytest tests/test_mcp_server.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

---

## Continuous Monitoring

Once deployed:

1. **Daily logs:** Check for errors in MCP server terminal
2. **Weekly backups:** `cp student.db student.db.backup.$(date +%Y%m%d)`
3. **Monthly audit:** `sqlite3 student.db "SELECT COUNT(*) FROM attempts;"`
4. **Quarterly update:** Review new medical guidelines, update knowledge base

---

## Known Limitations & Workarounds

| Issue | Workaround |
|-------|-----------|
| Slow retrieval on first run | Index is large; subsequent calls faster. Acceptable. |
| Occasional session timeout | Restart MCP server, resume from last saved state |
| Duplicate units in curriculum | Deduplication script runs on consolidation; expected minor overlap |
| High-scoring answers sometimes too strict | Adjust evaluation rubric in teaching_mode.py if needed |
| Rare database locks | Use `sqlite3 student.db "PRAGMA integrity_check;"` if suspect corruption |

---

**System ready for production deployment upon completion of all sign-off items.**
