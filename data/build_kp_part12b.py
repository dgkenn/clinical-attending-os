import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load part A
exec(open('data/build_kp_part12.py', encoding='utf-8').read())

# ── 14: Cerebral Amyloid Angiopathy (CAA) ───────────────────────────────────
kps += [
  {"id":"caa-1","topic":"Cerebral Amyloid Angiopathy (CAA)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What is the pathological hallmark of cerebral amyloid angiopathy?",
   "answer":"Accumulation of amyloid beta-peptide within the leptomeninges and small-to-medium-sized cerebral blood vessels.",
   "rationale":"Amyloid deposition weakens vessel walls, predisposing to lobar hemorrhage and cortical superficial siderosis.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":2}],"confusable_with":"hypertensive microangiopathy"},
  {"id":"caa-2","topic":"Cerebral Amyloid Angiopathy (CAA)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What APOE alleles are associated with cerebral amyloid angiopathy and how do they differ in their effects?",
   "answer":"APOE e2 and e4 are both more prevalent in CAA; e4 is associated with higher vascular amyloid burden while e2 is linked to more severe vasculopathic changes.",
   "rationale":"APOE regulates amyloid clearance from brain vessels; e4 impairs clearance while e2 may alter vessel wall integrity differently.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":3}],"confusable_with":""},
  {"id":"caa-3","topic":"Cerebral Amyloid Angiopathy (CAA)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"By the Boston criteria v2.0, what lobar hemorrhagic MRI lesions define probable CAA?",
   "answer":"Lobar intracerebral hemorrhage, cerebral microbleeds, foci of cortical superficial siderosis, or convexity subarachnoid hemorrhage.",
   "rationale":"These lesion types reflect amyloid vessel fragility at cortical/lobar locations, distinguishing CAA from hypertensive hemorrhage (which is typically deep/basal ganglia).","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":5}],"confusable_with":"hypertensive hemorrhage (deep location)"},
  {"id":"caa-4","topic":"Cerebral Amyloid Angiopathy (CAA)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What MRI white matter finding suggests probable CAA when seen alone (single white matter feature criterion)?",
   "answer":"Severe perivascular spaces in the centrum semiovale (>20 visible) as a single white matter criterion supports probable CAA.",
   "rationale":"Enlarged perivascular spaces in the centrum semiovale (not basal ganglia) reflect impaired interstitial fluid drainage from amyloid-laden vessels.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":5}],"confusable_with":"basal ganglia perivascular spaces (hypertensive)"},
  {"id":"caa-5","topic":"Cerebral Amyloid Angiopathy (CAA)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What factors predict unfavorable outcomes in patients who suffer ICH from cerebral amyloid angiopathy?",
   "answer":"Larger hematoma size and age 75 or older predict unfavorable outcomes; sparing of ventricles and superficial location predict better prognosis.",
   "rationale":"Hematoma expansion and mass effect drive mortality; lobar superficial ICH without intraventricular extension carries lower mortality than deep ICH.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Amyloid Angiopathy (CAA)","page":7}],"confusable_with":""},
  {"_type":"illness_script","topic":"Cerebral Amyloid Angiopathy (CAA)","discipline":"medicine",
   "enabling_conditions":"Age >65, APOE e4 or e2 carrier, history of lobar hemorrhage",
   "pathophysiology":"Amyloid beta deposits in leptomeningeal and cortical vessel walls cause fragility, impaired autoregulation, and rupture",
   "time_course":"Gradual cognitive decline with episodic lobar hemorrhages; transient focal neurological episodes from cortical spreading depolarization",
   "key_features":"Lobar ICH (not deep), cortical superficial siderosis, convexity SAH, transient focal neurological episodes, MRI microbleeds at cortico-subcortical junctions",
   "consequence_if_missed":"Anticoagulation causes catastrophic rebleeding; missed diagnosis delays prognostication and anticoagulation avoidance counseling"}
]

# ── 15: Cerebral Venous Sinus Thrombosis (CVST) ─────────────────────────────
kps += [
  {"id":"cvst-1","topic":"Cerebral Venous Sinus Thrombosis (CVST)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What is the estimated annual incidence of CVST, and which population has markedly higher frequency?",
   "answer":"Annual incidence is 3-4 cases per million; peripartum/postpartum women have approximately 12 cases per 100,000 deliveries.",
   "rationale":"Pregnancy-associated hypercoagulability and dehydration markedly increase thrombosis risk in cerebral venous sinuses.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Venous Sinus Thrombosis (CVST)","page":3}],"confusable_with":""},
  {"id":"cvst-2","topic":"Cerebral Venous Sinus Thrombosis (CVST)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What broad spectrum of presentations can CVST mimic, making it a diagnostic challenge?",
   "answer":"CVST can mimic acute stroke, subarachnoid hemorrhage, meningoencephalitis, or benign intracranial hypertension.",
   "rationale":"Venous thrombosis causes diverse presentations depending on which sinuses are occluded and whether infarction, hemorrhage, or raised ICP predominates.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Venous Sinus Thrombosis (CVST)","page":2}],"confusable_with":"arterial stroke"},
  {"id":"cvst-3","topic":"Cerebral Venous Sinus Thrombosis (CVST)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What proportion of CVST patients have genetic or acquired thrombophilia, per the International Study on Cerebral Vein and Dural Sinus Thrombosis?",
   "answer":"Genetic and acquired thrombophilia identified in 34% of CVST patients (ISCVT).",
   "rationale":"Thrombophilia testing is indicated in CVST to guide duration of anticoagulation and genetic counseling.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Venous Sinus Thrombosis (CVST)","page":2}],"confusable_with":""},
  {"id":"cvst-4","topic":"Cerebral Venous Sinus Thrombosis (CVST)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What is the cord sign on CT and what does it indicate?",
   "answer":"The cord sign is a curvilinear hyperdensity within a cortical vein indicating thrombosis; it can be seen for up to 2 weeks after thrombosis.",
   "rationale":"Acute thrombus is hyperdense on CT due to hemoglobin concentration; detection of the cord sign allows early diagnosis before MRI/MRV is obtained.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Venous Sinus Thrombosis (CVST)","page":12}],"confusable_with":"delta sign (empty delta sign on contrast CT)"},
  {"id":"cvst-5","topic":"Cerebral Venous Sinus Thrombosis (CVST)","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What is the sensitivity limitation of D-dimer for ruling out CVST?",
   "answer":"D-dimer has an unacceptable false-negative rate of up to 26% for CVST, making it insufficient as a standalone rule-out test.",
   "rationale":"Unlike pulmonary embolism where D-dimer has high sensitivity, CVST may occur without generating sufficient fibrin degradation products to elevate D-dimer.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cerebral Venous Sinus Thrombosis (CVST)","page":5}],"confusable_with":"PE (high D-dimer sensitivity)"},
  {"_type":"illness_script","topic":"Cerebral Venous Sinus Thrombosis (CVST)","discipline":"medicine",
   "enabling_conditions":"Pregnancy/puerperium, OCP use, thrombophilia, dehydration, infection, malignancy, COVID-19, vaccine-induced thrombocytopenia",
   "pathophysiology":"Thrombosis of cerebral venous sinuses raises venous pressure, causing vasogenic edema, cortical venous infarction, and hemorrhage",
   "time_course":"Subacute onset days to weeks; thunderclap onset possible; 34% have thrombophilia",
   "key_features":"Progressive headache, papilledema, seizures, focal deficits, altered consciousness; CT cord sign or empty delta sign; MRV confirms occlusion",
   "consequence_if_missed":"Herniation from edema/hemorrhage, blindness from raised ICP, death; anticoagulation is treatment (even with hemorrhage in most cases)"}
]

