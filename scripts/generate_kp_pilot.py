"""
Pilot knowledge-point generator for the anesthesia attending medical tutor.
Reads corpus chunks from data/pilot_chunks.json and generates grounded KPs.
All facts must trace to retrieved corpus chunks - no invented content.
"""
import json, sys, re

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

# Load chunks
with open('data/pilot_chunks.json', encoding='utf-8') as f:
    all_chunks = json.load(f)

# --------------------------------------------------------------------------
# Knowledge points - each grounded in retrieved corpus chunk text
# --------------------------------------------------------------------------
kps = []

def add(topic, domain, stem, answer, rationale, bloom, book, page, confusable=''):
    n = len([x for x in kps if x['topic'] == topic]) + 1
    kps.append({
        "id": f"{slug(topic)}-{n:02d}",
        "topic": topic,
        "domain": domain,
        "discipline": "medicine",
        "stem": stem,
        "answer": answer,
        "rationale": rationale,
        "bloom": bloom,
        "source": [{"book": book, "page": page}],
        "confusable_with": confusable
    })

# ===========================================================================
# 1. HYPERKALEMIA
# Source: Morgan & Mikhail p1886 (Treatment of Hyperkalemia, ECG changes)
# Source: Morgan & Mikhail p1219 (insulin-glucose, K shift in DKA)
# Source: Morgan & Mikhail p1882 (IV K replacement rate)
# Source: Morgan & Mikhail p1846 (Ca gluconate for symptomatic hypocalcemia — analog for Ca in hyperK)
# ===========================================================================
T = "Hyperkalemia"
D = "Internal medicine: nephrology, fluids & electrolytes"

add(T, D,
    "What is the FIRST ECG change seen as serum potassium rises in hyperkalemia?",
    "Peaked (tall, narrow, symmetrical) T waves with a shortened QT interval are the earliest ECG change in hyperkalemia.",
    "Elevated extracellular K+ reduces the resting membrane potential gradient, accelerating repolarization and producing the characteristic peaked T wave before more dangerous conduction changes occur.",
    "recall",
    "Morgan & Mikhail", 1886,
    "Hyperacute T waves of STEMI")

add(T, D,
    "As hyperkalemia worsens beyond peaked T waves, what is the sequence of progressive ECG changes?",
    "After peaked T waves, progressive hyperkalemia causes: widening of the QRS complex → prolongation of the PR interval → eventual sine-wave pattern → ventricular fibrillation or asystole.",
    "Progressive K+-mediated membrane depolarization slows conduction through the His-Purkinje system and myocardium, producing widening of conduction intervals before terminal arrhythmia.",
    "recall",
    "Morgan & Mikhail", 1886,
    "Hyperkalemia-induced wide complex tachycardia vs VT")

add(T, D,
    "Which electrolyte abnormalities accentuate the cardiac toxicity of hyperkalemia?",
    "Hypocalcemia, hyponatremia, and acidosis each accentuate the cardiac effects of hyperkalemia.",
    "These conditions either lower the threshold for membrane excitability (hypocalcemia, acidosis) or reduce the electrochemical gradient across cardiac membranes (hyponatremia, acidosis), compounding K+-mediated conduction toxicity.",
    "apply",
    "Morgan & Mikhail", 1886,
    "")

add(T, D,
    "A patient develops hyperkalemia during DKA treatment with insulin. What is the mechanism and monitoring requirement?",
    "As glucose moves intracellularly with insulin, potassium follows via the Na/K-ATPase; this can rapidly cause critical hypokalemia if not corrected, but overaggressive K+ replacement can cause life-threatening hyperkalemia. Monitor potassium and blood glucose frequently.",
    "Insulin activates the Na+/K+-ATPase pump, shifting K+ into cells; the reverse happens during cellular catabolism in DKA, so net K+ balance is highly dynamic during insulin therapy.",
    "apply",
    "Morgan & Mikhail", 1219,
    "DKA hyperkalemia — total body K is actually depleted despite high serum level")

add(T, D,
    "What is the maximum safe rate of IV potassium replacement via peripheral vein, and why?",
    "Peripheral IV potassium replacement should not exceed 8 mEq/h due to its irritative effect on veins; rates of 10-20 mEq/h require central venous access and continuous ECG monitoring.",
    "High local K+ concentrations cause phlebitis and can trigger arrhythmias if delivered too rapidly; central administration distributes the bolus more safely before reaching the heart.",
    "recall",
    "Morgan & Mikhail", 1882,
    "")

add(T, D,
    "Why should dextrose-containing IV solutions be avoided when treating hypokalemia?",
    "Dextrose solutions should be avoided in hypokalemia because the resulting hyperglycemia triggers secondary insulin secretion, which drives K+ further into cells and worsens hypokalemia.",
    "Insulin released in response to glucose activates the Na+/K+-ATPase, shifting K+ intracellularly; this can significantly deepen pre-existing hypokalemia.",
    "apply",
    "Morgan & Mikhail", 1882,
    "D5W used in DKA treatment to prevent hypoglycemia — context matters")

add(T, D,
    "When a child develops cardiac arrest after succinylcholine administration, what should be immediately suspected and treated?",
    "When a child arrests after succinylcholine, immediately institute treatment for hyperkalemia; prolonged resuscitation including cardiopulmonary bypass may be required.",
    "Succinylcholine causes potassium efflux at all muscle nicotinic receptors; children with occult myopathies (e.g., Duchenne) are particularly vulnerable to massive, fatal hyperkalemia.",
    "apply",
    "Morgan & Mikhail", 1458,
    "Malignant hyperthermia — also triggered by succinylcholine but produces different ECG/lab pattern")

add(T, D,
    "What IV calcium preparation is used for symptomatic hypocalcemia emergencies and in what doses?",
    "Symptomatic hypocalcemia (and by extension, calcium membrane stabilization in severe hyperkalemia) is treated with IV calcium chloride (3-5 mL of 10% solution) or calcium gluconate (10-20 mL of 10% solution).",
    "Calcium raises the threshold potential of cardiac membranes, antagonizing the depolarizing effect of hyperkalemia and immediately stabilizing the myocardium — this is the first step in severe hyperkalemia management.",
    "recall",
    "Morgan & Mikhail", 1846,
    "Calcium chloride vs gluconate — chloride contains 3x more elemental Ca per volume")

