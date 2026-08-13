import json, sys
sys.stdout.reconfigure(encoding='utf-8')

kps = []

# ── Topic 11: Spinal anesthesia for cesarean delivery ────────────────────────
kps += [
  {"id":"spinal-for-cesarean-1","topic":"Spinal anesthesia for cesarean delivery","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"What sensory level is required for cesarean delivery under spinal anesthesia, and how is a patchy block before delivery treated?",
   "answer":"T4 sensory level is required for cesarean delivery; patchy anesthesia before delivery can be treated with IV ketamine 10-20 mg plus midazolam 1-2 mg, or 30% nitrous oxide.",
   "rationale":"Peritoneal manipulation requires a T4 dermatomal block; subanesthetic ketamine provides dissociative analgesia and amnesia to bridge patchy regional coverage.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1406}],"confusable_with":"Epidural top-up (adds local anesthetic in increments; spinal is single-shot so ketamine bridges gaps)"},
  {"id":"spinal-for-cesarean-2","topic":"Spinal anesthesia for cesarean delivery","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"What are absolute contraindications to regional anesthesia for cesarean delivery?",
   "answer":"Absolute contraindications: patient refusal, infection at the injection site, and severe coagulopathy (inability to safely place needle).",
   "rationale":"Patient autonomy must be respected; local infection risks introducing pathogens to the epidural or subarachnoid space; coagulopathy risks epidural hematoma formation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1393}],"confusable_with":"Relative contraindications (prior spine surgery, anatomic abnormalities; can still attempt)"},
  {"id":"spinal-for-cesarean-3","topic":"Spinal anesthesia for cesarean delivery","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"What are the indications for emergency (crash) cesarean delivery that require immediate decision-making about anesthetic technique?",
   "answer":"Crash C-section indications: massive bleeding (placenta previa/accreta, abruption, uterine rupture), umbilical cord prolapse, and severe fetal distress requiring immediate delivery.",
   "rationale":"True emergencies (umbilical cord prolapse, fetal bradycardia to <60 bpm) require fastest anesthetic possible; general anesthesia is often preferred unless functional neuraxial catheter is in place.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1412}],"confusable_with":"Urgent C-section (allows time for spinal vs. activating existing epidural)"},
  {"id":"spinal-for-cesarean-4","topic":"Spinal anesthesia for cesarean delivery","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"What are the advantages of spinal versus continuous epidural anesthesia for cesarean delivery?",
   "answer":"Spinal: more rapid and predictable onset, denser block, smaller LA dose with less systemic toxicity risk, simpler technique. Epidural: continued dosing, better level control, option for postoperative analgesia via catheter.",
   "rationale":"Both techniques are safe and effective; the choice depends on urgency, expected duration, and whether postoperative epidural analgesia is desired.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1404}],"confusable_with":""},
  {"id":"spinal-for-cesarean-5","topic":"Spinal anesthesia for cesarean delivery","domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean delivery, obstetric emergencies, neonatal resuscitation)","discipline":"anesthesia",
   "stem":"In combined spinal-epidural (CSE) for cesarean, what does the intrathecal component provide and what does the epidural catheter provide?",
   "answer":"Intrathecal drugs provide essentially immediate pain control with minimal effect on early labor progress; the epidural catheter provides continuing control and ability to extend analgesia for prolonged or unexpected surgery.",
   "rationale":"CSE combines the rapid reliable onset of spinal anesthesia with the flexibility of an epidural catheter for dose titration, top-up, and postoperative analgesia.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1401}],"confusable_with":"Epidural alone (slower onset; no immediate dense block without test dose and incremental dosing)"}
]

# ── Topic 12: Spinal anesthesia pharmacology and block management ─────────────
kps += [
  {"id":"spinal-pharmacology-block-1","topic":"Spinal anesthesia: pharmacology and block management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"After spinal anesthesia, patients may have shivering, agitation, and pain upon emergence. What drug class received via spinal route minimizes these emergence issues?",
   "answer":"Patients receiving spinal opioids have a smoother emergence; conversely, those without adequate analgesia develop problems like pain, agitation, and autonomic lability on emergence.",
   "rationale":"Intrathecal opioids provide postoperative analgesia that persists into the recovery period, reducing the acute pain and sympathetic activation seen with pure local anesthetic spinals.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2098}],"confusable_with":""},
  {"id":"spinal-pharmacology-block-2","topic":"Spinal anesthesia: pharmacology and block management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Spinal anesthesia-induced hypotension may decrease cerebral blood flow in which specific patient population?",
   "answer":"Spinal anesthesia-induced hypotension may decrease cerebral blood flow in older patients and those with preexisting hypertension; however, studies did not demonstrate postoperative cognitive function changes.",
   "rationale":"Hypertensive patients have upward-shifted cerebral autoregulation, making them vulnerable to reduced CBF at MAP levels that maintain CBF in normotensive patients.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":319}],"confusable_with":""},
  {"id":"spinal-pharmacology-block-3","topic":"Spinal anesthesia: pharmacology and block management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Regarding cognitive effects, how do neuraxial and volatile anesthesia compare in the early postoperative period?",
   "answer":"Studies comparing volatile anesthesia with intravenous/neuraxial anesthesia found worse cognitive function with volatile anesthesia within the first week; rates are similar at 3 months.",
   "rationale":"Short-term cognitive effects differ by anesthetic technique and drug but converge over time; neuraxial avoidance of CNS-penetrating volatile agents may reduce early POCD.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":124}],"confusable_with":"Long-term POCD (similar incidence regardless of technique by 3 months)"},
  {"id":"spinal-pharmacology-block-4","topic":"Spinal anesthesia: pharmacology and block management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"A subdural (not epidural, not intrathecal) injection of local anesthetic presents with what characteristic features?",
   "answer":"Subdural block produces extensive but patchy sensory block with relative sparing of motor and sympathetic blockade; onset is slower than expected (up to 30 minutes after injection).",
   "rationale":"The subdural space (between dura and arachnoid) allows drug spread over a wide area; the patchy motor sparing and delayed onset distinguish it from intrathecal or epidural injection.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":339}],"confusable_with":"Total spinal (complete, rapid motor and sensory block; apnea and cardiovascular collapse)"},
  {"id":"spinal-pharmacology-block-5","topic":"Spinal anesthesia: pharmacology and block management","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Chloroprocaine has what unique pharmacokinetic property that makes it preferred for continuous epidural infusions in neonates?",
   "answer":"Chloroprocaine has rapid plasma clearance (ester hydrolysis), making it safe for continuous epidural infusion in neonates and very young infants who have immature hepatic metabolism.",
   "rationale":"Neonates and young infants have low hepatic amide-metabolizing enzyme activity; ester LAs like chloroprocaine depend on plasma pseudocholinesterase, which is present even in neonates.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":178}],"confusable_with":"Bupivacaine (amide; risk of systemic toxicity with continuous infusion in neonates due to immature hepatic clearance)"}
]

