"""
Generate KP redeepen part 7 — items[231:264] from _kp_redeepen.json
Each topic gets 6-9 atomic KPs grounded strictly in its own chunks.
"""
import json, os, sys

os.chdir("C:/Users/Dean/anesthesia_attending")
sys.stdout.reconfigure(encoding="utf-8")

with open("data/_kp_redeepen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data[231:264]

kps = []

# ─────────────────────────────────────────────────────────────────────────────
# 231 Healthcare-Associated Harm & Preventable Adverse Events
# ─────────────────────────────────────────────────────────────────────────────
T = "Healthcare-Associated Harm & Preventable Adverse Events"
D = "Patient safety, ethics, professionalism & quality"
DI = "anesthesia"

kps += [
  {"id":"healthcare-harm-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"In the ASA Closed Claims Project (1990s), what were the three most frequent claim categories by proportion?",
   "answer":"Death 22%, nerve injury 18%, brain damage 9%",
   "rationale":"These categories drove closed-claims reforms that shaped modern monitoring and documentation standards.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2015}],"confusable_with":""},

  {"id":"healthcare-harm-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"What proportion of anesthesia-related malpractice claims in a 2009 NHS analysis involved regional versus obstetrical cases?",
   "answer":"Regional anesthesia 44%, obstetrical anesthesia 29% of anesthesia claims",
   "rationale":"Neuraxial proximity and obstetric urgency concentrate liability risk in these two domains.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2015}],"confusable_with":""},

  {"id":"healthcare-harm-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"Preventable anesthetic accidents are predominantly caused by which category of failure?",
   "answer":"Human error (majority), not equipment malfunction",
   "rationale":"Improved equipment standards have shifted preventable harm toward cognitive, systems, and communication failures.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2015}],"confusable_with":"equipment malfunction"},

  {"id":"healthcare-harm-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"What does the Patient Safety Authority in Pennsylvania collect, and why is this data useful for anesthesia safety research?",
   "answer":"Mandatory reports of incidents of harm or near-harm (e.g., surgical fires data), enabling extrapolation of incidence rates",
   "rationale":"Mandatory reporting systems create population-level denominators unavailable from voluntary near-miss databases.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":64}],"confusable_with":""},

  {"id":"healthcare-harm-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"What patient safety principle is captured by the phrase that safety focuses on avoiding adverse events rather than on eliminating all error?",
   "answer":"Safety is defined by outcome (absence of harm), not by zero error rate; defences must prevent errors from reaching patients",
   "rationale":"High-reliability organisations accept a background error rate while building layered barriers to prevent patient harm.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":853}],"confusable_with":""},

  {"id":"healthcare-harm-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the current consensus regarding cognitive developmental harm from a single brief anesthetic exposure in infants?",
   "answer":"Single, brief anesthetic exposures in infants and young children are very unlikely to result in harm",
   "rationale":"Clinical studies have not demonstrated developmental deficits from single exposures; concern persists for repeated or prolonged exposures.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":252}],"confusable_with":""},

  {"id":"healthcare-harm-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"Which agent has been proposed as potentially neuroprotective against volatile anesthetic-induced neurotoxicity in children?",
   "answer":"Dexmedetomidine (alpha-2 agonist with proposed anti-apoptotic properties)",
   "rationale":"Dexmedetomidine may attenuate excitotoxic and apoptotic pathways activated by volatile anesthetics during critical neurodevelopmental windows.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":252}],"confusable_with":"xenon"},

  {"id":"healthcare-harm-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"Volatile anesthetics have been linked to promotion of which Alzheimer-associated protein modification?",
   "answer":"Tau protein hyperphosphorylation",
   "rationale":"Hyperphosphorylated tau aggregates into neurofibrillary tangles; anesthetic-induced hyperphosphorylation raises concern about long-term neurodegeneration risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":252}],"confusable_with":"amyloid-beta"},
]

