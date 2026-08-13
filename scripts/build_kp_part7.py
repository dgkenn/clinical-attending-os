import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch6.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch6")

# ============================================================
# ITEM 29: Airway management in the obese patient
# ============================================================
topic = "Airway management in the obese patient"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"obese-airway-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Obesity (BMI >30) is a predictor of difficult mask ventilation — what other anatomical features compound this risk?",
   "answer":"Mallampati III/IV, male sex, sleep apnea, beard, and large neck circumference compound mask ventilation difficulty in obese patients; together these increase the probability of impossible mask ventilation.",
   "rationale":"Obesity causes pharyngeal adipose tissue deposition narrowing the upper airway; in combination with OSA-related pharyngeal hypotonia and a short/fat neck, both mask ventilation and intubation become challenging.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":43}],"confusable_with":""},
  {"id":"obese-airway-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How does obesity reduce safe apnea time during airway management and what positioning strategy partially compensates?",
   "answer":"Obesity reduces FRC (abdominal adipose displaces diaphragm cephalad), dramatically shortening safe apnea time to as little as 2-3 minutes; ramping (head elevated, ears level with sternum) in the 'sniffing' position optimizes glottic view and maximizes preoxygenation FRC.",
   "rationale":"Reduced FRC = smaller O2 reservoir at apnea onset; ramping offloads abdominal weight from the diaphragm and aligns oral/pharyngeal axes for improved laryngoscopy view.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":286}],"confusable_with":""},
  {"id":"obese-airway-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Patients with OSA are vulnerable to postoperative airway obstruction — what is the specific mechanism and when is the risk highest?",
   "answer":"OSA patients have pharyngeal hypotonia worsened by opioids and sedatives; risk is highest in the supine position and in the first 24 hours when sedative medications are active and REM rebound occurs.",
   "rationale":"OSA pathophysiology involves loss of upper airway muscle tone; opioids and anesthetics further impair genioglossus activity, causing more severe and frequent obstruction postoperatively.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1240}],"confusable_with":""},
  {"id":"obese-airway-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"A patient with known difficult intubation, morbid obesity, and recent upper airway surgery is being evaluated for elective surgery — what relative contraindication exists for deep extubation?",
   "answer":"Deep extubation is relatively contraindicated when there is a history of difficult mask ventilation/intubation, high aspiration risk, morbid obesity, OSA, or a surgical procedure that may have caused airway edema.",
   "rationale":"Deep extubation precludes immediate reintubation in case of airway obstruction; in a patient who was previously difficult to intubate, loss of airway control after deep extubation may be catastrophic.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":301}],"confusable_with":""},
  {"id":"obese-airway-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"The STOP-BANG score is used to screen for obstructive sleep apnea — what score is associated with increased postoperative complications?",
   "answer":"STOP-BANG score >/=3 is associated with increased risk of postoperative complications; higher scores predict more severe OSA and greater perioperative risk.",
   "rationale":"STOP-BANG (Snoring, Tiredness, Observed apnea, Pressure, BMI, Age, Neck circumference, Gender) validated against polysomnography; score >/=3 prompts enhanced monitoring or PAP therapy.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":698}],"confusable_with":""},
  {"id":"obese-airway-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For obese patients with significant OSA and OSA-related complications (elevated bicarbonate, preoperative hypoxemia), what preoperative evaluation and treatment should be initiated?",
   "answer":"Patients with serum bicarbonate elevation (indicating chronic hypercapnia) or preoperative hypoxemia without other respiratory disease should undergo sleep study (PSG) and initiation of PAP (positive airway pressure) therapy preoperatively.",
   "rationale":"Elevated bicarbonate is a surrogate for chronic CO2 retention in obesity hypoventilation syndrome; untreated OHS patients have dramatically increased perioperative respiratory risk.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":890}],"confusable_with":""},
  {"id":"obese-airway-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Oral and nasal airways are sized using what anatomical landmark, and why is an oral airway hazardous in a lightly anesthetized patient?",
   "answer":"The distal tip should reach the angle of the mandible when the proximal end aligns with the mouth (oral) or nostril (nasal); an oral airway in a lightly anesthetized patient may trigger gag reflex or laryngospasm.",
   "rationale":"The oral airway displaces the tongue from the posterior pharynx; in light anesthesia, mechanical stimulation of the oropharyngeal mucosa triggers protective reflexes.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":287}],"confusable_with":"Nasopharyngeal airway (better tolerated)"},
]

