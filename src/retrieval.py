from __future__ import annotations

import json
import math
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

from .config import settings
from .reranking import keyword_overlap, rerank
from .schemas import SourceChunk
from .synonyms import expand_with_synonyms


# Query expansions are RETRIEVAL HINTS, not clinical claims: they widen which
# passages are considered, and the tutor still teaches only from what comes
# back. They matter because the corpus indexes a topic under the vocabulary its
# authors used, which is often not the vocabulary a question uses — "STEMI
# initial management" never reached the MGH Housestaff Manual's "Acute Coronary
# Syndrome" section, because no chunk of it says "STEMI".
#
# The original table was written for the anaesthesia/ICU use case and had no
# entry for STEMI, ACS, chest pain, heart failure, pneumonia, COPD, delirium,
# DKA, PE, stroke, or alcohol withdrawal — i.e. most of intern-year medicine.
QUERY_EXPANSIONS = {
    # --- core internal medicine (intern year) ---
    "stemi": "ST-segment elevation myocardial infarction acute coronary syndrome ACS "
             "aspirin heparin ticagrelor clopidogrel percutaneous coronary intervention "
             "PCI reperfusion fibrinolytic troponin ECG cardiology",
    "nstemi": "non-ST-segment elevation myocardial infarction acute coronary syndrome ACS "
              "aspirin heparin antiplatelet risk stratification TIMI GRACE troponin",
    "acs": "acute coronary syndrome STEMI NSTEMI unstable angina myocardial infarction "
           "aspirin heparin antiplatelet troponin ECG ischemia",
    "acute coronary": "acute coronary syndrome STEMI NSTEMI myocardial infarction aspirin "
                      "heparin antiplatelet troponin ECG",
    "myocardial infarction": "MI STEMI NSTEMI acute coronary syndrome ischemia troponin "
                             "ECG aspirin heparin reperfusion",
    "chest pain": "acute coronary syndrome ACS STEMI angina aortic dissection pulmonary "
                  "embolism pericarditis troponin ECG differential",
    "heart failure": "CHF acute decompensated heart failure pulmonary edema diuresis "
                     "furosemide ejection fraction BNP preload afterload volume overload",
    "pneumonia": "community-acquired pneumonia CAP ceftriaxone azithromycin CURB-65 "
                 "consolidation sputum antibiotics hospital-acquired",
    "copd": "chronic obstructive pulmonary disease exacerbation albuterol ipratropium "
            "steroids bronchodilator noninvasive ventilation BiPAP hypercapnia",
    "asthma": "status asthmaticus bronchospasm albuterol steroids magnesium peak flow "
              "wheezing bronchodilator",
    "delirium": "altered mental status confusion reversible causes infection medications "
                "reorientation antipsychotic haloperidol nonpharmacologic CAM-ICU",
    "alcohol withdrawal": "CIWA benzodiazepine lorazepam diazepam delirium tremens "
                          "seizure thiamine banana bag",
    "dka": "diabetic ketoacidosis insulin infusion potassium anion gap fluids bicarbonate "
           "hyperglycemia ketones",
    "diabetic ketoacidosis": "DKA insulin infusion potassium anion gap fluids hyperglycemia ketones",
    "pulmonary embolism": "PE venous thromboembolism anticoagulation heparin DOAC Wells "
                          "score CT pulmonary angiography thrombolytics right heart strain",
    "dvt": "deep vein thrombosis venous thromboembolism anticoagulation heparin DOAC "
           "ultrasound Wells score",
    "anaphylaxis": "epinephrine intramuscular airway angioedema antihistamine steroids "
                   "hypotension biphasic reaction",
    "hypertensive emergency": "malignant hypertension end-organ damage nicardipine labetalol "
                              "blood pressure lowering rate",
    "seizure": "status epilepticus benzodiazepine lorazepam levetiracetam phenytoin airway "
               "postictal",
    "stroke": "cerebrovascular accident ischemic hemorrhagic tPA thrombectomy NIHSS "
              "time last known well CT head",
    "pancreatitis": "lipase fluids Ranson BISAP gallstone alcohol necrotizing pain control",
    "cellulitis": "skin soft tissue infection cefazolin vancomycin MRSA erysipelas margins",
    "uti": "urinary tract infection pyelonephritis ceftriaxone nitrofurantoin urinalysis culture",
    "urinary tract infection": "UTI pyelonephritis ceftriaxone nitrofurantoin urinalysis culture",
    "hypoxemia": "desaturation low SpO2 oxygenation V/Q mismatch shunt hypoventilation diffusion atelectasis",
    "hypotension": "shock hypovolemia sepsis cardiogenic obstructive distributive fluids vasopressor",
    "hyperkalemia": "high potassium ECG changes calcium gluconate insulin dextrose albuterol dialysis",
    "hyponatremia": "low sodium serum osmolality urine osmolality urine sodium siadh hypovolemia",
    "afib": "atrial fibrillation RVR rate control beta blocker diltiazem anticoagulation",
    "atrial fibrillation": "afib RVR rate control beta blocker diltiazem anticoagulation",
    "shock": "septic cardiogenic obstructive hypovolemic distributive norepinephrine lactate hemodynamics Marino ICU critical care",
    "vasopressor": "pressor septic shock norepinephrine vasopressin dopamine phenylephrine hemodynamic drugs Marino ICU",
    "septic shock": "vasopressor norepinephrine vasopressin dopamine early goal directed therapy Marino ICU",
    "ventilator high pressure": "high pressure alarm obstruction bronchospasm pneumothorax biting kinked tube secretions",
    "ards": "acute respiratory distress syndrome low tidal volume plateau pressure peep proning",
    "extubation": "weaning readiness spontaneous breathing trial SBT cuff leak airway protection mechanical ventilation Marino ICU",
    "weaning": "extubation readiness spontaneous breathing trial SBT rapid shallow breathing index airway protection Marino ICU",
    "massive transfusion": "hemorrhage blood products plasma platelets coagulopathy calcium hypothermia hyperkalemia ICU critical care",
    "sepsis": "lactate blood cultures antibiotics fluids source control vasopressor",
    "gi bleed": "hematemesis melena transfusion ppi octreotide variceal endoscopy",
    "aki": "acute kidney injury prerenal intrinsic postrenal urinalysis creatinine",
    "local anesthetic systemic toxicity": "LAST lipid emulsion bupivacaine toxicity seizure arrhythmia",
    "malignant hyperthermia": "MH dantrolene hypercarbia volatile anesthetic succinylcholine",
    "mac": "minimum alveolar concentration age pregnancy hypothermia alcohol opioids benzodiazepines",
    "cico": "cannot intubate cannot oxygenate emergency front of neck airway cricothyrotomy",
    "cannot intubate": "cannot oxygenate CICO emergency front of neck airway cricothyrotomy",
    "high spinal": "total spinal hypotension bradycardia apnea neuraxial vasopressor airway",
    "bronchospasm": "wheezing high peak airway pressure albuterol epinephrine anaphylaxis",
    "laryngospasm": "jaw thrust positive pressure succinylcholine hypoxemia airway obstruction",
    "oxygen failure": "oxygen pipeline failure oxygen analyzer low inspired oxygen fio2 fail-safe backup cylinder",
    # Neuromuscular blockers / airway pharmacology
    "succinylcholine contraindications": "burn denervation hyperkalemia upregulation spinal cord injury receptor potassium cardiac arrest",
    "succinylcholine contraindication": "burn denervation hyperkalemia upregulation spinal cord injury receptor potassium cardiac arrest",
    "rapid sequence induction": "rocuronium succinylcholine RSI intubation depolarizing neuromuscular blocking agent induction",
    "rapid sequence intubation": "rocuronium succinylcholine RSI depolarizing neuromuscular blocking agent induction",
    # Calcium gluconate dosing (surfaces treatment text vs admission checklist)
    "calcium gluconate": "1 amp IV push 10% solution treatment dose EKG hyperkalemia potassium",
    # Named vasopressor in a shock/hemodynamic context
    "norepinephrine": "vasopressor septic shock first-line mean arterial pressure MAP alpha adrenergic receptor vasoconstriction Marino ICU",
    "vasopressin": "vasopressor septic shock adjunct second-line antidiuretic hormone V1 receptor",
    "phenylephrine": "vasopressor pure alpha agonist reflex bradycardia spinal hypotension",
    "dopamine": "vasopressor cardiogenic shock low-dose renal dose inotrope septic shock",
}


