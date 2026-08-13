# Daily auto-launch: starts uvicorn on loopback. Tailscale Funnel is already
# running as a Windows service and forwards https://deanslaptop.tail712dd4.ts.net
# to localhost:8000.
#
# Registered as a Task-Scheduler at-logon task by setup_autostart.ps1.

$ErrorActionPreference = "Stop"
$ProjectRoot = "C:\Users\Dean\anesthesia_attending"

Set-Location $ProjectRoot

# Ensure log dir exists
$LogDir = Join-Path $ProjectRoot "storage\logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null

# Resolve python: venv first, then system
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $VenvPython)) {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd) {
        $VenvPython = $cmd.Source
    } else {
        $VenvPython = "C:\Users\Dean\AppData\Local\Programs\Python\Python312\python.exe"
    }
}

# Kill any existing uvicorn on port 8000 to avoid double-binding
Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue |
    ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }

Start-Process -WindowStyle Hidden -FilePath $VenvPython `
    -ArgumentList "-u", "-m", "uvicorn", "src.api:app", "--host", "127.0.0.1", "--port", "8000", "--log-level", "info" `
    -WorkingDirectory $ProjectRoot `
    -RedirectStandardOutput (Join-Path $LogDir "uvicorn.out.log") `
    -RedirectStandardError  (Join-Path $LogDir "uvicorn.err.log")

Write-Output "anesthesia_attending: uvicorn launched on 127.0.0.1:8000"
Write-Output "Public URL (via Tailscale Funnel): https://deanslaptop.tail712dd4.ts.net"
