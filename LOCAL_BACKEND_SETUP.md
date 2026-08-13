# Local Backend Setup

Clinical Attending OS can run locally with no paid backend API calls. ChatGPT Custom GPT calls your local FastAPI backend through a public HTTPS tunnel.

## Run Backend

```powershell
cd C:\Users\Dean\anesthesia_attending
.\.venv\Scripts\Activate.ps1
uvicorn src.api:app --host 0.0.0.0 --port 8000
```

Keep the laptop awake while using the Custom GPT.

## Option A: cloudflared

```powershell
cloudflared tunnel --url http://localhost:8000
```

Copy the HTTPS URL, replace `https://YOUR-TUNNEL-URL-HERE` in `openapi.json`, and paste the schema into Custom GPT Actions.

## Option B: ngrok

```powershell
ngrok http 8000
```

Copy the HTTPS forwarding URL, replace the server URL in `openapi.json`, and paste the schema into Custom GPT Actions.

## Security

Set `API_KEY` in `.env`. Configure the same key in Custom GPT Action authentication as header:

```text
X-API-Key: your-secret
```

Do not expose the tunnel without an API key. The backend returns compact excerpts only and does not expose full PDFs.

Free tunnel URLs often change. If the URL changes, update the OpenAPI server URL in the Custom GPT.
