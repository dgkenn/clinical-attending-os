
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('data/kp_redeep_part11b_partial.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# ============================================================
# ITEM 377: Hepatopulmonary Syndrome & Portopulmonary Hypertension
# ============================================================
topic = "Hepatopulmonary Syndrome & Portopulmonary Hypertension"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"hps-pph-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What three criteria define hepatopulmonary syndrome (HPS)?",
   "answer":"HPS requires: (1) liver disease usually with portal hypertension, (2) alveolar-arterial oxygen gradient >15 mmHg, and (3) pulmonary arteriovenous connections demonstrated by delayed contrast echo or macroaggregated albumin scan.",
   "rationale":"Intrapulmonary vasodilation in HPS causes V/Q mismatch and diffusion-perfusion limitation, worsening hypoxemia (platypnea-orthodeoxia pattern).",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1197}],
   "confusable_with":"portopulmonary hypertension (also in cirrhosis but causes pulmonary arterial HTN, not shunting)"},

  {"id":"hps-pph-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the hemodynamic cardiovascular findings typical of end-stage liver disease and cirrhosis?",
   "answer":"Cirrhosis produces a hyperdynamic circulation: high cardiac output, increased heart rate, decreased SVR, increased circulating volume, and cirrhotic cardiomyopathy.",
   "rationale":"Splanchnic vasodilation from NO excess and bacterial translocation stimulate compensatory increases in cardiac output; reduced SVR conceals poor LV function.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1195}],
   "confusable_with":"cardiogenic shock (low CO, high SVR; opposite pattern)"},

  {"id":"hps-pph-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Why should hypotensive anesthesia be avoided in patients with end-stage liver disease?",
   "answer":"Hypotensive anesthesia should be avoided because of potentially deleterious effects on liver function in patients with ESLD.",
   "rationale":"The liver has limited autoregulation; hypotension reduces hepatic arterial flow, worsening ischemic hepatocellular injury in an already compromised liver.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},

  {"id":"hps-pph-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What complication may occur if a TEE or Doppler probe is placed in a patient with esophageal variceal disease?",
   "answer":"TEE or Doppler probe placement in a patient with esophageal varices carries risk of variceal trauma and hemorrhage.",
   "rationale":"Esophageal varices are fragile submucosal dilated veins; probe insertion can cause mechanical trauma and life-threatening hemorrhage.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},

  {"id":"hps-pph-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What antifibrinolytic agents may reduce operative blood loss in liver surgery, and under what condition should they not be used prophylactically?",
   "answer":"Epsilon-aminocaproic acid or tranexamic acid may reduce blood loss when fibrinolysis is detected; they should not be used prophylactically due to thrombosis risk.",
   "rationale":"Primary fibrinolysis in liver failure can cause coagulopathic bleeding, but prophylactic antifibrinolytics risk portal vein thrombosis.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1203}],
   "confusable_with":""},

  {"id":"hps-pph-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Portal hypertension in cirrhosis leads to what group of cardiovascular, pulmonary, and renal complications?",
   "answer":"Portal HTN causes esophageal varices, GI bleeding, hyperdynamic circulation, systemic AV shunts, low SVR, cirrhotic cardiomyopathy, intrapulmonary shunting (HPS), decreased FRC, pleural effusions, and ascites.",
   "rationale":"Portal hypertension increases splanchnic blood flow and releases vasoactive mediators that affect every organ system through shunting and inflammation.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1192}],
   "confusable_with":""},

  {"id":"hps-pph-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In patients with cirrhosis, low systemic vascular resistance conceals what cardiac problem?",
   "answer":"Low SVR in cirrhosis can conceal poor left ventricular function (cirrhotic cardiomyopathy); echocardiographic examination may initially appear deceptively normal.",
   "rationale":"Normal LVEF and low afterload can mask systolic dysfunction and reduced cardiac reserve; unmasked during liver transplant when SVR normalizes.",
   "bloom":"analyze",
   "source":[{"book":"Morgan & Mikhail","page":1196}],
   "confusable_with":""},
]
output.extend(kps)

script = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Cirrhosis with portal hypertension; any etiology; HPS predominantly in Child-Pugh B/C; PoPH in 5-10% of cirrhosis patients",
  "pathophysiology":"HPS: intrapulmonary arteriovenous vasodilation (NO excess) causing right-to-left shunt and V/Q mismatch; PoPH: pulmonary arterial vasoconstriction/remodeling from vasoactive mediators escaping portal filter",
  "time_course":"Progressive with underlying liver disease; HPS may improve after liver transplantation; PoPH is a contraindication to transplant if severe (mPAP >50 mmHg)",
  "key_features":"HPS: platypnea-orthodeoxia, PaO2 <70 mmHg, positive bubble echo; PoPH: dyspnea, elevated PAP on RHC, RV enlargement; both associated with cirrhosis",
  "consequence_if_missed":"Perioperative hypoxic respiratory failure; post-liver-transplant HPS requires prolonged supplemental O2; PoPH causes fatal RV failure perioperatively if not screened"}
