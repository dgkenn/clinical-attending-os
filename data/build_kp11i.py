import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 30: Venous Air Embolism: Treatment ───────────────────────────────────────
T = "Venous Air Embolism: Treatment"
D = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
kps += [
  {"id":"vae-treat-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the immediate treatment sequence when venous air embolism is confirmed during neurosurgery?",
   "answer":"Flood the surgical field with saline/compress wound, discontinue N2O, notify surgeon to occlude entry site, administer 100% O2, aspirate air via central venous catheter (right atrial position), left lateral Trendelenburg position.",
   "rationale":"Occluding the entry site stops further air entrainment; discontinuing N2O prevents embolus expansion; aspiration removes accumulated air; Durant's maneuver (left lateral decubitus) displaces air from RV outflow tract.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},
  {"id":"vae-treat-2","topic":T,"domain":D,"discipline":DI,
   "stem":"For which patient population undergoing pulmonary embolectomy does positive-pressure ventilation pose a specific hemodynamic risk?",
   "answer":"Critically ill patients with massive PE; they tolerate positive-pressure ventilation poorly because it increases RV afterload in an already-failing right ventricle.",
   "rationale":"PPV raises intrathoracic pressure, reducing venous return and increasing RV afterload; in RV failure from PE, this can precipitate cardiac arrest.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":880}],"confusable_with":""},
  {"id":"vae-treat-3","topic":T,"domain":D,"discipline":DI,
   "stem":"What does a sudden decrease in EtCO2 with hemodynamic instability in the sitting position during neurosurgery indicate, and what is the first response?",
   "answer":"Venous air embolism; first response is to immediately notify surgeon to flood the field/compress wound and discontinue nitrous oxide.",
   "rationale":"EtCO2 drop from dead space increase combined with hemodynamic compromise confirms significant VAE; rapid cessation of air entry and N2O elimination are the highest-priority interventions.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":"Pulmonary thromboembolism (also drops EtCO2 but more gradual, no surgical field relationship)"},
  {"id":"vae-treat-4","topic":T,"domain":D,"discipline":DI,
   "stem":"A patient undergoing amniotic fluid embolism has sudden tachypnea, cyanosis, shock, and generalized bleeding. What three major pathophysiological events explain this presentation?",
   "answer":"Acute pulmonary hypertension/RV failure, left heart failure, and disseminated intravascular coagulation (DIC).",
   "rationale":"Amniotic fluid components trigger mechanical obstruction, anaphylaxis-like mediator release causing pulmonary vasoconstriction, cardiac depression, and activation of the coagulation cascade.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1424}],"confusable_with":"Venous air embolism (no DIC component)"},
  {"id":"vae-treat-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Inotropic support is usually required for patients presenting for emergency pulmonary embolectomy. What hemodynamic pattern drives this need?",
   "answer":"Massive PE causes acute RV pressure overload and RV failure; RV dilation compresses the LV (interventricular interdependence) causing low CO.",
   "rationale":"The suddenly increased afterload from the embolus causes RV dilation and dysfunction; inotropes (dobutamine, norepinephrine) support RV output until surgical embolus removal.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":880}],"confusable_with":""}
]

# ── 31: Ventilation Modes in Anesthesia ──────────────────────────────────────
T = "Ventilation Modes in Anesthesia"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"vent-modes-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Volume-cycled ventilators terminate inspiration when what condition is met, and what secondary safety limit is often also included?",
   "answer":"Terminate when a preselected tidal volume is delivered; secondary pressure limit prevents dangerously high inflation pressures.",
   "rationale":"Volume cycling guarantees tidal volume delivery but may generate excessive pressures in stiff lungs; the secondary pressure limit acts as a safety cutoff to prevent barotrauma.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2181}],"confusable_with":"Pressure-cycled ventilator (terminates at preset pressure, not volume)"},
  {"id":"vent-modes-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Pressure-controlled ventilation (PCV) uses a constant preselected pressure; how does the ventilatory pattern differ from volume-controlled ventilation?",
   "answer":"PCV delivers a decelerating flow pattern with a constant inspiratory pressure; tidal volume varies with lung compliance and resistance. Ventilation is completely controlled by the ventilator with no patient interaction.",
   "rationale":"Constant pressure generation results in high initial flow that decelerates as airway pressure equilibrates; this improves gas distribution but makes VT patient-dependent.",
   "bloom":"analyze","source":[{"book":"Marino ICU Book","page":322}],"confusable_with":"Volume-controlled ventilation (constant flow, pressure varies)"},
  {"id":"vent-modes-3","topic":T,"domain":D,"discipline":DI,
   "stem":"IMV (intermittent mandatory ventilation) machine mandatory breaths provide backup ventilation, and a low level of pressure support is added for what purpose?",
   "answer":"To offset the increased work of breathing from breathing through the ETT, circuit resistance, and machine during spontaneous breaths.",
   "rationale":"Without pressure support, patients must generate enough effort to overcome both elastic (lung/chest wall) and resistive (ETT/circuit) work; a small PSV level offsets the resistive component.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2188}],"confusable_with":""},
  {"id":"vent-modes-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Modern anesthesia machine ventilators incorporate microprocessor controls and pressure/flow sensors to achieve what clinical capabilities beyond traditional volume delivery?",
   "answer":"Multiple ventilatory modes, PEEP delivery, accurate tidal volumes, and enhanced safety features.",
   "rationale":"Electronic control of gas flow allows precise breath timing, flow shaping, and PEEP valve actuation; microprocessors enable adaptive modes unavailable in pneumatically-only ventilators.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":118}],"confusable_with":""},
  {"id":"vent-modes-5","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the pathological distinction between barotrauma and volutrauma in mechanically ventilated patients?",
   "answer":"Barotrauma is related to high repetitive peak inflation pressures; volutrauma is related to repetitive collapse and reexpansion of alveoli (cyclic atelectrauma).",
   "rationale":"Both share the mechanism of stretch injury to alveolar epithelium and endothelium but differ in the driving force: pressure vs. volume cycling of recruitable lung units.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2179}],"confusable_with":""}
]

