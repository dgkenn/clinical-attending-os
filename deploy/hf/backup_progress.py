"""Pull the latest tutor progress DB from your private HF state dataset down to a
backup YOU control: a local folder, plus Google Drive (rclone) if available.

This is the "true forever" copy — even if Hugging Face vanished, your progress
sits in storage you own. Run anytime:  python deploy/hf/backup_progress.py
Reads the HF token from deploy/hf/.hf_token (or $HF_TOKEN).
"""
import os
import sys
import shutil
import subprocess
import pathlib
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN_FILE = ROOT / "deploy" / "hf" / ".hf_token"
BACKUP_DIR = pathlib.Path.home() / "tutor_backups"
KEEP_LAST = 30  # dated backups to retain


def _token() -> str:
    t = os.environ.get("HF_TOKEN", "")
    if not t and TOKEN_FILE.exists():
        t = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not t:
        sys.exit("No HF token (deploy/hf/.hf_token or $HF_TOKEN).")
    return t


def main() -> None:
    from huggingface_hub import HfApi, hf_hub_download
    tok = _token()
    api = HfApi(token=tok)
    user = api.whoami()["name"]
    repo = f"{user}/clinical-attending-state"

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    src = hf_hub_download(repo_id=repo, repo_type="dataset",
                          filename="student_model.db", token=tok)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dated = BACKUP_DIR / f"student_model_{stamp}.db"
    latest = BACKUP_DIR / "student_model_latest.db"
    shutil.copy(src, dated)
    shutil.copy(src, latest)
    print(f"Backed up -> {dated}  ({dated.stat().st_size} bytes)")

    # prune old dated backups
    backups = sorted(BACKUP_DIR.glob("student_model_2*.db"))
    for old in backups[:-KEEP_LAST]:
        try:
            old.unlink()
        except Exception:
            pass

    # best-effort copy to Google Drive via rclone (won't fail the backup)
    rclone = None
    home_rclone = pathlib.Path.home() / "rclone.exe"
    if home_rclone.exists():
        rclone = str(home_rclone)
    elif shutil.which("rclone"):
        rclone = "rclone"
    if rclone:
        try:
            subprocess.run([rclone, "copy", str(BACKUP_DIR),
                            "gdrive:tutor_backups/", "--quiet"],
                           timeout=180, check=False)
            print("Copied backups -> gdrive:tutor_backups/")
        except Exception as exc:
            print(f"(Google Drive copy skipped: {exc})")
    else:
        print("(rclone not found; local backup only)")


if __name__ == "__main__":
    main()