# ── Topic 13: Spinal anesthesia technique and setup ──────────────────────────
kps += [
  {"id":"spinal-technique-setup-1","topic":"Spinal anesthesia: technique and setup","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What vasopressor is recommended to treat hypotension during spinal anesthesia, and how is it administered?",
   "answer":"Phenylephrine (IV boluses or infusion) is first-line for spinal anesthesia-induced hypotension; ephedrine is an alternative if bradycardia is also present.",
   "rationale":"Phenylephrine's alpha-1 vasoconstriction restores SVR without increasing heart rate; it is preferred over ephedrine in obstetric patients due to less fetal acidosis.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1384}],"confusable_with":"Ephedrine (mixed alpha/beta; used when bradycardia accompanies hypotension)"},
  {"id":"spinal-technique-setup-2","topic":"Spinal anesthesia: technique and setup","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Epinephrine and phenylephrine added to spinal local anesthetics prolong block through what two mechanisms?",
   "answer":"Alpha-1 mediated vasoconstriction reduces systemic LA absorption (prolonging duration); epinephrine also enhances analgesia via direct alpha-2 adrenergic receptor agonism at the spinal cord.",
   "rationale":"Reduced vascular uptake maintains higher CSF LA concentration for longer; spinal alpha-2 receptors modulate pain transmission providing additional intrinsic analgesia.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":326}],"confusable_with":"Clonidine as spinal adjuvant (pure alpha-2 agonist; different from epinephrine's combined mechanisms)"},
  {"id":"spinal-technique-setup-3","topic":"Spinal anesthesia: technique and setup","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"For cesarean delivery, the preference between spinal and general anesthesia is typically case-by-case. What are the major risk categories that favor one over the other?",
   "answer":"No clear universal advantage exists for spinal vs general anesthesia in most patients; choice should consider specific medical issues: spinal avoids airway manipulation but risks hypotension; GA avoids regional failure but has higher maternal airway risk.",
   "rationale":"Evidence shows similar outcomes across techniques in most populations; individualized decision based on urgency, patient comorbidities, and anesthesiologist expertise is appropriate.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":594}],"confusable_with":""},
  {"id":"spinal-technique-setup-4","topic":"Spinal anesthesia: technique and setup","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"Opioids readily cross the placental barrier. What are the maternal and neonatal side effects of opioid use for labor analgesia?",
   "answer":"Maternal: nausea, vomiting, pruritus, delayed gastric emptying. Neonatal: decreased fetal heart rate variability, dose-related respiratory depression (particularly with systemic opioids).",
   "rationale":"All opioids cross the placenta; fetal/neonatal effects are dose-dependent and reversible with naloxone; neuraxial opioids at low doses produce less systemic fetal exposure.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":609}],"confusable_with":""},
  {"id":"spinal-technique-setup-5","topic":"Spinal anesthesia: technique and setup","domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)","discipline":"anesthesia",
   "stem":"What is the primary CNS effect and mechanism of action of barbiturates and propofol at GABA receptors used as IV anesthetics?",
   "answer":"Propofol and barbiturates decrease the rate of dissociation of GABA from its receptor, prolonging chloride channel opening, causing hyperpolarization and CNS depression.",
   "rationale":"GABA is the primary inhibitory neurotransmitter; activation of GABA-A receptor increases chloride conductance, hyperpolarizing the neuron; propofol and barbiturates potentiate this by slowing receptor-GABA dissociation.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":25}],"confusable_with":"Benzodiazepines (increase the frequency of GABA-receptor channel opening, not dissociation rate)"}
]

