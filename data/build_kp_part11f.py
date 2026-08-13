
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/kp_redeep_part11e_partial.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# ============================================================
# ITEM 393: Microscopic Colitis
# NOTE: chunks are heavily off-topic (hematuria article mislabeled)
# Using the valid IBD/diarrhea chunks that mention microscopic colitis
# ============================================================
topic = "Microscopic Colitis"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"microscopic-colitis-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Microscopic colitis appears in the differential of which diarrheal conditions in the MGH Housestaff Manual?",
   "answer":"Microscopic colitis appears in the differential of C. difficile-associated diarrhea, infectious diarrhea, post-infectious IBS, IBD, and celiac disease.",
   "rationale":"Microscopic colitis causes watery, nonbloody diarrhea with normal or near-normal colonoscopy; biopsy is required for diagnosis, distinguishing it from IBD.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":124}],
   "confusable_with":"IBD (mucosal changes visible on colonoscopy; microscopic colitis is macroscopically normal)"},

  {"id":"microscopic-colitis-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What distinguishes microscopic colitis from other causes of watery diarrhea, and why is biopsy required?",
   "answer":"Microscopic colitis has normal or near-normal macroscopic colonoscopy appearance; biopsy is required to demonstrate characteristic histological findings (collagenous or lymphocytic subtype).",
   "rationale":"The normal-appearing mucosa on colonoscopy means diagnosis is missed without systematic biopsies; histology reveals thickened collagen band (collagenous) or increased intraepithelial lymphocytes (lymphocytic).",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":124}],
   "confusable_with":"IBS (also normal colonoscopy; no biopsy abnormality)"},

  {"id":"microscopic-colitis-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Severe ulcerative colitis may be complicated by what life-threatening complication defined by hypotension and shock?",
   "answer":"Fulminant colitis is characterized by hypotension/shock and ileus; toxic megacolon is the extreme complication involving colonic dilation with systemic toxicity.",
   "rationale":"Transmural inflammation in fulminant colitis causes paralysis of colonic smooth muscle; toxic megacolon risks perforation and septic shock.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":124}],
   "confusable_with":"Ogilvie syndrome (pseudo-obstruction; no transmural inflammation)"},

  {"id":"microscopic-colitis-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"IBD is distinguished from infectious diarrhea by what approach in clinical evaluation?",
   "answer":"IBD should be diagnosed only after microbiologic exclusion of infectious causes; stool cultures and C. difficile testing must be obtained before initiating immunosuppression.",
   "rationale":"Infectious colitis (Salmonella, C. difficile, Entamoeba) can mimic IBD; treating infection with immunosuppression is dangerous.",
   "bloom":"apply",
   "source":[{"book":"MGH Housestaff Manual","page":77}],
   "confusable_with":"IBD exacerbation (may coexist with infection; both require separate evaluation)"},

  {"id":"microscopic-colitis-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Acute diarrhea is defined as what number of loose stools per day and duration?",
   "answer":"Acute diarrhea is defined as 3 or more loose stools per day for less than 14 days.",
   "rationale":"The operational definition distinguishes acute from persistent (>14 days) and chronic (>30 days) diarrhea, which have different diagnostic and management algorithms.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":77}],
   "confusable_with":""},

  {"id":"microscopic-colitis-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What clinical presentation differentiates small bowel from large bowel diarrhea?",
   "answer":"Small bowel diarrhea: watery, large volume, with cramping/bloating; large bowel diarrhea: frequent, small volume, painful, with fever, blood, or mucus.",
   "rationale":"Small bowel absorbs ~10L/day (vs 1L for colon); small bowel disease overwhelms colonic absorption with voluminous watery output; colonic disease causes tenesmus and blood.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":77}],
   "confusable_with":""},

  {"id":"microscopic-colitis-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"When are follow-up urine cytology evaluations considered in microscopic hematuria investigation?",
   "answer":"Follow-up urine cytology is considered in individuals with risk factors for carcinoma in situ; significant increases in microscopic hematuria, new gross hematuria, or new urologic symptoms warrant repeat evaluation.",
   "rationale":"Urothelial carcinoma in situ can be detected by cytology; the risk-stratified approach avoids over-investigation while identifying clinically significant findings.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Microscopic Colitis","page":13}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 394: Nephrotic Syndrome
