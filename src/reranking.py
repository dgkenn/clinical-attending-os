from __future__ import annotations

import json
import math
import os
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

from .config import settings


DEFAULT_WEIGHTS = {
    "vector": 0.20,
    "bm25": 0.10,
    "keyword": 0.18,
    "source_priority": 0.16,
    "library_priority": 0.10,
    "topic_score": 0.06,
    "phrase_score": 0.10,
    "mode_bonus": 0.10,
    "high_yield": 0.05,
    "cross_encoder": 0.30,
    "basics_source_boost": 5.0,
}


@lru_cache(maxsize=1)
def load_weights() -> dict[str, float]:
    path = Path(settings.chroma_dir).parent / "reranking_weights.json"
    if not path.exists():
        return dict(DEFAULT_WEIGHTS)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return dict(DEFAULT_WEIGHTS)
    merged = dict(DEFAULT_WEIGHTS)
    for k, v in data.items():
        if k in merged and isinstance(v, (int, float)):
            merged[k] = float(v)
    return merged


def _minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    lo = min(values)
    hi = max(values)
    span = hi - lo
    if span <= 0:
        return [0.5 for _ in values]
    return [(v - lo) / span for v in values]


SOURCE_PRIORITY = {
    "intern_teach": ["Intern Notes / Survival Guide", "Hospitalist / Intern Guide", "MGH Housestaff Manual", "OnlineMedEd Intern Guide", "Marino ICU Book", "Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller"],
    "cross_cover": ["Intern Notes / Survival Guide", "Hospitalist / Intern Guide", "MGH Housestaff Manual", "Marino ICU Book", "OnlineMedEd Intern Guide", "Stanford CA-1"],
    "ICU_teach": ["Marino ICU Book", "MGH Housestaff Manual", "Intern Notes / Survival Guide", "Hospitalist / Intern Guide", "Stanford CA-1", "Morgan & Mikhail"],
    "anesthesia_transition": ["Marino ICU Book", "Stanford CA-1", "Morgan & Mikhail", "MGH Housestaff Manual", "Miller/Baby Miller"],
    "anesthesia_boards": ["Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller", "Marino ICU Book", "MGH Housestaff Manual"],
    "OR_prep": ["Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller"],
    "broad_explain": ["Morgan & Mikhail", "Stanford CA-1", "Miller/Baby Miller"],
    "basics_exam": ["Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller"],
    "narrow_fact": ["Morgan & Mikhail", "Miller/Baby Miller", "Stanford CA-1"],
    "drug": ["Miller/Baby Miller", "Morgan & Mikhail", "Stanford CA-1"],
    "crisis": ["Stanford CA-1", "Morgan & Mikhail", "Miller/Baby Miller"],
    "oral_boards": ["Morgan & Mikhail", "Stanford CA-1", "Miller/Baby Miller"],
    "physiology": ["Miller/Baby Miller", "Morgan & Mikhail", "Stanford CA-1"],
}

LIBRARY_PRIORITY = {
    "intern_teach": ["intern_year_medicine", "ICU_critical_care", "personal_notes", "anesthesiology_boards"],
    "cross_cover": ["intern_year_medicine", "ICU_critical_care", "personal_notes", "anesthesiology_boards"],
    "ICU_teach": ["ICU_critical_care", "intern_year_medicine", "anesthesiology_boards", "personal_notes"],
    "anesthesia_transition": ["ICU_critical_care", "anesthesiology_boards", "intern_year_medicine", "personal_notes"],
    "anesthesia_boards": ["anesthesiology_boards", "ICU_critical_care", "intern_year_medicine", "personal_notes"],
    "basics_exam": ["anesthesiology_boards", "ICU_critical_care", "intern_year_medicine"],
    "crisis": ["anesthesiology_boards", "ICU_critical_care", "intern_year_medicine"],
}


_TERMS_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9-]{2,}")


@lru_cache(maxsize=4096)
def _terms_cached_tuple(text: str) -> tuple[str, ...]:
    return tuple(t.lower() for t in _TERMS_RE.findall(text))


