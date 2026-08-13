import json

kps = []

# ============================================================
# [0] Dural puncture epidural (DPE) analgesia
# ============================================================
t = "Dural puncture epidural (DPE) analgesia"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "dpe-analgesia"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"In the DPE technique, what is the sequence of needle and catheter placement?",
 "answer":"Intrathecal drugs injected through the spinal needle -> spinal needle withdrawn -> epidural catheter placed through the epidural needle",
 "rationale":"The spinal needle punctures the dura to deliver intrathecal drugs while the epidural catheter provides the route for ongoing labor analgesia or cesarean extension.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1401}],"confusable_with":"CSE technique"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What advantage does adding a small local anesthetic dose to the intrathecal opioid confer in DPE?",
 "answer":"Small intrathecal local anesthetic dose greatly potentiates opioid efficacy and significantly reduces total opioid requirements",
 "rationale":"Synergy at spinal cord level between opioid receptor agonism and sodium channel blockade reduces the total dose of each agent needed.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1401}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the incidence of PDPH when a large epidural needle accidentally punctures the dura in a young parturient?",
 "answer":"As high as 20-50% with a large epidural needle in a young pregnant woman",
 "rationale":"Young age and female sex increase risk; large needle caliber (17-18 gauge) creates a larger dural defect than pencil-point spinal needles.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1600}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the definitive therapy for PDPH and what is its success rate?",
 "answer":"Epidural blood patch is definitive therapy; single patch results in 90% initial improvement rate",
 "rationale":"Autologous blood injected into the epidural space seals the dural defect and raises epidural pressure, eliminating the CSF leak.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"Conservative treatment (recumbent positioning, caffeine, analgesics)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why is the Tuohy needle preferred over straight epidural needles for epidural placement?",
 "answer":"Blunt curved tip deflects the dura after traversing ligamentum flavum rather than penetrating it; straight Crawford needles have higher dural puncture incidence",
 "rationale":"The 15-30 degree curve tip pushes the dura away mechanically, reducing accidental wet tap rates compared with cutting-tip designs.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1585}],"confusable_with":"Crawford needle (straight tip, higher PDPH rate)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What PDPH rate can be achieved with small-gauge pencil-point needles for obstetric spinal anesthesia?",
 "answer":"As low as 3-4% with small-gauge pencil-point needles for cesarean delivery spinal anesthesia",
 "rationale":"Atraumatic pencil-point tip spreads rather than cuts dural fibers, causing less CSF leakage after needle withdrawal.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1600}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What position promotes sacral spread when placing an epidural for second-stage vaginal delivery?",
 "answer":"Sitting position promotes sacral spread of epidural local anesthetic",
 "rationale":"Gravity directs solution caudally toward sacral nerve roots when the patient remains seated after epidural injection.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1394}],"confusable_with":""},
{"id":f"{s}-d8","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the key advantage of a functioning epidural catheter when urgent cesarean delivery becomes necessary?",
 "answer":"Allows rapid extension to surgical anesthesia (T4 level), avoiding general anesthesia with its aspiration and difficult-airway risks in the parturient",
 "rationale":"Epidural catheter can be dosed with alkalinized lidocaine or 3% chloroprocaine for rapid surgical-level block, bypassing GA risks.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1394}],"confusable_with":""},
]

kps.append({"_type":"illness_script","topic":t,"discipline":disc,
 "enabling_conditions":"Parturient requesting neuraxial analgesia; severe early labor pain; desire for rapid onset with ongoing epidural flexibility",
 "pathophysiology":"Intentional dural puncture with spinal needle through epidural needle creates intrathecal drug delivery; epidural catheter provides ongoing dosing; microscopic hole may enhance epidural-to-intrathecal drug transfer",
 "time_course":"Immediate onset (minutes) from intrathecal component; continuous analgesia via epidural catheter throughout labor",
 "key_features":"Faster onset than plain epidural; PDPH risk from dural puncture; avoids CSE fetal bradycardia risk",
 "consequence_if_missed":"Failure to recognize intravascular or intrathecal catheter misplacement can cause LAST or total spinal"})

