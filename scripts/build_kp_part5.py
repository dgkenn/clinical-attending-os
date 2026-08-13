import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch4.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch4")

# ============================================================
# ITEM 22: Tuberculosis (TB)
# CHUNKS: Morgan/Mikhail TB mentions (spine, granuloma, occupational exposure)
# ============================================================
topic = "Tuberculosis (TB)"
domain = "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)"
disc = "medicine"

kps += [
  {"id":"tb-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Spinal tuberculosis (Pott's disease) classically presents how, and what distinguishes it from other causes of vertebral osteomyelitis?",
   "answer":"Chronic back pain without fever or leukocytosis (insidious onset); TB osteomyelitis can be afebrile with normal WBC unlike pyogenic vertebral osteomyelitis; anterior vertebral body involvement with gibbus deformity is classic.",
   "rationale":"TB spine infection is indolent; hematogenous seeding of anterior vertebral bodies causes disc space involvement, collapse, and paravertebral abscess; the absence of systemic signs is a diagnostic pitfall.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1744}],"confusable_with":"Pyogenic vertebral osteomyelitis"},
  {"id":"tb-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"TB is a type IV (delayed-type) hypersensitivity reaction — what is the mechanism and what cells mediate the granuloma?",
   "answer":"Type IV: CD4+ T-lymphocytes sensitized to mycobacterial antigens recruit macrophages that form granulomas (Langhans giant cells, epithelioid macrophages with caseous necrosis); cell-mediated immunity is required for containment.",
   "rationale":"TNF is essential for granuloma formation and maintenance; this explains why anti-TNF therapy for rheumatic disease reactivates latent TB.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2033}],"confusable_with":"Sarcoidosis (non-caseating granuloma)"},
  {"id":"tb-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Granulomatous disorders including TB can cause hypercalcemia through what mechanism?",
   "answer":"Granuloma macrophages produce 1-alpha-hydroxylase, converting 25-OH vitamin D to active 1,25-(OH)2 vitamin D autonomously — unregulated PTH-independent hypercalcemia.",
   "rationale":"Unlike PTH-mediated hypercalcemia, granuloma-associated hypercalcemia is driven by ectopic calcitriol production; PTH is suppressed in response to hypercalcemia.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1889}],"confusable_with":"Primary hyperparathyroidism"},
  {"id":"tb-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Healthcare workers are exposed to tuberculosis as an occupational hazard — what is the current OSHA approach for anesthesia providers regarding maximum acceptable trace concentrations of hazardous agents?",
   "answer":"TB is a direct occupational exposure risk via aerosol; N95 respirator protection is required for aerosolizing procedures; additionally, nitrous oxide <25 ppm and halogenated agents <0.5 ppm (or 2 ppm if used alone) are OSHA limits for chronic exposure.",
   "rationale":"Aerosolizing procedures (bronchoscopy, intubation) carry highest TB transmission risk; respiratory protection and negative-pressure isolation rooms protect healthcare workers.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2043}],"confusable_with":""},
  {"id":"tb-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Massive hemoptysis in a patient with a prior pulmonary cavitary disease is most commonly caused by what conditions?",
   "answer":"Tuberculosis (most common globally), bronchiectasis, neoplasm, or previous pulmonary artery catheter balloon overinflation causing rupture; bronchial artery embolization is the primary intervention.",
   "rationale":"TB cavities can erode into bronchial or pulmonary vessels (Rasmussen aneurysm); the high-pressure bronchial arterial circulation is the usual source of massive hemoptysis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":916}],"confusable_with":""},
]

# ============================================================
# ITEM 23: Ventilator Weaning & Liberation
# ============================================================
topic = "Ventilator Weaning & Liberation"
domain = "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)"
disc = "medicine"

kps += [
  {"id":"vent-weaning-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the rapid shallow breathing index (RSBI) and what threshold predicts successful versus failed spontaneous breathing trial?",
   "answer":"RSBI = respiratory rate / tidal volume (L); RSBI <100/L predicts successful weaning; RSBI >100/L predicts failure (original study: <105/L had 80% success rate).",
   "rationale":"RSBI integrates respiratory rate and tidal volume; high rate with small VT indicates diaphragmatic fatigue and inability to sustain spontaneous breathing.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":352}],"confusable_with":""},
  {"id":"vent-weaning-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the respiratory, cardiovascular, and mental status criteria that must be met before conducting a spontaneous breathing trial?",
   "answer":"Respiratory: PaO2 >/=60 mmHg on FiO2 <40-50% with PEEP </=5-8 cmH2O; able to initiate inspiratory effort. Cardiovascular: no myocardial ischemia, HR <140, BP normal without vasopressors (or minimal dopamine <5 mcg/kg/min). Mental status: arousable or GCS sufficient.",
   "rationale":"SBT readiness criteria ensure the patient is no longer requiring mechanical ventilation support for gas exchange or hemodynamic instability before being challenged with spontaneous breathing.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":351}],"confusable_with":""},
  {"id":"vent-weaning-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Maximum inspiratory force (MIF/Pimax) of less than -20 cmH2O has what predictive value for weaning success?",
   "answer":"Pimax less negative than -20 cmH2O (i.e., closer to zero) predicts higher probability of weaning failure; Pimax more negative than -20 cmH2O indicates little or no chance of successful weaning — but an adequate Pimax does not guarantee success.",
   "rationale":"Pimax reflects respiratory muscle strength; inability to generate adequate inspiratory pressure indicates muscle weakness that will prevent sustaining spontaneous ventilation.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":353}],"confusable_with":""},
  {"id":"vent-weaning-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What general physiological criteria must be met for a patient to be considered ready for weaning from mechanical ventilation?",
   "answer":"pH >7.25, adequate arterial O2 saturation on FiO2 <0.5, ability to spontaneously breathe, hemodynamic stability, no active myocardial ischemia.",
   "rationale":"These criteria ensure the underlying indication for ventilation (respiratory failure, shock) has resolved sufficiently to challenge the patient with spontaneous breathing.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2195}],"confusable_with":""},
  {"id":"vent-weaning-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"After single-lung resection, most patients are extubated soon after surgery — what specific complication motivates this early extubation and what is the criterion for continued ventilation?",
   "answer":"Extubation soon after surgery reduces risk of pulmonary barotrauma (particularly 'blowout' rupture of the bronchial suture line); patients with marginal pulmonary reserve should remain intubated until standard extubation criteria are met.",
   "rationale":"Positive pressure ventilation against a fresh bronchial stump risks anastomotic dehiscence and bronchopleural fistula; early extubation to spontaneous breathing reduces mean airway pressure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":914}],"confusable_with":""},
  {"id":"vent-weaning-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Auto-PEEP in a mechanically ventilated patient is measured by what technique, and what are its hemodynamic consequences?",
   "answer":"Auto-PEEP measured by end-expiratory hold (expiratory pause maneuver); auto-PEEP > set PEEP = dynamic hyperinflation. Consequences: hypotension from reduced venous return, alveolar overdistension (volutrauma/barotrauma), and increased work of breathing to trigger the ventilator.",
   "rationale":"Air trapping in obstructive disease creates intrinsic PEEP; the compressed venous capacitance vessels reduce preload and cardiac output while overdistended alveoli risk rupture.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":58}],"confusable_with":""},
  {"id":"vent-weaning-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What hybrid ventilation mode integrates both pressure and volume targeting and what are its proprietary names?",
   "answer":"Pressure-regulated volume control (PRVC) or pressure control ventilation-volume guaranteed (PCV-VG) — delivers a pressure-controlled breath while adjusting pressure to achieve a set volume target.",
   "rationale":"PRVC provides the flow-cycling advantages of pressure control (decelerating flow, better patient-vent synchrony) while guaranteeing a minimum tidal volume, combining benefits of both modes.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":769}],"confusable_with":""},
]