def terms(text: str) -> list[str]:
    if len(text) <= 4096:
        return list(_terms_cached_tuple(text))
    return [t.lower() for t in _TERMS_RE.findall(text)]


def keyword_overlap(query: str, text: str) -> float:
    q = set(terms(query))
    if not q:
        return 0.0
    d = set(terms(text))
    return len(q & d) / math.sqrt(len(q))


def bm25_scores(query: str, docs: list[str]) -> list[float]:
    try:
        from rank_bm25 import BM25Okapi
    except Exception:
        q = Counter(terms(query))
        return [sum(Counter(terms(doc))[t] for t in q) for doc in docs]
    tokenized = [terms(d) for d in docs]
    if not tokenized:
        return []
    return list(BM25Okapi(tokenized).get_scores(terms(query)))


def source_priority_score(book: str, mode: str) -> float:
    order = SOURCE_PRIORITY.get(mode, SOURCE_PRIORITY.get("broad_explain", []))
    if book in order:
        return (len(order) - order.index(book)) / len(order)
    return 0.2


def library_priority_score(library: str, mode: str) -> float:
    order = LIBRARY_PRIORITY.get(mode, [])
    if library in order:
        return (len(order) - order.index(library)) / len(order)
    return 0.2 if library else 0.0


def mode_match_bonus(meta: dict[str, Any], mode: str, query: str, text: str) -> float:
    library = meta.get("library", "")
    source = meta.get("source_name") or meta.get("book", "")
    q = query.lower()
    t = text.lower()
    bonus = 0.0
    if mode in {"intern_teach", "cross_cover"}:
        if library == "intern_year_medicine":
            bonus += 2.0
        if library == "anesthesiology_boards":
            bonus -= 1.0
    if mode == "ICU_teach":
        if library == "ICU_critical_care":
            bonus += 2.5
        elif library == "intern_year_medicine":
            bonus += 1.0
        elif library == "anesthesiology_boards":
            bonus -= 0.8
        if source == "Marino ICU Book":
            bonus += 2.0
        explicit_icu = any(
            term in q
            for term in (
                "icu",
                "critical care",
                "shock",
                "ards",
                "ventilator",
                "vasopressor",
                "pressor",
                "extubation",
                "weaning",
                "massive transfusion",
                "sedation",
                "delirium",
            )
        )
        if explicit_icu and source == "Marino ICU Book":
            bonus += 3.0
        if explicit_icu and library == "intern_year_medicine":
            bonus -= 0.75
        if ("vasopressor" in q or "pressor" in q or "septic shock" in q) and source == "Marino ICU Book":
            bonus += 6.0
        if ("vasopressor" in q or "pressor" in q or "septic shock" in q) and library == "intern_year_medicine":
            bonus -= 1.0
        if ("extubation" in q or "weaning" in q) and source == "Marino ICU Book":
            bonus += 5.0
        if ("massive transfusion" in q or "hemorrhage" in q) and source == "Marino ICU Book":
            bonus += 4.0
    if mode in {"anesthesia_boards", "basics_exam", "drug", "crisis", "oral_boards"} and library == "anesthesiology_boards":
        bonus += 1.4
    if "aki" in q or "acute kidney injury" in q:
        if library == "intern_year_medicine" and ("prerenal" in t or "urine" in t or "creatinine" in t):
            bonus += 2.0
    if "vasopressor" in q or "septic shock" in q:
        if library == "ICU_critical_care" and ("norepinephrine" in t or "vasopressin" in t or "septic shock" in t):
            bonus += 2.0
    # General: if the query names a vasopressor/drug and the chunk text contains that drug,
    # give a strong mode_bonus boost so it competes with source-priority signals.
    # Applies in any mode (not just ICU_teach) so it generalises.
    _NAMED_DRUGS = (
        "norepinephrine", "vasopressin", "phenylephrine", "dopamine",
        "epinephrine", "dobutamine", "milrinone", "rocuronium",
        "succinylcholine", "dantrolene", "metoprolol", "labetalol",
        "nitroglycerin", "nitroprusside", "furosemide", "albumin",
    )
    for _drug in _NAMED_DRUGS:
        if _w(q, _drug) and _drug in t:
            bonus += 5.0
            break  # one named-drug match is sufficient
    if "high pressure" in q or "ventilator" in q:
        if library == "ICU_critical_care" and ("pressure" in t or "alarm" in t or "ventilator" in t):
            bonus += 2.0
    return bonus


