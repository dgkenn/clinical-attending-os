<#
    Clinical Attending OS - one-shot setup for a new Windows machine.

    Run from the repo root:   .\setup_new_machine.ps1

    Idempotent and resumable: every step checks whether its work is already done
    and skips if so. Safe to re-run after a failure or a Ctrl-C.

    The only thing it needs from you is a Hugging Face token (read access is
    enough) to pull the private index. Set $env:HF_TOKEN first to skip the prompt.
#>

$ErrorActionPreference = "Stop"
$ROOT = $PSScriptRoot
Set-Location $ROOT

$INDEX_DATASET = "deankennedy/clinical-attending-index"
$STATE_DATASET = "deankennedy/clinical-attending-state"
$GDRIVE_LATEST  = "gdrive:tutor_backups/student_model_latest.db"

function Step($n, $msg) { Write-Host "`n[$n] $msg" -ForegroundColor Cyan }
function Ok($msg)       { Write-Host "      OK: $msg" -ForegroundColor Green }
function Skip($msg)     { Write-Host "      skip: $msg" -ForegroundColor DarkGray }
function Warn($msg)     { Write-Host "      WARN: $msg" -ForegroundColor Yellow }

# ---------------------------------------------------------------- 1. Python
Step 1 "Checking Python"
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { throw "Python not found on PATH. Install 3.10+ and re-run." }
$ver = (& python --version) -replace '[^\d.]', ''
$parts = $ver.Split('.')
if ([int]$parts[0] -lt 3 -or ([int]$parts[0] -eq 3 -and [int]$parts[1] -lt 10)) {
    throw "Python $ver is too old. Need 3.10+."
}
Ok "Python $ver"

$free = (Get-PSDrive -Name ($ROOT.Substring(0,1))).Free / 1GB
if ($free -lt 8) { Warn ("Only {0:N1} GB free. Need ~8 GB (2.5 GB index + ~3 GB deps + models)." -f $free) }
else { Ok ("{0:N1} GB free" -f $free) }

# ---------------------------------------------------------------- 2. venv
Step 2 "Creating virtual environment"
$VPY = Join-Path $ROOT ".venv\Scripts\python.exe"
if (Test-Path $VPY) { Skip ".venv already exists" }
else { & python -m venv .venv; Ok ".venv created" }

# ---------------------------------------------------------------- 3. deps
Step 3 "Installing dependencies (~3 GB, ~10 min on first run)"
$marker = Join-Path $ROOT ".venv\.deps_installed"
if (Test-Path $marker) { Skip "dependencies already installed" }
else {
    & $VPY -m pip install --upgrade pip --quiet
    & $VPY -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) { throw "pip install failed" }
    New-Item -ItemType File $marker -Force | Out-Null
    Ok "dependencies installed"
}

# ---------------------------------------------------------------- 4. .env
Step 4 "Writing .env"
if (Test-Path ".env") { Skip ".env already present (leaving it alone)" }
else {
    $apiKey = -join ((1..32) | ForEach-Object { '{0:x}' -f (Get-Random -Max 16) })
    $dataDir = (Join-Path $ROOT "data")
    @"
OPENAI_API_KEY=
OPENAI_CHAT_MODEL=gpt-4.1
OPENAI_EMBEDDING_MODEL=text-embedding-3-large
BACKEND_MODE=retrieval_only
FREE_LOCAL_MODE=true
EMBEDDING_PROVIDER=local
LOCAL_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
LOCAL_RERANKER_MODEL=BAAI/bge-reranker-base
ENABLE_LOCAL_RERANKER=true
API_GENERATION_ENABLED=false
ENABLE_OPENAI_GENERATION=false
LOCAL_MODELS_OFFLINE=false
DEFAULT_TRAINING_PHASE=intern_year
ANESTHESIA_CROSSOVER_PERCENT=0.10
DATA_DIR=$dataDir
SOURCE_FILES=
CHROMA_DIR=storage/chroma
SQLITE_DB_PATH=storage/sqlite/student_model.db
LOG_DIR=storage/logs
API_KEY=$apiKey
"@ | Out-File -FilePath ".env" -Encoding utf8
    Ok ".env written with a fresh API_KEY and paths pointed at this machine"
    Write-Host "      note: SOURCE_FILES is blank - only needed to rebuild the index from PDFs" -ForegroundColor DarkGray
}

# ---------------------------------------------------------------- 5. HF token
Step 5 "Hugging Face token (needed to download the private index)"
$tokenFile = Join-Path $ROOT "deploy\hf\.hf_token"
if (Test-Path $tokenFile) { Skip "deploy/hf/.hf_token already present" }
elseif ($env:HF_TOKEN) {
    New-Item -ItemType Directory (Split-Path $tokenFile) -Force | Out-Null
    $env:HF_TOKEN | Out-File -FilePath $tokenFile -Encoding ascii -NoNewline
    Ok "token taken from `$env:HF_TOKEN"
}
else {
    Write-Host "      Paste your HF token (https://huggingface.co/settings/tokens):" -ForegroundColor Yellow
    $sec = Read-Host -AsSecureString "      HF token"
    $plain = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($sec))
    if (-not $plain) { throw "No token given. Re-run with `$env:HF_TOKEN set, or paste when prompted." }
    New-Item -ItemType Directory (Split-Path $tokenFile) -Force | Out-Null
    $plain | Out-File -FilePath $tokenFile -Encoding ascii -NoNewline
    Ok "token saved to deploy/hf/.hf_token (gitignored)"
}

