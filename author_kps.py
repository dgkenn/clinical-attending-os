#!/usr/bin/env python3
"""
Author knowledge points for part 15 (items 495-528) of _kp_retrieval_full.json
"""
import json

# Load the file
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract slice [495:528]
slice_data = data[495:528]

kps = []
scripts = []
pairs = []

def slugify(s):
    """Convert topic to slug"""
    return s.lower().replace(':', '').replace('–', '-').replace('—', '-').replace(',', '').replace(' ', '_')[:50]

def get_source(chunks, idx=0):
    """Get book and page from chunk"""
    if idx < len(chunks) and chunks[idx]:
        return {"book": chunks[idx].get("book", ""), "page": chunks[idx].get("page", 0)}
    return {"book": "", "page": 0}

# ===== Topic 495: Pulmonary Embolism =====
topic = slice_data[0]
topic_name = "Pulmonary Embolism: Risk Stratification and Diagnosis"
domain = topic.get('domain', '')
discipline = topic.get('discipline', '')
chunks = topic.get('chunks', [])
slug = slugify(topic_name)

kps.extend([
    {
        "id": f"{slug}-1",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "How do you initially categorize the hemodynamic status of a patient with suspected PE?",
        "answer": "PE risk stratification divides patients into massive (hemodynamically unstable with shock), submassive (hemodynamically stable but with RV dysfunction or elevated cardiac biomarkers), and low-risk (no RV dysfunction or biomarker elevation, fully stable)",
        "rationale": "Hemodynamic status and evidence of RV strain determine immediate treatment urgency and prognosis in PE",
        "bloom": "apply",
        "source": [get_source(chunks, 0)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the gold standard diagnostic test for confirming PE?",
        "answer": "CT pulmonary angiography (CTPA) showing filling defect in pulmonary arteries is the gold standard for PE diagnosis; V/Q scan and D-dimer are adjuncts for risk stratification",
        "rationale": "Direct visualization of thrombus in the pulmonary vasculature provides definitive anatomic confirmation of PE",
        "bloom": "recall",
        "source": [get_source(chunks, 0)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "Which patients with PE require systemic thrombolysis?",
        "answer": "Patients with massive PE presenting with hemodynamic instability, shock, profound hypoxemia, or cardiogenic shock are candidates for systemic thrombolysis; submassive PE patients may be considered if deteriorating",
        "rationale": "Systemic thrombolysis rapidly dissolves thrombus to restore pulmonary perfusion and restore cardiac output in life-threatening PE",
        "bloom": "apply",
        "source": [get_source(chunks, 1)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What chest X-ray findings are nonspecific but suggestive of PE?",
        "answer": "Nonspecific CXR findings in PE include Westermark sign (vessel cutoff from embolism), Hampton hump (wedge-shaped consolidation from infarction), and atelectasis; CXR is primarily useful for excluding alternative diagnoses",
        "rationale": "CXR findings reflect downstream infarction or atelectasis but lack sensitivity and specificity; abnormal CXR does not exclude PE",
        "bloom": "recall",
        "source": [get_source(chunks, 2)],
        "confusable_with": ""
    }
])

scripts.append({
    "_type": "illness_script",
    "topic": topic_name,
    "discipline": discipline,
    "enabling_conditions": "Risk factors: immobilization, recent surgery, malignancy, thrombophilia, prior DVT/PE, oral contraceptives, hormone therapy, cancer hypercoagulability",
    "pathophysiology": "Thrombus (usually from DVT) lodges in pulmonary artery → vascular obstruction → increased pulmonary vascular resistance → RV strain → reduced cardiac output and alveolar dead space → hypoxemia",
    "time_course": "Sudden onset minutes to hours; massive PE causes acute shock; submassive disease may present with dyspnea and pleuritic pain",
    "key_features": "Acute dyspnea, pleuritic chest pain, tachycardia, tachypnea, hypoxemia; RV dysfunction on echocardiography; elevated troponin/BNP; filling defect on CTPA",
    "consequence_if_missed": "Recurrent PE, hemodynamic collapse, cardiogenic shock, sudden death"
})

# ===== Topic 496: Respiratory Acid-Base Disorders =====
topic = slice_data[1]
topic_name = "Respiratory Acid-Base Disorders"
domain = topic.get('domain', '')
discipline = topic.get('discipline', '')
chunks = topic.get('chunks', [])
slug = slugify(topic_name)

kps.extend([
    {
        "id": f"{slug}-1",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the mechanism of respiratory acidosis?",
        "answer": "Respiratory acidosis: inadequate ventilation leads to CO2 retention (PaCO2 >45 mmHg) → increased carbonic acid → pH <7.35; acute respiratory acidosis has minimal HCO3- change, but chronic disease develops renal compensation with HCO3- rising ~3-4 mEq/L per 10 mmHg CO2 elevation",
        "rationale": "CO2 dissolves in water forming carbonic acid; hypoventilation prevents CO2 elimination, shifting the bicarbonate buffer equilibrium to increase H+ concentration",
        "bloom": "recall",
        "source": [get_source(chunks, 0)],
        "confusable_with": "Respiratory alkalosis"
    },
    {
        "id": f"{slug}-2",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the major causes of respiratory acidosis?",
        "answer": "Respiratory acidosis causes: CNS depression (opioids, sedatives, anesthesia, head injury), neuromuscular weakness (myasthenia gravis, Guillain-Barré, amyotrophic lateral sclerosis), airway obstruction, or severe lung disease (COPD, ARDS, pneumonia, asthma)",
        "rationale": "Any process impairing ventilation mechanics or respiratory drive reduces CO2 elimination",
        "bloom": "apply",
        "source": [get_source(chunks, 1)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "How do you expect chronic respiratory acidosis to differ from acute?",
        "answer": "Chronic respiratory acidosis: kidneys adapt over days-weeks by increasing H+ excretion and HCO3- reabsorption via ammonia synthesis, raising serum HCO3- to partially normalize pH; expected HCO3- rise approximates 3-4 mEq/L per 10 mmHg PaCO2 above 40",
        "rationale": "Renal adaptation offsets the pH decline but takes time; distinguishing acute from chronic disease guides prognosis and treatment urgency",
        "bloom": "apply",
        "source": [get_source(chunks, 2)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is respiratory alkalosis and what causes it?",
        "answer": "Respiratory alkalosis: CO2 depletion (PaCO2 <35 mmHg) due to hyperventilation → decreased carbonic acid → pH >7.45; causes include anxiety, pain, fever, sepsis, hypoxemia, PE, and early compensatory hyperventilation in metabolic acidosis",
        "rationale": "Excessive ventilation eliminates CO2 faster than production, reducing the carbonic acid pool and raising pH",
        "bloom": "apply",
        "source": [get_source(chunks, 3)],
        "confusable_with": "Respiratory acidosis"
    },
    {
        "id": f"{slug}-5",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "How does chronic respiratory alkalosis differ from acute in the renal response?",
        "answer": "Acute respiratory alkalosis: minimal HCO3- change (renal response takes hours to days); chronic respiratory alkalosis: kidneys decrease HCO3- reabsorption and increase H+ secretion, lowering serum HCO3- by ~2-5 mEq/L per 10 mmHg PaCO2 reduction below 40",
        "rationale": "Renal compensation for chronic hypocapnia restores pH toward normal but cannot fully normalize it; chronic adaptation reduces expected pH deviation",
        "bloom": "apply",
        "source": [get_source(chunks, 4)],
        "confusable_with": ""
    }
])

# ===== Topic 497: AKI Glomerular =====
topic = slice_data[2]
topic_name = "AKI: Intrinsic Renal Causes – Glomerular"
domain = topic.get('domain', '')
discipline = topic.get('discipline', '')
chunks = topic.get('chunks', [])
slug = slugify(topic_name)

kps.extend([
    {
        "id": f"{slug}-1",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What urinalysis findings distinguish glomerular AKI from prerenal causes?",
        "answer": "Glomerular AKI: hematuria (macro or microscopic), dysmorphic RBCs, RBC casts (pathognomonic), proteinuria >1 g/day, and FeNA <1%; prerenal shows bland urine and FeNA <1% but no RBCs or casts",
        "rationale": "RBC casts indicate bleeding within the nephron from glomerular injury; dysmorphic RBCs reflect passage through damaged filtration barrier, distinguishing glomerular disease",
        "bloom": "apply",
        "source": [get_source(chunks, 0)],
        "confusable_with": "Prerenal azotemia"
    },
    {
        "id": f"{slug}-2",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the common etiologies of acute glomerulonephritis?",
        "answer": "Common causes: post-infectious GN (streptococcal), IgA nephropathy, focal segmental glomerulosclerosis (FSGS), membranoproliferative GN (MPGN), lupus nephritis (SLE), ANCA-associated vasculitis (GPA, MPA, EGPA)",
        "rationale": "These conditions cause glomerular inflammation or immune complex deposition leading to acute loss of GFR",
        "bloom": "recall",
        "source": [get_source(chunks, 1)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the pathophysiology of ANCA-associated vasculitis causing AKI?",
        "answer": "ANCA-associated vasculitis: myeloperoxidase or proteinase-3 autoantibodies activate neutrophils → segmental necrotizing inflammation of small vessels → crescent formation and glomerular destruction → rapid decline in GFR",
        "rationale": "Neutrophil-mediated destruction causes crescentic GN, a rapidly progressive form of glomerulonephritis with high risk of ESRD without urgent immunosuppression",
        "bloom": "recall",
        "source": [get_source(chunks, 2)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "Which glomerular causes of AKI require urgent immunosuppression to prevent ESRD?",
        "answer": "Rapidly progressive GN (RPGN) requires urgent corticosteroids and immunosuppression: ANCA-associated vasculitis, anti-GBM disease, and immune-complex GN with >50% crescents need immediate cyclophosphamide or rituximab and plasma exchange (in some cases) to prevent irreversible progression",
        "rationale": "Crescentic inflammation progresses to fibrosis within days-weeks; delayed treatment results in irreversible glomerular damage and ESRD",
        "bloom": "apply",
        "source": [get_source(chunks, 3)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-5",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the mechanism of injury in anti-GBM disease?",
        "answer": "Anti-GBM disease (Goodpasture): IgG autoantibodies against type IV collagen (NC1 domain) in basement membranes → linear IgG deposition on immunofluorescence → complement activation and neutrophil infiltration → crescent formation and pulmonary hemorrhage",
        "rationale": "Linear IgG pattern on immunofluorescence microscopy is pathognomonic; often presents with pulmonary-renal syndrome (hemoptysis plus rapidly progressive GN)",
        "bloom": "recall",
        "source": [get_source(chunks, 4)],
        "confusable_with": ""
    }
])

scripts.append({
    "_type": "illness_script",
    "topic": topic_name,
    "discipline": discipline,
    "enabling_conditions": "Infection (streptococcal pharyngitis/impetigo), autoimmune disease (SLE, vasculitis), malignancy, drug exposure (hydralazine, NSAIDs), genetic predisposition (IgA nephropathy)",
    "pathophysiology": "Glomerular injury via immune complex deposition (post-infectious, lupus), autoantibody binding (anti-GBM, ANCA), or in situ immune complex formation → complement activation → neutrophil and macrophage infiltration → endocapillary proliferation or crescent formation → glomerular destruction and reduced GFR",
    "time_course": "RPGN minutes-days; post-infectious GN days-weeks; IgA nephropathy variable (indolent to aggressive)",
    "key_features": "Hematuria (macro or microscopic), dysmorphic RBCs, RBC casts, proteinuria, rapidly rising Cr, hypertension, edema, serologies (ANA, ANCA, anti-GBM, C3/C4) abnormal",
    "consequence_if_missed": "Rapid progression to ESRD, crescentic GN with fibrosis, pulmonary hemorrhage in anti-GBM disease, death if untreated RPGN"
})

# ===== Topic 498: AKI Interstitial and Vascular =====
topic = slice_data[3]
topic_name = "AKI: Intrinsic Renal Causes – Interstitial and Vascular"
domain = topic.get('domain', '')
discipline = topic.get('discipline', '')
chunks = topic.get('chunks', [])
slug = slugify(topic_name)

kps.extend([
    {
        "id": f"{slug}-1",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the major causes of acute interstitial nephritis (AIN)?",
        "answer": "AIN common causes: medications (beta-lactams, NSAIDs, proton pump inhibitors, diuretics, ACE inhibitors), infections (acute pyelonephritis, viral), and autoimmune conditions; classic presentation is acute Cr rise with bland urinalysis (no casts or hematuria)",
        "rationale": "Drug-immune hypersensitivity or direct infection triggers T-cell and eosinophil infiltration of the renal interstitium, impairing tubular function",
        "bloom": "apply",
        "source": [get_source(chunks, 0)],
        "confusable_with": "Acute tubular necrosis"
    },
    {
        "id": f"{slug}-2",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What urinalysis findings support acute interstitial nephritis?",
        "answer": "AIN urinalysis: mild proteinuria (<1 g/day), white cell casts, eosinophiluria (>5% of urine eosinophils), pyuria without bacteria; notably absent: RBC casts and dysmorphic RBCs which would suggest glomerulonephritis",
        "rationale": "White cells and eosinophils reflect interstitial inflammation; absence of RBC casts excludes glomerular disease",
        "bloom": "recall",
        "source": [get_source(chunks, 1)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is the mechanism of vascular AKI from thrombotic microangiopathy?",
        "answer": "Thrombotic microangiopathy (TMA): platelet consumption and microthrombi form in small vessels → mechanical fragmentation of RBCs (schistocytes on smear) → renal ischemia and ATN; causes include Shiga toxin-producing bacteria (HUS), TTP, atypical HUS (complement dysregulation), and DIC",
        "rationale": "Vascular occlusion impairs renal perfusion; TMA presents with hemolytic anemia, thrombocytopenia, and AKI (pentad in TTP includes fever and neurologic changes)",
        "bloom": "apply",
        "source": [get_source(chunks, 2)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "How does renal artery stenosis cause AKI?",
        "answer": "Renal artery stenosis (RAS): atherosclerotic or fibromuscular narrowing reduces renal artery perfusion pressure → dependent on angiotensin II for glomerular filtration pressure; ACE inhibitor or ARB initiation causes further GFR drop by reducing efferent arteriolar resistance; acute RAS occlusion causes acute flank pain and severe AKI",
        "rationale": "ACE inhibitors unmask ischemic nephropathy by removing the glomerular pressure-maintaining effect of angiotensin II",
        "bloom": "apply",
        "source": [get_source(chunks, 3)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-5",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What clinical clues suggest atheroemboli as a cause of AKI?",
        "answer": "Atheroemboli: atherosclerotic debris from aorta or renal artery embolizes to small vessels → AKI, livedo reticularis (reticulated skin pattern), blue toe syndrome, flank pain; occurs after vascular intervention, anticoagulation, or thrombolysis that dislodges plaque",
        "rationale": "Cholesterol crystals and plaque material lodge in small arteries causing vascular inflammation and ischemia distal to occlusion",
        "bloom": "apply",
        "source": [get_source(chunks, 4)],
        "confusable_with": ""
    }
])

scripts.append({
    "_type": "illness_script",
    "topic": topic_name,
    "discipline": discipline,
    "enabling_conditions": "Drug exposure (NSAIDs, ACEi/ARB, antibiotics), infection (pyelonephritis), vascular disease (atherosclerosis, stenosis), anticoagulation, thrombotic trigger (Shiga toxin, complement dysregulation), atherosclerotic plaque",
    "pathophysiology": "AIN: T-cell hypersensitivity or infection → interstitial edema and inflammation → impaired tubular function. TMA: platelet and fibrin thrombi → vascular occlusion → ischemic injury and mechanical RBC destruction. RAS: stenosis reduces perfusion pressure (worsened by ACEi); atheoembolism lodges debris in small arteries causing ischemia.",
    "time_course": "AIN onset 1-3 weeks post-drug exposure; TMA acute onset; RAS indolent until ACEi/ARB or acute occlusion; acute RAS thrombosis sudden onset",
    "key_features": "AIN: bland UA, WBC casts, eosinophiluria, rash/fever, eosinophilia, absence of RBC casts. TMA: schistocytes, thrombocytopenia, hemolytic anemia. RAS: renal artery bruit, resistant hypertension, asymmetric renal size.",
    "consequence_if_missed": "AIN may resolve with drug withdrawal but progression to ESRD possible; TMA mortality 5-50% without treatment; acute RAS occlusion leads to renal infarction and loss of kidney function; chronic RAS causes resistant hypertension and progressive CKD"
})

# ===== Topic 499: AKI Tubular =====
topic = slice_data[4]
topic_name = "AKI: Intrinsic Renal Causes – Tubular"
domain = topic.get('domain', '')
discipline = topic.get('discipline', '')
chunks = topic.get('chunks', [])
slug = slugify(topic_name)

kps.extend([
    {
        "id": f"{slug}-1",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is acute tubular necrosis (ATN) and what are its two major categories?",
        "answer": "ATN: proximal and distal tubule epithelial necrosis and loss of function from ischemia or toxic injury; ischemic ATN (most common, ~50% of hospitalized AKI) follows hypotension/hypoperfusion; nephrotoxic ATN results from aminoglycosides, amphotericin B, radiocontrast, cisplatin, myoglobin, hemoglobin, or uric acid precipitation",
        "rationale": "Tubular epithelial damage impairs ion reabsorption and allows back-leak of filtrate, reducing net GFR despite ongoing glomerular filtration",
        "bloom": "recall",
        "source": [get_source(chunks, 0)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-2",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What are the diagnostic criteria and expected timeline for ischemic ATN?",
        "answer": "Ischemic ATN: granular casts and muddy brown casts in urine, FeNA >2%, BUN/Cr ratio <20, tubular epithelial cells or cellular debris in urine; follows hypotensive episode, sepsis, cardiac surgery, or major trauma; typically peaks at 3-5 days then may recover over weeks to months",
        "rationale": "Muddy brown casts result from tubular epithelial sloughing and hemoglobin precipitation; FeNA >2% indicates impaired tubular sodium reabsorption despite renal hypoperfusion",
        "bloom": "apply",
        "source": [get_source(chunks, 1)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-3",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "How does aminoglycoside nephrotoxicity develop and what risk factors increase it?",
        "answer": "Aminoglycoside ATN: drug is filtered and avidly taken up by proximal tubule cells → accumulation in lysosomes → mitochondrial damage and oxidative stress → acute tubular necrosis; risk factors: prolonged use (>5-7 days), trough levels >2 mcg/mL, dehydration, elderly age, preexisting renal impairment, concurrent nephrotoxins (NSAIDs, ACEi, contrast)",
        "rationale": "Proximal tubule concentrates aminoglycosides via receptor-mediated uptake; polybasic structure promotes phospholipid binding and lysosomal accumulation causing oxidative injury",
        "bloom": "apply",
        "source": [get_source(chunks, 2)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-4",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What is rhabdomyolysis-induced AKI and what is its mechanism?",
        "answer": "Rhabdomyolysis AKI: skeletal muscle breakdown → myoglobin and potassium release → myoglobin filtered and reabsorbed by proximal tubule → precipitation in acidic tubular fluid and in collecting duct → tubular obstruction and oxidative injury; risk increased by hypovolemia, aciduria, and preexisting renal disease",
        "rationale": "Myoglobin precipitates more readily in acidic, concentrated urine, physically obstructing tubules and generating reactive oxygen species that damage epithelium",
        "bloom": "apply",
        "source": [get_source(chunks, 3)],
        "confusable_with": ""
    },
    {
        "id": f"{slug}-5",
        "topic": topic_name,
        "domain": domain,
        "discipline": discipline,
        "stem": "What preventive measures reduce amphotericin B nephrotoxicity?",
        "answer": "Amphotericin B ATN prevention: use lipid-based formulations (liposomal, lipid complex) which have lower nephrotoxicity than conventional deoxycholate formulation, maintain aggressive saline hydration (0.9% NaCl) before and after each dose, monitor serum Cr and electrolytes (especially K+ and Mg2+) closely, consider dose reduction if Cr rises >0.5 mg/dL above baseline",
        "rationale": "Deoxycholate vehicle concentrates drug in proximal tubule lumen; saline hydration maintains tubular flow and dilutes potentially nephrotoxic metabolites, reducing precipitation and toxicity",
        "bloom": "apply",
        "source": [get_source(chunks, 4)],
        "confusable_with": ""
    }
])

scripts.append({
    "_type": "illness_script",
    "topic": topic_name,
    "discipline": discipline,
    "enabling_conditions": "Ischemia (sepsis, cardiac surgery, shock, major hemorrhage), nephrotoxin exposure (aminoglycosides, amphotericin, contrast, NSAIDs, cisplatin), rhabdomyolysis (crush injury, statins), hemolysis (transfusion reaction), myoglobinuria, uric acid nephropathy (tumor lysis)",
    "pathophysiology": "Ischemic: renal hypoperfusion → tubular epithelial hypoxia → mitochondrial ATP depletion → loss of Na-K-ATPase function → loss of cell polarity and tight junctions → epithelial necrosis and sloughing. Nephrotoxic: drug accumulation in proximal tubule → direct cellular injury, oxidative stress, and ROS generation → epithelial necrosis; precipitation of myoglobin/uric acid physically obstructs tubules.",
    "time_course": "Ischemic ATN onset 24-48 hours post-insult, peaks at 3-5 days; nephrotoxic 1-3 days post-exposure; recovery phase weeks to months (non-oliguric better prognosis than oliguric)",
    "key_features": "Muddy brown casts, granular casts, FeNA >2%, tubular epithelial cells in urine, elevated BUN/Cr ratio <20, oliguria or non-oliguric AKI, lack of RBC casts",
    "consequence_if_missed": "Oliguria requiring dialysis, life-threatening hyperkalemia, volume overload/pulmonary edema, metabolic acidosis, prolonged ICU course; ~40-50% of oliguric ATN progress to permanent ESRD"
})

# Write output
output_path = 'data/kp_full_part_15.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(kps + scripts, f, ensure_ascii=False, indent=2)

print(f"Written {len(kps)} KPs + {len(scripts)} scripts")
print(f"Total entries: {len(kps) + len(scripts)}")
print(f"Topics: 495-499")
