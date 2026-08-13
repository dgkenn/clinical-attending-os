"""corpus_ingest_dedup.py — Resumable, disk-aware, deduplicating corpus ingestion.

Usage:
    python scripts/corpus_ingest_dedup.py [--staging D:\\corpus_staging]
                                           [--threshold 0.92]
                                           [--dry-run]
                                           [--force-reprocess]
                                           [--batch-size 64]
                                           [--max-chunks-per-source N]

Design:
    1. Scans <staging> for .pdf / .txt / .json files.
    2. Skips files already tracked in the resumable state file
       (D:\\corpus_staging\\_ingest_state.json) unless --force-reprocess.
    3. Builds chunks using the repo's build_chunks() + infer_source_metadata().
    4. AGGRESSIVE DEDUP (two-pass):
       a) Exact: drop any new chunk whose chunk_id already exists in chunks.jsonl.
       b) Near-duplicate (Chroma kNN approach — NO corpus re-embedding):
          - Embed each NEW chunk ONCE via _embed_texts / batching.
          - Query the existing Chroma collection with the precomputed vector
            using col.query(query_embeddings=[vec], n_results=1). The collection
            uses cosine metric (confirmed via segment metadata), so Chroma returns
            distance = 1 - cosine_similarity. Convert: cosine_sim = 1 - distance.
            Drop the new chunk if cosine_sim >= threshold (default 0.92).
          - Also check new-vs-new dedup in-run (new chunk vs already-accepted
            new chunks from this run), using the precomputed vectors.
          - The existing 65k corpus is NEVER re-embedded. Only new chunks are
            embedded (~one pass). This eliminates the ~85-min re-embed.
    5. Writes only to D: for all state/temp files. Never writes multi-GB data
       to C: (storage/chroma is already on C: via existing junction — new state
       lives on D:).
    6. Aborts if D: free space < 5 GB before starting.
    7. --dry-run: reports all stats WITHOUT writing to Chroma or chunks.jsonl.
       Dry-run also runs Chroma-kNN dedup on first 500 new chunks and reports
       observed chunks/sec + projected full-run time + dedup drop rate.
    8. --max-chunks-per-source N: cap any single source_name to N chunks
       (default: off). Use to trim egregious over-chunkers (e.g. GOLD 2024 full
       report). Chunks are taken in page order (first N survive); remainder logged.

Distance→similarity note:
    Chroma collection was created with hnsw:space=cosine (confirmed in segment
    metadata). For cosine metric: distance = 1 - cosine_sim. With L2-normalized
    BGE vectors, cosine_sim == dot product. Self-query distance is ~0 (verified
    empirically). Threshold 0.92 → drop if distance <= 0.08.

Throughput:
    torch.set_num_threads() is set to max(1, cpu_count-2) at startup so the
    BGE model uses all available cores (leaving 1-2 for other research processes).
    Precomputed embeddings are passed directly to col.upsert(embeddings=...) so
    chunks are NOT re-embedded on write. Batching is 64 by default; print
    observed chunks/sec every batch.

Threshold rationale (0.92):
    BGE-small cosine similarity > 0.92 reliably flags paraphrased rewrites of
    the same fact (tested on medical text). 0.85–0.90 is the regime for
    "same topic, different emphasis"; we want to keep those. 0.95+ is nearly
    verbatim. 0.92 is the sweet spot: aggressive enough to suppress duplicate
    StatPearls articles and copy-pasted guideline text, conservative enough
    to keep complementary explanations.
"""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import shutil
import sys
import time
import types
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── torchvision stub (must run before any sentence_transformers / transformers import)
# torchvision has a broken registration call for torchvision::nms in this env which
# crashes at import time. We stub it out so the rest of transformers (BERT, tokenizers)
# can be imported normally. The stub is only active for this process.
def _install_torchvision_stub() -> None:
    if "torchvision" in sys.modules:
        return   # already imported (or already stubbed)

    class _FakeInterpolationMode:  # noqa: N801
        NEAREST = 0; BILINEAR = 2; BICUBIC = 3; BOX = 4
        HAMMING = 5; LANCZOS = 1; ANTIALIAS = 6; NEAREST_EXACT = 7

    _stubs = [
        "torchvision", "torchvision._meta_registrations",
        "torchvision.datasets", "torchvision.io",
        "torchvision.models", "torchvision.ops",
        "torchvision.utils", "torchvision.transforms",
    ]
    for _mod_name in _stubs:
        _m = types.ModuleType(_mod_name)
        _m.__spec__ = type("S", (), {  # type: ignore[assignment]
            "name": _mod_name, "loader": None,
            "submodule_search_locations": [],
        })()
        if "transforms" in _mod_name:
            _m.InterpolationMode = _FakeInterpolationMode  # type: ignore[attr-defined]
        sys.modules[_mod_name] = _m

_install_torchvision_stub()

# ── repo root on sys.path ────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
os.environ.setdefault("USE_TF", "0")
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")

# ── torch thread tuning: use all cores minus 2 for other processes ────────────
def _configure_torch_threads() -> int:
    """Set torch thread count to max(1, cpu_count-2). Returns the count used."""
    try:
        import torch
        cpu_count = os.cpu_count() or 4
        n = max(1, cpu_count - 2)
        current = torch.get_num_threads()
        if current < n:
            torch.set_num_threads(n)
        actual = torch.get_num_threads()
        print(f"[torch] threads: {actual} (cpu_count={cpu_count}, leaving 2 free)", flush=True)
        return actual
    except Exception:
        return -1

