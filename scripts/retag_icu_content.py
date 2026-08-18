"""Flag catalog topics that are genuinely critical care but filed elsewhere.

Found while answering "is the ICU knowledge base deep enough for an
anesthesiologist rotating through the unit?". The two ICU domains hold 346
facts across ~72 topics — about 4.8 facts per topic, a survey rather than
depth — while several bread-and-butter ICU subjects turned out to exist in the
catalog but OUTSIDE those domains, so an ICU-weighted session could never
surface them: RASS/CAM-ICU sedation scoring, CRRT, ICP and cerebral perfusion
management, tracheostomy, status epilepticus, bedside ultrasound.

`is_critical_care` is the right lever rather than rewriting `domain`. These
items legitimately belong to neurology, nephrology and airway as well —
status epilepticus IS a neurology topic — and the topic selector already treats
critical-care items as jumping the queue regardless of discipline weight.
Flagging adds them to ICU sessions without removing them from anywhere.

SELECTED BY TOPIC, DELIBERATELY, NOT BY KEYWORD SWEEP. A keyword pass on
"intracranial pressure|ICP" matched 61 unflagged items, but reading them showed
most were intraoperative neuroanesthesia — awake craniotomy complications,
barbiturate pharmacology, patient positioning, MRI anesthesia, post-dural
puncture headache. Flagging those would have put OR content into ICU sessions,
which is precisely the wasted-question failure the maintainer says would make
him stop using the system. Three prior errors in this project came from exactly
this shortcut (a redundancy figure inflated to 29% by a keyword regex, and an
attempt-correlation heuristic that condemned genuinely studied facts), so the
list below is curated and each entry is defensible.

    python scripts/retag_icu_content.py --dry-run
    python scripts/retag_icu_content.py
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import settings  # noqa: E402

# Each topic here is content a TY intern turned anesthesiologist would actually
# use while covering an ICU. Grouped by why it qualifies.
ICU_TOPICS: dict[str, tuple[str, ...]] = {
    "neurocritical care — ICP/CPP management is unit work, not OR work": (
        "TBI: ICP Management & Multimodal Monitoring",
        "Cerebral Perfusion Pressure & Herniation Syndromes",
        "Postoperative Intracranial Hypertension & Re-operation",
        "Intracranial Pressure: Physiology & Monitoring",
        "Intracranial Hypertension: Medical Management",
    ),
    "renal support — RRT modality and timing decisions are made in the unit": (
        "AKI: Management and Renal Replacement Therapy Indications",
        "Dialysis: Hemodialysis Principles and Access",
    ),
    "hemodynamics — invasive monitoring is the ICU's core skill": (
        "Hemodynamic Monitoring — Invasive & Advanced",
        "Hemodynamic Monitoring - Invasive & Advanced",
    ),
    "acid-base — the daily interpretive task on a vented patient": (
        "Acid-base disorders",
        "Respiratory acid-base disorders",
        "Respiratory Acid-Base Disorders",
        "Mixed Acid-Base Disorders",
    ),
    "sedation, delirium and paralysis monitoring": (
        "Delirium prevention programs & hospital-acquired complications",
        "Neuromuscular monitoring",
        "Opioid Safety, Monitoring, and Naloxone",
    ),
    "transfusion — the unit transfuses and reacts to transfusion constantly": (
        "Transfusion medicine: red blood cell transfusion",
        "Transfusion reactions",
        "Platelet transfusion",
    ),
    "metabolic support": (
        "Glycemic Targets & Monitoring",
        "Nutrition, malnutrition & enteral/parenteral nutrition",
    ),
}

# Considered and REJECTED, recorded so the judgement is not re-litigated:
#   Electricity, Safety and Monitoring Principles  — OR equipment
#   Separation from CPB / DHCA                     — cardiac operating room
#   Ultrasound fundamentals for regional anesthesia— nerve blocks, not POCUS
#   Intraoperative Neurophysiological Monitoring   — intraoperative by name
#   Intracranial Aneurysm: Surgical Clipping       — operative management
#   Dialysis: Peritoneal Dialysis                  — outpatient modality
#   Maternal cardiac arrest / perimortem cesarean  — obstetric, own pathway
#   Nutritional assessment and optimization        — preoperative clinic
#   Chemotherapy toxicities and monitoring         — oncology service


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    db = sqlite3.connect(str(settings.sqlite_db_path))
    db.row_factory = sqlite3.Row
    total = 0
    for rationale, topics in ICU_TOPICS.items():
        print(f"\n{rationale}")
        for t in topics:
            row = db.execute(
                "SELECT COUNT(*) n, SUM(is_critical_care) cc FROM kp_catalog WHERE topic = ?",
                (t,)).fetchone()
            if not row["n"]:
                print(f"   --  {t}  (no such topic — skipped)")
                continue
            pending = row["n"] - (row["cc"] or 0)
            total += pending
            print(f"   {pending:>3} of {row['n']:>3} to flag   {t}")
            if not args.dry_run and pending:
                db.execute(
                    "UPDATE kp_catalog SET is_critical_care = 1 WHERE topic = ?", (t,))
    if args.dry_run:
        print(f"\ndry run — {total} facts would be flagged critical-care")
        return
    db.commit()

    # Persist to data/curriculum_blueprint.json, which is where this value
    # actually originates.
    #
    # The chain matters and cost a full silent revert to work out:
    #   curriculum_blueprint.json -> seed_curriculum() -> curriculum table
    #     -> seed_kp_catalog() reads is_critical_care from THE CURRICULUM ROW
    #        (student_model.py: `is_critical_care = int(curr["is_critical_care"])`)
    #        for any topic present there, ignoring the catalog entry entirely
    #     -> kp_catalog
    #
    # Both seeders run on every MCP server start, so a database-only re-tag is
    # undone by the next restart — which is what happened to the first run of
    # this script, along with 131 currency corrections. Writing the flag into
    # kp_catalog.json does NOT help either, because the curriculum row wins.
    # seed_curriculum honours an explicit is_critical_care when the blueprint
    # supplies one, so this is the durable place to set it.
    import json as _json
    blueprint = ROOT / "data" / "curriculum_blueprint.json"
    if not blueprint.exists():
        print("WARNING: curriculum_blueprint.json missing — flags will NOT survive a restart")
        return
    wanted = {t for topics in ICU_TOPICS.values() for t in topics}
    items = _json.loads(blueprint.read_text(encoding="utf-8"))
    n = 0
    for entry in items:
        if entry.get("topic") in wanted and not entry.get("is_critical_care"):
            entry["is_critical_care"] = 1
            n += 1
    blueprint.write_text(_json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"set is_critical_care on {n} blueprint topics (survives restart)")
    after = db.execute(
        "SELECT COUNT(*) FROM kp_catalog WHERE is_critical_care = 1").fetchone()[0]
    print(f"\nflagged {total} additional facts; {after} now critical-care")
    db.close()


if __name__ == "__main__":
    main()
