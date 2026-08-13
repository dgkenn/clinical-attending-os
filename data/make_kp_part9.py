#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Author KP part 9 — items[297:330]"""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
sl = data[297:330]   # 33 items, indices 0-32

kps = []

def add(slug, topic, domain, disc, stem, answer, rationale, bloom, book, page, confusable=""):
    n = len([k for k in kps if k.get("id","").startswith(slug+"-")]) + 1
    kps.append({
        "id": f"{slug}-{n}",
        "topic": topic,
        "domain": domain,
        "discipline": disc,
        "stem": stem,
        "answer": answer,
        "rationale": rationale,
        "bloom": bloom,
        "source": [{"book": book, "page": page}],
        "confusable_with": confusable
    })

def script(topic, disc, enabling, patho, time_course, features, consequence):
    return {
        "_type": "illness_script",
        "topic": topic,
        "discipline": disc,
        "enabling_conditions": enabling,
        "pathophysiology": patho,
        "time_course": time_course,
        "key_features": features,
        "consequence_if_missed": consequence
    }

def pair(a, b, disc):
    return {"_type": "confusable_pair", "topic_a": a, "topic_b": b, "discriminator": disc}

# ── 0: Oxygen Delivery Systems and Airway Devices Physics ──────────────────────
t = sl[0]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='o2-delivery-physics'
add(slug,tp,dm,dc,
    "A nasal cannula at 6 L/min delivers approximately what FiO2, and why can it not be higher?",
    "Nasal cannula delivers ~4% FiO2 per 1 L/min above room air; at 6 L/min ~44% FiO2. It is variable-performance: patient tidal volume dilutes delivered O2, limiting achievable FiO2.",
    "Low-flow devices supply less than the patient's peak inspiratory flow, so room air is entrained around the cannula, diluting the FiO2.",
    "recall","Morgan & Mikhail",2167,"Simple face mask")
add(slug,tp,dm,dc,
    "Which oxygen device guarantees a precise FiO2 independent of the patient's breathing pattern?",
    "Venturi (air-entrainment) mask — a fixed orifice jet entrains a precise ratio of room air; total flow exceeds peak inspiratory demand, preventing room-air dilution. Delivers 24–50% FiO2.",
    "The Venturi principle creates a fixed air:O2 ratio; because total flow exceeds inspiratory demand, FiO2 is set by the jet orifice, not the patient's pattern.",
    "recall","Morgan & Mikhail",2173,"Non-rebreather mask")
add(slug,tp,dm,dc,
    "What limits a non-rebreather mask from achieving an FiO2 of 1.0?",
    "The non-rebreather mask achieves FiO2 ~0.60–0.80 at 10–15 L/min; imperfect face seal and side-port exhalation valves allow entrainment of some room air.",
    "A true seal equivalent to an anesthesia mask circuit is required for FiO2 = 1.0; the non-rebreather mask cannot provide this outside the OR.",
    "apply","Morgan & Mikhail",2167,"Venturi mask")
add(slug,tp,dm,dc,
    "Equipment-related adverse anesthesia outcomes are most commonly caused by what factor?",
    "Operator misuse of gas delivery systems — three times more prevalent than device malfunction; operator unfamiliarity or failure to verify machine function drives most closed claims.",
    "Modern anesthesia machines are mechanically reliable; the human-machine interface is the dominant failure mode.",
    "recall","Morgan & Mikhail",88,"Device malfunction")
add(slug,tp,dm,dc,
    "What FiO2 does a self-inflating BVM deliver without vs. with an O2 reservoir at 15 L/min?",
    "Without O2: ~21% (room air). With O2 at 15 L/min and reservoir bag: ~90–100% FiO2.",
    "The bag refills passively; the reservoir stores 100% O2 between breaths; a non-rebreathing valve prevents exhaled gas from re-entering.",
    "recall","Miller/Baby Miller",268,"Flow-inflating anesthesia bag")
add(slug,tp,dm,dc,
    "High-flow nasal cannula provides what CPAP-equivalent effect, and at what approximate magnitude?",
    "HFNC provides ~1–2 cmH2O of CPAP per 10 L/min flow by exceeding peak inspiratory flow and pressurizing the nasopharynx. At 60 L/min, ~4–6 cmH2O.",
    "Because delivered flow exceeds inspiratory demand, a positive pressure builds in the upper airway proportional to flow rate.",
    "apply","Morgan & Mikhail",2173,"Standard nasal cannula")

# ── 1: Palliative Care Integration in Critical Illness ─────────────────────────
t = sl[1]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='palliative-care-icu'
add(slug,tp,dm,dc,
    "What are the four core domains a palliative care team addresses in critically ill patients?",
    "Symptoms, goals of care, psychosocial issues, and spiritual issues — a biopsychosocial-spiritual approach.",
    "Palliative care addresses total suffering across physical, psychological, social, and existential dimensions, complementing disease-directed treatment.",
    "recall","Miller/Baby Miller",866,"Hospice (end-of-life only)")
add(slug,tp,dm,dc,
    "For a COPD patient with refractory dyspnea near end of life, which drug class is guideline-supported for palliation despite respiratory side effects?",
    "Opioids — accepted per ACCP for dyspnea palliation in advanced lung disease; withholding them out of fear of respiratory depression leads to undertreated suffering.",
    "Low-dose opioids reduce central perception of dyspnea; the principle of double effect supports their use when the goal is symptom relief.",
    "apply","Miller/Baby Miller",870,"Benzodiazepines for dyspnea")
add(slug,tp,dm,dc,
    "When should goals-of-care discussions be initiated for sepsis patients, and what content must they include?",
    "Early — patients at high risk for multi-organ failure and death should discuss limitations, incorporating chronic medical conditions alongside acute illness and predicted QoL.",
    "Sepsis carries high short-term mortality; early alignment prevents unwanted interventions and honors patient autonomy.",
    "apply","Society Guideline",49,"")
add(slug,tp,dm,dc,
    "What cognitive bias in surgical culture can impede timely palliative care integration?",
    "An exaggerated sense of accountability for the patient's outcome makes agreement on 'good' outcomes difficult and may delay transition to comfort-focused goals.",
    "Recognizing this cultural bias allows clinicians to separate their own emotional investment from the patient's actual prognosis and preferences.",
    "analyze","Miller/Baby Miller",867,"")
add(slug,tp,dm,dc,
    "Surviving Sepsis Campaign guidelines explicitly support what palliative care action in sepsis?",
    "A goals-of-care discussion should be held early, considering chronic medical conditions, invasiveness of interventions, prognosis, and patient-defined QoL; some patients may choose limitations on treatment.",
    "SSC formally integrates palliative care: not all patients with sepsis want maximal intervention, and guideline-concordant care includes honoring those preferences.",
    "recall","Society Guideline",50,"")

# ── 2: Pancreas and multivisceral transplant anesthesia ────────────────────────
t = sl[2]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='pancreas-transplant-anes'
add(slug,tp,dm,dc,
    "What are the two opposing glucose management hazards immediately after pancreas graft reperfusion?",
    "Intraoperative hyperglycemia (impairs islet function, promotes infection) AND postreperfusion hypoglycemia (graft begins secreting insulin abruptly); continuous glucose monitoring is mandatory.",
    "The newly perfused graft can release large insulin boluses as it begins functioning, while persistent hyperglycemia pre-reperfusion can damage the islets.",
    "apply","Miller/Baby Miller",693,"Liver transplant glucose management")
add(slug,tp,dm,dc,
    "Why are patients presenting for organ transplantation especially vulnerable during anesthetic induction?",
    "End-stage organ disease causes multi-system dysfunction: altered drug metabolism, reduced protein binding, cardiovascular compromise, and diminished physiologic reserve.",
    "End-organ failure changes PK/PD of all anesthetic agents and eliminates physiologic buffers against hemodynamic instability.",
    "apply","Miller/Baby Miller",693,"")
add(slug,tp,dm,dc,
    "Positive-pressure ventilation poses a specific risk in transplant patients with what cardiac condition?",
    "Severe pulmonary hypertension — PPV decreases venous return and increases RV afterload, risking cardiac arrest during induction; emergent cardiopulmonary bypass may be needed.",
    "The pressure-overloaded RV in pulmonary hypertension has little reserve; any increase in afterload or decrease in preload can cause acute RV failure.",
    "analyze","Miller/Baby Miller",692,"")
add(slug,tp,dm,dc,
    "What legal requirement must be met before organ procurement can begin?",
    "Donor death must be formally declared (brain death or cardiac death) before procurement; donation after brain death (DBD) is most common; DCD is increasing due to organ shortages.",
    "Separation of end-of-life care from donation requires death declaration to eliminate any conflict of interest in the care team.",
    "recall","Miller/Baby Miller",685,"")
add(slug,tp,dm,dc,
    "In a patient with an emphysematous bulla who requires positive-pressure ventilation, what is the primary ventilation complication?",
    "Bulla expansion and rupture causing tension pneumothorax or bronchopleural fistula; bullae have poorly communicating airways and expand under positive pressure relative to normal lung.",
    "Positive pressure preferentially distends bullae because they lack normal elastic recoil and communicating airways that allow equilibration.",
    "apply","Miller/Baby Miller",505,"")

# ── 3: Pediatric ENT and airway anesthesia ─────────────────────────────────────
t = sl[3]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-ent-anes'
add(slug,tp,dm,dc,
    "Why is even brief laryngospasm especially dangerous in small children during ENT surgery?",
    "Children have small FRC relative to their high O2 consumption; laryngospasm rapidly depletes O2 stores, causing critical hypoxemia within seconds.",
    "The high metabolic rate of infants combined with low FRC means apnea or obstruction causes SpO2 desaturation far faster than in adults.",
    "apply","Miller/Baby Miller",577,"Adult laryngospasm")
add(slug,tp,dm,dc,
    "After adenotonsillectomy, what early signs suggest occult postoperative hemorrhage before visible bleeding is apparent?",
    "Tachycardia, repeated swallowing, and PONV — blood is swallowed, underestimating blood loss; IV rehydration before re-operation is critical.",
    "Swallowed blood is a potent emetic and masks external hemorrhage; the first signs are hemodynamic and gastrointestinal, not visible bleeding.",
    "apply","Miller/Baby Miller",579,"PONV from anesthesia")
add(slug,tp,dm,dc,
    "In an emergency cannot-intubate-cannot-oxygenate situation requiring a surgical airway, what three preparatory steps improve success?",
    "Identify an assistant, place a shoulder roll to expose the trachea, direct a light source at the neck — always invest 20 seconds. Surgical techniques have far higher success than cannula-based.",
    "Proper positioning and lighting are prerequisites for surgical cricothyrotomy; percutaneous approaches have high failure rates in emergencies.",
    "apply","Stanford CA-1",45,"Cannula (percutaneous) cricothyrotomy")
add(slug,tp,dm,dc,
    "During nasal fiberoptic intubation in infants, how can oxygenation be maintained?",
    "Nasal cannula O2 in infants and children can maintain oxygenation during fiberoptic intubation by providing apneic oxygenation through the nasal airway.",
    "Infants have sufficient nasal and upper airway patency to receive passive O2 flow during instrumentation, extending the safe apnea time.",
    "apply","Miller/Baby Miller",308,"")