# ─────────────────────────────────────────────────────────────────────────────
# 232 Heart Failure – Pathophysiology & Perioperative Optimization
# ─────────────────────────────────────────────────────────────────────────────
T = "Heart Failure — Pathophysiology & Perioperative Optimization"
D = "Cardiovascular anesthesia & critical care"

kps += [
  {"id":"hf-pathophys-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"Beyond symptoms and signs, what two objective findings corroborate a diagnosis of heart failure per current definitions?",
   "answer":"Elevated natriuretic peptide levels OR evidence of pulmonary/systemic congestion (imaging or haemodynamic measurement)",
   "rationale":"Objective corroboration distinguishes cardiac from non-cardiac dyspnoea and avoids over-diagnosis.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":493}],"confusable_with":""},

  {"id":"hf-pathophys-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"List four consequences of intraoperative volume overload that increase perioperative morbidity in heart failure patients.",
   "answer":"Increased mortality/ICU stay; myocardial morbidity; pulmonary, periorbital, and gut edema; worsened wound healing and decreased albumin",
   "rationale":"Liberal fluid strategies harm the failing heart by raising preload beyond the plateau of the Frank-Starling curve.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":48}],"confusable_with":""},

  {"id":"hf-pathophys-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"What compensatory mechanism acutely maintains stroke volume when LV contractility falls, and what is the long-term consequence?",
   "answer":"Ventricular dilation (Frank-Starling); over time maladaptive remodelling leads to further contractile failure",
   "rationale":"Salt/water retention and sympathetic activation drive initial dilatation, but sustained wall stress causes irreversible myocyte loss.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":660}],"confusable_with":""},

  {"id":"hf-pathophys-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"Asymptomatic troponin elevation found after non-cardiac surgery should trigger what clinical response and carries what prognostic label?",
   "answer":"Myocardial Injury after Non-cardiac Surgery (MINS) — increased mortality risk requiring monitoring and risk factor optimisation",
   "rationale":"MINS can occur without classic MI symptoms due to supply-demand mismatch or plaque rupture, and carries excess 30-day mortality.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":624}],"confusable_with":"type 1 STEMI"},

  {"id":"hf-pathophys-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"HFmrEF is defined by what ejection fraction range, and what first-line treatment addresses congestion?",
   "answer":"EF 40–49%; diuretics (and consider guideline-directed neurohormonal therapy)",
   "rationale":"Mid-range EF HF is a heterogeneous phenotype that may represent recovering HFrEF or developing HFpEF; diuretics treat the dominant congestive symptom.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":27}],"confusable_with":"HFpEF (EF ≥50%)"},

  {"id":"hf-pathophys-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"A patient with HF and documented hypervolemia is admitted; what fluid management principle should guide care?",
   "answer":"Diuresis to achieve euvolemia (hold IVF); stop NSAIDs; optimize hemodynamics; avoid nephrotoxins",
   "rationale":"Euvolemia optimises renal perfusion pressure; IV fluids in a hypervolemic HF patient worsen pulmonary oedema and renal venous congestion.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":100}],"confusable_with":""},

  {"id":"hf-pathophys-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"Why is myocardial relaxation described as a dynamic, active process rather than passive recoil?",
   "answer":"It requires ATP-dependent calcium reuptake via SERCA2a and active cross-bridge detachment; impairment causes diastolic dysfunction",
   "rationale":"Diastolic heart failure with preserved EF results from impaired active relaxation and increased chamber stiffness, not systolic weakness.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":660}],"confusable_with":""},

  {"id":"hf-pathophys-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"Which five cardiovascular disease categories most frequently drive major perioperative anesthetic risk?",
   "answer":"Hypertensive, ischemic, congenital, and valvular heart disease, with heart failure as a common final pathway",
   "rationale":"All share reduced cardiac reserve and haemodynamic instability, demanding targeted preoperative assessment and optimisation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":617}],"confusable_with":""},
]

# ─────────────────────────────────────────────────────────────────────────────
# 233 Heart failure – preoperative assessment and optimization
# ─────────────────────────────────────────────────────────────────────────────
T = "Heart failure — preoperative assessment and optimization"
D = "Cardiovascular anesthesia & critical care"