EXACT_PHRASES = [
    "malignant hyperthermia",
    "local anesthetic systemic toxicity",
    "local anesthetic toxicity",
    "treatment of last",
    "intralipid",
    "succinylcholine",
    "shunt",
    "high spinal",
    "cannot intubate",
    "cannot oxygenate",
    "bronchospasm",
    "laryngospasm",
    "anaphylaxis",
    "oxygen failure",
    "hyperkalemia",
    "atrial fibrillation",
    "afib with rvr",
    "ards",
    "sepsis",
    "gi bleed",
]


@lru_cache(maxsize=4)
def _load_json_chunks_cached(path_str: str, mtime_ns: int, size: int) -> list[dict[str, Any]]:
    path = Path(path_str)
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def load_json_chunks() -> list[dict[str, Any]]:
    path = settings.chroma_dir / "chunks.jsonl"
    if not path.exists():
        return []
    stat = path.stat()
    return _load_json_chunks_cached(str(path), stat.st_mtime_ns, stat.st_size)


def expand_query(query: str) -> str:
    expanded = query
    q = query.lower()
    if "LAST" in query or "last treatment" in q:
        expanded += " local anesthetic systemic toxicity lipid emulsion bupivacaine toxicity seizure arrhythmia"
    if re.search(r"\bMH\b", query):
        expanded += " malignant hyperthermia dantrolene hypercarbia volatile anesthetic succinylcholine"
    for key, value in QUERY_EXPANSIONS.items():
        if key in q:
            expanded += " " + value
    return expand_with_synonyms(expanded)


