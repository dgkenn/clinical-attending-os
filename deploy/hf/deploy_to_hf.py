#!/usr/bin/env python3
"""One-shot deploy of the Clinical Attending OS tutor to Hugging Face (personal use).

Reads the HF token from deploy/hf/.hf_token (gitignored) or $HF_TOKEN.
Idempotent. Does NOT print the HF token. Prints the generated MCP bearer token
(needed for the Claude connector).

Steps:
  1. Create a PRIVATE dataset <user>/clinical-attending-index and upload the
     Chroma index (from D:) + curriculum/units.json.
  2. Create a PUBLIC Docker Space <user>/clinical-attending-os and push the
     server code + Dockerfile + a Space README (HF frontmatter).
  3. Set Space secrets: MCP_AUTH_TOKEN (generated), HF_TOKEN, INDEX_DATASET.
  4. Print the connector URL + bearer token.
"""
from __future__ import annotations
import os
import sys
import shutil
import secrets
import tempfile
import pathlib

from huggingface_hub import HfApi

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN_FILE = ROOT / "deploy" / "hf" / ".hf_token"
CHROMA_SRC = r"D:\anesthesia_attending\storage\chroma"
UNITS = ROOT / "storage" / "curriculum" / "units.json"

SPACE_README = """---
title: Clinical Attending OS
emoji: 🩺
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

Private medical-tutor MCP server (personal use). All tool access is gated by a
bearer token; the knowledge index is loaded from a private dataset at startup.
"""


def read_token() -> str:
    t = os.environ.get("HF_TOKEN", "")
    if not t and TOKEN_FILE.exists():
        t = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not t:
        sys.exit("No HF token found ($HF_TOKEN or deploy/hf/.hf_token).")
    return t


def main() -> None:
    token = read_token()
    api = HfApi(token=token)
    user = api.whoami()["name"]
    print("HF user:", user)

    index_repo = f"{user}/clinical-attending-index"
    space_repo = f"{user}/clinical-attending-os"

    # 1) Private dataset + index upload
    print("Creating private dataset", index_repo)
    api.create_repo(index_repo, repo_type="dataset", private=True, exist_ok=True)
    if not pathlib.Path(CHROMA_SRC, "chroma.sqlite3").exists():
        sys.exit(f"Chroma index not found at {CHROMA_SRC} (is D: connected?)")
    print("Uploading index (this can take several minutes)...")
    api.upload_folder(
        folder_path=CHROMA_SRC,
        repo_id=index_repo,
        repo_type="dataset",
        ignore_patterns=["*.predupe.bak", "*.bak"],
        commit_message="Upload Chroma index",
    )
    if UNITS.exists():
        api.upload_file(
            path_or_fileobj=str(UNITS),
            path_in_repo="curriculum/units.json",
            repo_id=index_repo,
            repo_type="dataset",
        )
    print("Index uploaded ->", index_repo)

    # 2) Public Docker Space + code push
    print("Creating Space", space_repo)
    api.create_repo(space_repo, repo_type="space", space_sdk="docker",
                    private=False, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="caos_space_"))
    shutil.copytree(ROOT / "src", tmp / "src",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    shutil.copy(ROOT / "requirements.txt", tmp / "requirements.txt")
    (tmp / "deploy" / "hf").mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "deploy" / "hf" / "start.sh", tmp / "deploy" / "hf" / "start.sh")
    shutil.copy(ROOT / "deploy" / "hf" / "Dockerfile", tmp / "Dockerfile")
    (tmp / "README.md").write_text(SPACE_README, encoding="utf-8")
    (tmp / "storage" / "curriculum").mkdir(parents=True, exist_ok=True)
    if UNITS.exists():
        shutil.copy(UNITS, tmp / "storage" / "curriculum" / "units.json")
    # Data files seeded into the DB at startup by build_server (curriculum blueprint,
    # generated knowledge-point catalog, dosing-drill rules). All best-effort.
    (tmp / "data").mkdir(parents=True, exist_ok=True)
    for _df in ("curriculum_blueprint.json", "kp_catalog.json", "dosing_rules.json"):
        _src = ROOT / "data" / _df
        if _src.exists():
            shutil.copy(_src, tmp / "data" / _df)
    print("Pushing Space code...")
    api.upload_folder(folder_path=str(tmp), repo_id=space_repo, repo_type="space",
                      commit_message="Deploy MCP server")
    shutil.rmtree(tmp, ignore_errors=True)
    print("Space code pushed ->", space_repo)

    # 2b) Seeded student DB (schema + topics) -> private state dataset.
    # Prefer the curated clean seed; fall back to the live dev DB only if absent.
    state_repo = f"{user}/clinical-attending-state"
    seed_db = ROOT / "deploy" / "hf" / "seed_student_model.db"
    db_local = seed_db if seed_db.exists() else (ROOT / "storage" / "sqlite" / "student_model.db")
    if db_local.exists():
        api.create_repo(state_repo, repo_type="dataset", private=True, exist_ok=True)
        # Preserve accumulated study progress: only seed when the dataset has no DB
        # yet, OR when RESET_PROGRESS is explicitly set (one-time cleanup / wipe).
        reset = os.getenv("RESET_PROGRESS", "") not in ("", "0", "false", "False")
        try:
            existing = api.list_repo_files(repo_id=state_repo, repo_type="dataset")
        except Exception:
            existing = []
        if reset or "student_model.db" not in existing:
            print("Uploading clean seed -> student_model.db",
                  "(RESET_PROGRESS)" if reset else "(first seed)")
            api.upload_file(path_or_fileobj=str(db_local), path_in_repo="student_model.db",
                            repo_id=state_repo, repo_type="dataset")
        else:
            print("Preserving existing progress (seed skipped; set RESET_PROGRESS=1 to wipe).")
    else:
        state_repo = ""

    # 3) Secrets (reuse a stable bearer token across redeploys)
    mcp_token_file = ROOT / "deploy" / "hf" / ".mcp_token"
    if mcp_token_file.exists():
        mcp_token = mcp_token_file.read_text(encoding="utf-8").strip()
    else:
        mcp_token = secrets.token_hex(32)
        mcp_token_file.write_text(mcp_token, encoding="utf-8")
    api.add_space_secret(repo_id=space_repo, key="MCP_AUTH_TOKEN", value=mcp_token)
    api.add_space_secret(repo_id=space_repo, key="HF_TOKEN", value=token)
    api.add_space_secret(repo_id=space_repo, key="INDEX_DATASET", value=index_repo)
    if state_repo:
        api.add_space_secret(repo_id=space_repo, key="STATE_DATASET", value=state_repo)
    print("Secrets set.")

    host = f"{user}-clinical-attending-os".lower().replace("_", "-")
    base = f"https://{host}.hf.space"
    print("\n==================== DEPLOY SUMMARY ====================")
    print("Space:          ", f"https://huggingface.co/spaces/{space_repo}")
    print("Connector URL:  ", base + "/mcp")
    print("Health URL:     ", base + "/health")
    print("Bearer token:    Authorization: Bearer " + mcp_token)
    print("Index dataset:  ", index_repo)
    print("========================================================")


if __name__ == "__main__":
    main()