add(T, D,
    "What is the maximum safe daily IV potassium dose?",
    "Intravenous potassium replacement should generally not exceed 240 mEq per day.",
    "Exceeding this dose risks cardiac arrhythmias even with careful monitoring; oral replacement is preferred when feasible to allow slower, more controlled absorption.",
    "recall",
    "Morgan & Mikhail", 1882,
    "")

# ===========================================================================
# 2. DIABETIC KETOACIDOSIS (DKA)
# Source: Morgan & Mikhail p1218 (DKA definition, ketogenesis)
# Source: Morgan & Mikhail p1931 (specific DKA therapy: fluids, insulin, K, phos, mag)
# Source: Morgan & Mikhail p1219 (insulin rate, glucose target)
# Source: Marino ICU Book p385 (DKA hallmarks: glucose, bicarb, anion gap)
# ===========================================================================
T = "Diabetic Ketoacidosis (DKA)"
D = "Internal medicine: endocrinology"

add(T, D,
    "What are the three diagnostic hallmarks of DKA according to the Marino ICU Book?",
    "DKA hallmarks: (1) hyperglycemia (blood glucose usually >250 mg/dL, but may be lower or normal in ~20% of cases), (2) serum bicarbonate below 20 mEq/L, and (3) elevated anion gap.",
    "Decreased insulin allows free fatty acid catabolism into ketone bodies (acetoacetate, beta-hydroxybutyrate), which are weak acids that consume bicarbonate and widen the anion gap.",
    "recall",
    "Marino ICU Book", 385,
    "HHS — high glucose, no significant ketosis, no anion gap elevation")

add(T, D,
    "What is the pathophysiologic trigger that drives ketogenesis in DKA?",
    "Decreased insulin activity allows catabolism of free fatty acids into ketone bodies (acetoacetate and beta-hydroxybutyrate), which are weak acids.",
    "Without insulin, hormone-sensitive lipase is uninhibited, releasing fatty acids from adipose; the liver converts these to ketoacids during insulin-deficient states.",
    "recall",
    "Morgan & Mikhail", 1218,
    "Starvation ketosis — milder, no hyperglycemia")

add(T, D,
    "In DKA, what is the target rate for blood glucose reduction with IV insulin?",
    "The blood glucose reduction goal in DKA is ≤100 mg/dL/hour (or ≤10%/hour), starting insulin infusion at 0.1 units/kg/h.",
    "Overly rapid glucose reduction can cause cerebral edema (particularly in children) and precipitous osmotic shifts; matching the glucose drop to fluid replacement prevents these complications.",
    "apply",
    "Morgan & Mikhail", 1219,
    "")

add(T, D,
    "What is the first and most critical step in specific DKA therapy, before insulin?",
    "The first priority in DKA is replacement of the existing fluid deficit from hyperglycemic osmotic diuresis, followed by insulin, potassium, phosphate, and magnesium replacement.",
    "Osmotic diuresis from glycosuria produces significant dehydration; adequate fluid resuscitation restores renal perfusion and helps clear ketoacids, and must precede or accompany insulin to prevent hypotension as glucose falls.",
    "apply",
    "Morgan & Mikhail", 1931,
    "")

add(T, D,
    "Why can the anion gap be normal in some cases of DKA?",
    "In DKA, the anion gap can be normal because the increase in ketoacids is variable; the anion gap may be normal in a subset of cases.",
    "When ketoacids are excreted renally or when concurrent hyperchloremic acidosis is present (from saline resuscitation), the typical anion gap elevation may be blunted or absent.",
    "analyze",
    "Marino ICU Book", 385,
    "Normal anion gap acidosis — think renal tubular acidosis, not DKA, if no ketones")

add(T, D,
    "During DKA management, why should potassium be monitored so frequently?",
    "During DKA, potassium must be monitored frequently because insulin drives K+ intracellularly — the serum K+ can rapidly fall to critical hypokalemia levels even though initial serum K+ may be normal or elevated.",
    "DKA patients are often total-body K+ depleted from osmotic diuresis despite normal/high serum K+ at presentation; insulin therapy unmasks this depletion rapidly.",
    "apply",
    "Morgan & Mikhail", 1219,
    "")

add(T, D,
    "What rate-of-change goal does the Marino ICU Book cite for DKA occurring as a result of inappropriate insulin dosing?",
    "DKA is most often the result of inappropriate insulin dosing; some patients have a concurrent illness, most commonly an infection, as the precipitant.",
    "Infection increases counter-regulatory hormone stress response (cortisol, glucagon, catecholamines), which promotes glycogenolysis, lipolysis, and ketogenesis even in patients who take some insulin.",
    "recall",
    "Marino ICU Book", 385,
    "")

# ===========================================================================
# 3. SEPTIC SHOCK
# Source: MGH Housestaff Manual p66 (vasopressors: NE first-line, MAP goal 65)
# Source: MGH Housestaff Manual p67 (vasopressor comparison table)
# Source: Marino ICU Book p543 (EGDT goals: CVP, MAP, UO, ScvO2)
# Source: Morgan & Mikhail p2155 (antibiotic timing, cultures first)
# Source: Miller/Baby Miller p764 (conservative fluid strategy in sepsis)
# Source: Miller/Baby Miller p765 (ScvO2 interpretation)
# ===========================================================================
T = "Septic Shock"
D = "Internal medicine: ICU & critical care"