# ============================================================
# ITEM 24: Viral Meningitis & Encephalitis
# ============================================================
topic = "Viral Meningitis & Encephalitis"
domain = "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)"
disc = "medicine"

kps += [
  {"id":"viral-meningitis-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most common type of viral encephalitis and what empirical treatment should be started immediately in any suspected encephalitis?",
   "answer":"HSV (herpes simplex virus) encephalitis is the most common; acyclovir 10 mg/kg IV every 8 hours for 14-21 days should be started empirically in all patients with suspected encephalitis without waiting for PCR results.",
   "rationale":"HSV encephalitis without treatment carries high mortality (~70%) and severe neurological morbidity; early acyclovir dramatically improves outcomes; PCR on CSF may take days.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":4}],"confusable_with":""},
  {"id":"viral-meningitis-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the incidence of viral encephalitis and which demographic groups are most affected?",
   "answer":"Incidence 3.5-7.5 per 100,000 persons; highest in young children and the elderly — the two age groups with relatively immature or declining immune function.",
   "rationale":"Immunological vulnerability at age extremes predisposes to more severe viral neuroinvasion; epidemiology has changed with vaccination reducing measles/mumps/rubella encephalitis.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":2}],"confusable_with":""},
  {"id":"viral-meningitis-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Japanese encephalitis virus (JEV) encephalitis is notable for producing what neurological syndrome that mimics another condition?",
   "answer":"JEV encephalitis may produce extrapyramidal symptoms (rigidity, bradykinesia, tremor) that mimic Parkinson disease.",
   "rationale":"JEV infects the basal ganglia and substantia nigra; this neurotropism produces parkinsonian features as a characteristic neurological complication.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":3}],"confusable_with":"Parkinson disease"},
  {"id":"viral-meningitis-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"CMV encephalitis treatment uses what combination regimen and what alternative exists?",
   "answer":"CMV encephalitis is treated with ganciclovir + foscarnet combination; acyclovir 10-15 mg/kg IV q8h with possible adjunctive corticosteroids is used for varicella-zoster encephalitis.",
   "rationale":"CMV is resistant to acyclovir and requires ganciclovir (inhibits CMV DNA polymerase) often combined with foscarnet for synergy in severe CNS disease.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":4}],"confusable_with":""},
  {"id":"viral-meningitis-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the key epidemiological elements in the history of a patient with viral encephalitis that help identify the causative virus?",
   "answer":"Immune status, exposure to insects/animals/birds, travel history, vaccination history, geographic region, time of year; rash/skin vesicles (herpes zoster), flaccid paralysis (West Nile), animal bites (rabies).",
   "rationale":"Arboviral encephalitides (WNV, EEE, LaCrosse) are seasonal and vector-specific; exposure history narrows the differential before serology/PCR results.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":3}],"confusable_with":""},
  {"id":"viral-meningitis-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What does it cost the healthcare system for a single bout of viral encephalitis in the United States?",
   "answer":"A single bout of viral encephalitis can cost upwards of $2 million; untreated herpes encephalitis mortality is high, justifying aggressive empirical treatment.",
   "rationale":"The economic burden of viral encephalitis reflects prolonged ICU care, rehabilitation, and long-term disability; early empirical acyclovir reduces this burden.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":5}],"confusable_with":""},
]
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Any age; immunocompromised (CMV, VZV, HHV-6); summer/fall arboviral exposure; herpes viral reactivation",
  "pathophysiology":"Direct viral neuronal invasion and/or immune-mediated inflammation; HSV: temporal lobe necrosis; arbovirus: basal ganglia/thalamic involvement",
  "time_course":"Acute over hours-days; fever + headache -> AMS -> seizures; HSV may show characteristic temporal lobe involvement on MRI",
  "key_features":"Fever, headache, altered consciousness, seizures, neuropsychiatric features; temporal lobe hypersignal on MRI (HSV); CSF: lymphocytic pleocytosis, elevated protein, normal glucose",
  "consequence_if_missed":"Fatal untreated HSV encephalitis (70% mortality untreated); permanent neurological disability"})

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch5.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch5")
