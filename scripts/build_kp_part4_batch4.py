
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = []
DOM_HEME = ('Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & '
            'treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)')
DOM_NEPH = 'Internal medicine: nephrology, fluids & electrolytes'
DOM_GEN = ('General internal medicine, preventive care & geriatrics (admission & cross-cover problems, '
           'perioperative medicine, screening & vaccination, polypharmacy & deprescribing, frailty, '
           'delirium prevention, goals of care)')
DOM_CARD = ('Internal medicine: cardiology (ACS, stable & unstable angina, heart failure, brady/tachyarrhythmias, '
            'valvular disease, hypertension & emergencies, lipids, syncope)')
DOM_ENDO = ('Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & '
            'storm, adrenal insufficiency, calcium disorders, pituitary)')
DIS = 'medicine'

# ── [144] Hypercoagulable states in malignancy ────────────────────────────────
T = 'Hypercoagulable states in malignancy (Trousseau syndrome)'
kps += [
  {'id':'trousseau-syndrome-d1','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'In Budd-Chiari syndrome, what proportion of cases have an underlying prothrombotic or hypercoagulable cause?',
   'answer':'80% of Budd-Chiari cases have some underlying prothrombotic cause (myeloproliferative disorders most common)',
   'rationale':'Hypercoagulable states (MPNs, antiphospholipid syndrome, factor V Leiden, PNH) preferentially thrombose hepatic veins due to sluggish flow.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Budd Chiari Syndrome','page':2}],'confusable_with':'secondary Budd-Chiari (external compression by malignancy rather than primary thrombosis)'},
  {'id':'trousseau-syndrome-d2','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'Which inherited thrombophilias are specifically listed as causes of Budd-Chiari syndrome?',
   'answer':'Factor V Leiden (protein C resistance), antiphospholipid antibody syndrome, antithrombin deficiency, and paroxysmal nocturnal haemoglobinuria (PNH)',
   'rationale':'These thrombophilias cause hyperactivation of the coagulation cascade; hepatic veins with naturally slow flow are particularly vulnerable.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Budd Chiari Syndrome','page':2}],'confusable_with':''},
  {'id':'trousseau-syndrome-d3','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'Superior vena cava (SVC) syndrome in malignancy: what are the most common malignant causes?',
   'answer':'Small-cell bronchogenic carcinoma (most common), followed by non-Hodgkins lymphoma; symptoms include neck/face swelling, arm swelling, dyspnea, dilated chest collaterals',
   'rationale':'Mediastinal tumours compress the SVC directly or via lymph node involvement; this is now the dominant aetiology since infectious (syphilitic) SVC occlusion has declined.',
   'bloom':'recall','source':[{'book':'StatPearls','page':2}],'confusable_with':'fibrosing mediastinitis (benign SVC obstruction)'},
  {'id':'trousseau-syndrome-d4','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'In DIC associated with malignancy, anticoagulant use (heparin) is generally limited to conditions with what risk profile?',
   'answer':'Heparin use in DIC is controversial and recommended to be limited to conditions with the highest thrombotic risk; antifibrinolytic therapy is generally contraindicated in DIC',
   'rationale':'DIC involves simultaneous coagulation activation and fibrinolysis; antifibrinolytics risk catastrophic thrombosis; heparin risks worsening haemorrhage.',
   'bloom':'analyze','source':[{'book':'Miller/Baby Miller','page':446}],'confusable_with':''},
  {'id':'trousseau-syndrome-d5','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'In Trousseau syndrome (cancer-associated hypercoagulability), which cancer type most characteristically presents with migratory superficial thrombophlebitis?',
   'answer':'Pancreatic carcinoma is classically associated with migratory thrombophlebitis (Trousseau sign); also seen in lung, GI, and mucin-secreting adenocarcinomas',
   'rationale':'Mucin and tissue factor released by pancreatic tumours activate coagulation; migratory thrombophlebitis may precede cancer diagnosis.',
   'bloom':'recall','source':[{'book':'Miller/Baby Miller','page':446}],'confusable_with':''},
  {'id':'trousseau-syndrome-d6','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'Tumour lysis syndrome (TLS) causes which electrolyte triad and what renal complication?',
   'answer':'Hyperuricaemia, hyperphosphataemia, and hyperkalemia (with resulting hypocalcaemia); renal complication is uric acid/calcium phosphate crystal deposition in distal tubules causing AKI',
   'rationale':'Massive cell lysis releases purines (->uric acid), phosphate, and potassium; precipitates deposit in tubules, worsening by low urine pH and flow.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Oncologic emergencies  tumor lysis syndrome','page':6}],'confusable_with':'rhabdomyolysis (elevated CK, normal uric acid relatively; myoglobin in tubules)'},
  {'id':'trousseau-syndrome-d7','topic':T,'domain':DOM_HEME,'discipline':DIS,
   'stem':'Liver failure in advanced cancer impairs coagulation; what proportion of transplant candidate MELD scores >=35 accounts for post-transplant need?',
   'answer':'Highest-acuity MELD >=35 recipients account for about a fifth of transplants; current median wait time for transplant candidates is 11 months',
   'rationale':'Understanding transplant allocation helps frame discussions about cancer patients with liver involvement and their transplant eligibility.',
   'bloom':'apply','source':[{'book':'Miller/Baby Miller','page':688}],'confusable_with':''},
]