# ============================================================
# ITEM 30: Airway management in the obstetric patient
# ============================================================
topic = "Airway management in the obstetric patient"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"obstetric-airway-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"How does preoxygenation in the term pregnant patient differ from a healthy non-pregnant adult and why?",
   "answer":"Pregnant patients desaturate faster (reduced FRC from elevated diaphragm + increased O2 consumption from fetus/placenta/uterus); preoxygenation with 100% O2 via tight-fitting mask for at least 3 minutes (or 4 maximal vital capacity breaths) is essential but provides a shorter safe apnea window.",
   "rationale":"Pregnancy reduces FRC by 20-25% via diaphragm elevation; increased maternal O2 demand reduces the margin of safety; urgent airway management must proceed more rapidly than in non-pregnant patients.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":505}],"confusable_with":""},
  {"id":"obstetric-airway-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the leading causes of anesthesia-related maternal death or brain injury according to 2019 obstetric closed claims analysis?",
   "answer":"High neuraxial block, embolic events, and failed intubation are the top three causes of maternal death or brain injury resulting in paid claims in the obstetric anesthesia closed claims analysis.",
   "rationale":"Obstetric airway management is high-risk due to edematous/friable airway, full stomach, reduced FRC, and urgency; failed intubation and high neuraxial blocks remain preventable causes of maternal death.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2050}],"confusable_with":""},
  {"id":"obstetric-airway-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Laryngospasm can lead to negative pressure pulmonary edema (NPPE) — through what mechanism?",
   "answer":"Forceful inspiratory effort against a closed glottis generates highly negative intrathoracic pressure; this increases hydrostatic pressure gradient across the alveolar-capillary membrane causing pulmonary edema.",
   "rationale":"Muller maneuver generates -40 to -100 cmH2O intrathoracic pressure; increased venous return and reduced interstitial pressure draw fluid into alveoli.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":73}],"confusable_with":"Cardiogenic pulmonary edema"},
  {"id":"obstetric-airway-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is modified RSI (rapid sequence induction) and when might positive pressure ventilation be applied despite full-stomach concern?",
   "answer":"Modified RSI uses positive pressure ventilation <20 cmH2O to maintain oxygenation if hypoxemia develops before intubation is secured; this small risk of gastric insufflation is outweighed by the catastrophic risk of hypoxemia in patients with reduced FRC (pregnant, obese).",
   "rationale":"Classical RSI avoids any PPV; modified RSI accepts a small gastric inflation risk to prevent maternal/fetal hypoxia during the apneic period before intubation.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":250}],"confusable_with":""},
  {"id":"obstetric-airway-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In preeclamptic patients with severe hypertension requiring general anesthesia, what invasive monitoring is indicated and what is the antihypertensive goal?",
   "answer":"Invasive arterial and central venous monitoring for severe hypertension, pulmonary edema, or refractory oliguria; IV vasodilator infusions may be necessary; spinal and epidural both cause comparable decreases in blood pressure.",
   "rationale":"Preeclampsia causes endothelial dysfunction and labile hypertension; invasive monitoring allows real-time titration of antihypertensives and fluid management during the hemodynamically unstable period.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1422}],"confusable_with":""},
  {"id":"obstetric-airway-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In obstetric general anesthesia, what are the concerns around neuromuscular blockade choice and reversal?",
   "answer":"Succinylcholine remains commonly used for RSI in obstetrics (fast onset/offset) but rocuronium with sugammadex reversal is an alternative; avoid residual NMB at delivery as it can cause neonatal respiratory depression.",
   "rationale":"Succinylcholine does not cross the placenta at clinical doses; rocuronium may cross if placenta has altered permeability; sugammadex enables rapid reversal but is expensive and rare in some settings.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1387}],"confusable_with":""},
]

# ============================================================
# ITEM 31: Airway management with cervical spine pathology
# ============================================================
topic = "Airway management with cervical spine pathology"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"cervical-spine-airway-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What three simultaneous challenges must be managed when intubating a trauma patient with suspected cervical spine injury?",
   "answer":"(1) Basic life support/airway intervention for hypoxia; (2) presumed cervical spinal cord injury until proven otherwise (in-line stabilization); (3) potential for failed endotracheal intubation — have all three backup plans ready simultaneously.",
   "rationale":"The trauma airway requires concurrent consideration of oxygenation urgency, cord protection, and failed airway contingency; addressing only one at a time risks the others.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1322}],"confusable_with":""},
  {"id":"cervical-spine-airway-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In-line stabilization is the standard for cervical spine precaution during intubation — what is the ideal head position and what is NOT recommended without radiographic clearance?",
   "answer":"Neutral head position with manual in-line stabilization; the sniffing position (neck flexion + head extension) is NOT recommended until cervical spine radiographs have been reviewed and cleared by an appropriate specialist.",
   "rationale":"The sniffing position maximally extends the atlantoaxial joint; in unstable cervical injury this can cause cord compression and permanent neurological injury.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":504}],"confusable_with":""},
  {"id":"cervical-spine-airway-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For TBI patients requiring RSI, what combination of agents blunts the ICP rise from intubation?",
   "answer":"Propofol 1.5-3.0 mg/kg + rapid-onset NMB (succinylcholine or rocuronium); pre-treatment with propofol blunts the ICP response to laryngoscopy; succinylcholine can be used despite theoretical ICP increase as the risk of delayed intubation is greater.",
   "rationale":"Laryngoscopy triggers a sympathetic surge raising ICP; propofol induction reduces CBF and CMR; the urgency of TBI airway management outweighs theoretical succinylcholine ICP risks.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":982}],"confusable_with":""},
  {"id":"cervical-spine-airway-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Spinal cord injuries most often occur from what mechanism at the cervical versus thoracic spine?",
   "answer":"Cervical spine: extension injuries (more common); thoracic spine: compression-flexion injuries; most are traumatic from fracture-dislocation of vertebral column causing partial or complete cord transection.",
   "rationale":"The cervical spine's greater mobility predisposes to hyperextension injuries (e.g., rear-end collision); the thoracic spine's rigidity means higher energy trauma causes compression-flexion injuries.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1012}],"confusable_with":""},
  {"id":"cervical-spine-airway-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Video laryngoscopy is particularly advantageous in the cervical spine patient — why?",
   "answer":"Video laryngoscopes do not require axis alignment (flexion-extension) of the oral/pharyngeal/laryngeal axes; glottic visualization is achieved without neck movement, preserving cervical spine protection.",
   "rationale":"Direct laryngoscopy requires neck extension to align the three airway axes; video laryngoscopy eliminates this requirement, making it the preferred primary technique in unstable cervical spine.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":518}],"confusable_with":""},
  {"id":"cervical-spine-airway-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the primary indication for spinal cord injury surgery and what anesthetic concern is paramount?",
   "answer":"Surgery for symptomatic nerve root/cord compression from disc protrusion, osteophyte, or trauma; intraoperative spinal cord monitoring (SSEPs, MEPs) is paramount and requires limiting volatile anesthetic concentrations and avoiding paralysis during MEP monitoring.",
   "rationale":"Cord monitoring requires preserved motor evoked potential pathways; high volatile anesthetic concentrations and NMBs abolish MEPs, requiring TIVA or low-dose volatile with opioid supplements.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":990}],"confusable_with":""},
]

