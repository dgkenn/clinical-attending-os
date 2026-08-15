# Archived old-machine scripts (2026-08-15)

`setup_claude_desktop_mcp.ps1`, `start_attending.ps1`, `setup_autostart.ps1`
are hardcoded to the OLD laptop (`C:\Users\Dean\anesthesia_attending`, a D:
drive precondition, `deanslaptop` Tailscale hostname, port 8000) and fail on
line 1-20 anywhere else. Superseded by:

- Claude Desktop MCP config: `%APPDATA%\Claude\claude_desktop_config.json`
  (see TRANSFER_TO_NEW_MACHINE.md Step 8)
- API autostart: `deploy/run_api_server.ps1` behind the
  `ClinicalAttendingOS-API` scheduled task (at logon, restart-on-exit)
- Weekly backup: `deploy/backup_to_gdrive.py` behind the
  `ClinicalAttendingOS-WeeklyBackup` scheduled task
