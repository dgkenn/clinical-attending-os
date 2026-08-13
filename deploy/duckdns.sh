#!/usr/bin/env bash
# Cron: */5 * * * * /home/ubuntu/anesthesia_attending/deploy/duckdns.sh
DOMAIN="${DUCKDNS_DOMAIN:?set DUCKDNS_DOMAIN}"
TOKEN="${DUCKDNS_TOKEN:?set DUCKDNS_TOKEN}"
curl -fsS "https://www.duckdns.org/update?domains=${DOMAIN}&token=${TOKEN}&ip=" >/dev/null
