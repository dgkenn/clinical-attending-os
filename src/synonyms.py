"""Medical synonym expansion for query-time retrieval.

Bundled seed table covers the highest-yield drug brand→generic mappings,
common medical abbreviations, and symptom/condition aliases. The retrieval
layer calls `expand_with_synonyms(query)` to add likely source-side
vocabulary without an LLM round-trip.

Optional extension: drop a JSON map at `data/synonyms_extra.json` to add
custom entries without code changes. Format:
    {"alias": "canonical name [optional comma-separated other forms]"}

For deeper coverage, run `python -m src.synonyms --import-rxnorm <RXNCONSO.RRF>`
to fold in the public-domain NIH RxNorm drug name table.
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Iterable

from .config import settings


# ---------- bundled seed (curated, high-yield) ----------

SEED_SYNONYMS: dict[str, str] = {
    # Cardiology
    "afib": "atrial fibrillation",
    "a fib": "atrial fibrillation",
    "a-fib": "atrial fibrillation",
    "rvr": "rapid ventricular response",
    "vfib": "ventricular fibrillation",
    "v fib": "ventricular fibrillation",
    "vt": "ventricular tachycardia",
    "svt": "supraventricular tachycardia",
    "mi": "myocardial infarction",
    "stemi": "ST elevation myocardial infarction",
    "nstemi": "non-ST elevation myocardial infarction",
    "acs": "acute coronary syndrome",
    "chf": "congestive heart failure",
    "hfref": "heart failure with reduced ejection fraction",
    "hfpef": "heart failure with preserved ejection fraction",
    "pe": "pulmonary embolism",
    "dvt": "deep vein thrombosis",
    "av block": "atrioventricular block",
    "lbbb": "left bundle branch block",
    "rbbb": "right bundle branch block",
    "lvh": "left ventricular hypertrophy",
    "as": "aortic stenosis",
    "ar": "aortic regurgitation",
    "ms": "mitral stenosis",
    "mr": "mitral regurgitation",
    "ai": "aortic insufficiency",
    # Pulmonary
    "copd": "chronic obstructive pulmonary disease",
    "ards": "acute respiratory distress syndrome",
    "cap": "community acquired pneumonia",
    "hap": "hospital acquired pneumonia",
    "vap": "ventilator associated pneumonia",
    "olv": "one lung ventilation",
    "sob": "shortness of breath dyspnea",
    "fev1": "forced expiratory volume in one second",
    "fvc": "forced vital capacity",
    "frc": "functional residual capacity",
    "rsbi": "rapid shallow breathing index",
    "sbt": "spontaneous breathing trial",
    "peep": "positive end expiratory pressure",
    "fio2": "fraction of inspired oxygen",
    "v/q": "ventilation perfusion ratio",
    "vq mismatch": "ventilation perfusion mismatch",
    # Renal / fluids
    "aki": "acute kidney injury",
    "ckd": "chronic kidney disease",
    "esrd": "end stage renal disease",
    "crrt": "continuous renal replacement therapy",
    "hd": "hemodialysis",
    "rrt": "renal replacement therapy",
    "fena": "fractional excretion of sodium",
    "ats": "acute tubular necrosis",
    "atn": "acute tubular necrosis",
    "ain": "acute interstitial nephritis",
    # Endocrine
    "dka": "diabetic ketoacidosis",
    "hhs": "hyperosmolar hyperglycemic state",
    "siadh": "syndrome of inappropriate antidiuretic hormone",
    "tsh": "thyroid stimulating hormone",
    "t3": "triiodothyronine",
    "t4": "thyroxine",
    "ptu": "propylthiouracil",
    # GI
    "gi bleed": "gastrointestinal bleed hematemesis melena",
    "ugib": "upper gastrointestinal bleed",
    "lgib": "lower gastrointestinal bleed",
    "sbp": "spontaneous bacterial peritonitis",
    "he": "hepatic encephalopathy",
    "tips": "transjugular intrahepatic portosystemic shunt",
    "ibd": "inflammatory bowel disease",
    "uc": "ulcerative colitis",
    # ID / sepsis
    "uti": "urinary tract infection",
    "sirs": "systemic inflammatory response syndrome",
    "sepsis 3": "sepsis-3 sofa qsofa",
    "qsofa": "quick sequential organ failure assessment",
    "sofa": "sequential organ failure assessment",
    # Heme / onc / coag
    "hit": "heparin induced thrombocytopenia",
    "ttp": "thrombotic thrombocytopenic purpura",
    "dic": "disseminated intravascular coagulation",
    "ptt": "partial thromboplastin time",
    "inr": "international normalized ratio",
    "vte": "venous thromboembolism",
    "doac": "direct oral anticoagulant",
    "noac": "non-vitamin K oral anticoagulant",
    # Neuro
    "ams": "altered mental status",
    "loc": "level of consciousness loss of consciousness",
    "tia": "transient ischemic attack",
    "cva": "cerebrovascular accident stroke",
    "ich": "intracerebral hemorrhage",
    "sah": "subarachnoid hemorrhage",
    "icp": "intracranial pressure",
    "cpp": "cerebral perfusion pressure",
    # Anesthesia / OR
    "ga": "general anesthesia",
    "mac": "minimum alveolar concentration",
    "rsi": "rapid sequence induction",
    "lma": "laryngeal mask airway",
    "ett": "endotracheal tube",
    "etco2": "end tidal carbon dioxide",
    "spo2": "oxygen saturation",
    "abg": "arterial blood gas",
    "vbg": "venous blood gas",
    "tee": "transesophageal echocardiogram",
    "tte": "transthoracic echocardiogram",
    "or": "operating room",
    "pacu": "post anesthesia care unit",
    "ponv": "postoperative nausea and vomiting",
    "tof": "train of four",
    "last": "local anesthetic systemic toxicity",
    "mh": "malignant hyperthermia",
    "cico": "cannot intubate cannot oxygenate",
    "pdph": "post dural puncture headache",
    "olp": "one lung physiology",
    # Crisis / ICU
    "icu": "intensive care unit",
    "rrt team": "rapid response team",
    "code blue": "cardiac arrest CPR ACLS",
    "acls": "advanced cardiac life support",
    "bls": "basic life support",
    "rosc": "return of spontaneous circulation",
    "ecmo": "extracorporeal membrane oxygenation",
    "vv ecmo": "venovenous ECMO",
    "va ecmo": "venoarterial ECMO",
    "iabp": "intra-aortic balloon pump",
    "cvp": "central venous pressure",
    "co": "cardiac output",
    "svr": "systemic vascular resistance",
    "pvr": "pulmonary vascular resistance",
    "map": "mean arterial pressure",
    # Drug brand → generic (high yield in US wards)
    "lasix": "furosemide",
    "ativan": "lorazepam",
    "valium": "diazepam",
    "versed": "midazolam",
    "fentanyl patch": "fentanyl transdermal",
    "dilaudid": "hydromorphone",
    "morphine sulfate": "morphine",
    "narcan": "naloxone",
    "romazicon": "flumazenil",
    "zofran": "ondansetron",
    "compazine": "prochlorperazine",
    "haldol": "haloperidol",
    "precedex": "dexmedetomidine",
    "diprivan": "propofol",
    "ketalar": "ketamine",
    "amidate": "etomidate",
    "anectine": "succinylcholine",
    "sux": "succinylcholine",
    "roc": "rocuronium",
    "vec": "vecuronium",
    "esmeron": "rocuronium",
    "nimbex": "cisatracurium",
    "bridion": "sugammadex",
    "robinul": "glycopyrrolate",
    "neo": "phenylephrine neostigmine",
    "levo": "levophed norepinephrine",
    "levophed": "norepinephrine",
    "dopa": "dopamine",
    "dobut": "dobutamine",
    "primacor": "milrinone",
    "epi": "epinephrine adrenaline",
    "vaso": "vasopressin",
    "pitressin": "vasopressin",
    "nipride": "nitroprusside sodium nitroprusside",
    "tridil": "nitroglycerin",
    "ntg": "nitroglycerin",
    "labetalol iv": "labetalol intravenous",
    "trandate": "labetalol",
    "cardene": "nicardipine",
    "brevibloc": "esmolol",
    "lopressor": "metoprolol",
    "toprol": "metoprolol",
    "cardizem": "diltiazem",
    "cordarone": "amiodarone",
    "pacerone": "amiodarone",
    "adenocard": "adenosine",
    "lidocaine bolus": "lidocaine intravenous",
    "lopressor iv": "metoprolol intravenous",
    "heparin gtt": "heparin infusion",
    "lovenox": "enoxaparin",
    "fragmin": "dalteparin",
    "coumadin": "warfarin",
    "eliquis": "apixaban",
    "xarelto": "rivaroxaban",
    "pradaxa": "dabigatran",
    "plavix": "clopidogrel",
    "brilinta": "ticagrelor",
    "asa": "aspirin acetylsalicylic acid",
    "tylenol": "acetaminophen",
    "motrin": "ibuprofen",
    "advil": "ibuprofen",
    "toradol": "ketorolac",
    "celebrex": "celecoxib",
    "neurontin": "gabapentin",
    "lyrica": "pregabalin",
    "ancef": "cefazolin",
    "rocephin": "ceftriaxone",
    "zosyn": "piperacillin tazobactam piperacillin-tazobactam",
    "vanco": "vancomycin",
    "cipro": "ciprofloxacin",
    "levaquin": "levofloxacin",
    "flagyl": "metronidazole",
    "bactrim": "trimethoprim sulfamethoxazole TMP-SMX",
    "tmp smx": "trimethoprim sulfamethoxazole",
    "augmentin": "amoxicillin clavulanate",
    "zithromax": "azithromycin",
    "z pak": "azithromycin",
    "claforan": "cefotaxime",
    "merrem": "meropenem",
    "primaxin": "imipenem cilastatin",
    "cubicin": "daptomycin",
    "zyvox": "linezolid",
    "fluconazole": "diflucan fluconazole",
    "diflucan": "fluconazole",
    "tamiflu": "oseltamivir",
    # Symptoms / signs
    "sob": "shortness of breath dyspnea breathlessness",
    "n/v": "nausea vomiting",
    "n&v": "nausea vomiting",
    "ha": "headache",
    "lbp": "low back pain",
    "abd pain": "abdominal pain",
    "lytes": "electrolytes",
    "bmp": "basic metabolic panel",
    "cmp": "comprehensive metabolic panel",
    "cbc": "complete blood count",
    "lfts": "liver function tests transaminases",
    "ekg": "ECG electrocardiogram",
    "echo": "echocardiogram",
    "cxr": "chest x-ray chest radiograph",
    "kub": "abdominal radiograph",
    "ct head": "computed tomography head",
    "mra": "magnetic resonance angiography",
    "tte": "transthoracic echocardiogram",
    "pft": "pulmonary function test",
    # Ward / admin
    "admit": "admission",
    "d/c": "discharge",
    "f/u": "follow up",
    "rtc": "return to clinic",
    "po": "by mouth oral",
    "pr": "per rectum rectal",
    "iv": "intravenous",
    "im": "intramuscular",
    "sq": "subcutaneous",
    "sub q": "subcutaneous",
    "prn": "as needed",
    "qid": "four times daily",
    "tid": "three times daily",
    "bid": "twice daily",
    "qhs": "at bedtime",
    "ac": "before meals",
    "pc": "after meals",
    "stat": "immediately",
    "npo": "nothing by mouth nil per os",
    "dnr": "do not resuscitate",
    "dni": "do not intubate",
    "goc": "goals of care",
    "loa": "leave of absence",
    # Anatomy / specialty
    "lle": "left lower extremity",
    "rle": "right lower extremity",
    "lue": "left upper extremity",
    "rue": "right upper extremity",
    "ll": "left leg",
    "rl": "right leg",
    "rrr": "regular rate and rhythm",
    "ctab": "clear to auscultation bilaterally",
    "s1 s2": "first and second heart sounds",
}


# ---------- loader / matcher ----------

@lru_cache(maxsize=1)
def _full_table() -> dict[str, str]:
    table = dict(SEED_SYNONYMS)
    extra_path = Path(settings.data_dir) / "synonyms_extra.json"
    if extra_path.exists():
        try:
            data = json.loads(extra_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(k, str) and isinstance(v, str):
                        table[k.lower()] = v
        except Exception:
            pass
    cache_path = Path(settings.data_dir) / "synonyms_rxnorm.json"
    if cache_path.exists():
        try:
            data = json.loads(cache_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(k, str) and isinstance(v, str):
                        table.setdefault(k.lower(), v)
        except Exception:
            pass
    return table


_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-/]*")


def _candidate_phrases(query: str, max_len: int = 3) -> Iterable[tuple[str, str]]:
    """Yield (lowercase_phrase, original_phrase) pairs for n-grams up to max_len."""
    tokens = _TOKEN_RE.findall(query)
    for n in range(min(max_len, len(tokens)), 0, -1):
        for i in range(len(tokens) - n + 1):
            window = tokens[i : i + n]
            yield " ".join(t.lower() for t in window), " ".join(window)


UPPERCASE_REQUIRED: set[str] = {
    "last",  # collides with English "last"
    "or",  # English conjunction (operating room)
    "as",  # aortic stenosis
    "ar",  # aortic regurgitation
    "ai",  # aortic insufficiency
    "ms",  # mitral stenosis / multiple sclerosis
    "mr",  # mitral regurgitation
    "im",  # intramuscular
    "po",  # per os
    "pr",  # per rectum
    "ac",  # before meals
    "pc",  # after meals
    "co",  # cardiac output
    "ha",  # headache
    "ll",  # left leg
    "vt",  # ventricular tachycardia
    "iv",  # intravenous
    "sq",  # subcutaneous
    "mh",  # malignant hyperthermia
    "vap",  # ventilator associated pneumonia
}


def _is_ambiguous_short(phrase: str) -> bool:
    """True for entries that should only expand when uppercase in source query."""
    return phrase in UPPERCASE_REQUIRED


def expand_with_synonyms(query: str, max_additions: int = 6) -> str:
    """Append likely source-side phrasings for any matched aliases in `query`.

    Short abbreviations (≤4 chars, all alphabetic) are only expanded when the
    original query has them in uppercase — otherwise "last case" expands to
    "local anesthetic systemic toxicity" and "or" expands to "operating room".

    Idempotent: if the canonical expansion already appears in the query, the
    expansion is skipped so re-applying the function adds nothing.
    """
    table = _full_table()
    query_low = query.lower()
    seen: set[str] = set()
    additions: list[str] = []
    for phrase_low, phrase_orig in _candidate_phrases(query):
        canonical = table.get(phrase_low)
        if not canonical:
            continue
        if _is_ambiguous_short(phrase_low):
            if not all(t.isupper() for t in phrase_orig.split()):
                continue
        canonical_low = canonical.lower()
        if canonical_low in seen or phrase_low in seen:
            continue
        # Idempotency: skip if the canonical expansion is already in the query.
        if canonical_low in query_low:
            continue
        # Also skip if every word of the canonical is already in the query —
        # handles cases where parts of the expansion already exist.
        canonical_tokens = canonical_low.split()
        if canonical_tokens and all(
            re.search(rf"\b{re.escape(tok)}\b", query_low) for tok in canonical_tokens
        ):
            continue
        seen.add(canonical_low)
        seen.add(phrase_low)
        additions.append(canonical)
        if len(additions) >= max_additions:
            break
    if not additions:
        return query
    return query + " " + " ".join(additions)


# ---------- optional: import RxNorm (NIH, public domain) ----------

def import_rxnorm(rxnconso_path: Path, output_path: Path | None = None) -> int:
    """Read a RXNCONSO.RRF file and emit a brand→generic JSON map.

    Format: pipe-delimited; columns of interest: TTY (term type), STR (string),
    SAB (source). Brand names have TTY=BN; generics have TTY=IN. Map BN→IN
    via the RXCUI when available.
    """
    if not rxnconso_path.exists():
        raise SystemExit(f"RXNCONSO file not found: {rxnconso_path}")
    cui_to_in: dict[str, str] = {}
    bn_rows: list[tuple[str, str]] = []
    with rxnconso_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            cols = line.rstrip("\n").split("|")
            if len(cols) < 16:
                continue
            cui = cols[0]
            tty = cols[12]
            sab = cols[11]
            string = cols[14]
            if sab != "RXNORM" or not string:
                continue
            if tty == "IN":
                cui_to_in.setdefault(cui, string.lower())
            elif tty == "BN":
                bn_rows.append((cui, string.lower()))
    table: dict[str, str] = {}
    for cui, brand in bn_rows:
        generic = cui_to_in.get(cui)
        if generic and brand != generic:
            table[brand] = generic
    out = output_path or (Path(settings.data_dir) / "synonyms_rxnorm.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(table, indent=2), encoding="utf-8")
    _full_table.cache_clear()
    return len(table)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--import-rxnorm", type=str, help="Path to RXNCONSO.RRF")
    parser.add_argument("--probe", type=str, help="Probe expansion on a query string")
    args = parser.parse_args()
    if args.import_rxnorm:
        n = import_rxnorm(Path(args.import_rxnorm))
        print(f"imported {n} brand→generic mappings to {settings.data_dir}/synonyms_rxnorm.json")
    if args.probe:
        print(f"input:    {args.probe}")
        print(f"expanded: {expand_with_synonyms(args.probe)}")
    if not args.import_rxnorm and not args.probe:
        print(f"loaded {len(_full_table())} synonym entries")


if __name__ == "__main__":
    main()
