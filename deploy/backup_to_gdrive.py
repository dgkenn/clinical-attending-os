"""Weekly backup of the LOCAL student-progress DB to Google Drive via rclone.

Why this exists alongside deploy/hf/backup_progress.py:
  backup_progress.py pulls the DB *from the Hugging Face state dataset*. That is
  correct for the hosted-Space topology, where the Space syncs its SQLite up to
  HF on a timer. On a LOCAL install (Claude Desktop over stdio MCP, or the local
  FastAPI) nothing syncs local -> HF, so that script would faithfully back up a
  stale HF snapshot while the real progress sat on disk untouched. This script
  backs up the file you are actually studying against.

Behaviour (per the requested policy):
  * ONE file on Drive: gdrive:tutor_backups/student_model_latest.db — each run
    replaces it. No dated history is accumulated.
  * Before replacing, the existing remote file is kept for one generation as
    student_model_prev.db, and a staleness guard refuses to upload a backup
    whose newest attempt is OLDER than the copy already on Drive. Overwriting a
    good backup with an older or emptier database is the one failure mode that
    silently destroys study history, and it is exactly what nearly happened
    during the 2026-08 machine transfer.

Usage:
    python deploy/backup_to_gdrive.py            # normal run
    python deploy/backup_to_gdrive.py --dry-run  # show what would happen
    python deploy/backup_to_gdrive.py --force    # skip the staleness guard

Requires rclone on PATH (or at ~/rclone.exe) with a configured `gdrive:` remote.
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

REMOTE_DIR = "gdrive:tutor_backups"
REMOTE_LATEST = f"{REMOTE_DIR}/student_model_latest.db"
REMOTE_PREV = f"{REMOTE_DIR}/student_model_prev.db"


def _rclone() -> str:
    home_rclone = Path.home() / "rclone.exe"
    if home_rclone.exists():
        return str(home_rclone)
    found = shutil.which("rclone")
    if not found:
        sys.exit(
            "rclone not found. Install it and configure a 'gdrive:' remote:\n"
            "  winget install Rclone.Rclone\n"
            "  rclone config     # n) new remote, name it gdrive, type drive\n"
        )
    return found


def _newest_attempt(db_path: Path) -> str:
    """Newest question_attempts timestamp, or '' if unreadable/empty."""
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        row = con.execute("SELECT MAX(date) FROM question_attempts").fetchone()
        con.close()
        return (row[0] or "") if row else ""
    except Exception:
        return ""


def _attempt_count(db_path: Path) -> int:
    try:
        con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        row = con.execute("SELECT COUNT(*) FROM question_attempts").fetchone()
        con.close()
        return int(row[0]) if row else 0
    except Exception:
        return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="upload even if the remote copy looks newer")
    args = ap.parse_args()

    from src.config import settings  # noqa: E402  (needs sys.path above)

    local = Path(settings.sqlite_db_path)
    if not local.exists():
        sys.exit(f"Local DB not found: {local}")

    rclone = _rclone()
    local_newest = _newest_attempt(local)
    local_count = _attempt_count(local)
    print(f"local : {local}")
    print(f"        newest attempt {local_newest or '(none)'}, {local_count} attempts")

    # A blank or unreadable local DB must never overwrite a good backup: with
    # local_newest == "" the newest-vs-newest guard below can't fire (it
    # requires BOTH sides non-empty), which is precisely the
    # silently-destroy-history case this script exists to prevent.
    if not local_newest or local_count == 0:
        if not args.force:
            sys.exit(
                "REFUSING TO UPLOAD: local DB has no readable question_attempts "
                f"(newest={local_newest!r}, count={local_count}). A fresh or "
                "corrupt local DB must not replace the Drive backup. "
                "Re-run with --force only if you truly intend to reset it."
            )
        print("WARNING: uploading an empty/unreadable local DB because --force was given")

    # --- is the remote itself reachable? ---
    # This check must happen BEFORE any judgement about the remote FILE. An
    # unconfigured remote, an expired token or a network blip makes the
    # download below fail, and treating that failure as "no backup exists yet"
    # would silently skip the staleness guard and let an older local DB
    # overwrite a good backup. Absence of evidence is not evidence of absence.
    probe = subprocess.run([rclone, "lsd", "gdrive:", "--max-depth", "1"],
                           capture_output=True, text=True, timeout=120)
    if probe.returncode != 0:
        sys.exit(
            "Cannot reach the 'gdrive:' remote — refusing to run.\n"
            f"rclone said: {(probe.stderr or probe.stdout).strip()[:400]}\n\n"
            "If you have not configured it yet:\n"
            "  rclone config   # n) new remote -> name it exactly 'gdrive' -> type 'drive'\n"
        )

    # --- staleness guard: compare against whatever is already on Drive ---
    listing = subprocess.run([rclone, "lsf", REMOTE_LATEST],
                             capture_output=True, text=True, timeout=120)
    remote_exists = listing.returncode == 0 and listing.stdout.strip() != ""

    if remote_exists:
        with tempfile.TemporaryDirectory() as td:
            remote_copy = Path(td) / "remote_latest.db"
            got = subprocess.run(
                [rclone, "copyto", REMOTE_LATEST, str(remote_copy)],
                capture_output=True, text=True, timeout=300,
            )
            if got.returncode != 0 or not remote_copy.exists():
                sys.exit(
                    "Remote backup exists but could not be downloaded for comparison — "
                    "refusing to overwrite it blindly.\n"
                    f"rclone said: {(got.stderr or got.stdout).strip()[:400]}"
                )
            remote_newest = _newest_attempt(remote_copy)
            remote_count = _attempt_count(remote_copy)
            print(f"remote: {REMOTE_LATEST}")
            print(f"        newest attempt {remote_newest or '(none)'}, {remote_count} attempts")
            if remote_newest and local_newest and remote_newest > local_newest and not args.force:
                sys.exit(
                    "\nREFUSING TO UPLOAD: the copy on Drive is NEWER than the local DB.\n"
                    "Uploading would destroy study history that exists only on Drive.\n"
                    "Recover the Drive copy locally first:\n"
                    f"  rclone copyto {REMOTE_LATEST} \"{local}\"\n"
                    "or re-run with --force if you are certain the local copy is right."
                )
    else:
        print(f"remote: {REMOTE_LATEST} (confirmed absent — this is the first backup)")

    if args.dry_run:
        print("\n--dry-run: would rotate latest -> prev, then upload local DB.")
        return

    # --- rotate one generation, then upload ---
    rot = subprocess.run([rclone, "copyto", REMOTE_LATEST, REMOTE_PREV],
                         capture_output=True, text=True, timeout=300)
    if rot.returncode != 0 and remote_exists:
        # If a latest exists but can't be preserved, uploading would leave us
        # with NO previous generation — the safety net the docstring promises.
        sys.exit(
            "Could not rotate latest -> prev; refusing to overwrite the only "
            f"remote copy.\nrclone said: {(rot.stderr or rot.stdout).strip()[:300]}"
        )

    # Consistent snapshot (WAL-safe) rather than copying the live file.
    with tempfile.TemporaryDirectory() as td:
        snap = Path(td) / "student_model.db"
        src = sqlite3.connect(str(local))
        dst = sqlite3.connect(str(snap))
        with dst:
            src.backup(dst)
        dst.close()
        src.close()
        up = subprocess.run([rclone, "copyto", str(snap), REMOTE_LATEST, "--quiet"],
                            capture_output=True, text=True, timeout=600)
    if up.returncode != 0:
        sys.exit(f"Upload failed: {up.stderr.strip()}")

    print(f"\nBacked up -> {REMOTE_LATEST}")
    print(f"Previous generation kept at {REMOTE_PREV}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired as exc:
        sys.exit(f"rclone timed out ({exc.cmd[0] if exc.cmd else 'rclone'}): "
                 "backup NOT completed. Nothing was overwritten unless the "
                 "upload itself timed out mid-transfer — check with: "
                 "rclone lsl gdrive:tutor_backups/")
