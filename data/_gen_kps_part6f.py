import json

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch5.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# ============================================================
# [24] GERD, gastroparesis, and upper GI disease
# ============================================================
t = "GERD, gastroparesis, and upper GI disease"
dom = "Perioperative medicine (preoperative assessment, risk stratification, premedication, ERAS, fluid management, temperature, positioning, post-op care)"
disc = "anesthesia"
s = "gerd-gastroparesis"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the mechanism by which metoclopramide reduces aspiration risk, and how is its prokinetic action mediated?",
 "answer":"Metoclopramide acts peripherally as a cholinomimetic (facilitates ACh at selective muscarinic receptors) and centrally as a dopamine receptor antagonist; increases lower esophageal sphincter tone, speeds gastric emptying, lowers gastric fluid volume; action not dependent on vagal innervation but abolished by anticholinergics",
 "rationale":"Enhancing gastric motility reduces the volume of gastric contents available for aspiration; LES tone increase reduces passive reflux.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":446}],"confusable_with":"H2 blockers (reduce acid pH but do not empty stomach)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the four risk factors for pulmonary aspiration in the perioperative patient?",
 "answer":"Intra-abdominal process (bowel obstruction, ileus, inflammation); gastroparesis (narcotics, DM, uremia, EtOH, infection); GE junction incompetence (GERD, hiatal hernia); pregnancy or obesity; also: difficult intubation, neuromuscular disease",
 "rationale":"Each factor either increases gastric volume/pressure, delays emptying, or reduces barrier function at the GE junction, increasing aspiration risk.",
 "bloom":"apply","source":[{"book":"Stanford CA-1","page":73}],"confusable_with":""},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is gastroparesis and what are its major etiologies?",
 "answer":"Gastroparesis: delayed gastric emptying of solid food without mechanical obstruction; major etiologies: diabetes (vagus nerve damage from hyperglycemia), post-viral, post-surgical (vagus injury), systemic disease (thyroid, critical illness, Parkinson's, CTD), medications (opiates, CCBs, anticholinergics)",
 "rationale":"Vagal nerve damage from chronic hyperglycemia is the most common cause; the vagus nerve is essential for gastric motility coordination.",
 "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":80}],"confusable_with":"Mechanical gastric outlet obstruction (structural cause, different management)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the standard diagnostic test for gastroparesis and how should motility medications be handled before testing?",
 "answer":"Gastric scintigraphy (most commonly used); hold motility medications (metoclopramide) and opiates for 48 hours prior to testing",
 "rationale":"Motility drugs and opioids alter gastric transit time; holding them reveals the underlying disease state rather than drug effect.",
 "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":80}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the aspiration risk management strategy for high-risk patients including those with GERD/gastroparesis?",
 "answer":"Metoclopramide + H2-blockers + antacids preoperatively; consider awake/upright intubation and RSI; cricoid pressure until ETT position confirmed; minimize bag-mask PPV or keep pressure <20 cmH2O; extubate after protective reflexes recover; leave NGT to suction if present",
 "rationale":"Multimodal aspiration prophylaxis reduces gastric volume and acidity; RSI with cricoid pressure minimizes the window for passive regurgitation.",
 "bloom":"apply","source":[{"book":"Stanford CA-1","page":74}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What three conditions account for 90% of chronic cough cases and what is their evaluation order?",
 "answer":"Upper airway cough syndrome (UACS), asthma, and GERD account for 90% of chronic cough (many patients have combinations); evaluate and treat empirically in this sequence; consider ACEi use as reversible cause",
 "rationale":"GERD can cause chronic cough via vagal reflex and/or microaspiration; treating GERD often resolves cough even without classic heartburn symptoms.",
 "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":226}],"confusable_with":""},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the risk stratification tool for upper GI bleeding and what score indicates low risk for rebleeding?",
 "answer":"Glasgow-Blatchford and ABC scores recommended for UGIB risk stratification; Blatchford score 0-1 indicates low risk of rebleeding",
 "rationale":"Low-risk UGIB patients can potentially be managed without urgent endoscopy; higher scores indicate need for admission and early endoscopic intervention.",
 "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"AIMS65 (less recommended)"},
]

kps.append({"_type":"illness_script","topic":t,"discipline":disc,
 "enabling_conditions":"Patient with diabetes, prior abdominal surgery, chronic opioid use, or systemic disease presenting for elective surgery",
 "pathophysiology":"Delayed gastric emptying via vagal or drug-mediated impairment of antral motility; increases risk of aspiration by maintaining large gastric volume",
 "time_course":"Chronic condition; acute exacerbation with opioids or acute illness; NPO guidelines insufficient alone",
 "key_features":"Nausea, early satiety, postprandial fullness, vomiting of undigested food; ASA full-stomach precautions",
 "consequence_if_missed":"Pulmonary aspiration during anesthesia induction -> aspiration pneumonitis/pneumonia; potentially fatal"})