output.append(script)

# ============================================================
# ITEM 378: Hereditary & Metabolic Liver Diseases
# ============================================================
topic = "Hereditary & Metabolic Liver Diseases"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"hereditary-metabolic-liver-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the most common cause of cirrhosis in the United States in recent years?",
   "answer":"Nonalcoholic steatohepatitis (NASH/MASLD) has overtaken chronic alcohol abuse as the most common cause of cirrhosis in the United States.",
   "rationale":"Rising rates of obesity and metabolic syndrome have dramatically increased NAFLD/NASH prevalence, making it the leading liver disease in Western countries.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1191}],
   "confusable_with":"alcoholic cirrhosis (previously #1; now #2 in the US)"},

  {"id":"hereditary-metabolic-liver-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"For what condition is liver transplantation indicated when MELD score reaches 15 or when complications develop?",
   "answer":"Liver transplantation is indicated for cirrhosis with MELD score ≥15 or with complications such as ascites, hepatic encephalopathy, variceal bleeding, HRS, or chronic gastropathy bleeding.",
   "rationale":"MELD score integrates bilirubin, INR, and creatinine to estimate 90-day mortality; complications indicate decompensation requiring transplant evaluation.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":98}],
   "confusable_with":""},

  {"id":"hereditary-metabolic-liver-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What MELD exception points are granted for hereditary metabolic liver diseases that lack direct MELD score elevation?",
   "answer":"MELD exception points are granted for conditions including hepatocellular carcinoma, Budd-Chiari syndrome, familial amyloidotic polyneuropathy, cystic fibrosis, hereditary hemorrhagic telangiectasia, primary hyperoxaluria, and rare metabolic diseases.",
   "rationale":"These conditions cause liver failure or systemic disease disproportionate to MELD score; exception points ensure appropriate transplant priority.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":4}],
   "confusable_with":""},

  {"id":"hereditary-metabolic-liver-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Primary hyperoxaluria type I is an autosomal recessive defect in what enzyme, and how is it treated?",
   "answer":"Primary hyperoxaluria type I results from deficiency of alanine:glyoxylate aminotransferase in the liver, impairing oxalate metabolism; combined liver-kidney transplantation is the treatment.",
   "rationale":"The defective enzyme is liver-specific; liver transplantation restores enzyme activity and prevents further oxalate production, while kidney transplantation replaces the damaged organ.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":8}],
   "confusable_with":""},

  {"id":"hereditary-metabolic-liver-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the absolute contraindications to liver transplantation mentioned in current guidelines?",
   "answer":"Active sepsis, multidrug-resistant organisms with pretransplant infection, profound leukopenia (<500/mm3), and uncontrolled extrahepatic malignancy are absolute contraindications.",
   "rationale":"Immunosuppression post-transplant would be fatal with active uncontrolled infection or malignancy; patient selection is critical for outcome.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":8}],
   "confusable_with":""},

  {"id":"hereditary-metabolic-liver-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What liver diseases require evaluation for liver transplantation including HCC, and what is the critical timing of acute-on-chronic liver failure transplant?",
   "answer":"LT evaluation is indicated for ALF, acute-on-chronic LF, cirrhosis with MELD ≥15 or HCC, and metabolic liver diseases; optimal ACLF transplant timing is within 7-15 days of ICU admission.",
   "rationale":"Delay beyond 15 days in ACLF dramatically worsens outcomes from progressive multi-organ failure; early transplant improves survival.",
   "bloom":"recall",
   "source":[{"book":"StatPearls","page":5}],
   "confusable_with":""},

  {"id":"hereditary-metabolic-liver-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Hepatitis A causes what clinical syndrome and what is the diagnostic test?",
   "answer":"HAV causes acute symptomatic hepatitis (nausea/vomiting, anorexia, malaise, fever, jaundice, ALT>AST often >1000) lasting 2-8 weeks; diagnosis is anti-HAV IgM (persists 3-6 months).",
   "rationale":"HAV is a self-limited fecal-oral infection in adults; fulminant hepatic failure is rare but possible; 70% of adults are symptomatic.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":90}],
   "confusable_with":"hepatitis E (also fecal-oral; anti-HEV IgM for diagnosis; dangerous in pregnancy)"},
]
output.extend(kps)

