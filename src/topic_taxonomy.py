from __future__ import annotations

import re
from collections import Counter

from .source_classifier import infer_source_name

TOPICS: dict[str, list[str]] = {
    "Chest pain": ["chest pain", "angina", "troponin", "acs"],
    "Dyspnea": ["dyspnea", "shortness of breath", "sob", "orthopnea"],
    "Hypoxemia": ["hypoxemia", "desaturation", "spo2", "low oxygen"],
    "Syncope": ["syncope", "presyncope", "loss of consciousness"],
    "Altered mental status": ["altered mental status", "ams", "encephalopathy"],
    "Fever": ["fever", "febrile"],
    "Sepsis": ["sepsis", "septic shock", "lactate", "source control"],
    "Shock": ["shock", "vasopressor", "hypoperfusion"],
    "Hypotension": ["hypotension", "low blood pressure"],
    "Hypertension urgency/emergency": ["hypertensive emergency", "hypertensive urgency"],
    "Heart failure": ["heart failure", "hfrEF", "hfpef", "diuresis", "volume overload"],
    "ACS": ["acute coronary syndrome", "acs", "nstemi", "stemi", "unstable angina"],
    "Arrhythmias": ["arrhythmia", "bradycardia", "tachycardia", "wide complex"],
    "Afib with RVR": ["afib with rvr", "atrial fibrillation", "rate control"],
    "COPD/asthma exacerbation": ["copd exacerbation", "asthma exacerbation", "wheezing"],
    "Pneumonia": ["pneumonia", "cap", "hcap"],
    "PE": ["pulmonary embolism", "pe", "d-dimer", "ctpa"],
    "AKI": ["aki", "acute kidney injury", "creatinine"],
    "CKD": ["ckd", "chronic kidney disease"],
    "Electrolytes": ["electrolyte", "sodium", "potassium", "magnesium"],
    "Hyponatremia": ["hyponatremia", "low sodium", "siadh"],
    "Hyperkalemia": ["hyperkalemia", "high potassium", "calcium gluconate", "insulin"],
    "DKA/HHS": ["dka", "hhs", "diabetic ketoacidosis", "hyperosmolar"],
    "GI bleed": ["gi bleed", "hematemesis", "melena", "variceal bleed"],
    "Cirrhosis complications": ["cirrhosis", "ascites", "hepatic encephalopathy", "varices"],
    "Pancreatitis": ["pancreatitis", "lipase"],
    "Anticoagulation": ["anticoagulation", "warfarin", "heparin", "doac"],
    "Delirium": ["delirium", "confusion", "cam-icu"],
    "Pain control": ["pain control", "analgesia"],
    "Alcohol withdrawal": ["alcohol withdrawal", "ciwa", "benzodiazepine"],
    "Opioid withdrawal": ["opioid withdrawal", "buprenorphine", "methadone"],
    "Insulin management": ["insulin", "basal", "sliding scale", "glargine"],
    "Fluids": ["fluid", "crystalloid", "resuscitation"],
    "Diuresis": ["diuresis", "furosemide", "lasix"],
    "Antibiotics": ["antibiotic", "vancomycin", "cefepime", "zosyn"],
    "Cross-cover pages": ["cross cover", "night float", "page", "called"],
    "Admission orders": ["admission orders", "admit", "orders"],
    "Discharge planning": ["discharge", "med rec", "follow up"],
    "Consults": ["consult", "consultation"],
    "Goals of care": ["goals of care", "goc", "code status"],
    "Rapid response": ["rapid response", "rrt", "code blue"],
    "Code status": ["code status", "full code", "dnr", "dni"],
    "Night float": ["night float", "overnight", "cross cover"],
    "Mechanical ventilation": ["mechanical ventilation", "ventilator", "tidal volume", "plateau pressure"],
    "ARDS": ["ards", "low tidal volume", "p/f ratio", "proning"],
    "Vasopressors": ["norepinephrine", "vasopressin", "phenylephrine", "pressor"],
    "Sedation": ["sedation", "propofol", "dexmedetomidine", "rass"],
    "Renal replacement therapy": ["renal replacement", "crrt", "hemodialysis"],
    "Ventilator alarms": ["high pressure alarm", "low pressure alarm", "vent alarm"],
    "Weaning/extubation": ["weaning", "extubation", "spontaneous breathing trial"],
    "Airway": ["airway", "mask ventilation", "laryngoscopy", "intubation", "extubation"],
    "Difficult airway": ["difficult airway", "awake intubation", "bougie", "video laryngoscope"],
    "Oxygenation and ventilation": ["oxygenation", "ventilation", "hypoxemia", "peep", "fio2"],
    "Respiratory physiology": ["v/q", "shunt", "dead space", "compliance", "closing capacity"],
    "Cardiovascular physiology": ["cardiac output", "preload", "afterload", "contractility", "svr"],
    "Inhaled anesthetics": ["volatile", "mac", "sevoflurane", "desflurane", "isoflurane", "nitrous"],
    "IV anesthetics": ["propofol", "etomidate", "ketamine", "barbiturate", "dexmedetomidine"],
    "Opioids": ["opioid", "fentanyl", "remifentanil", "hydromorphone", "morphine"],
    "Neuromuscular blockers": ["rocuronium", "succinylcholine", "vecuronium", "neuromuscular"],
    "Reversal agents": ["sugammadex", "neostigmine", "reversal", "glycopyrrolate"],
    "Local anesthetics": ["lidocaine", "bupivacaine", "ropivacaine", "local anesthetic"],
    "Regional anesthesia": ["peripheral nerve block", "regional", "ultrasound guided"],
    "Neuraxial anesthesia": ["spinal", "epidural", "neuraxial", "intrathecal"],
    "Obstetric anesthesia": ["obstetric", "pregnancy", "cesarean", "labor analgesia"],
    "Pediatric anesthesia": ["pediatric", "infant", "child", "neonate"],
    "Geriatric anesthesia": ["geriatric", "elderly", "frailty"],
    "Cardiac anesthesia": ["cardiac anesthesia", "bypass", "valve", "coronary"],
    "Thoracic anesthesia": ["one lung ventilation", "thoracic", "double lumen", "bronchial blocker"],
    "Neuroanesthesia": ["neuroanesthesia", "intracranial pressure", "cerebral perfusion"],
    "Trauma anesthesia": ["trauma", "rapid sequence", "hemorrhagic shock"],
    "Ambulatory anesthesia": ["ambulatory", "same-day", "ponv"],
    "Critical care": ["critical care", "icu", "vasopressor", "sepsis"],
    "Fluids and electrolytes": ["fluid", "sodium", "potassium", "crystalloid", "colloid"],
    "Transfusion medicine": ["transfusion", "massive transfusion", "prbc", "ffp", "platelet"],
    "Coagulation": ["coagulation", "inr", "ptt", "thromboelastography", "anticoagulant"],
    "Renal disease": ["renal", "kidney", "dialysis", "creatinine"],
    "Hepatic disease": ["hepatic", "liver", "cirrhosis"],
    "Endocrine disease": ["diabetes", "thyroid", "adrenal", "endocrine"],
    "Obesity/OSA": ["obesity", "obstructive sleep apnea", "osa", "bmi"],
    "Malignant hyperthermia": ["malignant hyperthermia", "dantrolene"],
    "LAST": ["local anesthetic systemic toxicity", "local anesthetic toxicity", "lipid emulsion", "intralipid", "bupivacaine-induced cardiac toxicity"],
    "Anaphylaxis": ["anaphylaxis", "epinephrine", "allergic"],
    "Bronchospasm": ["bronchospasm", "wheezing", "albuterol"],
    "Laryngospasm": ["laryngospasm", "jaw thrust", "positive pressure"],
    "Aspiration": ["aspiration", "gastric contents", "rsi"],
    "High spinal": ["high spinal", "total spinal", "bradycardia"],
    "Cannot intubate/cannot oxygenate": ["cannot intubate", "cannot oxygenate", "cico", "front of neck"],
    "Massive hemorrhage": ["massive hemorrhage", "massive transfusion", "hemorrhage"],
    "PACU complications": ["pacu", "postoperative", "emergence"],
    "Perioperative medicine": ["preoperative", "perioperative", "risk stratification"],
    "Monitoring": ["monitoring", "arterial line", "capnography", "pulse oximetry"],
    "Ventilators": ["ventilator", "pressure control", "volume control"],
    "Acid-base": ["acid-base", "anion gap", "metabolic acidosis", "respiratory acidosis"],
    "Pharmacokinetics/pharmacodynamics": ["pharmacokinetics", "pharmacodynamics", "context-sensitive"],
    "Oral boards cases": ["oral board", "case stem", "management"],
}

