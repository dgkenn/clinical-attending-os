#!/usr/bin/env python3
"""
generate_kp_graph.py  — Knowledge-Point Generation Pipeline
============================================================
Turns curriculum topics into ATOMIC knowledge points grounded in the corpus,
in priority order, and writes them to data/kp_catalog.json for seeding into
the tutor.

CRITICAL: Do NOT run without --mock while the corpus ingest is running.
          The real-run path calls src.retrieval.hybrid_search (corpus touch)
          and an LM Studio endpoint; both are skipped entirely in --mock mode.

Usage (mock validation — safe while ingest is running):
    python -m scripts.generate_kp_graph --mock --limit 8

Usage (real run — AFTER corpus ingest completes):
    LMSTUDIO_BASE_URL=http://localhost:1234/v1 \\
    KP_GEN_MODEL=lmstudio-community/Llama-3.2-3B-Instruct-GGUF \\
    python -m scripts.generate_kp_graph --limit 50 --tier 1

Filters:
    --tier 1|2|3          Only process topics of this priority_tier
    --discipline medicine|anesthesia
    --topics-from db|blueprint   Source of topic list (default: db, falls back to blueprint)
    --limit N              Process at most N topics (0 = all)
    --top-k N              Corpus chunks to retrieve per topic (default 8)
    --kps-per-topic N      Target KPs to generate per topic (default 5)
    --out PATH             Output catalog path (default data/kp_catalog.json)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import unicodedata
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Repo root on sys.path so we can `from src.X import Y` after ingest
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# ---------------------------------------------------------------------------
# Canonical output paths (D: for large temps per disk policy)
# ---------------------------------------------------------------------------
DEFAULT_OUT = _REPO_ROOT / "data" / "kp_catalog.json"
PROGRESS_LOG = _REPO_ROOT / "data" / "kp_generation_progress.jsonl"
BLUEPRINT_PATH = _REPO_ROOT / "data" / "curriculum_blueprint.json"

# ---------------------------------------------------------------------------
# Diagnosis-category heuristics (for illness_script trigger)
# ---------------------------------------------------------------------------
_DX_CATEGORY_RE = re.compile(
    r"\b(diagnosis|diagnos|approach to|evaluation of|workup|differential|"
    r"syndrome|disease|disorder|failure|crisis|emergency|toxicity|"
    r"insufficiency|infarct|arrest|bleed|shock)\b",
    re.IGNORECASE,
)

_DIAGNOSIS_DOMAINS = {
    "internal medicine: cardiology",
    "internal medicine: nephrology",
    "internal medicine: pulmonology",
    "internal medicine: gastroenterology",
    "internal medicine: endocrinology",
    "internal medicine: hematology",
    "internal medicine: neurology",
    "internal medicine: icu & critical care",
    "internal medicine: infectious disease",
}


def _is_diagnosis_topic(topic: str, category: str, domain: str) -> bool:
    """Return True if this topic should receive an illness_script."""
    if category == "presentation":
        return True
    if _DX_CATEGORY_RE.search(topic):
        return True
    dom_lower = domain.lower()
    if any(d in dom_lower for d in _DIAGNOSIS_DOMAINS):
        return True
    return False


# ---------------------------------------------------------------------------
# Priority ordering — mirror get_next_topic rules from src/mcp_endpoints.py
# ---------------------------------------------------------------------------

def _priority_key(row: dict[str, Any]) -> tuple:
    """
    Sort key for processing order (ascending = first processed):
      1. Presentation 'Approach to X' + critical-care first  (0 before 1)
      2. priority_tier ASC (1 < 2 < 3)
      3. discipline: medicine before anesthesia (0 < 1)
      4. high_yield DESC  (high_yield=1 → 0, so comes first)
    """
    is_presentation = 1 if row.get("category", "topic") == "presentation" else 0
    is_cc = 0 if row.get("is_critical_care", 0) else 1  # CC first → 0
    # Among presentations: CC presentations beat non-CC
    pres_first = 0 if (is_presentation and not is_cc) else (0 if (is_presentation and is_cc == 0) else 1)
    # Mirroring the get_next_topic three-pass approach:
    # pass 0 = presentation (any), pass 1 = CC non-presentation, pass 2 = non-CC
    if row.get("category") == "presentation":
        pass_bucket = 0
    elif row.get("is_critical_care", 0):
        pass_bucket = 1
    else:
        pass_bucket = 2

    tier = int(row.get("priority_tier", 2))
    disc_order = 0 if str(row.get("discipline", "medicine")).lower() == "medicine" else 1
    hy_order = 0 if row.get("high_yield", 1) else 1   # high_yield=1 → 0 (first)

    return (pass_bucket, tier, disc_order, hy_order, row.get("topic", ""))


# ---------------------------------------------------------------------------
# Stem normalisation for dedup
# ---------------------------------------------------------------------------

def _norm_stem(stem: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace for dedup."""
    s = unicodedata.normalize("NFKD", stem or "").lower()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _kp_dedup_key(topic: str, stem: str) -> str:
    raw = f"{topic.strip().lower()}||{_norm_stem(stem)}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Load existing catalog + build dedup index
