"""Cloze deletion generator.

Each ingested fact yields 1-4 cloze cards by masking high-yield spans:
- Numeric+unit (doses, vital sign thresholds): yields a "dose" cloze
- Drug names from the medical lexicon: "drug" cloze
- Disease/condition terms (-itis/-osis/-emia/etc.): "condition" cloze
- Lab/abbreviation tokens (MAC, ECG, etc.): "label" cloze

The user is forced into specific recall (dose vs drug vs mechanism vs
indication) rather than a single "do you know this fact" gate. Anki users
get 5-10× more learning per fact this way.

Storage: `storage/curriculum/cloze_cards.jsonl`. Each card references
`source_fact_id`. Curriculum/voice_shaper consumes them by unit_id.

CLI:
    python -m src.cloze                      # rebuild deck from chunks.jsonl
    python -m src.cloze --max-per-fact 6
    python -m src.cloze --probe "Calcium gluconate 1 g IV stabilizes the cardiac membrane in hyperkalemia."
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, asdict
from functools import lru_cache
from pathlib import Path
from typing import Iterable

from .config import settings


# Curated drug-name list for cloze masking. Broader than the seed synonyms
# but excluding adjectives/conditions ("hepatic", "ischemia", "hemorrhage")
# that the dedupe medical_lexicon mixes in.
DRUG_NAMES: set[str] = {
    # Anesthesia induction / sedation
    "propofol", "etomidate", "ketamine", "midazolam", "lorazepam", "diazepam",
    "fentanyl", "remifentanil", "sufentanil", "alfentanil", "morphine", "hydromorphone",
    "dexmedetomidine", "thiopental",
    # Neuromuscular blockers
    "succinylcholine", "rocuronium", "vecuronium", "cisatracurium", "atracurium",
    "pancuronium", "mivacurium",
    # Reversal
    "sugammadex", "neostigmine", "glycopyrrolate", "atropine", "edrophonium",
    # Local anesthetics
    "lidocaine", "bupivacaine", "ropivacaine", "mepivacaine", "tetracaine",
    "chloroprocaine", "procaine", "intralipid",
    # Volatiles
    "sevoflurane", "desflurane", "isoflurane", "halothane", "enflurane",
    # Vasopressors / inotropes
    "epinephrine", "norepinephrine", "vasopressin", "phenylephrine", "ephedrine",
    "dopamine", "dobutamine", "milrinone", "isoproterenol", "levosimendan",
    # Antihypertensives / antiarrhythmics
    "labetalol", "metoprolol", "esmolol", "propranolol", "carvedilol",
    "diltiazem", "verapamil", "amlodipine", "nicardipine", "clevidipine",
    "nitroglycerin", "nitroprusside", "hydralazine", "amiodarone", "lidocaine",
    "adenosine", "digoxin", "ibutilide",
    # Diuretics / electrolytes
    "furosemide", "bumetanide", "torsemide", "spironolactone", "hydrochlorothiazide",
    "calcium", "magnesium", "potassium", "sodium", "bicarbonate", "insulin",
    "dextrose", "glucagon",
    # Antibiotics
    "vancomycin", "ceftriaxone", "cefepime", "cefazolin", "cefotaxime",
    "ciprofloxacin", "levofloxacin", "azithromycin", "clarithromycin",
    "metronidazole", "piperacillin", "tazobactam", "meropenem", "imipenem",
    "ertapenem", "linezolid", "daptomycin", "clindamycin", "doxycycline",
    "ampicillin", "amoxicillin", "fluconazole", "voriconazole", "amphotericin",
    "trimethoprim", "sulfamethoxazole", "oseltamivir",
    # Anticoagulation
    "heparin", "enoxaparin", "warfarin", "apixaban", "rivaroxaban", "dabigatran",
    "argatroban", "bivalirudin", "fondaparinux",
    # Antiplatelet
    "aspirin", "clopidogrel", "ticagrelor", "prasugrel",
    # GI / hepatic
    "lactulose", "rifaximin", "octreotide", "pantoprazole", "esomeprazole",
    "famotidine", "ondansetron", "metoclopramide", "prochlorperazine",
    # Pulmonary
    "albuterol", "ipratropium", "salmeterol", "tiotropium", "budesonide",
    "fluticasone", "methylprednisolone", "prednisone", "hydrocortisone",
    "dexamethasone",
    # Endocrine / pain
    "levothyroxine", "propylthiouracil", "methimazole", "vasopressin",
    "naloxone", "flumazenil", "acetaminophen", "ibuprofen", "ketorolac",
    "gabapentin", "pregabalin", "haloperidol", "olanzapine", "quetiapine",
    # MH / crisis
    "dantrolene", "sodium",
    # Anti-emetic / steroid
    "methylene", "thiamine",
}


@lru_cache(maxsize=1)
def _drug_pattern_cached() -> "re.Pattern":
    drugs = sorted({d for d in DRUG_NAMES if d.isalpha() and len(d) >= 5}, key=len, reverse=True)
    if not drugs:
        return re.compile(r"\bxxxx\b")
    return re.compile(r"\b(?:" + "|".join(re.escape(d) for d in drugs) + r")\b", re.I)


CLOZE_DIR = "curriculum"
CLOZE_FILE = "cloze_cards.jsonl"

DOSE_RE = re.compile(
    r"\b\d+(?:\.\d+)?(?:\s*[-–]\s*\d+(?:\.\d+)?)?\s*"
    r"(?:mg|mcg|µg|ug|ml|l/min|mmHg|mEq|mmol|kg|cmH2O|%|hr|min|sec|bpm|fr|gauge|units?|iu|g)"
    r"(?:/kg|/min|/hr|/day|/dose)?\b",
    re.I,
)

CONDITION_RE = re.compile(
    r"\b\w{4,}(?:itis|osis|emia|uria|opathy|algia|pnea|plasia|trophy|emia)\b",
    re.I,
)

ABBREV_RE = re.compile(
    r"\b(?:ECG|EEG|EKG|ABG|VBG|MRI|CT|TTE|TEE|RSI|PEEP|FiO2|MAC|CPR|ACLS|ICU|OR|PACU|PCA|RVR|STEMI|NSTEMI|ACS|COPD|ARDS|AKI|CKD|DKA|SIADH|GIB|UTI|PE|DVT|HIT|TTP|DIC|PTT|INR|VTE|TIA|CVA|ICH|SAH|ICP|CPP|GA|LMA|ETT|TOF|LAST|MH|CICO|PDPH|CVP|MAP|SVR|PVR|RSBI|SBT|OLV)\b"
)

# Sentence segmentation
SENT_SPLIT_RE = re.compile(r"(?<=[\.!\?])\s+(?=[A-Z0-9])")


@dataclass
class ClozeCard:
    card_id: str
    source_fact_id: str
    book: str
    page: int | None
    section: str
    library: str
    topic_tags: list[str]
    chapter_title: str
    masked_text: str
    answer: str
    mask_type: str  # 'dose' | 'drug' | 'condition' | 'label'


def _drug_pattern() -> "re.Pattern":
    return _drug_pattern_cached()


def _hash(*parts: str) -> str:
    return hashlib.sha1("||".join(parts).encode("utf-8")).hexdigest()[:14]


def _generate_for_sentence(
    sent: str,
    fact_id: str,
    drug_re: re.Pattern,
    max_clozes: int = 4,
) -> Iterable[ClozeCard]:
    sent = sent.strip()
    if len(sent) < 25:
        return
    # Fact extractor strips trailing punctuation, so we don't require it.
    # We just need a sentence-like span with enough word content to be testable.
    if len(re.findall(r"[A-Za-z]+", sent)) < 5:
        return

    used_spans: set[tuple[int, int]] = set()
    cards: list[ClozeCard] = []

    def overlaps(span: tuple[int, int]) -> bool:
        return any(not (span[1] <= u[0] or span[0] >= u[1]) for u in used_spans)

    placeholders = {
        "dose": "[DOSE]",
        "drug": "[DRUG NAME]",
        "condition": "[CONDITION]",
        "label": "[ABBREVIATION]",
    }

    def emit(span: tuple[int, int], answer: str, mask_type: str) -> None:
        if overlaps(span):
            return
        used_spans.add(span)
        masked = sent[: span[0]] + placeholders[mask_type] + sent[span[1] :]
        cards.append(
            ClozeCard(
                card_id="cloze-" + _hash(fact_id, mask_type, str(span[0]), answer.lower()),
                source_fact_id=fact_id,
                book="",
                page=None,
                section="",
                library="",
                topic_tags=[],
                chapter_title="",
                masked_text=masked,
                answer=answer,
                mask_type=mask_type,
            )
        )

    # Order: structural patterns (dose, condition suffix, abbreviation) before
    # lexicon-based drug match — otherwise conditions like "encephalopathy"
    # get tagged as drug because they appear in the medical lexicon.
    for m in DOSE_RE.finditer(sent):
        emit((m.start(), m.end()), m.group(0), "dose")
        if len(cards) >= max_clozes:
            break

    if len(cards) < max_clozes:
        for m in CONDITION_RE.finditer(sent):
            emit((m.start(), m.end()), m.group(0), "condition")
            if len(cards) >= max_clozes:
                break

    if len(cards) < max_clozes:
        for m in ABBREV_RE.finditer(sent):
            emit((m.start(), m.end()), m.group(0), "label")
            if len(cards) >= max_clozes:
                break

    if len(cards) < max_clozes:
        for m in drug_re.finditer(sent):
            emit((m.start(), m.end()), m.group(0), "drug")
            if len(cards) >= max_clozes:
                break

    yield from cards


def generate_clozes(
    fact_text: str,
    fact_id: str,
    max_per_fact: int = 4,
) -> list[ClozeCard]:
    drug_re = _drug_pattern()
    out: list[ClozeCard] = []
    for sent in SENT_SPLIT_RE.split(fact_text.strip()):
        for card in _generate_for_sentence(sent, fact_id, drug_re, max_clozes=max_per_fact):
            out.append(card)
            if len(out) >= max_per_fact:
                return out
    return out


def cloze_path() -> Path:
    return Path(settings.chroma_dir).parent / CLOZE_DIR / CLOZE_FILE


def build_deck(max_per_fact: int = 4) -> dict:
    """Build cloze deck. Re-tag each card by its OWN sentence content via
    topic_taxonomy, not the parent chunk's tags — prevents off-topic cards
    from being served under the wrong unit's topic."""
    from .topic_taxonomy import tag_topics

    chunks_path = settings.chroma_dir / "chunks.jsonl"
    if not chunks_path.exists():
        raise SystemExit(f"chunks.jsonl not found: {chunks_path}")
    out_path = cloze_path()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    drug_re = _drug_pattern()

    by_type: dict[str, int] = {"dose": 0, "drug": 0, "condition": 0, "label": 0}
    n_facts = 0
    n_cards = 0
    n_dropped_offtopic = 0
    with chunks_path.open("r", encoding="utf-8") as src, out_path.open("w", encoding="utf-8") as dst:
        for line in src:
            try:
                row = json.loads(line)
            except Exception:
                continue
            meta = row.get("metadata") or {}
            if meta.get("chunk_type") != "fact":
                continue
            n_facts += 1
            fact_text = row.get("text") or meta.get("fact_text") or ""
            if not fact_text:
                continue
            fact_id = row.get("id") or meta.get("chunk_id", "")
            parent_tags = [t.strip() for t in (meta.get("topic_tags") or "").split(",") if t.strip()]
            for sent in SENT_SPLIT_RE.split(fact_text.strip()):
                for card in _generate_for_sentence(sent, fact_id, drug_re, max_clozes=max_per_fact):
                    card.book = meta.get("source_name") or meta.get("book", "")
                    card.page = meta.get("page")
                    card.section = meta.get("section", "")
                    card.library = meta.get("library", "")
                    card.chapter_title = meta.get("chapter_title", "") or ""
                    # Per-sentence retag: a chunk on Hyperkalemia may have a
                    # sentence about hypoglycemia. Keep parent tags only if
                    # the sentence content actually mentions them.
                    sent_tags = tag_topics(sent)
                    card.topic_tags = sent_tags or parent_tags
                    dst.write(json.dumps(asdict(card), ensure_ascii=False) + "\n")
                    by_type[card.mask_type] = by_type.get(card.mask_type, 0) + 1
                    n_cards += 1
    return {
        "facts_seen": n_facts,
        "cards_emitted": n_cards,
        "by_type": by_type,
        "path": str(out_path),
    }


def load_deck() -> list[ClozeCard]:
    path = cloze_path()
    if not path.exists():
        return []
    out: list[ClozeCard] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            out.append(ClozeCard(**d))
    return out


def deck_by_unit_topic_tag() -> dict[str, list[ClozeCard]]:
    """Index loaded cards by their first topic tag (matches CurriculumUnit.topic_tags[0])."""
    by_topic: dict[str, list[ClozeCard]] = {}
    for card in load_deck():
        if not card.topic_tags:
            continue
        by_topic.setdefault(card.topic_tags[0], []).append(card)
    return by_topic


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-per-fact", type=int, default=4)
    parser.add_argument("--probe", type=str)
    args = parser.parse_args()
    if args.probe:
        cards = generate_clozes(args.probe, "probe-fact", max_per_fact=args.max_per_fact)
        for c in cards:
            print(f"[{c.mask_type}] {c.masked_text}    -> {c.answer}")
        return
    summary = build_deck(max_per_fact=args.max_per_fact)
    print("cloze deck built:")
    for k, v in summary.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