add(slug,tp,dm,dc,
    "Which inhalation agent is preferred for pediatric ENT induction and which should be avoided?",
    "Sevoflurane is preferred; desflurane and isoflurane are avoided because they are pungent and cause coughing, breath-holding, and laryngospasm during inhalation induction.",
    "Airway irritants are especially hazardous in pediatric ENT patients whose airways are already reactive or instrumented.",
    "recall","Morgan & Mikhail",1466,"")

# ── 4: Pediatric airway anatomy and management ─────────────────────────────────
t = sl[4]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-airway-anatomy'
add(slug,tp,dm,dc,
    "There is no validated airway assessment in children analogous to the Mallampati score. What anatomic findings should the pediatric airway exam focus on instead?",
    "Inspect for micrognathia, midface hypoplasia, macroglossia, limited mouth opening, and neck mobility; history of prior difficult airway is most predictive.",
    "Children are uncooperative with formal scoring; anatomic clues and prior anesthetic history are the practical basis for pediatric difficult-airway prediction.",
    "recall","Miller/Baby Miller",644,"Mallampati in adults")
add(slug,tp,dm,dc,
    "What is the classic anatomic difference between infant and adult airways that affects laryngoscopy and tube passage?",
    "Infants have a relatively anterior and cephalad larynx, larger occiput (causing neck flexion when supine), shorter trachea, and a larger, omega-shaped epiglottis — requiring a straight (Miller) blade and neutral or slight extension.",
    "These anatomic differences shift the laryngeal axis and require different blade selection and head positioning compared to adults.",
    "recall","Miller/Baby Miller",277,"Adult laryngoscopy technique")
add(slug,tp,dm,dc,
    "For awake fiberoptic intubation when mask ventilation may be impossible, what ventilation principle must be preserved?",
    "Spontaneous ventilation must be maintained; losing spontaneous breathing before securing the airway in a cannot-ventilate patient removes the last safety margin.",
    "Apnea in a cannot-ventilate patient leads rapidly to hypoxic arrest; topicalization and judicious sedation preserve respiratory drive during fiberoptic intubation.",
    "analyze","Miller/Baby Miller",308,"RSI in difficult airway")
add(slug,tp,dm,dc,
    "What do multiple predictors of difficult mask ventilation include, and why does this matter for pediatric patients?",
    "Mallampati III/IV, mandibular protrusion limitation, large neck circumference, obesity, presence of a beard, and age >57 — if 3+ present, difficult mask ventilation is likely. In children, equivalent anatomic predictors plus syndromes (Pierre Robin, Treacher Collins) matter.",
    "Recognizing difficult mask ventilation preoperatively prompts preparation of adjuncts (oral airway, two-person technique, LMA) before encountering the problem.",
    "apply","Stanford CA-1",43,"")
add(slug,tp,dm,dc,
    "In a child with aspiration risk requiring intubation, which technique reduces aspiration while securing the airway?",
    "RSI with cricoid pressure (modified Sellick) and awake upright intubation are options; NGT to suction should be left in place; metoclopramide and H2-blockers reduce risk in high-risk patients.",
    "Full-stomach precautions in children require the same principles as adults: minimize time between loss of protective reflexes and cuff inflation.",
    "apply","Stanford CA-1",74,"")

# ── 5: Pediatric airway foreign body ──────────────────────────────────────────
t = sl[5]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-fb-airway'
add(slug,tp,dm,dc,
    "Tracheal aspiration of a foreign body in a child is described as what type of clinical emergency?",
    "An emergency — especially in the pediatric population; airway foreign bodies can cause complete obstruction, hypoxia, and death rapidly.",
    "Children's small airway diameter means even partial foreign body impaction can cause critical airflow reduction.",
    "recall","Miller/Baby Miller",579,"")
add(slug,tp,dm,dc,
    "For an asthmatic child with poorly controlled asthma requiring surgery, what is the preferred management strategy?",
    "Delay surgery to optimize asthma control; propofol is a suitable induction agent that avoids airway irritation from volatile agents; ketamine is suitable in hemodynamically unstable pediatric patients.",
    "Airway hyperreactivity in asthma increases the risk of bronchospasm at intubation; pretreatment with systemic steroids 5 days preoperatively markedly decreases bronchospasm incidence.",
    "apply","StatPearls: StatPearls   Asthma  Chronic Management",6,"")
add(slug,tp,dm,dc,
    "In patients with laryngeal papillomas, vocal cord dysfunction, or tracheal stenosis, what must precede anesthetic planning?",
    "A thorough preoperative history and physical examination focusing on the airway — including the nature of any prior airway surgery — must precede decisions on the anesthetic plan.",
    "Airway pathology changes the approach to induction, airway management tools, and the threshold for awake versus asleep techniques.",
    "recall","Morgan & Mikhail",1270,"")
add(slug,tp,dm,dc,
    "During office-based or clinic anesthesia for pediatric oral/dental procedures, what standard must be maintained?",
    "The same standard of care as required in a hospital must be met; medications for anticipated or unexpected anesthesia-related problems must be immediately available.",
    "Off-site locations carry the same patient risk as the OR; rescue drugs, equipment, and personnel must match in-hospital capability.",
    "recall","Morgan & Mikhail",1288,"")
add(slug,tp,dm,dc,
    "Oxygen hoods are used in which specific pediatric population and for what reason?",
    "Infants and neonates who will not tolerate facial appliances — the hood covers only the head, allowing body access while delivering supplemental O2.",
    "Neonates are obligate nasal breathers and frequently desaturate with face masks or cannulas they resist; hoods provide O2 delivery with less stimulation.",
    "recall","Morgan & Mikhail",2174,"Nasal cannula in neonates")

# ── 6: Pediatric cardiac arrest and resuscitation ──────────────────────────────
t = sl[6]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-cardiac-arrest'
add(slug,tp,dm,dc,
    "CPR was initially defined as what intervention, and what two landmark advances defined modern resuscitation?",
    "Mouth-to-mouth ventilation plus closed-chest cardiac compressions. Modern ACLS integrates electrical defibrillation and pharmacologic support (epinephrine, amiodarone/lidocaine).",
    "The foundational CPR framework has remained stable but pharmacology and rhythm management have evolved substantially over 50+ years.",
    "recall","Miller/Baby Miller",834,"")
add(slug,tp,dm,dc,
    "In a pulseless patient, what PETCO2 value after 20 minutes of CPR indicates poor likelihood of ROSC in an intubated patient?",
    "PETCO2 persistently less than 10 mmHg after 20 minutes of CPR in an intubated patient is associated with reduced likelihood of ROSC; can be used to guide resuscitation decisions.",
    "PETCO2 reflects pulmonary blood flow and thus cardiac output during CPR; low PETCO2 indicates inadequate circulation and predicts failure of resuscitation.",
    "apply","Morgan & Mikhail",2057,"PETCO2 in non-intubated patients")
add(slug,tp,dm,dc,
    "What does a PETCO2 greater than 10 mmHg during CPR indicate, and how is it used to guide compressions?",
    "PETCO2 >10 mmHg is a marker of adequate CPR quality; data from AHA registries show higher ROSC likelihood when CPR quality is monitored using PETCO2 or diastolic blood pressure.",
    "Real-time PETCO2 monitoring during CPR provides immediate feedback on compression depth and rate, allowing real-time quality improvement.",
    "apply","Miller/Baby Miller",838,"")
add(slug,tp,dm,dc,
    "Intraosseous access in pediatric resuscitation uses what anatomic principle, and where is the needle directed?",
    "The IO needle enters the large medullary venous channels of the bone marrow; it is directed away from the epiphyseal plate to minimize growth-plate injury.",
    "The medullary sinusoids drain into the central venous system, providing reliable vascular access with similar pharmacokinetics to IV administration.",
    "recall","Morgan & Mikhail",2073,"")
add(slug,tp,dm,dc,
    "In pediatric VF/VT arrest, which antiarrhythmic drugs have been studied, and what is the current evidence?",
    "Lidocaine shows favorable results versus placebo for OHCA; amiodarone did not show benefit versus placebo; vasopressin was removed from 2015 ACLS guidelines due to lack of benefit.",
    "Despite widespread historical use of amiodarone, controlled data in pediatric and adult OHCA do not demonstrate superiority over lidocaine.",
    "recall","Miller/Baby Miller",844,"Amiodarone superiority assumption")

# ── 7: Pediatric cardiac surgery anesthesia ────────────────────────────────────
t = sl[7]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-cardiac-surg-anes'
add(slug,tp,dm,dc,
    "In neonates and young infants undergoing regional anesthesia, which local anesthetic is preferred for continuous epidural infusion and why?",
    "Chloroprocaine — due to its rapid plasma clearance it is uniquely safe for continuous epidural infusion in neonates and repeat loading doses, minimizing systemic accumulation.",
    "Neonates have immature hepatic metabolism and reduced plasma cholinesterase activity; chloroprocaine is hydrolyzed by plasma esterases so accumulation risk is low.",
    "recall","Miller/Baby Miller",178,"Bupivacaine in neonates")
add(slug,tp,dm,dc,
    "For pediatric non-painful diagnostic studies such as MRI, which IV agent is increasingly preferred and why?",
    "Dexmedetomidine — provides sedation without respiratory depression, making it especially useful for procedures lasting more than one hour where airway protection without intubation is desired.",
    "Dexmedetomidine produces sedation via alpha-2 agonism with preserved respiratory drive, allowing MRI completion without endotracheal intubation.",
    "recall","Miller/Baby Miller",663,"Propofol for MRI sedation")
add(slug,tp,dm,dc,
    "Dexmedetomidine has demonstrated what specific benefit in pediatric anesthesia beyond sedation?",
    "Prevention of emergence delirium after pediatric anesthesia — dexmedetomidine reduces the incidence of emergence agitation following volatile agent-based anesthesia.",
    "Alpha-2 agonism smooths emergence by reducing catecholamine surge and providing residual sedation during the disorienting emergence phase.",
    "recall","Miller/Baby Miller",147,"")
add(slug,tp,dm,dc,
    "During NORA (non-operating room anesthesia) procedures, what standards must be maintained?",
    "The same monitoring, equipment, and personnel standards as in the OR must be present; requests for NORA services have been steadily increasing as procedural medicine expands.",
    "Remote locations pose the same physiologic risks as the OR with less backup; ASA standards for monitoring and rescue must not be compromised.",
    "recall","Morgan & Mikhail",1530,"")
add(slug,tp,dm,dc,
    "In pediatric perioperative cardiac arrest, what proportion of arrests were contributed to by anesthetic care in the POCA Registry?",
    "In the POCA Registry (193 arrests, 1998–2004, ~80 North American institutions), anesthetic care was judged to have contributed to 150 of 289 analyzed cardiac arrest cases.",
    "The high anesthetic contribution rate emphasizes that pediatric perioperative arrests are often preventable through careful preparation and vigilance.",
    "recall","Morgan & Mikhail",2022,"")

# ── 8: Pediatric emergence and recovery ───────────────────────────────────────
t = sl[8]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-emergence-recovery'
add(slug,tp,dm,dc,
    "What are the two most common postanesthetic complications uniquely vulnerable in pediatric patients?",
    "Laryngospasm and postintubation croup — both are far more common than in adults and can be life-threatening in small children.",
    "Pediatric airways are smaller, more reactive, and have less physiologic reserve than adults, making airway complications after extubation more dangerous.",
    "recall","Morgan & Mikhail",1474,"")