# ============================================================
# ITEM 32: Airway pharmacology: topical anesthesia and sedation for awake airway
# ============================================================
topic = "Airway pharmacology: topical anesthesia and sedation for awake airway"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"awake-airway-pharm-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the principal sensory nerve blocks required for awake fiberoptic intubation, and what nerves supply each region?",
   "answer":"Nose/nasopharynx: anterior ethmoidal + posterior nasal (sphenopalatine) nerves; oropharynx: glossopharyngeal nerve (IX); larynx above cords: internal branch of superior laryngeal nerve; trachea below cords: recurrent laryngeal nerve (topical transtracheal or direct application).",
   "rationale":"Systematic sensory denervation of each anatomical region eliminates the gag, cough, and vocal cord closure reflexes that impede awake airway instrumentation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":280}],"confusable_with":""},
  {"id":"awake-airway-pharm-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Dexmedetomidine is commonly used for awake intubation sedation — what is its key advantage over benzodiazepines and what is its mechanism?",
   "answer":"Dexmedetomidine (alpha-2 agonist) provides sedation while PRESERVING spontaneous ventilation and airway reflexes; it does not cause respiratory depression at clinical sedation doses, unlike benzodiazepines or propofol.",
   "rationale":"Dexmedetomidine acts on brainstem alpha-2 receptors (locus coeruleus) to produce sleep-like sedation without respiratory center depression; the patient remains arousable and responsive.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":390}],"confusable_with":"Midazolam sedation"},
  {"id":"awake-airway-pharm-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"MAC-awake is defined as the volatile anesthetic concentration at which 50% of patients respond to verbal command — how does this compare to MAC and MAC-amnesia?",
   "answer":"MAC-awake is approximately 0.3-0.4 MAC (about one-third of MAC immobility); MAC-amnesia is less than MAC-awake (conscious recall abolished before movement suppression); MAC-BAR (blunted autonomic response) is approximately 1.5 MAC.",
   "rationale":"These endpoints reflect distinct CNS functions lost at different anesthetic depths; MAC-awake is relevant for awake airway work as it defines the sedation threshold below which voluntary response is preserved.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":114}],"confusable_with":""},
  {"id":"awake-airway-pharm-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What pharmacodynamic change in the elderly reduces anesthetic requirement for all agents?",
   "answer":"Reduced minimum alveolar concentration (MAC) for volatile agents; lower dose requirements for propofol, etomidate, opioids, benzodiazepines, and barbiturates — the principal pharmacodynamic change of aging.",
   "rationale":"Elderly patients have reduced neuronal density, altered receptor sensitivity, and decreased cerebral metabolic rate; less anesthetic is required to achieve equivalent CNS effect.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""},
  {"id":"awake-airway-pharm-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is cricoid pressure (Sellick maneuver) and what is the current evidence regarding its effectiveness?",
   "answer":"Cricoid pressure compresses the esophagus against the cervical vertebrae to prevent passive regurgitation during RSI; a 2015 meta-analysis did NOT demonstrate a measurable impact on clinical outcomes, and it is not universally applied in current practice.",
   "rationale":"Despite decades of use, cricoid pressure may worsen laryngoscopic view without proven benefit in preventing aspiration; its routine use is questioned though it remains widely practiced.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":250}],"confusable_with":""},
  {"id":"awake-airway-pharm-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In pediatric patients, how do the pharmacokinetics of propofol differ from adults in terms of volume of distribution, elimination half-life, and implications for continuous infusion?",
   "answer":"Children have larger volume of distribution than adults (weight-adjusted), shorter elimination half-life, and higher plasma clearance; recovery from single bolus is similar to adults but recovery from continuous infusion may be MORE rapid in children.",
   "rationale":"Pediatric pharmacokinetic differences require higher weight-adjusted doses but also enable faster emergence after infusion; propofol infusion syndrome risk is higher in children with prolonged infusions.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1456}],"confusable_with":""},
  {"id":"awake-airway-pharm-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In awake airway management, what agents can be used intravenously to blunt the hemodynamic response to laryngoscopy while preserving spontaneous ventilation?",
   "answer":"Dexmedetomidine infusion (most commonly used for awake intubation sedation); remifentanil infusion; low-dose ketamine. These preserve spontaneous breathing while reducing sympathetic response to airway manipulation.",
   "rationale":"The ideal awake airway drug blunts reflexes (gag, cough, hemodynamic) while preserving respiratory drive; dexmedetomidine and remifentanil are the most evidence-based options.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":""},
]

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch7.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch7")
