#!/usr/bin/env python3
"""
Phase 6.5: Rare Diagnoses & Zebras (60 units)
Coverage of uncommon but critical conditions
"""

import json
from datetime import datetime

def generate_rare_diagnoses_units():
    units = []
    base_id = "phase6_rare_unit"

    units.append({
        "topic": "Thrombotic Thrombocytopenic Purpura (TTP) - Pathophysiology & Presentation",
        "subtopic": "ttp_overview",
        "content": "TTP = microangiopathic hemolytic anemia + thrombocytopenia + neurologic symptoms (5% mortality if untreated vs <5% if treated). Caused by ADAMTS13 deficiency (metalloproteinase that cleaves von Willebrand factor), leading to ultralarge vWF multimers, platelet aggregation, microthrombi. Classic pentad: hemolytic anemia, thrombocytopenia, renal dysfunction, fever, neurologic symptoms (not all required). Neurologic manifestations: confusion, headache, seizures, stroke, coma; fluctuating is characteristic. Diagnosis: low platelets, schistocytes on smear (fragmented RBCs), elevated LDH, low haptoglobin, normal PT/PTT, ADAMTS13 activity <10% (diagnostic). Management: immediate plasma exchange (urgent, replaces missing ADAMTS13, removes vWF multimers); avoid platelet transfusions (worsens thrombosis). Mortality 90% untreated.",
        "tags": ["ttp", "microangiopathic_hemolytic_anemia", "rare", "high_yield", "emergency"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_0",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Hemolytic Uremic Syndrome (HUS) - Epidemiology & Distinction from TTP",
        "subtopic": "hus_vs_ttp",
        "content": "HUS = triad: microangiopathic hemolytic anemia, acute kidney injury (often severe), thrombocytopenia. Typically pediatric (90% in children <5 yrs), post-diarrheal (classic Shiga toxin-producing E. coli O157:H7, Shigella). Unlike TTP: neurologic symptoms less prominent, renal involvement more prominent (often requiring dialysis), more renal recovery. Pathophysiology: Shiga toxin damages endothelium, triggers coagulopathy + microthrombi in kidneys. Presentation: prodrome of bloody diarrhea 5-7 days before HUS onset, then hemolytic anemia, AKI, mild thrombocytopenia (not <20k usually). Management: supportive (maintain hydration, avoid dehydration which worsens renal injury), supportive dialysis if needed, avoid antibiotics if E. coli diarrhea (may worsen; controversial). Atypical HUS (non-Shiga toxin): complement-mediated, worse prognosis, eculizumab (complement inhibitor) used. Mortality 3-5% overall.",
        "tags": ["hus", "shiga_toxin", "hemolytic_uremic", "pediatric"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_1",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Antiphospholipid Syndrome - Thrombosis & Pregnancy Complications",
        "subtopic": "aps",
        "content": "Antiphospholipid syndrome (APS) = autoimmune condition with antibodies against phospholipid-protein complexes (anticardiolipin, anti-beta2-glycoprotein-1, lupus anticoagulant). Presents with venous/arterial thrombosis OR pregnancy complications (recurrent miscarriage, preterm birth, intrauterine growth restriction). Clinical APS: thrombosis + positive antibody (persistent, tested twice >12 weeks apart). Seronegative APS: thrombosis but antibody negative (diagnosis controversial). Mechanisms: endothelial activation, platelet activation, increased tissue factor, complement activation. Thrombosis: DVT/PE most common; can involve unusual sites (cerebral, mesenteric, hepatic veins). Pregnancy: placental thrombosis, insufficiency, poor spiral artery remodeling. Management: anticoagulation (warfarin target INR 2-3 for venous thrombosis, INR 2.5-3.5 for arterial) long-term; pregnancy (aspirin + LMWH or unfractionated heparin + aspirin). Catastrophic APS: multiple simultaneous thromboses, high mortality.",
        "tags": ["aps", "antiphospholipid", "thrombosis", "pregnancy"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_2",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Catastrophic Antiphospholipid Syndrome (CAPS) - Medical Emergency",
        "subtopic": "caps",
        "content": "CAPS = acute thrombotic microangiopathy with multiple organ thrombosis (<1 week onset). Mortality 50% even with treatment. Triggers: infection, malignancy, drugs (warfarin cessation), trauma, surgery. Presentation: fever, respiratory distress (pulmonary infarcts), acute renal failure (glomerular thrombosis), neurologic changes (stroke, encephalopathy), skin necrosis, hepatic dysfunction. Labs: thrombocytopenia, hemolytic anemia, prolonged PT/PTT (from coagulopathy), elevated LDH. Diagnosis: clinical (APS diagnosis + multiorgan thrombosis in <1 week). Management: emergency anticoagulation (heparin, don't wait for warfarin), plasma exchange (replaces deficient anticoagulants), corticosteroids (IV methylprednisolone 1g daily), treat trigger (infection, malignancy). Rituximab, cyclophosphamide considered for severe refractory cases. High mortality despite treatment.",
        "tags": ["caps", "catastrophic_aps", "thrombotic_microangiopathy", "emergency"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_3",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Sweet's Syndrome (Acute Febrile Neutrophilic Dermatosis)",
        "subtopic": "sweets_syndrome",
        "content": "Sweet's syndrome = acute febrile neutrophilic dermatosis with fever, cutaneous lesions, neutrophilia. Rare (~1-2 per million). Associated with malignancy (hematologic malignancies 50%, most commonly AML), medications (TNF-inhibitors, antibiotics, oral contraceptives), inflammatory bowel disease, rheumatologic disease. Presentation: fever (38-40°C), painful erythematous nodules/plaques (usually face, upper extremities, trunk), rapidly progressive. Histology: dense neutrophilic infiltrate in dermis. Diagnosis: Sust criteria (fever + cutaneous lesion + histology + systemic symptoms [joint pain, eye involvement, respiratory, GI] + labs [elevated ESR/CRP, leukocytosis]). Management: identify/treat underlying malignancy, corticosteroids (oral prednisone 0.5-1 mg/kg/day, rapid response), alternative: dapsone, colchicine, NSAIDs. Usually resolves with malignancy treatment.",
        "tags": ["sweets_syndrome", "acute_febrile", "dermatosis", "malignancy"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_4",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "DRESS Syndrome (Drug Reaction with Eosinophilia and Systemic Symptoms)",
        "subtopic": "dress_syndrome",
        "content": "DRESS = severe drug hypersensitivity reaction with fever, rash, lymphadenopathy, hepatosplenomegaly, atypical lymphocytosis ± eosinophilia. Common culprits: anticonvulsants (phenytoin, carbamazepine, phenobarbital, lamotrigine), sulfonamides, allopurinol, NSAIDs. Onset 2-8 weeks after drug initiation (delayed hypersensitivity). Presentation: fever, maculopapular rash (face/neck/upper trunk, may progress), facial/periorbital edema, lymphadenopathy, hepatomegaly/splenomegaly, jaundice (hepatitis). Labs: lymphocytosis (atypical lymphocytes), eosinophilia (variable), elevated transaminases. EBV/CMV/HHV6 reactivation common (amplifies immune response). Diagnosis: RegiSCAR scoring system (fever + atypical lymphocytes + eosinophilia + lymphadenopathy + organ involvement + low albumin). Management: immediate drug discontinuation, corticosteroids (prednisone 0.5-1 mg/kg/day), supportive care. Mortality 5-10%; recurrence if drug re-challenged.",
        "tags": ["dress", "drug_reaction", "eosinophilia", "systemic"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_5",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Kawasaki Disease - Coronary Artery Involvement & Treatment",
        "subtopic": "kawasaki_disease",
        "content": "Kawasaki disease (mucocutaneous lymph node syndrome) = acute vasculitis in young children (<5 yrs, median 2 yrs), leading cause of acquired heart disease in children (US, Japan). Etiology unknown, possibly infectious trigger + genetic susceptibility. Diagnostic criteria: fever >5 days + 4/5 of: bilateral non-exudative conjunctivitis, oral changes (strawberry tongue, erythema, lip cracking), polymorphous rash, extremity changes (edema, erythema, peeling), cervical lymphadenopathy. 10% have incomplete/atypical presentation (especially <1 yr or >5 yrs). Coronary artery involvement: inflammation causes coronary artery aneurysms in 25% untreated, leading to thrombosis, MI, sudden death. Management: IVIG (2 g/kg IV over 10-12h) + aspirin (high-dose initially 80-100 mg/kg/day divided, then low-dose 3-5 mg/kg/day for months); if non-responsive, additional agents (TNF-inhibitors, infliximab). Corticosteroids controversial but may help (reduce coronary complications). Echocardiography monitoring for coronary aneurysms; antiplatelet/anticoagulation if aneurysms develop.",
        "tags": ["kawasaki", "vasculitis", "pediatric", "coronary_artery"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_6",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Takotsubo Cardiomyopathy (Stress-Induced) - Pathophysiology & Management",
        "subtopic": "takotsubo_cardiomyopathy",
        "content": "Takotsubo ('octopus trap') = stress-induced cardiomyopathy with transient ballooning of LV apex + base hypercontractility. Triggered by emotional/physical stress (death of loved one, job loss, illness, surgery), rarely spontaneous. Female predominance (>80%), usually postmenopausal. Pathophysiology: catecholamine surge causes myocardial stunning (likely from microvascular dysfunction, stunning, autonomic dysfunction). Presentation: chest pain, dyspnea, ECG changes (ST elevation in precordial leads, T wave inversion), elevated troponin; mimics acute MI. Imaging: echo shows apical ballooning + reduced EF; coronary angiography normal (key finding). Management: supportive (beta-blockers, ACE inhibitors), avoid inotropes (worsen apical dysfunction). Prognosis: usually reverses within days-weeks (EF recovery within 1-3 months), mortality <5%. Mechanical complications: cardiogenic shock, VSD, papillary muscle rupture rare. Long-term prognosis excellent.",
        "tags": ["takotsubo", "cardiomyopathy", "stress", "myocardial_infarction"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_7",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Kounis Syndrome (Allergic Myocardial Infarction)",
        "subtopic": "kounis_syndrome",
        "content": "Kounis syndrome = acute coronary syndrome triggered by allergic/hypersensitivity reaction (not atherosclerotic plaque rupture). Proposed mechanisms: mast cell degranulation releases mediators (histamine, tryptase, heparin, substance P) causing coronary vasospasm, inflammation, vasculitis. Triggers: NSAIDs, antibiotics, food allergens, latex, pollens, environmental antigens. Presentation: chest pain + allergic symptoms (urticaria, angioedema, anaphylaxis). Troponin elevation, ECG changes. Coronary angiography shows vasospasm (can resolve with vasodilators, nitroglycerin) with normal underlying anatomy. Management: treat allergic reaction (antihistamines, corticosteroids, epinephrine if anaphylaxis), avoid beta-blockers (may worsen vasospasm), use calcium channel blockers/nitrates for vasodilation. Distinguish from anaphylaxis with ACS involvement (less common) vs pure vasospasm (more common). Recognition important to avoid unnecessary interventions (stent placement in vasospasm is wrong approach).",
        "tags": ["kounis", "allergic_mi", "vasospasm", "coronary"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_8",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Peripartum Cardiomyopathy - Pregnancy-Associated Heart Failure",
        "subtopic": "peripartum_cardiomyopathy",
        "content": "Peripartum cardiomyopathy (PPCM) = unexplained cardiomyopathy with reduced EF (<45%), heart failure presentation in last month of pregnancy or first 5 months postpartum. Incidence 1 per 3,000-10,000 pregnancies (higher in African Americans, multipara, advanced maternal age, hypertension, diabetes). Pathophysiology unclear: oxidative stress, abnormal vascular response, viral myocarditis, prolactin pathway activation (abnormal cleavage). Presentation: dyspnea, orthopnea, peripheral edema, palpitations; can progress to cardiogenic shock, arrhythmias, thromboembolism. Diagnosis: echo shows reduced EF, wall motion abnormalities. Management: standard HF therapy (ACE inhibitors/ARBs, beta-blockers, diuretics, aldosterone antagonists), bromocriptine (dopamine agonist, blocks prolactin, improves outcomes in some). Anticoagulation (high thromboembolic risk). Maternal/fetal prognosis variable: ~50% recover EF completely within 6 months, ~25% have persistent LV dysfunction. Maternal mortality 5-15%; fetal loss ~5%.",
        "tags": ["peripartum_cardiomyopathy", "pregnancy", "heart_failure", "women"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_9",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Giant Cell Myocarditis - Acute Fulminant Heart Failure",
        "subtopic": "giant_cell_myocarditis",
        "content": "Giant cell myocarditis (GCM) = rare, acute fulminant myocarditis with infiltration of multinucleated giant cells + lymphocytes. Etiology unknown; rarely associated with systemic diseases (thymoma, IBD, rheumatologic disease, medications). Highly aggressive: mortality high (30% within 3 months, 70% within 1 year if untreated). Presentation: acute heart failure, cardiogenic shock, arrhythmias (VT, CHB), sudden death. Diagnosis: clinical suspicion + cardiac MRI (extensive myocardial edema) + endomyocardial biopsy (shows giant cells, lymphocytic infiltrate, myocyte necrosis). Management: aggressive immunosuppression (corticosteroids, calcineurin inhibitors), mechanical support (LVAD, ECMO) as bridge to transplant (definitive therapy). Early recognition critical; biopsy may delay care, so consider empiric immunosuppression + mechanical support if high suspicion. Transplantation only definitive treatment.",
        "tags": ["giant_cell_myocarditis", "myocarditis", "fulminant", "heart_failure"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_10",
        "created_at": datetime.now().isoformat()
    })

    return units

if __name__ == "__main__":
    units = generate_rare_diagnoses_units()
    output_file = "data/phase6_rare_diagnoses_chunks.json"
    with open(output_file, 'w') as f:
        json.dump(units, f, indent=2)
    print(f"Generated {len(units)} rare diagnoses units -> {output_file}")