# ── 16: Cholinergic Toxidrome ────────────────────────────────────────────────
kps += [
  {"id":"cholinergic-1","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What is the mechanism by which organophosphates produce toxicity different from carbamates?",
   "answer":"Organophosphates form stable, irreversible bonds to acetylcholinesterase that persist long after the drug disappears from circulation; carbamates form reversible bonds.",
   "rationale":"Irreversible AChE inhibition means organophosphate toxicity is prolonged and may require pralidoxime for enzyme regeneration within a time window.","bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":360}],"confusable_with":"carbamates (reversible)"},
  {"id":"cholinergic-2","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are the muscarinic effects of cholinergic toxidrome summarized by the SLUDGE mnemonic?",
   "answer":"Salivation, Lacrimation, Urination, Defecation, GI cramps, Emesis — plus miosis, bronchospasm, and bradycardia.",
   "rationale":"Excessive acetylcholine at muscarinic receptors activates secretory glands, smooth muscle, and slows the heart.","bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],"confusable_with":"nicotinic effects (fasciculations, paralysis)"},
  {"id":"cholinergic-3","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What nicotinic effects distinguish cholinergic toxidrome from a purely muscarinic presentation?",
   "answer":"Muscle fasciculations and paralysis (nicotinic); CNS effects include altered mentation and seizures.",
   "rationale":"Nicotinic receptor activation at neuromuscular junctions causes initial fasciculations followed by depolarizing blockade and flaccid paralysis.","bloom":"recall",
   "source":[{"book":"Curated Units","page":0}],"confusable_with":""},
  {"id":"cholinergic-4","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What cholinesterase inhibitors can act at cardiovascular and gastrointestinal cholinergic receptors to produce toxicity?",
   "answer":"All cholinesterase inhibitors (including organophosphates, carbamates, and therapeutic agents like neostigmine) can act at cardiovascular and GI cholinergic receptors.",
   "rationale":"Bradycardia and GI cramping from neostigmine in clinical use illustrate the same mechanism seen in more severe toxidrome.","bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":360}],"confusable_with":""},
  {"id":"cholinergic-5","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"Physostigmine reversal of anticholinergic toxidrome is limited to what specific indication?",
   "answer":"Physostigmine should only be used to reverse toxic, life-threatening delirium caused by an anticholinergic agent (atropine, scopolamine, diphenhydramine) — not for general cholinergic toxidrome.",
   "rationale":"Using physostigmine in cholinergic toxidrome would worsen ACh excess; it is an antidote for anticholinergic crisis, not for organophosphate poisoning.","bloom":"apply",
   "source":[{"book":"StatPearls","page":3}],"confusable_with":"atropine (treatment for cholinergic toxidrome)"},
  {"_type":"illness_script","topic":"Cholinergic Toxidrome (Organophosphates & Carbamates)","discipline":"medicine",
   "enabling_conditions":"Pesticide exposure, nerve agent (sarin, VX), excessive cholinesterase inhibitor dosing",
   "pathophysiology":"AChE inhibition causes accumulation of acetylcholine at muscarinic, nicotinic, and CNS synapses",
   "time_course":"Rapid onset minutes to hours after exposure; organophosphate effects persist longer due to irreversible binding",
   "key_features":"Miosis, bradycardia, bronchospasm, SLUDGE, fasciculations, paralysis, seizures, coma; may have normal or low pulse oximetry despite bronchospasm",
   "consequence_if_missed":"Respiratory failure from bronchospasm and paralysis; treatment is atropine (muscarinic) + pralidoxime (enzyme reactivation for OPs) + benzos (seizures)"}
]

# ── 17: Cryoglobulinemic vasculitis ─────────────────────────────────────────
kps += [
  {"id":"cryoglob-1","topic":"Cryoglobulinemic vasculitis","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What is the mechanism of type I cryoglobulinemia causing vascular obstruction versus mixed cryoglobulinemia causing vasculitis?",
   "answer":"Type I: monoclonal immunoglobulins (IgM or IgG) cause vascular obstruction through cryoprecipitate formation. Mixed (II/III): small-to-medium vessel vasculitis from complement-mediated immune complex deposition.",
   "rationale":"Type I is associated with B-cell lymphoproliferative disorders; mixed types are commonly HCV-associated and involve immune complex injury.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":3}],"confusable_with":""},
  {"id":"cryoglob-2","topic":"Cryoglobulinemic vasculitis","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What is the cornerstone of treatment for HCV-associated cryoglobulinemic vasculitis?",
   "answer":"Direct-acting antivirals (DAAs) for HCV; sustained virologic response is achieved in >95% of cases and halts antigenic stimulation driving cryoglobulin production.",
   "rationale":"HCV provides the ongoing B-cell antigenic stimulus for mixed cryoglobulin production; eradicating HCV removes this driver.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":8}],"confusable_with":""},
  {"id":"cryoglob-3","topic":"Cryoglobulinemic vasculitis","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What nephroprotective strategies reduce progression of renal disease in cryoglobulinemic vasculitis?",
   "answer":"Optimizing blood pressure control plus RAAS inhibitors and SGLT2 inhibitors to reduce proteinuria.",
   "rationale":"Cryoglobulinemic glomerulonephritis progresses with uncontrolled hypertension and proteinuria; these agents reduce renal hemodynamic stress.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":9}],"confusable_with":""},
  {"id":"cryoglob-4","topic":"Cryoglobulinemic vasculitis","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What prognosis do persistent cryoglobulinemia from untreated infections or B-cell disorders carry for kidney disease?",
   "answer":"Persistent cryoglobulinemia from untreated chronic infections, active autoimmune disease, or untreated B-cell lymphoproliferative disorders is associated with higher risk of kidney disease progression and cardiovascular complications.",
   "rationale":"Ongoing immune complex formation perpetuates glomerular injury; treatment of the underlying cause is the only disease-modifying strategy.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":11}],"confusable_with":""},
  {"id":"cryoglob-5","topic":"Cryoglobulinemic vasculitis","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What histopathological finding on renal biopsy distinguishes type I from mixed cryoglobulinemia?",
   "answer":"Type I: monoclonal IgG or IgM deposits with single light chain staining and C1q/C3. Mixed: both IgG and IgM with polyclonal light chains plus C1q, C3, C4, and membrane attack complex C5b-9.",
   "rationale":"Complement pathway involvement in mixed cryoglobulinemia reflects classical pathway activation by immune complexes, explaining the inflammatory vasculitis pattern.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Cryoglobulinemic vasculitis","page":4}],"confusable_with":""}
]

