import json, sys
sys.path.insert(0, 'data')
from build_kp_part6 import kps

disc = "anesthesia"

# =====================================================================
# [5] End-of-Life Care Ethics
# =====================================================================
topic5 = "End-of-Life Care Ethics"
dom5 = "Patient safety, ethics, professionalism & quality (closed-claims lessons, never events, root-cause analysis, informed consent, communication, handoffs, wellness)"

kps += [
  {"id":"end-of-life-care-ethics-d1","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"Temporary destruction of nerve fibers for palliative pain management can be accomplished by injection of which neurolytic agents, and what is a key limitation of these agents?",
   "answer":"Ethyl alcohol (alcohol) and phenol are neurolytic agents; they are not selective -- they affect visceral, sensory, AND motor fibers equally.",
   "rationale":"Non-selective neurolysis can relieve cancer pain but also causes motor weakness and bowel/bladder dysfunction; additionally, pain may recur or new deafferentation pain may develop within weeks to months.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":""},

  {"id":"end-of-life-care-ethics-d2","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"What additional neurodestructive procedures beyond nerve blocks may be useful in end-of-life palliative care for refractory pain?",
   "answer":"Pituitary adenolysis and cordotomy may be useful in end-of-life palliative care for refractory pain.",
   "rationale":"These procedures interrupt ascending pain pathways at the pituitary (hormonal-mediated pain in metastatic disease) or spinal cord level (cordotomy), providing relief when systemic opioids are insufficient.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":1798}],"confusable_with":""},

  {"id":"end-of-life-care-ethics-d3","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"In the ICU setting, prolonged use of propofol has been associated with a serious complication, particularly in children. What is it?",
   "answer":"Prolonged propofol use has been associated with propofol infusion syndrome, which is particularly dangerous in children.",
   "rationale":"Propofol infusion syndrome involves metabolic acidosis, cardiac failure, rhabdomyolysis, and renal failure from mitochondrial dysfunction caused by impaired fatty acid oxidation during prolonged high-dose infusion.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},

  {"id":"end-of-life-care-ethics-d4","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"In patients with sepsis or septic shock at the end of life, what is essential before determining which treatments are acceptable?",
   "answer":"A goals of care discussion exploring prognosis, invasiveness of interventions, and predicted quality of life is essential to determine which treatments are acceptable.",
   "rationale":"Septic patients have high risk of multi-organ failure and death; some accept all treatments while others may decline certain interventions -- patient values and prognosis must guide the plan.",
   "bloom":"apply","source":[{"book":"Society Guideline","page":49}],"confusable_with":""},

  {"id":"end-of-life-care-ethics-d5","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"When should palliative care be integrated for patients with sepsis or septic shock with significant comorbidities that impair quality of life?",
   "answer":"Palliative care should be integrated when patients have significant comorbidities that may be life-limiting or significantly impair quality of life, even while treating the acute illness.",
   "rationale":"Palliative care is not equivalent to withdrawing treatment; it focuses on symptom management and goals of care in parallel with curative efforts, improving outcomes and quality of life.",
   "bloom":"apply","source":[{"book":"Society Guideline","page":50}],"confusable_with":"hospice care"},

  {"id":"end-of-life-care-ethics-d6","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"PACU patient bed enclosures serve a privacy function. What ethically important interactions do they protect?",
   "answer":"Enclosures protect sensitive and confidential discussions between patients, families, and the care team that occur during postoperative recovery -- important for patient dignity and HIPAA compliance.",
   "rationale":"Open PACU bays create conditions where private medical information may be overheard; physical barriers protect patient confidentiality during vulnerable postoperative conversations.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2096}],"confusable_with":""},

  {"id":"end-of-life-care-ethics-d7","topic":topic5,"domain":dom5,"discipline":disc,
   "stem":"Physical restraints in critically ill patients should be used under what conditions, according to current ICU care principles?",
   "answer":"Restraints are inhumane and should be used only as a last resort for patient protection; they have been associated with adverse consequences.",
   "rationale":"Restraints cause psychological trauma, increase delirium, and have been replaced by light sedation, reorientation, and family engagement protocols in modern ICU care.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2158}],"confusable_with":""},
]

# =====================================================================
# [6] Endocrine Physiology Relevant to Anesthesia
# =====================================================================
topic6 = "Endocrine Physiology Relevant to Anesthesia"
dom6 = "Anesthesia: basic & clinical sciences (relevant anatomy, respiratory/cardiac/renal/neuro physiology, pharmacokinetics/dynamics principles, physics of gases & flow, statistics)"

kps += [
  {"id":"endocrine-physiology-relevant-anesthesia-d1","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Etomidate reduces CMRO2 and is a potent cerebral vasoconstrictor. What endocrine side effect has raised controversy about its use, particularly in septic patients?",
   "answer":"Etomidate causes adrenocortical suppression (inhibits 11-beta hydroxylase), raising concerns about increased mortality in septic patients though controversy remains.",
   "rationale":"Even a single dose of etomidate can suppress cortisol synthesis for 24 hours; in septic patients who depend on the stress cortisol response for hemodynamic stability, this may be harmful.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":145}],"confusable_with":""},

  {"id":"endocrine-physiology-relevant-anesthesia-d2","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Dexmedetomidine loading doses can produce a transient increase in blood pressure followed by bradycardia. What is the mechanism?",
   "answer":"Loading doses cause transient hypertension via vasoconstriction mediated by peripheral alpha-2 adrenergic receptors, followed by reflex bradycardia.",
   "rationale":"Alpha-2 receptors on vascular smooth muscle mediate vasoconstriction; the initial BP rise triggers baroreceptor-mediated reflex bradycardia, and central alpha-2 stimulation also reduces sympathetic outflow.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":146}],"confusable_with":""},

  {"id":"endocrine-physiology-relevant-anesthesia-d3","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Dexmedetomidine is described as particularly useful for epilepsy surgery monitoring. Why?",
   "answer":"Dexmedetomidine does not suppress spikes from seizure foci on EEG, unlike most other anesthetics, making it suitable for epilepsy surgery where foci must be identified.",
   "rationale":"Most GABAergic anesthetics (propofol, benzodiazepines, barbiturates) suppress epileptiform activity and interfere with intraoperative EEG mapping; dexmedetomidine's alpha-2 mechanism does not suppress seizure activity.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":146}],"confusable_with":"propofol for epilepsy surgery"},

  {"id":"endocrine-physiology-relevant-anesthesia-d4","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Thyroid hormones regulate oxygen consumption and metabolic rate. What thyroid disorder presents with unexplained weight gain, fatigue, and cold intolerance, and has implications for anesthesia?",
   "answer":"Hypothyroidism (deficient secretion of thyroid hormones) -- most commonly caused by iodine deficiency or autoimmune Hashimoto thyroiditis; relevant to anesthesia due to cardiovascular depression, impaired drug metabolism, and hypothermia risk.",
   "rationale":"Hypothyroid patients have decreased cardiac output, reduced hypoxic ventilatory drive, impaired thermoregulation, and prolonged drug action; elective surgery should be deferred until euthyroid.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":548}],"confusable_with":"hyperthyroidism"},

  {"id":"endocrine-physiology-relevant-anesthesia-d5","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"During thyroid storm, what differential diagnosis should be considered intraoperatively that presents with hyperthermia, tachycardia, and metabolic acidosis?",
   "answer":"Malignant hyperthermia (MH) must be distinguished from thyroid storm; MH is associated with elevated EtCO2, muscle rigidity, and typically occurs during volatile/succinylcholine exposure.",
   "rationale":"Thyroid storm usually has normal EtCO2 and temperature elevation is less rapid than MH; distinguishing these requires clinical context, triggerless anesthetic history, and metabolic assessment.",
   "bloom":"analyze","source":[{"book":"Stanford CA-1","page":85}],"confusable_with":"malignant hyperthermia"},

  {"id":"endocrine-physiology-relevant-anesthesia-d6","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Dexmedetomidine loading doses increase SVR and MAP. Clinically, does this also significantly increase pulmonary vascular resistance?",
   "answer":"Clinically useful loading doses of dexmedetomidine (0.5-1 mcg/kg IV) increase SVR and MAP but probably do not significantly increase pulmonary vascular resistance.",
   "rationale":"Alpha-2 receptors are less prominent in pulmonary vasculature; dexmedetomidine's systemic vasoconstrictive effects are largely confined to the systemic circulation, making it useful in pulmonary hypertension patients.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":146}],"confusable_with":""},

  {"id":"endocrine-physiology-relevant-anesthesia-d7","topic":topic6,"domain":dom6,"discipline":disc,
   "stem":"Barbiturates can reduce ICP and are used for neuroprotection in focal cerebral ischemia. In what type of ischemia do barbiturates probably NOT provide neuroprotection?",
   "answer":"Barbiturates probably do not provide neuroprotection from global cerebral ischemia (e.g., cardiac arrest), only from focal ischemia.",
   "rationale":"Barbiturates protect by suppressing metabolic demand in ischemic penumbra tissue; global ischemia affects all brain tissue uniformly without penumbra regions to salvage.",
   "bloom":"analyze","source":[{"book":"Miller/Baby Miller","page":139}],"confusable_with":"focal cerebral ischemia protection"},
]

