import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── 0: Shared airway principles — ENT/head-neck ──────────────────────────────
T = "Shared airway principles — ENT/head-neck"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
DI = "anesthesia"
kps += [
  {"id":"shared-airway-ent-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Before performing an emergency surgical front-of-neck airway, what three preparatory steps should always be taken even under time pressure?",
   "answer":"Identify an assistant, place a shoulder roll to expose the trachea, direct a light source at the neck.",
   "rationale":"Twenty seconds of preparation optimises anatomy exposure and team coordination, dramatically reducing failure rate.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":45}],"confusable_with":""},
  {"id":"shared-airway-ent-2","topic":T,"domain":D,"discipline":DI,
   "stem":"When at least 3 predictors of difficult mask ventilation are simultaneously present, what is the clinical implication?",
   "answer":"Anticipate cannot-ventilate scenario; plan for awake intubation or surgical airway before induction.",
   "rationale":"Cumulative risk factors for difficult mask ventilation are additive; 3+ predictors markedly increases probability of a failed airway.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":43}],"confusable_with":""},
  {"id":"shared-airway-ent-3","topic":T,"domain":D,"discipline":DI,
   "stem":"During shared-airway ENT procedures, spontaneous ventilation during fiber-optic intubation is preferred when there is concern about what specific condition?",
   "answer":"Inability to mask-ventilate (cannot-ventilate scenario) if intubation fails.",
   "rationale":"Preserving spontaneous ventilation maintains airway patency and oxygenation if intubation attempts fail, preventing the cannot-intubate-cannot-oxygenate crisis.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":308}],"confusable_with":""},
  {"id":"shared-airway-ent-4","topic":T,"domain":D,"discipline":DI,
   "stem":"For brief intense stimulation such as suspension laryngoscopy, what agent is a reasonable non-opioid alternative for blunting hemodynamic response?",
   "answer":"Esmolol.",
   "rationale":"Esmolol provides rapid-onset, short-duration beta-blockade attenuating sympathetic response to laryngoscopy without prolonged respiratory depression.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":32}],"confusable_with":"Remifentanil"},
  {"id":"shared-airway-ent-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In an emergency front-of-neck airway, which technique — cannula-based or scalpel-based — has a higher failure rate?",
   "answer":"Cannula-based (percutaneous) techniques have a far higher failure rate in emergencies than scalpel-based approaches.",
   "rationale":"Under emergency conditions, cannula kinking and inadequate ventilation are common; the scalpel technique is faster and more reliable.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":45}],"confusable_with":"Scalpel cricothyrotomy"}
]

# ── 1: Shock: Classification and Pathophysiology ─────────────────────────────
T = "Shock: Classification and Pathophysiology"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"shock-class-path-1","topic":T,"domain":D,"discipline":DI,
   "stem":"A serum lactate above what threshold has strong correlation with mortality in severe sepsis?",
   "answer":"4 mEq/L (4 mmol/L).",
   "rationale":"Hyperlactatemia above 4 mEq/L reflects severe tissue hypoperfusion and anaerobic metabolism, marking critical impairment of oxygen delivery.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":153}],"confusable_with":"2 mmol/L (screening threshold for elevated lactate)"},
  {"id":"shock-class-path-2","topic":T,"domain":D,"discipline":DI,
   "stem":"What are the four major categories of shock and which is caused by distributive vasodilation?",
   "answer":"Hypovolemic, cardiogenic, obstructive, and distributive; septic shock is the prototypical distributive shock (low SVR, high CO).",
   "rationale":"Distributive shock results from pathological vasodilation and maldistribution of blood flow rather than volume or pump failure.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":153}],"confusable_with":"Hypovolemic shock"},
  {"id":"shock-class-path-3","topic":T,"domain":D,"discipline":DI,
   "stem":"In damage-control resuscitation for hemorrhagic shock, what strategy replaces traditional large-volume crystalloid resuscitation?",
   "answer":"Early hemostatic products (pRBCs, plasma, platelets in balanced ratio) with permissive hypotension; minimize crystalloid.",
   "rationale":"Crystalloid dilutes clotting factors and worsens the lethal triad (coagulopathy, hypothermia, acidosis); hemostatic resuscitation addresses coagulopathy directly.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":801}],"confusable_with":"Aggressive crystalloid resuscitation"},
  {"id":"shock-class-path-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Why is gastric acid suppression with ranitidine now disfavored for stress ulcer prophylaxis in the ICU?",
   "answer":"More lives may be lost from hospital-acquired pneumonia than saved from GI bleeding, because acid suppression promotes bacterial overgrowth and aspiration risk.",
   "rationale":"Loss of gastric acid barrier allows colonization of stomach with gram-negative bacteria; aspiration of colonized contents carries higher mortality than most stress ulcer bleeds.",
   "bloom":"analyze","source":[{"book":"Marino ICU Book","page":45}],"confusable_with":"Proton pump inhibitor risk"},
  {"id":"shock-class-path-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In the reversible causes of cardiac arrest (Hs and Ts), what obstructive cause presents with sudden hypotension and rising peak airway pressure under positive-pressure ventilation?",
   "answer":"Tension pneumothorax.",
   "rationale":"Tension pneumothorax causes obstructive shock by compressing the heart and great vessels; the trapped air also elevates intrathoracic and peak airway pressure.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":843}],"confusable_with":"Cardiac tamponade"}
]

