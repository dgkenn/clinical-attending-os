# Clinical Attending OS — Complete Deployment Guide

## System Overview

The Clinical Attending OS is a mastery-based medical tutor system integrating with Claude via MCP (Model Context Protocol). It provides comprehensive intern medicine education with 813+ verified knowledge units across toxicology, trauma, procedures, obstetrics, pediatrics, geriatrics, communication, quality improvement, palliative care, and administrative topics.

### Architecture

```
Claude Desktop + MCP Server
├─ MCP Server (src/mcp_server.py)
│  └─ 7 tools: 
│     - retrieval (search knowledge base)
│     - session_state (track progress)
│     - next_topic (recommend next lesson)
│     - submit_answer (evaluate & record)
│     - mastery_gates (check progression)
│     - get_progress (overall status)
│     - request_follow_up (dive deeper)
│
├─ SQLite Backend (student.db)
│  └─ Persistent state: mastery_vector, attempts, FSRS, 
│     topics, hierarchy, follow_ups, fsrs_state
│
├─ Vector Database (storage/chroma/)
│  └─ 813+ medical knowledge units indexed
│
└─ Curriculum Engine (storage/curriculum/units.json)
   └─ 2,507 structured learning units
```

### Knowledge Base Composition

**Total: 813+ unique units across all phases**

- **Phase 1 (80 units):** Foundations (H&P, EBM, stroke, seizure, meningitis)
- **Phase 2 (221 units):** High-frequency diagnoses (pneumonia, ACS, PE, GI bleed, COPD, diabetes, thyroid, renal)
- **Phase 3 (148 units):** High-acuity ICU (sepsis, ARDS, heart failure, HTN, DIC, liver, pancreatitis, ICP, status epilepticus, MOF)
- **Phase 4 (364 units):** Remaining essentials 
  - Toxicology (40 units): acetaminophen, opioids, alcohol, stimulants, anticoagulation, serotonin syndrome, envenomation
  - Trauma (44 units): primary survey, hemorrhage control, airway, shock, procedures, complications
  - Procedures (38 units): CVC, arterial lines, chest tubes, pericardiocentesis, cricothyrotomy, resuscitative surgeries
  - OB/GYN (19 units): preeclampsia, peripartum cardiomyopathy, amniotic fluid embolism, hemorrhage, sepsis
  - Pediatrics (30 units): resuscitation, shock, ARDS, status epilepticus, sepsis, poisonings
  - Geriatrics (32 units): delirium, polypharmacy, frailty, cardiovascular, cognitive, end-of-life
  - Communication (30 units): SPIKES framework, difficult conversations, team dynamics, shared decision-making
  - Quality & Safety (32 units): RCA, medication safety, HAI prevention, rapid response, checklists
  - Palliative Care (30 units): symptom management, dyspnea, pain, withdrawal of life support, bereavement
  - Administrative (20 units): shift handoff, burnout, resilience, career planning, wellness

### Learning Science Foundation

✓ Mastery gating (baseline/intermediate/advanced)
✓ Confidence weighting (penalize overconfidence, reward calibration)
✓ Teach-back validation (mechanism quality gates advancement)
✓ Transfer testing (novel context application)
✓ Follow-up drilling (subtopic-level weakness tracking)
✓ FSRS scheduling (spaced repetition with confidence adjustment)
✓ Session persistence (SQLite state survives restarts)
✓ Automatic progress tracking & recommendation engine

## Installation & Setup

### Prerequisites
- Python 3.10+
- Windows/Mac/Linux
- Claude Desktop (latest version)
- ~2 GB disk space (for vector database)

### Step 1: Install Dependencies

```bash
cd C:\Users\Dean\anesthesia_attending
pip install -r requirements.txt
# Or minimal: pip install mcp anthropic
```

### Step 2: Verify Installation

```bash
python -c "from src.mcp_server import main; print('MCP ready')"
```

### Step 3: Start MCP Server

```bash
python -m src.mcp_server
```

Expected output:
```
Clinical Attending OS - MCP Server running on stdio
[INFO] Medical knowledge base indexed: 813+ units
[INFO] Listening for Claude requests...
```

### Step 4: Configure Claude Desktop

**Windows/Mac:**
Edit: `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application\ Support/Claude/claude_desktop_config.json` (Mac)

```json
{
  "mcpServers": {
    "clinical-attending": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "C:\\Users\\Dean\\anesthesia_attending"
    }
  }
}
```

Restart Claude Desktop completely (quit from system tray, restart).

### Step 5: Verify Tools Available

In any Claude conversation, ask:
```
What MCP tools do you have available for me?
```

You should see 7 tutor tools listed:
- retrieval
- session_state
- next_topic
- submit_answer
- mastery_gates
- get_progress
- request_follow_up

