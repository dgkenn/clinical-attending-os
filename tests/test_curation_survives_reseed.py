"""Curated edits must survive a server restart.

The failure this guards against was silent and total. 131 verified currency
corrections and 96 ICU re-tags were applied to the database, checked, reported
as done — and then wiped by a routine restart. `seed_kp_catalog()` and
`seed_curriculum()` run on every MCP server start and overwrite the seeded
columns from the JSON files under data/:

    ON CONFLICT(id) DO UPDATE SET answer=excluded.answer,
                                  rationale=excluded.rationale,
                                  is_critical_care=excluded.is_critical_care, ...

Worse than losing the fixes: `volatility` and `last_currency_check` are NOT in
that statement, so they survived. The corpus was left asserting "currency
verified" over restored, dangerous text — the DTI card back to "no specific
antidotes for DTIs" and the airway-fire card back to "deliver 100% oxygen to
clear any flames", both stamped as checked. A stamp that outlives the fix it
certifies is worse than no stamp at all.

And the two values do not even come from the same file. `is_critical_care` is
read from the CURRICULUM row for any topic present there, so writing it into
kp_catalog.json changes nothing; it has to go into curriculum_blueprint.json.

So: the JSON files are the source of truth, the database is a cache, and any
script that curates content must write the JSON.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "kp_catalog.json"
BLUEPRINT = ROOT / "data" / "curriculum_blueprint.json"

pytestmark = pytest.mark.skipif(
    not CATALOG.exists() or not BLUEPRINT.exists(), reason="seed data not present")


def _catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def _reseed():
    """Exactly what an MCP server start does, in the same order."""
    from src.student_model import seed_curriculum, seed_kp_catalog
    seed_curriculum(str(BLUEPRINT))
    seed_kp_catalog(str(CATALOG))


class TestCorrectionsArePersistedToJson:
    """Spot-check dangerous corrections in the file that actually gets seeded."""

    @pytest.mark.parametrize("kp_id,marker", [
        ("anticoag-mech-3", "idarucizumab"),      # "no antidotes for DTIs" was false
        ("airway_fires-2", "turn off"),            # had said "deliver 100% oxygen"
        ("thyroid-storm-04", "thionamide"),        # omitted blocking hormone synthesis
        ("cardiac-arrest-3", "32-37.5"),           # mandated 32-34C, pre-TTM2
        ("bls-chain-of-survival-3", "5th ICS"),    # 2nd ICS misses the pleura
    ])
    def test_the_correction_is_in_the_seed_file(self, kp_id, marker):
        entry = next((e for e in _catalog() if e.get("id") == kp_id), None)
        assert entry is not None, f"{kp_id} missing from the catalog"
        assert marker.lower() in str(entry.get("answer", "")).lower(), (
            f"{kp_id} was corrected in the DB only — a restart will revert it")

    def test_a_corrected_fact_has_no_stale_rationale(self):
        """The rationale justified the OLD answer and teaches it independently:
        the DTI card's answer said "no specific antidotes" and its rationale
        said "DTIs lack approved reversal agents"."""
        entry = next(e for e in _catalog() if e.get("id") == "anticoag-mech-3")
        assert not str(entry.get("rationale", "")).strip()


class TestReseedDoesNotRevertCuration:
    def test_corrections_survive_a_simulated_restart(self):
        from src.student_model import conn

        _reseed()
        with conn() as db:
            rows = {r["id"]: r["answer"] for r in db.execute(
                "SELECT id, answer FROM kp_catalog WHERE id IN "
                "('anticoag-mech-3','airway_fires-2','thyroid-storm-04')")}
        assert "idarucizumab" in rows["anticoag-mech-3"].lower()
        assert "turn off" in rows["airway_fires-2"].lower()
        assert "thionamide" in rows["thyroid-storm-04"].lower()

    def test_icu_retag_survives_a_simulated_restart(self):
        """is_critical_care comes from the CURRICULUM row, not the catalog entry,
        so this only holds if the blueprint carries the flag."""
        from src.student_model import conn

        _reseed()
        with conn() as db:
            for topic in ("TBI: ICP Management & Multimodal Monitoring",
                          "Acid-base disorders", "Transfusion reactions"):
                row = db.execute(
                    "SELECT COUNT(*) n, SUM(is_critical_care) cc FROM kp_catalog "
                    "WHERE topic = ?", (topic,)).fetchone()
                if not row["n"]:
                    continue
                assert row["cc"] == row["n"], (
                    f"{topic}: re-tag reverted on reseed ({row['cc']}/{row['n']})")

    def test_the_blueprint_carries_the_flag_not_just_the_catalog(self):
        items = json.loads(BLUEPRINT.read_text(encoding="utf-8"))
        flagged = {e["topic"] for e in items if e.get("is_critical_care")}
        assert "TBI: ICP Management & Multimodal Monitoring" in flagged
        assert "Acid-base disorders" in flagged

    def test_facts_added_only_to_the_db_still_survive(self):
        """Reseeding inserts and updates but never deletes, so appended facts
        are safe even though they are absent from the JSON. Asserted so the
        distinction between 'new fact' and 'edited fact' stays understood."""
        from src.student_model import conn

        _reseed()
        with conn() as db:
            n = db.execute(
                "SELECT COUNT(*) FROM kp_catalog WHERE id LIKE 'gapfill-%'").fetchone()[0]
        assert n > 0, "gap-fill facts vanished on reseed"
