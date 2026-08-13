import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# =====================================================================
# [0] Dural puncture epidural (DPE) analgesia
# =====================================================================
topic0 = "Dural puncture epidural (DPE) analgesia"
dom0 = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"

kps += [
  {"id":"dural-puncture-epidural-dpe-analgesia-d1","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"A DPE technique passes a spinal needle through the epidural needle to puncture the dura without injecting drug, then places an epidural catheter. What is the primary proposed mechanism for improved analgesia compared with standard epidural?",
   "answer":"Microfenestrations in the dura allow small amounts of epidural drug to migrate intrathecally, enhancing spread and onset without a full intrathecal dose.",
   "rationale":"The dural rent acts as a passive conduit for drug transfer into the subarachnoid space, improving block quality beyond epidural alone.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1400}],"confusable_with":"CSE (combined spinal-epidural)"},

  {"id":"dural-puncture-epidural-dpe-analgesia-d2","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"Compared with CSE for labor analgesia, which side effects are LESS frequent with DPE technique?",
   "answer":"DPE has less opioid-based pruritus, less uterine tachysystole, and lower incidence of fetal bradycardia after block placement; headache risk is similar.",
   "rationale":"CSE delivers drug directly intrathecally; DPE achieves augmented epidural analgesia without a full intrathecal bolus, reducing opioid-mediated and uterine side effects.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":613}],"confusable_with":"CSE"},

  {"id":"dural-puncture-epidural-dpe-analgesia-d3","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"What design feature of the Tuohy epidural needle reduces inadvertent dural puncture compared with straight-tipped Crawford needles?",
   "answer":"The Tuohy needle has a blunt curved tip (15-30 degrees) that pushes the dura away after passing through the ligamentum flavum rather than penetrating it.",
   "rationale":"The curved blunt tip deflects the dura on contact, reducing the likelihood of unintentional wet tap during epidural placement.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1585}],"confusable_with":"Crawford needle"},

  {"id":"dural-puncture-epidural-dpe-analgesia-d4","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"After accidental dural puncture with a large epidural needle in a young pregnant woman, what is the approximate incidence of PDPH?",
   "answer":"Approximately 20-50% of young pregnant women who experience accidental dural puncture with a large epidural needle will develop PDPH.",
   "rationale":"Larger gauge needles create bigger dural rents with greater CSF leakage; young women are at greater risk due to higher baseline CSF pressure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1600}],"confusable_with":""},

  {"id":"dural-puncture-epidural-dpe-analgesia-d5","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"For epidural placement in an obese parturient, which patient position best facilitates midline identification?",
   "answer":"The sitting position makes it easier to identify the midline and spine, particularly in obese patients.",
   "rationale":"Gravity helps separate adipose tissue folds and accentuates spinous process landmarks when the patient is upright.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1394}],"confusable_with":""},

  {"id":"dural-puncture-epidural-dpe-analgesia-d6","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"A thoracic epidural produces anesthesia over upper abdominal dermatomes while sparing cervical and lower lumbar roots. What is this pattern called and what enables it?",
   "answer":"Segmental block -- anesthetic is confined close to the injection level, blocking only nerve roots at that dermatome, leaving roots above and below unblocked.",
   "rationale":"Local anesthetic injected epidurally diffuses radially and cephalocaudally but remains concentrated near the injection site, allowing targeted segmental blockade.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1583}],"confusable_with":"total spinal"},

  {"id":"dural-puncture-epidural-dpe-analgesia-d7","topic":topic0,"domain":dom0,"discipline":disc,
   "stem":"What are the first-line conservative treatments for PDPH before considering epidural blood patch?",
   "answer":"Recumbent positioning, hydration, caffeine, and oral analgesics; spontaneous resolution within 7 days in most cases.",
   "rationale":"Supine positioning reduces the hydrostatic gradient driving CSF loss; caffeine is a cerebral vasoconstrictor that reduces compensatory dilation causing the headache.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":""},
]

# =====================================================================
# [1] Eclampsia management
# =====================================================================
topic1 = "Eclampsia management"
dom1 = dom0

kps += [
  {"id":"eclampsia-management-d1","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"A pregnant woman has a generalized tonic-clonic seizure. What is the first-line medication for seizure management and prevention of recurrence, and what is the loading dose?",
   "answer":"Magnesium sulfate is first-line: 4-6 g IV bolus over 15-20 minutes, then 1-2 g/h infusion maintenance.",
   "rationale":"Magnesium prevents recurrent eclamptic seizures (by ~60% vs placebo) through NMDA receptor antagonism and membrane stabilization.",
   "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":"diazepam or phenytoin"},

  {"id":"eclampsia-management-d2","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"During magnesium infusion for eclampsia prophylaxis, what three clinical signs should prompt discontinuation of the infusion?",
   "answer":"Stop magnesium if: urine output <80 mL over 4 hours, deep tendon reflexes are absent, or respiratory rate <12/min.",
   "rationale":"These signs indicate approaching toxic magnesium levels; loss of DTRs precedes respiratory arrest, providing a clinical warning window.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":5}],"confusable_with":""},

  {"id":"eclampsia-management-d3","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"What is the therapeutic serum magnesium target range for eclampsia management?",
   "answer":"Therapeutic serum magnesium: 1.7 to 3.5 mmol/L.",
   "rationale":"Levels in this range are anticonvulsant; toxicity (respiratory depression, cardiac arrest) occurs at levels >5 mmol/L, hence periodic serum level monitoring is essential.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":3}],"confusable_with":""},

  {"id":"eclampsia-management-d4","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"A preeclamptic patient has no headache or visual changes. Can eclamptic seizures still occur without warning symptoms?",
   "answer":"Yes -- eclamptic seizures may occur without antecedent warning symptoms; absence of prodrome does not exclude impending eclampsia.",
   "rationale":"Up to 25% of eclamptic seizures occur without premonitory symptoms; clinicians must not be falsely reassured by absence of prodrome in a preeclamptic patient.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":""},

  {"id":"eclampsia-management-d5","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"HELLP syndrome is a severe subcategory of preeclampsia. What does the acronym stand for?",
   "answer":"Hemolysis, Elevated Liver enzymes, Low Platelet count.",
   "rationale":"HELLP reflects widespread microangiopathic endothelial injury causing hemolysis, hepatic damage, and platelet consumption -- all manifestations of severe preeclampsia.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":621}],"confusable_with":"TTP/HUS"},

  {"id":"eclampsia-management-d6","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"How does magnesium sulfate affect neuromuscular blocking agents administered during cesarean delivery for eclampsia?",
   "answer":"Magnesium increases the efficacy and prolongs the duration of both depolarizing and non-depolarizing NMBs; doses must be reduced and neuromuscular monitoring used.",
   "rationale":"Magnesium inhibits presynaptic acetylcholine release and competes with calcium at the neuromuscular junction, potentiating the effect of NMB drugs.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":622}],"confusable_with":""},

  {"id":"eclampsia-management-d7","topic":topic1,"domain":dom1,"discipline":disc,
   "stem":"Eclamptic seizures develop in what approximate proportion of patients with preeclampsia?",
   "answer":"Less than 2% of patients with preeclampsia develop eclamptic seizures.",
   "rationale":"Most preeclampsia is managed without seizures; eclampsia represents severe end-organ involvement and is distinct from the broader preeclamptic spectrum.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":621}],"confusable_with":""},

  {"_type":"illness_script","topic":topic1,"discipline":disc,
   "enabling_conditions":"Primigravida, multiple gestation, chronic hypertension, diabetes, antiphospholipid syndrome, prior preeclampsia",
   "pathophysiology":"Severe endothelial dysfunction in preeclampsia causes cerebral vasospasm and/or breakthrough hyperperfusion, triggering generalized tonic-clonic seizures not attributable to other causes",
   "time_course":"Seizures occur antepartum (>50%), intrapartum (~25%), or postpartum (up to 48h after delivery); may be sudden without prodrome",
   "key_features":"Tonic-clonic seizures in setting of preeclampsia; secure airway, lateral position; magnesium 4-6g IV bolus then infusion; fetal monitoring; treat severe hypertension",
   "consequence_if_missed":"Maternal aspiration, intracranial hemorrhage, placental abruption, fetal hypoxia and death from prolonged seizure"},
]

