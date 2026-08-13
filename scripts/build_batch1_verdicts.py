"""
Build batch_1.json verdicts for records [80:278] of curated_candidates.json.
Run from project root: python scripts/build_batch1_verdicts.py
"""
import json, os

os.makedirs("data/factcheck", exist_ok=True)

# Each entry: (id, verdict, reason, corrected_text_or_None)
# Keyed by position 0..197 within slice [80:278]

VERDICTS_DATA = [
    # 0 - curated-phase2_unit_0 STEMI Definition
    ("curated-phase2_unit_0", "DROP_DUP",
     "MGH Manual ACS section covers STEMI criteria (score 0.782); same teaching content duplicated.",
     None),

    # 1 - curated-phase2_unit_1 NSTEMI/UA
    ("curated-phase2_unit_1", "DROP_DUP",
     "MGH Manual ACS section covers NSTEMI/UA distinction well (score 0.773).",
     None),

    # 2 - curated-phase2_unit_2 Troponin kinetics
    ("curated-phase2_unit_2", "DROP_DUP",
     "MGH Manual ACS section covers troponin kinetics and delta-rise algorithm (score 0.769).",
     None),

    # 3 - curated-phase2_unit_3 ACS atypical presentations
    ("curated-phase2_unit_3", "KEEP",
     "Adds detail on silent MI in diabetics/elderly with autonomic neuropathy not well-covered in corpus.",
     None),

    # 4 - curated-phase2_unit_4 Chest pain DDX
    ("curated-phase2_unit_4", "KEEP",
     "Corpus match was VTE section (off-topic). ACS vs non-ACS DDX structured summary adds value.",
     None),

    # 5 - curated-phase2_unit_5 TIMI score
    ("curated-phase2_unit_5", "KEEP",
     "Specific TIMI component breakdown and risk thresholds add teaching value beyond corpus summary.",
     None),

    # 6 - curated-phase2_unit_6 GRACE score
    ("curated-phase2_unit_6", "KEEP",
     "GRACE score components and risk thresholds not explicitly detailed in corpus ACS section.",
     None),

    # 7 - curated-phase2_unit_7 ACS initial stabilization
    ("curated-phase2_unit_7", "KEEP",
     "Corpus match was cardiac cath section (off-topic). Initial ACS stabilization checklist adds value.",
     None),

    # 8 - curated-phase2_unit_8 ECG LAD localization
    ("curated-phase2_unit_8", "KEEP",
     "Corpus ECG section general; LAD localization detail (diagonal branch, septal Q waves) adds value.",
     None),

    # 9 - curated-phase2_unit_9 ECG RCA localization
    ("curated-phase2_unit_9", "KEEP",
     "RCA territory ECG pattern and RV infarction contraindications (nitrates/morphine) add clinical value.",
     None),

    # 10 - curated-phase2_unit_10 ECG LCx/posterior
    ("curated-phase2_unit_10", "KEEP",
     "Posterior lead placement (V7-V9) and LCx territory detail not explicitly in corpus ECG section.",
     None),

    # 11 - curated-phase2_unit_11 RV infarction management
    ("curated-phase2_unit_11", "KEEP",
     "Practical RV infarction management (fluid bolus, avoid nitrates/morphine, HR 60-80 target) adds value.",
     None),

    # 12 - curated-phase2_unit_12 STEMI reperfusion
    ("curated-phase2_unit_12", "DROP_DUP",
     "MGH Manual ACS section covers PCI vs fibrinolysis, door-to-balloon time, and contraindications well.",
     None),

    # 13 - curated-phase2_unit_13 Aspirin in ACS
    ("curated-phase2_unit_13", "KEEP",
     "Corpus match was alcohol section (off-topic, score 0.615). Aspirin mechanism/dosing adds value.",
     None),

    # 14 - curated-phase2_unit_14 P2Y12 inhibitors
    ("curated-phase2_unit_14", "DROP_DUP",
     "MGH Manual ACS section covers P2Y12 inhibitors including loading doses and comparisons (score 0.781).",
     None),

    # 15 - curated-phase2_unit_15 DAPT duration
    ("curated-phase2_unit_15", "DROP_DUP",
     "MGH Manual ACS section covers DAPT duration and BMS vs DES distinction (score 0.769).",
     None),

    # 16 - curated-phase2_unit_16 Beta-blockers in ACS
    ("curated-phase2_unit_16", "FIX",
     "IV metoprolol dose stated as '25-50mg' is 10x too high; correct IV dose is 2.5-5mg q5min (Marino ICU Book confirms).",
     "Beta-blockers reduce mortality post-MI (15-20% relative risk reduction). Acute use: reduce cardiac work, heart rate, blood pressure. IV metoprolol 2.5-5mg IV q5min (max 3 doses / 15mg), then PO maintenance 25-50mg q6h (target HR 50-60). Esmolol for temporary control. Cautions: avoid if bradycardia <50, hypotension, AV block, decompensated heart failure, RV infarction (loss of RV chronotropic support). Continue long-term post-MI unless contraindicated. Cardioselective agents (metoprolol, atenolol) preferred over non-selective (propranolol)."),

    # 17 - curated-phase2_unit_17 ACE inhibitors in ACS
    ("curated-phase2_unit_17", "KEEP",
     "Specific timing (24-48h), dose titration, and ARB alternative for ACE-I intolerance add value.",
     None),

    # 18 - curated-phase2_unit_18 Statins in ACS
    ("curated-phase2_unit_18", "DROP_DUP",
     "MGH Manual ACS section covers high-intensity statin initiation and LDL targets (score 0.791).",
     None),

    # 19 - curated-phase2_unit_19 Nitroglycerin in ACS
    ("curated-phase2_unit_19", "KEEP",
     "PDE5 inhibitor interaction contraindication and RV infarction caution are high-yield safety pearls.",
     None),

    # 20 - curated-phase2_unit_20 Morphine in ACS
    ("curated-phase2_unit_20", "KEEP",
     "Corpus match was geriatric pain section (off-topic, score 0.605). Morphine caution in ACS adds value.",
     None),

    # 21 - curated-phase2_unit_21 Anticoagulation in ACS
    ("curated-phase2_unit_21", "DROP_DUP",
     "MGH Manual anticoagulation agents section covers UFH/LMWH in ACS comprehensively (score 0.795).",
     None),

    # 22 - curated-phase2_unit_22 GP IIb/IIIa inhibitors
    ("curated-phase2_unit_22", "KEEP",
     "Specific mechanism, dosing (abciximab 0.25mg/kg), and modern context (used less with newer P2Y12) add value.",
     None),

    # 23 - curated-phase2_unit_23 Calcium channel blockers ACS
    ("curated-phase2_unit_23", "KEEP",
     "Delineates limited/contraindicated role of CCBs in ACS vs chronic CAD management - teaching value.",
     None),

    # 24 - curated-phase2_unit_24 Aldosterone antagonists ACS
    ("curated-phase2_unit_24", "KEEP",
     "Eplerenone vs spironolactone dosing, EF <40% indication, and K+ monitoring adds specific clinical detail.",
     None),

    # 25 - curated-phase2_unit_25 Cardiogenic shock post-MI
    ("curated-phase2_unit_25", "DROP_DUP",
     "MGH Manual sepsis/shock section covers cardiogenic shock management comprehensively (score 0.799).",
     None),

    # 26 - curated-phase2_unit_26 MR post-MI
    ("curated-phase2_unit_26", "DROP_DUP",
     "MGH Manual MI complications section covers acute MR post-MI (score 0.736).",
     None),

    # 27 - curated-phase2_unit_27 VSD post-MI
    ("curated-phase2_unit_27", "DROP_DUP",
     "MGH Manual MI complications section covers VSD post-MI including O2 saturation step-up (score 0.761).",
     None),

    # 28 - curated-phase2_unit_28 Free wall rupture
    ("curated-phase2_unit_28", "DROP_DUP",
     "MGH Manual MI complications section covers free wall rupture and pseudoaneurysm (score 0.767).",
     None),

    # 29 - curated-phase2_unit_29 Brady/heart block post-MI
    ("curated-phase2_unit_29", "DROP_DUP",
     "MGH Manual MI complications section covers conduction disturbances post-MI (score 0.782).",
     None),

    # 30 - curated-phase2_unit_30 VF/VT post-MI
    ("curated-phase2_unit_30", "KEEP",
     "ICD EF <35% threshold and amiodarone use for hemodynamically tolerated VT add specific teaching value.",
     None),

    # 31 - curated-phase2_unit_31 LV remodeling/HF post-MI
    ("curated-phase2_unit_31", "KEEP",
     "LV thrombus risk with anterior MI + akinesis and DOAC/warfarin prophylaxis indications add value.",
     None),

    # 32 - curated-phase2_unit_32 Pericarditis/Dressler's
    ("curated-phase2_unit_32", "KEEP",
     "Dressler's syndrome timing (weeks-months), colchicine use, and distinction from reinfarction add value.",
     None),

    # 33 - curated-phase2_unit_33 RV infarction complications
    ("curated-phase2_unit_33", "KEEP",
     "Long-term RV recovery timeline and secondary TR development are teaching pearls not in corpus.",
     None),

    # 34 - curated-phase2_unit_34 Myocardial rupture types
    ("curated-phase2_unit_34", "DROP_DUP",
     "MI complications section covers all three rupture mechanisms. Echo section also retrieved (score 0.755).",
     None),

    # 35 - curated-phase2_unit_35 Post-infarction angina
    ("curated-phase2_unit_35", "KEEP",
     "Troponin reset timing (7-14 days) and how to use serial troponins to identify reinfarction is a key pearl.",
     None),

    # 36 - curated-phase2_unit_36 Post-MI discharge planning
    ("curated-phase2_unit_36", "KEEP",
     "Checklist format with ICD consideration timing (30 days post-MI) and echo at discharge adds clinical utility.",
     None),

    # 37 - curated-phase2_unit_37 Cardiac rehabilitation
    ("curated-phase2_unit_37", "KEEP",
     "Rehabilitation phases (I/II/III), mortality reduction 20-30%, and specific components add structured value.",
     None),

    # 38 - curated-phase2_unit_38 Risk factor modification post-MI
    ("curated-phase2_unit_38", "KEEP",
     "LDL <55 for very high risk, GLP-1/SGLT2i for diabetics, and exercise specifics add value over corpus summary.",
     None),

    # 39 - curated-phase2_unit_39 Anticoag strategy post-PCI
    ("curated-phase2_unit_39", "DROP_DUP",
     "MGH Manual anticoagulation agents section covers post-PCI anticoagulation and triple therapy (score 0.795).",
     None),

    # 40 - curated-phase2_unit_40 ICD/CRT post-MI
    ("curated-phase2_unit_40", "DROP_DUP",
     "MGH Manual cardiac devices section covers ICD/CRT indications (score 0.739).",
     None),

    # 41 - curated-phase2_unit_41 Ischemia testing/viability
    ("curated-phase2_unit_41", "DROP_DUP",
     "MGH Manual non-invasive cardiac testing section covers stress and viability testing (score 0.795).",
     None),

    # 42 - curated-phase2_unit_42 Depression post-MI
    ("curated-phase2_unit_42", "KEEP",
     "Corpus match was geriatric/frailty section (off-topic, score 0.640). PHQ-9 screening and SSRI use add value.",
     None),

    # 43 - curated-phase2_unit_43 Long-term follow-up post-MI
    ("curated-phase2_unit_43", "KEEP",
     "50% DAPT adherence at 12 months statistic and visit schedule framework add unique teaching content.",
     None),

    # 44 - curated-phase2_unit_44 COPD definition
    ("curated-phase2_unit_44", "KEEP",
     "Corpus match was mechanical vent (off-topic, 0.629). COPD pathophysiology and GOLD staging add value.",
     None),

    # 45 - curated-phase2_unit_45 Asthma phenotypes
    ("curated-phase2_unit_45", "KEEP",
     "Corpus match was chronic cough section (partial, 0.672). Asthma phenotype classification adds value.",
     None),

    # 46 - curated-phase2_unit_46 COPD exacerbation
    ("curated-phase2_unit_46", "KEEP",
     "Corpus match was bronchiectasis (partial, 0.723). Infection triggers (50-75%) and presentation detail add value.",
     None),

    # 47 - curated-phase2_unit_47 Asthma exacerbation severity
    ("curated-phase2_unit_47", "KEEP",
     "PEF percentage thresholds (>70%, 40-70%, <40%) and danger sign 'silent chest' add critical teaching value.",
     None),

    # 48 - curated-phase2_unit_48 Bronchodilators
    ("curated-phase2_unit_48", "KEEP",
     "LABA monotherapy safety warning in asthma (mortality risk) is a critical teaching point.",
     None),

    # 49 - curated-phase2_unit_49 Corticosteroids COPD/asthma
    ("curated-phase2_unit_49", "KEEP",
     "Specific dosing (prednisone 40-60mg vs methylprednisolone 125mg q6h), no-taper-if <2w adds value.",
     None),

    # 50 - curated-phase2_unit_50 Magnesium sulfate asthma
    ("curated-phase2_unit_50", "KEEP",
     "Mechanism (calcium antagonist), renal contraindication, and limited evidence context add value.",
     None),

    # 51 - curated-phase2_unit_51 Leukotriene inhibitors/omalizumab
    ("curated-phase2_unit_51", "KEEP",
     "Omalizumab IgE range (30-700 IU/mL), anaphylaxis monitoring, and neuropsychiatric warning add value.",
     None),

    # 52 - curated-phase2_unit_52 BiPAP COPD
    ("curated-phase2_unit_52", "KEEP",
     "IPAP/EPAP specific settings (8-12/3-5 cmH2O) and pH <7.35 threshold for BiPAP add specific value.",
     None),

    # 53 - curated-phase2_unit_53 Theophylline
    ("curated-phase2_unit_53", "KEEP",
     "Corpus match was toxicology (off-topic, 0.649). Theophylline narrow window and smoking cessation interaction add value.",
     None),

    # 54 - curated-phase2_unit_54 Intubation COPD/asthma
    ("curated-phase2_unit_54", "DROP_DUP",
     "MGH Manual respiratory distress section covers intubation indications comprehensively (score 0.795).",
     None),

    # 55 - curated-phase2_unit_55 Oxygen therapy targets
    ("curated-phase2_unit_55", "KEEP",
     "SpO2 88-92% vs 94-98% targets and Haldane effect mechanism add important teaching content.",
     None),

    # 56 - curated-phase2_unit_56 Discharge/pulm rehab
    ("curated-phase2_unit_56", "KEEP",
     "Corpus match was SOB intern guide (off-topic, 0.589). Pulm rehab reducing readmissions 30-40% adds value.",
     None),

    # 57 - curated-phase2_unit_57 Vaccination in COPD
    ("curated-phase2_unit_57", "KEEP",
     "RSV vaccine (AREXVY/ABRYSVO) inclusion and LAIV contraindication in COPD are current teaching pearls.",
     None),

    # 58 - curated-phase2_unit_58 COPD/asthma mimics DDX
    ("curated-phase2_unit_58", "KEEP",
     "Structured differential for dyspnea (anaphylaxis, ACS, pneumothorax) adds high clinical utility.",
     None),

    # 59 - curated-phase2_unit_59 Type 1 DM
    ("curated-phase2_unit_59", "KEEP",
     "Corpus match was DKA section (partial, 0.785). T1DM autoantibodies (anti-GAD, IA-2) and HLA add value.",
     None),

    # 60 - curated-phase2_unit_60 Type 2 DM
    ("curated-phase2_unit_60", "KEEP",
     "C-peptide distinction and metabolic syndrome association add nuance beyond corpus summary.",
     None),

    # 61 - curated-phase2_unit_61 Gestational DM
    ("curated-phase2_unit_61", "KEEP",
     "50g OGCT ≥140 threshold, 3-hour OGTT criteria, and 50% T2DM risk postpartum add specific value.",
     None),

    # 62 - curated-phase2_unit_62 DM diagnostic criteria
    ("curated-phase2_unit_62", "KEEP",
     "HbA1c limitations (hemolytic anemia, hemoglobin variants) and CGM mention add practical value.",
     None),

    # 63 - curated-phase2_unit_63 HbA1c targets
    ("curated-phase2_unit_63", "KEEP",
     "Individualized targets (<7% vs <8% vs <6.5%) and shared decision-making guidance add clinical value.",
     None),

    # 64 - curated-phase2_unit_64 Metformin
    ("curated-phase2_unit_64", "KEEP",
     "Contrast hold 48h rationale and GFR <30 contraindication vs GFR 30-45 caution distinction add value.",
     None),

    # 65 - curated-phase2_unit_65 Sulfonylureas/meglitinides
    ("curated-phase2_unit_65", "KEEP",
     "Secondary failure (beta-cell exhaustion) concept and preference shift to SGLT2i/GLP-1 add teaching value.",
     None),

    # 66 - curated-phase2_unit_66 SGLT2 inhibitors
    ("curated-phase2_unit_66", "KEEP",
     "Euglycemic DKA risk in T1DM and GFR <20 contraindication are critical safety teaching points.",
     None),

    # 67 - curated-phase2_unit_67 GLP-1 agonists
    ("curated-phase2_unit_67", "KEEP",
     "MEN-2 and medullary thyroid cancer contraindication (absolute) is a critical safety pearl.",
     None),

    # 68 - curated-phase2_unit_68 DPP-4/TZD
    ("curated-phase2_unit_68", "KEEP",
     "Pioglitazone bladder cancer risk and rosiglitazone CV concerns add safety teaching value.",
     None),

    # 69 - curated-phase2_unit_69 Insulin types/regimens
    ("curated-phase2_unit_69", "KEEP",
     "50/50 basal-bolus split rule and premix insulin 70/30 format add practical prescribing value.",
     None),

    # 70 - curated-phase2_unit_70 Hypoglycemia
    ("curated-phase2_unit_70", "KEEP",
     "Rule of 15, glucagon 1mg IM for severe, and hypoglycemia unawareness mechanism add clinical value.",
     None),

    # 71 - curated-phase2_unit_71 DKA pathophysiology
    ("curated-phase2_unit_71", "KEEP",
     "Kussmaul respirations, fruity breath mechanism, and 1-5% mortality if treated add teaching value.",
     None),

    # 72 - curated-phase2_unit_72 DKA treatment
    ("curated-phase2_unit_72", "FIX",
     "When glucose <250mg/dL in DKA, must add dextrose to IV fluids (D5 0.45NS), not switch to 0.45 NS alone; insulin must continue to close anion gap.",
     "DKA treatment: (1) IV fluids: 0.9% NS 500-1000 mL/hr initially (aggressive hydration), switch to D5 0.45% NS once glucose <250 (add dextrose to maintain glucose 150-200 while continuing insulin to clear ketones). Total deficit typically 5-10L. (2) Insulin: bolus 0.1 units/kg IV, then 0.1 units/kg/hr continuous infusion (usually 5-10 units/hr), titrate to reduce glucose 50-75 mg/dL/hr. (3) Potassium: check baseline; likely total body deficit 3-5 mEq/kg despite normal/high serum K+ (shifts). Replete cautiously (K+ shift into cells with insulin = hypokalemia risk). (4) Bicarbonate: controversial, reserved for pH <6.9 (3 amps NaHCO3 in D5W). Monitor: glucose, electrolytes, ABG q1-2h initially, neuro checks. Switch to SC insulin once ketosis resolves (glucose <200, HCO3- >15, eating)."),

    # 73 - curated-phase2_unit_73 HHS
    ("curated-phase2_unit_73", "KEEP",
     "HHS vs DKA osmolality threshold >320, slower glucose reduction target (25-50 mg/dL/hr) add value.",
     None),

    # 74 - curated-phase2_unit_74 Sick day management
    ("curated-phase2_unit_74", "KEEP",
     "Inpatient glycemic target 140-180 and 'avoid hypoglycemia <70' rationale add practical teaching value.",
     None),

    # 75 - curated-phase2_unit_75 Microvascular complications
    ("curated-phase2_unit_75", "KEEP",
     "Corpus match AKI section (off-topic, 0.587). Retinopathy/nephropathy/neuropathy structured overview adds value.",
     None),

    # 76 - curated-phase2_unit_76 Macrovascular complications
    ("curated-phase2_unit_76", "KEEP",
     "Corpus match was ACS section (off-topic for diabetes complications). Adds specific CV complications teaching.",
     None),

    # 77 - curated-phase2_unit_77 UGIB basics
    ("curated-phase2_unit_77", "DROP_DUP",
     "MGH Manual UGIB section covers incidence, presentation, and mortality comprehensively (score 0.795).",
     None),

    # 78 - curated-phase2_unit_78 PUD
    ("curated-phase2_unit_78", "KEEP",
     "H. pylori 90% risk statistic and 2mm definition of ulcer vs erosion add teaching detail.",
     None),

    # 79 - curated-phase2_unit_79 Variceal bleeding
    ("curated-phase2_unit_79", "KEEP",
     "Portal pressure gradient >12mmHg threshold and 5-15% yearly risk in cirrhosis are specific teachable facts.",
     None),

    # 80 - curated-phase2_unit_80 Esophagitis/MW/Boerhaave
    ("curated-phase2_unit_80", "KEEP",
     "Boerhaave diagnosis (contrast esophagography) and mortality 10-30% even with surgery add high-yield content.",
     None),

    # 81 - curated-phase2_unit_81 Gastric cancer/PHG
    ("curated-phase2_unit_81", "KEEP",
     "Portal hypertensive gastropathy distinction from varices and why banding is less effective adds value.",
     None),

    # 82 - curated-phase2_unit_82 UGIB initial management
    ("curated-phase2_unit_82", "DROP_DUP",
     "MGH Manual UGIB section covers initial management including octreotide, PPI, and endoscopy timing (score 0.774).",
     None),

    # 83 - curated-phase2_unit_83 Glasgow-Blatchford/AIMS65
    ("curated-phase2_unit_83", "DROP_DUP",
     "MGH Manual UGIB section covers risk scores including Glasgow-Blatchford and AIMS65 (score 0.795).",
     None),

    # 84 - curated-phase2_unit_84 PPI in UGIB
    ("curated-phase2_unit_84", "DROP_DUP",
     "MGH Manual UGIB section covers PPI dosing (80mg bolus + 8mg/hr) and H. pylori testing (score 0.795).",
     None),

    # 85 - curated-phase2_unit_85 Octreotide/antibiotics varices
    ("curated-phase2_unit_85", "DROP_DUP",
     "MGH Manual UGIB section covers octreotide and antibiotic use in variceal bleeding (score 0.784).",
     None),

    # 86 - curated-phase2_unit_86 Endoscopic hemostasis
    ("curated-phase2_unit_86", "DROP_DUP",
     "MGH Manual UGIB section covers endoscopic hemostasis techniques and success rates (score 0.795).",
     None),

    # 87 - curated-phase2_unit_87 Rebleeding risk/surgical
    ("curated-phase2_unit_87", "KEEP",
     "Specific high-risk locations (posterior duodenal, gastric body/fundus) and surgical thresholds add value.",
     None),

    # 88 - curated-phase2_unit_88 Transfusion strategy UGIB
    ("curated-phase2_unit_88", "DROP_DUP",
     "MGH Manual UGIB section covers restrictive transfusion strategy and massive transfusion protocol (score 0.795).",
     None),

    # 89 - curated-phase2_unit_89 TIPS indications
    ("curated-phase2_unit_89", "KEEP",
     "TIPS complications (40% shunt thrombosis by 1 year, 30% encephalopathy) and timing detail add value.",
     None),

    # 90 - curated-phase2_unit_90 LGIB basics
    ("curated-phase2_unit_90", "DROP_DUP",
     "MGH Manual UGIB/LGIB section covers LGIB epidemiology and etiology distribution (score 0.795).",
     None),

    # 91 - curated-phase2_unit_91 Diverticulosis/diverticulitis
    ("curated-phase2_unit_91", "KEEP",
     "Avoid colonoscopy during active diverticulitis inflammation (perforation risk) is a key safety pearl.",
     None),

    # 92 - curated-phase2_unit_92 IBD overview
    ("curated-phase2_unit_92", "DROP_DUP",
     "MGH Manual IBD section covers Crohn's vs UC distinction, extraintestinal manifestations, and biologics (score 0.782).",
     None),

    # 93 - curated-phase2_unit_93 Angiodysplasia
    ("curated-phase2_unit_93", "KEEP",
     "Corpus match was stroke section (off-topic, 0.716). Aortic stenosis/renal failure association and right colon predominance add value.",
     None),

    # 94 - curated-phase2_unit_94 Ischemic colitis
    ("curated-phase2_unit_94", "KEEP",
     "Corpus match was IBD section (partial, 0.608). Thumbprinting sign, sparing of rectum (dual supply) are specific pearls.",
     None),

    # 95 - curated-phase2_unit_95 C. difficile
    ("curated-phase2_unit_95", "FIX",
     "Per IDSA 2021 guidelines, vancomycin 125mg QID (not metronidazole) is first-line for non-severe CDI; metronidazole no longer recommended as first-line.",
     "C. difficile: leading cause antibiotic-associated colitis; toxins A/B damage mucosa, 5-10% develop toxic megacolon/perforation. Risk: antibiotics, age >65, immunosuppression, hospitalization. Presentation: watery diarrhea, abdominal pain, fever, leukocytosis, elevated creatinine. Diagnosis: stool PCR for toxin genes (most sensitive), or toxin enzyme immunoassay. Management: stop offending antibiotic if possible. Per IDSA 2021: vancomycin 125mg QID x 10 days first-line for non-severe AND severe CDI. Fidaxomicin 200mg BID x 10 days preferred for recurrent (lower relapse rate). Metronidazole no longer first-line (reserved for patients who cannot tolerate vancomycin/fidaxomicin). Severe: Cr >1.5x baseline, WBC >15k, hypotension, ICU. Avoid antiperistaltic agents (increase toxic megacolon risk)."),

    # 96 - curated-phase2_unit_96 Hemorrhoids
    ("curated-phase2_unit_96", "KEEP",
     "Dentate line distinction (internal=painless vs external=painful) and rubber-band ligation detail add clinical value.",
     None),

    # 97 - curated-phase2_unit_97 Meckel's diverticulum
    ("curated-phase2_unit_97", "KEEP",
     "Rule of 2s mnemonic, Meckel scan mechanism (pertechnetate binds gastric mucosa), and pediatric peak risk add value.",
     None),

    # 98 - curated-phase2_unit_98 Colonoscopy LGIB
    ("curated-phase2_unit_98", "DROP_DUP",
     "MGH Manual LGIB section covers colonoscopy indications, timing, and hemostasis techniques (score 0.795).",
     None),

    # 99 - curated-phase2_unit_99 Capsule endoscopy obscure GI
    ("curated-phase2_unit_99", "KEEP",
     "Sensitivity 50-75% for small bowel, retained capsule risk if stricture, and angiography >2mL/min threshold add value.",
     None),

    # 100 - curated-phase2_unit_100 Anticoagulation reversal GI bleed
    ("curated-phase2_unit_100", "DROP_DUP",
     "MGH Manual UGIB section covers anticoagulation reversal including idarucizumab and andexanet (score 0.795).",
     None),

    # 101 - curated-phase2_unit_101 Post-polypectomy hemorrhage
    ("curated-phase2_unit_101", "KEEP",
     "Corpus match was perioperative medicine (off-topic, 0.617). Delayed bleeding 3-7 days and hemoclip prevention add value.",
     None),

    # 102 - curated-phase2_unit_102 PE basics/Virchow's triad
    ("curated-phase2_unit_102", "KEEP",
     "Incidence/mortality comparison (2-10% treated vs 30% untreated) and triad components add value.",
     None),

    # 103 - curated-phase2_unit_103 Wells score for PE
    ("curated-phase2_unit_103", "DROP_INACCURATE",
     "Wells PE criteria are fabricated: 'shock (3.5 if hypotensive, 1.5 if syncope)', 'atelectasis/CXR normal' are NOT real Wells criteria. Real criteria: DVT signs=3, alt dx=3, HR>100=1.5, immobility/surg=1.5, prior VTE=1.5, hemoptysis=1, malignancy=1.",
     None),

    # 104 - curated-phase2_unit_104 D-dimer interpretation
    ("curated-phase2_unit_104", "KEEP",
     "Age-adjusted D-dimer cutoff (age x10 ng/mL) and high sensitivity vs low specificity explanation add value.",
     None),

    # 105 - curated-phase2_unit_105 CTPA interpretation
    ("curated-phase2_unit_105", "KEEP",
     "Corpus match was rheumatology (off-topic, 0.718). Subsegmental PE management debate (NEJM 2024) adds current value.",
     None),

    # 106 - curated-phase2_unit_106 PE clinical presentation
    ("curated-phase2_unit_106", "KEEP",
     "S1Q3T3 only 10-15% incidence and absence of dyspnea not ruling out PE are key clinical pearls.",
     None),

    # 107 - curated-phase2_unit_107 PE ECG/biomarkers
    ("curated-phase2_unit_107", "KEEP",
     "Troponin/BNP as prognostic (not diagnostic) in PE is a critical teaching distinction.",
     None),

    # 108 - curated-phase2_unit_108 Echo in PE
    ("curated-phase2_unit_108", "KEEP",
     "McConnell's sign (RV free wall hypokinesis with apical sparing) and RV/LV >0.9 add specific value.",
     None),

    # 109 - curated-phase2_unit_109 Massive vs submassive PE
    ("curated-phase2_unit_109", "KEEP",
     "Mortality stratification (massive 30-50% vs submassive 5-10% vs stable <5%) adds teaching structure.",
     None),

    # 110 - curated-phase2_unit_110 V/Q scan
    ("curated-phase2_unit_110", "KEEP",
     "Indications for V/Q over CTPA (contrast allergy, renal insufficiency, pregnancy) add clinical decision value.",
     None),

    # 111 - curated-phase2_unit_111 Incidental PE screening
    ("curated-phase2_unit_111", "KEEP",
     "Management algorithm for incidental PE by level (main/lobar vs segmental vs subsegmental) adds decision value.",
     None),

    # 112 - curated-phase2_unit_112 PE in pregnancy
    ("curated-phase2_unit_112", "KEEP",
     "Corpus match was thyroid section (off-topic, 0.708). LMWH preferred over warfarin in pregnancy and thrombolysis threshold add value.",
     None),

    # 113 - curated-phase2_unit_113 DVT basics
    ("curated-phase2_unit_113", "KEEP",
     "Post-thrombotic syndrome 20-50% and recurrent thrombosis risk without treatment add clinical context.",
     None),

    # 114 - curated-phase2_unit_114 Wells DVT score
    ("curated-phase2_unit_114", "KEEP",
     "DVT Wells score (different from PE Wells), alternative diagnosis (-2) criterion, and specific risk % add value.",
     None),

    # 115 - curated-phase2_unit_115 Compression US DVT
    ("curated-phase2_unit_115", "KEEP",
     "Corpus match was peripheral IV ultrasound (off-topic, 0.780). Technique and distal DVT follow-up timing add value.",
     None),

    # 116 - curated-phase2_unit_116 DVT presentation
    ("curated-phase2_unit_116", "KEEP",
     "Phlegmasia cerulea dolens as emergency presentation and 20% asymptomatic in hospitalized patients add value.",
     None),

    # 117 - curated-phase2_unit_117 SVT vs DVT
    ("curated-phase2_unit_117", "KEEP",
     "Saphenofemoral junction 5cm rule and anticoagulation decision tree for SVT add clinical utility.",
     None),

    # 118 - curated-phase2_unit_118 IVC thrombosis
    ("curated-phase2_unit_118", "KEEP",
     "Bilateral leg edema + dilated superficial veins as IVC thrombosis clue adds unique diagnostic value.",
     None),

    # 119 - curated-phase2_unit_119 VTE anticoagulation duration
    ("curated-phase2_unit_119", "KEEP",
     "D-dimer after stopping anticoagulation as guide for extended therapy adds evidence-based teaching content.",
     None),

    # 120 - curated-phase2_unit_120 LMWH/UFH/DOAC comparison
    ("curated-phase2_unit_120", "KEEP",
     "CrCl <30 threshold for UFH preference and DOAC bridge timing (start immediately vs 5-7d) add value.",
     None),

    # 121 - curated-phase2_unit_121 Warfarin vs DOAC
    ("curated-phase2_unit_121", "KEEP",
     "Monitoring comparison table and DOAC CrCl cutoffs (15-30 depending on agent) add prescribing value.",
     None),

    # 122 - curated-phase2_unit_122 IVC filter
    ("curated-phase2_unit_122", "KEEP",
     "Retrievable filter 3-month removal window and permanent filter criteria add procedural decision value.",
     None),

    # 123 - curated-phase2_unit_123 Post-thrombotic syndrome
    ("curated-phase2_unit_123", "KEEP",
     "Corpus match was ICH section (off-topic, 0.715). CEAP classification and compression stocking evidence add value.",
     None),

    # 124 - curated-phase2_unit_124 HAS-BLED bleeding risk
    ("curated-phase2_unit_124", "KEEP",
     "HAS-BLED components, annual risk thresholds, and strategies to reduce bleeding add clinical utility.",
     None),

    # 125 - curated-phase2_unit_125 Anticoagulation reversal
    ("curated-phase2_unit_125", "KEEP",
     "Idarucizumab vs andexanet distinction (apixaban/rivaroxaban vs dabigatran) is a key clinical decision point.",
     None),

    # 126 - curated-phase2_unit_126 Thrombophilia workup
    ("curated-phase2_unit_126", "KEEP",
     "Timing: avoid acute phase and protein S not during warfarin are practical testing pearls.",
     None),

    # 127 - curated-phase2_unit_127 Cancer VTE
    ("curated-phase2_unit_127", "KEEP",
     "HOKUSAI-VTE-C and SELECT-D trial references and DOAC evolution for cancer VTE add current evidence.",
     None),

    # 128 - curated-phase2_unit_128 Recurrent VTE
    ("curated-phase2_unit_128", "KEEP",
     "80-85% recurrence reduction with extended anticoagulation and occult malignancy workup add value.",
     None),

    # 129 - curated-phase2_unit_129 PERT
    ("curated-phase2_unit_129", "KEEP",
     "Corpus match was MGH TOC (off-topic, 0.657). PERT multidisciplinary team composition and indication add value.",
     None),

    # 130 - curated-phase2_unit_130 VTE prophylaxis
    ("curated-phase2_unit_130", "KEEP",
     "Padua/IMPROVE score mention, surgical duration differences (general 12d vs orthopedic 10-35d) add value.",
     None),

    # 131 - curated-phase2_unit_131 CTEPH
    ("curated-phase2_unit_131", "FIX",
     "mPAP >25 mmHg is outdated; ESC 2022 updated pulmonary hypertension definition to mPAP >=20 mmHg (confirmed by corpus).",
     "Chronic thromboembolic pulmonary hypertension (CTEPH): occurs if PE clots not completely resolved, leading to chronic RV strain, dyspnea, RV failure. Incidence 0.1-4% after acute PE. Risk: large PE, recurrent PE, inadequate anticoagulation. Diagnosis: right heart catheterization (elevated mean PA pressure >=20 mmHg at rest per ESC 2022 updated definition), CT angiography (mosaic perfusion, webs/bands), ventilation-perfusion scan (mismatched defects). Management: lifelong anticoagulation, pulmonary vasodilators (ambrisentan, bosentan, sildenafil), pulmonary endarterectomy if operable (curative, 5-10 year survival benefit). Early recognition/referral critical."),

    # 132 - curated-phase2_unit_132 CAP definition
    ("curated-phase2_unit_132", "KEEP",
     "Corpus match was HAP/VAP section (partial, 0.750). CAP incidence/mortality stratification by setting adds value.",
     None),

    # 133 - curated-phase2_unit_133 CAP risk factors
    ("curated-phase2_unit_133", "KEEP",
     "Structured risk factor list and initial assessment framework add teaching structure to CAP module.",
     None),

    # 134 - curated-phase2_unit_134 CAP presentation
    ("curated-phase2_unit_134", "KEEP",
     "Elderly lacking fever and altered mental status as CAP presentation adds important clinical teaching value.",
     None),

    # 135 - curated-phase2_unit_135 CAP CXR
    ("curated-phase2_unit_135", "DROP_DUP",
     "MGH Manual CAP section covers CXR patterns (lobar, bronchopneumonia, interstitial) well (score 0.795).",
     None),

    # 136 - curated-phase2_unit_136 CAP labs
    ("curated-phase2_unit_136", "KEEP",
     "Blood cultures only 10% positive and sputum quality criteria (>25 PMNs, <10 epithelials) add practical value.",
     None),

    # 137 - curated-phase2_unit_137 CAP viral vs bacterial
    ("curated-phase2_unit_137", "DROP_DUP",
     "MGH Manual CAP section covers viral vs bacterial distinction, cold agglutinins, and rapid testing (score 0.795).",
     None),

    # 138 - curated-phase2_unit_138 Gram stain interpretation
    ("curated-phase2_unit_138", "DROP_DUP",
     "MGH Manual CAP section covers Gram stain interpretation and quality criteria (score 0.795).",
     None),

    # 139 - curated-phase2_unit_139 Atypical pathogens overview
    ("curated-phase2_unit_139", "KEEP",
     "Q fever (Coxiella) and psittacosis (Chlamydia psittaci) exposure associations add unique teaching content.",
     None),

    # 140 - curated-phase2_unit_140 CURB-65 components
    ("curated-phase2_unit_140", "DROP_DUP",
     "MGH Manual CAP section covers CURB-65 components in detail (score 0.771).",
     None),

    # 141 - curated-phase2_unit_141 CURB-65 risk stratification
    ("curated-phase2_unit_141", "DROP_DUP",
     "MGH Manual CAP section covers CURB-65 risk stratification by score and 30-day mortality (score 0.756).",
     None),

    # 142 - curated-phase2_unit_142 CURB-65 clinical application
    ("curated-phase2_unit_142", "KEEP",
     "Worked example with specific patient and PSI as complementary tool add practical application value.",
     None),

    # 143 - curated-phase2_unit_143 CURB-65 confusion component
    ("curated-phase2_unit_143", "KEEP",
     "Dementia vs delirium distinction for CURB-65 confusion criterion is a critical teaching point.",
     None),

    # 144 - curated-phase2_unit_144 CURB-65 limitations
    ("curated-phase2_unit_144", "KEEP",
     "qSOFA comparison and CURB-65 limitations (no SpO2, no lactate) add value beyond standard scoring tables.",
     None),

    # 145 - curated-phase2_unit_145 S. pneumoniae
    ("curated-phase2_unit_145", "DROP_DUP",
     "MGH Manual CAP section covers pneumococcal pneumonia including blood culture positivity and complications (score 0.795).",
     None),

    # 146 - curated-phase2_unit_146 H. influenzae
    ("curated-phase2_unit_146", "KEEP",
     "HiB vaccine adult protection waning and beta-lactamase resistance (30-50%) via mechanism add value.",
     None),

    # 147 - curated-phase2_unit_147 Moraxella catarrhalis
    ("curated-phase2_unit_147", "KEEP",
     "80% ampicillin resistance and elderly/COPD predominance profile add specific pathogen teaching value.",
     None),

    # 148 - curated-phase2_unit_148 Aspiration pneumonia
    ("curated-phase2_unit_148", "FIX",
     "Penicillin V is not standard for aspiration pneumonia; correct anaerobic coverage is clindamycin OR amoxicillin-clavulanate (or ampicillin-sulbactam IV).",
     "Aspiration pneumonia: from oral anaerobes after aspiration (risk: altered mental status, dysphagia, seizures, alcohol abuse). Pathogens: Peptostreptococcus, Prevotella, Fusobacterium, Bacteroides (all anaerobes). Presents subacutely (1-2 weeks), often with foul-smelling sputum/breath. Apical-posterior/superior segment infiltrate (gravity-dependent). Cavitation if delayed treatment. Standard antibiotic coverage: clindamycin 600mg TID OR amoxicillin-clavulanate (875/125mg BID PO or ampicillin-sulbactam 3g IV q6h). Clindamycin preferred for documented anaerobic infection; beta-lactam/beta-lactamase inhibitor combinations offer broader coverage including aerobic gram-negatives."),

    # 149 - curated-phase2_unit_149 Gram-negative CAP
    ("curated-phase2_unit_149", "KEEP",
     "Pseudomonas risk factor FEV1 <25% threshold and Klebsiella/alcoholism association add specific value.",
     None),

    # 150 - curated-phase2_unit_150 CAP outpatient antibiotics
    ("curated-phase2_unit_150", "DROP_DUP",
     "MGH Manual CAP section covers outpatient antibiotic regimens including amoxicillin vs macrolide vs FQ (score 0.795).",
     None),

    # 151 - curated-phase2_unit_151 CAP inpatient non-ICU
    ("curated-phase2_unit_151", "DROP_DUP",
     "MGH Manual CAP section covers inpatient beta-lactam + macrolide or FQ monotherapy (score 0.795).",
     None),

    # 152 - curated-phase2_unit_152 CAP ICU/severe
    ("curated-phase2_unit_152", "KEEP",
     "Specific regimen (ceftriaxone 1-2g q12h + levofloxacin or azithromycin) and Pseudomonas risk criteria add value.",
     None),

    # 153 - curated-phase2_unit_153 FQ vs beta-lactam+macrolide
    ("curated-phase2_unit_153", "KEEP",
     "Balanced comparison including FQ side effects (CDIFF, QT, tendon) and clinical equivalence data adds value.",
     None),

    # 154 - curated-phase2_unit_154 Macrolide choice
    ("curated-phase2_unit_154", "KEEP",
     "Macrolide monotherapy failure risk in elderly/comorbid patients (use with beta-lactam) is a key safety teaching point.",
     None),

    # 155 - curated-phase2_unit_155 CAP antibiotic duration
    ("curated-phase2_unit_155", "KEEP",
     "3-5 day option if stable and short course evidence add value over standard 5-7 day recommendation.",
     None),

    # 156 - curated-phase2_unit_156 De-escalation stewardship
    ("curated-phase2_unit_156", "DROP_DUP",
     "MGH Manual HAP/VAP section covers de-escalation strategy (start broad, narrow on cultures) (score 0.791).",
     None),

    # 157 - curated-phase2_unit_157 Legionella epidemiology
    ("curated-phase2_unit_157", "KEEP",
     "Corpus match was PAD (off-topic, 0.697). Water source specifics, 2-10 day incubation, 25% mortality untreated add value.",
     None),

    # 158 - curated-phase2_unit_158 Legionella clinical
    ("curated-phase2_unit_158", "KEEP",
     "Hyponatremia (SIADH), elevated transaminases, and urine antigen test as first-line diagnosis add value.",
     None),

    # 159 - curated-phase2_unit_159 Legionella treatment
    ("curated-phase2_unit_159", "KEEP",
     "Corpus match was alcohol section (off-topic, 0.695). Beta-lactams ineffective and duration 7-10 days add value.",
     None),

    # 160 - curated-phase2_unit_160 Mycoplasma epidemiology
    ("curated-phase2_unit_160", "KEEP",
     "4-7 year epidemic cycle, 1-3 week incubation, and neurologic complications add specific teaching content.",
     None),

    # 161 - curated-phase2_unit_161 Mycoplasma clinical
    ("curated-phase2_unit_161", "KEEP",
     "Cold agglutinin titer >1:64 as suggestive threshold and special culture media requirement add value.",
     None),

    # 162 - curated-phase2_unit_162 Mycoplasma treatment
    ("curated-phase2_unit_162", "KEEP",
     "Cold agglutinin hemolysis management (warm transfusions, avoid cold exposure) adds unique clinical teaching.",
     None),

    # 163 - curated-phase2_unit_163 HAP definition
    ("curated-phase2_unit_163", "DROP_DUP",
     "MGH Manual HAP/VAP section covers HAP/VAP/HCAP definitions and mortality data (score 0.785).",
     None),

    # 164 - curated-phase2_unit_164 HAP/VAP organisms
    ("curated-phase2_unit_164", "DROP_DUP",
     "MGH Manual HAP/VAP section covers MDR gram-negatives and MRSA risk factors (score 0.735).",
     None),

    # 165 - curated-phase2_unit_165 VAP diagnosis
    ("curated-phase2_unit_165", "DROP_DUP",
     "MGH Manual HAP/VAP section covers VAP clinical diagnosis, quantitative cultures, and procalcitonin (score 0.780).",
     None),

    # 166 - curated-phase2_unit_166 VAP prevention bundle
    ("curated-phase2_unit_166", "KEEP",
     "SDD controversy, subglottic secretion drainage tubes, and 30-50% VAP reduction data add value.",
     None),

    # 167 - curated-phase2_unit_167 HAP/VAP empiric therapy
    ("curated-phase2_unit_167", "DROP_DUP",
     "MGH Manual CAP section retrieved covers empiric regimens; HAP/VAP section also covers piperacillin-tazobactam/cefepime/meropenem choices (score 0.765).",
     None),

    # 168 - curated-phase2_unit_168 HAP/VAP de-escalation/duration
    ("curated-phase2_unit_168", "KEEP",
     "7 vs 14+ day comparison and resistance risk with prolonged therapy add stewardship teaching value.",
     None),

    # 169 - curated-phase2_unit_169 VAP weaning/extubation
    ("curated-phase2_unit_169", "KEEP",
     "Spontaneous breathing trial settings (PS 7-8 cmH2O, PEEP 5) and NIF <-20 threshold add specific value.",
     None),

    # 170 - curated-phase2_unit_170 CAP sepsis
    ("curated-phase2_unit_170", "DROP_DUP",
     "MGH Manual sepsis section covers initial management (30mL/kg fluids, norepinephrine, lactate) comprehensively (score 0.822).",
     None),

    # 171 - curated-phase2_unit_171 Empyema
    ("curated-phase2_unit_171", "KEEP",
     "Empyema diagnostic criteria (pH <7.0, glucose <60, LDH >1000) and VATS for loculated effusion add value.",
     None),

    # 172 - curated-phase2_unit_172 ARDS from CAP
    ("curated-phase2_unit_172", "DROP_DUP",
     "MGH Manual ARDS section covers lung-protective ventilation and prone positioning (score 0.798).",
     None),

    # 173 - curated-phase2_unit_173 Pneumothorax from CAP
    ("curated-phase2_unit_173", "KEEP",
     "Staphylococcal/pneumococcal pneumatosis causing secondary pneumothorax and <2cm observation rule add value.",
     None),

    # 174 - curated-phase2_unit_174 Parapneumonic effusion
    ("curated-phase2_unit_174", "KEEP",
     "Distinction from empyema by pH 7.0-7.20 (vs <7.0) and when to drain uncomplicated vs complicated add value.",
     None),

    # 175 - curated-phase2_unit_175 Metastatic infection from CAP
    ("curated-phase2_unit_175", "KEEP",
     "Hematogenous spread risk (meningitis 5-10% of bacteremia, endocarditis with prosthetic valve) adds clinical teaching.",
     None),

    # 176 - curated-phase2_unit_176 Myocarditis/pericarditis CAP
    ("curated-phase2_unit_176", "KEEP",
     "PR depression on ECG and tamponade risk management (pericardiocentesis) add specific teaching value.",
     None),

    # 177 - curated-phase2_unit_177 Lung abscess
    ("curated-phase2_unit_177", "KEEP",
     "Cavitary lesion with air-fluid level, prolonged anaerobic coverage (2-4 weeks), and drainage >4-5cm threshold add value.",
     None),

    # 178 - curated-phase2_unit_178 PCP risk factors
    ("curated-phase2_unit_178", "KEEP",
     "Non-HIV risk factors (TNF-alpha inhibitors, JAK inhibitors, >20mg prednisone >1 month) and normal CXR in 15-20% add value.",
     None),

    # 179 - curated-phase2_unit_179 PCP diagnosis/treatment
    ("curated-phase2_unit_179", "KEEP",
     "Steroids if PaO2 <70 or A-a gradient >35 reduces mortality - a critical teaching decision point.",
     None),

    # 180 - curated-phase2_unit_180 HIV pneumonia approach
    ("curated-phase2_unit_180", "KEEP",
     "CD4-stratified OI approach and IRIS management with ART add unique HIV/immunocompromised teaching.",
     None),

    # 181 - curated-phase2_unit_181 CMV pneumonitis
    ("curated-phase2_unit_181", "KEEP",
     "CMV PCR blood load, inclusion bodies on histology, and 40-90% untreated mortality add specific value.",
     None),

    # 182 - curated-phase2_unit_182 OI prophylaxis
    ("curated-phase2_unit_182", "KEEP",
     "MAC prophylaxis at CD4 <100 (azithromycin) and CMV prophylaxis threshold <50 add structured guidance.",
     None),

    # 183 - curated-phase2_unit_183 Antibiotic stewardship principles
    ("curated-phase2_unit_183", "KEEP",
     "Five numbered stewardship principles as a structured teaching framework add educational organization.",
     None),

    # 184 - curated-phase2_unit_184 De-escalation strategy
    ("curated-phase2_unit_184", "DROP_DUP",
     "MGH Manual HAP/VAP section covers de-escalation workflow with same example (score 0.794).",
     None),

    # 185 - curated-phase2_unit_185 Monotherapy vs combination
    ("curated-phase2_unit_185", "KEEP",
     "When combination is justified (severe CAP, shock, local resistance) adds nuanced prescribing guidance.",
     None),

    # 186 - curated-phase2_unit_186 Clinical stability criteria
    ("curated-phase2_unit_186", "KEEP",
     "Specific defervescence >=24-48h, vasopressor-free, normalizing WBC criteria add concrete stopping rules.",
     None),

    # 187 - curated-phase2_unit_187 Fluoroquinolone appropriate use
    ("curated-phase2_unit_187", "KEEP",
     "Specific appropriate vs inappropriate FQ use cases and neuropathy side effect add stewardship teaching value.",
     None),

    # 188 - curated-phase2_unit_188 IV-to-PO transition
    ("curated-phase2_unit_188", "KEEP",
     "Levofloxacin PO = IV equivalence and specific agents with good oral bioavailability add clinical utility.",
     None),

    # 189 - curated-phase2_unit_189 KDIGO AKI staging
    ("curated-phase2_unit_189", "FIX",
     "Stage 2 urine output criterion stated as x16h but KDIGO defines Stage 2 as <0.5 mL/kg/hr for >=12h (not 16h).",
     "AKI (acute kidney injury): abrupt decline in renal function. KDIGO criteria: >=1.5x increase in creatinine within 7 days OR urine output <0.5 mL/kg/hr for 6-12 hours. Stage 1: 1.5-1.9x Cr, output <0.5 mL/kg/hr x 6-12h. Stage 2: 2.0-2.9x Cr, output <0.5 mL/kg/hr x >=12h. Stage 3: >=3x Cr or Cr >=4 or initiation RRT, output <0.3 mL/kg/hr x >=24h. Mortality increases with AKI stage: 2-5% Stage 1, 5-10% Stage 2, 15-25% Stage 3. Risk factors: age, CKD, diabetes, hypotension, nephrotoxic drugs (NSAIDs, ACE-I/ARBs in certain settings, aminoglycosides, contrast)."),

    # 190 - curated-phase2_unit_190 Prerenal AKI
    ("curated-phase2_unit_190", "KEEP",
     "FeNa <1%, BUN/Cr >20, urine sodium <20, urine osmolality >500 criteria and rapid fluid response add value.",
     None),

    # 191 - curated-phase2_unit_191 ATN intrinsic AKI
    ("curated-phase2_unit_191", "KEEP",
     "Oliguric ATN mortality 50-60% vs non-oliguric 5-10% distinction and muddy brown casts specificity add value.",
     None),

    # 192 - curated-phase2_unit_192 Postrenal AKI
    ("curated-phase2_unit_192", "KEEP",
     "Bilateral obstruction required (contralateral compensation) and outcomes with early vs late relief add value.",
     None),

    # 193 - curated-phase2_unit_193 Urinalysis/casts AKI
    ("curated-phase2_unit_193", "KEEP",
     "Crystal morphology (calcium oxalate star-shaped for ethylene glycol) and urine alkalinization rationale add value.",
     None),

    # 194 - curated-phase2_unit_194 Rhabdomyolysis
    ("curated-phase2_unit_194", "KEEP",
     "Urine alkalinization target pH >6.5, CK peaks day 3, and urine output 200-300 mL/hr target add specific value.",
     None),

    # 195 - curated-phase2_unit_195 Medication nephrotoxicity
    ("curated-phase2_unit_195", "KEEP",
     "Extended-interval aminoglycoside dosing (once-daily amikacin 15 mg/kg) reduces nephrotoxicity vs q8h adds value.",
     None),

    # 196 - curated-phase2_unit_196 CIN prevention
    ("curated-phase2_unit_196", "KEEP",
     "N-acetylcysteine controversy (later trials negative) and isotonic saline preference over bicarbonate add current evidence.",
     None),

    # 197 - curated-phase2_unit_197 CRRT vs IHD
    ("curated-phase2_unit_197", "KEEP",
     "CRRT preferred in sepsis/shock rationale (hemodynamic stability) vs IHD for mobile patients adds clinical decision value.",
     None),
]

# Build output list
output = []
for (uid, verdict, reason, corrected) in VERDICTS_DATA:
    entry = {"id": uid, "verdict": verdict, "reason": reason[:160]}
    if corrected:
        entry["corrected_text"] = corrected
    output.append(entry)

# Write output
with open("data/factcheck/batch_1.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Written {len(output)} verdicts to data/factcheck/batch_1.json")

# Count by verdict
counts = {}
for e in output:
    v = e["verdict"]
    counts[v] = counts.get(v, 0) + 1
print("Verdict counts:", counts)