def _hf_model_cached(model_name: str) -> bool:
    cache_name = f"models--{model_name.replace('/', '--')}"
    candidates = [
        Path.home() / ".cache" / "huggingface" / "hub" / cache_name,
        Path.home() / ".cache" / "torch" / "sentence_transformers" / model_name.replace("/", "_"),
    ]
    return any(path.exists() for path in candidates)


@lru_cache(maxsize=2)
def _embedding_function():
    try:
        from chromadb.utils import embedding_functions
    except Exception:
        return None
    provider = settings.embedding_provider.lower()
    if provider == "openai":
        if not settings.openai_api_key:
            return None
        try:
            return embedding_functions.OpenAIEmbeddingFunction(
                api_key=settings.openai_api_key, model_name=settings.openai_embedding_model
            )
        except Exception:
            return None
    if provider == "local":
        if settings.local_models_offline and not _hf_model_cached(settings.local_embedding_model):
            return None
        import os

        os.environ.setdefault("USE_TF", "0")
        os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
        try:
            return embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name=settings.local_embedding_model
            )
        except Exception:
            return None
    return None


def _passes_filters(
    meta: dict[str, Any],
    source_filter: str | None,
    topic_filter: str | None,
    library_filter: str | None = None,
    training_phase: str | None = None,
    clinical_context: str | None = None,
) -> bool:
    if library_filter and library_filter.lower() != meta.get("library", "").lower():
        return False
    if training_phase and training_phase.lower() != meta.get("training_phase", "").lower():
        return False
    if clinical_context and clinical_context.lower() not in meta.get("clinical_context", "").lower():
        return False
    if source_filter and all(
        source_filter.lower() not in str(meta.get(field, "")).lower()
        for field in ("book", "source_name", "filename")
    ):
        return False
    if topic_filter and all(
        topic_filter.lower() not in str(meta.get(field, "")).lower()
        for field in ("topic_tags", "keyword_tags", "synonym_tags", "retrieval_tags", "section")
    ):
        return False
    return True


@lru_cache(maxsize=1)
def _chroma_collection_cached(chroma_dir_str: str, collection_name: str, ef_id: int):
    try:
        import chromadb
    except Exception:
        return None
    try:
        client = chromadb.PersistentClient(path=chroma_dir_str)
        return client.get_collection(collection_name, embedding_function=_embedding_function())
    except Exception:
        return None