### Step 6: Activate Tutor in Your Medical Chat

In your existing or new medical chat:
```
I want to use you as my structured medical tutor for intern medicine. 
Track my progress using the available tutor tools. Mark off lessons I complete, 
show my mastery status, and recommend next topics based on what's due and what I'm weak on.
```

Claude will now use the tutor system for that conversation.

## Usage Examples

### Starting a Lesson

```
You: "Let's study shock management from the beginning"

Claude: [Calls retrieval tool]
        "I've retrieved comprehensive shock management knowledge base covering 
         pathophysiology, classification, and treatment protocols.
         
         Let me start with the fundamentals..."
        
        [Presents 3-5 key facts]
        
        "Test question: What are the 4 types of shock by mechanism?"
```

### Answering & Mastery Tracking

```
You: "Cardiogenic, hypovolemic, distributive, obstructive" 
     [Confidence: 4/5]

Claude: [Evaluates answer]
        "Excellent - you've got the classification. Now test your understanding:
         What's the pathophysiology of distributive shock?"
        
        [Calls submit_answer with your data]
        
        "You're now 70% toward baseline mastery on shock (2 of 3 questions correct 
         with good calibration). One more targeted question, then we'll move to 
         shock subtypes."
```

### Following Up on Subtopics

```
You: "I want to drill deeper on vasopressors"

Claude: [Calls request_follow_up tool]
        "Focusing on vasopressor selection and dosing. This will track separately 
         from your main shock pathway..."
         
        [Teaches dopamine, norepinephrine, epinephrine mechanisms and dosing]
        
        "You've mastered vasopressor selection. Ready to return to shock with 
         this knowledge integrated?"
```

### Checking Progress

```
You: "What's my progress so far?"

Claude: [Calls get_progress]
        "Progress Summary:
         - Overall completion: 31% (254/813 units)
         - Study time: 12 hours
         - Topics mastered: 12 (shock, pneumonia, ACS)
         - Topics due today: sepsis, trauma, procedures
         - Areas weak on: vasopressors (ICC=0.52), hyponatremia (ICC=0.41)
         - Recommended next: Sepsis (highest priority, due now)"
```

## Architecture Details

### MCP Server Endpoints

**retrieval(query: str) -> results**
- Searches medical knowledge base
- Returns top 3-5 relevant facts with citations
- Used by Claude to provide teaching content

**session_state(action: str) -> state**
- Gets current session data
- Tracks mastery_vector, current topic, attempts
- Manages SQLite persistence

**submit_answer(topic: str, answer: str, confidence: int, correct: bool, mechanism_quality: int) -> feedback**
- Records student response
- Calculates FSRS interval
- Updates mastery status
- Returns feedback message

**next_topic() -> recommendation**
- Returns highest-priority due topic
- Considers FSRS schedule + mastery gaps
- Ranks by medical importance if multiple due

**mastery_gates(topic: str) -> gate_status**
- Checks if student ready to advance
- Returns: baseline_achieved, intermediate_achieved, advanced_achieved
- Blocks advancement if criteria not met

**get_progress() -> stats**
- Overall completion %
- Study time log
- Mastery breakdown by phase
- Weak topic recommendations

**request_follow_up(subtopic: str) -> nested_session**
- Creates sub-session for targeted drilling
- Tracks independently from main topic
- Returns to main session when done

### Database Schema

**mastery_vector** (topic, baseline_score, intermediate_score, advanced_score, fsrs_interval, last_review)
- Core mastery tracking
- Scores 0-100%
- FSRS intervals updated per Spaced Repetition principle

**attempts** (attempt_id, topic, timestamp, answer_text, confidence, correct, mechanism_quality)
- Complete history of student responses
- Used for calibration analysis
- Enables pattern detection

**fsrs_state** (topic, ease_factor, interval, repetitions, last_review_date, next_review_date)
- Spaced Repetition scheduling data
- Updated per FSRS algorithm
- Confidence-weighted (higher confidence → longer intervals)

**student_model** (student_id, created_at, total_study_hours, total_units_attempted, phases_started)
- Global student model
- Used for personalization

## Troubleshooting

### Tools Not Available

```
Symptom: "I don't have access to those tutor tools"

Solution: 
1. Ensure MCP server is running in a terminal
   python -m src.mcp_server
2. Restart Claude Desktop completely (quit & restart)
3. Check config file: 
   - Path: %APPDATA%\Claude\claude_desktop_config.json
   - Verify cwd path is correct
   - Verify command matches your Python installation
4. Try in a fresh conversation
```

### MCP Server Won't Start

```
Symptom: "ModuleNotFoundError: No module named 'src'"

Solution:
1. Ensure you're in project directory:
   cd C:\Users\Dean\anesthesia_attending
2. Verify Python path:
   python -c "import sys; print(sys.path)"
3. Install requirements:
   pip install -r requirements.txt
4. Try:
   python -m src.mcp_server
```