# ── 18: Cryptococcal Meningitis & Fungal CNS Infections ─────────────────────
kps += [
  {"id":"crypto-cns-1","topic":"Cryptococcal Meningitis & Fungal CNS Infections","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"At what CD4 count do latent herpesviruses (HSV-1, VZV, CMV) disseminate to cause CNS opportunistic infections in HIV patients?",
   "answer":"When CD4+ T-lymphocyte counts decline (typically below 100-50 cells/uL), latent viruses exploit immune failure and disseminate.",
   "rationale":"CD4 cells are required to maintain viral latency; progressive depletion removes immune surveillance allowing reactivation and spread.","bloom":"recall",
   "source":[{"book":"StatPearls","page":4}],"confusable_with":""},
  {"id":"crypto-cns-2","topic":"Cryptococcal Meningitis & Fungal CNS Infections","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"TB CNS disease occurs at what frequency increase in HIV-infected patients compared to immunocompetent patients?",
   "answer":"TB CNS disease occurs up to 8 times more often in patients with HIV infection compared to immunocompetent patients.",
   "rationale":"HIV-induced CD4 depletion impairs granuloma formation needed to contain Mycobacterium tuberculosis, allowing CNS dissemination.","bloom":"recall",
   "source":[{"book":"StatPearls","page":7}],"confusable_with":""},
  {"id":"crypto-cns-3","topic":"Cryptococcal Meningitis & Fungal CNS Infections","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What diagnostic test is available in CSF for cryptococcal meningitis and what is its sensitivity?",
   "answer":"Cryptococcal antigen or antibody detection in CSF is diagnostic in approximately 70% of cases of cryptococcal meningitis; cultures may take several weeks.",
   "rationale":"Cryptococcal antigen has high sensitivity in CSF and serum, enabling rapid diagnosis while cultures are pending.","bloom":"recall",
   "source":[{"book":"StatPearls","page":9}],"confusable_with":"India ink stain (lower sensitivity)"},
  {"id":"crypto-cns-4","topic":"Cryptococcal Meningitis & Fungal CNS Infections","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"For disseminated or severe coccidioidomycosis in an HIV patient, what is the treatment regimen?",
   "answer":"Fluconazole 400-800 mg orally once daily; for rapidly progressive disease, initial amphotericin B followed by step-down to fluconazole.",
   "rationale":"Fluconazole has good oral bioavailability and CNS penetration; amphotericin B provides more rapid fungicidal activity for critical disease.","bloom":"recall",
   "source":[{"book":"StatPearls","page":12}],"confusable_with":""},
  {"id":"crypto-cns-5","topic":"Cryptococcal Meningitis & Fungal CNS Infections","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What serum diagnostic markers are used to detect most invasive fungal infections, and what is the exception?",
   "answer":"1,3-beta-D-glucan (BDG) detects most invasive fungi; galactomannan is Aspergillus-specific. Cryptococcus and Mucor are notable BDG-negative exceptions.",
   "rationale":"Cryptococcus has a capsule that may limit BDG release; Mucorales lack BDG in their cell wall; targeted antigen tests are needed for these.","bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":125}],"confusable_with":"galactomannan (Aspergillus-specific)"}
]

# ── 19: Cyanide Toxicity ─────────────────────────────────────────────────────
kps += [
  {"id":"cyanide-1","topic":"Cyanide Toxicity","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What is the primary mechanism by which cyanide causes cellular toxicity?",
   "answer":"Cyanide binds cytochrome oxidase enzymes and inhibits cellular production of ATP, causing histotoxic hypoxia.",
   "rationale":"Blockade of complex IV prevents electron transfer to oxygen, halting oxidative phosphorylation despite adequate oxygen delivery.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":"carbon monoxide poisoning"},
  {"id":"cyanide-2","topic":"Cyanide Toxicity","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What clinical triad characterizes acute cyanide toxicity?",
   "answer":"Metabolic acidosis, cardiac arrhythmias, and increased venous oxygen content (due to inability to utilize oxygen).",
   "rationale":"Failure to extract oxygen at the tissue level results in high mixed venous oxygen saturation; lactic acidosis from anaerobic metabolism drives the metabolic acidosis.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":403}],"confusable_with":"CO poisoning (low venous O2)"},
  {"id":"cyanide-3","topic":"Cyanide Toxicity","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are the two mechanisms by which sodium nitroprusside can produce cyanide toxicity?",
   "answer":"Cumulative daily dose >500 mcg/kg or infusion rates >2 mcg/kg/min for more than a few hours releases cyanide from nitroprusside metabolism.",
   "rationale":"Each nitroprusside molecule releases five cyanide ions; excessive doses overwhelm hepatic thiosulfate detoxification capacity.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":407}],"confusable_with":""},
  {"id":"cyanide-4","topic":"Cyanide Toxicity","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What is the pharmacological mechanism of sodium nitrite in treating cyanide toxicity?",
   "answer":"Sodium nitrite oxidizes hemoglobin to methemoglobin (target 10-20%), which provides alternative binding sites for cyanide ions.",
   "rationale":"Cyanide has higher affinity for ferric methemoglobin than cytochrome oxidase; methemoglobin acts as a cyanide sink, restoring cytochrome function.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":408}],"confusable_with":""},
  {"id":"cyanide-5","topic":"Cyanide Toxicity","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"In a fire victim with synthetic materials exposure, what specific toxin must be considered beyond carbon monoxide?",
   "answer":"Cyanide toxicity — specifically from burning polyurethane-containing materials which release HCN gas.",
   "rationale":"Polyurethane combustion produces significant HCN; combined CO+CN poisoning in fire victims must be treated with both oxygen and cyanide antidotes.","bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":2136}],"confusable_with":"carbon monoxide poisoning only"},
  {"_type":"confusable_pair","topic_a":"Cyanide toxicity","topic_b":"Carbon monoxide poisoning",
   "discriminator":"Cyanide: HIGH venous O2 saturation (tissue cannot extract O2), metabolic acidosis disproportionate to presentation. CO: LOW venous O2 saturation, carboxyhemoglobin elevated, normal or low lactate early."}
]

