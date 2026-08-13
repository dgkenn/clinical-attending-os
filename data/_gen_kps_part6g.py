import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch6.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [27] General anesthesia for cesarean delivery
# ============================================================
t = "General anesthesia for cesarean delivery"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "ga-cesarean"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the technique for rapid-sequence induction for cesarean section under general anesthesia?",
 "answer":"(1) Left uterine displacement wedge; (2) denitrogenation with 100% O2 for 3-5 min; (3) RSI with propofol 2 mg/kg (or ketamine 1-2 mg/kg if hypovolemic) + succinylcholine 1.5 mg/kg with cricoid pressure",
 "rationale":"Ketamine substituted for propofol in hypovolemic patients because ketamine maintains blood pressure via sympathomimetic effect; succinylcholine provides rapid onset for fast intubation.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1411}],"confusable_with":"Methohexital/etomidate (little benefit in obstetrics)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why is general anesthesia for vaginal delivery generally avoided except for true emergencies?",
 "answer":"Because of increased risk of aspiration (full stomach); regional anesthesia is preferred for vaginal delivery; GA only for true emergencies when regional not possible or time prohibits",
 "rationale":"All parturients are considered to have full stomachs; laryngoscopy during RSI risks regurgitation and aspiration; the gravid uterus increases intra-abdominal pressure.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1402}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What physiologic change in pregnancy most reduces preoxygenation time before general anesthesia induction?",
 "answer":"Decreased FRC (reduced expiratory reserve volume) combined with increased oxygen consumption promotes rapid oxygen desaturation during apnea",
 "rationale":"FRC is the oxygen reservoir during apnea; reduced FRC plus increased VO2 means the time to desaturation during intubation is shorter than in non-pregnant patients.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1359}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"During active bleeding from placenta previa, what is the required preparation before emergency cesarean under general anesthesia?",
 "answer":"Two large-bore IVs; replace intravascular volume deficits; blood available for transfusion; active bleeding or hemodynamic instability requires immediate cesarean under general anesthesia",
 "rationale":"Placenta previa with active bleeding demands aggressive resuscitation simultaneously with definitive surgery; the lower uterine segment placental implantation site may not contract well postdelivery.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1416}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"In a planned cesarean under regional anesthesia, what is the anesthesiologist's obligation if pain remains intolerable despite seemingly adequate sensory level?",
 "answer":"If pain is intolerable despite adequate sensory level and unresponsive to IV ketamine/midazolam or nitrous oxide supplementation, general anesthesia with endotracheal intubation is required",
 "rationale":"Inadequate regional anesthesia during surgical manipulation causes not only patient distress but unacceptable risk of movement; conversion to GA protects both patient and fetus.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the obstetric incidence of breech presentation and what does it dramatically increase?",
 "answer":"Breech presentations complicate 3-4% of deliveries; increases incidence of cord prolapse more than tenfold; external cephalic version may be attempted after 34 weeks",
 "rationale":"Cord prolapse is life-threatening requiring emergency delivery; breech position prevents the fetal head from occluding the cord during labor.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1414}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What anesthetic considerations apply when prior payments on behalf of anesthesiologists involved cesarean delivery complications?",
 "answer":"Closed claims include: delays in care, miscommunication about urgency of cesarean delivery, difficult intubation or high block management concerns, lapses in care or record keeping",
 "rationale":"These specific patterns from ASA closed claims identify the highest-risk failure points in obstetric anesthesia: communication, airway management, and documentation.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1387}],"confusable_with":""},
]

kps.append({"_type":"illness_script","topic":t,"discipline":disc,
 "enabling_conditions":"Parturient requiring emergency cesarean delivery; failed regional anesthesia; airway/aspiration concern",
 "pathophysiology":"Full-stomach parturient with reduced FRC and increased VO2; difficult airway from pregnancy edema; aspiration risk from reduced LES tone and delayed gastric emptying",
 "time_course":"RSI required within minutes for maternal/fetal compromise; inadequate preoxygenation causes rapid desaturation",
 "key_features":"RSI with propofol/ketamine + succinylcholine; cricoid pressure; T4 level not achievable via regional; failed airway is leading obstetric anesthesia mortality cause",
 "consequence_if_missed":"Aspiration pneumonitis/failed intubation -> maternal hypoxia -> fetal distress; leading cause of anesthesia-related maternal death"})

