
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/kp_redeep_part11d_partial.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# ============================================================
# ITEM 388: Liver Transplantation: Indications & Perioperative Care
# ============================================================
topic = "Liver Transplantation: Indications & Perioperative Care"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"liver-transplant-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the median wait time to transplant for liver candidates, and at what MELD score are outcomes poorest?",
   "answer":"The median wait time for liver transplant candidates is 11 months; highest-acuity recipients with MELD ≥35 (accounting for ~1/5 of transplants) have the worst pre-transplant outcomes.",
   "rationale":"MELD score predicts 90-day waitlist mortality; MELD ≥35 indicates severe hepatic decompensation requiring urgent transplantation.",
   "bloom":"recall",
   "source":[{"book":"Miller/Baby Miller","page":688}],
   "confusable_with":""},

  {"id":"liver-transplant-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What preoperative intravenous fluid is preferred in liver transplantation and why?",
   "answer":"Colloid (albumin) intravenous fluid is preferred to avoid sodium overload and to increase plasma oncotic pressure; preservation of intravascular volume and urinary output takes intraoperative priority.",
   "rationale":"Cirrhotic patients have low oncotic pressure from hypoalbuminemia; albumin infusion restores oncotic pressure without adding sodium that worsens ascites.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1202}],
   "confusable_with":"crystalloid (large volumes cause hyperchloremic acidosis and worsen ascites in liver failure)"},

  {"id":"liver-transplant-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What ICP management targets are used for patients with acute liver failure undergoing liver transplantation?",
   "answer":"ICP <20 mmHg, CPP >50 mmHg, MAP >60 mmHg, elevated head of bed 20-25 degrees, controlled ventilation, propofol sedation, controlled hypothermia (32-33 degrees C), and glycemic control.",
   "rationale":"Acute liver failure causes cerebral edema and raised ICP from ammonia and inflammatory mediators; aggressive ICP management prevents herniation until transplantation.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1208}],
   "confusable_with":""},

  {"id":"liver-transplant-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What coagulation complication occurs during the neohepatic phase of liver transplantation and how is it detected?",
   "answer":"Primary fibrinolysis can occur during the neohepatic phase; it is detected by point-of-care viscoelastic coagulation analysis (TEG/ROTEM).",
   "rationale":"The new liver releases plasminogen activators during reperfusion; fibrinolysis causes coagulopathic bleeding requiring antifibrinolytic therapy.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1213}],
   "confusable_with":"consumptive coagulopathy (DIC; different mechanism and treatment)"},

  {"id":"liver-transplant-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is Child B cirrhosis with portal hypertension and low MELD, and when can it be considered for transplantation?",
   "answer":"Child B cirrhosis with portal hypertension complications and low MELD can also be considered for liver transplant referral, not only MELD ≥15 cutoff.",
   "rationale":"Child-Pugh score captures clinical parameters (encephalopathy, ascites) not fully reflected in MELD; portal hypertension complications (variceal bleeding) indicate decompensation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":98}],
   "confusable_with":""},

  {"id":"liver-transplant-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Why should hypotensive anesthesia be avoided in patients with end-stage liver disease?",
   "answer":"Hypotensive anesthesia should be avoided because it has potentially deleterious effects on liver function; liver blood flow has limited autoregulation and is pressure-dependent.",
   "rationale":"Hepatic arterial buffer response can maintain flow to some degree, but hypotension significantly reduces hepatic perfusion in compromised livers.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},

  {"id":"liver-transplant-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What ICD-related renal complication in cirrhosis requires specific mention in liver transplant perioperative planning?",
   "answer":"Cirrhotic patients have derangements of fluid/electrolyte balance manifesting as ascites, edema, electrolyte disturbances, and hepatorenal syndrome; portal HTN is the key mechanism through increased hydrostatic pressure.",
   "rationale":"Hepatorenal syndrome reflects renal vasoconstriction from RAAS activation in response to splanchnic vasodilation; it often resolves after successful liver transplantation.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1199}],
   "confusable_with":"acute tubular necrosis (structural renal failure; HRS is functional, initially without tubular damage)"},
]
output.extend(kps)

