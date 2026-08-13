import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/kp_part23_batch4.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ── 27: Neuraxial anatomy ─────────────────────────────────────────────────────
kps += [
  {"id":"neuraxial-anat-1","topic":"Neuraxial anatomy",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"Describe the bony composition of the spinal column relevant to neuraxial anesthesia.",
   "answer":"The spine has 7 cervical (C), 12 thoracic (T), and 5 lumbar (L) vertebrae, plus the sacrum (fusion of 5 sacral vertebrae) and rudimentary coccygeal vertebrae; intervertebral disks separate the bodies.",
   "rationale":"Understanding vertebral levels guides landmark-based identification of intervertebral spaces; lumbar vertebrae (L2-L5) are the most common targets for neuraxial blocks.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1544}],
   "confusable_with":""},

  {"id":"neuraxial-anat-2","topic":"Neuraxial anatomy",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"What are the layers traversed in order from skin to epidural space when performing a lumbar epidural block?",
   "answer":"Skin -> subcutaneous fat -> supraspinous ligament -> interspinous ligament -> ligamentum flavum -> epidural space.",
   "rationale":"The ligamentum flavum provides the characteristic loss-of-resistance that identifies the epidural space; the distinct tactile change from the ligamentum flavum to the potential epidural space is the hallmark of epidural identification.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1568}],
   "confusable_with":"Layers for spinal anesthesia (continues through dura mater and arachnoid to subarachnoid space)"},

  {"id":"neuraxial-anat-3","topic":"Neuraxial anatomy",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"Neuraxial blocks should not be performed at cervical levels in awake patients with altered mental status. Why, and what is the exception?",
   "answer":"Cervical and high thoracic neuraxial blocks must be performed in awake, responsive patients (except unusual circumstances) because the patient's cooperation and ability to report paresthesias or CNS symptoms protects against spinal cord injury; pediatric neuraxial blocks are an accepted exception performed under general anesthesia.",
   "rationale":"The spinal cord ends at L1-L2 in adults; cervical punctures are immediately adjacent to the cord and require patient feedback to avoid direct neural injury; children's blocks at caudal/epidural level are routinely done under GA with acceptable safety.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1567}],
   "confusable_with":""},

  {"id":"neuraxial-anat-4","topic":"Neuraxial anatomy",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"When an accidental dural puncture occurs during epidural placement, larger epidural catheters are sometimes purposely advanced intrathecally. What critical precaution is mandatory?",
   "answer":"The catheter must be clearly labeled as subarachnoid (not epidural) to prevent accidental administration of epidural doses, which are 3-10x higher than intrathecal doses and would cause high/total spinal block.",
   "rationale":"Continuous spinal catheters via accidentally-placed large-bore epidural catheters are a valuable rescue technique, but the labeling confusion between epidural and subarachnoid catheters has caused fatal high spinal blocks.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1576}],
   "confusable_with":""},

  {"id":"neuraxial-anat-5","topic":"Neuraxial anatomy",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"Caudal epidural anesthesia enters the epidural space through what anatomical structure?",
   "answer":"Caudal epidural anesthesia accesses the sacral epidural space through the sacrococcygeal ligament (sacral hiatus), a defect in the lower sacrum created by failure of fusion of the S4-S5 vertebral arches.",
   "rationale":"The sacral hiatus provides a membrane-covered opening into the epidural space at the caudal end of the vertebral canal; this route is especially useful in pediatrics and for perineal/anal procedures.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1591}],
   "confusable_with":"Lumbar epidural (approaches the space between L2-L5 via interspinous ligament and ligamentum flavum; different entry point)"},
]

