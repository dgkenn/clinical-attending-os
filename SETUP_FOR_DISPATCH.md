# Runbook: Set up Clinical Attending OS as a Claude Desktop tutor

**For:** a dispatched Claude Code agent (has Bash/PowerShell/Read/Edit/Write).
**Goal:** wire the local MCP tutor server into Claude Desktop, install a
Claude-tailored tutor instruction block, and verify an end-to-end lesson works.
**Project root:** `C:\Users\Dean\anesthesia_attending` (run all commands from here).

Work only inside the project + the Claude Desktop config. Do NOT modify the
Chroma store on D:, and do NOT run `git commit` unless asked.

---

## Step 0 — Preconditions (verify, fix if broken)

Run each; all must pass before continuing.

1. **External drive D: is connected** (the 1.5 GB vector store lives there):
   ```powershell
   Get-Volume -DriveLetter D
   ```
   If absent: STOP and tell the user to plug in the Seagate drive — retrieval
   cannot work without it. No rebuild is needed once it's connected.

2. **Chroma index resolves and is populated** (expect ~65,573):
   ```bash
   python -c "from src.config import settings as s; import chromadb; print(chromadb.PersistentClient(path=str(s.chroma_dir)).get_collection(s.vector_collection_name()).count())"
   ```

3. **Dependencies + server import**:
   ```bash
   python -c "import mcp; import src.mcp_server as m; print('mcp+server OK; main:', hasattr(m,'main'))"
   ```
   If `mcp` is missing: `pip install mcp`.

4. **Tests green** (sanity):
   ```bash
   python -m pytest -q
   ```
   Expect `280 passed`.

5. **Resolve the Python interpreter path** that has `mcp` (Claude Desktop won't
   inherit your shell PATH — you must give it an absolute path):
   ```powershell
   (Get-Command python).Source
   ```
   Expected: `C:\Users\Dean\AppData\Local\Programs\Python\Python312\python.exe`.
   Call this `<PYTHON>` below.

---

## Step 1 — Register the MCP server in Claude Desktop

Config file: `C:\Users\Dean\AppData\Roaming\Claude\claude_desktop_config.json`

1. **Back it up first:**
   ```powershell
   Copy-Item "$env:APPDATA\Claude\claude_desktop_config.json" "$env:APPDATA\Claude\claude_desktop_config.json.bak" -Force
   ```

2. **Merge in an `mcpServers` block** (the file currently has none — add the key
   at the top level, preserving all existing `preferences`). Use the absolute
   `<PYTHON>` path from Step 0.5, JSON-escaped:
   ```json
   "mcpServers": {
     "clinical-attending-os": {
       "command": "C:\\Users\\Dean\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
       "args": ["-m", "src.mcp_server"],
       "cwd": "C:\\Users\\Dean\\anesthesia_attending"
     }
   }
   ```
   Edit the JSON programmatically (load → add key → write) so you don't corrupt
   the existing structure. Validate it parses:
   ```powershell
   Get-Content "$env:APPDATA\Claude\claude_desktop_config.json" -Raw | ConvertFrom-Json | Out-Null; "JSON valid"
   ```

3. The server reads `.env` from the project root automatically (FREE_LOCAL_MODE,
   local embeddings). Because `cwd` is set, no extra env is needed.

---

## Step 2 — Build the Claude-tailored tutor instruction block

The existing `CUSTOM_GPT_INSTRUCTIONS.md` is written for an OpenAPI Custom GPT and
references action names that DO NOT exist on the MCP server (`nextLesson`,
`submitAnswer`, `followUp`, `startTeachingMode`, `casePrep`, `getWeakPatterns`).

1. **Read the real registered tool names** and their signatures:
   ```bash
   grep -nE "mcp\.tool\(|^def " src/mcp_server.py
   ```
   The live tools are: `search_clinical_sources`, `answer_from_clinical_sources`,
   `start_study_session`, `submit_study_answer`, `get_due_reviews`,
   `get_student_dashboard`, `log_missed_topic`, `mark_topic_mastered`,
   `set_default_training_phase`, `mcp_retrieval`, `get_session_state`,
   `get_next_topic`, `submit_answer`, `get_mastery_gates`, `get_progress`.

2. **Confirm each tool's input/return shape** by reading `src/mcp_server.py`,
   `src/tutor_engine.py` (start_session / record_evaluated_answer), and
   `src/mcp_endpoints.py` (get_next_topic / submit_answer). You need to know what
   `start_study_session` and `submit_study_answer` return so the instructions
   describe the loop accurately.