add(slug,tp,dm,dc,
    "Laryngospasm is most common in which pediatric age group, and what is the approximate incidence?",
    "Infants 1–3 months old have the highest risk; overall incidence of laryngospasm in young pediatric patients is approximately 1 in 50 anesthetics.",
    "The immature laryngeal protective reflex and small airway diameter make infants most vulnerable to trigger-induced laryngospasm.",
    "recall","Morgan & Mikhail",1474,"")
add(slug,tp,dm,dc,
    "In what position should a somnolent pediatric patient recovering from anesthesia be placed to reduce airway risk?",
    "Lateral (recovery) position — oral secretions pool and drain away from the vocal cords, reducing the risk of laryngospasm from secretion irritation.",
    "In a supine, somnolent child, secretions pool at the vocal cords and trigger laryngospasm; the lateral position uses gravity to protect the airway.",
    "apply","Morgan & Mikhail",1474,"")
add(slug,tp,dm,dc,
    "What are the four risk factors that predict PONV in children?",
    "Age 3 years or older, strabismus surgery, duration of surgery longer than 30 minutes, and previous history of postoperative vomiting or motion sickness.",
    "These pediatric PONV predictors differ from the adult Apfel score; PONV is ranked by parents as the most unwanted postanesthetic side effect.",
    "recall","Miller/Baby Miller",649,"Adult Apfel PONV score")
add(slug,tp,dm,dc,
    "What is the key advantage of deep extubation vs. awake extubation in pediatric patients?",
    "Deep extubation avoids the period of light anesthesia during which airway reflexes are most reactive and laryngospasm risk is highest; the patient emerges without an ETT.",
    "Laryngospasm risk peaks during light anesthesia at extubation; removing the tube under deep anesthesia eliminates this vulnerable window, though at the cost of lost protective reflexes.",
    "analyze","Miller/Baby Miller",648,"Awake extubation advantages")

# ── 9: Pediatric induction techniques ─────────────────────────────────────────
t = sl[9]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-induction'
add(slug,tp,dm,dc,
    "Why do infants have a faster speed of inhalation induction than older children and adults?",
    "Greater minute ventilation-to-FRC ratio in infants causes rapid rise in alveolar anesthetic concentration; combined with relatively greater cerebral blood flow, brain uptake of anesthetic is accelerated.",
    "The high minute ventilation/FRC ratio accelerates alveolar equilibration; high cerebral blood flow then rapidly delivers anesthetic to the CNS.",
    "apply","Morgan & Mikhail",1443,"")
add(slug,tp,dm,dc,
    "Infants accounted for what proportion of anesthesia-related arrests in children, and what is the most common precipitating airway event?",
    "Infants accounted for 55% of all anesthesia-related arrests in children; laryngospasm during induction (most common equipment-related arrest association) is the leading airway precipitant.",
    "The infant's reactive airway and reduced reserve make induction the highest-risk period; laryngospasm in this age group can progress to cardiac arrest within seconds.",
    "recall","Morgan & Mikhail",1460,"")
add(slug,tp,dm,dc,
    "For a child with a penetrating eye injury, full stomach, and no IV access, what induction dilemma exists?",
    "The need for RSI to prevent aspiration conflicts with the risk of succinylcholine-induced IOP rise (which could extrude vitreous); no perfect solution exists. Rocuronium (1.2 mg/kg) plus sugammadex availability is a reasonable approach.",
    "Succinylcholine transiently raises IOP by 6–8 mmHg via extraocular muscle fasciculation, a risk with open globe; but aspiration risk from full stomach demands rapid sequence.",
    "analyze","Morgan & Mikhail",1266,"")
add(slug,tp,dm,dc,
    "Parental presence during induction (PPIA) — what does a Cochrane review conclude about its utility?",
    "PPIA is not clearly useful for all children; parental temperament and the child's temperament both matter; physiologic responses (parental syncope) can occur and must be considered.",
    "Parental anxiety transmits to the child; only calm, prepared parents add benefit — selecting appropriate families is more important than universal PPIA.",
    "apply","Miller/Baby Miller",647,"")
add(slug,tp,dm,dc,
    "What pharmacokinetic principle explains why single-dose thiopental or propofol causes awakening in infants despite short elimination half-lives?",
    "Awakening after a single bolus of thiopental or propofol depends on redistribution from the brain to vessel-rich and then muscle/fat tissues, not elimination; the same redistribution principle applies in infants.",
    "First-dose awakening is a redistribution phenomenon; repeated dosing saturates peripheral compartments and prolongs effect — context-sensitive.",
    "apply","Miller/Baby Miller",641,"")

# ── 10: Pediatric liver transplantation anesthesia ────────────────────────────
t = sl[10]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-liver-txp-anes'
add(slug,tp,dm,dc,
    "What is the reported 1-year survival rate in selected pediatric liver transplant centers?",
    "Selected pediatric centers report 1-year survival rates of 90% for pediatric liver transplantation.",
    "Pediatric liver transplantation outcomes are excellent in experienced centers, reflecting advances in surgical technique, immunosuppression, and perioperative anesthetic management.",
    "recall","Morgan & Mikhail",1208,"")
add(slug,tp,dm,dc,
    "What are the ICP and CPP targets during liver transplantation in a patient with acute liver failure and elevated ICP?",
    "ICP <20 mmHg, CPP >50 mmHg, MAP >60 mmHg; head of bed elevated 20–25 degrees, controlled airway, propofol sedation, vasopressor support as needed.",
    "Acute liver failure causes cerebral edema and ICP elevation; maintaining CPP prevents secondary ischemic injury during the transplant procedure.",
    "apply","Morgan & Mikhail",1208,"")
add(slug,tp,dm,dc,
    "The MELD score guides liver transplant listing at what threshold, and what complications trigger listing regardless of MELD?",
    "MELD >= 15 or complications of cirrhosis (ascites, hepatic encephalopathy, esophageal variceal bleeding, hepatorenal syndrome, chronic gastropathy bleeding) — Child B cirrhosis with portal hypertension also qualifies.",
    "The MELD score quantifies 90-day mortality risk from liver disease; complications signal decompensation that warrants transplant evaluation independent of MELD score.",
    "recall","MGH Housestaff Manual",98,"MELD score for hepatocellular carcinoma")
add(slug,tp,dm,dc,
    "In the prehepatic phase of liver transplantation, what are the three primary phases of the operation?",
    "Prehepatic phase (dissection, venous bypass if needed), anhepatic phase (native liver removed, graft implanted), and neohepatic phase (reperfusion, graft begins functioning); each phase has distinct anesthetic challenges.",
    "The neohepatic/reperfusion phase carries the highest risk of hemodynamic instability, electrolyte disturbance (hyperkalemia from preservation solution), and coagulopathy.",
    "recall","Morgan & Mikhail",2295,"")
add(slug,tp,dm,dc,
    "What hepatic condition is the most common cause of liver transplant referral in children with cirrhosis?",
    "End-stage liver disease with MELD >=15 or complications; in children, biliary atresia is the most common underlying condition; hepatocellular carcinoma risk is 2–4% per year in cirrhotic patients.",
    "Biliary atresia leads to progressive biliary cirrhosis in children; liver transplantation is the definitive treatment when Kasai procedure fails.",
    "recall","MGH Housestaff Manual",96,"")

# ── 11: Pediatric neurosurgery anesthesia ─────────────────────────────────────
t = sl[11]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-neurosurg-anes'
add(slug,tp,dm,dc,
    "Dexmedetomidine is preferred over propofol for pediatric non-painful procedures >1 hour in NORA settings for what reason?",
    "Dexmedetomidine causes less respiratory depression than propofol or opioids, maintaining spontaneous ventilation — critical when airway access is limited (e.g., MRI bore).",
    "Alpha-2 agonism produces sedation through endogenous sleep pathways without significant respiratory depression, unlike GABA-ergic agents.",
    "recall","Miller/Baby Miller",707,"Propofol for MRI sedation")
add(slug,tp,dm,dc,
    "Dexmedetomidine's benefit for emergence delirium in pediatric anesthesia operates via what mechanism?",
    "It prevents emergence delirium after volatile anesthesia by blunting the catecholamine surge of emergence through alpha-2-mediated CNS sympatholysis.",
    "Emergence delirium in children peaks during the transition from surgical anesthesia to wakefulness; dexmedetomidine smooths this transition.",
    "apply","Miller/Baby Miller",147,"")
add(slug,tp,dm,dc,
    "For asthmatic children, what preoperative steroid regimen demonstrably reduces intraoperative bronchospasm at intubation?",
    "Systemic corticosteroids plus inhaled beta-2 agonists administered for 5 days before surgery markedly decreases bronchospasm following intubation; a single preoperative dose of systemic steroids shows little benefit.",
    "Multi-day steroid pretreatment suppresses airway eosinophilic inflammation; single doses do not provide sufficient anti-inflammatory preparation.",
    "apply","StatPearls: StatPearls   Asthma  Chronic Management",4,"")
add(slug,tp,dm,dc,
    "Barbiturate effects on the CNS are relevant to pediatric neurosurgery for what purpose?",
    "Barbiturates decrease cerebral metabolism and ICP (reduce CMRO2 and cerebral blood flow); they provide cerebral protection but cause cardiovascular depression.",
    "Burst suppression with barbiturates reduces cerebral metabolic demand during ischemic events; the trade-off is cardiovascular compromise requiring vasopressor support.",
    "apply","Miller/Baby Miller",916,"")
add(slug,tp,dm,dc,
    "Bacterial meningitis in neonates — what organisms predominate in nosocomial versus community-acquired cases?",
    "Nosocomial: S. pneumoniae, S. aureus, S. albus, gram-negative bacilli. Community-acquired: S. pneumoniae predominates (out of 1670 US cases 2003–2007); H. influenzae in non-vaccinated children.",
    "Empirical antibiotic selection for neonatal meningitis must cover both gram-positive and gram-negative organisms given the diversity of pathogens.",
    "recall","StatPearls",2,"")

# ── 12: Pediatric oncology anesthesia ─────────────────────────────────────────
t = sl[12]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-oncology-anes'
add(slug,tp,dm,dc,
    "What are the three key admission history items when evaluating a pediatric patient with newly diagnosed acute leukemia?",
    "Sibling status (for donor search), family history (for inherited syndromes), and menstrual history in pre/perimenopausal females (date of LMP — chemotherapy is teratogenic).",
    "Leukemia workup must simultaneously address treatment eligibility, donor availability, and reproductive implications of chemotherapy.",
    "recall","MGH Housestaff Manual",148,"")
add(slug,tp,dm,dc,
    "In AYA (adolescent and young adult, age 15–39) ALL, which treatment approach is preferred and why?",
    "Pediatric-inspired regimens (often incorporating asparaginase) are used for AYA ALL because they produce superior outcomes compared to adult ALL regimens in this age group.",
    "AYA ALL behaves biologically more like pediatric ALL; clinical trials showed pediatric protocols achieve higher CR and OS rates in AYA patients.",
    "recall","MGH Housestaff Manual",148,"")
