import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 10: Tension Pneumothorax ──────────────────────────────────────────────────
T = "Tension Pneumothorax: Perioperative Recognition & Management"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"tension-ptx-1","topic":T,"domain":D,"discipline":DI,
   "stem":"In a ventilated patient, what combination of acute changes on the monitor strongly suggests tension pneumothorax?",
   "answer":"Sudden increase in peak airway pressure (if peak increases AND PEEP increases simultaneously, suspect decreased compliance or obstruction); also hypotension, tachycardia, decreased SpO2.",
   "rationale":"Air under pressure in the pleural space stiffens the chest and compresses the mediastinum, reducing both lung compliance and venous return.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":380}],"confusable_with":"Bronchospasm (also raises peak airway pressure but no hypotension early)"},
  {"id":"tension-ptx-2","topic":T,"domain":D,"discipline":DI,
   "stem":"In a patient with bullous lung disease on positive-pressure ventilation, what dangerous complication can a bulla develop?",
   "answer":"The bulla expands as its internal pressure becomes positive relative to adjacent lung; risk of rupture, tension pneumothorax, and bronchopleural fistula.",
   "rationale":"Positive-pressure ventilation forces gas into the low-resistance bulla; without effective drainage, progressive distension leads to rupture.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":505}],"confusable_with":""},
  {"id":"tension-ptx-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Tension pneumothorax is listed as one of the reversible Ts in cardiac arrest. What bedside intervention treats it?",
   "answer":"Immediate needle decompression (2nd intercostal space, midclavicular line) followed by chest tube insertion.",
   "rationale":"Rapid decompression of trapped pleural air restores venous return and cardiac output; delay is fatal.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)","page":5}],"confusable_with":"Cardiac tamponade (treated with pericardiocentesis)"},
  {"id":"tension-ptx-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Transtracheal jet ventilation via the cricothyroid membrane can be complicated by what tension-related emergency?",
   "answer":"Tension pneumothorax, because high-pressure jet ventilation without adequate exhalation time causes air trapping and barotrauma.",
   "rationale":"Jet ventilation at high pressures can drive air across any tracheal or bronchial leak into the pleural space; adequate exhalation time and low I:E ratio must be maintained.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":300}],"confusable_with":""},
  {"id":"tension-ptx-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Bronchopleural fistulas most commonly occur after what surgical procedure and what are the perioperative anesthetic priorities?",
   "answer":"Pneumonectomy (or lung resection); priorities include lung isolation to prevent soiling of healthy lung and avoiding high ventilatory pressures that enlarge the fistula.",
   "rationale":"A large fistula acts as an air leak; positive pressure preferentially escapes through it, compromising ventilation and risking contralateral contamination.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":918}],"confusable_with":""}
]
kps.append({"_type":"illness_script","topic":T,"discipline":DI,
   "enabling_conditions":"Positive-pressure ventilation, central line placement, bullous lung disease, trauma, or spontaneous pneumothorax in setting of airway obstruction",
   "pathophysiology":"One-way valve mechanism traps air in pleural space each breath; progressive pressure collapses ipsilateral lung, shifts mediastinum, compresses contralateral lung and great veins",
   "time_course":"Minutes; can occur suddenly during intubation, line placement, or ventilator adjustment",
   "key_features":"Hypotension, tachycardia, elevated peak airway pressure, decreased breath sounds ipsilateral, tracheal deviation (late), jugular venous distension",
   "consequence_if_missed":"Cardiac arrest from obstructive shock within minutes if not decompressed immediately"})