# ============================================================
topic = "Nephrotic Syndrome"
domain = "Internal medicine: nephrology, fluids & electrolytes"
discipline = "medicine"

kps = [
  {"id":"nephrotic-syndrome-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Nephrotic syndrome is an edematous state associated with sodium overload. What other conditions share this pathophysiology?",
   "answer":"Heart failure, cirrhosis, and nephrotic syndrome are the classic edematous states associated with sodium overload and reduced effective arterial blood volume.",
   "rationale":"All three conditions activate RAAS and ADH via reduced effective circulating volume, promoting sodium and water retention despite total body sodium excess.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1080}],
   "confusable_with":""},

  {"id":"nephrotic-syndrome-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In nephrotic syndrome, what urinary finding on dipstick suggests the diagnosis, and what does the BUN:creatinine ratio indicate?",
   "answer":"Heavy proteinuria on urine dipstick is the hallmark; BUN/Cr <20 with normal renal function suggests prerenal physiology from hypoalbuminemia causing reduced effective arterial volume.",
   "rationale":"The massive proteinuria of nephrotic syndrome (>3.5 g/day) reduces oncotic pressure causing edema and activating prerenal mechanisms.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1101}],
   "confusable_with":""},

  {"id":"nephrotic-syndrome-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Nephrotic syndrome appears as an indication for albumin administration in what clinical context?",
   "answer":"Albumin is indicated for nephrotic syndrome as one of the appropriate indications alongside ECMO, acute hemorrhagic shock, burns, and hepatorenal syndrome (but NOT decompensated cirrhosis).",
   "rationale":"In nephrotic syndrome, hypoalbuminemia is severe enough to cause oncotic pressure deficit; albumin transiently restores oncotic pressure but is cleared by urinary losses.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":110}],
   "confusable_with":"decompensated cirrhosis (albumin NOT helpful for edema in cirrhosis per NEJM 2021)"},

  {"id":"nephrotic-syndrome-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Loop diuretics are used in nephrotic syndrome. What is the mechanism of action and which drugs are included?",
   "answer":"Loop diuretics (furosemide, bumetanide, ethacrynic acid, torsemide) inhibit Na+/K+/2Cl- reabsorption in the thick ascending limb of Henle by competing at the carrier protein.",
   "rationale":"Blocking the Na+/K+/2Cl- carrier eliminates the medullary concentration gradient, producing profound sodium and water diuresis effective even with low GFR.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1080}],
   "confusable_with":"thiazide diuretics (distal tubule; less potent; useful in mild nephrotic edema adjunctively)"},

  {"id":"nephrotic-syndrome-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Progressive losses of sodium and water in nephrotic syndrome lead to what compensatory physiologic response?",
   "answer":"Progressive volume depletion activates nonosmotic ADH secretion; with severe deficit, baroreceptor-mediated nonosmotic ADH release overcomes osmotic regulation, contributing to hyponatremia.",
   "rationale":"Volume depletion is a stronger ADH stimulator than osmolality; this explains dilutional hyponatremia in severe nephrotic syndrome despite low plasma osmolality.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1865}],
   "confusable_with":"SIADH (also hyponatremia with ADH excess but euvolemic; different treatment)"},

  {"id":"nephrotic-syndrome-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What prerenal condition is associated with congestive heart failure, cirrhosis, and nephrotic syndrome that reduces renal blood flow?",
   "answer":"Reduced effective arterial blood volume in these conditions activates RAAS, causing prerenal azotemia and is also associated with obstructive uropathy as a cause of prerenal AKI.",
   "rationale":"Effective arterial volume reduction from decreased cardiac output or hypoalbuminemia triggers RAAS/ADH, causing prerenal reduction in GFR.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1101}],
   "confusable_with":""},

  {"id":"nephrotic-syndrome-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Primary aldosteronism (Conn syndrome) is caused by what lesion and what clinical findings result?",
   "answer":"Primary aldosteronism is caused by a unilateral adenoma (aldosteronoma/Conn syndrome), bilateral hyperplasia, or rarely carcinoma; it causes hypertension, hypokalemia, and metabolic alkalosis.",
   "rationale":"Autonomous aldosterone hypersecretion increases sodium reabsorption and potassium excretion; distinguishing unilateral adenoma from bilateral hyperplasia determines surgical vs medical management.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1235}],
   "confusable_with":"secondary hyperaldosteronism (from renal artery stenosis; elevated renin distinguishes)"},
]
output.extend(kps)

