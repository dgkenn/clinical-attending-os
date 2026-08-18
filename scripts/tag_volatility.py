"""Tag every catalog fact with how fast it goes stale, and when it was last checked.

The maintainer's point, in his words: "something to watch for is management as
these can change drastically with new studies." He is right, and a one-off audit
does not answer it — the audit is stale the moment a trial reads out. What the
corpus needs is a standing property per fact and a way to see what has gone
unchecked.

Facts do not age at one rate:

  LOW      anatomy, physiology, mechanism, pharmacodynamics, definitions.
           The Frank-Starling relationship and why PEEP recruits alveoli are
           the same in 2026 as in 1996. These essentially never need rechecking.

  MEDIUM   diagnostic criteria, scoring systems, classification schemes.
           These move, but on the scale of a decade (Berlin replaced AECC;
           Sepsis-3 replaced SIRS) and usually with warning.

  HIGH     management, therapy, drug choice, dosing, thresholds, targets,
           indications, prophylaxis. This is the band the maintainer named, and
           it is where every superseded item found so far has lived: dopamine
           first-line, tight glycemic control, Rivers EGDT, hydroxyethyl starch.
           A single trial can invert these overnight.

Combined with `last_currency_check`, this makes staleness measurable rather than
remembered: doctor.py can report "N high-volatility facts unchecked in 12
months", and the next audit targets exactly that slice instead of re-reading
6,300 facts, most of which cannot have changed.

    python scripts/tag_volatility.py --dry-run
    python scripts/tag_volatility.py
    python scripts/tag_volatility.py --stale-report
"""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

# Recheck cadence per band. HIGH is annual because that is roughly the interval
# at which a practice-changing trial plus guideline update lands in any given
# area; LOW is effectively never, and is listed only so the arithmetic is
# explicit rather than implied.
RECHECK_MONTHS = {"high": 12, "medium": 36, "low": 120}

_HIGH = re.compile(
    r"\b(manage|management|treat|treatment|therapy|therapeutic|first[- ]line|"
    r"drug of choice|dose|dosing|dosage|administer|give|start|initiate|infusion|"
    r"target|threshold|goal|titrate|indication|indicated|contraindicat|"
    r"prophylax|prevent|regimen|protocol|recommend|guideline|standard of care|"
    r"transfus|resuscitat|reversal|antidote|antibiotic|steroid|anticoagul)\b", re.I)
_MEDIUM = re.compile(
    r"\b(criteri|diagnos|classif|stage|staging|grade|grading|score|scoring|"
    r"definition|defined as|workup|work[- ]up|evaluat|screen|screening|"
    r"differential|rule out|sensitivit|specificit)\b", re.I)
_LOW = re.compile(
    r"\b(anatomy|anatomic|physiolog|mechanism|pathophysiolog|receptor|innervat|"
    r"pharmacokinetic|pharmacodynamic|metaboli[sz]|half[- ]life|why does|"
    r"explain why|structure|blood supply|nerve supply)\b", re.I)


def classify(text: str) -> str:
    """HIGH wins ties deliberately.

    A fact that mixes mechanism and management ("PEEP recruits alveoli, titrate
    in 2-4 cm increments") contains a number that can move, so it belongs in the
    band that gets rechecked. Under-calling volatility is the expensive error:
    it leaves an expired number sitting in the deck unexamined. Over-calling
    only costs an unnecessary re-read.
    """
    if _HIGH.search(text):
        return "high"
    if _MEDIUM.search(text):
        return "medium"
    if _LOW.search(text):
        return "low"
    return "medium"


def _ensure_columns(db: sqlite3.Connection) -> None:
    cols = {r[1] for r in db.execute("PRAGMA table_info(kp_catalog)")}
    if "volatility" not in cols:
        db.execute("ALTER TABLE kp_catalog ADD COLUMN volatility TEXT DEFAULT ''")
    if "last_currency_check" not in cols:
        db.execute("ALTER TABLE kp_catalog ADD COLUMN last_currency_check TEXT")
    db.commit()


def stale_report(db: sqlite3.Connection) -> None:
    now = datetime.now(timezone.utc)
    print("volatility band   facts   unchecked   overdue for recheck")
    print("-" * 62)
    for band in ("high", "medium", "low"):
        cutoff = (now - timedelta(days=RECHECK_MONTHS[band] * 30)).isoformat()
        n = db.execute("SELECT COUNT(*) FROM kp_catalog WHERE volatility=?",
                       (band,)).fetchone()[0]
        never = db.execute(
            "SELECT COUNT(*) FROM kp_catalog WHERE volatility=? AND last_currency_check IS NULL",
            (band,)).fetchone()[0]
        overdue = db.execute(
            "SELECT COUNT(*) FROM kp_catalog WHERE volatility=? AND "
            "(last_currency_check IS NULL OR last_currency_check < ?)",
            (band, cutoff)).fetchone()[0]
        print(f"  {band:<8} {n:>12} {never:>11} {overdue:>21}")
    print("\nrecheck cadence: " +
          ", ".join(f"{b}={m}mo" for b, m in RECHECK_MONTHS.items()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stale-report", action="store_true")
    ap.add_argument("--mark-checked", metavar="IDFILE",
                    help="file of fact ids (one per line) just audited; stamps them")
    args = ap.parse_args()

    db = sqlite3.connect(str(settings.sqlite_db_path))
    _ensure_columns(db)

    if args.stale_report:
        stale_report(db)
        return

    if args.mark_checked:
        ids = [l.strip() for l in Path(args.mark_checked).read_text().splitlines() if l.strip()]
        now = datetime.now(timezone.utc).isoformat()
        db.executemany("UPDATE kp_catalog SET last_currency_check=? WHERE id=?",
                       [(now, i) for i in ids])
        db.commit()
        print(f"stamped {len(ids)} facts as currency-checked at {now[:10]}")
        return

    rows = db.execute("SELECT id, stem, answer FROM kp_catalog").fetchall()
    counts = {"high": 0, "medium": 0, "low": 0}
    updates = []
    for kid, stem, answer in rows:
        band = classify(f"{stem or ''} {answer or ''}")
        counts[band] += 1
        updates.append((band, kid))
    for band in ("high", "medium", "low"):
        print(f"  {band:<7} {counts[band]:>5}")
    if args.dry_run:
        print("\ndry run — nothing written")
        return
    db.executemany("UPDATE kp_catalog SET volatility=? WHERE id=?", updates)
    db.commit()
    print(f"\ntagged {len(updates)} facts\n")
    stale_report(db)
    db.close()


if __name__ == "__main__":
    main()
