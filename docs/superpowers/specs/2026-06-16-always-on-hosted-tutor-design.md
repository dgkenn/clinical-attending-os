# Design Spec: Always-On Clinical Attending OS

**Date:** 2026-06-16
**Status:** Approved (design); ready for implementation planning
**Author:** Dean Kennedy + Claude

---

## Goal

Re-architect the Clinical Attending OS so it is **always-on and hosted**, removing
the dependency on the user's laptop, the local `python -m src.mcp_server` process,
and the external D: drive. The user interacts through **Claude** (desktop + mobile)
via a **remote MCP connector** — same 15 tools, same tutor behavior.

Hard constraints (user priorities, in order): **free**, **minimal effort for the
user**, **maximize retrieval/learning performance**, **truly always-on** (no cold
starts).

## Non-goals (SP1)

- No new front-end UI (Claude is the client).
- No change to the tutoring logic, tools, FSRS/mastery, or the curated knowledge.
- No re-embedding of the index (the Chroma collection is copied as-is).
- The self-driving daily-nudge layer is **SP2**, designed separately after SP1 ships.

## Decomposition

- **SP1 (this spec):** Hosted always-on backend + Claude remote connector. Delivers
  "always-on, no laptop, no D:, works from phone."
- **SP2 (later):** Self-driving daily layer — scheduled due-review computation +
  one-tap "study now" nudge + weekly progress digest. Depends on SP1 being live.

---

## SP1 Architecture

### Topology
- **Host:** Oracle Cloud **Always-Free** ARM VM (Ampere A1, target 4 OCPU / 24 GB /
  ~100–200 GB block volume), Ubuntu 22.04 LTS, running 24/7. Cost: $0.
- **App:** the existing `src/mcp_server.py` FastMCP server, run with
  `transport="streamable-http"` (a one-line change; the installed `mcp` package
  supports it). Runs as a **systemd service** (`Restart=always`, `WantedBy=
  multi-user.target`) so it survives reboots and crashes with no manual start.
- **TLS / ingress:** **Caddy** reverse proxy terminates HTTPS with automatic
  Let's Encrypt certs on a free **DuckDNS** hostname (Claude connectors require
  valid public TLS). Caddy proxies `https://<host>.duckdns.org/mcp` → local
  FastMCP port (e.g. 127.0.0.1:8000).
- **Vector store:** the Chroma index (collection
  `anesthesia_sources_local_baai_bge_small_en_v1_5`, 65,573 docs incl. the 946
  curated units) is **copied once** from D: to the VM block volume. No re-embed —
  the collection is portable.
- **Models:** `BAAI/bge-small-en-v1.5` (embeddings) + `BAAI/bge-reranker-base`
  (rerank) load on the ARM CPU via PyTorch ARM wheels. 24 GB RAM fits both for
  full retrieval quality.
- **Student state:** SQLite `storage/sqlite/student_model.db` on the VM volume
  (persistent, survives reboots).

### Client connection
The user adds a **custom remote connector** in Claude (Settings → Connectors)
pointing at `https://<host>.duckdns.org/mcp` with an `Authorization: Bearer <token>`
header. Available on desktop + mobile.

### Components (clean boundaries)
1. **`mcp_http_server`** — `src/mcp_server.py` extended to:
   - select transport via env (`MCP_TRANSPORT=streamable-http`, default `stdio` so
     local use is unchanged);
   - wrap the HTTP app in **bearer-token auth middleware** (reject requests
     lacking the shared secret with 401). The endpoint serves copyrighted textbook
     content + the user's data and MUST NOT be open.
   - expose a `/health` route (no auth) for monitoring.
2. **`deploy/`** — reproducible, idempotent provisioning:
   - `cloud-init` / setup script: install Python, system deps, clone repo, create
     venv, install `requirements.txt`;
   - `clinical-attending.service` systemd unit;
   - `Caddyfile`;
   - DuckDNS updater (cron) to keep the hostname pointed at the VM IP.