_LAST_QUERY_RE = re.compile(r"\bLAST\b")
_LAST_CONTEXT_RE = re.compile(r"local anesthetic|toxicity|intralipid|bupivacaine|lipid emulsion", re.I)


def _w(query: str, term: str) -> bool:
    """Word-boundary substring match (avoids 'last' matching inside 'last call')."""
    return re.search(rf"\b{re.escape(term)}\b", query, re.I) is not None


def exact_phrase_bonus(query: str, text: str) -> float:
    q_low = query.lower()
    t_low = text.lower()
    bonus = 0.0
    for phrase in [
        "malignant hyperthermia",
        "local anesthetic systemic toxicity",
        "succinylcholine contraindications",
        "shunt physiology",
    ]:
        if phrase in q_low and phrase in t_low:
            bonus += 2.0
    if _w(query, "MAC") and _w(text, "MAC"):
        bonus += 0.8
    if "malignant hyperthermia" in q_low and "dantrolene" in t_low:
        bonus += 1.0
        if "treatment - acute phase" in t_low or "call for help" in t_low or "mh cart" in t_low:
            bonus += 2.5
    last_query = (
        bool(_LAST_QUERY_RE.search(query))
        or "local anesthetic toxicity" in q_low
        or "local anesthetic systemic toxicity" in q_low
    )
    if last_query and (
        "treatment of last" in t_low or "intralipid" in t_low or "lipid emulsion" in t_low
    ):
        if _LAST_CONTEXT_RE.search(text):
            bonus += 3.0
    if "oxygen failure" in q_low and ("oxygen failure" in t_low or "pipeline" in t_low or "oxygen analyzer" in t_low):
        bonus += 3.0
    if "hyperkalemia" in q_low and ("calcium" in t_low or "insulin" in t_low or "ecg" in t_low):
        bonus += 1.5
    # Calcium gluconate dosing: strongly prefer treatment chunks (1 amp / 10% soln) over admission checklists
    if "calcium gluconate" in q_low and "calcium gluconate" in t_low:
        if any(tok in t_low for tok in ("1 amp", "10%", "iv push", "mg/kg", "gram", "1g", "1 g")):
            bonus += 3.5
    # Succinylcholine contraindications: boost chunks that list the specific clinical scenarios
    if "succinylcholine" in q_low and ("contraindication" in q_low or "avoid" in q_low):
        if any(tok in t_low for tok in ("burn", "denervation", "hyperkalemia", "upregulation", "spinal cord")):
            bonus += 3.0
    # Rapid sequence induction: boost chunks that name the actual RSI drugs
    if ("rapid sequence" in q_low or "rsi" in q_low) and any(
        tok in t_low for tok in ("rocuronium", "succinylcholine")
    ):
        bonus += 2.5
    if ("afib" in q_low or "atrial fibrillation" in q_low) and ("rate control" in t_low or "rvr" in t_low):
        bonus += 1.5
    if "ards" in q_low and ("tidal volume" in t_low or "plateau" in t_low or "peep" in t_low):
        bonus += 1.8
    if "sepsis" in q_low and ("lactate" in t_low or "antibiotic" in t_low or "fluid" in t_low):
        bonus += 1.5
    # General: if the query explicitly names a vasopressor/drug by word-boundary match,
    # boost chunks that also contain that drug name.  Generalises to any named drug in
    # a shock/hemodynamic query without hard-coding the expected answer text.
    _VASOPRESSORS = (
        "norepinephrine", "vasopressin", "phenylephrine", "dopamine",
        "epinephrine", "dobutamine", "milrinone", "rocuronium",
        "succinylcholine", "dantrolene", "metoprolol", "labetalol",
        "nitroglycerin", "nitroprusside", "furosemide", "albumin",
    )
    for drug in _VASOPRESSORS:
        if _w(query, drug) and drug in t_low:
            bonus += 2.5
            break  # one drug match is enough; avoid stacking
    return bonus