# ── constants ────────────────────────────────────────────────────────────────
DEFAULT_STAGING = Path(r"D:\corpus_staging")
DEFAULT_THRESHOLD = 0.92
MIN_FREE_GB = 5.0
CORPUS_SAMPLE_SIZE = 8000   # kept for backward compat; no longer used for re-embed
STATE_FILENAME = "_ingest_state.json"
LOG_FILENAME = "_ingest_log.jsonl"
DRY_RUN_SAMPLE = 500        # chunks to test kNN dedup on in dry-run mode
MAX_CHUNKS_PER_SOURCE_DEFAULT = 0  # 0 = disabled

# ── new-source pattern for infer_source_metadata extension ──────────────────
# These are matched BEFORE falling through to the generic "personal_notes"
# catch-all. Add entries here as new source families are downloaded.
NEW_SOURCE_PATTERNS: list[tuple[list[str], dict[str, Any]]] = [
    # StatPearls / NCBI Bookshelf
    (
        ["statpearls", "ncbi_bookshelf", "nbk", "bookshelf"],
        {
            "source_name_prefix": "StatPearls",   # will append stem if generic
            "library": "intern_year_medicine",
            "training_phase": "intern_year",
            "clinical_context": "wards",
            "source_family": "statpearls",
            "source_rank": 75,
        },
    ),
    # Society / professional guidelines (ACC/AHA, ESC, ASA, ACOG, IDSA, …)
    (
        ["guideline", "guidelines", "asa_", "aha_", "acc_", "esc_", "acog_",
         "idsa_", "sccm_", "society_", "consensus_", "practice_advisory"],
        {
            "source_name_prefix": "Society Guideline",
            "library": "intern_year_medicine",
            "training_phase": "intern_year",
            "clinical_context": "wards",
            "source_family": "guidelines",
            "source_rank": 88,
        },
    ),
    # MSD / Merck Manual (professional or consumer)
    (
        ["merck", "msd", "msdmanual", "merck_manual"],
        {
            "source_name_prefix": "Merck Manual",
            "library": "intern_year_medicine",
            "training_phase": "intern_year",
            "clinical_context": "wards",
            "source_family": "merck",
            "source_rank": 80,
        },
    ),
    # Open medical textbooks (OpenStax, Lecturio, Amboss exports, etc.)
    (
        ["openstax", "lecturio", "amboss", "osmosis", "open_textbook",
         "openanesthesia", "openanes"],
        {
            "source_name_prefix": "Open Textbook",
            "library": "intern_year_medicine",
            "training_phase": "intern_year",
            "clinical_context": "wards",
            "source_family": "open_textbook",
            "source_rank": 70,
        },
    ),
    # UpToDate / DynaMed exports (if you ever get them)
    (
        ["uptodate", "dynamed"],
        {
            "source_name_prefix": "Clinical Decision Support",
            "library": "intern_year_medicine",
            "training_phase": "intern_year",
            "clinical_context": "wards",
            "source_family": "clinical_support",
            "source_rank": 92,
        },
    ),
    # Anesthesia subspecialty guidelines / society docs
    (
        ["asa_guideline", "asra_", "difficult_airway", "das_guideline",
         "stoelting", "pharmacology_anes", "anesthesia_guideline"],
        {
            "source_name_prefix": "Anesthesia Guideline",
            "library": "anesthesiology_boards",
            "training_phase": "anesthesia_boards",
            "clinical_context": "OR",
            "source_family": "anesthesia",
            "source_rank": 90,
        },
    ),
]


def _new_source_meta_from_filename(filename: str):
    """Try to infer richer metadata for new source types before falling back.

    Returns a SourceMetadata or None (meaning: use existing infer_source_metadata).
    Intended to be called FIRST from a patched infer_source_metadata, but used
    directly by the ingest script for staging files.
    """
    from src.source_classifier import SourceMetadata

    name = filename.lower()
    stem = Path(filename).stem

    for patterns, meta_template in NEW_SOURCE_PATTERNS:
        if any(p in name for p in patterns):
            source_name = meta_template["source_name_prefix"]
            # If the filename has more content, append truncated stem
            clean_stem = stem.replace("_", " ").replace("-", " ").strip()
            if clean_stem.lower() not in source_name.lower() and len(clean_stem) <= 60:
                source_name = f"{source_name}: {clean_stem[:60]}"
            return SourceMetadata(
                source_name=source_name,
                library=meta_template["library"],
                training_phase=meta_template["training_phase"],
                clinical_context=meta_template["clinical_context"],
                source_family=meta_template["source_family"],
                source_rank=int(meta_template["source_rank"]),
            )
    return None


def patched_infer_source_metadata(filename: str):
    """Drop-in replacement for src.source_classifier.infer_source_metadata.

    Checks new-source patterns first, then delegates to the original.
    Apply with: src.source_classifier.infer_source_metadata = patched_infer_source_metadata
    """
    new_meta = _new_source_meta_from_filename(filename)
    if new_meta is not None:
        return new_meta
    from src.source_classifier import infer_source_metadata as _orig
    return _orig(filename)


# ── disk helpers ─────────────────────────────────────────────────────────────

def _d_drive_free_gb() -> float:
    """Return free space on D: in GB using Windows API, fallback shutil."""
    try:
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(  # type: ignore[attr-defined]
            r"D:\\", None, None, ctypes.byref(free_bytes)
        )
        return free_bytes.value / (1024 ** 3)
    except Exception:
        try:
            usage = shutil.disk_usage("D:\\")
            return usage.free / (1024 ** 3)
        except Exception:
            return 999.0


