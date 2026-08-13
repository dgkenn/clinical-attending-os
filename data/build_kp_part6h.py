import json, sys
sys.path.insert(0, 'data')
from build_kp_part6g import kps

disc = "anesthesia"
dom_preop = "Preoperative evaluation & perioperative medicine (risk stratification, cardiac/pulmonary/endocrine optimization, NPO & aspiration risk, chronic medication management, frailty, consent)"
dom_pain = "Pain medicine (acute perioperative pain, multimodal & opioid management, chronic pain syndromes, interventional techniques, opioid pharmacology & safety)"
dom_basic = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"
dom_obs = "Obstetric anesthesia (maternal physiology, labor analgesia, cesarean anesthesia, preeclampsia/eclampsia, obstetric hemorrhage, emergencies, fetal considerations)"
dom_pharm = "Anesthetic pharmacology (inhaled agents, IV induction agents, opioids, neuromuscular blockers & reversal, local anesthetics, benzodiazepines, vasoactive/adjunct drugs)"
dom_ethics = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"
dom_regional = "Regional & neuraxial anesthesia (spinal, epidural, combined, upper & lower extremity peripheral nerve blocks, truncal blocks, local anesthetic pharmacology, complications)"

# =====================================================================
# [23] Frailty assessment and prehabilitation
# =====================================================================
topic23 = "Frailty assessment and prehabilitation"

kps += [
  {"id":"frailty-assessment-prehabilitation-d1","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"The preoperative geriatric assessment checklist includes frailty scoring. What specific cognitive assessment tool is used, and what does it involve?",
   "answer":"The Mini-Cog is used for cognitive assessment: it involves 3-item recall and a clock draw test; results guide perioperative risk stratification.",
   "rationale":"Cognitive impairment is a major risk factor for postoperative delirium; the Mini-Cog can identify MCI in 3 minutes, making it practical for preoperative screening.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1494}],"confusable_with":"MMSE"},

  {"id":"frailty-assessment-prehabilitation-d2","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"Prehabilitation programs focus on what four goals to optimize surgical patients preoperatively?",
   "answer":"(1) Improved physical fitness, (2) dietary interventions to counteract catabolism and support anabolism with exercise, (3) antistress interventions to foster resilience and self-efficacy, and (4) cessation of adverse health habits (alcohol, smoking).",
   "rationale":"Prehabilitation addresses the physiological reserve deficit that frail patients bring to surgery; improving each domain increases tolerance of surgical stress and improves recovery.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":241}],"confusable_with":""},

  {"id":"frailty-assessment-prehabilitation-d3","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"In a patient with liver cirrhosis being evaluated for liver transplantation, frailty assessment is recommended using what specific tool?",
   "answer":"The Liver Frailty Index is recommended before transplantation, followed by prehabilitation measures; sarcopenia can also be assessed by measuring the skeletal muscle index at the L3 level on CT.",
   "rationale":"Cirrhotic patients have severe sarcopenia and frailty from protein malnutrition, ascites, and reduced activity; frailty independently predicts post-transplant morbidity and mortality.",
   "bloom":"apply","source":[{"book":"StatPearls","page":13}],"confusable_with":""},

  {"id":"frailty-assessment-prehabilitation-d4","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"Preoperative screening for modifiable conditions as part of perioperative medicine includes malnutrition. What screening tools and interventions are recommended?",
   "answer":"PONS, MST, or MUST scores are used for malnutrition screening; interventions include immunonutrition and oral nutrition supplementation for at least 1 week preoperatively, with early feeding intraoperatively.",
   "rationale":"Malnutrition impairs wound healing, immune function, and muscle recovery; preoperative optimization with supplementation reduces postoperative complications and length of stay.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":787}],"confusable_with":""},

  {"id":"frailty-assessment-prehabilitation-d5","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"Perioperative pulmonary complications (PPCs) add significantly to hospitalization costs. What is the approximate added cost per significant PPC episode?",
   "answer":"Significant PPCs (pneumonia, pleural effusion, reintubation, prolonged intubation) add an average of $25,000 or more per episode.",
   "rationale":"This cost burden justifies investment in preoperative pulmonary optimization (smoking cessation, bronchodilator therapy, physical conditioning) in high-risk patients.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":784}],"confusable_with":""},

  {"id":"frailty-assessment-prehabilitation-d6","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"The preoperative geriatric evaluation checklist includes what specific functional and fall-related assessment?",
   "answer":"Document functional status and history of falls; determine baseline frailty score as part of the preoperative geriatric evaluation.",
   "rationale":"Fall history reflects neuromuscular, cognitive, and balance impairments that predict perioperative complications; functional status guides anesthetic planning and postoperative care intensity.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1492}],"confusable_with":""},

  {"id":"frailty-assessment-prehabilitation-d7","topic":topic23,"domain":dom_preop,"discipline":disc,
   "stem":"Smoking increases post-liver transplant mortality due to what specific complication?",
   "answer":"Smoking increases mortality among liver transplant recipients due to cardiac disease and also increases the risk of hepatic artery thrombosis.",
   "rationale":"Nicotine causes endothelial damage and promotes a prothrombotic state; hepatic artery thrombosis is a devastating post-transplant complication causing graft failure.",
   "bloom":"recall","source":[{"book":"StatPearls","page":12}],"confusable_with":""},
]

