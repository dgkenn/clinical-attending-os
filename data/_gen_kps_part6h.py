import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch7.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [30] Halogenated volatile agents: pharmacokinetics
# Chunks mostly off-topic; use available MAC/volatile content
# ============================================================
t = "Halogenated volatile agents: pharmacokinetics"
dom = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
disc = "anesthesia"
s = "volatile-pk"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"Why do infants have faster inhalation induction with halogenated agents than adults?",
 "answer":"Greater minute ventilation-to-FRC ratio in infants + greater brain blood flow speeds rise in alveolar concentration; MAC for halogenated agents is GREATER in infants than in neonates and adults",
 "rationale":"Infants' MV:FRC ratio is higher because their tidal volume is relatively larger compared to their small FRC; rapid alveolar washout quickly elevates alveolar partial pressure.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the key relationship between MAC values for MAC-awake, MAC (immobility), MAC-BAR, and MAC-EI?",
 "answer":"MAC-awake ~0.4 MAC (prevent verbal response); MAC (immobility) = 1.0 MAC (standard); MAC-EI ~1.3 MAC (prevent laryngeal response/movement 95%); MAC-BAR ~1.5-1.7 MAC (blunt autonomic response)",
 "rationale":"Progressive CNS suppression requires increasing concentrations; MAC-EI is 30% above standard MAC, relevant for intubation under inhalational anesthesia.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":23}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"How do benzodiazepines modify volatile anesthetic requirement and what is the clinical significance?",
 "answer":"Benzodiazepines reduce the MAC of volatile anesthetics by as much as 30%; clinically used as premedication to reduce induction doses and lower the volatile agent requirement",
 "rationale":"GABA-A potentiation by benzodiazepines reduces the concentration of volatile agent needed to prevent movement; additive CNS depression at GABA receptors.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":284}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In pediatric patients undergoing inhalational anesthesia, what additional monitoring is critical and why?",
 "answer":"Temperature monitoring is critical in pediatric patients because of greater risk for malignant hyperthermia AND greater susceptibility to both intraoperative hypothermia and hyperthermia",
 "rationale":"Children have high surface area-to-volume ratio (predisposes to hypothermia) and are the primary population for MH triggers with potent volatile agents.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What factors alter the kinetics of CBF changes with prolonged volatile agent administration?",
 "answer":"CBF increase with volatile agents appears time-dependent; with continued administration (2-5 hours), blood flow begins to return toward normal",
 "rationale":"Autoregulatory mechanisms partially adapt over time, reducing the initial vasodilatory effect of volatile agents on CBF with prolonged exposure.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":949}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What effect do volatile anesthetics have on cognitive dysfunction when compared with IV anesthesia in the first week after surgery?",
 "answer":"Studies comparing volatile with IV anesthesia show worse cognitive function with volatile anesthesia within 1 week; at 3 months, volatile vs. neuraxial anesthesia show similar cognitive dysfunction rates",
 "rationale":"Short-term post-volatile cognitive effects may reflect residual agent effects; longer-term POCD appears related to surgical/anesthetic factors beyond specific agent choice.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":124}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What postprandial change in blood composition slows inhalational induction and why?",
 "answer":"Postprandial lipidemia increases the overall blood:gas partition coefficient of volatile agents by increasing fat in blood, slowing induction by providing a larger blood reservoir for the agent",
 "rationale":"Lipids dissolve volatile anesthetics (fat:blood coefficient >1); more fat in blood means more agent must be dissolved before alveolar concentration rises to equilibrium.",
 "bloom":"analyze","source":[{"book":"Stanford CA-1","page":19}],"confusable_with":""},
]

