
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/kp_redeep_part11c_partial.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# ============================================================
# ITEM 383: IBD Extraintestinal Manifestations
# ============================================================
topic = "IBD Extraintestinal Manifestations"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"ibd-extraintestinal-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What extraintestinal manifestations of IBD are listed as clinical findings that can indicate IBD presence?",
   "answer":"Uveitis, erythema nodosum, oral ulcers, inflammatory arthritis, and pyoderma gangrenosum are extraintestinal manifestations of IBD.",
   "rationale":"EIMs result from shared immune dysregulation; some (peripheral arthritis, erythema nodosum) parallel intestinal disease activity while others (uveitis, axial arthritis) are independent.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Behcet disease","page":7}],
   "confusable_with":"Behcet disease (shares many EIMs but caused by systemic vasculitis; differs in pathogenesis and ethnicity)"},

  {"id":"ibd-extraintestinal-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Evidence of extraintestinal manifestations in a patient with GI symptoms can indicate presence of what underlying diagnosis?",
   "answer":"Evidence of extraintestinal manifestations (joint, skin, eye, liver disease) can indicate the presence of inflammatory bowel disease.",
   "rationale":"EIMs precede, coincide with, or follow intestinal symptoms; their recognition can prompt IBD workup before overt GI disease manifests.",
   "bloom":"apply",
   "source":[{"book":"StatPearls","page":5}],
   "confusable_with":"systemic autoimmune diseases (RA, SLE; can have overlapping EIMs)"},

  {"id":"ibd-extraintestinal-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Patients with IBD (including Crohn's) may present with low back pain and what pattern of spondyloarthropathy?",
   "answer":"IBD patients may have IBD-associated spondyloarthropathy with low back pain (sacroiliitis, ankylosing spondylitis); extraspinal manifestations (GI, ocular, cutaneous) are usually more prominent.",
   "rationale":"IBD-associated spondylitis is HLA-B27 associated; anti-TNF therapy addresses both bowel disease and joint disease.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1745}],
   "confusable_with":"primary ankylosing spondylitis (axial disease dominant; IBD less common)"},

  {"id":"ibd-extraintestinal-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Anti-TNF-alpha agents used in IBD can cause what autoimmune adverse effect?",
   "answer":"TNF-alpha inhibitors (etanercept, infliximab, adalimumab, golimumab) can cause drug-induced lupus (DIL) with subacute cutaneous lupus or SLE-like features.",
   "rationale":"Anti-TNF agents induce autoantibodies (ANA, anti-dsDNA) in a subset of patients; DIL usually resolves upon drug discontinuation.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Drug induced lupus","page":3}],
   "confusable_with":"classic SLE (anti-dsDNA titre higher, organ involvement more severe; DIL usually milder)"},

  {"id":"ibd-extraintestinal-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Behcet disease shares multiple features with IBD; what distinguishes them?",
   "answer":"Behcet disease is a systemic vasculitis (not IBD) with similar EIMs (uveitis, oral/genital ulcers, articular, GI); it differs in pathogenesis (vasculitis), ethnicity (Silk Road distribution), and pathergy test.",
   "rationale":"Distinguishing Behcet from IBD is clinically important because GI Behcet may involve ileocecal lesions with perforation risk, and treatment differs.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Behcet disease","page":7}],
   "confusable_with":"Crohn's disease (both cause ileocecal ulcers and EIMs)"},

  {"id":"ibd-extraintestinal-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Genetic predisposition in IBD is linked to what risk factors?",
   "answer":"IBD genetic risk factors include positive family history and other autoimmune diseases; female sex and Jewish/white ethnicity increase risk; incidence is increasing in non-white populations.",
   "rationale":"NOD2/CARD15 mutations (Crohn's) and other immune-related genes increase susceptibility; environmental factors (Western diet, antibiotics, NSAIDs) interact with genetic predisposition.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":81}],
   "confusable_with":""},

  {"id":"ibd-extraintestinal-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Immune checkpoint inhibitors can cause immune-related adverse events including what IBD-like GI manifestation?",
   "answer":"ICIs cause irAEs including gastrointestinal disturbance (colitis/diarrhea as second most frequent irAE) with features indistinguishable from IBD; may require steroids or infliximab.",
   "rationale":"Anti-CTLA-4 causes colitis in up to 30% of patients; anti-PD-1/PDL-1 causes colitis in ~15%; mechanism is similar to IBD pathogenesis.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Acute Kidney Injury (AKI) in ICU","page":3}],
   "confusable_with":"infectious colitis (must exclude before immunosuppression in ICI colitis)"},
]
output.extend(kps)