# ── 28: Neuraxial and Regional Anatomy ───────────────────────────────────────
kps += [
  {"id":"neuraxial-reg-anat-1","topic":"Neuraxial and Regional Anatomy",
   "domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)",
   "discipline":"anesthesia",
   "stem":"Transient neurological symptoms (TNS) were first described in 1993. What are the clinical characteristics of TNS?",
   "answer":"TNS (also called transient radicular irritation) is back pain radiating to the legs occurring within 24 h after spinal anesthesia, lasting up to several days, without neurological deficit; most commonly associated with lidocaine spinal anesthesia.",
   "rationale":"The mechanism of TNS is unclear but may involve gluteal muscle stretching from the lithotomy position and lidocaine-specific neurochemical effects; incidence is highest with hyperbaric lidocaine and lithotomy position.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1603}],
   "confusable_with":"Cauda equina syndrome (permanent neurological injury; not transient; associated with hyperbaric lidocaine through microcatheter continuous spinal or high doses)"},

  {"id":"neuraxial-reg-anat-2","topic":"Neuraxial and Regional Anatomy",
   "domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)",
   "discipline":"anesthesia",
   "stem":"The ganglion impar (ganglion of Walther) is the most caudal sympathetic structure. What is it, where is it located, and what pain conditions are treated by its blockade?",
   "answer":"The ganglion impar is the lowest pelvic sympathetic ganglion (two sacral chains often fuse) located just anterior to the coccyx; it is blocked for perineal pain, coccydynia, and visceral pelvic pain.",
   "rationale":"Sympathetically-mediated pelvic pain travels through the ganglion impar; blockade interrupts sympathetic afferents and provides relief for complex regional pain syndromes of the perineum.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1792}],
   "confusable_with":"Stellate ganglion block (cervicothoracic sympathetic block for upper extremity/head sympathetically-mediated pain)"},

  {"id":"neuraxial-reg-anat-3","topic":"Neuraxial and Regional Anatomy",
   "domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)",
   "discipline":"anesthesia",
   "stem":"Ultrasound imaging of the lumbar epidural space uses what transducer orientation and what landmarks are visualized?",
   "answer":"A paramedian longitudinal view uses the transducer parallel to the spine; key structures visualized are the ligamentum flavum, anterior and posterior dura mater, and posterior longitudinal ligament as hyperechoic lines.",
   "rationale":"Ultrasound pre-scanning identifies intervertebral spaces, estimates needle depth to the epidural space, and is particularly useful in obese patients or those with challenging anatomy.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1568}],
   "confusable_with":""},

  {"id":"neuraxial-reg-anat-4","topic":"Neuraxial and Regional Anatomy",
   "domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)",
   "discipline":"anesthesia",
   "stem":"Excessive epidural or caudal local anesthetic absorption causing systemic toxicity is rare when appropriate doses are used. However, which patient factors increase systemic absorption?",
   "answer":"Highly vascular injection sites (intercostal > caudal > epidural > brachial plexus > femoral/sciatic > subcutaneous), inflamed or infected tissues, and lack of epinephrine all increase systemic absorption.",
   "rationale":"The rate of systemic absorption depends on tissue vascularity at the injection site; intercostal blocks have the highest absorption rate due to direct proximity to intercostal vessels.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1603}],
   "confusable_with":""},

  {"id":"neuraxial-reg-anat-5","topic":"Neuraxial and Regional Anatomy",
   "domain":"Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)",
   "discipline":"anesthesia",
   "stem":"In a patient receiving neuraxial anesthesia who develops abdominal pain not covered by the block, why might visceral pain from peritoneal traction persist even with a T4 sensory level?",
   "answer":"Visceral afferent fibers traveling with the vagus nerve are not blocked by neuraxial anesthesia regardless of sensory level; vagally-mediated visceral pain (e.g., traction on peritoneum, uterus) requires IV supplementation with opioids or other agents.",
   "rationale":"The vagus nerve carries visceral sensory fibers that enter the CNS at the medulla, completely bypassing the thoracolumbar sympathetic chain and any level of spinal blockade.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1591}],
   "confusable_with":""},
]