# ============================================================
# [31] Head and neck blocks
# ============================================================
t = "Head and neck blocks"
dom = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"
disc = "anesthesia"
s = "head-neck-blocks"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the stellate ganglion block used for and what anatomical structures does it denervate?",
 "answer":"Stellate ganglion block selectively blocks sympathetic fibers to the head, neck, and arm; indications: reflex sympathetic dystrophy, visceral pain, acute herpetic neuralgia, head/neck/arm/upper chest pain",
 "rationale":"The stellate ganglion is the largest of the four cervical sympathetic ganglia; its block interrupts sympathetic-mediated vasoconstriction and pain amplification in the upper extremity.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785},{"book":"Morgan & Mikhail","page":1799}],"confusable_with":"Brachial plexus block (motor/sensory, not sympathetic)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What sympathetic anatomical structure innervates the head, neck, and most of the arm?",
 "answer":"Sympathetic innervation of head, neck, and most of the arm is derived from four cervical ganglia; the largest is the stellate ganglion",
 "rationale":"The cervical sympathetic chain runs along the prevertebral fascia; the stellate ganglion is formed by the fusion of the inferior cervical and first thoracic ganglia.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the common indications for sympathetic nerve blocks in pain medicine?",
 "answer":"Reflex sympathetic dystrophy (CRPS), visceral pain, acute herpetic neuralgia, and providing long-term pain relief for sympathetically maintained pain",
 "rationale":"Sympathetic blocks interrupt the aberrant sympathetic amplification of pain; diagnostic blocks identify sympathetically maintained pain before neurolytic procedures.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1785}],"confusable_with":"Somatic nerve blocks (sensory/motor, not sympathetic)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"For axial neck pain with extension to the head or shoulders, what diagnostic block clarifies the pain source?",
 "answer":"Cervical medial branch blocks may clarify the diagnosis for primarily axial neck pain extending to the head or shoulders (from cervical facet joint origin)",
 "rationale":"Cervical facet joints are innervated by the medial branch of the dorsal ramus; diagnostic blocks confirm facet origin before proceeding to radiofrequency ablation.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1743}],"confusable_with":"Epidural steroid injection (for radicular/foraminal pain)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What intubation challenge is created by deep space neck infections involving tissue plane spread?",
 "answer":"Deep space neck infections can spread along tissue planes, displacing the airway; limited mouth opening and trismus restrict access; CT is needed to characterize spread; awake fiberoptic or video laryngoscopy is indicated",
 "rationale":"Airway displacement by infection and trismus can make direct laryngoscopy impossible; awake flexible endoscopy allows airway securing before muscle relaxants eliminate spontaneous ventilation.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":550}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the advantage of performing a diagnostic block IMMEDIATELY before a planned neurolytic procedure?",
 "answer":"Obtaining consent for neurolytic procedure in advance allows following the diagnostic block immediately with chemical neurolysis if diagnostic procedure results in pain relief, avoiding a second procedure",
 "rationale":"Immediate sequential diagnostic-to-neurolytic approach confirms efficacy and reduces patient burden; the pain relief from diagnostic block predicts neurolytic outcome.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1799}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the mild-to-moderate stenosis radicular symptom management options before surgery?",
 "answer":"Mild-to-moderate spinal stenosis with radicular symptoms: epidural steroid injections (transforaminal, interlaminar, or caudal approaches) may help tolerate physical therapy; MILD procedure for moderate-severe; multilevel severe warrants surgical decompression",
 "rationale":"ESI reduces radicular inflammation in the neuroforamen; the MILD procedure percutaneously reduces central canal compression without open surgery.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1743}],"confusable_with":""},
]