# ============================================================
# [25] Gabapentinoids in Pain Management
# ============================================================
t = "Gabapentinoids in Pain Management"
dom = "Perioperative medicine (preoperative assessment, risk stratification, premedication, ERAS, fluid management, temperature, positioning, post-op care)"
disc = "anesthesia"
s = "gabapentinoids"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"What was the original indication of gabapentin before its use in perioperative pain management?",
 "answer":"Gabapentin was initially employed as an anticonvulsant before being repurposed for perioperative pain management",
 "rationale":"Its mechanism of blocking voltage-gated calcium channels containing the alpha-2-delta subunit reduces central sensitization and neuropathic pain signaling.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":463}],"confusable_with":""},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the current status of perioperative gabapentinoid use in ERAS protocols?",
 "answer":"Perioperative gabapentinoid use has been challenged: evidence of harm and risk has grown without significant gains in benefit; their use in multimodal protocols is now questioned",
 "rationale":"Meta-analyses show gabapentinoids increase sedation, dizziness, and respiratory depression without consistent analgesic benefit in ERAS pathways.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":747}],"confusable_with":"NSAIDs and acetaminophen (clear multimodal analgesia benefit)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What evidence exists for vitamin C as an adjunct in perioperative pain management?",
 "answer":"Moderate evidence for 2g preoperative vitamin C reducing postoperative morphine consumption; high-level evidence for 1g/day for 50 days for CRPS I prevention after orthopedic extremity surgery",
 "rationale":"Vitamin C reduces oxidative stress that contributes to central sensitization and CRPS pathophysiology; antioxidant mechanism reduces neuroinflammation.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":747}],"confusable_with":""},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"In the multimodal analgesic approach, what categories of agents are combined for optimal perioperative pain management?",
 "answer":"Interventional techniques (epidural/peripheral nerve catheters/blocks) + systemic pharmacology (NSAIDs, alpha-2 agonists, NMDA antagonists, membrane stabilizers/gabapentinoids, and opioids at minimized dose)",
 "rationale":"Different analgesic mechanisms target different pain pathways; combination achieves better analgesia at lower doses of each individual agent.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":744}],"confusable_with":""},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What psychological factor is among the strongest predictors of chronic postsurgical pain (pain chronification)?",
 "answer":"Pain catastrophizing (an exaggerated negative mental set during painful experience) is among the strongest predictors of chronic pain vulnerability, along with anxiety and mood disorders",
 "rationale":"Central sensitization is amplified by psychological distress; catastrophizing activates pain amplification circuits and reduces endogenous inhibitory control.",
 "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":826}],"confusable_with":""},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the dexmedetomidine dosing approach for sedation with analgesic properties, and what precautions apply?",
 "answer":"Dexmedetomidine loading dose 1 mcg/kg IV over 10 min; maintenance 0.2-0.7 mcg/kg/h; rapid onset, terminal half-life 2h; reduce dose in liver/kidney disease; caution with vasodilators and cardiac depressants",
 "rationale":"Dexmedetomidine has analgesic and opioid-sparing properties via alpha-2 receptor activation; its hemodynamic effects (bradycardia, hypotension) require appropriate monitoring.",
 "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":463}],"confusable_with":"Clonidine (oral alpha-2 agonist, less potent, longer duration)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"What are the recommended pharmacological adjuvants for opioid-refractory neuropathic pain in palliative care?",
 "answer":"Tricyclic antidepressants (desipramine, amitriptyline - secondary amines preferred for fewer side effects); duloxetine/milnacipran (SNRIs, better side effect profile than TCAs but less evidence); dexamethasone for bone/neuropathic/edema pain",
 "rationale":"TCAs modulate descending noradrenergic inhibition; SNRIs similar mechanism; glucocorticoids reduce tumor edema and neuroinflammation around compressed nerves.",
 "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":869}],"confusable_with":"SSRIs alone (very scarce evidence for pain)"},
]

# ============================================================
# [26] Gas Flow Physics and Anesthesia Machine
# Chunks mostly off-topic; use available machine-relevant content
# ============================================================
t = "Gas Flow Physics and Anesthesia Machine"
dom = "Anesthesia equipment, monitoring & patient safety (machine checkout, breathing circuits, vaporizers, monitoring modalities, PONV, temperature)"
disc = "anesthesia"
s = "gas-flow-machine"

