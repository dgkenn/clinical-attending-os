import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 14: Total hip and total knee arthroplasty (THA/TKA) anesthesia ───────────
T = "Total hip and total knee arthroplasty (THA/TKA) anesthesia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"tka-tha-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the incidence of hip dislocation after primary versus revision total hip arthroplasty, and what precaution does this require?",
   "answer":"3% after primary THA; 20% after revision; hip implant patients require special positioning precautions during subsequent procedures.",
   "rationale":"Prosthetic hips dislocate with less force than native hips; extreme range of motion maneuvers during repositioning can dislodge the prosthesis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1309}],"confusable_with":""},
  {"id":"tka-tha-2","topic":T,"domain":D,"discipline":DI,
   "stem":"For ambulatory knee arthroscopy, what disadvantage does neuraxial anesthesia have compared with general anesthesia?",
   "answer":"Prolonged time to discharge following neuraxial anesthesia compared with general anesthesia for ambulatory procedures.",
   "rationale":"Neuraxial block regression requires time; motor block must resolve before ambulation and discharge criteria are met, prolonging PACU stay.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1310}],"confusable_with":""},
  {"id":"tka-tha-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Bone cement implantation syndrome (BCIS) is a recognized complication of joint arthroplasty; what is its clinical presentation?",
   "answer":"Sudden hypotension, hypoxia, cardiac arrhythmia, and cardiac arrest following cement introduction into the medullary canal.",
   "rationale":"Pressurized methylmethacrylate monomer and fat/air embolism from the medullary canal causes acute pulmonary vasoconstriction and right heart strain.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1318}],"confusable_with":"Fat embolism syndrome"},
  {"id":"tka-tha-4","topic":T,"domain":D,"discipline":DI,
   "stem":"For Jehovah's Witness patients undergoing THA, what anesthetic technique can facilitate blood conservation?",
   "answer":"Epidural catheter allows regional anesthesia and analgesia; combined with controlled hypotension and cell salvage, reduces allogeneic transfusion need.",
   "rationale":"Controlled hypotension via epidural reduces intraoperative blood loss; regional anesthesia also reduces postoperative DVT risk in these patients.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1317}],"confusable_with":""},
  {"id":"tka-tha-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Systemic absorption from the tourniquet release during lower extremity surgery can cause hypotension via what mechanism?",
   "answer":"Washout of ischemic metabolites (lactate, CO2, potassium) and reactive hyperemia causing sudden decrease in SVR.",
   "rationale":"Tourniquet deflation releases vasoactive metabolites accumulated in the ischemic limb into the systemic circulation, causing vasodilation and transient hypotension.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1597}],"confusable_with":""}
]

# ── 15: Tracheal resection and reconstruction ─────────────────────────────────
T = "Tracheal resection and reconstruction"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"tracheal-resect-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Why is little premedication given to patients presenting for tracheal resection?",
   "answer":"Most patients have moderate-to-severe airway obstruction; sedation may precipitate complete obstruction by reducing muscle tone and respiratory drive.",
   "rationale":"The already-narrowed tracheal lumen leaves minimal reserve; even mild sedation-induced relaxation of airway muscles can cause acute obstruction.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":920}],"confusable_with":""},
  {"id":"tracheal-resect-2","topic":T,"domain":D,"discipline":DI,
   "stem":"During tracheal resection, high-frequency jet ventilation allows what surgical maneuver that standard ventilation cannot?",
   "answer":"Ventilation can continue without interruption during resection and anastomosis; the catheter is advanced distally by the surgeon while jet ventilation maintains oxygenation.",
   "rationale":"HFJV delivers small tidal volumes at high frequency through a narrow catheter, avoiding the need to cross-clamp the airway for anastomosis.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":922}],"confusable_with":""},
  {"id":"tracheal-resect-3","topic":T,"domain":D,"discipline":DI,
   "stem":"For patients with superior vena cava syndrome undergoing mediastinal surgery, why should an IV catheter be placed in a lower extremity?",
   "answer":"Venous drainage from the upper body is unreliable (obstructed by SVC compression); lower extremity IV ensures reliable drug delivery.",
   "rationale":"SVC obstruction impairs upper-body venous return; medications injected into arm or hand veins may not reach the heart reliably.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":931}],"confusable_with":""},
  {"id":"tracheal-resect-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Awake intubation with an armored tracheal tube is preferred for tracheal resection in cooperative patients for what reason?",
   "answer":"Maintains airway patency and spontaneous ventilation; armored tube resists kinking around surgical manipulation of the trachea.",
   "rationale":"Preserving consciousness and spontaneous breathing prevents the catastrophic loss of airway that could occur with an already-obstructed trachea under general anesthesia.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":931}],"confusable_with":""},
  {"id":"tracheal-resect-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What principal advantages do double-lumen bronchial tubes provide for thoracic surgery?",
   "answer":"Ease of placement, ability to ventilate one or both lungs independently, and ability to suction either lung.",
   "rationale":"Lung isolation enables one-lung ventilation for surgical access while maintaining the option to reinflate the operative lung if needed.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":895}],"confusable_with":"Bronchial blocker (cannot suction non-ventilated lung)"}
]