add(slug,tp,dm,dc,
    "Tumor lysis syndrome can occur in what patient population, and what triggers it?",
    "Both adult and pediatric oncology patients undergoing chemotherapy — especially high-burden hematologic malignancies; massive cell death releases intracellular contents (K+, phosphate, uric acid, LDH).",
    "Rapid cytolysis overwhelms renal clearance capacity; resulting hyperkalemia, hyperphosphatemia, hypocalcemia, and uric acid nephropathy can be life-threatening.",
    "recall","StatPearls: StatPearls   Oncologic emergencies  tumor lysis syndrome",2,"")
add(slug,tp,dm,dc,
    "Allogeneic vs. autologous stem cell transplant — what is the fundamental therapeutic difference?",
    "Allogeneic: non-self donor cells reconstitute hematopoiesis AND provide graft-versus-tumor effect; autologous: patient's own cells reconstitute after high-dose conditioning without graft-versus-tumor benefit.",
    "The graft-versus-tumor effect of allogeneic transplant provides immunologic anti-cancer activity absent in autologous transplant, but at the cost of GVHD risk.",
    "recall","MGH Housestaff Manual",153,"")
add(slug,tp,dm,dc,
    "In neutropenic patients with severe sepsis or septic shock, what does data show about survival?",
    "Neutropenic patients with severe sepsis/septic shock have high mortality; early aggressive treatment with broad-spectrum antibiotics is critical — survival data shows early antibiotic administration improves outcomes.",
    "Neutropenia eliminates the normal cellular immune response; even opportunistic organisms cause rapidly fatal sepsis requiring immediate empirical broad-spectrum coverage.",
    "recall","Society Guideline: Guideline   IDSA 2014 SSTI",42,"")

# ── 13: Pediatric ophthalmic anesthesia ───────────────────────────────────────
t = sl[13]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-ophthalmic-anes'
add(slug,tp,dm,dc,
    "Topically applied phenylephrine eye drops in pediatric and geriatric patients should be limited to what concentration and why?",
    "At most 2.5% phenylephrine solution (not 10%); one drop of 10% contains ~5 mg — absorbed via conjunctival and nasolacrimal mucosa causing hypertension, tachycardia, and arrhythmias.",
    "Pediatric and geriatric patients are most vulnerable to systemic toxicity from topical eye drops due to higher relative drug exposure per body weight and altered physiology.",
    "apply","Morgan & Mikhail",1253,"")
add(slug,tp,dm,dc,
    "Epinephrine eye drops cause what systemic cardiovascular effects, and which volatile agent potentiates the arrhythmogenic risk?",
    "Hypertension, tachycardia, and ventricular arrhythmias; arrhythmogenic effects are potentiated by halothane (sensitizes myocardium to catecholamines).",
    "Halothane increases myocardial sensitivity to catecholamines; even small absorbed doses of topical epinephrine can precipitate VF under halothane anesthesia.",
    "apply","Morgan & Mikhail",1254,"Sevoflurane arrhythmia risk")
add(slug,tp,dm,dc,
    "What unique temperature management challenge occurs during pediatric ophthalmic surgery?",
    "Infant body temperature may RISE during ophthalmic surgery due to head-to-toe draping and minimal body surface exposure — monitor for hyperthermia, not just hypothermia.",
    "Unlike most pediatric surgeries where hypothermia dominates, the complete draping of ophthalmic procedures traps heat; active warming should be reduced or discontinued.",
    "apply","Morgan & Mikhail",1255,"")
add(slug,tp,dm,dc,
    "An open-globe injury patient requires rapid-sequence induction. What is the dilemma with succinylcholine?",
    "Succinylcholine transiently raises IOP by ~6–8 mmHg via extraocular muscle fasciculation; in open globe, this risks vitreous extrusion — yet RSI may be needed for full stomach. Rocuronium 1.2 mg/kg with sugammadex availability is an alternative.",
    "The conflict between aspiration risk (favoring RSI) and IOP elevation (opposing succinylcholine) requires weighing relative risks; high-dose rocuronium provides similar rapid onset.",
    "analyze","Morgan & Mikhail",1255,"")
add(slug,tp,dm,dc,
    "Insufflation of anesthetic gas across a child's face is categorized as what type of breathing system and why is it used?",
    "A breathing system (technique) that avoids direct circuit connection to the airway; used in children who resist face mask placement, providing partial anesthetic effect while allowing spontaneous ventilation.",
    "Insufflation delivers volatile agent vapors near the airway without requiring mask seal, useful for inhalation induction in uncooperative or pre-induction anxious children.",
    "recall","Morgan & Mikhail",68,"")

# ── 14: Pediatric orthopedic surgery ──────────────────────────────────────────
t = sl[14]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-ortho-surg'
add(slug,tp,dm,dc,
    "Major orthopedic surgery is classified as what level of bleeding risk in the perioperative period?",
    "High bleeding risk (30-day risk of major bleed >2%); this includes shoulder arthroplasty and other major orthopedic surgery.",
    "High-risk bleeding classification guides anticoagulation decisions and the timing of regional anesthesia in anticoagulated patients.",
    "recall","Miller/Baby Miller",228,"")
add(slug,tp,dm,dc,
    "Neuraxial anesthesia is contraindicated in what four major conditions?",
    "Lack of consent, coagulation abnormalities, severe hypovolemia, elevated ICP, and infection at the injection site. For epidural: sudden loss of resistance to injection confirms correct placement.",
    "These contraindications reflect the risk of hematoma (coagulopathy), cardiovascular collapse (hypovolemia), herniation (elevated ICP), and epidural abscess (infection).",
    "recall","Morgan & Mikhail",1541,"")
add(slug,tp,dm,dc,
    "What is the Gupta (MICA) cardiac risk model, and what five factors does it use?",
    "The Gupta MICA model predicts risk of STEMI or cardiac arrest within 30 days of surgery using: type of surgery, preoperative functional status, ASA class, creatinine, and dependent functional status.",
    "MICA was derived from the NSQIP database and outperforms the Lee RCRI for some procedure types, particularly inpatient surgeries.",
    "recall","MGH Housestaff Manual",237,"Lee RCRI")
add(slug,tp,dm,dc,
    "When should perioperative antibiotic prophylaxis be administered relative to incision, and what does it prevent?",
    "Within 60 minutes before incision (within 30 minutes for fluoroquinolones/vancomycin); prevents surgical site infection (SSI), the most common adverse surgical event in a landmark 1984 New York State study.",
    "Prophylactic antibiotics must achieve tissue levels at the time of bacterial inoculation (incision); administration too early or after incision significantly reduces efficacy.",
    "apply","Stanford CA-1",91,"")
add(slug,tp,dm,dc,
    "For postoperative pain after orthopedic procedures, what analgesic modality may prevent development of chronic post-surgical pain (CPSP)?",
    "Intraarticular opioid injection may provide analgesia for up to 24 hours and prevent CPSP development; peripheral opioid receptors on primary afferents mediate this effect.",
    "Chronic post-surgical pain develops via central sensitization; adequate early postoperative analgesia may prevent the neural sensitization that underlies CPSP.",
    "apply","Miller/Baby Miller",752,"")

# ── 15: Pediatric pain management ─────────────────────────────────────────────
t = sl[15]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-pain-mgmt'
add(slug,tp,dm,dc,
    "What pharmacologic property makes propofol potentially beneficial in oncologic surgery beyond its anesthetic effect?",
    "Preclinical studies show propofol has beneficial immune, anti-inflammatory, and antitumor properties compared to volatile anesthetics; retrospective data suggest TIVA may be associated with better long-term cancer outcomes.",
    "Propofol may preserve NK cell function and reduce immunosuppression compared to volatile agents, potentially reducing tumor dissemination — though prospective confirmation is lacking.",
    "analyze","Miller/Baby Miller",137,"")
add(slug,tp,dm,dc,
    "Intraarticular opioid injection postoperatively provides analgesia via what receptor mechanism?",
    "Peripheral opioid receptors on primary afferent nerve terminals; these receptors are upregulated by tissue inflammation and mediate analgesia for up to 24 hours.",
    "The peripheral opioid system can be targeted intraoperatively to provide prolonged local analgesia without central side effects.",
    "recall","Miller/Baby Miller",752,"")
add(slug,tp,dm,dc,
    "Extubation during deep anesthesia in pediatric patients — what is the primary advantage over awake extubation?",
    "Avoids the reactive period of light anesthesia when airway reflexes are at their most irritable and laryngospasm risk is highest; the child emerges without the endotracheal tube in place.",
    "The transition from surgical anesthesia to wakefulness is the most hazardous period for laryngospasm; deep extubation bypasses this window.",
    "apply","Miller/Baby Miller",648,"")
add(slug,tp,dm,dc,
    "Which finding is NOT consistent with malignant hyperthermia: PaCO2 150, MVO2 50, pH 6.9, or late onset 1 hour post-op?",
    "MVO2 of 50 is NOT consistent with MH — MH is a hypermetabolic state causing increased O2 consumption, so MVO2 should be very LOW (tissues extract more O2). PaCO2 150 (hypercarbia), pH 6.9 (acidosis), and late onset are all consistent.",
    "MH is driven by uncontrolled muscle metabolism; all tissues consume O2 voraciously, lowering mixed venous saturation. High MVO2 would indicate low metabolic demand.",
    "apply","Stanford CA-1",86,"NMS vs MH")

# ── 16: Pediatric pharmacology ────────────────────────────────────────────────
t = sl[16]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-pharmacology'
add(slug,tp,dm,dc,
    "How does MAC change across the lifespan from neonates to elderly adults?",
    "MAC is highest in infants (~0.5–1 year), decreases with age through childhood, and the principal pharmacodynamic change in the elderly is reduced anesthetic requirement (reduced MAC); older adults require less propofol and etomidate as well.",
    "Age-related CNS changes (receptor density, lipid composition, neuronal plasticity) reduce anesthetic requirements; MAC decreases ~6% per decade after age 40.",
    "recall","Morgan & Mikhail",1490,"")
add(slug,tp,dm,dc,
    "MAC-awake and MAC-amnesia differ from MAC-immobility — how do they compare?",
    "MAC-awake (~0.33 MAC) is lower than MAC immobility; MAC-amnesia is even lower, likely less than MAC-awake. MAC-immobility reflects spinal cord suppression (not cortical), so it is higher relative to the other endpoints.",
    "Anesthetic endpoints are pharmacologically dissociable: consciousness is suppressed at lower concentrations than movement; amnesia at even lower concentrations.",
    "recall","Miller/Baby Miller",114,"")
add(slug,tp,dm,dc,
    "Combination of opioids and benzodiazepines causes what hemodynamic effect, and why is this combination especially dangerous?",
    "Marked reduction in arterial blood pressure and peripheral vascular resistance (synergistic effect); this synergistic interaction is frequently observed in patients who are receiving IV opioid and benzodiazepine together.",
    "Each agent independently reduces SVR or cardiac output; combined they produce supra-additive cardiovascular depression, risking cardiac arrest in compromised patients.",
    "apply","Morgan & Mikhail",284,"")