3. **Write** `CLAUDE_DESKTOP_TUTOR_INSTRUCTIONS.md` — adapt the pedagogy from
   `CUSTOM_GPT_INSTRUCTIONS.md` but using the REAL tool names and verified return
   shapes. It MUST encode these principles (do not drop any):
   - **Never invent medicine.** Get every lesson/question from a tool; if a tool
     fails, say the backend is unreachable — do not improvise from training.
   - **Lesson loop:** `start_study_session(mode=...)` → ask the question → take the
     user's answer → grade `correct/partial/incorrect` + a `mistake_type` →
     **always** call the submit tool (`submit_study_answer` and/or `submit_answer`)
     → deliver the teach + the 1–2 sentence *why* → **auto-advance** to the next
     question in the same turn. Never end a turn waiting for "next".
   - **Confidence calibration:** ask for a 1–5 confidence before each answer and
     pass it through. (Engine: confident+wrong returns the card sooner ×0.7;
     uncertain+correct pushes it out ×1.2; confidence≥4 + wrong is auto-tagged
     `overconfident_wrong`.) Tell the user honesty here is the whole point.
   - **Teach-back:** after each item, ask the user to state the mechanism. Mastery
     (baseline→intermediate→advanced) requires mechanism, not just recall.
   - **Spaced review first:** at session start call `get_due_reviews` and surface
     weak areas (`get_progress` / `get_mastery_gates`); warn if overconfidence is
     trending high.
   - **Modes:** map context to mode — `intern_teach`, `cross_cover`, `ICU_teach`,
     `anesthesia_boards`, `crisis`, `drug`, `rapid_response`, `admission_plan`,
     `wards_rounding`, `pimp`.
   - **Follow-ups:** for mid-lesson "why/what-if" questions use
     `answer_from_clinical_sources` (or `search_clinical_sources`), answer fully,
     then return to the lesson.
   - **Citations:** the backend is the only source of truth; don't fabricate
     sources; for real-patient questions keep it educational and say "escalate to
     your local team."

4. Keep the full `CLAUDE_DESKTOP_TUTOR_INSTRUCTIONS.md` under ~1,500 words so it
   fits cleanly in a Claude Desktop Project's custom-instructions field.

---

## Step 3 — Install the instructions in Claude Desktop

Tell the user to do this (it cannot be automated — it's a GUI step):

1. Open Claude Desktop → create a **Project** named "Clinical Attending".
2. Paste the entire contents of `CLAUDE_DESKTOP_TUTOR_INSTRUCTIONS.md` into the
   project's **custom instructions**.
3. **Fully quit and reopen Claude Desktop** (so it loads the new
   `mcpServers` config). The `clinical-attending-os` tools should now appear.

---

## Step 4 — Smoke test (end to end)

1. After restart, in a new chat in that Project, the user asks:
   *"What MCP tools do you have?"* → confirm the `clinical-attending-os` tools list.
2. *"Start a study session in intern_teach mode. Pull my due reviews and weak
   patterns first, then run one lesson."* → confirm Claude calls
   `get_due_reviews` / `start_study_session`, asks a question, takes an answer +
   a 1–5 confidence, calls a submit tool, teaches the *why*, and auto-advances.
3. If the tools error in Claude Desktop, check the MCP logs at
   `%APPDATA%\Claude\logs\` and verify `<PYTHON> -m src.mcp_server` runs from the
   project cwd without error.

---

## Deliverables / report back
- Confirm Steps 0–2 passed (chroma count, tests, valid config JSON).
- The path to the new `CLAUDE_DESKTOP_TUTOR_INSTRUCTIONS.md`.
- The exact `mcpServers` block added (with the resolved Python path).
- The GUI steps the user still needs to do (Step 3) and the smoke-test result.

---

## Appendix A — Kickoff prompts the user will use
- **Start:** "Start a study session in <mode>. Pull my due reviews and weak
  patterns first, then run the lesson loop."
- **Before a real patient:** "I'm admitting a 70yo with a GI bleed — case prep."
- **Teach-back / protégé:** "Let me teach you about DKA management; quiz me."
- **Status:** "What's due today and what am I weakest at?"

## Appendix B — Optimal daily routine (bake into the instructions' intro)
~15 min/day: clear due reviews → new material in the current rotation's mode →
honest 1–5 confidence every item → always explain the mechanism. Add a `case prep`
before any real admission and one protégé-mode session on the weakest topic each
week. Short, daily, interleaved beats long cram blocks (FSRS only works if reviews
are done when due).