# =====================================================================
# [2] Effects of Anesthetic Agents on Cerebral Physiology
# =====================================================================
topic2 = "Effects of Anesthetic Agents on Cerebral Physiology"
dom2 = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"

kps += [
  {"id":"effects-anesthetic-agents-cerebral-physiology-d1","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"Most general anesthetics have a favorable effect on brain energy consumption. What is the key mechanism?",
   "answer":"Most general anesthetics reduce CMRO2 by decreasing electrical activity (EEG suppression), thereby reducing metabolic demand.",
   "rationale":"Anesthetics depress neuronal firing and synaptic transmission; less electrical work translates directly to lower oxygen consumption, providing a margin of protection during ischemia.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":947}],"confusable_with":""},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d2","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"Volatile anesthetics cause dose-dependent depression of cerebral autoregulation. At what MAP range is autoregulation intact in a healthy brain?",
   "answer":"Cerebral autoregulation is intact when MAP is between 50-60 mmHg and 150-160 mmHg; blood flow increases or decreases only outside these limits.",
   "rationale":"Volatile agents impair the myogenic and metabolic mechanisms that maintain constant CBF over a wide pressure range, making the brain pressure-passive under deep anesthesia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":935}],"confusable_with":""},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d3","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"Volatile agents initially increase CBF despite reducing CMRO2. What intervention can abolish or blunt this increase?",
   "answer":"Hyperventilation (hypocapnia) can abolish or blunt the CBF-increasing effects of volatile agents because CO2 reactivity is generally retained with all volatile agents.",
   "rationale":"Volatile agents increase CBF through cerebrovascular dilation; since cerebrovascular CO2 responsiveness is preserved, lowering PaCO2 via hyperventilation causes vasoconstriction and overrides the volatile-agent-induced increase.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":949}],"confusable_with":""},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d4","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"With continued administration of volatile agents (2-5 hours), what happens to CBF changes initially caused by the agent?",
   "answer":"With prolonged administration, CBF begins to return toward normal (the initial increase is time-dependent and attenuates over 2-5 hours).",
   "rationale":"Cerebrovascular adaptation occurs with sustained volatile agent exposure; autoregulatory mechanisms partially compensate, reducing the initial cerebral vasodilation.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":949}],"confusable_with":""},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d5","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"Ketamine has effects on CBF and ICP distinct from most other IV anesthetics. What are they?",
   "answer":"Ketamine increases CBF and ICP (unlike most IV agents which decrease them) due to its sympathomimetic effects and direct cerebral vasodilation.",
   "rationale":"Ketamine stimulates CNS sympathetic outflow and may directly dilate cerebral vasculature; this makes it relatively contraindicated in patients with elevated ICP unless airway is secured and ventilation controlled.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2280}],"confusable_with":"propofol"},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d6","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"The EEG is used to monitor patients undergoing carotid endarterectomy under general anesthesia. What EEG change prompts concern about cerebral ischemia?",
   "answer":"Gross EEG changes -- slowing or loss of activity -- associated with carotid clamping indicate potentially significant cerebral ischemia and may prompt shunt placement.",
   "rationale":"Anesthetic agents affect baseline EEG, but abrupt changes from clamping reflect a sudden reduction in ipsilateral cerebral blood flow; detecting these changes is the key monitoring goal.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":963}],"confusable_with":""},

  {"id":"effects-anesthetic-agents-cerebral-physiology-d7","topic":topic2,"domain":dom2,"discipline":disc,
   "stem":"Hypothermia is considered the most effective method for cerebral protection. During what type of ischemia is it most beneficial?",
   "answer":"Hypothermia is the most effective method for protecting the brain during both focal and global ischemia.",
   "rationale":"Lowering brain temperature reduces CMRO2 by 6-7% per 1 degree C reduction, dramatically decreasing the rate of ATP depletion and excitotoxic injury during ischemia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":935}],"confusable_with":"barbiturate coma"},
]

