import json

kps = []
dom = 'Internal medicine: on-call & cross-cover (approach to the acutely changing ward patient)'
dis = 'medicine'

# ============================================================
# [39] Approach to Hyponatremia
# ============================================================
t = 'Approach to Hyponatremia'
kps += [
  {
    'id': 'approach-to-hyponatremia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What does hyponatremia invariably reflect at the physiologic level?',
    'answer': 'Hyponatremia invariably reflects water retention — either an absolute increase in total body water (TBW) or sodium loss in relative excess to water loss.',
    'rationale': 'The kidneys can excrete >10 L free water/day; hyponatremia develops only when ADH is active or free water excretion is overwhelmed.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1864}],
    'confusable_with': 'Hypernatremia — water deficit; hyponatremia — water excess'
  },
  {
    'id': 'approach-to-hyponatremia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A patient has hyponatremia without edema and without signs of hypovolemia. What four causes should be considered?',
    'answer': 'Euvolemic hyponatremia: glucocorticoid insufficiency, hypothyroidism, drug therapy (SSRIs, NSAIDs, etc.), and SIADH.',
    'rationale': 'These conditions impair free-water excretion via ADH-mediated pathways without altering total body sodium significantly.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1865}],
    'confusable_with': 'Hypovolemic hyponatremia — distinguishable by volume status assessment'
  },
  {
    'id': 'approach-to-hyponatremia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'In hypovolemic hyponatremia, at what intravascular deficit does nonosmotic ADH secretion override osmolality-driven suppression?',
    'answer': 'When intravascular volume deficit approaches 5-10%, nonosmotic ADH release is triggered; with further volume depletion, volume preservation takes precedence over plasma osmolality.',
    'rationale': 'Baroreceptor signals override osmoreceptor signals at >5-10% volume deficit, maintaining perfusion at the expense of osmolality.',
    'bloom': 'analyze',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1865}],
    'confusable_with': 'SIADH — euvolemic; does not require volume deficit to activate ADH'
  },
  {
    'id': 'approach-to-hyponatremia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'How does Cerebral Salt Wasting (CSW) differ from SIADH in volume status and management?',
    'answer': 'CSW: hypovolemic with polyuria and renal Na wasting (replace Na and volume). SIADH: euvolemic or mildly hypervolemic (restrict free water). Volume status is the key distinguishing feature.',
    'rationale': 'CSW results from natriuretic peptide release from injured brain causing renal Na loss; SIADH causes water retention without natriuresis.',
    'bloom': 'analyze',
    'source': [{'book': 'StatPearls', 'page': 4}],
    'confusable_with': 'SIADH — both occur after CNS injury; CSW requires volume repletion, SIADH fluid restriction'
  },
  {
    'id': 'approach-to-hyponatremia-5',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A neurosurgical patient develops hyponatremia with polyuria and hypovolemia after SAH. What syndrome is suspected?',
    'answer': 'Cerebral Salt Wasting (CSW) — a syndrome of renal sodium wasting with polyuria and hypovolemia seen after CNS injury, particularly subarachnoid hemorrhage.',
    'rationale': 'CNS injury triggers release of natriuretic peptides that impair tubular Na reabsorption, causing Na and volume depletion.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1867}],
    'confusable_with': 'SIADH — may co-occur; volume assessment (hypo vs euvolemic) is critical'
  },
]

kps.append({
    '_type': 'confusable_pair',
    'topic_a': 'SIADH',
    'topic_b': 'Cerebral Salt Wasting',
    'discriminator': 'Volume status: SIADH is euvolemic/hypervolemic; CSW is hypovolemic with polyuria and urinary Na wasting — SIADH treated with fluid restriction, CSW with Na+volume repletion'
})