add(slug,tp,dm,dc,
    "Why does cimetidine reduce hepatic metabolism of other drugs, and what clinical drug interaction results?",
    "Cimetidine reduces hepatic blood flow and inhibits CYP450 enzymes; drugs with high hepatic extraction ratios (e.g., lidocaine, propranolol) accumulate and their effects are prolonged.",
    "High-extraction drugs depend on hepatic blood flow for clearance; cimetidine's dual action (flow reduction + enzyme inhibition) substantially prolongs their effect.",
    "apply","Morgan & Mikhail",352,"Ranitidine effects")
add(slug,tp,dm,dc,
    "What hepatic metabolic changes occur in neonates and young infants that affect drug clearance?",
    "Hepatic metabolism is immature in neonates; the activity of metabolic enzymes (CYP450 isoforms, glucuronyl transferases) is reduced, converting lipid-soluble drugs to inactive water-soluble forms more slowly — prolonging drug effect.",
    "Neonatal hepatic CYP3A4, CYP2D6, and conjugation enzymes mature gradually over months; doses must be adjusted and intervals extended to prevent accumulation.",
    "apply","Miller/Baby Miller",641,"")

# ── 17: Pediatric regional anesthesia ─────────────────────────────────────────
t = sl[17]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-regional-anes'
add(slug,tp,dm,dc,
    "Pediatric caudal blocks are most commonly performed at what point in the anesthetic and what procedures do they cover?",
    "After induction of general anesthesia; caudal blocks cover procedures below the diaphragm — urogenital, rectal, inguinal, and lower extremity surgery.",
    "Performing caudal blocks under general anesthesia in children is safe and avoids the distress of awake needle placement; the caudal space is easily accessed before ossification of the sacral hiatus.",
    "recall","Morgan & Mikhail",1592,"")
add(slug,tp,dm,dc,
    "Ultrasound guidance has changed pediatric femoral, adductor canal, and sciatic blocks how?",
    "Single-shot and continuous femoral, adductor canal, and sciatic blocks can be performed in children using ultrasound guidance; interscalene blocks in anesthetized adults carry a rare risk of accidental intramedullary injection.",
    "Ultrasound guidance allows real-time needle tip and local anesthetic spread visualization, reducing risk of nerve injury and intravascular injection in small pediatric patients.",
    "apply","Morgan & Mikhail",1473,"")
add(slug,tp,dm,dc,
    "For a child presenting for emergency cesarean section (maternal cardiac arrest), when must perimortem cesarean delivery be performed?",
    "The fetus should be emergently delivered if the mother is not resuscitated within 5 minutes of cardiac arrest; this guideline improves survival for both mother and neonate.",
    "Aortocaval compression by the gravid uterus prevents effective CPR; delivery relieves compression and improves maternal ROSC while giving the fetus a chance.",
    "recall","Miller/Baby Miller",615,"")
add(slug,tp,dm,dc,
    "Neuraxial blockade established BEFORE incision and continued postoperatively provides what advantage over systemic analgesia alone?",
    "Neuraxial blockade established pre-incision blunts the metabolic and neuroendocrine stress response to surgery more effectively than systemic analgesia; lidocaine infusion additionally has antihyperalgesic and anti-inflammatory properties.",
    "Blocking afferent nociceptive input before the surgical stimulus prevents central sensitization ('wind-up'); post-incision blockade cannot fully reverse established sensitization.",
    "apply","Stanford CA-1",99,"")

# ── 18: Pediatric respiratory physiology ──────────────────────────────────────
t = sl[18]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-resp-physiology'
add(slug,tp,dm,dc,
    "What does end-tidal CO2 monitoring confirm, and when is it mandatorily required?",
    "ETCO2 confirms adequate ventilation; it is mandatory during ALL anesthetic procedures. Increases in alveolar dead space decrease ETCO2 — a decrease may signal PE, hypoventilation, or circuit disconnection.",
    "Capnography is the most sensitive monitor for esophageal intubation, circuit disconnect, pulmonary embolism, and malignant hyperthermia — all of which alter CO2 elimination.",
    "recall","Morgan & Mikhail",194,"")
add(slug,tp,dm,dc,
    "Inspiratory pressures above what threshold during positive-pressure ventilation increase the risk of pulmonary barotrauma?",
    "Sustained inspiratory pressures >30 mmHg (cmH2O equivalent) increase the risk of pulmonary barotrauma (pneumothorax) and hemodynamic compromise.",
    "High peak pressures overdistend alveoli, risking rupture; hemodynamic compromise occurs via impaired venous return and direct cardiac compression.",
    "recall","Morgan & Mikhail",124,"")
add(slug,tp,dm,dc,
    "Heat and moisture exchangers (HME) — how do passive humidifiers work and what do they prevent?",
    "HME devices contain hygroscopic material that traps exhaled humidification and heat, returning them on the next inhalation. They minimize water and heat loss without adding external heat.",
    "Without humidification, dry inspired gas desiccates airway mucosa, impairs mucociliary clearance, and promotes inspissation of secretions — HME passively mitigates this.",
    "recall","Morgan & Mikhail",111,"Active heated humidifier")
add(slug,tp,dm,dc,
    "What hazards are associated with heated humidifiers in breathing circuits?",
    "Thermal lung injury (temperature must not exceed 41°C), nosocomial infection risk, increased airway resistance from excess water condensation, and interference with flow sensors.",
    "Heated humidifiers deliver more water vapor than passive HMEs; overheating scalds mucosa, and condensate accumulation in circuits alters flow dynamics.",
    "apply","Morgan & Mikhail",113,"")
add(slug,tp,dm,dc,
    "The Rendell-Baker-Soucek pediatric face mask differs from adult masks in what key design feature?",
    "Shallow body with minimal dead space — critical for avoiding CO2 rebreathing in small children with small tidal volumes where mask dead space would constitute a large fraction of each breath.",
    "Dead space in a mask is fixed volume; in small children with 15–20 mL tidal volumes, even 10 mL of dead space causes significant CO2 rebreathing.",
    "apply","Morgan & Mikhail",504,"")

# ── 19: Pediatric sedation outside the OR ─────────────────────────────────────
t = sl[19]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-sedation-nora'
add(slug,tp,dm,dc,
    "For what types of procedures is pediatric sedation outside the OR commonly requested?",
    "Nonsurgical procedures — MRI, CT, LP, bone marrow biopsy, cardiac catheterization, and radiation therapy; requests for NORA services have been steadily increasing.",
    "Modern diagnostic and interventional medicine increasingly requires immobility and patient cooperation in locations outside the traditional OR environment.",
    "recall","Morgan & Mikhail",1473,"")
add(slug,tp,dm,dc,
    "Head-injured pediatric patients in NORA settings often require what level of anesthetic care instead of sedation?",
    "General anesthesia — head-injured and pediatric patients present special challenges and often require GA because monitoring limitations in remote locations (MRI) and disease severity argue against sedation alone.",
    "Head injury alters intracranial compliance; sedation that causes hypoventilation and CO2 retention can acutely raise ICP to dangerous levels.",
    "apply","Morgan & Mikhail",219,"")
add(slug,tp,dm,dc,
    "Dexmedetomidine is preferred for pediatric NORA procedures lasting >1 hour for what specific property?",
    "Dexmedetomidine is less likely to cause respiratory depression than opioids or benzodiazepines, allowing spontaneous ventilation without intubation during prolonged procedures.",
    "Alpha-2 agonism sedates via locus coeruleus pathways without GABA-ergic respiratory depression; this is uniquely beneficial when airway access is restricted.",
    "recall","Miller/Baby Miller",707,"Propofol infusion in NORA")
add(slug,tp,dm,dc,
    "What are the key NORA (non-operating room anesthesia) safety requirements?",
    "The same monitoring standards (capnography, pulse oximetry, NIBP, temperature), rescue equipment, and trained anesthesia personnel as the OR; the anesthesia standard of care does not change by location.",
    "Remote locations have historically been under-resourced; regulatory and professional standards now mandate full OR-equivalent capability for all NORA settings.",
    "recall","Morgan & Mikhail",1530,"")
add(slug,tp,dm,dc,
    "Hepatic drug metabolism in small infants depends on redistribution for what purpose after a single dose?",
    "Awakening after a single dose of propofol or thiopental in infants depends on redistribution from the brain to peripheral compartments, not elimination; drug effect terminates before elimination occurs.",
    "Single-dose kinetics are redistribution-dependent; context-sensitive accumulation becomes important with repeated dosing or infusions.",
    "apply","Miller/Baby Miller",641,"")

# ── 20: Pediatric trauma anesthesia ───────────────────────────────────────────
t = sl[20]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-trauma-anes'
add(slug,tp,dm,dc,
    "Children are more susceptible than adults to which serious complications of succinylcholine?",
    "Cardiac arrhythmias, hyperkalemia, rhabdomyolysis, myoglobinemia, masseter spasm, and malignant hyperthermia — these risks are higher in children than adults with succinylcholine.",
    "Children have a higher proportion of undiagnosed myopathies (e.g., Duchenne muscular dystrophy) for which succinylcholine triggers life-threatening hyperkalemia and rhabdomyolysis.",
    "apply","Morgan & Mikhail",1458,"")
add(slug,tp,dm,dc,
    "Pediatric burn patients — what fluid resuscitation protocol is applied and how is burn area estimated?",
    "The Rule of Nines estimates burned BSA as a percentage of TBSA; Parkland formula (4 mL/kg/% TBSA in first 24 hours) is modified for children (includes maintenance fluid); actual fluid requirements are titrated to urine output.",
    "Children have different body surface area distributions than adults (larger head:body ratio); pediatric burn formulas must account for both burn-related losses and normal maintenance requirements.",
    "apply","Morgan & Mikhail",1345,"")
add(slug,tp,dm,dc,
    "In pediatric trauma patients, preferred induction agent for a hemodynamically unstable child is which drug and why?",
    "Ketamine — suitable for hemodynamically unstable pediatric patients because it maintains cardiovascular tone via sympathomimetic effects, unlike propofol which causes hypotension.",
    "Ketamine stimulates catecholamine release, maintaining heart rate and blood pressure during induction in hypovolemic states where other agents would cause cardiovascular collapse.",
    "apply","StatPearls: StatPearls   Asthma  Chronic Management",6,"Propofol in hemorrhagic shock")
add(slug,tp,dm,dc,
    "ETT size in pediatric patients is designated in what units, and how does tube diameter affect airflow resistance?",
    "Internal diameter (mm); resistance to airflow depends primarily on tube diameter (Poiseuille: R proportional to 1/r^4), with smaller contributions from length and curvature — small reductions in ID dramatically increase resistance.",
    "The 4th-power relationship means halving ETT diameter increases resistance 16-fold; tube selection in small children requires careful size optimization.",
    "apply","Morgan & Mikhail",515,"")
add(slug,tp,dm,dc,
    "Primary hemostatic defects (platelet/vascular) vs. secondary hemostatic defects (coagulation cascade) differ how in clinical bleeding pattern?",
    "Primary defects (platelet disorders): bleeding immediately follows minor trauma, superficial, mucosal. Secondary defects (coagulation factor deficiencies): bleeding is delayed, deep tissue (joints, muscles), may not occur until hours later.",
    "Primary hemostasis (platelet plug) stops initial bleeding immediately; coagulation cascade creates the stable fibrin clot — defects in each manifest at different time points.",
    "apply","Morgan & Mikhail",1181,"")

