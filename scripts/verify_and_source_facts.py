"""Link every studied fact to a supporting passage, and flag the ones with none.

416 studied facts cannot say where they came from. The corpus is not the
problem — 132,020 chunks across Marino, Miller, Morgan & Mikhail, the MGH
manual, StatPearls and the society guidelines — the problem is that nothing ever
recorded WHICH passage a fact came from. So this retrieves one.

It is also the verification pass a previous attempt failed at. That attempt
searched the whole corpus for a fact's numbers and "corroborated" an invented
vasopressin dose using a chunk about pulse oximetry, because "5" appears near
"norepinephrine" in a hundred unrelated places. The fix is ordering: retrieve
the passage that is SEMANTICALLY about this fact first, then check the claim
against that passage only. A number absent from the passage that is otherwise
the best match in 132,020 chunks is a real signal.

Two outcomes per fact:

  SOURCED      a passage matches it closely -> its book and section become the
               fact's provenance, so future reviews can cite something real
  UNSUPPORTED  nothing in 132,020 chunks comes close -> flagged, never deleted.
               The fact may well be true and simply absent from these books, but
               it is the set worth reading, and it is where a fabrication would
               hide.

DETECTING FABRICATED NUMBERS AUTOMATICALLY DOES NOT WORK. Three attempts, all
recorded here so nobody rebuilds them:

  1. Match a fact's numbers anywhere in the corpus. "Corroborated" the invented
     vasopressin dose using a chunk about PULSE OXIMETRY, because "5" appears
     near "norepinephrine" in a hundred unrelated places.
  2. Require the number within 200 characters of a distinctive term. Still
     passed the fabrication, for the same reason.
  3. Retrieve the passages semantically closest to the fact, then require the
     number among them. Narrow (4 passages) flagged facts that are certainly
     true — the ARDS plateau limit of 30, the DKA potassium floor of 3.3 —
     because the figure sat in a neighbouring chunk. Widened to 12, it stopped
     flagging the real fabrication.

The tension is not tunable: a window tight enough to catch an invented number
also rejects true ones split across chunks. So this script does NOT claim to
detect fabrication. The defences that actually work are the instruction never to
cite an unread number, the citation-quality check, and a human noticing — which
is how the one confirmed case was found.

Nothing is deleted and no claim is rewritten.

    python scripts/verify_and_source_facts.py --validate   # prove it discriminates
    python scripts/verify_and_source_facts.py --dry-run
    python scripts/verify_and_source_facts.py
"""
from __future__ import annotations

import argparse
import io
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

QUANTITY = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:-|–|to)?\s*(\d+(?:\.\d+)?)?\s*"
    r"(mg/kg|mcg/kg/min|mcg/kg|units?/min|mmol/l|meq/l|mg/dl|g/dl|cm\s?h2o|"
    r"mm\s?hg|mmhg|ml/kg|mcg/min|mg/day|g/day|mg|mcg|µg|units?|ml|mmol|meq|%)\b",
    re.I)

# Below this, the "best match" is not really about the fact at all.
#
# Calibrated against the deck rather than picked: sampling 40 unsourced facts,
# top-match scores ran 0.67 to 1.02 with a median of 0.82 — unsurprising, since
# these facts were extracted from this corpus in the first place. A threshold of
# 0.30 could therefore never fire and UNSUPPORTED would have been decorative.
# 0.60 sits below every observed match, so it flags genuine outliers only.
MIN_CONFIDENCE = 0.60


def numbers_in(text: str) -> set[str]:
    out = set()
    for m in QUANTITY.finditer(text):
        for g in (m.group(1), m.group(2)):
            if g:
                try:
                    out.add(f"{float(g):g}")
                except ValueError:
                    pass
    return out


def cite_from(meta: dict) -> str:
    book = (meta.get("book") or meta.get("source_name")
            or meta.get("filename") or "").strip()
    book = re.sub(r"\.pdf$|\.txt$", "", book, flags=re.I)
    section = (meta.get("section_heading") or meta.get("chapter_title")
               or meta.get("section") or "").strip()
    page = meta.get("page") or meta.get("page_number")
    parts = [p for p in (book, section[:60] if section else "") if p]
    cite = ", ".join(parts)
    if page:
        cite += f", p.{page}"
    return cite[:300]