# ============================================================
# ITEM 384: Idiopathic Pulmonary Fibrosis
# ============================================================
topic = "Idiopathic Pulmonary Fibrosis"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"ipf-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"IPF is listed as an indication for isolated lung transplantation. What other diseases share this indication?",
   "answer":"Cystic fibrosis, COPD, alpha-1 antitrypsin deficiency, pulmonary lymphangiomatosis, and primary pulmonary hypertension are other indications for isolated lung transplantation.",
   "rationale":"IPF leads to end-stage restrictive respiratory failure; lung transplantation is the only survival-extending intervention beyond antifibrotic therapy.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":925}],
   "confusable_with":""},

  {"id":"ipf-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"The GAP scoring system in IPF helps with what specific clinical decision, and what does a higher score indicate?",
   "answer":"GAP (Gender, Age, Physiology) score stratifies mortality risk and guides lung transplant referral; higher GAP score indicates worse mortality prognosis.",
   "rationale":"GAP integrates sex, age, FVC, and DLco to predict 1-, 2-, and 3-year mortality; patients with high GAP should be referred early for transplant evaluation.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Idiopathic Pulmonary Fibrosis","page":9}],
   "confusable_with":"BODE index (COPD-specific; different variables)"},

  {"id":"ipf-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What causes of pulmonary fibrosis must be excluded before diagnosing IPF?",
   "answer":"Hypersensitivity pneumonitis (occupational/environmental), drug toxicity (bleomycin, nitrofurantoin), radiation pneumonitis, autoimmune diseases, and sarcoidosis must be excluded.",
   "rationale":"IPF is a diagnosis of exclusion in the UIP pattern; CTD-ILD, HP, and drug-ILD require different management and have different prognoses.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":875}],
   "confusable_with":"UIP pattern from other causes (same HRCT pattern; history differentiates)"},

  {"id":"ipf-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What patient behaviors and interventions are essential for IPF management beyond antifibrotic medications?",
   "answer":"Smoking cessation, allergen avoidance, medication adherence, physical therapy to preserve lung function, and early lung transplant referral and workup are essential.",
   "rationale":"Smoking accelerates fibrosis; physical therapy maintains functional capacity; early transplant referral ensures patients are listed before deteriorating below transplant eligibility.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Idiopathic Pulmonary Fibrosis","page":13}],
   "confusable_with":""},

  {"id":"ipf-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the 6-minute walk test used to assess in ILD specialty centers?",
   "answer":"The 6-minute walk test assesses functional status and screens for hypoxic respiratory failure in ILD; it provides objective exercise capacity measurement for transplant evaluation.",
   "rationale":"Desaturation during 6MWT identifies exertional hypoxemia and correlates with mortality in IPF; serial testing tracks disease progression.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Idiopathic Pulmonary Fibrosis","page":9}],
   "confusable_with":""},

  {"id":"ipf-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ILD presents with what classic triad of symptoms?",
   "answer":"ILD typically presents with progressive dyspnea, nonproductive cough, and hypoxemia (especially with exercise); velcro-like crackles and clubbing may be present on examination.",
   "rationale":"Fibrotic lung disease reduces lung compliance and diffusion capacity, causing exertional dyspnea; the nonproductive cough reflects parenchymal irritation without airway secretions.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":53}],
   "confusable_with":""},

  {"id":"ipf-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What preoperative management is needed for a patient with a large pleural effusion or massive ascites before anesthesia?",
   "answer":"Large pleural effusions should typically be drained before anesthesia; massive ascites should be relieved by nasogastric suction or drainage; persistent hypoxemia may require mechanical ventilation.",
   "rationale":"Pleural effusion and ascites compress lung parenchyma, reducing FRC and worsening hypoxemia during anesthesia-induced changes in respiratory mechanics.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":875}],
   "confusable_with":""},
]
output.extend(kps)

script = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Age >60, male sex, smoking history, environmental exposures (metal/wood dust); no identifiable cause by definition; UIP pattern on HRCT",
  "pathophysiology":"Aberrant wound healing response: recurrent alveolar epithelial micro-injury triggers fibroblast activation and collagen deposition; TGF-beta central mediator",
  "time_course":"Progressive, irreversible; median survival 3-5 years from diagnosis; acute exacerbations carry 50% mortality; antifibrotics (pirfenidone, nintedanib) slow decline",
  "key_features":"Dry velcro crackles at lung bases, clubbing, restrictive pattern (reduced TLC/FVC/DLco), UIP on HRCT (basal, peripheral honeycombing with/without traction bronchiectasis)",
  "consequence_if_missed":"Missed window for antifibrotic therapy; delayed lung transplant referral when patient deteriorates below eligibility; acute exacerbation without ICU-level monitoring"}