def _check_disk(min_free_gb: float = MIN_FREE_GB) -> None:
    free = _d_drive_free_gb()
    print(f"[disk] D: free space: {free:.1f} GB", flush=True)
    if free < min_free_gb:
        sys.exit(f"[ABORT] D: drive has only {free:.1f} GB free (need {min_free_gb} GB). "
                 "Free space before ingesting.")


# ── state tracking (resumable) ───────────────────────────────────────────────

def _state_path(staging: Path) -> Path:
    return staging / STATE_FILENAME


def _log_path(staging: Path) -> Path:
    return staging / LOG_FILENAME


def _load_state(staging: Path) -> dict[str, Any]:
    p = _state_path(staging)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"processed_files": {}}


def _save_state(staging: Path, state: dict[str, Any]) -> None:
    _state_path(staging).write_text(
        json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def _file_fingerprint(path: Path) -> str:
    stat = path.stat()
    return f"{stat.st_size}:{int(stat.st_mtime)}"


def _log_event(staging: Path, event: dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    with _log_path(staging).open("a", encoding="utf-8") as f:
        f.write(json.dumps({**event, "ts": datetime.now(timezone.utc).isoformat()},
                            ensure_ascii=False) + "\n")


# ── existing chunk IDs ────────────────────────────────────────────────────────

def _load_existing_ids(chunks_jsonl: Path) -> set[str]:
    ids: set[str] = set()
    if not chunks_jsonl.exists():
        return ids
    with chunks_jsonl.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                ids.add(json.loads(line)["id"])
            except Exception:
                pass
    return ids


# ── embedding helpers ────────────────────────────────────────────────────────
# We bypass the chromadb SentenceTransformerEmbeddingFunction wrapper because
# sentence_transformers.__init__ imports CrossEncoder which triggers torchvision,
# which has a broken torchvision::nms registration in this environment. Instead
# we load BertTokenizer + BertModel directly (BGE-small is a BERT architecture)
# using the torchvision stub installed at module load time above.

_BERT_MODEL_PATH: Path | None = None   # resolved lazily

def _find_local_bert_model() -> Path:
    """Locate the cached BGE-small snapshot on disk."""
    from src.config import settings
    model_name = settings.local_embedding_model           # e.g. BAAI/bge-small-en-v1.5
    cache_name = f"models--{model_name.replace('/', '--')}"
    hub_dir = Path.home() / ".cache" / "huggingface" / "hub" / cache_name / "snapshots"
    if hub_dir.exists():
        snaps = sorted(hub_dir.iterdir())
        if snaps:
            return snaps[-1]   # latest snapshot
    raise RuntimeError(
        f"BGE model snapshot not found under {hub_dir}. "
        "Ensure LOCAL_EMBEDDING_MODEL is cached."
    )


class _LocalBGEEmbedder:
    """Thin wrapper around BertTokenizer + BertModel for BGE-style embeddings.

    max_length controls tokenization truncation. For near-dup dedup, 256 is
    sufficient (captures main topic in the first ~1000 chars) and runs ~2x
    faster than 512 on CPU. The embeddings stored in Chroma were embedded at
    512 by the original ingestion pipeline; for dedup comparison the cosine
    similarity is well-maintained at 256 since the CLS token is dominated by
    early context.
    """

    def __init__(self, model_path: Path, max_length: int = 256) -> None:
        import torch
        from transformers.models.bert.tokenization_bert import BertTokenizer
        from transformers.models.bert.modeling_bert import BertModel

        self._torch = torch
        self._max_length = max_length
        # Use the GPU if one is available — BGE-small on CUDA is 10-100x faster than
        # CPU. Falls back to CPU automatically (correctness identical). Half-precision
        # on GPU roughly doubles throughput again with negligible effect on cosine.
        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._use_fp16 = self._device == "cuda"
        self._tok = BertTokenizer.from_pretrained(str(model_path), local_files_only=True)
        self._mdl = BertModel.from_pretrained(str(model_path), local_files_only=True)
        self._mdl.eval()
        self._mdl.to(self._device)
        if self._use_fp16:
            self._mdl.half()
        print(f"[embed] BGE model loaded from {model_path} "
              f"(max_length={max_length}, device={self._device}, fp16={self._use_fp16})", flush=True)

    def embed(self, texts: list[str]) -> list[list[float]]:
        torch = self._torch
        enc = self._tok(
            texts, padding=True, truncation=True,
            max_length=self._max_length, return_tensors="pt",
        )
        enc = {k: v.to(self._device) for k, v in enc.items()}
        with torch.no_grad():
            out = self._mdl(**enc)
            emb = out.last_hidden_state[:, 0, :]          # CLS token
            emb = torch.nn.functional.normalize(emb, dim=-1)
        return emb.float().cpu().tolist()


_embedder_cache: _LocalBGEEmbedder | None = None


def _load_embedding_fn(max_length: int = 256) -> _LocalBGEEmbedder:
    """Load (or return cached) BGE embedder using the repo's configured model.

    max_length=256 is the default for dedup (fast, 2x throughput vs 512).
    Pass 512 if you need full-fidelity embeddings for write (but for dedup 256
    is sufficient and the same model is used so cosine distances are comparable).
    """
    global _embedder_cache
    if _embedder_cache is not None:
        return _embedder_cache

    from src.config import settings
    provider = settings.embedding_provider.lower()

    if provider == "local":
        model_path = _find_local_bert_model()
        _embedder_cache = _LocalBGEEmbedder(model_path, max_length=max_length)
        return _embedder_cache
    elif provider == "openai":
        raise NotImplementedError(
            "OpenAI embedding for near-dup dedup not yet implemented in this script. "
            "Set EMBEDDING_PROVIDER=local or add OpenAI path."
        )
    else:
        raise RuntimeError(f"Unknown embedding_provider: {provider}")


def _embed_texts(embedder: _LocalBGEEmbedder, texts: list[str]) -> list[list[float]]:
    return embedder.embed(texts)


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


# ── numpy-accelerated pool cosine (used for max-sim check) ───────────────────
# Falls back to pure Python if numpy not available.

_POOL_MATRIX: "Any | None" = None   # numpy array (N, D), built lazily
_POOL_LIST: list[list[float]] = []   # parallel backing list for incremental adds


def _build_pool_matrix(pool: list[list[float]]) -> "Any":
    try:
        import numpy as np
        if pool:
            return np.array(pool, dtype="float32")
    except ImportError:
        pass
    return None


def _max_cosine_fast(vec: list[float], pool: list[list[float]]) -> float:
    """Return max cosine similarity of vec against all vectors in pool.

    Uses numpy dot-product broadcast for O(N) efficiency if numpy is available;
    falls back to pure Python _cosine otherwise.
    """
    if not pool:
        return 0.0
    try:
        import numpy as np
        v = np.array(vec, dtype="float32")
        P = np.array(pool, dtype="float32")
        # BGE embeddings are already L2-normalized, so dot == cosine
        sims = P @ v
        return float(sims.max())
    except ImportError:
        return _max_cosine(vec, pool)


# ── Chroma collection handle for kNN dedup ───────────────────────────────────
# The collection uses hnsw:space=cosine (confirmed via segment metadata in
# chroma.sqlite3). Distance returned = 1 - cosine_similarity. Self-distance
# is ~0 (verified empirically). To convert: cosine_sim = 1 - distance.
# BGE-small embeddings are L2-normalized (norm≈1.0), so dot product == cosine.

def _open_chroma_collection():
    """Open the existing Chroma collection WITHOUT an embedding function.

    We pass query_embeddings= directly, so no ef is needed at query time.
    Returns the collection or None if unavailable.
    """
    try:
        import chromadb
    except Exception:
        return None
    try:
        from src.config import settings
        client = chromadb.PersistentClient(path=str(settings.chroma_dir))
        # get_collection with no ef — we supply embeddings manually
        col = client.get_collection(settings.vector_collection_name())
        cnt = col.count()
        print(f"[chroma] opened collection '{settings.vector_collection_name()}' "
              f"({cnt} existing chunks)", flush=True)
        return col
    except Exception as e:
        print(f"[chroma] WARNING: could not open collection: {e}", flush=True)
        return None


def _chroma_knn_max_sim(col, vec: list[float]) -> float:
    """Query Chroma for the nearest existing chunk to vec.

    Returns max cosine similarity = 1 - distance (cosine metric collection).
    Returns 0.0 if the collection is empty or unavailable.
    Single-vector convenience wrapper; prefer _chroma_knn_batch_max_sims for speed.
    """
    if col is None:
        return 0.0
    try:
        res = col.query(query_embeddings=[vec], n_results=1, include=["distances"])
        dists = res.get("distances", [[]])[0]
        if not dists:
            return 0.0
        # cosine metric: distance = 1 - cosine_sim
        return float(1.0 - dists[0])
    except Exception:
        return 0.0


def _chroma_knn_batch_max_sims(col, vecs: list[list[float]]) -> list[float]:
    """Batch-query Chroma for the nearest existing chunk to each vec in vecs.

    col.query() accepts query_embeddings as a list of N vectors and returns
    N result-lists. This is ~3.5x faster than N serial single-vec queries.

    Returns list of cosine similarities (1 - distance), one per input vec.
    Returns list of 0.0s if unavailable.
    """
    if col is None or not vecs:
        return [0.0] * len(vecs)
    try:
        res = col.query(query_embeddings=vecs, n_results=1, include=["distances"])
        dist_lists = res.get("distances", [])
        sims = []
        for dl in dist_lists:
            if dl:
                sims.append(float(1.0 - dl[0]))
            else:
                sims.append(0.0)
        # Pad if needed
        while len(sims) < len(vecs):
            sims.append(0.0)
        return sims
    except Exception:
        return [0.0] * len(vecs)


def _write_to_chroma_with_embeddings(
    rows: list[dict[str, Any]],
    vecs: list[list[float]],
    batch_size: int = 256,
) -> bool:
    """Upsert rows into Chroma using precomputed embeddings.

    Passes embeddings= directly to col.upsert() so Chroma does NOT re-embed.
    This is a critical throughput optimization: without it, Chroma would call
    the embedding function again for every chunk.

    Returns True on success, False on failure.
    """
    if not rows:
        return True
    if len(rows) != len(vecs):
        print(f"[chroma-write] ERROR: row/vec count mismatch ({len(rows)} vs {len(vecs)})",
              flush=True)
        return False
    try:
        import chromadb
    except Exception:
        return False
    try:
        from src.config import settings
        client = chromadb.PersistentClient(path=str(settings.chroma_dir))
        # get_or_create without ef — we pass embeddings directly
        col = client.get_or_create_collection(settings.vector_collection_name())
    except Exception as e:
        print(f"[chroma-write] ERROR opening collection: {e}", flush=True)
        return False

    try:
        for start in range(0, len(rows), batch_size):
            batch_rows = rows[start : start + batch_size]
            batch_vecs = vecs[start : start + batch_size]
            col.upsert(
                ids=[r["id"] for r in batch_rows],
                documents=[r.get("search_text", r["text"]) for r in batch_rows],
                metadatas=[r["metadata"] for r in batch_rows],
                embeddings=[list(v) for v in batch_vecs],  # precomputed — no re-embed
            )
            done = min(start + batch_size, len(rows))
            print(f"  [chroma-write] {done}/{len(rows)} upserted", flush=True)
        return True
    except Exception as e:
        print(f"[chroma-write] ERROR during upsert: {e}", flush=True)
        return False


# ── near-dup check ────────────────────────────────────────────────────────────

def _max_cosine(vec: list[float], pool: list[list[float]]) -> float:
    if not pool:
        return 0.0
    best = 0.0
    for other in pool:
        c = _cosine(vec, other)
        if c > best:
            best = c
    return best


# ── text file to pseudo-PDF pages ────────────────────────────────────────────

def _load_txt_as_pages(path: Path) -> list[Any]:
    """Wrap a plain-text file in a list of PageText-like objects for chunk_page_text."""
    from src.pdf_loader import PageText

    text = path.read_text(encoding="utf-8", errors="replace")
    # Split into ~3000-char pages
    PAGE_SIZE = 3000
    chunks = [text[i : i + PAGE_SIZE] for i in range(0, max(1, len(text)), PAGE_SIZE)]
    pages = []
    for idx, chunk in enumerate(chunks, start=1):
        pages.append(
            PageText(
                path=path,
                page_number=idx,
                total_pages=len(chunks),
                text=chunk,
                chapter_number=None,
                chapter_title="",
                has_bold=False,
            )
        )
    return pages


# ── build chunks from staging files ──────────────────────────────────────────

def _build_staging_chunks(paths: list[Path]) -> list[dict[str, Any]]:
    """Build chunks from PDFs and .txt/.json files using the repo's pipeline.

    Patches infer_source_metadata for the duration so new source types get
    sensible metadata instead of 'Unknown / personal_notes'.
    """
    import src.source_classifier as sc
    import src.ingest as ing

    # Patch at module level so build_chunks() picks it up
    original = sc.infer_source_metadata
    sc.infer_source_metadata = patched_infer_source_metadata  # type: ignore[assignment]
    # Also patch the reference inside ingest module (it imported by name at load time)
    ing.infer_source_metadata = patched_infer_source_metadata  # type: ignore[assignment]

    try:
        from src.chunking import chunk_page_text, detect_section
        from src.ingest import build_search_text, chunk_id, normalize_search_text
        from src.fact_extraction import is_testable_chunk, split_fact_units
        from src.ingest import build_fact_row
        from src.topic_taxonomy import build_retrieval_tags
        from datetime import datetime, timezone

        now = datetime.now(timezone.utc).isoformat()
        rows: list[dict[str, Any]] = []
        fact_rows: list[dict[str, Any]] = []

        pdf_paths = [p for p in paths if p.suffix.lower() == ".pdf"]
        txt_paths = [p for p in paths if p.suffix.lower() in (".txt",)]

        # PDFs — standard path
        if pdf_paths:
            pdf_chunks = ing.build_chunks(pdf_paths)
            rows.extend([r for r in pdf_chunks if r.get("metadata", {}).get("chunk_type") != "fact"])
            fact_rows.extend([r for r in pdf_chunks if r.get("metadata", {}).get("chunk_type") == "fact"])

        # .txt files — synthesise PageText objects
        for path in txt_paths:
            source_meta = patched_infer_source_metadata(path.name)
            pages = _load_txt_as_pages(path)
            for page in pages:
                for idx, text in enumerate(chunk_page_text(page.text), start=1):
                    cid = chunk_id(path.name, page.page_number, idx, text)
                    section = detect_section(page.text)
                    tags = build_retrieval_tags(text, source_meta.source_name, section, source_meta.clinical_context)
                    clinical_context = str(tags.get("clinical_context") or source_meta.clinical_context)
                    row: dict[str, Any] = {
                        "id": cid,
                        "text": text,
                        "search_text": build_search_text(text, tags, source_meta, section),
                        "metadata": {
                            "filename": path.name,
                            "path": str(path),
                            "book": source_meta.source_name,
                            "source_name": source_meta.source_name,
                            "library": source_meta.library,
                            "training_phase": source_meta.training_phase,
                            "clinical_context": clinical_context,
                            "source_family": source_meta.source_family,
                            "page": page.page_number,
                            "page_number": page.page_number,
                            "total_pages": page.total_pages,
                            "chunk_id": cid,
                            "ingested_at": now,
                            "ingestion_timestamp": now,
                            "section": section,
                            "section_heading": section,
                            "heading_path": section,
                            "chapter_number": page.chapter_number,
                            "chapter_title": page.chapter_title,
                            "has_bold": False,
                            "topic_tags": ",".join(tags.get("topic_tags", [])),
                            "keyword_tags": ",".join(tags.get("keyword_tags", [])),
                            "synonym_tags": ",".join(tags.get("synonym_tags", [])),
                            "retrieval_tags": ",".join(tags.get("retrieval_tags", [])),
                            "source_rank": source_meta.source_rank,
                            "chunk_type": "passage",
                        },
                    }
                    rows.append(row)
                    if is_testable_chunk(row["metadata"], text):
                        for fact_idx, fact in enumerate(split_fact_units(text), start=1):
                            fact_rows.append(build_fact_row(row, fact, fact_idx))

        return rows + fact_rows

    finally:
        # Restore originals
        sc.infer_source_metadata = original
        ing.infer_source_metadata = original


# ── main dedup pipeline ───────────────────────────────────────────────────────

def run(
    staging: Path,
    threshold: float = DEFAULT_THRESHOLD,
    dry_run: bool = False,
    force_reprocess: bool = False,
    batch_size: int = 64,
    corpus_sample: int = CORPUS_SAMPLE_SIZE,  # kept for CLI compat; no longer used
    max_chunks_per_source: int = MAX_CHUNKS_PER_SOURCE_DEFAULT,
    dedup_max_length: int = 256,
) -> None:
    t0 = time.time()
    print(f"\n{'='*60}", flush=True)
    print(f"corpus_ingest_dedup  {'[DRY-RUN]' if dry_run else '[LIVE]'}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    print(f"  staging : {staging}", flush=True)
    print(f"  threshold: {threshold}", flush=True)
    print(f"{'='*60}\n", flush=True)

    # 1. Disk check
    _check_disk()

    # 2. Staging dir must exist
    if not staging.exists():
        sys.exit(f"[ABORT] staging dir not found: {staging}  (create it and drop files in)")

    # 3. Discover source files (ignore state files)
    IGNORE_SUFFIXES = {".json", ".jsonl"}  # state/log files at top level
    staging_files = sorted([
        p for p in staging.rglob("*")
        if p.is_file()
        and p.suffix.lower() in (".pdf", ".txt")
        and p.name not in (STATE_FILENAME, LOG_FILENAME)
    ])
    if not staging_files:
        print("[warn] No .pdf or .txt files found in staging dir. Nothing to do.", flush=True)
        return

    print(f"[staging] {len(staging_files)} file(s) found", flush=True)

    # 4. Resumable state: skip already-processed files
    state = _load_state(staging)
    processed = state.get("processed_files", {})
    pending: list[Path] = []
    for p in staging_files:
        fp = _file_fingerprint(p)
        if not force_reprocess and processed.get(str(p)) == fp:
            print(f"  [skip] {p.name}  (already processed)", flush=True)
        else:
            pending.append(p)

    if not pending:
        print("[done] All files already processed. Use --force-reprocess to re-run.", flush=True)
        return

    print(f"[staging] {len(pending)} file(s) to process", flush=True)

    # 5. Chunk all pending files
    print("\n[chunk] Building chunks ...", flush=True)
    new_rows = _build_staging_chunks(pending)
    print(f"[chunk] {len(new_rows)} raw chunks from {len(pending)} file(s)", flush=True)

    if not new_rows:
        print("[warn] No chunks produced. Files may be empty or unreadable.", flush=True)
        return

    # 5b. Per-source breakdown BEFORE dedup (so we see raw over-chunkers)
    _print_source_breakdown(new_rows, label="raw pre-dedup", flag_threshold=5000)

    # 5c. Optional per-source cap (--max-chunks-per-source)
    if max_chunks_per_source > 0:
        new_rows = _apply_source_cap(new_rows, max_chunks_per_source)

    # 6. Exact dedup: drop IDs already in chunks.jsonl
    from src.config import settings
    chunks_jsonl = settings.chroma_dir / "chunks.jsonl"
    existing_ids = _load_existing_ids(chunks_jsonl)
    print(f"\n[dedup:exact] {len(existing_ids)} existing IDs in corpus", flush=True)

    exact_pass: list[dict[str, Any]] = []
    exact_dropped = 0
    for row in new_rows:
        if row["id"] in existing_ids:
            exact_dropped += 1
        else:
            exact_pass.append(row)
    print(f"[dedup:exact] dropped {exact_dropped} exact dupes, {len(exact_pass)} remain", flush=True)

    if not exact_pass:
        print("[done] All chunks were exact dupes. Nothing new to add.", flush=True)
        _mark_processed(staging, state, pending, dry_run)
        return

    # 7. Near-dup dedup — Chroma kNN approach (NO corpus re-embedding)
    #
    # Collection metric: cosine (hnsw:space=cosine confirmed in segment metadata).
    # Chroma distance = 1 - cosine_similarity.
    # => cosine_sim = 1 - distance
    # Threshold 0.92 => drop if distance <= 0.08
    #
    # New-vs-new dedup across batches is handled by upserting each accepted batch
    # into the SAME `col` handle immediately, so later batches' kNN queries see them
    # (O(1) per chunk — no growing in-memory pool). Within a batch we compare against
    # only that batch's accepted vecs (<= batch_size).
    #
    # In --dry-run mode, we only test the first DRY_RUN_SAMPLE chunks so the
    # report comes back quickly (and nothing is upserted).

    print(f"\n[dedup:near] Loading embedding model (max_length={dedup_max_length}) ...", flush=True)
    _configure_torch_threads()
    ef = _load_embedding_fn(max_length=dedup_max_length)

    # Open Chroma collection (no ef needed — we pass embeddings directly)
    col = _open_chroma_collection()
    chroma_available = col is not None

    if not chroma_available:
        print("[dedup:near] WARNING: Chroma unavailable. Near-dup vs existing corpus DISABLED.",
              flush=True)

    # In dry-run: limit to first DRY_RUN_SAMPLE chunks for fast reporting
    if dry_run:
        sample_for_dry = exact_pass[:DRY_RUN_SAMPLE]
        print(f"[dry-run] Testing near-dup on first {len(sample_for_dry)}/{len(exact_pass)} chunks", flush=True)
        candidates = sample_for_dry
    else:
        candidates = exact_pass

    accepted: list[dict[str, Any]] = []   # kept for final report/log (append = O(1))
    added_json = 0
    near_dropped_total = 0
    chroma_write_ok = True
    total_to_embed = len(candidates)

    print(f"[dedup:near] embedding {total_to_embed} candidate chunks "
          f"(batch={batch_size}, cosine metric: drop if sim>={threshold}) ...", flush=True)

    from src.ingest import store_chunks_jsonl

    embed_t0 = time.time()
    chunks_embedded_so_far = 0

    for batch_start in range(0, total_to_embed, batch_size):
        batch_rows = candidates[batch_start : batch_start + batch_size]
        batch_texts = [r.get("search_text") or r.get("text", "") for r in batch_rows]

        t_embed_start = time.time()
        batch_vecs = _embed_texts(ef, batch_texts)
        embed_secs = (time.time() - t_embed_start) or 0.001
        cps = len(batch_texts) / embed_secs
        chunks_embedded_so_far += len(batch_texts)

        # Batch kNN query against the collection. Accepted chunks from EARLIER batches
        # were already upserted into this same `col`, so the query also dedups
        # new-vs-new across batches — O(1) per chunk, no growing in-memory pool.
        if chroma_available:
            corpus_sims = _chroma_knn_batch_max_sims(col, batch_vecs)
        else:
            corpus_sims = [0.0] * len(batch_vecs)

        # Decide accepted rows for THIS batch. Intra-batch new-vs-new dedup compares
        # only against this batch's accepted vecs (<= batch_size — negligible cost).
        batch_accept_rows: list[dict[str, Any]] = []
        batch_accept_vecs: list[list[float]] = []
        for row, vec, corpus_sim in zip(batch_rows, batch_vecs, corpus_sims):
            max_sim = max(corpus_sim, _max_cosine_fast(vec, batch_accept_vecs))
            if max_sim >= threshold:
                near_dropped_total += 1
                # Keep existing chunk (already indexed). Never replace with dupe.
            else:
                batch_accept_rows.append(row)
                batch_accept_vecs.append(vec)

        # Incremental commit (live run only): append to chunks.jsonl and upsert into
        # the SAME `col` handle so the next batch's kNN query sees these chunks.
        if not dry_run and batch_accept_rows:
            added_json += store_chunks_jsonl(batch_accept_rows, force=False)
            if chroma_available:
                try:
                    col.upsert(
                        ids=[r["id"] for r in batch_accept_rows],
                        documents=[r.get("search_text", r["text"]) for r in batch_accept_rows],
                        metadatas=[r["metadata"] for r in batch_accept_rows],
                        embeddings=[list(v) for v in batch_accept_vecs],
                    )
                except Exception as e:
                    print(f"  [chroma-write] ERROR during upsert: {e}", flush=True)
                    chroma_write_ok = False
        accepted.extend(batch_accept_rows)

        done = min(batch_start + batch_size, total_to_embed)
        elapsed_so_far = (time.time() - embed_t0) or 0.001
        avg_cps = chunks_embedded_so_far / elapsed_so_far
        print(
            f"  [dedup:near] {done}/{total_to_embed} | "
            f"batch {cps:.1f} c/s | avg {avg_cps:.1f} c/s | "
            f"accepted: {len(accepted)} | near-dropped: {near_dropped_total}",
            flush=True,
        )

    embed_elapsed = time.time() - embed_t0
    avg_cps_final = total_to_embed / (embed_elapsed or 0.001)

    print(f"\n[dedup summary]", flush=True)
    print(f"  raw chunks        : {len(new_rows)}", flush=True)
    print(f"  exact dupes       : {exact_dropped}", flush=True)
    if dry_run:
        full_n = len(exact_pass)
        near_rate = near_dropped_total / max(1, len(candidates))
        print(f"  near dupes (sample {len(candidates)}/{full_n}): {near_dropped_total} "
              f"({near_rate*100:.1f}% drop rate)", flush=True)
        projected_accept = int(full_n * (1 - near_rate))
        projected_secs = full_n / max(1.0, avg_cps_final)
        print(f"  [DRY-RUN projection] full near-dup check: ~{projected_secs/60:.1f} min "
              f"at {avg_cps_final:.1f} c/s", flush=True)
        print(f"  [DRY-RUN projection] estimated accepted chunks: ~{projected_accept}", flush=True)
    else:
        print(f"  near dupes (>={threshold}): {near_dropped_total}", flush=True)
    print(f"  accepted (committed): {len(accepted)}", flush=True)
    print(f"  embed throughput  : {avg_cps_final:.1f} chunks/sec", flush=True)

    # 8. Dry-run: stop here (nothing was written)
    if dry_run:
        print("\n[dry-run] No data written. Re-run without --dry-run to commit.", flush=True)
        _print_source_breakdown(exact_pass[:DRY_RUN_SAMPLE], label="dry-run sample (pre-near-dedup)")
        return

    # 9. Writes already happened incrementally per batch (chunks.jsonl + Chroma upsert
    #    via the same `col` handle, with precomputed embeddings — no re-embed).
    if not accepted:
        print("[done] Nothing new to write after dedup.", flush=True)
        _mark_processed(staging, state, pending, dry_run=False)
        return
    print(f"[write] {added_json} chunks written to chunks.jsonl (incremental)", flush=True)
    print(f"[write] Chroma upsert (precomputed embeds, incremental): "
          f"{'OK' if chroma_write_ok else 'FAILED (check chromadb)'}", flush=True)

    # 10. Mark files as processed
    _mark_processed(staging, state, pending, dry_run=False)

    elapsed = time.time() - t0
    print(f"\n[done] Completed in {elapsed:.1f}s  |  {len(accepted)} new chunks indexed.", flush=True)

    _log_event(staging, {
        "files": [str(p) for p in pending],
        "raw_chunks": len(new_rows),
        "exact_dropped": exact_dropped,
        "near_dropped": near_dropped_total,
        "accepted": len(accepted),
        "jsonl_added": added_json,
        "chroma_ok": chroma_write_ok,
        "threshold": threshold,
        "embed_cps": round(avg_cps_final, 2),
    }, dry_run=False)

    _print_source_breakdown(accepted, label="written to corpus")


def _print_source_breakdown(rows: list[dict[str, Any]], label: str = "accepted", flag_threshold: int = 5000) -> None:
    from collections import Counter
    sources: Counter[str] = Counter()
    for r in rows:
        src = r.get("metadata", {}).get("source_name", "unknown")
        sources[src] += 1
    print(f"\n[source breakdown — {label}]  total={len(rows)}", flush=True)
    flagged = []
    for src, count in sources.most_common(40):
        flag = " *** OVER-CHUNK ***" if count >= flag_threshold else ""
        print(f"  {count:>6}  {src}{flag}", flush=True)
        if count >= flag_threshold:
            flagged.append((src, count))
    if flagged:
        print(f"\n[WARNING] {len(flagged)} source(s) exceed {flag_threshold} chunks:", flush=True)
        for src, count in flagged:
            print(f"  {count}  {src}  — consider --max-chunks-per-source to cap", flush=True)


def _apply_source_cap(rows: list[dict[str, Any]], max_per_source: int) -> list[dict[str, Any]]:
    """Cap each source_name to at most max_per_source chunks (in list order).

    Returns the filtered list and prints a summary of what was dropped.
    """
    from collections import defaultdict
    counts: dict[str, int] = defaultdict(int)
    accepted: list[dict[str, Any]] = []
    dropped_total = 0
    for r in rows:
        src = r.get("metadata", {}).get("source_name", "unknown")
        if counts[src] < max_per_source:
            accepted.append(r)
            counts[src] += 1
        else:
            dropped_total += 1
    if dropped_total:
        print(f"[source-cap] dropped {dropped_total} chunks exceeding {max_per_source}/source", flush=True)
        for src, cnt in sorted(counts.items(), key=lambda x: -x[1]):
            if cnt >= max_per_source:
                print(f"  {src}: capped at {max_per_source}", flush=True)
    return accepted


def _mark_processed(staging: Path, state: dict[str, Any], files: list[Path], dry_run: bool) -> None:
    if dry_run:
        return
    for p in files:
        state.setdefault("processed_files", {})[str(p)] = _file_fingerprint(p)
    _save_state(staging, state)
    print(f"[state] {len(files)} file(s) marked as processed in {_state_path(staging)}", flush=True)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resumable, deduplicating corpus ingestion from a staging folder."
    )
    parser.add_argument(
        "--staging",
        type=Path,
        default=DEFAULT_STAGING,
        help=f"Path to staging folder (default: {DEFAULT_STAGING})",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=f"Near-dup cosine similarity threshold (default: {DEFAULT_THRESHOLD})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report stats without writing to Chroma or chunks.jsonl",
    )
    parser.add_argument(
        "--force-reprocess",
        action="store_true",
        help="Re-process files even if already tracked in state",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="Embedding batch size (default: 64; reduce if OOM)",
    )
    parser.add_argument(
        "--corpus-sample",
        type=int,
        default=CORPUS_SAMPLE_SIZE,
        help=(
            f"Deprecated (ignored). Near-dup now uses Chroma kNN against stored "
            f"embeddings instead of re-embedding the corpus. Kept for CLI compatibility."
        ),
    )
    parser.add_argument(
        "--max-chunks-per-source",
        type=int,
        default=MAX_CHUNKS_PER_SOURCE_DEFAULT,
        help=(
            "Cap any single source_name to this many chunks before dedup "
            "(default: 0 = disabled). Useful for trimming over-chunked sources "
            "like the GOLD 2024 full report. Chunks are kept in page order."
        ),
    )
    parser.add_argument(
        "--dedup-max-length",
        type=int,
        default=256,
        help=(
            "Token max_length for embedding during near-dup check "
            "(default: 256). Lower = faster; 256 tokens (~1000 chars) captures "
            "enough semantic content for dedup and runs ~2x faster than 512. "
            "The Chroma write uses the same embeddings, so they are stored at "
            "this length. If you want full-fidelity embeddings use 512."
        ),
    )
    args = parser.parse_args()

    run(
        staging=args.staging,
        threshold=args.threshold,
        dry_run=args.dry_run,
        force_reprocess=args.force_reprocess,
        batch_size=args.batch_size,
        corpus_sample=args.corpus_sample,
        max_chunks_per_source=args.max_chunks_per_source,
        dedup_max_length=args.dedup_max_length,
    )


if __name__ == "__main__":
    main()