# ── 29: Neuraxial blocks in special populations ───────────────────────────────
kps += [
  {"id":"neuraxial-special-1","topic":"Neuraxial blocks in special populations",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"What is the double-crush phenomenon and how does it apply to neuraxial anesthesia in patients with preexisting neuropathy?",
   "answer":"The double-crush hypothesis posits that a preexisting proximal nerve lesion increases susceptibility to injury at a distal site from a second insult; patients with central or peripheral neurological conditions have increased risk of injury from neuraxial anesthesia and the risk-benefit ratio must be carefully weighed.",
   "rationale":"A compromised nerve (diabetic neuropathy, MS, spinal stenosis) has reduced tolerance for additional neural insult from local anesthetic, needle trauma, or ischemia; baseline neurological dysfunction complicates attribution of new postoperative deficits.",
   "bloom":"analyze",
   "source":[{"book":"Miller/Baby Miller","page":320}],
   "confusable_with":""},

  {"id":"neuraxial-special-2","topic":"Neuraxial blocks in special populations",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"Neuraxial clonidine use in obstetric patients carries an FDA black-box warning. What are the specific risks?",
   "answer":"The FDA has issued a black-box warning for neuraxial clonidine in obstetrics due to increased risks of hypotension and bradycardia; caution is required and epidural clonidine is contraindicated for labor and postpartum analgesia.",
   "rationale":"Clonidine's alpha-2 agonism causes dose-dependent hypotension and bradycardia; in parturients these effects are particularly hazardous because of already compromised uteroplacental perfusion.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":610}],
   "confusable_with":"Epidural dexmedetomidine (alpha-2 agonist with similar concerns; also used cautiously in non-obstetric patients)"},

  {"id":"neuraxial-special-3","topic":"Neuraxial blocks in special populations",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"An obstetric patient at term needs neuraxial analgesia but has received low-dose midazolam and fentanyl premedication. What is the maximum safe dose of midazolam in healthy parturients at term combined with fentanyl for analgesia facilitation?",
   "answer":"Small doses of midazolam up to 2 mg IV combined with fentanyl up to 100 mcg IV may be used to facilitate neuraxial blockade in healthy parturients at term.",
   "rationale":"These are minimum sedation doses to improve cooperation during block placement; higher doses raise concerns about neonatal effects (benzodiazepine fetal depression) and maternal airway risks.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1390}],
   "confusable_with":""},

  {"id":"neuraxial-special-4","topic":"Neuraxial blocks in special populations",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"Epidural catheter insertion is requested for a Jehovah's Witness patient for postoperative pain control after orthopedic surgery. What is the benefit and what specific concern arises?",
   "answer":"Epidural analgesia can provide opioid-sparing pain control, reducing the need for blood-product-triggering interventions; the concern is epidural hematoma risk requiring hematoma evacuation with potential transfusion in an anticoagulation-managed patient who refuses blood products.",
   "rationale":"Epidural hematoma causing spinal cord compression is a rare but catastrophic complication; in a patient refusing blood products, surgical management and its transfusion requirements must be explicitly discussed.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1317}],
   "confusable_with":""},

  {"id":"neuraxial-special-5","topic":"Neuraxial blocks in special populations",
   "domain":"Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)",
   "discipline":"anesthesia",
   "stem":"What are the nerve territories of the adductor canal block and what is its main advantage over a femoral nerve block for total knee arthroplasty?",
   "answer":"The adductor canal block primarily provides sensory analgesia to the medial knee and distal thigh via the saphenous nerve; its main advantage over femoral nerve block is preservation of quadriceps strength, enabling earlier mobilization and physical therapy.",
   "rationale":"The femoral nerve provides both sensory and motor innervation to the anterior thigh and knee; blocking it causes quadriceps weakness and fall risk; the adductor canal block targets the predominantly sensory saphenous nerve at this level.",
   "bloom":"analyze",
   "source":[{"book":"Stanford CA-1","page":98}],
   "confusable_with":"Femoral nerve block (also covers medial knee/anterior thigh but causes quadriceps motor block)"},
]

