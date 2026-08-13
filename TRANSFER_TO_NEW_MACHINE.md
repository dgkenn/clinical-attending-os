# Transferring Clinical Attending OS to a New Computer

**Written 2026-08-13.** Everything below was verified against the live system on the
source machine — HF repos queried, Space health-checked, file sizes measured.

---

## TL;DR — you have three options, pick one

| Option | Setup time | Needs the 2.5 GB download? | Works offline? |
|---|---|---|---|
| **A. Use the hosted Space** | ~2 minutes | No | No |
| **B. Local install, index from Hugging Face** | ~30 min | Yes (2.48 GB) | Yes |
| **C. Local install, rebuild index from PDFs** | ~2-4 hours | No (needs the 8 PDFs, 203 MB) | Yes |

**Option B is the recommended full transfer.** Option A is the fastest way to be
studying again today. You do **not** need the D: drive for any of them.

---

## Critical facts about what lives where

The 1.5 GB Chroma vector store is **not** only on the D: drive. It was uploaded to a
private Hugging Face dataset on 2026-06-23 and is fully recoverable from there.

| Asset | Location | Size | Notes |
|---|---|---|---|
| Source code, docs, curriculum units | This git repo | 51 MB | 686 files |
| Vector index (Chroma) | HF dataset `deankennedy/clinical-attending-index` (private) | **2.48 GB** | `chroma.sqlite3` 1.64 GB + `chunks.jsonl` 425 MB + HNSW binaries |
| Student progress DB | HF dataset `deankennedy/clinical-attending-state` (private) | 7.4 MB | Last updated **2026-06-29** |
| Progress backups (dated) | `gdrive:tutor_backups/` | 7.4 MB each | Daily 2026-06-21 → **2026-07-16**, plus `student_model_latest.db` |
| Live hosted tutor | HF Space `deankennedy/clinical-attending-os` (public, token-gated) | — | **Verified live**: `/health` → 200, `/mcp` unauthenticated → 401 |
| Source PDFs | `C:\Users\Dean\Downloads\` on the old machine | 203 MB | Gitignored (copyrighted). Only needed for Option C. |
| Secrets | `.env`, `deploy/hf/.hf_token`, `deploy/hf/.mcp_token` | 4 KB | Gitignored. **Must be copied manually — see below.** |

### Which copy of your progress is newest

Three copies exist and they disagree. In order of recency:

1. **`gdrive:tutor_backups/student_model_latest.db`** — mirrors HF, most recent snapshot 2026-07-16
2. **HF `clinical-attending-state`** — last modified 2026-06-29
3. **Local `storage/sqlite/student_model.db`** on the old machine — 2026-06-23, **oldest**

Use the Google Drive copy. Do **not** copy the local file over a newer one — you would
lose roughly three weeks of mastery and FSRS scheduling state.

---

## Option A — Use the hosted Space (no install)

The Space is already deployed and running. On the new computer:

1. Open Claude → **Settings → Connectors → Add custom connector** (requires a paid Claude plan).
2. URL: `https://deankennedy-clinical-attending-os.hf.space/mcp`
3. Header: `Authorization: Bearer <token>`

The token is in `deploy/hf/.mcp_token` on the old machine. Open that file and copy the
value — it is not in git and is not printed anywhere in this document.

**Caveat:** free Spaces sleep after ~15 minutes idle and lose their local disk on rebuild.
`start.sh` re-pulls the index and student DB from the private datasets on boot, so sleep
is survivable — the first request after a sleep just takes ~60s. A keep-warm workflow
exists at `deploy/keepwarm.github-workflow.yml`.

---

## Option B — Full local install (recommended)

### Step 1: Prerequisites

- **Python 3.11** (source machine runs 3.11.9; 3.10+ works). Must be on PATH.
- **Git**
- ~8 GB free disk: 2.5 GB index + ~2 GB HuggingFace model cache + working room
- Optional: `rclone` configured with your `gdrive:` remote, to pull the newest progress DB

### Step 2: Clone and create the environment

