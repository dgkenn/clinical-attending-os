import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch1.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch1")

# ============================================================
# ITEM 8: Myelitis & Inflammatory Spinal Cord Disease
# CHUNKS are GBS/AIDP electrodiagnostic content
# ============================================================
topic = "Myelitis & Inflammatory Spinal Cord Disease"
domain = "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)"
disc = "medicine"

kps += [
  {"id":"myelitis-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Guillain-Barre syndrome (AIDP) results from what pathophysiological mechanism, and what is the most common variant in North America?",
   "answer":"Immunological reaction causing molecular mimicry between peripheral nerve myelin components and microbial/viral antigens; AIDP is the most common variant (~75% of GBS cases in North America).",
   "rationale":"GBS follows infection in ~70% of cases; molecular mimicry between pathogen antigens and gangliosides triggers peripheral nerve antibody-mediated demyelination.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Myelitis & Inflammatory Spinal Cord Disease","page":1}],"confusable_with":""},
  {"id":"myelitis-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"On electrodiagnostic testing of AIDP, what EMG finding in neuropathic lesions indicates delayed recruitment?",
   "answer":"Delayed (reduced) motor unit recruitment on EMG in voluntary contraction indicates neuropathic/axonal disorder; fewer motor units fire at higher force than expected.",
   "rationale":"In neuropathy, loss of axons reduces the number of available motor units; remaining units fire at high frequency to compensate but total number is reduced.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Myelitis & Inflammatory Spinal Cord Disease","page":5}],"confusable_with":"Myopathy (early recruitment)"},
  {"id":"myelitis-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In AIDP, what is the classic CSF finding and when may it be absent early in the disease?",
   "answer":"Albuminocytological dissociation (elevated protein with normal or near-normal cell count); may be absent in the first 3 weeks of disease course.",
   "rationale":"CSF protein elevation reflects breakdown of the blood-nerve barrier from widespread root demyelination; early in disease, this process is still evolving.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Myelitis & Inflammatory Spinal Cord Disease","page":2}],"confusable_with":""},
  {"id":"myelitis-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"On nerve conduction studies in AIDP, what amplitude finding may signal reinnervation from chronic neuropathic lesions rather than acute demyelination?",
   "answer":"High-amplitude motor unit potentials on EMG signal reinnervation (collateral sprouting from surviving axons in chronic neuropathic lesions); this contrasts with the normal or reduced amplitudes of acute demyelination.",
   "rationale":"Chronic denervation-reinnervation results in enlarged motor units as surviving axons sprout to reinnervate adjacent denervated muscle fibers.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Myelitis & Inflammatory Spinal Cord Disease","page":5}],"confusable_with":""},
  {"id":"myelitis-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the key upper motor neuron (UMN) finding that localizes a spinal cord lesion versus a peripheral nerve process?",
   "answer":"UMN signs: spasticity, increased tone, hyperreflexia, positive Babinski; peripheral process: flaccidity, decreased reflexes, fasciculations. Spinal cord disease causes UMN signs below the lesion level.",
   "rationale":"The distinction between UMN (corticospinal tract) and LMN (anterior horn/peripheral nerve) pathology drives localization and guides further imaging/workup.",
   "bloom":"analyze","source":[{"book":"MGH Housestaff Manual","page":203}],"confusable_with":""},
  {"id":"myelitis-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In acute inflammatory demyelinating polyneuropathy, what feature indicates bulbar involvement and what is the respiratory concern?",
   "answer":"Bulbar involvement (cranial nerve involvement causing dysarthria, dysphagia, facial weakness) is common in GBS and signals imminent respiratory muscle paralysis; close monitoring of forced vital capacity is mandatory.",
   "rationale":"Ascending paralysis in GBS reaches the diaphragm and accessory muscles; bulbar signs predict more extensive cranial nerve/respiratory involvement requiring ICU monitoring.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1010}],"confusable_with":""},
]

# ============================================================
# ITEM 9: Neuro-ophthalmology Essentials
# CHUNKS are respiratory physiology — very thin for topic
# Produce 4 KPs only
# ============================================================
topic = "Neuro-ophthalmology Essentials"
domain = "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)"
disc = "medicine"