# ============================================================
# [40] Approach to Hypothermia
# ============================================================
t = 'Approach to Hypothermia'
kps += [
  {
    'id': 'approach-to-hypothermia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What is the primary cause of postoperative shivering, and why is it clinically dangerous?',
    'answer': 'Primary cause is perioperative hypothermia. Shivering greatly increases oxygen consumption, catecholamine release, cardiac output, heart rate, blood pressure, and intracranial/intraocular pressure — increasing cardiovascular morbidity in older patients.',
    'rationale': 'Thermogenesis via shivering is metabolically expensive; the resulting O2 demand surge can precipitate myocardial ischemia in patients with limited cardiac reserve.',
    'bloom': 'recall',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1830}],
    'confusable_with': 'Emergence delirium — also a cause of agitation but without the thermoregulatory mechanism'
  },
  {
    'id': 'approach-to-hypothermia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What is the difference between alpha-stat and pH-stat management during hypothermic CPB, and when is pH-stat advantageous?',
    'answer': 'Alpha-stat: maintain constant CO2 tension (40 mmHg) and pH (7.40) uncorrected for temperature. pH-stat: add CO2 to maintain these values temperature-corrected, increasing cerebral blood flow. pH-stat increases cerebral perfusion and may be useful for cerebral protection.',
    'rationale': 'Under pH-stat, CO2 is added to the oxygenator to maintain pCO2 at 40 mmHg at patient temperature — CO2-driven vasodilation augments cerebral blood flow beyond metabolic needs.',
    'bloom': 'analyze',
    'source': [{'book': 'Morgan & Mikhail', 'page': 746}],
    'confusable_with': 'Alpha-stat — preferred for adult cardiac surgery; pH-stat may be preferred for pediatric deep hypothermic circulatory arrest'
  },
  {
    'id': 'approach-to-hypothermia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'A hypothyroid patient receives general anesthesia. What specific hypothermia-related complications are anticipated in the postoperative period?',
    'answer': 'Recovery from anesthesia may be delayed by hypothermia (from low basal metabolic rate), respiratory depression, and slowed drug metabolism; hypothermia from reduced BMR is a specific risk.',
    'rationale': 'Thyroid hormone is a primary thermogenic hormone; its deficiency lowers BMR, reduces heat production, and impairs the metabolic clearance of anesthetic agents.',
    'bloom': 'apply',
    'source': [{'book': 'Morgan & Mikhail', 'page': 1229}],
    'confusable_with': 'Drug-related delayed awakening — hypothyroidism adds metabolic and thermoregulatory contributions'
  },
  {
    'id': 'approach-to-hypothermia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What does alpha-stat management preserve, and what is the physiologic basis for this approach?',
    'answer': 'Alpha-stat preserves constant intracellular electrochemical neutrality (the balance of charges on proteins) by maintaining constant CO2 tension and pH, allowing normal enzyme function during hypothermia.',
    'rationale': 'Protein charge state (alpha) governs enzyme kinetics; at lower temperatures, neutral pH rises, but alpha-stat maintains the protein charge ratio constant for optimal function.',
    'bloom': 'analyze',
    'source': [{'book': 'Morgan & Mikhail', 'page': 746}],
    'confusable_with': 'pH-stat — maintains pH constant for temperature, not protein charge state'
  },
]

# ============================================================
# [41] Approach to Insomnia and Sleep Requests
# ============================================================
t = 'Approach to Insomnia and Sleep Requests'
kps += [
  {
    'id': 'approach-to-insomnia-1',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'An on-call nurse asks for a sedative for a patient with new insomnia. What medical causes must be excluded before treating symptomatically?',
    'answer': 'Exclude medical conditions (pain, COPD, CHF, GERD, nocturia), psychiatric causes (PTSD, mood disorder), substances/medications (stimulants, steroids, beta-blockers, SSRIs, opioids), and primary sleep disorders (insufficient sleep syndrome, circadian rhythm disorder, OSA, RLS) before prescribing sedatives.',
    'rationale': 'Treating insomnia symptomatically without finding the cause can mask serious conditions or worsen them (e.g., sedatives in undiagnosed OSA).',
    'bloom': 'apply',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 225}],
    'confusable_with': 'Benzodiazepine-appropriate insomnia — requires prior workup'
  },
  {
    'id': 'approach-to-insomnia-2',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'In patients with Parkinson disease, what specific dopaminergic issue causes insomnia?',
    'answer': 'Inadequate dopamine agonism in Parkinson disease can lead to insomnia; motor symptoms (tremor, rigidity) often worsen at night due to wearing off of dopaminergic medications.',
    'rationale': 'Dopaminergic pathways regulate sleep-wake cycles; in Parkinson disease, nocturnal motor symptoms from dopamine deficiency fragment sleep.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 13}],
    'confusable_with': 'REM sleep behavior disorder in Parkinson — different mechanism (REM without atonia)'
  },
  {
    'id': 'approach-to-insomnia-3',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'What defines chronic insomnia, and what are its two key functional components?',
    'answer': 'Chronic insomnia: difficulty initiating or maintaining sleep for >3 months with compromised daytime functioning. The two components are the sleep disturbance itself and impaired daytime function.',
    'rationale': 'Both nocturnal sleep disruption and daytime consequences are required for diagnosis; sleep complaints without daytime impairment do not qualify as insomnia disorder.',
    'bloom': 'recall',
    'source': [{'book': 'MGH Housestaff Manual', 'page': 225}],
    'confusable_with': 'Short sleep duration — no daytime impairment; insomnia requires functional impact'
  },
  {
    'id': 'approach-to-insomnia-4',
    'topic': t, 'domain': dom, 'discipline': dis,
    'stem': 'In patients with neurodegenerative disease and sleep disorders, what is the impact of promptly recognizing and managing sleep disturbances?',
    'answer': 'Prompt recognition and management of sleep disorders can significantly improve outcomes and in some cases delay progression of the neurodegenerative condition.',
    'rationale': 'Sleep is required for glymphatic clearance of neurotoxic proteins (e.g., amyloid); sleep disruption may accelerate neurodegeneration.',
    'bloom': 'recall',
    'source': [{'book': 'StatPearls', 'page': 13}],
    'confusable_with': 'Insomnia in non-neurodegeneration — still important but less likely to alter disease course'
  },
]

print('Batch 2 KPs:', len(kps))
with open('data/_kp_part2_batch2.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print('Written.')
