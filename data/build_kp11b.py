import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── 5: Supraclavicular brachial plexus block ─────────────────────────────────
T = "Supraclavicular brachial plexus block"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
DI = "anesthesia"
kps += [
  {"id":"supraclav-bp-1","topic":T,"domain":D,"discipline":DI,
   "stem":"The supraclavicular block was historically called the 'spinal of the arm' because of what two properties?",
   "answer":"Relatively rapid onset and reliability, providing dense anesthesia of the brachial plexus for procedures at or distal to the elbow.",
   "rationale":"At the supraclavicular level all trunks/divisions of the brachial plexus are clustered tightly, allowing a single injection to achieve complete arm block.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1626}],"confusable_with":"Interscalene block (shoulder/proximal humerus only)"},
  {"id":"supraclav-bp-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What volume range is typically used for supraclavicular block for surgical anesthesia versus postoperative analgesia?",
   "answer":"20-30 mL for surgical anesthesia; 10 mL for postoperative analgesia.",
   "rationale":"Larger volumes ensure spread to all divisions; smaller volumes target specific nerves for analgesia while reducing side-effect risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1626}],"confusable_with":""},
  {"id":"supraclav-bp-3","topic":T,"domain":D,"discipline":DI,
   "stem":"As local anesthetic volume increases for the supraclavicular block, what dose-dependent side effect becomes more likely?",
   "answer":"Incidental phrenic nerve block (hemidiaphragmatic paresis).",
   "rationale":"The phrenic nerve (C3-C5) passes near the brachial plexus at the supraclavicular level; larger volumes spread cephalad and increase phrenic nerve involvement.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1626}],"confusable_with":"Horner syndrome (from interscalene block)"},
  {"id":"supraclav-bp-4","topic":T,"domain":D,"discipline":DI,
   "stem":"For shoulder procedures, which brachial plexus block level is ideally suited: interscalene, supraclavicular, or axillary?",
   "answer":"Interscalene block is ideally suited for shoulder procedures.",
   "rationale":"The interscalene approach targets the C5-C6 roots at the shoulder level; supraclavicular and axillary blocks are better for procedures distal to the mid-humerus.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1621}],"confusable_with":"Supraclavicular block"},
  {"id":"supraclav-bp-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the absolute contraindications to an interscalene brachial plexus block?",
   "answer":"Local infection, severe coagulopathy, local anesthetic allergy, and patient refusal.",
   "rationale":"These contraindications apply to all regional techniques; the interscalene approach additionally risks phrenic nerve block, so contralateral phrenic or diaphragmatic palsy is a relative contraindication.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1623}],"confusable_with":""}
]

# ── 6: Supraglottic Airway Devices ───────────────────────────────────────────
T = "Supraglottic Airway Devices"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"sad-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the two primary clinical roles of supraglottic airway devices (SADs) in anesthesia?",
   "answer":"Routine airway management (when intubation is not necessary) and airway rescue when both BMV and endotracheal intubation have failed.",
   "rationale":"SADs sit above the glottis and seal around the laryngeal inlet, providing a conduit for ventilation without tracheal intubation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":508}],"confusable_with":""},
  {"id":"sad-2","topic":T,"domain":D,"discipline":DI,
   "stem":"SADs can also be used as a conduit to aid endotracheal intubation in what scenario?",
   "answer":"When both bag-mask ventilation and direct/video laryngoscopy intubation have failed (failed airway rescue conduit).",
   "rationale":"Fiber-optic or intubating laryngeal mask airways allow passage of an endotracheal tube through the SAD while maintaining oxygenation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":508}],"confusable_with":""},
  {"id":"sad-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Why should the airway be secured with an ETT (rather than leaving an LMA) as soon as feasible during CPR?",
   "answer":"Gastric inflation with subsequent regurgitation and aspiration is possible with positive-pressure mask or SAD ventilation during compressions.",
   "rationale":"During CPR, the lower esophageal sphincter is not reliably protected by a supraglottic device; ETT provides a definitive seal against aspiration.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2060}],"confusable_with":""},
  {"id":"sad-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Prolonged mask ventilation risks injury to branches of which two cranial nerves?",
   "answer":"Trigeminal nerve (CN V) and facial nerve (CN VII) branches, from pressure injury.",
   "rationale":"Sustained mask pressure over bony prominences compresses superficial branches of the trigeminal and facial nerves, causing neuropraxia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":507}],"confusable_with":""},
  {"id":"sad-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What standard equipment items should be routinely available for airway management in addition to a bag-mask and ETTs?",
   "answer":"Oxygen source, laryngoscopes (direct and video), ETTs of different sizes with stylets, exhaled CO2 detector, and equipment for surgical airway.",
   "rationale":"Preparedness for escalating airway difficulty requires having backup devices immediately available; failure to prepare is the most common equipment-related adverse outcome.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":502}],"confusable_with":""}
]