output.append(script)

# ============================================================
# ITEM 385: Immune checkpoint inhibitor toxicities (irAEs)
# ============================================================
topic = "Immune checkpoint inhibitor toxicities (immune-related adverse events)"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
discipline = "medicine"

kps = [
  {"id":"ici-toxicities-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the three most common irAE categories in frequency order for anti-CTLA-4 and anti-PD-1/PD-L1 agents?",
   "answer":"Most common: (1) skin (itching/rash); (2) gastrointestinal (diarrhea/colitis); (3) endocrine (thyroid dysfunction, hypopituitarism) irAEs.",
   "rationale":"Anti-CTLA-4 causes colitis in up to 30%; anti-PD-1/PD-L1 more commonly causes thyroid dysfunction; combined therapy produces highest irAE rates.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Acute Kidney Injury (AKI) in ICU","page":3}],
   "confusable_with":""},

  {"id":"ici-toxicities-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ICI therapy can trigger acute seronegative myasthenia gravis. Which specific agents are implicated?",
   "answer":"Nivolumab, pembrolizumab, and ipilimumab have been associated with acute seronegative myasthenia gravis as an irAE.",
   "rationale":"ICI-induced MG results from T-cell attack on acetylcholine receptors; seronegative because traditional AChR antibodies may be absent.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1028}],
   "confusable_with":"Lambert-Eaton syndrome (also associated with malignancy but presynaptic; different exam findings)"},

  {"id":"ici-toxicities-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ICI-associated diabetes mellitus (ICI-DM) presents how and what distinguishes it from type 2 diabetes?",
   "answer":"ICI-DM typically presents with no prior diabetes history; it often presents abruptly like type 1 diabetes (DKA) with absolute insulin deficiency, unlike gradual T2DM onset.",
   "rationale":"ICI-induced autoimmune destruction of beta cells causes type 1-like diabetes; patients may present in DKA requiring insulin permanently.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Diabetic Ketoacidosis (DKA)","page":3}],
   "confusable_with":"type 2 DM (gradual onset, insulin resistance predominant, rarely presents with DKA)"},

  {"id":"ici-toxicities-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ICI-associated AKI typically presents in patients receiving anti-CTLA-4 therapy with what histological pattern?",
   "answer":"ICI-associated AKI most commonly presents as acute tubulointerstitial nephritis (ATIN) in patients receiving anti-CTLA-4 therapy (ipilimumab); immune-mediated T-cell infiltration of renal tubules.",
   "rationale":"Checkpoint inhibitors activate T-cells that attack self-antigens in renal tubules; treatment requires stopping the ICI and administering high-dose corticosteroids.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":1}],
   "confusable_with":"chemotherapy nephrotoxicity (different mechanism; tubular toxicity from cisplatin, not immune infiltration)"},

  {"id":"ici-toxicities-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ICI therapy can induce SLE-like disease and subacute cutaneous lupus. What is the mechanism?",
   "answer":"PD-1 and PD-L1 inhibitors can cause irAEs including subacute cutaneous lupus and SLE-like features through T-cell disinhibition leading to autoantibody production.",
   "rationale":"Checkpoint inhibition removes tolerance mechanisms that normally suppress autoreactive T and B cells, enabling anti-nuclear antibody and anti-dsDNA production.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Drug induced lupus","page":3}],
   "confusable_with":"classic SLE (anti-dsDNA very high, multi-organ involvement; ICI lupus milder)"},

  {"id":"ici-toxicities-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the mechanism of action of immune checkpoint inhibitors in cancer therapy?",
   "answer":"ICIs block receptors that downregulate T-cell activation: anti-CTLA-4, anti-PD-1 (on T-cells), or anti-PD-L1 (on cancer cells), thereby enhancing antitumor immune response.",
   "rationale":"Tumors exploit CTLA-4 and PD-1/PD-L1 pathways to evade immune destruction; blocking these checkpoints restores T-cell cytotoxic activity against tumor cells.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":159}],
   "confusable_with":""},

  {"id":"ici-toxicities-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Drug-induced lupus was historically caused by which medications, and how has the spectrum expanded?",
   "answer":"Classic DIL causes: hydralazine, procainamide, methyldopa, isoniazid, chlorpromazine, carbamazepine; expanded spectrum now includes TNF-alpha inhibitors and immune checkpoint inhibitors.",
   "rationale":"The expanded DIL spectrum reflects the proliferation of biologics; drug-induced mechanisms differ from classic DIL (more histone Ab in classic; anti-dsDNA in biologic-induced).",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Drug induced lupus","page":3}],
   "confusable_with":"idiopathic SLE (anti-dsDNA very high; complement low; renal involvement; doesn't remit with drug stop)"},
]
output.extend(kps)