# ── 21: Pediatric urologic surgery ────────────────────────────────────────────
t = sl[21]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-urology-surg'
add(slug,tp,dm,dc,
    "Neuraxial blockade for pediatric urologic surgery (hypospadias, orchiopexy) established before incision offers what advantage over postoperative-only systemic analgesia?",
    "Established before incision and continued postoperatively, neuraxial analgesia blunts the metabolic and neuroendocrine stress response; lidocaine infusion has additional antihyperalgesic and anti-inflammatory properties.",
    "Pre-incision neuraxial blockade prevents central sensitization during surgery; systemic opioids started after incision cannot fully prevent wind-up already established.",
    "apply","Stanford CA-1",99,"")
add(slug,tp,dm,dc,
    "Hypertension as a perioperative risk factor is most significant when what condition is present?",
    "Hypertension is most significant when it is severe or uncontrolled; controlled hypertension carries less additional risk. Major cause of cardiovascular disease, stroke, and end-stage renal disease.",
    "Uncontrolled hypertension predicts labile intraoperative blood pressure, increased risk of myocardial ischemia, and end-organ vulnerability during the hemodynamic swings of surgery.",
    "recall","Miller/Baby Miller",226,"")
add(slug,tp,dm,dc,
    "Deep extubation vs. awake extubation — for pediatric urologic procedures, which approach reduces laryngospasm risk?",
    "Deep extubation — removes the ETT while under surgical anesthesia, avoiding the light-anesthesia 'excitable' phase when reflexes are at maximum irritability; risk is loss of protective reflexes.",
    "Pediatric patients undergoing urologic procedures benefit from smooth emergence; deep extubation eliminates the period of maximum laryngospasm risk but requires careful patient selection.",
    "apply","Miller/Baby Miller",648,"")
add(slug,tp,dm,dc,
    "Major solid organ resection (cancer surgery) carries what 30-day major bleeding risk category?",
    "High bleeding risk — 30-day risk of major bleed >2%; includes major orthopedic surgery and cancer solid tumor resection.",
    "Tumor resections often involve highly vascular tissue, adhesions, and the need for wide resection margins; preoperative anticoagulation management is critical.",
    "recall","Miller/Baby Miller",228,"")

# ── 22: Pediatric vascular access ─────────────────────────────────────────────
t = sl[22]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='peds-vascular-access'
add(slug,tp,dm,dc,
    "When peripheral IV access fails in a resuscitating pediatric patient, what vascular access route should be established immediately?",
    "Intraosseous (IO) access — uses the large medullary venous channels; provides emergency access to the venous circulation; needle directed away from the epiphyseal plate to minimize growth-plate injury.",
    "IO access can be established in seconds using the sternum, proximal tibia, or distal femur; drug and fluid pharmacokinetics are similar to IV administration via the medullary venous sinusoids.",
    "recall","Morgan & Mikhail",2073,"")
add(slug,tp,dm,dc,
    "Failure of a neonate to respond to respiratory resuscitative efforts mandates what immediate actions?",
    "Vascular access and blood gas analysis; consider pneumothorax (1% incidence) and congenital airway anomalies including tracheoesophageal fistula (1:3000–5000 incidence).",
    "Neonatal respiratory failure unresponsive to PPV may reflect underlying anatomy (TEF, choanal atresia, CDH) or pneumothorax; diagnostic and vascular access steps proceed in parallel.",
    "apply","Morgan & Mikhail",1433,"")
add(slug,tp,dm,dc,
    "Neonatal chest compressions technique — how is the sternum compressed and at what rate?",
    "Both thumbs placed just below the nipple line with fingers encircling the chest; sternum compressed 1/3 to 3/4 inch (1 cm) at 120 compressions per minute.",
    "The two-thumb encircling technique generates higher peak systolic and coronary perfusion pressures than the two-finger technique in neonates.",
    "recall","Morgan & Mikhail",1436,"")
add(slug,tp,dm,dc,
    "Meconium aspiration — when is endotracheal suctioning indicated versus not indicated?",
    "Suctioning is indicated for neonates with depressed respirations and meconium-stained fluid; for vigorous neonates with thin watery meconium, routine intubation for suctioning is NOT indicated.",
    "Current NRP guidelines reserve intubation for non-vigorous meconium-stained neonates; vigorous meconium-stained neonates are managed with stimulation and standard resuscitation.",
    "apply","Morgan & Mikhail",1433,"")

# ── 23: Perioperative Anaphylaxis to Antibiotics & Chlorhexidine ──────────────
t = sl[23]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-anaphylaxis'
add(slug,tp,dm,dc,
    "Latex allergy foods that cross-react include which items, and what patient populations are at highest risk?",
    "Cross-reacting foods: mango, kiwi, chestnut, avocado, passion fruit, banana. High-risk: multiple surgeries (spina bifida), healthcare workers, atopic individuals.",
    "Latex proteins share epitopes with certain fruit proteins; repeated latex exposure from multiple surgeries sensitizes patients, making pediatric patients with spina bifida highest-risk.",
    "recall","Morgan & Mikhail",2040,"Drug allergy cross-reactivity")
add(slug,tp,dm,dc,
    "Angioedema from hereditary C1-inhibitor deficiency differs from allergic angioedema in treatment — what is the first-line agent?",
    "C1-inhibitor replacement protein (C1INHRP) or fresh frozen plasma (as C1-INH source); epinephrine, antihistamines, and steroids are NOT effective for hereditary angioedema (HAE).",
    "HAE is bradykinin-mediated (not IgE/histamine-mediated); treatments that block histamine or stabilize mast cells are ineffective; C1-INH replacement blocks the bradykinin pathway.",
    "apply","Morgan & Mikhail",2036,"IgE-mediated angioedema")
add(slug,tp,dm,dc,
    "In a patient with pheochromocytoma, which neuromuscular blocking agents should be avoided and why?",
    "Atracurium (histamine release provokes catecholamine secretion from the tumor); use vecuronium or rocuronium instead. Vagolytic drugs (anticholinergics, pancuronium) may contribute to tachycardia.",
    "Pheochromocytoma cells respond to histamine by releasing catecholamines; NMBs that release histamine can precipitate hypertensive crisis and arrhythmias.",
    "apply","Morgan & Mikhail",401,"")
kps.append(script(
    "Perioperative Anaphylaxis to Antibiotics & Chlorhexidine", dc,
    "Prior antibiotic exposure, chlorhexidine-containing products (CVCs, wound care), latex contact, atopic history",
    "IgE-mediated mast cell and basophil degranulation releasing histamine, tryptase, prostaglandins, leukotrienes; anaphylaxis is type I hypersensitivity",
    "Acute onset within minutes of exposure; anaphylaxis progresses rapidly from urticaria/flushing to bronchospasm, hypotension, cardiovascular collapse",
    "Bronchospasm, hypotension, urticaria, angioedema; tryptase elevation (peak 1-2h post-event) confirms mast cell activation; perioperative presentation often lacks classic skin findings",
    "Death from cardiovascular collapse or refractory bronchospasm; epinephrine must be given immediately — delay sharply increases mortality"
))
add(slug,tp,dm,dc,
    "H2 receptor antagonists (ranitidine, cimetidine) are used preoperatively in high-risk patients for what anaphylaxis-adjacent benefit?",
    "H2 blockers reduce gastric acid secretion and pH, preventing acid aspiration pneumonitis; they are not first-line for anaphylaxis but are adjuncts (H1 + H2 blockade) in treatment.",
    "Both H1 and H2 receptors mediate histamine effects; combining H1 and H2 antagonists provides more complete histamine blockade during treatment of anaphylaxis.",
    "apply","Morgan & Mikhail",444,"")

# ── 24: Perioperative Cardiac Arrest: Etiology & Differential ─────────────────
t = sl[24]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-ca-etiology'
add(slug,tp,dm,dc,
    "A 2019 closed claims review of obstetrical anesthesia identified what as the top causes of claims?",
    "High neuraxial block, embolic events, and failed intubation dominated obstetrical anesthesia closed claims; early neurological consultation helps discern anesthesia vs. obstetric nerve injury.",
    "Closed claims data drive safety improvements; in obstetrics, airway and neuraxial complications dominate — prompting focus on RSI techniques, aspiration prophylaxis, and neuraxial testing.",
    "recall","Morgan & Mikhail",2020,"")
add(slug,tp,dm,dc,
    "Hypothermia decreases metabolic rate by what amount per degree Celsius, and what cardiac protection does this confer?",
    "Metabolic rate decreases ~8% per 1 degree C decrease in temperature; this reduces oxygen delivery requirements to tissues, decreasing demand on the heart and providing partial CNS protection from ischemia.",
    "Therapeutic hypothermia after cardiac arrest exploits the reduced metabolic demand during controlled cooling to limit reperfusion injury.",
    "recall","Stanford CA-1",64,"")
add(slug,tp,dm,dc,
    "In the PACU, what are the immediately reversible causes of oliguria that should be evaluated first?",
    "Urinary catheter obstruction, hypovolemia, and neuraxial-induced sympathetic blockade (loss of sympathetic tone); oliguria defined as <0.5 mL/kg/hr.",
    "Reversible mechanical or hemodynamic causes of oliguria must be excluded before attributing decreased urine output to acute renal injury.",
    "apply","Miller/Baby Miller",732,"")
add(slug,tp,dm,dc,
    "New-onset atrial fibrillation in the PACU — what is the immediate treatment goal?",
    "Control ventricular response rate immediately; hemodynamically unstable patients require prompt electrical cardioversion; stable patients can be rate-controlled with beta-blockers or calcium channel blockers.",
    "Rate control is the first priority to restore hemodynamic stability; rhythm control is secondary unless the patient is hemodynamically unstable.",
    "apply","Miller/Baby Miller",731,"")
add(slug,tp,dm,dc,
    "Hypovolemic shock in the PACU presents with what classic clinical triad?",
    "Tachycardia, tachypnea, mottled skin, and decreased urine output; ongoing bleeding and hemorrhagic shock must be treated with volume resuscitation and control of bleeding source.",
    "Sympathetic activation in response to volume depletion produces tachycardia and vasoconstriction (mottling); decreased renal perfusion manifests as oliguria.",
    "recall","Miller/Baby Miller",729,"")

# ── 25: Perioperative Cardiac Arrest: Management & Modified ACLS ──────────────
t = sl[25]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-ca-mgmt'
add(slug,tp,dm,dc,
    "What PETCO2 threshold after 20 minutes of CPR in an intubated patient suggests poor likelihood of ROSC?",
    "PETCO2 persistently <10 mmHg after 20 minutes of CPR in an intubated patient predicts poor likelihood of ROSC; this threshold does NOT apply to non-intubated patients.",
    "PETCO2 reflects pulmonary blood flow; values persistently below 10 mmHg indicate that compressions are not generating adequate cardiac output for viable perfusion.",
    "apply","Morgan & Mikhail",2057,"Non-intubated PETCO2 thresholds")
