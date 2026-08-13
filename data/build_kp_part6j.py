import json, sys
sys.path.insert(0, 'data')
from build_kp_part6i import kps

disc = "anesthesia"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"
dom_ethics = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"

# =====================================================================
# [28] Geriatric Pain Management
# =====================================================================
topic28 = "Geriatric Pain Management"

kps += [
  {"id":"geriatric-pain-management-d1","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"Despite lower predicted risk for postoperative pain, why can elderly patients present with significant management challenges?",
   "answer":"Elderly patients can have significant management challenges despite lower predicted pain scores because comorbidities (renal/hepatic impairment, polypharmacy, cognitive impairment) limit analgesic options and alter pharmacokinetics.",
   "rationale":"Reduced organ reserve in the elderly constrains use of NSAIDs (renal), opioids (cognitive, respiratory), and acetaminophen (hepatic); individualized multimodal plans are required.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":741}],"confusable_with":""},

  {"id":"geriatric-pain-management-d2","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"In geriatric pain management, what is the WHO step-wise approach for mild to moderate pain?",
   "answer":"Mild-moderate pain: non-opioids (acetaminophen: max 4g/day, or 2-3g/day in liver disease) and adjuvants (NSAIDs: celecoxib preferred in elderly for reduced GI risk) as first step.",
   "rationale":"The WHO ladder starts with non-opioid analgesics to minimize opioid exposure; in the elderly, opioid-sparing strategies are prioritized due to higher risk of sedation, falls, and delirium.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":164}],"confusable_with":""},

  {"id":"geriatric-pain-management-d3","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"Hypoxemia in the postoperative period is common in elderly patients for what physiological reasons?",
   "answer":"Aging causes V/Q mismatch and increased shunting from loss of elastic recoil; combined with a reduced hypoxic ventilatory drive and propensity for pulmonary aspiration, elderly patients desaturate easily postoperatively.",
   "rationale":"V/Q mismatch increases with age as dependent lung zones close progressively; the blunted ventilatory response to hypoxia means less compensation for any desaturation.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":680}],"confusable_with":""},

  {"id":"geriatric-pain-management-d4","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"Regional anesthesia in the elderly has potential benefits over general anesthesia. What specific advantages are described?",
   "answer":"Regional techniques are opioid-sparing, have the potential to reduce PONV, and may preserve cognitive function -- advantages relevant to delirium risk reduction in the elderly.",
   "rationale":"Elderly patients are highly susceptible to opioid-induced delirium, respiratory depression, and PONV; regional anesthesia avoids these systemic effects while providing equivalent or superior analgesia.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":679}],"confusable_with":""},

  {"id":"geriatric-pain-management-d5","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"Meperidine is particularly problematic in elderly patients for what specific reason beyond renal accumulation?",
   "answer":"Meperidine may contribute to delirium in elderly patients because of its anticholinergic effects from normeperidine metabolite accumulation.",
   "rationale":"Anticholinergic burden is a major risk factor for delirium in the elderly; meperidine's active metabolite normeperidine has significant anticholinergic activity in addition to being neuroexcitatory.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":675}],"confusable_with":"morphine"},

  {"id":"geriatric-pain-management-d6","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"Postoperative delirium (POD) in elderly patients is formally diagnosed using which assessment tools, and what are the clinical subtypes?",
   "answer":"POD is formally diagnosed using the Confusion Assessment Method (CAM) or Riker Sedation Agitation Scale; it can present as hyperactive, hypoactive, or mixed types.",
   "rationale":"Hypoactive delirium (most common in elderly, often mistaken for 'quiet recovery') is the most dangerous type as it is underdiagnosed and carries worse outcomes than hyperactive delirium.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":682}],"confusable_with":"emergence delirium"},

  {"id":"geriatric-pain-management-d7","topic":topic28,"domain":dom_pain,"discipline":disc,
   "stem":"The incidence of spinal hematoma with LMWH was historically estimated at 1 in 150,000 for epidural block. What occurred in North America after LMWH introduction that changed this estimate?",
   "answer":"After LMWH introduction in North America, the incidence of spinal hematoma increased to as frequent as 1 in 40,800 for spinal anesthetics and 1 in 6600 for epidural anesthetics (1 in 3100 for continuous catheters).",
   "rationale":"European use without problems was confounded by different LMWH dosing; higher US doses combined with continued epidural catheter management created higher bleeding risk at critical time points relative to catheter manipulation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":751}],"confusable_with":""},
]