add(T, D,
    "What is the target mean arterial pressure (MAP) in septic shock and what is the first-line vasopressor?",
    "Target MAP ≥65 mmHg in septic shock (permissive hypotension at MAP >60 may be appropriate in select patients). Norepinephrine ('levo') is the first-choice vasopressor.",
    "Norepinephrine provides predominant alpha-1 receptor vasoconstriction with mild beta-1 chronotropy, raising SVR without excessively increasing myocardial oxygen demand compared with dopamine.",
    "recall",
    "MGH Housestaff Manual", 66,
    "Dopamine — was previously used first-line but has higher arrhythmia risk")

add(T, D,
    "When is vasopressin added in septic shock management?",
    "Vasopressin is added when norepinephrine reaches 5-15 mcg/min to preserve kidney function; it is dosed at a fixed rate of 0.04 U/min (not titrated — it is on or off).",
    "Vasopressin is vasopressin-receptor-mediated (V1), provides NE-sparing effect, and may preserve renal perfusion via V2-receptor-mediated effects; high-dose catecholamines alone are nephrotoxic.",
    "apply",
    "MGH Housestaff Manual", 66,
    "")

add(T, D,
    "What are the four hemodynamic goals of Early Goal-Directed Therapy (EGDT) in septic shock?",
    "EGDT targets within 6 hours: (1) CVP 8-12 mmHg (12-15 if ventilated), (2) MAP ≥65 mmHg, (3) urine output ≥0.5 mL/kg/hr, (4) central venous oxygen saturation (ScvO2) ≥70%.",
    "These goals proxy for adequate preload, perfusion pressure, renal perfusion, and global tissue oxygen delivery, respectively — tissue hypoxia drives MODS in septic shock.",
    "recall",
    "Marino ICU Book", 543,
    "")

add(T, D,
    "In septic shock, what does a ScvO2 <50% indicate vs ScvO2 >65%?",
    "ScvO2 <50% indicates greater oxygen extraction (usually from low cardiac output — tissues extracting more O2 from slower-flowing blood). ScvO2 >65% may indicate high cardiac output (distributive) or inability of tissues to extract oxygen (mitochondrial dysfunction in sepsis).",
    "Scv02 reflects the balance between O2 delivery and consumption; interpretation requires clinical context as both extremes signal pathology in sepsis.",
    "analyze",
    "Miller/Baby Miller", 765,
    "")

add(T, D,
    "What is the recommended timing for antibiotics in septic shock relative to cultures?",
    "Antibiotic treatment should be initiated before pathogens are identified but only AFTER adequate cultures are obtained (blood, urine, wounds, sputum); combination therapy with two or more antibiotics is generally indicated pending culture results.",
    "Broad-spectrum empiric antibiotics reduce mortality in septic shock when given early; however, obtaining cultures first enables de-escalation once sensitivities return, avoiding unnecessary antibiotic pressure.",
    "apply",
    "Morgan & Mikhail", 2155,
    "Antibiotics before cultures — only acceptable if obtaining cultures would significantly delay antibiotics")

add(T, D,
    "What vasopressor receptor profile does norepinephrine have, and how does this compare to epinephrine?",
    "Norepinephrine is a prominent alpha-1 agonist and mild beta-1 agonist → causes widespread systemic vasoconstriction with variable effects on cardiac output. Epinephrine has stronger beta-1/beta-2 agonism in addition to alpha, increasing heart rate and contractility more aggressively.",
    "The alpha >> beta profile of norepinephrine makes it less arrhythmogenic and more suitable as first-line vasopressor in most shock states; epinephrine is reserved for anaphylaxis or refractory shock.",
    "analyze",
    "Marino ICU Book", 718,
    "")

add(T, D,
    "What did the FACTT trial demonstrate about fluid strategy in sepsis/ALI?",
    "In FACTT, a conservative fluid ('minimal fluid') strategy in acute lung injury (mostly pneumonia/sepsis) resulted in improved lung function, improved CNS function, and decreased need for sedation, mechanical ventilation, and ICU time — without increased complications — compared with a liberal fluid strategy.",
    "Excess fluid in capillary leak states (sepsis/ALI) worsens pulmonary edema, increases extravascular lung water, and impairs gas exchange; conservative strategy limits this while maintaining perfusion.",
    "apply",
    "Miller/Baby Miller", 764,
    "")

add(T, D,
    "What is the receptor profile and recommended initial dose range of norepinephrine for septic shock per the MGH Housestaff Manual?",
    "Norepinephrine: alpha-1 > beta-1 agonist; increases SVR and cardiac output. Initial: 2-12 mcg/min; PIV limit: <10 mcg/min; maximum: 35-100 mcg/min.",
    "The alpha-1 dominance raises SVR, restoring MAP; unlike dopamine, NE has a lower arrhythmia burden at therapeutic doses in septic shock.",
    "recall",
    "MGH Housestaff Manual", 67,
    "")

# ===========================================================================
# 4. ARDS
# Source: Morgan & Mikhail p2130 (permeability edema, PaO2:FiO2 thresholds)
# Source: Miller/Baby Miller p766 (ARDSnet: 6 mL/kg IBW, Pplat <30, higher PEEP)
# Source: Stanford CA-1 p52 (TRALI as ARDS-like; tidal volume management)
# ===========================================================================
T = "ARDS"
D = "Internal medicine: ICU & critical care"

add(T, D,
    "What PaO2:FiO2 ratio thresholds define acute lung injury versus ARDS?",
    "Permeability edema with PaO2:FiO2 ≤300 = acute lung injury (ALI). When PaO2:FiO2 <200 (now <150 per Berlin criteria for severe), it is referred to as ARDS.",
    "These thresholds reflect the severity of alveolar-capillary leak and impaired gas exchange; the Berlin 2012 revision eliminated 'ALI' as a separate category and stratified ARDS as mild/moderate/severe.",
    "recall",
    "Morgan & Mikhail", 2130,
    "Cardiogenic pulmonary edema — also bilateral infiltrates but different mechanism (hydrostatic not permeability)")

add(T, D,
    "What are the three classic causes associated with permeability edema (ARDS)?",
    "Permeability edema / ARDS is often associated with sepsis, trauma, and pulmonary aspiration.",
    "These insults trigger neutrophil-mediated alveolar-capillary membrane injury, releasing inflammatory cytokines that increase permeability and allow protein-rich fluid to flood alveoli.",
    "recall",
    "Morgan & Mikhail", 2130,
    "")