kps += [
  {"id":"hf-preop-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"What stepwise ACC/AHA algorithm guides perioperative cardiac assessment for patients with known or suspected CAD?",
   "answer":"Step 1: assess urgency; Step 2: known ASCVD or risk? Step 3: functional capacity (METs); Step 4: elevated-risk surgery + poor METs → non-invasive testing if will change management",
   "rationale":"This stepwise approach prevents unnecessary testing while identifying patients who benefit from pre-surgical optimisation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":622}],"confusable_with":""},

  {"id":"hf-preop-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"Why does nitrate therapy benefit patients with ischaemic HF in the perioperative period beyond simple vasodilation?",
   "answer":"Nitrates dilate coronary arteries; even minor dilation at stenotic sites can substantially increase blood flow because flow is proportional to the fourth power of radius",
   "rationale":"Poiseuille’s law: a small increase in vessel radius produces a large increase in laminar flow, making nitrates disproportionately effective at stenotic lesions.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":640}],"confusable_with":""},

  {"id":"hf-preop-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"For a patient with known HF and significant OSA who is non-compliant with PAP therapy, what preoperative intervention should be prioritised?",
   "answer":"Counsel to resume PAP therapy preoperatively; consider elevated serum bicarbonate as a marker of chronic hypoventilation",
   "rationale":"OSA-related nocturnal hypoxia worsens pulmonary hypertension and right HF; PAP compliance reduces perioperative cardiopulmonary risk.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":890}],"confusable_with":""},

  {"id":"hf-preop-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"HF is a clinical syndrome requiring symptoms or signs plus corroboration. Name the two accepted corroborating objective criteria.",
   "answer":"Elevated natriuretic peptides OR objective evidence of cardiac structural/functional abnormality causing pulmonary/systemic congestion",
   "rationale":"Requiring objective corroboration avoids misclassification of non-cardiac dyspnoea as HF.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":493}],"confusable_with":""},

  {"id":"hf-preop-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"Post-operative troponin surveillance studies have found what unexpected finding in patients without ischaemic symptoms?",
   "answer":"A surprising number of asymptomatic patients have elevated troponin after surgery — indicative of myocardial injury",
   "rationale":"Silent MINS is common and carries excess mortality, motivating routine troponin surveillance in high-risk non-cardiac surgical patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":624}],"confusable_with":""},

  {"id":"hf-preop-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"For which specific surgical populations is preoperative exercise/rehabilitation prehabilitation most evidence-based for reducing complications?",
   "answer":"Colorectal, esophageal, prostate, and some orthopedic surgeries",
   "rationale":"These high-risk procedures have the strongest trial data supporting prehabilitation to improve functional capacity and reduce morbidity.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":785}],"confusable_with":""},

  {"id":"hf-preop-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the management principle for intraoperative fluid balance when a patient has known HF?",
   "answer":"Goal-directed, euvolemic approach: avoid both volume overload and hypovolemia; guide with haemodynamic monitoring",
   "rationale":"HF patients occupy a narrow haemodynamic window; excess volume raises filling pressures while hypovolaemia reduces cardiac output.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":48}],"confusable_with":""},

  {"id":"hf-preop-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"Why is a focused perioperative history and physical examination described as the foundation of preoperative cardiac evaluation rather than routine testing?",
   "answer":"It identifies functional status, symptom severity, and specific risk factors that direct targeted (not blanket) additional testing",
   "rationale":"Indiscriminate pre-operative testing adds cost and delay without improving outcomes; clinical assessment stratifies who needs further evaluation.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":779}],"confusable_with":""},
]


# ─────────────────────────────────────────────────────────────────────────────
# 234 Heat and Temperature Physiology and Physics
# ─────────────────────────────────────────────────────────────────────────────
T = "Heat and Temperature Physiology and Physics"
D = "Physiology & physics relevant to anesthesia practice"

