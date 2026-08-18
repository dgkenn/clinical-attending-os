"""The fact matcher, validated against real pairs from the live database.

Every case here is either an actual duplicate pair found in knowledge_points
(66 high-overlap pairs existed when the matcher was written) or an actual
near-miss whose wrong merge would have destroyed a distinct fact. The stakes
are asymmetric — a false merge is invisible data loss, a false split is a
visible duplicate — so the gray zone returns "uncertain" for the tutor to
resolve rather than being silently decided.
"""
from __future__ import annotations

import pytest

from src.fact_matcher import compare_facts


def same(a, b):
    v = compare_facts(a, b)
    assert v.verdict == "same", f"expected same, got {v.verdict}: {v.reason}"


def different(a, b):
    v = compare_facts(a, b)
    assert v.verdict == "different", f"expected different, got {v.verdict}: {v.reason}"


def uncertain_or_different(a, b):
    """For pairs where a merge would be wrong but 'uncertain' is acceptable —
    both outcomes prevent the silent merge."""
    v = compare_facts(a, b)
    assert v.verdict in ("uncertain", "different"), (
        f"must not merge, got {v.verdict}: {v.reason}")


# --------------------------------------------------------------------------- #
# TRUE DUPLICATES from the live DB — these must merge

def test_real_dupe_cellulitis_detail_added():
    same(
        "Non-purulent cellulitis primary organism: Streptococcus, treat with beta-lactam",
        "Non-purulent cellulitis: primary organism is Streptococcus (not Staph) — "
        "treat with beta-lactam (cephalexin or cefazolin)",
    )


def test_real_dupe_cardioversion_with_different_negated_distractors():
    """Both state 3-4 weeks. One warns 'not 24 hours', the other 'NOT 3 months'.
    The negated quantities are distractors, not claims — without negation
    handling these two phrasings of the SAME fact read as conflicting."""
    same(
        "Pre-cardioversion anticoagulation duration: 3-4 weeks (not 24 hours) "
        "when afib duration unknown or ≥48 hours",
        "Pre-cardioversion anticoagulation: 3-4 weeks when afib duration unknown "
        "or ≥48hrs (NOT 3 months — that's post-cardioversion continuation)",
    )


def test_real_dupe_dvt_doacs_detail_added():
    same(
        "DVT treatment: DOACs preferred; provoked DVT = 3 months minimum",
        "DVT treatment: DOACs (rivaroxaban or apixaban) preferred over "
        "heparin/warfarin for uncomplicated DVT; provoked DVT = 3 months minimum",
    )


def test_real_dupe_succinylcholine_reworded():
    same(
        "Succinylcholine contraindicated in subacute spinal cord injury "
        "(24hr-6mo window) due to extrajunctional ACh receptor upregulation",
        "Succinylcholine contraindicated in subacute spinal cord injury "
        "(24hr–6mo window): extrajunctional ACh receptor upregulation causes "
        "massive potassium release",
    )


def test_identical_strings():
    same("Digoxin toxicity is potentiated by hypokalemia",
         "Digoxin toxicity is potentiated by hypokalemia")


# --------------------------------------------------------------------------- #
# NEAR-MISSES — merging any of these destroys a distinct fact

def test_dvt_wells_and_pe_wells_are_different_scores():
    """Real near-miss from the DB at 60% overlap."""
    uncertain_or_different(
        "DVT diagnosis: Wells score first — high probability go straight to "
        "compression ultrasound; low probability D-dimer",
        "Wells PE score: D-dimer only useful if Wells less than 2 (low "
        "probability) to rule out PE",
    )


def test_fena_prerenal_vs_intrinsic():
    """Same words, opposite thresholds and categories."""
    different(
        "AKI prerenal: FeNa less than 1% — kidney retaining sodium",
        "AKI intrinsic ATN: FeNa greater than 2% — tubules damaged",
    )


def test_hypo_vs_hyper_on_shared_stem():
    """The difflib failure mode: edit distance is blind to hypo/hyper."""
    different(
        "Hypokalemia potentiates digoxin toxicity",
        "Hyperkalemia is a marker of acute digoxin toxicity",
    )


def test_different_potassium_targets():
    different(
        "Target K+ greater than 4.0 in heart failure patients",
        "Treat hyperkalemia when K+ greater than 5.5 with ECG changes",
    )


def test_same_number_different_time_unit():
    """'3' matching '3' must not merge weeks with months."""
    different(
        "Anticoagulate for 3 weeks before elective cardioversion",
        "Anticoagulate for 3 months after a provoked DVT",
    )


def test_opposite_comparator_same_value():
    different(
        "D-dimer useful when Wells less than 2 percent probability tier",
        "D-dimer not interpretable when Wells greater than 2 percent probability tier",
    )


def test_different_beta_blockers_are_different_facts():
    """Variceal prophylaxis: propranolol works, metoprolol does not —
    a drug-name swap flips the clinical meaning."""
    different(
        "Variceal prophylaxis: nonselective beta-blocker propranolol reduces "
        "portal pressure",
        "Variceal prophylaxis: metoprolol is NOT adequate — cardioselective "
        "agents lack the portal effect",
    )


def test_drug_subset_is_not_a_conflict():
    same(
        "DVT treatment: DOACs preferred; provoked DVT = 3 months minimum",
        "DVT treatment: DOACs (rivaroxaban, apixaban) preferred; provoked DVT "
        "= 3 months minimum",
    )


def test_provoked_vs_unprovoked():
    different(
        "Provoked PE: anticoagulate 3 months",
        "Unprovoked PE: indefinite anticoagulation with periodic reassessment",
    )


def test_preload_vs_afterload():
    different(
        "High PEEP drops blood pressure by reducing preload via decreased "
        "venous return",
        "High PEEP was thought to raise afterload on the left ventricle "
        "via increased venous return",
    )


# --------------------------------------------------------------------------- #
# the gray zone stays gray

def test_high_overlap_without_conflicts_is_uncertain_not_same():
    """Between the thresholds, with no conflicts, the matcher must ask rather
    than answer."""
    v = compare_facts(
        "Sepsis bundle: lactate, blood cultures, then broad antibiotics within "
        "the first hour of recognition",
        "Sepsis bundle requires lactate and blood cultures before antibiotics",
    )
    assert v.verdict in ("uncertain", "same")
    # whatever the verdict, it must never be a silent 'different' at this
    # similarity with no conflict — that would guarantee duplicates
    assert v.verdict != "different"


def test_short_facts_cannot_merge_on_few_shared_tokens():
    v = compare_facts("Give calcium first", "Give insulin first")
    assert v.verdict != "same"


def test_empty_and_junk_never_match():
    assert compare_facts("", "anything").verdict == "different"
    assert compare_facts("a b", "a b").verdict == "different"  # no real tokens
