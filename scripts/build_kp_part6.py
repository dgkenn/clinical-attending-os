import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch5.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch5")

# ============================================================
# ITEM 25: Airway assessment and prediction of difficult intubation
# ============================================================
topic = "Airway assessment and prediction of difficult intubation"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"airway-assessment-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the predictors of IMPOSSIBLE (not merely difficult) mask ventilation that require the highest level of airway planning?",
   "answer":"Impossible mask ventilation predictors: Mallampati III-IV, OSA, history of upper airway surgery, and radiation changes to the neck.",
   "rationale":"Impossible mask ventilation (cannot ventilate by mask at all) is the most dangerous scenario because it removes the rescue option while equipment is being prepared for intubation.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":43}],"confusable_with":""},
  {"id":"airway-assessment-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"The upper lip bite test predicts difficult intubation — what finding indicates potentially easier intubation and what finding indicates difficulty?",
   "answer":"Ability to bite BEYOND the lower border of the upper lip with lower incisors = potentially easier intubation. Inability to bite the upper lip at all = predicts difficult intubation.",
   "rationale":"The upper lip bite test assesses mandibular mobility and dental occlusion; inability to bite the upper lip reflects restricted mouth opening or class III dental occlusion associated with difficult laryngoscopy.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":500}],"confusable_with":"Mallampati score"},
  {"id":"airway-assessment-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the five predictors of difficult mask ventilation in the Stanford mnemonic?",
   "answer":"MOANS: Mallampati III or IV, Obstruction/OSA (or upper airway surgery/radiation), Age >57, No teeth (edentulous), Snoring; beard and obesity (BMI >30) and decreased mandibular protrusion also listed; 3+ predictors = difficult.",
   "rationale":"Difficult mask ventilation is an independent predictor of difficult airway management; identifying it prospectively allows preparation of rescue equipment and alternate techniques.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":43}],"confusable_with":""},
  {"id":"airway-assessment-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"After preoxygenation, for approximately how long can a healthy, non-obese adult be safely apneic before significant desaturation occurs?",
   "answer":"Approximately 9 minutes of safe apnea after adequate preoxygenation (breathing 100% O2 for several minutes, replacing nitrogen in FRC with O2).",
   "rationale":"Preoxygenation fills the FRC (~2L in adults) with O2; oxygen consumption of 200-250 mL/min depletes this reserve over ~8-9 minutes, providing the laryngoscopist adequate time for intubation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":286}],"confusable_with":""},
  {"id":"airway-assessment-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Pharyngoesophageal perforation is a rare complication of difficult intubation — what patient profile is at highest risk?",
   "answer":"Difficult intubation, age over 60 years, and female gender are risk factors; signs are often delayed (sore throat, cervical pain, cough progressing to fever, dysphagia, mediastinitis).",
   "rationale":"Older female patients have more fragile posterior pharyngeal mucosa; multiple intubation attempts and poor visualization increase posterior wall injury risk.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2025}],"confusable_with":""},
  {"id":"airway-assessment-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the 2022 ASA Practice Guideline reference used for difficult airway management in clinical practice?",
   "answer":"Apfelbaum et al. 2022 ASA Practice Guidelines for Management of the Difficult Airway (Anesthesiology 2021; doi:10.1097/ALN.0000000000004002) — updated from the 2013 guidelines.",
   "rationale":"The ASA difficult airway algorithm provides a structured decision tree for unanticipated and anticipated difficult airways including awake intubation, video laryngoscopy, and CICO rescue.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":311}],"confusable_with":""},
  {"id":"airway-assessment-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What conditions reduce the time to desaturation after apnea compared to a healthy adult, requiring accelerated airway management?",
   "answer":"Obesity, pregnancy, and other conditions with reduced functional residual capacity (e.g., abdominal compartment syndrome, pulmonary edema) — all reduce the O2 reservoir and decrease safe apnea time.",
   "rationale":"FRC is the main O2 reservoir during apnea; conditions that reduce FRC reduce safe apnea time proportionally; obese patients may desaturate in <3 minutes despite preoxygenation.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":286}],"confusable_with":""},
]

