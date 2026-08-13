
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_redeepen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = []
DOM_ENDO = ('Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & '
            'storm, adrenal insufficiency, calcium disorders, pituitary)')
DOM_NEPH = 'Internal medicine: nephrology, fluids & electrolytes'
DIS = 'medicine'

# ── [150] Hyperthyroidism ─────────────────────────────────────────────────────
T = 'Hyperthyroidism'
kps += [
  {'id':'hyperthyroidism-d1','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'What should be done before elective surgery in a known hyperthyroid patient, and why?',
   'answer':'All elective surgical procedures should be postponed until the patient is rendered clinically euthyroid; proceeding risks thyroid storm perioperatively',
   'rationale':'Anaesthesia and surgery are potent triggers for thyroid storm in uncontrolled hyperthyroidism; achieving euthyroid state reduces catecholamine excess and arrhythmia risk.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':1226}],'confusable_with':'hypothyroidism (mild cases may proceed; severe myxedema warrants postponement for different reasons)'},
  {'id':'hyperthyroidism-d2','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Thyroid storm occurs perioperatively: how does it differ from malignant hyperthermia in timing and EtCO2?',
   'answer':'Thyroid storm onset: 6-24h post-surgery (occasionally intraoperative); unlike MH it is not associated with masseter rigidity or elevated EtCO2; MH has rapid onset and elevated EtCO2',
   'rationale':'Distinguishing thyroid storm from MH is critical because treatments differ; MH requires dantrolene, thyroid storm requires beta-blockade, antithyroid drugs, and steroids.',
   'bloom':'analyze','source':[{'book':'Morgan & Mikhail','page':1227}],'confusable_with':'malignant hyperthermia (rapid onset, elevated EtCO2, masseter rigidity, responds to dantrolene)'},
  {'id':'hyperthyroidism-d3','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Graves disease is usually treated with which two modalities, and when is surgery indicated?',
   'answer':'Antithyroid drugs (methimazole/PTU) or radioactive iodine; surgery (subtotal thyroidectomy) is reserved for large toxic multinodular goitres or solitary toxic adenomas',
   'rationale':'Surgery and RAI are curative; antithyroid drugs are bridging therapy; goitre size and patient preference guide modality selection.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1226}],'confusable_with':''},
  {'id':'hyperthyroidism-d4','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Although the thyroid gland releases more T4 than T3, which is the more potent thyroid hormone and why?',
   'answer':'T3 is more potent; most circulating T4 is converted to T3 in peripheral tissues; T3 has higher affinity for thyroid hormone receptors',
   'rationale':'Understanding T4->T3 peripheral conversion explains why amiodarone and propylthiouracil inhibit conversion to reduce T3 effect in thyrotoxicosis.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1225}],'confusable_with':''},
  {'id':'hyperthyroidism-d5','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'In inpatient thyroid testing, when should TSH alone be ordered vs when is FT4 + T3 also required?',
   'answer':'If thyroidal illness is suspected, TSH alone is inadequate; should also obtain FT4 and T3. TSH reflects changes within 4-6 weeks; routine screening on admission is not indicated',
   'rationale':'TSH has a delayed response to thyroid hormone changes (4-6 weeks); acute illness can suppress TSH (sick euthyroid) creating false hyperthyroid picture.',
   'bloom':'apply','source':[{'book':'MGH Housestaff Manual','page':189}],'confusable_with':'euthyroid sick syndrome (TSH low from illness, not true hyperthyroidism)'},
  {'id':'hyperthyroidism-d6','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Hyperthyroidism associated with thyroid storm is associated with which specific ECG or rhythm findings?',
   'answer':'Tachycardia, atrial fibrillation, and potential ventricular arrhythmias; thyroid storm is NOT associated with masseter rigidity (unlike MH) but presents with hyperthermia, tachycardia, altered mental status',
   'rationale':'Thyroid hormone excess directly sensitises the heart to catecholamines and increases beta-receptor density, driving tachyarrhythmias.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1227}],'confusable_with':''},
  {'id':'hyperthyroidism-d7','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Myasthenia gravis can be confused with thyroid disease; what is the mechanism of weakness in MG?',
   'answer':'Autoimmune destruction or inactivation of postsynaptic ACh receptors at NMJ by IgG antibodies, leading to complement-mediated NMJ damage and reduced receptor numbers',
   'rationale':'Thyroid disease can co-occur with MG (both autoimmune); distinguishing causes of weakness (fatigable neuromuscular vs metabolic) is clinically important.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1028}],'confusable_with':'thyroid myopathy (metabolic weakness without fatiguable NMJ transmission)'},
]
kps.append({'_type':'illness_script','topic':T,'discipline':DIS,
  'enabling_conditions':'Graves disease (most common), toxic multinodular goitre, toxic adenoma, excess iodine/amiodarone, subacute thyroiditis',
  'pathophysiology':'Excess T3/T4 increases basal metabolic rate, sensitises heart to catecholamines, accelerates bone turnover and gut motility',
  'time_course':'Insidious onset; thyroid storm precipitated acutely by surgery, infection, or iodine load',
  'key_features':'Weight loss with increased appetite, heat intolerance, tremor, palpitations, AF, exophthalmos (Graves), lid lag',
  'consequence_if_missed':'Thyroid storm (mortality 10-25%), AF with stroke, osteoporosis, perioperative cardiovascular crisis'})

# ── [151] Hypocalcemia (endocrine domain) ─────────────────────────────────────
T = 'Hypocalcemia'
kps += [
  {'id':'hypocalcemia-endo-d1','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Hypocalcemia in kidney failure results from what two primary mechanisms?',
   'answer':'Hyperphosphataemia (binds calcium) and impaired renal 1-alpha-hydroxylation of 25-OHD to active 1,25(OH)2D, reducing GI calcium absorption',
   'rationale':'Both mechanisms are directly driven by loss of nephron mass; secondary hyperparathyroidism develops as compensation but cannot restore normocalcaemia without vitamin D activation.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1110}],'confusable_with':''},
  {'id':'hypocalcemia-endo-d2','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'In weaning from cardiopulmonary bypass, what ionised calcium threshold should trigger treatment?',
   'answer':'Ionised hypocalcaemia should be corrected before weaning CPB; along with pH <7.20 and K+ >5.5 mEq/L as co-criteria for treatment',
   'rationale':'Ionised calcium is required for myocardial contraction; hypocalcaemia reduces cardiac contractility, making CPB weaning hazardous.',
   'bloom':'apply','source':[{'book':'Morgan & Mikhail','page':749}],'confusable_with':''},
  {'id':'hypocalcemia-endo-d3','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Citrate toxicity from massive blood transfusion causes what electrolyte abnormality, and at what transfusion rate does it become clinically significant?',
   'answer':'Hypocalcaemia from calcium binding by citrate preservative; clinically important cardiac depression at transfusion rates >1 unit per 5 minutes in normal patients',
   'rationale':'The liver rapidly metabolises citrate; only at very high transfusion rates (or with liver dysfunction) does calcium binding become haemodynamically significant.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1968}],'confusable_with':''},
  {'id':'hypocalcemia-endo-d4','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Hypocalcaemia following rhabdomyolysis results from what mechanism?',
   'answer':'Precipitation of calcium in necrotic muscle tissue (calcium-phosphate deposition); serum calcium falls as calcium moves into injured tissue',
   'rationale':'Paradoxically, the hypocalcaemia phase of rhabdomyolysis is followed by hypercalcaemia during recovery as calcium is mobilised from deposits.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1892}],'confusable_with':''},
  {'id':'hypocalcemia-endo-d5','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Magnesium deficiency causes hypocalcaemia through what two mechanisms?',
   'answer':'Impairs PTH secretion (Mg required for PTH release) AND antagonises PTH action on bone; both mechanisms reduce calcium mobilisation',
   'rationale':'Hypocalcaemia refractory to calcium supplementation should prompt magnesium repletion first, as Mg deficiency must be corrected before PTH can normalise calcium.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1892}],'confusable_with':''},
  {'id':'hypocalcemia-endo-d6','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'How does alkalosis affect ionised calcium, and what is the clinical implication for anxious hyperventilating patients?',
   'answer':'Alkalosis increases Ca2+-albumin binding, reducing ionised calcium; hyperventilation-induced respiratory alkalosis causes perioral tingling, tetany (Chvostek/Trousseau signs)',
   'rationale':'Ionised (not total) calcium determines neuromuscular excitability; alkalosis reduces ionised Ca2+ even with normal total calcium.',
   'bloom':'analyze','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':6}],'confusable_with':'true hypocalcaemia (low total and ionised calcium)'},
  {'id':'hypocalcemia-endo-d7','topic':T,'domain':DOM_ENDO,'discipline':DIS,
   'stem':'Sepsis-associated hypocalcaemia results from which mechanism?',
   'answer':'Suppressed PTH release during sepsis, often accompanied by hypomagnesaemia, causing reduced calcium mobilisation from bone',
   'rationale':'PTH suppression in critical illness (non-thyroidal illness pattern) reduces calcium homeostatic response; magnesium deficiency compounds the defect.',
   'bloom':'recall','source':[{'book':'Morgan & Mikhail','page':1892}],'confusable_with':''},
]

# ── [152] Hypocalcemia nephrology ─────────────────────────────────────────────
T = 'Hypocalcemia: Causes and Management'
kps += [
  {'id':'hypocalcemia-neph-d1','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Before correcting hypocalcaemia, which electrolyte must be normalised first and why?',
   'answer':'Serum magnesium must be corrected before correcting hypocalcaemia; hypomagnesaemia impairs PTH secretion and action, making calcium correction ineffective',
   'rationale':'Magnesium is a cofactor for PTH release; without correcting Mg first, calcium supplementation will be poorly effective and transient.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':8}],'confusable_with':''},
  {'id':'hypocalcemia-neph-d2','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'CKD-related hypocalcaemia is typically corrected with which specific form of vitamin D, and why not standard vitamin D3?',
   'answer':'Activated vitamin D (calcitriol, 1,25(OH)2D3); CKD impairs renal 1-alpha-hydroxylation so standard D3 cannot be converted to the active form',
   'rationale':'The final activation step occurs in the kidney; with CKD, only the already-activated calcitriol bypasses the impaired conversion step.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':8}],'confusable_with':'ergocalciferol/cholecalciferol (require intact renal hydroxylation)'},
  {'id':'hypocalcemia-neph-d3','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Cinacalcet is a calcimimetic used for hyperparathyroidism; what is its mechanism of action?',
   'answer':'Stimulates the calcium-sensing receptor (CaSR) on parathyroid cells, decreasing PTH secretion; used for primary and secondary hyperparathyroidism',
   'rationale':'CaSR activation signals the parathyroid gland that calcium is sufficient, suppressing PTH without requiring elevated serum calcium.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':5}],'confusable_with':'vitamin D (increases calcium absorption; different mechanism)'},
  {'id':'hypocalcemia-neph-d4','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Vitamin D deficiency cannot be corrected by calcium supplementation alone; what must be repleted first?',
   'answer':'Vitamin D must be repleted first; without adequate 1,25(OH)2D, intestinal calcium absorption remains impaired regardless of calcium supplementation',
   'rationale':'1,25(OH)2D is the primary driver of intestinal calcium absorption (via TRPV6 channels); without it, supplemental calcium is poorly absorbed.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':8}],'confusable_with':''},
  {'id':'hypocalcemia-neph-d5','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Pseudohypoparathyroidism (PHP) causes hypocalcaemia despite elevated PTH; what is the molecular basis?',
   'answer':'End-organ resistance to PTH due to Gs-alpha protein mutation; PTH receptor signalling is impaired, causing phosphate retention and failure of calcium mobilisation',
   'rationale':'PHP patients have the Albright hereditary osteodystrophy phenotype; treatment targets serum calcium with calcitriol rather than trying to lower PTH.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':4}],'confusable_with':'hypoparathyroidism (low PTH vs elevated PTH in PHP)'},
  {'id':'hypocalcemia-neph-d6','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'The main hormones regulating calcium homeostasis are PTH, 1,25(OH)2D, FGF23, calcitonin, and the CaSR; what is calcitonin\'s role?',
   'answer':'Calcitonin inhibits osteoclast activity and promotes renal calcium excretion; released from thyroid C-cells in response to hypercalcaemia',
   'rationale':'Calcitonin is the acute counter-regulatory hormone to hypercalcaemia; its effect is modest compared to PTH, but pharmacological doses (salmon calcitonin) are used in hypercalcaemic crisis.',
   'bloom':'recall','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':2}],'confusable_with':'PTH (raises calcium); calcitonin lowers calcium'},
  {'id':'hypocalcemia-neph-d7','topic':T,'domain':DOM_NEPH,'discipline':DIS,
   'stem':'Denosumab and bisphosphonates used for osteoporosis/bone metastases cause hypocalcaemia when which co-deficiency is present?',
   'answer':'Concomitant vitamin D deficiency worsens hypocalcaemia with these drugs; vitamin D and calcium levels should be corrected before initiating treatment',
   'rationale':'Antiresorptive agents reduce calcium mobilisation from bone; without adequate vitamin D for GI absorption, the resulting calcium deficit causes symptomatic hypocalcaemia.',
   'bloom':'apply','source':[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':5}],'confusable_with':''},
]
kps.append({'_type':'confusable_pair',
  'topic_a':'Hypocalcemia from hypoparathyroidism','topic_b':'Hypocalcemia from pseudohypoparathyroidism',
  'discriminator':'Hypoparathyroidism: LOW PTH, low calcium, high phosphate (PTH absent -> phosphate retention). PHP: HIGH PTH with same labs (PTH resistance). Treatment with calcitriol in both; serum PTH level distinguishes them'})

print(f'Batch 6 KPs: {len(kps)}')
with open('data/_part4_batch6.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Batch 6 written OK')