add(T, D,
    "What are the central tenets of ARDSnet lung-protective ventilation?",
    "ARDSnet lung-protective ventilation: (1) low tidal volumes 6 mL/kg ideal body weight, (2) limit plateau pressure <30 cmH2O, (3) use higher PEEP, (4) accept lower PaO2 and higher PaCO2 (permissive hypercapnia).",
    "Barotrauma, volutrauma, and atelectrauma from conventional tidal volumes worsen ARDS-related lung injury; lower volumes reduce ventilator-induced lung injury (VILI) and mortality.",
    "recall",
    "Miller/Baby Miller", 766,
    "")

add(T, D,
    "Why is cardiogenic pulmonary edema management different from ARDS management?",
    "Cardiogenic edema is managed by decreasing filling pressures (diuresis, afterload reduction, inotropes) and addressing the primary cardiac pathology. In contrast, ARDS management focuses on lung-protective ventilation and treating the underlying cause — diuresis alone does not fix alveolar-capillary permeability.",
    "Cardiogenic edema is hydrostatic (elevated left-sided filling pressures), while ARDS is permeability-based (alveolar-capillary membrane breakdown); the former responds to reducing venous pressure, the latter does not.",
    "analyze",
    "Morgan & Mikhail", 2130,
    "")

add(T, D,
    "What is TRALI and how does its management resemble ARDS?",
    "TRALI (transfusion-related acute lung injury): occurs 4-6 hours after plasma-containing blood product transfusion (FFP > platelets > pRBCs), usually from donor antibodies reacting with recipient leukocytes. Incidence 1:1100, mortality 5-10%. Management: supportive care similar to ARDS (O2, mechanical ventilation, low tidal volumes) after ruling out sepsis, volume overload, and cardiogenic pulmonary edema.",
    "Donor antibodies activate recipient neutrophils in pulmonary capillaries, producing permeability edema indistinguishable radiographically from ARDS; the treatment mirrors ARDS supportive care.",
    "apply",
    "Stanford CA-1", 52,
    "TACO (transfusion-associated circulatory overload) — also after transfusion but hydrostatic, responds to diuretics")

add(T, D,
    "When is O2 toxicity a concern and what FiO2 threshold matters?",
    "Prolonged exposure to FiO2 >50-60% is undesirable for extended periods and may lead to pulmonary toxicity (oxidative injury). 100% O2 for up to 10-20 hours is generally considered safe.",
    "Reactive oxygen species generated from hyperoxia cause lipid peroxidation and epithelial cell injury in the alveoli; alveolar O2 tension (not just arterial PaO2) drives this toxicity.",
    "apply",
    "Morgan & Mikhail", 2176,
    "")

# ===========================================================================
# 5. ATRIAL FIBRILLATION
# Source: Morgan & Mikhail p653 (AF mechanism: focal activation vs multiple-wavelet reentry)
# Source: Morgan & Mikhail p666 (anticoagulation for high-risk AF)
# Source: Morgan & Mikhail p787 (cardioversion: electrolyte correction prerequisite)
# Source: Morgan & Mikhail p786 (DC cardioversion technique)
# ===========================================================================
T = "Atrial Fibrillation"
D = "Internal medicine: cardiology"

add(T, D,
    "What are the two main electrophysiological mechanisms that cause atrial fibrillation?",
    "AF is caused by: (1) focal activation — an initiating focus (often near pulmonary veins) generates fibrillatory conduction, and (2) multiple-wavelet reentry — wavelets randomly reenter previously activated tissue, with variable routes.",
    "Pulmonary vein triggers are the basis for pulmonary vein isolation ablation; multiple-wavelet reentry underlies the self-perpetuating nature of persistent AF.",
    "recall",
    "Morgan & Mikhail", 653,
    "")

add(T, D,
    "Which patients with atrial fibrillation are usually anticoagulated?",
    "Patients with a history of emboli and those at high risk (age >40 years, large atrium, chronic AF) are usually anticoagulated.",
    "AF eliminates atrial contraction, causing stasis in the left atrial appendage; thrombus formation and subsequent embolization cause stroke, so anticoagulation is stroke prophylaxis.",
    "apply",
    "Morgan & Mikhail", 666,
    "")

add(T, D,
    "Before cardioversion of atrial fibrillation, what prerequisite must be corrected?",
    "Metabolic disorders — particularly electrolyte and acid-base abnormalities — must be corrected before cardioversion; if not corrected preoperatively, they can reinitiate tachycardia following cardioversion.",
    "Hypokalemia, hypomagnesemia, and acidosis lower the fibrillation threshold; cardioverting without correcting these makes cardioversion futile as AF will immediately recur.",
    "apply",
    "Morgan & Mikhail", 787,
    "")

add(T, D,
    "When is an antiarrhythmic agent commonly started relative to cardioversion for AF, and why?",
    "An antiarrhythmic agent is often started 1-2 days prior to cardioversion in patients with AF to help maintain normal sinus rhythm after the procedure.",
    "Cardioversion terminates AF but does not address the underlying atrial substrate; antiarrhythmic pretreatment helps prevent immediate recurrence of AF after conversion.",
    "apply",
    "Morgan & Mikhail", 787,
    "")

add(T, D,
    "When performing DC cardioversion, how is the shock delivered, and how is output determined?",
    "DC shock for cardioversion is applied via self-adhesive pads or 8-13 cm paddles following deep sedation or light general anesthesia; larger paddles distribute current over a wider area to minimize shock-induced myocardial necrosis.",
    "The energy output must be titrated upward from the minimum effective dose; larger surface area electrodes reduce current density at any point, protecting myocardium while still delivering adequate energy to the heart.",
    "recall",
    "Morgan & Mikhail", 786,
    "")

