import json, sys
sys.path.insert(0, 'data')
from build_kp_part6j import kps

disc = "anesthesia"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"

# =====================================================================
# [31] Head and neck blocks
# =====================================================================
topic31 = "Head and neck blocks"

kps += [
  {"id":"head-neck-blocks-d1","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"The stellate ganglion block selectively blocks sympathetic fibers to what body regions?",
   "answer":"Stellate ganglion block selectively blocks sympathetic fibers to the head, neck, and arm.",
   "rationale":"The stellate ganglion (inferior cervical + first thoracic ganglion fusion) is the major sympathetic relay for the upper extremity and head/neck; blocking it produces Horner's syndrome and upper extremity vasodilation.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":"brachial plexus block"},

  {"id":"head-neck-blocks-d2","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"Sympathetic innervation of the head, neck, and most of the arm derives from what cervical ganglia, and which is the largest?",
   "answer":"Sympathetic innervation derives from four cervical ganglia; the stellate ganglion is the largest.",
   "rationale":"The stellate ganglion is formed by fusion of the inferior cervical and first thoracic ganglia; its large size and location make it the primary target for sympathetic blockade of the upper body.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":""},

  {"id":"head-neck-blocks-d3","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"What are the primary indications for stellate ganglion block as a pain intervention?",
   "answer":"Stellate ganglion block is often used for patients with head, neck, arm, and upper chest pain syndromes.",
   "rationale":"Sympathetically maintained pain (including CRPS of the upper extremity, post-herpetic neuralgia, vascular insufficiency) can be partially or fully relieved by blocking sympathetic afferent and efferent pathways.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":""},

  {"id":"head-neck-blocks-d4","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"For primarily axial neck pain with extension into the head or shoulders, what diagnostic nerve block may clarify the pain source?",
   "answer":"Cervical medial branch blocks may clarify the diagnosis in patients with primarily axial pain in the neck with extension into the head or shoulders.",
   "rationale":"The cervical medial branches innervate the facet (zygapophyseal) joints; diagnostic blocks with short-acting local anesthetic confirm facetogenic pain, guiding radiofrequency ablation decisions.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1743}],"confusable_with":""},

  {"id":"head-neck-blocks-d5","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"Differential neural blockade is advocated for what diagnostic purpose in pain medicine, and what is a major limitation?",
   "answer":"Differential neural blockade aims to distinguish somatic, sympathetic, and psychogenic pain mechanisms; it is controversial because of challenges interpreting the data and inability to define exactly which fibers or pathways are blocked.",
   "rationale":"The concept relies on differential fiber sensitivity to local anesthetics (sympathetic B fibers block first, then sensory, then motor); in practice, concentrations and volumes overlap, making interpretation unreliable.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1799}],"confusable_with":""},

  {"id":"head-neck-blocks-d6","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"When a diagnostic nerve block provides pain relief, what is the practical consideration before proceeding to a neurolytic procedure?",
   "answer":"It may be more practical to obtain consent for a neurolytic procedure in advance and follow the diagnostic block immediately with chemical neurolysis if the diagnostic procedure provides pain relief.",
   "rationale":"Scheduling a separate neurolytic procedure after a positive diagnostic block creates logistical barriers and may delay treatment; combined consent and sequential procedures reduce patient burden.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1799}],"confusable_with":""},

  {"id":"head-neck-blocks-d7","topic":topic31,"domain":dom_regional,"discipline":disc,
   "stem":"When surgical infections spread along tissue planes and displace the airway, what intubation approach is indicated?",
   "answer":"In patients with airway-displacing deep neck infections and limited mouth opening, awake intubation (oral or nasal, using fiberoptic visualization, direct laryngoscopy, or video laryngoscopy) is indicated.",
   "rationale":"General anesthesia induction in a patient with severe trismus and displaced airway risks complete airway loss after apnea; awake techniques preserve spontaneous ventilation and allow real-time assessment.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":550}],"confusable_with":""},
]

# =====================================================================
# [32] Headache Syndromes - Pain Medicine Perspective
# =====================================================================
topic32 = "Headache Syndromes - Pain Medicine Perspective"

kps += [
  {"id":"headache-syndromes-pain-medicine-d1","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"Migraine is described as a genetically influenced complex neurological disorder. What is the typical character of migraine headache?",
   "answer":"Migraine is characterized by episodes of moderate-to-severe headache, typically unilateral and frequently accompanied by nausea and heightened sensitivity to light (photophobia) and sound (phonophobia).",
   "rationale":"The unilateral throbbing pain, photophobia, phonophobia, and nausea/vomiting distinguish migraine from tension-type headache; understanding this profile guides appropriate triptan vs NSAID vs antiemetic therapy.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Migraine  Acute & Preventive Treatment","page":2}],"confusable_with":"tension headache"},

  {"id":"headache-syndromes-pain-medicine-d2","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"PDPH (post-dural puncture headache) begins within what typical time frame and what proportion resolves spontaneously within 7 days?",
   "answer":"PDPH typically begins within 3 days of the dural puncture (two-thirds within the first 48 hours); spontaneous resolution occurs within 7 days in the majority of cases.",
   "rationale":"CSF leak through the dural defect reduces intracranial pressure; the sitting-up position worsens headache while lying flat relieves it; most dural holes seal with platelet and fibrin deposition within days.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"migraine"},

  {"id":"headache-syndromes-pain-medicine-d3","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"Epidural blood patch is the definitive treatment for PDPH. What conservative measures are tried first?",
   "answer":"Conservative management for PDPH includes supine positioning, hydration, caffeine, and oral analgesics; sumatriptan has varying effects.",
   "rationale":"Blood patch involves injecting autologous blood into the epidural space to form a clot over the dural defect; it is reserved for refractory or severe PDPH because conservative measures resolve most cases.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":""},

  {"id":"headache-syndromes-pain-medicine-d4","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"CRPS (complex regional pain syndrome) is an archetypal sympathetically mediated pain syndrome. What is the typical presentation and demographic?",
   "answer":"CRPS manifests as pain disproportionate to any inciting event in a distal extremity, usually after trauma or prolonged immobilization; females are more commonly affected (at least 2:1), with peaks in the early twenties and mid-thirties.",
   "rationale":"CRPS involves neurogenic inflammation, autonomic dysfunction, and central sensitization; the disproportionate pain and allodynia in a peripheral distribution are pathognomonic features.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":825}],"confusable_with":"peripheral neuropathy"},

  {"id":"headache-syndromes-pain-medicine-d5","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"Spinal cord stimulation (SCS) is a neuromodulation technique for chronic pain. What is its proposed mechanism of action?",
   "answer":"SCS interrupts ascending pain input by activation of nonpainful signals; traditional SCS places electrodes in the dorsal epidural space to deliver electrical impulses that modulate pain transmission.",
   "rationale":"Activation of large-diameter A-beta fibers by SCS inhibits nociceptive C-fiber transmission at the dorsal horn (gate control theory); modern theories also involve GABA release and reduced excitatory amino acids.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":831}],"confusable_with":""},

  {"id":"headache-syndromes-pain-medicine-d6","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"Subarachnoid hemorrhage (SAH) classically presents with what specific headache description that distinguishes it from migraine?",
   "answer":"SAH presents with a sudden, severe 'thunderclap' headache often described as the 'worst headache of my life,' unlike the gradual onset and prodrome of migraine.",
   "rationale":"Aneurysmal rupture causes a sudden spike in CSF pressure; the instantaneous onset distinguishes SAH from all other headache types and mandates immediate CT/LP to exclude this life-threatening cause.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)","page":1}],"confusable_with":"migraine with aura"},

  {"id":"headache-syndromes-pain-medicine-d7","topic":topic32,"domain":dom_pain,"discipline":disc,
   "stem":"In the biopsychosocial model of chronic pain, psychological factors are considered part of a bidirectional link. What specific psychological factors are strongest predictors of pain chronification?",
   "answer":"Anxiety, mood disorders, and negative cognitive processes such as pain catastrophizing are among the strongest predictors of chronification of pain.",
   "rationale":"These factors activate descending pain facilitation pathways, maintain central sensitization, and drive avoidance behaviors that perpetuate disability; addressing them is essential to comprehensive chronic pain management.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":826}],"confusable_with":""},

  {"_type":"illness_script","topic":topic32,"discipline":disc,
   "enabling_conditions":"Female sex (migraine), family history (migraine), prior dural puncture (PDPH), aneurysmal subarachnoid hemorrhage history (SAH), extremity trauma (CRPS)",
   "pathophysiology":"Migraine: trigeminal sensitization + cortical spreading depression; PDPH: CSF leak causing intracranial hypotension; SAH thunderclap: sudden ICP spike from aneurysm rupture; CRPS: peripheral and central sensitization with autonomic dysregulation",
   "time_course":"Migraine: hours to days, recurrent; PDPH: onset within 48-72h post-procedure, typically resolves 7 days; SAH: sudden onset, maximal at onset; CRPS: weeks to months after injury, may persist years",
   "key_features":"Migraine: unilateral throbbing, photo/phonophobia, nausea; PDPH: positional headache (worse upright, better supine); SAH: worst headache of life sudden onset; CRPS: disproportionate pain, allodynia, autonomic changes in distal limb",
   "consequence_if_missed":"SAH: rebleeding, vasospasm, death (50% mortality untreated); PDPH: meningitis if untreated dural leak; CRPS: irreversible functional loss if not treated early"},
]

