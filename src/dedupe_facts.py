"""Post-process pass over chunks.jsonl that:

1. Applies a medical-content gate (drops boilerplate, chapter meta, "see Table"
   pointers) without dropping borderline real teaching prose.
2. Exact-hashes facts on aggressively normalized text and keeps one canonical
   per hash, preferring the book whose library is the spine for the topic.
3. Within each book, runs shingle-based Jaccard near-dedupe at 0.90 to drop
   reformatted summary boxes.

Run after ingestion (so we don't have to re-ingest just to dedupe). Backs up
the original `chunks.jsonl` and rewrites it with `dedupe_metadata` injected
into each surviving fact's metadata. Also deletes dropped IDs from Chroma.

CLI:
    python -m src.dedupe_facts                  # full pass
    python -m src.dedupe_facts --dry-run        # report only, don't rewrite
    python -m src.dedupe_facts --no-near-dedupe # skip Jaccard pass (faster)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from .config import settings


# ---------- normalization ----------

LEAD_NOISE_RE = re.compile(
    r"^\s*("
    r"pearl:|note:|key point:?|remember:?|warning:?|caution:?|"
    r"clinical scenario:?|important:?|"
    r"\d+[\.\)]\s+|"  # numbered list markers
    r"[•\*\-]\s+"  # bullets
    r")",
    re.I,
)

REF_INSIDE_RE = re.compile(
    r"\((?:see\s+(?:chapter|section|table|figure|fig\.?)\s*[\d.]+(?:[a-z])?)\)",
    re.I,
)
SECTION_HEADER_RE = re.compile(r"^\s*\d+(\.\d+)*\s+[a-z]", re.I)


def normalize_for_hash(text: str) -> str:
    text = text.strip()
    text = REF_INSIDE_RE.sub("", text)
    text = LEAD_NOISE_RE.sub("", text)
    text = re.sub(r"[\s ]+", " ", text)
    text = text.strip(" -:;,.•\t")
    return text.lower()


def shingles(text: str, k: int = 5) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    if len(tokens) < k:
        return {" ".join(tokens)} if tokens else set()
    return {" ".join(tokens[i : i + k]) for i in range(len(tokens) - k + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------- medical-content gate ----------

DOSE_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:mg|mcg|µg|ug|ml|l/min|mmHg|mEq|mmol|kg|cmH2O|%|hr|min|sec|bpm|fr|gauge|units?|iu)\b",
    re.I,
)
MEDICAL_SUFFIX_RE = re.compile(
    r"\b\w{4,}(?:itis|osis|emia|uria|opathy|algia|otomy|ostomy|ectomy|plasty|lysis|gram)\b",
    re.I,
)
ABBREV_RE = re.compile(r"\b(?:ECG|EEG|EKG|ABG|MRI|CT|VBG|TTE|TEE|RSI|PEEP|FiO2|MAC|CPR|ACLS|ICU|OR|PACU|PCA|PTH|TSH)\b")
BOILERPLATE_RE = re.compile(
    r"^\s*(?:in this|this chapter|this section|this book|the following|"
    r"as discussed|as mentioned|see (?:also|chapter|section|table|figure|fig\.?)|"
    r"figure \d+|table \d+|note that|please note|the authors?|"
    r"the goal of this|in summary,?\s*$|"
    r"acknowledg|copyright|all rights reserved|reproduced with|"
    r"www\.|http|edited by|chapter \d+|"
    r"published by|isbn|first edition|second edition|third edition)",
    re.I,
)
ENDING_PUNCT_RE = re.compile(r"[\.\?!]$")


def _seed_medical_lexicon() -> set[str]:
    """Tiny seed lexicon — anything from topic_taxonomy keywords plus crisis vocab."""
    from .topic_taxonomy import TOPICS

    lex: set[str] = set()
    for keywords in TOPICS.values():
        for kw in keywords:
            for tok in re.findall(r"[a-zA-Z]{4,}", kw):
                lex.add(tok.lower())
    extras = {
        "propofol", "etomidate", "ketamine", "midazolam", "fentanyl", "remifentanil",
        "rocuronium", "vecuronium", "succinylcholine", "cisatracurium", "sugammadex",
        "neostigmine", "glycopyrrolate", "lidocaine", "bupivacaine", "ropivacaine",
        "dantrolene", "intralipid", "sevoflurane", "desflurane", "isoflurane",
        "epinephrine", "norepinephrine", "vasopressin", "phenylephrine", "ephedrine",
        "dobutamine", "milrinone", "nitroprusside", "nicardipine", "labetalol",
        "metoprolol", "esmolol", "diltiazem", "amiodarone", "adenosine",
        "calcium", "insulin", "dextrose", "lactulose", "rifaximin", "ceftriaxone",
        "vancomycin", "azithromycin", "ciprofloxacin", "piperacillin", "tazobactam",
        "heparin", "enoxaparin", "warfarin", "apixaban", "rivaroxaban",
        "albuterol", "ipratropium", "magnesium", "potassium", "sodium", "bicarbonate",
        "naloxone", "flumazenil", "thiamine", "haloperidol", "dexmedetomidine",
        "intubation", "extubation", "anesthesia", "analgesia", "sedation",
        "hypoxemia", "hypoxia", "hypotension", "hypertension", "tachycardia",
        "bradycardia", "arrhythmia", "shock", "sepsis", "ards", "pneumothorax",
        "tamponade", "embolism", "infarction", "ischemia", "hemorrhage",
        "transfusion", "coagulation", "thrombosis", "hyperkalemia", "hyponatremia",
        "hypernatremia", "hypoglycemia", "hyperglycemia", "ketoacidosis",
        "ventilation", "oxygenation", "perfusion", "compliance", "resistance",
        "preload", "afterload", "contractility", "stroke", "seizure", "delirium",
        "withdrawal", "encephalopathy", "cirrhosis", "ascites", "varices",
        "pancreatitis", "cholecystitis", "appendicitis", "diverticulitis",
    }
    lex.update(extras)
    return lex


_MED_LEX: set[str] | None = None


def medical_lexicon() -> set[str]:
    global _MED_LEX
    if _MED_LEX is None:
        _MED_LEX = _seed_medical_lexicon()
    return _MED_LEX


def is_medical_fact(text: str) -> bool:
    """Loose gate: drop only obvious boilerplate. Recall > precision per user goal."""
    if not text or len(text) < 12:
        return False
    if BOILERPLATE_RE.match(text):
        return False
    if not ENDING_PUNCT_RE.search(text) and len(text) < 30:
        # very short fragments without sentence punctuation are usually nav text
        return False
    if DOSE_RE.search(text):
        return True
    if MEDICAL_SUFFIX_RE.search(text):
        return True
    if ABBREV_RE.search(text):
        return True
    tokens = set(re.findall(r"[a-z]{4,}", text.lower()))
    if tokens & medical_lexicon():
        return True
    # Generic fallback: a sentence with >=8 alphabetic tokens and ending punctuation
    # is probably medical prose, not navigation.
    return len([t for t in re.findall(r"[a-zA-Z]+", text) if len(t) >= 3]) >= 8


# ---------- source preference for canonical pick ----------

SPINE_RANK = {
    "Intern Notes / Survival Guide": 100,
    "OnlineMedEd Intern Guide": 95,
    "MGH Housestaff Manual": 92,
    "Hospitalist / Intern Guide": 90,
    "Marino ICU Book": 88,
    "Stanford CA-1": 86,
    "Morgan & Mikhail": 70,
    "Miller/Baby Miller": 65,
}


def canonical_priority(source_name: str) -> int:
    return SPINE_RANK.get(source_name, 50)


# ---------- main pass ----------

def _iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line)
            except Exception:
                continue


def _write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    n = 0
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            n += 1
    return n


def _delete_chroma_ids(ids: list[str]) -> bool:
    if not ids:
        return True
    try:
        import chromadb
    except Exception:
        return False
    try:
        client = chromadb.PersistentClient(path=str(settings.chroma_dir))
        col = client.get_collection(settings.vector_collection_name())
    except Exception:
        return False
    for i in range(0, len(ids), 1000):
        try:
            col.delete(ids=ids[i : i + 1000])
        except Exception:
            return False
    return True


def run(
    drop_non_medical: bool = True,
    near_dedupe: bool = True,
    dry_run: bool = False,
    near_threshold: float = 0.90,
) -> dict[str, Any]:
    chunks_path = settings.chroma_dir / "chunks.jsonl"
    if not chunks_path.exists():
        raise SystemExit(f"chunks.jsonl not found at {chunks_path}")

    t0 = time.time()
    rows = list(_iter_jsonl(chunks_path))
    facts = [r for r in rows if (r.get("metadata") or {}).get("chunk_type") == "fact"]
    passages = [r for r in rows if (r.get("metadata") or {}).get("chunk_type") != "fact"]

    n_initial = len(facts)
    dropped_non_medical: list[str] = []
    survived_after_gate: list[dict[str, Any]] = []

    if drop_non_medical:
        for fact in facts:
            text = fact.get("text") or fact.get("metadata", {}).get("fact_text") or ""
            if is_medical_fact(text):
                survived_after_gate.append(fact)
            else:
                dropped_non_medical.append(fact["id"])
    else:
        survived_after_gate = facts

    # Exact dedupe
    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for fact in survived_after_gate:
        text = fact.get("text") or fact.get("metadata", {}).get("fact_text") or ""
        norm = normalize_for_hash(text)
        if not norm:
            continue
        h = hashlib.sha1(norm.encode("utf-8")).hexdigest()[:16]
        fact["metadata"]["fact_norm_hash"] = h
        by_hash[h].append(fact)

    canonical: list[dict[str, Any]] = []
    dropped_exact: list[str] = []
    for h, group in by_hash.items():
        if len(group) == 1:
            canonical.append(group[0])
            continue
        group_sorted = sorted(
            group,
            key=lambda r: (
                -canonical_priority(r["metadata"].get("source_name") or r["metadata"].get("book", "")),
                int(r["metadata"].get("page") or 0),
            ),
        )
        winner = group_sorted[0]
        winner["metadata"]["dedupe_alternates"] = ",".join(
            f"{r['metadata'].get('book','')}|p{r['metadata'].get('page','')}"
            for r in group_sorted[1:]
        )
        canonical.append(winner)
        dropped_exact.extend(r["id"] for r in group_sorted[1:])

    # Within-book Jaccard near-dedupe
    dropped_near: list[str] = []
    if near_dedupe:
        by_book: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for fact in canonical:
            book = fact["metadata"].get("source_name") or fact["metadata"].get("book", "")
            by_book[book].append(fact)

        kept_in_book: list[dict[str, Any]] = []
        for book, items in by_book.items():
            with_shingles: list[tuple[dict[str, Any], set[str]]] = []
            length_buckets: dict[int, list[int]] = defaultdict(list)
            for fact in items:
                text = fact.get("text") or ""
                sh = shingles(text)
                with_shingles.append((fact, sh))
                bucket = max(1, len(sh) // 5)
                length_buckets[bucket].append(len(with_shingles) - 1)

            killed: set[int] = set()
            for bucket, idxs in length_buckets.items():
                idxs_set = []
                for offset in (-1, 0, 1):
                    idxs_set.extend(length_buckets.get(bucket + offset, []))
                idxs_set = sorted(set(idxs_set))
                for ai in idxs_set:
                    if ai in killed:
                        continue
                    a_fact, a_sh = with_shingles[ai]
                    if not a_sh:
                        continue
                    for bi in idxs_set:
                        if bi <= ai or bi in killed:
                            continue
                        b_fact, b_sh = with_shingles[bi]
                        if jaccard(a_sh, b_sh) >= near_threshold:
                            loser_idx = bi
                            killed.add(loser_idx)
                            dropped_near.append(with_shingles[loser_idx][0]["id"])

            kept_in_book.extend(f for i, (f, _) in enumerate(with_shingles) if i not in killed)
        canonical = kept_in_book

    # Tag the survivors
    for fact in canonical:
        fact["metadata"]["is_canonical_fact"] = True

    summary = {
        "input_facts": n_initial,
        "dropped_non_medical": len(dropped_non_medical),
        "dropped_exact_dupe": len(dropped_exact),
        "dropped_near_dupe": len(dropped_near),
        "canonical_facts": len(canonical),
        "passages": len(passages),
        "elapsed_s": round(time.time() - t0, 1),
    }

    if dry_run:
        return summary

    backup = chunks_path.with_suffix(".jsonl.predupe.bak")
    if not backup.exists():
        shutil.copy2(chunks_path, backup)

    new_rows = passages + canonical
    _write_jsonl(chunks_path, new_rows)

    drop_ids = dropped_non_medical + dropped_exact + dropped_near
    chroma_ok = _delete_chroma_ids(drop_ids) if drop_ids else True
    summary["chroma_delete_ok"] = chroma_ok
    summary["wrote"] = str(chunks_path)
    summary["backup"] = str(backup)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-medical-gate", action="store_true")
    parser.add_argument("--no-near-dedupe", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.90)
    args = parser.parse_args()
    summary = run(
        drop_non_medical=not args.no_medical_gate,
        near_dedupe=not args.no_near_dedupe,
        dry_run=args.dry_run,
        near_threshold=args.threshold,
    )
    print("dedupe_facts summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