# ============================================================
# ITEM 389: Lung Cancer: Screening and Diagnosis
# ============================================================
topic = "Lung Cancer: Screening and Diagnosis"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"lung-cancer-screening-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Low-dose CT (LDCT) screening for lung cancer reduces lung cancer-related deaths by what percentage compared to chest X-ray?",
   "answer":"LDCT screening reduced lung cancer-related deaths by approximately 20% compared to chest X-ray in the National Lung Screening Trial.",
   "rationale":"NLST demonstrated that LDCT detects early-stage lung cancer before symptom onset when curative resection is possible; mortality benefit drives screening guidelines.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lung Cancer  Screening and Diagnosis","page":3}],
   "confusable_with":""},

  {"id":"lung-cancer-screening-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"The USPSTF updated its lung cancer screening recommendation in 2021. What population and screening modality does it recommend?",
   "answer":"USPSTF 2021 recommends annual LDCT lung cancer screening for adults aged 50-80 with at least 20 pack-year smoking history who currently smoke or quit within the past 15 years.",
   "rationale":"The 2021 update expanded eligibility from the original NLST criteria (55-74, 30 pack-years) to capture more cancers, particularly in women and Black Americans.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":128}],
   "confusable_with":"NLST original criteria (age 55-74, 30 pack-years; superseded by 2021 USPSTF update)"},

  {"id":"lung-cancer-screening-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"LDCT screening in the NLST showed approximately how many fewer lung cancer deaths per 1000 persons screened?",
   "answer":"LDCT screening led to approximately 3 fewer lung cancer deaths per 1000 persons screened compared to chest X-ray.",
   "rationale":"The absolute benefit per 1000 is modest due to baseline lung cancer incidence; the relative risk reduction of 20% translates to meaningful population-level benefit.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lung Cancer  Screening and Diagnosis","page":3}],
   "confusable_with":""},

  {"id":"lung-cancer-screening-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Lung cancer has what relationship between incidence and mortality globally?",
   "answer":"Lung cancer has the highest rate of mortality and is the leading cause of cancer deaths worldwide; its incidence is approximately equal to its mortality.",
   "rationale":"The near 1:1 incidence-to-mortality ratio reflects diagnosis at advanced, incurable stages; screening aims to shift detection to earlier, potentially curable stages.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lung Cancer  Screening and Diagnosis","page":2}],
   "confusable_with":""},

  {"id":"lung-cancer-screening-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In the NLST, among individuals >65 years, LDCT screening also identified what commonly co-occurring pulmonary pathology?",
   "answer":"Quantitative CT density analysis in the NLST also detected COPD with varying sensitivity and specificity; LDCT screening provides incidental detection of emphysema/COPD.",
   "rationale":"Many heavy smokers have concurrent COPD; LDCT screening provides dual-purpose early detection of both lung cancer and COPD.",
   "bloom":"recall",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":41}],
   "confusable_with":""},

  {"id":"lung-cancer-screening-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the most common presenting symptoms of lung cancer that should prompt diagnostic evaluation?",
   "answer":"Cough, hemoptysis, wheezing, weight loss, productive sputum, dyspnea, fever, and pleuritic chest pain; metastatic disease may cause neurological symptoms or bone pain.",
   "rationale":"Many lung cancers present late with these symptoms; screening aims to identify asymptomatic lesions before symptom-driven presentation.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":904}],
   "confusable_with":""},

  {"id":"lung-cancer-screening-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What COPD comorbidity has been shown to correlate with lung cancer risk in matched case-control studies?",
   "answer":"Emphysema and airflow obstruction correlate with lung cancer risk; the correlation is independent of smoking history in matched case-controlled studies.",
   "rationale":"Shared inflammatory and oxidative pathways in emphysema and lung carcinogenesis explain the independent relationship beyond smoking exposure.",
   "bloom":"analyze",
   "source":[{"book":"Society Guideline: Guideline   GOLD 2024 COPD Full Report","page":167}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 390: Lymphoma: Hodgkin and non-Hodgkin approach
# ============================================================
topic = "Lymphoma: Hodgkin and non-Hodgkin approach"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
discipline = "medicine"

kps = [
  {"id":"lymphoma-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Follicular lymphoma is the most common type among indolent NHLs and has what disease course?",
   "answer":"Follicular lymphoma is the second most common NHL overall and the most common indolent NHL; it has a relapsing and remitting course with potential to progress to aggressive disease (histologic transformation in ~20% of patients).",
   "rationale":"FL originates from germinal center B-cells with BCL2 rearrangement; its indolent nature allows watchful waiting in early stages but it is rarely cured without transplant.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":2}],
   "confusable_with":"DLBCL (most common NHL overall; aggressive, not indolent; different treatment)"},

  {"id":"lymphoma-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Patients with follicular lymphoma refractory to rituximab have what prognosis, and what treatment approach is used?",
   "answer":"Rituximab-refractory FL has a poor prognosis; anti-CD20-based chemoimmunotherapy remains a standard treatment while more biologically active agents are increasingly used.",
   "rationale":"Resistance to rituximab indicates loss of CD20 expression or alternative survival pathway activation; novel agents (PI3K inhibitors, lenalidomide, CAR-T) target these mechanisms.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":2}],
   "confusable_with":""},

  {"id":"lymphoma-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"The AUGMENT trial evaluated lenalidomide plus rituximab in follicular lymphoma and showed what benefit?",
   "answer":"AUGMENT trial showed lenalidomide plus rituximab improved PFS (39 months vs 14 months) versus rituximab alone in relapsed/refractory FL; higher rates of infection, cutaneous reactions, and cytopenia were observed.",
   "rationale":"Lenalidomide enhances anti-tumor immune response and ADCC; combination with anti-CD20 therapy exploits complementary mechanisms.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":7}],
   "confusable_with":""},

  {"id":"lymphoma-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"WHO classifies follicular lymphoma grades 1, 2, and 3a/3b based on what histological method?",
   "answer":"WHO grades FL 1, 2, and 3a/3b based on the cell counting method of centroblasts (non-cleaved follicular center cells); FL grade 3b behaves like aggressive lymphoma.",
   "rationale":"Higher centroblast counts correlate with more aggressive behavior; grade 3b (solid sheets of centroblasts) is treated like diffuse large B-cell lymphoma.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":3}],
   "confusable_with":""},

  {"id":"lymphoma-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Axicabtagene ciloleucel (axi-cel) CAR-T therapy in follicular lymphoma showed what overall response rate in ZUMA-5?",
   "answer":"In ZUMA-5, axi-cel showed ORR 94% (79% complete remission, 15% partial remission) in FL patients, with median time to first response of 1 month.",
   "rationale":"CAR-T therapy redirects autologous T-cells against CD19 on lymphoma cells; responses are durable in a subset of patients, offering potential cure.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":8}],
   "confusable_with":""},

  {"id":"lymphoma-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What characterizes histologic transformation of follicular lymphoma, and what prognosis does it carry?",
   "answer":"Histologic transformation to aggressive lymphoma (usually DLBCL) occurs in ~20% of FL patients; it carries worse prognosis with shorter remissions and requires more aggressive therapy.",
   "rationale":"Acquisition of additional mutations (MYC, TP53) in FL B-cells drives transformation to aggressive phenotype; early treatment failure is a risk factor.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":8}],
   "confusable_with":""},

  {"id":"lymphoma-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"The CHRONOS-3 trial randomly assigned patients with relapsed indolent NHL to receive what treatment combination?",
   "answer":"CHRONOS-3 randomized 458 patients with relapsed clinically indolent NHL (including FL) 2:1 to copanlisib (PI3K inhibitor) plus rituximab versus placebo plus rituximab.",
   "rationale":"Copanlisib targets PI3K-alpha and PI3K-delta isoforms critical for B-cell survival; combination with rituximab enhances anti-tumor activity.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Lymphoma  Hodgkin and non Hodgkin approach","page":4}],
   "confusable_with":""},
]
output.extend(kps)

