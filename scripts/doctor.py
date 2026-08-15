"""One-command system diagnosis (and repair) for Clinical Attending OS.

The ops console for this system is a Claude Code session driven from a phone —
so any future session must be able to assess EVERYTHING with one command and
fix the common failures with a second. No hunting through logs.

    .venv\\Scripts\\python.exe scripts\\doctor.py          # diagnose
    .venv\\Scripts\\python.exe scripts\\doctor.py --fix    # + restart what's down

Checks: local API, public Funnel endpoint, instructions version, scheduled
tasks, DB integrity + freshness, Drive backup age, repo bundle age, disk
space, git state, recent server-log errors.
Exit code 0 = all green; 1 = something needs attention (listed).
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PUBLIC = "https://john-desktop-pavilion-hampton.tail712dd4.ts.net/api"
LOCAL = "http://127.0.0.1:8010"

PROBLEMS: list[str] = []


def ok(label: str, detail: str = "") -> None:
    print(f"  [OK]   {label}" + (f" — {detail}" if detail else ""))


def bad(label: str, detail: str = "") -> None:
    PROBLEMS.append(label)
    print(f"  [FAIL] {label}" + (f" — {detail}" if detail else ""))


def http(url: str, timeout: int = 15) -> tuple[int, str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")[:500]
    except Exception as exc:
        return 0, str(exc)[:200]


def ps(cmd: str) -> str:
    r = subprocess.run(["powershell", "-NoProfile", "-Command", cmd],
                       capture_output=True, text=True, timeout=60)
    return (r.stdout or "") + (r.stderr or "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true",
                    help="restart the API task / server if down")
    args = ap.parse_args()
    now = datetime.now(timezone.utc)
    print(f"DOCTOR — {now.isoformat()[:19]}Z\n")

    # 1. Local API
    code, body = http(f"{LOCAL}/health", 10)
    if code == 200 and "clinical_attending_os" in body:
        ok("local API (8010)")
    else:
        bad("local API (8010)", body)
        if args.fix:
            print("       fixing: restarting ClinicalAttendingOS-API task...")
            ps("Stop-ScheduledTask -TaskName ClinicalAttendingOS-API -ErrorAction SilentlyContinue; "
               "Start-ScheduledTask -TaskName ClinicalAttendingOS-API")
            import time
            for _ in range(24):
                time.sleep(5)
                code, body = http(f"{LOCAL}/health", 5)
                if code == 200:
                    ok("local API after restart")
                    PROBLEMS.pop()
                    break
            else:
                print("       restart did NOT bring it back — check "
                      "storage/logs/api_server.log")

    # 2. Public endpoint (what ChatGPT sees)
    code, body = http(f"{PUBLIC}/health", 20)
    if code == 200 and "clinical_attending_os" in body:
        ok("public Funnel endpoint")
    else:
        bad("public Funnel endpoint", body)
        print("       (if local is OK, check: tailscale funnel status)")

    # 3. Instructions version (fetch fully — http() truncates for display)
    try:
        with urllib.request.urlopen(f"{PUBLIC}/system_instructions", timeout=20) as r:
            payload = json.load(r)
        ok("live instructions", f"version {payload['version']}, {len(payload['instructions'])} chars")
    except Exception as exc:
        bad("live instructions", str(exc)[:150])

    # 4. Scheduled tasks
    out = ps("Get-ScheduledTask -TaskName 'ClinicalAttendingOS-*' | "
             "ForEach-Object { \"$($_.TaskName)=$($_.State)\" }")
    seen = {}
    for line in out.splitlines():
        if "=" in line:
            name, state = line.strip().split("=", 1)
            seen[name] = state
    for name, want in (("ClinicalAttendingOS-API", ("Running",)),
                       ("ClinicalAttendingOS-WeeklyBackup", ("Ready", "Running")),
                       ("ClinicalAttendingOS-WeeklyDigest", ("Ready", "Running"))):
        state = seen.get(name, "MISSING")
        if state in want:
            ok(f"task {name}", state)
        else:
            bad(f"task {name}", state)
            if args.fix and name == "ClinicalAttendingOS-API" and state != "MISSING":
                ps(f"Start-ScheduledTask -TaskName {name}")
                print(f"       fix attempted: started {name}")

    # 5. Database
    from src.config import settings
    db = Path(settings.sqlite_db_path)
    if not db.exists():
        bad("student DB", "missing")
    else:
        try:
            con = sqlite3.connect(str(db))
            integ = con.execute("PRAGMA integrity_check").fetchone()[0]
            n, newest = con.execute(
                "SELECT COUNT(*), MAX(date) FROM question_attempts").fetchone()
            kp = con.execute("SELECT COUNT(*) FROM knowledge_points").fetchone()[0]
            con.close()
            if integ == "ok":
                ok("student DB", f"integrity ok, {n} attempts (newest {str(newest)[:10]}), {kp} KPs")
            else:
                bad("student DB integrity", integ[:100])
        except Exception as exc:
            bad("student DB", str(exc)[:150])

    # 6. Drive backup freshness (daily task -> should be < 48h old)
    rclone = str(Path.home() / "rclone.exe")
    if Path(rclone).exists():
        r = subprocess.run([rclone, "lsl", "gdrive:tutor_backups/student_model_latest.db"],
                           capture_output=True, text=True, timeout=60)
        line = (r.stdout or "").strip().splitlines()
        if r.returncode == 0 and line:
            parts = line[-1].split()
            try:
                ts = datetime.fromisoformat(parts[1] + "T" + parts[2][:8])
                age_h = (datetime.now() - ts).total_seconds() / 3600
                (ok if age_h < 48 else bad)("Drive DB backup", f"{age_h:.0f}h old")
            except Exception:
                ok("Drive DB backup", "present (age unparsed)")
        else:
            bad("Drive DB backup", (r.stderr or "not found")[:120])
        r2 = subprocess.run([rclone, "lsl", "gdrive:tutor_backups/clinical-attending-os-latest.bundle"],
                            capture_output=True, text=True, timeout=60)
        if r2.returncode == 0 and r2.stdout.strip():
            ok("Drive repo bundle", "present")
        else:
            bad("Drive repo bundle", "missing")
    else:
        bad("rclone", "not at ~/rclone.exe")

    # 7. Disk space
    import shutil as _sh
    free_gb = _sh.disk_usage("C:\\").free / 1e9
    (ok if free_gb > 10 else bad)("disk space", f"{free_gb:.0f} GB free")

    # 8. Git state
    r = subprocess.run(["git", "-C", str(ROOT), "status", "--short"],
                       capture_output=True, text=True, timeout=30)
    dirty = [l for l in r.stdout.splitlines() if "units.json" not in l]
    r2 = subprocess.run(["git", "-C", str(ROOT), "rev-list", "--count",
                         "origin/main..HEAD"], capture_output=True, text=True, timeout=30)
    ahead = (r2.stdout or "0").strip()
    ok("git", f"{ahead} commits unpushed" + (f", {len(dirty)} dirty files" if dirty else ", tree clean"))
    # Push path: SSH key (~/.ssh/id_ed25519_github). Verify it still
    # authenticates — a broken push path is invisible until you need it.
    ssh_test = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no",
         "-T", "git@github.com"], capture_output=True, text=True, timeout=45)
    if "successfully authenticated" in (ssh_test.stderr + ssh_test.stdout):
        ok("github push path (SSH)")
    else:
        bad("github push path (SSH)", (ssh_test.stderr or "no response")[:120])

    # 9. Recent server-log errors
    log = ROOT / "storage" / "logs" / "api_server.log"
    if log.exists():
        tail = log.read_text(encoding="utf-8", errors="replace").splitlines()[-200:]
        errs = [l for l in tail if "Traceback" in l or "ERROR" in l]
        (ok if not errs else bad)("server log (last 200 lines)",
                                  f"{len(errs)} error lines" if errs else "clean")
        for e in errs[-3:]:
            print("       ", e[:120])

    print()
    if PROBLEMS:
        print(f"PROBLEMS ({len(PROBLEMS)}): " + "; ".join(PROBLEMS))
        sys.exit(1)
    print("ALL GREEN")


if __name__ == "__main__":
    main()
