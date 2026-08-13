# Always-On Hosted Tutor (SP1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Clinical Attending OS always-on and hosted, so the user studies through Claude (desktop + mobile) via a remote MCP connector — no laptop, no D: drive, no manually-run script.

**Architecture:** The existing `src/mcp_server.py` FastMCP server gains an HTTP transport (`streamable-http`) guarded by bearer-token auth, fronted by Caddy (HTTPS) on an Oracle Always-Free VM, run as a systemd service. The Chroma index is copied off D: onto the VM. Claude connects to `https://<host>/mcp`.

**Tech Stack:** Python 3.12, `mcp`/FastMCP (Starlette + uvicorn), Chroma, sentence-transformers (bge-small + bge-reranker), Oracle Cloud Free ARM (Ubuntu), Caddy, DuckDNS, systemd.

**Two phases:** Phase 1 (Tasks 1–5) is code + deploy artifacts — fully buildable and testable **locally now** (default transport stays `stdio`, so nothing local breaks). Phase 2 (Tasks 6–11) is the **one-time deploy on the VM**, executed once the user has provisioned the Oracle instance.

---

## File Structure

- `src/config.py` — add MCP transport/host/port/token settings (modify).
- `src/mcp_server.py` — split tool registration into a `build_server()` factory; add `build_http_app()` (auth + `/health`); env-driven `main()` (modify).
- `tests/test_mcp_http.py` — tests for transport selection, auth middleware, `/health` (create).
- `deploy/setup.sh` — VM bootstrap (create).
- `deploy/clinical-attending.service` — systemd unit (create).
- `deploy/Caddyfile` — reverse proxy + TLS (create).
- `deploy/duckdns.sh` — dynamic DNS updater (create).
- `deploy/migrate_to_vm.sh` — copy Chroma/SQLite/curated data to the VM (create).
- `deploy/README.md` — the manual one-time steps (create).
- `requirements.txt` — add `uvicorn` (modify).

---

## Phase 1 — Code + artifacts (local, testable now)

### Task 1: Config settings for HTTP transport

**Files:**
- Modify: `src/config.py` (the `Settings` dataclass)
- Test: `tests/test_mcp_http.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_mcp_http.py
import importlib, os

def test_settings_expose_mcp_http_fields(monkeypatch):
    monkeypatch.setenv("MCP_TRANSPORT", "streamable-http")
    monkeypatch.setenv("MCP_HOST", "127.0.0.1")
    monkeypatch.setenv("MCP_PORT", "9001")
    monkeypatch.setenv("MCP_AUTH_TOKEN", "secret123")
    import src.config as cfg
    importlib.reload(cfg)
    s = cfg.Settings()
    assert s.mcp_transport == "streamable-http"
    assert s.mcp_host == "127.0.0.1"
    assert s.mcp_port == 9001
    assert s.mcp_auth_token == "secret123"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_mcp_http.py::test_settings_expose_mcp_http_fields -v`
Expected: FAIL with `AttributeError: 'Settings' object has no attribute 'mcp_transport'`

- [ ] **Step 3: Add the fields to `Settings`**

In `src/config.py`, inside the `Settings` dataclass (next to the other `os.getenv` fields), add:

```python
    mcp_transport: str = os.getenv("MCP_TRANSPORT", "stdio")
    mcp_host: str = os.getenv("MCP_HOST", "127.0.0.1")
    mcp_port: int = int(os.getenv("MCP_PORT", "8000"))
    mcp_auth_token: str = os.getenv("MCP_AUTH_TOKEN", "")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_mcp_http.py::test_settings_expose_mcp_http_fields -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/config.py tests/test_mcp_http.py
git commit -m "feat: add MCP transport/host/port/token settings"
```

---

### Task 2: `build_server()` factory (refactor) + keep stdio behavior

**Files:**
- Modify: `src/mcp_server.py` (extract tool registration from `main()` into `build_server()`)
- Test: `tests/test_mcp_http.py`

- [ ] **Step 1: Write the failing test**