# ── 32: Ventilator Asynchrony and Patient-Ventilator Interaction ─────────────
T = "Ventilator Asynchrony and Patient-Ventilator Interaction"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"vent-asynch-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Continuous sedation in ICU patients is used to reduce patient-ventilator asynchrony through what mechanism?",
   "answer":"Reduces patient respiratory drive and suppresses the spontaneous breathing efforts that conflict with ventilator-delivered breaths.",
   "rationale":"Patient-ventilator asynchrony occurs when the patient's respiratory timing or effort does not match the ventilator's programmed pattern; sedation reduces the patient's competing respiratory drive.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   ICU Sedation","page":1}],"confusable_with":""},
  {"id":"vent-asynch-2","topic":T,"domain":D,"discipline":DI,
   "stem":"NIV (non-invasive ventilation) can cause unrecognized patient-ventilator asynchrony due to what NIV-specific problem?",
   "answer":"Interface leaks: air leak around the mask is misread by the ventilator as patient expiratory flow, causing trigger failure and cycle asynchrony.",
   "rationale":"NIV ventilators must compensate for intentional and unintentional leaks; large leaks disrupt pressure and flow sensing, causing the ventilator to deliver poorly-timed breaths.",
   "bloom":"analyze","source":[{"book":"Society Guideline","page":36}],"confusable_with":""},
  {"id":"vent-asynch-3","topic":T,"domain":D,"discipline":DI,
   "stem":"In pressure-controlled ventilation (PCV), there is no patient interaction with the ventilator. What does this mean for patients with intermittent spontaneous respiratory effort?",
   "answer":"PCV behaves like controlled mandatory ventilation; spontaneous patient efforts do not trigger additional breaths or modify the delivered breath, potentially causing patient-ventilator asynchrony and discomfort.",
   "rationale":"Unlike PSV or SIMV, pure PCV does not synchronize to patient effort; the patient's spontaneous drive competes with the fixed machine-controlled pattern.",
   "bloom":"analyze","source":[{"book":"Marino ICU Book","page":322}],"confusable_with":"Pressure support ventilation (patient-triggered, fully synchronous)"},
  {"id":"vent-asynch-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Before delivering anesthesia, the anesthesia time-out (Item 15 of the PAC) requires confirmation of what?",
   "answer":"Ventilator settings and readiness to deliver anesthesia care.",
   "rationale":"A final check of ventilator settings (tidal volume, rate, FiO2, PEEP) immediately before induction prevents incorrect setup from causing intraoperative hypoxia or barotrauma.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":276}],"confusable_with":""},
  {"id":"vent-asynch-5","topic":T,"domain":D,"discipline":DI,
   "stem":"NIV complications include gastric insufflation, facial skin breakdown, and excessively high tidal volumes. What specific lung injury risk does NIV generate that is often underrecognized?",
   "answer":"Excessively high tidal volumes from high pressure support can cause patient self-inflicted lung injury (P-SILI), worsening ARDS.",
   "rationale":"A strong patient inspiratory effort combined with high NIV support generates large uncontrolled tidal volumes; in ARDS this causes volutrauma equivalent to injurious mechanical ventilation.",
   "bloom":"analyze","source":[{"book":"Society Guideline","page":36}],"confusable_with":""}
]

print(f"Topics 30-32 drafted: {len(kps)} KPs")