# ── Topic 14: Spine Surgery Cervical ─────────────────────────────────────────
kps += [
  {"id":"spine-surgery-cervical-1","topic":"Spine Surgery: Cervical","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"A trauma patient with suspected cervical spine injury requires intubation. What consideration guides choice of induction agent?",
   "answer":"Induction agents (benzodiazepines, opioids, propofol) attenuate sympathetic tone and can cause life-threatening hemodynamic collapse in trauma patients; ketamine or etomidate may be preferred to avoid hypotension.",
   "rationale":"Trauma patients often have concurrent sympathetic activation compensating for hypovolemia; sympatholytic induction agents can unmask hemodynamic instability and cause cardiovascular collapse.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1350}],"confusable_with":""},
  {"id":"spine-surgery-cervical-2","topic":"Spine Surgery: Cervical","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Most spinal surgery is performed for what two causes of nerve root or cord compression?",
   "answer":"Spinal surgery most commonly addresses compression from intervertebral disc protrusion (often at C4-5 or C5-6 in cervical spine) or osteophytic bone (spondylosis) into the spinal canal or foramen.",
   "rationale":"Degenerative disc disease and spondylosis are the predominant causes of symptomatic cervical myelopathy and radiculopathy requiring surgical decompression.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":990}],"confusable_with":""},
  {"id":"spine-surgery-cervical-3","topic":"Spine Surgery: Cervical","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In what scenarios is fiberoptic intubation (FOI) performed awake versus asleep for cervical spine surgery?",
   "answer":"Awake FOI: predicted inability to ventilate by mask or upper airway obstruction. Asleep FOI: failed intubation, need for minimal cervical spine movement in a patient refusing awake intubation, or anticipated difficult intubation when mask ventilation seems easy.",
   "rationale":"Awake techniques preserve airway protective reflexes; asleep FOI is reserved for specific indications where the risk-benefit analysis favors it.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":537}],"confusable_with":""},
  {"id":"spine-surgery-cervical-4","topic":"Spine Surgery: Cervical","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"For therapeutic LMWH dosing before planned neuraxial procedure, what washout interval is required?",
   "answer":"Therapeutic LMWH requires a 24-hour washout before neuraxial block; prophylactic twice-daily LMWH requires the catheter be removed >=4 hours before the first postoperative dose.",
   "rationale":"LMWH's anti-Xa activity persists for 12-24 hours depending on dosing; inadequate washout dramatically increases epidural hematoma risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1294}],"confusable_with":"UFH (different timing: check PTT; standard heparin has shorter half-life)"},
  {"id":"spine-surgery-cervical-5","topic":"Spine Surgery: Cervical","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In patients with cervical cord compression, what does postoperative cognitive dysfunction (POCD) etiology include beyond cervical surgery itself?",
   "answer":"POCD etiology is multifactorial: drug effects, pain, underlying brain dysfunction, hypothermia, metabolic disturbances; older patients are particularly sensitive to centrally acting anticholinergic agents.",
   "rationale":"No single factor explains POCD; the geriatric brain is vulnerable to multiple perioperative insults including anticholinergic medications, sleep disruption, and inflammation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1505}],"confusable_with":""}
]

# ── Topic 15: Spine Surgery Lumbar and Thoracic ───────────────────────────────
kps += [
  {"id":"spine-surgery-lumbar-1","topic":"Spine Surgery: Lumbar & Thoracic","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Particulate steroid injections at what spinal level are contraindicated due to anomalous vascular anatomy risk?",
   "answer":"Particulate steroids must not be used with cervical paravertebral nerve blocks due to possible anomalous vertebral artery anatomy that could cause spinal cord infarction.",
   "rationale":"Particulate steroid injected into an anomalous vertebral artery feeding the spinal cord can cause devastating neurologic injury; non-particulate steroids are preferred for cervical injections.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1778}],"confusable_with":"Lumbar/thoracic paravertebral (particulate steroids generally safe; different risk profile)"},
  {"id":"spine-surgery-lumbar-2","topic":"Spine Surgery: Lumbar & Thoracic","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"What is anterior lumbar interbody fusion (ALIF) best indicated for?",
   "answer":"ALIF is best for disc space collapse causing foraminal stenosis without significant canal stenosis; indirect neural foraminal decompression is achieved through wide discectomy and large anterior cage placement.",
   "rationale":"ALIF provides disc height restoration and foraminal decompression without posterior element manipulation; it is inappropriate when direct posterior decompression of the spinal canal is needed.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Spinal Cord Compression  Non Traumatic","page":9}],"confusable_with":"PLIF/TLIF (posterior approaches; better for canal stenosis requiring direct decompression)"},
  {"id":"spine-surgery-lumbar-3","topic":"Spine Surgery: Lumbar & Thoracic","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"The most common causes of spinal cord injury in general are what mechanisms?",
   "answer":"The most common causes of SCI are motor vehicle accidents, falls, and assault; SCI affects about 54 new cases per million per year.",
   "rationale":"Blunt trauma accounts for the vast majority of SCI; knowing the mechanism guides anticipation of concurrent injuries and anesthetic planning.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":809}],"confusable_with":""},
  {"id":"spine-surgery-lumbar-4","topic":"Spine Surgery: Lumbar & Thoracic","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"For postoperative patients on twice-daily prophylactic LMWH, when should neuraxial catheters be removed and when should the first dose be given?",
   "answer":"Remove neuraxial catheters >=4 hours before the first LMWH prophylactic dose; do not leave catheters in situ while twice-daily prophylactic dosing.",
   "rationale":"Catheter removal in the presence of residual anti-Xa activity risks epidural hematoma; timing catheter removal with the trough of LMWH activity minimizes this risk.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1294}],"confusable_with":"Once-daily LMWH prophylaxis (catheter removal 12 hours after last dose, next dose 4 hours after removal)"},
  {"id":"spine-surgery-lumbar-5","topic":"Spine Surgery: Lumbar & Thoracic","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"What is the thoracic paravertebral nerve block used for that the intercostal approach cannot achieve?",
   "answer":"Thoracic paravertebral block can anesthetize upper thoracic dermatome segments where the scapula prevents intercostal access.",
   "rationale":"The scapula overlies upper ribs and blocks intercostal injection; thoracic paravertebral injection deposits LA in the paravertebral space adjacent to the thoracic nerve roots before they enter the intercostal groove.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1778}],"confusable_with":"Epidural (bilateral coverage; paravertebral is unilateral with less sympathectomy)"}
]

# ── Topic 16: Statistical Concepts in Clinical Research Design ────────────────
# Chunks are predominantly guideline references (KDIGO, ADA, ACC/AHA) not statistical content
# Write KPs from available conceptual content
kps += [
  {"id":"statistical-concepts-research-1","topic":"Statistical Concepts in Clinical Research Design","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"In clinical guideline development, what study design provides the highest quality evidence for recommendations?",
   "answer":"Randomized controlled trials (RCTs) provide the highest level of evidence for treatment efficacy; systematic reviews and meta-analyses of RCTs are the gold standard for guideline recommendations.",
   "rationale":"Randomization controls for known and unknown confounders; meta-analysis increases statistical power; guidelines like KDIGO and ACC/AHA explicitly grade recommendations by evidence quality.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":20}],"confusable_with":"Observational studies (higher bias risk; generate hypotheses but cannot establish causation)"},
  {"id":"statistical-concepts-research-2","topic":"Statistical Concepts in Clinical Research Design","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"Patients with lower GFR are systematically underrepresented in prospective RCTs. What consequence does this have for clinical guideline applicability?",
   "answer":"Underrepresentation of patients with lower GFR in RCTs limits generalizability; guidelines must acknowledge evidence gaps and often rely on expert opinion for this population.",
   "rationale":"Low eGFR was historically an exclusion criterion for trials; the resulting evidence gaps require extrapolation or weaker observational data to guide management in CKD patients.",
   "bloom":"analyze","source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":155}],"confusable_with":""},
  {"id":"statistical-concepts-research-3","topic":"Statistical Concepts in Clinical Research Design","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"Clinical guideline recommendations include qualifications stating they are not intended to preclude clinical judgment. What does this mean for individual patient care?",
   "answer":"Guidelines provide evidence-based population-level recommendations; they must be applied with individualized clinical judgment, as patient-specific factors may warrant deviation from guidelines.",
   "rationale":"Guidelines represent average effects in populations; individual patients may have contraindications, comorbidities, or values that make adherence to a guideline recommendation inappropriate.",
   "bloom":"apply","source":[{"book":"Society Guideline: Guideline   ADA Standards of Care 2024 Overview","page":2}],"confusable_with":""},
  {"id":"statistical-concepts-research-4","topic":"Statistical Concepts in Clinical Research Design","domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)","discipline":"anesthesia",
   "stem":"What is the purpose of including patients with CKD and other kidney-related conditions in prospective RCTs per current guideline research recommendations?",
   "answer":"Including CKD patients in RCTs fills critical evidence gaps; currently these patients are underrepresented, leading to guideline recommendations based on weak evidence for a high-risk population.",
   "rationale":"CKD patients have high cardiovascular and pharmacological risks but are excluded from most major trials; including them enables evidence-based rather than extrapolated recommendations.",
   "bloom":"recall","source":[{"book":"Society Guideline: Guideline   KDIGO 2024 CKD","page":196}],"confusable_with":""}
]

