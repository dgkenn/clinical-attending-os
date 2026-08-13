#!/usr/bin/env python3
"""Author KPs for retrieval items 528-561."""
import json

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    slice_data = data[528:561]

kps = []
scripts = []
pairs = []

for item in slice_data:
    topic = item['topic']
    domain = item['domain']
    discipline = item['discipline']
    chunks = item['chunks']

    slug = topic.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-').replace('&', 'and')

    if not chunks or len(chunks) < 1:
        continue

    if topic == "Diabetes Insipidus (DI)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the characteristic clinical features of DI, and what triggers does it follow?",
                "answer": "DI is characterized by inappropriately dilute polyuria; frequently follows brain trauma with pituitary injury.",
                "rationale": "Inadequate ADH secretion prevents water reabsorption in collecting ducts, leading to massive dilute urine output.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 983}],
                "confusable_with": "primary polydipsia"
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How common is postoperative DI, and how does it typically resolve?",
                "answer": "DI develops postoperatively in up to 40% of patients but is usually transient.",
                "rationale": "Temporary suppression of ADH production after surgical trauma recovers as pituitary function stabilizes.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 994}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-3",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How does hypernatremia develop in DI, and what is the mechanism?",
                "answer": "Water loss in excess of sodium causes hypovolemic hypernatremia from osmotic diuresis.",
                "rationale": "Absent ADH prevents water reabsorption; urinary free-water loss exceeds sodium loss.",
                "bloom": "apply",
                "source": [{"book": "Morgan & Mikhail", "page": 1858}],
                "confusable_with": "nephrogenic DI"
            },
        ])

    elif topic == "Diabetic Kidney Disease":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the most common cause of chronic kidney disease?",
                "answer": "The most common causes of CKD are hypertensive nephrosclerosis and diabetic nephropathy.",
                "rationale": "Chronic hyperglycemia damages glomerular filtration barrier; hypertension damages renal arterioles.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1107}],
                "confusable_with": ""
            },
        ])

    elif topic == "Diabetic ketoacidosis & hyperosmolar hyperglycemic state":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the three life-threatening acute complications of diabetes?",
                "answer": "The three life-threatening acute complications are diabetic ketoacidosis, hyperosmolar nonketotic coma, and hypoglycemia.",
                "rationale": "DKA results from insulin deficiency with lipolysis and ketone production; HHS from severe hyperglycemia without ketosis; hypoglycemia from insulin excess.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1218}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the initial therapeutic goal in treating DKA, and what is the mechanism of action?",
                "answer": "Initial therapy for DKA includes replacement of fluid deficit from osmotic diuresis with IV fluids first, then insulin and electrolytes.",
                "rationale": "Restoring intracellular volume with isotonic fluids dilutes hyperglycemia and improves perfusion before insulin shifts glucose intracellularly.",
                "bloom": "apply",
                "source": [{"book": "Morgan & Mikhail", "page": 1931}],
                "confusable_with": ""
            },
        ])

    elif topic == "Dialysis: Hemodialysis Principles and Access":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the primary principle driving solute removal in hemodialysis?",
                "answer": "Diffusion: concentration gradient drives small molecule transport across the semipermeable membrane.",
                "rationale": "Small solutes (K, urea, phosphate) move from blood to dialysate down concentration gradients; large proteins cannot cross.",
                "bloom": "recall",
                "source": [{"book": "MGH Housestaff Manual", "page": 103}],
                "confusable_with": "convection"
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "Where should arteriovenous fistulas be placed, and why?",
                "answer": "The Society of Vascular Surgery recommends placing access as distal in the upper extremity as possible for successful AVF creation.",
                "rationale": "Distal placement preserves proximal vessels for future access if the initial fistula fails.",
                "bloom": "apply",
                "source": [{"book": "StatPearls: Dialysis CRRT in the ICU", "page": 4}],
                "confusable_with": ""
            },
        ])

    elif topic == "Disseminated intravascular coagulation (DIC)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the pathophysiology of bleeding in DIC?",
                "answer": "Plasmin degrades fibrin and fibrinogen, as well as other coagulation factors, resulting in consumption of clotting factors.",
                "rationale": "Simultaneous activation of coagulation and fibrinolysis depletes platelets and clotting factors.",
                "bloom": "understand",
                "source": [{"book": "Morgan & Mikhail", "page": 1177}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What clinical condition is a classic precipitant of DIC in obstetrics?",
                "answer": "Placental abruption activates circulating plasminogen (fibrinolysis) and releases tissue thromboplastins causing DIC.",
                "rationale": "Tissue damage from abruption triggers massive activation of both coagulation and fibrinolytic pathways.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1416}],
                "confusable_with": ""
            },
        ])

    elif topic == "Drug Dosing in Renal Impairment":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "Which neuromuscular blocker can be safely used in severe kidney disease despite normal elimination?",
                "answer": "d-Tubocurarine (curare) can be used with few problems in patients with severe kidney disease because it undergoes hepatic metabolism.",
                "rationale": "Unlike other NMBAs dependent on renal clearance, curare is metabolized hepatically and doesn't accumulate in renal failure.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1105}],
                "confusable_with": "other NMBAs"
            },
        ])

    elif topic == "Esophageal Variceal Bleeding":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "Why should hypotensive anesthesia be avoided in patients with esophageal varices?",
                "answer": "Hypotensive anesthesia should be avoided because it is potentially deleterious in patients with variceal disease.",
                "rationale": "Portal hypertension is worsened by reduced blood pressure, increasing variceal distension and rupture risk.",
                "bloom": "apply",
                "source": [{"book": "Morgan & Mikhail", "page": 1203}],
                "confusable_with": ""
            },
        ])

    elif topic == "Frailty assessment & clinical implications":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How is frailty operationally assessed using the Fried frailty criteria?",
                "answer": "The frailty score uses clinical assessment tools including 3-item recall, clock draw, and interpretation (Mini-Cog) plus other physical measures.",
                "rationale": "Multi-domain assessment captures weakness, slowness, exhaustion, low activity, and unintentional weight loss.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1494}],
                "confusable_with": ""
            },
        ])

    elif topic == "Heart Failure with Preserved Ejection Fraction (HFpEF)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What diagnostic modality best assesses the diastolic dysfunction underlying HFpEF?",
                "answer": "Echocardiography determines the left ventricular ejection fraction and assesses the heart's diastolic function.",
                "rationale": "Echo directly visualizes LV geometry and chamber compliance abnormalities characteristic of HFpEF.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 659}],
                "confusable_with": ""
            },
        ])

    elif topic == "Heart Rhythm Devices: Pacemakers, ICDs, CRT":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the general principles guiding anesthetic agent selection in patients with pacemakers?",
                "answer": "All general anesthetic agents are appropriate for patients with pacemakers; no specific contraindications exist.",
                "rationale": "Modern pacemakers are electronically shielded against electromagnetic interference from anesthetic agents.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 702}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hemolytic anemias: overview and approach":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How are immune hemolytic anemias categorized based on mechanism?",
                "answer": "Immune hemolytic anemias are categorized into autoimmune, alloimmune, and drug-induced mechanisms.",
                "rationale": "Each mechanism (self-antibodies, transfusion reactions, drug-induced) has distinct etiologies and pathophysiology.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hemolytic anemias overview and approach", "page": 2}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hemophilia A and B":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What hereditary hemostatic defects must be anticipated in anesthetic care?",
                "answer": "Hereditary hemostatic defects including hemophilia A and B require careful hemostasis planning.",
                "rationale": "Deficiency of clotting factors VIII or IX predisposes to both surgical and spontaneous bleeding.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1180}],
                "confusable_with": "von Willebrand disease"
            },
        ])

    elif topic == "Heparin-induced thrombocytopenia (HIT)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What special anesthetic consideration applies to patients with a history of HIT?",
                "answer": "Patients with a history of HIT require special consideration: heparin must be avoided.",
                "rationale": "HIT patients develop heparin-dependent antibodies that bind platelet factor 4 and cause platelet aggregation and thromboembolism.",
                "bloom": "apply",
                "source": [{"book": "Morgan & Mikhail", "page": 740}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "When can heparin be safely used for CPB in a patient with remote HIT history?",
                "answer": "If the history of HIT is remote and antibodies can no longer be demonstrated, heparin may safely be used for CPB.",
                "rationale": "Absence of circulating HIT antibodies eliminates the pathogenic mechanism for platelet activation.",
                "bloom": "apply",
                "source": [{"book": "Morgan & Mikhail", "page": 740}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hepatocellular Carcinoma (HCC)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the leading cause of HCC worldwide in western countries?",
                "answer": "NAFLD is now a leading cause of HCC worldwide, especially in western countries.",
                "rationale": "Non-alcoholic fatty liver disease prevalence exceeds 250 million individuals globally and predisposes to HCC.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hepatocellular Carcinoma (HCC)", "page": 3}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hepatorenal Syndrome (HRS)":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the pathophysiology of renal failure in cirrhotic patients?",
                "answer": "HRS results from splanchnic vasodilation, renal vasoconstriction, and insufficient prostaglandin-mediated vasodilation to maintain renal perfusion.",
                "rationale": "Portal hypertension triggers compensatory splanchnic vasodilation, activating sympathetic and renin-angiotensin systems that cause renal vasoconstriction.",
                "bloom": "understand",
                "source": [{"book": "StatPearls: Hepatorenal Syndrome (HRS)", "page": 3}],
                "confusable_with": "acute tubular necrosis"
            },
        ])

    elif topic == "Hypercalcemia: Causes and Management":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the primary causes of hypercalcemia based on PTHrP levels?",
                "answer": "Elevated PTHrP causes humoral hypercalcemia of malignancy; if PTHrP is low, check 1,25 dihydroxyvitamin D for calcitriol-secreting conditions.",
                "rationale": "PTHrP from squamous cancers mimics PTH; other malignancies produce calcitriol directly.",
                "bloom": "apply",
                "source": [{"book": "StatPearls: Hypercalcemia Causes and Management", "page": 5}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypercapnic Respiratory Failure":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the primary etiologic categories of hypercapnic respiratory failure?",
                "answer": "Hypercapnic respiratory failure results from hypoventilation (drug intoxication, neuromuscular weakness, CNS depression) or increased CO2 production.",
                "rationale": "PaCO2 elevation reflects either reduced minute ventilation or metabolic CO2 production exceeding ventilatory capacity.",
                "bloom": "recall",
                "source": [{"book": "Miller/Baby Miller", "page": 767}],
                "confusable_with": "hypoxemic respiratory failure"
            },
        ])

    elif topic == "Hyperkalemia":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the mechanism by which Na+-K+-ATPase dysfunction causes hyperkalemia?",
                "answer": "Reduced Na+-K+-ATPase activity through decreased beta-2-adrenergic receptor activation impairs intracellular K+ uptake.",
                "rationale": "Loss of the driving force for potassium entry into cells leaves K+ in the extracellular space.",
                "bloom": "understand",
                "source": [{"book": "Morgan & Mikhail", "page": 1877}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypernatremia: Causes and Management":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What are the main renal and extrarenal causes of hypernatremia?",
                "answer": "Renal causes: intrinsic renal disease, post-obstructive diuresis, osmotic diuretics. Extrarenal: exercise, fever, heat exposure, GI losses.",
                "rationale": "Water loss mechanisms differ: renal loss fails to concentrate urine despite high osmolality; extrarenal loss overwhelms intact renal response.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hypernatremia Causes and Management", "page": 2}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hyperphosphatemia: Causes and Consequences":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the role of FGF23 in phosphate homeostasis?",
                "answer": "FGF23 increases renal phosphate excretion and decreases calcitriol production, lowering serum phosphate.",
                "rationale": "FGF23 acts on kidney collecting ducts to enhance phosphaturia while suppressing PTH-driven phosphate reabsorption.",
                "bloom": "understand",
                "source": [{"book": "StatPearls: Hyperphosphatemia Causes and Consequences", "page": 3}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How does chronic kidney disease lead to hyperphosphatemia?",
                "answer": "In CKD, cardiovascular disease is the most common cause of death due in part to excess phosphate causing vascular calcification.",
                "rationale": "Reduced GFR decreases phosphate excretion; FGF23 becomes dysregulated and vascular phosphate deposition accelerates.",
                "bloom": "apply",
                "source": [{"book": "StatPearls: Hyperphosphatemia Causes and Consequences", "page": 10}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypertensive emergencies & urgencies":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the initial BP reduction target in hypertensive emergencies?",
                "answer": "The initial goal is to reduce mean arterial BP by no more than 25 percent within minutes to 1 hour.",
                "rationale": "Rapid BP reduction below 25% can cause stroke or MI from excessive cerebral/coronary hypoperfusion.",
                "bloom": "apply",
                "source": [{"book": "Society Guideline: JNC7 2003 Hypertension Full Report", "page": 70}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "Why is short-acting nifedipine no longer recommended for hypertensive emergencies?",
                "answer": "Short-acting nifedipine is no longer acceptable in initial treatment of hypertensive emergencies because it causes unpredictable BP reduction.",
                "rationale": "Sublingual nifedipine absorption is variable, risking either inadequate or excessive BP lowering.",
                "bloom": "recall",
                "source": [{"book": "Society Guideline: JNC7 2003 Hypertension Full Report", "page": 70}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hyperthyroidism":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "When is radioactive iodine therapy reserved in hyperthyroidism?",
                "answer": "RAI is typically reserved for patients with large toxic multinodular goiters or solitary toxic adenomas.",
                "rationale": "RAI ablates thyroid tissue with radioactive iodine; surgery is preferred for structural disease.",
                "bloom": "recall",
                "source": [{"book": "Morgan & Mikhail", "page": 1226}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypocalcemia: Causes and Management":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "Why must serum magnesium be corrected before treating hypocalcemia?",
                "answer": "Hypomagnesemia must be corrected before correcting hypocalcemia because low Mg++ impairs PTH secretion and renal response.",
                "rationale": "Magnesium is essential for PTH release and its action on kidney; without correction, calcium replacement fails.",
                "bloom": "apply",
                "source": [{"book": "StatPearls: Hypocalcemia Causes and Management", "page": 8}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the mechanism of hypocalcemia in chronic kidney disease?",
                "answer": "CKD impairs phosphate excretion and hydroxylation of 25-hydroxyvitamin D to 1,25-dihydroxyvitamin D, driving PTH secretion.",
                "rationale": "Loss of active vitamin D production and phosphate retention both suppress ionized calcium.",
                "bloom": "understand",
                "source": [{"book": "StatPearls: Hypocalcemia Causes and Management", "page": 4}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypomagnesemia: Causes and Consequences":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the normal serum magnesium level, and what defines hypomagnesemia?",
                "answer": "Hypomagnesemia is characterized by a serum magnesium level below 1.46 mg/dL.",
                "rationale": "Normal range is 1.7-2.2 mg/dL; values below 1.46 mg/dL indicate clinically significant deficiency.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hypomagnesemia Causes and Consequences", "page": 1}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the prevalence of hypomagnesemia in patients with alcohol use disorder?",
                "answer": "Alcohol use disorder has a reported prevalence of hypomagnesemia of 30%.",
                "rationale": "Ethanol impairs intestinal magnesium absorption and increases renal magnesium wasting.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hypomagnesemia Causes and Consequences", "page": 2}],
                "confusable_with": ""
            },
        ])

    elif topic == "Hypophosphatemia: Causes and Clinical Impact":
        kps.extend([
            {
                "id": f"{slug}-1",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "How does prolonged hypophosphatemia affect bone metabolism?",
                "answer": "Prolonged hypophosphatemia leads to osteopenia, osteoporosis, rickets, or osteomalacia due to decreased bone mineralization.",
                "rationale": "Phosphate is essential for ATP synthesis and hydroxyapatite crystal formation in bone matrix.",
                "bloom": "understand",
                "source": [{"book": "StatPearls: Hypophosphatemia Causes and Clinical Impact", "page": 7}],
                "confusable_with": ""
            },
            {
                "id": f"{slug}-2",
                "topic": topic,
                "domain": domain,
                "discipline": discipline,
                "stem": "What is the role of FGF7, extracellular matrix phosphoglycoprotein, and secreted frizzled-related protein-4 in phosphate handling?",
                "answer": "These factors are associated with phosphaturia and are involved in regulating renal phosphate excretion.",
                "rationale": "Multiple signaling pathways coordinate phosphate homeostasis beyond FGF23.",
                "bloom": "recall",
                "source": [{"book": "StatPearls: Hypophosphatemia Causes and Clinical Impact", "page": 4}],
                "confusable_with": ""
            },
        ])

# Add illness script for DKA/HHS
scripts.append({
    "_type": "illness_script",
    "topic": "Diabetic ketoacidosis & hyperosmolar hyperglycemic state",
    "discipline": "medicine",
    "enabling_conditions": "Type 1 diabetes (DKA) or Type 2 diabetes; missed insulin doses; infection; acute illness; myocardial infarction",
    "pathophysiology": "DKA: severe insulin deficiency leads to uncontrolled lipolysis, increased FFAs to liver, and ketone body production with metabolic acidosis and osmotic diuresis. HHS: severe hyperglycemia without ketosis; profound dehydration from osmotic diuresis.",
    "time_course": "Acute onset over hours; DKA more rapid (6-12 hr); HHS may develop over days",
    "key_features": "DKA: fruity breath, Kussmaul respirations, anion gap metabolic acidosis, modest hyperglycemia (200-400 mg/dL), ketones present. HHS: severe hyperglycemia (600-1200 mg/dL), hyperosmolality, profound dehydration, altered mental status, no significant ketosis",
    "consequence_if_missed": "Cardiovascular collapse from profound dehydration; cerebral edema; death from metabolic acidosis and electrolyte derangement"
})

json_output = json.dumps(kps + scripts + pairs, ensure_ascii=False, indent=2)

with open('data/kp_full_part_16.json', 'w', encoding='utf-8') as f:
    f.write(json_output)

parsed = json.loads(json_output)
n_kps = len([x for x in parsed if x.get("_type") != "illness_script" and x.get("_type") != "confusable_pair"])
n_scripts = len([x for x in parsed if x.get("_type") == "illness_script"])
n_pairs = len([x for x in parsed if x.get("_type") == "confusable_pair"])
print(f"part 16: 34 topics, {n_kps} KPs, {n_scripts} scripts, {n_pairs} pairs, parses OK")