# ── [145] Hyperkalemia ────────────────────────────────────────────────────────
T = 'Hyperkalemia'
kps += [
  {'id':'hyperkalemia-d1','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'What are the three severity thresholds for hyperkalemia, and at what level do the most dangerous ECG changes appear?',
   'answer':'Mild 5.5-6.5 mEq/L, moderate 6.6-7.5 mEq/L, severe >7.5 mEq/L; most dangerous changes (sine wave, VF risk) occur at severe levels',
   'rationale':'ECG changes progress with K+: peaked T waves (mild), PR prolongation and wide QRS (moderate), sine wave pattern and VF risk (severe).',
   'bloom':'recall','source':[{'book':'Stanford CA-1','page':58}],'confusable_with':''},
  {'id':'hyperkalemia-d2','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'How do beta-2 adrenergic agonists shift potassium, and what clinical effect does this have?',
   'answer':'Beta-2 agonists activate Na-K-ATPase, shifting K+ into muscle and liver, decreasing plasma K+; can transiently treat hyperkalemia',
   'rationale':'Catecholamine-induced K+ redistribution is rapid (onset minutes); useful as temporising measure in severe hyperkalaemia alongside calcium and insulin/dextrose.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':1877}],'confusable_with':'alpha-adrenergic stimulation (impairs K+ intracellular movement, can worsen hyperkalemia)'},
  {'id':'hyperkalemia-d3','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Acute increases in plasma osmolality (e.g., from hyperglycemia or mannitol) elevate plasma K+ by approximately what amount?',
   'answer':'About 0.6 mEq/L per 10 mOsm/L increase in osmolality; water moves out of cells, dragging K+ with it',
   'rationale':'Osmotic water efflux concentrates intracellular K+ and creates a favourable gradient for K+ exit via channels, causing pseudohyperkalaemia or true elevation.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1877}],'confusable_with':''},
  {'id':'hyperkalemia-d4','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Succinylcholine administration is contraindicated in which patient conditions due to risk of dangerous hyperkalaemia?',
   'answer':'Burns, crush injuries, denervation injuries, prolonged immobility, severe sepsis, and upper/lower motor neuron lesions (extrajunctional ACh receptor upregulation causes K+ efflux)',
   'rationale':'Extrajunctional nicotinic receptors proliferate after denervation/immobility; succinylcholine-induced depolarisation causes massive K+ release from these receptors.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':333}],'confusable_with':''},
  {'id':'hyperkalemia-d5','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Contributing factors for hyperkalaemia requiring anaesthetic consideration include which drug classes?',
   'answer':'ACEi/ARBs, NSAIDs, potassium-sparing diuretics, heparin (reduces aldosterone), and beta-blockers (impair transcellular K+ shift)',
   'rationale':'Multiple drug classes interfere with aldosterone-mediated excretion or transcellular distribution of K+; polypharmacy compounds the risk.',
   'bloom':'recall','source':[{'book':'Stanford CA-1','page':58}],'confusable_with':''},
  {'id':'hyperkalemia-d6','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'In DKA management, as glucose moves intracellularly under insulin therapy, what critical electrolyte must be monitored and repleted?',
   'answer':'Potassium; insulin drives K+ into cells, causing hypokalaemia; K+ must be repleted before or alongside insulin if <3.5 mEq/L',
   'rationale':'DKA patients are total-body K+-depleted despite initial hyperkalaemia from acidosis; insulin therapy rapidly exposes the deficit.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':1219}],'confusable_with':''},
  {'id':'hyperkalemia-d7','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'During cardiac bypass weaning, what level of ionised hyperkalaemia should be corrected before separating from CPB?',
   'answer':'Hyperkalaemia >5.5 mEq/L (along with significant acidosis pH <7.20 and ionised hypocalcaemia) should be corrected before weaning from CPB',
   'rationale':'Electrolyte normalisation is required for adequate cardiac contractility and rhythm stability when weaning from CPB.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':749}],'confusable_with':''},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'CKD/ESRD, ACEi/ARB/NSAID use, hypoaldosteronism, type 4 RTA, massive cell lysis (trauma, TLS), succinylcholine in denervated patients',
  'pathophysiology':'Impaired renal excretion or transcellular shift causes elevated extracellular K+; reduces resting membrane potential, depolarising cardiac cells',
  'time_course':'Can be acute (succinylcholine, TLS) or chronic (CKD, drug-induced)',
  'key_features':'ECG changes (peaked T waves -> wide QRS -> sine wave), muscle weakness, ascending paralysis',
  'consequence_if_missed':'Ventricular fibrillation, cardiac arrest; succinylcholine in at-risk patient can cause death'})

