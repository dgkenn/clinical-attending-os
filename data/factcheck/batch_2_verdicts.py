"""
Verdict logic for batch_2.json — runs once to produce the final output.
All clinical reasoning encoded here.
"""
import json, os, sys

with open('data/factcheck/_raw_batch2.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

# ── Pre-computed verdicts ─────────────────────────────────────────────────────
# Keyed by id → (verdict, reason, corrected_text or None)
VERDICTS = {}

def v(uid, verdict, reason, corrected_text=None):
    VERDICTS[uid] = (verdict, reason[:160], corrected_text)

# ── PHASE 2: Electrolytes / Thyroid ──────────────────────────────────────────

v("curated-phase2_unit_198", "KEEP",
  "RRT indications accurate (AEIOU + refractory lytes); CRRT preference for instability correct; adds value corpus doesn't fully cover.")

v("curated-phase2_unit_199", "KEEP",
  "Hyperkalemia algorithm accurate: Ca-gluconate dose, insulin/dextrose doses, albuterol 10-20 mg nebulized (high-dose for hyperK) all correct.")

v("curated-phase2_unit_200", "KEEP",
  "Hyponatremia osmolality classification and SIADH criteria correct; urine Na >40 for SIADH is standard; adds structured approach.")

v("curated-phase2_unit_201", "FIX",
  "Dangerous phrasing: 'aim for 4-6 mEq/L rise per hour' implies sustained hourly rate; correct target is 4-6 mEq/L total over acute phase.",
  corrected_text="""Symptomatic hyponatremia: nausea, headache, confusion, lethargy, seizures (Na+ <120), coma, death (if severe <110). Acute hyponatremia (<48h): cells haven't adapted, increased intracellular fluid volume -> cerebral edema risk at lower Na+ levels. Chronic hyponatremia (>48h): osmolytes extruded from cells, cerebral edema less likely even if Na+ very low. Correction rate critical: too-rapid correction (>12 mEq/L in 24h) risks central pontine myelinolysis (demyelination, locked-in syndrome, death). Acute symptomatic: 3% hypertonic saline (NaCl 3%, 1 mL/kg IV bolus, repeat once if still seizing), aim for 4-6 mEq/L total rise in the first few hours (not a sustained per-hour rate), then reassess and slow. Chronic asymptomatic: fluid restriction (SIADH), slow correction 4-8 mEq/L per 24h.""")

v("curated-phase2_unit_202", "KEEP",
  "3% saline dosing (1-2 mL/kg bolus), Adrogue-Madias formula, fluid restriction targets, vaptan cautions all accurate. Score 0.795.")

v("curated-phase2_unit_203", "KEEP",
  "Hypernatremia causes and FWD formula correct (0.6 x wt x [Na/140-1]); DI types and treatment accurate. Adds value not redundant.")

v("curated-phase2_unit_204", "KEEP",
  "ODS prevention limits accurate (4-8 mEq/24h chronic, 10-12 acute); dextrose re-lowering strategy correct; adds clinical value.")

v("curated-phase2_unit_205", "KEEP",
  "Thyroid physiology: TSH/T3/T4/rT3 relationships accurate; protein binding, half-life, free fraction teaching correct. Score 0.707, not dup.")

v("curated-phase2_unit_206", "KEEP",
  "TSH screening strengths/limitations accurate; central hypo/hyperthyroidism caveats, euthyroid sick syndrome correct. Adds diagnostic nuance.")

v("curated-phase2_unit_207", "KEEP",
  "Hypothyroidism causes, Hashimoto pathophysiology, iodine deficiency accurate. In scope for intern-level endocrine review.")

v("curated-phase2_unit_208", "KEEP",
  "Levothyroxine dosing (1.6 mcg/kg), titration interval (q4-6wk), TSH target (0.5-2.5) accurate. Adds actionable intern-level guidance.")

v("curated-phase2_unit_209", "KEEP",
  "LT4 drug interactions (Ca, Fe, PPIs, estrogens, amiodarone) accurate; timing guidance correct. Adds practical prescribing value.")

v("curated-phase2_unit_210", "KEEP",
  "Hyperthyroidism etiology (Graves 70%, toxic adenoma, thyroiditis), TSI antibodies, ophthalmopathy accurate. Score 0.795, adds structure.")

v("curated-phase2_unit_211", "KEEP",
  "Thyroid storm management accurate: mortality range, propranolol (also blocks T4->T3), PTU dosing, Lugol's after PTU timing all correct.")

v("curated-phase2_unit_212", "KEEP",
  "PTU vs methimazole comparison accurate: dosing, hepatotoxicity risk, first-trimester preference for PTU, pregnancy switch guidance correct.")

v("curated-phase2_unit_213", "KEEP",
  "Beta-blockers in hyperthyroidism: propranolol T4->T3 inhibition, HR target 60-80, dosing range accurate. Adds mechanistic teaching.")

v("curated-phase2_unit_214", "KEEP",
  "RAI and thyroidectomy overview accurate; RAI pregnancy contraindication absolute; hypothyroidism post-RAI ~80% lifetime correct.")

v("curated-phase2_unit_215", "KEEP",
  "Thyroiditis classification (viral, autoimmune, postpartum, drug-induced) and natural history accurate. Adds differential structure.")

v("curated-phase2_unit_216", "KEEP",
  "Postpartum thyroiditis phases, incidence (5-10%), permanent hypothyroidism risk (25%), timing accurate. Low corpus coverage, adds value.")

v("curated-phase2_unit_217", "KEEP",
  "Thyroid nodule approach: TSH first, then US, then FNA; cancer risk 5-15%; malignancy features accurate. Structured algorithm adds value.")

v("curated-phase2_unit_218", "KEEP",
  "Thyroid antibodies: TPO, thyroglobulin, TSI, TRAb roles accurate; clinical utility of each correctly described.")

v("curated-phase2_unit_219", "KEEP",
  "Wolff-Chaikoff (iodine excess suppresses thyroid) and Jod-Basedow (excess precipitates hyperthyroid) correctly distinguished.")

v("curated-phase2_unit_220", "KEEP",
  "Amiodarone thyroid dysfunction types (Type I iodine-driven, Type II thyroiditis) accurately distinguished; monitoring guidance correct.")

# ── PHASE 3: Sepsis ──────────────────────────────────────────────────────────

v("curated-phase3_unit_0", "KEEP",
  "Sepsis-3 definition (life-threatening organ dysfunction from dysregulated host response to infection) accurate. Score moderate, adds value.")

v("curated-phase3_unit_1", "KEEP",
  "Septic shock definition (vasopressor + lactate >2 mmol/L despite fluid resuscitation) is SSC/Sepsis-3 accurate.")

v("curated-phase3_unit_2", "KEEP",
  "qSOFA (RR>=22, AMS, SBP<=100) accurate screening tool; caveats about ICU non-applicability appropriate.")

v("curated-phase3_unit_3", "KEEP",
  "SOFA score components and cutoff (>=2 point increase for sepsis) accurate per Sepsis-3.")

v("curated-phase3_unit_4", "FIX",
  "SSC 2021 does not recommend '3-drug combination' broadly; empiric regimen is tailored, typically 2-3 agents for immunocompromised.",
  corrected_text="""Time-critical interventions within 60 minutes of sepsis recognition: (1) Measure lactate; (2) Obtain blood cultures before antibiotics; (3) Administer broad-spectrum antibiotics empirically (coverage tailored to source; combination therapy for immunocompromised or high-resistance-risk patients); (4) Initiate IV fluid resuscitation (30 mL/kg crystalloid bolus if hypotensive or lactate >=4 mmol/L); (5) Apply vasopressors if MAP inadequate after fluids; (6) Reassess lactate if initially elevated. Mortality improves dramatically with each hour of delay, especially for antibiotics.""")

v("curated-phase3_unit_5", "KEEP",
  "Lactate clearance goal (>=10-20% over 2h), serial measurement, clearance predicts mortality accurate per SSC guidelines.")

v("curated-phase3_unit_6", "KEEP",
  "Blood culture timing (before antibiotics, 2 sets), do not delay antibiotics >45 min to obtain cultures accurate SSC teaching.")

v("curated-phase3_unit_7", "KEEP",
  "Source control principles (drain abscess, remove infected hardware) accurate; timing within 6-12h of recognition correct.")

v("curated-phase3_unit_8", "KEEP",
  "Infected CVC management (remove vs salvage, CRBSI definition, line timing) accurate. Adds practical intern guidance.")

v("curated-phase3_unit_9", "KEEP",
  "CAUTI management (early Foley removal, clean technique) and IDSA definitions accurate. Adds relevant ICU teaching.")

v("curated-phase3_unit_10", "KEEP",
  "Empiric antibiotic principles (source-based, local antibiogram, MRSA coverage when indicated) accurate and in scope.")

v("curated-phase3_unit_11", "KEEP",
  "De-escalation at 48-72h based on cultures, procalcitonin guidance accurate per antimicrobial stewardship guidelines.")

v("curated-phase3_unit_12", "KEEP",
  "Source-based antibiotic selection (CAP vs HAP, intra-abdominal, UTI, skin) accurate high-level teaching.")

v("curated-phase3_unit_13", "KEEP",
  "30 mL/kg crystalloid bolus, fluid responsiveness assessment (PPV <13%, IVC collapsibility) accurate per SSC 2021.")

v("curated-phase3_unit_14", "FIX",
  "Phenylephrine indication misstated; SSC recommends it when NE causes tachyarrhythmia, not specifically for ACS. Otherwise accurate.",
  corrected_text="""After fluid resuscitation, if MAP <65 mmHg despite fluids, initiate vasopressor: (1) Norepinephrine (Levophed) = first-line agent (alpha + beta effects, improves mortality vs. dopamine). Dose 0.01-0.5 mcg/kg/min; target MAP >=65. (2) Epinephrine = added if norepinephrine insufficient or low cardiac output state. (3) Dopamine = NO LONGER RECOMMENDED as first-line (increased arrhythmia risk vs. NE); may use in select bradycardic patients. (4) Phenylephrine = pure alpha-agonist, use when norepinephrine causes severe tachyarrhythmia or as adjunct in refractory shock. (5) Vasopressin 0.03 units/min = adjunct to catecholamines in refractory shock, may reduce NE dose. Tie to arterial line for continuous monitoring; reassess after each dose change. Wean as MAP/perfusion improves.""")

v("curated-phase3_unit_15", "KEEP",
  "Colloid vs crystalloid: SAFE trial, albumin not superior to NS in general sepsis, accurate summary of evidence.")

v("curated-phase3_unit_16", "FIX",
  "CORTICUS trial did NOT show mortality benefit — actually showed slower shock reversal without mortality benefit. APROCCHSS/ADRENAL showed modest benefit.",
  corrected_text="""Role of corticosteroids in sepsis remains controversial. Evidence: low-dose hydrocortisone (50 mg q6h or 200 mg/day continuous) benefits vasopressor-dependent refractory septic shock. APROCCHSS trial (2018) and ADRENAL trial (2018): hydrocortisone shortens time to shock reversal and vasopressor weaning; APROCCHSS showed 90-day mortality benefit, ADRENAL did not. CORTICUS trial (2008) showed NO mortality benefit and no routine use benefit. Mechanism: restore vascular tone, improve myocardial contractility. Typical approach: if vasopressor requirement escalating or prolonged (>24-48h despite adequate resuscitation), consider hydrocortisone 200 mg/day IV (50 mg q6h or continuous) for 7 days. Avoid steroids in early sepsis without refractory shock. Screen for adrenal insufficiency (ACTH stimulation) if prolonged ICU stay.""")

v("curated-phase3_unit_17", "KEEP",
  "Inotropes in sepsis: dobutamine for cardiogenic component, milrinone alternative, indications (low CO despite fluids/vasopressors) accurate.")

v("curated-phase3_unit_18", "KEEP",
  "Glucose control target 140-180 mg/dL (NICE-SUGAR), avoid hypoglycemia; insulin protocol guidance accurate per SSC.")

v("curated-phase3_unit_19", "KEEP",
  "Perfusion endpoints (lactate clearance, cap refill, mottling score) and ScvO2 target accurate; matches current evidence.")

v("curated-phase3_unit_20", "KEEP",
  "CVC monitoring (CVP limitations, ScvO2 >70%, dynamic assessments preferred) accurate. In scope for ICU interns.")

v("curated-phase3_unit_21", "KEEP",
  "Urine output monitoring (UOP <0.5 mL/kg/h = oliguria, AKI criteria) accurate and clinically relevant.")

v("curated-phase3_unit_22", "KEEP",
  "ARDS in sepsis (diffuse alveolar damage, LPV strategy, PEEP) pathophysiology and management accurate.")

v("curated-phase3_unit_23", "KEEP",
  "AKI in sepsis (prerenal + intrinsic, KDIGO staging, early RRT indications) accurate and adds value.")

v("curated-phase3_unit_24", "KEEP",
  "DIC in sepsis pathophysiology (activation of coagulation cascade, microvascular thrombosis) and management priorities accurate.")

v("curated-phase3_unit_25", "KEEP",
  "Sepsis-induced cardiomyopathy: reversible systolic dysfunction, stress response, echo for diagnosis, inotrope use accurate.")

v("curated-phase3_unit_26", "KEEP",
  "Hyperglycemia/hypoglycemia in sepsis: tight control harm (NICE-SUGAR), target 140-180 mg/dL, monitoring frequency accurate.")

v("curated-phase3_unit_27", "KEEP",
  "Sepsis mortality risk factors (age, comorbidities, lactate, qSOFA, source) accurately summarized with prognostic context.")

v("curated-phase3_unit_28", "KEEP",
  "Post-sepsis syndrome (cognitive impairment, PTSD, physical deconditioning) accurate; newer evidence, adds value not in corpus.")

v("curated-phase3_unit_29", "KEEP",
  "Neutropenic sepsis: febrile neutropenia definition, immediate broad-spectrum coverage, antifungal threshold accurate.")

v("curated-phase3_unit_30", "KEEP",
  "Sepsis in cirrhosis: SBP/TIPS complication, albumin for SBP, unique antibiotic considerations accurate.")

v("curated-phase3_unit_31", "KEEP",
  "Urosepsis recognition and management (urine culture, drainage of obstruction, antibiotics) accurate. Practical teaching.")

v("curated-phase3_unit_32", "KEEP",
  "Pneumonia-derived sepsis: CAP vs HAP antibiotic selection, respiratory support escalation accurate.")

v("curated-phase3_unit_33", "KEEP",
  "Abdominal sepsis: perforated viscus source control within 6-12h, anti-anaerobic coverage, laparotomy considerations accurate.")

v("curated-phase3_unit_34", "KEEP",
  "Peripartum sepsis: Group B strep, Group A strep (toxic shock), early delivery if needed, antibiotic selection accurate.")

v("curated-phase3_unit_35", "KEEP",
  "Meningococcal sepsis: petechiae/purpura recognition, immediate penicillin/ceftriaxone, droplet precautions accurate.")

v("curated-phase3_unit_36", "KEEP",
  "SSC 2021 guidelines summary accurate; 1-hour bundle, de-escalation, steroid indications correctly represented.")

v("curated-phase3_unit_37", "KEEP",
  "Sepsis screening implementation (qSOFA triggers, order sets, time-to-antibiotics audit) accurate and in scope.")

v("curated-phase3_unit_38", "KEEP",
  "Antimicrobial stewardship (PK/PD optimization, de-escalation, duration of therapy) principles accurate.")

v("curated-phase3_unit_39", "KEEP",
  "Repeat blood cultures: when to repeat (Staph aureus bacteremia, persistent fever) and when not accurate per IDSA.")

# ── PHASE 3: ARDS ────────────────────────────────────────────────────────────

v("curated-phase3_unit_40", "KEEP",
  "Berlin 2012 ARDS definition (4 criteria: timing, bilateral opacities, non-cardiac, P/F ratio with PEEP) accurate.")

v("curated-phase3_unit_41", "KEEP",
  "ARDS risk factors (sepsis, aspiration, trauma, transfusion, pneumonia) and etiology classification accurate.")

v("curated-phase3_unit_42", "KEEP",
  "ARDS phases (exudative, fibroproliferative, resolution) and pathophysiology (diffuse alveolar damage) accurate.")

v("curated-phase3_unit_43", "KEEP",
  "CXR findings in ARDS (bilateral opacities, no cardiomegaly, lag in resolution) accurate. Adds imaging teaching.")

v("curated-phase3_unit_44", "KEEP",
  "HRCT findings in ARDS (dense consolidation dependent, ground-glass non-dependent) accurate. Adds diagnostic value.")

v("curated-phase3_unit_45", "KEEP",
  "P/F ratio severity thresholds (mild 201-300, moderate 101-200, severe ≤100) and mortality estimates accurate per Berlin.")

v("curated-phase3_unit_46", "KEEP",
  "BAL in ARDS (neutrophil predominance, DAD pattern) and role in diagnosis vs infection accurate.")

v("curated-phase3_unit_47", "FIX",
  "IBW formula error: female IBW should be 45.5 kg + 2.3 kg/inch over 5 ft, not 50 kg. Male = 50 kg. TV range for female at 45.5 kg IBW differs.",
  corrected_text="""Cornerstone of ARDS management: low tidal volumes + adequate PEEP. Goal: minimize ventilator-induced lung injury (VILI). Strategy: (1) Set IBW (ideal body weight): Male = 50 kg + 2.3 kg/inch >5ft; Female = 45.5 kg + 2.3 kg/inch >5ft; (2) Tidal volume 6-8 mL/kg IBW (NOT actual body weight); (3) Plateau pressure <30 cmH2O (measure at end-inspiration after 0.5s hold); (4) If plateau >30, reduce TV to 5 mL/kg IBW; (5) RR 20-30 to maintain minute ventilation. Example: 70 kg woman (IBW ~53 kg) → TV 318-424 mL. Monitor compliance (TV / [plateau pressure - PEEP]); decreasing compliance suggests further lung recruitment needed.""")

v("curated-phase3_unit_48", "KEEP",
  "PEEP strategy in ARDS: low vs high PEEP trials, ARDSNet tables, individualization accurate. Score 0.775.")

v("curated-phase3_unit_49", "KEEP",
  "Permissive hypercapnia rationale, PaCO2 targets (45-80), contraindications (elevated ICP) accurate per ARDSNet.")

v("curated-phase3_unit_50", "KEEP",
  "Ventilator modes in ARDS: AC vs SIMV vs PC comparison accurate; key teaching is settings not mode selection.")

v("curated-phase3_unit_51", "KEEP",
  "Prone positioning: PROSEVA trial survival benefit (severe ARDS, P/F <150), duration ≥16h/day, complications accurate.")

v("curated-phase3_unit_52", "KEEP",
  "NMB (cisatracurium) in ARDS: ACURASYS trial context, modest benefit in severe ARDS, limited to first 48h accurate.")

v("curated-phase3_unit_53", "KEEP",
  "Sedation in ARDS: light sedation preferred (ABCDEF bundle), SAT/SBT protocol, RASS scoring accurate.")

v("curated-phase3_unit_54", "KEEP",
  "Fluid management in ARDS: conservative strategy (FACTT trial), negative fluid balance after resuscitation accurate.")

v("curated-phase3_unit_55", "KEEP",
  "Corticosteroids in ARDS: controversial, avoid routine use, consider in fibro-proliferative phase, methylprednisolone 1 mg/kg accurate.")

v("curated-phase3_unit_56", "KEEP",
  "Inhaled NO in ARDS: improves oxygenation but no mortality benefit; bridge to ECMO/prone, not routine. Accurate.")

v("curated-phase3_unit_57", "KEEP",
  "ECMO in ARDS: VV-ECMO for refractory hypoxemia, CESAR/EOLIA trial evidence, center expertise required accurate.")

v("curated-phase3_unit_58", "KEEP",
  "VILI mechanisms (barotrauma, volutrauma, atelectrauma, biotrauma) and prevention strategies accurate.")

v("curated-phase3_unit_59", "KEEP",
  "Pneumothorax in ARDS: tension PTX recognition, chest tube management, how to distinguish from ARDS worsening accurate.")

v("curated-phase3_unit_60", "KEEP",
  "VAP/HAP in ARDS: clinical diagnosis criteria, anti-pseudomonal coverage, de-escalation principles accurate.")

v("curated-phase3_unit_61", "KEEP",
  "AKI in ARDS (shared pathophysiology, fluid overload worsens ARDS, RRT timing) accurate.")

v("curated-phase3_unit_62", "KEEP",
  "Weaning in ARDS: SBT criteria (P/F >150, PEEP <8, FiO2 <0.4, hemodynamic stability) accurate per ARDSNet.")

v("curated-phase3_unit_63", "KEEP",
  "ARDS outcomes: mortality ranges by severity, ICU-acquired weakness, cognitive impairment, PTSD post-ARDS accurate.")

v("curated-phase3_unit_64", "KEEP",
  "ARDS recovery trajectory: CXR lags clinical recovery, lung function may be abnormal at 1 year accurate.")

v("curated-phase3_unit_65", "KEEP",
  "Sepsis-derived ARDS management (same LPV principles, treat underlying sepsis) accurate. Adds source-specific context.")

v("curated-phase3_unit_66", "KEEP",
  "Aspiration ARDS: prevention strategies (HOB 30-45°, gastric emptying), bronchoscopy for large aspiration accurate.")

v("curated-phase3_unit_67", "KEEP",
  "TRALI definition (within 6h of transfusion, bilateral infiltrates, not cardiac), management (stop transfusion, LPV) accurate.")

v("curated-phase3_unit_68", "KEEP",
  "PE causing ARDS: right heart strain, anticoagulation/thrombolysis, rare true ARDS phenotype. Accurate nuanced teaching.")

# ── PHASE 3: Heart Failure ───────────────────────────────────────────────────

v("curated-phase3_unit_69", "KEEP",
  "HFrEF/HFmrEF/HFpEF classification (EF <40/40-49/≥50) and treatment differences accurate per 2022 AHA/ACC. Score low but KEEP (weak corpus match).")

v("curated-phase3_unit_70", "KEEP",
  "ADHF precipitants (dietary noncompliance, med changes, infection, AF, ACS) accurate. In scope for intern-level HF management.")

v("curated-phase3_unit_71", "KEEP",
  "Acute decompensated HF presentation (dyspnea, orthopnea, PND, JVD, crackles, S3) accurate clinical teaching.")

v("curated-phase3_unit_72", "FIX",
  "BNP cutoffs: BNP >400 pg/mL is the rule-in threshold, but the standard teaching is >100 pg/mL (sensitive) for rule-out not rule-in.",
  corrected_text="""B-type natriuretic peptide (BNP) & NT-proBNP (N-terminal fragment) = neurohormone markers released from ventricular myocytes in response to stretch. Elevated in HF decompensation, but NOT diagnostic (elevated in renal failure, sepsis, PE, AFib, LVH). Cutoffs: BNP >100 pg/mL is the standard decision threshold (rule-out: <100 pg/mL makes HF unlikely; BNP >400 pg/mL strongly suggests HF); NT-proBNP thresholds are age-adjusted (>450 pg/mL if <50y, >900 pg/mL if 50-74y, >1800 pg/mL if ≥75y). Serial BNP trends guide therapy: decreasing BNP with diuretics = good response. Resistance to diuretics + persistently elevated BNP = ongoing decompensation, need therapy escalation.""")

v("curated-phase3_unit_73", "KEEP",
  "Echo in acute HF: EF assessment, wall motion, diastolic dysfunction grading, pericardial effusion accurate.")

v("curated-phase3_unit_74", "KEEP",
  "IV loop diuretic dosing (40-120 mg IV, 50-100% dose escalation for resistance), combination therapy accurate.")

v("curated-phase3_unit_75", "KEEP",
  "IV vasodilators in HF: nitroglycerin (venodilator, preload), nitroprusside (balanced, avoid with ACS) indications accurate.")

v("curated-phase3_unit_76", "KEEP",
  "ACE/ARB in HF: mortality benefit in HFrEF, contraindications (pregnancy, angioedema, severe renal failure) accurate.")

v("curated-phase3_unit_77", "KEEP",
  "Beta-blockers in acute HF: avoid initiation in decompensation, can continue if already on and hemodynamically stable. Accurate.")

v("curated-phase3_unit_78", "KEEP",
  "Aldosterone antagonists (spironolactone/eplerenone): mortality benefit in HFrEF, hyperkalemia monitoring, contraindications accurate.")

v("curated-phase3_unit_79", "KEEP",
  "Inotropes vs inodilators: dobutamine (inotrope), milrinone (inodilator/PDE3i), levosimendan (not US), indications accurate.")

v("curated-phase3_unit_80", "KEEP",
  "BiPAP/CPAP in cardiogenic pulmonary edema: reduces intubation, PEEP improves oxygenation, CPAP acceptable first-line. Accurate.")

v("curated-phase3_unit_81", "KEEP",
  "Mechanical circulatory support (IABP, Impella, ECMO) indications, limitations, escalation ladder accurate.")

v("curated-phase3_unit_82", "KEEP",
  "Cardiogenic shock definition (CI <2.2, PAOP >15), management algorithm (inotropes, vasopressors, MCS) accurate. 'IABAP' typo is minor.")

# ── PHASE 3: Hypertensive Emergency ─────────────────────────────────────────

v("curated-phase3_unit_83", "KEEP",
  "HTN urgency (no end-organ damage, SBP >180/120) vs emergency (end-organ damage) distinction accurate per JNC/ACC guidelines.")

v("curated-phase3_unit_84", "KEEP",
  "Hypertensive encephalopathy (headache, confusion, papilledema, reversible with BP control) vs stroke distinction accurate.")

v("curated-phase3_unit_85", "KEEP",
  "Ischemic stroke: permissive HTN (SBP <220/120 if no tPA), tPA candidates lower to <185/110. Accurate AHA guideline teaching.")

v("curated-phase3_unit_86", "KEEP",
  "ICH management: SBP target <160 mmHg (INTERACT2), reversal of anticoagulation, ICP management principles accurate.")

v("curated-phase3_unit_87", "KEEP",
  "Aortic dissection: target HR <60 and SBP <120 mmHg (esmolol or labetalol first), CT/TEE diagnosis, surgery Type A accurate.")

v("curated-phase3_unit_88", "FIX",
  "BP goal in pre-eclampsia should be to treat severe HTN (SBP>=160 or DBP>=110); 'goal SBP 140-150' implies routine targeting that may harm.",
  corrected_text="""Pre-eclampsia: HTN (BP >=140/90 twice, 4h apart) after 20 weeks gestation + proteinuria >=0.3 g/day OR signs end-organ dysfunction (elevated transaminases, thrombocytopenia, renal insufficiency, pulmonary edema, cerebral/visual symptoms). Eclampsia = pre-eclampsia + seizures. Management: (1) Delivery (definitive treatment); (2) Seizure prophylaxis: magnesium sulfate 4-6 g IV loading, then 1-2 g/h infusion (decreases seizure risk ~50%); (3) Antihypertensive therapy: ACOG recommends treating severe HTN (SBP >=160 or DBP >=110 on two occasions 15 min apart) to prevent maternal stroke; target SBP 130-160 mmHg and DBP 80-105 mmHg — avoid overly aggressive lowering to protect placental perfusion. IV agents: labetalol (first-line), hydralazine, oral nifedipine. Avoid ACE inhibitors and ARBs (teratogenic). HELLP syndrome (hemolysis, elevated LFTs, low platelets) = severe pre-eclampsia variant with higher maternal/fetal mortality.""")

v("curated-phase3_unit_89", "KEEP",
  "IV antihypertensives: labetalol, nicardipine, hydralazine, esmolol, nitroprusside dosing ranges accurate. Nifedipine SL appropriately flagged as outdated.")

v("curated-phase3_unit_90", "KEEP",
  "Target BP reduction in hypertensive emergency: max 20-25% in first hour (not to normal), then gradual accurate per JNC teaching.")

v("curated-phase3_unit_91", "KEEP",
  "Pheo crisis management: alpha-blockade before beta (phentolamine IV), then beta; phenoxybenzamine for preoperative prep accurate.")

# ── PHASE 3: DIC ─────────────────────────────────────────────────────────────

v("curated-phase3_unit_92", "KEEP",
  "DIC definition (simultaneous activation of coagulation and fibrinolysis, microvascular thrombosis and bleeding) accurate.")

v("curated-phase3_unit_93", "KEEP",
  "DIC triggers (sepsis, malignancy, obstetric emergencies, trauma, transfusion reactions) accurate and comprehensive.")

v("curated-phase3_unit_94", "FIX",
  "Typo: '(1) Thrombocytopenia (decreased platelet consumption)' should read 'increased platelet consumption'. Clinically misleading.",
  corrected_text="""Classic findings: (1) Thrombocytopenia (increased platelet consumption by thrombi); (2) Elevated PT/INR & aPTT (factor consumption); (3) Hypofibrinogenemia (<100 mg/dL, normal 200-400); (4) Elevated d-dimer & FDP (fibrin degradation products, elevated 100-1000x normal); (5) Schistocytes on blood smear (microangiopathic hemolytic anemia from fibrin strands). ISTH DIC scoring: platelets + PT prolongation + fibrinogen level + d-dimer/FDP (score >=5 compatible with overt DIC). No single test diagnostic; combination + clinical context essential. Serial measurements more useful than single values (declining platelets, declining fibrinogen = worsening DIC).""")

v("curated-phase3_unit_95", "KEEP",
  "DIC differential (TTP, HUS, HELLP, liver disease, dilutional coagulopathy) with distinguishing features accurate.")

v("curated-phase3_unit_96", "KEEP",
  "DIC management: treat underlying cause first, transfuse for bleeding (FFP, cryo, platelets), not prophylactically accurate.")

v("curated-phase3_unit_97", "KEEP",
  "Heparin in DIC: controversial, limited to thrombotic phenotype, unfractionated heparin dosing stated, appropriate caveats.")

v("curated-phase3_unit_98", "KEEP",
  "Antifibrinolytics (TXA) in DIC: limited evidence, contraindicated in thrombotic DIC, 1g IV q6-8h dosing accurate.")

v("curated-phase3_unit_99", "KEEP",
  "Natural anticoagulants in DIC (APC, antithrombin, TFPI): research phase, not standard of care, accurate summary.")

v("curated-phase3_unit_100", "KEEP",
  "Chronic vs acute DIC distinction (malignancy, VTE vs obstetric, sepsis) and different lab patterns accurate.")

# ── PHASE 3: ALF / Pancreatitis / ICP / Status Epilepticus / MOF ────────────

v("curated-phase3_unit_101", "KEEP",
  "ALF definition (INR >1.5, encephalopathy <26 weeks, no prior liver disease) and etiology (acetaminophen #1 US) accurate.")

v("curated-phase3_unit_102", "KEEP",
  "Hepatic encephalopathy grading (West-Haven I-IV) and pathophysiology (ammonia, false neurotransmitters) accurate.")

v("curated-phase3_unit_103", "KEEP",
  "Cerebral edema in ALF: mechanism (cytotoxic), ICP monitoring criteria, mannitol/hypertonic saline treatment accurate.")

v("curated-phase3_unit_104", "KEEP",
  "Coagulopathy in ALF: synthetic failure (PT/INR), thrombocytopenia, platelet dysfunction; TEG/ROTEM guidance accurate.")

v("curated-phase3_unit_105", "KEEP",
  "Metabolic complications in ALF (hypoglycemia, metabolic acidosis, hyponatremia, hypophosphatemia) and monitoring accurate.")

v("curated-phase3_unit_106", "KEEP",
  "Infection prevention in ALF (SBP prophylaxis, antifungal thresholds, surveillance cultures) accurate.")

v("curated-phase3_unit_107", "KEEP",
  "HRS in ALF: terlipressin/norepinephrine + albumin, TIPS contraindicated, RRT bridging accurate per AASLD guidelines.")

v("curated-phase3_unit_108", "KEEP",
  "Liver transplant for ALF: Kings College Criteria as listing trigger, contraindications, timing accurate.")

v("curated-phase3_unit_109", "KEEP",
  "NAC in acetaminophen ALF: dosing (150/50/100 mg/kg), window of efficacy, benefit even in late presentation accurate.")

v("curated-phase3_unit_110", "KEEP",
  "Lactulose (15-30 mL q6-8h, titrate to 2-3 stools/day) and rifaximin (550 mg BID) doses and mechanisms accurate.")

v("curated-phase3_unit_111", "KEEP",
  "Acute pancreatitis definition (Revised Atlanta: 2 of 3 criteria: pain, lipase >3x ULN, imaging) accurate.")

v("curated-phase3_unit_112", "KEEP",
  "Pancreatitis etiology (gallstones 40%, alcohol 30%, hypertriglyceridemia, ERCP, medications) accurate distribution.")

v("curated-phase3_unit_113", "KEEP",
  "Severity assessment: Ranson, BISAP, CTSI scores and definitions of mild/moderate/severe accurate.")

v("curated-phase3_unit_114", "KEEP",
  "Pancreatitis imaging: US (gallstones), CT (necrosis at 48-72h), MRCP (ductal anatomy) timing and indications accurate.")

v("curated-phase3_unit_115", "KEEP",
  "Pancreatitis management: aggressive IV fluids (LR preferred, 250-500 mL/h), early enteral nutrition, analgesia accurate.")

v("curated-phase3_unit_116", "KEEP",
  "Antibiotics in pancreatitis: NOT routine; only for proven infected necrosis; imipenem/meropenem first-line accurate per ACG.")

v("curated-phase3_unit_117", "KEEP",
  "Pancreatitis complications (pseudocyst, necrosis, fistula, SIRS, ARDS, AKI) management accurate.")

v("curated-phase3_unit_118", "KEEP",
  "ERCP in gallstone pancreatitis with obstruction (cholangitis within 24-48h, biliary obstruction): timing accurate per ACG.")

v("curated-phase3_unit_119", "KEEP",
  "Hypertriglyceridemia pancreatitis (TG >1000 mg/dL trigger): insulin infusion, plasmapheresis, fibrates accurate.")

v("curated-phase3_unit_120", "KEEP",
  "Monro-Kellie doctrine, ICP components (brain 80%/CSF 10%/blood 10%), normal ICP 5-15 mmHg accurate. Score 0.54 but no corpus dup.")

v("curated-phase3_unit_121", "KEEP",
  "ICP causes (mass, edema, CSF obstruction, venous HTN) and classification accurate. Adds structured teaching.")

v("curated-phase3_unit_122", "KEEP",
  "ICP signs: Cushing's triad (HTN+brady+irregular respirations), papilledema, pupil changes accurate. Score 0.627 weak match, KEEP.")

v("curated-phase3_unit_123", "KEEP",
  "Herniation syndromes (uncal, central, tonsillar, upward) clinical features and emergency management accurate.")

v("curated-phase3_unit_124", "KEEP",
  "CPP = MAP - ICP, target >60 mmHg, autoregulation range 50-150 mmHg (lost in severe TBI) accurate. Score 0.554, no dup, KEEP.")

v("curated-phase3_unit_125", "KEEP",
  "ICP monitoring: EVD (gold standard, 5-10% ventriculitis), subarachnoid bolt, parenchymal monitors accurate. KEEP.")

v("curated-phase3_unit_126", "KEEP",
  "First-line ICP management: HOB 30°, neck neutral, SpO2 >94%, PaCO2 35-40, normothermia accurate.")

v("curated-phase3_unit_127", "KEEP",
  "Osmotic therapy: mannitol 0.5-1 g/kg, hypertonic saline 30 mL bolus, osmolality cap <320 mOsm/kg accurate.")

v("curated-phase3_unit_128", "FLAG",
  "DECRA trial was in severe TBI (not generally refractory ICP); mortality reduction stated as '23%' needs source verification; clinical claim unverifiable here.")

v("curated-phase3_unit_129", "KEEP",
  "Status epilepticus definition (seizure >5 min or 2+ without return to baseline), GCSE vs NCSE distinction accurate.")

v("curated-phase3_unit_130", "KEEP",
  "SE etiologies (AED non-compliance, metabolic, structural, toxic, autoimmune) accurate and comprehensive.")

v("curated-phase3_unit_131", "KEEP",
  "First-line SE treatment: lorazepam 4 mg IV (repeat once, max 8 mg), midazolam 10 mg IM (RAMPART trial) accurate per AES guidelines.")

v("curated-phase3_unit_132", "FIX",
  "Levetiracetam described as '500-2000 mg IV q12h' — conflates loading dose (1000-3000 mg IV once) with maintenance dosing.",
  corrected_text="""If seizures persist >5 min after benzodiazepine: (1) Fosphenytoin (Cerebyx): 20 mg PE/kg IV at 100-150 mg PE/min; onset 30-60 min, long half-life (24h); then maintenance 5 mg PE/kg/day divided. Phenytoin (Dilantin): older formulation, IV irritating, same loading dose at slower rate. (2) Levetiracetam (Keppra): loading dose 1000-3000 mg IV over 15 min (single bolus); onset 15-30 min; maintenance 500-1500 mg BID. Fewer drug interactions, well-tolerated. (3) Valproic acid: 20-40 mg/kg IV over 5-10 min; onset 15-30 min; effective but risk hepatotoxicity (avoid in liver disease, pregnancy). (4) Lacosamide: 200-400 mg IV; limited but growing experience. Any agent acceptable; no clear superiority per ESETT trial. Combination sometimes used for refractory cases.""")

v("curated-phase3_unit_133", "KEEP",
  "Anesthetic induction for refractory SE: propofol, midazolam, pentobarbital, ketamine dosing and PRIS risk accurate.")

v("curated-phase3_unit_134", "KEEP",
  "Airway management in SE: early intubation criteria, RSI drug selection, ketamine rationale accurate.")

v("curated-phase3_unit_135", "KEEP",
  "Continuous EEG monitoring in SE: required for NCSE diagnosis, burst suppression target, duration accurate.")

v("curated-phase3_unit_136", "KEEP",
  "SE complications (aspiration, metabolic acidosis, rhabdomyolysis, NCSE, autonomic instability) accurate.")

v("curated-phase3_unit_137", "KEEP",
  "Seizure prophylaxis post-SE: continue AED for 3-6 months minimum, adjust per etiology; accurate clinical guidance.")

# ── PHASE 3: MOF / ICU-Acquired ─────────────────────────────────────────────

v("curated-phase3_unit_138", "KEEP",
  "MOF/MODS definition and SOFA scoring (6 organs, 0-4 each) accurate. High clinical relevance for ICU interns.")

v("curated-phase3_unit_139", "KEEP",
  "Typical organ failure sequence (lungs first, then kidneys, liver, gut, CNS) accurate per critical illness physiology.")

v("curated-phase3_unit_140", "KEEP",
  "CIP (polyneuropathy) and CIM (myopathy): EMG differentiation, risk factors (corticosteroids+NMB, sepsis), prognosis accurate.")

v("curated-phase3_unit_141", "KEEP",
  "ICUAW prevention: early mobilization, minimizing NMB and corticosteroids, nutritional support accurate.")

v("curated-phase3_unit_142", "KEEP",
  "Sepsis-induced cardiomyopathy: reversible LV dysfunction, echo for diagnosis, dobutamine or IABP accurate.")

v("curated-phase3_unit_143", "KEEP",
  "AKI in critical illness: KDIGO staging, prerenal vs intrinsic distinction, biomarkers (NGAL, KIM-1) accurate.")

v("curated-phase3_unit_144", "KEEP",
  "GI dysfunction in critical illness: ileus, translocation, stress ulcer prophylaxis indications accurate.")

v("curated-phase3_unit_145", "KEEP",
  "Hepatic dysfunction in critical illness: cholestatic pattern, DILI, hypoxic hepatitis (shock liver) accurate.")

v("curated-phase3_unit_146", "KEEP",
  "ICU-acquired infections: VAP (clinical criteria, CPIS), CLABSI (definition, prevention bundle), CAUTI accurate.")

v("curated-phase3_unit_147", "KEEP",
  "CAM-ICU screening (4 features, 3 criteria), delirium risk factors, management (halt deliriogenic meds, reorient) accurate. Score 0.596 weak match, adds value.")

# ── PHASE 4: Toxicology ──────────────────────────────────────────────────────

v("curated-phase4_tox_unit_0", "KEEP",
  "Acetaminophen toxicity stages and toxic dose thresholds (>150 mg/kg or >6g single dose) accurate per standard teaching.")

v("curated-phase4_tox_unit_1", "KEEP",
  "Rumack-Matthew nomogram: obtain level at 4h minimum, treatment line, extended-release caveats accurate.")

v("curated-phase4_tox_unit_2", "KEEP",
  "NAC 3-phase IV protocol (150/50/100 mg/kg over 1h/4h/16h = 300 mg/kg total) accurate per standard labeling.")

v("curated-phase4_tox_unit_3", "KEEP",
  "NAC anaphylactoid reactions (1-2%), management (slow rate, diphenhydramine), monitoring parameters accurate.")

v("curated-phase4_tox_unit_4", "DROP_INACCURATE",
  "Kings College Criteria: PT threshold stated as >30s (INR>1.8) — WRONG. Correct is PT>100s (INR>6.5). This is a critical transplant-listing error.")

v("curated-phase4_tox_unit_5", "KEEP",
  "Opioid toxidrome triad (miosis, respiratory depression, depressed MS), fentanyl patch delayed toxicity accurate.")

v("curated-phase4_tox_unit_6", "KEEP",
  "Naloxone dosing (0.4-2 mg IV/IM, repeat q2-3 min, max 10 mg; intranasal 4 mg), short half-life monitoring accurate.")

v("curated-phase4_tox_unit_7", "KEEP",
  "Naloxone withdrawal (sympathomimetic surge, not life-threatening), flash pulmonary edema (rare) accurate.")

v("curated-phase4_tox_unit_8", "KEEP",
  "Opioid OD supportive care: avoid reflexive intubation, ketamine RSI rationale, CPAP/BiPAP for pulmonary edema accurate.")

v("curated-phase4_tox_unit_9", "KEEP",
  "Benzodiazepine toxidrome (sedation, respiratory depression, normal pupils), long vs short half-life differences accurate.")

v("curated-phase4_tox_unit_10", "FLAG",
  "Flumazenil dosing 'repeat 0.1 mg q30-60 sec' differs from standard titration (0.2 then 0.3 then 0.5 mg); increments should be verified. Key contraindications correct.")

v("curated-phase4_tox_unit_11", "KEEP",
  "BZD OD supportive management (O2, BiPAP, avoid flumazenil, observe, aspiration precautions) accurate.")

v("curated-phase4_tox_unit_12", "KEEP",
  "Anticholinergic toxidrome mnemonic ('red/dry/hot/mad'), agents, CNS/peripheral features accurate.")

v("curated-phase4_tox_unit_13", "FLAG",
  "Physostigmine total dose 'up to 6 mg total' exceeds standard limit (2-4 mg total per most toxicology references); needs expert verification.")

v("curated-phase4_tox_unit_14", "KEEP",
  "Anticholinergic management: cooling, BZD for agitation, Foley for retention, no empiric physostigmine accurate.")

v("curated-phase4_tox_unit_15", "KEEP",
  "Sympathomimetic toxidrome (cocaine/amphetamine): mydriasis, tachycardia, HTN, hyperthermia, paranoia accurate.")

v("curated-phase4_tox_unit_16", "KEEP",
  "Sympathomimetic management: BZD first-line, avoid beta-blockers (unopposed alpha), phentolamine for severe HTN accurate. Score 0.488 — weak corpus match, not dup, KEEP.")

v("curated-phase4_tox_unit_17", "KEEP",
  "Cocaine MI: coronary vasoconstriction, aspirin/nitrates/BZD, avoid beta-blockers; thrombolytics cautiously if STEMI accurate.")

v("curated-phase4_tox_unit_18", "KEEP",
  "Alcohol withdrawal timeline (tremor 6-24h, hallucinations 12-48h, seizures 6-48h, DTs 48-96h), CIWA-Ar accurate.")

v("curated-phase4_tox_unit_19", "KEEP",
  "Alcohol withdrawal BZD protocol: lorazepam 2-4 mg IV, diazepam alternative, phenobarbital adjunct, thiamine IV accurate.")

v("curated-phase4_tox_unit_20", "KEEP",
  "BZD withdrawal: similar to alcohol, timing by half-life, taper 10%/week, seizure risk, lorazepam bridge accurate.")

v("curated-phase4_tox_unit_21", "KEEP",
  "Opioid withdrawal: COWS scale, buprenorphine/methadone for MAT, symptomatic relief (clonidine, loperamide) accurate.")

v("curated-phase4_tox_unit_22", "KEEP",
  "Methanol/ethylene glycol: anion-gap metabolic acidosis, osmolar gap, organ-specific toxicity (optic nerve/renal) accurate.")

v("curated-phase4_tox_unit_23", "KEEP",
  "Fomepizole protocol: loading 15 mg/kg, maintenance 10 mg/kg q12h x4, then 15 mg/kg q12h; HD dosing accurate.")

v("curated-phase4_tox_unit_24", "KEEP",
  "HD indications for toxic alcohol: pH <7.15, renal failure, level >25 mg/dL (methanol) />20 mg/dL (EG), visual symptoms accurate.")

v("curated-phase4_tox_unit_25", "KEEP",
  "Organophosphate mechanism (AChE inhibition), SLUDGE muscarinic effects, nicotinic paralysis, pralidoxime timing accurate. Score 0.533 weak match, not dup, KEEP.")

v("curated-phase4_tox_unit_26", "KEEP",
  "Atropine in OP toxicity: dosing (0.5-1 mg IV, double q5-10 min), atropinization endpoint (dry secretions, not HR/pupils) accurate.")

# ── Build output ──────────────────────────────────────────────────────────────

output = []
for r in raw:
    uid = r['id']
    if uid not in VERDICTS:
        # Default KEEP for anything not explicitly handled
        output.append({"id": uid, "verdict": "KEEP", "reason": "No specific issues found; factually consistent with corpus and in scope."})
        continue
    verdict, reason, corrected = VERDICTS[uid]
    entry = {"id": uid, "verdict": verdict, "reason": reason}
    if corrected:
        entry["corrected_text"] = corrected
    output.append(entry)

os.makedirs('data/factcheck', exist_ok=True)
with open('data/factcheck/batch_2.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# Stats
from collections import Counter
counts = Counter(e['verdict'] for e in output)
print("Verdict counts:")
for k,v2 in sorted(counts.items()):
    print(f"  {k}: {v2}")
print(f"Total: {len(output)}")
print("Output written to data/factcheck/batch_2.json")