# ============================================================
# ITEM 391: MEN Syndromes (Multiple Endocrine Neoplasia)
# NOTE: chunks are mislabeled (prostatitis content); only Morgan & Mikhail chunks are relevant
# ============================================================
topic = "MEN Syndromes (Multiple Endocrine Neoplasia)"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
discipline = "medicine"

kps = [
  {"id":"men-syndromes-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"MEN type 1 is characterized by tumors in which three endocrine organs?",
   "answer":"MEN type 1 (Wermer syndrome) consists of pancreatic tumors (gastrinomas, insulinomas), pituitary tumors, and parathyroid tumors.",
   "rationale":"MEN1 results from MEN1 gene mutation; the triad of pancreatic-pituitary-parathyroid involvement is pathognomonic.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1244}],
   "confusable_with":"MEN type 2A (medullary thyroid cancer, pheochromocytoma, parathyroid; different gene RET)"},

  {"id":"men-syndromes-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"MEN type 2 consists of what components and what causes a hypertensive crisis during anesthesia induction in MEN?",
   "answer":"MEN type 2 consists of medullary thyroid carcinoma, pheochromocytoma, and hyperparathyroidism; pheochromocytoma can cause a hypertensive crisis during anesthesia induction.",
   "rationale":"Undiagnosed pheochromocytoma releases catecholamines during surgery; preoperative alpha-blockade (then beta-blockade) is mandatory before MEN type 2 surgery.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1244}],
   "confusable_with":"primary hyperaldosteronism (Conn syndrome; causes hypertension but not catecholamine crises)"},

  {"id":"men-syndromes-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Because MEN syndromes are hereditary, what family members require screening and for what conditions?",
   "answer":"Family members of MEN patients should be screened for early signs of pheochromocytoma, thyroid cancer (medullary), and hyperparathyroidism.",
   "rationale":"MEN syndromes are autosomal dominant; first-degree relatives have 50% risk of inheriting the gene mutation and benefit from early detection.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1244}],
   "confusable_with":"sporadic endocrine tumors (no family screening required)"},

  {"id":"men-syndromes-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"A patient with MEN type 1 develops Zollinger-Ellison syndrome. Which specific pancreatic tumor is responsible and what is the clinical presentation?",
   "answer":"Gastrinoma (MEN1) causes Zollinger-Ellison syndrome: hypergastrinemia drives excessive acid secretion causing peptic ulcers, diarrhea, and malabsorption.",
   "rationale":"Gastrinomas in MEN1 are often multifocal, in the duodenum or pancreas; they produce autonomous gastrin leading to peptic ulceration refractory to standard therapy.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1244}],
   "confusable_with":"sporadic ZES (usually solitary; 25% associated with MEN1)"},

  {"id":"men-syndromes-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What postoperative complication occurs in up to 40% of patients after transsphenoidal pituitary surgery but is usually transient?",
   "answer":"Diabetes insipidus develops postoperatively in up to 40% of transsphenoidal pituitary surgery patients but is usually transient; less commonly it presents intraoperatively.",
   "rationale":"Surgical manipulation disrupts posterior pituitary ADH release or the hypothalamo-pituitary stalk, causing temporary or permanent DI.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":994}],
   "confusable_with":"cerebral salt wasting (also causes polyuria after pituitary surgery but involves sodium wasting)"},

  {"id":"men-syndromes-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What risks are encountered during transsphenoidal pituitary surgery for a MEN1 pituitary adenoma?",
   "answer":"Risks include cavernous sinus invasion, internal carotid artery injury, cranial nerve damage, pituitary hypofunction, and CSF leak; prophylactic glucocorticoids are routinely used.",
   "rationale":"The sella turcica is adjacent to critical structures; tumor extension risks vascular and neural injury; steroid coverage prevents adrenal crisis from pituitary manipulation.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":994}],
   "confusable_with":""},

  {"id":"men-syndromes-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the genetic inheritance pattern of MEN syndromes and what are the causative genes?",
   "answer":"MEN syndromes are hereditary (autosomal dominant); MEN1 is caused by MEN1 gene mutation; MEN2A and MEN2B are caused by RET proto-oncogene mutations.",
   "rationale":"Autosomal dominant inheritance means affected individuals have 50% chance of passing the mutation; genetic testing of family members enables early surveillance and intervention.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1244}],
   "confusable_with":""},
]
output.extend(kps)

script = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Family history of MEN; autosomal dominant; MEN1 mutation or RET mutation; may present with index case tumor (hyperparathyroidism most common in MEN1)",
  "pathophysiology":"MEN1: MEN1 tumor suppressor loss -> unchecked parathyroid/pituitary/pancreatic neuroendocrine cell proliferation; MEN2: RET gain-of-function -> C-cell and adrenal medulla hyperplasia",
  "time_course":"Penetrance increases with age; hyperparathyroidism often first manifestation in MEN1 (>90% penetrance by 50y); MTC and pheo may manifest earlier in MEN2",
  "key_features":"MEN1: 3Ps (pancreas/pituitary/parathyroid); MEN2A: MTC+pheo+parathyroid; MEN2B: MTC+pheo+marfanoid+mucosal neuromas; serum Ca/PTH/calcitonin/plasma metanephrines",
  "consequence_if_missed":"Unrecognized pheo causes fatal catecholamine crisis during surgery; MTC invades locally and metastasizes; ZES complications (bleeding, perforation) from refractory PUD"}
output.append(script)

# ============================================================
# ITEM 392: Malignant Pleural Effusion
# ============================================================
topic = "Malignant Pleural Effusion"
domain = "Internal medicine: pulmonology (COPD, asthma, pulmonary embolism, pneumonia, ILD, pleural effusion, pneumothorax, hypoxemic & hypercapnic respiratory failure, OSA)"
discipline = "medicine"