```python
def test_build_server_registers_tools():
    from src.mcp_server import build_server
    mcp = build_server()
    # FastMCP stores tools in its tool manager; at least the core tutor tools exist
    names = set(mcp._tool_manager._tools.keys())  # FastMCP internal registry
    assert {"get_next_topic", "submit_answer", "search_clinical_sources"} <= names
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_mcp_http.py::test_build_server_registers_tools -v`
Expected: FAIL with `ImportError: cannot import name 'build_server'`

- [ ] **Step 3: Refactor `main()` into a factory**

In `src/mcp_server.py`, replace the body of `main()` that creates `FastMCP(...)` and calls `mcp.tool()(...)` with a factory. Move ALL the existing `mcp = FastMCP("clinical-attending-os")` + every `mcp.tool()(...)`/`mcp.tool(name=...)(...)` registration into:

```python
def build_server():
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("clinical-attending-os")
    # Legacy endpoints
    mcp.tool()(search_clinical_sources)
    mcp.tool()(answer_from_clinical_sources)
    mcp.tool()(start_study_session)
    mcp.tool()(submit_study_answer)
    mcp.tool()(get_due_reviews)
    mcp.tool()(get_student_dashboard)
    mcp.tool()(log_missed_topic)
    mcp.tool(name="mark_topic_mastered")(mark_topic_mastered_tool)
    mcp.tool(name="set_default_training_phase")(set_default_training_phase_tool)
    # Phase 1 endpoints
    mcp.tool(name="mcp_retrieval")(mcp_retrieval)
    mcp.tool(name="get_session_state")(get_session_state)
    mcp.tool(name="get_next_topic")(get_next_topic)
    mcp.tool(name="submit_answer")(submit_answer)
    mcp.tool(name="get_mastery_gates")(get_mastery_gates)
    mcp.tool(name="get_progress")(get_progress)
    return mcp
```

Then make `main()` simply:

```python
def main() -> None:
    try:
        import mcp  # noqa: F401  (ensures dependency present)
    except Exception as exc:
        raise SystemExit("Install mcp to run the MCP server: pip install mcp") from exc
    server = build_server()
    server.run()  # stdio (default); HTTP wiring added in Task 4
```

- [ ] **Step 4: Run tests to verify pass + no regression**

Run: `python -m pytest tests/test_mcp_http.py::test_build_server_registers_tools -v && python -c "import src.mcp_server"`
Expected: PASS, and the import prints nothing/no error.

- [ ] **Step 5: Commit**

```bash
git add src/mcp_server.py tests/test_mcp_http.py
git commit -m "refactor: extract build_server() factory from main()"
```

---

### Task 3: Auth-guarded HTTP app (`build_http_app`)

**Files:**
- Modify: `src/mcp_server.py` (add `build_http_app`)
- Test: `tests/test_mcp_http.py`

- [ ] **Step 1: Write the failing test**

```python
def test_http_app_auth_and_health():
    from starlette.testclient import TestClient
    from src.mcp_server import build_server, build_http_app
    app = build_http_app(build_server(), auth_token="secret123")
    client = TestClient(app)
    # health is open
    assert client.get("/health").status_code == 200
    # mcp endpoint rejects missing token
    assert client.post("/mcp").status_code == 401
    # rejects wrong token
    assert client.post("/mcp", headers={"Authorization": "Bearer nope"}).status_code == 401
    # correct token passes the auth gate (not 401; MCP handshake may 400/406, that's fine)
    r = client.post("/mcp", headers={"Authorization": "Bearer secret123"})
    assert r.status_code != 401
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_mcp_http.py::test_http_app_auth_and_health -v`
Expected: FAIL with `ImportError: cannot import name 'build_http_app'`

- [ ] **Step 3: Implement `build_http_app`**

Add to `src/mcp_server.py` (top-level imports + function):

```python
import hmac


def build_http_app(server, auth_token: str):
    """Wrap the FastMCP streamable-http Starlette app with bearer-token auth
    and an unauthenticated /health route."""
    from starlette.responses import JSONResponse, PlainTextResponse
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.routing import Route

    app = server.streamable_http_app()  # Starlette app serving /mcp

    async def health(_request):
        return PlainTextResponse("ok")

    app.router.routes.append(Route("/health", health, methods=["GET"]))

    expected = f"Bearer {auth_token}" if auth_token else ""

    class _AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            if request.url.path == "/health":
                return await call_next(request)
            provided = request.headers.get("authorization", "")
            if not auth_token or not hmac.compare_digest(provided, expected):
                return JSONResponse({"error": "unauthorized"}, status_code=401)
            return await call_next(request)

    app.add_middleware(_AuthMiddleware)
    return app
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_mcp_http.py::test_http_app_auth_and_health -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/mcp_server.py tests/test_mcp_http.py
git commit -m "feat: bearer-token auth + /health for HTTP MCP transport"
```