# =====================================================================
# [29] HIPAA, Patient Privacy & Confidentiality
# (Chunks are mostly off-topic; use relevant privacy/monitoring content)
# =====================================================================
topic29 = "HIPAA, Patient Privacy & Confidentiality"

kps += [
  {"id":"hipaa-patient-privacy-confidentiality-d1","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"PACU patient bed enclosures are increasingly being constructed in new facilities. What is the patient rights rationale for this design choice?",
   "answer":"Enclosures protect patient privacy and confidentiality during sensitive discussions between patients, families, and the care team -- important for both dignity and HIPAA compliance.",
   "rationale":"PACU patients are vulnerable and may have reduced capacity to filter shared information; open bays create conditions where private medical information (diagnosis, prognosis, family matters) can be inadvertently overheard.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2096}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d2","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"Good clinical practice in remote patient consultations requires adherence to what three core patient-centered principles?",
   "answer":"(1) Treat patients with dignity, (2) respect their right to privacy and confidentiality, and (3) listen to patient needs and act in their best interest.",
   "rationale":"These principles from good clinical practice standards reflect the ethical obligations of beneficence (act in patient's interest), non-maleficence (avoid harm from breaches), and respect for autonomy (privacy/dignity).",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":147}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d3","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"Florida statutes on HIV testing require what specific patient rights regarding testing in healthcare settings?",
   "answer":"In Florida healthcare settings, patients must be notified of a planned HIV test and have the right to refuse; informed consent must include explanation of confidentiality, mandatory reporting, and opportunity for anonymous testing.",
   "rationale":"HIV-specific confidentiality protections reflect the unique stigma and discrimination risk associated with HIV status; these exceed general medical confidentiality requirements.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":6}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d4","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"ASA Standard I requires that qualified anesthesia personnel be present throughout the conduct of all anesthetics. What is the patient safety rationale?",
   "answer":"Continuous presence of qualified anesthesia personnel allows immediate response to any adverse event (airway emergency, hemodynamic collapse, equipment failure) that can develop at any moment during anesthesia.",
   "rationale":"Anesthesia adverse events can escalate within seconds; human presence provides monitoring, decision-making, and intervention capability that no automated system can fully replicate.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":13}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d5","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"Information provided in a PACU handoff from the anesthesia team to PACU nursing should include what elements according to ASA standards?",
   "answer":"The handoff includes pertinent details of the patient's history, medical condition, anesthesia management, and surgery -- covering relevant preoperative, intraoperative, and anticipated postoperative concerns.",
   "rationale":"Structured handoffs reduce information loss at care transitions; in the PACU, missing information about intraoperative events, allergies, or analgesic requirements can lead to inadequate or unsafe care.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":722}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d6","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"The PACU must be located near operating rooms and procedure areas. What are two specifically listed reasons for this proximity requirement?",
   "answer":"Proximity allows prompt patient transport back to surgery if needed, and enables members of the operating room team to quickly respond to urgent patient care issues in the PACU.",
   "rationale":"Rapid deterioration (bleeding, airway compromise) requires emergency return to OR; remote PACU locations add transport time that can be critical in time-sensitive emergencies.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2096}],"confusable_with":""},

  {"id":"hipaa-patient-privacy-confidentiality-d7","topic":topic29,"domain":dom_ethics,"discipline":disc,
   "stem":"When preventing awareness under anesthesia in TIVA, what monitoring adjunct and minimum inhalation agent guideline are recommended?",
   "answer":"Monitor brain activity using BIS or SedLine if using TIVA; if using inhalation agents, administer at least 0.5-0.7 MAC and set an alarm for low gas concentration.",
   "rationale":"Processed EEG (BIS, SedLine) provides quantitative depth-of-anesthesia information that end-tidal agent monitoring cannot during TIVA; minimum MAC thresholds prevent under-dosing during maintenance.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":24}],"confusable_with":""},
]