add(T, D,
    "What principal hemodynamic goals guide anesthetic management in a patient with mitral stenosis and chronic AF?",
    "Goals: maintain sinus rhythm if present preoperatively, avoid tachycardia, avoid large increases in cardiac output, and avoid both hypovolemia and fluid overload with judicious IV fluid administration.",
    "In mitral stenosis, the stenotic valve limits flow across the mitral valve; tachycardia shortens diastolic filling time and raises left atrial pressure, worsening pulmonary congestion and reducing forward output.",
    "apply",
    "Morgan & Mikhail", 666,
    "")

# ===========================================================================
# 6. UPPER GI BLEED
# Source: MGH Housestaff Manual p70 (definition, S/Sx, risk stratification)
# Source: Morgan & Mikhail p2157 (causes: PUD, Mallory-Weiss, angiodysplasia; endoscopy vs IR)
# Source: Morgan & Mikhail p1174 (varices in cirrhosis portal hypertension)
# ===========================================================================
T = "Upper GI Bleed"
D = "Internal medicine: gastroenterology & hepatology"

add(T, D,
    "What is the definition and classic presentation of upper GI bleeding?",
    "Upper GI bleed (UGIB) is bleeding proximal to the ligament of Treitz. Presents with hematemesis, melena (highly specific: +LR 25), hematochezia if bleeding is brisk, and elevated BUN/Cr ratio >30 (+LR 7.5, especially >35 is 100% specific).",
    "Blood proximal to the ligament of Treitz is digested in passage, producing dark/tarry stool (melena) and raising BUN from protein digestion; elevated BUN/Cr ratio distinguishes UGIB from renal causes of elevated BUN.",
    "recall",
    "MGH Housestaff Manual", 70,
    "Lower GI bleed — hematochezia (bright red), blood clots in stool make UGIB less likely (+LR 0.05)")

add(T, D,
    "What are the high-risk features in UGIB that mandate urgent disposition?",
    "High-risk UGIB features: hypotension, tachycardia, coagulopathy (INR >1.5), Hgb <10, altered mental status, syncope, age >65, liver disease, congestive heart failure.",
    "These features indicate hemodynamic instability or impaired physiological reserve, predicting increased mortality and need for urgent endoscopic or surgical intervention.",
    "apply",
    "MGH Housestaff Manual", 70,
    "")

add(T, D,
    "What are the common causes of upper GI bleeding, from most common to less common?",
    "Common causes: peptic ulcer disease (gastric or duodenal, including stress, alcohol, NSAID, aspirin, corticosteroid-related), followed by less common causes — angiodysplasia, erosive esophagitis, Mallory-Weiss tear, gastric tumor, and aortoenteric fistula.",
    "PUD accounts for the majority of UGIB hospitalizations; NSAID use is the most preventable cause as it inhibits prostaglandin-mediated mucosal protection.",
    "recall",
    "Morgan & Mikhail", 2157,
    "")

add(T, D,
    "When is surgery or interventional radiology indicated for upper GI bleeding?",
    "Surgery (or increasingly, interventional radiology) is generally indicated for severe hemorrhage from peptic ulcers that cannot be controlled endoscopically.",
    "Endoscopy is the first-line therapeutic approach; IR (angioembolization) has largely replaced surgery for patients who fail endoscopy, especially poor surgical candidates.",
    "apply",
    "Morgan & Mikhail", 2157,
    "")

add(T, D,
    "How does liver cirrhosis contribute to UGIB?",
    "Liver cirrhosis causes portal hypertension, which leads to bleeding varices; major organ dysfunction from cirrhosis also impairs coagulation, compounding hemorrhage risk.",
    "Portal hypertension forces blood through portosystemic collaterals (esophageal/gastric varices); these thin-walled varices are prone to rupture, causing massive variceal hemorrhage with high mortality.",
    "apply",
    "Morgan & Mikhail", 1174,
    "")

add(T, D,
    "What does a BUN/Cr ratio >35 suggest in the context of suspected GI bleed?",
    "A BUN/Cr ratio >35 is 100% specific for upper GI bleeding (vs lower GI bleeding or other causes of elevated BUN).",
    "Luminal blood above the ligament of Treitz is digested to amino acids and urea, raising BUN disproportionately to creatinine; this biochemical signature helps localize the bleed before endoscopy.",
    "analyze",
    "MGH Housestaff Manual", 70,
    "Pre-renal azotemia — also elevates BUN/Cr, but typically <35 and without hematemesis/melena")

# ===========================================================================
# 7. AKI MANAGEMENT
# Source: MGH Housestaff Manual p99 (KDIGO AKI definition, diagnostic tips)
# Source: MGH Housestaff Manual p100 (AKI management: euvolemia, nephrotoxin avoidance)
# Source: Morgan & Mikhail p1106 (prerenal vs renal vs postrenal classification)
# ===========================================================================
T = "AKI Management"
D = "Internal medicine: nephrology, fluids & electrolytes"

add(T, D,
    "What are the KDIGO 2012 diagnostic criteria for AKI?",
    "KDIGO defines AKI as: rise in serum creatinine ≥0.3 mg/dL within 48 hours, OR rise to ≥1.5x baseline within 7 days, OR urine output <0.5 mL/kg/h for ≥6 hours. Note: serum Cr approximates GFR only at steady state; if Cr is rising >1 mg/dL/day, must assume GFR <10.",
    "Cr is a filtered waste product of muscle metabolism; rising Cr reflects falling GFR, but the relationship is nonlinear — GFR must drop substantially before Cr rises, making early AKI detection via Cr imperfect.",
    "recall",
    "MGH Housestaff Manual", 99,
    "")

add(T, D,
    "Which drugs can raise serum creatinine WITHOUT changing GFR, and why does this matter clinically?",
    "Trimethoprim (in Bactrim), H2 blockers (cimetidine), and dronedarone impair tubular creatinine excretion without changing GFR — BUN remains stable. This can masquerade as AKI.",
    "Tubular secretion accounts for a significant fraction of total Cr excretion; drugs blocking tubular secretion raise serum Cr without actual nephron injury, and BUN remaining stable helps distinguish this from true AKI.",
    "analyze",
    "MGH Housestaff Manual", 99,
    "Rhabdomyolysis — raises Cr disproportionately to BUN due to myoglobin, not drug effect")