---

### Task 4: Env-driven `main()` (stdio default, HTTP when configured)

**Files:**
- Modify: `src/mcp_server.py` (`main`)
- Modify: `requirements.txt` (add `uvicorn`)
- Test: `tests/test_mcp_http.py`

- [ ] **Step 1: Write the failing test** (asserts HTTP path builds an app without starting a server)

```python
def test_main_http_mode_builds_app(monkeypatch):
    import src.mcp_server as srv
    captured = {}
    def fake_run(app, host, port):
        captured["host"], captured["port"] = host, port
    monkeypatch.setenv("MCP_TRANSPORT", "streamable-http")
    monkeypatch.setenv("MCP_HOST", "127.0.0.1")
    monkeypatch.setenv("MCP_PORT", "9123")
    monkeypatch.setenv("MCP_AUTH_TOKEN", "secret123")
    monkeypatch.setattr(srv, "_serve_http", lambda app, host, port: fake_run(app, host, port))
    srv.main()
    assert captured == {"host": "127.0.0.1", "port": 9123}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_mcp_http.py::test_main_http_mode_builds_app -v`
Expected: FAIL (`_serve_http` / new `main` branch not present)

- [ ] **Step 3: Implement transport branching in `main()`**

Replace `main()` in `src/mcp_server.py` with:

```python
def _serve_http(app, host, port):  # pragma: no cover - thin uvicorn wrapper
    import uvicorn
    uvicorn.run(app, host=host, port=port)


def main() -> None:
    import os
    try:
        import mcp  # noqa: F401
    except Exception as exc:
        raise SystemExit("Install mcp to run the MCP server: pip install mcp") from exc
    server = build_server()
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "stdio":
        server.run()
        return
    if transport in ("streamable-http", "sse"):
        host = os.getenv("MCP_HOST", "127.0.0.1")
        port = int(os.getenv("MCP_PORT", "8000"))
        token = os.getenv("MCP_AUTH_TOKEN", "")
        if not token:
            raise SystemExit("MCP_AUTH_TOKEN must be set for HTTP transport")
        app = build_http_app(server, token)
        _serve_http(app, host, port)
        return
    raise SystemExit(f"Unknown MCP_TRANSPORT: {transport}")
```

- [ ] **Step 4: Run tests + add uvicorn dep**

Add `uvicorn` to `requirements.txt`. Then:
Run: `python -m pytest tests/test_mcp_http.py -v && python -m pytest -q`
Expected: all of `tests/test_mcp_http.py` PASS; full suite still `281 passed` (280 prior + new file aggregated; 0 failed).

- [ ] **Step 5: Commit**

```bash
git add src/mcp_server.py requirements.txt tests/test_mcp_http.py
git commit -m "feat: env-driven stdio/http transport in mcp_server.main()"
```

---

### Task 5: Deploy artifacts + local HTTP smoke test

**Files:**
- Create: `deploy/setup.sh`, `deploy/clinical-attending.service`, `deploy/Caddyfile`, `deploy/duckdns.sh`, `deploy/migrate_to_vm.sh`, `deploy/README.md`

- [ ] **Step 1: Create `deploy/clinical-attending.service`**