# ── 20: Dementia Syndromes: Differential & Workup ────────────────────────────
# Chunks are thin for this specific topic — write defensible KPs from available text
kps += [
  {"id":"dementia-ddx-1","topic":"Dementia Syndromes: Differential & Workup","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What conditions must be distinguished from dementia in a patient presenting with cognitive decline and behavioral changes?",
   "answer":"Differential includes delirium, dementia, stroke, Parkinson disease, non-convulsive status epilepticus (NCSE), stiff person/locked-in syndromes, akinetic mutism, and anti-NMDAR encephalitis.",
   "rationale":"Many reversible conditions mimic dementia; NCSE and autoimmune encephalitis are particularly important to exclude as they are treatable.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":209}],"confusable_with":""},
  {"id":"dementia-ddx-2","topic":"Dementia Syndromes: Differential & Workup","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"When should EEG be performed in the workup of acute cognitive deterioration?",
   "answer":"EEG should be performed when non-convulsive status epilepticus is suspected, particularly after toxic/metabolic/infectious workup is completed.",
   "rationale":"NCSE causes persistent altered consciousness without convulsions; EEG is the only reliable way to detect subclinical seizure activity.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Delirium  Diagnosis, Subtypes & Assessment","page":5}],"confusable_with":""},
  {"id":"dementia-ddx-3","topic":"Dementia Syndromes: Differential & Workup","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"When is lumbar puncture indicated in the workup of cognitive decline or delirium?",
   "answer":"Lumbar puncture is rarely needed in delirium but should be performed when meningoencephalitis is suspected.",
   "rationale":"Most delirium is caused by systemic illness; LP is reserved when infectious or inflammatory CNS disease is specifically suspected based on clinical features.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Delirium  Diagnosis, Subtypes & Assessment","page":5}],"confusable_with":""},
  {"id":"dementia-ddx-4","topic":"Dementia Syndromes: Differential & Workup","domain":"Internal medicine: neurology (stroke, seizures, headache, neuro-ICU)","discipline":"medicine",
   "stem":"What is the role of neuroimaging in the evaluation of a new acute cognitive deterioration or delirium?",
   "answer":"Neuroimaging should be performed after toxic, metabolic, and infectious workup in cases of delirium to exclude structural causes.",
   "rationale":"Structural lesions (stroke, subdural hematoma, mass) can present as acute confusion; imaging complements the clinical evaluation.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Delirium  Diagnosis, Subtypes & Assessment","page":5}],"confusable_with":""}
]

# ── 21: Dialysis: CRRT in the ICU ────────────────────────────────────────────
kps += [
  {"id":"crrt-1","topic":"Dialysis: CRRT in the ICU","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"What is the principal physiological difference between diffusion (hemodialysis) and convection (hemofiltration)?",
   "answer":"Diffusion: concentration gradient drives small molecules (urea, creatinine) across a semi-permeable membrane. Convection: hydrostatic pressure forces medium-weight molecules across the membrane.",
   "rationale":"Convection removes middle molecules (cytokines, inflammatory mediators) more efficiently than diffusion, making it theoretically advantageous in sepsis.","bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":103}],"confusable_with":""},
  {"id":"crrt-2","topic":"Dialysis: CRRT in the ICU","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"What vascular access is typically used for renal replacement therapy in the ICU?",
   "answer":"A double-lumen catheter placed in the internal jugular, subclavian, or femoral vein.",
   "rationale":"Central venous access provides the blood flow rates (200-400 mL/min) required for adequate solute clearance with CRRT or IHD.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2145}],"confusable_with":""},
  {"id":"crrt-3","topic":"Dialysis: CRRT in the ICU","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"For what indications is renal replacement therapy employed in the ICU?",
   "answer":"To treat or prevent uremic complications in AKI when other measures fail.",
   "rationale":"Indications include refractory hyperkalemia, metabolic acidosis, volume overload, and uremic encephalopathy or pericarditis.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2145}],"confusable_with":""},
  {"id":"crrt-4","topic":"Dialysis: CRRT in the ICU","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"What does ultrafiltration (UF) accomplish in renal replacement therapy?",
   "answer":"Ultrafiltration removes plasma water by hydrostatic pressure (volume removal).",
   "rationale":"UF is essential for managing fluid overload in ICU patients; it can be performed independently of solute clearance in CRRT.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":103}],"confusable_with":""},
  {"id":"crrt-5","topic":"Dialysis: CRRT in the ICU","domain":"Internal medicine: nephrology","discipline":"medicine",
   "stem":"What comparative evidence exists for continuous versus intermittent hemodialysis in AKI survival and kidney function recovery?",
   "answer":"One RCT showed no difference in survival or recovery of kidney function between daily IHD and high-volume peritoneal dialysis; CRRT is preferred for hemodynamically unstable patients.",
   "rationale":"Hemodynamic instability during intermittent HD (from rapid fluid removal) makes CRRT preferable in critically ill patients.","bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   KDIGO 2012 AKI","page":113}],"confusable_with":""}
]

# ── 22: Drowning & Submersion Injury ─────────────────────────────────────────
kps += [
  {"id":"drowning-1","topic":"Drowning & Submersion Injury","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are the consistent blood gas findings in true near-drowning victims?",
   "answer":"Nearly all patients with true near-drowning have hypoxemia and hypercarbia with both metabolic and respiratory acidosis.",
   "rationale":"Prolonged submersion prevents gas exchange; mixed acidosis results from hypercapnia (respiratory) and lactic acid production (metabolic) from hypoxia.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2134}],"confusable_with":""},
  {"id":"drowning-2","topic":"Drowning & Submersion Injury","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What determines the degree of brain damage in near-drowning?",
   "answer":"Brain damage is primarily related to the duration of submersion and severity of asphyxia.",
   "rationale":"Cerebral ischemia from hypoxia is the primary driver of neurological injury; cold water submersion may paradoxically be protective via hypothermia.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2134}],"confusable_with":""},
  {"id":"drowning-3","topic":"Drowning & Submersion Injury","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What neurological complication frequently follows the hypoxic insult in near-drowning?",
   "answer":"Cerebral edema often complicates recovery after near-drowning.",
   "rationale":"Global cerebral ischemia triggers cytotoxic edema via NMDA receptor activation and calcium influx, leading to increased ICP.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2134}],"confusable_with":""},
  {"id":"drowning-4","topic":"Drowning & Submersion Injury","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"Near-drowning is listed as a direct cause of what critical pulmonary condition?",
   "answer":"Near-drowning causes direct lung injury leading to ARDS.",
   "rationale":"Aspiration of water (fresh or salt) damages the alveolar-capillary membrane, triggering diffuse alveolar damage characteristic of ARDS.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":59}],"confusable_with":""},
  {"id":"drowning-5","topic":"Drowning & Submersion Injury","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What additional traumatic injury must be considered in near-drowning from diving accidents?",
   "answer":"Cervical spine fractures must be considered in near-drowning victims from diving accidents.",
   "rationale":"Head-first impact at high speed transfers kinetic energy to the cervical spine; unstable fractures require immediate immobilization to prevent cord injury.","bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":2134}],"confusable_with":""}
]