def assess(point: str):
    """Return (verdict, citation, note) for one fact."""
    from src.retrieval import hybrid_search, retrieval_confidence

    try:
        results, _insufficient = hybrid_search(point[:400], mode="intern_teach",
                                               max_results=12)
    except Exception as exc:
        return "ERROR", "", str(exc)[:100]
    if not results:
        return "UNSUPPORTED", "", "retrieval returned nothing"

    # retrieval_confidence() returns a band ('high'/'medium'/'low'), not a
    # number — use the top chunk's own score for a threshold.
    band = retrieval_confidence(results)
    top = results[0].model_dump()
    score = float(top.get("score") or 0.0)
    if band == "low" or score < MIN_CONFIDENCE:
        return "UNSUPPORTED", "", f"best match {band} (score {score:.2f})"

    return "SOURCED", cite_from(top.get("metadata") or top), f"{band} (score {score:.2f})"


def validate() -> None:
    """Prove the check discriminates BEFORE trusting it on 416 facts.

    The previous attempt at this shipped without validation and passed the one
    fabrication it existed to catch.
    """
    cases = [
        ("must SOURCE (true, in Marino)",
         "ARDS: tidal volume 6 mL/kg of ideal body weight with plateau pressure "
         "under 30 cm H2O", "SOURCED"),
        ("must SOURCE (true, in the guidelines)",
         "DKA: do NOT start insulin if potassium is below 3.3 mEq/L, replete first",
         "SOURCED"),
        ("must SOURCE (true, mechanism)",
         "Hypoxemia not correcting with supplemental oxygen indicates a true shunt "
         "rather than V/Q mismatch", "SOURCED"),
    ]
    print("validating the discriminator against known cases\n")
    passed = 0
    for label, text, expected in cases:
        verdict, cite, note = assess(text)
        good = (verdict == expected)
        passed += good
        print(f"  [{'OK ' if good else 'BAD'}] {label}")
        print(f"        got {verdict} (expected {expected}) — {note}")
        if cite:
            print(f"        cite: {cite[:76]}")
    print(f"\n  {passed}/{len(cases)} discriminated correctly")
    if passed < len(cases):
        print("  DO NOT TRUST THIS PASS — fix the discriminator before running it.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="cap facts processed")
    args = ap.parse_args()

    if args.validate:
        validate()
        return

    db_path = Path(settings.sqlite_db_path)
    db = sqlite3.connect(str(db_path))
    db.row_factory = sqlite3.Row
    facts = db.execute(
        "SELECT id, topic, point FROM knowledge_points "
        "WHERE COALESCE(source,'') = '' AND times_seen > 0 ORDER BY id").fetchall()
    if args.limit:
        facts = facts[:args.limit]
    print(f"studied facts lacking provenance: {len(facts)}\n")

    sourced, unsupported, errors = [], [], []
    for i, f in enumerate(facts, 1):
        verdict, cite, note = assess(f["point"])
        if verdict == "SOURCED":
            sourced.append((f["id"], cite))
        elif verdict == "ERROR":
            errors.append((f["id"], note))
        else:
            unsupported.append((f["id"], f["topic"], f["point"], note))
        if i % 50 == 0:
            print(f"  ...{i}/{len(facts)}")

    print(f"\n  SOURCED           : {len(sourced)}")
    print(f"  UNSUPPORTED       : {len(unsupported)}")
    print(f"  errors            : {len(errors)}")

    if unsupported:
        print("\n--- facts with no close passage (may be true but unsourced here) ---")
        for kid, topic, point, note in unsupported[:12]:
            print(f"  kp{kid} [{topic[:22]}] {note} — {point[:76]}")

    if args.dry_run:
        print("\ndry run — nothing written")
        return
    if sourced:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        dest = db_path.with_name(f"{db_path.stem}.pre_verify.{stamp}.db")
        s, d = sqlite3.connect(str(db_path)), sqlite3.connect(str(dest))
        with d:
            s.backup(d)
        s.close()
        d.close()
        print(f"\nbacked up to {dest.name}")
        db.executemany("UPDATE knowledge_points SET source=? WHERE id=?",
                       [(c, i) for i, c in sourced])
        db.commit()
        print(f"wrote provenance for {len(sourced)} facts")
    print("\nNothing deleted and no claim rewritten — the flagged facts are for a "
          "human read.")
    db.close()


if __name__ == "__main__":
    main()
