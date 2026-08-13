# Clinical Attending OS

Local retrieval and memory backend for an intern-year medicine, ICU, and anesthesiology tutor. ChatGPT Custom GPT provides the conversational teaching; this backend provides source retrieval, citations, session planning, and longitudinal memory.

## Libraries

Chunks are stored in one unified knowledge base with metadata:

- `intern_year_medicine`: MGH, intern survival notes, OnlineMedEd intern guide, hospital medicine notes.
- `ICU_critical_care`: Marino ICU and critical care sources.
- `anesthesiology_boards`: Stanford CA-1, Morgan & Mikhail, Miller/Baby Miller.
- `personal_notes` and `missed_questions`: future notes and missed question material.

Default sessions use `intern_year_medicine`. ICU and anesthesia are included only when relevant unless you switch phase.

## Setup

```powershell
cd C:\Users\Dean\anesthesia_attending
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

No OpenAI API key is required in free local mode. Generate a random `API_KEY` in `.env` before exposing the API through a tunnel.

## Local Free Mode

The default backend is retrieval-only:

```text
BACKEND_MODE=retrieval_only
FREE_LOCAL_MODE=true
EMBEDDING_PROVIDER=local
LOCAL_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
API_GENERATION_ENABLED=false
OPENAI_API_KEY=
```

If `FREE_LOCAL_MODE=true`, backend LLM generation is hard-blocked. Retrieval, ingestion, local embeddings, session planning, and SQLite memory work without API keys. If local embedding model files are not cached, retrieval falls back to JSONL/BM25 keyword search.

## Adding PDFs

Put PDFs in `data/` or set `SOURCE_FILES` in `.env`. Current configured sources include Marino ICU, MGH, two shorter intern notes documents, OnlineMedEd intern guide, Stanford CA-1, Morgan & Mikhail, and Miller/Baby Miller.

Manual source overrides can be added to `source_overrides.json`.

## Ingestion

```powershell
python -m src.ingest
python -m src.ingest --force
python -m src.ingest --source "Marino"
```

Ingestion uses PyMuPDF, removes repeated headers/footers, keeps chunks page-local, detects section headings, adds topic/context/keyword/synonym retrieval tags, and writes `storage/chroma/ingestion_manifest.json`.

Fact-level learning targets are generated from indexed chunks for intern notes, Marino, and anesthesia sources. CA-1/BASICS coverage remains Stanford-first when anesthesia mode is explicit.

## Retrieval Debugging

```powershell
python -m src.retrieval_debug
python -m src.audit_retrieval
python -m src.retrieval_eval
```

Use the debugger to inspect source, library, page, topic tags, keyword tags, BM25 score, vector score, final score, and excerpt. Retrieval quality depends most on chunk cleaning and retrieval tags, so audit top results before trusting a source set.

Golden checks flag expected source families for hyperkalemia, ARDS ventilation, shunt physiology, and LAST.

## Run API

```powershell
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs`. All endpoints except `/health` and FastAPI's `/openapi.json` require `X-API-Key` when `API_KEY` is set.

## Custom GPT (Voice-Mode Tutor)

1. Run the API locally:

```powershell
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

2. Expose with cloudflared (free, no signup):

```powershell
cloudflared tunnel --url http://127.0.0.1:8000
```

3. Replace `https://YOUR-TUNNEL-URL-HERE` in `openapi.json` with the tunnel URL.
4. Paste the schema into ChatGPT Custom GPT Actions.
5. Configure API key auth with header `X-API-Key` (set `API_KEY` in your `.env`).
6. Paste `CUSTOM_GPT_INSTRUCTIONS.md` into the GPT instructions.

### Voice loop

The Custom GPT calls `POST /next_lesson` to fetch a `VoiceLesson` (precomputed,
no LLM, p99 < 2s), narrates the `question`, waits for the user, grades the
answer, calls `POST /submit_answer`, narrates `mini_teach`, then asks the
`teachback_prompt`. The returned `session` is passed back on the next
`/next_lesson` call. Behind the scenes:

- Curriculum is built once from the ingested chunks (intern-guides spine,
  MGH for medicine depth, Marino for ICU spine, Stanford CA-1 interleaved at
  ~10% per `ANESTHESIA_CROSSOVER_PERCENT`, Morgan/Miller as anesthesia depth).
- Spaced repetition uses FSRS-4. Topic mastery and next-due dates are
  persisted in SQLite.
- Pedagogy: each session walks `warm_up_retrieval -> weak_topic_drilling ->
  new_material -> clinical_case_application -> teach_back` (Roediger/Karpicke
  testing effect, Bjork desirable difficulties, Bloom mastery learning).

### Other endpoints

- `POST /follow_up`: iterative multi-round search for in-lesson follow-up questions. Returns answer-bearing sentences pre-extracted. **Use this for "is the dose weight-based?" / "what's the mechanism?" / "what if X?" questions.**
- `POST /search`: ad-hoc retrieval for content questions.
- `POST /case_prep`: pre-shift case stem → 3-5 review topics with rationale and source snippets.
- `GET /weak_patterns`: repeat-offender (topic, mistake_type) pairs + overconfidence rate.
- `POST /tutor`: multi-section markdown answer for typed (non-voice) use.
- `POST /submit_answer`: log a graded attempt; updates FSRS state. Pass `confidence_reported` (1-5) to enable confidence calibration.
- `GET /progress`: curriculum progress by band (spine / deep_medicine / icu / anesthesia).
- `GET /due_reviews`, `GET /student_dashboard`: review queue + summary.

### Daily build pipeline

After the initial ingest, run these once after PDF changes:

```powershell
python -m src.dedupe_facts --no-near-dedupe   # 5s   — drops boilerplate, exact dupes
python -m src.cloze                            # 30s  — generates cloze cards
python -m src.curriculum                       # 5s   — orders units by band
python -m src.lesson_cache --progress 200      # 25min — pre-builds /next_lesson responses
python -m src.migrate_fsrs                     # 1s   — seeds FSRS state for legacy rows
python -m src.eval_runner --no-cross-encoder   # 1min — sanity-check retrieval quality
```

Then `uvicorn src.api:app` for the live server.

## Study Sessions

Default unspecified sessions:

- 50% due weak topics.
- 25% new granular intern-note facts.
- 15% unstable/recent material.
- 10% maintenance checks.
- 0-15% ICU/anesthesia crossover when relevant.

Switch for one session by asking for ICU or anesthesia. Persistently switch with:

```http
POST /set_default_phase
{"default_training_phase":"anesthesia_boards"}
```

## Student Memory

SQLite tracks topics, attempts, sessions, learned facts, mastery, confidence, due reviews, and next review dates. Important topics are not fully retired; high-mastery topics move to maintenance or rare review.

## Tunnel Security

Do not expose the API without `API_KEY`. The API returns compact excerpts only, not full PDFs. Keep your laptop awake while the Custom GPT is using the local tunnel. Free tunnel URLs may change, requiring an OpenAPI server URL update.

## Troubleshooting

- No retrieval results: run ingestion and verify `SOURCE_FILES`.
- Bad citations: inspect `python -m src.retrieval_debug`; citations only come from retrieved metadata.
- Weak confidence: add better source PDFs, re-ingest with `--force`, or improve source overrides/tags.
- Local model errors: set `LOCAL_MODELS_OFFLINE=false` once to download models, then return to `true`.
- Chroma reset: delete `storage/chroma` or run `python -m src.ingest --force`.
- Database reset: delete `storage/sqlite/student_model.db`.
