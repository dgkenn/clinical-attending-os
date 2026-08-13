#!/usr/bin/env python3
"""
Comprehensive Phase 4 Expansion: 500-750 units

Expands on foundation with deeper coverage and additional topics.
"""

import json
from pathlib import Path
from datetime import datetime

def expand_phase4():
    """Generate comprehensive Phase 4 (500-750 units total)."""

    units = []

    # Load foundation units
    foundation_path = Path("data") / "phase4_units.json"
    with foundation_path.open("r", encoding="utf-8") as f:
        units = json.load(f)

    # Expand each section with additional depth
    expansions = {
        "toxicology_expanded": {
            "title": "Toxicology - Advanced Topics",
            "units": [
                # NAPQI (acetaminophen metabolite)
                "Acetaminophen metabolism: therapeutic acetaminophen conjugated with sulfate/glucuronic acid; overdose exhausts conjugation → NAPQI (N-acetyl-p-benzoquinoneimine) accumulates → glutathione depletion → liver cell death. Chronically malnourished, alcoholic, and elderly at higher risk.",

                # Toxidromes comparison
                "Toxidromes Quick Reference: Sympathomimetic (cocaine, amphetamine, pseudoephedrine): mydriasis, hypertension, tachycardia, hyperthermia. Anticholinergic (atropine, antihistamines): dry mouth, mydriasis, agitation, hyperthermia. Cholinergic (organophosphates, physostigmine): SLUDGE, miosis, bradycardia. Opioid (morphine, heroin): miosis, respiratory depression, hypothermia. Sedative (benzodiazepines, barbiturates): CNS depression, respiratory depression, hyporeflexia.",

                # Carbon monoxide poisoning
                "Carbon monoxide poisoning: colorless, odorless gas (combustion); binds hemoglobin with 200× affinity of oxygen → carboxyhemoglobin → tissue hypoxia. Symptoms: headache, confusion, syncope, cardiac arrhythmia, death. Diagnosis: carboxyhemoglobin level (normal <2%). Treatment: 100% oxygen (half-life 4-6 hours on room air, 1 hour on 100% O2, 30 min on hyperbaric oxygen 3 atm).",

                # Strychnine poisoning
                "Strychnine poisoning: blocks glycine inhibitory neurotransmitter → unopposed motor neuron firing → violent muscle contractions. Presentation: jaw clenching, opisthotonus (arched back), seizures, rhabdomyolysis. Treatment: benzodiazepines, neuromuscular blockade if intubated. Prognosis: 50% mortality historically; poor if seizures before treatment.",

                # Anticoagulation overdose
                "Warfarin/direct oral anticoagulant (DOAC) overdose: warfarin inhibits vitamin K-dependent clotting factors (II, VII, IX, X). Hemorrhage management: fresh frozen plasma (FFP) 10-15 mL/kg or prothrombin complex concentrate (PCC) 25-50 units/kg. Vitamin K1 5-10 mg slow IV (onset 12-24h, not immediate). Specific reversal agents: idarucizumab (Praxbind) for dabigatran, apixaban/rivaroxaban specific reversal agents.",

                # Heparin-induced thrombocytopenia (HIT)
                "Heparin-Induced Thrombocytopenia (HIT): paradoxical thrombosis despite anticoagulation; unfractionated heparin > low-molecular-weight heparin. HIT antibodies bind heparin-platelet factor 4 complex → platelet activation → thrombosis. Diagnosis: platelet count drop >50%, thrombotic event, timing (days 5-10). Management: stop heparin, switch to DTI (direct thrombin inhibitor: argatroban, dabigatran) or fondaparinux.",

                # Serotonin syndrome
                "Serotonin syndrome: excessive serotonergic activity from SSRIs, MAOIs, tramadol, linezolid, dextromethorphan, tryptophan. Triad: mental status change (agitation, confusion), autonomic instability (tachycardia, hypertension, hyperthermia), neuromuscular abnormalities (myoclonus, hyperreflexia, clonus). Treatment: benzodiazepines, cooling, cyproheptadine (serotonin antagonist) 12 mg loading then 2-8 mg q6h.",

                # Neuroleptic malignant syndrome (NMS)
                "Neuroleptic Malignant Syndrome (NMS): life-threatening reaction to antipsychotics (dopamine blockade). Tetrad: hyperthermia, muscle rigidity (lead pipe), altered mental status, autonomic dysfunction (labile BP/HR, diaphoresis). Treatment: stop offending agent, dantrolene 1 mg/kg IV q5-10min (max 10 mg/kg/day, reduces muscle metabolism), aggressive cooling, supportive care. Prognosis: 10% mortality if untreated, lower with dantrolene.",

                # Malignant hyperthermia (MH)
                "Malignant Hyperthermia (MH): genetic predisposition (ryanodine receptor mutation) → exposure to volatile anesthetics/succinylcholine → uncontrolled calcium release in muscle → hyperthermia, rhabdomyolysis, disseminated intravascular coagulation. Treatment: stop anesthetics, discontinue succinylcholine, dantrolene 2.5 mg/kg IV repeat q5min (max 10 mg/kg), aggressive cooling, monitor for complications (hyperkalemia, myoglobinuria).",

                # Transition metal toxicity
                "Heavy metal toxicity mechanisms: iron (oxidative stress via Fenton reaction), lead (neurotoxin, renal toxin), mercury (CNS effects), arsenic (arsenic trioxide → ARDS, dermatitis). Chelation strategy: iron (deferoxamine, deferasirox), lead/arsenic/mercury (DMSA, DMPS, EDTA). Timing critical: mobilizing metals can worsen toxicity; must antecedent to excretion.",

                # Pesticide toxicity
                "Pesticide toxicity beyond organophosphates: carbamates (SLUDGE, seizures), pyrethroids (paresthesia, ataxia, tremor), neonicotinoids (nicotine-like, CNS effects). Treatment: symptom-focused; carbamates respond to atropine/2-PAM like organophosphates but shorter duration.",
            ]
        },

        "trauma_expanded": {
            "title": "Trauma - Advanced Management",
            "units": [
                # Damage control orthopedics
                "Damage control orthopedics: unstable patient with multiple fractures → temporary stabilization (pelvic binder, traction splints, provisional fixation) avoiding prolonged OR time. Early total care reserved for physiologically stable patients. Principle: prioritize life-saving interventions (hemorrhage control, airway) over limb salvage initially.",

                # Rhabdomyolysis
                "Rhabdomyolysis: muscle breakdown → myoglobin release → acute kidney injury (tubular precipitation + direct toxicity). Sources: crush injury, prolonged immobilization, heat stress, statins, malignant hyperthermia. Management: aggressive IV hydration (goal urine output 200-300 mL/h), sodium bicarbonate (alkalinize urine prevents myoglobin precipitation), monitor CK, potassium, calcium.",

                # FAST extended exam
                "FAST (Focused Assessment with Sonography for Trauma) extended: standard 4 views (Morrison's, splenorenal, pelvic, pericardium) + extended views (right paracolic, left paracolic, pelvic longitudinal, pericardial transverse) increases sensitivity. Fluid detection in Morrison's pouch indicates 0.5-1 L free fluid in non-obese patients.",

                # Trauma triage guidelines
                "Massive transfusion protocol activation: varies by institution but generally triggered by (1) transfusion of 4+ units RBC in 1h, (2) anticipated need for >10 units, or (3) shock physiology (lactate >2 mmol/L, base deficit <-6). Guidelines favor 1:1:1 ratio of RBC:FFP:platelets over traditional 3:1 due to improved outcomes in massive transfusion.",

                # Mangled extremity score
                "Mangled Extremity Severity Score (MESS): predicts need for amputation. Components: injury severity (low, medium, high, massive), limb ischemia (none, <6h, >6h), shock, age. Score >7 associated with amputation; <7 may be salvageable with aggressive intervention. Not absolute; functional prognosis and patient preference factor in.",

                # Crush syndrome
                "Crush syndrome: entrapment with muscle injury → rhabdomyolysis → hyperkalemia (can cause cardiac arrest), acidosis, AKI. Risk after extraction: reperfusion injury from washout of metabolites. Management: pre-extraction IV fluids, monitor EKG for peaked T waves (hyperkalemia), calcium gluconate, insulin + glucose, sodium bicarbonate, prepare for hemodialysis.",

                # Intra-abdominal pressure monitoring
                "Intra-abdominal Hypertension (IAH) & Abdominal Compartment Syndrome (ACS): IAH (>12 mmHg) reduces organ perfusion; ACS (>20 mmHg with organ dysfunction) requires intervention. Measurement: transurethral catheter pressure (gold standard), transurethral bladder pressure. Management: fluid resuscitation optimization, neuromuscular blockade, sedation, decompressive laparotomy if ACS.",

                # Trauma-related coagulopathy
                "Acute Traumatic Coagulopathy: trauma → tissue damage → massive transfusion → platelet loss and coagulation factor dilution → DIC. Earlier recognition (INR, PTT, platelet, fibrinogen) compared to traditional PT/PTT improves outcomes. Thrombelastography (TEG) or rotational thromboelastometry (ROTEM) guides transfusion in real-time.",

                # Delayed bleeding complications
                "Delayed hemorrhage in trauma: Day 3-7 post-injury from anastomotic failure, missed injuries, sepsis, mesenteric ischemia. Higher mortality (30-50%) than immediate hemorrhage. Management: vigilance with serial exams, imaging for suspicious findings, low threshold for re-exploration.",

                # Necrotizing soft tissue infection
                "Necrotizing soft tissue infection post-trauma: rapid progression with systemic toxicity; high mortality (20-40%). Types: Type 1 (polymicrobial, most common), Type 2 (Group A Strep + Staph), Type 3 (marine/freshwater gram-negatives), Type 4 (fungal, rare). Treatment: antibiotics + immediate surgical debridement (may need multiple operations).",

                # Death from hemorrhage timing
                "Death from Hemorrhage - Temporal Distribution: '10-minute deaths' (exsanguination from massive hemorrhage), '1-hour deaths' (tension pneumothorax, tamponade, major vascular injury), '3-hour deaths' (head injury, spinal injury, organ injury with slower bleeding). Resuscitation most effective for 1-3 hour deaths; 10-minute deaths often unsalvageable.",
            ]
        },

        "procedures_expanded": {
            "title": "Procedures - Advanced Techniques",
            "units": [
                # REBOA
                "Resuscitative Endovascular Balloon Occlusion of the Aorta (REBOA): catheter-based aortic occlusion for non-compressible torso hemorrhage. Access: femoral artery, fluoroscopy (or bedside ultrasound blind), balloon positioned above/below aortic injury. Zone I (suprarenal) for intra-abdominal hemorrhage, Zone III (infrarenal) for lower extremity. Bridge to definitive OR control.",

                # Extracorporeal membrane oxygenation (ECMO)
                "ECMO basics: VV (veno-venous) for respiratory failure, VA (veno-arterial) for cardiopulmonary failure. Cannulation: femoral, internal jugular, or central lines. Blood pump maintains flow 4-6 L/min, oxygenator exchanges gas, heater maintains temperature. Complications: bleeding, infection, circuit thrombosis, limb ischemia (femoral), neurologic injury. Support duration: days to weeks.",

                # Resuscitative hysterotomy
                "Resuscitative Cesarean Hysterotomy (perimortem C-section): pregnant cardiac arrest, perform C-section at scene/ED (improve maternal cardiac output by 50%, fetus >20 weeks gestation). Technique: midline incision, incise uterus vertically, deliver baby, clamp cord, deliver placenta. Continue CPR with gravid uterus off IVC.",

                # Finger thoracotomy vs needle decompression
                "Needle decompression failures: may occur due to (1) needle not reaching pleura, (2) clogging, (3) tension persists. Finger thoracotomy more reliable for traumatic tension pneumothorax; insert finger 4-5 cm into chest wall to verify pleural entry before proceeding.",

                # Resuscitative laparotomy incisions
                "Resuscitative laparotomy incision options: midline (fastest, most extensile access), left anterolateral (if need aortic cross-clamp), right subcostal (hepatic control, less common). Midline supraumbilical incision within 3 minutes for hemorrhage control is priority over cosmesis.",

                # Clamshell thoracotomy
                "Clamshell (bilateral anterior thoracotomy): provides access to all mediastinal structures. Incision: bilateral anterolateral 4th-5th space with transverse sternal division. Advantage: better than left anterolateral alone for accessing right pleura/vessels. Resuscitative thoracotomy technique variation.",

                # Finger sweep airway clearance
                "Finger sweep for airway obstruction: last-ditch effort if can't ventilate, can't intubate. Blind finger sweep only if foreign body visible or in suspected choking. Avoid in children (risk of impaction). Confirm relief before proceeding to other airway interventions.",

                # Cricoid pressure (controversial)
                "Cricoid pressure (Sellick maneuver): applied during RSI to prevent aspiration; controversial—may impair visualization, can be incomplete occlu sion. Current evidence suggests selective use (recommend against routine); some favor gentle cricoid, then release if impairs view.",

                # Bougie introduction
                "Bougie (gum-elastic bougie) for difficult intubation: 10 Fr bougie passed to trachea blindly or with partial visualization, then ETT railroaded over bougie. Reduces failed intubations in difficult anatomy. Confirm position with 'hold-up' (bougie catches at right mainstem bronchus ~27-30 cm).",

                # CPAP/BiPAP in ED
                "CPAP/BiPAP non-invasive ventilation: avoids intubation for respiratory distress if conscious, cooperative, and no airway concerns. Uses: pulmonary edema (CPAP reduces afterload), asthma/COPD exacerbation. Risk: delays intubation if patient tires; have intubation equipment ready.",
            ]
        },

        "pediatric_expanded": {
            "title": "Pediatric Critical Care - Advanced",
            "units": [
                # Congenital heart disease emergencies
                "Patent ductus arteriosus (PDA) in premature infant: keep duct open (prostaglandin E1 0.05-0.1 mcg/kg/min) for cyanotic heart disease dependent on PDA (Tetralogy of Fallot, transposition). Closure (indomethacin, ibuprofen, or surgical ligation) for symptomatic left-to-right shunt (pulmonary edema, cardiomegaly).",

                # Cyanotic heart disease hyperoxia test
                "Hyperoxia test for cyanotic heart disease: place on 100% O2, measure PaO2. Cardiac cause (VSD, tetralogy) → PaO2 remains <100-150 mmHg. Pulmonary disease → PaO2 rises significantly. Not definitive but helps differentiation in newborn.",

                # Septic shock in children
                "Pediatric septic shock early recognition: may present as hypothermia, poor perfusion without fever; lactate elevation (>2 mmol/L) predicts poor outcome. Fluid bolus 20 mL/kg within 1 hour, vasopressors if persistently hypotensive after fluids. Pediatric-specific corticosteroid consideration in refractory shock.",

                # Drowning/near-drowning
                "Drowning pathophysiology: aspiration → surfactant wash-out → atelectasis → ARDS. Fresh water aspiration → hypervolemia; salt water → hypernatremia. Treatment: aggressive ventilation management, PEEP, permissive hypercapnia. Consider ECMO for severe cases (may recover with prolonged resuscitation if cold-water immersion).",

                # Fever in immunocompromised child
                "Immunocompromised child with fever: hematologic malignancy, post-transplant, HIV. High risk for opportunistic infections (CMV, PCP, fungal). Empiric broad-spectrum antibiotics, fungal coverage if prolonged fever. Blood cultures, imaging (CXR, CT), invasive testing if localization unclear.",

                # Meningococcemia
                "Meningococcemia in children: fulminant sepsis with petechial rash progressing to purpura, DIC, shock. Mortality 5-15%; survivors may have amputations (endotoxin-induced thrombosis). Treatment: ceftriaxone 2 g IV q12h (immediate, don't wait for LP), supportive care, consider dexamethasone 10 mg IV x4 days.",

                # PICU pain assessment
                "Pediatric pain assessment when nonverbal: use FLACC scale (Face, Legs, Activity, Cry, Consolability) for <3 years. Observe for physiologic signs: tachycardia, hypertension, diaphoresis, pupil dilation. Treat aggressively (undertreating common in PICU); opioid tolerance develops with continuous use.",

                # Pediatric fluid requirements
                "Pediatric daily fluid requirements (Holliday-Segar): first 10 kg = 100 mL/kg, next 10 kg = 50 mL/kg, each kg >20 = 20 mL/kg. Add 10-50 mL/kg for insensible losses. Adjust for losses (diarrhea, vomiting), fevers, sepsis. Critically ill: often require 1.5-2× maintenance.",

                # Pediatric transfusion thresholds
                "Pediatric RBC transfusion thresholds: stable patient Hgb 7-9 g/dL acceptable (similar to adults), critically ill/septic target Hgb >10 g/dL. Avoid excessive transfusion (increased mortality, immunosuppression). Packed RBCs 10 mL/kg increase Hgb ~3 g/dL.",

                # Pediatric NEC and IBD
                "Necrotizing enterocolitis (NEC) in premature: bowel ischemia + bacterial invasion → necrosis, perforation. Risk factors: prematurity, formula feeding (vs. breast milk), rapid feeding advancement. Signs: abdominal distention, blood in stool, pneumatosis intestinalis on X-ray. Treatment: stop feeds, antibiotics, supportive care; surgery if perforation.",
            ]
        },

        "geriatric_expanded": {
            "title": "Geriatric Medicine - Advanced",
            "units": [
                # Orthostatic hypotension in elderly
                "Orthostatic hypotension in elderly: drop >20 mmHg systolic or >10 mmHg diastolic within 3 min of standing. Causes: medications (beta-blockers, antihypertensives), autonomic dysfunction, hypovolemia, prolonged bedrest. Management: adequate hydration, compression stockings, slow position changes, midodrine (alpha-agonist) 5 mg TID, fludrocortisone 0.1-0.2 mg daily.",

                # Incontinence types
                "Urinary incontinence in elderly: stress (leak with Valsalva, cough), urge (sudden need to void, overactive bladder), overflow (retention with high residual), functional (unable to reach toilet). Different pharmacology: anticholinergics (tolterodine, oxybutynin) for urge, alpha-agonists (pseudoephedrine) for stress.",

                # Cognitive impairment assessment
                "Dementia assessment: Mini-Cog (3-item recall + clock drawing, <3 min), Montreal Cognitive Assessment (MoCA), Mini-Mental State Exam (MMSE). Differentiate delirium (acute, reversible) from dementia (chronic, progressive). Investigate reversible causes: B12 deficiency, thyroid, normal pressure hydrocephalus, subdural hematoma.",

                # Timed Up and Go test
                "Timed Up and Go (TUG) test: patient stands from chair, walks 10 feet, turns, walks back, sits. Time >12 seconds indicates high fall risk. Combined with other assessments (strength, balance, vision) to identify interventions (PT, home safety, assistive devices).",

                # Medication deprescribing in elderly
                "Deprescribing strategy: (1) assess appropriateness (Beers Criteria, disease-specific guidelines), (2) engage patient in shared decision-making, (3) taper dose (gradual if long-term to avoid withdrawal), (4) monitor for withdrawal symptoms, (5) assess benefit after discontinuation.",

                # Sarcopenia
                "Sarcopenia: age-related muscle loss and weakness; predictor of disability, falls, mortality. Screening: EWGSOP2 criteria (low muscle strength or quantity). Management: resistance training 2-3×/week, adequate protein (1.0-1.2 g/kg), vitamin D supplementation, treat underlying conditions.",

                # Hypertension targets in elderly
                "Blood pressure targets in elderly: younger elderly (65-79) intensive control (SBP <130) beneficial; older elderly (>80) or frail, individualize target (may be 130-140 or higher if intolerant). Avoid rapid reduction (risk of stroke, AKI). Monitor for orthostasis with any antihypertensive adjustment.",

                # Atrial fibrillation in elderly
                "AFib in elderly: common (5-10% prevalence >65 yo), increased stroke risk (2-3% per year without anticoagulation). Anticoagulation: DOAC preferred over warfarin (easier, faster); adjust dose for age/renal function. Rate control vs. rhythm control: rate control preferred in most (lenient target HR <110 acceptable unless symptomatic).",

                # Fall prevention
                "Fall prevention multifactorial approach: (1) assess gait/balance, (2) review medications, (3) vision/hearing assessment, (4) home safety evaluation, (5) vitamin D supplementation, (6) PT/strengthening exercises, (7) balance training, (8) assistive devices. Reducing falls prevents fractures, hospitalization, mortality.",

                # Pressure ulcer prevention
                "Pressure ulcer (decubitus) prevention in immobile elderly: use support surfaces (gel mattress, air mattress), frequent turning (q2h at minimum), skin assessment (stage I = nonblanchable erythema), manage moisture/incontinence, optimize nutrition. Prevention easier than treatment (stage 3-4 difficult to heal).",
            ]
        },

        "communication_expanded": {
            "title": "Communication - Advanced Skills",
            "units": [
                # Motivational interviewing
                "Motivational interviewing (MI) for behavior change: collaborative conversation to elicit change talk. Techniques: open-ended questions, affirmations, reflections, summaries (OARS). Avoid confrontation; roll with resistance. Assess readiness to change; meet patient where they are (not your agenda).",

                # Family meeting facilitation
                "Family meeting facilitation: clarify goals (establish prognosis, understand values, decide on plan). Preparation: have clear information, identify decision-maker, arrange quiet space. Technique: open-ended questions, listen more than speak, address emotions, summarize and confirm understanding.",

                # Psychological first aid
                "Psychological first aid for acute trauma/disaster: focus on safety, practical support, information provision. Techniques: establish calm, assess immediate needs, listen (don't probe), normalize responses, connect to resources. Distinguish from therapeutic counseling (not needed immediately).",

                # Addressing harmful request
                "Addressing patient request for medically harmful intervention: 'I understand you want X, but that would cause harm. Instead, we can offer Y which achieves your goal safely.' Explain rationale, offer alternatives, respect autonomy within safe bounds.",

                # Team huddles
                "Brief team huddles: <10 min daily, identify high-risk patients, communicate plan to all staff, identify resource needs. Improves safety culture, reduces errors. Structure: patient name, diagnosis, key concerns, plan for day.",

                # Responding to anger
                "De-escalating angry patient/family: stay calm, listen without defending, validate emotion ('I understand your frustration'), establish boundaries ('I want to help, but I need you to lower your voice'), involve security if threatening. Document threats.",

                # Translator use
                "Using medical interpreters: avoid family members (privacy, accuracy); use professional (phone/video) or in-person. Speak slowly, use simple words, avoid idioms. Address patient directly, not interpreter. Verify understanding by teach-back.",

                # Discussing iatrogenic injury
                "Disclosing medical error to patient: prompt disclosure (same day if possible), explain what happened, how it will be managed, what steps to prevent recurrence. Apologize for harm. Avoid defensive language. Documentation objective and factual.",

                # Cultural competency
                "Cultural competency in ICU: assess patient/family values, dietary restrictions, decision-making preferences (individual vs. family), spiritual needs. Ask 'What's important to you?' to guide care. Interpreter may be cultural broker; accommodate family presence if safe.",

                # Advance directive conversation
                "Advance directive conversation: introduce topic early (not in crisis). Explain living will (medical wishes), healthcare proxy (surrogate decision-maker), DNR/DNI. Explore values (quality vs. quantity of life, functional goals, fear of burden). Document clearly.",
            ]
        },

        "quality_expanded": {
            "title": "Quality & Safety - Advanced",
            "units": [
                # Healthcare-associated infection prevention
                "HAI prevention bundle: hand hygiene, appropriate antibiotics (stewardship), insertion technique (sterile), device removal (ASAP), aseptic maintenance. Bundle approach (all elements together) more effective than single interventions. Measure & report metrics (CLABSI, CAUTI, SSI rates) publicly.",

                # Antibiotic stewardship
                "Antibiotic stewardship: narrow-spectrum agents for documented infection, step-down to oral, time-limited courses (avoid indefinite), therapeutic drug monitoring for aminoglycosides/vancomycin. Broad-spectrum empiric initially, de-escalate once culture results available. Improve resistance, reduce C. diff, save costs.",

                # Rapid cycle testing
                "PDSA cycle (Plan-Do-Study-Act) for QI: small tests of change, rapid feedback, refine and scale. Example: implement central line checklist → audit compliance → identify barriers → revise → re-test. Rapid cycles (days/weeks) vs. lengthy project approvals.",

                # Never events
                "Never events (serious safety events): retained surgical object, wrong-site surgery, wrong patient, CRBSI, CAUTI, bloodstream infection. Aim: zero tolerance. Prevention: checklists (WHO Surgical Safety Checklist), counts (instruments, sponges, needles), team communication.",

                # Crew resource management
                "Crew Resource Management (CRM) from aviation: team communication, hierarchy not absolute (junior can speak up), cross-checks, briefings/debriefings. Reduces errors in high-stakes environments. Training: team-based, focus on communication skills.",

                # Incident reporting systems
                "Incident reporting (near-miss and actual errors): confidential, non-punitive culture encourages reporting. Analysis: not blame-focused but system-focused. Actionable changes: design failures, training gaps, workflow improvements. Transparency: share lessons learned anonymously.",

                # Patient safety metrics
                "Patient safety metrics: culture surveys (Safety Attitudes Questionnaire), outcome metrics (mortality, readmissions), process metrics (compliance with bundles, timely antibiotics). Balanced scorecard approach (clinical + safety + efficiency).",

                # Simulation for team training
                "High-fidelity simulation training: develops crisis resource management, team communication, technical skills. Scenarios: sepsis recognition, massive transfusion, difficult airway. Benefits: safe practice, error recovery, team building. Debriefing critical (structured reflection on performance).",

                # Root cause analysis documentation
                "RCA documentation: objective facts (what happened, when, to whom), contributing factors (system failures, human factors), not assigned blame. Recommendations: specific, actionable, addressed to owner. Follow-up: verify implementation, monitor for effectiveness.",

                # Transparency & disclosure
                "Transparency in adverse events: communicate with patient/family (what happened, what will be done, prevention measures), offer support (chaplain, social work, counseling). Early disclosure and apology reduce litigation and improve trust.",
            ]
        },

        "palliative_expanded": {
            "title": "Palliative Care - Advanced Management",
            "units": [
                # Symptom management (opioids detailed)
                "Opioid dosing principles: start low (morphine 5-10 mg PO q4h or 2-4 mg IV), titrate q3-5 days by 25-50% increments until pain controlled. Equianalgesic dosing: morphine 30 mg PO = fentanyl 12.5 mcg/h patch = hydromorphone 7.5 mg PO. Watch for tolerance (requires dose escalation) vs. addiction (psychological dependence).",

                # Breakthrough pain
                "Breakthrough pain: pain that exceeds baseline controlled pain; requires fast-acting opioid (short-acting morphine, liquid hydromorphone) in addition to long-acting agent (extended-release morphine, fentanyl patch). Dose: 10-20% of total daily opioid dose, q1-2h PRN.",

                # Dyspnea management
                "Dyspnea management palliative: low-dose opioids (morphine 2-4 mg IV q1-2h), oxygen if hypoxic, fan (psychological benefit), anxiolytics (lorazepam) if anxiety component. Goal: comfort, not necessarily normalizing O2 sat. Position of comfort, minimize activity, speak calmly.",

                # Nausea & constipation
                "Nausea in palliative care: causes (opioid-induced most common, metabolic, increased ICP). Anti-emetics: ondansetron 4-8 mg IV (chemoreceptor), metoclopramide 5-10 mg PO q6h (motility, blocks dopamine), dexamethasone (raised ICP, brain mets). Constipation near-universal with opioids: stool softener + osmotic laxative (senna) scheduled (not PRN).",

                # Palliative sedation
                "Palliative sedation: intentional sedation to relieve intractable symptoms at end of life. Requires informed consent, documented refractory symptoms. Medications: propofol, midazolam, pentobarbital titrated to comfort. Family present, continue comfort measures (positioning, mouth care). Ethical but distinct from euthanasia.",

                # Existential suffering
                "Existential suffering: loss of meaning, identity, control; fear of dying, dying process. Interventions: chaplaincy, counseling, meaning-making conversations, spiritual practices. Recognize when it's beyond medical symptom management; address with interdisciplinary team.",

                # Bereavement support
                "Bereavement support: immediate (during hospitalization/after death), short-term (1-6 months), long-term (ongoing). Resources: support groups, counseling, educational materials. High-risk: sudden/traumatic death, complicated grief, prior losses, lack of social support.",

                # Opioid-induced respiratory depression risk
                "Opioid-induced respiratory depression: risk increases with age, renal failure, COPD, concurrent sedatives. Monitoring: observe respiration rate, adequacy of ventilation. At end of life: controlled sedation may reduce consciousness → reduced respiratory drive (acceptable as goal is comfort). Document goals.",

                # Advance care planning
                "Advance care planning: proactive (not just in crisis); explore values, preferred place of death, goals for dying (dignity, family time, pain-free). Document: advance directive, healthcare proxy, POLST (Physician Orders for Life-Sustaining Treatment). Revisit periodically as preferences evolve.",

                # Dying process awareness
                "Educating family on dying process: what to expect (breathing changes, consciousness, incontinence, temperature drops, sounds, final breaths). Normalize process, reduce fear, prepare for death. Allow family presence, private time, rituals (reading, prayer, music).",
            ]
        },
    }

    # Add expansion units
    unit_id_counter = len(units) + 700

    for section_key, section_data in expansions.items():
        for text in section_data["units"]:
            units.append({
                "id": f"phase4_unit_{unit_id_counter}",
                "text": text,
                "metadata": {
                    "topic": section_data["title"],
                    "topic_tags": [section_key.replace("_expanded", "")] + ["advanced", "detailed"],
                    "library": "intern_year_medicine",
                    "source_name": "Phase 4 Knowledge Base - Expansion",
                    "book": "Phase 4 - Remaining Essentials (Advanced)",
                    "section": section_key.replace("_expanded", ""),
                    "created_at": datetime.now().isoformat(),
                    "chunk_type": "fact"
                }
            })
            unit_id_counter += 1

    return units


if __name__ == "__main__":
    units = expand_phase4()

    # Save to JSON
    output_path = Path("data") / "phase4_comprehensive.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(units, f, indent=2, ensure_ascii=False)

    # Statistics
    by_section = {}
    for unit in units:
        section = unit["metadata"]["section"]
        by_section[section] = by_section.get(section, 0) + 1

    print(f"[OK] Phase 4 comprehensive generated: {len(units)} total units")
    print(f"  Output: {output_path}\n")

    print("Phase 4 Complete Breakdown by Section:")
    total_count = 0
    for section, count in sorted(by_section.items()):
        total_count += count
        print(f"  {section:30s}: {count:3d} units")

    print(f"\nTotal Phase 4 Units: {total_count}")
    print(f"Cumulative with Phase 1-3: ~{total_count + 475} units (target 1,200)")