# ── 30: Neuraxial complications in obstetrics ─────────────────────────────────
kps += [
  {"id":"neuraxial-ob-comp-1","topic":"Neuraxial complications in obstetrics",
   "domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)",
   "discipline":"anesthesia",
   "stem":"What is the typical onset and natural history of post-dural puncture headache (PDPH)?",
   "answer":"PDPH typically begins within 3 days (two-thirds within 48 hours), is postural (worsening upright, relieved supine), and spontaneously resolves within 7 days in most cases; a minority still have symptoms at 6 months.",
   "rationale":"CSF leak through the dural hole reduces intracranial CSF pressure; the postural nature reflects gravitational effects on reduced CSF cushioning of pain-sensitive intracranial structures.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":336}],
   "confusable_with":"Migraine headache (not positional; aura common; not related to dural puncture; no relief in supine)"},

  {"id":"neuraxial-ob-comp-2","topic":"Neuraxial complications in obstetrics",
   "domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)",
   "discipline":"anesthesia",
   "stem":"Compared with standard epidural, CSE (combined spinal-epidural) in obstetrics is associated with what specific side effects related to the intrathecal opioid component?",
   "answer":"CSE compared with epidural alone is associated with increased opioid-based pruritus, increased risk of uterine tachysystole, and greater incidence of fetal bradycardia after block placement (though not increased risk of emergency cesarean).",
   "rationale":"Intrathecal opioids cause more intense and acute spinal receptor stimulation than epidural opioids; the uterotonic effect of intrathecal fentanyl/sufentanil may cause uterine hypercontractility and consequent fetal bradycardia.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":613}],
   "confusable_with":"DPE (dural puncture epidural) has fewer one-sided blocks and fewer catheter failures than standard epidural; less pruritus than CSE"},

  {"id":"neuraxial-ob-comp-3","topic":"Neuraxial complications in obstetrics",
   "domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)",
   "discipline":"anesthesia",
   "stem":"Hypotension following spinal anesthesia for cesarean delivery is defined and treated how?",
   "answer":"Hypotension is defined as systolic BP decrease >20% from baseline or below 100 mmHg; treatment includes left uterine displacement, IV fluid bolus (crystalloid or colloid), and vasopressors (phenylephrine first-line; ephedrine if bradycardic).",
   "rationale":"Spinal-induced sympathectomy causes vasodilation and hypotension; phenylephrine maintains uteroplacental perfusion with less fetal acidosis than ephedrine in healthy parturients; ephedrine is preferred when maternal bradycardia is present.",
   "bloom":"apply",
   "source":[{"book":"Miller/Baby Miller","page":615}],
   "confusable_with":""},

  {"id":"neuraxial-ob-comp-4","topic":"Neuraxial complications in obstetrics",
   "domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)",
   "discipline":"anesthesia",
   "stem":"The epidural re-dose strategy for extension of labor analgesia to cesarean delivery anesthesia uses what volumes and what sensory level target?",
   "answer":"Repeat doses of epidural local anesthetic are administered in one-third to one-half of the original dose when block regression begins; the target sensory level for cesarean delivery is T4 (to cover peritoneal traction).",
   "rationale":"A T4 sensory level covers the thoracoabdominal dermatomes necessary for cesarean delivery; patchy analgesia before delivery can be treated with 10-20 mL of dilute LA in increments.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1406},{"book":"Morgan & Mikhail","page":1589}],
   "confusable_with":""},

  {"id":"neuraxial-ob-comp-5","topic":"Neuraxial complications in obstetrics",
   "domain":"Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)",
   "discipline":"anesthesia",
   "stem":"Neuraxial clonidine in obstetrics carries an FDA black-box warning for what specific complications?",
   "answer":"Increased risk of hypotension and bradycardia; neuraxial clonidine is contraindicated for labor and postpartum analgesia due to these hemodynamic risks.",
   "rationale":"Alpha-2 agonism decreases sympathetic outflow; in already vasodilated parturients, additional sympatholysis causes clinically dangerous hypotension that can compromise uteroplacental perfusion.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":610}],
   "confusable_with":"Neuraxial opioids (pruritus, nausea, urinary retention as main side effects; not bradycardia/hypotension as primary warning)"},
]