# ============================================================
# [32] Headache Syndromes - Pain Medicine Perspective
# ============================================================
t = "Headache Syndromes — Pain Medicine Perspective"
dom = "Acute and chronic pain (acute pain management, chronic pain, CRPS, neuropathic pain, opioid therapy, interventional pain, psychological aspects)"
disc = "anesthesia"
s = "headache-syndromes"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the clinical definition of migraine and what are its distinguishing features?",
 "answer":"Migraine: genetically influenced complex neurological disorder; episodes of moderate-to-severe, typically UNILATERAL headache frequently accompanied by nausea and heightened sensitivity to light and sound",
 "rationale":"Unilaterality reflects trigeminovascular activation and cortical spreading depression; nausea and photophobia result from brainstem and cortical involvement in the migraine circuit.",
 "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Migraine  Acute & Preventive Treatment","page":2}],"confusable_with":"Tension headache (bilateral, no nausea/photophobia)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the classic presentation of subarachnoid hemorrhage (SAH) headache and what is its pathophysiology?",
 "answer":"SAH: thunderclap headache (sudden, severe, described as worst headache of life) with nausea/vomiting and meningismus; caused by aneurysm rupture -> blood in subarachnoid space causing meningeal irritation",
 "rationale":"Blood in the subarachnoid space rapidly increases ICP and causes meningeal irritation explaining the sudden onset and severity; neck stiffness from meningism follows.",
 "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)","page":1}],"confusable_with":"Migraine (can be severe but not thunderclap onset; no meningismus)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the PDPH presentation and what distinguishes it from other postoperative headaches?",
 "answer":"PDPH: positional bilateral headache onset within 3 days of neuraxial procedure; worse when upright, better when supine; caused by CSF leak through dural defect lowering CSF pressure",
 "rationale":"Postural exacerbation with relief supine is the hallmark distinguishing PDPH from other headaches; reduced CSF pressure allows brain sagging that stretches pain-sensitive meningeal structures.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":"Migraine (not position-dependent); tension headache (not position-dependent)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is spinal cord stimulation (SCS) and through what mechanism does it provide pain relief?",
 "answer":"SCS: placement of electrodes in the dorsal epidural space (percutaneous or surgical paddle) delivering electrical impulses; mechanism includes interruption of ascending pain input by activating nonpainful signals (gate control theory)",
 "rationale":"The traditional gate control mechanism activates large-diameter A-beta fibers that inhibit pain transmission in the dorsal horn; modern understanding also includes supraspinal effects.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":831}],"confusable_with":"Peripheral nerve stimulation (electrodes on peripheral nerve, not epidural space)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"How do large unruptured cerebral aneurysms cause neurological signs compared to ruptured aneurysms?",
 "answer":"Large unruptured aneurysms compress adjacent cerebral tissue causing neurological signs; rupture creates reduced blood flow and vasospasm leading to cerebral ischemia; pathophysiological mechanisms of formation/rupture involve hemodynamic stress to vessel wall",
 "rationale":"Unruptured aneurysms act as mass lesions; ruptured aneurysms trigger vasospasm (delayed cerebral ischemia) days later as the major cause of post-SAH morbidity.",
 "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)","page":4}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What conservative measures are first-line for PDPH and when does epidural blood patch become indicated?",
 "answer":"Conservative: supine positioning, hydration, caffeine, oral analgesics (sumatriptan has varying effects); blood patch is definitive therapy for severe or persistent PDPH - 90% initial improvement rate",
 "rationale":"Conservative measures work for mild PDPH; blood patch is reserved for severe cases limiting function or those not responding to 24-48 hours of conservative management.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":336}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What features distinguish CRPS from simple neuropathic pain from a nerve injury?",
 "answer":"CRPS: pain disproportionate to inciting event in distal extremity (usually after trauma/immobilization); CRPS type 1 = no clear peripheral nerve injury; CRPS type 2 = clear nerve injury; autonomic features (vasomotor, sudomotor changes) present",
 "rationale":"The disproportionate severity and autonomic component of CRPS distinguish it from simple post-traumatic neuropathy; central sensitization and sympathetic involvement are prominent.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":825}],"confusable_with":"Post-traumatic neuropathic pain (proportionate to injury, no autonomic features)"},
]

kps.append({"_type":"confusable_pair","topic_a":"Subarachnoid hemorrhage headache","topic_b":"Migraine",
 "discriminator":"SAH: thunderclap onset (seconds to peak severity), meningismus, no prior similar headaches, loss of consciousness possible; Migraine: gradual build-up over minutes to hours, prior similar attacks, no meningismus"})

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch8.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 8 saved OK")