# ── Topic 17: Stereotactic & Functional Neurosurgery ─────────────────────────
kps += [
  {"id":"stereotactic-functional-neuro-1","topic":"Stereotactic & Functional Neurosurgery","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"A patient with elevated ICP is scheduled for stereotactic neurosurgery. Why should sedation be omitted?",
   "answer":"Sedation should be omitted if the patient already has elevated ICP, as sedatives can cause hypercapnia and further increase ICP through cerebral vasodilation.",
   "rationale":"In elevated ICP states, any CO2 rise from sedative-induced respiratory depression worsens intracranial hypertension; maintaining spontaneous ventilation or ensuring adequate ventilation is critical.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":978}],"confusable_with":""},
  {"id":"stereotactic-functional-neuro-2","topic":"Stereotactic & Functional Neurosurgery","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"What unique anesthetic challenge does a stereotactic frame create during emergency craniotomy?",
   "answer":"The localizing frame attached to the patient's head complicates rapid general anesthesia and airway management; the ability to provide controlled ventilation and emergency craniotomy under GA must be maintained despite the frame.",
   "rationale":"Stereotactic frames fix the head and restrict access to the airway; pre-procedure airway planning and rapid-sequence preparation are mandatory.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":978}],"confusable_with":""},
  {"id":"stereotactic-functional-neuro-3","topic":"Stereotactic & Functional Neurosurgery","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Functional neurosurgery is increasingly performed for lesions adjacent to what brain centers, requiring special anesthetic considerations?",
   "answer":"Functional neurosurgery is performed for lesions adjacent to speech and other vital brain centers; this often requires awake craniotomy with the patient able to respond to testing.",
   "rationale":"Intraoperative cortical mapping of speech, motor, and sensory cortex requires patient cooperation; awake-asleep-awake or monitored anesthesia care (MAC) techniques are used.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":978}],"confusable_with":"Deep brain stimulation (DBS) (also functional; requires awake patient for microelectrode recording)"},
  {"id":"stereotactic-functional-neuro-4","topic":"Stereotactic & Functional Neurosurgery","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In a preoperative evaluation for neurosurgery, why should sedative or opioid premedication be avoided when intracranial hypertension is suspected?",
   "answer":"Hypercapnia secondary to respiratory depression from sedatives increases ICP via cerebral vasodilation; premedication should be avoided or used with extreme caution in suspected intracranial hypertension.",
   "rationale":"CO2 is the primary regulator of cerebral blood flow; CO2 retention from CNS-depressant premedication causes cerebrovascular dilation, increasing cerebral blood volume and ICP.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":970}],"confusable_with":""},
  {"id":"stereotactic-functional-neuro-5","topic":"Stereotactic & Functional Neurosurgery","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In patients undergoing electroconvulsive therapy (ECT) with a pacemaker, what should be immediately available?",
   "answer":"A magnet should be readily available to convert the pacemaker to a fixed mode if needed; patients with pacemakers may safely undergo ECT with this precaution.",
   "rationale":"ECT-induced seizure activity can interfere with pacemaker sensing; a magnet converts demand pacemakers to asynchronous (fixed-rate) mode, preventing inhibition of pacing during the ECT current.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1022}],"confusable_with":"ICD (requires different management: magnet disables shock therapy but not pacing)"}
]