# ── 16: Tracheal stenosis and tracheomalacia ──────────────────────────────────
T = "Tracheal stenosis and tracheomalacia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"tracheal-sten-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the most common cause of acquired tracheal stenosis?",
   "answer":"Prolonged tracheal intubation and tracheostomy (tube-related tracheal stenosis); also caused by penetrating or blunt trauma.",
   "rationale":"Cuff-related ischemia at the tracheal wall causes mucosal necrosis, granulation, and fibrotic stricture; high-volume low-pressure cuffs reduce but do not eliminate this risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":918}],"confusable_with":"Extrinsic compression (thyroid goiter, tumor)"},
  {"id":"tracheal-sten-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Laryngoscopy and intubation can lead to a range of complications from minor to severe; what is the most severe tracheal complication of prolonged intubation?",
   "answer":"Tracheal stenosis (glottic, subglottic, or tracheal).",
   "rationale":"Progressive ischemic injury to the tracheal mucosa causes granulation tissue and circumferential fibrosis narrowing the lumen over weeks to months.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":544}],"confusable_with":"Vocal cord granuloma (less severe, more common)"},
  {"id":"tracheal-sten-3","topic":T,"domain":D,"discipline":DI,
   "stem":"For critically ill patients requiring prolonged ventilation, what is the recommended maximum duration for orotracheal or nasotracheal intubation before tracheostomy should be considered?",
   "answer":"2-3 weeks is generally considered safe for both orotracheal and nasotracheal intubation before mucosal injury risk favors tracheostomy.",
   "rationale":"Beyond 2-3 weeks, cumulative cuff-related and tube-related mucosal injury substantially increases risk of subglottic stenosis and other complications.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2192}],"confusable_with":""},
  {"id":"tracheal-sten-4","topic":T,"domain":D,"discipline":DI,
   "stem":"In a patient with tracheal stenosis due to external compression (e.g., thyroid mass, papilloma), what specific airway question must be answered preoperatively?",
   "answer":"Whether positive-pressure ventilation is feasible and what the anesthetic plan is if mask ventilation fails.",
   "rationale":"Extrinsic compression may worsen under anesthesia-induced muscle relaxation; pre-planning for awake intubation or surgical airway is essential.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1270}],"confusable_with":""},
  {"id":"tracheal-sten-5","topic":T,"domain":D,"discipline":DI,
   "stem":"High-pressure low-volume ETT cuffs are associated with what tracheal complication compared to low-pressure high-volume cuffs?",
   "answer":"More ischemic damage to tracheal mucosa; less suitable for intubations of long duration.",
   "rationale":"High-pressure cuffs exert focal ischemic pressure on the tracheal wall; low-pressure cuffs distribute pressure over a larger area, reducing mucosal injury.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":516}],"confusable_with":""}
]

# ── 17: Tracheobronchomalacia and dynamic airway collapse ─────────────────────
T = "Tracheobronchomalacia and dynamic airway collapse"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"tbm-collapse-1","topic":T,"domain":D,"discipline":DI,
   "stem":"At low lung volumes, what happens to airway resistance and why is PEEP beneficial in dynamic airway collapse?",
   "answer":"Airway resistance becomes inversely proportional to lung volume (increases as volume falls); increasing lung volume to normal with PEEP restores radial traction and reduces resistance.",
   "rationale":"Positive airway pressure acts as a pneumatic splint, maintaining airway patency by recreating the radial traction that lung parenchyma normally exerts on airway walls.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":811}],"confusable_with":""},
  {"id":"tbm-collapse-2","topic":T,"domain":D,"discipline":DI,
   "stem":"During forced exhalation from various lung volumes, what phenomenon makes terminal expiratory flows effort-independent?",
   "answer":"Dynamic airway compression at the equal pressure point; regardless of effort or initial lung volume, expiratory flows plateau at a maximum (effort-independent) value.",
   "rationale":"When pleural pressure exceeds airway pressure at some point along the airway, further effort compresses the airway and limits flow; this is the physiologic basis of flow-volume curves.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":814}],"confusable_with":""},
  {"id":"tbm-collapse-3","topic":T,"domain":D,"discipline":DI,
   "stem":"In patients with tracheobronchomalacia, what intraoperative ventilation strategy prevents expiratory airway collapse?",
   "answer":"Apply PEEP to maintain positive airway pressure throughout the respiratory cycle, acting as an internal pneumatic stent.",
   "rationale":"TBM causes the softened airway to collapse during expiration when transmural pressure is negative; PEEP prevents this collapse by maintaining positive intraluminal pressure.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":811}],"confusable_with":""},
  {"id":"tbm-collapse-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Loss of proprioception from the chest wall in lateral or lithotomy positions accentuates what symptom in awake patients with compromised respiratory muscles?",
   "answer":"Dyspnea, from impaired sensory feedback and inability to compensate for position-related reductions in FRC.",
   "rationale":"Normal chest wall proprioception assists in regulating respiratory effort; loss in abnormal positions worsens perception of breathlessness in already-compromised patients.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":873}],"confusable_with":""},
  {"id":"tbm-collapse-5","topic":T,"domain":D,"discipline":DI,
   "stem":"In a patient with known bullous emphysema on positive-pressure ventilation, what intraoperative complication from the bulla must be anticipated?",
   "answer":"Bulla expansion under positive pressure leading to rupture, tension pneumothorax, or bronchopleural fistula.",
   "rationale":"Bullae have poor communication with the rest of the lung, causing preferential air trapping with each positive-pressure breath until rupture.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":505}],"confusable_with":""}
]

print(f"Topics 14-17 drafted: {len(kps)} KPs")