# ============================================================
# [1] Eclampsia management
# ============================================================
t = "Eclampsia management"
dom = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
disc = "anesthesia"
s = "eclampsia-mgmt"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the first-line agent for seizure management in eclampsia and what is the loading dose and infusion rate?",
 "answer":"Magnesium sulfate first-line: 4-6 g IV bolus over 15-20 min loading dose, then 1-2 g/h maintenance infusion",
 "rationale":"Magnesium prevents approximately 60% of seizures in preeclampsia by acting as an NMDA antagonist and reducing cerebral vasospasm.",
 "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":"Benzodiazepines (second-line only)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What therapeutic serum magnesium level is targeted in eclampsia management?",
 "answer":"Therapeutic serum magnesium 1.7 to 3.5 mmol/L for eclampsia",
 "rationale":"Below this range seizure prophylaxis is inadequate; above it, progressive toxicity (lost reflexes, respiratory depression, cardiac arrest) ensues.",
 "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":3}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What three clinical signs require stopping the magnesium infusion in eclampsia?",
 "answer":"Stop magnesium if: urine output <80 mL in 4 hours, deep tendon reflexes absent, or respiratory rate <12/min",
 "rationale":"These signs indicate impending magnesium toxicity; respiratory arrest and cardiac arrest follow at progressively higher serum levels.",
 "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":5}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What BP threshold defines preeclampsia with severe features?",
 "answer":"SBP >=160 mmHg or DBP >=110 mmHg on two occasions at least 4 hours apart",
 "rationale":"Sustained severe hypertension at this level drives stroke risk; the 4-hour interval distinguishes episodic from sustained severe hypertension.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":621}],"confusable_with":"Preeclampsia without severe features"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What proportion of preeclamptic patients develop eclamptic seizures?",
 "answer":"Less than 2% of patients with preeclampsia develop eclamptic seizures",
 "rationale":"Most preeclampsia does not progress to eclampsia; seizures may occur without antecedent warning symptoms.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":621}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What essential laboratory monitoring is required during high-dose magnesium therapy for eclampsia?",
 "answer":"Periodic serum magnesium levels plus renal function (urine output, BUN, creatinine, GFR) and electrolytes (K, Ca, Phos)",
 "rationale":"Magnesium is renally cleared with a half-life of approximately 28 hours; reduced GFR prolongs half-life and escalates toxicity risk.",
 "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":5}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does magnesium sulfate affect neuromuscular blocking agents, and what clinical implication does this have?",
 "answer":"Magnesium significantly increases efficacy and prolongs duration of both depolarizing and non-depolarizing NMBAs; reduce NMB doses and monitor neuromuscular function carefully",
 "rationale":"Magnesium competes with calcium at the neuromuscular junction, reducing acetylcholine release and decreasing motor end-plate sensitivity.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":622}],"confusable_with":""},
{"id":f"{s}-d8","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the immediate management sequence after an eclamptic seizure begins?",
 "answer":"Secure airway (lateral position, prevent aspiration) -> oxygen -> fetal monitoring -> magnesium sulfate loading dose",
 "rationale":"Lateral positioning clears the airway; fetal monitoring detects bradycardia from maternal hemodynamic compromise during and after the seizure.",
 "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":""},
]

kps.append({"_type":"illness_script","topic":t,"discipline":disc,
 "enabling_conditions":"Parturient with preeclampsia; hypertension; prior headache, visual changes, or epigastric pain",
 "pathophysiology":"Eclampsia = preeclampsia + generalized tonic-clonic seizures; cerebral vasospasm and endothelial dysfunction lower seizure threshold",
 "time_course":"May occur without warning antepartum, intrapartum, or postpartum",
 "key_features":"Tonic-clonic seizures in preeclamptic patient; may lack prodrome; HELLP syndrome is a subset",
 "consequence_if_missed":"Maternal stroke, aspiration, death; fetal hypoxia and acidosis from placental insufficiency during seizure"})

