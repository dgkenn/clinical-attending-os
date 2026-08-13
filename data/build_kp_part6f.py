import json, sys
sys.path.insert(0, 'data')
from build_kp_part6e import kps

disc = "anesthesia"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_neuro = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"
dom_obs = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"
dom_basic = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"
dom_preop = "Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)"

# =====================================================================
# [17] Etomidate: pharmacology
# (Chunks are mostly off-topic benzodiazepine/MAC content; etomidate-specific chunks exist)
# =====================================================================
topic17 = "Etomidate: pharmacology"

kps += [
  {"id":"etomidate-pharmacology-d1","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"Etomidate reduces CMRO2 and causes cerebral vasoconstriction. What is its net effect on CBF and ICP?",
   "answer":"Etomidate decreases both CBF and ICP (it is a potent direct cerebral vasoconstrictor in addition to reducing CMRO2).",
   "rationale":"Unlike volatile agents that may increase CBF, etomidate's cerebrovascular constriction parallels its metabolic suppression, making it useful for induction in patients with intracranial hypertension.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"ketamine"},

  {"id":"etomidate-pharmacology-d2","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"Despite reducing CMRO2, etomidate has mixed neuroprotection results. In what clinical scenario should its use prompt a specific risk assessment?",
   "answer":"Etomidate adrenocortical suppression in septic patients requires risk-benefit assessment; the mortality risk from single-dose etomidate in sepsis remains controversial but cannot be dismissed.",
   "rationale":"Etomidate inhibits 11-beta hydroxylase, suppressing cortisol synthesis; septic patients rely on the cortisol stress response -- any impairment may worsen hemodynamics and outcomes.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":145}],"confusable_with":""},

  {"id":"etomidate-pharmacology-d3","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"Etomidate shows excitatory EEG spikes more frequently than thiopental after induction. What is the clinical significance and how does it compare to methohexital?",
   "answer":"Etomidate produces excitatory EEG spikes (myoclonic movements); similar to methohexital, this can be used to facilitate seizure focus identification in epilepsy surgery -- it activates rather than suppresses epileptiform activity.",
   "rationale":"Most induction agents suppress EEG activity; etomidate and methohexital's excitatory properties enable epileptiform foci to manifest intraoperatively, aiding ECoG-guided resection.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"propofol or thiopental for epilepsy surgery"},

  {"id":"etomidate-pharmacology-d4","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"In older adult patients, what pharmacokinetic change affects etomidate dosing?",
   "answer":"The initial volume of distribution for etomidate significantly decreases with aging, so lower doses are required to achieve the same effect.",
   "rationale":"Reduced Vd means a given dose achieves a higher initial plasma concentration in elderly patients; dose reductions of 30-50% are appropriate to avoid prolonged effect.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1507}],"confusable_with":""},

  {"id":"etomidate-pharmacology-d5","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"In patients with kidney disease, how is etomidate pharmacology affected?",
   "answer":"The pharmacokinetics of etomidate are minimally affected by impaired kidney function; however, decreased protein binding in hypoalbuminemia may enhance its pharmacological effects.",
   "rationale":"Etomidate is highly protein-bound; in hypoalbuminemic renal patients, more free drug is available, intensifying and prolonging its CNS effects despite unchanged total drug clearance.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1102}],"confusable_with":""},

  {"id":"etomidate-pharmacology-d6","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"Etomidate is described as having minimal deleterious effects on cardiac function, making it useful in specific patient populations. Name two such patient groups.",
   "answer":"Etomidate is preferred for induction in patients with significant cardiac disease (e.g., valvular disease, reduced ejection fraction) and hemodynamically unstable patients because of its cardiovascular stability.",
   "rationale":"Unlike propofol (which causes vasodilation and cardiac depression) or ketamine (which is tachycardic), etomidate preserves heart rate, blood pressure, and cardiac output, making it ideal for cardiovascular compromise.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":144}],"confusable_with":"propofol"},

  {"id":"etomidate-pharmacology-d7","topic":topic17,"domain":dom_pharm,"discipline":disc,
   "stem":"Barbiturates can decrease ICP and have been used as an option for managing patients with space-occupying intracranial lesions. How do they compare to etomidate for neuroprotection from global vs focal ischemia?",
   "answer":"Barbiturates may provide neuroprotection from focal cerebral ischemia but probably not from global cerebral ischemia (cardiac arrest); etomidate's neuroprotection in humans remains unproven.",
   "rationale":"Both agents reduce CMRO2 maximally to burst suppression, protecting ischemic penumbra in focal ischemia; global ischemia without penumbra tissue is not amenable to metabolic suppression alone.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":139}],"confusable_with":""},
]