# ── 7: Surgical airway: cricothyrotomy and tracheotomy ───────────────────────
T = "Surgical airway: cricothyrotomy and tracheotomy"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"surg-airway-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Front-of-neck airway (FONA) is required in which clinical scenario?",
   "answer":"Cannot-intubate, cannot-oxygenate (CICO) scenario; or in anticipation of it in selected patients with predicted airway failure.",
   "rationale":"FONA bypasses the upper airway entirely; it is the last resort when all other methods of oxygenation have failed or are predicted to fail.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":539}],"confusable_with":"Tracheostomy (elective, not emergency)"},
  {"id":"surg-airway-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the FONA options when the cannot-intubate, cannot-oxygenate situation arises?",
   "answer":"Surgical tracheostomy, cricothyrotomy, catheter/needle cricothyrotomy, and transtracheal jet ventilation.",
   "rationale":"Each technique varies in speed, equipment requirements, and reliability; scalpel-based techniques are most reliable under emergency conditions.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":539}],"confusable_with":""},
  {"id":"surg-airway-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Why must preparation for a surgical airway be established before every anesthetic induction?",
   "answer":"Laryngospasm can make positive-pressure mask ventilation impossible even in a non-paralyzed awake patient; succinylcholine failure then leads to CICO.",
   "rationale":"Laryngospasm at any depth of anesthesia can close the glottis completely; if succinylcholine is unavailable or fails, surgical airway is the only rescue.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":553}],"confusable_with":""},
  {"id":"surg-airway-4","topic":T,"domain":D,"discipline":DI,
   "stem":"An airway exchange catheter (e.g., Cook AEC with Rapi-Fit Adapter) serves what dual function in the postextubation period?",
   "answer":"Facilitates reintubation as a guide and provides oxygenation (jet ventilation) in the setting of immediate postextubation respiratory obstruction.",
   "rationale":"The hollow catheter allows jet ventilation while maintaining tracheal access until definitive reintubation or recovery is achieved.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1286}],"confusable_with":""},
  {"id":"surg-airway-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What equipment items specifically fulfill requirements for an emergency surgical airway at the anesthesia workstation?",
   "answer":"Transtracheal jet ventilator, hollow jet ventilation stylet, Combitube, and cricothyrotomy kit.",
   "rationale":"These devices provide the options of oxygenation and ventilation bypassing the upper airway when standard intubation has failed.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":554}],"confusable_with":""}
]