3. **`migration`** — one-time: copy `storage/chroma/` + `storage/sqlite/` +
   `data/curated_keep.json` to the VM; verify counts.

### Data flow
```
Claude (desktop/mobile)
  → HTTPS  https://<host>.duckdns.org/mcp   (Bearer token)
  → Caddy (TLS, reverse proxy)
  → FastMCP /mcp  (auth middleware)
  → tool → retrieval (Chroma on disk + bge-small/reranker) / student_model (SQLite)
  → response
```

### Security
- **Bearer token** on all tool traffic; token stored in VM env (`MCP_AUTH_TOKEN`),
  never committed. Rotatable.
- Only ports 80/443 open in the Oracle security list (+ 22 restricted to the
  user's IP for admin). FastMCP binds to 127.0.0.1 (only Caddy reaches it).
- DuckDNS hostname is unguessable-ish; token is the real gate. Optional: restrict
  by source IP later.

### Config / env additions (`.env` on the VM)
- `MCP_TRANSPORT=streamable-http`
- `MCP_HOST=127.0.0.1`, `MCP_PORT=8000`
- `MCP_AUTH_TOKEN=<random 32+ char secret>`
- Existing: `FREE_LOCAL_MODE=true`, `EMBEDDING_PROVIDER=local`, `CHROMA_DIR`,
  `SQLITE_DB_PATH` (point at VM paths).

---

## Deployment sequence (one-time)
1. User creates an Oracle Cloud Free account; a dispatched agent (or the user with
   the agent's guidance) provisions the A1 VM (auto-retry on "out of capacity").
2. User creates a free DuckDNS subdomain + token; points it at the VM public IP.
3. Agent runs `deploy/setup.sh`: clone repo, venv, deps, Caddy, systemd, DuckDNS
   cron.
4. Agent copies the Chroma + SQLite + curated data to the VM (migration).
5. Agent generates `MCP_AUTH_TOKEN`, starts the service, verifies `/health` + a
   tool call locally.
6. User adds the connector (URL + token) in Claude; runs the smoke test.

After cutover, the laptop and D: drive are no longer needed for the tutor.

## Acceptance criteria
- `systemctl status clinical-attending` = active (running); survives a `reboot`.
- `curl https://<host>.duckdns.org/health` = 200; `/mcp` without token = 401.
- On the VM: `python -m src.eval_runner` → **recall@10 = 0.962** (parity with local,
  proving the index copied intact and models run on ARM).
- From Claude **mobile**: "start a study session" triggers a real tool call and a
  grounded lesson.

## Risks & fallbacks
- **Oracle A1 capacity** ("out of capacity" on create) → deploy script auto-retries
  across availability domains; if it never lands, the SAME code + Caddy config
  deploys to a **free private Hugging Face Space** (sleeps when idle; ~30–60 s cold
  start) with no code changes. This is the documented fallback.
- **ARM wheel issues** (torch/sentence-transformers/chromadb) → all have ARM64
  wheels for py3.12; pin versions; verified by the eval parity check.
- **Claude plan** — remote connectors require a paid Claude plan (Pro/Max).
  Prerequisite to confirm before cutover (user is a heavy Claude user → expected
  fine).

## Effort split
- **Agent (automated):** transport change + auth middleware, deploy scripts,
  systemd/Caddy, migration, parity tests.
- **User (manual, ~15 min once):** Oracle signup + VM create click-through, DuckDNS
  subdomain, add the connector in Claude.

---

## SP2 outline (to brainstorm after SP1)
A systemd timer / cron on the VM computes due reviews (`get_due_reviews`) + weak
topics each morning and sends a **one-tap "study now"** nudge plus a weekly
progress digest. **Open decision:** notification channel (free email/SMTP vs phone
push vs a Claude scheduled task). Out of scope for SP1.