# =====================================================================
# [30] Halogenated volatile agents: pharmacokinetics
# (Chunks are mostly MAC/aging/benzodiazepine -- use agent-specific content)
# =====================================================================
topic30 = "Halogenated volatile agents: pharmacokinetics"

kps += [
  {"id":"halogenated-volatile-agents-pharmacokinetics-d1","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"Why is a greater minute ventilation-to-FRC ratio in infants significant for inhalation induction pharmacokinetics?",
   "answer":"A greater minute ventilation-to-FRC ratio in infants, combined with greater blood flow to the brain, speeds the increase in alveolar anesthetic concentration and accelerates inhalation induction.",
   "rationale":"Alveolar concentration rises faster when more fresh gas is delivered relative to the existing lung volume; rapid alveolar equilibration combined with high brain blood flow speeds effect-site equilibration.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d2","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"Sevoflurane has the lowest blood:gas partition coefficient of the commonly used volatile agents. What clinical pharmacokinetic advantages does this confer?",
   "answer":"Low blood:gas solubility (lower than N2O) means sevoflurane equilibrates rapidly between blood and alveolus, providing fast onset of induction and fast elimination -- ideal for outpatient/ambulatory anesthesia.",
   "rationale":"Insoluble agents do not accumulate significantly in blood; alveolar washout during emergence rapidly lowers blood concentrations, enabling faster awakening than more soluble agents like isoflurane.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":20}],"confusable_with":"desflurane"},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d3","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"In pediatric patients, temperature monitoring during halogenated volatile agent administration is specifically emphasized. Why?",
   "answer":"Temperature must be closely monitored in pediatric patients because of their greater risk for malignant hyperthermia and greater susceptibility to intraoperative hypothermia or hyperthermia.",
   "rationale":"Children have high surface-area-to-body-weight ratio causing rapid heat loss; volatile agents also impair thermoregulation; MH risk is highest in children receiving volatile agents with succinylcholine.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d4","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"MAC is reduced by approximately 30% when benzodiazepines are co-administered with volatile agents. What is the clinical significance for anesthetic management?",
   "answer":"Benzodiazepine premedication allows significant reduction in volatile agent doses; this reduction is clinically important for hemodynamic stability but must account for delayed awakening from the benzodiazepine itself.",
   "rationale":"The GABAergic synergism between benzodiazepines and volatile agents allows opioid-sparing and hemodynamic-sparing anesthetic technique, but prolonged benzodiazepine action can offset the benefit of fast-offset volatile agents.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d5","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"During cardiac surgery, what specific action maintains awareness prevention when delivering volatile anesthesia through the cardiopulmonary bypass machine?",
   "answer":"Monitor anesthetic gas concentration during cardiopulmonary bypass from the bypass machine itself; this is specifically listed as a prevention measure for intraoperative awareness.",
   "rationale":"During CPB, gas is delivered through the oxygenator rather than the anesthesia machine; failure to monitor gas from the bypass circuit can result in undetected anesthetic undersupply and awareness.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":204}],"confusable_with":""},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d6","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"Albumin concentrations decline with aging and affect drug binding. How does reduced albumin alter the pharmacological effects of acidic anesthetic drugs?",
   "answer":"Reduced albumin decreases binding of acidic drugs (barbiturates, benzodiazepines, opioid agonists), increasing the free fraction and thus enhancing and potentially prolonging their pharmacological effects.",
   "rationale":"Only free (unbound) drug crosses the blood-brain barrier and produces effect; hypoalbuminemia effectively increases the bioavailable dose, meaning the same total dose has a greater and longer effect.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1506}],"confusable_with":"basic drug binding to alpha-1 acid glycoprotein"},

  {"id":"halogenated-volatile-agents-pharmacokinetics-d7","topic":topic30,"domain":dom_pharm,"discipline":disc,
   "stem":"Intraoperative hyperventilation is described as a common cause of what postoperative problem?",
   "answer":"Intraoperative hyperventilation is a common cause of delayed awakening from anesthesia (by causing hypocapnia that blunts respiratory drive, delaying elimination of volatile agents).",
   "rationale":"Hypocapnia reduces cerebral blood flow and respiratory drive; decreased CBF slows central anesthetic washout; the breathing depression from alkalosis prolongs apnea periods and slows emergence.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