```powershell
git clone https://github.com/dgkenn/clinical-attending-os.git
cd clinical-attending-os
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

This installs FastAPI, ChromaDB, sentence-transformers, PyMuPDF, llama-index, the MCP
SDK, and `rank-bm25`. Expect ~10 minutes and ~3 GB — torch comes along with
sentence-transformers.

### Step 3: Copy the secret files from the old machine

These are gitignored by design and will not arrive with the clone. Transfer them by USB
stick, password manager, or an encrypted channel — **not** by email or chat.

| File | What it holds |
|---|---|
| `.env` | Backend config + `API_KEY`. Start from `.env.example` if you would rather regenerate. |
| `deploy/hf/.hf_token` | Hugging Face **write** token. Needed to download the private index. |
| `deploy/hf/.mcp_token` | Bearer token for the hosted Space connector. Only needed for Option A. |

Then edit `.env` on the new machine and fix the absolute paths, which are hardcoded to
the old machine:

```
DATA_DIR=<new path>\clinical-attending-os\data
SOURCE_FILES=<new paths to the 8 PDFs, semicolon-separated>   # only needed for Option C
CHROMA_DIR=storage/chroma
SQLITE_DB_PATH=storage/sqlite/student_model.db
```

`CHROMA_DIR` and `SQLITE_DB_PATH` are relative — leave them alone. On the new machine
`storage/chroma` should be an **ordinary folder**, not a junction. Do not recreate the
D: junction; that was a disk-space workaround specific to the old laptop.

### Step 4: Download the vector index (2.48 GB)

```powershell
python -c "import pathlib; from huggingface_hub import snapshot_download; snapshot_download(repo_id='deankennedy/clinical-attending-index', repo_type='dataset', local_dir='storage/chroma', token=pathlib.Path('deploy/hf/.hf_token').read_text().strip())"
```

Verify — `storage/chroma/chroma.sqlite3` should be ~1.64 GB, alongside two UUID-named
subdirectories holding the HNSW binaries.

### Step 5: Restore your learning progress

Newest copy first (Google Drive):

```powershell
rclone copyto gdrive:tutor_backups/student_model_latest.db storage/sqlite/student_model.db
```

If rclone is not set up on the new machine, pull from Hugging Face instead — about a
week staler, but authoritative and needs no extra config:

```powershell
python -c "import pathlib,shutil,os; from huggingface_hub import hf_hub_download; os.makedirs('storage/sqlite',exist_ok=True); p=hf_hub_download(repo_id='deankennedy/clinical-attending-state',repo_type='dataset',filename='student_model.db',token=pathlib.Path('deploy/hf/.hf_token').read_text().strip()); shutil.copy(p,'storage/sqlite/student_model.db')"
```

### Step 6: Rebuild the regenerable caches

These are gitignored because they are large and derived. Run after the index is in place:

```powershell
python -m src.dedupe_facts --no-near-dedupe
python -m src.cloze
python -m src.curriculum
python -m src.lesson_cache --progress 200
python -m src.migrate_fsrs
```

`lesson_cache` is the slow one — roughly 25 minutes. It pre-builds `/next_lesson`
responses so voice mode answers in under 2 seconds. The system runs without it, just
more slowly on first touch of each lesson.

### Step 7: Verify before trusting it

```powershell
python -m pytest -q
```

Expect **280 passed**. Then check retrieval quality end to end:

```powershell
python -m src.eval_runner --no-cross-encoder
```

Expect roughly recall@10 0.96, MRR@5 0.83, nDCG@5 0.75 on the 104-question gold set.
Materially lower means the index did not download completely — check
`storage/chroma/chroma.sqlite3` size first.

First run downloads the embedding model `BAAI/bge-small-en-v1.5` and reranker
`BAAI/bge-reranker-base` (~600 MB). If `.env` has `LOCAL_MODELS_OFFLINE=true`, set it to
`false` for that first run, then set it back.

### Step 8: Wire up the tutor front end

**As a Claude Desktop MCP server** — edit `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "clinical-attending": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "C:\\path\\to\\clinical-attending-os"
    }
  }
}
```

Use double backslashes. Point `command` at the venv Python
(`C:\\path\\to\\clinical-attending-os\\.venv\\Scripts\\python.exe`) if the system Python
lacks the dependencies. Restart Claude Desktop fully. The server exposes 15 tools.

**Or as the HTTP API** (for the ChatGPT Custom GPT voice loop):

```powershell
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

Then `http://127.0.0.1:8000/docs`. All endpoints except `/health` require the `X-API-Key`
header when `API_KEY` is set in `.env`. To expose it to a Custom GPT, tunnel with
`cloudflared tunnel --url http://127.0.0.1:8000` and update the server URL in
`openapi.json`. Paste `CLAUDE_PROJECT_INSTRUCTIONS.md` into the GPT instructions.

---

## Option C — Rebuild the index from the PDFs

Only if you cannot reach Hugging Face. Copy all 8 PDFs from the old machine's
`Downloads` folder, set `SOURCE_FILES` in `.env` to their new paths, then:

```powershell
python -m src.ingest --force
```

Several hours: PyMuPDF text extraction, header/footer stripping, chunking, and local
embedding of ~64,600 chunks. Then re-ingest the fact-checked curated units, which are
in the repo and are **not** derived from the PDFs:

```powershell
python -m src.ingest --curated data/curated_keep.json
```

Skipping that second command costs you 946 hand-verified units and drops recall@10 from
0.962 to 0.904. Then continue from Step 5 above.

---

## Housekeeping worth doing during the move

1. **Progress backups stopped.** `deploy/hf/backup_progress.py` pulls the DB from HF to
   `~/tutor_backups` and Google Drive. The last dated snapshot is 2026-07-16 — whatever
   scheduled it is no longer running. Re-establish it on the new machine.

2. **The old repo is tangled.** On the old machine these files are tracked in *two*
   repos: this standalone one, and the `MeridianV2` repo rooted at `C:\Users\Dean`.
   Once the transfer is verified, remove them from MeridianV2's index so edits cannot
   land in the wrong place.

3. **Recover the D: drive separately.** `Get-Disk` on the old machine sees only the
   internal NVMe, so the enclosure is not enumerating — a hardware issue, not a Windows
   one. Nothing in this transfer depends on it, but D: may hold other projects.

4. **Scratch files came along.** `author_kps_part26_v3.py`, `_temp_slice_924_957.json`,
   and two malformed `C:UsersDean...` filenames are in the repo by choice, to avoid
   losing anything. Prune them once you are settled.
