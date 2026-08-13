#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update -y
sudo apt-get install -y python3.12 python3.12-venv python3-pip git curl debian-keyring debian-archive-keyring apt-transport-https
if ! command -v caddy >/dev/null; then
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
  sudo apt-get update -y && sudo apt-get install -y caddy
fi
cd "$HOME"
[ -d anesthesia_attending ] || git clone <REPO_URL> anesthesia_attending
cd anesthesia_attending
python3.12 -m venv .venv --upgrade
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt
echo "setup.sh done"
