# Operations runbook — phone-first

**Design goal: this system is operated from a phone.** You talk to a Claude
Code session; it diagnoses and repairs. Sitting at the PC is never required
for anything routine. If you find yourself needing physical access, that is a
bug in this runbook — say so and it gets fixed.

## For the Claude Code session (read this first)

```
cd C:\Users\jackk\github\clinical-attending-os
.venv\Scripts\python.exe scripts\doctor.py          # full system state
.venv\Scripts\python.exe scripts\doctor.py --fix    # + auto-restart what's down
```

`doctor.py` checks, in one pass: local API, public Funnel endpoint, live
instructions version, all three scheduled tasks, DB integrity + freshness,
Drive backup age, repo bundle presence, disk space, git state, and recent
server-log errors. Exit 0 = green, 1 = problems (named in the last line).
**Run it before diagnosing anything.** Do not go log-diving first.

## The five failures that actually happen

| Symptom (what the user reports) | Cause | Fix |
|---|---|---|
| "ChatGPT says it can't reach the backend" | uvicorn died or PC rebooted | `doctor.py --fix` |
| "Everything times out" | Funnel dropped | `& "C:\Program Files\Tailscale\tailscale.exe" funnel --bg --set-path /api 8010` |
| "The tutor is behaving like the old version" | ChatGPT cached instructions | Tell user: start a NEW conversation. (Claude: re-paste Project instructions.) |
| "It's not calling a tool it should have" | GPT schema stale after an endpoint change | Tell user: delete + re-import the action from `/api/openapi.json`, re-set the `X-API-Key` header |
| "My progress looks wrong / lost" | check before touching anything | `doctor.py` shows attempt count + newest date; Drive has `student_model_latest.db` and one `_prev` generation |

## Pushing to GitHub

Push uses an **SSH key** (`~/.ssh/id_ed25519_github`, no passphrase, so
unattended sessions can push), configured in `~/.ssh/config` with the remote
at `git@github.com:dgkenn/clinical-attending-os.git`. `doctor.py` verifies the
handshake on every run.

The old HTTPS path is dead and should not be revived: the cached
`x-access-token` credential authenticates as the user and the REST API even
reports `push: true` (that field reflects the USER's permissions, not the
token's), but the token is read-scoped — every push returned 403. If SSH auth
ever breaks, generate a new key and add the PUBLIC half at
github.com/settings/ssh/new (`scripts/add_ssh_key_to_github.ps1` copies it to
the clipboard and opens the page); do not go back to token auth.

## Standing constraints (do not break)

- **Never let a test write the real DB.** `tests/conftest.py` isolates pytest,
  but ad-hoc scripts and TestClient calls bypass it — copy the DB to a temp
  path and point `settings.sqlite_db_path` at the copy (see
  `scripts/cleanup_20260815_test_pollution.py` for the safe pattern).
- **ChatGPT Actions cap = 30 operations.** The served schema is at exactly 30.
  Adding an endpoint means hiding one (`include_in_schema=False`).
- **Instruction changes need no re-import** (ChatGPT fetches live) — only
  SCHEMA changes do.
- **Restarting the API after code changes**: kill the uvicorn PID on 8010; the
  scheduled task's restart loop brings it back in ~15s. Verify with doctor.
- **The DB is the irreplaceable asset.** Code is bundled to Drive daily and
  reproducible; study history is not.

## Scheduled automation (all at logon or nightly — nothing manual)

| Task | When | What |
|---|---|---|
| `ClinicalAttendingOS-API` | At logon, restarts on exit | Keeps uvicorn alive on 8010 |
| `ClinicalAttendingOS-WeeklyBackup` | Daily 03:00 | DB → Drive (staleness-guarded, keeps one prev) + repo bundle |
| `ClinicalAttendingOS-WeeklyDigest` | Sundays 03:10 | Learning digest → `storage/logs` + Drive |

## Recovery from total machine loss

1. `rclone copyto gdrive:tutor_backups/clinical-attending-os-latest.bundle repo.bundle`
2. `git clone repo.bundle clinical-attending-os`
3. `.\setup_new_machine.ps1` (venv, deps, HF index, caches)
4. `rclone copyto gdrive:tutor_backups/student_model_latest.db storage\sqlite\student_model.db`
5. Re-register the three scheduled tasks (see `deploy/run_api_server.ps1` and SETUP.md)
6. Re-point `PUBLIC_BASE_URL` in `.env` at the new host's Funnel URL, regenerate
   `openapi.json`, re-import the action into the GPT.

## Health snapshot on demand

The user can ask the tutor itself "how's the system?" — but the authoritative
answer is `doctor.py`. The tutor only knows what its own calls returned.