# ============================================================
# ITEM 379: Hereditary hemolytic anemias
# ============================================================
topic = "Hereditary hemolytic anemias"
domain = "Internal medicine: hematology & oncology (anemias, anticoagulation & reversal, VTE prophylaxis & treatment, thrombocytopenia & DIC, transfusion medicine, oncologic emergencies, neutropenic fever)"
discipline = "medicine"

kps = [
  {"id":"hereditary-hemolytic-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Sickle cell anemia results from what molecular defect and is classified as what type of anemia?",
   "answer":"Sickle cell anemia is a hereditary hemolytic anemia resulting from the formation of abnormal hemoglobin HbS (glutamic acid to valine substitution at position 6 of the beta-globin chain).",
   "rationale":"HbS polymerizes when deoxygenated, deforming RBCs into sickle shapes that cause vascular occlusion and hemolysis.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1970}],
   "confusable_with":"HbC disease (different point mutation; milder hemolysis)"},

  {"id":"hereditary-hemolytic-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Thalassemia is characterized by what type of hemoglobin defect, and what determines severity?",
   "answer":"Thalassemia is a hereditary defect in alpha- or beta-chain production; severity depends on the subunit affected and degree to which hemoglobin production is impaired (ranges from asymptomatic to transfusion-dependent).",
   "rationale":"Reduced globin chain production causes imbalanced chains that precipitate in RBCs, causing ineffective erythropoiesis and hemolysis.",
   "bloom":"recall",
   "source":[{"book":"Morgan & Mikhail","page":1975}],
   "confusable_with":"sickle cell anemia (structural hemoglobin defect; vs thalassemia = quantitative production defect)"},

  {"id":"hereditary-hemolytic-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In sickle cell perioperative management, what is the target hematocrit achieved by preoperative hemodilution, and why is normovolemia maintained?",
   "answer":"One to two units of blood removed preoperatively reduce hematocrit to 21-25%; replaced with crystalloid/colloid to maintain normovolemia because cardiac output remains normal with normovolemia.",
   "rationale":"Reducing HbS concentration decreases sickling risk; normovolemia is essential to maintain oxygen delivery despite lower hematocrit.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1970}],
   "confusable_with":""},

  {"id":"hereditary-hemolytic-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Paroxysmal cold hemoglobinuria (PCH) is characterized by what immunological mechanism?",
   "answer":"PCH is caused by an IgG autoantibody (Donath-Landsteiner antibody) that activates complement at cold temperatures, leading to intravascular hemolysis and hemoglobinuria upon rewarming.",
   "rationale":"The biphasic nature of PCH (antibody binds at cold, lysis occurs at warm) is pathognomonic and explains the hemoglobinuria pattern.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Autoimmune hemolytic anemia (AIHA)","page":3}],
   "confusable_with":"cold agglutinin disease (IgM, also cold-activated but different mechanism)"},

  {"id":"hereditary-hemolytic-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Rh hemolytic disease of the newborn generally does not occur in the first pregnancy (without prior transfusion). Why?",
   "answer":"First-exposure sensitization occurs during first Rh-positive pregnancy; IgG anti-D antibodies produced during sensitization cross the placenta and cause hemolysis only in subsequent Rh-positive pregnancies.",
   "rationale":"Primary immune response during first pregnancy is insufficient to cause severe HDN; secondary response in subsequent pregnancies produces high-titer IgG anti-D.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Autoimmune hemolytic anemia (AIHA)","page":8}],
   "confusable_with":"ABO HDN (can occur in first pregnancy; IgM anti-A/B naturally occurring)"},

  {"id":"hereditary-hemolytic-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Immune hemolytic anemias are classified based on what principle, and which are categorized as 'immune'?",
   "answer":"Immune hemolytic anemias are classified by the immune system targeting RBCs; they include warm AIHA (IgG, 37 degrees C), cold agglutinin disease (IgM), mixed type, and PCH.",
   "rationale":"The immune mechanism determines treatment: warm AIHA responds to steroids; cold agglutinin disease may require rituximab or complement inhibitors.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Autoimmune hemolytic anemia (AIHA)","page":2}],
   "confusable_with":"microangiopathic hemolytic anemia (mechanical, not immune)"},

  {"id":"hereditary-hemolytic-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Thrombophilia workup includes testing for antiphospholipid syndrome in which clinical scenarios?",
   "answer":"Test for antiphospholipid syndrome in unprovoked VTE, unexplained arterial thrombosis, obstetric complications (pregnancy loss), and other criteria of microvascular thrombosis.",
   "rationale":"APS antibodies (lupus anticoagulant, anticardiolipin, anti-beta2-GP1) cause thrombosis through platelet activation and endothelial effects.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Thrombophilia  inherited and acquired","page":26}],
   "confusable_with":"inherited thrombophilias (factor V Leiden, prothrombin mutation; tested differently)"},
]
output.extend(kps)

