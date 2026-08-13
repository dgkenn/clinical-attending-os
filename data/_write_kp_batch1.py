import json

kps = []

dom = 'Internal medicine: on-call & cross-cover (approach to the acutely changing ward patient)'
dis = 'medicine'

# ============================================================
# [35] Approach to Hypernatremia
# ============================================================
t = 'Approach to Hypernatremia'
kps += [
  {
    'id': 'approach-to-hypernatremia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A patient on TPN develops Na 158. What fundamental pathophysiologic process defines hypernatremia?',
    'answer': 'Hypernatremia reflects water deficit relative to sodium — either pure water loss or hypotonic fluid loss — always producing intracellular dehydration.',
    'rationale': 'Sodium is the dominant extracellular osmole; its relative excess raises plasma osmolality and draws water out of cells.',
    'bloom': 'recall',
    'source': [{'book': 'Miller/Baby Miller', 'page': 464}],
    'confusable_with': 'Hypervolemic hypernatremia (Na loading) vs hypovolemic (pure water loss)'
  },
  {
    'id': 'approach-to-hypernatremia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'When is 5% dextrose in water (D5W) the preferred replacement fluid for hypernatremia?',
    'answer': 'D5W is preferred when pure water deficit exists without significant volume depletion; it delivers free water after glucose metabolism without adding sodium.',
    'rationale': 'D5W is isotonic on infusion but glucose is rapidly metabolized, leaving only free water to dilute plasma sodium.',
    'bloom': 'apply',
    'source': [{'book': 'Miller/Baby Miller', 'page': 464}],
    'confusable_with': 'Normal saline — corrects volume but raises sodium further'
  },
  {
    'id': 'approach-to-hypernatremia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Why can measured plasma sodium be spuriously low in severe hyperlipidemia?',
    'answer': 'In hyperlipidemia or hyperproteinemia, the non-aqueous plasma fraction increases; flame photometry measures Na per unit plasma volume, so the actual aqueous-phase Na is underestimated (pseudohyponatremia, not true hypernatremia).',
    'rationale': 'When lipids or proteins expand to 30% of plasma volume, the aqueous Na concentration is considerably higher than the flame-photometry result.',
    'bloom': 'analyze',
    'source': [{'book': 'Marino ICU Book', 'page': 438}],
    'confusable_with': 'True hypernatremia — use direct ion-selective electrode to distinguish'
  },
  {
    'id': 'approach-to-hypernatremia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What is the maximum safe correction rate for chronic hypernatremia, and why?',
    'answer': 'Correct no faster than ~0.5 mEq/L/h (or ~10-12 mEq/L per day) to avoid cerebral edema from rapid water re-entry into brain cells that have accumulated osmolytes.',
    'rationale': 'Brain cells adapt to chronic hyperosmolarity by accumulating idiogenic osmoles; rapid correction creates a hypotonic gradient driving water into cells.',
    'bloom': 'apply',
    'source': [{'book': 'Marino ICU Book', 'page': 438}],
    'confusable_with': 'Acute hyponatremia correction — different limits apply'
  },
]

