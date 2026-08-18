"""Restart the servers ONLY when no study session is live.

The maintainer restarted mid-session twice in one morning; a severed MCP
session leaves the user's tutor hanging against a dead connection — reported
as "it's been stuck for over an hour". A session is considered live when a
tool call landed recently; default threshold 15 minutes.

    python scripts/safe_restart.py            # refuses if a session is live
    python scripts/safe_restart.py --force    # restart anyway (user consented)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

IDLE_MINUTES = 15


def minutes_since_last_call() -> float | None:
    log = Path(settings.log_dir) / "tool_calls.log"
    if not log.exists():
        return None
    lines = [l for l in log.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    if not lines:
        return None
    # Only REAL tutor tool calls indicate a live session. Names beginning with
    # "_" are internal markers the server writes about itself
    # (_sources_delivered, _grounded_declared) and are emitted by the test suite
    # and maintenance scripts. Counting them made this guard refuse a restart
    # because of my own testing seconds earlier, with no user session anywhere.
    for line in reversed(lines):
        parts = line.split("\t")
        if len(parts) < 2 or parts[1].startswith("_"):
            continue
        try:
            last = datetime.fromisoformat(parts[0]).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        return (datetime.now(timezone.utc) - last).total_seconds() / 60
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    idle = minutes_since_last_call()
    if idle is not None and idle < IDLE_MINUTES and not args.force:
        raise SystemExit(
            f"REFUSING: a tool call landed {idle:.0f} min ago — a session is "
            f"likely live, and restarting severs its MCP connection (the tutor "
            f"then hangs on a dead session). Wait for {IDLE_MINUTES} idle "
            f"minutes or ask the user, then re-run (--force to override).")

    print(f"last tool call {'never' if idle is None else f'{idle:.0f} min ago'} — safe to restart")
    subprocess.run([
        "powershell", "-NoProfile", "-Command",
        "Get-NetTCPConnection -LocalPort 8010,8011 -State Listen -EA SilentlyContinue | "
        "Select-Object -Expand OwningProcess -Unique | "
        "ForEach-Object { Stop-Process -Id $_ -Force -EA SilentlyContinue }"])
    for _ in range(14):
        time.sleep(8)
        try:
            a = urllib.request.urlopen("http://127.0.0.1:8010/health", timeout=5).status
            m = urllib.request.urlopen("http://127.0.0.1:8011/health", timeout=5).status
            if a == 200 and m == 200:
                print("both servers up")
                return
        except Exception:
            continue
    raise SystemExit("servers did not come back — run doctor.py --fix")


if __name__ == "__main__":
    main()