# ============================================================
# ITEM 26: Airway fires
# ============================================================
topic = "Airway fires"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"airway-fires-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most commonly reported surgical fire scenario and what is the most effective prevention?",
   "answer":"Supplemental oxygen delivery during head/neck/airway surgery (surgical site above the xiphoid with open O2 delivery) is the most common scenario; prevention is elimination of open oxygen delivery (use closed mask systems or reduce FiO2 before ignition sources).",
   "rationale":"The fire triangle requires oxidizer + ignition + fuel; removing open O2 delivery eliminates the oxidizer in the surgical field and prevents the vast majority of airway fires.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":55}],"confusable_with":""},
  {"id":"airway-fires-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first action when a fire occurs IN the airway during surgery?",
   "answer":"Immediately stop delivery of all fresh gases to the patient (disconnect circuit/oxygen supply); remove the endotracheal tube; pour saline into the airway; assess for injury and reestablish airway.",
   "rationale":"Stopping gas flow removes the oxidizer feeding the fire; removing the burning ETT eliminates the fuel; saline quenches residual heat and prevents further mucosal injury.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":54}],"confusable_with":""},
  {"id":"airway-fires-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Before using laser or electrocautery in airway surgery, what oxygen concentration precaution should be taken?",
   "answer":"Reduce oxygen concentration to a safe level (often FiO2 <0.3) for a sufficient period before ignition device use; for laser airway surgery, use jet ventilation without ETT or an appropriate laser-safe ETT specific to the laser wavelength.",
   "rationale":"High FiO2 dramatically lowers the ignition threshold; reducing O2 concentration before electrocautery/laser activation prevents combustion of flammable materials in the high-oxygen field.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":54}],"confusable_with":""},
  {"id":"airway-fires-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What type of fire extinguisher is safe for fires occurring ON a patient in the operating room?",
   "answer":"CO2 extinguisher is safe for fires on the patient; both class A and AC extinguishers can be constructed as nonferromagnetic devices, making them best for fires near MRI equipment.",
   "rationale":"CO2 does not leave residue on wounds and does not cause tissue injury; water or dry powder extinguishers would cause additional injury to the patient and contaminate the surgical field.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":55}],"confusable_with":""},
  {"id":"airway-fires-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Alcohol-based skin preparations used in surgical prep require what precaution before draping?",
   "answer":"Alcohol-based prep must be allowed to fully dry and vapors dissipate before draping; pooling under drapes creates a flammable vapor reservoir that can be ignited by electrocautery.",
   "rationale":"Isopropyl alcohol is highly flammable; residual vapor trapped under drapes near the surgical site can combust when an ignition source is used — a preventable cause of OR fires.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":54}],"confusable_with":""},
  {"id":"airway-fires-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Cyanide toxicity from synthetic fires involves what antidote strategy?",
   "answer":"Cyanide from synthetic/polyurethane fires inhibits cytochrome oxidase; treatment: remove from exposure, 100% O2, hydroxocobalamin (chelates cyanide) or sodium thiosulfate; dicobalt edetate in some protocols.",
   "rationale":"Hydroxocobalamin binds cyanide to form cyanocobalamin, which is renally excreted; it does not cause methemoglobinemia unlike older antidotes and is safe to use empirically in fire victims.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":"CO poisoning"},
]

# ============================================================
# ITEM 27: Airway management for ENT and shared-airway surgery
# ============================================================
topic = "Airway management for ENT and shared-airway surgery"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"ent-airway-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Laryngospasm in ENT surgery is mediated by which nerve and what are the two main types (complete vs incomplete) of laryngospasm?",
   "answer":"Laryngospasm is mediated by the Superior Laryngeal Nerve; complete (true cords + false cords closed) causes silent chest and rapid hypoxia; incomplete (partially open) causes crowing inspiratory stridor.",
   "rationale":"Laryngospasm is a protective reflex; the superior laryngeal nerve triggers closure of true cords; false cord involvement in complete spasm eliminates any airway passage.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":577}],"confusable_with":""},
  {"id":"ent-airway-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the key predisposing factors for laryngospasm in the perioperative period?",
   "answer":"Stage 2 anesthesia (excitement/delirium phase), light anesthesia relative to stimulation, mechanical irritants (blood/mucus/vomit/secretions in airway), ETT (RR 12 vs LMA RR 7 vs facemask), reactive airway disease, recent URI.",
   "rationale":"Laryngospasm occurs when airway reflexes are active (light anesthesia) but protective responses are exaggerated; bloodied airways in ENT surgery compound the risk.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":73}],"confusable_with":""},
  {"id":"ent-airway-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why is nitrous oxide washed out before ending ear surgery, and approximately how long does this take?",
   "answer":"Nitrous oxide must be washed out before ending surgery to prevent middle ear pressure changes from N2O diffusing into/out of the closed middle ear space; 15-30 min of washout is typically recommended.",
   "rationale":"N2O diffuses into air-containing spaces faster than nitrogen can exit; in the closed middle ear this causes pressure build-up intraoperatively and sudden pressure loss on N2O discontinuation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1287}],"confusable_with":""},
  {"id":"ent-airway-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"During emergence from head and neck cancer surgery, what extubation criterion is mandatory given the ongoing aspiration risk?",
   "answer":"Patient must be fully awake with intact airway reflexes before extubation; deep extubation is relatively contraindicated given aspiration risk from blood/secretions in the oropharynx.",
   "rationale":"Head/neck surgery creates a blood-contaminated oropharyngeal field; patients cannot safely protect their airway until fully awake with active gag and cough reflexes.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1290}],"confusable_with":""},
  {"id":"ent-airway-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"During an ENT surgical emergency requiring a surgical airway, what are the recommended 20 seconds of preparation before cricothyrotomy?",
   "answer":"Identify an assistant, place a shoulder roll to expose the trachea, direct a light source at the neck; surgical cricothyrotomy with scalpel (#10 or #11 blade), bougie, and 6.0 cuffed ETT is successful >90% of the time.",
   "rationale":"Even in emergencies, 20 seconds of preparation dramatically improves success; cannula-based techniques have far higher failure rates than surgical approach.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":45}],"confusable_with":""},
  {"id":"ent-airway-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In epistaxis management, what anesthetic emergence criterion is specific to this population?",
   "answer":"Full awakening with intact airway reflexes is required; patient must not be extubated until protective reflexes return to prevent aspiration of blood; IV lidocaine or dexmedetomidine can reduce coughing during emergence.",
   "rationale":"Epistaxis leaves blood in the hypopharynx and stomach; deep extubation risks aspiration in this blood-contaminated field even if standard extubation criteria are met.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1290}],"confusable_with":""},
]

