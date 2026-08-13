#!/usr/bin/env python3
"""
Phase 3: Remaining high-acuity modules

Tasks 3.3-3.10:
- Acute Decompensated Heart Failure
- Hypertensive Crisis & Emergency
- DIC (Disseminated Intravascular Coagulation)
- Acute Liver Failure & Hepatic Encephalopathy
- Acute Pancreatitis
- Intracranial Hypertension & Cerebral Edema
- Status Epilepticus (Advanced)
- Organ Dysfunction Syndromes (MOF, MODS, CIP, ICUAW)
"""

import json
from datetime import datetime

def create_heart_failure_units():
    """Generate acute decompensated heart failure units."""
    units = [
        {
            "topic": "Heart Failure Phenotypes - EF Classification",
            "subtopic": "hf_phenotypes",
            "content": "Heart failure classified by ejection fraction: HFrEF (reduced EF) = EF <40%, HFmrEF (mildly reduced) = EF 40-49%, HFpEF (preserved EF) = EF ≥50%. HFrEF typically systolic dysfunction (dilated chambers, reduced contractility); HFmrEF mixed; HFpEF typically diastolic dysfunction (stiff LV, impaired filling). ACE inhibitors/ARBs, beta-blockers, aldosterone antagonists proven mortality benefit in HFrEF. HFpEF limited pharmacotherapy options; focus on symptom relief, rate control, comorbidity management. Acute decompensation may occur in any phenotype; precipitants differ slightly (HFrEF: non-adherence, ischemia; HFpEF: HTN, AFib, renal failure).",
            "tags": ["heart_failure", "hf_phenotypes", "ejection_fraction"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Decompensated Heart Failure - Precipitants",
            "subtopic": "adf_precipitants",
            "content": "Common triggers: (1) Non-adherence to medications/fluid restriction; (2) Infection (UTI, pneumonia, endocarditis); (3) Acute coronary syndrome; (4) Uncontrolled hypertension; (5) Arrhythmia (AFib with RVR, VT); (6) Anemia; (7) Renal failure (decreased renal clearance); (8) Thyroid dysfunction; (9) Medications (NSAIDs, steroids, negative inotropes); (10) Pregnancy-related (peripartum cardiomyopathy). Identify precipitant to guide therapy; addressing underlying cause critical for success.",
            "tags": ["heart_failure", "adf", "precipitants"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Decompensated HF Presentation",
            "subtopic": "adf_presentation",
            "content": "Classic signs: dyspnea (exertional, orthopnea, PND), fatigue, lower extremity edema, weight gain (>2-3 lb/day suggests fluid retention). Physical exam: elevated JVD (>4 cm suggests elevated CVP), hepatomegaly (due to RV failure, hepatic congestion), hepatojugular reflex positive, pulmonary crackles (rales), S3 gallop (due to rapid ventricular filling), ascites (advanced). Dyspnea on exertion earliest symptom; progression to PND, orthopnea indicates worsening. Acute presentation: severe dyspnea at rest, orthopnea, pink frothy sputum (cardiogenic pulmonary edema), tachycardia, cool extremities (low cardiac output).",
            "tags": ["heart_failure", "adf", "presentation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "BNP & NT-proBNP in Heart Failure",
            "subtopic": "adf_diagnostics",
            "content": "B-type natriuretic peptide (BNP) & NT-proBNP (N-terminal fragment) = neurohormone markers released from ventricular myocytes in response to stretch. Elevated in HF decompensation, but NOT diagnostic (elevated in renal failure, sepsis, PE, AFib, LVH). Cutoffs: BNP >400 pg/mL or NT-proBNP >900 pg/mL suggest HF; lower values make HF unlikely (good negative predictive value). Serial BNP trends guide therapy: decreasing BNP with diuretics = good response. Resistance to diuretics + persistently elevated BNP = ongoing decompensation, need therapy escalation.",
            "tags": ["heart_failure", "adf", "bnp", "diagnostics"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Echocardiography in Acute HF",
            "subtopic": "adf_diagnostics",
            "content": "Echo: measure EF (Simpson method, visual estimate), chamber sizes (LV, LA, RV dimensions), diastolic dysfunction parameters (E/A ratio, E/e', LA pressure). Valvular disease assessment (MR, TR common in HF). RV function assessment (TAPSE, S' velocity). Pericardial effusion, tamponade physiology. Global longitudinal strain (GLS) emerging marker of systolic dysfunction (more sensitive than EF alone for ischemic disease). Serial echo useful post-admission to assess response to therapy.",
            "tags": ["heart_failure", "adf", "echocardiography"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Diuretic Therapy in Acute Decompensated HF",
            "subtopic": "adf_treatment",
            "content": "First-line: IV loop diuretics (furosemide, torsemide, bumetanide). Dosing: start 40-120 mg IV bolus depending on baseline renal function + diuretic dose at home. Goal: negative fluid balance 0.5-1.0 L/day. Monitor: daily weight, I&Os, creatinine, electrolytes (K, Cl, Mg), urine output. Titration: if inadequate response after 30-60 min, increase dose by 50-100%. Resistance (no urine output despite high diuretic): try higher dose, more frequent dosing (q6h), or continuous infusion. Addition of second agent (thiazide, aldosterone antagonist) may overcome resistance. Watch for: volume depletion (worsening renal function, hypotension), electrolyte abnormalities (hypokalemia, hyponatremia, hypomagnesemia).",
            "tags": ["heart_failure", "adf", "diuretics"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Vasodilators in Acute HF (Nitroglycerin, Nitroprusside)",
            "subtopic": "adf_treatment",
            "content": "IV vasodilators for acute afterload reduction: (1) Nitroglycerin: 10-200 mcg/min IV infusion, primarily venodilator (reduces preload) + arterial vasodilation at higher doses. Benefit: rapid relief dyspnea in pulmonary edema. Tolerance develops after 12-24h (tachyphylaxis). (2) Nitroprusside: 0.3-10 mcg/kg/min IV, balanced arterial/venous vasodilation. More potent hypotensive effect; requires close monitoring (risk hypotension, AKI). Cyanide toxicity risk if >4 mcg/kg/min for >4h. Use: severe hypertensive emergency + pulmonary edema. Both agents require continuous hemodynamic monitoring, arterial line preferred.",
            "tags": ["heart_failure", "adf", "vasodilators"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ACE Inhibitors & ARBs in Heart Failure",
            "subtopic": "adf_treatment",
            "content": "ACE inhibitors (lisinopril, enalapril) & ARBs (losartan, valsartan) proven mortality benefit in HFrEF (SOLVD trial: reduced mortality + hospitalizations). Mechanism: vasodilation, reduced aldosterone secretion, cardiac remodeling prevention. Dosing: start low (lisinopril 5 mg daily), titrate up as tolerated. Contraindications: acute AKI (SCr rise >30%), hyperkalemia (K >5.5), severe hypotension (SBP <90). Monitor: K, creatinine at baseline + 1-2 weeks, then as needed. Can continue even in acute decompensation (avoid in acute MI with cardiogenic shock until stabilized). ARNI (sacubitril/valsartan) newer option; superior to ACE inhibitor alone (PARADIGM trial).",
            "tags": ["heart_failure", "adf", "ace_inhibitor", "arb"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Beta-Blockers in Acute HF - Initiation & Safety",
            "subtopic": "adf_treatment",
            "content": "Beta-blockers (carvedilol, metoprolol succinate) reduce mortality + hospitalizations in HFrEF (COPERNICUS, MERIT-HF trials). Counter-intuitive: initiate during acute decompensation AFTER stabilization (once euvolemic, hemodynamically stable). Start low dose (carvedilol 3.125 mg daily), double every 1-2 weeks to target dose. Risk early: negative inotropic effect may worsen acute decompensation, hypotension. Contraindications: acute pulmonary edema, cardiogenic shock (until inotrope support), severe bradycardia (HR <50). Continue beta-blocker even in admitted with HF exacerbation; don't discontinue.",
            "tags": ["heart_failure", "adf", "beta_blockers"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Aldosterone Antagonists (Spironolactone, Eplerenone)",
            "subtopic": "adf_treatment",
            "content": "Spironolactone & eplerenone (potassium-sparing diuretics, aldosterone antagonists) reduce mortality in HFrEF with moderate-severe symptoms (RALES trial: 30% mortality reduction). Dosing: spironolactone 12.5-50 mg daily; eplerenone (selective aldosterone antagonist) 25-50 mg daily. Onset: slow (weeks to months for full effect); don't add for acute symptom relief. Key risk: hyperkalemia (especially if K >5.0 or renal dysfunction). Monitor K closely (baseline, 3 days, 1 week, then monthly). Caution: avoid combined with ACE inhibitor + loop diuretic at high doses (triple therapy = hyperkalemia risk). SGLT2 inhibitors (dapagliflozin, empagliflozin) emerging newer agents with mortality benefit, favorable side effect profile.",
            "tags": ["heart_failure", "adf", "aldosterone_antagonist"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Inotropes vs Inodilators in Acute HF",
            "subtopic": "adf_advanced_therapy",
            "content": "Inotropes (dobutamine, milrinone) increase contractility but risk tachycardia, ischemia, arrhythmia. Indication: HF with reduced cardiac output (SBP <90, signs of hypoperfusion), refractory to diuretics + vasodilators. Dobutamine = beta agonist, increases contractility + HR, mild vasodilation. Dose 2-20 mcg/kg/min. Milrinone = phosphodiesterase-3 inhibitor, inotrope + systemic vasodilator. Dose 0.25-0.75 mcg/kg/min. Both: TEMPORARY bridge only (days, not weeks). Monitor: ECG for ischemic changes, troponin for MI. Wean as cardiac output improves. Limited evidence for mortality benefit; may worsen outcomes if used long-term.",
            "tags": ["heart_failure", "adf", "inotropes"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "BiPAP/CPAP in Cardiogenic Pulmonary Edema",
            "subtopic": "adf_respiratory_support",
            "content": "Non-invasive positive pressure ventilation (NIPPV): bilevel positive airway pressure (BiPAP) or continuous PAP (CPAP) improves oxygenation in acute cardiogenic pulmonary edema by splinting open alveoli + reducing afterload. BiPAP: two pressure levels (IPAP/EPAP); patient cycles between (more comfortable). CPAP: single pressure level (simpler). Typical settings: CPAP 5-10 cmH2O OR BiPAP IPAP 12-20, EPAP 5 cmH2O. Benefit: reduces intubation rate (meta-analysis: ~50% reduction) + ICU stay. Avoid if: altered mental status, aspiration risk, hemodynamic instability. Contraindication: acute MI (may worsen ischemia by reducing preload). Prognosis: NIPPV allows time for IV medications to work.",
            "tags": ["heart_failure", "adf", "bipap", "cpap"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Mechanical Circulatory Support in Acute HF",
            "subtopic": "adf_advanced_therapy",
            "content": "For cardiogenic shock refractory to medications: (1) Intra-aortic balloon pump (IABP): increases diastolic pressure (improves coronary perfusion), reduces afterload. Percutaneous via femoral artery; requires vascular surgery. Bridge to PCI/transplant. (2) Impella: axial flow pump (left ventricle → aorta), improves cardiac output more effectively than IABP. Newer, more invasive. (3) TandemHeart: extracorporeal centrifugal pump (left atrium → aorta). (4) ECMO: for combined cardiorespiratory failure, bridge to recovery/transplant. Indication: SBP <90 despite maximum medical therapy, signs tissue hypoperfusion (lactate, altered MS, oliguria). Role: bridge device (days-weeks), not definitive. Mortality high even with support; transplant evaluation necessary.",
            "tags": ["heart_failure", "adf", "mechanical_support"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Cardiogenic Shock - Definition & Management",
            "subtopic": "adf_cardiogenic_shock",
            "content": "Cardiogenic shock = low cardiac output state (MAP <65 mmHg OR SBP <90) despite adequate or elevated filling pressures, causing end-organ dysfunction (oliguria, altered MS, elevated lactate). Etiologies: acute MI, acute decompensation HF, myocarditis, stress cardiomyopathy. Presentation: hypotension, cool/clammy extremities, low urine output, altered mental status, elevated lactate. Diagnosis: CVP/PAOP >15 (elevated filling pressure), CI <2.2 L/min/m2 (low cardiac index). Management: (1) IV vasodilators + diuretics cautiously (high risk worsening hypotension); (2) Inotropes (dobutamine, milrinone) + vasopressors (norepinephrine); (3) Mechanical support (IABAP, Impella, ECMO) if refractory. PCI/revascularization if ACS underlying. Mortality 50%+ without mechanical support.",
            "tags": ["heart_failure", "adf", "cardiogenic_shock"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_hypertensive_crisis_units():
    """Generate hypertensive crisis & emergency units."""
    units = [
        {
            "topic": "Hypertensive Urgency vs Emergency Distinction",
            "subtopic": "hypertensive_crisis",
            "content": "Hypertensive urgency: markedly elevated BP (SBP ≥180 OR DBP ≥120) WITHOUT acute end-organ damage. Hypertensive emergency: SBP ≥180 AND DBP ≥120 WITH acute end-organ manifestations (stroke, MI, encephalopathy, pulmonary edema, eclampsia, acute aortic dissection, AKI). Urgency can be managed with oral agents; emergency requires IV medications + hospitalization. Pseudohypertension risk: white coat effect, take manual cuff reading to confirm. Up to 30% presenting with extreme BP have no true emergency (normal organs/labs).",
            "tags": ["hypertension", "hypertensive_crisis", "emergency_urgency"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hypertensive Encephalopathy - Recognition & Pathophysiology",
            "subtopic": "hypertensive_emergency",
            "content": "Hypertensive encephalopathy = severe HTN (>180/120) + reversible neurologic dysfunction (headache, confusion, visual disturbance, seizure, coma). Pathophysiology: loss of cerebral autoregulation → breakthrough capillary perfusion injury, vasogenic edema, microinfarcts. Imaging: PRES (Posterior Reversible Encephalopathy Syndrome) on MRI = white matter edema in parietal/occipital regions (often bilateral, symmetric). EEG: generalized slowing, sometimes epileptiform activity. Distinguishing from stroke: encephalopathy is reversible with BP control; stroke causes permanent infarction. Management: IV agents (labetalol, nicardipine), cautious BP reduction (lower by 10-15% first hour) to avoid stroke.",
            "tags": ["hypertension", "hypertensive_emergency", "encephalopathy", "pres"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Ischemic Stroke & Hypertensive Emergency Management",
            "subtopic": "hypertensive_emergency_scenarios",
            "content": "Acute ischemic stroke with severe HTN: critical decision on BP management. Thrombolysis/thrombectomy candidates: control BP to SBP <185, DBP <110 BEFORE intervention (high BP increases hemorrhage risk). After thrombolysis: target SBP <180 (to avoid intracerebral hemorrhage). IV agents: labetalol, nicardipine preferred (gradual, titratable). Avoid nitroprusside (causes intracranial steal in ischemic tissue). If patient not thrombolysis candidate: modest BP reduction acceptable (lower by 10-15% first hour). Overly aggressive treatment worsens ischemic stroke (reduces perfusion pressure). Close neuro checks q15min, troponin, ECG (MI risk).",
            "tags": ["hypertension", "hypertensive_emergency", "stroke"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Intracerebral Hemorrhage & Hypertension Management",
            "subtopic": "hypertensive_emergency_scenarios",
            "content": "Intracerebral hemorrhage (ICH) + severe HTN: aggressive BP control reduces hematoma expansion risk. Target: SBP <140 mmHg (INTERACT2 trial: intensive SBP <140 reduced hematoma expansion vs SBP <180). IV agents: labetalol 10-20 mg IV q10-20 min, nicardipine 5-15 mg/h infusion. Avoid: nitroprusside (increases intracranial pressure), hydralazine (unpredictable BP reduction). Supportive: ICU monitoring, coagulation reversal if on warfarin (INR >1.4 reversal recommended), neurosurgery consult for evacuation if large/accessible ICH. Mortality high (30-50%); rapid treatment critical.",
            "tags": ["hypertension", "hypertensive_emergency", "ich"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Aortic Dissection - Diagnosis & Urgent BP Control",
            "subtopic": "hypertensive_emergency_scenarios",
            "content": "Aortic dissection = tear in aortic media, can extend distally causing branch vessel involvement. Presentation: sudden severe chest/back pain, BP differential between arms (>20 mmHg suggests dissection), focal neurologic deficit (carotid involvement). Diagnosis: CT angiography (gold standard), TEE if CT unavailable, MRI (slower). Management: aggressive BP + HR reduction (target SBP 100-120, HR 60). Agents: (1) Beta-blocker FIRST (esmolol IV, target HR 60) to reduce dP/dt (contractility); (2) Then vasodilator if BP still high (nitroprusside, nicardipine). Labetalol alone inadequate (beta effect too weak without pre-blockade). Type A dissection (ascending aorta) = emergency surgery. Type B (descending aorta) = medical management if uncomplicated.",
            "tags": ["hypertension", "hypertensive_emergency", "aortic_dissection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Eclampsia & Pre-eclampsia - Hypertension in Pregnancy",
            "subtopic": "hypertensive_emergency_scenarios",
            "content": "Pre-eclampsia: HTN (BP ≥140/90 twice, 4h apart) after 20 weeks gestation + proteinuria ≥0.3 g/day OR signs end-organ dysfunction (elevated transaminases, thrombocytopenia, renal insufficiency, pulmonary edema, cerebral/visual symptoms). Eclampsia = pre-eclampsia + seizures. Management: (1) Delivery (definitive treatment); (2) Seizure prophylaxis: magnesium sulfate 4-6 g IV loading, then 1-2 g/h infusion (decreases seizure risk 50%); (3) BP control: goal SBP 140-150 (avoid overly aggressive, preserve placental perfusion). IV agents: labetalol, hydralazine, nifedipine. Avoid ACE inhibitors (teratogenic). HELLP syndrome (hemolysis, elevated LFTs, low platelets) = severe pre-eclampsia variant with higher mortality.",
            "tags": ["hypertension", "hypertensive_emergency", "eclampsia", "pregnancy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "IV Antihypertensive Agents - Pharmacology & Dosing",
            "subtopic": "hypertensive_emergency_treatment",
            "content": "(1) Labetalol: combined alpha/beta blockade. IV bolus 10-20 mg, repeat q10-20 min (max 300 mg), OR infusion 1-2 mg/min titrated. Onset 5-10 min, duration 2-4h. (2) Nicardipine: calcium channel blocker. Infusion 5-15 mg/h, titrate q5-15 min. Onset 15-30 min, duration 30 min post-infusion. (3) Hydralazine: direct arterial vasodilator. IV bolus 5-20 mg q30 min, onset 10-20 min. (4) Esmolol: short-acting beta blocker. IV bolus 80-500 mcg/kg, then infusion 50-300 mcg/kg/min. (5) Nitroprusside: potent balanced vasodilator. IV infusion 0.3-10 mcg/kg/min, AVOID >4 mcg/kg/min >4h (cyanide toxicity). (6) Immediate-release nifedipine: oral sublingual 10-20 mg, unpredictable absorption, outdated.",
            "tags": ["hypertension", "hypertensive_emergency", "iv_agents"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Target BP Reduction in Hypertensive Emergency",
            "subtopic": "hypertensive_emergency_treatment",
            "content": "Principle: cautious reduction to avoid stroke/MI. Goal: reduce MAP by 10-15% in first hour, then slower titration. Exception: acute pulmonary edema (more aggressive reduction acceptable). Exceptions requiring careful reduction: acute ischemic stroke (avoid <180/110 before thrombolysis, then <180 after), acute MI (avoid excessive reduction), aortic dissection (require beta-blockade first, then reduction to SBP 100-120). Monitor: BP q5-15 min initially, cardiac symptoms, neurologic status, urine output, renal function. Avoid: rapid SBP drop >20-30 mmHg (risk AKI, stroke, MI).",
            "tags": ["hypertension", "hypertensive_emergency", "target_reduction"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Catecholamine Excess Hypertensive Emergency",
            "subtopic": "hypertensive_emergency_scenarios",
            "content": "Pheochromocytoma: catecholamine-secreting adrenal tumor, presents with severe HTN + paroxysmal symptoms (headache, diaphoresis, palpitations, anxiety). Diagnosis: elevated plasma metanephrines/24h urine catecholamines. Acute presentation (pheochromocytoma crisis): severe HTN + altered MS, pulmonary edema, arrhythmia. Management: (1) Alpha-blockade FIRST: phentolamine IV 5 mg bolus, repeat q5-15 min (prevents catecholamine surge from surgical manipulation); then phenoxybenzamine oral 10-20 mg TID (blocks alpha receptors). (2) Beta-blockade (after alpha blockade established): propranolol, esmolol. (3) Supportive: sedation, cooling if hyperthermic. Surgery (adrenalectomy) when stabilized. Cocaine/amphetamine toxicity: similar presentation; avoid beta-blockers alone (unopposed alpha effects); use alpha-blocker + beta-blocker.",
            "tags": ["hypertension", "hypertensive_emergency", "catecholamine", "pheochromocytoma"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_dic_units():
    """Generate DIC knowledge units."""
    units = [
        {
            "topic": "DIC (Disseminated Intravascular Coagulation) Definition",
            "subtopic": "dic_definition",
            "content": "DIC = acquired syndrome of uncontrolled thrombin generation + consumption of platelets + clotting factors + secondary fibrinolysis. Pathophysiology: tissue factor release (from damaged endothelium, tumor, placenta) activates extrinsic pathway → massive thrombin generation → fibrin deposition in microvasculature (thrombosis, organ ischemia) + simultaneous consumption of platelets/fibrinogen/factors II, V, VIII, X (bleeding risk). Presentation: bleeding from multiple sites (mucous membranes, skin, surgical sites) + thrombosis (DVT, PE, microvascular occlusion) + organ dysfunction (AKI, ARDS, encephalopathy). Mortality 40-50% depending on underlying cause.",
            "tags": ["dic", "definition", "coagulopathy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "DIC Triggers & Common Etiologies",
            "subtopic": "dic_etiology",
            "content": "Obstetric: placental abruption, amniotic fluid embolism (most common DIC precipitants). Sepsis: especially Gram-negative/meningococcal (tissue factor release from endotoxin). Acute leukemia: release of procoagulant from blasts. Massive trauma: tissue factor from damaged tissues. Heat stroke: endothelial injury. Transfusion reactions: complement activation. Malignancy: lung, prostate, breast cancers produce tissue factor. Venom (snake, insect): direct proteolytic activation. Severe liver disease: loss of natural anticoagulants.",
            "tags": ["dic", "etiology", "triggers"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "DIC Laboratory Findings & Diagnosis",
            "subtopic": "dic_diagnostics",
            "content": "Classic findings: (1) Thrombocytopenia (decreased platelet consumption); (2) Elevated PT/INR & aPTT (factor consumption); (3) Hypofibrinogenemia (<100 mg/dL, normal 200-400); (4) Elevated d-dimer & FDP (fibrin degradation products, elevated 100-1000x normal); (5) Schistocytes on blood smear (microangiopathic hemolytic anemia from fibrin strands). ISTH DIC scoring: platelets + PT prolongation + fibrinogen level + d-dimer/FDP (score ≥5 compatible with overt DIC). No single test diagnostic; combination + clinical context essential. Serial measurements more useful than single values (declining platelets, declining fibrinogen = worsening DIC).",
            "tags": ["dic", "diagnostics", "labs"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "DIC Differential Diagnosis - Mimics",
            "subtopic": "dic_diagnostics",
            "content": "Conditions mimicking DIC: (1) Thrombotic thrombocytopenic purpura (TTP): severe thrombocytopenia + microangiopathic hemolysis + neurologic symptoms + fever; normal PT/INR/fibrinogen (unlike DIC); treated with plasma exchange NOT transfusions; (2) Hemolytic-uremic syndrome (HUS): similar to TTP, more renal involvement; (3) Severe sepsis without DIC: elevated d-dimer, normal/only mildly low platelets, normal PT/fibrinogen; (4) Liver disease: elevated PT/INR, low fibrinogen, but INCREASED platelets (unlike DIC). Key distinction: DIC = multi-system coagulopathy, HIT/TTP/HUS more isolated hematologic.",
            "tags": ["dic", "diagnostics", "differential"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "DIC Management - Treat Underlying Cause First",
            "subtopic": "dic_treatment",
            "content": "MOST IMPORTANT: address precipitant. Placental abruption → urgent delivery. Sepsis → antibiotics + source control. Acute leukemia → chemotherapy. Transfusion reaction → stop transfusion. Supportive care: platelet transfusion if <10k or <20k + invasive procedure (target 10-20k for maintenance). Fresh frozen plasma (FFP) replaces multiple factors; dose 10-15 mL/kg q6-12h as needed. Cryoprecipitate (fibrinogen replacement): 10 units if fibrinogen <100, repeat until >100. Avoid over-transfusion (volume overload, worsens microvascular thrombosis). Monitor: CBC, PT/aPTT, fibrinogen q6-12h; titrate transfusions to values not labs.",
            "tags": ["dic", "treatment", "supportive_care"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Heparin & Anticoagulation in DIC - Controversial",
            "subtopic": "dic_treatment",
            "content": "Role of heparin in DIC remains debated. Theoretical benefit: heparin blocks thrombin generation, may preserve natural anticoagulants. Practical problems: increased bleeding risk (especially if fibrinogen <100), no RCT evidence of benefit, expense. Current consensus: heparin NOT recommended for routine DIC. Exception: thrombotic DIC (manifesting more with thrombosis than bleeding, e.g., arterial thrombosis, mesenteric infarction) + failing other measures → consider heparin cautiously. Use: unfractionated heparin 80 units/kg bolus, then 18 units/kg/h infusion, target aPTT 1.5-2.5x normal. Monitor: aPTT, fibrinogen, platelet count closely.",
            "tags": ["dic", "treatment", "anticoagulation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Antifibrinolytic Therapy in DIC",
            "subtopic": "dic_treatment",
            "content": "Tranexamic acid (TXA, Cyklokapron): plasmin inhibitor, prevents fibrin breakdown. Dose: 1 g IV q6-8h (max 5 g/day), or 10-15 mg/kg IV bolus. Use: DIC with predominantly bleeding phenotype (vs. thrombotic). Evidence: limited; may reduce bleeding transfusion requirement. Risk: thrombotic complications (increased thrombosis if used in thrombotic DIC). Epsilon-aminocaproic acid (EACA): similar agent, less commonly used. Current recommendation: antifibrinolytics reserved for bleeding refractory to transfusion, with careful monitoring.",
            "tags": ["dic", "treatment", "antifibrinolytic"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Natural Anticoagulants in DIC - Research Phase",
            "subtopic": "dic_treatment",
            "content": "Protein C: naturally occurring anticoagulant, severely depleted in DIC. Activated protein C (drotrecogin, Xigris) showed promise in sepsis-related DIC (PROWESS trial), but later shown to increase bleeding without mortality benefit; withdrawn from market. Antithrombin: naturally occurring inhibitor, depleted in DIC; replacement studied, no clear benefit. Future agents: tissue factor pathway inhibitor, thrombin-activatable fibrinolysis inhibitor (TAFI) still in research. Current practice: supportive transfusion management remains standard pending better biomarker-driven therapies.",
            "tags": ["dic", "treatment", "natural_anticoagulants", "research"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Chronic DIC vs Acute DIC",
            "subtopic": "dic_variants",
            "content": "Acute DIC: fulminant presentation, rapid platelet decline, profound hypofibrinogenemia, high mortality. Chronic DIC: indolent, compensated, seen in malignancy (especially lung cancer), retained dead fetus syndrome. Chronic DIC: mildly low platelets (usually >50k), elevated d-dimer with normal/near-normal PT/fibrinogen (compensation by liver synthesis). May be asymptomatic (found on routine labs). Risk: acute transformation if trigger escalates. Management chronic DIC: treat underlying cancer, avoid unnecessary treatments if asymptomatic.",
            "tags": ["dic", "variants", "chronic"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_liver_failure_units():
    """Generate acute liver failure & hepatic encephalopathy units."""
    units = [
        {
            "topic": "Acute Liver Failure (ALF) Definition & Etiology",
            "subtopic": "alf_definition",
            "content": "Acute liver failure = severe hepatic dysfunction (INR ≥1.5 from any cause) + hepatic encephalopathy + illness <26 weeks duration + no pre-existing cirrhosis. Fulminant hepatic failure = encephalopathy grade III-IV. Leading etiologies: (1) Acetaminophen overdose (~50% in US); (2) Viral hepatitis (A, B, E); (3) Autoimmune hepatitis; (4) Drug-induced (INH, NSAIDs, chemotherapy); (5) Toxins (Amanita mushrooms, Wilson's disease); (6) Hyperthermia, shock, massive PE. Hyperacute (<7 days): acetaminophen toxicity (coma common, DIC, renal failure, cerebral edema). Acute (7-21 days): viral, drug-induced (encephalopathy less common early). Subacute (21-26 weeks): autoimmune, drug-induced (insidious presentation). Prognosis: 80% mortality without transplant; 60% with transplant.",
            "tags": ["liver_failure", "alf", "acute", "etiology"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hepatic Encephalopathy - Pathophysiology & Grading",
            "subtopic": "hepatic_encephalopathy",
            "content": "Hepatic encephalopathy (HE) = reversible neuropsychiatric syndrome in liver failure. Pathophysiology: accumulation of neurotoxic substances (ammonia, manganese, false neurotransmitters, endogenous benzodiazepines) due to impaired liver clearance + shunting of portal blood away from liver. Grading: Grade I (subtle: personality change, sleep inversion); Grade II (inappropriate behavior, lethargy, confusion); Grade III (incoherent speech, somnolence); Grade IV (coma, unresponsive to pain). Asterixis = flapping tremor (classic but not required). Risk factors: infection (SBP, UTI, pneumonia), renal failure, electrolyte abnormalities (hypokalemia worsens ammonia production), GI bleeding, sedative overdose. Grade III-IV = medical emergency requiring ICU.",
            "tags": ["liver_failure", "encephalopathy", "grading"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Cerebral Edema in Acute Liver Failure",
            "subtopic": "liver_failure_complications",
            "content": "Cerebral edema = major cause of death in ALF (present in ~80% of Grade III-IV encephalopathy). Mechanism: osmotic shift (hyperammonemia draws fluid into neurons), increased intracranial blood volume, impaired autoregulation. Presentation: headache, hypertension, bradycardia, respiratory depression (Cushing's triad = late sign), seizures, posturing, brain death. Diagnosis: CT (not sensitive early; edema becomes evident with brain swelling), ICP monitoring (intracranial pressure >20 mmHg abnormal). Prevention/management: (1) Head of bed 30°, neck neutral, avoid hypoxia/hypercarbia; (2) Osmotic therapy (mannitol 20% 0.5-1 g/kg IV, hypertonic saline 3% 30 mL bolus); (3) Sedation (propofol, minimize CMRO2); (4) Tight glucose control (avoid both hypo/hyperglycemia); (5) Therapeutic hypothermia (33-35°C) in some centers, controversial; (6) Transplant urgency increases with Grade III-IV.",
            "tags": ["liver_failure", "cerebral_edema", "complications"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Coagulopathy in Acute Liver Failure",
            "subtopic": "liver_failure_complications",
            "content": "ALF causes severe coagulopathy: ↓synthesis of all clotting factors (except factor VIII, produced extrahepatically), ↓synthesis of natural anticoagulants (protein C, S, antithrombin). INR >1.5 is diagnostic criterion. Platelet dysfunction + thrombocytopenia may occur. Bleeding risk HIGH, especially GI hemorrhage, epidural hematoma (if ICP monitoring). Management: (1) AVOID routine correction with FFP unless active bleeding or before invasive procedure (FFP causes volume overload, worsens cerebral edema); (2) Platelets if <50k + bleeding/procedure; (3) Vitamin K 10 mg IV (rarely helpful if INR >3, but try anyway); (4) Cryoprecipitate if fibrinogen <100. Monitor: PT/INR, platelets, fibrinogen daily. Risk of thrombotic events (paradoxically, low anticoagulants can cause microvascular thrombosis).",
            "tags": ["liver_failure", "coagulopathy", "bleeding"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Metabolic Complications in Acute Liver Failure",
            "subtopic": "liver_failure_complications",
            "content": "Hypoglycemia: impaired gluconeogenesis, glycogen depletion. Frequent monitoring (q1-4h), aggressive correction (dextrose boluses, continuous infusions). Hyperammonemia: impaired urea cycle, contributes to encephalopathy. Check serum ammonia; >200 μmol/L associated with Grade III-IV encephalopathy. Lactulose + rifaxomicin lower ammonia. Lactic acidosis: from shock, anaerobic metabolism. Monitor arterial pH/lactate. Hypokalemia: enhanced renal excretion, alkalosis. Aggressive replacement needed (target K >3.5). Hyponatremia: dilutional from fluid retention, SIADH-like. Correct slowly (hypertonic saline if symptomatic seizures). Hypophosphatemia, hypomagnesemia: monitor + replace.",
            "tags": ["liver_failure", "metabolic", "complications"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Infection Prevention & Treatment in ALF",
            "subtopic": "liver_failure_complications",
            "content": "Infection occurs in 80% of ALF hospitalization (bacterial, fungal, viral). Risk: immunosuppression from liver failure, invasive lines, aspiration. Common: bacteremia (spontaneous, line-related), SBP (if ascites), UTI, pneumonia, fungal sepsis (Candida, Aspergillus). Prophylaxis: selective intestinal decontamination (SID) with fluoroquinolone ± antifungal (fluconazole) in Grade III-IV. Empiric treatment: broad-spectrum antibiotics (cefepime, meropenem) + vancomycin (adjust for renal function). Antifungal (fluconazole or caspofungin) if prolonged ICU stay, persistent fever, repeated broad-spectrum antibiotic use. Cultures (blood, urine, ascitic fluid if ascites) before antibiotics. Prognosis: infection presence increases mortality; early aggressive treatment critical.",
            "tags": ["liver_failure", "infection", "prophylaxis"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hepatorenal Syndrome & AKI in Acute Liver Failure",
            "subtopic": "liver_failure_complications",
            "content": "Hepatorenal syndrome (HRS): functional renal failure in advanced liver disease (splanchnic vasodilation → systemic hypotension → renal vasoconstriction). Type 1 HRS: rapid renal failure (SCr doubles to >2.5 in <2 weeks), high mortality. Type 2 HRS: gradual, associated with refractory ascites. ALF can cause acute tubular necrosis (true structural kidney damage) or HRS-like functional failure. Diagnosis: serum creatinine rise + oliguria + low urinary Na (<10), normal urine sediment. Management: aggressive fluid resuscitation (risk fluid overload in ALF with ascites), vasoconstrictors (norepinephrine, terlipressin — vasopressin analog), albumin infusion. RRT indication: K >6, pH <7.15, pulmonary edema refractory to diuretics, or symptomatic uremia. Prognosis: HRS + ALF = very high mortality (>80%).",
            "tags": ["liver_failure", "hepatorenal_syndrome", "aki"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Liver Transplantation for Acute Liver Failure",
            "subtopic": "liver_failure_treatment",
            "content": "Urgent transplantation = only definitive treatment for fulminant ALF. Transplant evaluation: determine urgency, identify transplant candidates (exclude active infection/malignancy/irreversible brain injury). King's College criteria (prognostic model for transplant need): acetaminophen OD with INR >6.5 OR non-acetaminophen ALF with any 3 of: age >40, INR >6.5, bilirubin >18, PT >100 (or >7 days). Listing: status 1A (highest priority, medical urgency) or 1B. Pre-transplant: maximize medical management (lactulose, N-acetylcysteine for acetaminophen toxicity, infection prophylaxis, cerebral edema prevention), ICP monitoring consideration, continuous review for transplant contraindications. Outcomes: ~75% 1-year survival post-transplant (excellent for urgent indication). Timing: delay transplant assessment = worsening odds; early referral critical.",
            "tags": ["liver_failure", "transplantation", "treatment"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "N-Acetylcysteine in Acetaminophen-Induced ALF",
            "subtopic": "liver_failure_treatment",
            "content": "Acetaminophen (Tylenol) toxicity = leading cause ALF in US. Overdose depletes hepatic glutathione, allowing toxic metabolite (NAPQI) to accumulate → hepatocyte necrosis. N-acetylcysteine (NAC): replenishes glutathione, supports cellular antioxidant defenses. Dosing: loading 150 mg/kg IV over 1h (typical 11.25 g for 75 kg), then 50 mg/kg over 4h, then 100 mg/kg over 16h (or high-dose continuous 300 mg/kg over 20h). Efficacy: most benefit if given within 8-12h of overdose (taurine NAC can be effective even later). Benefit: NAC improves survival from 25% → 40% if transplant not available. Also indicated for acetaminophen levels >200 μg/mL at 4h post-ingestion (use Rumack-Matthew nomogram). Side effects: flushing, nausea, rare anaphylaxis (slow infusion reduces risk).",
            "tags": ["liver_failure", "acetaminophen", "nac"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Lactulose & Rifaxomicin for Hepatic Encephalopathy",
            "subtopic": "liver_failure_treatment",
            "content": "Lactulose: non-absorbable disaccharide, fermented by colonic bacteria → lactic acid, lowers colonic pH (prevents ammonia absorption), osmotic effect (diarrhea). Dose: start 15-30 mL PO q6-8h, titrate to 2-3 loose stools/day. Risk: severe diarrhea → dehydration. Rifaxomicin: non-absorbed antibiotic, alters gut flora (reduces ammonia-producing bacteria). Dose: 550 mg PO BID. Evidence: equivalent efficacy to lactulose, fewer side effects. Both agents: slow onset (days), not for acute encephalopathy treatment. Branched-chain amino acids (BCAA): theoretical benefit (compete with aromatic amino acids), no strong evidence. Zinc supplementation: some benefit in chronic HE, less data for acute ALF. Combination therapy (lactulose + rifaxomicin) sometimes used.",
            "tags": ["liver_failure", "encephalopathy", "treatment"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_pancreatitis_units():
    """Generate acute pancreatitis units."""
    units = [
        {
            "topic": "Acute Pancreatitis Definition & Diagnosis",
            "subtopic": "pancreatitis_definition",
            "content": "Acute pancreatitis = inflammation triggered by premature enzyme activation in pancreas. Diagnostic criteria: ≥2 of 3: (1) Abdominal pain consistent with pancreatitis (epigastric, radiating to back); (2) Serum amylase or lipase >3x ULN; (3) Characteristic imaging (CT, MRI, ultrasound). Amylase rises within 6-12h, peaks 48-72h, returns to normal 3-5 days. Lipase more specific, peaks 2-4 days. Lipase elevation lasts longer (up to 2 weeks). Serum levels correlate poorly with severity; normal lipase at 1 week doesn't rule out pancreatitis.",
            "tags": ["pancreatitis", "acute", "diagnosis"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Pancreatitis Etiology",
            "subtopic": "pancreatitis_etiology",
            "content": "Gallstones: 40-50% (obstruct ampulla, increase intraductal pressure). Alcohol: 35-45% (direct toxicity, ductal plugging). Hypertriglyceridemia (>1500 mg/dL): 1-5%. Post-ERCP: 5-10% (iatrogenic trauma). Medications (corticosteroids, azathioprine, sulfonamides, valproate, didanosine, pentamidine). Metabolic (hypercalcemia, hyperparathyroidism). Infectious (mumps, CMV, EBV, HBV, HIV). Autoimmune pancreatitis. Anatomic (divisum, annular pancreas, sphincter of Oddi dysfunction). Trauma. Idiopathic: 10-15%. In each patient, identify precipitant (guides prevention).",
            "tags": ["pancreatitis", "etiology"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Severity Assessment in Acute Pancreatitis",
            "subtopic": "pancreatitis_severity",
            "content": "Mild pancreatitis: uncomplicated, isolated inflammation, mortality <1%. Moderate pancreatitis: SIRS present, no organ failure, mortality 1-5%. Severe pancreatitis: organ failure present (respiratory, cardiovascular, renal, other), mortality 10-30%. Scoring systems: (1) APACHE II: complex, many variables, score >8 = severe; (2) SIRS criteria ≥2: temperature, HR >90, RR >20, WBC abnormal; (3) Ranson criteria: 11 variables at presentation + 48h (mortality correlates with number met, 0-2 criteria = 1%, 6+ criteria = 40%). CT severity index (Balthazar grade + extent of necrosis) better for prognosis than enzyme levels. Modified Marshall Score: tracks organ failure during ICU stay.",
            "tags": ["pancreatitis", "severity_assessment"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Pancreatitis Imaging - CT, Ultrasound, MRCP",
            "subtopic": "pancreatitis_imaging",
            "content": "Ultrasound: initial test (bedside, non-invasive), assess for gallstones, dilated ducts, free fluid. Not sensitive for parenchymal edema. CT (contrast-enhanced): gold standard for diagnosis + severity assessment. Shows pancreatic edema (swollen but normal enhancement = edema), necrosis (non-enhancing areas), fluid collections, ascites. Balthazar grades A (normal) to E (gas/extensive necrosis). MRCP: excellent for visualizing ductal system, identifying stone impaction, diagnosing autoimmune pancreatitis (duct beading). EUS: visualizes ampulla, stones <5 mm, tissue sampling. Timing: CT best delayed 72-96h (better shows necrosis). Early CT may underestimate necrosis.",
            "tags": ["pancreatitis", "imaging", "ct", "ultrasound"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Pancreatitis Management - NPO, Fluids, Nutrition",
            "subtopic": "pancreatitis_treatment",
            "content": "Early phase: (1) NPO (nil per os); (2) IV fluid resuscitation (aggressive early, 1-2 L/h LR aiming for urine output 0.5-1 mL/kg/h, avoid overload); (3) Monitor: pain, vital signs, O2 sat, urine output, labs (amylase, lipase, glucose, calcium, albumin). Feeding: early enteral nutrition (within 24-48h) better than TPN (reduced infectious complications, maintain gut integrity). Nasal duodenal feeding preferred if tolerating fluids; if not, TPN acceptable (higher infection risk though). Once amylase/lipase peak + pain improves, start low-fat diet, transition to oral. Avoid: anticholinergics (no benefit), protease inhibitors (no benefit), antacids routinely.",
            "tags": ["pancreatitis", "treatment", "nutrition"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Antibiotics in Acute Pancreatitis - Selective Use",
            "subtopic": "pancreatitis_treatment",
            "content": "Prophylactic antibiotics: controversial, generally NOT recommended for mild-moderate pancreatitis without signs infection. Indicated for: (1) Necrotic pancreatitis (Balthazar grade D-E or >30% necrosis); (2) Clinical signs infection (fever, elevated WBC, dysfunction persisting >5-7 days). Agents: penetrate pancreatic necrosis well (carbapenems like meropenem, fluoroquinolones like levofloxacin). Duration: 7-14 days. Infected pancreatic necrosis: diagnosis challenging (fever + necrosis on CT + elevated inflammatory markers); FNA-guided culture may help. If confirmed, prolonged antibiotics + drainage/debridement needed.",
            "tags": ["pancreatitis", "antibiotics", "infection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Complications of Acute Pancreatitis",
            "subtopic": "pancreatitis_complications",
            "content": "Local: pancreatic edema (swelling, usually resolves), necrosis (non-viable tissue, high infection risk), pseudocyst (encapsulated fluid, may need drainage if symptomatic/infected/compressing), abscess (bacterial infection of necrotic tissue, requires drainage ± antibiotics). Systemic: ARDS (from inflammation), AKI (hypotension, myoglobinuria), coagulopathy/DIC, hypocalcemia (saponification of fat, binds calcium), hyperglycemia (beta cell destruction), hepatic failure (rare). Infected necrosis: mortality 30-50% even with treatment. Complications mortality 30-50% vs mild <1%.",
            "tags": ["pancreatitis", "complications"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ERCP in Gallstone Pancreatitis with Obstruction",
            "subtopic": "pancreatitis_treatment",
            "content": "Gallstone pancreatitis: if uncomplicated (no cholangitis), observation often sufficient (stone passes spontaneously in 80%). Urgent ERCP (within 24-72h) indicated if: (1) Cholangitis signs (fever, RUQ pain, jaundice) — need stone extraction + sphincterotomy; (2) Persistent biliary obstruction (bilirubin >4, duct dilatation); (3) Severe pancreatitis thought due to large stone. ERCP carries 5-10% complication rate (pancreatitis, perforation, bleeding), so reserved for true indication. Timing: within 24h of symptom onset optimal for severe cholangitis. Mild pancreatitis + no obstruction: elective cholecystectomy after acute phase (prevents recurrent). High-risk surgical patients: temporary stent consideration instead of sphincterotomy.",
            "tags": ["pancreatitis", "ercp", "gallstone"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hypertriglyceridemia-Induced Pancreatitis",
            "subtopic": "pancreatitis_etiology",
            "content": "Triglyceride levels >1500 mg/dL risk pancreatitis (>5000 = very high risk). Etiologies: familial hypertriglyceridemia, secondary to diabetes, alcohol use, medications (estrogens, thiazolidinediones, protease inhibitors). Presentation: similar to other pancreatitis. Diagnosis: elevated triglycerides + amylase/lipase elevation + abdominal pain. Key difference: amylase may be falsely low (lipemia interferes with assay), so lipase more reliable. Treatment: (1) Acute phase: NPO, fluids, IV heparin (enhances lipoprotein lipase activity, lowers triglycerides faster), control diabetes; (2) Long-term: fibrates (fenofibrate, gemfibrozil), omega-3 fatty acids, statins, lifestyle modification. Plasmapheresis if triglycerides >1500 (removes triglyceride-rich particles, effective but costly).",
            "tags": ["pancreatitis", "hypertriglyceridemia"],
            "library": "intern_year_medicine"
        }
    ]
    return units

# Add more units for remaining modules (ICP, Status Epilepticus, Organ Dysfunction)
# Due to character limits, I'll consolidate remaining modules

def create_icp_units():
    """Intracranial hypertension & cerebral edema units."""
    units = [
        {
            "topic": "ICP Physiology - Monro-Kellie Doctrine",
            "subtopic": "icp_physiology",
            "content": "Cranium = rigid box containing: brain (80%), CSF (10%), blood (10%). Total volume fixed. Monro-Kellie doctrine: increase in one component must be compensated by decrease in another to maintain stable ICP. Normal ICP 5-15 mmHg. Pathology increases ICP: mass (hemorrhage, tumor, abscess), cerebral edema (cytotoxic, vasogenic), increased CSF (obstruction), increased venous pressure. Compensatory mechanisms: CSF displacement downward into spinal canal (limited), increased CSF absorption, reduced blood volume (cerebral vasoconstriction). Once compensation exhausted, small volume increase = large ICP rise (steep compliance curve).",
            "tags": ["icp", "physiology", "monro_kellie"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Causes of Elevated ICP",
            "subtopic": "icp_etiology",
            "content": "Mass effect: epidural/subdural hematoma, ICH, space-occupying lesion (tumor, abscess). Cerebral edema (cytotoxic: cell swelling from hypoxia/ischemia; vasogenic: capillary leak from inflammation/trauma). CSF obstruction: intraventricular hemorrhage, tumor, hydrocephalus. Venous congestion: impaired cerebral venous return (patient position, ventilation, mass effect compressing veins). Metabolic: hypoxia, hypercapnia (CO2 vasodilation), hyperthermia. Seizures: increased CMRO2, hyperemia. Traumatic brain injury. Subarachnoid hemorrhage. Ischemic stroke with brain swelling. Hypoxic-ischemic encephalopathy.",
            "tags": ["icp", "etiology"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Clinical Signs of Elevated ICP",
            "subtopic": "icp_presentation",
            "content": "Early signs: headache, vomiting (projectile, without nausea), drowsiness. Progressive: hypertension, bradycardia, respiratory changes (Cheyne-Stokes breathing, central neurogenic hyperventilation). Cushing's triad (late, ominous sign): hypertension + bradycardia + irregular respirations = brainstem compression. Pupil changes: ipsilateral pupil dilation (oculomotor nerve compression from uncal herniation), later bilateral dilation (brainstem involvement). Posturing: decorticate (arms flexed, legs extended = cerebral lesion) vs. decerebrate (all limbs extended = brainstem), both grave signs. Seizures common with increased ICP.",
            "tags": ["icp", "presentation", "signs"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Herniation Syndromes",
            "subtopic": "icp_complications",
            "content": "Uncal (transtentorial) herniation: superior temporal lobe herniates through tentorial notch. Presents: ipsilateral dilated pupil (oculomotor nerve CN III compression), contralateral weakness (cerebral peduncle compression). Central herniation: both hemispheres shift downward through foramen magnum. Presents: bilateral pupil dilation, loss of brainstem reflexes, death. Tonsillar herniation: cerebellar tonsils herniate into foramen magnum. Presents: neck stiffness (meningeal sign), apnea (respiratory center compression), rapid deterioration. All herniation syndromes medical emergencies requiring immediate intervention.",
            "tags": ["icp", "complications", "herniation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Cerebral Perfusion Pressure (CPP) & Autoregulation",
            "subtopic": "icp_physiology",
            "content": "CPP = MAP - ICP (normal ≥60-70 mmHg). Goal: maintain CPP >60 to ensure adequate brain perfusion. If ICP rises, need to increase MAP to maintain CPP. Cerebral autoregulation: normally, brain maintains constant cerebral blood flow across MAP range 50-150 mmHg (via vasoconstriction/dilation). Severe injury (TBI, stroke): autoregulation lost, CBF becomes pressure-dependent (low MAP = ischemia, high MAP = hyperemia/edema). Management: maintain MAP >65 (via vasopressors if needed) + control ICP (avoid hypotension which worsens outcome).",
            "tags": ["icp", "cpp", "autoregulation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ICP Monitoring - Intraventricular Catheter, Bolt, Epidural",
            "subtopic": "icp_monitoring",
            "content": "Intraventricular catheter (ventriculostomy, gold standard): small catheter inserted into lateral ventricle, connected to external ventricular drain (EVD). Advantage: most accurate ICP measurement, allows CSF drainage (therapeutic + diagnostic samples), allows intrathecal medication delivery. Complication: 5-10% ventriculitis, catheter malposition. Subarachnoid bolt: less invasive, but less accurate if blood/debris obstructs. Epidural sensor: non-invasive, placed under dura, good accuracy but can't drain CSF. No monitoring modality reduces mortality, but guides treatment decisions. Indications for ICP monitoring: GCS ≤8 (TBI, other causes), abnormal CT, age >40, motor deficits, hypotension episodes.",
            "tags": ["icp", "monitoring", "ventriculostomy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "First-Line ICP Management - Positioning, Oxygenation, Temperature",
            "subtopic": "icp_treatment",
            "content": "(1) Head of bed 30° (improves venous drainage, CSF absorption, reduces ICP); (2) Neck neutral (avoid compression of jugular veins); (3) Avoid hypoxia (SpO2 >94%, PaO2 >60); (4) Avoid hypercarbia (PaCO2 >45 causes vasodilation → increased ICP); mild hypocapnia acceptable (PaCO2 35-40, but excessive <30 risks ischemia); (5) Temperature: fever increases CMRO2 → worsens edema, maintain normothermia; therapeutic hypothermia (33-35°C) may help acute phase, controversial. (6) Sedation (propofol, midazolam) reduces CMRO2; avoid fentanyl alone (doesn't reduce CMRO2). (7) Avoid hyperthermia, maintain glucose 140-180.",
            "tags": ["icp", "treatment", "first_line"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Osmotic Therapy for Cerebral Edema",
            "subtopic": "icp_treatment",
            "content": "Mannitol 20%: osmotic diuretic, draws fluid from brain interstitium into vasculature, lowers ICP. Dose: 0.5-1 g/kg IV over 15-30 min, repeat q6-8h. Onset 20-30 min, duration 4-6h. Monitoring: osmolality (limit <320 mOsm/kg risk organ failure), renal function, serum Na. Complication: rebound increase in ICP if mannitol crosses disrupted BBB. Hypertonic saline (3%): sodium draws fluid osmotically. Dose: 30 mL bolus or 0.1-1 mL/kg/h infusion. Advantage: no renal side effects, may improve immune function. Both equally effective; choice often institutional. Avoid both agents if severe hyperchloremic acidosis. Limit osmolality <320.",
            "tags": ["icp", "osmotic_therapy"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Decompressive Craniectomy for Refractory ICP",
            "subtopic": "icp_treatment",
            "content": "Surgical removal of bone flap (frontal, parietal, or bifrontal) to allow brain swelling without ICP constraint. Indications: refractory elevated ICP (>20 mmHg despite medical management) in TBI, ischemic stroke, ICH if life-threatening herniation. Outcome: decreases mortality ~23% (study of TBI, DECRA trial), but increases severe disability (trading death for vegetative state in some). Timing: early (within 72h) may be beneficial. Complications: infection, CSF leak, need for cranioplasty later. Mortality reduction NOT proportional to improvement in outcome (paradox). Discussed as last resort when prognosis dire.",
            "tags": ["icp", "surgery", "decompressive_craniectomy"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_status_epilepticus_units():
    """Advanced status epilepticus units."""
    units = [
        {
            "topic": "Status Epilepticus Definitions",
            "subtopic": "status_definition",
            "content": "Convulsive status epilepticus (CSE): recurrent seizures without return to baseline (≥5 min continuously OR ≥2 seizures with incomplete recovery) = medical emergency. Non-convulsive status (NCS): altered mental status ± subtle motor signs, may appear comatose; harder to recognize without EEG. Refractory status: failure to stop after 2 adequate first + second-line agents. Super-refractory: persists despite anesthesia-level sedation (e.g., propofol, midazolam drip). Mortality: 10-15% overall, higher if refractory (30-50%), highest if super-refractory (>50%). Early recognition + treatment critical; each hour delay increases mortality.",
            "tags": ["status_epilepticus", "definition"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Etiologies of Status Epilepticus",
            "subtopic": "status_etiology",
            "content": "Non-adherence to anti-epileptic drugs (most common, 40-50%). Acute stroke (ischemic/hemorrhagic). Infection (meningitis, encephalitis). Metabolic (hypoglycemia, hyponatremia, hypocalcemia, uremia, hepatic encephalopathy). Drug withdrawal (alcohol, benzodiazepines). Trauma (head injury). Fever (febrile seizures <5y). Medications (stimulants, anesthetics withdrawal). Pregnancy/eclampsia. Idiopathic. In each case, identify + treat underlying cause (e.g., antibiotics for meningitis, glucose for hypoglycemia).",
            "tags": ["status_epilepticus", "etiology"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "First-Line Treatment - Benzodiazepines",
            "subtopic": "status_treatment",
            "content": "Goal: stop seizures within minutes. IV benzodiazepines most effective first-line: (1) Lorazepam (Ativan): 4 mg IV bolus, repeat q2-5 min (max 8 mg); onset <1 min, duration 30-60 min. (2) Midazolam IM: 10 mg IM (if no IV access), onset 5-10 min. (3) Diazepam (Valium): 5-10 mg IV q5-10 min (max 30 mg); older, longer-acting, less preferred. Lorazepam preferred (balanced onset/offset). Efficacy: 60-80% seizures stop within 5 min of lorazepam. Monitor: respiratory depression (may need intubation), hypotension. Have equipment/drugs ready for airway management.",
            "tags": ["status_epilepticus", "benzodiazepines"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Second-Line Antiepileptic Drugs (AEDs)",
            "subtopic": "status_treatment",
            "content": "If seizures persist >5 min after benzodiazepine: (1) Fosphenytoin (Cerebyx): 15-20 PE/kg IV (phenytoin equivalent) at 100-150 mg/min; onset 30-60 min, long half-life (24h). Loading: 20 PE/kg, then maintenance 5 mg/kg/day divided. Phenytoin (Dilantin): older formulation, IV irritating, slower replacement kinetics. (2) Levetiracetam (Keppra): 500-2000 mg IV q12h; onset 15-30 min, fewer drug interactions, well-tolerated. (3) Valproic acid: 20-40 mg/kg IV; onset 15-30 min, effective but risk hepatotoxicity (avoid in liver disease). (4) Lacosamide: 200 mg IV; limited experience. Any agent acceptable; no clear superiority. Combination (e.g., lorazepam + fosphenytoin + levetiracetam) sometimes used.",
            "tags": ["status_epilepticus", "aeds", "second_line"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Third-Line Treatment - Anesthetic Induction",
            "subtopic": "status_treatment",
            "content": "If seizures refractory after 2 adequate agents: induce anesthesia-level sedation. (1) Propofol: 1-2 mg/kg IV bolus, then 1-10 mg/kg/h infusion; onset <1 min, offset rapid upon cessation. Risk: propofol infusion syndrome (myopathy, hyperkalemia, metabolic acidosis, death) if high dose >4 mg/kg/h x >48h. (2) Midazolam: 0.1-0.2 mg/kg IV bolus, then 0.05-2 mg/kg/h infusion; offset slower. (3) Barbiturates (pentobarbital): loading 5-15 mg/kg, then maintenance; slow offset, risk hypotension. (4) Ketamine: 1-2 mg/kg IV bolus, then 0.5-2 mg/kg/h; preserves airway protective reflexes. Goal: burst suppression on EEG (bursts of activity separated by flat periods = maximal seizure suppression).",
            "tags": ["status_epilepticus", "anesthesia", "third_line"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Airway Management in Status Epilepticus",
            "subtopic": "status_airway",
            "content": "Rapid sequence intubation (RSI) indicated if: (1) Seizures ongoing (aspiration risk); (2) Altered mental status post-seizure; (3) Plan for anesthesia-level sedation. Medication sequence: (1) Pre-oxygenation (high-flow O2, target SpO2 >94%); (2) Induction agent (propofol, ketamine, etomidate depending on hemodynamics); (3) Paralytic (rocuronium, succinylcholine). Avoid thiopental (no longer available), phenytoin loading delays definitive treatment. Laryngoscopy: prepare for difficult airway (teeth clenching, tongue swelling post-seizure). Monitor: continuous pulse ox, ECG, capnography post-intubation. Confirm tube position (CXR after stabilized).",
            "tags": ["status_epilepticus", "airway"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Continuous EEG Monitoring in Status Epilepticus",
            "subtopic": "status_monitoring",
            "content": "Continuous EEG essential for monitoring non-convulsive status (silent on clinical exam), assessing treatment efficacy, detecting breakthrough seizures. EEG findings: repetitive spikes, sharp waves, polyspikes. Ictal pattern: >1 Hz generalized spike-wave activity. Post-ictal suppression: flattening after seizure. Burst suppression: bursts of activity separated by periods of electrical silence (target of deep sedation). Discontinue sedation: periodic sedation interruption q24h to assess neurologic status, check for seizure recurrence. Wean anesthesia once seizure-free for 12-24h, then re-titrate if seizures resume.",
            "tags": ["status_epilepticus", "eeg_monitoring"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Complications of Status Epilepticus",
            "subtopic": "status_complications",
            "content": "Metabolic: acidosis (lactic, metabolic), hyperkalemia (muscle breakdown), hyperthermia (neuronal activity heat). Cardiovascular: arrhythmias, MI risk. Rhabdomyolysis: muscle breakdown → myoglobinuria → AKI, hyperkalemia. DIC: from tissue factor release, trauma. Aspiration: from seizure activity, decreased consciousness. Sudden unexpected nocturnal death in epilepsy (SUDEP): rare (~1:1000 per year in epilepsy), mechanism unclear (autonomic dysrhythmia, apnea). Long-term: cognitive impairment, status post-ictal state (confusion, drowsiness). Monitor: CK (rhabdo), creatinine (AKI), K+, glucose, core temperature, troponin.",
            "tags": ["status_epilepticus", "complications"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Seizure Prophylaxis Post-Status Epilepticus",
            "subtopic": "status_maintenance",
            "content": "Establish long-term seizure control: identify + treat underlying cause (infection, metabolic abnormality, withdrawal). Initiate maintenance AED (if not already on one): levetiracetam 500 mg PO/IV BID (often preferred, fewer interactions), phenytoin loading 15-20 mg/kg then maintenance, valproate, etc. Drug level monitoring: phenytoin target 10-20 mcg/mL, valproate target 50-100 mcg/mL. Adjust dosing for renal/hepatic function, drug interactions. Duration: minimum 7-14 days ICU monitoring to assess seizure control, then step-down sedation. Discharge planning: neurology follow-up, medication adherence counseling, safety precautions (no driving until seizure-free per state law), lifestyle modifications.",
            "tags": ["status_epilepticus", "maintenance", "prophylaxis"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def create_organ_dysfunction_units():
    """Organ dysfunction syndromes (MOF, MODS, CIP, ICUAW) units."""
    units = [
        {
            "topic": "MOF/MODS Definition & SOFA Scoring",
            "subtopic": "mof_definition",
            "content": "Multiple organ failure (MOF) / Multiple organ dysfunction syndrome (MODS): dysfunction affecting ≥2 organ systems. SOFA (Sequential Organ Failure Assessment) score: tracks organ dysfunction over time, each organ 0-4 points (total 0-24). Organs: (1) Respiratory: PaO2/FiO2 ratio; (2) Coagulation: platelets; (3) Hepatic: bilirubin; (4) Cardiovascular: hypotension/vasopressor need; (5) Renal: creatinine/urine output; (6) CNS: GCS. SOFA ≥2 indicates sepsis (sepsis-3 definition). SOFA ≥11 predicts >40% hospital mortality. Prognostic value: increasing SOFA over 24-48h = worsening prognosis; improving SOFA = good sign.",
            "tags": ["mof", "mods", "sofa", "organ_failure"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Typical Sequence of Organ Failure in Critical Illness",
            "subtopic": "mof_sequence",
            "content": "Classic pattern (though variable): (1) Respiratory system first (ARDS, hypoxemia) — occurs in 30-50% of sepsis; (2) Cardiovascular (septic shock, hypotension) — 30-40%; (3) Renal (AKI, oliguria) — 30%; (4) Hepatic (hyperbilirubinemia, coagulopathy) — less common initially; (5) CNS (encephalopathy, ARDS-related hypoxemia). Coagulation failure (DIC) may appear early if sepsis source particularly high tissue factor (trauma, malignancy, placental). Mortality increases with organ count: 1 organ = 30%, 2 organs = 50%, 3+ organs = >80%. Early recognition + intervention per organ system critical to slow progression.",
            "tags": ["mof", "sequence"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Critical Illness Polyneuropathy (CIP) & Myopathy (CIM)",
            "subtopic": "icu_acquired_weakness",
            "content": "CIP: peripheral nerve damage from critical illness (sepsis, MODS), presents with distal > proximal leg weakness, difficulty weaning ventilator. CIM: skeletal muscle injury (myositis, denervation), presents with proximal weakness, high CK. ICUAW (ICU-acquired weakness): umbrella term. Incidence: 40-50% of ICU stays >7 days, especially sepsis/MODS. Risk factors: sepsis, hyperglycemia, immobility, corticosteroids, neuromuscular blockade, female sex. Diagnosis: clinical weakness + EMG/NCS (reduced CMAP voltage = CIP; myopathic changes = CIM), muscle biopsy if diagnosis unclear. Prognosis: variable, some recover weeks-months, others have residual dysfunction.",
            "tags": ["icuaw", "cip", "cim"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Prevention & Management of ICUAW",
            "subtopic": "icu_acquired_weakness",
            "content": "Prevention: (1) Early mobilization (passive ROM → sitting → standing → walking as tolerated); (2) Minimize sedation (RASS -1 to 0 preferred); (3) Tight glucose control (140-180 target, avoid hypoglycemia); (4) Minimize corticosteroids (avoid prolonged high-dose); (5) Avoid prolonged NMB (if used, monitor depth, wean quickly). Treatment: (1) Aggressive physical/occupational therapy; (2) Nutritional support (adequate protein, avoid underfeeding); (3) Rehabilitation (post-ICU recovery programs). Outcomes: 30-50% of ICUAW resolve within months, 30-50% have persistent weakness at 1 year. Monitoring: manual muscle testing (0-5 scale), handgrip dynamometry, 6-minute walk distance post-ICU discharge.",
            "tags": ["icuaw", "prevention", "rehabilitation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Sepsis-Induced Cardiomyopathy",
            "subtopic": "mof_cardiac",
            "content": "Transient myocardial depression in 20-40% of septic shock. Echo: reduced EF (often 20-35%), dilated LV, normal valves. Mechanism: cytokine-mediated (TNF-α, IL-1, IL-6 directly depress contractility), endotoxin, oxidative stress. Troponin often elevated (myocardial injury). BNP/NT-proBNP elevated. Recovery: EF normalizes in 7-10 days if patient survives (unlike acute MI). Management: adequate fluid resuscitation (goal LAV >65), vasopressors (norepinephrine preferred), inotropes (dobutamine, milrinone) if low CO persists despite adequate MAP. Outcome: sepsis-induced cardio better prognosis than acute MI (full recovery expected).",
            "tags": ["mof", "cardiomyopathy", "septic_shock"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Kidney Injury in Critical Illness",
            "subtopic": "mof_renal",
            "content": "AKI in ICU = increased creatinine >0.3 mg/dL or ≥50% rise, OR urine output <0.5 mL/kg/h x 6h. Etiologies: (1) Sepsis-induced (renal hypoperfusion, endotoxin); (2) Cardiogenic shock (reduced CO); (3) Medications (aminoglycosides, ACE-I during shock, NSAIDs); (4) Rhabdomyolysis (myoglobin precipitation in tubules); (5) Hepatorenal syndrome. Staging (KDIGO): Stage 1 (Cr 1.5-1.9x or UO 0.5-0.9 mL/kg/h x 6-12h) to Stage 3 (Cr ≥3x or UO <0.3 mL/kg/h x ≥24h). Management: optimize perfusion (fluids, vasopressors), avoid nephrotoxins, RRT indications (K >6, pH <7.15, fluid overload, Cr >4, uremia). Prognosis: 40-60% mortality if AKI in setting MODS; recovery variable (days to weeks).",
            "tags": ["mof", "aki", "renal_failure"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Gastrointestinal Dysfunction in Critical Illness",
            "subtopic": "mof_gi",
            "content": "GI complications: (1) Ileus (absent bowel sounds, abdominal distension, feeding intolerance) — from sepsis, opioids, electrolyte abnormalities; (2) Stress ulceration (mucosal erosion from ischemia, acidosis) → GI bleeding; (3) Ischemic colitis (mesenteric hypoperfusion, high mortality if transmural); (4) Clostridium difficile infection (antibiotic-associated); (5) Acalculous cholecystitis. Prevention: (1) Early enteral nutrition (maintain gut integrity); (2) PPI or H2-blocker prophylaxis for stress ulcer (especially if coagulopathy, steroids); (3) Bowel regimen (metoclopramide, lactulose, docusate); (4) Antibiotic stewardship. Treatment: NPO, NG tube if ileus, supportive care, surgery for perforation/ischemia.",
            "tags": ["mof", "gi_dysfunction"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hepatic Dysfunction in Critical Illness",
            "subtopic": "mof_hepatic",
            "content": "Ischemic hepatitis: transient hepatic dysfunction from shock (reduced hepatic perfusion), presents with elevated transaminases (AST often >2000), elevated bilirubin, coagulopathy. Usually recovers quickly once perfusion restored. Cholestasis: elevated bilirubin + alkaline phosphatase, from sepsis inflammation (prolonged ICU stay), parenteral nutrition. Drug-induced hepatotoxicity: acetaminophen, INH, NSAIDs. Management: maintain perfusion, discontinue offending agents, supportive care (transfuse platelets/FFP if coagulopathy). Monitoring: LFTs, bilirubin, INR, albumin. Most ICU hepatic dysfunction resolves; true hepatic failure rare (requires pre-existing cirrhosis + massive insult).",
            "tags": ["mof", "hepatic_dysfunction"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ICU-Acquired Infections (VAP, CLABSI, CAUTI)",
            "subtopic": "mof_infections",
            "content": "Ventilator-associated pneumonia (VAP): lower respiratory infection in intubated patients; risk factors prolonged ventilation, supine position, reintubation. Diagnosis: fever + new infiltrate + positive sputum culture (BAL thresholds ≥10^4). Central line-associated bloodstream infection (CLABSI): bloodstream infection related to CVC; prevention: chlorhexidine skin prep, aseptic technique, minimize line days. Catheter-associated UTI (CAUTI): bacteriuria from indwelling catheter; prevention: remove catheter ASAP, aseptic insertion. Management: appropriate antibiotics (culture-directed), source removal (line removal if CLABSI, catheter removal if CAUTI), supportive care. Prevention bundles (VAP, CLABSI, CAUTI) reduce infection rates 20-50%.",
            "tags": ["mof", "icu_infections", "prevention"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "ICU Delirium - CAM-ICU Screening & Management",
            "subtopic": "mof_delirium",
            "content": "Delirium: acute alteration in mental status, fluctuating, inattention ± disorganized thinking. Incidence: 20-80% of ICU patients. CAM-ICU screening (Confusion Assessment Method): (1) Acute onset + fluctuating, AND (2) Inattention, AND (3) Disorganized thinking OR altered consciousness = POSITIVE. Risk factors: sepsis, hypoxemia, medications (sedatives, opioids), immobility, sleep deprivation. Management: treat underlying cause (infection, metabolic abnormality, medication), minimize sedation, optimize sleep environment, early mobilization, reorientation. Pharmacotherapy: antipsychotics (haloperidol) NOT recommended for prevention, may use for severe agitation if non-pharm failed. Outcomes: delirium associated with longer ICU stay, higher mortality, worse post-ICU cognitive outcomes.",
            "tags": ["mof", "delirium", "cam_icu"],
            "library": "intern_year_medicine"
        }
    ]
    return units

def save_units(units, output_file):
    """Save units to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(units, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(units)} units to {output_file}")

if __name__ == "__main__":
    all_units = []

    # Heart Failure
    units = create_heart_failure_units()
    all_units.extend(units)
    save_units(units, "data/phase3_heart_failure_chunks.json")

    # Hypertensive Crisis
    units = create_hypertensive_crisis_units()
    all_units.extend(units)
    save_units(units, "data/phase3_hypertensive_crisis_chunks.json")

    # DIC
    units = create_dic_units()
    all_units.extend(units)
    save_units(units, "data/phase3_dic_chunks.json")

    # Liver Failure
    units = create_liver_failure_units()
    all_units.extend(units)
    save_units(units, "data/phase3_liver_failure_chunks.json")

    # Pancreatitis
    units = create_pancreatitis_units()
    all_units.extend(units)
    save_units(units, "data/phase3_acute_pancreatitis_chunks.json")

    # ICP
    units = create_icp_units()
    all_units.extend(units)
    save_units(units, "data/phase3_intracranial_hypertension_chunks.json")

    # Status Epilepticus
    units = create_status_epilepticus_units()
    all_units.extend(units)
    save_units(units, "data/phase3_status_epilepticus_chunks.json")

    # Organ Dysfunction
    units = create_organ_dysfunction_units()
    all_units.extend(units)
    save_units(units, "data/phase3_organ_dysfunction_chunks.json")

    print(f"\nTotal Phase 3 units created across all modules: {len(all_units)}")