# ── 23: Endocarditis Prophylaxis & Special Scenarios ─────────────────────────
kps += [
  {"id":"endo-prophy-1","topic":"Endocarditis Prophylaxis & Special Scenarios","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What four cardiac conditions are at significantly increased risk for endocarditis and warrant antibiotic prophylaxis for dental procedures?",
   "answer":"Prosthetic cardiac valves/material; prior infective endocarditis; unrepaired or partially repaired congenital heart disease; congenital HD with residual defects after repair.",
   "rationale":"These conditions have high endocarditis risk and severe potential consequences; evidence supports prophylaxis for dental procedures breaching oral mucosa.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":681}],"confusable_with":""},
  {"id":"endo-prophy-2","topic":"Endocarditis Prophylaxis & Special Scenarios","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What is the Class III recommendation regarding routine endocarditis prophylaxis?",
   "answer":"Prophylaxis is NOT recommended for nondental procedures and most cardiac conditions not on the high-risk list.",
   "rationale":"Evidence does not support prophylaxis for GI or GU procedures or for most congenital defects; overuse increases adverse effects and antibiotic resistance.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":681}],"confusable_with":""},
  {"id":"endo-prophy-3","topic":"Endocarditis Prophylaxis & Special Scenarios","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What are second-line agents for endocarditis prophylaxis in dental procedures for patients with penicillin allergy?",
   "answer":"Azithromycin and clindamycin are second-line agents for prophylaxis in penicillin-allergic patients.",
   "rationale":"Amoxicillin covers oral streptococci as first-line; in penicillin allergy, macrolides or clindamycin provide coverage for procedure-induced bacteremia.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Infective Endocarditis  Treatment & Surgery","page":7}],"confusable_with":""},
  {"id":"endo-prophy-4","topic":"Endocarditis Prophylaxis & Special Scenarios","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"In patients with a history of heparin-induced thrombocytopenia requiring cardiac surgery, what anticoagulation consideration applies?",
   "answer":"HIT patients produce heparin-dependent platelet factor 4 antibodies; if HIT history is remote and antibodies are undetectable, alternative timing or non-heparin anticoagulants must be considered.",
   "rationale":"Heparin re-exposure in patients with active HIT antibodies causes severe thrombocytopenia and life-threatening thrombosis.","bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":740}],"confusable_with":""},
  {"id":"endo-prophy-5","topic":"Endocarditis Prophylaxis & Special Scenarios","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What surgical prophylaxis dosing is recommended for cefazolin in patients over 120 kg?",
   "answer":"Cefazolin 3 g for patients >120 kg (standard dose 2 g for patients <120 kg).",
   "rationale":"Higher body weight requires higher doses to achieve adequate tissue concentrations throughout the surgical procedure.","bloom":"recall",
   "source":[{"book":"Stanford CA-1","page":92}],"confusable_with":""}
]

# ── 24: Envenomation: Snake & Arthropod ──────────────────────────────────────
kps += [
  {"id":"envenom-1","topic":"Envenomation: Snake & Arthropod","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"When should early endotracheal intubation be performed after envenomation to the head and neck area?",
   "answer":"Early intubation should occur if signs of airway compromise are present, because subsequent angioedema is highly likely to cause complete airway loss.",
   "rationale":"Venom-induced angioedema progresses rapidly; delaying intubation risks a lost airway in a patient already deteriorating.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Envenomation  Snake & Arthropod","page":3}],"confusable_with":""},
  {"id":"envenom-2","topic":"Envenomation: Snake & Arthropod","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What determines the degree of Crotalidae envenomation severity, rather than species alone?",
   "answer":"Management should be based on a combination of history, clinical severity, and lab findings — species alone does NOT dictate envenomation severity.",
   "rationale":"Venom composition and injected volume vary within species; clinical assessment of local and systemic effects guides antivenom dosing.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Envenomation  Snake & Arthropod","page":4}],"confusable_with":""},
  {"id":"envenom-3","topic":"Envenomation: Snake & Arthropod","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are the threshold values for repeat Crotalidae antivenom dosing when coagulopathy recurs between 3-7 days after treatment?",
   "answer":"Repeat dosing if platelet count <25,000, fibrinogen <50 ug/mL, or multi-component coagulopathy.",
   "rationale":"Late coagulopathy recurrence occurs as early antivenom is cleared; venom persists in tissues and can continue consuming clotting factors.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Envenomation  Snake & Arthropod","page":6}],"confusable_with":""},
  {"id":"envenom-4","topic":"Envenomation: Snake & Arthropod","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are the characteristics of severe Crotalidae envenomation?",
   "answer":"5-10% of envenomations; life-threatening coagulopathies with profound local findings (erythema, edema), hypotension, and angioedema.",
   "rationale":"Severe envenomation reflects high venom load with systemic effects; aggressive antivenom dosing and ICU support are required.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Envenomation  Snake & Arthropod","page":5}],"confusable_with":""},
  {"id":"envenom-5","topic":"Envenomation: Snake & Arthropod","domain":"Internal medicine: emergency & toxicology","discipline":"medicine",
   "stem":"What are signs of distal bleeding that may occur from Crotalidae venom's effect on coagulation and platelet aggregation?",
   "answer":"Gingival bleeding and epistaxis are common signs of distal bleeding from venom-induced coagulopathy.",
   "rationale":"Venom disintegrins and phospholipases impair platelet aggregation and degrade fibrinogen, causing systemic hemorrhage remote from the bite site.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Envenomation  Snake & Arthropod","page":9}],"confusable_with":""}
]