# ---------------------------------------------------------------------------

def _load_catalog(path: Path) -> tuple[list[dict], set[str]]:
    """Return (items, dedup_key_set). Handles missing/empty/corrupt files."""
    if not path.exists():
        return [], set()
    try:
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            return [], set()
        items = json.loads(raw)
        if not isinstance(items, list):
            items = []
    except Exception as exc:
        print(f"[WARN] Could not read existing catalog ({exc}). Starting fresh.")
        return [], set()
    keys = {_kp_dedup_key(it.get("topic", ""), it.get("stem", "")) for it in items}
    return items, keys


def _save_catalog(path: Path, items: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Progress log (JSONL — one record per processed topic)
# ---------------------------------------------------------------------------

def _log_progress(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _load_done_topics(path: Path) -> set[str]:
    """Topics already successfully processed (from progress log)."""
    if not path.exists():
        return set()
    done: set[str] = set()
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
                if rec.get("status") == "done":
                    done.add(rec["topic"])
            except Exception:
                pass
    return done


# ---------------------------------------------------------------------------
# Topic loading — from DB or blueprint JSON
# ---------------------------------------------------------------------------

def _load_topics_from_db(filters: dict) -> list[dict]:
    """Read curriculum table from the student-model SQLite DB."""
    from src.config import settings  # type: ignore
    db_path = str(settings.sqlite_db_path)
    try:
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        q = "SELECT topic, domain, discipline, is_critical_care, high_yield, priority_tier, category FROM curriculum WHERE 1=1"
        params: list[Any] = []
        if filters.get("tier"):
            q += " AND priority_tier = ?"
            params.append(int(filters["tier"]))
        if filters.get("discipline"):
            q += " AND discipline = ?"
            params.append(filters["discipline"])
        rows = con.execute(q, params).fetchall()
        con.close()
        return [dict(r) for r in rows]
    except Exception as exc:
        print(f"[WARN] DB load failed ({exc}). Falling back to blueprint.")
        return []


def _load_topics_from_blueprint(filters: dict) -> list[dict]:
    """Load topics from the curriculum_blueprint.json file."""
    if not BLUEPRINT_PATH.exists():
        print(f"[ERROR] Blueprint not found at {BLUEPRINT_PATH}")
        return []
    data = json.loads(BLUEPRINT_PATH.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "topics" in data:
        data = data["topics"]
    rows = []
    for item in data:
        tier = int(item.get("priority_tier", 2))
        disc = str(item.get("discipline", "")).strip()
        if not disc:
            dom = str(item.get("domain", "")).lower()
            disc = "medicine" if ("internal medicine" in dom or "general internal medicine" in dom) else "anesthesia"
        if filters.get("tier") and tier != int(filters["tier"]):
            continue
        if filters.get("discipline") and disc != filters["discipline"]:
            continue
        rows.append({
            "topic": str(item.get("topic", "")),
            "domain": str(item.get("domain", "")),
            "discipline": disc,
            "is_critical_care": 1 if item.get("is_critical_care") else 0,
            "high_yield": 1 if item.get("high_yield", True) else 0,
            "priority_tier": tier,
            "category": str(item.get("category", "topic")),
        })
    return rows


# ---------------------------------------------------------------------------
# Mock retrieval + mock LLM  (--mock mode only, no corpus/network touch)
# ---------------------------------------------------------------------------

class MockSourceChunk:
    def __init__(self, text: str, book: str, page: int, score: float):
        self.text = text
        self.book = book
        self.page = page
        self.score = score


_MOCK_CHUNKS: list[MockSourceChunk] = [
    MockSourceChunk(
        text="Hyperkalemia: peaked T waves are the earliest ECG change. Calcium gluconate stabilises the membrane. Insulin + dextrose shifts K into cells. Treatment sequence: calcium → insulin/glucose → sodium bicarbonate → kayexalate → dialysis.",
        book="Morgan & Mikhail",
        page=1886,
        score=0.92,
    ),
    MockSourceChunk(
        text="Septic shock: first-line vasopressor is norepinephrine targeting MAP ≥65 mmHg. Add vasopressin 0.04 U/min when NE ≥5–15 mcg/min to spare catecholamines. Obtain blood cultures BEFORE antibiotics if possible.",
        book="Marino ICU Book",
        page=543,
        score=0.88,
    ),
    MockSourceChunk(
        text="Malignant hyperthermia: triggered by volatile agents + succinylcholine. Hypercarbia is the earliest sign. Treatment: stop trigger, give dantrolene 2.5 mg/kg IV (repeat to max 10 mg/kg), active cooling, treat hyperkalemia and acidosis.",
        book="Morgan & Mikhail",
        page=982,
        score=0.85,
    ),
    MockSourceChunk(
        text="Approach to chest pain: immediate ECG within 10 min, troponin, consider aortic dissection (BP differential, wide mediastinum), PE (Wells criteria), and cardiac tamponade. High-risk features: diaphoresis, radiation, hypotension, ST elevation.",
        book="MGH Housestaff Manual",
        page=42,
        score=0.83,
    ),
    MockSourceChunk(
        text="ARDS Berlin criteria: P/F ratio <300 mild, <200 moderate, <100 severe — all within 1 week of known insult, bilateral opacities not fully explained by effusions or collapse, not fully explained by cardiac failure. Lung-protective ventilation: Vt 6 mL/kg IBW, plateau <30 cmH2O.",
        book="Miller/Baby Miller",
        page=766,
        score=0.80,
    ),
]


def _mock_retrieve(topic: str, top_k: int) -> list[MockSourceChunk]:
    """Return a deterministic mock retrieval result (no corpus access)."""
    # Rotate chunks to make output vary per topic
    h = int(hashlib.md5(topic.encode()).hexdigest(), 16) % len(_MOCK_CHUNKS)
    rotated = _MOCK_CHUNKS[h:] + _MOCK_CHUNKS[:h]
    return rotated[:min(top_k, len(rotated))]


def _mock_generate_kps(
    topic: str,
    domain: str,
    discipline: str,
    category: str,
    chunks: list[MockSourceChunk],
    kps_per_topic: int,
    is_dx: bool,
) -> dict[str, Any]:
    """
    Deterministic mock KP generator — produces well-formed KPs from chunk 0
    text without any LLM/network call. Validates schema in --mock mode.
    """
    # Generate a stable set of mock KPs (up to kps_per_topic)
    kps: list[dict] = []
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")

    stems_and_answers = [
        (
            f"What is the MOST IMPORTANT immediate step in managing {topic}?",
            f"Based on corpus: {chunks[0].text[:120]}..." if chunks else f"Key action for {topic}.",
        ),
        (
            f"What pathophysiologic mechanism underlies {topic}?",
            f"Mechanism: see {chunks[0].book if chunks else 'source'} p{chunks[0].page if chunks else '?'}.",
        ),
        (
            f"Which finding distinguishes {topic} from its closest mimic?",
            f"Discriminating feature: derived from retrieved context on {topic}.",
        ),
        (
            f"In {topic}, when would you escalate to a higher level of care?",
            f"Escalation trigger: haemodynamic instability, failure of first-line therapy.",
        ),
        (
            f"What is the dosing/target parameter for first-line treatment of {topic}?",
            f"Dose/target: as per {chunks[0].book if chunks else 'reference'} — see rationale.",
        ),
    ]

    bloom_cycle = ["recall", "apply", "analyze", "apply", "recall"]

    for i, (stem, answer) in enumerate(stems_and_answers[:kps_per_topic]):
        src = [{"book": c.book, "page": c.page} for c in chunks[:2]] if chunks else []
        kp_id = f"{slug}-{i+1:02d}"
        kps.append({
            "id": kp_id,
            "topic": topic,
            "domain": domain,
            "discipline": discipline,
            "stem": stem,
            "answer": answer,
            "rationale": f"Grounded in retrieved chunks from {', '.join(c.book for c in chunks[:2])}." if chunks else "Rationale placeholder.",
            "bloom": bloom_cycle[i % len(bloom_cycle)],
            "source": src,
            "confusable_with": "",
        })

    illness_script = None
    if is_dx:
        illness_script = {
            "topic": topic,
            "enabling_conditions": f"Mock: who gets {topic}? (age, comorbidities, exposures)",
            "pathophysiology": f"Mock: mechanism — drawn from chunk text: {chunks[0].text[:80]}..." if chunks else "Mechanism TBD.",
            "time_course": f"Mock: onset/progression pattern for {topic}.",
            "key_features": f"Mock: discriminating signs/labs/imaging for {topic}.",
            "consequence_if_missed": f"Mock: worst-case outcome if {topic} is not recognised/treated.",
        }

    confusable_pairs: list[dict] = []
    if len(kps) >= 3:
        # Generate one mock confusable pair from the third KP
        confusable_pairs.append({
            "topic_a": topic,
            "topic_b": f"{topic} mimic (mock)",
            "discriminator": kps[2]["stem"],
        })

    return {
        "kps": kps,
        "illness_script": illness_script,
        "confusable_pairs": confusable_pairs,
    }


# ---------------------------------------------------------------------------
# Real LLM generation via OpenAI-compatible endpoint (LM Studio)
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """\
You are a medical education expert generating ATOMIC knowledge points for a clinical tutor.
Each knowledge point must be grounded ONLY in the provided corpus chunks.
Output valid JSON — no prose, no markdown fences, no extra keys.
"""

_KP_SCHEMA_EXAMPLE = {
    "kps": [
        {
            "id": "SLUG-NN",
            "topic": "...",
            "domain": "...",
            "discipline": "medicine|anesthesia",
            "stem": "Question stem — does NOT reveal the answer; tests ONE atomic fact.",
            "answer": "Trigger -> action/value, complete and self-contained.",
            "rationale": "Why this is correct (mechanism or evidence, 1-3 sentences).",
            "bloom": "recall|apply|analyze",
            "source": [{"book": "...", "page": 0}],
            "confusable_with": "Entity or concept this is most often confused with (or empty string).",
        }
    ],
    "illness_script": {
        "topic": "...",
        "enabling_conditions": "Who gets it? (demographics, risk factors, exposures)",
        "pathophysiology": "Core mechanism in 1-2 sentences.",
        "time_course": "Onset, progression, duration.",
        "key_features": "Discriminating signs/symptoms/labs/imaging.",
        "consequence_if_missed": "Worst outcome if not recognised/treated promptly.",
    },
    "confusable_pairs": [
        {"topic_a": "...", "topic_b": "...", "discriminator": "Key feature that separates them."}
    ],
}


def _build_user_prompt(
    topic: str,
    domain: str,
    discipline: str,
    category: str,
    chunks: list,
    kps_per_topic: int,
    is_dx: bool,
) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    chunk_text = "\n\n".join(
        f"[Chunk {i+1} | {c.book} p{c.page} | score={c.score:.2f}]\n{c.text}"
        for i, c in enumerate(chunks)
    )

    dx_note = (
        "Because this is a DIAGNOSIS/PRESENTATION topic, also produce an illness_script "
        "with all 5 fields (enabling_conditions, pathophysiology, time_course, key_features, "
        "consequence_if_missed). If NOT a diagnosis topic, set illness_script to null."
    )
    confusable_note = (
        "Produce 0-2 confusable_pairs entries for entities/conditions this topic is commonly "
        "confused with. If none apply, leave the array empty."
    )

    return f"""\
Topic: {topic}
Domain: {domain}
Discipline: {discipline}
Category: {category}

CORPUS CHUNKS (grounding source — cite only books/pages that appear here):
{chunk_text}

TASK:
Generate exactly {kps_per_topic} atomic knowledge points for this topic.
Rules:
- Each KP tests ONE fact (not a list).
- stem must NOT reveal the answer.
- answer must be complete and self-contained (trigger -> action/value).
- bloom: recall (memorise a value/fact), apply (use in a clinical scenario), analyze (compare/contrast/deduce).
- source: cite only books and pages visible in the chunk headers above.
- Use id format "{slug}-NN" (zero-padded sequential, e.g. "{slug}-01").
- discipline must be exactly "medicine" or "anesthesia".
{dx_note}
{confusable_note}

Output ONLY the JSON object matching this schema (no prose, no markdown):
{json.dumps(_KP_SCHEMA_EXAMPLE, indent=2)}
"""


def _call_lmstudio(prompt: str, base_url: str, model: str, temperature: float = 0.2) -> Optional[dict]:
    """
    Call an OpenAI-compatible local endpoint (LM Studio).
    Returns parsed JSON dict or None on failure.
    """
    try:
        import urllib.request
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": _SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": temperature,
            "max_tokens": 4096,
        }).encode("utf-8")
        req = urllib.request.Request(
            f"{base_url.rstrip('/')}/chat/completions",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        content = body["choices"][0]["message"]["content"].strip()
        # Strip markdown fences if the model adds them
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
        return json.loads(content)
    except Exception as exc:
        print(f"  [LLM ERROR] {exc}")
        return None


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------

_VALID_BLOOM = {"recall", "apply", "analyze"}
_VALID_DISC = {"medicine", "anesthesia"}


def _validate_kp(kp: dict) -> list[str]:
    """Return list of validation errors (empty = valid)."""
    errs = []
    for field in ("id", "topic", "stem", "answer", "rationale", "bloom", "discipline"):
        if not kp.get(field):
            errs.append(f"Missing/empty field: {field}")
    if kp.get("bloom") and kp["bloom"] not in _VALID_BLOOM:
        errs.append(f"Invalid bloom: {kp['bloom']!r} — must be recall|apply|analyze")
    if kp.get("discipline") and kp["discipline"] not in _VALID_DISC:
        errs.append(f"Invalid discipline: {kp['discipline']!r}")
    src = kp.get("source", [])
    if not isinstance(src, list):
        errs.append("source must be a list")
    else:
        for s in src:
            if not isinstance(s, dict) or "book" not in s:
                errs.append(f"source entry missing 'book': {s!r}")
    return errs


def _validate_illness_script(is_: dict) -> list[str]:
    errs = []
    for field in ("topic", "enabling_conditions", "pathophysiology", "time_course",
                  "key_features", "consequence_if_missed"):
        if not is_.get(field):
            errs.append(f"illness_script missing/empty: {field}")
    return errs


# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------

def run(args: argparse.Namespace) -> None:
    out_path = Path(args.out)
    mock = args.mock
    top_k = args.top_k
    kps_per_topic = args.kps_per_topic
    limit = args.limit
    filters = {"tier": args.tier, "discipline": args.discipline}

    # --- LM Studio config (real run only) ---
    base_url = os.environ.get("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
    model = os.environ.get("KP_GEN_MODEL", "local-model")

    if not mock:
        print(f"[INFO] Real-run mode. LM Studio: {base_url}  Model: {model}")
        print("[INFO] Loading retrieval module (corpus must be ready)...")
        from src.retrieval import hybrid_search as _real_hybrid_search  # type: ignore
    else:
        _real_hybrid_search = None
        print("[MOCK] Running in mock mode — no corpus or LLM access.")

    # --- Load topic list ---
    source = getattr(args, "topics_from", "db")
    rows: list[dict] = []
    if source != "blueprint":
        rows = _load_topics_from_db(filters)
    if not rows:
        rows = _load_topics_from_blueprint(filters)

    if not rows:
        print("[ERROR] No topics loaded. Check DB or blueprint path.")
        sys.exit(1)

    # Apply priority sort
    rows.sort(key=_priority_key)

    # Apply limit
    if limit and limit > 0:
        rows = rows[:limit]

    # --- Load existing catalog (resumability) ---
    catalog, dedup_keys = _load_catalog(out_path)
    done_topics = _load_done_topics(PROGRESS_LOG)

    print(f"\n[INFO] Topics to process: {len(rows)}")
    print(f"[INFO] Existing catalog entries: {len(catalog)}")
    print(f"[INFO] Already-done topics (from progress log): {len(done_topics)}")
    print("\n=== PROCESSING ORDER ===")
    for i, r in enumerate(rows):
        cc_marker = " [CC]" if r.get("is_critical_care") else ""
        pres_marker = " [PRES]" if r.get("category") == "presentation" else ""
        print(f"  {i+1:3d}. [{r.get('discipline','?')[:4]}] tier={r.get('priority_tier','?')} hy={r.get('high_yield','?')}{cc_marker}{pres_marker}  {r['topic']}")
    print("=" * 60)

    # --- Processing loop ---
    new_kps_added = 0
    topics_processed = 0
    topics_skipped = 0

    for row in rows:
        topic = row["topic"]
        domain = row.get("domain", "")
        discipline = row.get("discipline", "medicine")
        category = row.get("category", "topic")

        if topic in done_topics:
            print(f"  [SKIP] Already done: {topic}")
            topics_skipped += 1
            continue

        is_dx = _is_diagnosis_topic(topic, category, domain)
        print(f"\n  [PROCESS] {topic} (dx={is_dx}, disc={discipline}, tier={row.get('priority_tier')})")

        # --- Retrieval ---
        if mock:
            chunks = _mock_retrieve(topic, top_k)
        else:
            try:
                sources, _insufficient = _real_hybrid_search(topic, mode="broad_explain", max_results=top_k)
                chunks = sources
            except Exception as exc:
                print(f"  [RETRIEVAL ERROR] {exc}. Skipping topic.")
                _log_progress(PROGRESS_LOG, {
                    "topic": topic, "status": "error", "error": str(exc),
                    "ts": datetime.now(timezone.utc).isoformat(),
                })
                continue

        print(f"    Retrieved {len(chunks)} chunks.")

        # --- Generation ---
        if mock:
            result = _mock_generate_kps(topic, domain, discipline, category, chunks, kps_per_topic, is_dx)
        else:
            prompt = _build_user_prompt(topic, domain, discipline, category, chunks, kps_per_topic, is_dx)
            result = _call_lmstudio(prompt, base_url, model)
            if result is None:
                print(f"  [GEN ERROR] LLM returned None. Skipping.")
                _log_progress(PROGRESS_LOG, {
                    "topic": topic, "status": "llm_error",
                    "ts": datetime.now(timezone.utc).isoformat(),
                })
                continue

        # --- Merge KPs with dedup ---
        raw_kps = result.get("kps", [])
        illness_script = result.get("illness_script")
        confusable_pairs = result.get("confusable_pairs", [])

        added_this_topic = 0
        for kp in raw_kps:
            # Ensure required fields default gracefully
            kp.setdefault("topic", topic)
            kp.setdefault("domain", domain)
            kp.setdefault("discipline", discipline)
            kp.setdefault("source", [])
            kp.setdefault("confusable_with", "")
            kp.setdefault("bloom", "recall")
            kp.setdefault("id", f"{re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')}-{uuid.uuid4().hex[:6]}")

            # Validate schema
            errs = _validate_kp(kp)
            if errs:
                print(f"    [SCHEMA WARN] KP {kp.get('id','?')}: {'; '.join(errs)}")

            # Dedup
            dk = _kp_dedup_key(kp["topic"], kp.get("stem", ""))
            if dk in dedup_keys:
                print(f"    [DEDUP] Skipping duplicate: {kp.get('id','?')}")
                continue
            dedup_keys.add(dk)
            catalog.append(kp)
            added_this_topic += 1

        # Validate and attach illness_script inline with each KP (stored as metadata)
        # ALSO store illness_script as a top-level entry with a special sentinel key
        if illness_script and is_dx:
            is_errs = _validate_illness_script(illness_script)
            if is_errs:
                print(f"    [IS WARN] illness_script: {'; '.join(is_errs)}")
            else:
                print(f"    [OK] illness_script validated for: {topic}")
            # Attach illness_script to catalog as a typed entry
            is_entry = {
                "_type": "illness_script",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                **illness_script,
            }
            # Dedup illness_scripts by topic
            is_dk = _kp_dedup_key(f"_illness_script_{topic}", topic)
            if is_dk not in dedup_keys:
                dedup_keys.add(is_dk)
                catalog.append(is_entry)

        # Attach confusable pairs
        for cp in confusable_pairs:
            cp_dk = _kp_dedup_key(f"_confusable_{cp.get('topic_a','')}_{cp.get('topic_b','')}", cp.get("discriminator", ""))
            if cp_dk not in dedup_keys:
                dedup_keys.add(cp_dk)
                cp["_type"] = "confusable_pair"
                catalog.append(cp)

        print(f"    Added {added_this_topic} KPs (illness_script={'yes' if illness_script and is_dx else 'no'})")
        new_kps_added += added_this_topic
        topics_processed += 1

        # Persist after each topic (crash-safe)
        _save_catalog(out_path, catalog)
        _log_progress(PROGRESS_LOG, {
            "topic": topic,
            "status": "done",
            "kps_added": added_this_topic,
            "is_dx": is_dx,
            "illness_script": illness_script is not None and is_dx,
            "ts": datetime.now(timezone.utc).isoformat(),
        })

    # --- Final summary ---
    print(f"\n=== GENERATION COMPLETE ===")
    print(f"  Topics processed : {topics_processed}")
    print(f"  Topics skipped   : {topics_skipped}  (resumability)")
    print(f"  New KPs added    : {new_kps_added}")
    print(f"  Total catalog    : {len([e for e in catalog if e.get('stem')])} KPs + "
          f"{len([e for e in catalog if e.get('_type') == 'illness_script'])} illness_scripts + "
          f"{len([e for e in catalog if e.get('_type') == 'confusable_pair'])} confusable_pairs")
    print(f"  Catalog path     : {out_path.resolve()}")
    print(f"  Progress log     : {PROGRESS_LOG.resolve()}")

    if mock:
        print("\n=== REAL-RUN COMMAND (after corpus ingest completes) ===")
        print(
            "LMSTUDIO_BASE_URL=http://localhost:1234/v1 \\\n"
            "KP_GEN_MODEL=lmstudio-community/Llama-3.2-3B-Instruct-GGUF \\\n"
            "python -m scripts.generate_kp_graph \\\n"
            "    --topics-from db \\\n"
            "    --tier 1 \\\n"
            "    --top-k 8 \\\n"
            "    --kps-per-topic 5 \\\n"
            "    --limit 0\n"
            "\n"
            "# For a larger model (better quality, slower):\n"
            "KP_GEN_MODEL=lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF \\\n"
            "# Or any model loaded in LM Studio — check http://localhost:1234/v1/models"
        )

    # Final JSON parse check
    try:
        reparsed = json.loads(out_path.read_text(encoding="utf-8"))
        assert isinstance(reparsed, list)
        print(f"\n[VALIDATE] Catalog JSON parses OK: {len(reparsed)} entries.")
    except Exception as exc:
        print(f"\n[VALIDATE ERROR] Catalog JSON did not parse: {exc}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate atomic knowledge points from curriculum topics (KP graph pipeline).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--mock", action="store_true",
                   help="Run with mock retrieval + mock LLM (safe during corpus ingest).")
    p.add_argument("--limit", type=int, default=0,
                   help="Process at most N topics (0 = all). Default: 0.")
    p.add_argument("--tier", type=int, default=0, choices=[0, 1, 2, 3],
                   help="Filter by priority_tier (0 = all tiers). Default: 0.")
    p.add_argument("--discipline", type=str, default="",
                   choices=["", "medicine", "anesthesia"],
                   help="Filter by discipline. Default: both.")
    p.add_argument("--topics-from", dest="topics_from", type=str,
                   default="db", choices=["db", "blueprint"],
                   help="Source of topic list: 'db' (curriculum table) or 'blueprint' JSON. Default: db.")
    p.add_argument("--top-k", dest="top_k", type=int, default=8,
                   help="Number of corpus chunks to retrieve per topic. Default: 8.")
    p.add_argument("--kps-per-topic", dest="kps_per_topic", type=int, default=5,
                   help="Target number of KPs to generate per topic. Default: 5.")
    p.add_argument("--out", type=str, default=str(DEFAULT_OUT),
                   help=f"Output catalog path. Default: {DEFAULT_OUT}")
    return p.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args()
    if not args.mock:
        print(
            "\n[SAFETY] You are about to run REAL generation (corpus + LLM access).\n"
            "  This touches the Chroma corpus. Ensure ingest is complete first.\n"
            "  Press Ctrl-C within 5 seconds to abort, or wait to continue...\n"
        )
        import time
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            print("Aborted.")
            sys.exit(0)
    run(args)