# ============================================================
# [2] Effects of Anesthetic Agents on Cerebral Physiology
# ============================================================
t = "Effects of Anesthetic Agents on Cerebral Physiology"
dom = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
disc = "anesthesia"
s = "anes-cerebral-physiology"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"Within what MAP range does cerebral autoregulation maintain constant CBF?",
 "answer":"Cerebral autoregulation maintains constant CBF when MAP is between approximately 50-60 mmHg (lower limit) and 150-160 mmHg (upper limit)",
 "rationale":"Outside this range CBF becomes pressure-passive; below the lower limit ischemia threatens, above the upper limit hyperemia and edema occur.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":935}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What effect do volatile agents have on cerebral autoregulation, and is CO2 reactivity preserved?",
 "answer":"Volatile agents cause dose-dependent depression of cerebral autoregulation; the CBF response to CO2 is generally retained with all volatile agents",
 "rationale":"Volatile agents directly vasodilate cerebral vessels; CO2 reactivity is mediated via pH at arteriolar smooth muscle, a separate pathway.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":949}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does timing of hyperventilation relative to halothane administration affect the CBF increase?",
 "answer":"With halothane, hyperventilation must be initiated BEFORE administration to prevent halothane-induced CBF increases; post-halothane hyperventilation is less effective",
 "rationale":"Halothane's vasodilatory effect on CBF is time-dependent; pretreatment with hypocapnia establishes vasoconstriction before the direct vasodilator effect begins.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":949}],"confusable_with":"Other volatile agents (timing less critical)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the most effective method for brain protection during both focal and global ischemia?",
 "answer":"Hypothermia is the most effective method for brain protection during focal and global ischemia",
 "rationale":"Hypothermia reduces CMRO2 approximately 7% per 1 degree C, attenuating excitotoxicity, free radical production, and inflammation.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":935}],"confusable_with":"Barbiturates (effective for focal but not global ischemia)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"Barbiturates provide neuroprotection in what type but NOT what type of cerebral ischemia?",
 "answer":"Barbiturates provide neuroprotection from focal cerebral ischemia (stroke, retraction, temporary clips) but probably NOT from global cerebral ischemia (cardiac arrest)",
 "rationale":"Barbiturates suppress electrical activity and reduce CMRO2, which is beneficial when some perfusion remains (focal) but not when global perfusion is absent.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":139}],"confusable_with":"Hypothermia (effective for both focal and global)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are etomidate's EEG effects, and in what clinical setting can this be exploited therapeutically?",
 "answer":"Etomidate causes excitatory EEG spikes more frequently than thiopental and may activate seizure foci; exploited in ECT to facilitate longer motor seizure activity",
 "rationale":"Etomidate's combination of CMRO2 reduction with excitatory spike activity is paradoxical; the excitatory component is clinically useful in ECT.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"Propofol (anticonvulsant properties)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What cerebral effects does ketamine produce, and how can they be blunted?",
 "answer":"Ketamine increases CBF and ICP; hypocapnia (hyperventilation) blunts these increases",
 "rationale":"Ketamine is a sympathomimetic and direct cerebral vasodilator; concurrent hypocapnia-mediated vasoconstriction counteracts this effect.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":947}],"confusable_with":"Propofol (decreases CBF/ICP)"},
{"id":f"{s}-d8","topic":t,"domain":dom,"discipline":disc,
 "stem":"During CEA under general anesthesia, what neurophysiological monitoring is used and what intraoperative finding indicates need for shunt placement?",
 "answer":"EEG monitoring; gross changes with carotid clamping indicate ischemia -> surgeon places vascular shunt for ipsilateral cerebral perfusion",
 "rationale":"Carotid cross-clamping interrupts ipsilateral CBF; EEG slowing/amplitude reduction signals ischemia and guides surgical shunt decision.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":963}],"confusable_with":""},
]

