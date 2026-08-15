# Keeps the Clinical Attending OS API alive on 127.0.0.1:8010.
#
# Registered as the "ClinicalAttendingOS-API" scheduled task (at logon). The
# Tailscale Funnel (https://<host>/api -> 127.0.0.1:8010) persists across
# reboots on its own, but the uvicorn process does not — without this task the
# public endpoint silently 502s after every reboot and the ChatGPT connector
# looks "down" for no visible reason.
#
# Restart-on-exit loop rather than a one-shot start: uvicorn can die (unhandled
# error, OOM), and a study session shouldn't stay dead until someone notices.
# The venv python is invoked by absolute path — python.exe is NOT on PATH on
# this machine (only the py launcher), which has already broken one script here.

$ROOT = Split-Path $PSScriptRoot -Parent
$PY = Join-Path $ROOT ".venv\Scripts\python.exe"
$LOG = Join-Path $ROOT "storage\logs\api_server.log"

New-Item -ItemType Directory -Force (Split-Path $LOG) | Out-Null

while ($true) {
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content $LOG "[$stamp] starting uvicorn"
    # Blocks until the server exits. Output goes to the log; keep only the
    # newest ~2 MB so it can't grow without bound.
    & $PY -m uvicorn src.api:app --host 127.0.0.1 --port 8010 *>> $LOG
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content $LOG "[$stamp] uvicorn exited (code $LASTEXITCODE); restarting in 15s"
    if ((Get-Item $LOG).Length -gt 2MB) {
        $tail = Get-Content $LOG -Tail 2000
        Set-Content $LOG $tail
    }
    Start-Sleep -Seconds 15
}
