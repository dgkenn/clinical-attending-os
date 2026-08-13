# Hugging Face Docker Space for the Clinical Attending OS MCP server.
# Serves the FastMCP server over streamable-http (bearer-token auth) on :7860.
# The 1.5 GB Chroma index is pulled at startup from a PRIVATE HF dataset
# (so the copyrighted corpus is never in this public Space repo).
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/app/.hfcache \
    MCP_TRANSPORT=streamable-http \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=7860 \
    FREE_LOCAL_MODE=true \
    EMBEDDING_PROVIDER=local \
    LOCAL_MODELS_OFFLINE=false

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt huggingface_hub

COPY . .
RUN chmod +x deploy/hf/start.sh

EXPOSE 7860
CMD ["bash", "deploy/hf/start.sh"]