# ============================================================
# ITEM 395: Non-IPF Interstitial Lung Diseases
# ============================================================
topic = "Non-IPF Interstitial Lung Diseases"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"non-ipf-ild-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Sarcoidosis is the most common non-IPF ILD in what age group, and how does this differ from IPF epidemiology?",
   "answer":"Sarcoidosis is the most common non-IPF ILD particularly in adults younger than 45; IPF predominantly affects adults over 60.",
   "rationale":"The younger age at sarcoidosis presentation reflects its immune-mediated granulomatous pathogenesis distinct from the fibroproliferative mechanism of IPF.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":4}],
   "confusable_with":"IPF (older adults; UIP pattern; antifibrotics not steroids)"},

  {"id":"non-ipf-ild-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Nintedanib was established as the first antifibrotic approved for progressive pulmonary fibrosis (PPF) across multiple non-IPF fibrotic ILD subtypes by which trial?",
   "answer":"The INBUILD trial established nintedanib as the first antifibrotic approved for PPF across multiple non-IPF fibrotic ILD subtypes (SSc-ILD, RA-ILD, HP, and others).",
   "rationale":"PPF in non-IPF ILD shares similar fibrotic progression mechanisms with IPF; nintedanib's antifibrotic effect is applicable regardless of underlying etiology.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":16}],
   "confusable_with":"SENSCIS trial (nintedanib in SSc-ILD specifically; INBUILD was broader PPF trial)"},

  {"id":"non-ipf-ild-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"When should nintedanib be considered in a patient with non-IPF ILD?",
   "answer":"Nintedanib should be considered when a non-IPF ILD patient meets PPF (progressive pulmonary fibrosis) criteria, regardless of the underlying ILD etiology.",
   "rationale":"PPF criteria (worsening symptoms, physiology, or radiological progression in 12 months) indicate a fibrotic phase requiring antifibrotic intervention.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":25}],
   "confusable_with":""},

  {"id":"non-ipf-ild-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"How does fibrotic hypersensitivity pneumonitis management differ from IPF management?",
   "answer":"Fibrotic HP may respond to antigen avoidance and immunosuppression (unlike IPF which is treated with antifibrotic therapy; immunosuppression harms IPF).",
   "rationale":"HP has an immune-mediated granulomatous mechanism that can respond to antigen removal and steroids/immunosuppression; IPF is a fibroproliferative disorder where immunosuppression worsens outcomes.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":25}],
   "confusable_with":"IPF with UIP pattern (clinically identical on HRCT; requires BAL/biopsy and clinical history to distinguish)"},

  {"id":"non-ipf-ild-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What genetic predisposition accounts for up to 20% of IPF cases, and which genes are implicated?",
   "answer":"Familial pulmonary fibrosis (IPF in 2+ first-degree relatives) accounts for up to 20% of IPF cases; mutations in telomere-related genes (TERT, TERC) and surfactant protein genes are implicated.",
   "rationale":"Short telomeres from TERT/TERC mutations impair alveolar epithelial cell renewal; the resulting accelerated cellular senescence drives fibrosis.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":4}],
   "confusable_with":""},

  {"id":"non-ipf-ild-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"ILD presents with what hallmark clinical triad and examination findings?",
   "answer":"Progressive dyspnea, nonproductive cough, and hypoxemia (especially with exercise); velcro crackles, clubbing, and reduced exercise tolerance on exam.",
   "rationale":"Fibrotic lung disease reduces compliance and DLco; exertional hypoxemia and velcro crackles at lung bases reflect basilar fibrosis.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":53}],
   "confusable_with":"CHF (also dyspnea and crackles; orthopnea, JVD, and elevated BNP distinguish)"},

  {"id":"non-ipf-ild-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Sarcoidosis, cryptogenic organizing pneumonia, and idiopathic interstitial pneumonias are classified among what group of lung diseases?",
   "answer":"These are classified among non-IPF ILD subtypes including sarcoidosis, COP, desquamative interstitial pneumonia (DIP/alveolar macrophage pneumonia), nonspecific interstitial pneumonitis (NSIP), and acute interstitial pneumonia (AIP).",
   "rationale":"Non-IPF ILD is a heterogeneous group with diverse etiologies and HRCT patterns; accurate classification is essential because prognosis and treatment differ substantially.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Non IPF Interstitial Lung Diseases","page":3}],
   "confusable_with":"IPF (progressive, UIP pattern; antifibrotics only)"},
]
output.extend(kps)

script = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Variable by subtype: CTD-ILD (young women with autoimmune disease); sarcoidosis (young adults, Black > white); HP (antigen-exposed individuals); drug-ILD (iatrogenic); familial ILD (TERT/TERC mutations)",
  "pathophysiology":"Heterogeneous: immune-mediated granulomatous (sarcoidosis, HP), autoimmune (CTD-ILD), fibroproliferative when meets PPF criteria; common final pathway of alveolar injury and fibrosis",
  "time_course":"Highly variable; sarcoidosis may remit; CTD-ILD may be stable or progressive; HP improves with antigen avoidance; PPF follows IPF-like irreversible progression",
  "key_features":"Progressive dyspnea, restrictive PFTs (low TLC, FVC, DLco), HRCT patterns (GGO, traction bronchiectasis, honeycombing depending on subtype); BAL may show lymphocytosis (HP/sarcoidosis)",
  "consequence_if_missed":"Missed treatable HP (antigen avoidance curative early); incorrect antifibrotic vs immunosuppressive choice; delayed PPF recognition misses nintedanib therapy window"}
output.append(script)

# Final: Write output
with open('data/kp_redeep_part_11.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# Validate
with open('data/kp_redeep_part_11.json', 'r', encoding='utf-8') as f:
    check = json.load(f)

total = len(check)
kp_count = sum(1 for x in check if '_type' not in x)
script_count = sum(1 for x in check if x.get('_type') == 'illness_script')
pair_count = sum(1 for x in check if x.get('_type') == 'confusable_pair')

print(f"FINAL: {total} total items")
print(f"KPs: {kp_count}")
print(f"Scripts: {script_count}")
print(f"Pairs: {pair_count}")

# Count unique topics
topics = set()
for x in check:
    if '_type' not in x:
        topics.add(x['topic'])
    elif x.get('_type') == 'illness_script':
        topics.add(x['topic'])
print(f"Unique topics with content: {len(topics)}")

# Verify all IDs unique
ids = [x.get('id') for x in check if 'id' in x]
print(f"Unique IDs: {len(set(ids))}, Total ID'd: {len(ids)}")
if len(set(ids)) != len(ids):
    from collections import Counter
    dups = [k for k,v in Counter(ids).items() if v > 1]
    print(f"Duplicate IDs: {dups}")
else:
    print("No duplicate IDs - OK")
