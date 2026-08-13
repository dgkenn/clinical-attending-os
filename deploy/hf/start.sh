#!/usr/bin/env bash
# HF Space entrypoint: ensure the Chroma index is present, then run the server.
# Required Space secrets/vars:
#   MCP_AUTH_TOKEN  - bearer token Claude must send (gates all tool access)
#   HF_TOKEN        - read token for the private index dataset
#   INDEX_DATASET   - e.g. "youruser/clinical-attending-index"
# Optional:
#   STATE_DATASET   - private dataset to persist the SQLite student DB across rebuilds
set -euo pipefail

CHROMA_DIR="${CHROMA_DIR:-/app/storage/chroma}"
SQLITE_PATH="${SQLITE_DB_PATH:-/app/storage/sqlite/student_model.db}"
mkdir -p "$CHROMA_DIR" "$(dirname "$SQLITE_PATH")"

# 1) Pull the vector index from the private dataset if not already present.
if [ ! -f "$CHROMA_DIR/chroma.sqlite3" ]; then
  echo "[start] downloading index from ${INDEX_DATASET} ..."
  python - <<'PY'
import os
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id=os.environ["INDEX_DATASET"],
    repo_type="dataset",
    local_dir=os.environ.get("CHROMA_DIR", "/app/storage/chroma"),
    token=os.environ.get("HF_TOKEN"),
)
print("[start] index download complete")
PY
fi

# 2) Restore prior student progress if a STATE_DATASET is configured.
if [ -n "${STATE_DATASET:-}" ] && [ ! -f "$SQLITE_PATH" ]; then
  echo "[start] restoring student DB from ${STATE_DATASET} ..."
  python - <<'PY' || echo "[start] no prior student DB (first run)"
import os
from huggingface_hub import hf_hub_download
p = hf_hub_download(repo_id=os.environ["STATE_DATASET"], repo_type="dataset",
                    filename="student_model.db", token=os.environ.get("HF_TOKEN"))
import shutil
dest = os.environ.get("SQLITE_DB_PATH", "/app/storage/sqlite/student_model.db")
os.makedirs(os.path.dirname(dest), exist_ok=True)
shutil.copy(p, dest)
print("[start] student DB restored")
PY
fi

echo "[start] launching MCP server on ${MCP_HOST}:${MCP_PORT} (transport=${MCP_TRANSPORT})"
exec python -m src.mcp_server
