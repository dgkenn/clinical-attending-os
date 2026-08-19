"""Give existing facts a citable source.

`knowledge_points` never recorded provenance. So when the tutor served a stored
fact for review it had nothing to cite, and honestly wrote "<Topic> knowledge
point bank" — which reads as a rubber stamp but was an accurate description of
the data available to it. 11 of 17 citations in one session looked like laziness
and were actually a missing column. Blaming the tutor would have fixed nothing.

Going forward `submit_answer` passes `grounded_in` down as the fact's source.
This backfills what can be recovered for facts already studied, in descending
order of confidence:

  1. The attempt that created it. Facts are written in the same call that logs
     the answer, so an attempt on the same topic within a couple of minutes of
     the fact's creation, carrying a real citation, is that fact's source.
  2. The catalog entry it came from, matched on exact answer or stem text,
     which carries a `source` array from ingestion.
  3. Nothing — left empty. An empty source is honest; a guessed one recreates
     the problem this exists to solve, since an unverifiable citation is what
     let an invented vasopressor threshold look sourced.

Self-referential citations ("<Topic> knowledge point bank") are NOT copied
forward — they are the symptom.

    python scripts/backfill_fact_sources.py --dry-run
    python scripts/backfill_fact_sources.py
"""
from __future__ import annotations

import argparse
import io
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402
from src.answer_evidence import citation_quality  # noqa: E402


def _readable_citation(raw: str) -> str:
    """Render a catalog `source` as something a tutor can say out loud.

    The field holds JSON in several shapes across ingestion vintages: a plain
    string, a list of strings, or a list of {"book", "page"} objects. Storing
    the raw JSON would put `[{"book": "MGH Housestaff Manual", "page": 66}]`
    into a citation, which is not a citation.
    """
    if not raw:
        return ""
    try:
        parsed = json.loads(raw)
    except (ValueError, TypeError):
        return str(raw).strip()[:300]

    def one(item) -> str:
        if isinstance(item, dict):
            book = str(item.get("book") or item.get("source") or item.get("title") or "").strip()
            page = item.get("page") or item.get("p")
            return f"{book}, p.{page}" if book and page else book or str(item)
        return str(item).strip()

    if isinstance(parsed, list):
        parts = [p for p in (one(i) for i in parsed) if p]
        return "; ".join(parts)[:300]
    return one(parsed)[:300]


def backup(db_path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = db_path.with_name(f"{db_path.stem}.pre_srcfill.{stamp}.db")
    src, dst = sqlite3.connect(str(db_path)), sqlite3.connect(str(dest))
    with dst:
        src.backup(dst)
    src.close()
    dst.close()
    return dest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    db_path = Path(settings.sqlite_db_path)
    db = sqlite3.connect(str(db_path))
    db.row_factory = sqlite3.Row

    facts = db.execute(
        "SELECT id, topic, point, created_at FROM knowledge_points "
        "WHERE COALESCE(source,'') = ''").fetchall()
    print(f"facts without a source: {len(facts)}\n")

    from_attempt: list[tuple[int, str]] = []
    from_catalog: list[tuple[int, str]] = []
    unknown = 0

    for f in facts:
        # 1. The attempt that created it.
        row = db.execute(
            """SELECT grounded_in FROM question_attempts
                WHERE topic = ? AND COALESCE(grounded_in,'') != ''
                  AND abs(julianday(date) - julianday(?)) * 86400 < 180
                ORDER BY abs(julianday(date) - julianday(?)) LIMIT 1""",
            (f["topic"], f["created_at"], f["created_at"])).fetchone()
        if row and citation_quality(row["grounded_in"])[0] == "real":
            from_attempt.append((f["id"], row["grounded_in"]))
            continue

        # 2. The catalog entry, matched on exact text.
        row = db.execute(
            "SELECT source FROM kp_catalog WHERE answer = ? OR stem = ? LIMIT 1",
            (f["point"], f["point"])).fetchone()
        if row and (row["source"] or "").strip():
            cite = _readable_citation(row["source"])
            if cite.strip():
                from_catalog.append((f["id"], cite.strip()[:300]))
                continue
        unknown += 1

    print(f"  recoverable from the creating attempt : {len(from_attempt)}")
    print(f"  recoverable from the catalog entry    : {len(from_catalog)}")
    print(f"  left empty (honest, not guessed)      : {unknown}")

    for kid, cite in (from_attempt[:5] + from_catalog[:5]):
        row = db.execute("SELECT point FROM knowledge_points WHERE id=?", (kid,)).fetchone()
        print(f"\n  kp{kid}: {cite[:70]}")
        print(f"      {row['point'][:78]}")

    if args.dry_run:
        print("\ndry run — nothing written")
        return
    if not (from_attempt or from_catalog):
        print("\nnothing to backfill")
        return

    dest = backup(db_path)
    print(f"\nbacked up to {dest.name}")
    db.executemany("UPDATE knowledge_points SET source=? WHERE id=?",
                   [(c, i) for i, c in from_attempt + from_catalog])
    db.commit()
    total = db.execute(
        "SELECT COUNT(*) FROM knowledge_points WHERE COALESCE(source,'') != ''").fetchone()[0]
    studied = db.execute(
        "SELECT COUNT(*) FROM knowledge_points WHERE times_seen > 0").fetchone()[0]
    print(f"backfilled {len(from_attempt) + len(from_catalog)}; "
          f"{total} facts now carry a source ({studied} studied facts total)")
    db.close()


if __name__ == "__main__":
    main()
