# Prompt for the Claude session on the new machine

Copy everything inside the fence below into a fresh Claude Code session on the new
computer, after cloning the repo. Replace `<REPO_URL>` and `<PROJECT_PATH>` first.

Contains no secrets — it tells Claude where to *find* the tokens locally.

---

```
I'm setting up my medical tutor backend (Clinical Attending OS) on a new computer.

FASTEST PATH: run `.\setup_new_machine.ps1` from the repo root. It does the whole
install end to end — venv, dependencies, .env, index download, progress restore,
cache rebuild, tests — and prints the Claude Desktop config at the end. It is
idempotent, so re-run it after any failure. It will ask for my Hugging Face token
once. Watch its output and tell me if any step warns or fails.

If the script fails in a way you can't resolve, fall back to the manual sequence:
read TRANSFER_TO_NEW_MACHINE.md and execute Option B. Background below either way.

WHAT THIS IS
A retrieval + memory backend for an intern-medicine / ICU / anesthesiology tutor.
Hybrid retrieval (vector + BM25 + cross-encoder rerank) over ~65,573 chunks from 8
textbooks plus 946 fact-checked curated units. Student mastery and FSRS-4 spaced
repetition live in SQLite. Two front ends: a FastAPI HTTP API (src/api.py) and an
MCP server (src/mcp_server.py, 15 tools) for Claude Desktop.

WHERE EVERYTHING LIVES
- Code: this repo, cloned from <REPO_URL>, at <PROJECT_PATH>
- Vector index: private HF dataset deankennedy/clinical-attending-index (2.48 GB,
  chroma.sqlite3 is 1.64 GB). Download into storage/chroma as an ORDINARY FOLDER.
- Student progress: newest copy is gdrive:tutor_backups/student_model_latest.db
  (2026-07-16). HF dataset deankennedy/clinical-attending-state is the fallback
  (2026-06-29). The copy on my old laptop is the OLDEST (2026-06-23) — never
  restore that one over a newer file.
- Live hosted tutor: HF Space deankennedy/clinical-attending-os, endpoint
  https://deankennedy-clinical-attending-os.hf.space/mcp (verified live, returns
  401 without a bearer token). This keeps working regardless of the local install.
- Source PDFs: not in the repo (copyrighted, gitignored). Only needed if the HF
  index download fails and you must rebuild with `python -m src.ingest --force`.

CREDENTIALS — I copy these in manually, they are NOT in git
- .env                   backend config + API_KEY
- deploy/hf/.hf_token    Hugging Face write token; needed for the index download
- deploy/hf/.mcp_token   bearer token for the hosted Space connector
Tell me if any are missing rather than inventing values. Never commit them, never
print their contents, and never paste them into a web page or message.

WHAT I NEED YOU TO DO
1. Read TRANSFER_TO_NEW_MACHINE.md.
2. Confirm Python 3.10+ and ~8 GB free disk.
3. Create the venv, pip install -r requirements.txt.
4. Check that the three credential files exist. Then fix the absolute paths in
   .env — DATA_DIR and SOURCE_FILES still point at C:\Users\Dean on the old
   machine. Leave CHROMA_DIR and SQLITE_DB_PATH relative.
5. Download the index from HF into storage/chroma. Verify chroma.sqlite3 is
   ~1.64 GB before continuing.
6. Restore student_model.db from Google Drive if rclone is configured here,
   otherwise from the HF state dataset. Tell me which one you used and its date.
7. Rebuild the derived caches: dedupe_facts, cloze, curriculum, lesson_cache
   (~25 min), migrate_fsrs.
8. Verify: `python -m pytest -q` should be 280 passed, and
   `python -m src.eval_runner --no-cross-encoder` should be about recall@10 0.96 /
   MRR@5 0.83 / nDCG@5 0.75. Show me the real output — if numbers are materially
   lower, the index download was probably incomplete.
9. Configure the Claude Desktop MCP server per Step 8 of the guide, pointing
   `command` at the venv Python.

THINGS THAT WILL TRIP YOU UP
- On the old laptop storage/chroma was a junction to a D: drive that no longer
  enumerates. Do NOT recreate that junction. A plain folder is correct here.
- First retrieval downloads BAAI/bge-small-en-v1.5 and bge-reranker-base (~600 MB).
  If .env has LOCAL_MODELS_OFFLINE=true, flip it to false for that first run, then
  set it back.
- FREE_LOCAL_MODE=true hard-blocks backend LLM generation. That is intentional —
  retrieval only, no API key required. Don't "fix" it.
- If local embedding models aren't cached, retrieval silently falls back to
  BM25 keyword search. Quieter and worse — check eval numbers, don't assume.

Start by reading the guide and telling me your plan before you install anything.
```

---

## After it's running, verify with real questions

Ask the tutor something whose answer you can check against a source — LAST
management, hyperkalemia treatment, ARDS ventilation settings, shunt physiology.
Those four are the golden checks the retrieval suite uses. Citations come only from
retrieved chunk metadata, so a confident answer with no citation means retrieval
failed and something upstream is generating from memory.
