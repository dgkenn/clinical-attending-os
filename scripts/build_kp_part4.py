import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch3.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch3")

# ============================================================
# ITEM 18: Tick-Borne Infections
# CHUNKS include Rickettsial infection (StatPearls), MGH travel medicine section
# ============================================================
topic = "Tick-Borne Infections"
domain = "Internal medicine: infectious disease (sepsis & septic shock, pneumonia, UTI/pyelonephritis, cellulitis & necrotizing infections, endocarditis, meningitis, C. diff, HIV, antimicrobial selection & stewardship)"
disc = "medicine"

kps += [
  {"id":"tick-borne-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Tick-borne disease presents with ascending paralysis, decreased reflexes, and respiratory distress from a neurotoxin in tick saliva — how does this differ from GBS?",
   "answer":"Tick paralysis: ascending flaccid paralysis with decreased reflexes from tick neurotoxin; minimal constitutional symptoms; may have ophthalmoplegia/bulbar symptoms; resolves rapidly after tick removal. GBS: post-infectious, albuminocytological dissociation on CSF, slower resolution.",
   "rationale":"Tick paralysis is a reversible toxin-mediated condition; removing the tick halts toxin delivery and symptoms resolve within hours to days, unlike GBS which requires immunotherapy.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Myasthenia Gravis","page":7}],"confusable_with":"Guillain-Barre syndrome"},
  {"id":"tick-borne-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the most important tick-borne infections to consider in a returned traveler with fever, and what are the key culprits in the US?",
   "answer":"In the US: Rocky Mountain spotted fever (Rickettsia rickettsii), Lyme disease (Borrelia burgdorferi), ehrlichiosis, anaplasmosis, babesiosis; travel exposure widens the differential to include rickettsial infections globally.",
   "rationale":"Geographic exposure and tick species determine the organism; early treatment of RMSF (within 5 days) is critical as late treatment is associated with high mortality.",
   "bloom":"recall","source":[{"book":"MGH Housestaff Manual","page":129}],"confusable_with":""},
  {"id":"tick-borne-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Why should outdoor activities in tick-endemic areas be avoided for patients recovering from viral encephalitis?",
   "answer":"Tick-borne encephalitis viruses (flaviviruses) and other tick-borne infections are additive risks for neurological complications; immunocompromised or neurologically vulnerable patients are at higher risk of severe tick-borne neuroinvasive disease.",
   "rationale":"Tick-borne encephalitis risk is highest in spring-summer-early fall in tick-endemic regions; avoiding tick exposure after viral CNS illness is a practical preventive measure.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Viral Meningitis & Encephalitis","page":5}],"confusable_with":""},
  {"id":"tick-borne-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What patient safety precautions prevent home electrical accidents that may cause tick-like presentations (acute flaccid paralysis from organophosphates)?",
   "answer":"Organophosphate poisoning (from pesticides) is in the differential of acute flaccid paralysis alongside tick paralysis; distinguishing features include miosis, excessive secretions (SLUDGE), and acetylcholinesterase inhibition on testing.",
   "rationale":"Both tick toxin and organophosphates cause acute flaccid paralysis by neuromuscular junction dysfunction; organophosphates produce cholinergic excess while tick paralysis is a pure motor toxin.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":1026}],"confusable_with":"Organophosphate toxicity"},
]

# ============================================================
# ITEM 19: Toxicology in the ICU
# ============================================================
topic = "Toxicology in the ICU"
domain = "Internal medicine: ICU & critical care (all-cause shock, vasopressors & inotropes, invasive & noninvasive ventilation, sedation & analgesia, multiorgan failure, rapid response, ACLS)"
disc = "medicine"

