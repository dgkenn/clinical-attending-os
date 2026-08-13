# Deploy the Clinical Attending OS tutor to a free Hugging Face Space

Free, no credit card. Public Docker Space (reachable by Claude) + bearer-token
auth gating all access + the copyrighted index in a **private** HF dataset.

## What the user does (only this)
1. Create a free account at https://huggingface.co/join (email only — no card).
2. Create a **write** access token at https://huggingface.co/settings/tokens
   ("New token" → type: Write). Copy it.
3. Hand the token to the assistant. (Revocable anytime from the same page.)
4. At the end, paste the connector URL + bearer token into Claude → Settings →
   Connectors (requires a paid Claude plan).

## What the assistant does (from the dev machine, with the token)
1. `pip install huggingface_hub` (already present via sentence-transformers).
2. Upload the index: create a **private dataset** `<user>/clinical-attending-index`
   and upload `storage/chroma/` (resolving the D: junction). ~1.5 GB.
3. Create a **public** Docker Space `<user>/clinical-attending-os` and push the
   project (with `deploy/hf/Dockerfile` placed at the Space root as `Dockerfile`,
   and a Space `README.md` carrying the HF frontmatter `sdk: docker`, `app_port: 7860`).
4. Set Space secrets (via `huggingface_hub.add_space_secret`):
   - `MCP_AUTH_TOKEN` = a generated 32-byte hex (this is the Claude bearer token)
   - `HF_TOKEN` = the user's read/write token (to pull the private dataset)
   - `INDEX_DATASET` = `<user>/clinical-attending-index`
   - (optional) `STATE_DATASET` = `<user>/clinical-attending-state` to persist progress
5. Wait for the Space to build; verify:
   - `GET https://<user>-clinical-attending-os.hf.space/health` → 200
   - `POST .../mcp` without token → 401
   - one authenticated tool call returns a grounded result
6. Keep it warm (defeat idle-sleep): add the user's Space `/health` URL to a free
   UptimeRobot monitor (5-min interval), **or** commit `deploy/hf/keepwarm.yml` to a
   GitHub repo with repo variable `HF_SPACE_URL` set.

## Connector details handed back to the user
- URL: `https://<user>-clinical-attending-os.hf.space/mcp`
- Header: `Authorization: Bearer <MCP_AUTH_TOKEN>`

## Known limitation
Free Spaces have ephemeral disk: a full rebuild wipes the SQLite student DB. The
`STATE_DATASET` option (start.sh restores it on boot) mitigates this; a periodic
push-back of `student_model.db` is a follow-up enhancement.