# ── Topic 18: Subarachnoid Hemorrhage Perioperative Management ────────────────
# Chunks: SAH management, air embolism, cerebral amyloid angiopathy, pituitary apoplexy
kps += [
  {"id":"sah-perioperative-1","topic":"Subarachnoid Hemorrhage: Perioperative Management","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Venous air embolism is encountered during posterior fossa neurosurgery in the sitting position. What are the five steps of management?",
   "answer":"(1) Flood surgical field with saline; (2) place patient head-down; (3) gently compress internal jugular veins and give IV fluids to increase venous pressure; (4) ensure 100% FiO2; (5) hemodynamic support; if N2O present, discontinue immediately.",
   "rationale":"N2O rapidly expands any air space; flooding the field prevents further entrainment; elevating venous pressure prevents continued air ingress; 100% O2 facilitates air resorption.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":566}],"confusable_with":""},
  {"id":"sah-perioperative-2","topic":"Subarachnoid Hemorrhage: Perioperative Management","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"In managing elevated ICP after TBI when no surgical clot is present, what are the primary medical interventions?",
   "answer":"Medical ICP management includes: head elevation, osmotic therapy (mannitol, hypertonic saline), controlled hyperventilation (temporary), sedation, maintain CPP >=60-70 mmHg (MAP-ICP); corticosteroids are NOT indicated for traumatic ICP.",
   "rationale":"Osmotic agents reduce cerebral water content; controlled hyperventilation causes cerebral vasoconstriction; maintaining CPP prevents ischemia; corticosteroids increase mortality in TBI.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":984}],"confusable_with":"Corticosteroids for ICP (indicated for vasogenic edema from tumor, NOT traumatic ICP)"},
  {"id":"sah-perioperative-3","topic":"Subarachnoid Hemorrhage: Perioperative Management","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"Cerebral amyloid angiopathy (CAA) affects which blood vessels and what is the primary complication?",
   "answer":"CAA involves deposition of amyloid beta protein in small-to-medium cortical and leptomeningeal blood vessels, causing lobar hemorrhagic stroke, often recurrent.",
   "rationale":"Amyloid-laden vessel walls are fragile and prone to rupture; CAA is distinct from hypertensive hemorrhage (which affects deep structures) and is a major cause of spontaneous lobar ICH in the elderly.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":2}],"confusable_with":"Hypertensive hemorrhage (affects basal ganglia, thalamus, brainstem; not lobar)"},
  {"id":"sah-perioperative-4","topic":"Subarachnoid Hemorrhage: Perioperative Management","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"GI bleeding from stress ulceration is common in which neurosurgical patients without prophylaxis?",
   "answer":"GI stress ulceration is common in head trauma patients and other critically ill neurosurgical patients; prophylaxis with PPI or H2 blocker is recommended.",
   "rationale":"CNS injury causes autonomic dysregulation and increased gastric acid secretion (Cushing effect); stress ulcer prophylaxis reduces morbidity in ventilated and brain-injured patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":984}],"confusable_with":""},
  {"id":"sah-perioperative-5","topic":"Subarachnoid Hemorrhage: Perioperative Management","domain":"Neuroanesthesia (intracranial pressure & cerebral perfusion, craniotomy, spine surgery, evoked potentials, awake craniotomy, neuromonitoring)","discipline":"anesthesia",
   "stem":"For patients with CAA, what criteria (Boston criteria v2.0) are used to diagnose definite, probable, and possible CAA?",
   "answer":"Boston criteria v2.0 classify CAA as: definite (pathologic confirmation), probable (clinical + MRI features: multiple lobar microbleeds/hemorrhages, cortical superficial siderosis on susceptibility sequences, age >55), possible (single lobar bleed, no pathology).",
   "rationale":"MRI susceptibility-weighted imaging detects hemosiderin deposits from prior microhemorrhages; the pattern and location of bleeds distinguish CAA from hypertensive angiopathy.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":2}],"confusable_with":""}
]

