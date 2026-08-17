# Keeps the MCP server (streamable-http) alive on 127.0.0.1:8011.
#
# This is what makes Claude usable FROM A PHONE: Claude Desktop's MCP is a
# local stdio process, so a phone can never reach it. Served over HTTP behind
# the Tailscale Funnel (https://<host>/mcp), claude.ai can add it as a custom
# connector and get all 33 tools from any device — no desktop app involved.
#
# Bearer auth (MCP_AUTH_TOKEN in .env) is the access gate; build_http_app()
# disables MCP's DNS-rebinding host check because the Funnel rewrites Host.
#
# Restart-on-exit loop, same rationale as run_api_server.ps1.

$ROOT = Split-Path $PSScriptRoot -Parent
$PY = Join-Path $ROOT ".venv\Scripts\python.exe"
$LOG = Join-Path $ROOT "storage\logs\mcp_server.log"

New-Item -ItemType Directory -Force (Split-Path $LOG) | Out-Null

# Load MCP_AUTH_TOKEN from .env (not stored in the task definition).
$envFile = Join-Path $ROOT ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.*)$') {
            [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2].Trim(), 'Process')
        }
    }
}
$env:MCP_TRANSPORT = "streamable-http"
$env:MCP_HOST = "127.0.0.1"
$env:MCP_PORT = "8011"

while ($true) {
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content $LOG "[$stamp] starting MCP http server"
    & $PY -m src.mcp_server *>> $LOG
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content $LOG "[$stamp] MCP server exited (code $LASTEXITCODE); restarting in 15s"
    if ((Get-Item $LOG).Length -gt 2MB) {
        Set-Content $LOG (Get-Content $LOG -Tail 2000)
    }
    Start-Sleep -Seconds 15
}
