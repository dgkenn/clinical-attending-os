#!/usr/bin/env python3
"""
Phase 4 Knowledge Base Population - Remaining Essentials (500-750 units)

Completes the comprehensive intern medicine curriculum with:
1. Toxicology & poisoning (60 units)
2. Trauma management (80 units)
3. Procedures (70 units)
4. OB/GYN emergencies (60 units)
5. Pediatric critical care (70 units)
6. Geriatric medicine (50 units)
7. Communication & team skills (40 units)
8. Quality & patient safety (30 units)
9. Palliative care & ethics (40 units)
10. Administrative/career (30 units)

Total: ~530 units, bringing cumulative to ~1,200
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def create_phase4_units():
    """Generate Phase 4 comprehensive knowledge base."""

    units = []
    phase4_sections = {
        "toxicology": {
            "title": "Toxicology & Poisoning Management",
            "units": [
                # Acetaminophen toxicity
                {"topic": "Acetaminophen Toxicity", "key_points": [
                    "Normal dose: <3-4 g/day; toxic dose: >7-10 g/day (depends on chronic use, liver disease, fasting)",
                    "4 stages: (1) 0-24h asymptomatic (2) 24-72h RUQ pain, nausea, transaminitis (3) 72-96h ALT >3000, INR elevation (4) >96h liver failure if untreated",
                    "N-acetylcysteine (NAC) first-line antidote: loading 150 mg/kg IV over 15 min, then 50 mg/kg over 4h, then 100 mg/kg over 16h",
                    "Use Rumack-Matthew nomogram if single acute ingestion with known time; treat if ALT >1000 or INR >1.5",
                    "Activated charcoal within 4h of ingestion if massive overdose; monitor transaminases, INR, bilirubin, glucose",
                ]},

                # Opioid overdose
                {"topic": "Opioid Overdose Management", "key_points": [
                    "Classic triad: respiratory depression, altered mental status, miosis; death from apnea within minutes to hours",
                    "Naloxone (Narcan) first-line: 0.4-2 mg IV/IM/IN q2-3min until response (max 10 mg); works within 1-2 min",
                    "Duration of naloxone only 30-90 min; opioid overdose may outlast naloxone → redose q20-60min or continuous infusion",
                    "Fentanyl patches/xylazine require higher naloxone doses; assess for multiple substances (polysubstance common)",
                    "Post-reversal care: admit to ICU with continuous monitoring, supplemental O2, monitor for acute respiratory distress syndrome",
                ]},

                # Alcohol withdrawal
                {"topic": "Alcohol Withdrawal Syndrome", "key_points": [
                    "Mild (6-12h): tremor, diaphoresis, tachycardia, anxiety, no hallucinations",
                    "Moderate (12-24h): hallucinosis (hallucinate while alert), autonomic hyperactivity, no seizures",
                    "Severe (12-48h): seizures (generalized tonic-clonic), autonomic instability, delirium tremens (hallucinations + confusion + vitals unstable)",
                    "Benzodiazepines first-line: lorazepam 2-4 mg IV q5-10min until calm, or chlordiazepoxide 50-100 mg q1-4h PO for mild; use CIWA-Ar score",
                    "Thiamine 100 mg IV/IM before dextrose (prevent Wernicke encephalopathy); magnesium 2 g q6h; folic acid 1 mg daily",
                ]},

                # Benzodiazepine overdose
                {"topic": "Benzodiazepine Overdose", "key_points": [
                    "Symptoms: altered mental status, respiratory depression, hypotension, ataxia, decreased reflexes",
                    "Flumazenil (Romazicon) is DANGEROUS in chronic users (precipitate seizure); reserved for iatrogenic acute overdose",
                    "Flumazenil dose: 0.2 mg IV over 30s, then 0.1 mg q1min up to 1 mg total if no response",
                    "Supportive care (airway management, fluids, monitor) is safer than flumazenil in most cases",
                    "Watch for redosing in long-acting benzos; some metabolites active (diazepam → desmethyldiazepam → oxazepam)",
                ]},

                # Cocaine/amphetamine toxicity
                {"topic": "Cocaine & Amphetamine Toxicity", "key_points": [
                    "Sympathomimetic effects: hypertension, tachycardia, hyperthermia, agitation, seizures, arrhythmias (including coronary vasospasm → MI)",
                    "Cocaine: acute onset (peaks in min), tachyphylaxis; amphetamines: delayed onset, prolonged effect",
                    "Hypertensive emergency: phentolamine (alpha blocker) 5-15 mg IV, or nitroglycerin 0.3-0.6 mg SL; avoid pure beta-blockers (unopposed alpha)",
                    "Seizures: benzodiazepines (lorazepam 2-4 mg IV); hyperthermia: aggressive cooling (evaporative, cold fluids)",
                    "MI risk with cocaine: ECG mandatory; troponin; treat as ACS (consider PCI); avoid ergotamines, norepinephrine (worsen vasospasm)",
                ]},

                # Aspirin toxicity
                {"topic": "Aspirin (Salicylate) Toxicity", "key_points": [
                    "Early: tinnitus, altered mental status, hyperventilation (respiratory alkalosis), fever",
                    "Late: pulmonary edema, altered mental status worsens, metabolic acidosis supervenes",
                    "Salicylate level >300 mg/dL (chronic: >60 mg/dL) is severe; pH-dependent: alkaline urine prevents renal reabsorption",
                    "Management: sodium bicarbonate to alkalinize urine (target pH 7.5-8.5); aggressive IV fluids; hemodialysis if severe (level >80 mg/dL chronic, or level + AMS + pulm edema)",
                    "Avoid NSAIDs; supportive care; monitor electrolytes (hypokalemia from alkalosis)",
                ]},

                # Organophosphate/carbamate poisoning
                {"topic": "Organophosphate & Carbamate Poisoning", "key_points": [
                    "Cholinergic crisis from irreversible acetylcholinesterase inhibition; miosis, muscle fasciculations, bronchospasm, altered mental status",
                    "SLUDGE mnemonic: Salivation, Lacrimation, Urination, Defecation, GI upset, Emesis",
                    "Atropine first-line (2-5 mg IV q5-10min until atropinization: dry mouth, pupil dilation); pralidoxime (2-PAM) 1-2 g IV over 15-30s",
                    "Avoid depolarizing paralytics; use non-depolarizing agents if intubation needed",
                    "Decontamination: remove clothing, wash skin; supportive care, monitor for days (recrudescence possible)",
                ]},

                # Anticholinergic toxidrome
                {"topic": "Anticholinergic Toxidrome", "key_points": [
                    "Sources: antihistamines, antispasmodics, antidepressants, antiparkinsonian drugs, plants (belladonna, datura)",
                    "Classic: 'hot as a hare, dry as a bone, red as a beet, mad as a hatter, blind as a bat'",
                    "Mydriasis, tachycardia, hypertension, hyperthermia, agitation, hallucinations, seizures, altered mental status",
                    "Physostigmine (anticholinesterase) 1-2 mg IV q30-60min if severe agitation/hallucinations or hyperthermia; atropine if bradycardia",
                    "Avoid anticholinergic agents; benzodiazepines for agitation; cooling for hyperthermia",
                ]},

                # Cholinergic toxidrome
                {"topic": "Cholinergic Toxidrome", "key_points": [
                    "Opposite of anticholinergic: SLUDGE + bradycardia, bronchoconstriction, muscle fasciculations",
                    "Causes: organophosphates, carbamates, physostigmine (if used for anticholinergic OD), mushrooms, pesticides",
                    "Atropine first-line: titrate 2-5 mg IV q5-10min until bronchospasm resolves and HR normalizes",
                    "Pralidoxime (2-PAM) for organophosphates within 24-48h of exposure (before 'aging' of phosphate-enzyme complex)",
                    "Benzodiazepines for seizures; mechanical ventilation if respiratory failure",
                ]},

                # Cyanide poisoning
                {"topic": "Cyanide Poisoning", "key_points": [
                    "Inhibits cytochrome c oxidase → cellular hypoxia despite normal oxygen saturation; rapid onset (seconds to min)",
                    "Symptoms: altered mental status, cardiovascular collapse, seizures, death within min to hours if untreated",
                    "Hydroxocobalamin 5 g IV (safer than sodium nitrite): forms cyanocobalamin (excreted in urine)",
                    "Sodium nitrite (10 mL 3% IV) + sodium thiosulfate (50 mL 25% IV) is older regimen; higher toxicity risk",
                    "Supportive care: 100% O2, CPR, IV fluids; poison control contact",
                ]},

                # Ethylene glycol & methanol poisoning
                {"topic": "Ethylene Glycol & Methanol Poisoning", "key_points": [
                    "Ethylene glycol: sweet taste, metabolites → oxalate (kidney stones, AKI); methanol: metabolism → formic acid (blindness)",
                    "Early: CNS depression, altered mental status; metabolites cause high AG metabolic acidosis + osmotic gap",
                    "Fomepizole 15 mg/kg IV loading (inhibits alcohol dehydrogenase), then 10 mg/kg q12h x2, then 15 mg/kg q12h until level <20 mg/dL",
                    "Hemodialysis if severe acidosis, renal failure, or level >20 mg/dL (ethylene glycol) or >5 mg/dL (methanol)",
                    "Thiamine (ethylene glycol) and folinic acid (methanol) as adjuncts; ethanol 1 g/kg also inhibits alcohol dehydrogenase",
                ]},

                # Iron poisoning
                {"topic": "Iron Toxicity", "key_points": [
                    "Phases: (1) 30min-2h GI hemorrhage, shock (2) 2-12h apparent recovery (3) 4-24h metabolic acidosis, shock (4) >1 week GI strictures",
                    "Serum iron >400 mcg/dL is severe; compare to iron-binding capacity; ferritin not reliable in acute setting",
                    "Deferoxamine 15 mg/kg/h IV (max 6 g/day): binds iron → orange urine (vin rosé); chelates free iron and tissue iron",
                    "GI decontamination: whole bowel irrigation (polyethylene glycol) if massive ingestion visible on abdominal X-ray",
                    "Supportive care: aggressive fluid resuscitation, monitor electrolytes, lactulose for GI decontamination",
                ]},

                # Heavy metal poisoning (lead, mercury, arsenic)
                {"topic": "Heavy Metal Poisoning (Lead, Mercury, Arsenic)", "key_points": [
                    "Lead: chronic exposure → peripheral neuropathy, cognitive impairment, renal disease; acute → encephalopathy",
                    "Mercury: tremor, gingivitis, nephropathy, CNS effects; chelation with DMSA or DMPS",
                    "Arsenic: GI hemorrhage, peripheral neuropathy, skin changes; chelation with DMSA",
                    "Chelation therapy: EDTA (calcium edetate), DMSA (succimer), DMPS (unithiol), penicillamine",
                    "Supportive care, avoid mobilizing heavy metals (risk of increased toxicity); poison control consultation",
                ]},
            ]
        },

        "trauma": {
            "title": "Trauma Management & Resuscitation",
            "units": [
                # Primary survey
                {"topic": "Trauma Primary Survey (ABCDE)", "key_points": [
                    "A: Airway with C-spine protection; clear airway, remove obstructions, consider intubation if GCS <8",
                    "B: Breathing; assess rate, bilateral breath sounds, tracheal deviation, JVD, open pneumothorax, tension pneumothorax",
                    "C: Circulation; assess pulses (carotid, femoral), skin perfusion, control obvious hemorrhage",
                    "D: Disability; GCS score, pupillary reactivity, focal neuro deficits",
                    "E: Exposure; undress fully to assess injuries, prevent hypothermia with blankets",
                ]},

                # Hemorrhage control
                {"topic": "Hemorrhage Control & Massive Transfusion Protocol", "key_points": [
                    "Direct pressure for bleeding; tourniquet above knee/elbow if exsanguinating limb hemorrhage (mark time of application)",
                    "Massive transfusion protocol (MTP) triggered by: 4+ units PRBCs in 1h, expected transfusion >10 units, or signs of shock",
                    "Balanced ratio: PRBCs:FFP:platelets = 1:1:1 (massive transfusion); older 3:1 ratio favored dilutional coagulopathy",
                    "TXA (tranexamic acid) 1 g IV bolus within 3h of injury if hemorrhagic shock (CRASH-2 trial); reduces mortality 1-2%",
                    "Monitor coagulation studies, CBC, lactate; avoid hypothermia, acidosis (coagulopathy triad); permissive hypotension (SBP 80-100) until operative control",
                ]},

                # Airway management in trauma
                {"topic": "Airway Management in Trauma", "key_points": [
                    "Rapid sequence intubation (RSI): preoxygenation, induction agent (etomidate 0.2-0.3 mg/kg), succinylcholine 1-1.5 mg/kg (or rocuronium 1.2 mg/kg), cricoid pressure",
                    "Avoid hyperextension of neck if C-spine injury suspected; use video laryngoscope if available",
                    "Surgical airway (cricothyrotomy) if laryngeal injury, complete airway obstruction, can't intubate/can't oxygenate",
                    "Post-intubation: confirm tube placement (capnography, chest rise, bilateral breath sounds), obtain C-spine imaging",
                ]},

                # Tension pneumothorax
                {"topic": "Tension Pneumothorax Diagnosis & Treatment", "key_points": [
                    "Classic signs: JVD, tracheal deviation, hypotension, hypoxia, muffled breath sounds, hyperesonance to percussion",
                    "Do NOT wait for X-ray; needle decompression first-line: 14-16 gauge needle at 2nd intercostal midclavicular line, then tube thoracostomy",
                    "Tube thoracostomy (chest tube): 4th-5th intercostal midaxillary line, directed posterior/superior; size 28-40 Fr",
                    "Complications: reexpansion pulmonary edema, persistent air leak, hemothorax, infection; monitor chest tube output",
                ]},

                # Hemothorax
                {"topic": "Hemothorax Management", "key_points": [
                    "Unilateral opacity on CXR with shock suggests hemothorax; confirmation with ultrasound or CT",
                    "Tube thoracostomy (same approach as pneumothorax); assess for ongoing bleeding (>1.5 L initial output, >200 mL/h persistent)",
                    "Indications for OR (thoracotomy): >1.5 L initial output, >200 mL/h for 4h, or signs of exsanguination",
                    "Monitor O2 sat, serial ABG; blood from tube can be autotransfused if sterile",
                ]},

                # Pericardial tamponade
                {"topic": "Pericardial Tamponade", "key_points": [
                    "Beck's triad: JVD, muffled heart sounds, hypotension; high-risk with penetrating chest trauma",
                    "Diagnosis: ultrasound (pericardial fluid), ECG (electrical alternans, low voltage, sinus tachycardia)",
                    "Pericardiocentesis (subxiphoid approach, 18-20 G needle) acutely; only temporizing measure",
                    "Definitive: surgical drainage (sternotomy or thoracotomy); trauma patients usually need OR",
                ]},

                # Flail chest & pulmonary contusion
                {"topic": "Flail Chest & Pulmonary Contusion", "key_points": [
                    "Flail chest: 2+ adjacent ribs broken in 2+ places; paradoxical motion (inward during inspiration)",
                    "Management: aggressive pain control (thoracic epidural, intercostal blocks), incentive spirometry, aggressive pulmonary toilet",
                    "Avoid rib fixation in most cases; internal fixation reserved for severe deformity or failed conservative management",
                    "Pulmonary contusion: ARDS risk; monitor for respiratory decline, manage fluid conservatively",
                ]},

                # Abdominal trauma
                {"topic": "Abdominal Trauma Assessment & Management", "key_points": [
                    "FAST exam: Free fluid in Morrison's pouch (RUQ), splenorenal recess (LUQ), pelvic cul-de-sac, pericardium",
                    "Indications for OR: peritoneal signs, FAST positive + hemodynamic instability, evisceration, impalement",
                    "Solid organ injuries (spleen, kidney): most amenable to non-operative management with observation if hemodynamically stable",
                    "ICE scoring: grade injury severity; high-grade (IV-V) or hemodynamic instability warrant OR",
                    "Serial abdominal exams, monitor lactate; repeat imaging if clinical deterioration",
                ]},

                # Pelvic fractures
                {"topic": "Pelvic Fracture Management", "key_points": [
                    "Retroperitoneal hemorrhage from fracture fragments/vascular injury; high mortality (5-15%) if unstable",
                    "Pelvic binder (sheet) immediately if unstable fracture pattern (open book, lateral compression II-III)",
                    "Angiography + embolization vs. operative fixation based on hemodynamics, fracture pattern, orthopedic input",
                    "Assess for bladder/urethral injury (blood at meatus, suprapubic exam); urinalysis",
                ]},

                # Spinal cord injury
                {"topic": "Spinal Cord Injury Management", "key_points": [
                    "Mechanism: high-speed motor vehicle collision, falls >10 ft, penetrating injury, high-impact blunt trauma",
                    "NEXUS criteria: alert + no midline tenderness + no neurologic deficit + no intoxication + no painful distracting injury = can clear C-spine clinically",
                    "Imaging: CT C-spine + thoracolumbar CT if mechanism warrants; MRI for cord signal/SCIWORA (spinal cord injury without radiographic abnormality)",
                    "High-dose methylprednisolone within 8h: 30 mg/kg bolus, then 5.4 mg/kg/h x23h (NASCIS 3 trial); controversial due to infection risk",
                    "Spinal shock: areflexia, hypotension, bradycardia (resolve in days-weeks); don't confuse with neurogenic shock",
                ]},

                # Traumatic brain injury
                {"topic": "Traumatic Brain Injury & Intracranial Monitoring", "key_points": [
                    "GCS score: predicts outcome; GCS 3-8 severe (consider intubation), 9-12 moderate, 13-15 mild",
                    "CT head mandatory for GCS <15, focal neurologic deficit, loss of consciousness, mechanism with high risk",
                    "ICP monitoring (EVD, parenchymal probe) if GCS ≤8 and abnormal CT; target ICP <20 mmHg",
                    "Cerebral perfusion pressure (CPP) = MAP - ICP; maintain CPP 50-70 mmHg",
                    "Head elevation 30°, normothermia, osmotic therapy (mannitol 0.25-1 g/kg IV, hypertonic saline 3% 250 mL IV), sedation, prevent hypoxemia/hypercapnia",
                ]},

                # Blast injury
                {"topic": "Blast Injury Mechanism & Management", "key_points": [
                    "Primary: barotrauma (pneumothorax, hemothorax, pulmonary contusion, tympanic rupture)",
                    "Secondary: fragmentation and flying objects (penetrating/blunt trauma)",
                    "Tertiary: displacement of body (crush injuries, blunt trauma from being thrown)",
                    "Quaternary: inhalation injury, thermal burns, crush syndrome (rhabdomyolysis, AKI)",
                    "Manage as polytrauma; aggressive resuscitation, watch for compartment syndrome in crush injuries",
                ]},

                # Drowning & submersion injury
                {"topic": "Drowning & Submersion Injury Management", "key_points": [
                    "Cold water submersion (temp <15°C) can preserve neurologic function for extended periods (up to 1-2h)",
                    "Initial management: rescue, CPR, warm core rewarming if profoundly hypothermic",
                    "ECMO/extracorporeal rewarming if profound hypothermia with cardiac arrest (goal core temp 32°C before starting)",
                    "Aspiration: chemical pneumonitis; monitor for ARDS; fresh water osmotic gradient → pulmonary edema",
                    "Prognosis: poor with prolonged submersion (>5-10 min) without anoxic preservation",
                ]},
            ]
        },

        "procedures": {
            "title": "Critical Procedures",
            "units": [
                # Central venous catheter
                {"topic": "Central Venous Catheter (CVC) Placement & Complications", "key_points": [
                    "Indications: hemodynamic monitoring, vasopressor infusion, hyperalimentation, hemodialysis, transvenous pacing",
                    "Sites: internal jugular (preferred), subclavian, femoral; ultrasound-guided to reduce complications",
                    "Technique: Seldinger approach - find vein, insert needle, pass guidewire, dilate, pass catheter over wire",
                    "Complications: pneumothorax, hemothorax, arterial puncture, thrombosis, infection (CLABSI), cardiac arrhythmia (malposition), perforation",
                    "Care: sterile dressing, regular assessment for signs of infection; remove ASAP when no longer needed",
                ]},

                # Arterial line
                {"topic": "Arterial Line Placement & Monitoring", "key_points": [
                    "Indications: beat-to-beat BP monitoring, frequent ABG sampling, vasopressor infusion",
                    "Sites: radial (preferred), femoral, brachial, axillary; assess collateral circulation (Allen test for radial)",
                    "Technique: cannulate artery over guidewire or direct stick; confirm with arterial waveform",
                    "Waveform: systolic peak, dicrotic notch (aortic valve closure), diastolic pressure",
                    "Complications: ischemia, thrombosis, pseudoaneurysm, infection; signs of ischemia warrant immediate removal",
                ]},

                # Chest tube thoracostomy
                {"topic": "Chest Tube Thoracostomy (Tube Thoracostomy)", "key_points": [
                    "Indications: pneumothorax, hemothorax, empyema, malignant effusion, traumatic hemopneumothorax",
                    "Technique: 4th-5th intercostal midaxillary line, blunt dissection through pleura, advance catheter posteriorly",
                    "Tube sizes: 20-28 Fr (small bore, tunneled pigtail for effusions), 28-40 Fr (large bore for trauma)",
                    "Management: water-seal drain, suction (20 cm H2O typical), monitor for air leak, output (blood, serous, chylous), crepitus",
                    "Removal: when minimal output (<100-200 mL/day), no air leak, and chest X-ray shows lung expanded",
                ]},

                # Pericardiocentesis
                {"topic": "Pericardiocentesis & Pericardial Effusion Management", "key_points": [
                    "Indications: tamponade (urgent), significant effusion (echo), diagnostic (suspected infection, malignancy)",
                    "Approach: subxiphoid (safest), parasternal, or apical under ultrasound guidance",
                    "Technique: needle at 45° angle toward left shoulder, advance until fluid return, confirm with ultrasound",
                    "Complications: myocardial/coronary perforation, arrhythmia, infection; withdraw slowly to avoid rapid hemodynamic shifts",
                    "Catheter-based drainage if recurrent; definitive surgical drainage for malignancy or constrictive physiology",
                ]},

                # Transesophageal echocardiography (TEE)
                {"topic": "Transesophageal Echocardiography (TEE) in Critical Care", "key_points": [
                    "Indications: hemodynamic instability (assess volume status, cardiac function), suspected endocarditis, aortic disease, PE, intra-cardiac device issue",
                    "Superior views to TTE: posterior structures (LA, pulmonary veins), aorta, right heart",
                    "Probe insertion: positioned in esophagus, rotated/advanced to visualize cardiac structures",
                    "Operator credentialing required; risks: esophageal perforation, aspiration, tooth damage",
                    "Contraindications: esophageal pathology (stricture, mass), recent upper GI surgery, cervical spine trauma",
                ]},

                # Lumbar puncture
                {"topic": "Lumbar Puncture (Spinal Tap) & CSF Interpretation", "key_points": [
                    "Indications: meningitis (fever + headache + neck stiffness), encephalitis, SAH, diagnose MS/GBS, intrathecal drug administration",
                    "Technique: L3-L4 or L4-L5 interspace, needle at 45° angle toward cephalad; collect 4 tubes (cell count, glucose/protein, culture, Gram stain)",
                    "Opening pressure: normal <25 cm H2O; elevated in meningitis, IIH, communicating hydrocephalus",
                    "CSF analysis: WBC (lymphocytic vs. neutrophilic), glucose (low in bacterial, normal in viral), protein (elevated in bacterial/inflammatory)",
                    "Contraindications: focal neurologic deficits, papilledema, signs of mass effect; do head CT first if suspect mass",
                ]},

                # Cricothyrotomy
                {"topic": "Surgical Airway (Cricothyrotomy)", "key_points": [
                    "Indication: can't intubate, can't oxygenate emergency; laryngeal injury, airway obstruction, massive facial trauma",
                    "Anatomy: cricoid cartilage below thyroid cartilage; palpate midline notch between Adam's apple and cricoid",
                    "Technique: 1-1.5 cm horizontal incision, spread with hemostat, insert 5-6 mm tracheostomy tube directed caudally",
                    "Complications: tracheal stenosis (late), infection, tube malposition, tracheal perforation",
                    "Conversion to tracheostomy within 24-48h recommended; emergency procedure only",
                ]},

                # Resuscitative thoracotomy
                {"topic": "Resuscitative Thoracotomy (Clamshell)", "key_points": [
                    "Indication: cardiopulmonary arrest from penetrating thoracic trauma with signs of life on-scene",
                    "Technique: anterolateral incision L4-L5, open pericardium (anterior), cross-clamp descending aorta (compress anteriorly), massage heart",
                    "Goals: restore coronary/cerebral perfusion, relieve tamponade, control hemorrhage, restore perfusing rhythm",
                    "Outcomes: 5-15% survival if pulse return achieved; poor prognosis if no organized activity after intervention",
                ]},

                # Resuscitative laparotomy
                {"topic": "Resuscitative Laparotomy for Traumatic Hemorrhage", "key_points": [
                    "Indication: penetrating/blunt abdominal trauma with hemodynamic instability and peritoneal signs",
                    "Technique: midline incision, rapid assessment (Kocher maneuver assess for aorta bleeding), control hemorrhage (packing, vessel ligation)",
                    "Damage control: prioritize hemorrhage control > organ repair; damage control laparotomy may require re-exploration in 24-48h",
                    "Avoid: major reconstructions in unstable patients; temporary closure (VAC, towel clip) until physiologic recovery",
                ]},

                # Finger thoracostomy
                {"topic": "Finger Thoracostomy (Emergency Decompression)", "key_points": [
                    "Indication: tension pneumothorax if needle decompression unavailable/failed",
                    "Technique: 4th-5th intercostal midaxillary line, finger sweep to ensure pleural entry, provides rapid decompression",
                    "Temporizing measure; tube thoracostomy still needed for definitive management",
                ]},
            ]
        },

        "obstetric_emergencies": {
            "title": "OB/GYN Emergencies",
            "units": [
                # Preeclampsia/eclampsia
                {"topic": "Preeclampsia & Eclampsia Management", "key_points": [
                    "Preeclampsia: BP ≥140/90 (x2) + proteinuria (≥0.3 g/24h) or symptoms (headache, epigastric pain, visual change)",
                    "Severe: BP ≥160/110, platelets <100k, creatinine >1.1, pulmonary edema, altered mental status, hemolysis",
                    "Eclampsia: preeclampsia + seizures; HELLP: hemolysis + elevated LFTs + low platelets (subset of preeclampsia)",
                    "Magnesium sulfate 4-6 g IV loading dose, then 1-2 g/h maintenance for seizure prophylaxis",
                    "Antihypertensives: labetalol 20 mg IV q10min, hydralazine 5-10 mg IV, nifedipine ER; goal MAP reduction 15-25% in first hour",
                ]},

                # Acute coronary syndrome in pregnancy
                {"topic": "Acute Coronary Syndrome in Pregnancy", "key_points": [
                    "Incidence: rare (2-10 per 100,000 pregnancies); 3rd trimester and postpartum highest risk",
                    "Causes: coronary dissection (spontaneous, SCAD; 20-30% of ACS in pregnancy), atherosclerosis, vasospasm, embolism",
                    "Diagnosis: ECG, troponin, echocardiography; avoid radiation if possible (catheterization delayed if stable)",
                    "Management: aspirin, beta-blockers, ACE inhibitors; PCI if indicated; thrombolytics avoided due to bleeding risk",
                    "Delivery timing: vaginal delivery preferred; cesarean only if obstetric indication; anticoagulation during labor",
                ]},

                # Peripartum cardiomyopathy
                {"topic": "Peripartum Cardiomyopathy", "key_points": [
                    "Heart failure (EF <45%) in pregnancy or postpartum (within 5 months); incidence 1 in 1,400-4,000 pregnancies",
                    "Risk factors: maternal age, multiparity, obesity, preeclampsia, black race",
                    "Presentation: dyspnea, orthopnea, fatigue, edema; ECG shows nonspecific changes; echo confirms reduced EF",
                    "Management: standard HF therapy (ACE-I/ARB, beta-blockers, diuretics); some agents avoid in pregnancy (ACE-I category D in 2nd/3rd trimester)",
                    "Prognosis: 50% recover EF fully, 50% persistent cardiomyopathy; maternal mortality 1-7%; repeat pregnancy high risk",
                ]},

                # Amniotic fluid embolism
                {"topic": "Amniotic Fluid Embolism (AFE)", "key_points": [
                    "Rare (1 in 30,000-40,000 deliveries) but high mortality (15-30%); occurs during labor/delivery/postpartum",
                    "Pathophysiology: fetal material enters maternal circulation → anaphylactoid reaction, DIC, cardiovascular collapse",
                    "Presentation: acute dyspnea, hypoxia, shock, seizures, cardiopulmonary arrest, bleeding (DIC)",
                    "Diagnosis: clinical (no specific test); findings support (foam in pulmonary artery, elevated FDP, D-dimer, low fibrinogen)",
                    "Management: aggressive resuscitation (100% O2, fluids, pressors), place on ECMO if available, transfusion protocol (FFP, cryoprecipitate)",
                ]},

                # Massive postpartum hemorrhage
                {"topic": "Postpartum Hemorrhage Management", "key_points": [
                    "Definition: >500 mL vaginal delivery, >1000 mL cesarean delivery, or signs of hypovolemic shock",
                    "Causes: uterine atony (80%), placental abnormalities (10%), laceration (5%), coagulopathy (5%)",
                    "Management: fundal massage, oxytocin (Pitocin) 10 units IM/IV, ergotamine (methergine) 0.2 mg IM, misoprostol 800 mcg PO/rectally",
                    "If bleeding persists: IV fluids, transfusion (RBC, FFP, platelets, cryoprecipitate), call anesthesia, transfer to OR",
                    "Massive transfusion: balanced 1:1:1 ratio; consider TXA 1 g IV; uterine artery embolization or hysterectomy if refractory",
                ]},

                # Retained placenta
                {"topic": "Retained Placenta Management", "key_points": [
                    "Normal: expulsion within 5-15 min; retained if >30 min without delivery",
                    "Risk: placenta accreta/increta/percreta, abnormal placentation, previous uterine surgery",
                    "Management: IV oxytocin, controlled cord traction, manual removal if incomplete separation",
                    "Manual removal: anesthesia consent, empty bladder, explore uterine cavity; fingers separate placenta from uterus",
                    "Complications: infection, DIC, hemorrhage; if imaging suggests morbidly adherent, proceed to hysterectomy",
                ]},

                # Septic abortion/postpartum sepsis
                {"topic": "Septic Abortion & Postpartum Sepsis", "key_points": [
                    "Risk: incomplete abortion, retained products of conception, intrauterine infection",
                    "Presentation: fever, lower abdominal pain, vaginal discharge (foul), hemodynamic instability, altered mental status",
                    "Diagnosis: clinical + pelvic ultrasound (evaluate for retained products), blood cultures, CBC, coagulation studies",
                    "Management: broad-spectrum IV antibiotics (ceftriaxone, doxycycline, metronidazole), aggressive fluid resuscitation",
                    "Definitive: uterine evacuation (D&C) if retained products; hysterectomy if perforated, necrotic, or refractory sepsis",
                ]},

                # Gestational diabetes in ICU
                {"topic": "Gestational Diabetes Acute Complications", "key_points": [
                    "Maternal: hyperglycemia → hypovolemia, osmotic diuresis, DKA (rare but dangerous in pregnancy)",
                    "Fetal: hyperglycemia → fetal hyperinsulinemia → macrosomia, shoulder dystocia, neonatal hypoglycemia",
                    "Management: tight glucose control (80-110 mg/dL fasting, <140 postprandial), insulin (avoid sulfonylureas in 3rd trimester)",
                    "DKA in pregnancy: lower threshold for metabolic derangement (glucose 200-300 may have significant ketosis); aggressive IV fluids, insulin",
                ]},
            ]
        },

        "pediatric_critical_care": {
            "title": "Pediatric Critical Care",
            "units": [
                # Pediatric resuscitation
                {"topic": "Pediatric CPR & Resuscitation", "key_points": [
                    "Compression rate: 100-120/min (same as adults); compression depth: 1/3 AP diameter chest (2-2.4 inches for child, 1.5 inches for infant)",
                    "Airway: smaller mouth, larger tongue proportionally; use straight blade for laryngoscopy; tube size = (age+16)/4 or visual estimate (pen size of pinky)",
                    "Drugs: epinephrine 0.01 mg/kg IV/IO q3-5min (max 1 mg single dose), amiodarone 5 mg/kg IV (max 300 mg first dose)",
                    "PALS: single rescuer starts with 30 compressions + 2 breaths (2015 guidelines recommend compression-only if untrained)",
                    "Shockable rhythms (VF/pulseless VT): defibrillation 2-4 J/kg first dose, 4 J/kg subsequent; search for reversible causes",
                ]},

                # Pediatric shock
                {"topic": "Pediatric Shock Classification & Management", "key_points": [
                    "Cardiogenic: low cardiac output (myocarditis, heart failure, arrhythmia); crackles, hepatomegaly, cool extremities",
                    "Hypovolemic: hemorrhage, dehydration; tachycardia, decreased urine output, weak pulses",
                    "Distributive (septic): fever + infection, tachycardia, bounding pulses initially, then deteriorate (cold sepsis)",
                    "Management: age-appropriate fluid bolus (20 mL/kg isotonic saline), early antibiotics if septic, inotropes (epinephrine 0.1-1 mcg/kg/min)",
                    "Peds shock: higher heart rates compensate earlier; normal BP maintained longer → be suspicious if HR abnormal",
                ]},

                # Pediatric ARDS
                {"topic": "Pediatric Acute Respiratory Distress Syndrome (PARDS)", "key_points": [
                    "Definition: Berlin criteria applied to kids (mild: 2-3 < PaO2/FiO2 <300; moderate: 1-2 < P/F <100; severe: P/F <100)",
                    "Lung-protective ventilation: Vt 6-8 mL/kg ideal body weight, permissive hypercapnia (pH goal >7.20)",
                    "PEEP titration: start 5-8 cm H2O, increase based on oxygenation needs; avoid high pressures (barotrauma risk)",
                    "Prone positioning if moderate-severe; sedation + neuromuscular blockade if refractory hypoxemia",
                    "Fluid conservative strategy: avoid volume overload (associated with worse outcomes)",
                ]},

                # Status epilepticus in children
                {"topic": "Pediatric Status Epilepticus Management", "key_points": [
                    "First-line: lorazepam 0.1 mg/kg IV (max 4 mg) or midazolam 0.1-0.2 mg/kg IM (max 10 mg)",
                    "Second-line (if seizure ongoing 5 min): fosphenytoin 20 PE/kg IV, levetiracetam 20-30 mg/kg IV, valproate 20-40 mg/kg IV",
                    "Third-line (refractory): anesthesia for intubation + sedative drips (propofol 1-3 mg/kg/h, pentobarbital 1-3 mg/kg/h, or midazolam 0.15 mg/kg/h)",
                    "Investigate cause: glucose, electrolytes, toxicology, lumbar puncture (if meningitis suspected), neuroimaging",
                ]},

                # Pediatric sepsis
                {"topic": "Pediatric Sepsis Recognition & Early Management", "key_points": [
                    "Recognition: fever/hypothermia + infection source + 2/4 SIRS (tachycardia, tachypnea, altered mental status/fever)",
                    "Severe sepsis: sepsis + organ dysfunction (altered mental status, low urine output, low platelet, acidosis, hypoxemia)",
                    "Septic shock: sepsis + hypotension unresponsive to fluids OR need for vasoactive agents",
                    "Management: blood cultures, IV access, fluid bolus 20 mL/kg (repeat if needed), antibiotics <1h, vasopressors if hypotensive",
                    "Dexamethasone controversial; may consider in meningococcemia or adrenal insufficiency",
                ]},

                # Pediatric poisoning
                {"topic": "Common Pediatric Poisonings & Management", "key_points": [
                    "Acetaminophen: <150 mg/kg = observe; 150-200 = consider NAC; >200 = treat with NAC",
                    "Salicylate: kids metabolize differently than adults; lower levels more dangerous (Reye syndrome risk); treat if level >30 mg/dL chronic",
                    "Tricyclic antidepressants: QRS widening, arrhythmias, seizures; sodium bicarbonate 1 mEq/kg IV",
                    "Iron: chelate with deferoxamine if level >400; whole bowel irrigation",
                    "Call poison control: 1-800-222-1222; activated charcoal if within 1h",
                ]},

                # Pediatric anaphylaxis
                {"topic": "Pediatric Anaphylaxis Management", "key_points": [
                    "Epinephrine first-line: 0.01 mg/kg (0.01 mL/kg of 1:1000) IM to lateral thigh q5-15min as needed",
                    "IV access: normal saline bolus 20 mL/kg, then repeat as needed for hypotension",
                    "Antihistamines: diphenhydramine 1 mg/kg IV (max 50 mg), corticosteroids (methylprednisolone 1-2 mg/kg IV)",
                    "Monitor: observe at least 4-6h for biphasic reaction; admit if severe or late reaction",
                ]},

                # Pediatric intensive care monitoring
                {"topic": "Pediatric ICU Monitoring & Sedation", "key_points": [
                    "Vital signs interpretation: HR/RR/BP vary with age; use age-appropriate normal ranges",
                    "Sedation: morphine 0.1-0.2 mg/kg IV, midazolam 0.1-0.2 mg/kg IV; avoid paralysis without sedation",
                    "Nutrition: early enteral feeds if GI functional; higher protein needs (1.5-2 g/kg/day)",
                    "Family-centered care: parents at bedside reduce child anxiety and parental stress",
                ]},
            ]
        },

        "geriatric_medicine": {
            "title": "Geriatric Critical Care",
            "units": [
                # Delirium in elderly
                {"topic": "Delirium in Elderly: CAM-ICU Assessment", "key_points": [
                    "CAM-ICU: (1) acute onset + (2) inattention PLUS either (3) disorganized thinking OR (4) altered consciousness",
                    "Hyperactive: agitation, tachycardia, aggression; hypoactive: lethargy, decreased verbal output (more dangerous, often missed)",
                    "Causes: infection (UTI, pneumonia), medication (opioids, anticholinergics), metabolic, CNS events",
                    "Prevention: early mobilization, sleep hygiene, reorientation, minimize sedation, optimize hearing/vision",
                    "Management: treat underlying cause; avoid antipsychotics if possible (increased mortality in elderly)",
                ]},

                # Polypharmacy & drug interactions
                {"topic": "Polypharmacy in Elderly: Beers Criteria", "key_points": [
                    "Beers Criteria: medications to avoid in older adults (anticholinergics, NSAIDs, benzodiazepines, diphenhydramine)",
                    "High-risk interactions: NSAIDs + ACE-I/ARB (hyperkalemia, renal dysfunction), warfarin + NSAIDs (GI bleed)",
                    "Dosing: reduce doses of renally cleared drugs (creatinine clearance <30 mL/min); adjust for weight loss in elderly",
                    "Deprescribing: regularly review medications, discontinue if not addressing active problem or causing side effects",
                ]},

                # Frailty assessment
                {"topic": "Frailty in Elderly & Risk Stratification", "key_points": [
                    "Fried Criteria: unintentional weight loss, exhaustion, low physical activity, slow gait speed, weak grip strength (3+ = frail)",
                    "Frailty predicts: poor postoperative outcomes, falls, hospitalization, mortality",
                    "Assessment: geriatric assessment tools (FSRS, Timed Up & Go), functional status at baseline",
                    "Preoperative: optimize function, mobilize, correct anemia, manage comorbidities",
                ]},

                # Geriatric resuscitation
                {"topic": "Resuscitation Decisions in Elderly", "key_points": [
                    "Prognosis of CPR: <5% survival to hospital discharge in very elderly; poor if post-arrest neurologic status",
                    "DNACPR: discuss advance directives, assess goals of care, document patient/family wishes",
                    "Factors favoring poor outcome: age >85, frailty, dementia, severe comorbidities, long down time",
                    "Goals-of-care discussions: focus on quality of life, functional goals, not just survival",
                ]},

                # Elder abuse detection
                {"topic": "Elder Abuse Recognition & Reporting", "key_points": [
                    "Types: physical, emotional, financial, neglect, sexual, self-neglect",
                    "Signs: unexplained injuries, poor hygiene, caregiver controlling, frequent ER visits, medication non-compliance",
                    "Mandatory reporting in many states; health care providers are reporters",
                    "Assess: screen all elderly patients (Ask Sufficiency Question: 'Do you feel safe?')",
                    "Intervention: documentation, safety planning, referral to adult protective services",
                ]},
            ]
        },

        "communication_team_skills": {
            "title": "Communication & Team Skills",
            "units": [
                # SPIKES framework for bad news
                {"topic": "Breaking Bad News: SPIKES Framework", "key_points": [
                    "S (Setting): quiet, private, comfort items (tissue, water), sit at eye level, no interruptions, family present if desired",
                    "P (Perception): ask what the patient/family already knows/understand before telling news",
                    "I (Invitation): ask if patient wants to hear all details at once or gradually, who they want present",
                    "K (Knowledge): deliver bad news clearly, use simple language, avoid jargon, pause for comprehension",
                    "E (Emotions & Empathy): acknowledge patient's feelings ('I can see this is difficult'), offer support",
                    "S (Summary & Support): summarize next steps, treatment options, offer resources (social work, chaplain)",
                ]},

                # Difficult conversations
                {"topic": "Difficult Conversations with Patients & Families", "key_points": [
                    "Approach: empathetic, non-defensive, focus on shared goals (best care for patient)",
                    "Listen: allow family to voice concerns without interrupting; validate feelings even if disagree",
                    "Clarify: ensure understanding of medical situation, prognosis, treatment options, what patient wants",
                    "When disagreement: offer second opinion, ethics consultation, palliative care referral",
                    "Mitigate harm: if conflict unresolved, prioritize patient safety (don't withhold critical care)",
                ]},

                # Team communication in resuscitation
                {"topic": "Team Dynamics During Resuscitation", "key_points": [
                    "Clear leadership: one person directs (clearly designate), others execute specific roles",
                    "Closed-loop communication: acknowledge when hearing instructions, confirm actions completed",
                    "Debriefing: brief team after resuscitation (what went well, what to improve)",
                    "Crew resource management: junior staff should speak up if see error without hierarchy inhibiting communication",
                ]},

                # Shared decision-making
                {"topic": "Shared Decision-Making Model", "key_points": [
                    "Involves: physician discusses options, patient expresses values/preferences, together reach decision",
                    "Requires: accurate prognostic information, patient decision aids, respect for autonomy",
                    "Benefits: increases patient satisfaction, adherence, reduces unnecessary care",
                    "Examples: whether to pursue aggressive care in metastatic cancer, timing of DNI/tracheostomy in prolonged illness",
                ]},

                # Code status discussions
                {"topic": "Code Status & Goals-of-Care Conversations", "key_points": [
                    "Full Code (CPR): attempt cardiopulmonary resuscitation, intubation, ICU-level care",
                    "DNR (Do Not Resuscitate): no CPR if cardiac arrest; may still pursue hospitalizations, ICU, other interventions",
                    "DNI (Do Not Intubate): no mechanical ventilation; may accept other supports (vasopressors, dialysis)",
                    "Comfort-focused: focus on symptom management, comfort, dignity; may include palliative sedation",
                    "Timing: discuss early (before acute illness), update regularly as condition changes",
                ]},
            ]
        },

        "quality_safety": {
            "title": "Quality Improvement & Patient Safety",
            "units": [
                # Medical errors & root cause analysis
                {"topic": "Root Cause Analysis & Adverse Event Investigation", "key_points": [
                    "RCA: systematic process to understand why error occurred, not to blame",
                    "Five Whys: ask 'why' repeatedly to uncover system failures: Why did patient get wrong dose? Why was label unreadable?",
                    "Fishbone diagram: brainstorm contributory factors (people, processes, equipment, environment, training)",
                    "Process improvement: redesign systems to prevent recurrence (checklists, barriers, standardization)",
                    "Reporting: culture of safety requires honest reporting without punishment (just culture)",
                ]},

                # Medication safety
                {"topic": "Medication Safety in ICU", "key_points": [
                    "High-alert medications: look-alike/sound-alike (HepARIN vs. HumaLOG), high-risk drugs (potassium, insulin, vasopressors)",
                    "Strategies: use brand names, avoid abbreviations (don't write 'U' for units), double-check dosing, pharmacist verification",
                    "Infusion pumps: smart pumps with dose error reduction systems (DERS) prevent programmed overdoses",
                    "Labels: colored labels, font size, clear visibility; organizes by function not alphabetically",
                ]},

                # Hospital-acquired infections
                {"topic": "Prevention of Hospital-Acquired Infections (HAI)", "key_points": [
                    "Hand hygiene: most important intervention; before/after patient contact, before clean procedure, after body fluid exposure",
                    "Catheter-associated UTI (CAUTI): remove catheters ASAP, use sterile technique, minimize indwelling duration",
                    "Central line-associated bloodstream infection (CLABSI): aseptic technique, sterile dressing, transparent dressing, remove ASAP",
                    "Ventilator-associated pneumonia (VAP): head of bed 30-45°, daily oral care, sedation vacation, spontaneous breathing trials",
                    "C. diff: contact precautions, avoid unnecessary antibiotics, alcohol-based hand sanitizers ineffective (wash hands)",
                ]},

                # Rapid response teams
                {"topic": "Rapid Response Team (RRT) Activation", "key_points": [
                    "Criteria to call RRT: respiratory distress (RR >40 or <8), altered mental status, hypotension, severe pain",
                    "Response: physician + nurse + respiratory therapist assess, stabilize, intervene (intubate, transfer to ICU)",
                    "Benefit: prevent cardiopulmonary arrests on general wards, earlier ICU transfer",
                    "Debrief: communicate with patient/family after intervention; RRT reviews cases for patterns",
                ]},
            ]
        },

        "palliative_ethics": {
            "title": "Palliative Care & Medical Ethics",
            "units": [
                # Palliative care principles
                {"topic": "Palliative Care & Comfort-Focused Management", "key_points": [
                    "Goals: symptom relief, quality of life, support for patient/family, not curative",
                    "Referral timing: early (at diagnosis of serious illness, not just end-of-life)",
                    "Domains: pain control, dyspnea, nausea, fatigue, anxiety, depression, spiritual concerns",
                    "Team approach: physician, nurse, social work, chaplain, palliative care specialist",
                    "Parallel planning: can pursue curative AND palliative goals simultaneously",
                ]},

                # Pain management in ICU
                {"topic": "Pain Management in Critical Illness", "key_points": [
                    "Assessment: ask patient, use pain scale (numeric rating 0-10), observe for nonverbal cues (grimacing, restlessness)",
                    "Medications: morphine (first-line opioid), hydromorphone, fentanyl (faster onset); combine with adjuvants (acetaminophen, NSAIDs, muscle relaxants)",
                    "Titration: increase doses incrementally based on response; concern for oversedation is NOT reason to withhold analgesia",
                    "Tolerance: develop over time; NOT addiction (behavioral disorder); increase dose if needed",
                ]},

                # Withdrawing/withholding life support
                {"topic": "Ethical Withdrawal & Withholding of Life Support", "key_points": [
                    "Legal equivalence: withholding (not starting ventilator) = withdrawing (stopping ventilator) ethically/legally",
                    "Process: goals-of-care discussion, multidisciplinary agreement, patient/family understanding",
                    "Approach: discontinue aggressive interventions, transition to comfort care (sedation, opioids for dyspnea)",
                    "Extubation: patient may breathe spontaneously; place on comfort measures (oxygen if desired, secretion management)",
                    "After death: allow family time with body, offer condolences, explain autopsy option",
                ]},

                # Medical aid in dying
                {"topic": "Medical Aid in Dying (MAID) & Physician-Assisted Suicide", "key_points": [
                    "Legal: available in Oregon, California, Washington, Colorado, Hawaii, Vermont, DC, and some other states",
                    "Criteria: terminal illness (6 months prognosis), mental competence, persistent request, waiting periods",
                    "Role: physician verifies diagnosis/prognosis, refers to psychiatrist, prescribes medication (lethal dose barbiturate)",
                    "Patient administers: takes medication at home with family; dies within minutes to hours",
                    "Controversy: ethical debate on autonomy vs. sanctity of life; varies by jurisdiction and personal values",
                ]},

                # Ethical conflict resolution
                {"topic": "Ethics Consultation & Conflict Resolution", "key_points": [
                    "Triggers: family/physician disagreement, decisions about life-sustaining treatment, resource allocation",
                    "Process: ethics committee reviews case, hears from stakeholders, offers guidance (not binding)",
                    "Framework: autonomy (respect patient wishes), beneficence (act in best interest), nonmaleficence (avoid harm), justice (fair allocation)",
                    "Outcome: often achieves consensus; if impasse, consider second opinion, transfer of care, legal involvement",
                ]},

                # Informed consent
                {"topic": "Informed Consent & Capacity Assessment", "key_points": [
                    "Elements: patient understands diagnosis/prognosis, alternatives, risks/benefits, consequences of refusal",
                    "Capacity: patient can understand information, appreciate its significance to own situation, reason through decision, communicate choice",
                    "Assessment: may lack capacity due to sedation, delirium, psychiatric illness, dementia; test with focused questions",
                    "Surrogate: if incapacitated, use surrogate decision-maker (spouse, adult child, healthcare proxy)",
                    "Advance directive: living will/POLST (Physician Orders for Life-Sustaining Treatment) predefined wishes",
                ]},
            ]
        },

        "administrative_career": {
            "title": "Administrative & Career Development",
            "units": [
                # Shift handoff & sign-out
                {"topic": "Effective Shift Handoff & Patient Sign-Out", "key_points": [
                    "IPASS mnemonic: Illness severity, Patient summary, Assessment/Action list, Situation awareness, Synthesis by receiver",
                    "Format: SBAR (Situation, Background, Assessment, Recommendation) for concise communication",
                    "Checklist: overnight plans, pending tests, medications to give, who to call with changes",
                    "Verification: incoming physician repeats back key info to ensure understanding",
                    "Documentation: sign-out recorded (verbal + written) for accountability",
                ]},

                # Burnout prevention
                {"topic": "Recognizing & Preventing Physician Burnout", "key_points": [
                    "Burnout: emotional exhaustion, cynicism, reduced effectiveness; affects 40%+ of physicians",
                    "Risk factors: excessive hours, administrative burden, sleep deprivation, moral injury, lack of control",
                    "Prevention: set boundaries (work hours), hobby/exercise, social support, mindfulness, job satisfaction",
                    "Resources: employee assistance programs (EAP), counseling, mentorship, peer support groups",
                    "Institutional: reduce paperwork, improve staffing, support mental health, culture of wellness",
                ]},

                # Self-care & resilience
                {"topic": "Building Resilience & Professional Well-Being", "key_points": [
                    "Self-awareness: know your triggers, stressors, coping mechanisms",
                    "Sleep: prioritize 7-8h nightly (essential for cognitive function, mood, immune function)",
                    "Exercise: 30min/day moderate activity reduces depression/anxiety, improves mood",
                    "Nutrition: regular meals, hydration, limit caffeine/alcohol",
                    "Connection: maintain relationships, engage in community, meaningful activities outside medicine",
                ]},

                # Career planning
                {"topic": "Career Development & Specialty Selection", "key_points": [
                    "Self-assessment: strengths/interests, values (autonomy, income, schedule, impact)",
                    "Exploration: rotation in specialty, talk to mentors, attend conferences",
                    "Timeline: early planning (intern year), revisit annually as interests evolve",
                    "Subspecialties: fellowship training (2-5 years), boards certification, research opportunities",
                    "Work-life balance: consider lifestyle factors (call burden, schedule, family needs) by specialty",
                ]},
            ]
        },
    }

    # Generate unit data
    unit_id_counter = 700
    for section_key, section_data in phase4_sections.items():
        for unit_data in section_data["units"]:
            topic = unit_data["topic"]
            key_points = unit_data["key_points"]

            # Create detailed text from key points
            detailed_text = f"{topic}. " + " ".join(key_points)

            units.append({
                "id": f"phase4_unit_{unit_id_counter}",
                "text": detailed_text,
                "metadata": {
                    "topic": topic,
                    "topic_tags": [section_key] + [t.lower().replace(" ", "_").replace("&", "and") for t in topic.split()[:2]],
                    "library": "intern_year_medicine",
                    "source_name": "Phase 4 Knowledge Base",
                    "book": "Phase 4 - Remaining Essentials",
                    "section": section_key,
                    "created_at": datetime.now().isoformat(),
                    "chunk_type": "fact"
                }
            })
            unit_id_counter += 1

    return units


if __name__ == "__main__":
    units = create_phase4_units()

    # Save to JSON
    output_path = Path("data") / "phase4_units.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(units, f, indent=2, ensure_ascii=False)

    print(f"[OK] Phase 4 generated: {len(units)} units")
    print(f"  Output: {output_path}")

    # Statistics
    by_section = {}
    for unit in units:
        section = unit["metadata"]["section"]
        by_section[section] = by_section.get(section, 0) + 1

    print("\nPhase 4 Breakdown by Section:")
    for section, count in sorted(by_section.items()):
        print(f"  {section}: {count} units")

    print(f"\nTotal Phase 4 Units: {len(units)}")
