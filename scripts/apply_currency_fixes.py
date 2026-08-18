"""Apply verified currency corrections to the fact corpus.

Reads the confirmed findings out of the currency-audit workflow journals and
rewrites the affected facts. Only CONFIRMED_OUTDATED verdicts are applied — each
one has already survived an adversarial Opus pass whose explicit instruction was
to REFUTE the flag and default to "actually fine". Flags that pass raised but
verification rejected are left alone, which is the point of the two-stage design:
a Sonnet sweep is a good net and a poor judge.

Two destinations:

  kp_catalog        the pool of things that COULD be asked. The corrected text
                    replaces `answer`; the `stem` (the question) is untouched,
                    because the question was rarely the thing that aged.
  knowledge_points  the ledger of what the maintainer has actually studied.
                    Corrections here matter most and are rarest: these facts are
                    on an active spaced-repetition schedule, so an expired one is
                    being rehearsed into long-term memory on a timer.

Every corrected fact is stamped `last_currency_check`, which is what makes the
doctor's staleness report meaningful and lets the next audit target only what
has gone unverified rather than re-reading 6,300 facts.

Backs up via the sqlite3 backup API (a filesystem copy of a WAL database omits
un-checkpointed frames — that mistake once appeared to "lose" 9 exposures).

    python scripts/apply_currency_fixes.py --dry-run
    python scripts/apply_currency_fixes.py
"""
from __future__ import annotations

import argparse
import io
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# Corrected clinical text is full of arrows, degree signs and micro symbols, and
# this console defaults to cp1252 — printing a diff crashed the whole run on a
# single "→". Replace rather than fail: a mangled character in a preview is a
# cosmetic problem, an aborted migration is not.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

WORKFLOW_DIR = (Path.home() / ".claude" / "projects" / "C--Users-jackk"
                / "f0761c86-1062-445f-9e12-a117cbd77719" / "subagents" / "workflows")


def load_confirmed() -> dict[str, dict]:
    """Collect CONFIRMED_OUTDATED verdicts from every audit run, newest wins."""
    out: dict[str, dict] = {}
    if not WORKFLOW_DIR.exists():
        return out
    for journal in sorted(WORKFLOW_DIR.glob("*/journal.jsonl")):
        for line in journal.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            result = rec.get("result")
            if not isinstance(result, dict):
                continue
            for v in result.get("results") or []:
                if (v.get("verdict") == "CONFIRMED_OUTDATED"
                        and v.get("id") and v.get("corrected_text")):
                    out[str(v["id"])] = v
    return out


CATALOG_JSON = ROOT / "data" / "kp_catalog.json"


def write_catalog_json(fixes: dict[str, str]) -> int:
    """Apply the corrections to data/kp_catalog.json as well as the database.

    THE JSON IS THE SOURCE OF TRUTH AND THE DATABASE IS NOT. seed_kp_catalog()
    runs on every MCP server start and does

        ON CONFLICT(id) DO UPDATE SET answer=excluded.answer,
                                      rationale=excluded.rationale,
                                      is_critical_care=excluded.is_critical_care, ...

    so a correction written only to the database is silently reverted by the
    next restart. This actually happened: all 131 currency corrections and 96
    ICU re-tags were wiped by a routine restart, while `volatility` and
    `last_currency_check` survived because they do not appear in that INSERT —
    leaving the corpus claiming "verified" over restored, dangerous text
    (idarucizumab gone again, airway-fire card back to "deliver 100% oxygen").
    A stamp that outlives the fix it certifies is worse than no stamp.

    Returns the number of JSON entries updated.
    """
    if not CATALOG_JSON.exists():
        print(f"WARNING: {CATALOG_JSON} missing — corrections will not survive a restart")
        return 0
    items = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    n = 0
    for entry in items:
        new = fixes.get(str(entry.get("id")))
        if new and entry.get("answer") != new:
            entry["answer"] = new
            # The rationale was written to justify the OLD answer and keeps
            # teaching it otherwise — see the DTI-reversal card, whose rationale
            # carried the error independently of its answer.
            entry["rationale"] = ""
            n += 1
    CATALOG_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=1),
                            encoding="utf-8")
    return n