kps += [
  {"id":"toxicology-icu-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Cyanide toxicity following fires involving synthetic materials presents with what clinical triad and what is the mechanism?",
   "answer":"Neurological impairment + lactic acidosis + increased cardiac output with marked vasodilation (and arrhythmias); mechanism: cyanide binds cytochrome oxidase (complex IV), blocking mitochondrial ATP production -> histotoxic hypoxia.",
   "rationale":"Cyanide causes cellular hypoxia despite normal PaO2; the high venous O2 (cytochrome block) and lactic acidosis distinguish it from other causes of altered consciousness in fire victims.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":"CO poisoning (both from fires)"},
  {"id":"toxicology-icu-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In managing an inhalation injury patient, what bronchoscopic finding requires securing the airway urgently and what is a key risk if NOT intubated early?",
   "answer":"Progressive airway edema on bronchoscopy; in non-intubated patients with inhalation injury, progressive edema can threaten patency — bronchoscopy should be performed with a tracheal tube loaded over the bronchoscope so intubation can occur immediately if edema threatens the airway.",
   "rationale":"Airway edema from thermal/chemical injury progresses over hours; early securing before severe edema develops prevents emergent surgical airway in a hostile burned airway.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":""},
  {"id":"toxicology-icu-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Etomidate used for ICU sedation/induction has what clinically significant adrenal effect?",
   "answer":"Etomidate suppresses adrenocortical synthesis by inhibiting 11-beta-hydroxylase; even a single induction dose causes transient adrenal suppression (12-24 hours), concerning in septic shock patients who need intact stress cortisol response.",
   "rationale":"Etomidate's adrenal suppression is dose-dependent; in septic patients, blunted cortisol response worsens vasopressor requirements, making its use controversial in ICU management.",
   "bloom":"analyze","source":[{"book":"Morgan & Mikhail","page":290}],"confusable_with":""},
  {"id":"toxicology-icu-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the key organ system effects of etomidate useful for neurotoxicology/ICU management of elevated ICP?",
   "answer":"Etomidate decreases cerebral metabolic rate, cerebral blood flow, and ICP; minimal cardiovascular depression preserves cerebral perfusion pressure; similar EEG changes to barbiturates but increases somatosensory evoked potential amplitude.",
   "rationale":"Etomidate's cerebrovascular profile makes it useful for RSI in elevated ICP patients where cardiovascular stability is critical; it preserves CPP better than propofol.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":290}],"confusable_with":"Ketamine (increases ICP)"},
  {"id":"toxicology-icu-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Flumazenil reversal of benzodiazepines in an overdose patient carries what important clinical risk?",
   "answer":"Precipitation of benzodiazepine withdrawal seizures in dependent patients; re-sedation as flumazenil is cleared (half-life shorter than most benzodiazepines); gradual titration at 0.2 mg/min to total 0.6-1.0 mg is recommended.",
   "rationale":"Flumazenil's rapid hepatic clearance means re-sedation occurs after 1-2 hours if the benzodiazepine is still active; abrupt reversal in dependent patients triggers seizures.",
   "bloom":"apply","source":[{"book":"Morgan & Mikhail","page":467}],"confusable_with":""},
  {"id":"toxicology-icu-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the serotonin syndrome triad and what first-line pharmacological treatment is used?",
   "answer":"Triad: altered mental status + autonomic instability + neuromuscular abnormalities (clonus, hyperreflexia); first-line: benzodiazepines (lorazepam 1-2 mg IV per dose); cyproheptadine (serotonin antagonist) for severe cases; sedation/paralysis/intubation for severe hyperthermia.",
   "rationale":"Serotonin syndrome results from excess serotonergic activity; benzodiazepines reduce neuromuscular hyperactivity and agitation without directly blocking serotonin receptors.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":8}],"confusable_with":"NMS"},
]

# ============================================================
# ITEM 20: Tricuspid and Pulmonic Valve Disease
# ============================================================
topic = "Tricuspid and Pulmonic Valve Disease"
domain = "Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, valvular disease, hypertension & emergencies, lipids, syncope)"
disc = "medicine"