# =====================================================================
# [3] Electricity, Safety, and Monitoring Principles
# =====================================================================
topic3 = "Electricity, Safety, and Monitoring Principles"
dom3 = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"

kps += [
  {"id":"electricity-safety-monitoring-principles-d1","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"Leakage current is present in all electrical equipment. How does an accidentally grounded patient become at risk for macroshock?",
   "answer":"An accidentally grounded person who simultaneously contacts the hot wire of defective equipment completes an electrical circuit -- the loop originates with the transformer and passes through the victim via ground contact.",
   "rationale":"Leakage current normally flows harmlessly to ground; when the patient bridges the circuit between the hot conductor and ground, lethal current can flow through the body.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":44}],"confusable_with":"microshock"},

  {"id":"electricity-safety-monitoring-principles-d2","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"When using electrosurgery near an implanted pacemaker or defibrillator, how should the return electrode (dispersive pad) be positioned?",
   "answer":"Place the return electrode as close to the surgical field as practical and as far from the implanted device as possible.",
   "rationale":"This routing minimizes electrosurgical current through the implanted device; current flowing through the device can cause pacemaker inhibition, inappropriate shock delivery, or device damage.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":49}],"confusable_with":""},

  {"id":"electricity-safety-monitoring-principles-d3","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"What is the last line of defense against the patient receiving a hypoxic gas mixture from the anesthesia machine?",
   "answer":"The oxygen analyzer (typically a galvanic cell sensor) in the breathing circuit, with a low O2 concentration alarm that must sound within 30 seconds if FiO2 drops below the set limit (not less than 18%).",
   "rationale":"Upstream safeguards (pin index, proportional valves) can fail; the inspired oxygen analyzer independently verifies gas composition at the patient interface.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":266}],"confusable_with":""},

  {"id":"electricity-safety-monitoring-principles-d4","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"ASA Standard II requires continuous evaluation of four patient parameters during all anesthetics. What are they?",
   "answer":"Oxygenation, ventilation, circulation, and temperature must be continually evaluated during all anesthetics (ASA Standard II).",
   "rationale":"These four parameters encompass the major physiological systems at risk during anesthesia; failure of any one can rapidly lead to patient harm.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":13}],"confusable_with":""},

  {"id":"electricity-safety-monitoring-principles-d5","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"During an anesthesia time-out before induction, what six items should the anesthesia provider confirm?",
   "answer":"(1) monitors functional, (2) capnogram tracing present, (3) oxygen saturation displayed, (4) airway equipment ready, (5) suction working, (6) drugs prepared -- an institutional checklist approach.",
   "rationale":"The pre-induction anesthesia time-out systematically verifies readiness across equipment, monitoring, and pharmacological domains, reducing errors of omission.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":276}],"confusable_with":""},

  {"id":"electricity-safety-monitoring-principles-d6","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"In crew resource management (CRM) applied to anesthesia, what is the defined role of communication?",
   "answer":"Communication is the clear and accurate sending and receiving of information, instructions, or commands with useful feedback; it is a two-way loop process.",
   "rationale":"CRM principles recognize that closed-loop communication (sender confirms receipt and understanding) prevents miscommunication errors that are a common root cause in anesthetic adverse events.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},

  {"id":"electricity-safety-monitoring-principles-d7","topic":topic3,"domain":dom3,"discipline":disc,
   "stem":"Residual neuromuscular blockade occurs frequently postoperatively. What is the standard of care to address this?",
   "answer":"Monitoring of neuromuscular blockade (train-of-four) and pharmacological reversal are standard of care for patients receiving NMBAs.",
   "rationale":"Residual NMB impairs airway protective reflexes and ventilation; objective TOF monitoring detects incomplete recovery that clinical signs alone miss.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":37}],"confusable_with":""},
]

