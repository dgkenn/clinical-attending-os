# Copies the GitHub public key to the clipboard and opens the "New SSH key"
# page. Paste (Ctrl+V) into the Key box, name it anything, click Add.
#
# Why this isn't fully automated: adding an SSH key is an authenticated WRITE
# to the GitHub account, and the only credential on this machine is the
# read-scoped token that caused the push failure in the first place.
$pub = "$env:USERPROFILE\.ssh\id_ed25519_github.pub"
if (-not (Test-Path $pub)) { throw "Public key not found at $pub" }
Get-Content $pub -Raw | Set-Clipboard
Write-Host "Public key copied to clipboard:" -ForegroundColor Green
Get-Content $pub
Write-Host "`nOpening github.com/settings/ssh/new — paste into 'Key', add a title, click 'Add SSH key'." -ForegroundColor Cyan
Start-Process "https://github.com/settings/ssh/new"