# =====================================================================
# [18] Femoral nerve and adductor canal blocks
# =====================================================================
topic18 = "Femoral nerve and adductor canal blocks"

kps += [
  {"id":"femoral-nerve-adductor-canal-blocks-d1","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"The femoral nerve block provides what sensory coverage, and why is the adductor canal block sometimes preferred for postoperative knee analgesia?",
   "answer":"Femoral nerve block covers the anterior thigh, medial leg, and medial ankle; adductor canal block is preferred for knee analgesia because it affects the quadriceps muscles to a lesser degree, facilitating ambulation.",
   "rationale":"Femoral nerve block causes significant quadriceps weakness (fall risk); adductor canal block at mid-thigh targets the saphenous nerve and other sensory branches with less motor blockade.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1667}],"confusable_with":""},

  {"id":"femoral-nerve-adductor-canal-blocks-d2","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"Patients with continuous adductor canal catheters after total knee arthroplasty have what functional advantage compared with femoral nerve catheters?",
   "answer":"Patients with continuous adductor canal catheters can ambulate further on the first postoperative day compared with femoral nerve catheter patients due to better-preserved quadriceps strength.",
   "rationale":"Preserved quadriceps function enables safe weight-bearing and early physical therapy -- critical for faster recovery after TKA and for preventing DVT.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1667}],"confusable_with":""},

  {"id":"femoral-nerve-adductor-canal-blocks-d3","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"For adductor canal block, where is the ultrasound transducer positioned and what anatomical target is identified?",
   "answer":"A high-frequency linear transducer is positioned transversely over the medial thigh, halfway between the ASIS and the superior patellar pole; the saphenous nerve lies anterior to the superficial femoral artery, deep to the sartorius muscle.",
   "rationale":"Accurate needle placement requires identifying the saphenous nerve in the subsartorial canal adjacent to the femoral artery; injection anterior to the artery achieves reliable sensory blockade.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1668}],"confusable_with":""},

  {"id":"femoral-nerve-adductor-canal-blocks-d4","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"An obturator nerve block is often added to femoral and sciatic blocks for knee analgesia. What is another specific indication for obturator nerve block?",
   "answer":"Obturator nerve block may also be performed to prevent adductor muscle spasms during transurethral bladder resection when a non-depolarizing muscle relaxant is undesirable.",
   "rationale":"The obturator nerve innervates the medial thigh adductors; electrical stimulation during TURB can trigger adductor spasm causing bladder injury -- blocking it prevents this complication.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1660}],"confusable_with":""},

  {"id":"femoral-nerve-adductor-canal-blocks-d5","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"Fascia iliaca block typically affects which nerve distributions, and how many tissue planes are traversed?",
   "answer":"Fascia iliaca block typically affects the femoral and lateral femoral cutaneous nerves (lateral thigh sensation); two pops are felt as the needle passes through the fascia lata and fascia iliaca.",
   "rationale":"The injection depot beneath the fascia iliaca allows local anesthetic to spread along the compartment investing the femoral, lateral femoral cutaneous, and sometimes obturator nerves.",
   "bloom":"recall","source":[{"book":"Stanford CA-1","page":98}],"confusable_with":"femoral nerve block"},

  {"id":"femoral-nerve-adductor-canal-blocks-d6","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"Single-shot and continuous femoral, adductor canal, and sciatic blocks can be safely performed in children using what guidance modality?",
   "answer":"These lower extremity blocks are easily performed in children using ultrasound guidance.",
   "rationale":"Ultrasound identifies nerve anatomy, vessel proximity, and fascial planes in real time, reducing the risk of inadvertent vascular injection and improving block accuracy in small patients.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1473}],"confusable_with":""},

  {"id":"femoral-nerve-adductor-canal-blocks-d7","topic":topic18,"domain":dom_regional,"discipline":disc,
   "stem":"Epinephrine may be added to peripheral nerve block solutions. What pharmacokinetic benefit does it provide?",
   "answer":"Epinephrine reduces the rate of systemic absorption of local anesthetic, thereby reducing peak plasma levels and potentially reducing local anesthetic systemic toxicity risk.",
   "rationale":"Alpha-1-mediated local vasoconstriction at the injection site slows vascular uptake; this prolongs block duration AND lowers systemic exposure, providing both efficacy and safety benefits.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":343}],"confusable_with":""},
]

# =====================================================================
# [19] Fentanyl, sufentanil, alfentanil: comparative pharmacology
# (Chunks are mostly MAC/propofol/aging content -- use what is relevant)
# =====================================================================
topic19 = "Fentanyl, sufentanil, alfentanil: comparative pharmacology"

kps += [
  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d1","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"Enhanced sensitivity to fentanyl, alfentanil, and sufentanil in elderly patients is due to what dual mechanism?",
   "answer":"Both pharmacokinetic factors (altered distribution/clearance) and pharmacodynamic factors (reduced receptor threshold) cause enhanced sensitivity to these opioids in older patients.",
   "rationale":"Aging reduces opioid clearance and increases brain sensitivity to opioids; the combination means elderly patients achieve greater effect at lower doses -- requiring approximate 50% dose reduction.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1507}],"confusable_with":""},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d2","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"Remifentanil has a uniquely context-insensitive pharmacokinetic profile. What does this mean clinically?",
   "answer":"The time necessary to achieve a 50% decrease in remifentanil plasma concentration (half-time) is very short and is NOT influenced by the duration of the infusion -- it is context-insensitive.",
   "rationale":"Remifentanil is metabolized by plasma and tissue esterases independently of liver/kidney function; this non-saturable elimination means offset is rapid and predictable regardless of infusion duration.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":307}],"confusable_with":"fentanyl context-sensitive half-time"},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d3","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"In patients with kidney disease, what specific consideration applies to opioids that depend on renal clearance?",
   "answer":"Meperidine and morphine, which are converted to active metabolites (normeperidine, morphine-6-glucuronide) excreted by kidneys, should be avoided in renal failure due to accumulation and toxicity.",
   "rationale":"Normeperidine accumulation causes neuroexcitatory effects (seizures, CNS stimulation); M6G accumulation causes narcosis and respiratory depression -- fentanyl lacks renally-cleared active metabolites.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":675}],"confusable_with":""},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d4","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"Fentanyl is preferred over other opioids in the elderly for what specific pharmacological reason?",
   "answer":"Fentanyl can be an ideal agent in elderly patients because there are fewer pharmacokinetic-related considerations and no active metabolites that accumulate.",
   "rationale":"Unlike morphine (M6G), meperidine (normeperidine), or codeine (morphine via CYP2D6), fentanyl metabolites are pharmacologically inactive, reducing unpredictable toxicity in patients with altered clearance.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":675}],"confusable_with":"morphine"},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d5","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"The end products of morphine and meperidine biotransformation are eliminated primarily where, and what fraction undergoes biliary excretion?",
   "answer":"Morphine and meperidine metabolites are eliminated primarily by the kidneys, with less than 10% undergoing biliary excretion.",
   "rationale":"Hepatic glucuronidation of morphine produces water-soluble metabolites that require renal excretion; accumulation in renal failure prolongs and intensifies opioid effect.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":307}],"confusable_with":""},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d6","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"Older adult patients require approximately what percentage reduction in propofol blood levels to achieve anesthesia compared with younger patients?",
   "answer":"Older adult patients require nearly 50% lower blood levels of propofol for anesthesia than younger patients.",
   "rationale":"Brain sensitivity to propofol increases with age due to altered GABA receptor function and reduced CNS inhibitory reserves; concurrent reduced clearance further amplifies effect at lower concentrations.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1507}],"confusable_with":""},

  {"id":"fentanyl-sufentanil-alfentanil-pharmacology-d7","topic":topic19,"domain":dom_pharm,"discipline":disc,
   "stem":"During target-controlled infusion (TCI) for propofol, the clinician enters what two patient parameters to set the desired effect-site concentration?",
   "answer":"For propofol TCI (e.g., Diprifusor), the clinician enters the patient's age and weight; the system uses pharmacokinetic modeling to deliver drug to achieve the desired blood concentration.",
   "rationale":"TCI algorithms (Marsh, Schnider models) use age and weight to estimate pharmacokinetic parameters; the pump adjusts infusion rate to maintain the target concentration at plasma or effect site.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":737}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