kps += [
  {"id":"tricuspid-pulmonic-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What are the common presenting symptoms of severe tricuspid stenosis and what physical examination findings result from elevated right atrial pressures?",
   "answer":"Fatigue/malaise, reduced cardiac output; exam: jugular venous distension, ascites, peripheral edema, pleural effusions, palpable hepatomegaly from venous congestion; right atrium dilates and thickens over time.",
   "rationale":"Tricuspid stenosis impedes RA-to-RV flow, elevating RA pressure and causing systemic venous congestion with all its downstream manifestations.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricuspid and Pulmonic Valve Disease","page":3}],"confusable_with":""},
  {"id":"tricuspid-pulmonic-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the most common indication for intervention in patients presenting with tricuspid valve pathology?",
   "answer":"Functional tricuspid regurgitation (TR) — the most common reason for intervention; results from right ventricular dilation/pulmonary hypertension rather than primary leaflet disease.",
   "rationale":"Functional TR results from annular dilation secondary to RV volume/pressure overload; addressing the underlying cause (pulmonary HTN, left-sided disease) is key alongside valve repair.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricuspid and Pulmonic Valve Disease","page":7}],"confusable_with":"Primary TR"},
  {"id":"tricuspid-pulmonic-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the diastolic pressure gradient between the right atrium and right ventricle, and what does this mean for prosthetic tricuspid valve anticoagulation?",
   "answer":"Right atrium has 3-5 mmHg higher diastolic pressure than the RV; the low-flow state on the right side of the heart mandates lifelong anticoagulation after TV prosthesis placement.",
   "rationale":"Low transvalvular flow in the right heart creates thrombogenic conditions; the risk of prosthetic valve thrombosis is higher for tricuspid than mitral/aortic prostheses.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Tricuspid and Pulmonic Valve Disease","page":7}],"confusable_with":""},
  {"id":"tricuspid-pulmonic-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the perioperative mortality rate for tricuspid valve surgery and what preoperative assessment is critical for transcatheter procedures?",
   "answer":"Perioperative mortality up to 10% in selected cases; appropriate patient selection is the most important preoperative assessment for transcatheter interventions, with post-procedure echocardiography required.",
   "rationale":"Tricuspid valve surgery carries higher mortality than left-sided valve surgery due to right heart failure, hepatic congestion, and comorbidities; careful selection optimizes outcomes.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricuspid and Pulmonic Valve Disease","page":11}],"confusable_with":""},
  {"id":"tricuspid-pulmonic-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"In congenital pulmonic stenosis, what is the hemodynamic consequence of obstruction to right ventricular outflow?",
   "answer":"Concentric right ventricular hypertrophy (pressure-overload pattern) from obstruction to RV outflow; severe stenosis causes fixed pulmonary blood flow and RV failure.",
   "rationale":"Sustained outflow obstruction forces the RV to generate supranormal systolic pressure; concentric hypertrophy adapts initially but eventually reduces RV compliance and cardiac output.",
   "bloom":"recall","source":[{"book":"Morgan & Mikhail","page":686}],"confusable_with":""},
  {"id":"tricuspid-pulmonic-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Patients with pacemakers receiving tricuspid valve replacement — what specific pacemaker complication may result from the procedure?",
   "answer":"TV prosthesis placement may displace or damage pacemaker leads; AV block and heart block are recognized complications requiring careful lead management; lifelong anticoagulation for the prosthesis.",
   "rationale":"Tricuspid valve anatomy is closely related to the AV node and bundle of His; surgical manipulation or device placement can cause conduction system injury.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Tricuspid and Pulmonic Valve Disease","page":7}],"confusable_with":""},
]

# ============================================================
# ITEM 21: Tricyclic Antidepressant (TCA) Toxicity
# ============================================================
topic = "Tricyclic Antidepressant (TCA) Toxicity"
domain = "Internal medicine: emergency & acute care (cardiopulmonary resuscitation, trauma primary survey, toxicology & overdoses, environmental emergencies, anaphylaxis, acute abdomen)"
disc = "medicine"