def backup(db_path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = db_path.with_name(f"{db_path.stem}.pre_currency.{stamp}.db")
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

    confirmed = load_confirmed()
    print(f"confirmed-outdated facts with a replacement text: {len(confirmed)}\n")
    if not confirmed:
        return

    db_path = Path(settings.sqlite_db_path)
    db = sqlite3.connect(str(db_path))
    db.row_factory = sqlite3.Row
    cols = {r[1] for r in db.execute("PRAGMA table_info(kp_catalog)")}
    if "last_currency_check" not in cols and not args.dry_run:
        db.execute("ALTER TABLE kp_catalog ADD COLUMN last_currency_check TEXT")
        db.commit()

    now = datetime.now(timezone.utc).isoformat()
    cat_updates, kp_updates, missing = [], [], []

    for kid, v in sorted(confirmed.items()):
        sev = v.get("severity", "?")
        new = v["corrected_text"].strip()
        row = db.execute("SELECT topic, stem, answer FROM kp_catalog WHERE id=?",
                         (kid,)).fetchone()
        if row:
            cat_updates.append((kid, row["topic"], sev, row["answer"] or "", new))
            continue
        # Not in the catalog: the studied-deck batch carries knowledge_points
        # ids, which are integers rather than slugs.
        krow = None
        if kid.isdigit():
            krow = db.execute("SELECT id, topic, point FROM knowledge_points WHERE id=?",
                              (int(kid),)).fetchone()
        if krow:
            kp_updates.append((krow["id"], krow["topic"], sev, krow["point"], new))
        else:
            missing.append((kid, v.get("topic", "?")))

    print(f"--- kp_catalog (question pool): {len(cat_updates)} ---")
    for kid, topic, sev, old, new in cat_updates:
        print(f"\n  [{sev}] {topic[:60]}  ({kid})")
        print(f"    OLD: {old[:150]}")
        print(f"    NEW: {new[:150]}")

    print(f"\n--- knowledge_points (ACTIVELY DRILLED): {len(kp_updates)} ---")
    for kid, topic, sev, old, new in kp_updates:
        print(f"\n  [{sev}] {topic[:60]}  (kp {kid})")
        print(f"    OLD: {old[:200]}")
        print(f"    NEW: {new[:200]}")

    if missing:
        print(f"\n--- NOT FOUND in either table: {len(missing)} ---")
        for kid, topic in missing:
            print(f"    {kid}  ({topic[:60]})")

    if args.dry_run:
        print("\ndry run — nothing written")
        return

    dest = backup(db_path)
    print(f"\nbacked up to {dest.name}")
    # Clear `rationale` on every corrected fact. It was written to justify the
    # OLD answer, so it independently teaches the superseded claim even after
    # the answer is fixed. The DTI-reversal card is the proof: its answer said
    # "no specific antidotes for DTIs" and its rationale said "DTIs lack
    # approved reversal agents and must be cleared renally or hepatically" —
    # correcting only the answer would have left the contradiction in place,
    # with idarucizumab still absent from what the card actually teaches.
    # A blank rationale loses some value; a stale one is actively wrong.
    db.executemany(
        "UPDATE kp_catalog SET answer=?, rationale='', last_currency_check=? WHERE id=?",
        [(new, now, kid) for kid, _t, _s, _o, new in cat_updates])
    # A corrected studied fact must be RE-TAUGHT, not left sitting on whatever
    # long interval it earned while it was wrong. Reset to weak and due
    # tomorrow, and clear the FSRS state that accrued under the old text.
    db.executemany(
        """UPDATE knowledge_points
              SET point=?, status='weak', consecutive_correct=0, interval_days=1,
                  fsrs_state=NULL, mistake_type='superseded_guidance',
                  next_review_date=date('now','localtime','+1 day'),
                  evidence='', updated_at=?
            WHERE id=?""",
        [(new, now, kid) for kid, _t, _s, _o, new in kp_updates])
    db.commit()
    # Without this the next server restart reverts everything above.
    written = write_catalog_json({kid: new for kid, _t, _s, _o, new in cat_updates})
    print(f"updated {len(cat_updates)} catalog facts, {len(kp_updates)} studied facts")
    print(f"wrote {written} corrections into data/kp_catalog.json (survives restart)")
    if kp_updates:
        print("studied facts were reset to weak and due tomorrow so the corrected "
              "version gets taught rather than inheriting the old schedule")
    db.close()


if __name__ == "__main__":
    main()