kps += [
  {"id":"neuroophthalmology-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What intraoperative concern is specific to patients with ocular disease requiring awake endotracheal intubation, and how is this weighed against aspiration risk?",
   "answer":"Awake intubation increases intraocular pressure (IOP) which can be catastrophic in open-globe injuries; this risk must be weighed against the aspiration risk of a full stomach — ideally delay surgery until aspiration risk decreases.",
   "rationale":"Coughing, crying, and laryngoscopy dramatically increase IOP; open-globe injury risks vitreous extrusion with even moderate IOP spikes.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":576}],"confusable_with":""},
  {"id":"neuroophthalmology-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the tradeoff between deep versus awake extubation in a patient with a repaired eye injury at risk from increased intraocular pressure?",
   "answer":"Deep extubation avoids coughing/straining and IOP spikes but risks loss of airway control; awake extubation is safer for airway but increases IOP from coughing. IV lidocaine or dexmedetomidine can blunt cough response during awake emergence.",
   "rationale":"Both awake and deep extubation carry risks in the eye patient; pharmacological attenuation of cough response with lidocaine/dexmedetomidine is a middle-ground strategy.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1290}],"confusable_with":""},
  {"id":"neuroophthalmology-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"The succinylcholine-related IOP increase is relevant in which ophthalmic emergency?",
   "answer":"Open-globe (penetrating eye) injury — succinylcholine transiently raises IOP by 5-10 mmHg from extraocular muscle contraction, risking vitreous extrusion. Risk must be weighed against benefits of RSI in full-stomach patients.",
   "rationale":"The brief IOP spike from succinylcholine may be outweighed by the catastrophic risk of aspiration if rapid sequence is not achieved; the debate is ongoing but many use modified RSI with rocuronium.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":576}],"confusable_with":""},
  {"id":"neuroophthalmology-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Epistaxis requiring surgical management has what anesthetic emergence concern specific to the nasal/oropharyngeal blood field?",
   "answer":"Patient must be fully awake with intact airway reflexes before extubation to prevent aspiration of blood; coughing on ETT during emergence may be difficult to avoid in the awakening patient but IV lidocaine or dexmedetomidine can help.",
   "rationale":"Blood in the oropharynx from epistaxis poses ongoing aspiration risk; deep extubation is relatively contraindicated due to the blood-contaminated field.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1290}],"confusable_with":""},
]

# ============================================================
# ITEM 10: Neurocritical Care Emergencies
# ============================================================
topic = "Neurocritical Care Emergencies"
domain = "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)"
disc = "medicine"