```ini
[Unit]
Description=Clinical Attending OS MCP server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/anesthesia_attending
EnvironmentFile=/home/ubuntu/anesthesia_attending/.env
ExecStart=/home/ubuntu/anesthesia_attending/.venv/bin/python -m src.mcp_server
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

- [ ] **Step 2: Create `deploy/Caddyfile`** (replace `HOSTNAME` at deploy time)

```
HOSTNAME {
    handle /health { reverse_proxy 127.0.0.1:8000 }
    handle /mcp* { reverse_proxy 127.0.0.1:8000 }
    handle { respond "Clinical Attending OS" 200 }
}
```

- [ ] **Step 3: Create `deploy/duckdns.sh`** (replace tokens at deploy time)

```bash
#!/usr/bin/env bash
# Cron: */5 * * * * /home/ubuntu/anesthesia_attending/deploy/duckdns.sh
DOMAIN="${DUCKDNS_DOMAIN:?set DUCKDNS_DOMAIN}"
TOKEN="${DUCKDNS_TOKEN:?set DUCKDNS_TOKEN}"
curl -fsS "https://www.duckdns.org/update?domains=${DOMAIN}&token=${TOKEN}&ip=" >/dev/null
```

- [ ] **Step 4: Create `deploy/setup.sh`** (idempotent VM bootstrap)

```bash
#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update -y
sudo apt-get install -y python3.12 python3.12-venv python3-pip git curl debian-keyring debian-archive-keyring apt-transport-https
# Caddy
if ! command -v caddy >/dev/null; then
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
  sudo apt-get update -y && sudo apt-get install -y caddy
fi
cd "$HOME"
[ -d anesthesia_attending ] || git clone <REPO_URL> anesthesia_attending
cd anesthesia_attending
python3.12 -m venv .venv
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt
echo "setup.sh done"
```

- [ ] **Step 5: Create `deploy/migrate_to_vm.sh`** (run from the LOCAL machine; copies data up)

```bash
#!/usr/bin/env bash
set -euo pipefail
# Usage: VM=ubuntu@<vm-ip> ./deploy/migrate_to_vm.sh
: "${VM:?set VM=ubuntu@<ip>}"
DEST=/home/ubuntu/anesthesia_attending
# Chroma store (resolve the D: junction to the real files), sqlite, curated data
rsync -avz --progress storage/chroma/ "$VM:$DEST/storage/chroma/"
rsync -avz storage/sqlite/student_model.db "$VM:$DEST/storage/sqlite/"
rsync -avz storage/curriculum/units.json "$VM:$DEST/storage/curriculum/"
rsync -avz data/curated_keep.json "$VM:$DEST/data/"
echo "migration copy done"
```

- [ ] **Step 6: Create `deploy/README.md`** documenting the manual one-time steps

Content must include, in order: (1) Oracle Free signup + create an **Ampere A1** Ubuntu 22.04 VM (4 OCPU/24 GB), open ports 80/443 in the security list, SSH 22 to your IP only; if "out of capacity", retry create or try another availability domain. (2) Create a free DuckDNS subdomain + token; set it to the VM public IP. (3) `scp` the repo or `git clone`; run `deploy/setup.sh`. (4) Run `deploy/migrate_to_vm.sh` from the laptop. (5) Write `.env` on the VM with `MCP_TRANSPORT=streamable-http`, `MCP_PORT=8000`, a generated `MCP_AUTH_TOKEN` (`openssl rand -hex 32`), `FREE_LOCAL_MODE=true`, `EMBEDDING_PROVIDER=local`, and VM `CHROMA_DIR`/`SQLITE_DB_PATH`. (6) `sudo cp deploy/clinical-attending.service /etc/systemd/system/ && sudo systemctl enable --now clinical-attending`. (7) Put the Caddyfile at `/etc/caddy/Caddyfile` (replace `HOSTNAME`) and `sudo systemctl reload caddy`. (8) Install the DuckDNS cron. (9) In Claude → Settings → Connectors → add custom connector URL `https://<host>.duckdns.org/mcp` with header `Authorization: Bearer <token>`.

- [ ] **Step 7: Local HTTP smoke test**

Run (PowerShell, local machine):
```
$env:MCP_TRANSPORT="streamable-http"; $env:MCP_PORT="8765"; $env:MCP_AUTH_TOKEN="localtest"
Start-Process -NoNewWindow python "-m","src.mcp_server"
Start-Sleep 8
curl.exe -s -o NUL -w "%{http_code}" http://127.0.0.1:8765/health        # expect 200
curl.exe -s -o NUL -w "%{http_code}" -X POST http://127.0.0.1:8765/mcp    # expect 401
```
Expected: `200` then `401`. Then stop the process.

- [ ] **Step 8: Commit**