# ── 31: Neurogenic Pulmonary Edema ────────────────────────────────────────────
kps += [
  {"id":"npe-1","topic":"Neurogenic Pulmonary Edema",
   "domain":"Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)",
   "discipline":"anesthesia",
   "stem":"What neurological events are known to precipitate neurogenic pulmonary edema?",
   "answer":"Head injury, intracranial bleeding, and abrupt reversal of opioid overdosage with naloxone can all precipitate neurogenic pulmonary edema.",
   "rationale":"A marked increase in sympathetic tone (from any acute CNS insult) causes severe pulmonary hypertension and disruption of the alveolar-capillary membrane, flooding the alveoli.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2133}],
   "confusable_with":"Cardiogenic pulmonary edema (LV failure-driven elevated PCWP; different mechanism though overlap can occur after neurological injury)"},

  {"id":"npe-2","topic":"Neurogenic Pulmonary Edema",
   "domain":"Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)",
   "discipline":"anesthesia",
   "stem":"What is the proposed pathophysiology of neurogenic pulmonary edema?",
   "answer":"An abrupt, massive increase in sympathetic tone causes severe pulmonary hypertension; this, combined with disruption of the alveolar-capillary membrane, produces non-cardiogenic pulmonary edema.",
   "rationale":"Massive sympathetic discharge elevates pulmonary vascular pressure acutely beyond the capacity of the alveolar-capillary barrier; hydrostatic and inflammatory damage lead to alveolar flooding.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2129},{"book":"Morgan & Mikhail","page":2133}],
   "confusable_with":"ARDS (diffuse alveolar damage from non-CNS causes; bilateral infiltrates; similar appearance on CXR)"},

  {"id":"npe-3","topic":"Neurogenic Pulmonary Edema",
   "domain":"Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)",
   "discipline":"anesthesia",
   "stem":"What is the typical time course of neurogenic pulmonary edema?",
   "answer":"Neurogenic pulmonary edema typically presents very rapidly after the inciting CNS event and usually dissipates over approximately 24 hours.",
   "rationale":"The transient nature reflects the transient sympathetic surge; as sympathetic tone normalizes after the acute CNS event, pulmonary vascular pressure decreases and edema resolves.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2133}],
   "confusable_with":"Aspiration pneumonitis (also acute-onset post-event; but worsens over 24-48 h rather than resolving)"},

  {"id":"npe-4","topic":"Neurogenic Pulmonary Edema",
   "domain":"Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)",
   "discipline":"anesthesia",
   "stem":"Why is distinguishing neurogenic from cardiogenic pulmonary edema after a major neurological injury clinically challenging?",
   "answer":"Major neurological injuries can also produce direct cardiac effects (neurogenic myocardial injury, Takotsubo-like dysfunction, arrhythmias), so neurogenic and cardiogenic pulmonary edema may overlap and coexist.",
   "rationale":"The same massive catecholamine surge that causes pulmonary vasoconstriction can directly injure myocardium and impair LV function; both mechanisms may contribute simultaneously to pulmonary edema.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":2133}],
   "confusable_with":""},

  {"id":"npe-5","topic":"Neurogenic Pulmonary Edema",
   "domain":"Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)",
   "discipline":"anesthesia",
   "stem":"Pulmonary edema develops when the pulmonary interstitium's reserve capacity for accommodating capillary transudation is exceeded. What normally prevents pulmonary edema from forming with modest increases in capillary pressure?",
   "answer":"The lung's unique ultrastructure has a large capacity to increase lymphatic flow, accommodating substantial increases in capillary transudation before interstitial pressure becomes positive; only when this lymphatic reserve is exceeded does pulmonary edema develop.",
   "rationale":"Pulmonary lymphatics can increase flow 10-fold above baseline; this safety factor allows substantial fluid accumulation in the interstitium before alveolar flooding occurs.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2129}],
   "confusable_with":""},

  {"_type":"illness_script",
   "topic":"Neurogenic Pulmonary Edema",
   "discipline":"anesthesia",
   "enabling_conditions":"Acute CNS injury (head trauma, intracranial hemorrhage, seizure, subarachnoid hemorrhage) or abrupt naloxone reversal; any event causing massive sympathetic discharge",
   "pathophysiology":"Massive sympathetic surge -> severe pulmonary hypertension -> disruption of alveolar-capillary membrane -> non-cardiogenic pulmonary edema; direct CNS cardiac effects can add cardiogenic component",
   "time_course":"Rapid onset within minutes to hours of CNS event; typically resolves within 24 hours as sympathetic tone normalizes",
   "key_features":"Acute hypoxemia, bilateral pulmonary infiltrates, frothy sputum, tachycardia in setting of acute CNS injury; PCWP may be normal (non-cardiogenic) but can overlap with cardiogenic component",
   "consequence_if_missed":"Respiratory failure, prolonged mechanical ventilation; may obscure the severity of the underlying CNS injury"},
]