# =====================================================================
# [4] Electrolyte Disturbances - Cardiac Effects
# =====================================================================
topic4 = "Electrolyte Disturbances - Cardiac Effects"
dom4 = "Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)"

kps += [
  {"id":"electrolyte-disturbances-cardiac-effects-d1","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"Isolated hypomagnesemia should be corrected before elective surgery. What is the primary cardiac concern?",
   "answer":"Hypomagnesemia can cause arrhythmias; magnesium also has intrinsic antiarrhythmic properties, so correction reduces perioperative arrhythmia risk.",
   "rationale":"Magnesium stabilizes myocardial cell membranes, suppresses triggered activity, and is necessary for Na/K-ATPase function; deficiency lowers the threshold for ventricular arrhythmias.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1900}],"confusable_with":"hypokalemia"},

  {"id":"electrolyte-disturbances-cardiac-effects-d2","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"Hyperkalemia exceeding what level always requires correction because of its lethal potential?",
   "answer":"Hyperkalemia exceeding 6 mEq/L should always be corrected due to its lethal potential.",
   "rationale":"Potassium >6 mEq/L can cause progressive ECG changes (peaked T-waves, PR prolongation, wide QRS, sine wave pattern) leading to ventricular fibrillation or asystole.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},

  {"id":"electrolyte-disturbances-cardiac-effects-d3","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"In the management of symptomatic hypercalcemia, what is the most effective initial treatment?",
   "answer":"Rehydration followed by brisk diuresis (urinary output 200-300 mL/h) using IV saline and a loop diuretic to accelerate calcium excretion.",
   "rationale":"Volume expansion dilutes serum calcium and increases GFR; loop diuretics inhibit tubular calcium reabsorption, accelerating urinary calcium loss.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},

  {"id":"electrolyte-disturbances-cardiac-effects-d4","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"Symptomatic hypocalcemia is a medical emergency. What is the immediate IV treatment?",
   "answer":"IV calcium chloride (3-5 mL of 10% solution) or calcium gluconate (10-20 mL of 10% solution) given immediately.",
   "rationale":"Calcium directly stabilizes myocardial membrane potential; hypocalcemia causes neuromuscular excitability, hypotension, and can lead to cardiac arrest if untreated.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":"calcium gluconate vs calcium chloride dosing"},

  {"id":"electrolyte-disturbances-cardiac-effects-d5","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"Coexistent electrolyte disturbances should be corrected before elective surgery in a patient with isolated hypomagnesemia. What three electrolyte abnormalities are often concurrently present?",
   "answer":"Hypokalemia, hypophosphatemia, and hypocalcemia are often present concurrently with hypomagnesemia and should be corrected preoperatively.",
   "rationale":"Magnesium is required for parathyroid hormone secretion and renal potassium conservation; deficiency commonly depletes calcium and potassium through multiple mechanisms.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1900}],"confusable_with":""},

  {"id":"electrolyte-disturbances-cardiac-effects-d6","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"Potassium is the most important determinant of which osmotic compartment?",
   "answer":"Potassium is the most important determinant of intracellular osmotic pressure; sodium is the most important determinant of extracellular osmotic pressure.",
   "rationale":"ICF potassium and ECF sodium create the osmotic gradients that determine fluid distribution between cellular and extracellular compartments.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1845}],"confusable_with":""},

  {"id":"electrolyte-disturbances-cardiac-effects-d7","topic":topic4,"domain":dom4,"discipline":disc,
   "stem":"What ECG tool is described as valuable for diagnosing disturbances of cardiac conduction and rhythm in the perioperative setting?",
   "answer":"The ECG is a valuable tool for diagnosing disturbances of cardiac conduction and rhythm and should be monitored when electrolyte disturbances are present.",
   "rationale":"Electrolyte changes (K, Ca, Mg) directly affect cardiac action potential duration and threshold, producing characteristic ECG changes that guide diagnosis and treatment.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":490}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