```bash
git add deploy/ requirements.txt
git commit -m "feat: deploy artifacts (systemd, Caddy, DuckDNS, migration) + local http smoke test"
```

---

## Phase 2 — One-time deploy on the VM (run once the Oracle VM exists)

> These tasks run against the live VM and require the user's Oracle account. They follow `deploy/README.md`. Each has an explicit verification.

### Task 6: Provision the Oracle Always-Free A1 VM
- [ ] User creates the Oracle Free account and an **Ampere A1** Ubuntu 22.04 instance (4 OCPU / 24 GB / ~100 GB boot volume). Open ingress 80/443 (all sources) and 22 (user IP) in the security list.
- [ ] **Verify:** `ssh ubuntu@<ip> 'nproc && free -g'` → ≥4 cores, ≥20 GB RAM.
- [ ] If "out of capacity": retry create (different availability domain); if persistently unavailable, switch to the HF Spaces fallback in `deploy/README.md`.

### Task 7: DuckDNS hostname
- [ ] Create a DuckDNS subdomain, point it at the VM IP.
- [ ] **Verify:** `nslookup <host>.duckdns.org` resolves to the VM IP.

### Task 8: Bootstrap the VM
- [ ] Copy repo (`git clone` with `<REPO_URL>` or `scp`); run `deploy/setup.sh`.
- [ ] **Verify:** `ssh ubuntu@<ip> 'cd anesthesia_attending && ./.venv/bin/python -c "import src.mcp_server; print(1)"'` → `1`.

### Task 9: Migrate data + parity check
- [ ] From the laptop: `VM=ubuntu@<ip> ./deploy/migrate_to_vm.sh`.
- [ ] On the VM, warm the model cache once (`./.venv/bin/python -c "from src.retrieval import hybrid_search; hybrid_search('sepsis', max_results=3)"`).
- [ ] **Verify (parity):** `ssh ubuntu@<ip> 'cd anesthesia_attending && ./.venv/bin/python -c "from src.config import settings as s; import chromadb; print(chromadb.PersistentClient(path=str(s.chroma_dir)).get_collection(s.vector_collection_name()).count())"'` → `65573`.
- [ ] **Verify (quality):** `ssh ... './.venv/bin/python -m src.eval_runner'` → recall@10 ≈ `0.962`.

### Task 10: Service + TLS + always-on
- [ ] Write `.env` (with `openssl rand -hex 32` token), install + enable the systemd unit, install the Caddyfile (real hostname), install the DuckDNS cron.
- [ ] **Verify:** `systemctl is-active clinical-attending` → `active`; `curl https://<host>.duckdns.org/health` → `200`; `curl -X POST https://<host>.duckdns.org/mcp` → `401`.
- [ ] **Verify (always-on):** `sudo reboot`; after ~60 s, `curl https://<host>.duckdns.org/health` → `200` (proves auto-start).

### Task 11: Connect Claude + end-to-end
- [ ] In Claude (mobile) add the connector (URL + Bearer token).
- [ ] **Verify:** "Start a study session in intern_teach mode" triggers a real tool call and a grounded lesson from the phone, with the laptop **off**.

---

## Self-Review (completed)

- **Spec coverage:** transport change (T1–T4), auth (T3), `/health` (T3), systemd always-on (T5/T10), Caddy/TLS (T5/T10), DuckDNS (T5/T7), Chroma migration off D: (T5/T9), parity recall@10=0.962 (T9), 401 check (T5/T10), reboot survival (T10), Claude connector (T6 spec → T11). Risk/fallback (HF Spaces) referenced in T6. All spec sections map to a task.
- **Placeholders:** intentional deploy-time substitutions are `<REPO_URL>`, `HOSTNAME`/`<host>`, `<ip>`, `<token>` — all explained in `deploy/README.md`. No "TBD/TODO".
- **Type/name consistency:** `build_server()`, `build_http_app(server, auth_token)`, `_serve_http(app, host, port)`, settings `mcp_transport/mcp_host/mcp_port/mcp_auth_token` used consistently across T1–T4.

## Out of scope (SP2, separate plan)
Self-driving daily nudges + weekly digest (cron on the VM). Notification channel decision deferred.