# ---------------------------------------------------------------- 6. index
Step 6 "Downloading the vector index (2.48 GB) - this is the slow one"
$chromaDb = Join-Path $ROOT "storage\chroma\chroma.sqlite3"
$needIndex = $true
if (Test-Path $chromaDb) {
    $sz = (Get-Item $chromaDb).Length / 1GB
    if ($sz -gt 1.5) { Skip ("index already present ({0:N2} GB)" -f $sz); $needIndex = $false }
    else { Warn ("chroma.sqlite3 is only {0:N2} GB - incomplete, re-downloading" -f $sz) }
}
if ($needIndex) {
    $dl = @"
import pathlib
from huggingface_hub import snapshot_download
tok = pathlib.Path(r'$tokenFile').read_text().strip()
snapshot_download(repo_id='$INDEX_DATASET', repo_type='dataset',
                  local_dir=r'$(Join-Path $ROOT "storage\chroma")', token=tok)
print('index download complete')
"@
    $dl | Out-File -FilePath "$env:TEMP\_ca_dl.py" -Encoding utf8
    & $VPY "$env:TEMP\_ca_dl.py"
    if ($LASTEXITCODE -ne 0) { throw "Index download failed. Check the HF token has read access to $INDEX_DATASET." }
    $sz = (Get-Item $chromaDb).Length / 1GB
    if ($sz -lt 1.5) { throw ("Download finished but chroma.sqlite3 is only {0:N2} GB - expected ~1.64 GB." -f $sz) }
    Ok ("index downloaded ({0:N2} GB)" -f $sz)
}

# ---------------------------------------------------------------- 7. progress
Step 7 "Restoring learning progress (student_model.db)"
$dbPath = Join-Path $ROOT "storage\sqlite\student_model.db"
if (Test-Path $dbPath) { Skip "student_model.db already present - NOT overwriting" }
else {
    New-Item -ItemType Directory (Split-Path $dbPath) -Force | Out-Null
    $rclone = Get-Command rclone -ErrorAction SilentlyContinue
    $restored = $false
    if ($rclone) {
        Write-Host "      trying Google Drive (newest copy)..." -ForegroundColor DarkGray
        & rclone copyto $GDRIVE_LATEST $dbPath
        if ($LASTEXITCODE -eq 0 -and (Test-Path $dbPath)) {
            Ok "restored from Google Drive (newest available)"; $restored = $true
        } else { Warn "rclone restore failed, falling back to Hugging Face" }
    } else { Write-Host "      rclone not installed - using Hugging Face copy" -ForegroundColor DarkGray }

    if (-not $restored) {
        $rs = @"
import pathlib, shutil
from huggingface_hub import hf_hub_download
tok = pathlib.Path(r'$tokenFile').read_text().strip()
p = hf_hub_download(repo_id='$STATE_DATASET', repo_type='dataset',
                    filename='student_model.db', token=tok)
shutil.copy(p, r'$dbPath')
print('student DB restored from HF')
"@
        $rs | Out-File -FilePath "$env:TEMP\_ca_state.py" -Encoding utf8
        & $VPY "$env:TEMP\_ca_state.py"
        if ($LASTEXITCODE -ne 0) { Warn "Could not restore progress. System will start with a blank student model." }
        else { Ok "restored from Hugging Face (older than the Drive copy - see TRANSFER_TO_NEW_MACHINE.md)" }
    }
}

# ---------------------------------------------------------------- 8. caches
Step 8 "Rebuilding derived caches (lesson_cache is ~25 min)"
$cache = Join-Path $ROOT "storage\curriculum\lesson_cache.json"
if (Test-Path $cache) { Skip "lesson_cache.json already built" }
else {
    & $VPY -m src.dedupe_facts --no-near-dedupe
    & $VPY -m src.cloze
    & $VPY -m src.curriculum
    & $VPY -m src.lesson_cache --progress 200
    & $VPY -m src.migrate_fsrs
    Ok "caches rebuilt"
}

# ---------------------------------------------------------------- 9. verify
Step 9 "Verifying"
& $VPY -m pytest -q
$testsOk = ($LASTEXITCODE -eq 0)
if ($testsOk) { Ok "tests passed (expect 280)" } else { Warn "tests FAILED - see output above" }

Write-Host "      running retrieval eval (~1 min)..." -ForegroundColor DarkGray
& $VPY -m src.eval_runner --no-cross-encoder
Write-Host "      expected: recall@10 ~0.96, MRR@5 ~0.83, nDCG@5 ~0.75" -ForegroundColor DarkGray
Write-Host "      materially lower => index download was incomplete" -ForegroundColor DarkGray

# ---------------------------------------------------------------- 10. MCP
Step 10 "Claude Desktop config"
$cfgPath = Join-Path $env:APPDATA "Claude\claude_desktop_config.json"
$snippet = @"
{
  "mcpServers": {
    "clinical-attending": {
      "command": "$($VPY -replace '\\','\\\\')",
      "args": ["-m", "src.mcp_server"],
      "cwd": "$($ROOT -replace '\\','\\\\')"
    }
  }
}
"@
Write-Host "`nAdd this to $cfgPath then restart Claude Desktop:`n" -ForegroundColor Yellow
Write-Host $snippet

Write-Host "`nSetup complete." -ForegroundColor Green
Write-Host "Local API instead of MCP:  .\.venv\Scripts\Activate.ps1  then  uvicorn src.api:app --port 8000"
Write-Host "Hosted tutor (no local install needed): https://deankennedy-clinical-attending-os.hf.space/mcp"