def _chroma_collection():
    chroma_sqlite = Path(settings.chroma_dir) / "chroma.sqlite3"
    if not chroma_sqlite.exists():
        return None
    ef = _embedding_function()
    if ef is None:
        return None
    return _chroma_collection_cached(
        str(settings.chroma_dir),
        settings.vector_collection_name(),
        id(ef),
    )


def chroma_candidates(
    query: str,
    n: int = 30,
    source_filter: str | None = None,
    topic_filter: str | None = None,
    library_filter: str | None = None,
    training_phase: str | None = None,
    clinical_context: str | None = None,
) -> list[dict[str, Any]]:
    col = _chroma_collection()
    if col is None:
        return []
    try:
        res = col.query(query_texts=[query], n_results=n)
    except Exception:
        return []
    json_by_id = {row["id"]: row for row in load_json_chunks()}
    rows = []
    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]
    ids = res.get("ids", [[]])[0]
    distances = res.get("distances", [[]])[0] or [0.0] * len(docs)
    for doc, meta, cid, dist in zip(docs, metas, ids, distances):
        if not _passes_filters(meta, source_filter, topic_filter, library_filter, training_phase, clinical_context):
            continue
        source_row = json_by_id.get(cid, {})
        rows.append(
            {
                "id": cid,
                "text": source_row.get("text", doc),
                "search_text": source_row.get("search_text", doc),
                "metadata": meta,
                "vector_score": 1.0 / (1.0 + max(0.0, float(dist))),
                "retrieval_method": "vector",
            }
        )
    return rows


_TERM_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9-]{2,}")


@lru_cache(maxsize=4)
def _chunk_term_index(path_str: str, mtime_ns: int, size: int) -> list[tuple[dict[str, Any], frozenset[str]]]:
    """Pre-tokenize every chunk's search_text once per process.

    Returns parallel list of (row, term_set). The keyword scorer can then do
    a set-intersection without re-running findall+lower per query.
    """
    rows = _load_json_chunks_cached(path_str, mtime_ns, size)
    out: list[tuple[dict[str, Any], frozenset[str]]] = []
    for row in rows:
        text = row.get("search_text") or row.get("text", "")
        meta = row.get("metadata") or {}
        # Add the SOURCE DOCUMENT's identity to the chunk's searchable terms.
        #
        # Chunking splits an article into pieces that no longer name their own
        # subject: the "Treatment / Management" chunks of the StatPearls STEMI
        # article open mid-sentence ("elevation, is proportional with infarct
        # size...") and say "STEMI" nowhere — only 3 of 21 carried the word at
        # all. The management content was therefore unreachable by a query
        # naming the disease, which is exactly how a reader asks for it.
        #
        # The document title is a legitimate relevance signal for every chunk
        # taken from it, and this costs one extra tokenization at load time —
        # no re-embedding and no reindex, since this index is built from
        # chunks.jsonl per process.
        doc_ident = " ".join(
            str(meta.get(k, "")) for k in ("source_name", "book", "section", "topic_tags")
        )
        terms_set = frozenset(
            t.lower() for t in _TERM_RE.findall(text + " " + doc_ident)
        )
        out.append((row, terms_set))
    return out


def _term_index() -> list[tuple[dict[str, Any], frozenset[str]]]:
    path = settings.chroma_dir / "chunks.jsonl"
    if not path.exists():
        return []
    stat = path.stat()
    return _chunk_term_index(str(path), stat.st_mtime_ns, stat.st_size)


def keyword_candidates(
    query: str,
    n: int = 40,
    source_filter: str | None = None,
    topic_filter: str | None = None,
    library_filter: str | None = None,
    training_phase: str | None = None,
    clinical_context: str | None = None,
) -> list[dict[str, Any]]:
    q_terms = frozenset(t.lower() for t in _TERM_RE.findall(query))
    if not q_terms:
        return []
    q_norm = math.sqrt(len(q_terms))
    scored: list[tuple[float, dict[str, Any]]] = []
    for row, doc_terms in _term_index():
        meta = row.get("metadata", {})
        if not _passes_filters(meta, source_filter, topic_filter, library_filter, training_phase, clinical_context):
            continue
        overlap = len(q_terms & doc_terms)
        if overlap == 0:
            continue
        score = overlap / q_norm
        scored.append((score, row))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [{**row, "vector_score": 0.0, "retrieval_method": "keyword"} for _, row in scored[:n]]