kps += [
{"id":f"{s}-d1","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does the blood:gas partition coefficient affect the speed of inhalation anesthetic uptake?",
 "answer":"Lower blood:gas partition coefficient = faster induction; N2O = 0.47 (fastest), desflurane = 0.42, sevoflurane = 0.69, isoflurane = 1.40, halothane = 2.3; fat:blood coefficient >1 means postprandial lipidemia slows induction",
 "rationale":"A low blood:gas coefficient means blood holds little agent, so alveolar concentration rises quickly to equilibrium with inspired concentration.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":19}],"confusable_with":"Oil:gas partition coefficient (determines potency, not speed)"},
{"id":f"{s}-d2","topic":t,"domain":dom,"discipline":disc,
 "stem":"How does the electronic flowmeter work in modern anesthesia machines for measuring gas flow?",
 "answer":"Electronic flowmeters measure the pressure drop caused by a flow restrictor; each gas (O2, N2O, air) has a separate electronic flow measurement device; required if gas flow data is acquired by computerized anesthesia recording systems",
 "rationale":"Pressure drop across a fixed restrictor is proportional to flow rate; electronic measurement allows precise digital control and data acquisition for automated record keeping.",
 "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":102}],"confusable_with":"Thorpe tube flowmeters (mechanical, float height indicates flow)"},
{"id":f"{s}-d3","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is MAC-BAR and what is its value relative to standard MAC?",
 "answer":"MAC-BAR (blunted autonomic response): concentration at which 50% of population will not mount an adrenergic response (tachycardia, hypertension) to stimulation; approximately 1.5-1.7 MAC (higher than immobility MAC of 1.0)",
 "rationale":"Sympathetic response to surgical stimulation requires higher anesthetic depth than immobility; MAC-BAR guides dosing to prevent cardiovascular responses to incision.",
 "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":114}],"confusable_with":"MAC-awake (0.4 MAC, much lower)"},
{"id":f"{s}-d4","topic":t,"domain":dom,"discipline":disc,
 "stem":"What factors increase MAC (require higher anesthetic concentration)?",
 "answer":"Factors increasing MAC: hyperthermia, chronic ethanol abuse (tolerance), inhibition of catecholamine reuptake (amphetamines, ephedrine), first months of life for infants >6 months",
 "rationale":"Hyperthermia increases CNS metabolic demand and arousal; catecholamine excess stimulates the CNS countering anesthetic depression.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":23}],"confusable_with":"Factors decreasing MAC (age, hypothermia, pregnancy, opioids, alpha-2 agonists)"},
{"id":f"{s}-d5","topic":t,"domain":dom,"discipline":disc,
 "stem":"What unique hazard does sevoflurane produce in desiccated CO2 absorbent?",
 "answer":"Sevoflurane can form compound A in CO2 absorbent (nephrotoxic in rats, no human clinical evidence of nephrotoxicity); guidelines recommend fresh gas flow >2 L/min to prevent rebreathing of compound A; does NOT form with calcium hydroxide absorbent",
 "rationale":"Compound A formation occurs in alkaline absorbents (barium hydroxide lime, soda lime) through interaction with sevoflurane; higher fresh gas flows dilute and remove compound A.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":20}],"confusable_with":"Desflurane/isoflurane in desiccated absorbent (can form CO, not compound A)"},
{"id":f"{s}-d6","topic":t,"domain":dom,"discipline":disc,
 "stem":"What is the minimum alveolar concentration of sevoflurane and what is its blood:gas solubility coefficient?",
 "answer":"Sevoflurane MAC = 2% (half as potent as isoflurane MAC 1%); blood:gas partition coefficient = 0.69 (lower than N2O = 0.47); lowest solubility among clinical halogenated agents",
 "rationale":"Low blood:gas coefficient predicts rapid induction and emergence; its low potency (high MAC) is offset by its low pungency making it preferred for inhalational induction.",
 "bloom":"recall","source":[{"book":"Stanford CA-1","page":20}],"confusable_with":"Desflurane (blood:gas 0.42, lowest of all but highly pungent)"},
{"id":f"{s}-d7","topic":t,"domain":dom,"discipline":disc,
 "stem":"In pediatric patients undergoing inhalational anesthesia, how does the minute ventilation-to-FRC ratio affect induction speed?",
 "answer":"Greater minute ventilation-to-FRC ratio in infants (combined with greater blood flow to brain) speeds increase in alveolar anesthetic concentration, producing faster inhalation induction than in adults",
 "rationale":"High MV:FRC ratio means the alveolar gas is replaced rapidly, quickly raising alveolar concentration to inspired concentration.",
 "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1443}],"confusable_with":""},
]

print(f"KPs so far: {len(kps)}")

with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch6.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Batch 6 saved OK")