# =====================================================================
# [24] GERD, gastroparesis, and upper GI disease
# =====================================================================
topic24 = "GERD, gastroparesis, and upper GI disease"

kps += [
  {"id":"gerd-gastroparesis-upper-gi-disease-d1","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"Metoclopramide is used as an aspiration prophylaxis agent. What is its mechanism in the upper GI tract?",
   "answer":"Metoclopramide acts as a cholinomimetic peripherally and a dopamine receptor antagonist centrally; it increases lower esophageal sphincter tone, speeds gastric emptying, and does not stimulate secretions.",
   "rationale":"By enhancing ACh-mediated intestinal smooth muscle contraction, metoclopramide reduces gastric volume and LES incompetence -- the two key risk factors for aspiration.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":446}],"confusable_with":"H2 blockers"},

  {"id":"gerd-gastroparesis-upper-gi-disease-d2","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"Metoclopramide's prokinetic effect in the upper GI tract is not dependent on vagal innervation but is abolished by what type of drug?",
   "answer":"Metoclopramide's prokinetic effect is abolished by anticholinergic agents (despite not requiring vagal innervation for its action).",
   "rationale":"Metoclopramide facilitates ACh transmission at selective muscarinic receptors; anticholinergics block these receptors directly, negating the drug's effect regardless of vagal status.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":446}],"confusable_with":""},

  {"id":"gerd-gastroparesis-upper-gi-disease-d3","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"Gastroparesis is defined as delayed gastric emptying of solid food without mechanical obstruction. What are the major etiological categories?",
   "answer":"Major causes: diabetes (vagus nerve damage from hyperglycemia), post-viral, post-surgical (vagus nerve injury), systemic disease (thyroid, critical illness, Parkinson's, CTD), and medications (opioids, CCBs, anticholinergics).",
   "rationale":"The vagus nerve is the primary driver of gastric motility; any process damaging it (diabetes, surgery) or blocking its receptors (anticholinergics) impairs gastric emptying.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":80}],"confusable_with":"mechanical gastric outlet obstruction"},

  {"id":"gerd-gastroparesis-upper-gi-disease-d4","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"What are the classic risk factors for aspiration relevant to anesthetic management that should be identified preoperatively?",
   "answer":"Risk factors include GE junction incompetence (GERD, hiatal hernia, scleroderma), gastroparesis (DM, opioids), pregnancy, obesity, bowel obstruction, difficult intubation history, and neuromuscular disease.",
   "rationale":"These conditions either reduce the barrier to regurgitation (decreased LES tone, structural abnormalities) or increase gastric contents (delayed emptying); identifying them prompts RSI and aspiration precautions.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":73}],"confusable_with":""},

  {"id":"gerd-gastroparesis-upper-gi-disease-d5","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"In upper GI bleeding, BUN:Cr ratio >30 has what diagnostic significance?",
   "answer":"BUN:Cr ratio >30 (especially >35) has high specificity for upper GI bleeding, as blood proteins are digested and absorbed as urea in the small intestine, raising BUN disproportionately.",
   "rationale":"Digestion of red blood cells in the proximal GI tract releases amino acids that are catabolized to urea; this protein load from the 'upper GI source' creates the disproportionate BUN rise.",
   "bloom":"apply","source":[{"book":"MGH Housestaff Manual","page":70}],"confusable_with":"renal azotemia"},

  {"id":"gerd-gastroparesis-upper-gi-disease-d6","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"Laryngospasm is mediated by which nerve and what are the anesthetic stages most associated with its occurrence?",
   "answer":"Laryngospasm is mediated by the superior laryngeal nerve; it most commonly occurs during Stage 2 (excitement/delirium) of anesthesia and during emergence under light anesthesia relative to stimulation.",
   "rationale":"The superior laryngeal nerve mediates the protective glottic closure reflex; partial anesthesia removes cortical inhibition while preserving the reflex, making the larynx hyperresponsive to secretions or manipulation.",
   "bloom":"apply","source":[{"book":"Stanford CA-1","page":73}],"confusable_with":"bronchospasm"},

  {"id":"gerd-gastroparesis-upper-gi-disease-d7","topic":topic24,"domain":dom_preop,"discipline":disc,
   "stem":"Chronic cough with GERD as a cause accounts for what percentage of chronic cough, and what is the typical empiric treatment approach?",
   "answer":"GERD contributes to approximately 90% of chronic cough cases (as part of UACS/asthma/GERD triad); empiric sequential treatment of GERD with H2 blockers or PPIs is recommended.",
   "rationale":"Chronic microaspiration of gastric acid irritates the upper airway and triggers afferent cough reflexes; acid suppression reduces this stimulus and is both diagnostic and therapeutic.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":226}],"confusable_with":""},
]