script2 = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Family history; specific ethnicities (sickle cell: African descent; thalassemia: Mediterranean/SE Asian; G6PD: African/Mediterranean/SE Asian males)",
  "pathophysiology":"Intrinsic RBC defects: membrane (spherocytosis), enzyme (G6PD), hemoglobin structure (HbS) or production (thalassemia) causing premature RBC destruction",
  "time_course":"Chronic compensated hemolytic anemia with crises (sickle cell: vaso-occlusive, aplastic, splenic sequestration); thalassemia: transfusion-dependent if severe",
  "key_features":"Elevated LDH, low haptoglobin, elevated indirect bilirubin, reticulocytosis; peripheral smear (sickle cells, target cells, spherocytes); positive direct Coombs test in AIHA",
  "consequence_if_missed":"Perioperative sickle crisis (hypoxia, dehydration, hypothermia triggers); transfusion alloimmunization; undiagnosed thalassemia receiving iron supplementation worsens iron overload"}
output.append(script2)

# ============================================================
# ITEM 380: Hypermagnesemia: Causes and Management
# ============================================================
topic = "Hypermagnesemia: Causes and Management"
domain = "Internal medicine: nephrology, fluids & electrolytes"
discipline = "medicine"

kps = [
  {"id":"hypermagnesemia-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the cardiovascular consequences of severe hypermagnesemia (>12 mg/dL)?",
   "answer":"Severe hypermagnesemia (>12 mg/dL) can lead to cardiovascular collapse, cardiac arrest, and death.",
   "rationale":"Magnesium acts as a calcium channel blocker; extreme levels block cardiac conduction and neuromuscular transmission, causing bradycardia, heart block, and asystole.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":6}],
   "confusable_with":"hyperkalemia (also causes cardiac toxicity; different ECG findings and treatment)"},

  {"id":"hypermagnesemia-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What iatrogenic causes of hypermagnesemia are described in elderly and obstetric patients?",
   "answer":"Magnesium oxide in geriatric patients (>1000 mg/day risk), bowel preparation agents (sodium picosulphate magnesium citrate), and IV magnesium for eclampsia are iatrogenic causes.",
   "rationale":"Oral magnesium overload can overwhelm GI regulation; IV magnesium for eclampsia requires monitoring to prevent toxicity.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":3}],
   "confusable_with":""},

  {"id":"hypermagnesemia-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What monitoring parameters are required during high-dose IV magnesium therapy for eclampsia?",
   "answer":"Periodic serum magnesium levels, urinary output, potassium/phosphate/calcium levels, renal function (creatinine, BUN, GFR, urine specific gravity) must be monitored during eclampsia magnesium therapy.",
   "rationale":"IV magnesium toxicity progresses from loss of reflexes to respiratory arrest; monitoring prevents dangerous accumulation, especially with renal impairment.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":5}],
   "confusable_with":""},

  {"id":"hypermagnesemia-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What role does magnesium play in relation to other electrolytes?",
   "answer":"Magnesium influences sodium, calcium, and potassium; together with calcium, extracellular magnesium is essential for enzymatic action, transporters, and nucleic acid synthesis.",
   "rationale":"Magnesium deficiency impairs PTH secretion and antagonizes PTH effects on bone, leading to hypocalcemia; hypomagnesemia also causes refractory hypokalemia.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":2}],
   "confusable_with":""},

  {"id":"hypermagnesemia-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Hypermagnesemia requires what specific anesthetic monitoring and what is indicated for significant renal impairment?",
   "answer":"Hypermagnesemia requires close monitoring; [Mg2+] must be obtained, urinary catheter placed, and dialysis is necessary for patients with significant renal impairment or failure.",
   "rationale":"Magnesium is almost exclusively renally cleared; renal failure leads to dangerous accumulation; dialysis is the definitive treatment for severe hypermagnesemia.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1898}],
   "confusable_with":""},

  {"id":"hypermagnesemia-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the pathophysiology of hypermagnesemia from laxative overuse versus dietary excess?",
   "answer":"Dietary excess rarely causes hypermagnesemia in healthy kidneys; laxative overuse overwhelms GI regulation with massive intraluminal magnesium, bypassing renal protective mechanisms.",
   "rationale":"The kidneys can normally excrete excess dietary magnesium; the large pharmacological doses in laxatives exceed renal clearance capacity.",
   "bloom":"analyze",
   "source":[{"book":"StatPearls: StatPearls   Hypermagnesemia  Causes and Management","page":4}],
   "confusable_with":""},

  {"id":"hypermagnesemia-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"In a poorly responsive ventilated patient post-anesthesia, what electrolyte should be checked to exclude persisting neuromuscular blockade-like effects?",
   "answer":"Hypermagnesemia should be checked (serum Mg2+) in patients with delayed emergence; it can cause neuromuscular blockade-like effects; a nerve stimulator helps exclude persistent NMB.",
   "rationale":"Magnesium competes with calcium at the neuromuscular junction and potentiates NMB; hypermagnesemia mimics residual paralysis.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":2099}],
   "confusable_with":"residual neuromuscular blockade (both cause delayed emergence; nerve stimulator differentiates)"},
]
output.extend(kps)

