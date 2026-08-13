"""Pre-compute VoiceLesson JSONs per (unit_id, phase) at curriculum-build time.

The session_runner can then serve `/next_lesson` as a dict lookup against
this cache instead of running hybrid_search per call. Latency drops from
~600 ms (post-tokenization-fix) to <20 ms.

The cache is rebuilt by `python -m src.lesson_cache`. Stored at
`storage/curriculum/lesson_cache.json` as a single dict keyed by
"<unit_id>::<phase>". Voice fields are pre-trimmed; relevance hooks are
already band-aware via `voice_shaper.shape_lesson`.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .config import settings
from .curriculum import CurriculumUnit, _band_for_unit, load_curriculum
from .pedagogy import SESSION_STRUCTURE
from .retrieval import hybrid_search
from .voice_shaper import shape_lesson


def cache_path() -> Path:
    return Path(settings.chroma_dir).parent / "curriculum" / "lesson_cache.json"


def _retrieval_mode_for(unit: CurriculumUnit) -> str:
    band = _band_for_unit(unit)
    if band == "icu":
        return "ICU_teach"
    if band == "anesthesia":
        return "anesthesia_boards"
    return "intern_teach"


def _retrieve(unit: CurriculumUnit, max_results: int = 3) -> list:
    """Use the unit's own fact_chunk_ids — direct lookup, no retrieval call.

    Units are built from the fact corpus and already know which chunks belong
    to them. Skipping hybrid_search here turns lesson-cache build from
    ~25 minutes to ~5 seconds for the whole curriculum.
    """
    from .retrieval import _term_index
    from .schemas import SourceChunk

    if not unit.fact_chunk_ids:
        # No fact ids on the unit — fall back to a cheap topic search via index
        idx = _term_index()
        query_terms = set((unit.topic_tags[0] if unit.topic_tags else "").lower().split())
        if not query_terms:
            return []
        candidates: list[tuple[int, dict]] = []
        for row, doc_terms in idx:
            meta = row.get("metadata", {})
            if (meta.get("source_name") or meta.get("book", "")) != unit.book:
                continue
            if meta.get("chunk_type") == "fact":
                continue
            overlap = len(query_terms & doc_terms)
            if overlap > 0:
                candidates.append((overlap, row))
        candidates.sort(key=lambda x: -x[0])
        return _rows_to_sourcechunks(candidates[:max_results])

    # Direct lookup by fact_chunk_id
    idx = _term_index()
    by_id = {}
    for row, _ in idx:
        meta = row.get("metadata", {})
        cid = meta.get("chunk_id") or row.get("id")
        if cid:
            by_id[cid] = row
    rows: list[tuple[int, dict]] = []
    for fact_id in unit.fact_chunk_ids[:max_results * 3]:  # take a few extras to filter
        r = by_id.get(fact_id)
        if r is not None:
            rows.append((1, r))
        if len(rows) >= max_results:
            break
    return _rows_to_sourcechunks(rows)


def _rows_to_sourcechunks(rows: list[tuple[int, dict]]):
    from .schemas import SourceChunk

    out = []
    for _score, row in rows:
        meta = row.get("metadata", {})
        text = (row.get("text") or meta.get("fact_text") or "")[:1000]
        out.append(
            SourceChunk(
                text=text,
                excerpt=text,
                book=meta.get("source_name") or meta.get("book", ""),
                source_name=meta.get("source_name") or meta.get("book", ""),
                source=meta.get("source_name") or meta.get("book", ""),
                library=meta.get("library", ""),
                training_phase=meta.get("training_phase", ""),
                clinical_context=meta.get("clinical_context", ""),
                filename=meta.get("filename", ""),
                page=meta.get("page"),
                section=meta.get("section", ""),
                topic_tags=[t for t in (meta.get("topic_tags") or "").split(",") if t],
                score=0.0,
                retrieval_method="curriculum",
                vector_score=0.0,
                bm25_score=0.0,
                reranker_score=None,
                chunk_id=meta.get("chunk_id", row.get("id", "")),
            )
        )
    return out


def _infer_cloze_type(question: str) -> str:
    """Cheap mask-type inference from the cloze question prompt."""
    q = (question or "").lower()
    if "what dose" in q:
        return "dose"
    if "what drug" in q:
        return "drug"
    if "what condition" in q:
        return "condition"
    if "abbreviation" in q or "term fits" in q:
        return "label"
    return "free"


def build_cache(progress_every: int = 100) -> dict[str, Any]:
    """Build lesson cache, with distributed-practice enforcement: within each
    unit's 5-phase block, no two consecutive phases use the same cloze type.
    If the next phase would repeat the prior cloze type, bump cloze_seed
    until it varies (or we exhaust the pool)."""
    units = load_curriculum()
    if not units:
        raise SystemExit("No curriculum loaded; run `python -m src.curriculum` first.")
    out: dict[str, dict] = {}
    for i, unit in enumerate(units):
        sources = _retrieve(unit)
        prev_type: str | None = None
        for phase_idx, phase in enumerate(SESSION_STRUCTURE):
            # Try increasing cloze_seed offsets to find a different cloze type
            # than the previous phase used.
            chosen_lesson = None
            for bump in range(8):
                lesson = shape_lesson(
                    unit=unit, sources=sources, phase=phase, cloze_seed=phase_idx + bump,
                )
                this_type = _infer_cloze_type(lesson.question)
                if this_type != prev_type or this_type == "free":
                    chosen_lesson = lesson
                    prev_type = this_type
                    break
            if chosen_lesson is None:
                chosen_lesson = shape_lesson(unit=unit, sources=sources, phase=phase, cloze_seed=phase_idx)
                prev_type = _infer_cloze_type(chosen_lesson.question)
            key = f"{unit.unit_id}::{phase}"
            out[key] = chosen_lesson.model_dump()
        if (i + 1) % progress_every == 0:
            print(f"cached {i + 1}/{len(units)} units", flush=True)
    path = cache_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"version": "1", "n_units": len(units), "n_lessons": len(out), "lessons": out}
    path.write_text(json.dumps(payload), encoding="utf-8")
    return {"n_units": len(units), "n_lessons": len(out), "path": str(path)}


_LOADED: dict | None = None


def _ensure_loaded() -> dict[str, dict]:
    global _LOADED
    if _LOADED is not None:
        return _LOADED
    path = cache_path()
    if not path.exists():
        _LOADED = {}
        return _LOADED
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        _LOADED = data.get("lessons", {})
    except Exception:
        _LOADED = {}
    return _LOADED


def get_cached(unit_id: str, phase: str) -> dict | None:
    return _ensure_loaded().get(f"{unit_id}::{phase}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", type=int, default=100)
    args = parser.parse_args()
    summary = build_cache(progress_every=args.progress)
    print("lesson cache built:")
    for k, v in summary.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