# =====================================================================
# [7] Endovascular Neurosurgery: Neurointerventional Anesthesia
# =====================================================================
topic7 = "Endovascular Neurosurgery: Neurointerventional Anesthesia"
dom7 = "Neuroanesthesia (intracranial pressure & cerebral physiology, craniotomy, awake craniotomy, spine surgery, neuromonitoring, TBI, aneurysm)"

kps += [
  {"id":"endovascular-neurosurgery-neurointerventional-d1","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"What is the primary anesthetic goal when managing a patient with an unruptured cerebral aneurysm undergoing endovascular coiling?",
   "answer":"Prevent rupture (or rebleeding) and avoid factors that promote cerebral ischemia or vasospasm; sudden increases in blood pressure with intubation or stimulation must be avoided.",
   "rationale":"Aneurysmal rupture during manipulation dramatically worsens outcome; controlled BP during laryngoscopy and throughout the procedure is the central anesthetic management goal.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":988}],"confusable_with":""},

  {"id":"endovascular-neurosurgery-neurointerventional-d2","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"Arteriovenous malformations (AVMs) typically present at what age range with hemorrhage, and what is the unusual hemodynamic consequence of large AVMs?",
   "answer":"AVM bleeding is most common between ages 10-30; large AVMs with high blood flow and low vascular resistance can rarely cause high-output cardiac failure.",
   "rationale":"The arteriovenous shunting in a large AVM mimics a systemic arteriovenous fistula, chronically increasing cardiac output; if large enough, this leads to high-output heart failure.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":989}],"confusable_with":""},

  {"id":"endovascular-neurosurgery-neurointerventional-d3","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"For AVM treatment, in what setting is the endovascular approach to occlude feeding vessels typically attempted?",
   "answer":"The endovascular approach is typically attempted in the hybrid operating room or neurointerventional suite.",
   "rationale":"The hybrid suite combines neuroimaging (fluoroscopy/angiography) with surgical capability, allowing rapid conversion to open surgery if endovascular treatment fails or causes hemorrhage.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":989}],"confusable_with":""},

  {"id":"endovascular-neurosurgery-neurointerventional-d4","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"Dexmedetomidine is particularly useful for neurointerventional procedures requiring frequent mental status assessment. Why is it advantageous over propofol in this context?",
   "answer":"Dexmedetomidine is less likely to cause respiratory depression than propofol, making it especially useful for patients requiring frequent neurological assessment or those with severe pulmonary hypertension.",
   "rationale":"Propofol reliably depresses respiration; dexmedetomidine provides sedation and anxiolysis while preserving spontaneous ventilation and allowing responsive cooperation during procedures.",
   "bloom":"apply","source":[{"book":"Miller/Baby Miller","page":707}],"confusable_with":"propofol sedation"},

  {"id":"endovascular-neurosurgery-neurointerventional-d5","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"Interventional neuroradiology (INR) is also known by what other names, and what specialties does it combine?",
   "answer":"INR is also called endovascular neurosurgery; it mixes traditional neurosurgery with neuroradiology and includes aspects of head and neck surgery.",
   "rationale":"This combined specialty has evolved to treat conditions (aneurysms, AVMs, stroke, carotid stenosis) using minimally invasive endovascular rather than open surgical approaches.",
   "bloom":"recall","source":[{"book":"Miller/Baby Miller","page":707}],"confusable_with":""},

  {"id":"endovascular-neurosurgery-neurointerventional-d6","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"What monitoring is recommended for patients undergoing endovascular neurosurgical procedures, similar to craniotomies?",
   "answer":"Monitoring should be carried out similarly to craniotomies, including intraarterial pressure monitoring; venous access with large-bore catheters is desirable for massive hemorrhage.",
   "rationale":"Endovascular procedures carry the same risk of catastrophic hemorrhage as open procedures; rapid identification of BP changes and ability to infuse blood products quickly are critical.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":995}],"confusable_with":""},

  {"id":"endovascular-neurosurgery-neurointerventional-d7","topic":topic7,"domain":dom7,"discipline":disc,
   "stem":"What is the primary role of stereotaxis in neurosurgery, and for what conditions can it be used?",
   "answer":"Stereotaxis can be employed in treating involuntary movement disorders, intractable pain, and epilepsy, and for diagnosing and treating deep-seated tumors.",
   "rationale":"Stereotactic frames or image guidance systems allow precise targeting of deep brain structures without extensive tissue disruption, enabling minimally invasive procedures in eloquent areas.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":977}],"confusable_with":""},
]

print(f"Generated so far: {len(kps)} KPs")
print("OK")
