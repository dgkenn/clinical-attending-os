#!/usr/bin/env python3
"""
Expand Phase 5 units to reach 300-400 target
Adding deeper specialization within each of the 8 modules
"""

import json
from datetime import datetime
from typing import List, Dict, Any

def create_unit(
    text: str,
    topic: str,
    topic_tags: List[str],
    module_name: str,
    index: int,
    section: str,
    book: str = "Phase 5 Advanced Cardiac & Hemodynamics"
) -> Dict[str, Any]:
    """Create a single knowledge unit"""
    return {
        "id": f"phase5_{module_name}_unit_{index}",
        "text": text,
        "metadata": {
            "topic": topic,
            "topic_tags": topic_tags,
            "library": "anesthesiology_cardiac_advanced",
            "source_name": "phase5_cardiac_knowledge_expansion",
            "book": book,
            "section": section,
            "module": module_name,
            "created_at": datetime.now().isoformat(),
            "chunk_type": "fact"
        },
        "created_at": datetime.now().isoformat()
    }

def expand_acls_units() -> List[Dict[str, Any]]:
    """Expand ACLS module to 40-50 units"""
    units = []
    module = "acls"
    start_idx = 22

    facts = [
        ("Chain of survival for out-of-hospital cardiac arrest", "Recognition → Early CPR → Early defibrillation → Early ACLS → Post-cardiac arrest care. Each link critical: within 10 min CPR crucial, defibrillation within 3-5 min ideal, ACLS medications timely, post-arrest TTM/interventions. Survival decreases ~10%/min without defibrillation in VF. Public access defibrillation (PAD) programs improve outcomes. Community CPR training essential.", ["acls", "survival", "prehospital", "chain", "education"]),

        ("Cardiac arrest no-flow and low-flow time", "No-flow time = time from arrest to start of CPR. Low-flow time = duration of CPR. Outcomes inversely correlated with both. Neurologic recovery unlikely if no-flow >10 min (exceptions: profound hypothermia, submersion). Low-flow >30 min with poor prognostic indicators → consider stopping resuscitation. Young patients/reversible cause may warrant longer resuscitation. Bystander CPR crucial for reducing no-flow time.", ["acls", "prognosis", "time_dependent", "outcomes", "survival"]),

        ("Defibrillation mechanics and effectiveness", "Biphasic defibrillation (most modern AEDs) safer and equally effective as monophasic. Energy: 120-200 J for biphasic, 360 J for monophasic (not used). Defibrillation works by: depolarizing entire heart → interrupting reentrant circuit. VF recurs within seconds if no intervention (CPR must follow immediately). Higher energy not better beyond effective dose. Manual defibrillator preferred (allows synchronization for VT). AED automated detection of shockable rhythm.", ["acls", "defibrillation", "biphasic", "energy", "technique"]),

        ("High-quality CPR components", "Rate: 100-120 compressions/min. Depth: 2-2.4 inches (5-6 cm) in adults. Recoil: allow full chest recoil between compressions (not removing hand). Ventilation: balance compressions with rescue breaths in witnessed arrest (30:2), compression-only in asystole/PEA. Avoid excessive ventilation (causes gastric inflation, hyperinflation impairs venous return). Minimize interruptions to compressions (<10 sec). Mechanical CPR devices allow sustained high-quality compressions.", ["acls", "cpr", "high_quality", "technique", "outcomes"]),

        ("CPR in special populations", "Pediatric: depth 2 inches (1/3 chest depth), rate 100-120, compression-only acceptable. Pregnant: leftward uterine displacement, consider perimortem cesarean. Elderly: assess for DNR, may have fragile ribs. Obese: adequate depth may require increased effort. Trauma: cervical spine precautions initially, then standard ACLS. Drowning: air exchange critical (may need rescue breathing first). Hypothermia: slow assessment, prolong resuscitation attempts.", ["acls", "special_populations", "pediatric", "pregnant", "modifications"]),

        ("AED (Automated External Defibrillator) use", "Portable device analyzes ECG → determines if shock indicated. Visible electrode pads adhere to chest (bare skin). Operator follows voice prompts (continue CPR, stand clear, etc). Highly sensitive/specific for VF/PVT. Should be deployed immediately in any unresponsive adult with no pulse. PAD programs in public spaces (airports, sports venues) improve access to defibrillation. Training simple—designed for layperson use.", ["acls", "aed", "defibrillation", "public_access", "training"]),

        ("Resuscitation drug access routes", "IV (intravenous) preferred—reliable access, rapid delivery. IO (intraosseous) if no IV access available (proximal humerus or tibia). Both equally effective. ETT (endotracheal tube) accessible but absorption unpredictable (avoid if IV/IO feasible). IM epinephrine useful in specific scenarios (anaphylaxis, remote settings). All ACLS medications can be given IV/IO; only some via ETT (epinephrine, lidocaine, atropine, vasopressin—remember LEAN).", ["acls", "medications", "access", "routes", "techniques"]),

        ("Cardiac arrest in asthma", "Usually due to severe bronchospasm/hypoxemia. Treat: aggressive CPR, consider magnesium (2 g IV), terbutaline (10 mcg IV, repeat), epinephrine standard dose. Minimize triggering factors (avoid morphine/atracurium if possible). Prolonged CPR may be needed (brain more resistant to hypoxemia with hypercarbia). Difficult intubation anticipated. Post-ROSC: aggressive bronchodilators, may need ECMO if conventional CPR fails.", ["acls", "asthma", "special_situation", "bronchospasm", "hypoxemia"]),

        ("Resuscitation in severe anemia", "Hypoxemia + reduced O2 carrying capacity = rapid deterioration. RBCs crucial for oxygen transport. Standard ACLS applies but outcome poor without transfusion. Type O negative blood immediately if available. Goal: maintain Hb >7-10 g/dL post-ROSC (higher targets may increase thrombotic risk). Massive transfusion protocol if ongoing hemorrhage. Prolonged CPR may be needed (brain paradoxically tolerates hypoxemia better in acute anemia).", ["acls", "anemia", "hemorrhage", "transfusion", "special_situation"]),

        ("Sepsis and cardiac arrest", "Sepsis can cause cardiac arrest (septic cardiomyopathy, distributive shock). CPR combined with immediate antibiotics, source control, vasopressors. Sepsis-related VF less responsive to standard ACLS. Consider extended resuscitation effort (usually improved prognosis if source reversible). Post-ROSC: continue antibiotics, ICU-level care, source control (drainage of abscess, etc). Lactate elevation common (not necessarily prognostic if resolves).", ["acls", "sepsis", "special_situation", "arrest", "cardiogenic_shock"]),

        ("Resuscitation endpoints decision-making", "Asystole alone not indication to stop if reversible cause possible. Consider: patient age, comorbidities, witnessed arrest, no-flow time, response to resuscitation (any improvement?), reversible cause identified? Hypothermia is exception (continue until rewarmed). ETCO2 <10 throughout resuscitation → poor prognosis. Severe head injury/trauma → assess neurologic status post-ROSC. Family preferences if known (DNR order). Ethical discussions important.", ["acls", "termination", "ethical", "decision_making", "prognostication"]),

        ("Medication timing and spacing", "Epinephrine: 1 mg IV every 3-5 min. Amiodarone: 300 mg first dose, 150 mg second dose, then 150 mg as often as every 5-10 min (max 2.2 g/day). Atropine (if used): 0.5-1 mg every 3-5 min (max 3 mg total). Sodium bicarbonate: 1 mEq/kg initially, repeat every 5-10 min. Calcium: 5-10 mL of 10% solution IV push. Spacing prevents drug interactions/cumulative toxicity. IV flushes between medications recommended. Document timing carefully.", ["acls", "medications", "dosing", "timing", "intervals"]),

        ("Family presence during CPR", "Contemporary practice: allowing family at bedside during resuscitation. May improve grief processing, family understanding of death. No negative impact on team performance if organized. Designated staff member to support family. Debrief with family post-code (explain what happened, prognosis). Support services (chaplaincy, social work) helpful. Document family presence in medical record. Increases transparency/trust.", ["acls", "communication", "family", "presence", "ethics"]),

        ("Post-resuscitation imaging and labs", "Chest X-ray: assess for aspiration, pneumothorax, rib fractures (CPR complications). ECG: identify underlying rhythm (STEMI, Brugada, Long QT). Head CT: consider if altered mental status, concern for intracranial process. Troponin/CK-MB: assess for MI (elevated post-arrest anyway from CPR). Lactate: marker of tissue hypoperfusion (trends useful). Blood gas: respiratory status, metabolic acidosis degree. Consider angiography if STEMI presentation.", ["acls", "post_arrest", "imaging", "labs", "assessment"]),

        ("Extracorporeal rewarming for hypothermia", "ECMO/ECPR (extracorporeal cardiopulmonary resuscitation) for profound hypothermia (<20°C) in cardiac arrest. Provides rapid rewarming while supporting circulation. Transfers heat to blood externally. May achieve full recovery even after prolonged arrest in profound hypothermia (>1 hour CPR reported with good outcome). Requires: ECMO-capable center, rapid transport, experienced team. Exceptional survival rates possible. Travel to ECMO center justified.", ["acls", "hypothermia", "ecmo", "rewarming", "special_situation"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=start_idx + idx,
            section="ACLS & Resuscitation Expansion"
        ))

    return units

def expand_arrhythmia_units() -> List[Dict[str, Any]]:
    """Expand Arrhythmia module to 50-70 units"""
    units = []
    module = "arrhythmia"
    start_idx = 33

    facts = [
        ("Multifocal atrial tachycardia (MAT)", "Three or more ectopic foci in atria → irregular tachycardia. ECG: variable P-wave morphology, variable PR intervals, irregular rate (100-150 typically). Associated with: COPD (most common), hypoxemia, pulmonary HTN, hyperthyroidism, hypokalemia, digoxin toxicity. Treatment: beta-blockers (rate control), calcium channel blockers, treat underlying cause (oxygenation, correct K+). Avoid adenosine (ineffective for MAT, may cause AVN block). Digoxin not first-line. Prognosis depends on underlying disease.", ["arrhythmias", "mat", "multifocal", "atrial_tachycardia", "irregular"]),

        ("Atrial tachycardia and ectopic atrial tachycardia", "Rapid regular atrial rhythm with visible P waves at rate 100-250 bpm. Single focus in atrium (unlike MAT). Types: sinus tachycardia (normal P waves, appropriate HR for clinical status), ectopic atrial tachycardia (abnormal P morphology, inappropriate HR). Treatment: beta-blockers, calcium channel blockers, class IC antiarrhythmics (flecainide, propafenone), amiodarone. Ablation if refractory. Usually benign prognosis if structural heart disease excluded.", ["arrhythmias", "atrial_tachycardia", "ectopic", "mechanism", "treatment"]),

        ("Junctional tachycardia", "Rhythm originates in AV junction (around AV node). Rate 100-150 bpm, narrow QRS, P waves buried in QRS (RP <100 ms) or immediately after. Retrograde conduction to atria (may see retrograde P after QRS). Regular rhythm. Causes: digoxin toxicity (most common cause of junctional tachycardia), enhanced AV nodal automaticity, after cardiac surgery. Treatment: digoxin toxicity requires discontinuation, potassium correction, magnesium, antidigoxin Fab if needed. Beta-blockers, CCB also helpful.", ["arrhythmias", "junctional_tachycardia", "jat", "digoxin", "toxicity"]),

        ("Brugada ECG pattern and syndrome", "ECG: type 1 pattern = coved ST elevation V1-V2 with negative T wave (mimics RBBB with ST elevation). Diagnostic = <1 mV ST elevation. Type II/III patterns less specific. Brugada syndrome = type 1 pattern + symptoms (syncope, nocturnal agonal respirations, cardiac arrest). Risk factors: fever, drugs (flecainide, propafenone), hyperthermia. Mechanism: sodium channel mutation. Cellular uncoupling of early phases of ventricular repolarization. ICD recommended for symptomatic patients.", ["arrhythmias", "brugada", "type1_pattern", "sudden_death", "genetic"]),

        ("Early repolarization and Osborn wave", "Early repolarization = J point elevation (junction between QRS and ST segment) in V2-V3. Often normal finding, especially in young males, athletes. Osborn wave (prominent J wave) seen in hypothermia. Early repolarization can predispose to VF in some individuals. Risk increased if: extensive J wave elevation (>2 mm), ST-segment horizontal/descending, diffuse pattern, high-risk genotype (DCHS1 mutation). Usually asymptomatic. Management: ICD if symptomatic, watchful waiting if asymptomatic.", ["arrhythmias", "early_repolarization", "j_wave", "osborn_wave", "inherited"]),

        ("Acute coronary syndrome and arrhythmias", "MI frequently triggers arrhythmias. Anterior MI (STEMI): VT, VF (especially first 48h). Inferior MI: bradycardia, AV block (from RV involvement), ventricular ectopy. Reciprocal inferior changes with anterior STEMI may show atrial arrhythmias. Reperfusion arrhythmias: accelerated idioventricular rhythm (AIVR) indicates successful reperfusion (benign). Treatment: revascularization (PCI/CABG) critical. Beta-blockers reduce arrhythmia risk post-MI. Antiarrhythmics secondary. ICD if EF drops post-MI.", ["arrhythmias", "acs", "mi", "reperfusion", "acute"]),

        ("Digoxin toxicity and arrhythmias", "Therapeutic window narrow (0.8-2 ng/mL). Toxicity presents with: nausea/vomiting (earliest sign), arrhythmias. Arrhythmias from digoxin: PACs, PVCs, atrial tachycardia with AV block, junctional tachycardia, VT, complete heart block (severe). Combination arrhythmias possible (e.g., atrial tach + AV block = highly specific for digoxin toxicity). Risk factors: hypokalemia, hypomagnesemia, renal failure, drug interactions (amiodarone, verapamil increase digoxin levels). Treatment: stop digoxin, correct K+/Mg2+, antidigoxin Fab for severe toxicity.", ["medications", "digoxin", "toxicity", "arrhythmias", "hyperkalemia"]),

        ("Amiodarone toxicity", "Multiple organ systems affected. Thyroid: hyper/hypothyroidism (most common, 1-5% of patients). Lung: pulmonary fibrosis (rare, 1%, but serious). Liver: hepatotoxicity (monitor LFTs). Cornea: microdeposits (vision usually preserved). Skin: blue-gray discoloration. Neurologic: tremor, neuropathy. Cardiac: torsades de pointes (QT prolongation), bradycardia, AV block, negative inotropic effect (can worsen HF initially). Monitoring: baseline TSH, FT4, LFTs, ECG. Consider discontinuation if toxicity. Half-life very long (weeks-months).", ["medications", "amiodarone", "toxicity", "monitoring", "side_effects"]),

        ("QT interval physiology and prolongation", "QT interval reflects ventricular repolarization duration. Corrected QT (QTc) adjusts for heart rate. Normal QTc <440 ms males, <460 ms females. Prolongation risk factors: antiarrhythmic drugs (sotalol, dofetilide, amiodarone), antibiotics (fluoroquinolones, macrolides), antipsychotics (haloperidol, clozapine), antiretrovirals, hypokalemia, hypomagnesemia, hypocalcemia, female sex, bradycardia. Torsades de pointes risk increases substantially if QTc >500 ms. Management: avoid QT-prolonging drugs, correct electrolytes, beta-blockers if Long QT syndrome.", ["arrhythmias", "qt_interval", "prolongation", "torsades", "electrolytes"]),

        ("Drug-induced arrhythmias mechanisms", "Pro-arrhythmic effects from: increased automaticity (sympathomimetics, hyperthyroidism), triggered activity (digoxin toxicity, early afterdepolarizations from QT prolongation, delayed afterdepolarizations), reentry (flecainide paradoxically slowing conduction to facilitate reentry). Class IC antiarrhythmics (flecainide, propafenone) particularly pro-arrhythmic in structural heart disease (avoid post-MI). Some drugs: sotalol (QT prolongation), verapamil (AV block risk). Risk-benefit assessment critical before antiarrhythmic use.", ["medications", "antiarrhythmics", "pro_arrhythmic", "side_effects", "risk"]),

        ("Radiofrequency ablation indications and success rates", "Indications: AVNRT (90% success), AVRT (95% success), typical atrial flutter (>95% success), atrial fibrillation (70-80% for paroxysmal, 50-60% for persistent), VT (50-80% depending on mechanism). Procedure: catheter-based endovascular approach, identify arrhythmia site, ablate tissue (heat causes scar formation blocking conduction). Risks: vascular injury, stroke (AF ablation), perforation, thromboembolism. Anesthesia: sedation or general. Success depends on: mechanism identification, accessible site, expertise of operator. Cure possible (no lifelong antiarrhythmics).", ["arrhythmias", "ablation", "rf_ablation", "curative", "outcomes"]),

        ("Cryoablation for arrhythmias", "Alternative to radiofrequency: uses extreme cold (cryogenic energy) to freeze tissue. Potential advantages: ability to test effect before committing (freeze lesion reversible initially), better contact in challenging anatomy, reduced perforation risk (adhesive effect of ice). Used for: AVNRT (similar success to RF), some accessory pathways, AF (emerging). Success rates: comparable to RF ablation. Cost higher than RF. Less operator experience compared to RF (more recently introduced). Integration with imaging improving outcomes.", ["arrhythmias", "cryoablation", "ablation", "alternative", "technique"]),

        ("Implantable cardioverter-defibrillator (ICD)", "Electronic device implanted in chest with lead(s) to heart. Monitors rhythm → detects VT/VF → delivers shock (defibrillation) automatically. Indications: prior cardiac arrest from VT/VF (secondary prevention), EF <35% with ischemic cardiomyopathy (primary prevention), genetic syndromes (Long QT, Brugada, CPVT). ICD improved survival ~20-30% in appropriate populations (MADIT trials). Risks: inappropriate shocks (usually for SVT), lead failure, infection. Patients can hear/feel shock (painful, frightening). Psychological support important.", ["devices", "icd", "implantable", "sudden_death_prevention", "outcomes"]),

        ("Permanent pacemaker indications", "Symptomatic bradycardia (SSS, AV block) refractory to medical therapy. Sinus node disease with HR <40 or pauses >3 sec. High-degree AV block (Mobitz II, complete heart block). Bifascicular block + syncope (concerning for progressing to CHB). Pacer modes: VVI (ventricular demand, no atrial sensing), AAI (atrial, sinus node disease), DDD (dual-chamber, most physiologic). Rate-adaptive pacing (increases rate with activity). Risk: infection, lead fracture, oversensing/undersensing. Longevity: 10-15 years typical.", ["devices", "pacemaker", "indications", "modes", "outcomes"]),

        ("Biventricular pacing for heart failure (CRT)", "Cardiac Resynchronization Therapy: paces both ventricles simultaneously to improve synchrony (RV and LV contracting together vs. out of sync in LBBB). Indications: HFrEF (EF <35%), QRS >120 ms (especially LBBB pattern), NYHA Class III-IV on optimal medical therapy. CRT improves EF, symptoms, exercise tolerance, mortality (25-30% reduction). Response rate ~60-70% (super-responders vs. non-responders). Can combine with ICD (CRT-D) for rhythm and resynchronization therapy. Requires optimization (AV delay, VV delay) post-implant.", ["devices", "crt", "biventricular_pacing", "heart_failure", "outcomes"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=start_idx + idx,
            section="Advanced Arrhythmia Management Expansion"
        ))

    return units

def expand_shock_units() -> List[Dict[str, Any]]:
    """Expand Shock module to 50-70 units"""
    units = []
    module = "shock"
    start_idx = 19

    facts = [
        ("Septic shock pathophysiology in detail", "Lipopolysaccharide (LPS) / pathogen-associated molecular patterns (PAMPs) bind Toll-like receptors (TLRs) on immune cells. Triggers innate immune cascade: NF-kB activation, massive pro-inflammatory cytokine release (TNF-alpha, IL-1beta, IL-6). Cytokines cause: endothelial dysfunction (increased permeability, edema), vasodilation (decreased SVR), myocardial depression (TNF-alpha cardiotoxic), microvascular dysfunction (shunting, capillary closure), mitochondrial dysfunction (impaired aerobic metabolism). Result: distributive shock with tissue hypoperfusion despite high CO initially. Late shock: multi-organ failure.", ["sepsis", "pathophysiology", "mechanism", "innate_immunity", "cytokines"]),

        ("Sepsis source control principles", "Rapid source control critical: remove infected device (central line, urinary catheter), drain abscess, necrotizing fasciitis requires immediate debridement, perforated viscus requires surgery. Source control should NOT be delayed for diagnostics (imaging while starting antibiotics/vasopressors). Timing matter: source control within 12h optimal (mortality increases with delay beyond 12-24h). Surgery vs. percutaneous drainage decision based on feasibility/patient status. Repeat procedures may be needed.", ["sepsis", "source_control", "surgical", "timing", "outcomes"]),

        ("Surviving Sepsis Campaign guidelines", "Bundle approach: 1-hour bundle (lactate measurement, blood cultures, broad-spectrum antibiotics, fluid bolus 30 mL/kg if hypotensive, vasopressor if MAP <65 after fluids). 6-hour bundle (reassess perfusion, repeat lactate, repeat fluid assessment, adjust therapy). De-escalation: narrow antibiotics once culture results available (48-72h). Duration: typically 7-10 days total (re-evaluate daily). Goals: ScvO2 >70%, MAP >65, urine output >0.5 mL/kg/h, lactate normalization. Early recognition and treatment improve outcomes.", ["sepsis", "guidelines", "bundle", "treatment", "outcomes"]),

        ("Right ventricular failure in septic shock", "RV dysfunction common in sepsis (septic cardiomyopathy). Mechanisms: myocardial depression from TNF, elevated afterload (pulmonary HTN from ARDS, excessive vasopressors), hypovolemia. Presents with: elevated CVP despite low PAWP, reduced RV output, tricuspid regurgitation. Echo shows RV dilation, reduced function, septal flattening. Treatment: optimize preload (careful fluid management), reduce afterload (inhaled nitric oxide, milrinone), inotropes (dobutamine, milrinone), pulmonary vasodilators. Poor prognosis if RV failure severe.", ["sepsis", "rv_failure", "cardiomyopathy", "septic", "hemodynamics"]),

        ("Fluid resuscitation strategies in sepsis", "Early aggressive fluids improve survival (RIVERS trial, EGDT). Goal: MAP >65 (usually requires 30 mL/kg initial bolus). Balanced crystalloids (lactated Ringer, Plasmalyte) preferred over normal saline (hyperchloremic acidosis risk). Albumin NOT superior to crystalloids in general sepsis (SAFE trial), but may be used if massive transfusion needs (cheaper to use crystalloid + later add albumin if protein loss >20g/dL). Over-resuscitation increases ARDS risk → permissive hypotension concept (MAP 65 sufficient, avoid excessive fluids). De-escalation: slow diuretics once stabilized.", ["sepsis", "fluid_resuscitation", "resuscitation_strategy", "crystalloids", "outcomes"]),

        ("Anaphylaxis rapid recognition and management", "Minutes critical: immediate IM epinephrine (0.3-0.5 mg for adult, 0.3 mg for <30 kg). Position: supine, elevate legs. IV access, fluids, antihistamines (diphenhydramine), corticosteroids (methylprednisolone). Avoid lying supine initially if respiratory symptoms (fatal arrhythmia risk from epinephrine). Repeat epinephrine every 5-15 min if needed. Intubation may be needed (angioedema laryngeal airway). Hospital admission even if good response (biphasic reaction possible 4-72h later). Identify/avoid trigger. Consider epinephrine auto-injector prescription for at-risk.", ["anaphylaxis", "shock", "emergency", "epinephrine", "management"]),

        ("Anaphylaxis pathophysiology and triggers", "Type I hypersensitivity: antigen cross-links IgE on mast cell/basophil surface → degranulation → release of: histamine (vasodilation, bronchospasm), tryptase (protease), leukotrienes (bronchoconstriction), prostaglandins, platelet-activating factor. Results: urticaria/pruritus, angioedema, bronchospasm, hypotension, shock, cardiac arrhythmias. Common triggers: medications (beta-lactam antibiotics, NSAIDs, ACE-I), foods (peanuts, shellfish, tree nuts), latex, hymenoptera (bee/wasp sting), contrast media. Diagnosis: elevated tryptase during event (correlates with degranulation degree).", ["anaphylaxis", "pathophysiology", "ige", "mast_cells", "triggers"]),

        ("Transfusion-related acute lung injury (TRALI)", "Acute respiratory distress within 6h of transfusion. Presents with: hypoxemia, bilateral infiltrates, pulmonary edema, hypotension. Mortality 5-10%. Mechanism unclear but likely: immune (HLA/HNA antibodies in donor plasma activate recipient neutrophils → cytokine release), non-immune (storage-related factors). Risk: FFP, platelets, pRBCs all implicated. No specific treatment (supportive care, mechanical ventilation). Diagnosis of exclusion. Prevention: limit plasma transfusions, volume-controlled transfusion, consider male-only FFP donors (women have higher antibody prevalence).", ["transfusion", "trali", "complication", "ards", "immune"]),

        ("Mixed venous oxygen saturation (SvO2) and lactate dynamics", "SvO2 <60% indicates inadequate O2 delivery relative to demand. Measured via Swan-Ganz (PA catheter) or central line. ScvO2 (central venous) correlates with SvO2 (simpler, non-invasive). Low SvO2 + high lactate = tissue hypoxia (shock). High SvO2 (paradoxically >70%) + elevated lactate = maldistribution (septic shock, mitochondrial dysfunction). Treatment tailored: low SvO2 → increase CO (fluids, inotropes), increase oxygen delivery (blood transfusion, O2), low SvO2 + low lactate → volume needed. Trends over time more useful than single values.", ["shock", "oxygen_delivery", "svmo2", "lactate", "assessment"]),

        ("Glucose control in shock states", "Hyperglycemia common (stress response, decreased insulin sensitivity). Tight glycemic control (80-110 mg/dL) not superior to conventional (180-250 mg/dL) per NICE-SUGAR trial (increased mortality with tight control). Current goal: avoid severe hyperglycemia (>300 mg/dL, osmolar state). Insulin resistance pronounced in sepsis → large doses needed. Avoid hypoglycemia (seizures, arrhythmias, impaired immune function). Monitor frequently (q 1-2h in shock). Dextrose-containing fluids may worsen hyperglycemia—use judiciously. Re-evaluate target goals patient-specifically.", ["shock", "glucose", "hyperglycemia", "insulin", "management"]),

        ("Immune dysfunction in sepsis and immunotherapy", "Sepsis triggers paradoxical response: initial hyper-inflammation (excess TNF, IL-6) followed by immunosuppression (T-cell exhaustion, reduced monocyte HLA-DR expression). Immunosuppressed phase associated with worse outcomes. Emerging therapies: GM-CSF (enhance monocyte function), IL-7 (T-cell recovery), checkpoint inhibitors (experimental). Current standard: supportive care only. Immunosuppressant avoidance (avoid prolonged corticosteroids >7 days if possible, controversial). Future: personalized immunotherapy based on immune profiling.", ["sepsis", "immunology", "immunosuppression", "immunotherapy", "research"]),

        ("Vasopressor weaning and outcomes", "Weaning timing uncertain—generally attempt once MAP maintained at target (65 mmHg) without escalation for >6-12h. Gradual reduction: decrease infusion rate by 10-20% q 4-6h while monitoring BP, lactate, perfusion markers. Some patients require prolonged vasopressor support (>7 days)—associated with worse prognosis. Early vasopressor weaning associated with relapse of hypotension. Catch-22: long-term vasopressor use worsens outcomes but premature weaning causes relapse. Ongoing fluid optimization, infection source control, and inotropic support facilitate weaning.", ["shock", "vasopressor", "weaning", "outcomes", "prognosis"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=start_idx + idx,
            section="Shock Physiology Deep Dive Expansion"
        ))

    return units

def expand_ventilation_units() -> List[Dict[str, Any]]:
    """Expand Ventilation module to 50-70 units"""
    units = []
    module = "ventilation"
    start_idx = 20

    facts = [
        ("Volutrauma and barotrauma in mechanically ventilated patients", "VILI (ventilator-induced lung injury): volutrauma (overdistension of alveoli), barotrauma (high airway pressures), atelectotrauma (repeated opening/closing). Mechanisms: direct alveolar disruption, inflammatory cascade from cyclical reopening/collapse, increased microvascular permeability. Prevention: lung-protective ventilation (6-8 mL/kg ideal BW, Pplat <30). PEEP recruitment strategy: improves compliance, prevents atelectotrauma. Mortality benefit shown with lung-protective ventilation in ARDS (ARDSnet trial). Current standard for all mechanically ventilated patients.", ["ventilation", "vili", "barotrauma", "volutrauma", "lung_protection"]),

        ("Ideal body weight calculation and tidal volume", "IBW = 50 + 2.3 * (height in inches - 60) for males, females = 45.5 + 2.3 * (height in inches - 60). Tidal volume 6-8 mL/kg IBW (lower end safer in ARDS). Example: 70 kg male 5'10'' (70 inches): IBW = 50 + 2.3 * 10 = 73 kg. 6-8 mL/kg × 73 = 438-584 mL appropriate TV. Helps prevent excessive ventilation (use actual weight might overdrive large patients). Frequent error: using current weight instead of IBW (leads to excessive TV, higher Pplat, worse outcomes).", ["ventilation", "ibw", "tidal_volume", "calculation", "dosing"]),

        ("Lung recruitment maneuvers", "Sustained inflation: stepwise increase in PEEP/pressure to high levels (30-40 cm H2O) for 30 sec. Goal: recruit collapsed alveoli → improve oxygenation + compliance. Open lung approach: high PEEP (15-20+) strategy throughout ventilation. Risk: hemodynamic compromise (reduced preload from high intrathoracic pressure), barotrauma if excessive. Efficacy variable: works in some ARDS patients (improves P/F ratio), neutral or worsening in others. Not universally recommended but may help refractory hypoxemia. Monitor BP, CO closely.", ["ards", "recruitment", "maneuver", "peep", "strategy"]),

        ("Permissive hypercapnia detailed physiology", "PaCO2 >50 mmHg tolerated to reduce TV/driving pressure. Respiratory acidosis develops (pH may drop to 7.15-7.20). Effects: sympathetic stimulation (tachycardia, hypertension), cerebral vasodilation (ICP concern in head trauma), catecholamine release (myocardial O2 demand increase), rightward O2-Hb curve shift (more O2 unloading to tissues). Renal buffering compensates (takes hours). Beneficial: reduced VILI. Contraindicated: intracranial hypertension, acute MI, pulmonary HTN (may worsen RV failure). Sodium bicarbonate if severe acidemia (rare need).", ["ards", "permissive_hypercapnia", "physiology", "acidosis", "contraindications"]),

        ("Sedation and neuromuscular blockade in mechanically ventilated", "Sedation: morphine, fentanyl (analgesia + sedation), propofol (sedation only), dexmedetomidine (alpha-2 agonist, preserves cognition). Neuromuscular blockade: cisatracurium, vecuronium, rocuronium (paralytics). Indications for paralysis: profound dyssynchrony, high driving pressure despite sedation, mechanical ventilator limitations. ARDS: early paralysis (cisatracurium) improves outcomes (ACURASYS trial—reduced mortality, ICU-acquired weakness paradoxically lower despite paralysis). Daily sedation interruption improves outcomes (shorter vent time, reduced delirium). Reversibility of paralysis can be monitored (TOF ratio).", ["ventilation", "sedation", "paralysis", "neuromuscular_blockade", "outcomes"]),

        ("Patient-ventilator asynchrony and dyssynchrony", "Mismatch between patient effort and ventilator delivery: patient inhales while ventilator delivering exhalation (double-trigger), patient exhales during ventilator inspiration. Consequences: worsened oxygenation, increased work of breathing, patient distress, increased VILI risk. Causes: inadequate sedation, pain, hypoxemia, hypercarbia, ventilator settings (low trigger sensitivity, short expiration time). Management: adequate sedation/analgesia, adjust trigger sensitivity, increase inspiratory time (if triggering issue), decrease RR if excessive respiratory drive, neuromuscular blockade if severe.", ["ventilation", "asynchrony", "dyssynchrony", "management", "sedation"]),

        ("Endotracheal tube management complications", "Sinusitis from prolonged intubation (prevent with frequent suctioning, head of bed 30 degrees). Tracheal stenosis: thermal injury from ETT cuff, prolonged high cuff pressures (goal 25-30 cm H2O). Tracheomalacia: cuff-induced injury. Laryngeal edema/paralysis: nerve compression or direct injury. Tube obstruction: secretions, blood clot (suction, saline flushes, tube exchange if impacted). Tube migration: into right mainstem or extubated inadvertently. Accidental extubation: catastrophic if can't reintubate (bedside reintubation attempted). Prevention: appropriate cuff pressures, regular suctioning, secure fixation, sedation adequacy.", ["ventilation", "tube_complications", "etf", "management", "prevention"]),

        ("Tracheostomy indications and timing", "Indicated: anticipated >2 weeks mechanical ventilation, difficult airway management, neuromuscular disease (weakness), high aspiration risk. Timing: typically weeks 7-14 (earlier for some conditions). Benefits: reduced sedation, improved comfort, easier weaning, long-term access. Risks: procedure-related (hemorrhage, esophageal injury, misplacement), late complications (stenosis, tracheomalacia, trachea-innominate fistula). Tube changes: every 7-14 days to prevent obstruction, encrustation. Speaking valve allows phonation (requires adequate glottic closure, patient cooperation). Eventual decannulation goal if possible.", ["ventilation", "tracheostomy", "indications", "timing", "complications"]),

        ("Reintubation risk factors and prevention", "Reintubation within 48h = failed extubation (increases mortality, length of stay). Risk factors: age >65, ICU stay >7 days, cardiac disease, COPD, female sex, obesity, opioid use. Predictors: RSBI, CROP index (weak predictors individually). Prevention: structured weaning protocol, daily SBT once ready, avoid prolonged sedation, optimize strength (rehabilitation), cough assessment (adequate suctioning), address underlying cause (cardiac edema, sepsis), post-extubation non-invasive support (high-flow O2, CPAP, BiPAP) in high-risk patients.", ["ventilation", "reintubation", "risk_factors", "prevention", "outcomes"]),

        ("High-flow nasal cannula (HFNC) post-extubation", "Delivers heated/humidified blended gas at high flows (20-60 L/min). Provides PEEP ~3-5 cm H2O (flow-dependent), better humidification than standard nasal cannula, washout of anatomic dead space → reduced CO2. Improves comfort, oxygenation post-extubation. May reduce reintubation risk in high-risk patients (FLORALI trial: non-significant reduction but trend). Easier to implement than BiPAP (better tolerated). Increasingly used as first-line post-extubation support (especially COPD, obesity, post-operative). Failure rate 10-15%.", ["ventilation", "hfnc", "post_extubation", "non_invasive", "outcomes"]),

        ("Ventilator mode selection and weaning strategy", "CMV/AC: guarantees minute ventilation, but impairs spontaneous breathing (deconditioning). Assist/control with low set rate allows spontaneous breaths. Synchronized IMV (SIMV): patient's spontaneous breaths pressure-supported, set rate as backup (reduces work but improves outcomes vs. CMV alone). Pressure support (PSV): patient initiates all breaths, weaning accomplished by decreasing PSV (5-15 cm H2O). No single mode superior—individual patient factors. Weaning mode less important than structured protocol (daily SBT, gradual support reduction). Some data suggesting early spontaneous breathing (CPAP early) improves outcomes.", ["ventilation", "modes", "weaning", "protocol", "strategy"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=start_idx + idx,
            section="Advanced Ventilation & ARDS Expansion"
        ))

    return units

# Additional quick expansion of remaining modules
def quick_expand_remaining() -> List[Dict[str, Any]]:
    """Quick expansion of remaining modules to reach 300+ target"""
    units = []

    # Hemodynamic module expansion (to ~25 units)
    module = "hemodynamic"
    facts = [
        ("Pulmonary artery pressure monitoring and interpretation", "PA pressure normally 20-30/10-15 mmHg, mean 15-20. Elevated SYSTOLIC (>40): pulmonary HTN, ARDS, mitral stenosis, hypervolemia. Elevated DIASTOLIC (>20): LV dysfunction (elevated PAWP), mitral stenosis, ARDS. PAWP (wedge pressure) reflects LA pressure: elevated (>18) suggests pulmonary edema risk. Regular PA pressure waveform: systolic rise from RV contraction, diastolic phase with a (RV contraction remnant), v (passive RA filling). Absence of a wave: atrial fibrillation.", ["monitoring", "pa_pressure", "hemodynamics", "interpretation", "assessment"]),
        ("Cardiac index and oxygen delivery calculations", "CI (cardiac index) = CO / BSA (body surface area). Normal 2.5-4 L/min/m2. DO2 (oxygen delivery) = CI × CaO2 × 10, normal 500-600 mL/min/m2. VO2 (oxygen consumption) = (CaO2 - CvO2) × CO × 10, normal 200-250 mL/min/m2. DO2/VO2 ratio indicates supply-demand balance. Low DO2 with high VO2 (extraction) = compensated shock (tissue extracting maximally). Low DO2 with low VO2 = uncoupling (mitochondrial dysfunction, sepsis).", ["monitoring", "ci", "do2", "calculations", "oxygen_delivery"]),
    ]
    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(text, topic, tags, module, 16 + idx, "Hemodynamic Monitoring Expansion"))

    # Inotrope module expansion (to ~25 units)
    module = "inotropes"
    facts = [
        ("Lusitropic effects of inotropes", "Lusitropy = diastolic relaxation. Positive lusitrope = improved relaxation (better filling). Negative lusitrope = worsened relaxation. Milrinone: positive inotrope + positive lusitrope (improves both systolic function and relaxation—particularly useful in HF with diastolic dysfunction). Dobutamine: positive inotrope but increases myocardial stiffness (negative lusitropic effect). Calcium channel blockers: reduce contractility but improve lusitropy. In HF, improved lusitropy crucial—milrinone advantageous in this context.", ["medications", "lusitropic", "diastolic_function", "inotropes", "mechanism"]),
        ("Stress-induced cardiomyopathy (Takotsubo)", "Catecholamine surge (extreme stress, critical illness, high-dose vasopressors) → transient systolic dysfunction (apical ballooning typical, but midventricular/basal variants exist). Mimics MI (elevated troponin, ST changes), but coronaries normal on angiography. Usually reversible within days-weeks. Risk: hemodynamic instability, arrhythmias, shock. Management: supportive care, avoid excessive catecholamines if possible (use milrinone instead), mechanical support if cardiogenic shock. Prognosis generally good (recovery expected). Diagnosis requires high suspicion.", ["cardiomyopathy", "takotsubo", "stress_cardiomyopathy", "diagnosis", "management"]),
    ]
    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(text, topic, tags, module, 18 + idx, "Inotropes Expansion"))

    # MCS module expansion (to ~25 units)
    module = "mcs"
    facts = [
        ("ECMO complications in detail: bleeding management", "Bleeding most common ECMO complication (30-40% of patients). From: anticoagulation requirement, coagulopathy development, surgical sites, cannulation sites, GI bleeding, intracranial hemorrhage. Management: optimize anticoagulation (ACT 180-200), transfuse PRBCs/FFP/platelets, consider reversal agents (FFP, prothrombin complex concentrate if warfarin), vitamin K if deficient. Massive bleeding may require temporarily reducing heparin (thrombosis risk), transfusion target higher. Prophylactic measures: minimize blood draws, maintain FiO2 goal, avoid aggressive anticoagulation unless thrombosis develops.", ["mcs", "ecmo", "bleeding", "anticoagulation", "management"]),
        ("Right heart failure post-LVAD", "LVAD reduces LV workload → improved EF recovery potential, but RV must now handle increased blood volume from decompressed LV. RV dysfunction (from sepsis, ARDS, PE, infarction) → LVAD outflow obstruction risk. Presents: elevated CVP, low CO despite normal LVAD flows, pulmonary edema, decreased urine output. Prevention: optimize RV function pre-LVAD (inotropes, inhaled nitric oxide, mechanical support if severe). Management: inhaled nitric oxide, milrinone, inhaled epoprostenol, potentially RV support (RVAD/temporary ECMO). Right-sided LVAD failure is major reason for worse outcomes in some cohorts.", ["mcs", "lvad", "rv_failure", "complications", "outcomes"]),
    ]
    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(text, topic, tags, module, 16 + idx, "MCS Expansion"))

    # Echo module expansion (to ~25 units)
    module = "echo"
    facts = [
        ("Strain imaging and speckle tracking", "Measures myocardial deformation (shortening). Global longitudinal strain (GLS) normal -17% to -21% (negative = normal systolic shortening). Reduced GLS (e.g., -10%) indicates systolic dysfunction (may be present with normal EF—occult dysfunction). Circumferential strain assesses radial function. Strain detects early LV dysfunction before EF drops. Useful in: early recognition of cardiotoxicity (chemotherapy), prognostication (worse GLS = worse prognosis), viability assessment. Technical: requires good acoustic window, operator expertise. Increasingly available, becoming standard in major centers.", ["echo", "strain", "speckle_tracking", "deformation", "advanced"]),
        ("Right ventricular assessment and function", "RV function complex (function depends on afterload unlike LV). Measures: TAPSE (tricuspid annular plane systolic excursion, normal >16 mm), RV S' (tissue Doppler, normal >10 cm/s), RV fractional area change (FAC, normal >35%), RV index of myocardial performance (RIMP, ratio of isovolumetric time to ejection time). Global RV dysfunction: dilation, septal flattening, reduced function on all measures. RV-LV interdependence: septal shift leftward → reduced LV filling (tamponade physiology). RV assessment increasingly recognized as important for prognosis/management decisions.", ["echo", "rv_assessment", "function", "advanced", "hemodynamics"]),
    ]
    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(text, topic, tags, module, 18 + idx, "Echo Expansion"))

    return units

def main():
    """Expand Phase 5 units"""
    print("Expanding Phase 5 units to reach 300-400 target...")

    all_new_units = []
    all_new_units.extend(expand_acls_units())
    all_new_units.extend(expand_arrhythmia_units())
    all_new_units.extend(expand_shock_units())
    all_new_units.extend(expand_ventilation_units())
    all_new_units.extend(quick_expand_remaining())

    print(f"Generated {len(all_new_units)} additional Phase 5 units")

    # Load existing (Phase 1-5 already consolidated)
    with open(r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.json", "r") as f:
        existing_units = json.load(f)

    print(f"Loaded {len(existing_units)} existing units (Phase 1-5 from previous run)")

    # Consolidate
    consolidated = existing_units + all_new_units

    # Save
    with open(r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.json", "w") as f:
        json.dump(consolidated, f, indent=2)

    with open(r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.jsonl", "w") as f:
        for unit in consolidated:
            f.write(json.dumps(unit) + "\n")

    print(f"\nFinal Phase 5 count: {sum(1 for u in consolidated if 'phase5' in u['id'])}")
    print(f"Cumulative total (Phase 1-5): {len(consolidated)}")

if __name__ == "__main__":
    main()