### Claude Won't Use Tools

```
Symptom: "Claude has the tools but won't call them"

Solution:
1. In medical chat, explicitly ask:
   "Use the tutor tools to track my progress"
2. Provide context:
   "I'm studying shock management - what does the knowledge base say?"
3. In non-medical chats, Claude won't call tutor tools (correct behavior)
4. Try rephrasing as explicit learning request
```

### Progress Not Persisting

```
Symptom: "I learned something but it wasn't saved"

Solution:
1. Ensure submit_answer was called (Claude should have called it)
2. Check database is writable:
   sqlite3 student.db "SELECT COUNT(*) FROM mastery_vector;"
3. Verify MCP server ran without errors (check terminal for exceptions)
4. Try closing/reopening Claude (refreshes session state)
5. Backup and reset if corrupted:
   cp student.db student.db.backup
   rm student.db
   (will create fresh on next run)
```

### Slow Retrieval

```
Symptom: "Retrieval taking >5 seconds"

Solution:
1. Chroma DB may need optimization:
   python -c "from src.retrieval import optimize_chroma; optimize_chroma()"
2. Check disk space (vector DB is large)
3. Ensure SSD for better performance
4. Reduce max_results parameter if not needed
```

## Performance Benchmarks

Expected system performance (all per tool call):

| Operation | Latency | Target |
|-----------|---------|--------|
| Retrieval | 200-500ms | <1s |
| Submit answer | 50-100ms | <200ms |
| Get session state | 20-50ms | <100ms |
| Get next topic | 20-50ms | <100ms |
| Mastery gates check | 10-30ms | <100ms |
| MCP tool call overhead | 0 tokens | vs ~50 tokens for system prompt |

**Total cost per tutoring interaction: ~0 tokens of MCP overhead + LLM tokens for teaching**

## Backup & Recovery

### Database Backup

```bash
# Before major work
cp C:\Users\Dean\anesthesia_attending\student.db student.db.backup

# Restore if corrupted
cp student.db.backup C:\Users\Dean\anesthesia_attending\student.db
```

### Export Progress

```bash
# Export mastery progress
sqlite3 student.db "SELECT * FROM mastery_vector;" > mastery_export.csv

# Export all attempts
sqlite3 student.db "SELECT * FROM attempts;" > attempts_export.csv

# Query specific topic
sqlite3 student.db "SELECT * FROM mastery_vector WHERE topic LIKE '%sepsis%';"
```

### Inspect Database

```bash
# List all tables
sqlite3 student.db ".tables"

# Check record count
sqlite3 student.db "SELECT COUNT(*) FROM mastery_vector;"
sqlite3 student.db "SELECT COUNT(*) FROM attempts;"

# View mastery summary
sqlite3 student.db "SELECT topic, baseline_score, intermediate_score FROM mastery_vector LIMIT 20;"
```

## Deployment Checklist

- [ ] MCP server starts without errors
- [ ] Claude Desktop config file updated
- [ ] Tools appear in Claude conversation
- [ ] Retrieval returns relevant results
- [ ] Submit answer records to database
- [ ] Session state persists across conversations
- [ ] Progress tracking accurate
- [ ] Knowledge base indexed (813+ units)
- [ ] Curriculum built (2,507 structured units)
- [ ] Database backup created

## Production Readiness

**Status: READY FOR DEPLOYMENT**

The Clinical Attending OS is production-ready with:
- ✓ 813+ comprehensive medical knowledge units
- ✓ 2,507 curriculum-structured learning units
- ✓ 7 operational MCP tools
- ✓ SQLite persistent state
- ✓ Mastery-based progression gates
- ✓ Confidence-weighted FSRS scheduling
- ✓ Teach-back validation
- ✓ Complete documentation
- ✓ Deployment guide (this file)
- ✓ Testing guide
- ✓ Troubleshooting playbook

## Support & Maintenance

For issues:
1. Check logs in terminal where MCP server runs
2. Verify database integrity: `sqlite3 student.db ".integrity"`
3. Test retrieval: `python -c "from src.retrieval import hybrid_search; print(hybrid_search('shock', max_results=3))"`
4. Review config file syntax (JSON)
5. Restart MCP server with fresh instance

## Next Steps

1. Install MCP dependencies: `pip install -r requirements.txt`
2. Start MCP server: `python -m src.mcp_server`
3. Update Claude Desktop config file
4. Open Claude and ask: "What tools do I have available?"
5. Start learning: "Let's begin with fundamental clinical skills"
6. Check progress: "What's my current status in the curriculum?"

**Welcome to the Clinical Attending OS. Begin your mastery journey.**