# =====================================================================
# Write final output
# =====================================================================
# Add confusable pairs
pairs = [
  {"_type":"confusable_pair","topic_a":"DPE (dural puncture epidural)","topic_b":"CSE (combined spinal-epidural)","discriminator":"DPE punctures dura without injecting intrathecally; CSE injects drug through the spinal needle -- DPE has less pruritus/uterine tachysystole/fetal bradycardia than CSE"},
  {"_type":"confusable_pair","topic_a":"Femoral nerve block","topic_b":"Adductor canal block","discriminator":"Femoral block provides motor + sensory block (quadriceps weakness, fall risk); adductor canal is predominantly sensory-sparing of quadriceps, enabling ambulation after TKA"},
  {"_type":"confusable_pair","topic_a":"Migraine","topic_b":"Subarachnoid hemorrhage","discriminator":"SAH is sudden-onset 'thunderclap' at maximal intensity immediately; migraine builds gradually over minutes-hours with prodrome; SAH requires CT/LP to exclude"},
  {"_type":"confusable_pair","topic_a":"PDPH (post-dural puncture headache)","topic_b":"Migraine","discriminator":"PDPH is positional (worse upright, better supine) and onset within 72h of a dural puncture; migraine is not positional and unrelated to procedure"},
  {"_type":"confusable_pair","topic_a":"Vasogenic cerebral edema","topic_b":"Cytotoxic cerebral edema","discriminator":"Vasogenic: BBB disruption allows protein-rich fluid into interstitium -- responds to corticosteroids; Cytotoxic: intracellular water accumulation from ischemia -- does NOT respond to steroids"},
]
kps += pairs

output_path = 'data/kp_redeep_part_6.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Validate and report
kp_items = [x for x in kps if '_type' not in x]
script_items = [x for x in kps if x.get('_type') == 'illness_script']
pair_items = [x for x in kps if x.get('_type') == 'confusable_pair']

print(f"Total items: {len(kps)}")
print(f"KPs: {len(kp_items)}")
print(f"Illness scripts: {len(script_items)}")
print(f"Confusable pairs: {len(pair_items)}")

# Verify JSON parses back correctly
with open(output_path, 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f"Parse verification: {len(verify)} items -- OK")

# Count unique topics
topics = set()
for x in kp_items:
    topics.add(x.get('topic',''))
print(f"Unique topics covered: {len(topics)}")
print("part 6: 33 topics,", len(kp_items), "KPs,", len(script_items), "scripts,", len(pair_items), "pairs, parses OK")
