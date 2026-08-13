from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .chunking import chunk_page_text, detect_section
from .config import settings
from .fact_extraction import fact_subtopic, fact_target_id, is_testable_chunk, split_fact_units
from .pdf_loader import discover_pdfs, load_pdf_pages
from .source_classifier import infer_source_metadata
from .topic_taxonomy import build_retrieval_tags


def normalize_search_text(text: str) -> str:
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)
    return re.sub(r"\s+", " ", text).strip()


def build_search_text(text: str, tags: dict[str, Any], source_meta: Any, section: str) -> str:
    tag_text = " ".join(str(item) for item in tags.get("retrieval_tags", []))
    source_text = f"{source_meta.source_name} {source_meta.library} {source_meta.training_phase} {section}"
    return normalize_search_text(f"{text}\n\nRetrieval tags: {tag_text} {source_text}")


def build_fact_row(parent: dict[str, Any], fact: str, fact_idx: int) -> dict[str, Any]:
    meta = parent["metadata"]
    source_name = meta.get("source_name") or meta.get("book", "")
    page = meta.get("page")
    fid = "fact-" + fact_target_id(source_name, page, fact, fact_idx)
    section = meta.get("section", "")
    tags = build_retrieval_tags(fact, source_name, section, meta.get("clinical_context", "wards"))
    retrieval_text = normalize_search_text(
        f"{fact}\n\nSource fact target: {fact_subtopic(source_name, page, fact)}\n"
        f"Retrieval tags: {' '.join(str(item) for item in tags.get('retrieval_tags', []))} "
        f"{source_name} {meta.get('library','')} {meta.get('training_phase','')} {section}"
    )
    fact_meta = dict(meta)
    fact_meta.update(
        {
            "chunk_id": fid,
            "chunk_type": "fact",
            "parent_chunk_id": meta.get("chunk_id", parent.get("id", "")),
            "fact_index": fact_idx,
            "fact_text": fact,
            "subtopic": fact_subtopic(source_name, page, fact),
            "topic_tags": ",".join(sorted(set((meta.get("topic_tags", "").split(",") if meta.get("topic_tags") else []) + list(tags.get("topic_tags", []))))),
            "keyword_tags": ",".join(tags.get("keyword_tags", [])),
            "synonym_tags": ",".join(tags.get("synonym_tags", [])),
            "retrieval_tags": ",".join(tags.get("retrieval_tags", [])),
        }
    )
    return {"id": fid, "text": fact, "search_text": retrieval_text, "metadata": fact_meta}


def chunk_id(filename: str, page: int, idx: int, text: str) -> str:
    digest = hashlib.sha1(f"{filename}|{page}|{idx}|{text[:200]}".encode("utf-8")).hexdigest()[:16]
    return f"{Path(filename).stem}-{page}-{idx}-{digest}"


def build_chunks(pdf_paths: list[Path]) -> list[dict[str, Any]]:
    now = datetime.now(timezone.utc).isoformat()
    rows: list[dict[str, Any]] = []
    fact_rows: list[dict[str, Any]] = []
    for pdf in pdf_paths:
        source_meta = infer_source_metadata(pdf.name)
        for page in load_pdf_pages(pdf):
            for idx, text in enumerate(chunk_page_text(page.text), start=1):
                cid = chunk_id(pdf.name, page.page_number, idx, text)
                section = detect_section(page.text)
                tags = build_retrieval_tags(text, source_meta.source_name, section, source_meta.clinical_context)
                clinical_context = str(tags.get("clinical_context") or source_meta.clinical_context)
                rows.append(
                    row := {
                        "id": cid,
                        "text": text,
                        "search_text": build_search_text(text, tags, source_meta, section),
                        "metadata": {
                            "filename": pdf.name,
                            "path": str(pdf),
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
                            "has_bold": bool(page.has_bold),
                            "topic_tags": ",".join(tags.get("topic_tags", [])),
                            "keyword_tags": ",".join(tags.get("keyword_tags", [])),
                            "synonym_tags": ",".join(tags.get("synonym_tags", [])),
                            "retrieval_tags": ",".join(tags.get("retrieval_tags", [])),
                            "source_rank": source_meta.source_rank,
                            "chunk_type": "passage",
                        },
                    }
                )
                if is_testable_chunk(row["metadata"], text):
                    for fact_idx, fact in enumerate(split_fact_units(text), start=1):
                        fact_rows.append(build_fact_row(row, fact, fact_idx))
    return rows + fact_rows


def _json_store_path() -> Path:
    return settings.chroma_dir / "chunks.jsonl"


def _hf_model_cached(model_name: str) -> bool:
    cache_name = f"models--{model_name.replace('/', '--')}"
    candidates = [
        Path.home() / ".cache" / "huggingface" / "hub" / cache_name,
        Path.home() / ".cache" / "torch" / "sentence_transformers" / model_name.replace("/", "_"),
    ]
    return any(path.exists() for path in candidates)