SYNONYM_TAGS: dict[str, list[str]] = {
    "Hypoxemia": ["desaturation", "low spo2", "oxygen requirement", "v/q mismatch", "shunt", "hypoventilation"],
    "Hyperkalemia": ["ecg changes", "calcium gluconate", "insulin dextrose", "albuterol", "dialysis"],
    "Hyponatremia": ["serum osmolality", "urine osmolality", "urine sodium", "siadh"],
    "Afib with RVR": ["atrial fibrillation", "rapid ventricular response", "rate control", "diltiazem", "metoprolol"],
    "Sepsis": ["lactate", "blood cultures", "broad spectrum antibiotics", "source control", "fluids"],
    "Shock": ["septic shock", "cardiogenic shock", "obstructive shock", "hypovolemic shock", "norepinephrine"],
    "ARDS": ["low tidal volume", "plateau pressure", "peep", "proning", "pf ratio"],
    "Ventilator alarms": ["high pressure alarm", "low pressure alarm", "disconnect", "obstruction", "pneumothorax"],
    "LAST": ["local anesthetic systemic toxicity", "lipid emulsion", "intralipid", "seizure", "arrhythmia"],
    "Malignant hyperthermia": ["dantrolene", "hypercarbia", "rigidity", "volatile anesthetic", "succinylcholine"],
    "Cannot intubate/cannot oxygenate": ["cico", "front of neck airway", "cricothyrotomy"],
    "Respiratory physiology": ["v/q", "shunt", "dead space", "diffusion", "compliance"],
}