# ── 32: Neurological Complications of Cardiac Surgery ────────────────────────
kps += [
  {"id":"cardiac-neuro-1","topic":"Neurological Complications of Cardiac Surgery",
   "domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)",
   "discipline":"anesthesia",
   "stem":"Preoperative neurological evaluation is essential before cardiac surgery. What three organ systems besides the heart should be specifically assessed in preoperative cardiac surgical evaluation?",
   "answer":"Pulmonary, neurological, and kidney function should be specifically assessed preoperatively, as impairment of these systems predisposes to myriad postoperative complications.",
   "rationale":"CPB exposes all organ systems to non-pulsatile flow, emboli, and inflammatory activation; preexisting impairment dramatically increases the risk of postoperative organ dysfunction in each system.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":719}],
   "confusable_with":""},

  {"id":"cardiac-neuro-2","topic":"Neurological Complications of Cardiac Surgery",
   "domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)",
   "discipline":"anesthesia",
   "stem":"Carotid endarterectomy is indicated for symptomatic patients with ipsilateral carotid stenosis. What degree of stenosis is the current threshold and what has replaced surgery for some asymptomatic lesions?",
   "answer":"CEA is indicated for symptomatic patients with 30-70% ipsilateral stenosis (especially with ulcerated plaque); for asymptomatic lesions previously treated surgically at >60%, carotid stenting is now the recommendation for many patients.",
   "rationale":"Randomized trials (NASCET, ACAS) established benefit of CEA for symptomatic stenosis; endovascular stenting has become the preferred approach for asymptomatic significant lesions in many centers.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":782}],
   "confusable_with":""},

  {"id":"cardiac-neuro-3","topic":"Neurological Complications of Cardiac Surgery",
   "domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)",
   "discipline":"anesthesia",
   "stem":"An asymptomatic carotid bruit is found in 4% of patients over age 40. Does this finding significantly increase perioperative stroke risk for non-cardiac surgery?",
   "answer":"An asymptomatic carotid bruit does not necessarily increase perioperative stroke risk for non-cardiac surgery; fewer than 10% of patients with asymptomatic bruits have hemodynamically significant lesions.",
   "rationale":"An asymptomatic bruit is a marker of atherosclerotic disease but does not reliably predict hemodynamically significant stenosis; the stroke risk during non-cardiac surgery is determined more by the degree of stenosis than by the presence of a bruit alone.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":998}],
   "confusable_with":"Symptomatic carotid disease (TIA/stroke within 6 months — significantly increases perioperative stroke risk)"},

  {"id":"cardiac-neuro-4","topic":"Neurological Complications of Cardiac Surgery",
   "domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)",
   "discipline":"anesthesia",
   "stem":"What is the operative mortality for carotid endarterectomy and what is it primarily due to?",
   "answer":"Operative mortality for open CEA is 1-4%, primarily due to cardiac complications (myocardial infarction) rather than neurological complications.",
   "rationale":"Patients requiring CEA have diffuse atherosclerosis; coronary artery disease is the dominant cause of perioperative death, not stroke, reflecting the shared pathophysiology of carotid and coronary disease.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":782}],
   "confusable_with":""},

  {"id":"cardiac-neuro-5","topic":"Neurological Complications of Cardiac Surgery",
   "domain":"Cardiovascular & cardiac anesthesia (CABG, valvular, cardiopulmonary bypass, TEE basics, cardiac physiology, hemodynamic & vasoactive management, ICDs/pacemakers)",
   "discipline":"anesthesia",
   "stem":"Perioperative morbidity after carotid endarterectomy is 4-10% and is primarily neurological. What intraoperative maneuver causes blood pressure and rhythm instability during carotid surgery?",
   "answer":"Manipulation of the carotid sinus and stellate ganglion during radical neck or carotid dissection causes wide swings in blood pressure, bradycardia, arrhythmias, sinus arrest, and prolonged QT intervals.",
   "rationale":"The carotid sinus contains baroreceptors that respond to stretch; surgical manipulation stimulates them, triggering reflex vagal responses; stellate ganglion manipulation affects cardiac sympathetic tone.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1269}],
   "confusable_with":""},
]

print(f"Final total KPs+scripts+pairs: {len(kps)}")

# Count types
kp_count = sum(1 for x in kps if '_type' not in x)
script_count = sum(1 for x in kps if x.get('_type') == 'illness_script')
pair_count = sum(1 for x in kps if x.get('_type') == 'confusable_pair')
print(f"KPs: {kp_count}, illness_scripts: {script_count}, confusable_pairs: {pair_count}")

with open('data/kp_full_part_23.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Verify parses back
with open('data/kp_full_part_23.json', 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f"Verified: {len(verify)} entries parsed OK")
print("kp_full_part_23.json written OK")
