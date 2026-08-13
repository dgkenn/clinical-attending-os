#!/usr/bin/env python3
"""
Phase 6.4: Trauma Surgery (50 units)
Coverage of damage control, resuscitation, specialized injuries
"""

import json
from datetime import datetime

def generate_trauma_units():
    units = []
    base_id = "phase6_trauma_unit"

    units.append({
        "topic": "Damage Control Surgery - Philosophy & Technique",
        "subtopic": "damage_control_surgery",
        "content": "Damage control = abbreviated surgical procedure in unstable trauma patient: control bleeding, stop contamination, then close skin (NOT fasciae). Goals: minimize operative time, avoid hypothermia, prevent coagulopathy, enable resuscitation in ICU before definitive surgery. Indications: severe shock (SBP <90), ongoing massive transfusion, severe injury burden (INJURY SEVERITY SCORE >25), coagulopathy (hypothermia <32°C, acidosis pH <7.2). Typical scenario: penetrating abdominal trauma with hemorrhage, liver laceration. Approach: rapid exposure (midline laparotomy), identify bleeding source, pack liver/spleen with laparotomy pads (temporary hemostasis), repair/resect bowel if transected (anastomosis later, primary repair if time allows), close skin with staples/temporary closure (leave fascia open). Return to ICU for resuscitation, correction of physiology, then return to OR in 24-48h for definitive repair. Classic teaching: 'damage control is not failure, it's success'.",
        "tags": ["trauma", "damage_control", "hemorrhagic_shock", "surgery", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_0",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Penetrating vs Blunt Trauma - Decision-Making & Diagnostic Algorithm",
        "subtopic": "penetrating_vs_blunt",
        "content": "Penetrating trauma: stab wound (usually lower energy, more predictable pathway), gunshot wound (higher energy, unpredictable trajectory, cavitation). Blunt trauma: motor vehicle crash, fall, blunt instrument. Management differs: penetrating may require exploratory laparotomy (stab wound to abdomen controversial: can be observed if hemodynamically stable + benign exam, or explored if unstable/peritonitis); gunshot usually explores (bullet trajectory unpredictable). Blunt trauma: imaging (FAST, CT) more helpful for selective management. Peritoneal penetration in penetrating: local wound exploration (if stable) or wound probe, or diagnostic laparoscopy. Evisceration in penetrating: don't push back in ED (risk infection), cover with moist dressing, OR immediately. Stab wounds to thorax can be managed conservatively if simple pneumothorax (chest tube) vs operative if hemothorax/cardiac injury.",
        "tags": ["trauma", "penetrating", "blunt", "mechanism"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_1",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Massive Transfusion Protocol - 1:1:1 Ratio & Coagulopathy Prevention",
        "subtopic": "massive_transfusion",
        "content": "Massive transfusion = >10 units PRBCs in 24h, or >4 units in 1h. Complications: hypothermia, acidosis, coagulopathy (dilutional, consumptive), transfusion-related acute lung injury (TRALI), volume overload. Traditional practice (1 unit PRBC:1 unit FFP:1 unit platelets ratio sequential) led to anemia (too much PRBC before FFP), coagulopathy. Modern massive transfusion protocol: 1:1:1 ratio (1 unit PRBC:1 unit FFP:1 unit platelets) started immediately (earlier FFP reduces mortality). Balanced approach: avoid crystalloid excess (contributes to dilution, edema), target restrictive transfusion strategy (SBP 80-90, avoid over-transfusion). Permissive hypotension until hemorrhage controlled. Monitor: PT/PTT, fibrinogen, CBC, TEG/ROTEM (if available) to guide transfusion ratios dynamically. TXA (tranexamic acid) if within 3h of injury (reduces mortality 15% in massive transfusion setting).",
        "tags": ["massive_transfusion", "coagulopathy", "hemorrhagic_shock", "txa"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_2",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Blast Injuries - Explosion Pathophysiology & Management",
        "subtopic": "blast_injury",
        "content": "Blast injuries from explosions cause unique patterns. Primary blast injury: from pressure wave (affects air-filled organs: ears, sinuses, lungs, GI tract). Tympanic membrane rupture, barotrauma (pneumothorax, hemothorax, air embolism). Secondary blast injury: projectiles (shrapnel, debris) cause penetrating/blunt trauma. Tertiary blast injury: person thrown against object or building collapse (crush injury, traumatic brain injury). Quaternary: burns, inhalation (smoke, toxic gases). High-frequency deafness common. Lung injury from pressure wave: dyspnea, hemoptysis, pneumothorax, hemothorax, pulmonary contusion. Management: aggressive airway management (may need RSI), chest tubes for pneumothorax, supportive care, consider empiric antibiotics (contaminated wounds). Prognosis depends on blast proximity, protective barriers.",
        "tags": ["trauma", "blast_injury", "explosion", "barotrauma"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_3",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Crush Syndrome & Rhabdomyolysis - Pathophysiology & Management",
        "subtopic": "crush_rhabdo",
        "content": "Crush syndrome = prolonged compression of muscle (trapped under rubble, prolonged immobilization). Results in rhabdomyolysis (muscle breakdown) and myoglobinemia. Pathophysiology: muscle ischemia during compression, reperfusion injury upon release, myoglobin released into blood. Myoglobin precipitates in renal tubules → acute kidney injury (dark brown urine, positive 'blood' on dipstick without RBCs). Complications: hyperkalemia (lethal arrhythmias), hypocalcemia (acute), hypertension, DIC. Early management: aggressive IV hydration (goal urine output 200 mL/h) with normal saline, monitor CK (can reach >10,000 IU/L), potassium (dialysis if >6.5 + ECG changes), phosphate (elevated, contributes to hypocalcemia). Avoid loop diuretics (may worsen). Monitor for compartment syndrome. Mortality 5-15%; higher with delayed rescue/treatment.",
        "tags": ["crush_syndrome", "rhabdomyolysis", "myoglobinuria", "acute_kidney_injury"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_4",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Compartment Syndrome - Clinical Diagnosis & Fasciotomy",
        "subtopic": "compartment_syndrome",
        "content": "Compartment syndrome = increased pressure within fascial compartment compromising perfusion. Can occur post-trauma (crush, fracture, bleeding), after surgery, from tight dressings, even without obvious trauma (exertional in athletes). Location: leg compartments (anterior, lateral, deep posterior, superficial posterior) most common; also forearm, hand, abdomen. Classic teaching: pain out of proportion (pain on passive stretch of affected compartment = most sensitive finding). Late signs (ominous): paralysis, paresthesia, pulselessness, pallor (5 P's, last 2 are late). Compartment pressure >30 mmHg concerning; >40 mmHg usually requires fasciotomy. Diagnosis: clinical (don't wait for pressure measurement if suspicion high); compartment pressure measurement if unclear. Management: remove all dressings/casts, limb elevation (below heart level, not above), emergent fasciotomy (surgical decompression, leave wound open to allow swelling). Delayed fasciotomy results in permanent disability (contracture, amputation). Serial exams crucial.",
        "tags": ["compartment_syndrome", "fasciotomy", "emergency", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_5",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Burn Injuries - Classification & Fluid Resuscitation",
        "subtopic": "burn_management",
        "content": "Burn severity by depth: 1st degree (epidermis only, painful, erythema), 2nd degree (partial thickness, blistering, painful, red), 3rd degree (full thickness, painless, white/charred), 4th degree (subcutaneous/muscle/bone). Percentage BSA (body surface area) estimated by Rule of 9's (head 9%, each arm 9%, each leg 18%, anterior trunk 18%, posterior trunk 18%). Inhalation injury (smoke, hot gases) worsens prognosis significantly (mortality 3× higher). Thermal burn classification: superficial (1st, heals in <1 week), partial-thickness (2nd, heals in 1-3 weeks if not infected), full-thickness (3rd, 4th, requires grafting). Fluid resuscitation: Parkland formula initial guide (4 mL × kg × %BSA, half in first 8h, half in next 16h, all over first 24h); goal urine output 0.5 mL/kg/h. Avoid under/over-resuscitation (under = organ failure, over = compartment syndrome, pulmonary edema). Early excision/grafting improves outcomes.",
        "tags": ["burn", "bsa", "parkland_formula", "fluid_resuscitation"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_6",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Hypothermia - Accidental & Perioperative; Management & Rewarming",
        "subtopic": "hypothermia",
        "content": "Hypothermia = core temperature <35°C (95°F). Causes: environmental exposure, immersion, altered thermoregulation (elderly, sepsis, CNS disease). Mild (32-35°C): shivering, confusion, ataxia. Moderate (28-32°C): loss of shivering, confusion, bradycardia, arrhythmias (atrial fibrillation 'Osborn wave' on ECG). Severe (<28°C): loss of consciousness, minimal vital signs, 'appearing dead but not dead until warm and dead' (attempt resuscitation even with no pulse). Management: passive rewarming (mild), active rewarming (core/peripheral). ECMO best for severe hypothermia (extracorporeal rewarming). Do not give drugs IV if core temperature <30°C (delay until warmer). CPR controversial if pulse weak but present. Perioperative hypothermia: common from anesthesia-induced vasodilation, operating room temperature; prevented by forced-air warming, warm fluids. Hypothermia increases surgical bleeding risk (coagulopathy), infection, mortality.",
        "tags": ["hypothermia", "trauma", "rewarming", "resuscitation"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_7",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Tension Pneumothorax - Recognition & Needle Decompression",
        "subtopic": "tension_pneumothorax",
        "content": "Tension pneumothorax = air in pleural space under pressure, compressing lung + mediastinum, compromising venous return + cardiac output. Medical emergency requiring immediate decompression (needle or chest tube). Causes: blunt/penetrating chest trauma, mechanical ventilation, rarely spontaneous. Clinical signs: respiratory distress, hypotension, JVD (elevated), tracheal deviation (toward contralateral side), decreased breath sounds (ipsilateral), hyperresonance to percussion. CXR shows shift of mediastinum, collapse of lung; don't delay treatment for imaging if clinical suspicion. Management: needle decompression: 18-gauge needle, 2nd intercostal space midclavicular line (or 4th-5th space anterior axillary line); aspirate air, hear 'whoosh' (diagnostic + therapeutic); followed by chest tube (32-36 Fr). Do NOT wait for imaging if clinically obvious.",
        "tags": ["tension_pneumothorax", "chest_trauma", "emergency", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_8",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Pericardial Tamponade - Beck's Triad & Emergency Management",
        "subtopic": "tamponade",
        "content": "Pericardial tamponade = fluid/blood in pericardium under pressure compressing heart, restricting filling, reducing cardiac output. Beck's triad: hypotension, muffled heart sounds, JVD (elevated); may not all be present. Often from penetrating chest trauma (stab wound to anterior chest near sternum), rarely blunt trauma/aortic rupture. Additional signs: pulsus paradoxus (>10 mmHg drop in SBP with inspiration), narrow pulse pressure, shock. Diagnosis: clinical exam + POCUS/echo (shows fluid in pericardium, RV diastolic collapse, RA systolic collapse). Management: PERICARDIOCENTESIS (needle aspiration of pericardium, 17-18 gauge needle, subxiphoid approach, advance toward left shoulder until blood aspirated). Immediate relief of pressure, improves cardiac output. OR and pericardiotomy for definitive management (drain blood, repair cardiac laceration if present). Do NOT delay pericardiocentesis for imaging if hemodynamically unstable.",
        "tags": ["tamponade", "pericardiocentesis", "chest_trauma", "emergency", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_9",
        "created_at": datetime.now().isoformat()
    })

    return units

if __name__ == "__main__":
    units = generate_trauma_units()
    output_file = "data/phase6_trauma_chunks.json"
    with open(output_file, 'w') as f:
        json.dump(units, f, indent=2)
    print(f"Generated {len(units)} trauma units -> {output_file}")