# ============================================================
# [36] Approach to Hyperthermia
# ============================================================
t = 'Approach to Hyperthermia'
kps += [
  {
    'id': 'approach-to-hyperthermia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A patient develops fever and rigidity intraoperatively after succinylcholine and a volatile agent. What structured first step does the evaluation prioritize?',
    'answer': 'Immediately evaluate for life-threatening causes: malignant hyperthermia (MH), sepsis, and pulmonary embolism must be excluded before considering benign etiologies.',
    'rationale': 'Postoperative fever with early onset and muscle rigidity after volatile agents/succinylcholine is MH until proven otherwise; delay is fatal.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 9}],
    'confusable_with': 'Serotonin syndrome, NMS — differ in trigger and time course'
  },
  {
    'id': 'approach-to-hyperthermia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Does a history of uneventful prior general anesthetics rule out malignant hyperthermia susceptibility?',
    'answer': 'No. Uneventful prior anesthetics do NOT rule out MH susceptibility.',
    'rationale': 'MH susceptibility is genetic (RYR1/CACNA1S); phenotypic expression depends on agent concentration, duration, and co-triggers — prior exposures may have been sub-threshold.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 351}],
    'confusable_with': 'Assuming prior tolerance equals no genetic risk'
  },
  {
    'id': 'approach-to-hyperthermia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What confirmatory test for MH has a near-zero false-negative rate but is limited to very few centers worldwide?',
    'answer': 'The halothane-caffeine contracture test (CHCT) on fresh skeletal muscle biopsy; false-negative rate is close to zero though false-positive rate is 10-20%; genetic testing is now more commonly used.',
    'rationale': 'Living muscle exposed to halothane or caffeine contracts abnormally in susceptible individuals due to uncontrolled SR calcium release via mutant RYR1.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1992}],
    'confusable_with': 'Genetic testing alone — misses novel RYR1 variants not yet catalogued'
  },
  {
    'id': 'approach-to-hyperthermia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'In children, which succinylcholine-associated complications overlap with hyperthermia emergencies and require immediate hyperkalemia treatment?',
    'answer': 'Children are more susceptible to cardiac arrhythmias, hyperkalemia, rhabdomyolysis, myoglobinemia, masseter spasm, and MH from succinylcholine; cardiac arrest in a child post-succinylcholine should trigger immediate hyperkalemia treatment.',
    'rationale': 'Pediatric muscle has higher metabolic demand and succinylcholine can trigger uncontrolled K+ efflux; hyperkalemia-induced VF can follow.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1458}],
    'confusable_with': 'Adult succinylcholine side effects — less severe'
  },
]

# ============================================================
# [37] Approach to Hypokalemia
# ============================================================
t = 'Approach to Hypokalemia'
kps += [
  {
    'id': 'approach-to-hypokalemia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A patient on loop diuretics has K 3.0 and pH 7.50. Why does metabolic alkalosis worsen hypokalemia?',
    'answer': 'Metabolic alkalosis causes transcellular K+ shift into cells in exchange for H+, and loop diuretics promote urinary K+ wasting; both lower serum K.',
    'rationale': 'H+/K+ antiporters shift K+ intracellularly to buffer alkalosis; loop diuretic-driven Na delivery to the collecting duct also increases K+ secretion.',
    'bloom': 'analyze',
    'source': [{'book': 'Miller/Baby Miller', 'page': 431}],
    'confusable_with': 'Metabolic acidosis — causes hyperkalemia via reverse transcellular shift'
  },
  {
    'id': 'approach-to-hypokalemia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Which urinary diversion procedure carries ~80% incidence of hyperchloremic metabolic acidosis frequently accompanied by hypokalemia?',
    'answer': 'Ureterosigmoidostomy — colonic mucosa absorbs Cl- and secretes K+ and HCO3-, causing hyperchloremic acidosis and potassium depletion.',
    'rationale': 'Sigmoid colon has active Cl-/HCO3- exchange; prolonged urine contact produces net bicarbonate loss and chloride gain.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1903}],
    'confusable_with': 'Ileal conduit — much lower incidence of hyperchloremic acidosis'
  },
  {
    'id': 'approach-to-hypokalemia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Why does refractory hypokalemia persist despite potassium replacement in a patient with concurrent hypomagnesemia?',
    'answer': 'Hypomagnesemia impairs Na-K-ATPase and promotes renal K+ wasting; magnesium must be repleted for K+ correction to succeed.',
    'rationale': 'Mg2+ is a cofactor for Na-K-ATPase; its deficiency allows continued urinary K+ loss regardless of K+ supplementation.',
    'bloom': 'analyze',
    'source': [{'book': 'Marino ICU Book', 'page': 773}],
    'confusable_with': 'Isolated hypokalemia — check Mg in all refractory cases'
  },
  {
    'id': 'approach-to-hypokalemia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'An interprofessional team manages a patient with hypokalemia from kidney disease. Which specialist is most relevant for underlying cause evaluation?',
    'answer': 'A nephrologist evaluates and manages underlying kidney disease causing potassium wasting; endocrinology rules out underlying endocrine disorders (e.g., hyperaldosteronism).',
    'rationale': 'Potassium homeostasis is primarily renal; distinguishing renal from extrarenal losses guides definitive treatment.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 9}],
    'confusable_with': 'Extrarenal K loss (GI) — urine K:Cr ratio differentiates renal from GI loss'
  },
]

