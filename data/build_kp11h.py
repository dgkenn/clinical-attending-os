import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []
DI = "anesthesia"

# ── 27: Vascular access and hybrid procedure anesthesia ──────────────────────
T = "Vascular access and hybrid procedure anesthesia"
D = "Subspecialty & out-of-OR anesthesia (ENT/shared airway, ophthalmology, orthopedics, transplant, vascular, ambulatory/office, non-operating-room anesthesia, robotic, laser)"
kps += [
  {"id":"vasc-hybrid-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the primary concern for detecting venous cannulation during central line placement, and why is blood color/pulsatility unreliable?",
   "answer":"Color and pulsatility can be misleading; more than one confirmation method (ultrasound, pressure transduction, manometer) must be used to verify venous vs. arterial placement.",
   "rationale":"High venous pressure in volume-overloaded or obstructed patients can simulate arterial pulsatility; inadvertent arterial cannulation causes serious complications.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":155}],"confusable_with":""},
  {"id":"vasc-hybrid-2","topic":T,"domain":D,"discipline":DI,
   "stem":"For arteriovenous malformations (AVMs) presenting at ages 10-30, what unusual hemodynamic complication can high-flow low-resistance AVMs rarely cause?",
   "answer":"High-output cardiac failure (from arteriovenous shunting of large blood volumes).",
   "rationale":"Large AVMs function as significant systemic arteriovenous fistulas; the continuous shunting imposes a chronic volume overload on the heart causing high-output failure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":989}],"confusable_with":""},
  {"id":"vasc-hybrid-3","topic":T,"domain":D,"discipline":DI,
   "stem":"Patients are placed in Trendelenburg position during internal jugular venous cannulation for what purpose?",
   "answer":"To decrease the risk of air embolism during venous cannulation (by increasing venous pressure above atmospheric).",
   "rationale":"Trendelenburg raises CVP above atmospheric pressure, preventing air entrainment through the needle or catheter if the vein is opened to atmosphere.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":153}],"confusable_with":""},
  {"id":"vasc-hybrid-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Patients with constrictive pericarditis show a prominent y descent on the CVP waveform. How does this differ from cardiac tamponade?",
   "answer":"Constrictive pericarditis: prominent y descent, JVD preserved with deep inspiration (Kussmaul sign), no pulsus paradoxus; tamponade: blunted/absent y descent, pulsus paradoxus present.",
   "rationale":"In constrictive pericarditis, early diastolic filling is rapid (prominent y) but then abruptly stops; tamponade impairs filling throughout diastole, blunting the y descent.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":772}],"confusable_with":"Cardiac tamponade"},
  {"id":"vasc-hybrid-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Anesthesia requirements for interventional radiology (IR) procedures vary greatly; what characterizes most minimally invasive IR procedures from an anesthetic standpoint?",
   "answer":"Many procedures can be performed with minimal sedation or monitored anesthesia care (MAC) due to their minimally invasive nature; general anesthesia reserved for complex or prolonged cases.",
   "rationale":"The minimally invasive access (catheter-based) causes limited tissue trauma; patient cooperation and immobility are usually achievable with moderate sedation.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":709}],"confusable_with":""}
]