script2 = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Cancer patients receiving anti-CTLA-4 (ipilimumab), anti-PD-1 (nivolumab, pembrolizumab), or anti-PD-L1 (atezolizumab); combination ICI highest risk",
  "pathophysiology":"Checkpoint blockade removes T-cell tolerance; autoreactive T-cells attack normal tissues causing organ-specific inflammation; mechanisms parallel to autoimmune disease",
  "time_course":"Skin and GI irAEs: early (weeks); endocrine irAEs: weeks to months (often permanent); neurological irAEs: variable; renal irAEs: months",
  "key_features":"Skin rash, colitis/diarrhea, thyroid dysfunction, hypophysitis, pneumonitis, hepatitis, nephritis; skin and GI irAEs most common; severity grades 1-4 guide management",
  "consequence_if_missed":"Grade 3-4 irAEs can be fatal (ICI pneumonitis, myocarditis, encephalitis); inadequate corticosteroid dosing fails to control irAEs; permanent endocrine deficiencies if not replaced"}
output.append(script2)

# ============================================================
# ITEM 386: Interstitial Lung Disease: Connective Tissue Disease
# ============================================================
topic = "Interstitial Lung Disease: Connective Tissue Disease"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"ctd-ild-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ILD can occur in connective tissue disease. What major ILD subtypes must be differentiated from CTD-ILD based on HRCT and histology?",
   "answer":"IPF (UIP pattern), CTD-ILD, hypersensitivity pneumonitis, and sarcoidosis must be differentiated using clinical history, HRCT patterns, and histopathology.",
   "rationale":"Treatment differs fundamentally: IPF uses antifibrotics; CTD-ILD and HP may respond to immunosuppression; sarcoidosis uses steroids.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":2}],
   "confusable_with":"IPF (UIP pattern may be identical; requires clinical/serological differentiation)"},

  {"id":"ctd-ild-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Undifferentiated connective tissue disease (UCTD) shares clinical features with which established CTDs?",
   "answer":"UCTD shares clinical features with SLE and rheumatoid arthritis; precise clinical practice guidelines for UCTD are not yet defined.",
   "rationale":"UCTD patients have autoimmune features insufficient to meet criteria for a specific CTD; some eventually evolve to a defined disease.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":7}],
   "confusable_with":"SLE/RA (defined criteria met; UCTD is pre-differentiation)"},

  {"id":"ctd-ild-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Nintedanib (SENSCIS trial) showed what effect in systemic sclerosis-associated ILD and what is its mechanism?",
   "answer":"Nintedanib reduced annual FVC decline by 44% versus placebo in SSc-ILD (SENSCIS: -52.4 vs -93.3 mL/year, P<0.04); it is a tyrosine kinase inhibitor targeting VEGFR, FGFR, and PDGFR.",
   "rationale":"Nintedanib blocks fibroblast proliferation and activation pathways; it was the first approved pharmacological therapy for SSc-ILD.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":16}],
   "confusable_with":"pirfenidone (TGF-beta pathway; also antifibrotic but approved for IPF not SSc-ILD initially)"},

  {"id":"ctd-ild-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Tocilizumab was considered for SSc-ILD based on its mechanism but ultimately was not standard treatment. Why?",
   "answer":"Tocilizumab (IL-6 inhibitor) did not meet the primary endpoint (skin score) in the focuSSced phase 3 trial in SSc despite being listed in some secondary sources.",
   "rationale":"Despite biologicalrationale for IL-6 blockade in SSc, the primary outcome (modified Rodnan Skin Score) was not significantly improved, limiting its approval for this indication.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":25}],
   "confusable_with":""},

  {"id":"ctd-ild-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Sarcoidosis is the most common non-IPF ILD in what age group?",
   "answer":"Sarcoidosis is the most common non-IPF ILD, particularly among those younger than 45 years of age.",
   "rationale":"Unlike most ILDs that predominate in older adults, sarcoidosis has peak incidence in young adults (20-40 years), a distinguishing epidemiological feature.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":4}],
   "confusable_with":"IPF (older adults; UIP pattern)"},

  {"id":"ctd-ild-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is a rheumatologic overview approach to ILD in connective tissue diseases?",
   "answer":"Rheumatologic ILD workup includes fevers, arthritis, rashes/photosensitivity, alopecia, nail/nailfold changes, sicca symptoms, conjunctivitis, uveitis, episcleritis, and Raynaud phenomenon as clues to CTD.",
   "rationale":"Identifying the underlying CTD guides treatment; CTD-ILD often responds to immunosuppression unlike IPF.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":172}],
   "confusable_with":""},

  {"id":"ctd-ild-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Drug-induced ILD screening should consult what resource, and which drugs are monitored by the clinical pharmacist?",
   "answer":"Drug-ILD screening uses pneumotox.com; monitoring focuses on cyclophosphamide (bladder toxicity), mycophenolate (GI), and azathioprine (myelosuppression).",
   "rationale":"Immunosuppressive drugs used for CTD-ILD have significant toxicity profiles requiring pharmacist-led monitoring to prevent drug-ILD and other serious adverse effects.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":22}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 387: Kidney Stones (Nephrolithiasis)