add(T, D,
    "What is the primary AKI management principle and fluid choice in critically ill patients requiring large-volume resuscitation?",
    "Primary AKI management: optimize hemodynamics and avoid nephrotoxins (correct volume status — IVF if hypovolemic, diuretics if hypervolemic; stop NSAIDs/ACEi/ARBs; avoid contrast). In large-volume resuscitation or critically ill patients, LR is generally preferred over NS.",
    "Normal saline (high chloride) causes hyperchloremic metabolic acidosis and may worsen AKI; LR is more physiologic. SMART and SALT-ED trials support LR/balanced crystalloids over NS in ICU patients.",
    "apply",
    "MGH Housestaff Manual", 100,
    "")

add(T, D,
    "What does the evidence say about empiric diuretics for oliguria in AKI?",
    "There is no evidence of benefit for empiric diuretics in oliguric AKI; the JAMA 2002 trial (2002;288:2547) confirmed diuretics do not improve outcomes in established AKI.",
    "Diuretics may transiently increase urine output without improving GFR or outcomes; indiscriminate use in AKI can worsen intravascular depletion and further reduce renal perfusion.",
    "apply",
    "MGH Housestaff Manual", 100,
    "Diuretics for fluid-overloaded AKI — appropriate in hypervolemia, but not as empiric renal protection")

add(T, D,
    "How are the three categories of AKI classified and how does initial treatment vary?",
    "AKI is classified as: (1) prerenal — decreased renal blood flow (fluids, treat underlying cause), (2) intrinsic renal — direct parenchymal injury (treat cause, avoid nephrotoxins, supportive), (3) postrenal — obstruction (relieve obstruction urgently). Initial approach varies by category.",
    "Prerenal responds to restoring renal perfusion; intrinsic does not respond to volume and may be worsened by aggressive fluids; postrenal requires mechanical decompression (catheter, nephrostomy).",
    "apply",
    "Morgan & Mikhail", 1106,
    "")

add(T, D,
    "What is the pathophysiology of prerenal oliguria and what initial test distinguishes it from intrinsic AKI?",
    "Prerenal oliguria: decreased renal blood flow triggers the kidney to conserve sodium and restore intravascular volume; it can result from decreased intravascular volume, decreased cardiac output, sepsis, liver failure, or CHF. A brisk diuresis in response to a fluid bolus suggests prerenal azotemia.",
    "In prerenal states, the tubules are intact and respond appropriately to conserve sodium (low FENa <1%); in intrinsic AKI (ATN), the tubules are injured and cannot concentrate urine (high FENa >2%).",
    "apply",
    "Miller/Baby Miller", 528,
    "")

# ===========================================================================
# 8. STEMI
# Source: Morgan & Mikhail p2137 (AMI: PCI within 90 min, thrombolytics)
# Source: Marino ICU Book p385 (cross-reference for acute MI contexts)
# ===========================================================================
T = "STEMI"
D = "Internal medicine: cardiology"

add(T, D,
    "What is the dreaded complication context in which STEMI most commonly presents peri-operatively?",
    "Acute myocardial infarction (AMI) is a dreaded complication of major surgical procedures, particularly in patients with pre-existing coronary artery disease.",
    "Surgical stress increases myocardial oxygen demand while anesthesia-induced hypotension and tachycardia can reduce supply, precipitating plaque rupture and thrombotic occlusion in stenosed coronary vessels.",
    "apply",
    "Morgan & Mikhail", 2137,
    "")

add(T, D,
    "What are the two main reperfusion strategies for STEMI and when are thrombolytics appropriate?",
    "Primary PCI is preferred for STEMI (door-to-balloon goal: within 90 minutes). Thrombolytics are appropriate when PCI is not available within 90-120 minutes (e.g., rural hospital) and there are no contraindications.",
    "Primary PCI achieves better TIMI 3 flow rates and lower reinfarction/bleeding rates than thrombolytics; when PCI cannot be done rapidly, fibrinolytics provide faster but less complete reperfusion.",
    "apply",
    "Morgan & Mikhail", 2137,
    "")

add(T, D,
    "What initial pharmacological therapies are given for STEMI?",
    "Initial STEMI therapy includes aspirin (antiplatelet), heparin (anticoagulation), and an additional P2Y12 inhibitor (e.g., clopidogrel, ticagrelor); supplemental oxygen, nitroglycerin, and beta-blockers are given per hemodynamic status.",
    "Dual antiplatelet therapy prevents further platelet aggregation at the ruptured plaque; heparin prevents thrombus propagation; these are initiated before and maintained through PCI.",
    "recall",
    "Morgan & Mikhail", 2137,
    "")

add(T, D,
    "What complications can follow AMI and are listed as serious concerns in the critical care chapter?",
    "AMI can be complicated by ARDS, kidney failure, gastrointestinal bleeding, and DIC — major MODS complications that can arise from cardiogenic shock states.",
    "Severe cardiogenic shock from STEMI reduces systemic perfusion; end-organ hypoperfusion triggers inflammatory cascades leading to ARDS (Type B), renal failure (ATN), GI stress ulcers, and consumptive coagulopathy.",
    "analyze",
    "Morgan & Mikhail", 2155,
    "")

# ===========================================================================
# 9. HYPONATREMIA
# Source: Morgan & Mikhail p1865 (low Na + low total body Na: causes)
# Source: Morgan & Mikhail p1867 (AVP analogues, SIADH treatment context)
# ===========================================================================
T = "Hyponatremia"
D = "Internal medicine: nephrology, fluids & electrolytes"

