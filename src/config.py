from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    def load_dotenv(*args, **kwargs):
        return False


ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
os.environ.setdefault("USE_TF", "0")
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")


def _path(value: str | None, default: str) -> Path:
    p = Path(value or default)
    return p if p.is_absolute() else ROOT / p


def _bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_]+", "_", value).strip("_").lower()
    return slug[:48] or "default"


@dataclass
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_chat_model: str = os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1")
    openai_embedding_model: str = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
    backend_mode: str = os.getenv("BACKEND_MODE", "retrieval_only")
    free_local_mode: bool = _bool(os.getenv("FREE_LOCAL_MODE"), True)
    api_generation_enabled: bool = _bool(os.getenv("API_GENERATION_ENABLED"), False)
    embedding_provider: str = os.getenv("EMBEDDING_PROVIDER", "local")
    local_embedding_model: str = os.getenv("LOCAL_EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
    local_reranker_model: str = os.getenv("LOCAL_RERANKER_MODEL", "BAAI/bge-reranker-base")
    enable_local_reranker: bool = _bool(os.getenv("ENABLE_LOCAL_RERANKER"), True)
    enable_openai_generation: bool = _bool(os.getenv("ENABLE_OPENAI_GENERATION"), False) or api_generation_enabled
    local_models_offline: bool = _bool(os.getenv("LOCAL_MODELS_OFFLINE"), True)
    default_training_phase: str = os.getenv("DEFAULT_TRAINING_PHASE", "intern_year")
    anesthesia_crossover_percent: float = float(os.getenv("ANESTHESIA_CROSSOVER_PERCENT", "0.10"))
    data_dir: Path = _path(os.getenv("DATA_DIR"), "data")
    source_files: tuple[Path, ...] = tuple(
        Path(p.strip().strip('"')) for p in os.getenv("SOURCE_FILES", "").split(";") if p.strip()
    )
    chroma_dir: Path = _path(os.getenv("CHROMA_DIR"), "storage/chroma")
    sqlite_db_path: Path = _path(os.getenv("SQLITE_DB_PATH"), "storage/sqlite/student_model.db")
    log_dir: Path = _path(os.getenv("LOG_DIR"), "storage/logs")
    api_key: str = os.getenv("API_KEY", "")
    collection_name: str = os.getenv("CHROMA_COLLECTION", "anesthesia_sources")
    mcp_transport: str = os.getenv("MCP_TRANSPORT", "stdio")
    mcp_host: str = os.getenv("MCP_HOST", "127.0.0.1")
    mcp_port: int = int(os.getenv("MCP_PORT", "8000"))
    mcp_auth_token: str = os.getenv("MCP_AUTH_TOKEN", "")

    def ensure_dirs(self) -> None:
        for path in [self.data_dir, self.chroma_dir, self.sqlite_db_path.parent, self.log_dir]:
            path.mkdir(parents=True, exist_ok=True)

    def vector_collection_name(self) -> str:
        provider = self.embedding_provider.lower()
        if provider == "openai":
            model = self.openai_embedding_model
        elif provider == "local":
            model = self.local_embedding_model
        else:
            model = "none"
        return f"{self.collection_name}_{provider}_{_slug(model)}"

    def assert_backend_generation_allowed(self, provider: str) -> None:
        if self.free_local_mode or self.backend_mode == "retrieval_only" or not self.api_generation_enabled:
            raise RuntimeError(
                f"Backend LLM generation through {provider} is disabled. "
                "Clinical Attending OS is running in free local retrieval-only mode."
            )


settings = Settings()
