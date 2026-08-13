#!/usr/bin/env python3
"""Push ONLY the Space code + curriculum blueprint to Hugging Face (no index upload).

Use this for code/curriculum changes when the Chroma index is unchanged — it is far
faster than the full deploy and never touches the corpus. The Space rebuilds on push
and re-seeds the curriculum at startup (UPSERT), so new blueprint topics land while
accumulated student progress (restored from the state dataset) is preserved.

Reads the HF token from deploy/hf/.hf_token (gitignored) or $HF_TOKEN.
Does NOT upload the Chroma index and does NOT touch the student-state dataset.
"""
from __future__ import annotations
import os
import sys
import shutil
import tempfile
import pathlib

from huggingface_hub import HfApi

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN_FILE = ROOT / "deploy" / "hf" / ".hf_token"
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
    space_repo = f"{user}/clinical-attending-os"
    print("HF user:", user, "| Space:", space_repo)

    api.create_repo(space_repo, repo_type="space", space_sdk="docker",
                    private=False, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="caos_code_"))
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
    (tmp / "data").mkdir(parents=True, exist_ok=True)
    for _df in ("curriculum_blueprint.json", "kp_catalog.json", "dosing_rules.json"):
        _src = ROOT / "data" / _df
        if _src.exists():
            shutil.copy(_src, tmp / "data" / _df)
    print("Pushing Space code + blueprint (no index upload)...")
    api.upload_folder(folder_path=str(tmp), repo_id=space_repo, repo_type="space",
                      commit_message="Code-only deploy: on-call approach topics")
    shutil.rmtree(tmp, ignore_errors=True)

    host = f"{user}-clinical-attending-os".lower().replace("_", "-")
    base = f"https://{host}.hf.space"
    print("Space code pushed. Rebuilding ->", f"https://huggingface.co/spaces/{space_repo}")
    print("Health URL:", base + "/health")


if __name__ == "__main__":
    main()
