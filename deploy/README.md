# Clinical Attending OS — VM Deploy Runbook

One-time deploy of the MCP server onto an Oracle Cloud Free Tier Ampere A1 VM behind Caddy + DuckDNS, then connected to Claude as a remote connector.

**Prerequisite:** remote connectors require a **paid Claude plan** (Pro or Team).

---

## 1. Provision the Oracle Cloud VM

1. Sign up at https://cloud.oracle.com (Free Tier, no credit card charged for Always Free resources).
2. Go to **Compute → Instances → Create Instance**.
3. Choose image: **Ubuntu 22.04** (Canonical).
4. Shape: **VM.Standard.A1.Flex** — set **4 OCPU / 24 GB RAM**. Boot volume: **~100 GB**.
5. Add your SSH public key.
6. Under **Networking → Security List**, open ingress:
   - TCP port **80** from source `0.0.0.0/0`
   - TCP port **443** from source `0.0.0.0/0`
   - TCP port **22** from source `<your-laptop-IP>/32` only
7. Click Create. Note the **Public IP** once the instance is RUNNING.

> **"Out of capacity" error?** Retry in a few minutes, or switch to a different Availability Domain (AD-1 → AD-2 → AD-3) in the same region. Oracle releases capacity throughout the day.
>
> **Free fallback:** create a private [Hugging Face Space](https://huggingface.co/spaces) (SDK: Docker, hardware: CPU Free). Use the same `python -m src.mcp_server` entrypoint with `MCP_TRANSPORT=streamable-http`. Note: the Space sleeps after ~15 min of inactivity.

---

## 2. Create a DuckDNS subdomain

1. Go to https://www.duckdns.org and sign in with GitHub/Google.
2. Create a subdomain, e.g. `clinical-attending` → your subdomain is `clinical-attending.duckdns.org`.
3. Note the **token** shown on the DuckDNS dashboard.
4. Point the subdomain at the VM's public IP (enter it in the "current ip" field and click Update IP).

---

## 3. Get the code onto the VM

**Option A — git clone (recommended):**
```bash
# On your laptop: edit deploy/setup.sh and replace <REPO_URL> with your actual repo URL
# Then on the VM:
ssh ubuntu@<vm-ip>
bash -c "$(curl -fsSL https://raw.githubusercontent.com/<user>/<repo>/main/deploy/setup.sh)"
```

**Option B — rsync the whole directory:**
```bash
# From your laptop (from the parent of anesthesia_attending/):
rsync -avz --progress anesthesia_attending/ ubuntu@<vm-ip>:/home/ubuntu/anesthesia_attending/
```

Either way: `deploy/setup.sh` installs Python 3.12, creates `.venv`, installs requirements, and installs Caddy.

---

## 4. Migrate the data

From your laptop, inside the `anesthesia_attending/` directory:

```bash
VM=ubuntu@<vm-ip> ./deploy/migrate_to_vm.sh
```

This rsyncs:
- `storage/chroma/` — the 1.5 GB Chroma vector index
- `storage/sqlite/student_model.db` — spaced-repetition state
- `storage/curriculum/units.json` — curriculum units
- `data/curated_keep.json` — curated knowledge

---

## 5. Write `.env` on the VM

```bash
ssh ubuntu@<vm-ip>
TOKEN=$(openssl rand -hex 32)   # SAVE this value - needed for the Claude connector (step 10)
cat > /home/ubuntu/anesthesia_attending/.env <<EOF
MCP_TRANSPORT=streamable-http
MCP_HOST=127.0.0.1
MCP_PORT=8000
MCP_AUTH_TOKEN=$TOKEN
FREE_LOCAL_MODE=true
EMBEDDING_PROVIDER=local
CHROMA_DIR=/home/ubuntu/anesthesia_attending/storage/chroma
SQLITE_DB_PATH=/home/ubuntu/anesthesia_attending/storage/sqlite/student_model.db
EOF
chmod 600 /home/ubuntu/anesthesia_attending/.env
echo "Saved MCP token: $TOKEN"
```

> `<<EOF` (unquoted) expands `$TOKEN` into the file. Keep the printed token; you need it for the Claude connector in step 10.

---

## 6. Enable the systemd service

```bash
sudo cp /home/ubuntu/anesthesia_attending/deploy/clinical-attending.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now clinical-attending
# Verify:
sudo systemctl status clinical-attending
journalctl -u clinical-attending -n 50 --no-pager
```

---

## 7. Configure Caddy

```bash
# Replace HOSTNAME with your actual DuckDNS hostname:
sudo cp /home/ubuntu/anesthesia_attending/deploy/Caddyfile /etc/caddy/Caddyfile
sudo sed -i 's/HOSTNAME/clinical-attending.duckdns.org/' /etc/caddy/Caddyfile
sudo systemctl reload caddy
# Caddy auto-provisions a Let's Encrypt TLS certificate on first request.
```

---

## 8. Install the DuckDNS cron

```bash
# On the VM:
export DUCKDNS_DOMAIN=clinical-attending
export DUCKDNS_TOKEN=<your-duckdns-token>

# Add to crontab:
(crontab -l 2>/dev/null; echo "*/5 * * * * DUCKDNS_DOMAIN=$DUCKDNS_DOMAIN DUCKDNS_TOKEN=$DUCKDNS_TOKEN /home/ubuntu/anesthesia_attending/deploy/duckdns.sh") | crontab -
```

This refreshes the DNS record every 5 minutes so it follows any VM IP change.

---

## 9. Verify the deployment

```bash
# Health check (should return 200):
curl -v https://clinical-attending.duckdns.org/health

# Unauthenticated MCP call (should return 401):
curl -s -o /dev/null -w "%{http_code}\n" -X POST https://clinical-attending.duckdns.org/mcp

# Run the eval suite on the VM (recall@10 should be ≈ 0.962):
cd /home/ubuntu/anesthesia_attending
.venv/bin/python -m src.eval_runner

# Reboot test:
sudo reboot
# Wait ~60 seconds, then:
curl https://clinical-attending.duckdns.org/health
# Should return 200 — confirming the systemd unit auto-starts.
```

---

## 10. Add the remote connector in Claude

1. Open Claude → **Settings → Connectors** (or **Claude.ai → Settings → Integrations**).
2. Click **Add custom connector** (requires a paid Claude plan).
3. Set:
   - **URL:** `https://clinical-attending.duckdns.org/mcp`
   - **Header:** `Authorization: Bearer <your-MCP_AUTH_TOKEN>`
4. Save and test from the Claude chat interface — ask a clinical question and confirm the attending tutor responds.
5. Test from your **phone with the laptop off** to confirm the VM is serving independently.