# ── 25: eGPA/Churg-Strauss ──────────────────────────────────────────────────
kps += [
  {"id":"egpa-1","topic":"Eosinophilic granulomatosis with polyangiitis (eGPA/Churg-Strauss)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What clinical diagnostic criteria support a diagnosis of eosinophilic granulomatosis with polyangiitis?",
   "answer":"4 or more of: asthma, blood eosinophilia >10%, neuropathy, pulmonary infiltrates, sinusitis, extravascular eosinophils on biopsy.",
   "rationale":"EGPA is defined by its triad of asthma, eosinophilia, and necrotizing vasculitis; the diagnostic criteria reflect these core features.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":177}],"confusable_with":"GPA (no asthma/eosinophilia requirement)"},
  {"id":"egpa-2","topic":"Eosinophilic granulomatosis with polyangiitis (eGPA/Churg-Strauss)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"In what temporal relationship does asthma precede EGPA vasculitis?",
   "answer":"Asthma and allergic rhinitis precede the vasculitic phase in EGPA.",
   "rationale":"EGPA evolves in three phases: allergic (asthma/rhinitis), eosinophilic (organ infiltration), and vasculitic; recognizing the prodrome enables earlier diagnosis.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":177}],"confusable_with":""},
  {"id":"egpa-3","topic":"Eosinophilic granulomatosis with polyangiitis (eGPA/Churg-Strauss)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What is the major cause of mortality in eosinophilic granulomatosis with polyangiitis?",
   "answer":"Cardiac involvement (cardiomyopathy, eosinophilic myocarditis) is the major cause of mortality in EGPA.",
   "rationale":"Eosinophilic infiltration of the myocardium causes endomyocardial fibrosis and cardiomyopathy, which is the leading cause of death in EGPA.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":177}],"confusable_with":""},
  {"id":"egpa-4","topic":"Eosinophilic granulomatosis with polyangiitis (eGPA/Churg-Strauss)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"EGPA is part of which broader group of diseases sharing necrotizing vasculitis of small-to-medium vessels?",
   "answer":"EGPA is one of three ANCA-associated vasculitides along with GPA (Wegener) and microscopic polyangiitis (MPA).",
   "rationale":"ANCA-associated vasculitides share pathological features of pauci-immune necrotizing vasculitis; EGPA is the eosinophil-predominant variant.","bloom":"recall",
   "source":[{"book":"StatPearls","page":2}],"confusable_with":"GPA, MPA"},
  {"_type":"confusable_pair","topic_a":"eGPA (Churg-Strauss)","topic_b":"GPA (Wegener)",
   "discriminator":"eGPA: asthma + eosinophilia + cardiac involvement; MPO-ANCA positive. GPA: upper airway destruction (saddle nose), renal involvement, pulmonary nodules; PR3-ANCA positive. Neither requires eosinophilia."}
]

# ── 26: Fibromyalgia & central sensitization ──────────────────────────────────
kps += [
  {"id":"fibro-1","topic":"Fibromyalgia & central sensitization","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What three spinal cord mechanisms are responsible for central sensitization?",
   "answer":"(1) Wind-up and sensitization of second-order wide dynamic range neurons; (2) dorsal horn neuron receptive field expansion; (3) hyperexcitability of flexion reflexes.",
   "rationale":"Central sensitization amplifies pain signals beyond the site of peripheral injury, explaining widespread allodynia and hyperalgesia in fibromyalgia.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1702}],"confusable_with":""},
  {"id":"fibro-2","topic":"Fibromyalgia & central sensitization","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What neurotransmitter receptor is critical for wind-up and induction of central sensitization in the spinal cord?",
   "answer":"NMDA receptor activation by L-glutamate and L-aspartate is critical for wind-up and induction and maintenance of central sensitization.",
   "rationale":"NMDA receptors amplify repeated C-fiber input through calcium influx, causing long-term potentiation of dorsal horn neurons.","bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1724}],"confusable_with":"AMPA receptors"},
  {"id":"fibro-3","topic":"Fibromyalgia & central sensitization","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What neurochemical mediators drive central sensitization in addition to excitatory amino acids?",
   "answer":"Substance P, CGRP, vasoactive intestinal peptide (VIP), cholecystokinin (CCK), angiotensin, and galanin.",
   "rationale":"These neuropeptides co-released from primary afferents facilitate dorsal horn neuron excitability through G-protein coupled receptors.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1724}],"confusable_with":""},
  {"id":"fibro-4","topic":"Fibromyalgia & central sensitization","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What peripheral mechanisms contribute to neuropathic pain states that overlap with central sensitization?",
   "answer":"Spontaneous discharges, sensitization of receptors to mechanical/thermal/chemical stimuli, upregulation of adrenergic receptors, and neural inflammation.",
   "rationale":"Peripheral sensitization lowers the threshold for central sensitization; both mechanisms operate together in fibromyalgia and chronic pain.","bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1726}],"confusable_with":""},
  {"id":"fibro-5","topic":"Fibromyalgia & central sensitization","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What is the phenomenon of wind-up in the context of wide dynamic range neurons?",
   "answer":"WDR neurons increase discharge frequency with the same repetitive stimuli and exhibit prolonged firing even after C-fiber input stops.",
   "rationale":"Wind-up represents temporal summation at the spinal level; repeated C-fiber activation progressively lowers the firing threshold, amplifying pain.","bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1724}],"confusable_with":""}
]

# ── 27: GPA/Wegener ──────────────────────────────────────────────────────────
kps += [
  {"id":"gpa-1","topic":"Granulomatosis with polyangiitis (GPA/Wegener)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What type of vasculitis is granulomatosis with polyangiitis and what vessels are affected?",
   "answer":"GPA is a necrotizing granulomatous vasculitis affecting small to medium-sized vessels.",
   "rationale":"Granulomatous inflammation distinguishes GPA from MPA (non-granulomatous); the classic triad involves upper airways, lungs, and kidneys.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)","page":2}],"confusable_with":"MPA (no granulomas)"},
  {"id":"gpa-2","topic":"Granulomatosis with polyangiitis (GPA/Wegener)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"GPA is one of three ANCA-associated vasculitides. What are the other two?",
   "answer":"Microscopic polyangiitis (MPA) and eosinophilic granulomatosis with polyangiitis (EGPA/Churg-Strauss).",
   "rationale":"All three share ANCA positivity and pauci-immune necrotizing vasculitis but differ in granuloma formation and organ involvement patterns.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)","page":1}],"confusable_with":""},
  {"id":"gpa-3","topic":"Granulomatosis with polyangiitis (GPA/Wegener)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What proportion of patients with anti-GBM disease also have detectable ANCA, and what does GBM antibody pattern resemble?",
   "answer":"Up to 10% of ANCA-associated vasculitis patients have circulating anti-GBM antibodies; in double-positive patients, renal manifestations follow the anti-GBM pattern while systemic features follow ANCA pattern.",
   "rationale":"ANCA-associated inflammation may expose GBM epitopes, inducing secondary anti-GBM antibodies; double-positive disease carries worse renal prognosis.","bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)","page":4}],"confusable_with":""},
  {"id":"gpa-4","topic":"Granulomatosis with polyangiitis (GPA/Wegener)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"What biopsy approach maximizes diagnostic yield in GPA?",
   "answer":"Avoid necrotic areas when performing biopsies; FDG-PET/CT can identify active lesions to increase biopsy yield.",
   "rationale":"Biopsy of necrotic tissue yields only dead cells and fibrin, not the diagnostic granulomatous vasculitis required for histological confirmation.","bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)","page":9}],"confusable_with":""},
  {"id":"gpa-5","topic":"Granulomatosis with polyangiitis (GPA/Wegener)","domain":"Internal medicine: rheumatology & immunology","discipline":"medicine",
   "stem":"The ACR and EULAR are developing treatment criteria for ANCA-associated vasculitis. What is the basis for current treatment protocols?",
   "answer":"Treatment based on new clinical trial data with protocols including rituximab or cyclophosphamide for induction plus maintenance therapy.",
   "rationale":"Both rituximab and cyclophosphamide achieve remission in GPA; rituximab is favored for relapsing disease or when cyclophosphamide toxicity is a concern.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Granulomatosis with polyangiitis (GPA Wegener)","page":9}],"confusable_with":""}
]

