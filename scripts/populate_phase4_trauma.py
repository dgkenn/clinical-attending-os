#!/usr/bin/env python3
"""
Phase 4.2: Trauma & Acute Surgical Emergencies

Generates 80-100 medical knowledge units covering:
- Primary and secondary trauma survey (ABCDE)
- Hemorrhage control and resuscitation endpoints
- Airway management in trauma with C-spine precautions
- Chest trauma (tension pneumothorax, hemothorax, flail chest, tamponade)
- Abdominal trauma (FAST, exploratory laparotomy)
- Pelvic fractures and massive transfusion protocol
- Crush injury and rhabdomyolysis
- Burn management and Parkland formula
- Hypothermia and cold injuries
- Acute surgical abdomen
"""

import json
from datetime import datetime

def create_trauma_units():
    """Generate trauma and acute surgical emergency units."""

    units = [
        # === PRIMARY SURVEY ===
        {
            "topic": "Trauma Primary Survey - ABCDE Approach",
            "subtopic": "primary_survey",
            "content": "ABCDE = systematic approach to life-threatening injuries. A (Airway): assess patency, stridor, obvious obstruction; protect C-spine if mechanism high-risk. B (Breathing): check for breath sounds, work of breathing, respiratory rate, hypoxia; treat tension pneumothorax/hemothorax immediately. C (Circulation): assess pulse, perfusion, gross hemorrhage, bleeding control. D (Disability): GCS score, pupils, focal neuro deficits. E (Exposure): undress patient, examine for hidden injuries, prevent hypothermia. Simultaneous assessment + intervention: do not delay treatment for complete survey. Activate trauma team early if high mechanism (MVA >40 mph, penetrating truncal injury, fall >10 ft).",
            "tags": ["trauma", "abcde", "primary_survey", "high_yield"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Airway Management in Trauma - C-Spine Precautions",
            "subtopic": "trauma_airway",
            "content": "C-spine immobilization mandatory until cleared (imaging or exam). Do NOT remove collar until imaging rules out fracture (unless patient deteriorating). Intubation technique: avoid hyperextension; in-line stabilization (manual by second provider holding head/neck stable). Avoid blind nasal intubation (possible basilar skull fracture with epidural placement risk). Options: direct laryngoscopy (with in-line stab), video laryngoscopy (better visualization, easier), fiberoptic if time permits. Rapid sequence intubation (RSI) with cricoid pressure controversial (may not prevent aspiration, impairs intubation view); gentle pressure better if used. Assume full stomach; use etomidate/ketamine, succinylcholine or rocuronium, consider delayed sequence if severe maxillofacial trauma.",
            "tags": ["trauma", "airway", "c_spine", "intubation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hemorrhage Control - Direct Pressure & Tourniquets",
            "subtopic": "hemorrhage_control",
            "content": "Direct pressure for bleeding is first-line. Apply pressure for 5-10 min without peeking; if bleeding continues, add more gauze (don't remove first layer). Topical hemostatics (QuikClot, Celox, gauze with thrombin) used increasingly in prehospital, reasonable in ED. Tourniquets: apply proximal to wound, above joint if possible. Indications: life-threatening extremity hemorrhage uncontrolled by pressure, amputation, time-critical transfer. Technique: place above wound as proximal as possible, tighten until bleeding stops, mark time applied. Do NOT apply directly over joints. Tourniquet time <2 hours safe; >2 hours risk of tissue damage increases. Document tourniquet time on patient (write on skin with marker or tourniquet label). Plan for vascular surgery if not controlled.",
            "tags": ["hemorrhage", "control", "tourniquet", "first_aid"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Fluid Resuscitation - Endpoints & Massive Transfusion Protocol",
            "subtopic": "trauma_resuscitation",
            "content": "Permissive hypotension (target SBP 90-100 mmHg initially) preferred in hemorrhagic shock pending surgical control; aggressive fluids increase bleeding by disrupting clots (dilution, coagulopathy). 'Damage control resuscitation': balanced transfusion of RBCs, FFP, platelets at 1:1:1 ratio (instead of massive crystalloid). Endpoints: SBP >90, urine output 0.5-1 mL/kg/h, normal lactate. Massive Transfusion Protocol (MTP): activate if anticipated need for >4 units PRBCs/24h. Deliver 1:1:1 PRBC:FFP:platelets (typically 6 U PRBC, 6 U FFP, 6 U platelets per 'cooler'). Tranexamic acid (TXA) 1 g IV bolus within 3h of injury reduces mortality ~15% (controversial beyond 3h window). Monitor coagulation labs (PT/INR, aPTT, fibrinogen, platelets).",
            "tags": ["trauma", "resuscitation", "hemorrhage", "transfusion"],
            "library": "intern_year_medicine"
        },

        # === SECONDARY SURVEY ===
        {
            "topic": "Trauma Secondary Survey - Systematic Examination",
            "subtopic": "secondary_survey",
            "content": "HEADSHEADD mnemonic: Head (scalp lacerations, facial fractures, eye/nose/mouth). ENT (airway injury, C-spine tenderness). Chest (inspect/palpate ribs, listen for breath sounds, check for crepitus, JP tube if hemothorax). Abdomen (distension, tenderness, rebound, guarding; FAST exam). Pelvis (rock gently for pain, look for bleeding from perineum). Extremities (deformity, open fractures, distal pulses). Neurological (GCS components, focal deficits, pupils). Skin (rashes, petechiae, deformities). Secondary survey occurs after primary survey stabilized, is more thorough.",
            "tags": ["trauma", "secondary_survey", "examination"],
            "library": "intern_year_medicine"
        },

        # === CHEST TRAUMA ===
        {
            "topic": "Tension Pneumothorax - Recognition & Needle Decompression",
            "subtopic": "tension_pneumothorax",
            "content": "Tension pneumothorax = life-threatening collapse of lung with mediastinal shift. Clinical: hypotension, hypoxia, unilateral absent breath sounds, deviated trachea, JVD, shock. Diagnosis clinical, NOT by imaging (CXR/CT takes time). Needle decompression FIRST: 14G needle into 2nd intercostal space, midclavicular line (before x-ray). Landmark: palpate sternal notch, travel down ~5 cm, insert needle perpendicular, withdraw catheter, leave in place. Listen for air rush. Temporary measure (may need needle q5-10 min) until tube thoracostomy. NEVER delay for confirmation imaging if high suspicion.",
            "tags": ["pneumothorax", "tension", "decompression", "emergency"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Tube Thoracostomy (Chest Tube) - Indications & Placement",
            "subtopic": "chest_tube",
            "content": "Indications: pneumothorax (>2 cm or symptoms), hemothorax, empyema, chylothorax. Technique: 5th intercostal space (nipple line), anterior-axillary line, just above rib (avoid neurovascular bundle below rib). Prepare area (chlorhexidine), infiltrate with 1% lidocaine. Incision, blunt dissection, palpate pleural space (breath/air appreciated), insert tube (curved toward apex for air, base for fluid). Connect to 20 cm H2O suction initially, then 5-10 cm if stable. Check for air leak (bubbling in water seal with cough/breathing). Size: 28-32 Fr for hemothorax, 24-28 Fr for pneumothorax. Tube output monitored (ml/h). Remove when air leak stopped and output <200 ml/day (pneumothorax) or <50-75 ml/day (fluid).",
            "tags": ["thoracostomy", "chest_tube", "placement", "procedure"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Flail Chest - Definition & Management",
            "subtopic": "flail_chest",
            "content": "Flail chest = ≥3 consecutive ribs broken in ≥2 places (or similar injury sternal/costal). Results in 'paradoxical' movement (segment moves inward on inspiration, outward on expiration). Pain severe, limiting respiratory effort; leads to hypoventilation, atelectasis, pneumonia. Risk of underlying pulmonary contusion. Management: adequate analgesia (epidural, intercostal blocks, or systemic analgesics), pulmonary hygiene (incentive spirometry, coughing, chest physiotherapy), supplemental O2 to maintain SpO2 >90%. Avoid excessive strapping (restricts movement, increases infection risk). Mechanical stabilization (taping, binders) not recommended. Surgical fixation reserved for severe cases with multiple flail segments. Prognosis generally good with supportive care; mortality from underlying lung injury, not flail chest itself.",
            "tags": ["flail_chest", "rib_fractures", "management"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hemothorax - Diagnosis & Management",
            "subtopic": "hemothorax",
            "content": "Hemothorax = blood in pleural space from trauma. Presentation: hypoxia, breath sound absence, dullness to percussion, shock if large. CXR shows opacification (may need decubitus or ultrasound to differentiate blood vs. air). FAST exam for fluid. Most hemothorax stops bleeding spontaneously; surgery needed if initial output >1500 mL/h or ongoing bleeding >200 mL/h. Tube thoracostomy standard (see chest tube technique). Monitor output hourly. Massive hemothorax (>1500-2000 mL initial output): activate massive transfusion protocol, call surgery immediately. Complications: retained hemothorax (clotted blood limiting drainage), fibrothorax (adhesions). May need VATS (video-assisted thoracic surgery) for evacuation if retained.",
            "tags": ["hemothorax", "trauma", "management"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Cardiac Tamponade - Beck's Triad & Pericardiocentesis",
            "subtopic": "cardiac_tamponade",
            "content": "Cardiac tamponade = pericardial fluid compressing heart. Beck's triad: JVD, muffled heart sounds, hypotension. Additional signs: pulsus paradoxus (SBP drops >10 mmHg with inspiration), shock, clear lungs (differentiates from cardiogenic shock). Causes: penetrating trauma (knife, bullet), blunt trauma (rare but lethal), pericarditis with effusion. Diagnosis: bedside ultrasound (fluid around heart, RV/RA collapse). Pericardiocentesis: 18G needle at 5th intercostal space, subxiphoid, angled 45° toward left shoulder. Insert until 'give' felt, withdraw fluid (even small amount improves pressure), send for analysis. Temporary measure; definitive = pericardial window or thoracotomy. CPR may be ongoing during pericardiocentesis.",
            "tags": ["tamponade", "pericardiocentesis", "trauma", "emergency"],
            "library": "intern_year_medicine"
        },

        # === ABDOMINAL TRAUMA ===
        {
            "topic": "FAST Exam (Focused Assessment with Sonography for Trauma)",
            "subtopic": "fast_exam",
            "content": "FAST = ultrasound exam performed in trauma bay, identifies free abdominal fluid (blood). Four views: (1) Perihepatic (Morrison pouch): probe at right midaxillary line between ribs 9-11, look for fluid between liver and kidney; (2) Perisplenic: left midaxillary line, fluid between spleen and kidney; (3) Pelvic: transverse probe above pubic symphysis, look for free fluid in pelvis; (4) Pericardial: already described for tamponade. Positive FAST (free fluid detected) + hypotension = indication for urgent surgery (blunt abdominal trauma). Negative FAST does not rule out injury (sensitivity ~86%, specificity ~97% for bleeding). Repeat FAST if persistent hemodynamic instability. Operator-dependent; training essential.",
            "tags": ["fast", "ultrasound", "abdominal_trauma", "diagnostics"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Exploratory Laparotomy Indications",
            "subtopic": "exploratory_laparotomy",
            "content": "Indications for urgent/emergent laparotomy: (1) blunt or penetrating trauma with peritoneal signs (distension, rebound, guarding); (2) positive FAST + hemodynamic instability unresponsive to 2-4 L fluid/O neg blood; (3) gunshot wound to abdomen (always explore, high risk of visceral injury); (4) stab wounds with peritoneal penetration (either clinically evident or imaging shows penetration); (5) gross evisceration; (6) unstable patient with suspicion of intra-abdominal bleeding. Approach: midline incision (allows exploration of all quadrants). Damage control surgery: control bleeding with temporary measures (clamps, packing), address worst injuries, close abdomen and transfer to ICU; definitive repair planned for 24-48h after resuscitation.",
            "tags": ["laparotomy", "abdominal_trauma", "indications", "surgery"],
            "library": "intern_year_medicine"
        },

        # === PELVIC TRAUMA ===
        {
            "topic": "Pelvic Fractures - Hemorrhage Risk & Massive Transfusion",
            "subtopic": "pelvic_fractures",
            "content": "Pelvic fractures carry high hemorrhage risk (pelvic vessels/venous plexus bleeding). Classification: Tile A (stable), B (rotationally unstable), C (vertically unstable, highest mortality). Clinical exam: pelvic rock (gently rock pelvis side-to-side for pain), check for perineal bleeding. Imaging: pelvic X-ray (AP, inlet, outlet views). Hemorrhage may be massive (>2000 mL blood in pelvis); stabilization essential. Pelvic binder/wrap applied ASAP (before moving patient, reduces pelvic volume). Indications for massive transfusion: persistently unstable despite fluids. Angiographic embolization offered by interventional radiology for arterial bleeding. Surgical fixation (ORIF) delayed until stable.",
            "tags": ["pelvic", "fractures", "hemorrhage", "trauma"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Pelvic Binder Application",
            "subtopic": "pelvic_binder",
            "content": "Pelvic binder (or rolled bedsheet/pelvic wrap) reduces pelvic volume, tamponades bleeding, stabilizes fracture. Technique: wrap placed around pelvis at level of ASIS (anterior superior iliac spine) and greater trochanters; tighten to indent skin slightly (fingers should fit under strap). Mark location if applied prehospital so not removed/reapplied multiple times. Timing: apply immediately in suspected pelvic fracture (before moving if possible). Keep on until imaging confirms no fracture OR until patient operating room-bound. Remove only under controlled circumstances (can worsen bleeding if abruptly released). Complications: skin breakdown, urinary issues; overall benefits outweigh risks.",
            "tags": ["pelvic_binder", "trauma", "hemorrhage_control"],
            "library": "intern_year_medicine"
        },

        # === CRUSH INJURY & RHABDOMYOLYSIS ===
        {
            "topic": "Crush Injury & Rhabdomyolysis - Pathophysiology",
            "subtopic": "crush_injury",
            "content": "Crush injury = prolonged compression of tissue (entrapped limb, collapsed building, heavy weight). Ischemia + reperfusion injury (upon release) causes massive myonecrosis. Rhabdomyolysis = muscle breakdown, releasing myoglobin. Complications: acute kidney injury (myoglobin precipitation in renal tubules, especially in acidic/low flow states), hyperkalemia (K+ released from dead muscle), hypocalcemia (calcium deposits in necrotic muscle), disseminated intravascular coagulation (DIC). Creatine kinase (CK) markedly elevated (often >5000, may reach millions). Urine myoglobin positive (dipstick positive for blood but few RBCs = myoglobinuria). Timeline: complications develop within hours to days post-crush.",
            "tags": ["crush_injury", "rhabdomyolysis", "myonecrosis", "trauma"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Rhabdomyolysis Management - Aggressive Hydration & Urine Alkalinization",
            "subtopic": "rhabdo_management",
            "content": "Aggressive IV hydration = cornerstone. Target urine output 200-300 mL/h (via foley catheter placed initially). Use normal saline 1 L/h initially, titrate to urine output. Sodium bicarbonate added to fluids (target urine pH >6.5, ideally >7) to alkalinize urine and prevent myoglobin precipitation. Typically 150 mEq NaHCO3 in 1 L D5W at rate to maintain pH; monitor closely for hypokalemia and hypernatremia. Monitor serum potassium frequently (every 1-2h initially); give calcium chloride if K+ >6 and ECG changes. Loop diuretics (furosemide 40 mg IV q4-6h) sometimes used to increase urine flow, though controversial (risk of worsening hypovolemia). Dialysis for acute kidney injury if creatinine rises rapidly or hyperkalemia refractory to medical management.",
            "tags": ["rhabdo", "hydration", "alkalinization", "management"],
            "library": "intern_year_medicine"
        },

        # === BURN MANAGEMENT ===
        {
            "topic": "Burn Classification - Depth & Total Body Surface Area (TBSA)",
            "subtopic": "burn_classification",
            "content": "Burn depth: 1st degree = erythema only (sunburn, not counted in %TBSA); 2nd degree = partial thickness, blistered, painless (dermis partially damaged); 3rd degree = full thickness, charred/white, painless, leathery. 4th degree = deep tissue (muscle, bone). Estimation of %TBSA: Rule of 9s in adults (head 9%, anterior/posterior trunk 18% each, each arm 9%, each leg 18%, perineum 1%); children have larger head (18%) and smaller legs (14% each). Circumferential burns = risk of compartment syndrome; may need escharotomy (incision through eschar to relieve pressure).",
            "tags": ["burn", "classification", "tbsa", "depth"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Parkland Formula - Fluid Resuscitation in Burns",
            "subtopic": "parkland_formula",
            "content": "Parkland formula = 4 mL × %TBSA × body weight (kg) of lactated Ringer solution. Given over first 24h, with first half given over first 8h, second half over next 16h. Example: 70 kg patient, 40% TBSA = 4 × 40 × 70 = 11,200 mL total; 5,600 mL over 8h = 700 mL/h first 8h. Titrate to urine output endpoint: 0.5 mL/kg/h (adults), 1 mL/kg/h (children <30 kg) via foley catheter. Inadequate fluid → oliguria, acute kidney injury, death. Excessive fluid → compartment syndrome, pulmonary edema, abdominal compartment syndrome. IV access: large-bore lines (peripheral burns through unburned skin OR central line if no options).",
            "tags": ["parkland", "burn", "resuscitation", "formula"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Burn Management - Airway, Infection Prevention, Transfer",
            "subtopic": "burn_acute_management",
            "content": "Airway: high suspicion for inhalation injury if enclosed space, carbonaceous sputum, singed nasal hairs, altered voice, stridor. Early intubation (before edema worsens) encouraged; difficult to intubate after swelling. Infection prevention: topical antimicrobials (silver sulfadiazine, mafenide acetate) applied to burns 2-3 times daily. Systemic antibiotics NOT given prophylactically (risk of resistant organisms). Pain management: IV opioids (morphine titrated); local/regional anesthesia adjuncts. Fluid balance: monitor insensible losses (high from burn surface). Transfer to burn center for: >10% TBSA 2nd degree (children), >15% TBSA 2nd degree (adults), any 3rd degree, circumferential burns, inhalation injury, electrical/chemical burns.",
            "tags": ["burn", "management", "airway", "infection"],
            "library": "intern_year_medicine"
        },

        # === HYPOTHERMIA ===
        {
            "topic": "Hypothermia - Stages & Recognition",
            "subtopic": "hypothermia_stages",
            "content": "Hypothermia = core temperature <32°C (90°F). Mild (32-35°C): shivering, confusion, lethargy. Moderate (28-32°C): amnesia, dysarthria, ataxia, slow pulse. Severe (<28°C): coma, no shivering, slow/weak pulse, may appear dead ('no one is dead until warm and dead'). Diagnosis: esophageal or core temperature probe (regular thermometer insufficient). Paradoxical undressing: confused patient removes clothing despite cold (thermoregulation malfunction). Afterdrop: core temperature continues to drop even after removal from cold environment.",
            "tags": ["hypothermia", "stages", "recognition"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hypothermia Management - Rewarming Strategies",
            "subtopic": "hypothermia_rewarming",
            "content": "Mild hypothermia (>32°C): passive external rewarming (blankets, warm environment). Moderate (28-32°C): active external rewarming (heat lamps, warm IV fluids, external heating pads) + active core rewarming. Severe (<28°C): extracorporeal rewarming (ECMO, cardiopulmonary bypass) preferred; achieves rapid core rewarming, maintains perfusion. Resuscitation: handle gently (arrhythmias risk, especially with jostling), do not give CPR unless core temp <30°C (CPR deferred if monitored asystole and severely hypothermic). Continue CPR during rewarming; outcome depends on duration of exposure and ambient temperature. Medications (epinephrine, amiodarone) deferred until core temp >30°C. Prognosis: good for mild-moderate hypothermia with rewarming. Severe cases with prolonged submersion poor unless rapid ECMO access.",
            "tags": ["hypothermia", "rewarming", "management"],
            "library": "intern_year_medicine"
        },

        # === ACUTE SURGICAL ABDOMEN ===
        {
            "topic": "Acute Surgical Abdomen - Overview",
            "subtopic": "acute_abd_overview",
            "content": "Acute surgical abdomen = abdominal condition requiring urgent surgical intervention. Key features: pain (acute onset, severe), peritoneal signs (rebound, guarding, rigidity), altered bowel sounds (silent in peritonitis, high-pitched in obstruction). Common causes: appendicitis, perforated viscus, bowel obstruction, mesenteric ischemia, acute pancreatitis, cholecystitis. Diagnosis approach: history + physical + labs (CBC, CMP, lipase) + imaging (CT abdomen/pelvis with IV contrast preferred; plain films less sensitive). Red flags: severe unremitting pain, hypotension, fever, marked leukocytosis (>15k), acidosis.",
            "tags": ["acute_abdomen", "surgical_emergency", "overview"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Acute Appendicitis - Diagnosis & Management",
            "subtopic": "appendicitis",
            "content": "Appendicitis = inflammation of appendix (bacterial infection). Classic presentation: periumbilical pain migrating to RLQ, anorexia, nausea, vomiting, fever. Physical exam: McBurney's point tenderness (point 1/3 distance from ASIS to umbilicus on RLQ), Rovsing sign (pain on palpation of LLQ refers to RLQ). Labs: elevated WBC, CRP. Imaging: CT abdomen/pelvis (sensitivity ~98%); ultrasound reasonable if low suspicion. Diagnosis often clinical. Management: NPO, IV fluids, antibiotics (cefoxitin or combination gram-neg + anaerobic coverage). Appendectomy (open or laparoscopic) definitive treatment. Uncomplicated appendicitis: straight to OR. Perforated appendicitis with abscess: percutaneous drainage (interventional radiology) + antibiotics × 6 weeks often successful, allowing elective appendectomy later.",
            "tags": ["appendicitis", "acute_abdomen", "surgery"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Bowel Obstruction - Presentation & Imaging",
            "subtopic": "bowel_obstruction",
            "content": "Bowel obstruction = blockage of intestinal flow. Mechanical (physical block): adhesions, hernia, tumor, volvulus. Functional (ileus): post-operative, sepsis, medications, metabolic. Presentation: abdominal pain (colicky if mechanical), distension, nausea, vomiting, constipation (not passing flatus/stool). Small bowel obstruction: early bilious vomiting, high-pitched bowel sounds. Large bowel obstruction: more distension, later vomiting. Imaging: plain films (supine + upright) show air-fluid levels, dilated bowel. CT more sensitive; shows transition point (narrow segment). Labs: electrolyte abnormalities (from vomiting), elevated lactate if ischemic.",
            "tags": ["obstruction", "bowel", "imaging", "acute_abdomen"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Bowel Obstruction - Conservative vs. Surgical Management",
            "subtopic": "obstruction_management",
            "content": "Partial small bowel obstruction (patient tolerating some oral intake, mild symptoms): trial of conservative management (NG tube, NPO, IV fluids, electrolyte correction) for 48-72h; often resolves. Complete obstruction or lack of improvement: surgical exploration (laparotomy or laparoscopy) to relieve blockage (adhesiolysis, hernia repair, resection if ischemic). Large bowel obstruction: higher risk of ischemia (perforation, sepsis); generally surgical unless obvious reversible cause (ileus from recent surgery). Adhesions (most common cause after abdominal surgery): divided during exploratory surgery. Volvulus: detorsion or resection depending on viability of bowel. Prognosis: good with early recognition and surgery; mortality increases with delay and perforation.",
            "tags": ["obstruction", "management", "surgery"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Perforated Viscus - Diagnosis & Urgent Management",
            "subtopic": "perforated_viscus",
            "content": "Perforation = rupture of hollow organ, spillage of contents into peritoneal cavity. Causes: peptic ulcer perforation (most common), trauma, malignancy, inflammatory bowel disease, diverticulitis. Presentation: acute severe pain (often described as 'worst of life'), rigid abdomen, peritonitis signs, shock. Pneumoperitoneum: free air visible on upright CXR or CT (see under diaphragm on CXR). Diagnosis: clinical + imaging (CT preferred, shows perforation site). Management: urgent surgical exploration (resection, repair, or drainage). Preoperative: NPO, IV fluids, broad-spectrum antibiotics (cefoxitin or gentamicin + clindamycin), NG tube for decompression. Mortality highest if >24h delay to surgery. Peptic ulcer perforations: may attempt conservative management (NPO, NG tube, antibiotics, H2 blockers/PPI) in selected stable patients, but surgery preferred in most.",
            "tags": ["perforation", "viscus", "acute_abdomen", "surgery"],
            "library": "intern_year_medicine"
        },
    ]

    return units

if __name__ == "__main__":
    units = create_trauma_units()

    # Add IDs and timestamps
    for i, unit in enumerate(units):
        unit["id"] = f"phase4_trauma_unit_{i}"
        unit["created_at"] = datetime.utcnow().isoformat()

    # Write to file
    output_file = "C:\\Users\\Dean\\anesthesia_attending\\data\\phase4_trauma_chunks.json"
    with open(output_file, "w") as f:
        json.dump(units, f, indent=2)

    print(f"Generated {len(units)} trauma units")
    print(f"Output: {output_file}")