# =====================================================================
# [25] Gabapentinoids in Pain Management
# =====================================================================
topic25 = "Gabapentinoids in Pain Management"

kps += [
  {"id":"gabapentinoids-pain-management-d1","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"Studies show that gabapentinoids may reduce perioperative opioid consumption, but other reports have questioned their utility. What is the current evidence status for gabapentinoids in ERAS protocols?",
   "answer":"Gabapentinoids can reduce perioperative opioid consumption in multimodal pain management, but evidence of harm and risk has led to challenges against their widespread use; recent evidence questions routine perioperative use.",
   "rationale":"Side effects including dizziness, sedation, respiratory depression (especially in elderly), and fall risk have accumulated; meta-analyses show modest opioid-sparing effects that may not justify routine use in all patients.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":747}],"confusable_with":""},

  {"id":"gabapentinoids-pain-management-d2","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"Gabapentinoids (gabapentin and pregabalin) were included in multimodal analgesia protocols as 'membrane stabilizers.' What other drug class is included in multimodal analgesia as membrane stabilizers?",
   "answer":"Gabapentinoids serve as membrane stabilizers (voltage-gated calcium channel alpha-2-delta subunit modulators) alongside other membrane-stabilizing agents; NMDA receptor antagonists (ketamine) are also included in multimodal protocols.",
   "rationale":"Multimodal analgesia combines drugs acting at different pain pathway sites: NSAIDs (peripheral), opioids (spinal/supraspinal), NMDA antagonists (central sensitization), alpha-adrenergic agonists, and gabapentinoids (presynaptic calcium channel modulation).",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":744}],"confusable_with":""},

  {"id":"gabapentinoids-pain-management-d3","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"In palliative care, what drug classes are considered multipurpose analgesics for bone pain, neuropathic pain, and headache from cancer?",
   "answer":"Dexamethasone and prednisone are described as multipurpose analgesics effective for bone pain, neuropathic pain, lymphoedema pain, headache, and bowel obstruction pain in palliative settings.",
   "rationale":"Corticosteroids reduce tumor-related inflammation and edema; their broad analgesic spectrum in cancer pain reflects multiple mechanisms including reduced prostaglandin synthesis and direct neuropathic effects.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":869}],"confusable_with":"gabapentin"},

  {"id":"gabapentinoids-pain-management-d4","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"For management of opioid-refractory neuropathic pain in palliative care, what antidepressants are described as first-line, and which secondary amine compound may be preferred?",
   "answer":"Desipramine and amitriptyline (TCAs) are used for opioid-refractory neuropathic pain, especially when comorbid depression exists; desipramine (secondary amine) may be preferred due to fewer side effects.",
   "rationale":"TCAs block serotonin and norepinephrine reuptake, enhancing descending inhibitory pain pathways; secondary amines (desipramine) have fewer anticholinergic side effects than tertiary amines (amitriptyline).",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":869}],"confusable_with":"SNRIs"},

  {"id":"gabapentinoids-pain-management-d5","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"Pain catastrophizing is identified as among the strongest predictors of what pain outcome?",
   "answer":"Pain catastrophizing (exaggerated negative mental set brought to bear during pain) is among the strongest predictors of 'chronification' of pain -- transition from acute to chronic pain.",
   "rationale":"Psychological factors are not merely reactive to pain but are bidirectional drivers; catastrophizing activates fear-avoidance behaviors and central sensitization mechanisms that perpetuate and amplify pain.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":826}],"confusable_with":"depression as pain predictor"},

  {"id":"gabapentinoids-pain-management-d6","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"Vitamin C supplementation has been studied as a perioperative analgesic adjunct. For what specific condition is there high-level evidence supporting perioperative vitamin C?",
   "answer":"High-level evidence supports perioperative vitamin C supplementation (1 g/day for 50 days) for CRPS type I prevention after orthopedic extremity surgery.",
   "rationale":"CRPS involves oxidative stress-mediated neuroinflammation; vitamin C's antioxidant properties may reduce the inflammatory cascade that triggers CRPS following limb trauma or surgery.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":747}],"confusable_with":""},

  {"id":"gabapentinoids-pain-management-d7","topic":topic25,"domain":dom_pain,"discipline":disc,
   "stem":"Dexmedetomidine is used in ambulatory and postanesthetic settings for managing agitation and pain. What is its specific advantage for procedures exceeding one hour?",
   "answer":"Dexmedetomidine is particularly useful for procedures lasting more than one hour because it provides sedation and anxiolysis with less respiratory depression compared with propofol or opioids.",
   "rationale":"For prolonged procedures requiring cooperative sedation, dexmedetomidine's analgesic-sparing and respiratory-preserving properties allow patient interaction while minimizing respiratory monitoring concerns.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":463}],"confusable_with":"propofol for long procedures"},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