def _hf_model_cached(model_name: str) -> bool:
    cache_name = f"models--{model_name.replace('/', '--')}"
    candidates = [
        Path.home() / ".cache" / "huggingface" / "hub" / cache_name,
        Path.home() / ".cache" / "torch" / "sentence_transformers" / model_name.replace("/", "_"),
    ]
    return any(path.exists() for path in candidates)


@lru_cache(maxsize=1)
def _cross_encoder():
    if not settings.enable_local_reranker:
        return None
    if settings.local_models_offline:
        if not _hf_model_cached(settings.local_reranker_model):
            return None
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("USE_TF", "0")
    os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
    try:
        from sentence_transformers import CrossEncoder
    except Exception:
        return None
    try:
        return CrossEncoder(settings.local_reranker_model)
    except Exception:
        return None


def _apply_cross_encoder(query: str, candidates: list[dict[str, Any]], limit: int = 40) -> None:
    """Populate reranker_score (0-1, min-max normalized) on the top `limit` candidates."""
    model = _cross_encoder()
    if model is None or not candidates:
        return
    pool = candidates[:limit]
    pairs = [(query, c.get("search_text") or c["text"]) for c in pool]
    try:
        raw_scores = [float(s) for s in model.predict(pairs)]
    except Exception:
        return
    normalized = _minmax(raw_scores)
    for c, score in zip(pool, normalized):
        c["reranker_score"] = score


# Deliberately modest: enough to lift a treatment passage past a same-topic
# checklist, not enough to override vector/BM25 relevance and pull in an
# actionable passage about a different disease.
_ACTIONABILITY_WEIGHT = 0.12
# Enough to drop a pure reference list below real content, not enough to bury
# a genuine passage that happens to carry citations.
_CITATION_PENALTY = 0.20

_MANAGEMENT_INTENT = re.compile(
    r'\b(management|manage|treat|treatment|therapy|initial|first[- ]line|'
    r'next step|what do you (?:do|give)|how do you treat|dose|dosing|'
    r'resuscitat|stabiliz|stabilis)\w*', re.I,
)

# What "saying what to do" looks like: a dose, a route, or an imperative
# clinical action. Counted as a density so a long passage that mentions one
# drug in passing does not outrank a genuine treatment paragraph.
_ACTION_SIGNAL = re.compile(
    r'\b(\d+\s*(?:mg|mcg|g|units?|mL|mEq)(?:/kg)?|'
    r'IV|IM|PO|subcutaneous|infusion|bolus|drip|'
    r'start|give|administer|load|titrate|initiate|begin|'
    r'first[- ]line|indicated|contraindicated)\b', re.I,
)


# A numbered journal citation: "6. Chioncel O, Mebazaa A, Maggioni AP, et al."
_CITATION = re.compile(r'\d{1,3}\.\s+[A-Z][a-z]+ [A-Z]{1,3},')


def _has_management_intent(query: str) -> bool:
    return bool(_MANAGEMENT_INTENT.search(query or ""))


def _citation_density(text: str) -> float:
    """Fraction of a passage that is bibliography rather than teaching content.

    A reference list ranked FIRST for "heart failure exacerbation management"
    ("6. Chioncel O, Mebazaa A, Maggioni AP, et al. Acute heart failure...") —
    it matches every query term while teaching nothing.

    This is a PENALTY, not a filter, and it scales with density: many chunks
    legitimately end with a citation or two after real content, and dropping
    those would delete teaching material. Only a passage that is mostly
    citations is pushed down, and even then it stays retrievable.
    """
    t = text or ""
    if len(t) < 80:
        return 0.0
    # ~60 chars is a typical citation; compare that span against the passage.
    return min(1.0, len(_CITATION.findall(t)) * 60.0 / len(t))