# ── 28: HIV-Associated Opportunistic Infections: Diagnosis & Treatment ────────
kps += [
  {"id":"hiv-oi-1","topic":"HIV-Associated Opportunistic Infections: Diagnosis & Treatment","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What CSF test is diagnostic in approximately 70% of cryptococcal meningitis in HIV patients?",
   "answer":"Cryptococcal antigen or antibody detection in CSF is diagnostic in ~70% of cases; cultures can take weeks.",
   "rationale":"Cryptococcal antigen has high sensitivity and specificity in both serum and CSF; it enables diagnosis before slow-growing culture results return.","bloom":"recall",
   "source":[{"book":"StatPearls","page":9}],"confusable_with":""},
  {"id":"hiv-oi-2","topic":"HIV-Associated Opportunistic Infections: Diagnosis & Treatment","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What is the preferred regimen for Toxoplasma encephalitis (TE) in an HIV patient when pyrimethamine is unavailable?",
   "answer":"Co-trimoxazole (TMP-SMX) is equally effective to pyrimethamine-based regimens and should be preferred when pyrimethamine is unavailable or cost-limited.",
   "rationale":"Recent meta-analysis shows co-trimoxazole matches pyrimethamine/sulfadiazine efficacy with potentially better safety profile and global availability.","bloom":"apply",
   "source":[{"book":"StatPearls","page":11}],"confusable_with":""},
  {"id":"hiv-oi-3","topic":"HIV-Associated Opportunistic Infections: Diagnosis & Treatment","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What diagnostic workup should be performed in HIV patients with suspected lymph node or bone marrow opportunistic infections?",
   "answer":"Lymph node biopsy and bone marrow aspirate or biopsy with microbiological cultures and pathological examination.",
   "rationale":"Disseminated infections (MAC, histoplasma, leishmaniasis) commonly involve lymph nodes and bone marrow; tissue diagnosis is often required.","bloom":"recall",
   "source":[{"book":"StatPearls","page":9}],"confusable_with":""},
  {"id":"hiv-oi-4","topic":"HIV-Associated Opportunistic Infections: Diagnosis & Treatment","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"For disseminated coccidioidomycosis in HIV, what is the treatment regimen?",
   "answer":"Fluconazole 400-800 mg orally once daily; amphotericin B for rapidly progressive disease with step-down to fluconazole.",
   "rationale":"Coccidioidomycosis disseminates in severe immunosuppression; azoles are mainstay but fungicidal amphotericin B is required for critical presentations.","bloom":"recall",
   "source":[{"book":"StatPearls","page":12}],"confusable_with":""},
  {"id":"hiv-oi-5","topic":"HIV-Associated Opportunistic Infections: Diagnosis & Treatment","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"Why is lumbar puncture and CNS imaging important in HIV patients with suspected opportunistic infections?",
   "answer":"CNS investigation is required as TB CNS disease occurs up to 8x more often in HIV; opportunistic infections almost always require LP and imaging for prognostication.",
   "rationale":"Multiple OIs (cryptococcus, toxoplasma, TB, CMV) can cause CNS disease simultaneously; LP and imaging guide specific diagnosis and treatment.","bloom":"apply",
   "source":[{"book":"StatPearls","page":7}],"confusable_with":""}
]

# ── 29: HIV: Antiretroviral Therapy (ART) ────────────────────────────────────
# Chunks are thin/off-topic (Florida lab safety); write defensible KPs from available content
kps += [
  {"id":"hiv-art-1","topic":"HIV: Antiretroviral Therapy (ART)","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What has antiretroviral therapy (ART) achieved for the life expectancy of people with HIV when started early?",
   "answer":"When started early, ART has enabled people with HIV to live as long as those without the disease.",
   "rationale":"Untreated HIV progresses to AIDS in ~11 years; effective ART suppresses viral replication, preserving CD4 count and preventing AIDS-defining illnesses.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":2}],"confusable_with":""},
  {"id":"hiv-art-2","topic":"HIV: Antiretroviral Therapy (ART)","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"HIV belongs to what virus family and what is the significance of its retroviral genome?",
   "answer":"HIV belongs to the retrovirus family; retroviruses use reverse transcriptase to convert RNA genome into DNA for integration into the host genome.",
   "rationale":"Reverse transcription and genomic integration make HIV a permanent resident in host cells; ART must suppress replication without eradicating integrated provirus.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":2}],"confusable_with":""},
  {"id":"hiv-art-3","topic":"HIV: Antiretroviral Therapy (ART)","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What IDSA metabolic monitoring is recommended at initiation of ART and within 3 months?",
   "answer":"Fasting plasma glucose and HbA1c should be obtained before and within 3 months of initiating ART.",
   "rationale":"Some ART regimens (especially older PIs) cause insulin resistance and metabolic syndrome; early detection enables preventive interventions.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Osteoporosis  screening, diagnosis & treatment","page":16}],"confusable_with":""},
  {"id":"hiv-art-4","topic":"HIV: Antiretroviral Therapy (ART)","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What modes of HIV transmission are NOT possible through casual contact?",
   "answer":"HIV cannot be transmitted through saliva, kissing, spitting, or sharing drinks.",
   "rationale":"HIV requires contact with blood, semen, vaginal secretions, or breast milk in sufficient concentrations; saliva has inhibitory proteins and insufficient viral load.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":5}],"confusable_with":""}
]

# ── 30: HIV: Complications & Comorbidities ───────────────────────────────────
# Chunks are very thin (structural HIV facts + unrelated pages)
kps += [
  {"id":"hiv-compl-1","topic":"HIV: Complications & Comorbidities","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What structural proteins form the spikes on the HIV envelope and what is their functional role?",
   "answer":"gp120 and gp41 form the envelope spikes; gp120 binds CD4 and CCR5/CXCR4 co-receptors while gp41 mediates membrane fusion.",
   "rationale":"gp120-CD4 binding is the initial step in viral entry; CCR5 antagonists target this co-receptor, preventing entry in CCR5-tropic HIV strains.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   HIV  Complications & Comorbidities","page":2}],"confusable_with":""},
  {"id":"hiv-compl-2","topic":"HIV: Complications & Comorbidities","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What bone density change is associated with tenofovir disoproxil fumarate (TDF)-based ART regimens in HIV patients?",
   "answer":"Tenofovir disoproxil fumarate is associated with more significant bone density loss; switching to a non-TDF regimen improves bone density.",
   "rationale":"TDF inhibits mitochondrial DNA polymerase in osteoblasts and impairs proximal tubular reabsorption of phosphate, both reducing bone mineral density.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Osteoporosis  screening, diagnosis & treatment","page":4}],"confusable_with":""},
  {"id":"hiv-compl-3","topic":"HIV: Complications & Comorbidities","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"HIV infection causes thrombocytopenia by what mechanisms?",
   "answer":"HIV-associated thrombocytopenia occurs through immune destruction (HIV/HCV infection), impaired production, and drug effects (chemo, antibiotics).",
   "rationale":"Multiple mechanisms contribute: direct viral suppression of megakaryocytes, antiplatelet antibodies, and co-infection with HCV or CMV causing marrow suppression.","bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":139}],"confusable_with":""}
]