# ============================================================
# [3] Electricity, Safety, and Monitoring Principles
# ============================================================
t = "Electricity, Safety, and Monitoring Principles"
dom = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
disc = "anesthesia"
s = "electricity-safety"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does leakage current arise in OR electrical equipment, and what is the pathway that creates electrocution risk?",
 "answer":"Leakage current arises in all electrical equipment from capacitive coupling; risk pathway: hot wire -> defective equipment -> patient -> ground contact -> neutral transformer",
 "rationale":"Even with intact insulation, capacitive coupling between wires generates small leakage currents that can cause ventricular fibrillation if directed through the heart.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":44}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"How should the electrosurgery return electrode be positioned in patients with implanted cardiac devices?",
 "answer":"Place return electrode as close to the surgical field and as far from the implanted cardiac device as practical",
 "rationale":"This minimizes the current path through cardiac tissue, reducing the risk of pacemaker/ICD malfunction or inappropriate shock.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":49}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What oxygen monitoring alarm is mandatory on the anesthesia machine and at what threshold must it sound?",
 "answer":"Low oxygen concentration alarm must sound within 30 seconds if inspired oxygen drops below a set limit that cannot be adjusted below 18%; galvanic cell O2 analyzer requires daily calibration",
 "rationale":"The O2 analyzer is the last defense against delivering a hypoxic gas mixture; alarm is mandatory under ASA standards.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":266}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the ASA Standard II monitoring requirements during all anesthetics?",
 "answer":"Continually evaluate oxygenation, ventilation, circulation, and temperature; required: FiO2 analyzer + alarm, pulse oximetry, capnography (expired Vt), and temperature monitoring",
 "rationale":"These mandatory monitors detect the most common life-threatening intraoperative physiologic derangements.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":13}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What six items are confirmed during the pre-induction anesthesia time-out?",
 "answer":"(1) monitors functional; (2) capnogram tracing present; (3) SpO2 measured; (4) flowmeter/ventilator settings working; (5) manual/ventilator switch set to manual; (6) vaporizer adequately filled",
 "rationale":"The pre-induction checklist catches equipment failures before the patient is anesthetized and cannot report problems.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":276}],"confusable_with":"Surgical safety time-out (different purpose and content)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"In crew resource management (CRM), what specific communication structure is required to minimize error?",
 "answer":"Communication must be closed-loop (two-way): clear sending AND receiving with feedback confirming understanding; not one-directional",
 "rationale":"One-way communication without closed-loop confirmation is a common root cause of OR errors; feedback confirms messages are received and accurately understood.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":57}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why can high-frequency electrosurgical current cause burns even when the intended circuit path appears intact?",
 "answer":"High-frequency current can complete circuit gaps via capacitances (without requiring recognized conductors); small contact-area current concentration produces burns",
 "rationale":"Capacitive coupling bypasses insulators and air gaps at high frequencies, redirecting current to unintended grounding paths with potentially high current density.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":49}],"confusable_with":""},
]

# ============================================================
# [4] Electrolyte Disturbances - Cardiac Effects
# ============================================================
t = "Electrolyte Disturbances — Cardiac Effects"
dom = "Critical care & ICU medicine (sepsis/shock, mechanical ventilation, AKI, electrolytes, hemodynamics, vasopressors, end-organ support)"
disc = "anesthesia"
s = "electrolyte-cardiac"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"Which electrolyte disturbances should be corrected before elective surgery because of arrhythmia risk?",
 "answer":"Correct hypokalemia, hypophosphatemia, hypocalcemia, and hypomagnesemia before elective procedures; magnesium is administered preemptively in cardiac surgery for its antiarrhythmic properties",
 "rationale":"These deficiencies lower arrhythmia threshold; magnesium has intrinsic antiarrhythmic and possible cerebral protective effects.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1900}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"At what serum potassium level must hyperkalemia always be treated due to lethal cardiac risk?",
 "answer":"Hyperkalemia exceeding 6 mEq/L should always be corrected",
 "rationale":"Severe hyperkalemia causes peaked T-waves, QRS widening, sine-wave pattern, ventricular fibrillation or asystole.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the most effective initial treatment for symptomatic hypercalcemia?",
 "answer":"Rehydration followed by brisk diuresis (urinary output 200-300 mL/h) using IV saline plus loop diuretic to accelerate calcium excretion",
 "rationale":"Volume expansion dilutes serum calcium and increases GFR; loop diuretics block calcium reabsorption in the ascending loop of Henle.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"How is symptomatic hypocalcemia treated emergently?",
 "answer":"IV calcium chloride (3-5 mL of 10% solution) or calcium gluconate (10-20 mL of 10% solution) immediately",
 "rationale":"Ionized hypocalcemia causes myocardial depression, QT prolongation, and tetany; calcium chloride provides 3x more ionized calcium per mL than gluconate.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1846}],"confusable_with":"Calcium gluconate vs. calcium chloride dosing"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why is isolated hypomagnesemia corrected before elective procedures?",
 "answer":"Isolated hypomagnesemia is corrected before elective procedures because of potential to cause arrhythmias",
 "rationale":"Magnesium stabilizes cardiac membrane potential and inhibits arrhythmogenic triggered activity; deficiency particularly dangerous in cardiac surgery patients.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1900}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What cardiovascular effects have been associated with rapid acetate accumulation from large-volume balanced crystalloid infusion?",
 "answer":"Rapid acetate accumulation has been associated with hypotension and decreased cardiac contractility",
 "rationale":"Acetate is a vasodilator and negative inotrope at high plasma concentrations; metabolism to bicarbonate may also cause alkalosis affecting myocardial function.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":463}],"confusable_with":"Lactate (Ringer's lactate) - different metabolic handling"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What cardiac rhythm intervention is contraindicated for ectopic or multifocal atrial tachycardia, and what treatments are appropriate?",
 "answer":"DC cardioversion is contraindicated for ectopic or multifocal atrial tachycardia; treat with amiodarone or calcium channel blockers/beta-blockers",
 "rationale":"MAT is driven by multiple ectopic foci (not re-entry), so cardioversion will not terminate it and may cause myocardial injury.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2139}],"confusable_with":"Paroxysmal SVT (cardioversion is appropriate)"},
]