# ============================================================
# [28] Geriatric Pain Management
# ============================================================
t = "Geriatric Pain Management"
dom = "Perioperative medicine (preoperative assessment, risk stratification, premedication, ERAS, fluid management, temperature, positioning, post-op care)"
disc = "anesthesia"
s = "geriatric-pain"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why are elderly patients at higher risk for cognitive dysfunction after perioperative opioids?",
 "answer":"Elderly patients are at higher risk for cognitive dysfunction in the perioperative period; meperidine has anticholinergic effects contributing to delirium; opioids with active metabolites (morphine, meperidine) accumulate with renal impairment",
 "rationale":"Age-related reduction in cholinergic reserve makes elderly patients more susceptible to anticholinergic delirium; reduced renal clearance prolongs opioid metabolite exposure.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":741}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the WHO stepped analgesic approach to pain management and what agents are recommended at each step?",
 "answer":"Step 1 (mild-moderate): non-opioids (acetaminophen max 4g/day, 2-3g in liver disease; NSAIDs with caution); Step 2 (moderate): weak opioids + adjuvants; Step 3 (severe): strong opioids + adjuvants; CDC guidelines apply to opioid prescribing",
 "rationale":"The WHO ladder provides a structured approach to pain management; starting non-opioids minimizes opioid-related side effects while maintaining analgesia.",
 "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":164}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What opioid is preferred in elderly patients with no active metabolites, and what is the advantage of remifentanil in this context?",
 "answer":"Fentanyl is preferred in elderly (fewer PK-related considerations, no active metabolites); remifentanil advantageous for its organ-independent metabolism via nonspecific esterases",
 "rationale":"Fentanyl clearance is hepatic but predictable; remifentanil's esterase-based metabolism makes it independent of renal/hepatic function, ideal for frail elderly.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":675}],"confusable_with":"Morphine/meperidine (active metabolites, avoid in elderly with renal impairment)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the potential benefit of regional anesthesia techniques in elderly patients beyond pain management?",
 "answer":"Regional techniques are opioid-sparing, limit polypharmacy and associated complications, and may better prevent postoperative cognitive dysfunction and delirium than systemic opioids",
 "rationale":"Opioid-sparing via regional anesthesia avoids anticholinergic effects, reduces CNS side effects, and may preserve cognitive function by reducing systemic drug burden.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":679}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the postoperative monitoring requirements for elderly patients regarding pulmonary complications?",
 "answer":"Elderly patients have higher propensity for V/Q mismatch and shunting + reduced hypoxic ventilatory drive + propensity for aspiration; maintain pulse oximetry + supplemental O2 + incentive spirometry when sufficiently alert",
 "rationale":"Age-related pulmonary changes combined with anesthetic residual effects create significant hypoxemia risk in the PACU; continuous SpO2 monitoring detects this.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":680}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What incidence of spinal hematoma is estimated for neuraxial techniques, and how did LMWH introduction in North America affect this?",
 "answer":"Spinal hematoma approximately 1:150,000 epidural, 1:220,000 spinal; after LMWH introduction in the US (1993-1998), incidence increased to 1:40,800 spinal and 1:6,600 epidural (1:3,100 postoperative epidural)",
 "rationale":"LMWH's pharmacokinetics were not initially well understood for neuraxial timing; ASRA guidelines for LMWH-neuraxial intervals were developed after these reports of hematoma.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":751}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is CRPS (complex regional pain syndrome) type 1 vs. type 2 and which gender and age group is more commonly affected?",
 "answer":"CRPS type 1: no clear peripheral nerve injury (90% of cases); CRPS type 2: clear nerve injury; females more commonly affected (at least 2:1); peaks in early twenties and mid-thirties",
 "rationale":"CRPS type 1 may develop after minor trauma or immobilization; the mechanism involves sympathetic dysregulation and central sensitization.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":825}],"confusable_with":"Neuropathic pain (broad category including CRPS)"},
]

# ============================================================
# [29] HIPAA, Patient Privacy & Confidentiality
# Chunks are very limited on direct HIPAA content; use what's available
# ============================================================
t = "HIPAA, Patient Privacy & Confidentiality"
dom = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
disc = "anesthesia"
s = "hipaa-privacy"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What PACU design feature protects patient privacy and why is it important for HIPAA compliance?",
 "answer":"Individually enclosed PACU patient bays protect privacy; sensitive discussions between patient, family, and care team often involve confidential medical information that should not be overheard by other patients",
 "rationale":"HIPAA requires protection of PHI; open-ward PACU designs risk inadvertent disclosure; enclosed bays also serve infection control.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2096}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What principles of clinical practice apply equally to in-person and remote telemedicine consultations for COPD follow-up?",
 "answer":"Treat patients with dignity; respect privacy and confidentiality; listen to patient needs and act in their best interest; same documentation standards apply",
 "rationale":"Telemedicine creates new privacy risks (video recordings, data security); the same ethical and legal obligations apply regardless of visit modality.",
 "bloom":"apply","source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":147}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What patient rights must be established before HIV testing in a healthcare setting?",
 "answer":"Patient must be notified of planned HIV test and has the right to refuse; informed consent must include explanation of confidentiality, mandatory reporting, and opportunity for anonymous testing; refusal documented in chart",
 "rationale":"HIV testing carries significant social implications; autonomy requires informed consent with knowledge of confidentiality protections and exceptions (mandatory reporting).",
 "bloom":"recall","source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":6}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the ASA monitoring standards regarding documentation of anesthetic care?",
 "answer":"ASA Standard II requires continual evaluation and documentation of oxygenation, ventilation, circulation, and temperature during all anesthetics; accurate record keeping is a professional and legal obligation",
 "rationale":"Documentation creates the medical record for continuity of care, quality review, medicolegal defense, and billing; incomplete records are a closed-claims risk factor.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":13}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What professional obligation exists when an anesthesiologist has concerns about patient management before proceeding?",
 "answer":"Anesthesiologist should voice concerns and should not proceed until a safe anesthetic and surgical plan have been agreed upon by the team",
 "rationale":"Professional accountability and patient safety require speaking up; proceeding despite unresolved safety concerns creates both patient harm risk and professional liability.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"In the context of intraoperative awareness, what patient disclosure obligation exists?",
 "answer":"Patients managed with regional anesthesia and propofol sedation should be made aware they might recall perioperative events; clarification of technique prevents patients from believing they experienced GA awareness",
 "rationale":"Informed consent for MAC/monitored sedation must include the possibility of recall; mislabeling conscious sedation as GA awareness causes unnecessary psychological harm.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":207}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What documentation is required when a patient refuses a recommended test (e.g., HIV test) in a healthcare setting?",
 "answer":"Patient's refusal of the test is documented in the chart; informed refusal requires the same documentation rigor as informed consent",
 "rationale":"Documentation of informed refusal protects the clinician legally and ensures future providers know the patient was offered and declined the test.",
 "bloom":"apply","source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":6}],"confusable_with":""},
]

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch7.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 7 saved OK")
