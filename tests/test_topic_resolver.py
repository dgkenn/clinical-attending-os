"""Topic canonicalization must merge across framing words and NOTHING else.

The resolver exists because freeform tutor topic names ("AKI", "GI bleed")
fragment history away from the curriculum blueprint. But an over-eager merge is
worse than none: it silently files answers under someone else's topic, and the
damage is invisible until the coverage map is already wrong.

Two real near-misses are pinned here:
  - difflib fuzzy matching merged Hyperkalemia into Hypercalcemia (edit distance
    is blind to hypo/hyper and -kal-/-calc-, which carry all the meaning).
  - plain unique-containment merged a bare "Hypoxemia" into "Hypoxemia during
    OLV: diagnosis and management" — a one-lung-ventilation topic — because it
    was the only blueprint name containing the word.
"""
from __future__ import annotations

from src.topic_resolver import _same_subject, _strip_framing, resolve_topic


def test_framing_words_are_stripped_but_scope_words_are_not():
    assert _strip_framing("approach to chest pain") == "chest pain"
    assert _strip_framing("hyponatremia: pathophysiology and classification") == "hyponatremia"
    # "during OLV" narrows the subject; it must survive stripping.
    assert "during olv" in _strip_framing("hypoxemia during olv: diagnosis and management")


def test_same_subject_accepts_framing_only_differences():
    assert _same_subject("chest pain", "approach to chest pain")
    assert not _same_subject("hypoxemia", "hypoxemia during olv: diagnosis and management")


def test_bare_term_does_not_absorb_a_narrower_specialist_topic():
    """The regression: general intern hypoxemia must NOT land on the thoracic
    anaesthesia one-lung-ventilation topic just because it is the sole match."""
    canonical, resolved = resolve_topic("Hypoxemia")
    assert not resolved
    assert "OLV" not in canonical


def test_genuine_shorthand_still_resolves():
    for shorthand in ("AKI", "GI bleed"):
        canonical, resolved = resolve_topic(shorthand)
        assert resolved, f"{shorthand} should still canonicalize"
        assert canonical != shorthand


def test_ambiguous_names_pass_through_untouched():
    """Several blueprint entries contain "Hyponatremia"; guessing between them
    would corrupt two histories, so the resolver must decline."""
    for name in ("Hyponatremia", "Delirium"):
        canonical, resolved = resolve_topic(name)
        assert not resolved
        assert canonical == name


def test_blank_and_junk_input_never_raises():
    for junk in ("", "   ", "x"):
        canonical, resolved = resolve_topic(junk)
        assert not resolved
        assert canonical == junk.strip()
