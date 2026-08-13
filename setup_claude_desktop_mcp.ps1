<#
  setup_claude_desktop_mcp.ps1
  Runbook Steps 0 + 1 for "Clinical Attending OS" as a Claude Desktop tutor.

  WHAT IT DOES (safe + idempotent):
    Step 0  Verify preconditions: D: drive, Chroma count (~65,573), mcp+server
            import, pytest, and resolve the absolute Python interpreter path.
    Step 1  Back up claude_desktop_config.json, then merge in an `mcpServers`
            block for `clinical-attending-os` WITHOUT touching existing keys,
            and validate the JSON still parses.

  It does NOT: modify the Chroma store, run git, or touch Claude Desktop's GUI.
  Run from the project root:
      cd C:\Users\Dean\anesthesia_attending
      powershell -ExecutionPolicy Bypass -File .\setup_claude_desktop_mcp.ps1
#>

$ErrorActionPreference = 'Stop'
$proj = 'C:\Users\Dean\anesthesia_attending'
Set-Location $proj
$fail = 0
function Pass($m){ Write-Host "  [PASS] $m" -ForegroundColor Green }
function Fail($m){ Write-Host "  [FAIL] $m" -ForegroundColor Red; $script:fail++ }
function Info($m){ Write-Host "  [INFO] $m" -ForegroundColor Cyan }

Write-Host "`n=== Step 0: Preconditions ===" -ForegroundColor Yellow

# 0.5 Resolve Python first (needed for the import/count checks)
$python = $null
try { $python = (Get-Command python -ErrorAction Stop).Source } catch {}
if (-not $python -or -not (Test-Path $python)) {
    $python = 'C:\Users\Dean\AppData\Local\Programs\Python\Python312\python.exe'
}
if (Test-Path $python) { Pass "Python interpreter: $python" }
else { Fail "Could not resolve a Python interpreter (tried PATH and the expected Python312 path)" }

# 0.1 D: drive
try { Get-Volume -DriveLetter D -ErrorAction Stop | Out-Null; Pass "D: drive is connected" }
catch { Fail "D: drive NOT connected -- plug in the Seagate drive (the Chroma store lives there). STOP until fixed." }

# 0.2 Chroma index resolves + populated (~65,573)
if ($python -and (Test-Path $python)) {
    try {
        $count = & $python -c "from src.config import settings as s; import chromadb; print(chromadb.PersistentClient(path=str(s.chroma_dir)).get_collection(s.vector_collection_name()).count())" 2>&1
        if ($LASTEXITCODE -eq 0 -and ($count -match '^\d+$')) { Pass "Chroma collection count = $count (expect ~65573)" }
        else { Fail "Chroma count check failed: $count" }
    } catch { Fail "Chroma count check errored: $_" }
}

# 0.3 mcp + server import
if ($python -and (Test-Path $python)) {
    $imp = & $python -c "import mcp; import src.mcp_server as m; print('mcp+server OK; main:', hasattr(m,'main'))" 2>&1
    if ($LASTEXITCODE -eq 0) { Pass "Import check: $imp" }
    else { Fail "Import check failed (run: pip install mcp): $imp" }
}

# 0.4 Tests
if ($python -and (Test-Path $python)) {
    Info "Running pytest -q (this can take a minute)..."
    $pt = & $python -m pytest -q 2>&1
    $tail = ($pt | Select-Object -Last 1)
    if ($LASTEXITCODE -eq 0) { Pass "pytest: $tail" }
    else { Fail "pytest non-zero exit. Last line: $tail" }
}

Write-Host "`n=== Step 1: Register MCP server in Claude Desktop config ===" -ForegroundColor Yellow
$cfg = Join-Path $env:APPDATA 'Claude\claude_desktop_config.json'

if (-not (Test-Path $cfg)) {
    Info "No config found at $cfg -- creating a fresh one."
    '{}' | Set-Content -Path $cfg -Encoding UTF8
}

# Backup (timestamped + the canonical .bak the runbook names)
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
Copy-Item $cfg "$cfg.bak" -Force
Copy-Item $cfg "$cfg.$stamp.bak" -Force
Pass "Backed up config -> $cfg.bak (and $cfg.$stamp.bak)"

# Load -> merge -> write (preserve all existing keys, e.g. preferences)
$json = Get-Content $cfg -Raw | ConvertFrom-Json
if (-not $json.PSObject.Properties.Name.Contains('mcpServers')) {
    $json | Add-Member -NotePropertyName 'mcpServers' -NotePropertyValue ([pscustomobject]@{}) -Force
}
$server = [pscustomobject]@{
    command = $python
    args    = @('-m','src.mcp_server')
    cwd     = $proj
}
# add/replace only our server key; leave any other servers untouched
$json.mcpServers | Add-Member -NotePropertyName 'clinical-attending-os' -NotePropertyValue $server -Force

$json | ConvertTo-Json -Depth 12 | Set-Content -Path $cfg -Encoding UTF8

# Validate
try {
    Get-Content $cfg -Raw | ConvertFrom-Json | Out-Null
    Pass "Config JSON is valid and now contains mcpServers.clinical-attending-os"
} catch { Fail "Config JSON failed to parse after edit! Restore with: Copy-Item `"$cfg.bak`" `"$cfg`" -Force" }

Write-Host "`n--- Resulting mcpServers block ---" -ForegroundColor Yellow
($json.mcpServers | ConvertTo-Json -Depth 12)

Write-Host "`n=== Summary ===" -ForegroundColor Yellow
if ($fail -eq 0) {
    Write-Host "All checks passed. Now do the GUI steps:" -ForegroundColor Green
} else {
    Write-Host "$fail check(s) FAILED above -- resolve them before relying on the tutor." -ForegroundColor Red
}
Write-Host "  1) Open Claude Desktop -> create a Project named 'Clinical Attending'."
Write-Host "  2) Paste the contents of CLAUDE_DESKTOP_TUTOR_INSTRUCTIONS.md into the project's custom instructions."
Write-Host "  3) Fully QUIT Claude Desktop (system tray -> Quit) and reopen it, so it loads the new MCP config."
Write-Host "  4) In a new chat in that Project, ask: 'What MCP tools do you have?' -- expect the clinical-attending-os tools."