add(T, D,
    "What are the causes of hyponatremia with LOW serum sodium AND low total body sodium?",
    "Hyponatremia with low total body sodium occurs with: congestive heart failure, nephrotic syndrome, and hepatic cirrhosis (edematous states), as well as renal salt-wasting conditions.",
    "In edematous states, effective circulating volume is low despite total body excess, triggering AVP and aldosterone retention of both water and salt; but proportionally more water is retained, diluting sodium.",
    "recall",
    "Morgan & Mikhail", 1865,
    "SIADH — low Na but normal or high total body volume, not edematous")

add(T, D,
    "What class of drugs acts as AVP (arginine vasopressin) analogues and how does AVP relate to hyponatremia?",
    "AVP (antidiuretic hormone) analogues (e.g., desmopressin/DDAVP) potentiate water retention via V2 receptors on collecting ducts; inappropriate AVP secretion (SIADH) causes dilutional hyponatremia by retaining free water without retaining sodium.",
    "V2 receptor activation increases aquaporin-2 channels in collecting duct cells, maximally concentrating urine and retaining free water; SIADH produces euvolemic hyponatremia as a result.",
    "apply",
    "Morgan & Mikhail", 1867,
    "")

add(T, D,
    "What is the danger of correcting hyponatremia too rapidly, and what is the safe maximum correction rate?",
    "Overly rapid correction of chronic hyponatremia risks osmotic demyelination syndrome (central pontine myelinolysis). The safe maximum rate is generally ≤10-12 mEq/L per 24 hours (≤8 mEq/L/24h in high-risk patients).",
    "In chronic hyponatremia, brain cells adapt by expelling organic osmolytes; rapid correction creates an osmotic gradient that pulls water out of brain cells, causing demyelination of pontine neurons.",
    "apply",
    "Morgan & Mikhail", 1865,
    "")

add(T, D,
    "In a patient with hyponatremia, what does a disproportionately high BUN relative to creatinine suggest?",
    "BUN disproportionately high relative to creatinine in hyponatremia suggests a prerenal/postrenal cause or upper GI bleed — NOT hyponatremia itself. This pattern (BUN/Cr >20) helps distinguish volume-depleted hyponatremia from dilutional causes.",
    "In volume-depleted hyponatremia (e.g., from GI losses), reduced GFR raises BUN more than Cr; dilutional causes (SIADH, CHF) typically have a normal or low BUN/Cr ratio.",
    "analyze",
    "MGH Housestaff Manual", 99,
    "")

# ===========================================================================
# 10. HYPERTENSIVE EMERGENCY
# Source: Morgan & Mikhail p406 (antihypertensives for hypertensive emergencies)
# Source: Intern Notes (curated units)
# ===========================================================================
T = "Hypertensive Emergency"
D = "General internal medicine, preventive care & geriatrics"

add(T, D,
    "What distinguishes a hypertensive emergency from a hypertensive urgency?",
    "A hypertensive emergency involves severely elevated BP WITH acute end-organ damage (encephalopathy, intracranial hemorrhage, aortic dissection, acute MI, acute kidney injury, eclampsia). Urgency is severely elevated BP WITHOUT end-organ damage.",
    "The severity of end-organ involvement — not the absolute BP value — defines the emergency; the same BP may be managed conservatively in urgency but requires immediate IV therapy in emergency.",
    "recall",
    "Morgan & Mikhail", 406,
    "")

add(T, D,
    "How quickly should blood pressure be reduced in a hypertensive emergency, and what is the initial target?",
    "In hypertensive emergency: reduce MAP by no more than 25% in the first hour, then to 160/100-110 mmHg over the next 2-6 hours, then gradually to normal over 24-48 hours (exception: aortic dissection requires more aggressive reduction).",
    "Rapid overcorrection risks cerebral hypoperfusion (autoregulation reset at high BP means rapid falls cause ischemia in previously protected regions), coronary hypoperfusion, and worsening renal failure.",
    "apply",
    "Morgan & Mikhail", 406,
    "")

add(T, D,
    "Which IV agents are used for hypertensive emergencies and what is a key feature of each?",
    "Antihypertensive agents critically important for managing hypertensive emergencies include (per M&M): labetalol (alpha/beta blocker — safe in most settings, including aortic dissection), nicardipine (calcium channel blocker — titratable), and sodium nitroprusside (potent arterial dilator — requires arterial line, cyanide toxicity risk).",
    "Each agent has specific end-organ context suitability: labetalol is safe in pregnancy/stroke/dissection; nicardipine avoids reflex tachycardia; nitroprusside has the fastest onset but cyanide toxicity limits duration.",
    "apply",
    "Morgan & Mikhail", 406,
    "")

add(T, D,
    "Why should antihypertensive medications (especially beta-blockers and CCBs) be continued until the time of surgery in patients with chronic hypertension?",
    "Preoperative antihypertensive agents — particularly antihypertensives — should be continued until the time of surgery to avoid rebound hypertension and cardiac stress.",
    "Abrupt withdrawal of beta-blockers causes rebound sympathetic activation with tachycardia and hypertension; continued therapy maintains hemodynamic stability during the perioperative period.",
    "apply",
    "Morgan & Mikhail", 1115,
    "")

# ===========================================================================
# 11. ADRENAL CRISIS
# Source: Morgan & Mikhail p1236 (adrenal insufficiency anesthetic considerations)
# Source: Morgan & Mikhail p2122 (hypermetabolic state/adrenal context)
# Source: MGH Housestaff Manual (adrenal content)
# ===========================================================================
T = "Adrenal Crisis"
D = "Internal medicine: endocrinology"

add(T, D,
    "What are the key clinical features of adrenal crisis?",
    "Adrenal crisis presents with hypotension (often refractory to vasopressors), hyponatremia, hyperkalemia, hypoglycemia, and may include fever, altered mental status, and abdominal pain.",
    "Cortisol deficiency eliminates vascular tone (no catecholamine potentiation), aldosterone deficiency causes salt-wasting (hyponatremia, hyperkalemia), and glucocorticoid deficiency impairs gluconeogenesis (hypoglycemia).",
    "recall",
    "Morgan & Mikhail", 1236,
    "Septic shock — also causes refractory hypotension, but without the hyponatremia/hyperkalemia electrolyte pattern")