kps.append({"_type":"confusable_pair","topic_a":"Hypomagnesemia","topic_b":"Hypocalcemia",
 "discriminator":"Both cause arrhythmias and neuromuscular irritability; hypomagnesemia often secondarily causes hypokalemia and hypocalcemia; correcting magnesium may normalize calcium and potassium without direct replacement"})

# ============================================================
# [5] End-of-Life Care Ethics
# ============================================================
t = "End-of-Life Care Ethics"
dom = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
disc = "anesthesia"
s = "eol-ethics"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What neurodestructive procedures may be useful in end-of-life palliative care for intractable pain?",
 "answer":"Pituitary adenolysis and cordotomy may be useful in end-of-life palliative care for intractable pain",
 "rationale":"When systemic opioids fail, ablative procedures interrupt pain pathways definitively; irreversibility is acceptable in terminal patients.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":"Neurolytic blocks (temporary destruction with alcohol or phenol)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What agents are used for temporary neurolysis and what is the mechanism of each?",
 "answer":"Ethyl alcohol 50-100% (extracts membrane phospholipids, precipitates lipoproteins) and phenol 6-12% (coagulates proteins) provide temporary nerve fiber destruction",
 "rationale":"Neither agent is selective: both affect visceral, sensory, and motor fibers; alcohol causes pain on injection, phenol is painless initially.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":"Radiofrequency ablation (heat-based, not chemical)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"In critically ill patients near end of life, what problems have been associated with prolonged use of propofol and prolonged neuromuscular blockade?",
 "answer":"Prolonged propofol: 'propofol infusion syndrome' (especially in children); prolonged NMBAs: critical illness myopathy",
 "rationale":"Both complications worsen morbidity; propofol infusion syndrome causes metabolic acidosis, rhabdomyolysis, and cardiac failure; critical illness myopathy causes prolonged weakness.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What improved sedation agent has replaced prolonged propofol and NMBAs in critically ill patients with fewer adverse consequences?",
 "answer":"Dexmedetomidine is more effective for ICU sedation with fewer adverse consequences than prolonged propofol or NMBAs",
 "rationale":"Dexmedetomidine is an alpha-2 agonist providing sedation without respiratory depression, less delirium, and preserved communicability with patients.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":"Midazolam or lorazepam (older sedatives with more delirium risk)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the key consideration in goals-of-care discussions for critically ill septic patients with significant comorbidities?",
 "answer":"Discuss prognosis and which treatments are acceptable vs. not desired; account for chronic comorbidities in addition to acute sepsis; palliative care when sepsis is end-stage manifestation",
 "rationale":"Patients differ in their acceptance of invasive interventions; advance directives and family discussions guide the balance between curative and comfort-focused care.",
 "bloom":"apply","source":[{"book":"Society Guideline","page":50}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why might neurolytic pain relief recur or be complicated by new pain after initial excellent results?",
 "answer":"Original pain may recur OR new deafferentation or central pain may develop in a majority of patients within weeks to months of neurolytic procedures",
 "rationale":"Deafferentation hypersensitivity occurs when sensory input is eliminated; central sensitization can create new neuropathic pain independent of the original source.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What ethical principle applies when a patient with sepsis and poor prognosis desires limitations on invasive interventions?",
 "answer":"Respect autonomy: goals-of-care discussion establishes which interventions are acceptable; advance care planning guides treatment limitations including withholding or withdrawing life-sustaining therapy",
 "rationale":"Autonomy is a foundational bioethical principle; patients with decision-making capacity have the right to refuse any intervention regardless of prognosis.",
 "bloom":"analyze","source":[{"book":"Society Guideline","page":49}],"confusable_with":"Beneficence (doing good) vs. autonomy (patient's own values)"},
]