kps += [
  {"id":"tca-toxicity-d1","topic":topic,"domain":domain,"discipline":disc,
   "stem":"TCA overdose causes what classic ECG finding that helps distinguish it from other causes of altered consciousness and hypotension?",
   "answer":"QRS prolongation >100-120 ms (sodium channel blockade) and a rightward terminal 40-ms QRS axis; also PR prolongation, QTc prolongation, and right bundle branch block pattern.",
   "rationale":"TCAs block fast sodium channels in the His-Purkinje system causing conduction slowing; QRS >100 ms predicts seizures and >160 ms predicts ventricular arrhythmias.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":7}],"confusable_with":"Hyperkalemia"},
  {"id":"tca-toxicity-d2","topic":topic,"domain":domain,"discipline":disc,
   "stem":"TCAs are more toxic in overdose than newer antidepressant classes — what fatal toxicity index metric quantifies this?",
   "answer":"Fatal toxicity index (FTI) = ratio of self-poisoning mortality rates to prescription rates; older TCAs have higher FTI than SSRIs/SNRIs, reflecting greater lethality per overdose episode.",
   "rationale":"TCAs cause fatal cardiac arrhythmias and seizures at doses close to therapeutic; the narrow therapeutic index and multiple receptor blockade mechanisms make them extremely dangerous in overdose.",
   "bloom":"recall","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":7}],"confusable_with":""},
  {"id":"tca-toxicity-d3","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the first-line treatment for TCA-induced cardiac arrhythmia and why does alkalinization help?",
   "answer":"Sodium bicarbonate IV boluses to achieve arterial pH 7.45-7.55; alkalinization increases protein binding of TCAs (reducing free drug) and provides sodium loading that overcomes Na-channel blockade.",
   "rationale":"Alkaline pH increases TCA protein binding and reduces ionized drug fraction; elevated sodium gradient directly competes with TCA sodium channel blockade — dual mechanism of action.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":1}],"confusable_with":""},
  {"id":"tca-toxicity-d4","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What is the major drug-drug interaction risk when combining TCAs with SSRIs or MAOIs?",
   "answer":"Serotonin syndrome — the combination of TCAs (which inhibit serotonin reuptake) with SSRIs, SNRIs, or MAOIs causes serotonin excess, producing the triad of altered mental status, autonomic instability, and neuromuscular abnormalities.",
   "rationale":"TCAs have significant serotonin reuptake inhibition in addition to their norepinephrine and histamine effects; combining with other serotonergic agents causes dangerous serotonin accumulation.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":6}],"confusable_with":"Neuroleptic malignant syndrome"},
  {"id":"tca-toxicity-d5","topic":topic,"domain":domain,"discipline":disc,
   "stem":"Brain-derived neurotrophic factor (BDNF) is involved in antidepressant mechanism — what is the relationship between BDNF and antidepressant response?",
   "answer":"Antidepressants increase neuroprotective proteins including BDNF; BDNF concentrations in depression normalize with pharmacological treatment; increased BDNF and enhanced neuroplasticity correlates with remission.",
   "rationale":"The neuroplasticity hypothesis of depression proposes that BDNF deficiency causes synaptic atrophy in limbic structures; antidepressant-induced BDNF restoration is a final common pathway.",
   "bloom":"analyze","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":4}],"confusable_with":""},
  {"id":"tca-toxicity-d6","topic":topic,"domain":domain,"discipline":disc,
   "stem":"What factors predict non-compliance with antidepressant medications and increase risk of intentional overdose?",
   "answer":"Concerns about side effects (primary predictor), cognitive impairment comorbidities, alcohol/substance abuse, cardiovascular disease, metabolic disorders, young age, low income, and use of older-generation agents.",
   "rationale":"Non-adherence increases risk of both relapse and stockpiling of medication; identifying at-risk patients allows for closer monitoring and preference for safer antidepressant classes.",
   "bloom":"apply","source":[{"book":"StatPearls: StatPearls   Tricyclic Antidepressant (TCA) Toxicity","page":9}],"confusable_with":""},
]
kps.append({"_type":"illness_script","topic":topic,"discipline":disc,
  "enabling_conditions":"Depression/chronic pain treated with TCAs; intentional overdose; narrow therapeutic index",
  "pathophysiology":"Sodium channel blockade (cardiac conduction) + anticholinergic (tachycardia, dry mucous membranes, urinary retention, ileus) + antihistamine (sedation) + alpha-blockade (hypotension) + serotonin reuptake inhibition",
  "time_course":"Rapid onset <1-2 hours; arrhythmias may occur before or after CNS symptoms",
  "key_features":"QRS >100 ms, hypotension, altered consciousness/seizures, tachycardia, anticholinergic signs; ECG right terminal axis deviation",
  "consequence_if_missed":"Fatal ventricular arrhythmia from untreated Na-channel blockade; bicarb and airway control are life-saving interventions"})

print("Total KPs:", len(kps))
with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch4.json", "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Saved batch4")