# ── 2: Sodium & Osmolality Disorders in Neurocritical Care ───────────────────
T = "Sodium & Osmolality Disorders in Neurocritical Care"
D = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
kps += [
  {"id":"sodium-osm-neuro-1","topic":T,"domain":D,"discipline":DI,
   "stem":"How is the sodium deficit calculated when using hypertonic saline for rapid correction of symptomatic hyponatremia?",
   "answer":"Na+ deficit (mEq) = Normal TBW x (Desired [Na+] - Current [Na+]).",
   "rationale":"Total body water is the volume of distribution for sodium; the formula quantifies the mEq needed to raise serum sodium to target.",
   "bloom":"apply","source":[{"book":"Marino ICU Book","page":442}],"confusable_with":"Free water deficit formula (used in hypernatremia)"},
  {"id":"sodium-osm-neuro-2","topic":T,"domain":D,"discipline":DI,
   "stem":"In isovolemic hyponatremia, what is the principal disorder to consider?",
   "answer":"SIADH (syndrome of inappropriate antidiuretic hormone secretion).",
   "rationale":"SIADH causes euvolemic hyponatremia by ADH-driven free water retention without sodium deficit, distinguishing it from hypervolemic and hypovolemic causes.",
   "bloom":"recall","source":[{"book":"Marino ICU Book","page":439}],"confusable_with":"Cerebral salt wasting (hypovolemic hyponatremia)"},
  {"id":"sodium-osm-neuro-3","topic":T,"domain":D,"discipline":DI,
   "stem":"What urine sodium level distinguishes cerebral salt wasting from SIADH in a hyponatremic neurocritical care patient?",
   "answer":"Both have urine sodium >20 mEq/L; differentiation requires volume status assessment (CSW = hypovolemic, SIADH = euvolemic).",
   "rationale":"Urine sodium alone cannot distinguish CSW from SIADH; volume status (clinical exam, CVP, fluid responsiveness) is the discriminating factor.",
   "bloom":"analyze","source":[{"book":"Marino ICU Book","page":439}],"confusable_with":"SIADH"},
  {"id":"sodium-osm-neuro-4","topic":T,"domain":D,"discipline":DI,
   "stem":"What symptoms can symptomatic hyponatremia produce, and at what serum sodium level is urgent correction warranted?",
   "answer":"AMS, headache, nausea/vomiting, weakness, seizures; urgent correction warranted with severe neurological symptoms regardless of absolute sodium value.",
   "rationale":"Cerebral edema from hypo-osmolality causes neurological symptoms; severity guides urgency, not only the absolute sodium number.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":107}],"confusable_with":""},
  {"id":"sodium-osm-neuro-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What prerenal caveat limits using urine sodium as the sole marker for oliguria differentiation in the ICU?",
   "answer":"Prerenal conditions can be associated with obligatory sodium loss causing urine sodium >40 mEq/L, overlapping with intrinsic renal disorders.",
   "rationale":"Loop diuretics or renal tubular defects can produce high urine sodium despite prerenal physiology, making urine sodium an unreliable sole discriminator.",
   "bloom":"analyze","source":[{"book":"Marino ICU Book","page":411}],"confusable_with":"Intrinsic renal disorder"}
]