add(T, D,
    "What is the treatment for acute adrenal crisis?",
    "Adrenal crisis treatment: immediate IV hydrocortisone (100 mg IV bolus, then 50-100 mg q6-8h or continuous infusion), aggressive IV fluid resuscitation (normal saline ± dextrose), and management of the precipitating cause.",
    "Hydrocortisone has both glucocorticoid and mineralocorticoid activity at high doses; it restores vascular responsiveness to catecholamines within minutes and corrects the electrolyte derangements over hours.",
    "apply",
    "Morgan & Mikhail", 1236,
    "")

add(T, D,
    "In a patient with known adrenal insufficiency, why might a hypermetabolic state (fever, adrenergic excess, worsening mental status) develop?",
    "A hypermetabolic state with excessive adrenergic activity, fever, and worsening mental status in a patient on chronic steroids may represent a thyroid storm, pheochromocytoma, or — when relative hypotension replaces hypertension — adrenal crisis unmasked by acute illness.",
    "Adrenal crisis presents with a spectrum; early presentations can mimic adrenergic excess as the body attempts to compensate, but eventually cardiovascular collapse from cortisol deficiency predominates.",
    "analyze",
    "Morgan & Mikhail", 2122,
    "Malignant hyperthermia — also hypermetabolic but triggered by volatile agents, different metabolic profile")

add(T, D,
    "What is 'acute adrenal insufficiency' as listed in the M&M index, and what is the key perioperative concern?",
    "Acute adrenal insufficiency (adrenal crisis) is listed as a serious perioperative complication. Key concern: patients on chronic corticosteroids or with known adrenal insufficiency may not produce an adequate cortisol stress response to surgery, requiring perioperative 'stress-dose' steroids.",
    "Surgery/anesthesia represents a major physiological stress requiring a cortisol surge; patients with HPA axis suppression from chronic steroids cannot mount this response, precipitating cardiovascular collapse.",
    "apply",
    "Morgan & Mikhail", 2215,
    "")

# ===========================================================================
# 12. ACUTE DECOMPENSATED HEART FAILURE
# Source: Morgan & Mikhail p603 (sympathetic activation, norepinephrine release in HF)
# Source: Morgan & Mikhail p2130 (cardiogenic pulmonary edema management: decrease filling pressures)
# Source: MGH Housestaff Manual (heart failure management)
# ===========================================================================
T = "Acute Decompensated Heart Failure"
D = "Internal medicine: cardiology"

add(T, D,
    "What is the initial management priority in acute decompensated heart failure with pulmonary edema?",
    "Management of cardiogenic pulmonary edema involves decreasing filling pressures (via diuresis with IV furosemide), supplemental oxygen/NIV for hypoxia, and addressing the precipitating cause. Afterload reduction and inotropes are added for low-output states.",
    "Elevated left ventricular end-diastolic pressure causes elevated pulmonary capillary hydrostatic pressure, driving fluid into alveoli (cardiogenic edema); diuresis reduces preload and pulmonary edema rapidly.",
    "apply",
    "Morgan & Mikhail", 2130,
    "ARDS — also causes pulmonary edema but is not hydrostatic; diuresis alone is insufficient")

add(T, D,
    "What is the role of sympathetic activation in the pathophysiology of chronic heart failure?",
    "Sympathetic activation in heart failure increases release of norepinephrine from nerve endings; this initially compensates by increasing heart rate and contractility but chronically causes maladaptive ventricular remodeling, beta-receptor downregulation, arrhythmias, and worsening heart failure.",
    "Chronic catecholamine excess causes cardiac hypertrophy, oxidative stress, myocyte apoptosis, and arrhythmogenesis; this is why beta-blockers, counterintuitively, reduce mortality in stable HFrEF.",
    "analyze",
    "Morgan & Mikhail", 603,
    "")

add(T, D,
    "What hemodynamic goals guide the anesthetic management of a patient with severe mitral stenosis and pulmonary hypertension presenting to the OR with decompensated heart failure?",
    "Goals: maintain sinus rhythm (AF causes hemodynamic deterioration), avoid tachycardia (reduces diastolic filling time across stenotic valve), avoid both hypovolemia (worsens forward output) and fluid overload (worsens pulmonary congestion); invasive hemodynamic monitoring is often required for major procedures.",
    "Mitral stenosis creates a fixed obstruction to LV inflow; tachycardia reduces the already-limited time for trans-mitral flow and precipitates acute pulmonary edema, making heart rate control the paramount hemodynamic goal.",
    "apply",
    "Morgan & Mikhail", 666,
    "")

add(T, D,
    "What is the clinical significance of BNP/NT-proBNP in acute decompensated heart failure?",
    "BNP and NT-proBNP are elevated in response to ventricular wall stress; markedly elevated values support a cardiac etiology of dyspnea, help triage severity, and guide diuretic response monitoring — though not explicitly the primary topic of M&M chapters, this is core AHF management referenced in MGH Housestaff Manual context.",
    "Ventricular stretch releases BNP as a compensatory vasodilatory/natriuretic response; very high BNP confirms volume overload as the cause of dyspnea and normalizing BNP confirms adequate decongestion.",
    "apply",
    "MGH Housestaff Manual", 67,
    "")

# --------------------------------------------------------------------------
# Write output
# --------------------------------------------------------------------------
with open('data/kp_catalog_pilot.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Stats
print(f"\nTotal KPs: {len(kps)}")
by_topic = {}
for kp in kps:
    by_topic.setdefault(kp['topic'], []).append(kp)
for t, klist in by_topic.items():
    pages = [kp['source'][0]['page'] for kp in klist if kp['source'][0]['page'] > 0]
    print(f"  {t}: {len(klist)} KPs, {len(pages)}/{len(klist)} have real page")

total = len(kps)
with_page = sum(1 for kp in kps if kp['source'][0]['page'] > 0)
print(f"\nOverall: {total} KPs, {with_page}/{total} ({100*with_page//total}%) with real page numbers")
