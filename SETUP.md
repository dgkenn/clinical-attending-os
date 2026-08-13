# Setup — One-time, then zero-touch daily

Goal: log into Windows → open Custom GPT → voice mode → "start a lesson". No terminals.

## Prerequisites (one-time, ~10 min)

```powershell
cd C:\Users\Dean\anesthesia_attending

# Python venv + deps
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Cloudflare tunnel CLI (free; no signup needed for the trycloudflare.com path,
# but a free Cloudflare account gives you a stable hostname).
winget install --id Cloudflare.cloudflared
```

Then make sure `.env` has an `API_KEY`. If it doesn't:

```powershell
$key = [guid]::NewGuid().ToString('N')
Add-Content -Path .env -Value "API_KEY=$key"
Write-Output "Your API key (paste into Custom GPT auth): $key"
```

## Build the corpus (one-time after PDFs change, ~30 min total)

```powershell
python -m src.ingest --force                  # ~25 min — extracts + embeds all books
python -m src.dedupe_facts --no-near-dedupe   # 5 sec   — drops boilerplate, exact dupes
python -m src.cloze                           # 30 sec  — 27k+ cloze cards
python -m src.curriculum                      # 5 sec   — 2,500+ lesson units
python -m src.lesson_cache --progress 500     # ~1 sec  — pre-computes /next_lesson responses
python -m src.migrate_fsrs                    # 1 sec   — seeds FSRS state
```

Sanity check — should be MRR@5 ≥ 0.80, recall@10 ≥ 0.97:

```powershell
python -m src.eval_runner --no-cross-encoder
```

## Cloudflared setup (one-time, ~3 min) — gives you a stable URL

```powershell
cloudflared login                       # opens browser; pick any cf account (free signup ok)
cloudflared tunnel create attending     # prints UUID + path to a credentials.json
```

Note the UUID and the credentials file path it printed.

Create `C:\Users\Dean\.cloudflared\config.yml`:

```yaml
tunnel: attending
credentials-file: C:\Users\Dean\.cloudflared\<UUID>.json
ingress:
  - service: http://localhost:8000
```

Print your stable URL:

```powershell
cloudflared tunnel info attending
```

You'll see a `<UUID>.cfargotunnel.com` hostname. Save it. Use it in `openapi.json`'s `servers[0].url` and in the Custom GPT Action config — **forever**.

## Auto-start at login (one-time)

```powershell
.\setup_autostart.ps1
```

This pre-flight checks the previous steps, then registers a Task Scheduler job that runs at every user logon. After this, every Windows login silently starts uvicorn + cloudflared.

## Custom GPT (one-time)

1. ChatGPT → My GPTs → Create → Configure tab.
2. Paste contents of `CUSTOM_GPT_INSTRUCTIONS.md` into Instructions.
3. Actions → Create new action:
   - Auth: API Key, Custom, header name `X-API-Key`, value = the key from `.env`.
   - Schema: paste contents of `openapi.json` (after replacing `YOUR-TUNNEL-URL-HERE` with your `<UUID>.cfargotunnel.com`).
   - Privacy policy: any URL works (`https://example.com/privacy`).
4. Save.

## Daily flow

1. Wake laptop.
2. Open ChatGPT → your Custom GPT → voice mode → "start a lesson".

That's it.

## Diagnostics

```powershell
# Health
curl https://<UUID>.cfargotunnel.com/health

# Logs
Get-Content storage\logs\uvicorn.err.log -Tail 30
Get-Content storage\logs\cloudflared.err.log -Tail 30

# Manually start / stop
Start-ScheduledTask -TaskName AnesthesiaAttending
Stop-ScheduledTask  -TaskName AnesthesiaAttending
Get-Process python,cloudflared | Stop-Process    # nuclear option

# Disable auto-start
Disable-ScheduledTask -TaskName AnesthesiaAttending
```

## Re-build after adding new PDFs

```powershell
# Full rebuild
python -m src.ingest --force
python -m src.dedupe_facts --no-near-dedupe
python -m src.cloze
python -m src.curriculum
python -m src.lesson_cache --progress 500
# Restart the running uvicorn so it loads the new caches:
Stop-ScheduledTask -TaskName AnesthesiaAttending
Start-ScheduledTask -TaskName AnesthesiaAttending
```

## Rollback if something breaks

```powershell
# Disable auto-start
Disable-ScheduledTask -TaskName AnesthesiaAttending

# Restore pre-dedupe corpus
Copy-Item storage\chroma\chunks.jsonl.predupe.bak storage\chroma\chunks.jsonl -Force
python -m src.curriculum
python -m src.lesson_cache --progress 500
Enable-ScheduledTask  -TaskName AnesthesiaAttending
Start-ScheduledTask   -TaskName AnesthesiaAttending
```