add(slug,tp,dm,dc,
    "Higher ROSC likelihood is associated with monitoring what two parameters during CPR?",
    "PETCO2 and diastolic blood pressure — both reflect cardiac output during compressions; monitoring either in real time is associated with higher ROSC in AHA registry data.",
    "Real-time physiologic feedback during CPR allows dynamic adjustment of compression depth, rate, and vasopressor dosing to optimize perfusion.",
    "apply","Miller/Baby Miller",838,"")
add(slug,tp,dm,dc,
    "In cardiac arrest with a PEA or asystole rhythm, what can mimic respiratory arrest and delay recognition?",
    "Agonal gasps — patients with cardiac arrest may exhibit agonal respirations that appear to be adequate breathing; this can lead to delay in starting compressions.",
    "Agonal breathing is a brainstem reflex unrelated to respiratory function; it does not provide adequate ventilation and should not delay CPR initiation.",
    "recall","StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)",7,"")
add(slug,tp,dm,dc,
    "Crisis resource management (CRM) in anesthesia was adapted from which industry, and what is its key organizational benefit?",
    "Adapted from the aviation industry to medical care by anesthesiologists; CRM decreases disorganization during crises and improves outcomes by accessing the collective knowledge of the team.",
    "Aviation's CRM framework addresses human factors in high-stakes, time-pressured environments; its translation to anesthesia formalized team communication, role clarity, and cognitive aid use.",
    "recall","Miller/Baby Miller",838,"")
add(slug,tp,dm,dc,
    "Epinephrine's role in ACLS was reaffirmed in 2020 AHA guidelines — what is its primary mechanism in cardiac arrest?",
    "Alpha-1 adrenergic vasoconstriction increases aortic diastolic pressure and coronary perfusion pressure, improving chances of ROSC; vasopressin was removed from guidelines due to lack of demonstrated benefit.",
    "Coronary perfusion pressure during CPR determines likelihood of ROSC; epinephrine-mediated vasoconstriction maintains aortic diastolic pressure, the main driver of coronary flow during compressions.",
    "apply","Morgan & Mikhail",2057,"Vasopressin in ACLS")

# ── 26: Perioperative Crisis Resource Management ───────────────────────────────
t = sl[26]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-crm'
add(slug,tp,dm,dc,
    "Crisis resource management (CRM) in anesthesia originated from which domain and what does it fundamentally improve?",
    "CRM was adapted from aviation by anesthesiologists; it decreases disorganization during crises and improves patient outcomes by leveraging the collective knowledge and skills of the entire care team.",
    "Aviation's CRM formalized that human errors in high-stakes environments are reduced by structured communication, role assignment, and shared mental models — directly applicable to the OR.",
    "recall","Miller/Baby Miller",838,"")
add(slug,tp,dm,dc,
    "Anesthesiologists are involved in what broad scope of patient care beyond intraoperative management?",
    "Perioperative medicine: preoperative assessment and optimization, the surgical procedure, and subsequent care until the patient returns to primary/longitudinal care — spanning the full perioperative period.",
    "The modern anesthesiologist's role has expanded beyond the OR to encompass preoperative risk stratification, optimization, and postoperative recovery facilitation.",
    "recall","Miller/Baby Miller",778,"")
add(slug,tp,dm,dc,
    "PETCO2 is specifically listed as a marker of what CPR quality metric, and how does a prolonged drop signal?",
    "PETCO2 is a marker of CPR quality (reflects cardiac output from compressions); a prolonged reduction signals inadequate compressions or systemic vasodilation and should prompt reassessment of technique.",
    "Real-time PETCO2 feedback allows immediate detection of compression ineffectiveness or vasodilatory states, enabling corrective action during resuscitation.",
    "apply","Miller/Baby Miller",838,"")
add(slug,tp,dm,dc,
    "Laser safety in the OR requires what protection for OR personnel?",
    "Protective eyewear specific to the laser type; some lasers (ophthalmic, vascular mapping with short focal length) do not require eyewear; for others, protective goggles must be worn by all personnel.",
    "Each laser wavelength requires wavelength-specific optical filters; generic goggles do not protect against all laser types and must match the specific device in use.",
    "recall","Morgan & Mikhail",56,"")
add(slug,tp,dm,dc,
    "Routine use of intraoperative TEE outside the cardiac OR is limited by what two factors?",
    "Cost of equipment and training required to correctly interpret images; TEE use is expected to increase as anesthesia staff perform more echocardiographic examinations perioperatively.",
    "TEE provides real-time assessment of cardiac function, volume status, and surgical complications; expanding training in echocardiography is a key trend in perioperative medicine.",
    "recall","Morgan & Mikhail",185,"")

# ── 27: Perioperative Management of the Anticoagulated Patient & Reversal ──────
t = sl[27]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-anticoag-reversal'
add(slug,tp,dm,dc,
    "Supplemental protamine after CPB — when should additional protamine (50–100 mg) be considered?",
    "After administration of unwashed blood remaining in the pump reservoir post-CPB, because that blood contains heparin; supplemental protamine prevents residual heparin effect.",
    "Pump-reservoir blood is heparin-containing; returning it without additional protamine can cause postoperative coagulopathy from heparin rebound.",
    "apply","Morgan & Mikhail",755,"")
add(slug,tp,dm,dc,
    "Flumazenil reversal of benzodiazepine sedation — what dose and what limitation exists?",
    "0.2 mg/min IV until desired reversal, usual total dose 0.6–1.0 mg; limitation: rapid hepatic clearance means resedation can occur — repeat doses may be needed.",
    "Flumazenil's short half-life (less than most benzodiazepines) means the antagonist is cleared before the agonist, risking resedation — patients must be monitored after reversal.",
    "apply","Morgan & Mikhail",467,"Naloxone re-narcotization")
add(slug,tp,dm,dc,
    "Anticoagulation must be established before CPB to prevent what complication?",
    "Acute disseminated intravascular coagulation (DIC) — contact of blood with the CPB circuit activates the complement, coagulation, and kallikrein systems, requiring full anticoagulation with heparin before bypass initiation.",
    "The synthetic surfaces of the CPB circuit act as a massive thrombogenic stimulus; without full anticoagulation, consumptive coagulopathy (DIC) develops rapidly.",
    "recall","Morgan & Mikhail",707,"")
add(slug,tp,dm,dc,
    "For an urgent appendectomy with INR 1.8, what is the most appropriate coagulation management?",
    "FFP administration is most appropriate (ITE answer B); warfarin reversal with FFP is indicated for urgent/emergent surgery where waiting for vitamin K effect is not feasible.",
    "Vitamin K alone takes 6–24 hours to reverse warfarin; FFP provides immediate factor replacement for urgent surgical hemostasis.",
    "apply","Stanford CA-1",50,"")
add(slug,tp,dm,dc,
    "Naloxone, flumazenil, and physostigmine — what is the indication for each in delayed emergence?",
    "Naloxone reverses opioid-induced delayed emergence; flumazenil reverses benzodiazepine effect; physostigmine (1–2 mg IV) may partially reverse other sedating agents including anticholinergics.",
    "Delayed emergence has multiple pharmacologic causes; systematic reversal of suspected drug effects guides the differential diagnosis before attributing emergence delay to neurologic causes.",
    "apply","Morgan & Mikhail",353,"")

# ── 28: Perioperative Patient Safety Standards & Monitoring ───────────────────
t = sl[28]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-patient-safety'
add(slug,tp,dm,dc,
    "Lung-protective ventilation uses what tidal volume and plateau pressure targets, and what mortality benefit was shown?",
    "Vt 6 mL/kg (IBW) with plateau pressure <30 cmH2O associated with reduced mortality compared to Vt 12 mL/kg in patients with ARDS.",
    "High tidal volumes cause volutrauma and barotrauma, perpetuating inflammatory injury in ARDS; low-Vt ventilation reduces biotrauma and improves survival.",
    "recall","Morgan & Mikhail",2165,"")
add(slug,tp,dm,dc,
    "Pulmonary edema results from two pathophysiologic mechanisms — what are they?",
    "Increased net hydrostatic pressure across capillaries (hemodynamic/cardiogenic) OR increased alveolar-capillary membrane permeability (non-cardiogenic/ARDS); these have different treatments.",
    "Distinguishing cardiogenic (elevated PAWP, responds to diuresis) from non-cardiogenic edema (normal PAWP, requires lung-protective ventilation) guides specific therapy.",
    "recall","Morgan & Mikhail",2125,"")
add(slug,tp,dm,dc,
    "Patients with FEV1 below what threshold may require postoperative ventilation after thoracic or upper abdominal surgery?",
    "FEV1 <50% predicted — these patients with restrictive or obstructive disease may not have sufficient respiratory reserve to clear secretions and maintain gas exchange post-extubation.",
    "Postoperative respiratory muscle dysfunction combined with pre-existing lung disease reduces peak expiratory flow below the threshold needed for effective cough.",
    "recall","Morgan & Mikhail",874,"")
add(slug,tp,dm,dc,
    "An anesthesia 'time-out' at the conclusion of machine check confirms what as its final step?",
    "Ventilator settings are confirmed and readiness to deliver anesthesia care is verified — an 'anesthesia time-out' is the last step before patient care begins.",
    "The anesthesia time-out mirrors the surgical time-out concept, ensuring all safety checks are complete and equipment is configured for the specific patient and case.",
    "recall","Miller/Baby Miller",276,"")
add(slug,tp,dm,dc,
    "Peak airway pressure increases with what two distinct physiologic causes, and how can you distinguish them?",
    "Increased resistance (bronchospasm, secretions, kinked ETT — plateau pressure unchanged) vs. decreased compliance (pneumothorax, pulmonary edema, abdominal distension — plateau pressure also rises).",
    "Peak pressure reflects both resistance and compliance; simultaneous plateau pressure measurement with an inspiratory hold distinguishes the two — normal plateau excludes compliance decrease.",
    "analyze","Miller/Baby Miller",380,"")

# ── 29: Perioperative Pulmonary Edema ─────────────────────────────────────────
t = sl[29]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-pulm-edema'
add(slug,tp,dm,dc,
    "Cardiovascular complications account for what proportion of deaths following noncardiac surgery?",
    "25% to 50% of deaths following noncardiac surgery; perioperative MI, pulmonary edema, arrhythmias, stroke, and thromboembolism are the most common complications.",
    "The perioperative period creates a pro-inflammatory, pro-thrombotic, hemodynamically stressful environment that precipitates cardiovascular events in at-risk patients.",
    "recall","Morgan & Mikhail",615,"")
add(slug,tp,dm,dc,
    "Pulmonary venous hypertension from LV failure or mitral stenosis causes pulmonary edema by what mechanism?",
    "Elevated pulmonary venous pressure is transmitted retrograde to the pulmonary capillaries (Pc'), raising hydrostatic pressure above oncotic pressure and forcing fluid into the alveolar interstitium.",
    "Starling's law of fluid exchange: when capillary hydrostatic pressure exceeds colloid oncotic pressure, net filtration into the interstitium exceeds lymphatic drainage, causing edema.",
    "apply","Morgan & Mikhail",2130,"")
add(slug,tp,dm,dc,
    "Nitroglycerin's beneficial effect in cardiac patients with pulmonary edema operates via what mechanism?",
    "Nitroglycerin redistributes coronary blood flow, reduces preload (venodilation), and reduces afterload (arteriolar dilation at higher doses) — decreasing end-systolic pressure and oxygen demand while reducing pulmonary congestion.",
    "Venodilation reduces ventricular filling pressure and pulmonary capillary wedge pressure, acutely reducing pulmonary edema without requiring diuresis.",
    "apply","Morgan & Mikhail",410,"")