kps += [
  {"id":"heat-temp-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"By approximately what fraction does metabolic oxygen requirement change with each 10 degree reduction in body temperature during CPB?",
   "answer":"Reduced by approximately 50% (halved) per 10 degree C drop",
   "rationale":"This Q10 effect underlies profound hypothermia at 15-18 C to allow circulatory arrest for complex cardiac repairs.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":714}],"confusable_with":""},

  {"id":"heat-temp-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"To what target temperatures is profound hypothermia induced for circulatory arrest during complex cardiac surgery?",
   "answer":"15 to 18 degrees C",
   "rationale":"Temperatures this low suppress cerebral and myocardial metabolism to safe levels during circulatory arrest.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":714}],"confusable_with":"moderate hypothermia (28-32 C)"},

  {"id":"heat-temp-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the most important cause of intraoperative hypothermia and when does it predominate?",
   "answer":"Redistribution of heat from body core to peripheral compartments — predominates in the first 30 minutes after induction",
   "rationale":"Anesthetic vasodilation rapidly transfers core heat to cool peripheral tissues, producing the initial steep temperature drop.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2105}],"confusable_with":"heat loss to environment"},

  {"id":"heat-temp-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"What single intervention most effectively reduces heat redistribution loss in the first 30 minutes after induction?",
   "answer":"Preoperative forced-air warming of torso and legs for 30 minutes before induction",
   "rationale":"Pre-warming equilibrates core and peripheral compartment temperatures, minimising the gradient that drives redistribution after vasodilation.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":65}],"confusable_with":"intraoperative warming blankets alone"},

  {"id":"heat-temp-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"Postoperative shivering in the PACU has two distinct causes beyond ambient cold — what are they?",
   "answer":"Intraoperative hypothermia and pharmacological effects of anesthetic agents (each can independently trigger shivering)",
   "rationale":"Thermoregulatory shivering corrects core hypothermia; anesthetic agents can trigger non-thermoregulatory shivering via central mechanisms.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2105}],"confusable_with":"transfusion rigors"},

  {"id":"heat-temp-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"During cardiac surgery, what temperature range is achieved when surgeons allow passive 'drift' rather than active cooling?",
   "answer":"30 to 35 degrees C (mild to moderate hypothermia by passive drift)",
   "rationale":"Mild drift hypothermia provides metabolic protection without the haemodynamic and coagulation complications of deeper cooling.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":714}],"confusable_with":""},

  {"id":"heat-temp-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"Neuroleptic malignant syndrome (NMS) versus malignant hyperthermia: what clinical features distinguish them by onset timing and trigger?",
   "answer":"NMS develops over days (antidopaminergic agents or dopamine withdrawal); MH develops over minutes to hours (volatile agents or succinylcholine)",
   "rationale":"NMS is a dopamine-deficiency syndrome; MH is a hypermetabolic skeletal muscle calcium-release disorder — different mechanisms, different timelines.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":85}],"confusable_with":"malignant hyperthermia"},

  {"id":"heat-temp-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"In neonates, what property of the chest wall and cartilaginous ribs affects thermoregulation indirectly through work of breathing?",
   "answer":"Very compliant cartilaginous rib cage increases airway resistance and work of breathing, increasing metabolic heat production",
   "rationale":"Neonates have high metabolic rates and limited insulation; increased work of breathing adds metabolic heat load that must be balanced against large surface-area heat loss.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1442}],"confusable_with":""},
]

# ─────────────────────────────────────────────────────────────────────────────
# 235 Hemodynamic Monitoring – Invasive & Advanced
# ─────────────────────────────────────────────────────────────────────────────
T = "Hemodynamic Monitoring — Invasive & Advanced"
D = "Monitoring, equipment & patient safety"

