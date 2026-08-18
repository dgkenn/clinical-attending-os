"""Decide whether two clinical facts are the same fact.

Used to dedupe knowledge points at capture time (log_tangent) so the record
converges instead of accumulating near-copies — 66 high-overlap pairs already
exist from before this existed.

The stakes are asymmetric and the design follows from that:

  * A FALSE MERGE destroys a distinct fact, and the loss is invisible — the
    user simply never gets asked about one of them again. Near-identical
    clinical strings routinely have opposite meanings ("FeNa <1% = prerenal"
    vs "FeNa >2% = intrinsic ATN"; difflib once merged Hyperkalemia into
    Hypercalcemia in this codebase).
  * A FALSE SPLIT leaves a duplicate in the queue. Annoying, visible, cheap.

So the verdict is three-way, not two-way: "same", "different", or "uncertain".
Uncertain is returned to the caller to resolve — never silently decided in
either direction. Merges additionally require that no CLINICAL-MEANING
CONFLICT exists, checked structurally rather than lexically:

  * quantities, unit-aware: "3-4 weeks" vs "3 months" conflict even though the
    digit 3 matches; "target Hgb 7-8" vs "target Hgb 9-10" conflict; a value
    set that is a SUBSET of the other is fine (same fact, extra detail).
  * negated quantities are distractors, not claims: in "3-4 weeks (NOT 24
    hours)" the 24 does not conflict with anything — it is the wrong answer
    the fact warns against. Without this rule, two phrasings of the SAME
    cardioversion fact (one warning "not 24 hours", the other "not 3 months")
    read as conflicting.
  * opposite comparators on the same value conflict: "FeNa <1%" vs "FeNa >1%".
  * polar morphemes conflict: hypo/hyper on a shared stem, provoked/unprovoked,
    plus an explicit pair list (preload/afterload, sensitivity/specificity...).
  * drug sets conflict when both sides name drugs and neither set contains the
    other: {propranolol} vs {metoprolol} is a different fact; {DOAC} vs
    {DOAC, rivaroxaban, apixaban} is the same fact with detail.

Validated against real pairs from the live database in
tests/test_fact_matcher.py — every rule above traces to one of them.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# --------------------------------------------------------------------------- #
# tokenization

_STOP = frozenset(
    "the a an of to in for and or with not is are be as on at by from if this "
    "that what which when why how do does you your it its when while during "
    "than then also only more most some can may might should must".split())

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokens(s: str) -> set[str]:
    return {w for w in _TOKEN_RE.findall((s or "").lower())
            if len(w) > 3 and w not in _STOP}


def _norm(s: str) -> str:
    return " ".join(_TOKEN_RE.findall((s or "").lower()))


# --------------------------------------------------------------------------- #
# quantities — unit-aware, negation-aware

_UNIT_SYNONYMS = {
    "hr": "hour", "hrs": "hour", "hour": "hour", "hours": "hour", "h": "hour",
    "min": "minute", "mins": "minute", "minute": "minute", "minutes": "minute",
    "day": "day", "days": "day",
    "wk": "week", "wks": "week", "week": "week", "weeks": "week",
    "mo": "month", "mos": "month", "month": "month", "months": "month",
    "yr": "year", "yrs": "year", "year": "year", "years": "year",
    "mg": "mg", "mcg": "mcg", "g": "g", "gram": "g", "grams": "g",
    "meq": "meq", "mmol": "mmol", "ml": "ml", "l": "l",
    "%": "pct", "percent": "pct", "mmhg": "mmhg",
    "unit": "unit", "units": "unit",
    "mg/kg": "mg_per_kg", "mcg/kg": "mcg_per_kg", "ml/kg": "ml_per_kg",
    "meq/l": "meq_per_l", "mmol/l": "mmol_per_l", "g/dl": "g_per_dl",
}

# Hours per unit, for cross-unit conflicts within the time class
# ("3 weeks" vs "3 months" is a conflict even though the digits match).
_TIME_IN_HOURS = {"minute": 1 / 60, "hour": 1.0, "day": 24.0,
                  "week": 168.0, "month": 730.0, "year": 8766.0}

_QTY_RE = re.compile(
    r"(?P<cmp><=|>=|≤|≥|<|>|less than|greater than|under|over|at least|up to|max(?:imum)?|min(?:imum)?)?"
    r"\s*(?P<a>\d+(?:\.\d+)?)"
    r"(?:\s*[-–—]|\s+to\s+)?(?P<b>\d+(?:\.\d+)?)?"
    r"\s*(?P<unit>mg/kg|mcg/kg|ml/kg|meq/l|mmol/l|g/dl|hours?|hrs?|days?|weeks?|wks?|"
    r"months?|mos?|years?|yrs?|minutes?|mins?|mcg|mg|grams?|meq|mmol|ml|mmhg|units?|percent|%)?",
    re.I,
)

_NEGATORS = ("not", "never", "avoid", "no", "without", "isn't", "aren't", "don't")

_CMP_DIRECTION = {
    "<": "lt", "<=": "lt", "≤": "lt", "less than": "lt", "under": "lt",
    "up to": "lt", "max": "lt", "maximum": "lt",
    ">": "gt", ">=": "gt", "≥": "gt", "greater than": "gt", "over": "gt",
    "at least": "gt", "min": "gt", "minimum": "gt",
}


@dataclass
class Quantity:
    values: tuple[float, ...]
    unit: str | None
    direction: str | None
    negated: bool


def _is_negated(text: str, start: int) -> bool:
    """A quantity preceded (within a few words / its parenthetical) by a negator
    is a distractor the fact is warning against, not a claim it makes."""
    window = text[max(0, start - 24):start].lower()
    paren = window.rfind("(")
    if paren != -1:
        window = window[paren:]
    words = _TOKEN_RE.findall(window)
    return any(w in _NEGATORS for w in words[-4:])


def _quantities(s: str) -> list[Quantity]:
    out = []
    for m in _QTY_RE.finditer(s or ""):
        vals = [float(m.group("a"))]
        if m.group("b"):
            vals.append(float(m.group("b")))
        unit_raw = (m.group("unit") or "").lower().rstrip(".")
        unit = _UNIT_SYNONYMS.get(unit_raw)
        cmp_raw = (m.group("cmp") or "").lower()
        out.append(Quantity(
            values=tuple(sorted(vals)),
            unit=unit,
            direction=_CMP_DIRECTION.get(cmp_raw),
            negated=_is_negated(s, m.start()),
        ))
    return out


def _quantity_conflict(qa: list[Quantity], qb: list[Quantity]) -> str | None:
    """A conflict between the ASSERTED (non-negated) quantities of two facts."""
    a = [q for q in qa if not q.negated and q.unit]
    b = [q for q in qb if not q.negated and q.unit]
    if not a or not b:
        return None

    def by_class(qs):
        classes: dict[str, set[float]] = {}
        for q in qs:
            cls = "time" if q.unit in _TIME_IN_HOURS else q.unit
            scale = _TIME_IN_HOURS.get(q.unit, 1.0)
            classes.setdefault(cls, set()).update(v * scale for v in q.values)
        return classes

    ca, cb = by_class(a), by_class(b)
    for cls in set(ca) & set(cb):
        va, vb = ca[cls], cb[cls]
        if not (va <= vb or vb <= va):
            return (f"conflicting {cls} values "
                    f"{sorted(va)} vs {sorted(vb)}")

    # Opposite comparator on the same value+unit: "FeNa <1%" vs "FeNa >1%".
    for x in a:
        for y in b:
            if (x.unit == y.unit and set(x.values) & set(y.values)
                    and x.direction and y.direction and x.direction != y.direction):
                return f"opposite comparators on {x.values[0]} {x.unit}"
    return None


# --------------------------------------------------------------------------- #
# polarity — morphemes that flip clinical meaning

_POLAR_PAIRS = (
    ("prerenal", "intrinsic"), ("prerenal", "postrenal"), ("intrinsic", "postrenal"),
    ("increase", "decrease"), ("increases", "decreases"), ("increased", "decreased"),
    ("agonist", "antagonist"), ("contraindicated", "indicated"),
    ("systolic", "diastolic"), ("sensitivity", "specificity"),
    ("afterload", "preload"), ("dilation", "constriction"),
    ("bradycardia", "tachycardia"), ("acidosis", "alkalosis"),
    ("arterial", "venous"), ("inspiratory", "expiratory"),
    ("prophylaxis", "treatment"),
)

# hypoX vs hyperX on the SAME stem (hypokalemia/hyperkalemia). Checked by stem
# so it covers pairs the explicit list never anticipated.
_STEM_PREFIXES = (("hypo", "hyper"), ("brady", "tachy"))


def _polar_conflict(ta: set[str], tb: set[str]) -> str | None:
    for x, y in _POLAR_PAIRS:
        if (x in ta and y in tb and x not in tb and y not in ta):
            return f"polar opposition {x}/{y}"
        if (y in ta and x in tb and y not in tb and x not in ta):
            return f"polar opposition {y}/{x}"
    for p, q in _STEM_PREFIXES:
        stems_a = {t[len(p):] for t in ta if t.startswith(p)}
        stems_b = {t[len(q):] for t in tb if t.startswith(q)}
        both = {s for s in stems_a & stems_b if len(s) >= 4}
        for s in both:
            if (q + s) not in ta and (p + s) not in tb:
                return f"polar opposition {p}{s}/{q}{s}"
        # and the mirrored direction
        stems_a2 = {t[len(q):] for t in ta if t.startswith(q)}
        stems_b2 = {t[len(p):] for t in tb if t.startswith(p)}
        for s in {s for s in stems_a2 & stems_b2 if len(s) >= 4}:
            if (p + s) not in ta and (q + s) not in tb:
                return f"polar opposition {q}{s}/{p}{s}"
    # un-/non- negation of a term the other side asserts bare:
    # "provoked PE" vs "unprovoked PE" are different facts.
    for neg in ("un", "non"):
        for t in ta:
            if t.startswith(neg) and len(t) > len(neg) + 3:
                bare = t[len(neg):]
                if bare in tb and t not in tb and bare not in ta:
                    return f"negated term {t} vs {bare}"
        for t in tb:
            if t.startswith(neg) and len(t) > len(neg) + 3:
                bare = t[len(neg):]
                if bare in ta and t not in ta and bare not in tb:
                    return f"negated term {bare} vs {t}"
    return None


# --------------------------------------------------------------------------- #
# drugs — different named agents are different facts

_DRUG_SUFFIXES = (
    "olol", "alol", "ilol", "pril", "sartan", "statin", "cillin", "mycin",
    "micin", "azole", "oxacin", "dipine", "semide", "thiazide", "parin",
    "gliptin", "glitazone", "prazole", "tidine", "triptan", "curonium",
    "curium", "choline", "caine", "zosin", "afil", "dronate", "setron",
    "vudine", "navir", "mab", "nib", "grel",
)
_DRUG_NAMES = frozenset((
    "aspirin", "digoxin", "insulin", "dantrolene", "tpa", "alteplase",
    "tenecteplase", "heparin", "warfarin", "rivaroxaban", "apixaban",
    "dabigatran", "amiodarone", "adenosine", "epinephrine", "norepinephrine",
    "vasopressin", "dopamine", "dobutamine", "phenylephrine", "albuterol",
    "ipratropium", "magnesium", "naloxone", "flumazenil", "ketamine",
    "propofol", "etomidate", "fentanyl", "morphine", "hydromorphone",
    "acetaminophen", "ibuprofen", "ceftriaxone", "azithromycin", "vancomycin",
    "octreotide", "lactulose", "rifaximin", "thiamine", "haloperidol",
    "quetiapine", "olanzapine", "lorazepam", "diazepam", "midazolam",
    "furosemide", "nitroglycerin", "nicardipine", "labetalol", "hydralazine",
    "levetiracetam", "phenytoin", "kayexalate", "patiromer",
))


def _drugs(tokens: set[str]) -> set[str]:
    return {t for t in tokens
            if t in _DRUG_NAMES or any(t.endswith(s) for s in _DRUG_SUFFIXES)}


def _drug_conflict(ta: set[str], tb: set[str]) -> str | None:
    da, db = _drugs(ta), _drugs(tb)
    if da and db and not (da <= db or db <= da):
        return f"different agents {sorted(da - db)} vs {sorted(db - da)}"
    return None


# --------------------------------------------------------------------------- #
# verdict

@dataclass
class Verdict:
    verdict: str          # "same" | "different" | "uncertain"
    reason: str
    overlap: float = 0.0
    conflicts: list[str] = field(default_factory=list)


# Above SAME_T with no conflicts: confidently the same fact.
# Between UNCERTAIN_T and SAME_T with no conflicts: a human (the tutor) decides.
# Real data separates cleanly: true duplicate pairs in the live DB sit at
# 88-100% overlap; the closest genuinely-distinct pair (DVT Wells vs PE Wells)
# sits at 60%.
SAME_T = 0.85
UNCERTAIN_T = 0.65
MIN_SHARED = 4  # short facts must share this many tokens to merge at all


def _equivalent(x: str, y: str) -> bool:
    """Token equivalence with light morphology.

    Exact match, or one token is a prefix of the other with the shorter at
    least 5 characters: "strep"/"streptococcus", "treat"/"treated",
    "anticoagulation"/"anticoagulate". Without this, a rewording as mild as
    "caused by Strep, treated with beta-lactam" failed to match "primary
    organism: Streptococcus, treat with beta-lactam" — a false negative on a
    pair of real duplicates.

    The 5-char floor keeps this away from the polar morphemes: "hypo"/"hyper"
    are 4 chars and never treated as prefixes of their compounds, and polar
    conflicts are checked on RAW tokens before any of this applies.
    """
    if x == y:
        return True
    shorter, longer = (x, y) if len(x) <= len(y) else (y, x)
    return len(shorter) >= 5 and longer.startswith(shorter)


def _fuzzy_overlap(ta: set[str], tb: set[str]) -> tuple[float, int]:
    small, large = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    matched = sum(1 for t in small if any(_equivalent(t, u) for u in large))
    return (matched / len(small) if small else 0.0), matched


def compare_facts(a: str, b: str) -> Verdict:
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        # Content-free strings can never be "the same fact" — identical junk
        # ("a b" vs "a b") must not merge, so this check precedes the
        # exact-match fast path.
        return Verdict("different", "no comparable content")
    if _norm(a) == _norm(b):
        return Verdict("same", "identical after normalization", 1.0)
    overlap, shared = _fuzzy_overlap(ta, tb)

    conflicts = []
    for check, args in ((_polar_conflict, (ta, tb)),
                        (_drug_conflict, (ta, tb)),
                        (_quantity_conflict, (_quantities(a), _quantities(b)))):
        c = check(*args)
        if c:
            conflicts.append(c)

    if conflicts:
        # A meaning conflict is decisive at any overlap: these are different
        # facts no matter how many words they share.
        return Verdict("different", conflicts[0], overlap, conflicts)

    if overlap >= SAME_T and shared >= MIN_SHARED:
        return Verdict("same", f"overlap {overlap:.0%}, no conflicts", overlap)
    if overlap >= UNCERTAIN_T:
        return Verdict("uncertain",
                       f"overlap {overlap:.0%} — high but not conclusive",
                       overlap)
    return Verdict("different", f"overlap {overlap:.0%}", overlap)


def find_matching_point(topic: str, text: str, rows) -> tuple[dict | None, dict | None]:
    """Scan existing knowledge points for a match.

    Returns (same, uncertain): the best confident duplicate, and the best
    uncertain candidate if no confident one exists. `rows` is an iterable of
    mappings with topic/point/id/status/times_seen. Same-topic rows are
    preferred — that is where duplicates cluster — but all topics are checked,
    because tangent material often already sits under another topic.
    """
    best_same, best_unc = None, None
    for r in sorted(rows, key=lambda r: r["topic"] != topic):
        v = compare_facts(text, r["point"])
        entry = {"id": r["id"], "topic": r["topic"], "point": r["point"],
                 "status": r["status"], "times_seen": r["times_seen"],
                 "why": v.reason, "overlap": round(v.overlap, 2)}
        if v.verdict == "same":
            if best_same is None or v.overlap > best_same["overlap"]:
                best_same = entry
        elif v.verdict == "uncertain":
            if best_unc is None or v.overlap > best_unc["overlap"]:
                best_unc = entry
    return best_same, (None if best_same else best_unc)