# ============================================================
# [6] Endocrine Physiology Relevant to Anesthesia
# ============================================================
t = "Endocrine Physiology Relevant to Anesthesia"
dom = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
disc = "anesthesia"
s = "endocrine-physiology"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the differential diagnosis for intraoperative hyperthermia beyond malignant hyperthermia?",
 "answer":"Neuroleptic malignant syndrome (develops over days, antidopaminergic drugs), thyroid storm (hypokalemia, tachycardia, metabolic acidosis, normal EtCO2), serotonin syndrome (MAOIs + meperidine/SSRIs), iatrogenic hyperthermia, CO2 insufflation",
 "rationale":"NMS develops over days not minutes; thyroid storm lacks elevated EtCO2; serotonin syndrome has specific drug trigger; distinguishing guides treatment.",
 "bloom":"analyze","source":[{"book":"Stanford CA-1","page":85}],"confusable_with":"Malignant hyperthermia (elevated EtCO2, muscle rigidity, familial)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the thyroid disorders with implications for anesthetic management?",
 "answer":"Hypothyroidism (bradycardia, weight gain, sensitivity to sedatives), hyperthyroidism (tachycardia, risk of thyroid storm), thyroiditis, and goiter (airway compression)",
 "rationale":"Thyroid hormones regulate metabolic rate, cardiac output, and respiratory drive; perioperative thyroid dysfunction increases risk of cardiovascular complications.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":548}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What CNS targets do common IV anesthetic agents act on?",
 "answer":"GABA-A receptors (propofol, barbiturates increase GABA binding; benzodiazepines increase GABA-receptor efficiency); NMDA receptors (ketamine - uncompetitive antagonist); Alpha-2 receptors (dexmedetomidine - inhibits NE release)",
 "rationale":"Understanding receptor targets predicts drug interactions, reversal strategies, and selection for specific clinical contexts.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":25}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"Dexmedetomidine loading doses can cause what cardiovascular effects, and who is at highest risk?",
 "answer":"Loading doses (0.5-1 mcg/kg over 10 min) increase SVR and MAP from peripheral alpha-2 vasoconstriction, followed by reflex bradycardia; risk factors: older age, baseline MAP <70 mmHg, hypovolemia",
 "rationale":"Peripheral alpha-2 receptor activation causes vasoconstriction; the reflex bradycardia can be severe in susceptible patients requiring dose adjustment.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":146}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the neuroprotective effect of dexmedetomidine in the setting of anesthetic-induced neurotoxicity in children?",
 "answer":"Dexmedetomidine mitigates isoflurane-induced neuroapoptosis and behavioral impairment via cell survival signaling pathways at clinical doses (high doses can themselves induce neuroapoptosis)",
 "rationale":"Dexmedetomidine activates pro-survival kinase pathways (Akt, ERK) that counter anesthetic-induced apoptosis in developing neurons.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":212}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What endocrine concern is unique to etomidate use in septic patients?",
 "answer":"Etomidate inhibits adrenocortical synthesis (11-beta-hydroxylase) causing adrenocortical suppression; single-dose use in septic patients is controversial with ongoing risk-benefit debate",
 "rationale":"Septic patients already have HPA axis dysfunction; etomidate-induced cortisol suppression may worsen stress response and potentially increase mortality risk.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":145}],"confusable_with":"Etomidate in non-septic patients (less clinical significance)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the dantrolene treatment principle for malignant hyperthermia and which other hyperthermia syndromes does it also treat?",
 "answer":"Dantrolene is first-line for MH; it can also treat thyroid storm and NMS (both listed as conditions dantrolene can treat)",
 "rationale":"Dantrolene inhibits ryanodine receptor calcium release in skeletal muscle; hyperthermia in thyroid storm and NMS also involves muscle hypermetabolism that dantrolene can reduce.",
 "bloom":"apply","source":[{"book":"Stanford CA-1","page":85}],"confusable_with":""},
]