add(slug,tp,dm,dc,
    "The five conditions associated with increased perioperative cardiac risk include which diagnoses?",
    "Ischemic heart disease (MI history, ECG changes), congestive heart failure (dyspnea, pulmonary edema), cerebrovascular disease (stroke), diabetes mellitus, and renal insufficiency — forming the basis of the Lee Revised Cardiac Risk Index.",
    "These conditions reflect generalized arteriosclerosis and end-organ vulnerability; each independently increases perioperative cardiac event risk.",
    "recall","Morgan & Mikhail",619,"")
add(slug,tp,dm,dc,
    "Intraoperative bronchospasm manifests as what capnograph waveform pattern?",
    "Slowly rising capnogram waveform with a shark-fin shape (upsloping plateau), increasing peak airway pressures (plateau may be unchanged), and decreasing exhaled tidal volumes — reflecting expiratory airflow obstruction.",
    "Bronchospasm prolongs alveolar emptying; CO2-rich gas continues being exhaled during the plateau phase, creating a rising rather than flat ETCO2 waveform.",
    "apply","Morgan & Mikhail",868,"")
kps.append(script(
    "Perioperative Pulmonary Edema", dc,
    "LV failure, mitral stenosis, volume overload, postobstructive (negative-pressure), neurogenic; laparoscopic procedures",
    "Cardiogenic: elevated Pc' from elevated LVEDP/PAWP forces fluid across alveolar-capillary membrane. Non-cardiogenic: increased membrane permeability from inflammatory mediators",
    "Acute, often within minutes to hours of precipitating event; postobstructive can occur within minutes of laryngospasm/upper airway obstruction relief",
    "Bilateral crackles, hypoxia, pink frothy sputum (cardiogenic); decreased SaO2, elevated peak airway pressures; chest X-ray bilateral infiltrates",
    "Respiratory failure requiring intubation; cardiovascular collapse if untreated; death"
))

# ── 30: Perioperative Stroke & Neurological Crises ────────────────────────────
t = sl[30]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-stroke'
add(slug,tp,dm,dc,
    "Perioperative stroke is rare except after which surgical categories?",
    "Neurological, cardiac, and cerebrovascular surgery carry the highest perioperative stroke risk; diagnosis requires neurological evaluation and radiological imaging.",
    "These surgical categories directly manipulate or cause hemodynamic effects on cerebral vasculature; embolism and hypoperfusion are the dominant mechanisms.",
    "recall","Morgan & Mikhail",2099,"")
add(slug,tp,dm,dc,
    "Carotid endarterectomy is recommended for what degree of carotid stenosis, and what are the criteria?",
    "Symptomatic stenosis 30–70% (ulcerated plaque or TIA) or asymptomatic stenosis >60%; stenting has replaced CEA in some indications. 30-day perioperative morbidity is 4–10%, primarily neurological.",
    "CEA removes the stenotic atherosclerotic plaque to prevent embolic stroke; benefit exceeds risk only when surgical mortality/stroke rate is below the natural history stroke risk of the lesion.",
    "recall","Morgan & Mikhail",782,"")
add(slug,tp,dm,dc,
    "An asymptomatic carotid bruit has what relationship to hemodynamically significant stenosis?",
    "Fewer than 10% of patients with asymptomatic bruits have hemodynamically significant carotid artery lesions; asymptomatic bruits occur in up to 4% of patients >40 years but do not necessarily indicate significant obstruction.",
    "Turbulent flow causing a bruit can occur at many degrees of stenosis; the bruit itself does not predict the degree of luminal compromise without imaging.",
    "recall","Morgan & Mikhail",998,"")
add(slug,tp,dm,dc,
    "In patients with multiple sclerosis undergoing anesthesia, what intraoperative condition must be avoided?",
    "Increases in body temperature — hyperthermia causes exacerbation of MS symptoms and must be avoided; temperature management (active cooling if necessary) is essential.",
    "Elevated temperature impairs conduction in demyelinated axons by blocking sodium channels that are already marginally functional; even 0.5°C can precipitate symptom exacerbation.",
    "apply","Morgan & Mikhail",997,"")
add(slug,tp,dm,dc,
    "Induction of anesthesia in patients on long-term levodopa therapy may result in what hemodynamic effects?",
    "Either marked hypotension OR hypertension — levodopa affects dopaminergic and adrenergic tone unpredictably; anesthetic agents further alter these pathways.",
    "Levodopa is converted to dopamine, which affects vascular tone; abrupt fluctuations in levodopa levels combined with anesthetic vasodilation create unpredictable hemodynamic responses.",
    "apply","Morgan & Mikhail",997,"")
kps.append(script(
    "Perioperative Stroke & Neurological Crises", dc,
    "Cardiac surgery, CEA, aortic surgery; atrial fibrillation, carotid stenosis, coagulopathy; sustained hypotension or hypertension",
    "Embolic (air, thrombus, atheromatous debris) or hypoperfusion-mediated ischemia in cerebrovascular territories; hemorrhagic less common perioperatively",
    "Intraoperative to within 24–72 hours postoperatively; delayed presentations up to 7 days occur with hypercoagulable states or AF conversion",
    "New focal neurological deficit on emergence or postoperative wake-up; altered consciousness; confirmed by CT/MRI; may present as delayed emergence",
    "Permanent neurological disability or death; failure to recognize in PACU delays thrombolysis window (if applicable) and worsens outcome"
))

# ── 31: Perioperative temperature management ───────────────────────────────────
t = sl[31]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periop-temp-mgmt'
add(slug,tp,dm,dc,
    "What is the most effective method to reduce heat redistribution from core to periphery during the first 30 minutes after induction?",
    "Preoperative forced-air warming to the torso and legs for 30 minutes before induction — this pre-warms the peripheral compartment, reducing the temperature gradient that drives redistribution.",
    "Redistribution hypothermia occurs in the first 30–60 minutes as vasodilated peripheral tissues absorb heat from the warm core; pre-warming the periphery before induction eliminates this gradient.",
    "recall","Stanford CA-1",65,"")
add(slug,tp,dm,dc,
    "Acidemia produces adverse consequences regardless of whether it is respiratory or metabolic in origin. What are the main adverse effects of severe acidosis?",
    "Severe acidosis causes myocardial depression, arrhythmias, decreased response to catecholamines, pulmonary vasoconstriction, and impaired coagulation.",
    "Acidosis shifts the oxyhemoglobin dissociation curve rightward (Bohr effect) and directly depresses myocardial contractility by reducing intracellular calcium sensitivity.",
    "recall","Miller/Baby Miller",428,"")
add(slug,tp,dm,dc,
    "Cardiovascular complications account for what proportion of deaths following noncardiac surgery, and what does this motivate perioperatively?",
    "25–50% of perioperative deaths; this motivates cardiac risk stratification (RCRI, MICA), preoperative optimization, and intraoperative temperature and hemodynamic management.",
    "Temperature management directly affects cardiac outcomes: hypothermia increases myocardial oxygen demand via shivering, promotes coagulopathy, and worsens arrhythmia susceptibility.",
    "recall","Morgan & Mikhail",617,"")
add(slug,tp,dm,dc,
    "During cardiac surgery with CPB, ischemia causes what metabolic changes that active temperature management addresses?",
    "Ischemia depletes high-energy phosphate compounds (ATP) and causes accumulation of lactate and free radicals; hypothermic cardioplegia reduces metabolic demand, slowing depletion of energy stores.",
    "Each degree C of cooling reduces myocardial O2 consumption ~8%; cardioplegia combined with hypothermia provides maximal myocardial protection during the ischemic period of CPB.",
    "apply","Morgan & Mikhail",715,"")

# ── 32: Peripheral vascular surgery anesthesia ────────────────────────────────
t = sl[32]; tp=t['topic']; dm=t['domain']; dc=t['discipline']; slug='periph-vasc-surg-anes'
add(slug,tp,dm,dc,
    "CAD is responsible for approximately what proportion of all deaths in Western societies, and what is its anesthetic significance?",
    "CAD is responsible for ~25% of all deaths in Western societies; it is a major cause of perioperative morbidity and mortality requiring careful preoperative risk stratification.",
    "Peripheral vascular surgery patients have the highest CAD prevalence of any surgical population; coronary atherosclerosis coexists with peripheral arterial disease as a manifestation of systemic arteriosclerosis.",
    "recall","Morgan & Mikhail",635,"")
add(slug,tp,dm,dc,
    "Patients with asymptomatic but elevated postoperative troponin — what does this indicate?",
    "Myocardial injury after non-cardiac surgery (MINS) — troponin elevation without classic MI symptoms indicates myocardial cell death and is associated with increased 30-day mortality even without other MI evidence.",
    "The concept of MINS recognizes that perioperative troponin elevation, even asymptomatic, reflects myocardial ischemia or microinfarction with meaningful prognostic implications.",
    "recall","Morgan & Mikhail",624,"")
add(slug,tp,dm,dc,
    "Controlled hypertension — how does this affect intraoperative hemodynamic stability compared to uncontrolled hypertension?",
    "Controlled hypertensive patients are more prone to intraoperative episodes of myocardial ischemia, arrhythmias, and hemodynamic instability than normotensive patients; careful anesthetic depth adjustment and vasoactive drugs reduce this risk.",
    "Chronically hypertensive patients have a reset autoregulatory range and blunted baroreceptor sensitivity; hemodynamic swings under anesthesia exceed their narrowed physiologic reserve.",
    "apply","Morgan & Mikhail",629,"")
add(slug,tp,dm,dc,
    "For major aortic or peripheral vascular surgery, what monitoring and IV access is typically required?",
    "Two large-bore IV lines, indwelling arterial catheter; TEE, esophageal Doppler, or pulse wave analysis (Lidco/Vigileo) for cardiac output monitoring; combined general-epidural anesthesia is frequently used.",
    "Major vascular surgery involves aortic cross-clamping and unclamping causing dramatic hemodynamic swings; continuous arterial monitoring and cardiac output assessment are essential for management.",
    "apply","Morgan & Mikhail",1147,"")
add(slug,tp,dm,dc,
    "Dobutamine's primary cardiovascular mechanism and an important risk to know for cardiac patients?",
    "Dobutamine primarily increases cardiac output by increasing myocardial contractility (beta-1); peripheral resistance falls from beta-2 activation. Risk: increases myocardial oxygen consumption — should NOT be used routinely in patients at risk of ischemia.",
    "Dobutamine's inotropic effect increases oxygen demand; in patients with limited coronary reserve this can precipitate demand-related ischemia even while improving output.",
    "apply","Morgan & Mikhail",394,"")

print(f"Total KPs authored: {len(kps)}")
# Count by type
kp_count = sum(1 for k in kps if 'stem' in k)
script_count = sum(1 for k in kps if k.get('_type')=='illness_script')
pair_count = sum(1 for k in kps if k.get('_type')=='confusable_pair')
print(f"KPs: {kp_count}, scripts: {script_count}, pairs: {pair_count}")

with open('data/kp_full_part_9.json', 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)
print("Written OK")
