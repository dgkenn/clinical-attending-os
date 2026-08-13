# Render Deployment Notes

Local laptop mode is the recommended free setup because it can use local PDFs, local Chroma, and SQLite directly. Render is useful only if you want a stable HTTPS URL and are willing to manage persistent disk/storage limits.

## Render Setup

1. Create a new Web Service from this repo.
2. Use Python 3.11+.
3. Build command:

```bash
pip install -r requirements.txt
```

4. Start command:

```bash
uvicorn src.api:app --host 0.0.0.0 --port $PORT
```

## Environment Variables

```text
BACKEND_MODE=retrieval_only
FREE_LOCAL_MODE=true
EMBEDDING_PROVIDER=local
LOCAL_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
API_GENERATION_ENABLED=false
DATA_DIR=/opt/render/project/src/data
CHROMA_DIR=storage/chroma
SQLITE_DB_PATH=storage/sqlite/student_model.db
API_KEY=<random secret>
DEFAULT_TRAINING_PHASE=intern_year
ANESTHESIA_CROSSOVER_PERCENT=0.10
```

## Persistent Disk

Attach a persistent disk for `storage/` if you want Chroma and SQLite to survive deploys. Without a disk, re-ingest after redeploy.

## Ingestion

Render shells can run:

```bash
python -m src.ingest --force
```

Large textbook PDFs may exceed free-tier disk/build limits. For free use, local laptop plus tunnel is usually simpler.

## Custom GPT

Use the Render HTTPS URL as the `servers.url` value in `openapi.json`. Configure Action authentication with header `X-API-Key`.

## Troubleshooting

- If retrieval is empty, confirm PDFs are present and `storage/chroma/chunks.jsonl` exists.
- If local model loading fails, disable vector retrieval and rely on BM25 or use a smaller cached model.
- If database resets, attach persistent disk and point `SQLITE_DB_PATH` at it.