# ── [146] Hypernatremia ───────────────────────────────────────────────────────
T = 'Hypernatremia: Causes and Management'
kps += [
  {'id':'hypernatremia-d1','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'What is the most serious neurological complication of severe hypernatremia?',
   'answer':'Subarachnoid or subdural haemorrhage due to rupture of bridging veins as the brain shrinks away from the skull during acute hypernatremia',
   'rationale':'Rapid dehydration of brain cells causes the brain to shrink, stretching and rupturing bridging veins; this is the primary life-threatening CNS complication.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypernatremia  Causes and Management','page':4}],'confusable_with':'osmotic demyelination syndrome (complication of overly rapid correction of hyponatremia, not hypernatremia)'},
  {'id':'hypernatremia-d2','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Central DI is characterised by decreased ADH production; which pharmacological treatment is used and what adverse effect must be monitored?',
   'answer':'Desmopressin (DDAVP) in intranasal or oral form; adverse effect is water intoxication and hyponatremia with excessive dosing',
   'rationale':'DDAVP selectively activates V2 receptors to increase collecting duct water reabsorption without the vasopressor V1 effects of AVP.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypernatremia  Causes and Management','page':4}],'confusable_with':'nephrogenic DI (does not respond to DDAVP; treat with thiazides + low-sodium diet)'},
  {'id':'hypernatremia-d3','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'In a patient with symptomatic hypernatremia and CNS changes (confusion, seizures), what agent should be used cautiously and why?',
   'answer':'3% hypertonic saline should be used cautiously (to correct concurrent hyponatremia if present); for hypernatremia itself, risk of over-rapid correction is osmotic demyelination if chronic',
   'rationale':'Chronic hypernatremia causes brain adaptation (idiogenic osmoles); over-rapid correction causes cerebral oedema and osmotic injury.',
   'bloom':'analyze','source':[{'book':'Miller/Baby Miller','page':553}],'confusable_with':''},
  {'id':'hypernatremia-d4','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Renal free water loss causing hypernatremia can result from which five broad categories?',
   'answer':'Central DI, nephrogenic DI, post-obstructive diuresis, intrinsic renal disease, osmotic diuretics (glucose, mannitol, loop diuretics)',
   'rationale':'Free water loss from any of these sources raises serum Na+ when oral intake cannot compensate; distinguishing central from nephrogenic DI guides treatment.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypernatremia  Causes and Management','page':2}],'confusable_with':''},
  {'id':'hypernatremia-d5','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'In children with hypernatremia, why can the degree of dehydration be underestimated on clinical examination?',
   'answer':'Shift of water from intracellular to extravascular space partially maintains extracellular volume, masking the degree of total body water deficit',
   'rationale':'Hypertonicity draws intracellular water out, preserving plasma volume at the expense of cellular dehydration; clinical signs of dehydration are less prominent.',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   Hypernatremia  Causes and Management','page':3}],'confusable_with':''},
  {'id':'hypernatremia-d6','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'In SIADH, how does the patient volume status differ from cerebral salt wasting (CSW)?',
   'answer':'SIADH: euvolaemic or mildly hypervolaemic (retained free water); CSW: hypovolaemic (sodium and water loss from kidneys)',
   'rationale':'Distinguishing SIADH from CSW is critical because treatments differ: fluid restriction for SIADH but volume repletion for CSW.',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   SIADH (Syndrome of Inappropriate ADH)','page':4}],'confusable_with':'CSW (cerebral salt wasting; volume status is the key discriminator)'},
  {'id':'hypernatremia-d7','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Hypopituitarism as a cause of secondary DI may be caused by what aetiologies?',
   'answer':'Surgery/trauma, radiation, infection (TB, fungal, meningitis), infiltration (sarcoid, haemochromatosis, Langerhans cell histiocytosis, lymphocytic hypophysitis), genetic, pituitary tumours',
   'rationale':'Identifying a pituitary cause of DI directs imaging (MRI pituitary) and aetiology-specific treatment beyond DDAVP supplementation.',
   'bloom':'recall','source':[{'book':'MGH Housestaff Manual','page':186}],'confusable_with':''},
]

print(f'Batch 4 KPs: {len(kps)}')
with open('data/_part4_batch4.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 4 written OK')
