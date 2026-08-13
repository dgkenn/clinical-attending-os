# Clinical Attending OS — Verified System Status

**Date:** 2026-06-16
**Verified empirically (not from prior phase docs).** This file supersedes the
status claims in `COMPLETION_SUMMARY.md`, `EXECUTION_SUMMARY.md`, and the
`PHASE*_COMPLETION_*` docs where they conflict.

---

## Corrections to prior docs (read first)

The earlier "PRODUCTION READY" docs contained material inaccuracies:

1. **"Chroma vector DB indexed (813+ units)" — was FALSE.** The retrieval index
   is built **only from the 8 source PDFs** (`ingest.py` → `discover_pdfs` →
   `build_chunks`). The hand-authored phase1–6 JSON units (`data/*.json`) were
   **never ingested** and fed nothing in the live system. *(As of 2026-06-16
   this has been fixed — see "Curated knowledge integration" below.)*
2. **Conflicting unit counts** (597 / 813 / 1321) across docs were build-artifact
   counts, not the live index. Live retrieval = PDF chunks; live curriculum is
   also derived from the same PDF chunks.
3. **"Retrieval ~26.6% pass-rate"** was a partial-index artifact. Real measured
   quality is far higher (see metrics).

---

## Architecture (verified)

- **Retrieval:** `src/retrieval.py` hybrid (vector + BM25 + cross-encoder rerank)
  over a Chroma collection `anesthesia_sources_local_baai_bge_small_en_v1_5`.
- **Embeddings:** local `BAAI/bge-small-en-v1.5`; reranker `BAAI/bge-reranker-base`.
- **Curriculum:** `src/curriculum.py` groups the same chunks (book→chapter→section)
  into `storage/curriculum/units.json` (2,507 units) for lesson ordering.
- **Tutoring state:** SQLite `storage/sqlite/student_model.db` (mastery, attempts,
  FSRS state, follow-up sessions).
- **MCP server:** `src/mcp_server.py` (`python -m src.mcp_server`) exposes 15
  FastMCP tools (9 legacy + 6 core). Launched by Claude Desktop.
- **Storage:** the Chroma store lives on **external drive D:**
  (`D:\anesthesia_attending\storage\chroma`, ~1.5 GB) via a directory junction at
  `storage/chroma`. **If D: is unplugged the junction dangles and all retrieval
  fails** (`os error 183`). Fix = reconnect D:; no rebuild needed.

## Knowledge index (verified counts)

| Source | Docs in Chroma |
|---|---|
| 8 textbook PDFs (Miller, Morgan & Mikhail, Marino, MGH, Stanford CA-1, intern guides) | 64,627 |
| Curated units (fact-checked, ingested 2026-06-16) | +946 |
| **Total** | **65,573** |

## Retrieval quality (verified via `python -m src.eval_runner`, n=104 gold set)

| Metric | PDF-only | After curated ingest |
|---|---|---|
| recall@10 | 0.904 | **0.962** |
| MRR@5 | 0.701 | **0.826** |
| nDCG@5 | 0.613 | **0.748** |

Remaining misses (4/104) are ICU-mode queries where the gold answer requires the
Marino ICU Book, which lacks dedicated ECMO / arterial-line pages.

## Tests

`python -m pytest -q` → **280 passed, 0 failed.**

---

## Curated knowledge integration (2026-06-16)

The orphaned phase1–6 hand-authored units were consolidated, **fact-checked
against the textbook corpus**, and selectively ingested:

- Candidates (deduped by id + text): **1,071** (`data/curated_candidates.json`)
- Fact-check verdicts (`data/factcheck/batch_*.json`):
  - KEEP 906 · FIX 40 (corrected before ingest) · DROP_DUP 113 ·
    DROP_INACCURATE 4 · FLAG 8 (unverifiable/safety-omission)
- **Ingested: 946** (`data/curated_keep.json`), tagged `source_name="Curated Units"`,
  `training_phase="curated"`, id prefix `curated-`. Additive/reversible.

The fact-check caught and removed/corrected dangerous errors (e.g. acetaminophen
transplant threshold off by 3×, IV metoprolol dose 10× high, CaCl arrest dose 5×
low, ceftriaxone in neonates, "painless" 2nd-degree burns, SIRS taught as
"Sepsis-3"). Dropped/flagged units are recorded in `data/factcheck/` and were NOT
ingested.

### Re-ingesting curated units (reproducible)
```
python -m src.ingest --curated data/curated_keep.json          # real
python -m src.ingest --curated data/curated_keep.json --dry-run # validate only
```
Note: a cold HuggingFace model cache makes `store_chunks_chroma` return
`chroma_upsert_ok: False` (offline guard). The model is now cached, so this works;
if it ever recurs, warm the cache once (any retrieval query) then re-run.

---

## What was fixed this session (2026-06-16)

1. Reconnected external D: → restored the (intact) 64,627-chunk Chroma index.
2. Restored `src/mcp_server.py` (had been emptied to 0 bytes on disk).
3. Completed the half-finished FSRS migration in `src/mcp_endpoints.py`
   (`compute_next_review` → `fsrs_review`; fixed `conn` factory usage and a
   non-existent `mastery_level` column). End-to-end `submit_answer` verified.
4. Ranking fixes (query expansions + reranker/answer-extraction boosts) for
   drug-named queries → 3 failing tests fixed, no eval regression.
5. Fact-checked + ingested 946 curated units (above).

## Known limitations

- ICU-mode retrieval still under-serves a few topics absent from Marino (ECMO, MTP
  calcium) — would need supplemental ICU content.
- `data/cumulative_all_phases.json/.jsonl` have large uncommitted edits (pre-existing).
- Much of the project source is untracked in git (the repo root is the user home
  directory). Persisting this work requires a deliberate, scoped commit.