# ── 8: Surgical anatomy relevant to thoracic anesthesia ──────────────────────
T = "Surgical anatomy relevant to thoracic anesthesia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"thorac-anat-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the typical distance from the carina to the orifice of the right upper lobe bronchus, and why does this matter for double-lumen tube placement?",
   "answer":"Approximately 1-2.5 cm; the very short distance means a right-sided DLT must be carefully positioned to avoid occluding the RUL bronchus.",
   "rationale":"The short carina-to-RUL distance makes right-sided DLTs more technically demanding and more prone to RUL obstruction than left-sided tubes.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":896}],"confusable_with":"Left main bronchus (bifurcation ~5 cm from carina)"},
  {"id":"thorac-anat-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the anatomical definition of the thoracic paravertebral space that makes it a target for regional analgesia?",
   "answer":"Defined posteriorly by the superior costotransverse ligament; contains intercostal nerves and communicates with adjacent paravertebral spaces.",
   "rationale":"Local anesthetic injected here spreads along multiple dermatomes, providing ipsilateral somatic and sympathetic block equivalent to thoracic epidural without bilateral effects.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1610}],"confusable_with":"Intercostal nerve block (single dermatome)"},
  {"id":"thorac-anat-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Intercostal nerve blocks produce the highest blood levels of local anesthetic per unit dose of which nerve block procedure, and what does this mean clinically?",
   "answer":"Highest systemic absorption; when multiple intercostal blocks are planned, total dose must be carefully limited to avoid local anesthetic systemic toxicity.",
   "rationale":"Intercostal space has rich vascularity; absorption is faster and more complete than any other nerve block site, requiring lower total dose limits.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1610}],"confusable_with":"IV regional anesthesia (Bier block)"},
  {"id":"thorac-anat-4","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the principal advantage of fascial plane blocks (e.g., serratus, ESP) over conventional nerve blocks for thoracic analgesia?",
   "answer":"A single injection can anesthetize multiple nerves or dermatomes that would require multiple individual injections with conventional techniques.",
   "rationale":"Fascial planes are anatomical compartments through which local anesthetic spreads widely, covering multiple segmental nerves from one injection point.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1620}],"confusable_with":""},
  {"id":"thorac-anat-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In thoracic surgery, where should the TEE probe be positioned to obtain temperature measurements closest to core temperature?",
   "answer":"Behind the heart in the lower third of the esophagus, avoiding measurement of tracheal gas temperature.",
   "rationale":"This esophageal position reflects cardiac (core) temperature; the upper esophagus is influenced by tracheal gas temperature, which can be misleadingly low.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":177}],"confusable_with":"Nasopharyngeal temperature probe position"}
]

# ── 9: Temperature Monitoring ─────────────────────────────────────────────────
T = "Temperature Monitoring"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"temp-monitor-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the most effective single intervention to reduce intraoperative heat loss due to redistribution from core to periphery in the first 30 minutes after induction?",
   "answer":"Preoperative forced air warming to torso and legs for 30 minutes before induction.",
   "rationale":"Redistribution hypothermia occurs because induction causes vasodilation redistributing core heat to periphery; pre-warming the periphery reduces this gradient.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":65}],"confusable_with":"Intraoperative forced air warming (less effective for first 30 min)"},
  {"id":"temp-monitor-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Hypothermia reduces metabolic rate by approximately what percentage per degree Celsius decrease in temperature?",
   "answer":"8% per 1 degree Celsius decrease.",
   "rationale":"Reduced metabolic rate lowers oxygen demand and provides myocardial and CNS protection during periods of ischemia, the basis for therapeutic cooling.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":64}],"confusable_with":"Q10 rule (roughly 50% per 10 degrees, but 8%/degree is the clinically used value)"},
  {"id":"temp-monitor-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Malignant hyperthermia is distinguished from thyroid storm intraoperatively by what key feature?",
   "answer":"MH is associated with rising EtCO2 and rising temperature triggered by volatile anesthetics or succinylcholine; thyroid storm has normal EtCO2 and temperature and is associated with hypokalemia.",
   "rationale":"MH involves uncontrolled skeletal muscle metabolism (hypermetabolic crisis) producing massive CO2 and heat; thyroid storm is a hyperadrenergic state without skeletal muscle hypermetabolism.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":85}],"confusable_with":"Neuroleptic malignant syndrome"},
  {"id":"temp-monitor-4","topic":T,"domain":D,"discipline":DI,
   "stem":"ASA Standard II requires temperature monitoring during all anesthetics when what condition is present?",
   "answer":"When clinically significant changes in body temperature are intended, anticipated, or suspected.",
   "rationale":"Routine temperature monitoring allows early detection of hypothermia, hyperthermia, and MH, enabling timely intervention before complications develop.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":13}],"confusable_with":""},
  {"id":"temp-monitor-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In a patient with a sudden increase in EtCO2 during CPR, what does this indicate?",
   "answer":"Return of spontaneous circulation (ROSC); EtCO2 goal during CPR is >10 mmHg, and a sudden increase signals effective cardiac output has been restored.",
   "rationale":"EtCO2 is a surrogate for pulmonary blood flow; ROSC restores cardiac output dramatically increasing CO2 delivery to the lungs and exhaled CO2.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":16}],"confusable_with":"Hyperventilation (reduces EtCO2, not increases it)"}
]

print(f"Topics 5-9 drafted: {len(kps)} KPs")