def _actionability(text: str) -> float:
    """Density of do-this signal in a passage, roughly per 100 words."""
    t = text or ""
    if not t.strip():
        return 0.0
    words = max(1, len(t.split()))
    return 100.0 * len(_ACTION_SIGNAL.findall(t)) / words


def rerank(
    query: str,
    candidates: list[dict[str, Any]],
    mode: str = "broad_explain",
    topic_filter: str | None = None,
    use_cross_encoder: bool = True,
) -> list[dict[str, Any]]:
    if not candidates:
        return []
    from .fact_extraction import high_yield_score

    weights = load_weights()
    scoring_texts = [c.get("search_text") or c["text"] for c in candidates]
    bm25 = bm25_scores(query, scoring_texts)
    for i, c in enumerate(candidates):
        meta = c.get("metadata", {})
        text = scoring_texts[i]
        c["bm25_score"] = float(bm25[i]) if i < len(bm25) else 0.0
        c["keyword_score"] = keyword_overlap(query, text)
        c["phrase_score"] = exact_phrase_bonus(query, text)
        c["source_priority"] = source_priority_score(meta.get("source_name") or meta.get("book", ""), mode)
        c["library_priority"] = library_priority_score(meta.get("library", ""), mode)
        c["mode_bonus"] = mode_match_bonus(meta, mode, query, text)
        tags = meta.get("topic_tags", "")
        c["topic_score"] = 1.0 if topic_filter and topic_filter.lower() in tags.lower() else 0.0
        c["high_yield"] = high_yield_score(meta, c.get("text", ""))
        c["reranker_score"] = None

    components = ("vector_score", "bm25_score", "keyword_score", "phrase_score", "mode_bonus")
    norms: dict[str, list[float]] = {
        comp: _minmax([float(c.get(comp, 0.0)) for c in candidates]) for comp in components
    }

    basics_boost = weights["basics_source_boost"] if mode == "basics_exam" else 1.0

    for i, c in enumerate(candidates):
        c["final_score"] = (
            norms["vector_score"][i] * weights["vector"]
            + norms["bm25_score"][i] * weights["bm25"]
            + norms["keyword_score"][i] * weights["keyword"]
            + c["source_priority"] * weights["source_priority"] * basics_boost
            + c["library_priority"] * weights["library_priority"]
            + c["topic_score"] * weights["topic_score"]
            + norms["phrase_score"][i] * weights["phrase_score"]
            + norms["mode_bonus"][i] * weights["mode_bonus"]
            + c["high_yield"] * weights["high_yield"]
        )

    # When the question asks what to DO, prefer passages that say what to do.
    #
    # "STEMI initial management" ranked a chest-pain intake checklist ("Details
    # of pain: onset, site, nature") above "start heparin drip, aspirin load,
    # and plavix or brilinta load". Both are topically about chest pain; only
    # one answers a management question. Intake checklists and
    # risk-stratification tables are lexically rich and score well on every
    # other component, so without this they crowd out the actual treatment
    # steps on exactly the queries where those matter most.
    #
    # Applied ONLY to management-intent queries — for "differential of chest
    # pain" the checklist is genuinely the better passage.
    if _has_management_intent(query):
        act = _minmax([_actionability(c.get("text", "")) for c in candidates])
        for i, c in enumerate(candidates):
            c["actionability"] = act[i]
            c["final_score"] += act[i] * _ACTIONABILITY_WEIGHT

    # Push bibliography down, proportionally to how much of it is bibliography.
    for c in candidates:
        density = _citation_density(c.get("text", ""))
        if density > 0.25:
            c["citation_density"] = density
            c["final_score"] -= density * _CITATION_PENALTY

    initially_ranked = sorted(candidates, key=lambda x: x["final_score"], reverse=True)
    if use_cross_encoder:
        _apply_cross_encoder(query, initially_ranked)
        for c in initially_ranked:
            if c.get("reranker_score") is not None:
                c["final_score"] += float(c["reranker_score"]) * weights["cross_encoder"]
    return sorted(initially_ranked, key=lambda x: x["final_score"], reverse=True)