kps += [
  {"id":"hemo-monitor-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"A pulmonary artery catheter is 110 cm long; what is a critical practical limitation when it is placed through an introducer sheath?",
   "answer":"Catheter placement into the sheath significantly reduces fluid flow rate through the sheath",
   "rationale":"The PAC occupies most of the sheath lumen; a second large-bore access is needed for rapid fluid resuscitation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":397}],"confusable_with":""},

  {"id":"hemo-monitor-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"Thermodilution CO measurement: what injectate volume and temperature are standard, and what are normal CO and CI values?",
   "answer":"10 mL normal saline at 0 degrees C into RA; normal CO 4-6 L/min, CI 2.5-4 L/min per m2",
   "rationale":"CO is calculated from the Stewart-Hamilton equation: inversely proportional to the area under the temperature-time curve.",
   "bloom":"recall","source":[{"book":"Curated Units","page":0}],"confusable_with":""},

  {"id":"hemo-monitor-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"Thoracic electrical bioimpedance provides which haemodynamic estimates, and what factors degrade its accuracy?",
   "answer":"Estimates SV, CO, SVR, fluid status; accuracy degraded by obesity, arrhythmias, edema, and patient positioning",
   "rationale":"Altered thoracic impedance from fluid, fat, or electrical noise distorts the impedance-flow relationship.",
   "bloom":"apply","source":[{"book":"Curated Units","page":0}],"confusable_with":"bioreactance (NICOM)"},

  {"id":"hemo-monitor-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"Doppler-based CO monitoring relies on what physical principle to derive blood velocity?",
   "answer":"Doppler frequency shift of reflected ultrasound proportional to red blood cell velocity; velocity times cross-sectional area gives flow",
   "rationale":"Oesophageal Doppler or transoesophageal echo exploits this principle to provide continuous, less invasive CO monitoring.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":398}],"confusable_with":""},

  {"id":"hemo-monitor-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"In a cardiac transplant recipient, why are indirect sympathomimetics ineffective for treating bradycardia?",
   "answer":"Cardiac denervation removes autonomic reflex arcs; only direct-acting agents (isoproterenol) or pacing are effective",
   "rationale":"Indirect agents such as ephedrine require intact neuronal catecholamine release; the denervated heart lacks this pathway.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":691}],"confusable_with":""},

  {"id":"hemo-monitor-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"What intraoperative MAP threshold or percent decrease is associated with end-organ injury in prospective observational data?",
   "answer":"MAP below 50 mm Hg OR a 40% decrease from baseline",
   "rationale":"These thresholds approximate the lower limit of cerebral and renal autoregulation, below which perfusion pressure dependence emerges.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":390}],"confusable_with":""},

  {"id":"hemo-monitor-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"How does acute aortic regurgitation differ haemodynamically from chronic AR at presentation?",
   "answer":"Acute AR: sudden pulmonary edema and hypotension (LV unprepared); chronic AR: gradual CHF with compensatory LV dilatation",
   "rationale":"Absence of eccentric hypertrophy in acute AR means the regurgitant volume overloads a stiff, undilated ventricle producing immediate pulmonary oedema.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":677}],"confusable_with":"acute mitral regurgitation"},

  {"id":"hemo-monitor-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"Arterial pressure monitoring is listed as a monitoring adjunct for which specific intraoperative scenarios in standard guidelines?",
   "answer":"Significant aortic regurgitation, blood pressure manipulation in interventional neuroradiology, and other high-risk haemodynamic cases requiring continuous beat-to-beat monitoring",
   "rationale":"Arterial lines detect rapid haemodynamic changes and allow arterial blood gas sampling in conditions where oscillometric NIBP would be too slow or inaccurate.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":490}],"confusable_with":""},
]

# ─────────────────────────────────────────────────────────────────────────────
# 236 Heparin-Induced Thrombocytopenia (HIT) & Cardiac Surgery
# ─────────────────────────────────────────────────────────────────────────────
T = "Heparin-Induced Thrombocytopenia (HIT) & Cardiac Surgery"
D = "Cardiovascular anesthesia & critical care"