kps += [
  {"id":"neurocrit-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Any trauma patient with altered consciousness must be assumed to have what condition until proven otherwise, and what is the most reliable clinical assessment tool?",
   "answer":"Traumatic brain injury (TBI); the Glasgow Coma Scale (GCS) is the most reliable clinical tool for determining TBI significance.",
   "rationale":"Altered consciousness after trauma mandates TBI workup; the GCS quantifies level of consciousness and guides triage, monitoring, and prognostication.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1336}],"confusable_with":""},
  {"id":"neurocrit-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Cerebral perfusion pressure monitoring requires zeroing the arterial line at what anatomical reference level?",
   "answer":"The external auditory meatus (at the level of the circle of Willis) — zeroing at this level gives true MAP at the brain rather than at the heart level.",
   "rationale":"CPP = MAP - ICP; accurate MAP measurement requires zeroing at brain level (not heart level) to correctly calculate cerebral perfusion in the upright or head-up position.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":415}],"confusable_with":""},
  {"id":"neurocrit-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In MRI for head-injured patients requiring sedation, what airway management concern is paramount?",
   "answer":"Loss of airway control from deep sedation could be catastrophic in head-injured patients; general anesthesia with controlled airway may be preferable to deep sedation in this population despite logistic challenges.",
   "rationale":"Head-injured patients have impaired airway reflexes and elevated ICP; loss of airway leads to hypercapnia, hypoxia, and worsened cerebral injury.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":219}],"confusable_with":""},
  {"id":"neurocrit-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Botulinum toxin produces clinical botulism through what mechanism, and what concern exists regarding bioterrorism?",
   "answer":"Botulinum toxin blocks acetylcholine release at the NMJ causing descending flaccid paralysis; aerosolized botulinum toxin is a potential bioterrorism agent with a very low median lethal dose.",
   "rationale":"Botulinum toxin is the most potent known toxin; its inhibition of presynaptic ACh vesicle fusion causes irreversible NMJ blockade until nerve sprouting regenerates the junction.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1039}],"confusable_with":"Myasthenia gravis"},
  {"id":"neurocrit-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In the past, critically ill patients with delirium were managed with restraints, sedatives, or paralytics — what are the recognized adverse consequences of these approaches?",
   "answer":"Restraints are inhumane except as last resort; prolonged propofol infusion causes propofol infusion syndrome (especially in children); sedation and paralysis are associated with prolonged ICU stay, muscle wasting, and PTSD.",
   "rationale":"The shift to sedation minimization, early mobilization, and delirium prevention (ABCDEF bundle) was driven by recognizing these harms of heavy sedation and restraint.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},
  {"id":"neurocrit-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the three aspects of airway management that must be simultaneously considered in any head-injured trauma patient?",
   "answer":"(1) Need for basic life support/airway intervention; (2) presumed cervical spinal cord injury until proven otherwise; (3) potential for failed endotracheal intubation.",
   "rationale":"These three concurrent challenges define the neurocritical care airway approach: secure the airway while protecting the cervical spine and having a backup plan for failed intubation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1322}],"confusable_with":""},
]

# ============================================================
# ITEM 11: Peripheral Neuropathy
# ============================================================
topic = "Peripheral Neuropathy"
domain = "Internal medicine: neurology (ischemic & hemorrhagic stroke, seizures & status epilepticus, altered mental status & delirium, headache, neuromuscular weakness, spinal cord syndromes)"
disc = "medicine"

kps += [
  {"id":"peripheral-neuropathy-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most common diabetic neuropathy syndrome and what is its sensory distribution?",
   "answer":"Symmetric distal polyneuropathy producing numbness, paresthesia, dysesthesia, and pain in a stocking-and-glove distribution; pain is often worst at night.",
   "rationale":"Hyperglycemia causes metabolic and ischemic injury to the longest nerve fibers first (distal symmetrical pattern), explaining the stocking-glove distribution.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1746}],"confusable_with":"Radiculopathy (dermatomal distribution)"},
  {"id":"peripheral-neuropathy-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Loss of proprioception in diabetic peripheral neuropathy leads to what functional consequence?",
   "answer":"Gait disturbances from loss of proprioceptive feedback; sensory deficits lead to repetitive traumatic injuries (Charcot foot, pressure ulcers) due to painless trauma.",
   "rationale":"Proprioceptive loss impairs the reflexive corrections that maintain balance; combined with loss of protective pain sensation, it creates a cycle of unrecognized repeated trauma.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1746}],"confusable_with":""},
  {"id":"peripheral-neuropathy-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is neuropathic pain's classical quality and associated phenomenon of painful response to normally innocuous stimuli?",
   "answer":"Neuropathic pain is classically paroxysmal, lancinating, burning, and associated with hyperpathia (painful response to normally innocuous stimuli); when associated with sensory loss it is called deafferentation pain.",
   "rationale":"Ectopic discharges from injured nerves produce spontaneous and stimulus-evoked pain; the abnormal amplification of normal stimuli (hyperpathia/allodynia) distinguishes neuropathic from nociceptive pain.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1710}],"confusable_with":"Nociceptive pain"},
  {"id":"peripheral-neuropathy-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Pregabalin is FDA-approved for treatment of what specific peripheral neuropathy syndrome?",
   "answer":"Diabetic peripheral neuropathy (and fibromyalgia); it is also widely prescribed for other neuropathic pain states by blocking alpha-2-delta subunit of voltage-gated calcium channels.",
   "rationale":"Pregabalin and gabapentin reduce calcium-dependent neurotransmitter release at hyperexcitable synapses, attenuating central sensitization in neuropathic pain.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1761}],"confusable_with":""},
  {"id":"peripheral-neuropathy-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In a diabetic patient undergoing surgery, what perioperative neuropathy risk requires documentation in the consent process?",
   "answer":"Preexisting diabetic neuropathy increases vulnerability to positioning injuries and regional anesthetic nerve injury; documentation of baseline neurological deficits is essential before regional techniques.",
   "rationale":"A diabetic nerve already injured by hyperglycemia is more vulnerable to additional ischemic, compressive, or neurotoxic injury from regional anesthesia or prolonged positioning.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1220}],"confusable_with":""},
  {"id":"peripheral-neuropathy-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Regional anesthesia closed claims analysis identifies what as the leading cause of peripheral nerve injury in the obstetric population?",
   "answer":"Peripheral nerve injuries in obstetrics are most commonly from obstetrical (positioning/compression) rather than anesthetic causes; early neurological consultation is recommended to determine causation.",
   "rationale":"The lithotomy position, prolonged labor, and fetal head compression injure lumbosacral plexus and common peroneal nerve far more often than regional anesthetic techniques.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":2020}],"confusable_with":""},
  {"id":"peripheral-neuropathy-d7","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Abnormally elevated HbA1c predicts what perioperative complication related to peripheral neuropathy?",
   "answer":"HbA1c elevation identifies poor long-term glucose control; these patients are more likely to have preexisting neuropathy, hyperglycemia on the day of surgery, and increased risk of adverse outcomes and complications.",
   "rationale":"Chronic hyperglycemia causes cumulative nerve injury; high HbA1c at surgery predicts both more advanced neuropathy and poor perioperative glycemic control.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1220}],"confusable_with":""},
]

# ============================================================
# ITEM 12: Post-ICU Syndrome & ICU Rehabilitation
# CHUNKS are mostly SCCM guideline references and non-specific content
# ============================================================
topic = "Post-ICU Syndrome & ICU Rehabilitation"
domain = "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)"
disc = "medicine"

kps += [
  {"id":"pics-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the three domains of impairment encompassed by post-intensive care syndrome (PICS)?",
   "answer":"Physical (muscle weakness, functional impairment), cognitive (memory, attention, executive function deficits), and psychiatric (PTSD, depression, anxiety) — all persisting after ICU discharge.",
   "rationale":"PICS reflects the multi-system consequences of critical illness, sedation, immobility, and ICU environmental stressors; recognition requires screening in all three domains.",
   "bloom":"recall","source":[{"book":"Society Guideline","page":78}],"confusable_with":""},
  {"id":"pics-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What novel approach to PICS rehabilitation has been developed through SCCM's THRIVE initiative?",
   "answer":"Peer support models — connecting ICU survivors with trained peer supporters who have personal ICU experience — have been developed to address psychological sequelae of PICS.",
   "rationale":"Peer support leverages lived experience to reduce isolation, normalize symptoms, and provide mentorship that healthcare providers cannot offer; THRIVE International peer support collaborative documented this approach.",
   "bloom":"recall","source":[{"book":"Society Guideline","page":78}],"confusable_with":""},
  {"id":"pics-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What communication and information transfer failure at hospital discharge contributes to poor post-ICU outcomes?",
   "answer":"Deficits in communication and information transfer between hospital-based and primary care physicians — discharge summary gaps leave PCPs uninformed about ICU events, medications, and follow-up needs.",
   "rationale":"ICU survivors have complex ongoing needs; incomplete information transfer to primary care and patients themselves contributes to medication errors, missed follow-up, and unaddressed PICS.",
   "bloom":"apply","source":[{"book":"Society Guideline","page":80}],"confusable_with":""},
  {"id":"pics-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Prolonged propofol infusion, particularly in children, causes what potentially fatal syndrome?",
   "answer":"Propofol infusion syndrome (PRIS) — manifests as metabolic acidosis, rhabdomyolysis, cardiac dysfunction, renal failure, and hepatomegaly; often fatal; avoid propofol infusions >4 mg/kg/h for prolonged periods.",
   "rationale":"Propofol impairs mitochondrial respiratory chain function; prolonged infusion causes catastrophic mitochondrial failure in multiple organs.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},
  {"id":"pics-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the recommended approach to ICU delirium management that replaced restraints and heavy sedation?",
   "answer":"The ABCDEF bundle: Assess/treat pain, Both SAT and SBT daily, Choice of sedation (minimize benzodiazepines), Delirium monitoring/management, Early mobility, Family engagement.",
   "rationale":"ABCDEF bundle implementation reduces ICU LOS, ventilator days, delirium, and mortality by prioritizing awakening, mobility, and family involvement over sedation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},
  {"id":"pics-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Flumazenil used to reverse benzodiazepine sedation has what important pharmacokinetic limitation requiring monitoring after discharge?",
   "answer":"Flumazenil has a short half-life due to rapid hepatic clearance; repeat doses may be needed after 1-2 hours to avoid re-sedation; liver failure prolongs both flumazenil and benzodiazepine clearance.",
   "rationale":"Re-sedation after flumazenil is a patient safety hazard; patients must not be discharged after flumazenil reversal without monitoring for re-emergence of sedation.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":467}],"confusable_with":""},
]

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch2.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch2")