# ============================================================
# ITEM 381: Hypopituitarism
# ============================================================
topic = "Hypopituitarism"
domain = "Internal medicine: endocrinology (diabetes & inpatient glucose, DKA & HHS, thyroid disorders & storm, adrenal insufficiency, calcium disorders, pituitary)"
discipline = "medicine"

kps = [
  {"id":"hypopituitarism-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What are the anterior pituitary hormones and what does the posterior pituitary secrete?",
   "answer":"Anterior pituitary: GH, TSH, ACTH, FSH, LH, prolactin; posterior pituitary: ADH (vasopressin) and oxytocin.",
   "rationale":"Hypopituitarism can affect one or all hormonal axes; complete pituitary failure (panhypopituitarism) requires replacement of multiple hormones.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":2}],
   "confusable_with":""},

  {"id":"hypopituitarism-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Kallmann syndrome causes hypopituitarism through what mechanism and what is the hallmark non-endocrine finding?",
   "answer":"Kallmann syndrome results from a Kal1 gene mutation causing hypogonadotropic hypogonadism (decreased FSH/LH, low testosterone/estradiol); hallmark non-endocrine finding is anosmia or hyposmia.",
   "rationale":"GnRH neurons fail to migrate to the hypothalamus due to absent olfactory bulb development; both reproductive and olfactory pathways share developmental origins.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":4}],
   "confusable_with":"other causes of hypogonadotropic hypogonadism (pituitary adenoma, functional; no anosmia)"},

  {"id":"hypopituitarism-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Lymphocytic hypophysitis is most commonly seen in what clinical setting and how does it appear on MRI?",
   "answer":"Lymphocytic hypophysitis most commonly occurs in the postpartum period; MRI shows a mass lesion from lymphocyte and plasma cell infiltration; responds well to steroid therapy.",
   "rationale":"Autoimmune pituitary infiltration during the postpartum hormonal shift mimics a pituitary adenoma and can cause varying degrees of hypopituitarism.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":3}],
   "confusable_with":"pituitary adenoma (mass effect on MRI; no steroid response)"},

  {"id":"hypopituitarism-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Immune checkpoint inhibitors (ICI) cause hypopituitarism through what mechanism and which specific pituitary hormone axis is most commonly affected?",
   "answer":"ICIs (anti-CTLA-4, anti-PD-1/PD-L1) cause immune-related hypophysitis; hypopituitarism with ACTH deficiency (secondary adrenal insufficiency) is among the most common endocrinopathies.",
   "rationale":"T-cell activation by ICI leads to immune infiltration of the pituitary; secondary AI is life-threatening and may not recover unlike thyroid ICI toxicity.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":3}],
   "confusable_with":"ICI thyroiditis (more common but less acutely dangerous)"},

  {"id":"hypopituitarism-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the preferred imaging modality for the pituitary gland and what does it primarily detect?",
   "answer":"MRI with gadolinium enhancement is the preferred imaging modality for the pituitary, primarily to detect mass lesions and characterize pituitary adenomas.",
   "rationale":"MRI provides superior soft tissue resolution for the sella turcica; gadolinium enhancement allows detection of microadenomas and assessment of cavernous sinus invasion.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":7}],
   "confusable_with":"CT head (inferior soft tissue resolution for pituitary; used when MRI unavailable)"},

  {"id":"hypopituitarism-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What patient education is essential for adults with secondary adrenal insufficiency from hypopituitarism?",
   "answer":"Patients should wear medical alert identification (bracelet/necklace) and carry hydrocortisone 100 mg vial with syringe at home and during travel for emergency self-administration.",
   "rationale":"Secondary AI is life-threatening if untreated during physiological stress (illness, surgery, trauma); patient self-awareness and emergency hydrocortisone prevent adrenal crisis.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":8}],
   "confusable_with":""},

  {"id":"hypopituitarism-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Growth hormone replacement in adults with GH deficiency: what is the therapeutic objective?",
   "answer":"In pediatric GH deficiency, the objective is to attain normal linear growth (titrated to IGF-1 levels); in adults, the role of GH replacement has not been firmly established.",
   "rationale":"Adult GH deficiency causes metabolic abnormalities (dyslipidemia, reduced muscle/bone mass, quality of life); replacement may improve these but long-term mortality benefit is uncertain.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Hypopituitarism","page":7}],
   "confusable_with":""},
]
output.extend(kps)