# ── 28: Vasoactive and Inotropic Drug Pharmacology ────────────────────────────
T = "Vasoactive and Inotropic Drug Pharmacology"
D = "Anesthesia critical care (shock & resuscitation, sepsis, ARDS & mechanical ventilation, hemodynamic monitoring, AKI, sedation/delirium, nutrition, end-of-life)"
kps += [
  {"id":"vasoinotrope-1","topic":T,"domain":D,"discipline":DI,
   "stem":"Target-controlled infusion (TCI) employs software and hardware to achieve what specific pharmacokinetic target?",
   "answer":"A set drug concentration at the effect site, based on pharmacokinetic models; widely available outside North America for propofol and remifentanil.",
   "rationale":"TCI automatically adjusts infusion rate to maintain a chosen plasma or effect-site concentration, reducing the need for manual titration and improving hemodynamic stability.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":"TIVA without TCI (weight-based fixed infusion rates)"},
  {"id":"vasoinotrope-2","topic":T,"domain":D,"discipline":DI,
   "stem":"The combination of opioids and benzodiazepines markedly reduces what two hemodynamic parameters through synergistic interaction?",
   "answer":"Arterial blood pressure and peripheral vascular resistance (SVR).",
   "rationale":"Opioids reduce sympathetic tone and benzodiazepines blunt autonomic responses; the combination produces synergistic vasodilation exceeding the effect of either drug alone.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
  {"id":"vasoinotrope-3","topic":T,"domain":D,"discipline":DI,
   "stem":"The principal pharmacodynamic change of aging relevant to vasoactive drug dosing is what?",
   "answer":"Reduced anesthetic requirement (reduced MAC); older adults display lower dose requirements for propofol and etomidate.",
   "rationale":"Age-related reductions in neuronal density, neurotransmitter function, and end-organ sensitivity mean standard adult doses produce exaggerated hemodynamic effects in elderly patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1490}],"confusable_with":""},
  {"id":"vasoinotrope-4","topic":T,"domain":D,"discipline":DI,
   "stem":"Antiparkinsonian drugs and tricyclic antidepressants have anticholinergic side effects that augment what premedication-related effect?",
   "answer":"The sedation produced by scopolamine (anticholinergic premedication).",
   "rationale":"Additive anticholinergic effects from concurrent medications and scopolamine can cause excessive sedation, confusion, and urinary retention, particularly in elderly patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":352}],"confusable_with":""},
  {"id":"vasoinotrope-5","topic":T,"domain":D,"discipline":DI,
   "stem":"During cardiac surgery with CPB, what opioid infusion strategy is used when target-controlled infusion of remifentanil is selected?",
   "answer":"Remifentanil 0-1 mcg/kg bolus followed by 0.25-1 mcg/kg/min infusion during cardiac surgery.",
   "rationale":"Remifentanil's ultra-short context-sensitive half-time allows rapid titration and offset after bypass, facilitating early extubation in fast-track cardiac protocols.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":"Sufentanil (longer acting, used for high-dose opioid technique)"}
]

# ── 29: Venous Air Embolism (VAE): Pathophysiology & Detection ────────────────
T = "Venous Air Embolism (VAE): Pathophysiology & Detection"
D = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
kps += [
  {"id":"vae-detect-1","topic":T,"domain":D,"discipline":DI,
   "stem":"What is the earliest monitor to detect venous air embolism before overt clinical signs appear?",
   "answer":"Precordial Doppler (most sensitive) or transesophageal echocardiography; end-tidal CO2 decreases are an early but less specific sign.",
   "rationale":"Doppler detects air bubbles acoustically before they cause hemodynamic compromise; TEE visualizes air directly in the right heart; EtCO2 drop reflects increased dead space.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":"Blood pressure changes and mill-wheel murmur (late signs)"},
  {"id":"vae-detect-2","topic":T,"domain":D,"discipline":DI,
   "stem":"Venous air embolism causes a sudden decrease in end-tidal CO2 through what mechanism?",
   "answer":"Increase in pulmonary dead space; air blocks pulmonary capillary perfusion, creating unperfused (dead space) alveoli that dilute exhaled CO2.",
   "rationale":"Alveoli supplied with air-blocked vessels continue ventilating but not perfusing; the unmixed alveolar gas lowers the mixed exhaled CO2 concentration.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":194}],"confusable_with":"Decreased EtCO2 from hyperventilation (no change in dead space)"},
  {"id":"vae-detect-3","topic":T,"domain":D,"discipline":DI,
   "stem":"A reappearance or increase of nitrogen in expired gases during monitoring signals what complication?",
   "answer":"Venous air embolism (nitrogen in expired gas comes from entrained atmospheric air).",
   "rationale":"Atmospheric air is 78% nitrogen; entrained air reaching the pulmonary circulation produces measurable exhaled nitrogen detectable by mass spectrometry.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},
  {"id":"vae-detect-4","topic":T,"domain":D,"discipline":DI,
   "stem":"A mill-wheel murmur heard during cardiac auscultation in a neurosurgical patient represents what clinical finding, and at what stage of VAE does it appear?",
   "answer":"A churning sound from air mixing with blood in the right heart; it is a late manifestation of VAE, appearing after significant air has accumulated.",
   "rationale":"The mill-wheel murmur requires a large air bolus to produce turbulent mixing in the cardiac chambers; by the time it appears, hemodynamic compromise is usually already present.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},
  {"id":"vae-detect-5","topic":T,"domain":D,"discipline":DI,
   "stem":"Nitrous oxide is 35 times more soluble than nitrogen; why is this relevant when VAE occurs under nitrous oxide anesthesia?",
   "answer":"N2O rapidly diffuses into an air embolus, expanding its volume and potentially converting a small clinically insignificant embolus into a life-threatening one.",
   "rationale":"N2O's high blood:gas solubility allows it to enter and expand gas bubbles; discontinuing N2O is an essential first step when VAE is suspected.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":260}],"confusable_with":""}
]

print(f"Topics 27-29 drafted: {len(kps)} KPs")