@lru_cache(maxsize=4)
def _phrase_index_cached(path_str: str, mtime_ns: int, size: int) -> dict[str, list[int]]:
    """Map phrase -> list of row indices in load_json_chunks() containing it.

    Built once per chunks.jsonl mtime change. Lets exact_phrase_candidates
    do dict lookups instead of iterating 60k rows per query.
    """
    rows = _load_json_chunks_cached(path_str, mtime_ns, size)
    all_phrases = list(EXACT_PHRASES) + ["treatment of last", "intralipid", "local anesthetic toxicity"]
    index: dict[str, list[int]] = {p: [] for p in all_phrases}
    for i, row in enumerate(rows):
        text = (row.get("search_text") or row.get("text", "") or "").lower()
        if not text:
            continue
        for p in all_phrases:
            if p in text:
                index[p].append(i)
    return index


def _phrase_index() -> tuple[dict[str, list[int]], list[dict[str, Any]]]:
    path = settings.chroma_dir / "chunks.jsonl"
    if not path.exists():
        return {}, []
    stat = path.stat()
    return (
        _phrase_index_cached(str(path), stat.st_mtime_ns, stat.st_size),
        _load_json_chunks_cached(str(path), stat.st_mtime_ns, stat.st_size),
    )


def exact_phrase_candidates(
    query: str,
    source_filter: str | None = None,
    topic_filter: str | None = None,
    library_filter: str | None = None,
    training_phase: str | None = None,
    clinical_context: str | None = None,
) -> list[dict[str, Any]]:
    phrases = []
    q = query.lower()
    for phrase in EXACT_PHRASES:
        if phrase in q:
            phrases.append(phrase)
    if re.search(r"\bLAST\b", query) or "last treatment" in q or "local anesthetic" in q:
        phrases.extend(["treatment of last", "intralipid", "local anesthetic toxicity"])
    if not phrases:
        return []
    index, rows_all = _phrase_index()
    matched_idxs: set[int] = set()
    for p in phrases:
        for i in index.get(p, []):
            matched_idxs.add(i)
    rows: list[dict[str, Any]] = []
    for i in matched_idxs:
        row = rows_all[i]
        meta = row.get("metadata", {})
        if not _passes_filters(meta, source_filter, topic_filter, library_filter, training_phase, clinical_context):
            continue
        rows.append({**row, "vector_score": 0.0, "retrieval_method": "exact"})
        if len(rows) >= 200:
            break
    return rows


def retrieval_confidence(results: list[SourceChunk]) -> str:
    if not results:
        return "low"
    top = results[0].score
    if top >= 0.75 or (len(results) >= 3 and top >= 0.55):
        return "high"
    if top >= 0.35 or len(results) >= 2:
        return "medium"
    return "low"


# A leading "Section: <title>" header. The title runs to the first period, or to
# the end of the string when the chunk is nothing BUT a header.
_SECTION_HEADER = re.compile(r'^\s*Section:\s*[^.]*(?:\.\s*)?', re.I)


# "Source: StatPearls NCBI Bookshelf NBK ID: NBK545267 URL: https://... Topic: X"
# — ingest prepended this to many StatPearls chunks. It is pure provenance.
_CITATION_HEADER = re.compile(
    r'^\s*(?:Section:\s*)?(?:Source:\s*)?[\w ]{0,40}?'
    r'NCBI Bookshelf\s*NBK ID:\s*\w+\s*URL:\s*\S+\s*(?:Topic:\s*)?',
    re.I,
)


def _strip_citation_header(text: str) -> str:
    """Remove a leading bibliographic header from a chunk body."""
    t = (text or "").lstrip()
    # Collapse the doubled "Section: Source: StatPearls. Source: StatPearls"
    # that ingest produced before the real header.
    t = re.sub(r'^\s*Section:\s*Source:\s*[\w ]{0,40}?\.\s*', '', t, flags=re.I)
    stripped = _CITATION_HEADER.sub('', t).lstrip()
    # Never strip a chunk down to nothing — if the header WAS the whole chunk,
    # keep the original and let _is_contentless decide.
    return stripped if len(stripped) >= 40 else t