CLINICAL_CONTEXT_KEYWORDS = {
    "cross_cover": ["night float", "cross cover", "called", "page", "overnight", "rapid response"],
    "ICU": ["icu", "ventilator", "pressor", "vasopressor", "arterial line", "central line", "shock"],
    "ED": ["emergency department", "ed", "triage"],
    "OR": ["operating room", "anesthesia", "induction", "intubation", "extubation", "pacu"],
    "PACU": ["pacu", "post-anesthesia", "emergence"],
    "consult": ["consult", "consultation"],
    "clinic": ["clinic", "outpatient"],
    "wards": ["ward", "rounds", "admission", "discharge"],
}

STOPWORDS = {
    "about",
    "after",
    "also",
    "because",
    "before",
    "between",
    "chapter",
    "clinical",
    "could",
    "disease",
    "during",
    "figure",
    "follow",
    "general",
    "however",
    "include",
    "includes",
    "management",
    "medical",
    "medicine",
    "patient",
    "patients",
    "section",
    "should",
    "table",
    "their",
    "there",
    "these",
    "those",
    "treatment",
    "using",
    "where",
    "which",
    "while",
    "with",
    "without",
}


def tag_topics(text: str) -> list[str]:
    haystack = text.lower()
    tags: list[str] = []
    for topic, keywords in TOPICS.items():
        if any(re.search(r"\b" + re.escape(k.lower()) + r"\b", haystack) for k in keywords):
            tags.append(topic)
    return tags


def infer_clinical_context(text: str, default: str = "wards") -> str:
    haystack = text.lower()
    scores = {
        context: sum(1 for keyword in keywords if keyword in haystack)
        for context, keywords in CLINICAL_CONTEXT_KEYWORDS.items()
    }
    best, score = max(scores.items(), key=lambda item: item[1])
    return best if score > 0 else default


def extract_key_terms(text: str, max_terms: int = 24) -> list[str]:
    words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9/-]{2,}", text)]
    counts = Counter(w for w in words if w not in STOPWORDS and not w.isdigit())
    priority_terms = []
    for phrase in [
        "atrial fibrillation",
        "calcium gluconate",
        "local anesthetic",
        "malignant hyperthermia",
        "renal replacement",
        "rapid response",
        "tidal volume",
    ]:
        if phrase in text.lower():
            priority_terms.append(phrase)
    ranked = [term for term, _ in counts.most_common(max_terms)]
    return list(dict.fromkeys(priority_terms + ranked))[:max_terms]


def build_retrieval_tags(text: str, source_name: str = "", section: str = "", default_context: str = "wards") -> dict[str, list[str] | str]:
    topic_tags = tag_topics(text)
    synonym_tags: list[str] = []
    for topic in topic_tags:
        synonym_tags.extend(SYNONYM_TAGS.get(topic, []))
    key_terms = extract_key_terms(" ".join([section, text]))
    context = infer_clinical_context(text, default_context)
    retrieval_tags = list(dict.fromkeys(topic_tags + synonym_tags + key_terms + [source_name, context]))
    return {
        "topic_tags": topic_tags,
        "keyword_tags": key_terms,
        "synonym_tags": list(dict.fromkeys(synonym_tags)),
        "retrieval_tags": retrieval_tags,
        "clinical_context": context,
    }