# ============================================================
# [7] Endovascular Neurosurgery: Neurointerventional Anesthesia
# ============================================================
t = "Endovascular Neurosurgery: Neurointerventional Anesthesia"
dom = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
disc = "anesthesia"
s = "neurointerventional"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the primary anesthetic goal in patients undergoing endovascular repair of cerebral aneurysms?",
 "answer":"Prevent rupture/rebleeding and avoid factors promoting cerebral ischemia or vasospasm; use intraarterial pressure monitoring; avoid sudden BP increases with intubation or stimulation",
 "rationale":"Aneurysm rupture risk increases with acute hypertension; adequate volume loading allows surgical anesthetic depth without excessive hypotension.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":988}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What vascular pathology presents with high-flow/low-resistance hemodynamics, and how is it treated endovascularly?",
 "answer":"Arteriovenous malformations (AVMs) have high blood flow with low vascular resistance; endovascular embolization with coils, glues, and balloons in the hybrid OR or neurointerventional suite, followed by possible surgical excision",
 "rationale":"AVMs steal blood from normal brain; high flow can rarely cause high-output cardiac failure; endovascular embolization reduces AVM size and vascularity before definitive treatment.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":989}],"confusable_with":"Aneurysm (focal dilation, not arteriovenous shunting)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why are calcium channel blockers, ARBs, and ACE inhibitors used cautiously when treating vasospasm after subarachnoid hemorrhage in the setting of endovascular repair?",
 "answer":"These agents cause systemic vasodilation and reduce systemic vascular resistance, which may compromise cerebral perfusion pressure during vasospasm treatment",
 "rationale":"In vasospasm, the brain depends on elevated MAP to maintain CBF through narrowed vessels; systemic vasodilation lowers CPP and worsens ischemia.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":988}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What monitoring and venous access principles apply to large skull base tumor resections in neuroradiology suites?",
 "answer":"Intraarterial pressure monitoring, large-bore IV catheters for massive hemorrhage risk, precordial Doppler for venous air embolism, visual evoked potentials for optic nerve involvement",
 "rationale":"Skull base tumors can hemorrhage massively and encroach on the optic nerve; monitoring anticipates the specific surgical risks.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":995}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"In interventional neuroradiology, what makes dexmedetomidine particularly useful compared with propofol for prolonged sedation cases?",
 "answer":"Dexmedetomidine is less likely to cause respiratory depression than propofol, making it especially useful for patients with pulmonary hypertension or those requiring frequent mental status assessments",
 "rationale":"In the neuroangio suite, preserved respiratory drive allows spontaneous ventilation and regular neuro checks without interrupting infusion.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":707}],"confusable_with":"Propofol (respiratory depression risk)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"AVM bleeding is most common in what age group and what are the other typical presentations?",
 "answer":"AVM bleeding most common between age 10-30 years; other presentations include headache and seizures; combination of high flow with low resistance can rarely cause high-output cardiac failure",
 "rationale":"AVMs progressively enlarge; their high-flow steal physiology explains the headache and seizure presentations before hemorrhage.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":989}],"confusable_with":"Aneurysm (peak rupture 40-60 years, more sudden onset)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"Awake craniotomy is the norm for what procedures in neuroanesthesia?",
 "answer":"Awake craniotomy is the norm for epilepsy surgery and commonly used for deep brain stimulation procedures",
 "rationale":"Awake patients can provide real-time language, motor, and sensory feedback during cortical mapping, reducing resection of eloquent cortex.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1006}],"confusable_with":""},
]