def _is_contentless(text: str) -> bool:
    """True for chunks that are pure section headings with no teaching content.

    Ingest emitted ~1,800 of these ("Section: Atrial Fibrillation & Flutter",
    "Section: Summary of EKG Changes"). They are actively harmful rather than
    merely useless: BM25 normalises by document length, so a 38-character
    heading whose every token matches the query outscores the real passage —
    one of these took a top-3 slot on "afib RVR rate control" with bm25 18.7,
    displacing content that could actually be taught from.

    Short chunks containing a digit are kept: dose and threshold lines
    ("Propofol 1.5-2 mg/kg IV") are legitimately terse.
    """
    t = (text or "").strip()
    if not t:
        return True
    body = _SECTION_HEADER.sub("", t).strip()
    if not body:
        return True
    if any(ch.isdigit() for ch in body):
        return False
    return len(body) < 30


def hybrid_search(
    query: str,
    mode: str = "broad_explain",
    source_filter: str | None = None,
    topic_filter: str | None = None,
    library_filter: str | None = None,
    training_phase: str | None = None,
    clinical_context: str | None = None,
    max_results: int = 8,
    use_cross_encoder: bool = False,
) -> tuple[list[SourceChunk], bool]:
    if not query or not query.strip():
        return [], True
    expanded_query = expand_query(query)
    raw = chroma_candidates(
        expanded_query,
        source_filter=source_filter,
        topic_filter=topic_filter,
        library_filter=library_filter,
        training_phase=training_phase,
        clinical_context=clinical_context,
    )
    raw.extend(
        keyword_candidates(
            expanded_query,
            source_filter=source_filter,
            topic_filter=topic_filter,
            library_filter=library_filter,
            training_phase=training_phase,
            clinical_context=clinical_context,
        )
    )
    raw.extend(
        exact_phrase_candidates(
            query,
            source_filter=source_filter,
            topic_filter=topic_filter,
            library_filter=library_filter,
            training_phase=training_phase,
            clinical_context=clinical_context,
        )
    )
    dedup: dict[str, dict[str, Any]] = {}
    for r in raw:
        if _is_contentless(r.get("text", "")):
            continue
        dedup.setdefault(r["id"], r)
        if r.get("retrieval_method") != dedup[r["id"]].get("retrieval_method"):
            dedup[r["id"]]["retrieval_method"] = "hybrid"
    ranked = rerank(expanded_query, list(dedup.values()), mode=mode, topic_filter=topic_filter, use_cross_encoder=use_cross_encoder)
    results: list[SourceChunk] = []
    for r in ranked[:max_results]:
        meta = r.get("metadata", {})
        tags = [t for t in meta.get("topic_tags", "").split(",") if t]
        source_name = meta.get("source_name") or meta.get("book", "")
        # Trim the bibliographic header before the 1000-char window, so the
        # excerpt the tutor teaches from opens on medicine rather than on
        # "Source: StatPearls NCBI Bookshelf NBK ID: NBK545267 URL: ...".
        # Provenance is preserved — it travels in source_name/book, not the body.
        excerpt = _strip_citation_header(r["text"])[:1000]
        results.append(
            SourceChunk(
                text=excerpt,
                excerpt=excerpt,
                book=source_name,
                source_name=source_name,
                source=source_name,
                library=meta.get("library", ""),
                training_phase=meta.get("training_phase", ""),
                clinical_context=meta.get("clinical_context", ""),
                filename=meta.get("filename", ""),
                page=meta.get("page"),
                section=meta.get("section", ""),
                topic_tags=tags,
                score=round(float(r.get("final_score", 0.0)), 4),
                retrieval_method=r.get("retrieval_method", ""),
                vector_score=round(float(r.get("vector_score", 0.0)), 4),
                bm25_score=round(float(r.get("bm25_score", 0.0)), 4),
                reranker_score=None if r.get("reranker_score") is None else round(float(r.get("reranker_score", 0.0)), 4),
                chunk_id=meta.get("chunk_id", r.get("id", "")),
            )
        )
    confidence = retrieval_confidence(results)
    insufficient = confidence == "low"
    return results, insufficient