# ── 11: Thromboembolism Prophylaxis and Management ────────────────────────────
T = "Thromboembolism Prophylaxis and Management"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"vte-ppx-mgmt-1","topic":T,"domain":D,"discipline":DI,
   "stem":"For high-risk VTE patients (trauma and orthopedic), what pharmacological prophylaxis is recommended?",
   "answer":"Low molecular weight heparin (LMWH).",
   "rationale":"LMWH provides predictable anticoagulation with lower bleeding risk than unfractionated heparin and is supported by strong evidence for VTE prevention in high-risk orthopedic and trauma patients.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":773}],"confusable_with":"Unfractionated heparin (used in moderate-risk patients)"},
  {"id":"vte-ppx-mgmt-2","topic":T,"domain":D,"discipline":DI,
   "stem":"For patients at increased bleeding risk, what alternative to pharmacological thromboprophylaxis is recommended?",
   "answer":"Mechanical thromboprophylaxis: graduated compression stockings or intermittent pneumatic compression devices.",
   "rationale":"Mechanical methods reduce VTE risk without increasing bleeding risk, making them the preferred strategy when anticoagulants are contraindicated.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":773}],"confusable_with":""},
  {"id":"vte-ppx-mgmt-3","topic":T,"domain":D,"discipline":DI,
   "stem":"In atrial fibrillation with CKD (CrCl <60 mL/min), what modification is made to the CHADS2 score?",
   "answer":"Adding 2 points for CrCl <60 mL/min (Renal CHADS2 variant) has been proposed; however, adding GFR to AF risk scores has not shown important incremental benefit.",
   "rationale":"CKD increases thromboembolic risk in AF (annual rate 2.9% vs 0.2% without CKD), but the incremental predictive value of adding GFR to standard scores is limited.",
   "bloom":"analyze","source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":126}],"confusable_with":""},
  {"id":"vte-ppx-mgmt-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Perioperative management of antithrombotic therapy requires involvement of which specialties for a multidisciplinary approach?",
   "answer":"Patient, primary care physician, hematologist, surgeon, and anesthesia provider.",
   "rationale":"Decisions require balancing the thrombotic risk of holding anticoagulation against the bleeding risk of continuing it; this requires coordinated input across specialties.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":459}],"confusable_with":""},
  {"id":"vte-ppx-mgmt-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Andexanet alfa for Factor Xa inhibitor reversal shows what hemostatic effectiveness at 12 hours, and what is the 30-day VTE risk?",
   "answer":"Mean hemostatic effectiveness 82% at 12 hours (vs 88% for PCC); 30-day VTE rate approximately 5%.",
   "rationale":"Andexanet alfa neutralizes Factor Xa inhibitors but carries a rebound thrombotic risk because it also neutralizes endogenous anticoagulants.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation","page":46}],"confusable_with":"PCC (broader reversal agent, slightly higher hemostatic effectiveness)"}
]

