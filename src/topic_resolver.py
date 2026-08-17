"""Canonicalize freeform tutor topic names onto curriculum blueprint names.

Why this exists: the tutor (Claude or the Custom GPT) names topics freely —
"Chest pain", "AKI", "Afib with RVR" — while the curriculum blueprint has
"Approach to Chest Pain", "Acute Kidney Injury", etc. Without resolution, 25
of the first 27 studied topics matched nothing in the blueprint: coverage
tracking read 0.2%, get_next_topic re-served "new" topics that were already
studied under another name, and the same fact history fragmented across
spellings.

Resolution ladder (first hit wins):
  1. exact match, case/whitespace-insensitive
  2. alias table (common clinical shorthand)
  3. unique substring containment either direction ("Chest pain" is contained
     in exactly one curriculum name -> that name)
  (NO fuzzy matching: difflib merged Hyperkalemia into Hypercalcemia in the
   first live test — edit distance is blind to the hypo/hyper and -kal-/-calc-
   distinctions that carry all the meaning in clinical vocabulary.)

Anything unresolved passes through unchanged — a wrong merge is worse than a
missed one. The mapping applied is returned to the caller so the tutor can see
(and say) the canonical name, which trains both tutors toward blueprint
vocabulary over time.
"""
from __future__ import annotations

import re
from functools import lru_cache

from .student_model import conn, initialize_database

# Clinical shorthand -> blueprint phrasing fragments. Values are matched
# against curriculum names with the same ladder, so they need only get us
# close enough for step 3/4 to land uniquely.
ALIASES: dict[str, str] = {
    "afib": "atrial fibrillation",
    "afib with rvr": "atrial fibrillation",
    "aki": "acute kidney injury",
    "chf": "heart failure",
    "adhf": "acute decompensated heart failure",
    "gi bleed": "gastrointestinal bleeding",
    "uti": "urinary tract infection",
    "dka": "diabetic ketoacidosis",
    "pe": "pulmonary embolism",
    "dvt": "venous thromboembolism",
    "dvt/pe": "venous thromboembolism",
    "copd exacerbation": "copd",
    "mi": "myocardial infarction",
    "acs": "acute coronary syndrome",
    "ams": "altered mental status",
    "last": "local anesthetic systemic toxicity",
    "mh": "malignant hyperthermia",
    "osa": "obstructive sleep apnea",
    "ponv": "postoperative nausea",
}

def _norm(s: str) -> str:
    return " ".join((s or "").lower().split())


@lru_cache(maxsize=1)
def _curriculum_names_cached(version: int) -> tuple[tuple[str, str], ...]:
    """(normalized, original) curriculum names. version busts the cache."""
    initialize_database()
    with conn() as db:
        rows = db.execute("SELECT topic FROM curriculum").fetchall()
    return tuple((_norm(r[0]), r[0]) for r in rows if r[0])


def _curriculum_names() -> tuple[tuple[str, str], ...]:
    # Cache keyed on row count: curriculum changes rarely (re-seed), and a
    # count change busts the cache without a per-call table scan of names.
    initialize_database()
    with conn() as db:
        n = db.execute("SELECT COUNT(*) FROM curriculum").fetchone()[0]
    return _curriculum_names_cached(n)


# Words that FRAME a topic without narrowing it. "Approach to Chest Pain" is
# the same subject as "Chest pain"; "Hypoxemia during OLV" is not the same
# subject as "Hypoxemia".
_FRAMING = re.compile(
    r'^(approach to|evaluation of|assessment of|management of|overview of|'
    r'introduction to|principles of|diagnosis and management of|'
    r'recognition of|the)\s+|'
    r'\s*:\s*(diagnosis and management|management|overview|basics|'
    r'pathophysiology and classification|classification|principles)\s*$',
    re.I,
)


def _strip_framing(s: str) -> str:
    prev = None
    out = s
    while prev != out:            # a name may carry both a prefix and a suffix
        prev = out
        out = _FRAMING.sub("", out).strip()
    return out


def _same_subject(q: str, norm: str) -> bool:
    """True when containment is only across framing words, not new clinical scope.

    Plain unique-containment was too permissive: "Hypoxemia" is contained in
    exactly one blueprint name — "Hypoxemia during OLV: diagnosis and
    management" — so six attempts of general intern hypoxemia would have been
    filed under a thoracic-anaesthesia one-lung-ventilation topic. The extra
    words there ("during OLV") change the subject; the extra words in "Approach
    to Chest Pain" do not.

    So strip known framing phrases from both sides and require what remains to
    match exactly. Anything that still differs is a genuinely different (and
    usually narrower) topic, and is left unresolved — a wrong merge is worse
    than a missed one.
    """
    return _strip_framing(q) == _strip_framing(norm)


def resolve_topic(name: str) -> tuple[str, bool]:
    """Return (canonical_or_original_name, was_resolved).

    Never raises; empty/blank input passes through unresolved.
    """
    raw = (name or "").strip()
    q = _norm(raw)
    if not q:
        return raw, False
    names = _curriculum_names()
    if not names:
        return raw, False

    # 1. exact
    for norm, orig in names:
        if norm == q:
            # exact hits count as resolved even when spelling already matched
            return orig, orig != raw
    # 2. alias -> re-enter ladder with the alias expansion
    alias = ALIASES.get(q)
    if alias:
        q = _norm(alias)
        for norm, orig in names:
            if norm == q:
                return orig, True

    # 3. unique containment, but ONLY across framing words (min length 4)
    if len(q) >= 4:
        contains = [
            orig for norm, orig in names
            if (q in norm or norm in q) and _same_subject(q, norm)
        ]
        if len(contains) == 1:
            return contains[0], True

    return raw, False