kps = [
  {"id":"malignant-pleural-effusion-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the most common malignancies causing pleural metastases and malignant pleural effusion?",
   "answer":"Cancers of the kidney, breast, ovary, testis, colon, rectum, head and neck, and uterus commonly cause pleural metastases; lung cancer is also a leading cause.",
   "rationale":"Pleural metastases result from hematogenous or direct extension; malignant cells disrupt pleural lymphatics and mesothelial surface, causing exudative effusion.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":904}],
   "confusable_with":""},

  {"id":"malignant-pleural-effusion-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What standard panel of tests must be performed on diagnostic thoracentesis fluid?",
   "answer":"Standard diagnostic thoracentesis panel includes cytology, protein, LDH, glucose, pH, cell count/differential, and culture to characterize the effusion and establish malignant etiology.",
   "rationale":"Light criteria distinguish exudate from transudate; cytology confirms malignant cells; additional molecular testing improves diagnostic accuracy.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Malignant Pleural Effusion","page":12}],
   "confusable_with":""},

  {"id":"malignant-pleural-effusion-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Pleural fluid elastance measurement by pleural manometry predicts what in malignant pleural effusion management?",
   "answer":"Pleural fluid elastance (decrease in pleural pressure in cmH2O per 500 mL removed) identifies trapped lung; low, dropping pressure indicates trapped lung and predicts poor pleurodesis response.",
   "rationale":"Trapped lung from tumoral pleural encasement prevents lung re-expansion; pleurodesis is ineffective if the lung cannot expand against the chest wall.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Malignant Pleural Effusion","page":22}],
   "confusable_with":""},

  {"id":"malignant-pleural-effusion-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What CT features suggest malignant pleural effusion over benign causes?",
   "answer":"Nodular pleural thickening, mediastinal pleural thickening, circumferential thickening encasing the lung, and parietal pleura thickening >1 cm suggest malignant pleural effusion.",
   "rationale":"Malignant tumor deposits on the pleura cause irregular nodular thickening; these features help target biopsy sites and assess disease extent.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Malignant Pleural Effusion","page":11}],
   "confusable_with":"mesothelioma (similar CT features; requires specific IHC for diagnosis)"},

  {"id":"malignant-pleural-effusion-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What physical findings are classic for pleural effusion and where are whispered pectoriloquy and egophony appreciated?",
   "answer":"Dullness to percussion and decreased vocal fremitus are classic; whispered pectoriloquy and egophony may be appreciated at the upper border of the pleural effusion.",
   "rationale":"Fluid replaces air at the effusion level, reducing sound transmission (dullness, decreased fremitus); at the effusion border, compressed lung transmits sounds differently.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Malignant Pleural Effusion","page":9}],
   "confusable_with":"pneumonia (dullness with increased fremitus; no fluid)"},

  {"id":"malignant-pleural-effusion-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What specific contraindications exist for pleurodesis in malignant pleural effusion?",
   "answer":"Contraindications include aspirate >150 mL/day, residual fluid on radiograph, suspicion of pleural infection, and lack of informed consent; NSAIDs should be held to avoid interference with fibrotic pleurodesis response.",
   "rationale":"NSAIDs impair the inflammatory response necessary for pleurodesis; residual fluid and undrained infection prevent adequate pleurodesis and increase complications.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Malignant Pleural Effusion","page":18}],
   "confusable_with":""},

  {"id":"malignant-pleural-effusion-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What does pericardial effusion from malignancy cause, and what is the hemodynamic definition of tamponade?",
   "answer":"Malignant pericardial effusion causes cardiac tamponade: hemodynamic insufficiency from impaired cardiac filling due to pericardial pressure, with equalization of diastolic pressures in all four chambers.",
   "rationale":"Tamponade physiology occurs when pericardial pressure exceeds intracardiac filling pressure; Beck's triad (hypotension, JVD, muffled heart sounds) is the classic presentation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":34}],
   "confusable_with":"constrictive pericarditis (also equalized pressures but chronic, calcified pericardium)"},
]
output.extend(kps)

# Save partial output E
with open('data/kp_redeep_part11e_partial.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Part E done: {len(output)} items total")