# ============================================================
topic = "Kidney Stones (Nephrolithiasis)"
domain = "Internal medicine: nephrology, fluids & electrolytes"
discipline = "medicine"

kps = [
  {"id":"nephrolithiasis-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Uric acid kidney stones have what radiological characteristic and why?",
   "answer":"Uric acid stones are radiolucent on plain abdominal X-ray (KUB); calcium-based stones are radioopaque.",
   "rationale":"Uric acid lacks calcium; without calcium, stones do not attenuate X-rays and are invisible on plain film but visible on CT (HU <500).",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":7}],
   "confusable_with":"calcium oxalate stones (most common; radioopaque)"},

  {"id":"nephrolithiasis-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Uric acid nephrolithiasis is associated with gout and hyperuricemia in what proportion of patients?",
   "answer":"Gout and hyperuricemia are associated with uric acid uropathy in 15-25% of patients.",
   "rationale":"Uric acid crystallizes in acidic urine (pH <5.5); morning urine is most acidic, making uric acid stone formation most likely at that time.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":5}],
   "confusable_with":""},

  {"id":"nephrolithiasis-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the target urinary pH for urinary alkalinization in uric acid stone prevention and treatment?",
   "answer":"Urinary alkalinization aims for a consistently elevated urine pH above 6.5 to dissolve and prevent uric acid stones.",
   "rationale":"Uric acid solubility increases dramatically above pH 6.5; alkalinization converts insoluble uric acid to more soluble urate.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":8}],
   "confusable_with":"calcium stone prevention (require different interventions: thiazides, low oxalate diet)"},

  {"id":"nephrolithiasis-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What constitutes hyperuricosuria as a risk factor for uric acid stones?",
   "answer":"Hyperuricosuria is defined as 24-hour urinary uric acid excretion >750 mg/day in females and >800 mg/day in males.",
   "rationale":"Elevated urinary uric acid increases the concentration available for crystallization, particularly in low-volume, acidic urine.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":5}],
   "confusable_with":""},

  {"id":"nephrolithiasis-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A urinary tract infection with a blocked kidney from a nephrolithiasis is what type of emergency, and what drainage options exist?",
   "answer":"Obstructed UTI with nephrolithiasis is a surgical emergency requiring urgent drainage via double J stent (cystoscopic) or percutaneous nephrostomy.",
   "rationale":"Obstruction prevents antibiotic penetration into infected collecting system; urosepsis from pyelonephritis with obstruction can be rapidly fatal without drainage.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":10}],
   "confusable_with":"uncomplicated UTI (no obstruction; antibiotic-only management appropriate)"},

  {"id":"nephrolithiasis-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What urine dipstick finding correlates with specific gravity and how is urine osmolality estimated?",
   "answer":"Urine osmolality is approximated: decimal of SG multiplied by 30 (e.g., SG 1.020 = 20 x 30 = ~600 mOsm/kg).",
   "rationale":"Specific gravity reflects urine concentration; the approximation allows rapid bedside assessment of hydration status relevant to kidney stone risk.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":111}],
   "confusable_with":""},

  {"id":"nephrolithiasis-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Uric acid stone formation is especially increased in laborers working in what conditions, and what is the incidence?",
   "answer":"Laborers working in hot environmental conditions have a uric acid stone incidence of several percent; those working at standard room temperature have 0.9% incidence.",
   "rationale":"Heat causes hypovolemia and concentrated acidic urine, creating ideal conditions for uric acid crystallization and stone formation.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Kidney Stones (Nephrolithiasis)","page":5}],
   "confusable_with":""},
]
output.extend(kps)

# Save partial output D
with open('data/kp_redeep_part11d_partial.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Part D done: {len(output)} items total")