kps.append({"_type":"illness_script","topic":t,"discipline":disc,
 "enabling_conditions":"Patient with cerebral aneurysm, AVM, or acute ischemic stroke in hybrid OR or angio suite; remote anesthesia location",
 "pathophysiology":"Aneurysm: focal vessel wall weakness; AVM: arteriovenous shunting with high flow; both create risk of hemorrhage from hemodynamic changes",
 "time_course":"Acute: hemorrhage can occur at any moment with hemodynamic instability; procedural time variable (1-6+ hours)",
 "key_features":"Remote location from OR support; radiation exposure; need for hemodynamic precision; anticoagulation during procedure",
 "consequence_if_missed":"Uncontrolled BP spike during aneurysm coiling -> rupture; vasospasm inadequately treated -> cerebral infarction"})

# ============================================================
# [8] Enhanced Recovery After Surgery (ERAS)
# ============================================================
t = "Enhanced Recovery After Surgery (ERAS)"
dom = "Perioperative medicine (preoperative assessment, risk stratification, premedication, ERAS, fluid management, temperature, positioning, post-op care)"
disc = "anesthesia"
s = "eras"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What perioperative care model integrates multimodal analgesia, goal-directed fluid therapy, and early mobilization?",
 "answer":"Enhanced Recovery After Surgery (ERAS) / enhanced recovery programs (ERPs) / fast-track surgery - coordinated multidisciplinary perioperative care programs",
 "rationale":"ERAS bundles evidence-based practices that each individually reduce morbidity; combined implementation produces synergistic reduction in complications and length of stay.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1813}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does ERAS address postoperative ileus through fluid management and analgesia strategies?",
 "answer":"Goal-directed fluid therapy (neither excessive nor overly restricted); opioid-sparing multimodal analgesia shortens or prevents ileus; avoid/minimize nasogastric tubes",
 "rationale":"Excessive and excessively restricted fluid therapy both increase ileus incidence; opioid-sparing regimens reduce ileus duration because opioids suppress GI motility.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1813}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"When does a patient's initial contact with an ERAS program ideally occur?",
 "answer":"Ideally at the time of the preoperative evaluation visit",
 "rationale":"Pre-admission education about ERAS expectations (carbohydrate loading, early mobility, multimodal pain plan) improves patient compliance and outcomes.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the evidence base for the ERAS recommendation against restricting carbohydrate/protein fluid intake more than 2 hours before anesthesia induction in healthy elective patients?",
 "answer":"Strong evidence that nondiabetic patients drinking carbohydrate/protein fluids up to 2 hours before induction experience less perioperative nausea and dehydration than those fasted longer",
 "rationale":"Carbohydrate loading reduces insulin resistance, attenuates catabolic response, and reduces nausea; the 2-hour gastric emptying time for clear fluids is well established.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":"NPO policy for solid food (6-8 hours)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"In ERAS protocols, what are the morphine metabolites that accumulate in renal failure and cause narcosis and ventilatory depression?",
 "answer":"Morphine 3-glucuronide and morphine 6-glucuronide accumulate in kidney failure and are associated with narcosis and ventilatory depression",
 "rationale":"Glucuronide metabolites are renally excreted; in renal failure they accumulate, prolonging and intensifying opioid effects beyond the expected drug duration.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":"Normeperidine (metabolite of meperidine, causes seizures)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What opioid-sparing agents are included in multimodal analgesia as part of ERAS to minimize opioid-related side effects?",
 "answer":"NSAIDs/COX inhibitors, acetaminophen, gabapentinoids (with growing caution about harm), ketamine, alpha-2 agonists, and regional/neuraxial techniques",
 "rationale":"Each agent targets a different part of the pain pathway; combined use achieves better analgesia at lower doses of each, reducing side effects of any single agent.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":299}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What does the perioperative surgical home (PSH) model add to standard ERAS?",
 "answer":"PSH provides coordinated, longitudinal, patient-centered care across the entire perioperative continuum from decision for surgery through recovery - patient's initial contact ideally at the preoperative evaluation",
 "rationale":"The PSH extends ERAS principles from the preoperative period through post-discharge recovery, improving long-term outcomes beyond the hospitalization.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":475}],"confusable_with":"ERAS (procedure-specific, inpatient-focused)"},
]

print(f"KPs so far: {len(kps)}")

# Save checkpoint
with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 1 saved OK")
