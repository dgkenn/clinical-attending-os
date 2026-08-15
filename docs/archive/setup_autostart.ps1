# One-time installer for the at-logon auto-start.
# Run ONCE in PowerShell (no admin needed — user-scope task).
#
#   cd C:\Users\Dean\anesthesia_attending
#   .\setup_autostart.ps1
#
# After this, every Windows login silently starts uvicorn.
# Tailscale Funnel runs as a system service and brokers the public URL.

$ErrorActionPreference = "Stop"
$ProjectRoot = "C:\Users\Dean\anesthesia_attending"
$ScriptPath  = Join-Path $ProjectRoot "start_attending.ps1"
$TaskName    = "AnesthesiaAttending"

if (-not (Test-Path $ScriptPath)) {
    Write-Error "start_attending.ps1 not found at $ScriptPath"
    exit 1
}

Write-Output "=== Pre-flight checks ==="

# 1. Tailscale installed + logged in?
$ts = "C:\Program Files\Tailscale\tailscale.exe"
if (-not (Test-Path $ts)) {
    Write-Warning "Tailscale not installed. Run: winget install --id tailscale.tailscale"
    exit 1
}
$tsStatus = & $ts status 2>&1 | Out-String
if ($tsStatus -match "Logged out") {
    Write-Warning "Tailscale not logged in. Run: & '$ts' up"
    exit 1
}
Write-Output "Tailscale: logged in"

# 2. Funnel enabled?
$funnel = & $ts funnel status 2>&1 | Out-String
if ($funnel -notmatch "Funnel on") {
    Write-Warning "Tailscale Funnel not configured. Run: & '$ts' funnel --bg http://localhost:8000"
    exit 1
}
$funnelUrl = ($funnel -split "`n" | Select-String "https://" | Select-Object -First 1).ToString().Trim() -replace '^#\s*-\s*',''
Write-Output "Tailscale Funnel: $funnelUrl"

# 3. Python (venv preferred, system fallback)
$Venv = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (Test-Path $Venv) {
    Write-Output "Python (venv): $Venv"
} else {
    $sys = Get-Command python -ErrorAction SilentlyContinue
    if (-not $sys) {
        Write-Warning "No Python found. Install Python 3.11+ and re-run."
        exit 1
    }
    $pyTest = & $sys.Source -c "import fastapi, uvicorn, chromadb, sentence_transformers; print('ok')"
    if ($pyTest -notmatch "ok") {
        Write-Warning "System Python missing dependencies. Run: pip install -r requirements.txt"
        exit 1
    }
    Write-Output "Python (system): $($sys.Source)"
}

# 4. API_KEY set in .env?
$envFile = Join-Path $ProjectRoot ".env"
if (-not (Test-Path $envFile)) {
    Write-Warning ".env not found"
    exit 1
}
$envContent = Get-Content $envFile -Raw
if ($envContent -notmatch "(?m)^API_KEY=\S+") {
    Write-Warning "API_KEY missing or empty in .env"
    exit 1
}
Write-Output "API_KEY: present"

# 5. Lesson cache built?
$lessonCache = Join-Path $ProjectRoot "storage\curriculum\lesson_cache.json"
if (-not (Test-Path $lessonCache)) {
    Write-Warning "Lesson cache missing - /next_lesson will fall back to live retrieval."
    Write-Output  "Build with: python -m src.lesson_cache --progress 500"
}

Write-Output ""
Write-Output "=== Registering Task Scheduler entry: $TaskName ==="

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`""

$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -RestartCount 5 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -ExecutionTimeLimit ([TimeSpan]::Zero)

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal | Out-Null

Write-Output "Registered task '$TaskName' to run at user logon."
Write-Output ""
Write-Output "=== Smoke test (start now without rebooting) ==="

Start-ScheduledTask -TaskName $TaskName
Start-Sleep -Seconds 12

try {
    $h = Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -TimeoutSec 5
    if ($h.ok) {
        Write-Output "Local /health: OK ($($h.service))"
    } else {
        Write-Warning "Local responded but /health.ok was false"
    }
} catch {
    Write-Warning "Local 8000 not yet responding - check $ProjectRoot\storage\logs\uvicorn.err.log"
}

# Public URL via Funnel
try {
    $h2 = Invoke-RestMethod -Uri "$funnelUrl/health" -TimeoutSec 15
    if ($h2.ok) {
        Write-Output "Public  /health: OK via $funnelUrl"
    } else {
        Write-Warning "Public responded but /health.ok was false"
    }
} catch {
    Write-Warning "Public URL ($funnelUrl) not reachable yet - try again in ~30s"
}

Write-Output ""
Write-Output "=== Done ==="
Write-Output "Stable URL: $funnelUrl"
Write-Output "Daily flow: ChatGPT -> your Custom GPT -> voice mode -> 'start a lesson'"
Write-Output ""
Write-Output "Stop:    Stop-ScheduledTask -TaskName $TaskName  (then Get-Process python | Stop-Process)"
Write-Output "Logs:    Get-Content $ProjectRoot\storage\logs\uvicorn.err.log -Tail 30"
Write-Output "Disable: Disable-ScheduledTask -TaskName $TaskName"