# ── 31: HIV: Diagnosis & Initial Evaluation ──────────────────────────────────
kps += [
  {"id":"hiv-dx-1","topic":"HIV: Diagnosis & Initial Evaluation","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What are the clinical manifestations of acute HIV infection and when do they typically present after infection?",
   "answer":"Mono-like syndrome with rash, lymphadenopathy, fever, oral ulcers, pharyngitis, myalgias, and diarrhea; presents 3-6 weeks after infection.",
   "rationale":"Acute retroviral syndrome reflects high-level viremia during primary infection before the immune response mounts; early recognition allows early ART initiation.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":127}],"confusable_with":"EBV mononucleosis"},
  {"id":"hiv-dx-2","topic":"HIV: Diagnosis & Initial Evaluation","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What defines AIDS in a patient with known HIV infection?",
   "answer":"AIDS = HIV infection with CD4 count <200 cells/uL or an AIDS-defining illness.",
   "rationale":"CD4 <200 defines severe immunosuppression at which opportunistic infections occur; AIDS-defining illnesses represent clinical manifestations of this immunodeficiency.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":127}],"confusable_with":""},
  {"id":"hiv-dx-3","topic":"HIV: Diagnosis & Initial Evaluation","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What epidemiologic risk factors increase transmission risk and should be assessed at initial HIV evaluation?",
   "answer":"Multiple sexual partners, exchange of sex for money/drugs, alcohol or drug use before/during sex, intravenous drug use.",
   "rationale":"Behavioral risk assessment guides counseling, partner testing, and pre-exposure prophylaxis (PrEP) discussions for uninfected close contacts.","bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   HIV  Antiretroviral Therapy (ART)","page":5}],"confusable_with":""},
  {"id":"hiv-dx-4","topic":"HIV: Diagnosis & Initial Evaluation","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What is the risk of HIV transmission following needlestick injury with HIV-infected blood?",
   "answer":"Needlestick injury with HIV-infected blood represents the most common occupational transmission mechanism; risk can be estimated based on depth of injury, blood volume, and viral load.",
   "rationale":"Parenteral transmission is the most efficient occupational route; post-exposure prophylaxis (PEP) must be started within 72 hours.","bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":2044}],"confusable_with":""}
]

# ── 32: HIV: Opportunistic Infection Prophylaxis ─────────────────────────────
kps += [
  {"id":"hiv-oipx-1","topic":"HIV: Opportunistic Infection Prophylaxis","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What prophylaxis regimen should be initiated for Pneumocystis jirovecii pneumonia (PCP) and Toxoplasma encephalitis, and at what CD4 threshold?",
   "answer":"TMP-SMX (co-trimoxazole) is first-line prophylaxis for both PCP and Toxoplasma encephalitis; started at CD4 <200 (PCP) and CD4 <100 with positive Toxo IgG (Toxoplasma).",
   "rationale":"TMP-SMX inhibits folic acid synthesis in both Pneumocystis and Toxoplasma; primary prophylaxis prevents these common AIDS-defining infections.","bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":127}],"confusable_with":""},
  {"id":"hiv-oipx-2","topic":"HIV: Opportunistic Infection Prophylaxis","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What monitoring is required during ganciclovir or valganciclovir prophylaxis for CMV disease in HIV patients?",
   "answer":"Close monitoring of CBC for myelosuppression (neutropenia, anemia, thrombocytopenia) and renal function for nephrotoxicity.",
   "rationale":"Ganciclovir is a potent inhibitor of bone marrow proliferation; neutropenia is the dose-limiting toxicity and requires dose adjustment or G-CSF support.","bloom":"recall",
   "source":[{"book":"StatPearls","page":15}],"confusable_with":"acyclovir (renal monitoring only)"},
  {"id":"hiv-oipx-3","topic":"HIV: Opportunistic Infection Prophylaxis","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What liver function monitoring is required during antifungal prophylaxis in HIV patients?",
   "answer":"Liver function must be monitored for hepatotoxicity during azole antifungal prophylaxis.",
   "rationale":"Azoles (fluconazole, itraconazole) inhibit CYP3A4 and are hepatotoxic; drug interactions with ART require careful monitoring.","bloom":"recall",
   "source":[{"book":"StatPearls","page":15}],"confusable_with":""},
  {"id":"hiv-oipx-4","topic":"HIV: Opportunistic Infection Prophylaxis","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"HIV infection shares overlapping epidemiologic pathways with which sexually transmitted and IV drug use-related infections?",
   "answer":"Hepatitis A, B, and C; syphilis (STI-shared); S. aureus and hepatitis C (IVDU-associated).",
   "rationale":"Shared transmission routes mean HIV-positive patients should be screened and vaccinated for these co-infections at initial evaluation.","bloom":"recall",
   "source":[{"book":"StatPearls","page":3}],"confusable_with":""},
  {"id":"hiv-oipx-5","topic":"HIV: Opportunistic Infection Prophylaxis","domain":"Internal medicine: infectious disease","discipline":"medicine",
   "stem":"What is the global burden of HIV infection as of recent estimates?",
   "answer":"Approximately 40.8 million people are living with HIV infection globally.",
   "rationale":"Understanding epidemiology guides public health screening strategies and resource allocation for prophylaxis programs.","bloom":"recall",
   "source":[{"book":"StatPearls","page":3}],"confusable_with":""}
]

print(f"Total KPs: {len(kps)}")
kp_count = len([x for x in kps if '_type' not in x])
script_count = len([x for x in kps if x.get('_type') == 'illness_script'])
pair_count = len([x for x in kps if x.get('_type') == 'confusable_pair'])
print(f"KP objects: {kp_count}, illness_scripts: {script_count}, confusable_pairs: {pair_count}")

# Validate IDs unique
ids = [x.get('id') for x in kps if 'id' in x]
assert len(ids) == len(set(ids)), "Duplicate IDs found!"
print("IDs unique: OK")

# Write output
with open('data/kp_full_part_12.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written to data/kp_full_part_12.json")

# Verify parses
with open('data/kp_full_part_12.json', 'r', encoding='utf-8') as f:
    check = json.load(f)
print(f"Parses OK: {len(check)} entries")