script3 = {"_type":"illness_script","topic":topic,"discipline":discipline,
  "enabling_conditions":"Pituitary adenoma (most common cause), pituitary surgery/radiation, Sheehan syndrome (postpartum pituitary infarction), TBI, ICI therapy, infiltrative disease (sarcoid, hemochromatosis)",
  "pathophysiology":"Loss of anterior pituitary trophic hormones causing downstream gland deficiency (secondary hypothyroidism, secondary adrenal insufficiency, hypogonadism, GH deficiency)",
  "time_course":"Depends on cause; post-surgical hypopituitarism may be immediate; Sheehan syndrome presents weeks to years postpartum; ICI hypophysitis within weeks to months",
  "key_features":"Fatigue, weight change, sexual dysfunction, headache, visual field defects (bitemporal hemianopia with macroadenoma); MRI mass lesion",
  "consequence_if_missed":"Adrenal crisis (life-threatening); central hypothyroidism may be treated incorrectly if thyroid hormone given without first treating secondary AI (precipitates crisis)"}
output.append(script3)

# ============================================================
# ITEM 382: IBD Complications & Special Situations
# ============================================================
topic = "IBD Complications & Special Situations"
domain = "Internal medicine: gastroenterology & hepatology (upper & lower GI bleed, acute liver failure, cirrhosis & its complications, pancreatitis, IBD, bowel obstruction, hepatic encephalopathy)"
discipline = "medicine"