# ── 3: Specific congenital heart lesions ─────────────────────────────────────
T = "Specific congenital heart lesions"
D = "Pediatric anesthesia (neonatal & pediatric physiology, pediatric airway, congenital conditions, fluid & glucose management, emergence, common procedures)"
kps += [
  {"id":"congenital-heart-1","topic":T,"domain":D,"discipline":DI,
   "stem":"For anesthetic management, congenital heart defects are divided into what three functional categories?",
   "answer":"Obstructive lesions, predominantly left-to-right shunts, and predominantly right-to-left shunts.",
   "rationale":"This classification drives anesthetic goals: obstructive lesions require avoiding tachycardia/increased afterload; shunt direction determines how to manipulate PVR vs SVR.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":684}],"confusable_with":""},
  {"id":"congenital-heart-2","topic":T,"domain":D,"discipline":DI,
   "stem":"In Tetralogy of Fallot, what is the physiological consequence of the combination of right ventricular outflow obstruction with a VSD?",
   "answer":"Right-to-left shunting of deoxygenated right ventricular blood into the aorta, causing cyanosis.",
   "rationale":"The RVOT obstruction raises RV pressure above LV pressure, forcing deoxygenated blood rightward through the VSD into the systemic circulation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":690}],"confusable_with":"Left-to-right VSD shunting"},
  {"id":"congenital-heart-3","topic":T,"domain":D,"discipline":DI,
   "stem":"What systemic ventricular ejection fraction threshold places a patient with congenital heart disease at highest perioperative risk?",
   "answer":"EF less than 35% (severe systemic ventricular dysfunction).",
   "rationale":"Severely reduced ventricular function limits cardiac reserve, increasing susceptibility to decompensation from anesthetic-induced myocardial depression.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":685}],"confusable_with":"EF <50% (moderate dysfunction)"},
  {"id":"congenital-heart-4","topic":T,"domain":D,"discipline":DI,
   "stem":"In large left-to-right shunts, what pulmonary consequence develops as a result of increased pulmonary blood flow?",
   "answer":"Pulmonary vascular congestion, increased extravascular lung water, decreased lung compliance, impaired gas exchange.",
   "rationale":"Chronic high pulmonary flow causes endothelial damage and eventual pulmonary hypertension (Eisenmenger physiology), while acutely increasing work of breathing.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":687}],"confusable_with":"Right-to-left shunt physiology"},
  {"id":"congenital-heart-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Because magnesium potentiates nondepolarizing neuromuscular blockers, what monitoring adjustment is required in patients receiving magnesium therapy?",
   "answer":"Reduce NDMB doses and guide all dosing with peripheral nerve stimulator.",
   "rationale":"Magnesium competitively inhibits calcium at the neuromuscular junction, potentiating block and prolonging recovery; standard doses cause profound, prolonged blockade.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1423}],"confusable_with":""},
  {"id":"congenital-heart-script","_type":"illness_script","topic":T,"discipline":DI,
   "enabling_conditions":"Congenital cardiac anatomy (VSD, ASD, TOF, TGA, coarctation); 4 patient groups: post-corrective, post-palliative, pre-surgical, or adult survivors",
   "pathophysiology":"Shunt direction (L→R vs R→L) determines mixing and cyanosis; obstructive lesions increase pressure-work on affected ventricle; pulmonary hypertension from chronic L→R may reverse shunt (Eisenmenger)",
   "time_course":"Congenital; symptoms worsen over years; pulmonary hypertension develops after years of high flow",
   "key_features":"Cyanosis (R→L shunt), pulmonary plethora (L→R shunt), heart failure, arrhythmia, clubbing, polycythemia",
   "consequence_if_missed":"Unrecognized pulmonary hypertension with anesthetic-induced SVR drop → catastrophic R→L shunt reversal; air embolism crosses patent shunt causing stroke"}
]

# ── 4: Spine surgery anesthesia ──────────────────────────────────────────────
T = "Spine surgery anesthesia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"spine-surg-anes-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What patient risk factors predispose to ischemic optic neuropathy (ION) in prone spine surgery?",
   "answer":"Hypertension, large-volume crystalloid use, anemia/hemodilution, increased intraocular or venous pressure from prone position.",
   "rationale":"ION results from reduced optic nerve perfusion; these factors either decrease perfusion pressure or increase venous back-pressure in the orbit.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":373}],"confusable_with":"Central retinal artery occlusion"},
  {"id":"spine-surg-anes-2","topic":T,"domain":D,"discipline":DI,
   "stem":"The double-crush phenomenon in spine patients means that pre-existing peripheral neuropathy increases what perioperative risk?",
   "answer":"Risk of neurological injury after neuraxial anesthesia or analgesia (the double-crush phenomenon makes already-compromised nerves more vulnerable).",
   "rationale":"A nerve already compressed at one level has reduced capacity to tolerate additional ischemia or mechanical injury from neuraxial technique.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":320}],"confusable_with":""},
  {"id":"spine-surg-anes-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Neuraxial ultrasound by experienced practitioners provides what advantage over landmark-based epidural placement?",
   "answer":"Identifies skin-to-dura distance and reduces lumbar epidural block failure rate; improves block efficacy.",
   "rationale":"Real-time or pre-procedure ultrasound visualization of neuraxial anatomy compensates for difficult landmarks (obesity, scoliosis, prior surgery).",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":333}],"confusable_with":""},
  {"id":"spine-surg-anes-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Postdural puncture headache typically begins within what time frame and resolves spontaneously by when?",
   "answer":"Begins within 3 days (two-thirds within 48 hours); spontaneous resolution usually within 7 days.",
   "rationale":"PDPH results from CSF leak through the dural defect, causing traction on pain-sensitive intracranial structures; most resolve as the dural hole seals.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"Meningitis headache (does not resolve spontaneously in days)"},
  {"id":"spine-surg-anes-5","topic":T,"domain":D,"discipline":DI,
   "stem":"An epidural catheter is described as flexible, calibrated, radiopaque plastic with either a single end hole or multiple side orifices. What is the clinical significance of multiple side orifices?",
   "answer":"Multiple orifices distribute local anesthetic more evenly and reduce the risk of catheter obstruction causing incomplete block.",
   "rationale":"A single end-hole catheter can abut dura or neural tissue; multiple side orifices allow flow even if the tip is occluded.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":331}],"confusable_with":""}
]

print(f"Topics 0-4 drafted: {len(kps)} KPs")
