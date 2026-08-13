# MCP Endpoints Reference

Complete API reference for the 7 core Clinical Attending OS MCP endpoints.

## Table of Contents

1. [retrieval](#1-retrieval) — Retrieve medical knowledge
2. [get_session_state](#2-get_session_state) — Get student session state
3. [get_next_topic](#3-get_next_topic) — Get next FSRS topic
4. [submit_answer](#4-submit_answer) — Record answer & update mastery
5. [get_mastery_gates](#5-get_mastery_gates) — Check mastery status
6. [get_progress](#6-get_progress) — Get progress statistics
7. [request_follow_up](#7-request_follow_up) — Request nested lesson

---

## 1. retrieval

Retrieve medical knowledge chunks from the knowledge base using hybrid search (BM25 + semantic).

### Signature

```python
mcp_retrieval(
    query: str,
    mode: str = "intern_teach",
    library_filter: Optional[str] = None,
    max_results: int = 8
) -> Dict[str, Any]
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | str | required | Medical question or topic (e.g., "NIHSS stroke severity scoring") |
| `mode` | str | "intern_teach" | Tutor mode: `intern_teach`, `cross_cover`, `rapid_response`, `pimp`, `crisis` |
| `library_filter` | Optional[str] | None | Filter by library: `intern_year_medicine`, `ICU_critical_care`, `anesthesiology_boards` |
| `max_results` | int | 8 | Maximum number of chunks to return |

### Returns

```json
{
  "results": [
    {
      "text": "Shock is tissue hypoperfusion with inability to meet cellular oxygen demands...",
      "metadata": {
        "topic": "shock",
        "subtopic": "definition",
        "source": "lecture_notes_phase1",
        "tags": ["cardiovascular", "critical_care"]
      },
      "score": 0.94,
      "retrieval_method": "semantic"
    }
  ],
  "retrieval_confidence": 0.875,
  "insufficient_context": false
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `results` | List[Dict] | Ranked list of knowledge chunks |
| `results[*].text` | str | Chunk text content |
| `results[*].metadata` | Dict | Topic, subtopic, source, tags |
| `results[*].score` | float | Relevance score (0-1) |
| `results[*].retrieval_method` | str | `semantic`, `bm25`, or `hybrid` |
| `retrieval_confidence` | float | Proportion of requested chunks returned (0-1) |
| `insufficient_context` | bool | True if query returned 0 chunks |

### Examples

**Example 1: Basic retrieval**
```python
result = mcp_retrieval("shock management")
# Returns: 8 highest-relevance chunks on shock
```

**Example 2: Filtered retrieval**
```python
result = mcp_retrieval(
    "sepsis treatment",
    mode="crisis",
    library_filter="ICU_critical_care",
    max_results=5
)
# Returns: Top 5 sepsis chunks from ICU library, crisis-mode filter
```

**Example 3: In conversation**
```
User: "How do I assess shock severity?"

Claude: [Calls mcp_retrieval("shock severity assessment")]
        [Receives 8 chunks on SIRS criteria, lactate, SOFA, SBP]

Claude: "Here are the key ways to assess shock severity:
         1. Lactate level: Normal <2 mmol/L...
         [Content from retrieval]"
```

### Tutor Modes

- **intern_teach**: Comprehensive, beginner-friendly explanations
- **cross_cover**: Practical applications for covering other services
- **rapid_response**: Concise clinical pearls for urgent situations
- **pimp**: Deep mechanistic details for board-style grilling
- **crisis**: Hyper-focused management algorithms

### Error Handling

If retrieval fails:
```json
{
  "results": [],
  "retrieval_confidence": 0.0,
  "insufficient_context": true,
  "error": "Chroma connection failed"
}
```

---

## 2. get_session_state

Get current student session state: due topics, weak areas, mastery, progress.

### Signature

```python
get_session_state() -> Dict[str, Any]
```

### Parameters

None. Returns state for the current student.

### Returns

```json
{
  "fsrs_due_today": [
    {"topic_id": 1, "topic": "shock"},
    {"topic_id": 3, "topic": "sepsis"},
    {"topic_id": 5, "topic": "stroke"}
  ],
  "weak_topics": [
    {"topic": "vasopressors", "error_rate": 0.35},
    {"topic": "fluid_resuscitation", "error_rate": 0.28}
  ],
  "mastery_matrix": {
    "shock": true,
    "sepsis": false,
    "stroke": false,
    "vasopressors": true,
    "fluid_resuscitation": false
  },
  "phase": "intern_year_medicine",
  "progress_pct": 25.3
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `fsrs_due_today` | List[Dict] | Topics scheduled for review today (FSRS) |
| `fsrs_due_today[*].topic_id` | int | Internal topic ID |
| `fsrs_due_today[*].topic` | str | Topic name |
| `weak_topics` | List[Dict] | Topics with >25% error rate in last 7 days |
| `weak_topics[*].topic` | str | Topic name |
| `weak_topics[*].error_rate` | float | Error rate (0-1) |
| `mastery_matrix` | Dict[str, bool] | Mastery achieved for each topic |
| `phase` | str | Current training phase |
| `progress_pct` | float | % of topics with mastery achieved (0-100) |

### Usage

```python
state = get_session_state()

# Which topics need review today?
if state['fsrs_due_today']:
    print(f"Study {len(state['fsrs_due_today'])} topics today")

# Are there weak areas?
if state['weak_topics']:
    print(f"Struggling with: {state['weak_topics'][0]['topic']}")

# Overall progress?
print(f"Progress: {state['progress_pct']:.1f}%")
```

### In Conversation

```
User: "What should I study?"

Claude: [Calls get_session_state]

Claude: "You have 3 topics due today:
        1. Shock (due: 2026-06-04)
        2. Sepsis (due: 2026-06-03)
        3. Stroke (due: 2026-06-05)
        
        You're also struggling with vasopressors (35% error rate).
        
        Overall progress: 25.3% of topics mastered."
```

---

## 3. get_next_topic

Get the system's recommended next topic (FSRS-prioritized, weak-area-aware).

### Signature

```python
get_next_topic(session_id: str = "default") -> Dict[str, Any]
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `session_id` | str | "default" | Session identifier for tracking follow-ups |

### Returns

```json
{
  "topic": "vasopressors",
  "reason": "active_follow_up",
  "retrieval_query": "Comprehensive guide to vasopressors in shock management",
  "suggested_phase": "drilling",
  "is_nested": true,
  "parent_topic_available_after_mastery": true
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `topic` | str | Recommended topic name |
| `reason` | str | Why this topic was selected |
| `retrieval_query` | str | Suggested search query for mcp_retrieval |
| `suggested_phase` | str | `new_material`, `drilling`, `case_application`, `integration` |
| `is_nested` | bool | True if this is a nested follow-up session |
| `parent_topic_available_after_mastery` | bool | Will return to parent topic after mastery |

### Reason Values

| Reason | Priority | Explanation |
|--------|----------|-------------|
| `active_follow_up` | 0 (highest) | Nested session in progress (paused parent lesson) |
| `due_today` | 1 | FSRS review date reached |
| `weak` | 2 | >25% error rate in last 7 days |
| `new_material` | 3 | Never attempted before |
| `integration` | 4 (lowest) | Challenge question / review |

### Phase Values

| Phase | Purpose |
|-------|---------|
| `new_material` | First exposure to topic |
| `drilling` | Repeated practice on known topic |
| `case_application` | Apply knowledge to clinical scenarios |
| `integration` | Cross-topic integration challenges |

### Examples

**Example 1: Due for review**
```python
next_topic = get_next_topic()
# Returns: {"topic": "shock", "reason": "due_today", ...}
```

**Example 2: In conversation**
```
User: "Ready for the next topic."

Claude: [Calls get_next_topic()]

Claude: "Great! Let's drill vasopressors — you had trouble with 
        dosing last time (35% error rate).
        
        Here's what you need to know about vasopressors..."
        
        [Calls mcp_retrieval("vasopressors management")]
```

---

## 4. submit_answer

Record student answer and update mastery tracking (FSRS, confidence weighting, mastery gates).

### Signature

```python
submit_answer(
    topic: str,
    user_answer: str,
    is_correct: bool,
    confidence_reported: int,
    teach_back_quality: float = 0.0,
    transfer_success: bool = False,
    session_id: str = "default",
    mistake_type: str = "other",
    subtopic: Optional[str] = None
) -> Dict[str, Any]
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `topic` | str | required | Topic name (e.g., "shock") |
| `user_answer` | str | required | Student's verbatim answer |
| `is_correct` | bool | required | True if answer is correct |
| `confidence_reported` | int | required | Student's confidence (1-5 scale) |
| `teach_back_quality` | float | 0.0 | Mechanistic understanding (0-1 rubric) |
| `transfer_success` | bool | False | True if answer applied knowledge to novel context |
| `session_id` | str | "default" | Session identifier |
| `mistake_type` | str | "other" | Error classification: `recall`, `mechanism`, `dosing`, `differential`, `other` |
| `subtopic` | Optional[str] | None | Subtopic for nested sessions (e.g., "vasopressor_dosing") |

### Confidence Scale

| Value | Meaning |
|-------|---------|
| 1 | Guessing / random response |
| 2 | Somewhat uncertain |
| 3 | Neutral / 50-50 |
| 4 | Fairly confident |
| 5 | Certain / very confident |

### Teach-Back Quality Scale

The student explains the mechanism in their own words:

| Value | Criteria |
|-------|----------|
| 0.0 | No explanation or completely wrong |
| 0.3 | Partial/surface-level explanation |
| 0.6 | Mostly correct mechanism, minor gaps |
| 0.8 | Complete mechanism, clear language |
| 1.0 | Textbook-quality mechanistic explanation |

### Returns

```json
{
  "ok": true,
  "next_review_date": "2026-06-07T14:30:00",
  "mastery_updated": true,
  "level_achieved": "baseline",
  "follow_up_complete": false
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `ok` | bool | Success indicator |
| `next_review_date` | str | ISO8601 timestamp of next FSRS review |
| `mastery_updated` | bool | Whether mastery vector was updated |
| `level_achieved` | str or null | `baseline`, `intermediate`, `advanced`, or null |
| `follow_up_complete` | bool | True if nested session achieved mastery |
| `error` | str | Error message if `ok=false` |

### Examples

**Example 1: Correct answer with high confidence**
```python
result = submit_answer(
    topic="shock",
    user_answer="Norepinephrine increases both afterload and inotropy",
    is_correct=True,
    confidence_reported=5,
    teach_back_quality=0.9
)
# Returns: next_review_date 7 days out, mastery updated
```

**Example 2: Incorrect answer with low confidence**
```python
result = submit_answer(
    topic="vasopressors",
    user_answer="Dopamine has no inotropic effect",
    is_correct=False,
    confidence_reported=2,
    teach_back_quality=0.0,
    mistake_type="mechanism"
)
# Returns: next_review_date 1 day out (weighting down), weak area flagged
```

**Example 3: Transfer success (clinical application)**
```python
result = submit_answer(
    topic="shock",
    user_answer="Patient with septic shock needs fluids + vasopressor",
    is_correct=True,
    confidence_reported=4,
    teach_back_quality=0.8,
    transfer_success=True  # Applied to novel case
)
# Returns: mastery accelerated
```

**Example 4: In conversation**
```
User: "Norepinephrine primarily increases heart rate by beta-1 effects."

Claude: [Evaluates as incorrect]
        [Calls submit_answer(
           topic="vasopressors",
           user_answer="Norepinephrine primarily increases heart rate by beta-1 effects",
           is_correct=False,
           confidence_reported=3,
           mistake_type="mechanism"
        )]

Claude: "Not quite. Norepinephrine's main effect is alpha-1 
        vasoconstriction, which increases blood pressure. 
        Beta-1 effects on heart rate are secondary.
        
        Next review scheduled for 2026-06-05."
```

### Confidence Weighting Algorithm

If correct:
- High confidence (5): Interval multiplied by 1.5x
- Mid confidence (3): Interval 1.0x
- Low confidence (1): Interval 0.7x

If incorrect:
- High confidence (5): Interval 0.5x (surprised learning)
- Low confidence (1): Interval 0.9x (expected)

### Mastery Level Criteria

| Level | Criteria |
|-------|----------|
| `baseline` | ≥75% accuracy, teach-back ≥0.6, confidence ≥3 |
| `intermediate` | ≥85% accuracy, teach-back ≥0.75, transfer in 3/5 cases |
| `advanced` | ≥90% accuracy, teach-back ≥0.85, cross-context transfer, retention ≥90% at 6mo |

---

## 5. get_mastery_gates

Check mastery status across all topics and phase advancement readiness.

### Signature

```python
get_mastery_gates() -> Dict[str, Any]
```

### Parameters

None. Returns mastery for all topics.

### Returns

```json
{
  "mastery_matrix": {
    "shock": {
      "level": "advanced",
      "vector": {
        "accuracy": 0.95,
        "transfer_auc": 0.92,
        "mechanism_quality": 0.88,
        "calibration_icc": 0.85,
        "retention_6mo": 0.90,
        "integration_score": 0.87
      }
    },
    "sepsis": {
      "level": "baseline",
      "vector": {
        "accuracy": 0.78,
        "transfer_auc": 0.62,
        "mechanism_quality": 0.65,
        "calibration_icc": 0.58,
        "retention_6mo": 0.70,
        "integration_score": 0.55
      }
    },
    "vasopressors": {
      "level": null,
      "vector": {
        "accuracy": 0.45,
        "transfer_auc": 0.40,
        "mechanism_quality": 0.30,
        "calibration_icc": 0.25,
        "retention_6mo": 0.20,
        "integration_score": 0.15
      }
    }
  },
  "ready_for_phase_advance": false
}
```

### Mastery Vector Fields

| Field | Description |
|-------|-------------|
| `accuracy` | % correct answers on recent attempts |
| `transfer_auc` | AUC on transfer/application questions |
| `mechanism_quality` | Average teach-back quality score |
| `calibration_icc` | ICC between reported confidence and actual correctness |
| `retention_6mo` | Estimated 6-month retention rate |
| `integration_score` | Performance on cross-topic integration questions |

### Mastery Levels

| Level | Threshold |
|-------|-----------|
| `null` | Not started or <50% accuracy |
| `baseline` | Accuracy ≥75%, mechanism ≥0.6 |
| `intermediate` | Accuracy ≥85%, transfer_auc ≥0.70, mechanism ≥0.75 |
| `advanced` | Accuracy ≥90%, transfer_auc ≥0.85, mechanism ≥0.85, calibration ≥0.75 |

### Phase Advancement Criteria

`ready_for_phase_advance` = true when:
- ≥80% of topics at `advanced` level
- Overall accuracy ≥90%
- Transfer AUC ≥0.85 across topics

### Usage

```python
gates = get_mastery_gates()

# Check if ready to advance phase
if gates['ready_for_phase_advance']:
    print("Ready for ICU phase!")

# Find weakest topic
weakest = min(gates['mastery_matrix'].items(), 
              key=lambda x: x[1]['vector']['accuracy'])
print(f"Weakest topic: {weakest[0]} ({weakest[1]['level']})")
```

---

## 6. get_progress

Get overall progress statistics across curricula.

### Signature

```python
get_progress() -> Dict[str, Any]
```

### Parameters

None.

### Returns

```json
{
  "intern_medicine_pct": 31.2,
  "icu_pct": 8.5,
  "anesthesia_pct": 2.1,
  "overall_pct": 25.4,
  "hours_studied": 12.5
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `intern_medicine_pct` | float | % topics mastered in intern year curriculum (0-100) |
| `icu_pct` | float | % topics mastered in ICU curriculum (0-100) |
| `anesthesia_pct` | float | % topics mastered in anesthesia curriculum (0-100) |
| `overall_pct` | float | Overall % mastered across all curricula (0-100) |
| `hours_studied` | float | Estimated hours of study (1 session ≈ 45 min) |

### Usage

```python
progress = get_progress()

print(f"Overall progress: {progress['overall_pct']:.1f}%")
print(f"Time invested: {progress['hours_studied']:.1f} hours")
```

---

## 7. request_follow_up

Request deeper learning on a subtopic during parent lesson (nested learning sessions).

### Signature

```python
request_follow_up(
    parent_topic: str,
    requested_subtopic: str,
    session_id: str = "default"
) -> Dict[str, Any]
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent_topic` | str | required | Parent topic (e.g., "shock") |
| `requested_subtopic` | str | required | Subtopic to drill (e.g., "vasopressors") |
| `session_id` | str | "default" | Current session ID |

### Returns

```json
{
  "ok": true,
  "parent_topic": "shock",
  "child_topic": "vasopressors",
  "follow_up_session_id": 42,
  "related_subtopics": ["fluid_resuscitation", "cardiac_output"],
  "retrieval_query": "Comprehensive guide to vasopressors in shock management",
  "suggested_phase": "drilling"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `ok` | bool | Success indicator |
| `parent_topic` | str | Parent topic name |
| `child_topic` | str | Child topic name |
| `follow_up_session_id` | int | ID for nested session |
| `related_subtopics` | List[str] | Other child topics available |
| `retrieval_query` | str | Search query for mcp_retrieval |
| `suggested_phase` | str | Suggested learning phase |
| `error` | str | Error message if `ok=false` |

### Usage Pattern

```
1. Student learning "shock"
2. Student asks: "I want to learn more about vasopressors"
3. Call request_follow_up("shock", "vasopressors")
4. System pauses parent lesson, starts child lesson
5. Calls get_next_topic() returns vasopressors
6. Student drills vasopressors
7. After mastery, system returns to shock lesson
```

### Nested Session Flow

```
Session Start
  ↓
teach(shock) — mcp_retrieval("shock management")
  ↓
User: "Let's drill vasopressors"
  ↓
request_follow_up("shock", "vasopressors")
  ↓
[Pause shock lesson]
[Start vasopressors lesson]
  ↓
get_next_topic() → "vasopressors"
  ↓
submit_answer(topic="vasopressors", ...) × N
  ↓
[Achieve baseline mastery on vasopressors]
  ↓
follow_up_complete=True
  ↓
[Resume shock lesson]
  ↓
Session End
```

### Example in Conversation

```
User: "I understand shock, but I need more on vasopressors specifically."

Claude: [Calls request_follow_up("shock", "vasopressors")]

Claude: "Let's take a deeper dive into vasopressors. I'm pausing 
        the shock lesson and starting a vasopressor drilling session.
        
        Here's what you need to master on vasopressors..."
        
        [Calls mcp_retrieval("Comprehensive guide to vasopressors")]
        
User: [Drills vasopressors]

[After baseline mastery achieved]

Claude: "Great! You've mastered vasopressors. Let's return to shock 
        management and apply this knowledge."
```

---

## Error Handling

All endpoints return graceful errors:

```json
{
  "ok": false,
  "error": "Topic 'invalid_topic' not found"
}
```

Common error scenarios:

| Scenario | Error | Resolution |
|----------|-------|-----------|
| Topic not in database | Topic not found | Initialize database with `populate_phase1_knowledge.py` |
| Database locked | SQLite database is locked | Wait for other processes to release lock |
| Chroma connection failed | Chroma connection failed | Restart server, check `data/chroma_db/` |
| Empty knowledge base | No results for query | Ensure knowledge base was ingested |

---

## Rate Limiting

No rate limits. All tools are local and can be called as frequently as needed.

---

## Versioning

Current version: **1.0** (2026-06-04)

All endpoints are stable and production-ready.

---

**Last Updated:** 2026-06-04  
**Status:** Complete & Production Ready