# ============================================================
# ITEM 28: Airway management in head and neck pathology
# ============================================================
topic = "Airway management in head and neck pathology"
domain = "Airway management (assessment & prediction, supraglottic & ETT devices, laryngoscopy/video, awake intubation, difficult & failed airway algorithm, extubation, complications)"
disc = "anesthesia"

kps += [
  {"id":"head-neck-airway-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"For head and neck cancer surgery including laryngectomy, what determines timing of tracheostomy planning?",
   "answer":"Timing of tracheostomy depends on preoperative degree of airway compromise; if significant compromise, awake tracheostomy before induction may be necessary; less severe compromise allows induction then surgical tracheostomy.",
   "rationale":"Head/neck cancer can distort airway anatomy, making post-induction cannot-intubate-cannot-oxygenate scenarios likely; preoperative tracheostomy under local is the safest option when doubt exists.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1277}],"confusable_with":""},
  {"id":"head-neck-airway-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the correct approach to airway management when cervical spine pathology is suspected?",
   "answer":"Maintain head in neutral position with manual in-line stabilization of the neck during all airway maneuvers; do NOT place in sniffing position without radiographic clearance of the cervical spine.",
   "rationale":"Flexion-extension movements during laryngoscopy risk cord compression in unstable cervical spine; in-line stabilization prevents movement while allowing intubation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":504}],"confusable_with":""},
  {"id":"head-neck-airway-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In head and neck anatomy relevant to awake intubation, what is the functional anatomy at the level of the carina?",
   "answer":"The carina overlies the fifth thoracic vertebra; the adult trachea extends from the larynx to the carina; understanding this anatomy guides nasotracheal intubation depth and tube positioning.",
   "rationale":"Accurate knowledge of tracheal length prevents right mainstem bronchial intubation (ETT too deep) or cuff malposition above the vocal cords (too shallow).",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":280}],"confusable_with":""},
  {"id":"head-neck-airway-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What anesthetic techniques minimize blood at the microsurgical field during ear and head/neck surgery?",
   "answer":"Head elevation 15 degrees, epinephrine infiltration (1:50,000-1:200,000) or topical application, and moderate controlled hypotension; prevent coughing on ETT during emergence (coughing during neck movement causes movement of the surgical site).",
   "rationale":"Microsurgery requires a bloodless field; controlled hypotension and vasoconstrictors reduce surgical bleeding; coughing produces blood pressure spikes and mechanical movement that disrupt delicate repairs.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1287}],"confusable_with":""},
  {"id":"head-neck-airway-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Video laryngoscopy has revolutionized airway management in difficult airways — what is the key advantage of video laryngoscopes over direct laryngoscopy?",
   "answer":"Video laryngoscopes do NOT require alignment of oral, pharyngeal, and laryngeal axes (the 'sniffing position' requirement); the chip at the blade tip provides indirect glottic visualization even without direct line of sight.",
   "rationale":"Direct laryngoscopy requires precise axis alignment; video laryngoscopy circumvents this by delivering real-time video of the glottis regardless of neck mobility or anatomy.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":518}],"confusable_with":""},
]

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch6.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch6")