kps += [
  {"id":"hit-cardiac-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"What antibody mediates heparin-induced thrombocytopenia and what platelet protein is the target antigen?",
   "answer":"Heparin-dependent IgG antibodies targeting the heparin-platelet factor 4 (PF4) complex, which agglutinate and activate platelets",
   "rationale":"PF4 released from activated platelets binds heparin; this complex is highly immunogenic, generating IgG that cross-links FcgRIIa receptors and causes platelet activation and thrombocytopenia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":"thrombotic thrombocytopenic purpura"},

  {"id":"hit-cardiac-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"For a patient with a history of HIT who requires cardiac surgery, what alternative anticoagulation strategies are used?",
   "answer":"Use of alternative anticoagulants (e.g., bivalirudin or argatroban); preoperative pheresis of platelet-rich plasma at some centres",
   "rationale":"HIT antibodies can persist; re-exposure to heparin risks life-threatening thrombosis, mandating non-heparin anticoagulation strategies.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":""},

  {"id":"hit-cardiac-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the purpose of intraoperative platelet-rich plasma collection by pheresis prior to CPB in some centres?",
   "answer":"To collect and preserve autologous platelets before heparin/CPB exposure, then reinfuse after bypass to decrease bleeding and reduce transfusion requirements",
   "rationale":"CPB activates and destroys platelets; autologous platelet reinfusion post-bypass improves platelet count and function.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":""},

  {"id":"hit-cardiac-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"With a 4T score of 4-5 (intermediate probability) for HIT and no active thrombosis and high bleeding risk, what anticoagulation decision is appropriate?",
   "answer":"Prophylactic dose of an alternative anticoagulant (non-heparin) may be initiated; therapeutic anticoagulation is not mandatory if no active thrombosis",
   "rationale":"Intermediate 4T probability warrants avoiding heparin products but balances thrombosis prevention against bleeding risk.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Heparin induced thrombocytopenia (HIT)","page":5}],"confusable_with":""},

  {"id":"hit-cardiac-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"Low-dose subcutaneous heparin prophylaxis: is it a contraindication to neuraxial anesthesia, and when should neuraxial procedures occur relative to dosing?",
   "answer":"NOT a contraindication; neuraxial anesthesia should occur 4-6 hours after the SC heparin dose",
   "rationale":"ASRA guidelines permit neuraxial blocks with prophylactic SC heparin if a sufficient time interval elapses and platelet count is checked to exclude HIT.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1563}],"confusable_with":"therapeutic heparin"},

  {"id":"hit-cardiac-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"A patient presenting with HIT has a platelet count below 50,000 and an active bleed; what is the risk threshold for spontaneous bleeding?",
   "answer":"Platelet count below 10,000 is associated with spontaneous bleeding risk; below 50,000 with surgery or active bleed; below 30,000 with mild trauma",
   "rationale":"These thresholds guide transfusion triggers and procedural timing in thrombocytopenia management.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":139}],"confusable_with":""},

  {"id":"hit-cardiac-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"Which heparin formulation carries the highest risk of triggering HIT, and why?",
   "answer":"Unfractionated heparin (UFH) has higher HIT risk than low-molecular-weight heparin (LMWH) because it has greater PF4-binding avidity",
   "rationale":"Longer UFH chains bind multiple PF4 molecules forming more immunogenic complexes than short LMWH chains.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2269}],"confusable_with":"fondaparinux (very low HIT risk)"},

  {"id":"hit-cardiac-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"The comprehensive preoperative haemostasis assessment should include what multidisciplinary team to optimise antithrombotic management?",
   "answer":"Patient, primary care physician, hematologist, surgeon, and anesthesia provider",
   "rationale":"Antithrombotic and bridging decisions require integration of thrombotic risk (from hematology) with surgical bleeding risk (from surgery and anesthesia).",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":459}],"confusable_with":""},
]

# ─────────────────────────────────────────────────────────────────────────────
# 237 Hepatic disease and cirrhosis risk assessment
# ─────────────────────────────────────────────────────────────────────────────
T = "Hepatic disease and cirrhosis risk assessment"
D = "Hepatic & GI anesthesia"

kps += [
  {"id":"hepatic-cirrhosis-d1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the annual incidence of hepatocellular carcinoma (HCC) in cirrhotic patients, and what are two first-level preventive interventions?",
   "answer":"2-4% risk per year; HBV vaccination and antiviral therapy are primary prevention strategies",
   "rationale":"Cirrhosis is the dominant HCC risk factor; viral hepatitis eradication and surveillance reduce progression to malignancy.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":96}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d2","topic":T,"domain":D,"discipline":DI,
   "stem":"Hepatic encephalopathy in cirrhosis is classified as Type C; what are its three sub-categories?",
   "answer":"Episodic, persistent, and minimal hepatic encephalopathy",
   "rationale":"Minimal HE lacks overt neurological signs but is detected on psychometric testing and carries prognostic significance for progression to overt HE.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Hepatic Encephalopathy","page":14}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d3","topic":T,"domain":D,"discipline":DI,
   "stem":"What mechanism explains why opioids increase the risk of choledochoduodenal sphincter spasm, and how is spasm treated?",
   "answer":"Opioids contract the sphincter of Oddi via mu-receptor stimulation; spasm is treated with naloxone or glucagon",
   "rationale":"Not all patients respond with clinically significant spasm; inter-individual variability limits routine avoidance of opioids in biliary patients.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":537}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d4","topic":T,"domain":D,"discipline":DI,
   "stem":"In cirrhosis-associated ascites, what is the first-line medical treatment, and what electrolyte abnormality warrants special monitoring?",
   "answer":"Aldosterone antagonist (spironolactone) or sodium restriction; hypokalemia is common and increases arrhythmia risk",
   "rationale":"Hyperaldosteronism drives ascites formation; spironolactone blocks aldosterone-mediated sodium retention but can cause hyperkalemia or fail to prevent hypokalemia in combined diuretic regimens.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":550}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d5","topic":T,"domain":D,"discipline":DI,
   "stem":"Splanchnic nerve stimulation (pain, hypoxia, sympathetic activation) reduces hepatic blood flow — by what mechanism?",
   "answer":"Sympathetic innervation of splanchnic vessels causes vasoconstriction, reducing portal and hepatic arterial flow",
   "rationale":"This reflex underlies anesthesia-associated hepatic perfusion reduction during surgical stimulation and highlights the importance of depth adequacy.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":530}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d6","topic":T,"domain":D,"discipline":DI,
   "stem":"HAS-BLED scoring is used for bleeding risk with anticoagulation; which two organ-dysfunction components contribute to the score?",
   "answer":"Abnormal renal function (CrCl below 50) and liver disease — each contributing 1 point to the HAS-BLED score",
   "rationale":"Both renal and hepatic dysfunction impair drug metabolism and haemostasis, compounding anticoagulation bleeding risk.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":14}],"confusable_with":"CHA2DS2-VASc"},

  {"id":"hepatic-cirrhosis-d7","topic":T,"domain":D,"discipline":DI,
   "stem":"Laparoscopic surgery near the liver can reduce hepatic blood flow by what approximate fraction?",
   "answer":"Up to 60% reduction in hepatic blood flow during laparoscopic/robotic surgery (especially steep Trendelenburg)",
   "rationale":"Pneumoperitoneum increases intraabdominal pressure, compressing portal venous flow, while the Trendelenburg position shifts blood centrally and further impairs hepatic perfusion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1173}],"confusable_with":""},

  {"id":"hepatic-cirrhosis-d8","topic":T,"domain":D,"discipline":DI,
   "stem":"Intermediate-duration NMB drugs metabolised by the liver may have prolonged duration in liver transplant recipients; when does liver function recovery become apparent?",
   "answer":"Evidence of liver function (including drug metabolism) typically appears after reperfusion of the new graft",
   "rationale":"The anhepatic phase abolishes hepatic drug metabolism; post-reperfusion recovery is variable but usually begins within minutes of graft reperfusion.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":689}],"confusable_with":""},
]

print(f"Generated {len(kps)} KPs through item 237")