# ============================================================
# [38] Approach to Hypomagnesemia and Hypophosphatemia
# ============================================================
t = 'Approach to Hypomagnesemia and Hypophosphatemia'
kps += [
  {
    'id': 'approach-to-hypomagnesemia-hypophosphatemia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Why is oral phosphate replacement generally preferred over IV phosphate in hypophosphatemia?',
    'answer': 'IV phosphate risks precipitation with calcium causing acute hypocalcemia, hyperphosphatemia, and hypomagnesemia; oral route allows controlled intestinal absorption.',
    'rationale': 'Calcium phosphate product threshold is easily exceeded with rapid IV infusion; gut absorbs phosphate at a physiologically regulated rate.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1895}],
    'confusable_with': 'Severe symptomatic hypophosphatemia (<1 mg/dL) — may require cautious IV repletion'
  },
  {
    'id': 'approach-to-hypomagnesemia-hypophosphatemia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What intraoperative conditions should be avoided to prevent worsening hypophosphatemia?',
    'answer': 'Hyperglycemia and respiratory alkalosis should both be avoided — each drives transcellular phosphate shift into cells, lowering serum phosphate.',
    'rationale': 'Insulin from hyperglycemia activates glycolysis requiring phosphate; alkalosis also increases intracellular phosphate uptake via cellular pH shifts.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1896}],
    'confusable_with': 'Refeeding syndrome — also causes hypophosphatemia via insulin surge post-refeeding'
  },
  {
    'id': 'approach-to-hypomagnesemia-hypophosphatemia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A patient with severe hypophosphatemia needs neuromuscular blocking agents. What specific monitoring is required?',
    'answer': 'Neuromuscular function must be carefully monitored; severe hypophosphatemia causes muscle weakness and some patients may require postoperative mechanical ventilation.',
    'rationale': 'Phosphate is required for ATP generation; ATP depletion impairs myofibrillar cross-bridge cycling, magnifying NMB effects.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1896}],
    'confusable_with': 'Hypokalemia-related weakness — same practical warning but different ionic mechanism'
  },
  {
    'id': 'approach-to-hypomagnesemia-hypophosphatemia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Why should isolated hypomagnesemia be corrected before elective surgery?',
    'answer': 'Hypomagnesemia can cause arrhythmias; magnesium also has intrinsic antiarrhythmic and possible cerebral protective effects — correct before elective procedures.',
    'rationale': 'Mg2+ stabilizes myocardial cell membranes by antagonizing calcium at voltage-gated channels; deficiency lowers the dysrhythmia threshold.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1900}],
    'confusable_with': 'Hypokalemia — also arrhythmogenic; often coexists with hypomagnesemia'
  },
  {
    'id': 'approach-to-hypomagnesemia-hypophosphatemia-5',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'Hypercalcemia is being treated. What electrolyte abnormalities commonly accompany it and require concurrent repletion?',
    'answer': 'Hypercalcemia often co-presents with hypokalemia, hypomagnesemia, and hypophosphatemia — all should be repleted to normal levels concurrently.',
    'rationale': 'Hypercalcemia-induced polyuria causes renal wasting of K+, Mg2+, and phosphate; calcitonin and bisphosphonate treatment does not correct these losses.',
    'bloom': 'apply',
    'source': [{'book': 'StatPearls', 'page': 6}],
    'confusable_with': 'Hypocalcemia electrolyte shifts — different co-disturbances'
  },
]

print('Batch 1 KPs:', len(kps))
with open('data/_kp_part2_batch1.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