# ── 12: Thyroid and parathyroid surgery anesthesia ────────────────────────────
T = "Thyroid and parathyroid surgery anesthesia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"thyroid-para-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Thyroid storm may be encountered in a patient with inadequately controlled hyperthyroidism; how does it differ from malignant hyperthermia in onset and EtCO2?",
   "answer":"Thyroid storm onset is typically 6-24h postoperative (not immediate); unlike MH, it is not associated with rising EtCO2 and temperature triggered by volatile agents.",
   "rationale":"Thyroid storm is a hyperadrenergic crisis, not a hypermetabolic skeletal muscle disorder; EtCO2 does not surge as in MH.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1227}],"confusable_with":"Malignant hyperthermia"},
  {"id":"thyroid-para-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What causes airway obstruction after thyroid or parathyroid surgery?",
   "answer":"Bleeding from the operative site compressing the trachea.",
   "rationale":"Hematoma expansion in the confined neck compartment exerts external pressure on the trachea, causing progressive airway obstruction that requires immediate surgical decompression.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":581}],"confusable_with":"Recurrent laryngeal nerve palsy (causes hoarseness, not acute obstruction)"},
  {"id":"thyroid-para-3","topic":T,"domain":D,"discipline":DI,
   "stem":"What intervention reduces hematoma risk during emergence from thyroid surgery?",
   "answer":"Mitigating hypertension and coughing during emergence and extubation.",
   "rationale":"Surges in venous pressure during bucking or coughing can disrupt surgical hemostasis and initiate hematoma formation in the neck.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":549}],"confusable_with":""},
  {"id":"thyroid-para-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Unilateral recurrent laryngeal nerve (RLN) palsy after thyroid surgery produces what clinical findings?",
   "answer":"Hoarseness.",
   "rationale":"The unilateral RLN supplies the ipsilateral vocal cord; palsy causes the cord to be paralyzed in the paramedian position, producing a hoarse but still patent airway.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1227}],"confusable_with":"Bilateral RLN palsy (aphonia and stridor, airway emergency)"},
  {"id":"thyroid-para-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Multiple endocrine neoplasia (MEN) type 2 is characterized by what combination of tumors that is relevant to the anesthesiologist?",
   "answer":"MEN type 2 includes medullary thyroid carcinoma, pheochromocytoma, and parathyroid hyperplasia; pheochromocytoma causes hypertensive crisis on induction if not treated preoperatively.",
   "rationale":"Undiagnosed pheochromocytoma in a MEN2 patient undergoing thyroid surgery can cause catecholamine release triggered by surgical or anesthetic stimulation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1244}],"confusable_with":"MEN type 1 (pancreatic, pituitary, parathyroid — no pheo)"}
]

# ── 13: Tonsillectomy and adenoidectomy (T&A) anesthesia ─────────────────────
T = "Tonsillectomy and adenoidectomy (T&A) anesthesia"
D = "Pediatric anesthesia (neonatal & pediatric physiology, pediatric airway, congenital conditions, fluid & glucose management, emergence, common procedures)"
kps += [
  {"id":"ta-anes-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Severe lymphoid hyperplasia leading to upper airway obstruction can cause what end-organ complication from chronic hypoxia?",
   "answer":"Pulmonary hypertension with cor pulmonale.",
   "rationale":"Chronic upper airway obstruction causes nocturnal hypoxia and hypercapnia; sustained pulmonary vasoconstriction leads to elevated PVR, right ventricular hypertrophy, and cor pulmonale.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1484}],"confusable_with":""},
  {"id":"ta-anes-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Although deep extubation reduces laryngospasm risk after T&A, why is awake extubation generally preferred?",
   "answer":"Awake extubation reduces the likelihood of aspiration of blood and secretions from the operative field.",
   "rationale":"Blood pooled in the pharynx from the operative site can be aspirated if protective airway reflexes are obtunded during deep extubation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1484}],"confusable_with":""},
  {"id":"ta-anes-3","topic":T,"domain":D,"discipline":DI,
   "stem":"What pre-extubation steps are recommended before removing the ETT at the end of T&A?",
   "answer":"Gentle inspection and suctioning of the pharynx, then gastric suctioning (given common postoperative vomiting).",
   "rationale":"Blood and secretions in the pharynx and stomach increase aspiration risk; clearing these before extubation reduces complications.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1484}],"confusable_with":""},
  {"id":"ta-anes-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Which patient factors after T&A increase the risk of postoperative complications requiring hospital admission?",
   "answer":"Sleep apnea and recent upper respiratory infection.",
   "rationale":"OSA patients are at higher risk of postoperative respiratory events (desaturation, obstruction); recent URI increases airway reactivity and risk of laryngospasm/bronchospasm.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1484}],"confusable_with":""},
  {"id":"ta-anes-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Children younger than what age undergoing T&A may be hospitalized for the first postoperative night because of what specific risks?",
   "answer":"Age <3 years; risks of bleeding and airway obstruction.",
   "rationale":"Very young children have smaller airways with less reserve, higher risk of postoperative bleeding, and limited ability to report distress, warranting overnight monitoring.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1484}],"confusable_with":""}
]

print(f"Topics 10-13 drafted: {len(kps)} KPs")
