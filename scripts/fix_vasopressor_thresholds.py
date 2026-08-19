"""Remove fabricated vasopressor dose thresholds attributed to Surviving Sepsis.

The maintainer caught this himself, mid-session: the tutor had taught specific
norepinephrine cutoffs — "add vasopressin at 5-15 mcg/min", "epinephrine beyond
25 mcg/min" — and cited Surviving Sepsis 2021 for them. He checked the source.
No such thresholds exist.

What SSC 2021 actually says, verified against the corpus text:

  "For adults with septic shock on norepinephrine with inadequate mean arterial
   pressure levels, we suggest adding vasopressin instead of escalating the dose
   of norepinephrine"                                    <- no dose cutoff at all

and, separately, in narrative rather than as a recommendation:

  "In our practice, vasopressin is usually started when the dose of
   norepinephrine is in the range of 0.25-0.5 μg/kg/min"  <- WEIGHT-BASED

0.25-0.5 mcg/kg/min is roughly 17-35 mcg/min in a 70 kg adult, so "5-15 mcg/min"
is not a rounding of it — it is about four times too low, and would have him
reaching for a second agent far earlier than any source supports.

This is the failure the `grounded_in` field exists to prevent, and it did the
opposite: the session cited "Surviving Sepsis Campaign 2021, p.7, p.30" for a
number the guideline does not contain, which lent the invention authority. A
citation that is not checked is worse than no citation.

The same fact had also been carded four separate times (kp300, 575, 599, 638)
with different wordings and different invented numbers, so the error was being
drilled from four directions at once.

Writes the catalog JSON as well as the database — a database-only edit is
reverted by the next server restart, which has already happened once.

    python scripts/fix_vasopressor_thresholds.py --dry-run
    python scripts/fix_vasopressor_thresholds.py
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

CATALOG_JSON = ROOT / "data" / "kp_catalog.json"

CANONICAL = (
    "Septic shock on norepinephrine with inadequate MAP: ADD vasopressin rather "
    "than escalating norepinephrine (SSC 2021). The guideline sets NO dose "
    "threshold for when to add it — its narrative notes vasopressin is usually "
    "started around norepinephrine 0.25-0.5 mcg/kg/min (weight-based; roughly "
    "17-35 mcg/min in a 70 kg adult). Vasopressin runs at a FIXED 0.03-0.04 "
    "units/min, never titrated. Epinephrine is third-line, after norepinephrine "
    "plus vasopressin."
)

# Studied facts carrying an invented threshold. kp440 already holds the correct
# text and is the merge target.
KEEP = 440
RETIRE = [300, 301, 575, 599, 638]

CATALOG_FIXES = {
    "sepsis-septic-shock-2": CANONICAL,
    "septic-shock-2": CANONICAL,
}


def backup(db_path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = db_path.with_name(f"{db_path.stem}.pre_pressorfix.{stamp}.db")
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

    keep = db.execute("SELECT * FROM knowledge_points WHERE id=?", (KEEP,)).fetchone()
    if keep is None:
        print(f"canonical fact kp{KEEP} not found — aborting")
        return

    retiring = db.execute(
        f"SELECT * FROM knowledge_points WHERE id IN ({','.join('?'*len(RETIRE))})",
        RETIRE).fetchall()
    print(f"canonical: kp{KEEP}\n  {keep['point'][:110]}\n")
    print(f"retiring {len(retiring)} duplicates carrying invented thresholds:")
    seen = keep["times_seen"]
    correct = keep["times_correct"]
    for r in retiring:
        print(f"  kp{r['id']} ({r['times_correct']}/{r['times_seen']}): {r['point'][:92]}")
        seen += r["times_seen"]
        correct += r["times_correct"]
    print(f"\nmerged history -> {correct}/{seen} on kp{KEEP}")

    print(f"\ncatalog entries to correct: {len(CATALOG_FIXES)}")
    for kid in CATALOG_FIXES:
        row = db.execute("SELECT answer FROM kp_catalog WHERE id=?", (kid,)).fetchone()
        if row:
            print(f"  {kid}\n    OLD: {row['answer'][:100]}")

    if args.dry_run:
        print("\ndry run — nothing written")
        return

    dest = backup(db_path)
    print(f"\nbacked up to {dest.name}")
    now = datetime.now(timezone.utc).isoformat()

    # Merge the duplicates' history onto the canonical fact and retire them.
    # Due tomorrow rather than parked: he has been drilled on a wrong number
    # several times, so the corrected version needs to be taught, not shelved.
    db.execute(
        """UPDATE knowledge_points
              SET point=?, times_seen=?, times_correct=?, status='weak',
                  consecutive_correct=0, interval_days=1, fsrs_state=NULL,
                  mistake_type='superseded_guidance', evidence='',
                  next_review_date=date('now','localtime','+1 day'), updated_at=?
            WHERE id=?""",
        (CANONICAL, seen, correct, now, KEEP))
    db.executemany("DELETE FROM knowledge_points WHERE id=?", [(i,) for i in RETIRE])

    for kid, text in CATALOG_FIXES.items():
        db.execute("UPDATE kp_catalog SET answer=?, rationale='', last_currency_check=? "
                   "WHERE id=?", (text, now, kid))
    db.commit()

    if CATALOG_JSON.exists():
        items = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
        n = 0
        for entry in items:
            fix = CATALOG_FIXES.get(str(entry.get("id")))
            if fix:
                entry["answer"] = fix
                entry["rationale"] = ""
                n += 1
        CATALOG_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=1),
                                encoding="utf-8")
        print(f"wrote {n} corrections into data/kp_catalog.json (survives restart)")

    print(f"merged {len(retiring)} duplicates into kp{KEEP}; corrected "
          f"{len(CATALOG_FIXES)} catalog entries")
    db.close()


if __name__ == "__main__":
    main()