def store_chunks_jsonl(rows: list[dict[str, Any]], force: bool = False) -> int:
    settings.ensure_dirs()
    path = _json_store_path()
    existing_ids: set[str] = set()
    if path.exists() and not force:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    existing_ids.add(json.loads(line)["id"])
                except Exception:
                    pass
    mode = "w" if force else "a"
    added = 0
    with path.open(mode, encoding="utf-8") as f:
        for row in rows:
            if row["id"] in existing_ids:
                continue
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            added += 1
    return added


def write_ingestion_manifest(rows: list[dict[str, Any]], pdfs: list[Path]) -> Path:
    manifest: dict[str, dict[str, Any]] = {}
    for pdf in pdfs:
        source_meta = infer_source_metadata(pdf.name)
        manifest[pdf.name] = {
            "file": str(pdf),
            "chunks": 0,
            "passage_chunks": 0,
            "fact_chunks": 0,
            "pages": 0,
            "library": source_meta.library,
            "training_phase": source_meta.training_phase,
            "source_name": source_meta.source_name,
            "clinical_context": source_meta.clinical_context,
            "ingested_at": datetime.now(timezone.utc).isoformat(),
        }
    pages_by_file: dict[str, set[int]] = {pdf.name: set() for pdf in pdfs}
    for row in rows:
        meta = row.get("metadata", {})
        filename = meta.get("filename")
        if filename not in manifest:
            continue
        manifest[filename]["chunks"] += 1
        if meta.get("chunk_type") == "fact":
            manifest[filename]["fact_chunks"] += 1
        else:
            manifest[filename]["passage_chunks"] += 1
        if meta.get("page"):
            pages_by_file[filename].add(int(meta["page"]))
    for filename, pages in pages_by_file.items():
        manifest[filename]["pages"] = len(pages)
    path = settings.chroma_dir / "ingestion_manifest.json"
    path.write_text(json.dumps(list(manifest.values()), indent=2), encoding="utf-8")
    return path


def store_chunks_chroma(rows: list[dict[str, Any]], force: bool = False) -> bool:
    try:
        import chromadb
        from chromadb.utils import embedding_functions
    except Exception:
        return False

    provider = settings.embedding_provider.lower()
    if provider == "openai":
        if not settings.openai_api_key:
            return False
        ef = embedding_functions.OpenAIEmbeddingFunction(
            api_key=settings.openai_api_key, model_name=settings.openai_embedding_model
        )
    elif provider == "local":
        if settings.local_models_offline and not _hf_model_cached(settings.local_embedding_model):
            return False
        os.environ.setdefault("USE_TF", "0")
        os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
        if settings.local_models_offline:
            os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
            os.environ.setdefault("HF_HUB_OFFLINE", "1")
        try:
            ef = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name=settings.local_embedding_model
            )
        except Exception:
            return False
    else:
        return False

    client = chromadb.PersistentClient(path=str(settings.chroma_dir))
    if force:
        try:
            client.delete_collection(settings.vector_collection_name())
        except Exception:
            pass
    col = client.get_or_create_collection(settings.vector_collection_name(), embedding_function=ef)
    if not rows:
        return True
    batch_size = int(os.getenv("EMBEDDING_BATCH_SIZE", "256"))
    for start in range(0, len(rows), batch_size):
        batch = rows[start : start + batch_size]
        col.upsert(
            ids=[r["id"] for r in batch],
            documents=[r.get("search_text", r["text"]) for r in batch],
            metadatas=[r["metadata"] for r in batch],
        )
        print(f"embedded {min(start + batch_size, len(rows))}/{len(rows)}", flush=True)
    return True


def ingest(force: bool = False, source: str | None = None) -> dict[str, Any]:
    settings.ensure_dirs()
    pdfs = discover_pdfs(settings.data_dir, settings.source_files, source)
    rows = build_chunks(pdfs)
    added_json = store_chunks_jsonl(rows, force=force)
    chroma_ok = store_chunks_chroma(rows, force=force)
    manifest_path = write_ingestion_manifest(rows, pdfs)
    return {
        "pdfs": len(pdfs),
        "chunks_built": len(rows),
        "chunks_added_jsonl": added_json,
        "chroma_enabled": chroma_ok,
        "embedding_provider": settings.embedding_provider,
        "vector_collection": settings.vector_collection_name(),
        "store": str(_json_store_path()),
        "manifest": str(manifest_path),
        "bm25_index": "jsonl-backed; rebuilt automatically from chunk store at query time",
    }