# ── Topic 19: Substance use disorders preoperative assessment ─────────────────
kps += [
  {"id":"substance-use-preop-1","topic":"Substance use disorders - preoperative assessment","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"What questionnaire is commonly used to screen for substance use disorders during preoperative assessment?",
   "answer":"The CAGE questionnaire is commonly used to screen for substance use disorders (alcohol) during preoperative assessment.",
   "rationale":"CAGE (Cut down, Annoyed, Guilty, Eye-opener) is a validated 4-question screen for alcohol use disorder that can be rapidly administered in preoperative settings.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":676}],"confusable_with":"PHQ-9 (depression screening, not substance use); AUDIT (more comprehensive alcohol screen)"},
  {"id":"substance-use-preop-2","topic":"Substance use disorders - preoperative assessment","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"Patients with type 2 diabetes taking SGLT-2 inhibitors undergoing surgery are at risk for what metabolic complication?",
   "answer":"SGLT-2 inhibitor use in surgical or hospitalized patients is associated with risk of euglycemic diabetic ketoacidosis (DKA); these medications should typically be held 24-72 h before major surgery.",
   "rationale":"SGLT-2 inhibitors increase glucagon and ketone production; perioperative fasting and surgical stress can precipitate DKA even with near-normal glucose levels.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1491}],"confusable_with":"Hypoglycemia (more concern with sulfonylureas and insulin, not SGLT-2 inhibitors)"},
  {"id":"substance-use-preop-3","topic":"Substance use disorders - preoperative assessment","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"A STOP-BANG score >=3 is associated with what perioperative risk?",
   "answer":"STOP-BANG score >=3 is associated with increased risk of postoperative complications, including respiratory complications and cardiovascular events related to obstructive sleep apnea.",
   "rationale":"STOP-BANG screens for OSA (Snoring, Tiredness, Observed apnea, Pressure, BMI, Age, Neck, Gender); higher scores indicate more severe OSA with greater perioperative risk.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":698}],"confusable_with":"Berlin questionnaire (another OSA screen; STOP-BANG is more validated perioperatively)"},
  {"id":"substance-use-preop-4","topic":"Substance use disorders - preoperative assessment","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"What routine medications from a patient's preoperative medication review should flag concern for renal function or electrolyte abnormalities?",
   "answer":"ACE inhibitors, ARBs, antiplatelet agents, SGLT-2 inhibitors, and statins all require review; ACE inhibitors/ARBs flag renal/potassium concerns; SGLT-2 inhibitors flag DKA risk perioperatively.",
   "rationale":"Careful preoperative medication review identifies agents that interact with anesthesia, increase perioperative risk, or require holding prior to surgery.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1491}],"confusable_with":""},
  {"id":"substance-use-preop-5","topic":"Substance use disorders - preoperative assessment","domain":"Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)","discipline":"anesthesia",
   "stem":"In preoperative assessment for substance use disorders, why is evaluating for mood disorders such as depression essential?",
   "answer":"Depression and substance use disorders frequently co-occur; unrecognized depression affects consent capacity, perioperative behavior, pain perception, analgesic requirements, and recovery outcomes.",
   "rationale":"Psychiatric comorbidities are common in surgical patients; concurrent depression and substance abuse increase complexity of perioperative management, opioid titration, and postoperative delirium risk.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":676}],"confusable_with":""}
]

print('Topics 11-19 done:', len(kps))
with open('data/kp_part26_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 2 written')
