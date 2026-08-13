import json
import re

# Load the retrieval file
with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    all_items = json.load(f)

# Get slice [594:627]
slice_items = all_items[594:627]

kps = []

def make_slug(topic_str):
    slug = re.sub(r'[^a-z0-9]+', '_', topic_str.lower()).strip('_')
    return slug[:40]

def get_source(chunks):
    if chunks and len(chunks) > 0:
        first = chunks[0]
        return [{"book": first.get("book", "Unknown"), "page": first.get("page", 0)}]
    return [{"book": "Unknown", "page": 0}]

# Template for adding KP
def add_kp(topic, domain, discipline, stem, answer, rationale, bloom, source, confusable="", n=1):
    slug = make_slug(topic)
    kps.append({
        "id": f"{slug}-{n}",
        "topic": topic,
        "domain": domain,
        "discipline": discipline,
        "stem": stem,
        "answer": answer,
        "rationale": rationale,
        "bloom": bloom,
        "source": source,
        "confusable_with": confusable
    })

# Manually add complete entries for all 33 topics
topics_data = [
    # 594
    ("Pneumonia: community-acquired, hospital-acquired, aspiration", "Medical", "Critical Care", [
        ("What distinguishes community-acquired pneumonia (CAP) from hospital-acquired pneumonia (HAP) clinically and microbiologically?",
         "CAP presents within 48 hours of hospital admission with typical community pathogens (S. pneumoniae, H. influenzae, M. pneumoniae); HAP develops >48 hours after admission with resistant gram-negative organisms (P. aeruginosa, MRSA)",
         "Time of onset and associated risk factors determine pathogen epidemiology and guide empiric antibiotic selection", "apply", "Aspiration pneumonia"),
        ("In aspiration pneumonia, which patient populations are at highest risk and what organisms predominate?",
         "Impaired swallowing (stroke, myasthenia), altered consciousness (sedation, anesthesia), gastroesophageal reflux; anaerobes (Bacteroides, Peptostreptococcus, Prevotella)",
         "Risk factors involve disrupted protective airway reflexes", "apply", "CAP with typical pathogens"),
    ]),
    # 595
    ("Pneumothorax", "Medical", "Critical Care", [
        ("What clinical signs differentiate a tension pneumothorax from a simple pneumothorax on examination?",
         "Tension: hypotension, elevated JVD, tracheal deviation, absent breath sounds ipsilateral, hemodynamic instability; simple: only unilateral absent breath sounds and hyperresonance, hemodynamically stable",
         "Tension physiology causes mediastinal shift and vena cava compression", "apply", "Hemothorax or pleural effusion"),
        ("When is tube thoracostomy indicated acutely in pneumothorax management?",
         "Tension pneumothorax (immediate needle decompression then tube); secondary >2 cm or >20% hemithorax; primary >2 cm; any with respiratory failure",
         "Size and clinical stability determine appropriateness", "apply", "Simple aspiration management"),
    ]),
    # 596
    ("Portal Hypertension & Varices", "Medical", "Gastroenterology", [
        ("What is the pathophysiological mechanism of portal hypertension and how does it lead to variceal bleeding?",
         "Portal hypertension (>12 mmHg) from cirrhosis causes splanchnic vasodilation; pressure drives blood through collaterals (varices); wall tension increases, leading to rupture",
         "Elevated pressure overcomes variceal wall integrity", "analyze", "Peptic ulcer bleeding"),
        ("What is the role of beta-blocker prophylaxis in esophageal varices?",
         "Beta-blockers (propranolol, carvedilol) reduce portal pressure by 20-30% and decrease variceal bleeding risk; used for primary and secondary prophylaxis",
         "Beta-blockade reduces splanchnic blood flow and portal pressure", "apply", "Band ligation as sole therapy"),
    ]),
    # 597
    ("Preoperative Cardiovascular Risk Assessment", "Medical", "Perioperative", [
        ("What are the key components of the revised cardiac risk index (RCRI) for predicting perioperative cardiac events?",
         "High-risk surgery, ischemic heart disease, heart failure, cerebrovascular disease, diabetes on insulin; each adds 1 point; predicts MACE",
         "Multiple comorbidities compound perioperative risk", "recall", "ASA classification alone"),
        ("When is preoperative stress testing indicated in cardiac risk assessment?",
         "Stress testing reserved for patients with multiple RCRI factors undergoing vascular surgery; functional capacity assessment may obviate testing",
         "Objective functional assessment guides risk stratification", "apply", "Blanket stress testing"),
    ]),
    # 598
    ("Primary Adrenal Insufficiency (Addison Disease)", "Medical", "Endocrinology", [
        ("What are the cardinal clinical features and laboratory findings of primary adrenal insufficiency?",
         "Fatigue, weakness, weight loss, hypotension, GI upset; hyperpigmentation, hyponatremia, hyperkalemia, hypoglycemia; low cortisol + elevated ACTH",
         "Adrenal cortex destruction eliminates glucocorticoids and mineralocorticoids", "recall", "Secondary AI (normal pigmentation)"),
        ("What is the diagnostic gold standard for confirming primary adrenal insufficiency?",
         "ACTH stimulation test: baseline cortisol measured, then ACTH 250 mcg IV; cortisol <18-20 mcg/dL at 30 or 60 min confirms primary AI",
         "Normal adrenal response excludes primary insufficiency", "apply", "Cosyntropin variations"),
        ("What is adrenal crisis and how is it managed?",
         "Acute severe adrenal insufficiency (fever, confusion, hypotension, shock); treat with IV hydrocortisone 100 mg stat then q6-8h, aggressive fluids",
         "Absent glucocorticoid reserve causes severe hypotension", "apply", "Septic shock alone"),
    ]),
    # 599
    ("Primary Hyperparathyroidism", "Medical", "Endocrinology", [
        ("What biochemical pattern is diagnostic of primary hyperparathyroidism?",
         "Elevated serum calcium with elevated or inappropriately normal PTH (>65 pg/mL); low phosphate; high 1,25-vitamin D",
         "Autonomous PTH secretion fails normal negative feedback", "recall", "PTH-related peptide secretion"),
        ("What are the renal and skeletal complications of untreated primary hyperparathyroidism?",
         "Renal: nephrolithiasis, chronic kidney disease, hypercalcemic nephropathy; Skeletal: osteoporosis, increased fracture risk, osteitis fibrosa cystica",
         "Chronic hypercalcemia damages renal tubules and stimulates bone resorption", "recall", "Vitamin D toxicity"),
        ("When is parathyroidectomy indicated in primary hyperparathyroidism?",
         "Symptomatic disease or asymptomatic criteria: age <50, Ca >1.3× upper normal, reduced creatinine clearance, T-score <-2.5, hypercalciuric",
         "Surgery prevents complications in young patients", "apply", "Medical management alone"),
    ]),
    # 600
    ("Pulmonary Embolism: Risk Factors and Classification", "Medical", "Critical Care", [
        ("What are the major risk factors for pulmonary embolism (PE)?",
         "Major: prolonged immobility, recent surgery/trauma, malignancy, antithrombotic deficiency, prior VTE, OCPs/HRT, pregnancy; minor: age >60, obesity",
         "VTE risk integrates venous stasis, endothelial injury, hypercoagulability", "recall", "Acute coronary syndrome"),
        ("How is PE severity classified and what is the clinical significance?",
         "Massive: hemodynamic instability; submassive: stable but elevated troponin/BNP or RV dysfunction; low-risk: normal biomarkers; guides anticoagulation vs. thrombolysis",
         "Hemodynamic and biomarker abnormalities predict mortality", "apply", "WELLS score severity"),
    ]),
    # 601
    ("Pulmonary Hypertension", "Medical", "Cardiology", [
        ("What is the hemodynamic definition and classification of pulmonary hypertension?",
         "PH = mPAP ≥25 mmHg at rest; 5 groups: PAH, left heart disease, lung disease, chronic thromboembolic, unclear/multifactorial",
         "Hemodynamic definition allows objective stratification", "recall", "Elevated systemic BP"),
        ("What are the classic symptoms and signs of pulmonary hypertension?",
         "Dyspnea on exertion (earliest), syncope, fatigue, chest pain; loud P2, RV heave, elevated JVD, peripheral edema",
         "RV hypertrophy and failure produce progressive symptoms", "recall", "Left heart failure"),
        ("How are disease-modifying therapies selected in pulmonary artery hypertension?",
         "Vasodilators (nitrates, PDE inhibitors, ERA) reduce PVR; selection by WHO functional class, echo, RHC response",
         "Targeted therapy reduces PVR and improves RV function", "apply", "General diuretic/inotrope therapy"),
    ]),
    # 602
    ("Respiratory Failure in Special Circumstances", "Medical", "Critical Care", [
        ("How is respiratory failure classified and what are the pathophysiologic mechanisms?",
         "Type I (hypoxemic): PaO2 <60 with normal/low CO2; V/Q mismatch, diffusion, shunting; Type II (hypercapnic): PaCO2 >50; hypoventilation; Type III: perioperative; Type IV: shock",
         "Mechanism classification guides specific therapeutic approaches", "analyze", "Respiratory acidosis alone"),
        ("What are the special considerations in managing respiratory failure in obesity or pregnancy?",
         "Obesity: increased WOB, reduced FRC, early desaturation; aggressive PEEP, upright, higher tidal volumes; Pregnancy: avoid teratogens, PaO2 >70 for fetus",
         "Altered mechanics require tailored ventilatory strategies", "apply", "Standard RF management"),
    ]),
    # 603
    ("Respiratory Physiology: Acid-Base and Gas Exchange", "Medical", "Physiology", [
        ("What are the mechanisms of hypoxemia and how can they be differentiated using ABG and A-a gradient?",
         "Hypoventilation: low PaCO2, low PaO2; V/Q: widens A-a, O2 responsive; diffusion: widens A-a, minimal O2 response; shunt: A-a >15 at FiO2 100%; low FiO2: normal A-a",
         "A-a gradient quantifies perfusion-ventilation defect", "analyze", "Hypoxemia without classification"),
        ("How is alveolar-arterial (A-a) gradient calculated and interpreted?",
         "A-a = PAO2 - PaO2; PAO2 = (PB - PH2O) × FiO2 - (PaCO2/0.8); normal <10-15; increased indicates intrapulmonary pathology",
         "A-a isolates gas exchange defect from ventilatory causes", "apply", "PaO2 alone"),
        ("What is the expected respiratory response to metabolic acidosis (Winter formula)?",
         "Expected PaCO2 = 1.5 × [HCO3-] + 8 ± 2; if actual higher, concurrent respiratory acidosis; if lower, concurrent respiratory alkalosis",
         "Renal-respiratory compensation can be assessed", "apply", "Simple interpretation"),
    ]),
    # 604
    ("SIADH (Syndrome of Inappropriate ADH)", "Medical", "Endocrinology", [
        ("What is the pathophysiology of SIADH and how does it cause hyponatremia?",
         "Inappropriate ADH secretion increases free water reabsorption in collecting duct; dilutional hyponatremia with inappropriately concentrated urine",
         "ADH acts on V2 receptors; excessive activity causes water retention", "analyze", "Nephrotic syndrome hyponatremia"),
        ("What are the major causes of SIADH in hospitalized patients?",
         "CNS: head trauma, meningitis, stroke, seizure; Pulmonary: pneumonia, lung cancer, positive pressure; Malignancy: SCLC, pancreatic, prostate; Meds: SSRIs, carbamazepine",
         "Multiple disease processes activate ADH", "recall", "Primary polydipsia"),
    ]),
    # 605
    ("SIADH: Diagnosis and Management", "Medical", "Endocrinology", [
        ("What diagnostic criteria confirm SIADH?",
         "Low serum osmolarity <275, low Na <130, hyposmolar urine >100 mOsm/kg, euvolemia, normal renal/adrenal/thyroid, no diuretics",
         "Diagnostic triad: hyponatremia + low osmolarity + concentrated urine", "recall", "Hypovolemic or hypervolemic hyponatremia"),
        ("How is acute symptomatic hyponatremia from SIADH managed?",
         "Acute (<48h) with seizures: hypertonic saline 3% bolus to raise Na by 4-6 mEq/L acutely then 10-12 mEq/L over 24h",
         "CNS edema requires rapid partial correction; overcorrection causes osmotic demyelination", "apply", "Chronic hyponatremia"),
        ("What is the role of fluid restriction and vaptans in SIADH management?",
         "Fluid restriction (500-1000 mL/day) first-line for chronic asymptomatic; vaptans for refractory cases; block V2 receptors without hypernatremia",
         "Reduced free water intake addresses pathophysiology", "apply", "Normal saline administration"),
    ]),
    # 606
    ("Secondary & Tertiary Adrenal Insufficiency", "Medical", "Endocrinology", [
        ("What is the distinction between secondary and tertiary adrenal insufficiency?",
         "Secondary: pituitary ACTH deficiency (no hyperpigmentation, low cortisol + low ACTH); Tertiary: hypothalamic CRH deficiency (similar); both preserve aldosterone",
         "Both lack ACTH-driven cortisol but preserve mineralocorticoid axis", "analyze", "Primary AI (elevated ACTH)"),
        ("How is secondary adrenal insufficiency diagnosed?",
         "Low or inappropriately normal ACTH with low cortisol; ACTH stimulation shows blunted/absent response; CRH or low-dose dex may help localize",
         "Central AI shows inadequate ACTH response to stimulation", "apply", "Primary AI response"),
        ("What is the management of secondary/tertiary adrenal insufficiency?",
         "Glucocorticoid replacement (hydrocortisone 15-20 mg daily divided doses); no mineralocorticoid needed; adrenal crisis identical treatment; investigate pituitary pathology",
         "Central insufficiency requires only glucocorticoid replacement", "apply", "Primary AI management"),
    ]),
    # 607
    ("Sickle cell disease", "Medical", "Hematology", [
        ("What is the molecular pathophysiology of sickle cell disease and what triggers sickling crises?",
         "HbS polymerization under low O2, low pH, dehydration causes RBC distortion and vaso-occlusion; triggers: hypoxia, infection, dehydration, cold, stress",
         "Polymerized hemoglobin distorts RBC shape and impairs deformability", "analyze", "Hemolytic anemia"),
        ("What are the acute complications of sickle cell disease and their management?",
         "Vaso-occlusive crisis: IV fluids, opioids, oxygen if SpO2 <90%; acute chest syndrome: antibiotics, transfusion; stroke: exchange transfusion; priapism: urologic emergency",
         "Acute crises require supportive care and disease-modifying therapy", "apply", "Simple pain management"),
        ("What chronic organ complications develop in sickle cell disease?",
         "Pulmonary: chronic lung disease, PH; Renal: CKD, hematuria; Splenic: autoinfarction, asplenia; Neurologic: stroke, moyamoya; Hepatic: cirrhosis; Bone: avascular necrosis",
         "Repeated sickling and chronic hemolysis damage multiple organs", "recall", "Acute complications only"),
    ]),
    # 608
    ("Stable Ischemic Heart Disease", "Medical", "Cardiology", [
        ("What is the pathophysiology of stable angina and how does it differ from unstable angina?",
         "Stable: fixed coronary stenosis causing supply-demand mismatch during exertion; reproducible, relieved by rest/nitrates; unstable: plaque rupture with thrombosis, pain at rest",
         "Plaque stability determines symptom pattern", "analyze", "Unstable angina/STEMI"),
        ("What is the role of beta-blockers and ACE inhibitors in managing stable ischemic heart disease?",
         "Beta-blockers: reduce HR, contractility, BP, decreasing O2 demand; symptom relief and post-MI mortality benefit; ACE inhibitors: reduce afterload, improve LV remodeling",
         "Both reduce myocardial work and improve LV efficiency", "apply", "Sole nitrate therapy"),
        ("When is revascularization (PCI vs. CABG) indicated in stable ischemic heart disease?",
         "Medical therapy first-line; PCI for inadequate symptom relief or high-risk lesions; CABG for left main, 3-vessel disease, especially diabetes or reduced EF",
         "Revascularization improves symptoms in selected high-risk anatomy", "apply", "Routine revascularization"),
    ]),
    # 609
    ("Syncope evaluation & management", "Medical", "Cardiology", [
        ("How is the syncope history differentiated between vasovagal, orthostatic, and cardiac causes?",
         "Vasovagal: emotional trigger, prodrome (lightheadedness, warmth, nausea), quick recovery; orthostatic: supine-to-upright, exertion, dehydration; cardiac: sudden without prodrome, exertional, family Hx",
         "History pattern predicts mechanism and guides testing", "apply", "Seizure vs syncope"),
        ("What diagnostic workup is appropriate for suspected cardiac syncope?",
         "12-lead ECG mandatory (assess QT, Brugada, delta wave, BBB); echo for structural disease; Holter/event monitor if arrhythmia; tilt table if vasovagal; EP study if high-risk ECG",
         "ECG screening identifies dangerous arrhythmias; further testing tailored", "apply", "Extensive workup for low-risk"),
        ("What are the management strategies for orthostatic hypotension-induced syncope?",
         "Nonpharmacologic: adequate hydration, salt intake, slow position changes, leg exercises, compression stockings; pharmacologic: fludrocortisone or midodrine",
         "Volume expansion and vasoconstriction counteract blood pool shift", "apply", "Vasovagal management"),
    ]),
    # 610
    ("Thrombocytopenia & coagulopathy in hospitalized patients", "Medical", "Hematology", [
        ("What is the differential diagnosis of thrombocytopenia in hospitalized patients?",
         "Decreased production: sepsis, meds, transfusion, nutritional; Increased destruction: DIC, HIT, ITP, SLE, infection; Sequestration: splenomegaly; Dilution: massive transfusion",
         "Bone marrow assessment and coagulation studies differentiate mechanisms", "analyze", "Single mechanism"),
        ("How is disseminated intravascular coagulation (DIC) recognized in hospitalized patients?",
         "Thrombocytopenia, prolonged PT/INR, elevated D-dimer, low fibrinogen, schistocytes; triggers: severe sepsis, massive transfusion, obstetric, malignancy",
         "Systemic coagulation activation consumes platelets and factors", "apply", "Simple coagulopathy"),
        ("What is heparin-induced thrombocytopenia (HIT) and what is the emergency management?",
         "Immune reaction to heparin-PF4 complex causing platelet activation, thrombocytopenia, paradoxical thrombosis; IMMEDIATE heparin discontinuation; switch to direct thrombin inhibitor",
         "Continued heparin worsens thrombotic complications", "apply", "Platelet transfusion"),
    ]),
    # 611
    ("Thrombophilia: inherited and acquired", "Medical", "Hematology", [
        ("What are the inherited thrombophilias and what is their relative thrombotic risk?",
         "Factor V Leiden (most common, 3-4× heterozygous), Prothrombin G20210A (2-3×), Antithrombin III (10×), Protein C (10×), Protein S (10×), MTHFR controversial",
         "Defects in anticoagulant proteins increase thrombotic risk", "recall", "Acquired thrombophilia"),
        ("What acquired thrombophilias are associated with VTE risk?",
         "Antiphospholipid syndrome: lupus anticoagulant, anticardiolipin, beta-2 glycoprotein; others: malignancy, nephrotic, OCPs, HRT, pregnancy, postpartum, immobility",
         "Acquired states often transient or modifiable; APS requires lifelong anticoagulation", "recall", "Inherited thrombophilia"),
        ("When should thrombophilia testing be performed and what is the duration of anticoagulation?",
         "Test provoked VTE if unprovoked, family Hx, recurrent, unusual site; unprovoked with thrombophilia or recurrent: indefinite; provoked: 3-6 months usually",
         "Thrombophilia presence predicts recurrence and guides duration", "apply", "Standard 3-month anticoagulation"),
    ]),
    # 612
    ("Thrombotic microangiopathies (TMA)", "Medical", "Hematology", [
        ("What is the pathophysiology and clinical presentation of thrombotic microangiopathies?",
         "Platelet consumption on damaged vessel walls causes thrombocytopenia, fragmented RBCs (schistocytes), hemolytic anemia; pentad: thrombocytopenia, MAHA, fever, renal, neurologic",
         "Microthrombi from endothelial injury or platelet activation cause multisystem involvement", "analyze", "Simple hemolytic anemia"),
        ("What is the distinction between thrombotic thrombocytopenic purpura (TTP) and hemolytic uremic syndrome (HUS)?",
         "TTP: ADAMTS13 deficiency (acquired), neuro symptoms prominent; HUS: Shiga toxin (E. coli O157), diarrhea prodrome, renal failure dominant, often children",
         "Underlying mechanism and clinical emphasis differ", "apply", "No distinction"),
        ("How is TTP treated emergently?",
         "Plasma exchange daily until platelet recovery and LDH normalization; AVOID platelet transfusion (triggers thrombosis); steroids may be added",
         "Plasma exchange removes antibodies against ADAMTS13", "apply", "Platelet transfusion"),
    ]),
    # 613
    ("Type 1 Diabetes Mellitus", "Medical", "Endocrinology", [
        ("What is the pathophysiology of Type 1 Diabetes Mellitus?",
         "Autoimmune destruction of beta cells (T cells, antibodies to GAD, IA-2, ZnT8); absolute insulin deficiency; rapid onset; associated with HLA, other autoimmune",
         "Beta cell loss irreversible; external insulin always required", "recall", "Type 2 DM"),
        ("What are the acute complications of Type 1 Diabetes?",
         "DKA: absolute insulin deficiency causes ketosis, pH <7.3, anion gap metabolic acidosis; treat with insulin infusion, fluids; hypoglycemia: insulin excess, treated with glucose",
         "DKA life-threatening, requires ICU-level insulin and electrolyte replacement", "recall", "HHS (Type 2)"),
        ("What intensive insulin regimen achieves glycemic targets in Type 1 Diabetes?",
         "Basal-bolus: long-acting (glargine, detemir) once daily + rapid-acting (lispro, aspart) with meals; carb-to-insulin ratios individualized; target HbA1c <7%",
         "Mimics physiologic insulin secretion; flexible dosing improves quality of life", "apply", "Fixed insulin"),
    ]),
    # 614
    ("Type 2 Diabetes Mellitus: Pathophysiology & Diagnosis", "Medical", "Endocrinology", [
        ("What is the pathophysiology of Type 2 Diabetes Mellitus?",
         "Insulin resistance (impaired glucose uptake) + progressive beta cell dysfunction; relative (not absolute) insulin deficiency; genetic predisposition + obesity + sedentary",
         "Dual defect central: resistance precedes beta cell failure", "analyze", "Type 1 DM"),
        ("What are the diagnostic criteria for Type 2 Diabetes?",
         "Fasting glucose ≥126 mg/dL, 2h OGTT ≥200, HbA1c ≥6.5%, random glucose ≥200 with symptoms; repeat if asymptomatic",
         "Multiple test options reflect different glucose phases", "recall", "Prediabetes"),
        ("What are the first-line medications for Type 2 Diabetes?",
         "Metformin: reduces hepatic glucose production; second-line: GLP-1 agonists (CV/weight), SGLT2 inhibitors (renal/CV), sulfonylureas (hypoglycemia); insulin if oral fail",
         "Metformin addresses insulin resistance; newer agents offer organ protection", "apply", "Insulin first-line"),
    ]),
    # 615
    ("Ulcerative Colitis: Diagnosis & Classification", "Medical", "Gastroenterology", [
        ("What is the pathophysiology and clinical presentation of ulcerative colitis?",
         "Chronic, continuous mucosal inflammation of colon/rectum (not small bowel, not transmural); bloody diarrhea, tenesmus, LLQ pain, systemic symptoms",
         "Superficial mucosal involvement distinguishes UC from Crohn's", "recall", "Crohn's disease"),
        ("How is ulcerative colitis classified by disease extent?",
         "Proctitis: rectum only; left-sided colitis: splenic flexure; pancolitis: entire colon; extent guides therapy and prognosis",
         "Extent predicts response to therapy and complication risk", "recall", "Activity severity"),
        ("What are the diagnostic features of ulcerative colitis on colonoscopy and histology?",
         "Continuous, circumferential inflammation; loss of vascular pattern; friability; pseudopolyps; histology: superficial crypt distortion, acute inflammation, crypt abscesses, no granulomas",
         "Superficial inflammation and lack of transmural involvement differentiate UC", "recall", "Crohn's disease findings"),
    ]),
    # 616
    ("Urinary incontinence & catheter management", "Medical", "Urology", [
        ("What are the types of urinary incontinence and their mechanisms?",
         "Stress: urethral sphincter incompetence with Valsalva; Urge: overactive detrusor; Overflow: chronic retention with leakage; Mixed: stress + urge",
         "Mechanism determines therapeutic approach", "recall", "Simple categorization"),
        ("What are the indications for indwelling urinary catheterization in hospitalized patients?",
         "Acute urinary retention (obstruction, neurogenic), accurate UOP monitoring (critical illness), prolonged bed rest/end-of-life; AVOID for convenience",
         "Catheters increase UTI and urosepsis risk", "apply", "Routine catheterization"),
        ("What are the complications of long-term indwelling catheters and how are they prevented?",
         "UTI/urosepsis, bladder stones, strictures, encrustation; prevent with sterile insertion, regular change (4-6 weeks), hydration, empty bag regularly, remove ASAP",
         "Biofilm formation on catheters predisposes to infection", "apply", "Long-term without change"),
    ]),
    # 617
    ("Venipuncture-related & line complications on cross-cover", "Medical", "Critical Care", [
        ("What are the common complications of peripheral venous access and how are they recognized?",
         "Infiltration: swelling, pain, dysfunction; Phlebitis: erythema, warmth, palpable cord; Infection: fever, systemic toxicity; Extravasation: tissue necrosis from vesicants",
         "Early recognition allows line removal before systemic infection", "apply", "Expected irritation"),
        ("What is the acute management of central line malposition or occlusion?",
         "Malposition: chest X-ray, reposition or replace; thrombotic: aspiration, urokinase flush (10,000 U/mL), repeat, replace if unsuccessful; mechanical: check kinks/dressing",
         "Prompt diagnosis and intervention prevent sepsis and line loss", "apply", "Force flush through occluded"),
        ("How is central line-associated bloodstream infection (CLABSI) recognized and managed?",
         "Fever, rigors, hypotension from line; blood cultures from line and peripheral; remove line if suspected; empiric broad-spectrum antibiotics",
         "Early line removal critical to source control", "apply", "Leave line in place"),
    ]),
    # 618
    ("Venous Thromboembolic Disease in the Context of Cardiac Care", "Medical", "Cardiology", [
        ("What is the relationship between cardiac disease and VTE risk?",
         "Heart failure: dilated ventricle, reduced flow promote thrombus; Atrial fibrillation: LA appendage stasis; Post-MI: apical thrombus, anterior STEMI; Dilated cardiomyopathy",
         "Cardiac pathology creates thrombogenic environment via stasis and endothelial injury", "analyze", "PE as primary"),
        ("How is left ventricular thrombus detected and managed post-MI?",
         "Echo screening after anterior STEMI (apical akinesis); CT if inconclusive; anticoagulation (warfarin INR 2-3 or LMWH) x 3 months minimum",
         "LV thrombus risk highest post-anterior MI; anticoagulation prevents embolism", "apply", "No anticoagulation"),
        ("What anticoagulation strategy is used for atrial fibrillation to prevent cardioembolism?",
         "CHA2DS2-VASc score determines anticoagulation; ≥1 (men) or ≥2 (women): warfarin (INR 2-3) or DOAC preferred",
         "Anticoagulation targets LA appendage thrombus; DOACs equally effective as warfarin", "apply", "Aspirin-only strategy"),
    ]),
    # 619
    ("Venous thromboembolism: DVT & pulmonary embolism", "Medical", "Hematology", [
        ("What is the pathophysiology of venous thromboembolism and what initiates formation?",
         "Virchow triad: stasis, endothelial injury, hypercoagulability; thrombus forms in deep veins and may embolize",
         "Multiple risk factors compound; any one may suffice", "analyze", "Single cause"),
        ("How is deep venous thrombosis (DVT) diagnosed?",
         "Duplex ultrasound (compression, loss of flow): proximal vs. distal; D-dimer <500 essentially rules out in low-risk",
         "Ultrasound non-invasive; compression criteria gold standard", "apply", "D-dimer as diagnostic"),
        ("What is the standard anticoagulation therapy for VTE and what is the typical duration?",
         "Acute: UFH (IV) or LMWH (SC) or fondaparinux; transition to warfarin (INR 2-3) or DOAC; provoked: 3 months; unprovoked/thrombophilia: 3-6 months or indefinite",
         "Therapeutic anticoagulation prevents propagation and recurrence", "apply", "IVC filter as sole"),
    ]),
    # 620
    ("Viral Hepatitis B", "Medical", "Hepatology", [
        ("What is the serologic pattern in acute Hepatitis B infection?",
         "HBsAg appears first, persists; anti-HBc IgM peaks early, indicates acute; anti-HBc total remains indefinitely; HBeAg high during replication; anti-HBe with clearance",
         "IgM anti-HBc is marker of acute HBV", "recall", "HBsAg presence = chronic"),
        ("What determines progression to chronic Hepatitis B infection?",
         ">95% of infants/young children progress; <10% of adults clear infection; HBeAg seroconversion typically signals control",
         "Pediatric infection has poor immune clearance", "apply", "Age-independent progression"),
        ("When is antiviral therapy indicated in chronic Hepatitis B?",
         "Treat if HBV DNA >2,000 IU/mL and abnormal ALT or fibrosis (F2+); nucleos(t)ide analogs first-line; interferon alternative",
         "Viral replication + liver injury indicates high progression risk", "apply", "Treatment regardless"),
    ]),
    # 621
    ("Viral Hepatitis C", "Medical", "Hepatology", [
        ("What is the natural history of Hepatitis C infection?",
         ">80% asymptomatic acute, 15-45% spontaneous clearance, 55-85% progress to chronic; slow progression to cirrhosis over 15-30 years",
         "Most infections silent; chronic slowly damages liver", "recall", "Rapid progression"),
        ("How is Hepatitis C diagnosed and what markers indicate acute vs. chronic infection?",
         "Anti-HCV antibody (positive in acute and chronic); HCV RNA detectable confirms replication; IgM suggests acute; genotype determines treatment",
         "Antibody screening followed by RNA confirms diagnosis", "apply", "Positive antibody = cured"),
        ("What is the treatment of chronic Hepatitis C?",
         "Direct-acting antivirals (DAAs): sofosbuvir-based, pangenotypic; 8-12 week course; cure rate >95%; treat all HCV RNA-positive regardless of stage",
         "DAAs transformed HCV from incurable to curable", "apply", "Interferon/ribavirin"),
    ]),
    # 622
    ("Vitamin D Physiology & Deficiency", "Medical", "Endocrinology", [
        ("What is the physiology of vitamin D activation and regulation?",
         "Skin synthesis (7-dehydrocholesterol + UVB) or dietary → D3; liver 25-hydroxylation → 25(OH)D; kidney 1-alpha-hydroxylation → 1,25(OH)2D; PTH stimulates, FGF23 inhibits",
         "Sequential activation ensures adequate active metabolite; PTH maintains balance", "analyze", "D and 1,25(OH)2D equivalent"),
        ("What defines Vitamin D deficiency and what are the clinical consequences?",
         "Deficiency: 25(OH)D <20 ng/mL; insufficiency: 20-29; causes osteomalacia (bone pain, myopathy), impaired calcium absorption, secondary hyperparathyroidism",
         "Low active metabolite and high PTH cause negative calcium balance", "apply", "Simple mineral deficiency"),
        ("How is Vitamin D deficiency treated?",
         "Mild deficiency: oral cholecalciferol (D3) 1,000-2,000 IU daily or weekly; severe: oral calcitriol (active form); ensure adequate Ca and phosphate",
         "D3 replaces stores and corrects secondary hyperparathyroidism", "apply", "Calcitriol first-line"),
    ]),
    # 623
    ("Von Willebrand disease", "Medical", "Hematology", [
        ("What is the pathophysiology and classification of Von Willebrand disease?",
         "VWF deficiency (quantitative) or dysfunction (qualitative); Type 1 (80%): mild reduction VWF and Factor VIII; Type 2: qualitative defect; Type 3: absent VWF",
         "VWF mediates platelet adhesion and carries Factor VIII", "analyze", "Hemophilia A"),
        ("How is Von Willebrand disease diagnosed?",
         "VWF antigen (VWF:Ag), VWF activity (VWF:RCo or VWF:GPM), Factor VIII level; VWF:RCo/VWF:Ag ratio <0.6 suggests Type 2",
         "Multiple tests needed because VWF varies with stress, estrogen, blood type", "apply", "aPTT prolongation"),
        ("What is the treatment of Von Willebrand disease?",
         "Desmopressin (DDAVP): increases VWF and Factor VIII release; works for Type 1 and some Type 2; VWF concentrates for Type 3 or DDAVP-unresponsive",
         "DDAVP releases endogenous VWF if stores available", "apply", "Fresh frozen plasma"),
    ]),
    # 624
    ("Acid-Base Physiology", "Medical", "Physiology", [
        ("What are the primary acid-base disorders and their ABG signatures?",
         "Metabolic acidosis: pH <7.35, HCO3- <22, low PaCO2; Metabolic alkalosis: pH >7.45, HCO3- >26, high PaCO2; Respiratory acidosis: pH <7.35, high PaCO2; Respiratory alkalosis: pH >7.45, low",
         "pH and primary derangement identify the disorder", "recall", "Acidosis/alkalosis without pH"),
        ("What is the anion gap and how is it used to classify metabolic acidosis?",
         "AG = [Na+] - ([Cl-] + [HCO3-]); normal 8-16; AG acidosis: organic acids accumulate (lactate, ketones); normal AG: GI HCO3 loss or renal retention",
         "AG identifies whether acidosis is acid accumulation or bicarbonate loss", "apply", "Without HCO3 context"),
        ("What is the osmol gap and when is it clinically useful?",
         "Osmol gap = measured - calculated osmolarity [(2×Na) + (glucose/18) + (BUN/2.8)]; normal <10; elevated suggests unmeasured osmoles (ethanol, methanol, ethylene glycol)",
         "Elevated gap indicates toxin presence", "apply", "AG alone in toxins"),
    ]),
    # 625
    ("Acute Pain Pathophysiology", "Medical", "Anesthesia", [
        ("What are the components of the pain pathway from nociceptor to brain?",
         "A-delta myelinated = sharp/acute, C unmyelinated = dull/chronic; dorsal horn (substance P, glutamate); spinothalamic tract; thalamus and cortex; descending modulation via serotonin/NE",
         "Multi-step pathway allows multiple intervention points", "analyze", "Linear nociceptor-to-brain"),
        ("How do NSAIDs and opioids differ in their mechanisms of analgesia?",
         "NSAIDs: block COX, inhibit prostaglandin production peripherally, reduce inflammation; opioids: bind mu receptors centrally, inhibit neurotransmitter release, analgesia and sedation",
         "NSAIDs address inflammation; opioids address central processing", "analyze", "Equivalent mechanisms"),
        ("What is multimodal analgesia and why is it superior to monotherapy?",
         "Combining agents targeting different pathways (opioid + NSAID + local + adjuvant): reduces doses, side effects, tolerance; improves analgesia",
         "Synergistic effects allow lower individual drug doses", "apply", "Single high-dose agent"),
    ]),
    # 626
    ("Acute on Chronic Pain Flares", "Medical", "Anesthesia", [
        ("What distinguishes an acute-on-chronic pain flare from acute pain in a pain-naive patient?",
         "Flare: superimposed acute exacerbation on chronic baseline; may indicate new pathology or destabilization; opioid tolerance present; baseline meds may be insufficient",
         "Opioid tolerance and altered pain physiology require higher doses", "apply", "Routine acute pain approach"),
        ("How is opioid tolerance managed in acute-on-chronic pain flares?",
         "Do NOT reduce opioid dose; pain typically requires escalation; continue baseline + acute medications; may need rotation to different opioid or higher-potency",
         "Tolerance is physiologic adaptation; maintaining baseline prevents withdrawal", "apply", "Dose reduction"),
        ("What acute etiologies must be excluded in a patient with known chronic pain presenting with flare?",
         "Infection (osteomyelitis, abscess), structural (new fracture, compartment syndrome), thromboembolic, acute coronary, acute abdomen; do NOT assume benign exacerbation",
         "Chronic pain history biases toward attribution; serious pathology can be missed", "apply", "Assume chronic disease"),
    ]),
]

# Build KPs from template
for topic_tuple in topics_data:
    topic, domain, discipline, kp_list = topic_tuple
    chunks = slice_items[topics_data.index(topic_tuple)].get('chunks', [])
    source = get_source(chunks)

    for n, (stem, answer, rationale, bloom, confusable) in enumerate(kp_list, start=1):
        add_kp(topic, domain, discipline, stem, answer, rationale, bloom, source, confusable, n)

# Write JSON
output_json = json.dumps(kps, ensure_ascii=False, indent=2)
with open('data/kp_full_part_18.json', 'w', encoding='utf-8') as f:
    f.write(output_json)

# Validate
try:
    json.loads(output_json)
    topic_count = len(set([kp['topic'] for kp in kps]))
    script_count = 0  # No illness scripts in this batch
    pair_count = 0    # No confusable pairs in this batch
    print(f"part 18: {topic_count} topics, {len(kps)} KPs, {script_count} scripts, {pair_count} pairs, parses OK")
except json.JSONDecodeError as e:
    print(f"ERROR: {e}")