kps = [
  {"id":"ibd-complications-d1","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Primary sclerosing cholangitis (PSC) is classified into what subtypes and which is most common?",
   "answer":"Classic/large-duct PSC (both intrahepatic and extrahepatic ducts, ~90%), small-duct PSC (~5%), and PSC-AIH overlap (~5%); large-duct PSC is most common.",
   "rationale":"PSC causes multifocal biliary strictures and eventual biliary cirrhosis; the subtype influences prognosis and surveillance strategy.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Primary Sclerosing Cholangitis (PSC)","page":2}],
   "confusable_with":"primary biliary cholangitis (PBC, different disease; affects small intrahepatic ducts; anti-mitochondrial antibody positive)"},

  {"id":"ibd-complications-d2","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"IBD has a strong association with which biliary disease, and what IBD-specific complication requires awareness?",
   "answer":"IBD has a strong association with PSC (approximately 80-90% of PSC patients have IBD, usually UC); PSC increases cholangiocarcinoma risk even after colectomy.",
   "rationale":"Shared immune dysregulation links IBD and PSC; PSC patients with IBD require colonoscopic surveillance due to high colorectal cancer risk.",
   "bloom":"recall",
   "source":[{"book":"StatPearls: StatPearls   Primary Sclerosing Cholangitis (PSC)","page":2}],
   "confusable_with":""},

  {"id":"ibd-complications-d3","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"Fulminant ulcerative colitis is characterized by what features and what is a defining complication?",
   "answer":"Fulminant colitis is characterized by hypotension/shock, ileus, toxic megacolon; severe colitis may present with hypovolemia, AKI, marked leukocytosis, lactic acidosis, and protein-losing enteropathy.",
   "rationale":"Transmural inflammation in fulminant colitis causes loss of neuromuscular tone (toxic megacolon) with risk of perforation and septic shock.",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":124}],
   "confusable_with":"infectious colitis causing toxic megacolon (must exclude before immunosuppression)"},

  {"id":"ibd-complications-d4","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"During liver transplantation, what specific blood management complication requires administration of only washed packed RBCs?",
   "answer":"Citrate toxicity (hypocalcemia) during massive transfusion in liver transplantation may require washed RBCs; ionized calcium must be monitored and calcium salts administered as needed.",
   "rationale":"Citrate chelates ionized calcium; the failing liver cannot metabolize citrate, causing hypocalcemia with massive transfusion.",
   "bloom":"apply",
   "source":[{"book":"Morgan & Mikhail","page":1207}],
   "confusable_with":""},

  {"id":"ibd-complications-d5","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What is the epidemiology of IBD in the US and what are the bimodal age peaks?",
   "answer":"IBD affects approximately 1.3% of the US population; onset is bimodal at ages 15-30 years and a second peak at 50-80 years.",
   "rationale":"The bimodal distribution reflects both early-onset immune dysregulation (genetic) and late-onset disease (environmental/microbiome changes).",
   "bloom":"recall",
   "source":[{"book":"MGH Housestaff Manual","page":81}],
   "confusable_with":""},

  {"id":"ibd-complications-d6","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"What patient and healthcare team education is essential for PSC management?",
   "answer":"PSC is a chronic liver condition with no definitive cure; early detection and regular follow-up are crucial for reducing complications (cholangiocarcinoma, cirrhosis); specialist referral is required.",
   "rationale":"Annual cholangiocarcinoma surveillance (MRCP, CA 19-9) and liver transplant evaluation at appropriate MELD score are essential management components.",
   "bloom":"apply",
   "source":[{"book":"StatPearls: StatPearls   Primary Sclerosing Cholangitis (PSC)","page":7}],
   "confusable_with":""},

  {"id":"ibd-complications-d7","topic":topic,"domain":domain,"discipline":discipline,
   "stem":"IBD patients with hypereosinophilia due to steroid tapering: why does eosinophilia unmask during steroid taper?",
   "answer":"Eosinophils are rapidly eliminated by steroids; eosinophilia may be unmasked when patients taper off chronic glucocorticoids, revealing underlying eosinophilic conditions.",
   "rationale":"Steroid suppression of eosinophils is rapid; withdrawal reveals baseline eosinophil count that may reflect allergic, parasitic, or hypereosinophilic disease.",
   "bloom":"analyze",
   "source":[{"book":"MGH Housestaff Manual","page":140}],
   "confusable_with":""},
]
output.extend(kps)

# Save partial output C
with open('data/kp_redeep_part11c_partial.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Part C done: {len(output)} items total")