def build_curated_chunks(units: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Convert curated knowledge units (from curated_candidates.json) into the same
    row schema produced by build_chunks() for PDF-derived passages.

    Each output row has exactly:
        id           : stable, deterministic, prefixed 'curated-' (already in source)
        text         : teaching content
        search_text  : text + retrieval tags string (same build_retrieval_tags path)
        metadata     : dict matching PDF chunk metadata keys, with source_name='Curated Units'

    Returns (valid_rows, dropped) where dropped is a list of
    {'id', 'reason'} dicts for units that lacked required fields.
    """
    now = datetime.now(timezone.utc).isoformat()
    valid_rows: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []

    for unit in units:
        uid = unit.get("id", "")
        text = unit.get("text", "").strip()
        topic = unit.get("topic", "").strip()

        # Validation: must have non-empty text and topic
        if not text:
            dropped.append({"id": uid, "reason": "missing text"})
            continue
        if not topic:
            dropped.append({"id": uid, "reason": "missing topic"})
            continue

        # Ensure id carries 'curated-' prefix (already set in curated_candidates.json,
        # but guard against direct use of raw source records)
        if not uid.startswith("curated-"):
            uid = "curated-" + uid

        library = unit.get("library", "intern_year_medicine") or "intern_year_medicine"
        subtopic = unit.get("subtopic", "")
        section = subtopic or ""

        # Mirror the clinical_context inference the PDF pipeline uses
        tags = build_retrieval_tags(text, "Curated Units", section, "wards")
        clinical_context = str(tags.get("clinical_context") or "wards")

        # Build search_text the same way build_search_text() does for PDF chunks
        tag_text = " ".join(str(item) for item in tags.get("retrieval_tags", []))
        source_text = f"Curated Units {library} curated {section}"
        search_text = normalize_search_text(f"{text}\n\nRetrieval tags: {tag_text} {source_text}")

        # Normalise tags list for metadata (CSV string, same as PDF pipeline)
        raw_tags: list[str] = unit.get("tags") or []
        if isinstance(raw_tags, str):
            raw_tags = [t.strip() for t in raw_tags.split(",") if t.strip()]
        original_tags_csv = ",".join(raw_tags)

        metadata: dict[str, Any] = {
            # Fields present in PDF passage metadata — curated equivalents
            "filename": "curated_candidates.json",
            "path": "curated_candidates.json",
            "book": "Curated Units",
            "source_name": "Curated Units",
            "library": library,
            "training_phase": "curated",
            "clinical_context": clinical_context,
            "source_family": "curated",
            "page": 0,
            "page_number": 0,
            "total_pages": 0,
            "chunk_id": uid,
            "ingested_at": now,
            "ingestion_timestamp": now,
            "section": section,
            "section_heading": section,
            "heading_path": section,
            "chapter_number": 0,
            "chapter_title": topic,
            "has_bold": False,
            "topic_tags": ",".join(tags.get("topic_tags", [])),
            "keyword_tags": ",".join(tags.get("keyword_tags", [])),
            "synonym_tags": ",".join(tags.get("synonym_tags", [])),
            "retrieval_tags": ",".join(tags.get("retrieval_tags", [])),
            "source_rank": 80,
            "chunk_type": "fact",
            # Curated-specific bonus fields (harmless extras consumers can ignore)
            "topic": topic,
            "subtopic": subtopic,
            "original_tags": original_tags_csv,
        }

        valid_rows.append({"id": uid, "text": text, "search_text": search_text, "metadata": metadata})

    return valid_rows, dropped


def ingest_curated(curated_path: Path, dry_run: bool = False) -> dict[str, Any]:
    """Load curated_candidates.json, convert to rows, and optionally upsert into Chroma.

    With dry_run=True this function validates rows and reports counts WITHOUT touching
    the jsonl store or Chroma collection.
    """
    with curated_path.open("r", encoding="utf-8") as f:
        units: list[dict[str, Any]] = json.load(f)

    valid_rows, dropped = build_curated_chunks(units)

    result: dict[str, Any] = {
        "units_loaded": len(units),
        "rows_valid": len(valid_rows),
        "rows_dropped": len(dropped),
        "dropped_details": dropped,
        "dry_run": dry_run,
    }

    if dry_run:
        return result

    added_json = store_chunks_jsonl(valid_rows, force=False)
    chroma_ok = store_chunks_chroma(valid_rows, force=False)
    result.update({"chunks_added_jsonl": added_json, "chroma_upsert_ok": chroma_ok})
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--rebuild-bm25", action="store_true", help="Compatibility flag; BM25 is rebuilt from persisted chunks at query time.")
    parser.add_argument("--source")
    parser.add_argument(
        "--curated",
        metavar="PATH",
        help="Path to curated_candidates.json to ingest alongside PDF chunks.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate curated rows and report counts without writing to jsonl or Chroma.",
    )
    args = parser.parse_args()

    if args.curated:
        curated_path = Path(args.curated)
        if not curated_path.exists():
            print(f"ERROR: curated file not found: {curated_path}")
            return
        summary = ingest_curated(curated_path, dry_run=args.dry_run)
        label = "Curated dry-run summary" if args.dry_run else "Curated ingest summary"
        print(label)
        for k, v in summary.items():
            if k == "dropped_details":
                if v:
                    print(f"  dropped_details ({len(v)} items):")
                    for item in v[:20]:
                        print(f"    {item}")
                    if len(v) > 20:
                        print(f"    ... and {len(v)-20} more")
            else:
                print(f"  {k}: {v}")
        return

    summary = ingest(force=args.force, source=args.source)
    print("Ingestion summary")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
