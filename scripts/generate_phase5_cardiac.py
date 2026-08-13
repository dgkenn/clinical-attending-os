#!/usr/bin/env python3
"""
Generate Phase 5: Advanced Cardiac & Hemodynamics (300-400 units)
8 modules covering ACLS, arrhythmias, hemodynamic monitoring, shock, drugs, ventilation, MCS, and echo
"""

import json
import uuid
from datetime import datetime
from typing import List, Dict, Any

def generate_unit_id(module_name: str, index: int) -> str:
    """Generate unique unit ID"""
    return f"phase5_{module_name}_unit_{index}"

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
        "id": generate_unit_id(module_name, index),
        "text": text,
        "metadata": {
            "topic": topic,
            "topic_tags": topic_tags,
            "library": "anesthesiology_cardiac_advanced",
            "source_name": "phase5_cardiac_knowledge",
            "book": book,
            "section": section,
            "module": module_name,
            "created_at": datetime.now().isoformat(),
            "chunk_type": "fact"
        },
        "created_at": datetime.now().isoformat()
    }

def generate_acls_units() -> List[Dict[str, Any]]:
    """ACLS & Resuscitation (40-50 units)"""
    units = []
    module = "acls"

    facts = [
        # BLS vs ACLS
        ("BLS overview", "BLS (Basic Life Support) is compression-only CPR with hands-only emphasis. ACLS (Advanced Cardiac Life Support) adds medications (epinephrine, amiodarone, atropine), rhythm interpretation, and post-arrest care. Current guidelines emphasize early high-quality chest compressions: 100-120 compressions/min, 2-2.4 inches depth, allow full recoil.", ["acls", "resuscitation", "bls", "cpr", "rhythms"]),

        # Shockable rhythms
        ("Ventricular fibrillation (VF)", "VF is the most common initial rhythm in out-of-hospital cardiac arrest. Treatment: immediate CPR for 2 minutes, then defibrillate (immediate defibrillation if witnessed/in hospital). After ROSC, post-arrest care includes TTM and neurologic prognostication. VF deteriorates to asystole without intervention.", ["acls", "rhythms", "vf", "defibrillation", "resuscitation"]),

        ("Pulseless ventricular tachycardia (PVT)", "PVT is treated identically to VF. Give shock, then epinephrine 1 mg IV/IO every 3-5 minutes. Amiodarone 300 mg IV for first dose, then 150 mg for second. Continue CPR 2 min, reassess rhythm every 2 minutes. Consider reversible causes (5 H's and 5 T's).", ["acls", "rhythms", "pvt", "vt", "defibrillation", "medications"]),

        # Non-shockable rhythms
        ("Asystole management", "Asystole ('flatline') requires CPR and epinephrine 1 mg IV/IO every 3-5 minutes. Do NOT defibrillate. Amiodarone does not improve survival in asystole. Consider reversible causes: hypothermia, hyperkalemia, tension pneumothorax, cardiac tamponade, massive PE. Median survival is poor without early intervention.", ["acls", "rhythms", "asystole", "pea", "medications"]),

        ("Pulseless electrical activity (PEA)", "PEA is organized electrical activity without detectable pulse. CPR + epinephrine 1 mg every 3-5 min. No amiodarone. Goal is finding and treating reversible cause (tension pneumothorax, tamponade, massive PE, severe hypovolemia, toxic ingestion, severe acidosis). Survivability depends on underlying etiology.", ["acls", "rhythms", "pea", "resuscitation", "medications"]),

        # Medications
        ("Epinephrine in resuscitation", "Epinephrine 1 mg IV/IO every 3-5 minutes. Current evidence shows benefit mainly in witnessed VF/PVT with early defibrillation. For asystole/PEA, give first dose at 3-5 min, then every 3-5 min. Higher doses (>1 mg) do not improve outcomes. If no IV/IO access, can give via ETT but absorption is unpredictable.", ["acls", "medications", "epinephrine", "resuscitation", "pharmacology"]),

        ("Amiodarone dosing and indications", "Amiodarone 300 mg IV bolus for first episode of VF/PVT that's refractory to defibrillation and epinephrine. If recurrent, give 150 mg IV bolus after 3-5 min. Not recommended for asystole/PEA. Can also use for wide-complex tachycardia. Class III antiarrhythmic, blocks K+ channels. No clear survival benefit vs lidocaine.", ["acls", "medications", "amiodarone", "antiarrhythmics", "vf"]),

        ("Atropine in bradycardia", "Atropine 0.5-1 mg IV every 3-5 minutes (max 3 mg) for symptomatic bradycardia, especially AV block. Blocks acetylcholine at SA node and AV node. Effective in vagal (AV nodal block) but ineffective in infranodal block (wide QRS escape rhythm). For asystole, atropine is no longer routinely recommended in latest guidelines.", ["acls", "medications", "atropine", "bradycardia", "av_block"]),

        # Post-cardiac arrest
        ("Therapeutic hypothermia (TTM) indications", "Target temperature management (TTM) involves cooling to 32-36°C after ROSC for unconscious patients with VF/PVT cardiac arrest or blunt trauma. Goal is neuroprotection and reduction of cerebral metabolism. Cool for 24 hours, then slowly rewarm. Improves neurologic outcomes. Now called 'targeted temperature management' (any targeted temperature 32-36°C).", ["acls", "post_arrest", "ttm", "hypothermia", "neuroprotection"]),

        ("ROSC recognition and post-arrest care", "ROSC (Return of Spontaneous Circulation) = return of palpable pulse. After ROSC, goals are: 1) Optimize oxygenation/ventilation (PaO2 target 100-300 mmHg), 2) Target BP (SBP >90), 3) TTM (32-36°C x 24h), 4) Treat underlying cause (IHD, sepsis, etc), 5) Prognosticate (at 72h post-arrest, assess with biomarkers, neuroimaging). Early ICU admission critical.", ["acls", "post_arrest", "rosc", "resuscitation", "management"]),

        ("Prognostication after cardiac arrest", "Poor prognosis indicators: asystole, PEA, witnessed arrest >60 min, no ROSC in field, severely elevated lactate. At 72h post-TTM, use: absent pupillary light reflex, absent corneal reflex, extensor posturing, elevated NSE/S100B, diffusion-weighted imaging (DWI) showing extensive injury. Withdraw support if multiple poor predictors.", ["acls", "post_arrest", "prognosis", "neurologic", "biomarkers"]),

        # Special resuscitations
        ("Pregnancy cardiac arrest", "Perimortem cesarean delivery for maternal arrest: perform within 4 min (before ACLS team arrives if alone). Remove gravid uterus off vena cava→improve preload. Also: leftward uterine displacement if not delivering. Cause list differs (PE, amniotic fluid embolism, eclampsia, peripartum cardiomyopathy). Standard ACLS applies but with cesarean urgency.", ["acls", "special_situations", "pregnancy", "obstetrics"]),

        ("Hypothermia cardiac arrest", "Severe hypothermia (<30°C, especially <20°C) can appear clinically dead but still be salvageable ('no one is dead until they're warm and dead'). Manage carefully: avoid rough handling which can precipitate VF. Rewarm passively (remove wet clothes, insulate) or actively (ECMO/ECPR preferred for profound hypothermia). Standard ACLS applies.", ["acls", "special_situations", "hypothermia", "environmental", "resuscitation"]),

        ("Cardiac arrest from pulmonary embolism", "Causes PEA arrest. Treatment: aggressive CPR + epinephrine. Consider ECPR if available. Thrombolytics (alteplase 100 mg IV) can be given during CPR for suspected massive PE. Avoid decompensation if possible. Early CT PE protocol or echo may show RV dysfunction. Consider emergency thrombectomy if ECPR/mechanical support available.", ["acls", "special_situations", "pe", "pulmonary_embolism", "resuscitation"]),

        ("Cardiac arrest from tension pneumothorax", "Causes PEA. Treatment: needle decompression in 2nd ICS at midclavicular line (or 4th/5th ICS anterior axillary line) without waiting for imaging. Listen for air rush and pressure relief. Followed by chest tube. Standard ACLS + identify/treat primary cause. Prevent via cautious bag-mask ventilation.", ["acls", "special_situations", "tension_pneumothorax", "resuscitation"]),

        ("Poisoning-related cardiac arrest", "Causes vary (bradycardia, hypotension, VF). Classics: beta-blockers/calcium channel blockers (bradycardia, cardiogenic shock), tricyclic antidepressants (VT, hyperkalemia), cyanide (tissue hypoxia despite normal O2), carbon monoxide (VF). Treatment is ACLS + specific antidotes (glucagon for beta-blockers, calcium for CCB, hydroxocobalamine for cyanide, etc).", ["acls", "special_situations", "poisoning", "toxins", "resuscitation"]),

        # Team dynamics
        ("Team dynamics during code blue", "Designate clear team leader who directs compressions, medications, rhythm checks. Rotate compressors every 2 minutes to prevent fatigue-related compression inadequacy. Debrief after code (successful or unsuccessful) to identify improvement areas. Clear communication, closed-loop communication ('I heard you say...'), minimize interruptions to compressions. Use megacode simulation training.", ["acls", "team_dynamics", "communication", "leadership"]),

        ("When to stop resuscitation", "Continue resuscitation for minimum 20-30 minutes (or until ROSC achieved). Criteria to stop: unwitnessed arrest >30 min, asystole throughout, no reversible cause identified, DNR order present. Special populations (drowning, hypothermia) may warrant longer resuscitation. Consider extracorporeal CPR (ECPR) for young patients with reversible cause.", ["acls", "resuscitation", "ethical_decisions", "termination"]),

        # ECPR
        ("Extracorporeal CPR (ECPR) indications", "ECPR (VA-ECMO during CPR) improves outcomes in select patients: cardiac etiology of arrest, young age, witnessed arrest, <60 min CPR, reversible cause. Institutions with ECMO capabilities should consider ECPR pathway. Bridges to definitive treatment (angiography for STEMI, transplant, etc). Patient selection critical—exclude irreversible conditions.", ["acls", "ecpr", "ecmo", "va_ecmo", "advanced_support"]),

        ("ECPR technique and setup", "ECPR requires: ECMO team availability 24/7, peripheral or central cannulation (femoral cannula for IV access, venous return). Continue CPR during cannulation. VA-ECMO provides full hemodynamic support. Outcomes better in younger patients (<50 y/o) with reversible cause. Transfer to ECMO center may be necessary.", ["acls", "ecpr", "ecmo", "technique", "resuscitation"]),

        # Medications continued
        ("Sodium bicarbonate in arrest", "Indicated in specific conditions: tricyclic overdose (wide QRS, hypotension), severe hyperkalemia (peaked T waves, cardiac standstill risk), sustained local anesthetic toxicity. Goal is alkalinize to increase drug ionization and reduced seizure/arrhythmia risk. Give 1 mEq/kg IV, may repeat every 5-10 min. Monitor pH closely.", ["acls", "medications", "bicarbonate", "toxicology", "hyperkalemia"]),

        ("Calcium in resuscitation", "Give calcium gluconate 5-10 mL of 10% solution (or calcium chloride 2-4 mL of 10%) for: hyperkalemia (stabilizes myocardium), severe hypocalcemia (tetany, seizure risk), calcium channel blocker overdose (refractory shock). Works rapidly on myocardial membrane. Repeat every 10 min as needed. Use central line if possible (extravasation burns with chloride).", ["acls", "medications", "calcium", "hyperkalemia", "toxicology"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="ACLS & Resuscitation"
        ))

    return units

def generate_arrhythmia_units() -> List[Dict[str, Any]]:
    """Advanced Arrhythmia Management (50-70 units)"""
    units = []
    module = "arrhythmia"

    facts = [
        # Bradycardia
        ("Bradycardia definition and causes", "Bradycardia = HR <60 bpm. Causes: athlete's heart, increased vagal tone (sleep, Valsalva), hypothyroidism, hypothermia, increased ICP, medications (beta-blockers, CCB, digoxin), infiltrative diseases (amyloidosis, sarcoidosis), conduction system disease. Symptomatic bradycardia with signs of poor perfusion (hypotension, altered mental status, chest pain) requires treatment.", ["arrhythmias", "bradycardia", "causes", "rate_control"]),

        ("Sinus bradycardia", "Sinus bradycardia = regular rhythm with normal P wave morphology, rate <60 bpm. Differential includes normal variant, sleep, athletic conditioning, hypothermia, hypothyroidism, increased ICP. If symptomatic, treat with atropine or pacing. Requires ECG and rhythm strip confirmation.", ["arrhythmias", "bradycardia", "sinus_rhythm", "normal_variant"]),

        ("First-degree AV block", "PR interval >200 ms (>5 small squares) with every P wave followed by QRS. Benign, often asymptomatic, seen in athletes, may be vagal. No treatment unless symptomatic bradycardia develops. Monitor for progression to higher-degree block (rare). Normal finding in 1-2% of population.", ["arrhythmias", "av_block", "conduction", "benign"]),

        ("Second-degree AV block Type I (Wenckebach)", "Progressive PR prolongation until a P wave is dropped. Rhythm is irregular. Usually benign, often vagal. At or above AV node. If symptomatic or severe, atropine or pacing. May progress to complete heart block rarely. Check for beta-blocker or CCB use.", ["arrhythmias", "av_block", "wenckebach", "type_i"]),

        ("Second-degree AV block Type II (Mobitz II)", "Fixed PR interval with occasional P waves NOT followed by QRS (dropped beats). Usually at infranodal level (within or below His bundle). Ominous sign—high risk of progression to complete heart block. Usually requires pacing. Often symptomatic. Narrow QRS usually means block above His.", ["arrhythmias", "av_block", "mobitz", "type_ii", "ominous"]),

        ("Third-degree AV block (complete heart block)", "No AV conduction. P waves and QRS are independent. Narrow QRS escape (40-60 bpm, nodal) or wide QRS escape (20-40 bpm, infranodal). Nodal is more stable. Infranodal requires urgent pacing. Causes: infiltrative disease, Lyme disease, inferior MI, medications. Completely asymptomatic to severe syncope.", ["arrhythmias", "av_block", "complete_block", "chb", "pacing"]),

        ("Sick sinus syndrome", "Bradycardia-tachycardia syndrome: sinus bradycardia alternating with atrial fibrillation or atrial flutter, often with pauses/sinus arrest. Causes: aging, infiltrative disease (amyloidosis, sarcoidosis), cardiomyopathy, medications (digoxin, beta-blockers). Treatment: dual-chamber pacemaker (prevents bradycardia) + AV nodal blocking agent if needed for tachycardia.", ["arrhythmias", "bradycardia", "sick_sinus", "tachy_brady", "pacing"]),

        # Atropine
        ("Atropine mechanism and pharmacology", "Atropine blocks muscarinic acetylcholine receptors. Increases SA and AV nodal firing rates. Increases HR and speeds AV conduction. Anticholinergic side effects: mydriasis, dry mouth, urinary retention, CNS effects. Dose: 0.5-1 mg IV for bradycardia, max 3 mg. Ineffective in infranodal block (wide QRS escape).", ["medications", "atropine", "anticholinergic", "bradycardia"]),

        ("Atropine paradox", "Low doses of atropine (<0.5 mg) can paradoxically SLOW HR via central vagal stimulation. Use adequate doses (0.5-1 mg minimum) to avoid this. Once effective, repeat doses continue to increase HR. Useful in vagal bradycardia (neurocardiogenic syncope, vasovagal response) but not in infranodal block.", ["medications", "atropine", "paradox", "pharmacology"]),

        # Pacing
        ("Transcutaneous pacing indications", "For symptomatic bradycardia refractory to atropine, hypotensive with altered mental status or chest pain, severe AV block. Temporary measure while awaiting transvenous pacing or treating underlying cause. Painful—always sedate if possible. Confirm electrical capture (pacing spike) and mechanical capture (pulse with pacing). Demand mode if intrinsic rhythm.", ["pacing", "transcutaneous", "emergency", "bradycardia"]),

        ("Transvenous pacing technique", "Central line placement (internal jugular, subclavian, femoral) with pacing catheter. Advance to right atrium, then right ventricle (target apical endocardium). Establish capture threshold (lowest voltage ensuring 1:1 capture). Set rate (usually 60-80 bpm) and sensitivity. May be temporary (external wires) or permanent (implanted system). Risk of perforation, infection, lead fracture.", ["pacing", "transvenous", "temporary", "technique"]),

        # Narrow complex tachycardia
        ("Narrow complex tachycardia differential", "Narrow QRS (<120 ms, <3 small squares). Rhythmic (SVT, atrial flutter, atrial fibrillation, atrial tachycardia, AVNRT, AVRT) vs irregular (atrial fibrillation, atrial flutter with variable AV block). Differential includes: sinus tachycardia (P wave visible), AVNRT (50% of SVT, retrograde P in QRS or just after), AVRT (WPW, delta wave on baseline), atrial flutter (saw-tooth baseline), atrial tachycardia.", ["arrhythmias", "tachycardia", "narrow_complex", "svt"]),

        ("Supraventricular tachycardia (SVT) overview", "SVT = rapid regular narrow-complex rhythm originating above ventricles. Rate 150-250 bpm. Mechanism: AVNRT (50%, reentry in AV node), AVRT (30%, WPW), atrial tachycardia (20%). Presents with palpitations, chest discomfort, dyspnea, syncope. ECG shows regular narrow QRS. Initial treatment: vagal maneuvers, adenosine.", ["arrhythmias", "tachycardia", "svt", "regular"]),

        ("AVNRT (AV nodal reentrant tachycardia)", "Most common SVT (50% of cases). Reentry within AV node (dual pathways: fast and slow). Often appears with retrograde P wave within QRS or immediately after QRS. Presents suddenly with rapid HR 150-250 bpm. Diagnosis: ECG, EPS if needed. Treatment: adenosine (first-line), verapamil, diltiazem, beta-blockers.", ["arrhythmias", "tachycardia", "avnrt", "reentry"]),

        ("AVRT and Wolff-Parkinson-White (WPW)", "AVRT = accessory pathway (bypass tract) outside AV node enabling reentry. WPW = pathway present on baseline ECG (delta wave = slurred QRS upstroke, short PR interval). AVRT rate faster than AVNRT. Avoid beta-blockers/CCB that block AV node (forces conduction down bypass tract→VF risk). Use adenosine, ibutilide, or ablation. Definitive: RF ablation of pathway.", ["arrhythmias", "tachycardia", "avrt", "wpw", "accessory_pathway"]),

        ("Vagal maneuvers for SVT", "First-line for stable SVT: Valsalva (bear down ~15 sec), carotid massage (10 sec, unilateral, not in elderly/carotid stenosis), ice water to face. Success rate 20-40%. Work by increasing vagal tone, slowing AV nodal conduction, breaking reentry. If unsuccessful after 1-2 attempts, proceed to adenosine.", ["arrhythmias", "tachycardia", "svt", "treatment", "vagal"]),

        ("Adenosine for SVT", "Adenosine IV push 6-12 mg (or 3-6 mg if central line). Ultra-short half-life (~10 sec). Blocks AV node transiently→breaks AVNRT/AVRT/other reentry. Flushes with saline immediately after. Side effects: chest discomfort, flushing, dyspnea, transient asystole (normal). Contraindications: severe asthma/COPD (can cause bronchospasm), decompensated HF. May convert rhythm or unmask underlying rhythm (atrial flutter with AV block).", ["medications", "adenosine", "svt", "treatment", "av_node_block"]),

        ("Verapamil and diltiazem for SVT", "Both calcium channel blockers that slow AV nodal conduction. Verapamil 5-10 mg IV (repeat q 10 min). Diltiazem 0.25 mg/kg IV (usual 20-25 mg), repeat with higher dose if needed. Similar efficacy to adenosine (70-80% conversion). Can cause hypotension, bradycardia. Avoid in VT (paradoxically speeds conduction) or severe HF. Advantage over adenosine: longer duration.", ["medications", "verapamil", "diltiazem", "svt", "treatment"]),

        ("Beta-blockers for SVT", "Metoprolol 2.5-5 mg IV, esmolol 0.5-1 mg/kg IV, propranolol 0.5-1 mg IV. Slow AV node. Efficacy slightly lower than adenosine/verapamil. Useful for ongoing rate control post-conversion. Avoid in decompensated HF (negative inotrope), asthma/COPD. Contraindicated in WPW/AVRT (can facilitate conduction down accessory pathway).", ["medications", "beta_blockers", "metoprolol", "svt", "treatment"]),

        # Atrial fibrillation
        ("Atrial fibrillation overview", "AF = chaotic atrial depolarization without organized P waves. Irregular, often rapid ventricular response (no AV block) or controlled (<100 bpm). Causes: hypertension, CAD, cardiomyopathy, valvular disease, hyperthyroidism, pulmonary disease, sepsis. Complications: stroke (1-2% yearly, 5% if >75 y/o), HF. Treatment: rate control vs rhythm control.", ["arrhythmias", "tachycardia", "af", "irregular", "stroke_risk"]),

        ("Atrial flutter", "Atrial flutter = organized atrial activity with sawtooth baseline at ~300 bpm. Ventricular response depends on AV nodal conduction: 150 bpm (2:1 block), 100 bpm (3:1 block), irregular if variable block. Usually regular. Causes similar to AF. Often easier to convert than AF. Treatment: rate control (beta-blockers, CCB, digoxin) or rhythm control (cardioversion, amiodarone).", ["arrhythmias", "tachycardia", "flutter", "organized", "rate_control"]),

        ("Anticoagulation in atrial fibrillation", "CHA2DS2-VASc score predicts stroke risk. Score ≥1 in men, ≥2 in women → anticoagulation indicated. Options: warfarin (INR 2-3), DOAC (apixaban, rivaroxaban, dabigatran, edoxaban). In acute AF with hemodynamic instability, anticoagulate immediately (UFH → warfarin or DOAC). Rate control should be achieved first. Continue anticoagulation even if converted to NSR.", ["arrhythmias", "af", "anticoagulation", "stroke_prevention", "cha2ds2"]),

        ("Rate control vs rhythm control in AF", "Rate control goal: HR <110 bpm at rest, <130 bpm with activity. Agents: beta-blockers (metoprolol), CCB (diltiazem, verapamil), digoxin (slower onset, good for HFrEF). Rhythm control: amiodarone, flecainide, sotalol, dofetilide, dronedarone. Both strategies similar mortality (AFFIRM trial), but rate control is usually first-line due to fewer side effects. Rhythm control if HF, poor rate control tolerance.", ["arrhythmias", "af", "rate_control", "rhythm_control", "strategy"]),

        ("Cardioversion for atrial fibrillation", "Electrical (synchronized shock) or pharmacologic (amiodarone, ibutilide, flecainide). Indicated if hemodynamically unstable, new-onset AF (<7 days, low thrombus risk), or failed medical rate control. Sedate first if time permits. Anticoagulate before if AF >48 hours or unknown duration (to prevent thromboembolic events). Success rate ~70-90% for electrical.", ["arrhythmias", "af", "cardioversion", "treatment", "emergency"]),

        # Wide complex tachycardia
        ("Wide complex tachycardia differential", "QRS >120 ms (>3 small squares). Differential: VT (60-80% of cases), SVT with aberrancy (bundle branch block), WPW with AF, antidromic SVT. Approach: Brugada criteria, Vereckei algorithm, Josephson sign. If uncertain, treat as VT (safer). VT = hemodynamically unstable usually. SVT + aberrancy = usually stable.", ["arrhythmias", "tachycardia", "wide_complex", "vt", "svt"]),

        ("Ventricular tachycardia (VT) overview", "VT = rapid ventricular origin rhythm, rate 120-300 bpm. Monomorphic (same QRS morphology) or polymorphic. Hemodynamically unstable usually. Causes: acute MI (most common), old MI scar (re-entry), cardiomyopathy, channelopathies (Long QT, Brugada). EPS/ICD indicated for sustained VT or recurrent. Acute treatment: lidocaine, amiodarone, synchronized cardioversion.", ["arrhythmias", "tachycardia", "vt", "ventricular", "emergency"]),

        ("Torsades de pointes", "Polymorphic VT with twisting appearance around baseline. Often triggered by prolonged QT interval (Long QT syndrome, medications like dofetilide/amiodarone, electrolyte abnormality). Causes syncope, SCD. Initial treatment: defibrillate if unstable. Then: correct QT (magnesium, correct hypokalemia, discontinue QT-prolonging drugs). Beta-blockers or pacing if pause-dependent.", ["arrhythmias", "tachycardia", "torsades", "long_qt", "polymorphic"]),

        ("Long QT syndrome", "Inherited (LQTS 1-17) or acquired (medications, electrolytes). QTc >440 ms males, >460 ms females. Risk of torsades/SCD. Types: LQT1 (swimming-triggered, beta-blocker responsive), LQT2 (auditory triggers, beta-blocker responsive), LQT3 (sleep/rest-triggered, sodium channel blocker responsive). Management: beta-blockers, avoid QT-prolonging drugs, implantable defibrillators (ICD) for high-risk.", ["arrhythmias", "inherited", "long_qt", "lqts", "sudden_death"]),

        ("Brugada syndrome", "Inherited sodium channelopathy. ECG shows type 1 pattern: ST elevation in V1-V2 with negative T wave (coved ST). Risk of VF, SCD, especially at rest/fever. Management: ICD if high-risk (symptomatic, multiple risk factors). Avoid fever (antipyretics), certain medications (flecainide, TCAs). Genetic counseling. Affects ~1:2000 worldwide, more common in Asian descent.", ["arrhythmias", "inherited", "brugada", "sudden_death", "sodium_channel"]),

        # Antiarrhythmic drugs
        ("Class I antiarrhythmics (sodium channel blockers)", "Ia: quinidine, procainamide, disopyramide (slow conduction, prolonged APD, widened QRS). Ib: lidocaine, mexiletine (shorten APD). Ic: flecainide, propafenone (minimal APD change, marked conduction slowing). Ia useful for AF/VT, but narrow therapeutic window. Ib useful for VT post-MI. Ic very effective for SVT, used in structurally normal heart.", ["medications", "antiarrhythmics", "class_i", "sodium_channel", "conduction"]),

        ("Class II antiarrhythmics (beta-blockers)", "Slow AV nodal conduction, increase AV nodal refractoriness. Useful for SVT, AF (rate control), VT post-MI. Agents: propranolol, metoprolol, esmolol, labetalol. Avoid in severe bradycardia, decompensated HF, asthma. Efficacy similar to verapamil for SVT. Post-MI, beta-blockers reduce mortality.", ["medications", "antiarrhythmics", "class_ii", "beta_blockers", "rate_control"]),

        ("Class III antiarrhythmics (potassium channel blockers)", "Prolong APD and refractory period. Amiodarone (also has class I/II/IV effects), sotalol, dofetilide, ibutilide. Amiodarone is most effective but most toxic (pulmonary toxicity, hepatotoxicity, thyroid, corneal deposits). Sotalol is easier to use but QT prolongation risk. Dofetilide for AF. Ibutilide for acute conversion.", ["medications", "antiarrhythmics", "class_iii", "potassium_channel", "apd_prolongation"]),

        ("Class IV antiarrhythmics (calcium channel blockers)", "Verapamil, diltiazem. Slow AV nodal conduction, increase refractoriness. Useful for SVT, AF (rate control). Avoid in VT/WPW with AF (paradoxically speeds conduction down accessory pathway). Negative inotropic effect—use carefully in HF. IV dose is rapid; oral for chronic rate control.", ["medications", "antiarrhythmics", "class_iv", "calcium_channel", "av_block"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Advanced Arrhythmia Management"
        ))

    return units

def generate_hemodynamic_monitoring_units() -> List[Dict[str, Any]]:
    """Invasive Hemodynamic Monitoring (40-60 units)"""
    units = []
    module = "hemodynamic"

    facts = [
        # CVP
        ("Central venous pressure (CVP) normal values", "Normal CVP = 2-8 mmHg (or 3-11 cm H2O). Reflects right atrial pressure, estimates RV preload. Elevated CVP (>12 mmHg) suggests: volume overload, RV dysfunction, pulmonary HTN, tamponade, constrictive pericarditis. Low CVP (<2 mmHg) suggests hypovolemia. Trends more useful than single values. Measure at level of right atrium (mid-axillary line at 4th-5th ICS).", ["monitoring", "cvp", "hemodynamics", "preload", "assessment"]),

        ("CVP waveform analysis", "Normal CVP trace: a (atrial contraction), c (ventricular contraction/tricuspid bulge), x (atrial relaxation), v (passive atrial filling), y (atrial emptying into RV). Prominent a wave: canon a wave (simultaneous atrial-ventricular contraction in JVD, arrhythmias), hypervolemia. Absent a wave: atrial fibrillation. Elevated x descent: tamponade (paradoxical BP drop). Elevated y descent: restrictive pathology.", ["monitoring", "cvp", "waveform", "hemodynamics", "physiology"]),

        # Swan-Ganz
        ("Swan-Ganz catheter overview", "Pulmonary artery catheter (PAC) measures: CVP (RAP), RV pressure, pulmonary artery pressure, PAWP (wedge/occlusive pressure), mixed venous O2 saturation (SvO2), cardiac output. Normal: PAWP 8-15 mmHg (reflects LV preload), PA pressure 20-30/10-15 mmHg. Allows calculation of SVR, PVR, CI. Controversial—no mortality benefit, but useful for hemodynamically unstable patients.", ["monitoring", "swan_ganz", "pac", "hemodynamics", "cardiac_output"]),

        ("PAWP (pulmonary artery wedge pressure)", "Reflects left atrial pressure = LV preload. Normal 8-15 mmHg. Elevated PAWP (>18 mmHg) = pulmonary edema risk. Low PAWP (<8 mmHg) = hypovolemia. Elevated PAWP + low CO = cardiogenic shock (afterload reduction needed). Low PAWP + low CO = hypovolemic shock (fluids needed). Equilibration reflects: no PA branch rupture, tip in West zone III (blood flow around catheter).", ["monitoring", "swan_ganz", "pawp", "wedge_pressure", "preload"]),

        ("Cardiac output measurement", "Thermodilution: inject cold saline (10 mL normal saline at 0°C) into RA, measure temperature change downstream in PA. CO = volume injected × temperature change / area under curve. Normal CO = 4-6 L/min, CI = 2.5-4 L/min/m2. Trends useful; absolute values depend on technique. Continuous CO monitoring available.", ["monitoring", "cardiac_output", "thermodilution", "hemodynamics", "technique"]),

        ("Fick equation for cardiac output", "CO = (VO2) / (CaO2 - CvO2), where VO2 = oxygen consumption, CaO2 = arterial O2 content, CvO2 = venous O2 content. Requires arterial and mixed venous blood gases. More accurate than thermodilution in low-flow states (cardiogenic shock). VO2 can be measured (O2 consumption) or estimated. Less commonly used in acute setting but gold standard for accuracy.", ["monitoring", "cardiac_output", "fick_equation", "oxygen_delivery"]),

        # Calculations
        ("SVR (systemic vascular resistance) calculation", "SVR = (MAP - CVP) / CO × 80, units mmHg·min/L. Normal SVR = 800-1200 mmHg·min/L. Elevated SVR (>1500): septic shock (late), cardiogenic shock, hypertensive crisis. Low SVR (<500): septic shock (early), anaphylaxis, cirrhosis, high cardiac output states. SVR helps guide vasopressor choice. SvR = (PAWP - CVP) / CI × 80 (using cardiac index).", ["calculations", "svr", "hemodynamics", "vascular_resistance", "shock"]),

        ("PVR (pulmonary vascular resistance) calculation", "PVR = (MPAP - PAWP) / CO × 80, units mmHg·min/L. Normal PVR = 40-150 mmHg·min/L. Elevated PVR = pulmonary HTN (from any cause). Key determination of RV afterload. Acute increase in PVR (PE, ARDS) can cause RV dysfunction. Decreased with inhaled nitric oxide (iNO), sildenafil, epoprostenol. Affects RV function and prognosis.", ["calculations", "pvr", "hemodynamics", "pulmonary_vascular", "rh"]),

        # Specific conditions
        ("Systemic vascular resistance in shock states", "Cardiogenic shock: elevated SVR + low CO (compensatory vasoconstriction). Septic shock: biphasic—early high CO low SVR, late low CO high SVR. Hypovolemic shock: elevated SVR. Anaphylactic shock: low SVR + low CO acutely, then low SVR high CO. Understanding SVR helps select therapy: cardiogenic→afterload reduction; septic→fluids + vasopressor.", ["shock", "svr", "hemodynamics", "diagnosis", "treatment"]),

        ("Diastolic dysfunction patterns", "Type I (impaired relaxation): elevated PAWP, elevated LAP, prolonged DFT. Type II (pseudonormal): PAWP and diastolic pressures appear normal, but restrictive pattern on echo (E/A >1). Type III (restrictive): markedly elevated PAWP, steep x descent, shortened DFT, atrial fibrillation common. Measured via echo (E/A ratio, tissue Doppler) or Swan-Ganz pressure tracings.", ["monitoring", "diastolic_function", "hemodynamics", "echo", "assessment"]),

        ("Tamponade physiology", "Pericardial fluid accumulation → equalization of RA, RV, PA diastolic, and PAWP pressures (all ~20 mmHg in severe tamponade). Beck's triad: elevated JVP, muffled heart sounds, hypotension. Pulsus paradoxus: SBP drops >10 mmHg with inspiration. Echo shows diastolic RV collapse, RA collapse, swinging heart. Swan-Ganz shows plateau pattern (square root sign). Treatment: pericardiocentesis.", ["shock", "tamponade", "pericardial", "hemodynamics", "emergency"]),

        ("Constrictive pericarditis hemodynamics", "Pericardium restricts filling at end-diastole. Swan-Ganz shows: elevated and equal diastolic pressures, prominent y descent (not x), square root sign (early diastolic dip → plateau). Dip-plateau pattern on ventricular pressure. Discordance of RV and LV systolic pressures (RV >LV systolic). Echo shows thickened pericardium, septal bounce, respiratory variation. Cardiac MRI/CT for imaging. Treatment: pericardiectomy.", ["shock", "constrictive", "pericarditis", "hemodynamics", "restriction"]),

        # Non-invasive
        ("Transthoracic echocardiography for hemodynamics", "Non-invasive assessment: EF, wall motion, valve function, E/A ratio (diastolic function), TR jet velocity (RV pressure estimation = 4V^2), IVC diameter (CVP estimation). Limitations: operator-dependent, acoustic window limited (obesity, COPD). Ideal for initial assessment, trending volume status. Can estimate CO via stroke volume × HR.", ["monitoring", "echo", "tte", "non_invasive", "hemodynamics"]),

        ("Tissue Doppler for diastolic function", "Peak E velocity (early filling), peak A velocity (atrial kick). E/A ratio normal 1-2. E/e' ratio correlates with PAWP (>14 suggests elevated PAWP). Tissue Doppler s' (systolic velocity) reflects longitudinal function. e' reduced in diastolic dysfunction. Helps differentiate restrictive from impaired relaxation patterns. More specific than conventional Doppler.", ["monitoring", "echo", "tissue_doppler", "diastolic", "function"]),

        ("NICOM (non-invasive cardiac output monitoring)", "Bioreactance technology measures whole-body electrical conductivity changes with cardiac ejection. Non-invasive (electrodes on thorax). Continuous CO/CI monitoring. Less accurate than thermodilution in low-flow states but useful for trending. No calibration needed. Useful in ICU for hemodynamic management. FDA approved for adult/pediatric use.", ["monitoring", "nicom", "cardiac_output", "non_invasive", "real_time"]),

        ("Bioimpedance for hemodynamics", "Measures thoracic electrical impedance. Provides SV, CO, SVR, fluid status estimates. Trendy in operating room for hemodynamic optimization. Less accurate than invasive or NICOM. Subject to positioning, patient factors. Useful for continuous monitoring and guiding fluid therapy. Integration into hemodynamic management protocols ongoing.", ["monitoring", "bioimpedance", "hemodynamics", "or", "fluid_management"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Invasive Hemodynamic Monitoring"
        ))

    return units

def generate_shock_units() -> List[Dict[str, Any]]:
    """Shock Physiology Deep Dive (50-70 units)"""
    units = []
    module = "shock"

    facts = [
        # Cardiogenic shock
        ("Cardiogenic shock definition", "Tissue hypoperfusion from inadequate cardiac pumping. CO <2.2 L/min/m2 and PAWP >18 mmHg. Clinical: hypotension, oliguria, altered mental status, cool/clammy skin, elevated lactate. Causes: acute MI (most common), heart failure exacerbation, myocarditis, cardiomyopathy, valvular emergency, arrhythmia. Mortality 40-50% despite therapy. Requires prompt diagnosis and intervention.", ["shock", "cardiogenic", "definition", "hemodynamics", "mortality"]),

        ("Cardiogenic shock from acute MI", "Anterior MI most common (LAD territory). RV infarction can cause isolated cardiogenic shock (see below). Pathophysiology: necrotic myocardium loses contractility → reduced CO → hypotension → coronary hypoperfusion → worsened ischemia. Early revascularization (PCI/CABG) critical. Temporary support devices (IABP, Impella, ECMO) bridge to definitive therapy. Inotropes for bridge only.", ["shock", "cardiogenic", "ami", "mi", "revascularization"]),

        ("RV infarction physiology", "Inferior wall MI extends into RV (50% of inferior MIs, 10% have RV shock). RV depends on preload. Treatment: aggressive fluid resuscitation (opposite of LV failure). DO NOT give nitroglycerin (preload reducer—worsens RV cardiogenic shock). Right-sided ECG shows ST elevation in V4R. Swan-Ganz shows elevated RA pressure, low PAWP. Pacing if bradycardic. RV mechanical support if severe (IABP ineffective).", ["shock", "cardiogenic", "rvi", "rv_infarction", "fluid_resuscitation"]),

        ("Mechanical complications of MI", "Acute mitral regurgitation (papillary muscle rupture), acute VSD (septal rupture), free wall rupture (rapidly fatal). Echo shows: MR = systolic jet; VSD = left-to-right shunt, peak CW signal; FWR = pericardial effusion/tamponade. Management: urgent surgery for VSD/papillary rupture. Afterload reduction (nitroprusside) + inotropes temporizes. IABP/ECMO for bridge. High mortality (50-90%). Early recognition critical.", ["shock", "mechanical_complications", "mi", "acute_mr", "vsd", "surgery"]),

        ("Management algorithm for cardiogenic shock", "1) Optimize preload (euvolemia per PAWP), 2) Reduce afterload (vasodilators, ACE-I/ARB), 3) Improve contractility (inotropes), 4) Revascularize (PCI/CABG if CAD), 5) Consider mechanical support (IABP, Impella, VA-ECMO). Inotropes: dobutamine (inotropy + vasodilation), milrinone (inodilator), dopamine (inotrope + vasoconstrictor). Vasopressors: norepinephrine, epinephrine. Outcomes better with early intervention.", ["shock", "cardiogenic", "algorithm", "management", "inotropes"]),

        # Hypovolemic shock
        ("Hypovolemic shock pathophysiology", "Acute volume loss (hemorrhage, dehydration, burns, peritonitis) → reduced preload → reduced SV → reduced CO → hypotension. CO and PAWP both low. SVR elevated (compensatory). Clinical: tachycardia, tachypnea, hypotension, cool skin, oliguria, altered mental status. Lactate elevated. Treatment: aggressive fluid resuscitation (goal normalization of perfusion markers).", ["shock", "hypovolemic", "hemorrhage", "fluid_resuscitation", "hemodynamics"]),

        ("Hemorrhagic shock classification", "Class I: <15% blood volume loss (750 mL), normal BP/HR, minimal symptoms. Class II: 15-30% loss (750-1500 mL), tachycardia (100-120), anxiety. Class III: 30-40% loss (1500-2000 mL), tachycardia >120, hypotension, altered mental status. Class IV: >40% loss (>2000 mL), severe shock, altered mental status, near-death. Requires massive transfusion protocol (1:1:1 PRBC:FFP:platelets ratio).", ["shock", "hypovolemic", "hemorrhage", "classification", "transfusion"]),

        ("Fluid resuscitation endpoints in shock", "Goals: MAP >65 mmHg, urine output 0.5-1 mL/kg/h, lactate clearance >10% over 6h, improved mental status. Avoid over-resuscitation (increased mortality in sepsis/ARDS—permissive hypotension concept). Use balanced crystalloids (LR) vs normal saline (hyperchloremic acidosis risk). Early goal-directed therapy (EGDT) in sepsis: ScvO2 >70%, urine output, lactate trending down.", ["shock", "resuscitation", "endpoints", "monitoring", "fluid_management"]),

        # Distributive shock
        ("Septic shock overview", "Infection + organ dysfunction + refractory hypotension despite fluid resuscitation. Caused by gram-positive, gram-negative, fungi, or viral pathogens. Pathophysiology: endotoxin/pathogen toxins → TLR activation → massive cytokine release (TNF, IL-1, IL-6) → endothelial dysfunction, vasodilation, increased capillary permeability, mitochondrial dysfunction. Mortality 30-40% despite antibiotics/support.", ["shock", "septic", "infection", "sepsis", "cytokine"]),

        ("Sepsis-3 definitions", "Sepsis = infection + SIRS (fever, tachycardia, tachypnea, elevated WBC or left shift). Severe sepsis = sepsis + organ dysfunction. Septic shock = sepsis + hypotension refractory to fluid resuscitation (requiring vasopressors) + elevated lactate (tissue hypoperfusion). qSOFA (quick SOFA): altered mental status, systolic BP <100, RR >22—high risk of poor outcome.", ["sepsis", "definitions", "sirs", "organ_dysfunction", "septic_shock"]),

        ("Anaphylactic shock", "IgE-mediated type I hypersensitivity: mast cell/basophil degranulation → histamine/tryptase release. Presents with urticaria, angioedema, bronchospasm, hypotension, cardiovascular collapse. Triggers: medications (penicillin, NSAIDs, ACE-I), foods, latex, hymenoptera stings. Pathophysiology: vasodilation + increased vascular permeability. Treatment: IM epinephrine (0.3-0.5 mg IM, repeat q 15 min) immediate. IV access, fluids, antihistamines, corticosteroids.", ["shock", "anaphylactic", "anaphylaxis", "hypersensitivity", "emergency"]),

        # Obstructive shock
        ("Obstructive shock classification", "Mechanical obstruction to blood flow: PE (pulmonary embolism), tension pneumothorax, cardiac tamponade, aortic dissection, massive ascites, abdominal compartment syndrome. Characterized by elevated SVR (compensatory), low CO, elevated PAWP (if LV compression involved), high mortality. Treatment: relieve obstruction (thrombolysis/thrombectomy, needle decompression, pericardiocentesis, aortic imaging).", ["shock", "obstructive", "mechanical", "obstruction", "treatment"]),

        ("PE causing cardiogenic shock", "Massive PE causes sudden increase in RV afterload → RV dysfunction → CO collapse. Presents with sudden hypotension, altered mental status, elevated JVP, RV gallop. Echo shows RV dilation, elevated TR velocity, septal flattening. Chest X-ray may show Hampton's hump (wedge opacity), oligemic areas. Treatment: immediate thrombolysis (alteplase 100 mg) vs thrombectomy vs ECPR if available. Anticoagulation if stable.", ["shock", "obstructive", "pe", "pulmonary_embolism", "rv_failure"]),

        ("Tension pneumothorax", "Air in pleural space under pressure → lung collapse + mediastinal shift. Presents with acute dyspnea, unilateral absent breath sounds, hypotension, elevated JVP, tracheal deviation (late). Causes: blunt/penetrating trauma, mechanical ventilation (barotrauma), spontaneous (COPD blebs, tall thin males). Treatment: needle decompression (2nd ICS midclavicular line) BEFORE imaging, then chest tube. Immediate relief expected.", ["shock", "obstructive", "tension_pneumothorax", "trauma", "emergency"]),

        ("Aortic dissection shock", "Acute aortic dissection (type A) can cause shock from: pericardial rupture (tamponade), acute aortic regurgitation, MI (if dissection involves coronary ostia), aortic rupture. Presents with sudden severe chest pain, hypotension, unequal arm BPs, aortic regurgitation murmur. CT angiography or TEE for diagnosis. Type A requires emergency surgery. Avoid vasodilators alone (reflex tachycardia). Use beta-blockers first.", ["shock", "obstructive", "aortic_dissection", "hypertensive_emergency", "surgery"]),

        # Mixed shock
        ("Mixed shock pathophysiology", "Common in ICU: sepsis + MI (sepsis-induced cardiomyopathy), sepsis + severe anemia, post-operative hemorrhage + sepsis. Requires multimodal approach: fluids, antibiotics, vasopressors, inotropes, source control. Decisions: when to decrease fluids? When to add inotropes? When to add vasopressors? Serial reassessment critical. Often worst prognosis (combined organ failure).", ["shock", "mixed", "multifactorial", "icu", "management"]),

        # Lactate
        ("Lactate as prognostic marker", "Elevated lactate (>2 mmol/L) indicates anaerobic metabolism (tissue hypoperfusion). Lactate clearance (>10% over 6h) associated with better survival. Persistent hyperlactemia despite fluids/vasopressors = worse prognosis. Lactate >5 mmol/L = concern for inadequate perfusion. Serial measurement more useful than single value. Renal failure, liver disease, metformin also increase lactate.", ["shock", "lactate", "biomarker", "prognosis", "tissue_perfusion"]),

        # Microcirculation
        ("Microcirculatory dysfunction in sepsis", "Despite macroscopic normalization of CO/BP, microcirculation remains dysfunctional: shunting, capillary closure, heterogeneous flow. Results in tissue hypoperfusion despite normal lactate sometimes. Direct observation (sublingual capillary microscopy) shows sluggish/absent capillary flow. Treatment: aggressive fluid resuscitation, vasopressors (norepinephrine), inotropes, nitric oxide inhibitors being investigated.", ["sepsis", "microcirculation", "capillary_flow", "tissue_perfusion", "dysfunction"]),

        # Refractory shock
        ("Refractory shock management", "Shock unresponsive to fluids and single vasopressor. Consider: additional vasopressor (epinephrine), inotrope (dobutamine, milrinone), mechanical support (IABP, Impella, VA-ECMO), steroids (if refractory septic shock), immunotherapy (if fungal/atypical infections). Also reassess for: missed diagnosis (endocarditis, pericarditis, adrenal insufficiency), ongoing losses (hemorrhage, GI bleed), source control failure.", ["shock", "refractory", "resistant", "escalation", "support"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Shock Physiology Deep Dive"
        ))

    return units

def generate_inotrope_vasopressor_units() -> List[Dict[str, Any]]:
    """Inotropes, Vasopressors, Vasodilators (50-70 units)"""
    units = []
    module = "inotropes"

    facts = [
        # Dopamine
        ("Dopamine overview and dose-dependent effects", "Dopamine (DA) is a catecholamine precursor to norepinephrine. Dose-dependent effects: 1-2 mcg/kg/min = renal vasodilation (DA1 receptor, increases renal blood flow, diuresis). 2-5 mcg/kg/min = cardiac effects (DA1 + beta-1 stimulation, increased HR + contractility, mild vasodilation). 5-10 mcg/kg/min = alpha-1 activation (vasoconstriction, increased SVR). >10 mcg/kg/min = predominantly alpha (peripheral vasoconstriction). Tachyphylaxis common.", ["medications", "dopamine", "catecholamines", "dose_dependent", "vasopressor"]),

        ("Dopamine 'renal dose' controversy", "Low-dose dopamine (2-5 mcg/kg/min) was historically used to preserve renal perfusion in shock. However, multiple RCTs show no benefit for renal protection, no mortality benefit, increased arrhythmia risk. Current recommendation: do NOT use 'renal dose' dopamine—use fluids + appropriate vasopressor instead. Beta-1 effects often cause tachycardia (unfavorable).", ["medications", "dopamine", "renal_dose", "controversy", "deprecated"]),

        # Dobutamine
        ("Dobutamine mechanism", "Synthetic catecholamine with combined beta-1 (inotropy), beta-2 (vasodilation), and mild alpha-1 effects. Increases contractility + decreases afterload (useful in cardiogenic shock). Beta-2 effect causes systemic and pulmonary vasodilation. Often used with norepinephrine to maintain BP while reducing afterload. Increases myocardial O2 demand (concern in ischemia). Tachycardia common. May worsen hypotension if given alone.", ["medications", "dobutamine", "inotrope", "inotropic_agent", "afterload_reduction"]),

        ("Dobutamine dosing and indications", "Dose: 2.5-20 mcg/kg/min IV infusion (typical 5-10 mcg/kg/min). Used for cardiogenic shock (reduced EF, preserved BP), low-output heart failure, septic shock (if CO still low after fluids/pressors). Careful in CAD (increases myocardial O2 demand, may precipitate ischemia). Tolerance develops quickly (tachyphylaxis). Combination with norepinephrine often needed. Not used in hypertensive crisis.", ["medications", "dobutamine", "dosing", "cardiogenic_shock", "indications"]),

        # Milrinone
        ("Milrinone mechanism and advantages", "Phosphodiesterase-3 inhibitor → increases cAMP → positive inotropic + lusitrophic (improves diastolic relaxation) + systemic vasodilation. Unique in that it improves diastolic function (unlike dopamine/dobutamine which worsen relaxation). Useful in diastolic HF, post-operative HF. Systemic vasodilation may require concurrent vasopressor. Does NOT increase myocardial O2 demand (advantage in ischemia). Hypotension common.", ["medications", "milrinone", "inotrope", "pde3", "lusitrophic"]),

        ("Milrinone dosing and indications", "Dose: loading bolus 50 mcg/kg over 10 min (optional, if time permits), then 0.25-0.75 mcg/kg/min infusion. Used for low-output heart failure + diastolic dysfunction, cardiogenic shock (combined with vasopressor), septic shock refractory to dobutamine. Hypotension requires norepinephrine concurrent use. Risk of atrial/ventricular arrhythmias. Useful post-operatively if poor diastolic function.", ["medications", "milrinone", "dosing", "heart_failure", "diastolic"]),

        # Norepinephrine
        ("Norepinephrine mechanism and first-line status", "Norepinephrine (NE) = mixed alpha-1 + beta-1 catecholamine. Dose-dependent: at low doses, beta-1 effects predominate (inotropy, mild HR increase); at high doses, alpha-1 predominates (vasoconstriction). Increases MAP and SVR. Does NOT increase myocardial O2 demand as much as epinephrine. Current first-line vasopressor for septic/cardiogenic shock per Surviving Sepsis guidelines. Preferred over dopamine (lower arrhythmia risk).", ["medications", "norepinephrine", "vasopressor", "catecholamine", "first_line"]),

        ("Norepinephrine dosing and target", "Dose: 0.01-0.2 mcg/kg/min IV infusion (typical 0.05-0.2 mcg/kg/min). Target MAP >65 mmHg. Central line preferred (extravasation causes tissue necrosis). Often combined with inotrope (dobutamine, milrinone) for cardiogenic shock. Risk of hypertension, reflex bradycardia if MAP overshoots. Allows weaning of other pressors as underlying condition improves.", ["medications", "norepinephrine", "dosing", "map_target", "technique"]),

        # Epinephrine
        ("Epinephrine mechanism", "Mixed alpha-1 + beta-1 + beta-2 catecholamine. At low doses, beta effects (inotropy, some vasodilation). At high doses, alpha-1 effects predominate (vasoconstriction, increased SVR). Increases heart rate and myocardial O2 demand significantly. Less favored than norepinephrine for shock (due to tachycardia, increased MVO2, potential myocardial ischemia). Reserved for refractory shock or intra-operative use.", ["medications", "epinephrine", "catecholamine", "vasopressor", "inotrope"]),

        ("Epinephrine dosing and indications", "Dose: 0.05-0.5 mcg/kg/min IV infusion (typical 0.1-0.3 mcg/kg/min). Used for refractory septic shock (second-line, after NE/other agents), intra-operative hypotension, anaphylaxis (IM 0.3-0.5 mg). Combined inotropic/vasopressor effect. Risk of hypertension, tachycardia, SVT, myocardial ischemia. Monitor lactate carefully (epinephrine may increase it despite improved BP).", ["medications", "epinephrine", "dosing", "refractory_shock", "anaphylaxis"]),

        # Phenylephrine
        ("Phenylephrine mechanism", "Pure alpha-1 agonist → vasoconstriction, increased SVR, increased MAP. NO beta effects (no inotropic action, no increase in HR). Thus MAP rises but CO may fall (reflex bradycardia via baroreceptors). Used when pure vasoconstriction needed without inotropic effect (e.g., hypotension in setting of high CO state, or in tachy-arrythmic patients). Useful post-operative for hypertension.", ["medications", "phenylephrine", "alpha_agonist", "vasopressor", "pure_vasoconstriction"]),

        ("Phenylephrine dosing and indications", "Dose: 0.5-1.4 mcg/kg/min IV infusion (typical 0.5-1 mcg/kg/min). Or IV boluses of 200 mcg (push) for acute hypotension. Target MAP >65 mmHg. Used for post-operative hypotension (sympathectomy from anesthesia), septic shock refractory to NE (add as second agent), anaphylaxis (secondary to epinephrine). Risk of reflex bradycardia, decreased CO (not ideal in cardiogenic shock). Better than dopamine for selective vasoconstriction.", ["medications", "phenylephrine", "dosing", "post_operative", "indications"]),

        # Vasopressin
        ("Vasopressin mechanism and clinical use", "Vasopressin (antidiuretic hormone) acts via V1 and V2 receptors. V1 activation → vasoconstriction (via G-protein coupled receptor, direct smooth muscle contraction). V2 activation → increased aquaporin-2 in kidney (water reabsorption). Used as second-line vasopressor in refractory septic shock. Dose: 0.03-0.04 units/min (fixed dose, not weight-based). Often combined with norepinephrine. Low endogenous vasopressin levels in sepsis.", ["medications", "vasopressin", "adh", "vasopressor", "septic_shock"]),

        ("Vasopressin benefits and limitations", "Benefits: fixed dose (no titration needed), combined with other pressors, may reduce norepinephrine requirement. Limitations: no inotropic effect, non-selective vasoconstriction (risk of peripheral/splanchnic ischemia), increased mortality risk if doses exceed 0.04 units/min, tachyphylaxis after 24-48h. Current recommendation: use as second-line or add-on to NE, not first-line. Terlipressin (longer-acting) available in some countries.", ["medications", "vasopressin", "benefits", "limitations", "concerns"]),

        # Levosimendan
        ("Levosimendan overview", "Inodilator available in Europe/Asia (NOT FDA-approved in US). Mechanism: sensitizes myocardial contractile apparatus to calcium (increases contractility) + vasodilates (KATP channel opener). Unique in increasing contractility WITHOUT increasing myocardial O2 demand. Improves diastolic function. Useful in acute HF, cardiogenic shock. Studies show mortality benefit in some populations. May become available in US.", ["medications", "levosimendan", "inodilator", "novel", "calcium_sensitizer"]),

        # Steroids in shock
        ("Hydrocortisone in refractory septic shock", "Low-dose hydrocortisone (50 mg IV every 6h) considered in refractory septic shock (persistent hypotension despite high-dose vasopressors + fluids). CORTICUS trial showed improved reversal of shock but NO mortality benefit in hospital survivors. Current recommendation: consider if refractory shock, especially if concern for adrenal insufficiency. Not routine. ACTH stimulation test controversial.", ["medications", "hydrocortisone", "septic_shock", "refractory", "steroids"]),

        # Tachyphylaxis
        ("Tachyphylaxis and tolerance mechanisms", "Loss of effect with continuous exposure. Catecholamines cause: receptor downregulation (fewer receptors), receptor desensitization (phosphorylation), increased phosphodiesterase (degrades cAMP). Solutions: rotation of agents (different mechanisms), intermittent dosing (if applicable), combination therapy (e.g., milrinone + vasopressor). Tachyphylaxis of dopamine particularly common (develops within hours). May need higher doses or agent change.", ["medications", "tachyphylaxis", "tolerance", "resistance", "pharmacology"]),

        # Combination therapy
        ("Multi-agent hemodynamic support", "Cardiogenic shock often requires: inotrope (dobutamine, milrinone) + vasopressor (norepinephrine) + afterload reduction (nitroglycerin, nitroprusside, hydralazine). Septic shock: norepinephrine first-line, add dobutamine if CO remains low, consider epinephrine if refractory, add vasopressin if persistent hypotension. Post-operative: phenylephrine + dobutamine/milrinone often effective. Serial reassessment and medication titration critical. Goal: lowest possible doses.", ["medications", "combination_therapy", "hemodynamic_support", "optimization", "titration"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Inotropes, Vasopressors, Vasodilators Deep Dive"
        ))

    return units

def generate_ventilation_units() -> List[Dict[str, Any]]:
    """Advanced Ventilation & ARDS (50-70 units)"""
    units = []
    module = "ventilation"

    facts = [
        # Modes
        ("Volume-controlled ventilation (VC-CMV)", "Ventilator delivers set tidal volume (typically 6-8 mL/kg ideal body weight). Airway pressure varies with compliance/resistance changes. Advantages: guaranteed minute ventilation, predictable. Disadvantages: risk of barotrauma (high pressures in poor compliance), volutrauma (overdistension). Monitor plateau pressure (goal <30 cm H2O). Hypoventilation if patient breathing over ventilator (add sedation if needed).", ["ventilation", "modes", "volume_controlled", "cmv", "strategy"]),

        ("Pressure-controlled ventilation (PC-CMV)", "Ventilator delivers set inspiratory pressure (typically 15-30 cm H2O). Tidal volume varies with compliance/resistance. Advantages: limits peak pressure (lower barotrauma risk), synchronous with patient effort (pressure-support component). Disadvantages: variable minute ventilation, risk of hypoventilation if compliance worsens. Monitor tidal volumes. Often preferred in ARDS for pressure limitation.", ["ventilation", "modes", "pressure_controlled", "pcv", "strategy"]),

        ("CPAP (Continuous Positive Airway Pressure)", "Non-invasive mode: patient breathes spontaneously against continuous positive pressure (typically 5-10 cm H2O). Maintains FRC, prevents atelectasis. Used for: post-extubation support, OSA, mild hypoxemia. Requires intact airway (no aspiration risk) and patient cooperation. Discomfort/claustrophobia common. Can be delivered via mask or nasal prongs. No mandatory ventilations.", ["ventilation", "modes", "cpap", "non_invasive", "spontaneous"]),

        ("BiPAP (Bilevel Positive Airway Pressure)", "Two pressure levels: higher during inhalation (IPAP, typically 12-20 cm H2O), lower during exhalation (EPAP, typically 4-8 cm H2O). More comfortable than CPAP. Used for COPD exacerbations, pulmonary edema, mild-moderate hypoxemia. Requires patient cooperation. Inadequate if severe respiratory distress or apnea risk. Can be delivered via nasal/oronasal mask.", ["ventilation", "modes", "bipap", "non_invasive", "comfort"]),

        ("Pressure Support Ventilation (PSV)", "Patient initiates breath, ventilator delivers set pressure support (typically 5-15 cm H2O above PEEP). Patient controls rate, duration. Synchronous with patient effort. Used for: gradual weaning (decreasing pressure over time), spontaneous breathing trials, post-extubation support. Risk of hypoventilation if PS too low or patient effort inadequate. Good for patient comfort/synchrony.", ["ventilation", "modes", "psv", "pressure_support", "weaning"]),

        # Advanced modes
        ("High-frequency oscillatory ventilation (HFOV)", "Rapidly oscillates (900-3000 cycles/min) small tidal volumes around mean airway pressure. Maintains FRC while minimizing VILI (ventilator-induced lung injury). Used for severe ARDS refractory to conventional ventilation, rescue therapy. Learning curve steep. Requires sedation/paralysis. Expensive. Limited RCT evidence of benefit over conventional ventilation; OSCILLATE trial neutral. Consider in centers with expertise.", ["ventilation", "hfov", "advanced", "ards", "rescue"]),

        ("Airway Pressure Release Ventilation (APRV)", "Delivers two levels of CPAP with time spent mostly at high pressure (Phigh, typically 20-30 cm H2O) with brief releases to lower pressure (Plow, typically 0-5 cm H2O). Patient breathes spontaneously. Maintains FRC, reduces sedation requirement. Used in ARDS, COPD exacerbations. Learning curve. Potential for breath stacking if Plow too brief. May improve oxygenation quickly.", ["ventilation", "aprv", "advanced", "spontaneous", "ards"]),

        ("Inverse Ratio Ventilation (IRV)", "I:E ratio >1:1 (e.g., 2:1). Prolonged inspiration → increased mean airway pressure → improved oxygenation. Used for refractory hypoxemia in ARDS. Discomfort/dysynchrony common (requires heavy sedation/paralysis). Risk of air trapping/auto-PEEP. Limited data. Generally reserved for rescue therapy. Conventional ventilation with higher PEEP usually preferred.", ["ventilation", "irv", "inverse_ratio", "rescue", "advanced"]),

        # PEEP
        ("PEEP (Positive End-Expiratory Pressure) physiology", "Maintains positive pressure at end-expiration → recruits collapsed alveoli → increases FRC and oxygenation. Normal PEEP = 0 (ambient). Typical range 5-15 cm H2O. Increases intrathoracic pressure → reduces venous return and CO (monitor BP/CVP). Risk of barotrauma/volutrauma. Higher PEEP needed in ARDS (lung recruitment strategy). PEEP < 20 cm H2O usually safe. Monitor driving pressure (Pplat - PEEP; goal <15).", ["ventilation", "peep", "alveolar_recruitment", "oxygenation", "physiology"]),

        ("Auto-PEEP (intrinsic PEEP)", "Unintentional positive pressure remaining at end-expiration due to inadequate expiration time (air trapping). Common in asthma, COPD, high respiratory rates. Increases RV afterload → reduces venous return. Treatment: prolong expiration time (↓ RR, ↑ IE ratio), decrease minute ventilation, consider passive exhalation. Can precipitate hemodynamic collapse if severe + acute (occurs suddenly with mode change). Measure with end-expiration hold.", ["ventilation", "auto_peep", "air_trapping", "asthma", "management"]),

        # ARDS
        ("ARDS management strategy", "ARDS = bilateral opacities on imaging + respiratory failure + PaO2/FiO2 <300 + cause consistent with pulmonary edema. Management: 1) Identify/treat cause, 2) Lung-protective ventilation (6-8 mL/kg ideal BW, Pplat <30), 3) Adequate PEEP (titrate to improve oxygenation + compliance), 4) Prone positioning (if severe, P/F <150), 5) Neuromuscular blockade if not improving, 6) ECMO if refractory. Mortality 30-50% depending on severity.", ["ards", "ards_management", "lung_protective", "ventilation", "strategy"]),

        ("Driving pressure optimization", "Driving pressure = Pplat (plateau pressure) - PEEP. Target <15 cm H2O. Higher driving pressure associated with worse outcomes (increased VILI). Optimize by: reducing TV if driving pressure high (accept lower pH if needed—permissive hypercapnia), adjusting PEEP to improve compliance (recruit atelectasis or reduce overdistension), improving patient-ventilator synchrony (sedation/paralysis if desynchrony). Trending driving pressure useful during ventilator management.", ["ards", "driving_pressure", "lung_protective", "optimization", "vili"]),

        ("Prone positioning in ARDS", "Proning improves oxygenation in 60-70% of patients via recruitment of dorsal lung regions (more perfused in prone). Indicated for severe ARDS (PaO2/FiO2 <150) if hypoxemia refractory to other measures. Sessions 12-16 hours daily. Proning protocols require trained staff (frequent repositioning needed). Complications: facial pressure injury, tube obstruction, dislodgement. PROSEVA trial showed mortality benefit in severe ARDS. Increasingly done in moderate ARDS.", ["ards", "prone_positioning", "proning", "oxygenation", "treatment"]),

        # Special populations
        ("Ventilation in COPD exacerbation", "Goal: avoid air trapping (lengthen expiration, lower RR 10-12, decrease TV if possible). Permissive hypercapnia acceptable (pH >7.25). High PEEP usually not needed (risk of auto-PEEP). Avoid overventilation (increases CO2 clearance → hypocapnia → pH rise → worsening hypotension/syncope after weaning). BiPAP often tried first. If intubation needed, beware rapid reintubation post-extubation. Sedation/paralysis only if absolutely needed (air trapping risk).", ["ventilation", "copd", "exacerbation", "air_trapping", "special"]),

        ("Ventilation in asthma", "Similar to COPD: long expiration times, low RR (8-10 is acceptable), permissive hypercapnia (pH >7.20 acceptable). High PEEP risky (worsens air trapping). Limit TV to avoid overdistension. May need sedation/paralysis to reduce respiratory drive/patient effort. Ketamine excellent induction agent (preserves airway tone, no respiratory depression). Avoid histamine-releasing agents (atracurium, mivacurium). Status asthmaticus = life-threatening, requires intensive management.", ["ventilation", "asthma", "status_asthmaticus", "air_trapping", "special"]),

        ("Ventilation in obesity", "Increased airway pressure needed (reduced compliance from abdominal wall restriction). Use higher PEEP (5-15 cm H2O baseline). Target higher Pplat safely (up to 35 acceptable in obese patients). Position supine often causes desaturation—consider reverse Trendelenburg. BiPAP useful pre-intubation. Post-extubation, high risk of reintubation. Delayed extubation often needed (slower metabolism of sedatives).", ["ventilation", "obesity", "high_peep", "compliance", "special"]),

        # Permissive hypercapnia
        ("Permissive hypercapnia concept", "Accept PaCO2 >50 mmHg (even >80 in severe ARDS) to minimize VILI (reduce TV/driving pressure). pH should remain >7.20 (consider buffers if lower). Benefits: lower mortality in ARDS (possibly), lower barotrauma/volutrauma. Risks: sympathetic stimulation (tachycardia), cerebral vasodilation (ICP increase—caution in neurosurgery), respiratory acidosis may worsen hyperkalemia. Contraindications: head trauma, intracranial pathology, acute MI.", ["ards", "permissive_hypercapnia", "lung_protective", "strategy", "benefits_risks"]),

        # Weaning
        ("Spontaneous breathing trial (SBT) protocol", "Assessment of readiness: adequate oxygenation (PaO2 >60 on FiO2 ≤0.4, PEEP ≤5), adequate RR (usually <35), minimal secretions, adequate alertness, no recent sedation. Trial: 30-120 min of minimal support (T-piece, PSV 5, or CPAP 5-7). Success criteria: RR <35, SpO2 >90%, no distress, HR stable, no new arrhythmias. If successful, extubate. If failed, reassess cause + optimize settings.", ["weaning", "sbt", "extubation", "readiness", "protocol"]),

        ("Weaning predictors and failure causes", "Success predictors: RSBI (RR/TV ratio) <100, CROP index, P0.1/Pmax, MIP (inspiratory muscle strength). Failure causes: inadequate oxygenation, excessive secretions, weak respiratory muscles (myopathy, prolonged paralysis), cardiac failure (pulmonary edema post-extubation), CNS depression (sedatives not cleared), accidental tube obstruction. Reintubation within 48h = failure. 10-15% reintubation rate typical. Manage predictably.", ["weaning", "predictors", "failure_causes", "management", "extubation"]),

        ("Structured weaning protocols", "Reduce support daily (TV, FiO2, PEEP, or PSV) based on tolerance. Assess daily for SBT readiness. Spontaneous breathing trial once ready. Extubate if SBT passed. Structured approach reduces ventilator days vs. physician preference. Automated weaning protocols (e.g., SMARTCARE) may accelerate weaning but require monitoring. Daily interruption of sedation + SBT = best outcome. Avoid prolonged weaning (risk of worsening deconditioning).", ["weaning", "structured_protocol", "daily_goals", "sedation_holiday", "optimization"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Advanced Ventilation & ARDS Management"
        ))

    return units

def generate_mcs_ecmo_units() -> List[Dict[str, Any]]:
    """Mechanical Circulatory Support & ECMO (40-60 units)"""
    units = []
    module = "mcs"

    facts = [
        # IABP
        ("IABP (Intra-Aortic Balloon Pump) mechanism", "Catheter with inflatable balloon placed in descending thoracic aorta (via femoral artery). Inflation during diastole increases coronary perfusion pressure (diastolic augmentation). Deflation during systole reduces afterload (diastolic pressure drops = less resistance for LV). Result: increased coronary flow + reduced afterload = improved CO. Mechanical support device. No direct oxygenation support. Requires synchronized ECG (inflates at dicrotic notch).", ["mcs", "iabp", "mechanical_support", "afterload_reduction", "coronary_perfusion"]),

        ("IABP indications and limitations", "Indications: cardiogenic shock (post-MI, acute valvular disease), refractory hypotension intra-operative, bridge to transplant. Useful in acute MR or VSD (reduce afterload, improve hemodynamics). Limitations: modest support (no significant oxygenation), requires 1:1 counterpulsation (high HR = inadequate support), aortic insufficiency contraindication (inflates aorta directly), requires catheterization. Mortality benefit unproven but widely used as bridge.", ["mcs", "iabp", "indications", "limitations", "bridge"]),

        ("IABP complications", "Vascular: femoral artery dissection, thrombosis, distal limb ischemia (monitor perfusion). Aortic: aortic rupture (rare), aortic dissection. Renal: atheroemboli, renal ischemia. Infection: balloon sepsis (rare). Hemolysis: from balloon friction. Migration: balloon malposition. Weaning: gradual reduction of support before removal (usually 3 days). Timing critical (poor synchrony worsens hemodynamics).", ["mcs", "iabp", "complications", "vascular", "management"]),

        # Impella
        ("Impella mechanism", "Percutaneous axial-flow pump. Catheter with small pump draws blood from LV cavity, ejects into ascending aorta. Provides continuous hemodynamic support. Can achieve higher flow (2.5-5 L/min) than IABP. No pulsatility (continuous flow). Allows LV unloading, reduces LV workload. Works in arrhythmias (no synchronization needed). Requires larger arterial access (usually 13-14 Fr).", ["mcs", "impella", "axial_flow", "hemodynamic_support", "lv_unloading"]),

        ("Impella indications and advantages", "Indications: cardiogenic shock refractory to IABP, acute MI with shock, post-cardiotomy shock, bridge to transplant/VAD. Advantages: superior support vs IABP (higher flows), works with arrhythmias, effective LV unloading (reduces LV wall stress, improves coronary flow, reduces O2 demand). Disadvantages: larger access, cost, requires experience, potential hemolysis, suction events if hypovolemic.", ["mcs", "impella", "indications", "advantages", "cardiogenic_shock"]),

        # TandemHeart
        ("TandemHeart mechanism", "Percutaneous ventricular assist device. Blood drawn from left atrium (via transseptal catheter) and ejected into descending aorta. Provides 3-5 L/min support. Requires vascular access: venous (14 Fr femoral) + arterial (15-17 Fr femoral). Continuous flow. Causes left atrial unloading. Used for cardiogenic shock, bridge to transplant/VAD.", ["mcs", "tandemmheart", "lvad", "percutaneous", "hemodynamic_support"]),

        # ECMO
        ("ECMO overview and types", "Extracorporeal membrane oxygenation = mechanical oxygenation + CO support. VA-ECMO (arterio-venous): provides both oxygenation + hemodynamic support. Deoxygenated blood withdrawn from vein, oxygenated via membrane, returned to artery. VV-ECMO (venous-venous): oxygenated blood returned to vein; helps oxygenation only, requires preserved CO. VV-ECMO preferred for pure respiratory failure (ARDS, severe pneumonia). VA-ECMO for cardiogenic shock, refractory ARDS with shock.", ["mcs", "ecmo", "va_ecmo", "vv_ecmo", "oxygenation"]),

        ("VA-ECMO indications", "Cardiogenic shock refractory to medications/IABP (acute MI, myocarditis, fulminant HF, post-operative). Massive PE (bridge to thrombolysis/thrombectomy). Severe hypothermia cardiac arrest (extracorporeal rewarming). Bridge to transplant, VAD, or decision-making. ARDS with shock. Requires ECMO center with 24/7 capability. Patient selection critical (age <50-60 y/o ideal, irreversible conditions excluded).", ["mcs", "va_ecmo", "cardiogenic_shock", "bridge", "indications"]),

        ("VV-ECMO indications", "Severe ARDS refractory to optimal conventional ventilation (P/F <100 despite Pplat optimization, PEEP optimization, prone positioning). Severe pneumonia with hypoxemia. Interstitial pneumonitis. Acute RV failure (if cardiac output preserved). Does NOT provide hemodynamic support—requires preserved cardiac output. EOLIA trial: VV-ECMO vs continued conventional ventilation in severe ARDS, improved oxygenation but mortality similar.", ["mcs", "vv_ecmo", "ards", "pneumonia", "respiratory_failure"]),

        ("ECMO cannulation strategies", "VA-ECMO: peripheral cannulation (femoral artery/vein) most common, avoids sternotomy. Central cannulation (aorta/RA) for post-operative. VV-ECMO: dual-lumen catheter (single access) or separate access (cannula tips in IVC, RA). Position critical (avoid IVC obstruction, aortic dissection). Ultrasound or fluoroscopy guides placement. Surgical cut-down vs Seldinger technique.", ["mcs", "ecmo", "cannulation", "technique", "placement"]),

        ("ECMO management and anticoagulation", "Maintain ACT 180-200 sec (or higher per protocol) with unfractionated heparin. Full heparinization required (risk of thrombosis without it). Transition to warfarin for bridge. Monitor platelet count (consumption on ECMO). Manage metabolic acidosis (lactate elevation common). Optimize oxygenation, CO, renal function, nutrition. Sedation/analgesia needed. Daily assessments for decanulation readiness (trials of reduced ECMO support).", ["mcs", "ecmo", "management", "anticoagulation", "heparinization"]),

        ("ECMO complications", "Cannulation: femoral artery dissection, aortic dissection, limb ischemia (distal perfusion catheter often placed). Bleeding: all surfaces in contact with blood activate coagulation. Thrombosis: catheter clots, oxygenator failure. Hemolysis: pump induces RBC damage (elevated free Hb, bilirubin). Infection: sepsis risk high. Hypertension: vasoconstriction from device. Weaning: gradual trial of reduced support before decannulation. Outcomes: 50-70% survival depending on indication.", ["mcs", "ecmo", "complications", "management", "outcomes"]),

        ("ECPR (Extracorporeal CPR)", "VA-ECMO initiated during ongoing CPR for refractory cardiac arrest. Bridges to definitive treatment (thrombolysis for PE, PCI for MI, etc) or decision-making. Best outcomes in young patients (<50 y/o) with witnessed arrest, reversible cause, early initiation (within 60 min CPR). Requires ECMO team 24/7. Outcomes: ~50% ROSC, ~25% survival to hospital discharge in selected populations. Becoming standard in ECMO centers.", ["mcs", "ecpr", "cardiac_arrest", "bridge", "special_indication"]),

        ("Weaning from ECMO", "Gradually reduce ECMO flow (assess patient's ability to generate CO at lower flows). Monitor: SVaO2, CO, VAE (vessel access event = decreased support abruptly), mixed venous O2 (should remain >60%). Assess cardiac function (echo, milrinone trial), pulmonary recovery (if respiratory failure, assess PaO2, lung appearance). Once ready, trial off ECMO (continue anticoagulation on catheter). Decannulation follows. Failed decannulation = re-initiate or escalate to VAD/transplant.", ["mcs", "ecmo", "weaning", "decannulation", "readiness_assessment"]),

        ("VAD (Ventricular Assist Device) overview", "Implanted (surgical) pumps for long-term support. LVAD (left ventricular) most common. Used for: bridge to transplant (temporary 6-12 months), bridge to recovery (myocarditis, post-operative stunning), destination therapy (permanent, for ineligible transplant candidates). Requires open surgery. Improves survival in advanced HF. Complications: infection, thrombosis, mechanical failure, bleeding (right HF common post-LVAD).", ["mcs", "vad", "lvad", "implanted", "bridge_transplant"]),

        ("Destination therapy with LVAD", "FDA-approved for patients ineligible for transplant with advanced HF (EF <25%, NYHA Class IV). Continuous-flow LVADs (HeartMate 3, HVAD) offer better outcomes than pulsatile devices. Improves survival ~2 years and quality of life. Complications: infection (most common), stroke, bleeding, RV failure, hepatic congestion. Requires strict anticoagulation (warfarin + aspirin). Patient selection critical (compliance, support system, organ function). Median survival 5-7 years.", ["mcs", "vad", "lvad", "destination_therapy", "advanced_hf"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Mechanical Circulatory Support & ECMO"
        ))

    return units

def generate_echo_units() -> List[Dict[str, Any]]:
    """Cardiac Imaging & Echocardiography (40-60 units)"""
    units = []
    module = "echo"

    facts = [
        # TTE vs TEE
        ("TTE (Transthoracic Echocardiography) overview", "Non-invasive imaging via chest wall. Transducer placed on chest (parasternal, apical, subcostal, suprasternal windows). Provides: chamber size, wall motion, EF, valve function, septal integrity, pericardial effusion. Limitations: acoustic window (obesity, COPD, post-op, mechanical ventilation impair quality). Standard imaging for most cardiac pathology. No risk beyond time/discomfort. Portable—bedside use ideal.", ["echo", "tte", "non_invasive", "imaging", "assessment"]),

        ("TEE (Transesophageal Echocardiography) overview", "Semi-invasive: ultrasound probe in esophagus (proximity to heart improves image quality). Superior image quality vs TTE. Used for: endocarditis (vegetations, abscess), source of embolus (LA clot, PFO, aortic atheroma), intra-operative monitoring, complex anatomy (post-op, congenital), aortic dissection. Requires: ability to pass probe, NPO status, sedation. Risks: esophageal perforation (rare), aspiration, medication side effects. Provides 3D imaging, detailed Doppler.", ["echo", "tee", "semi_invasive", "detailed_imaging", "indications"]),

        ("TEE indications", "Endocarditis (assess vegetation size, valve destruction, perivalvular abscess, fistula). Source of embolus (LA/LAA thrombus, aortic atheroma, PFO/ASD, septal aneurysm). Intra-operative use (valve repair guidance, CABG monitoring, post-operative assessment). Aortic disease (dissection, intramural hematoma, rupture). HF assessment if TTE quality poor. Complications risk-benefit decision needed.", ["echo", "tee", "indications", "diagnosis", "assessment"]),

        # Measurements
        ("EF (Ejection Fraction) estimation", "Visual estimation: normal EF >50%, mild reduction 40-49%, moderate 30-39%, severe <30%. Quantitative: EF = (EDV - ESV) / EDV × 100. Measured from apical 4-chamber or 2-chamber view at end-diastole and end-systole. Modified Simpson method (biplane) or 3D for more accurate. EF <40% = systolic dysfunction. Operator-dependent variability ~10%. Trends more useful than absolute values. Prognostication: lower EF = worse prognosis.", ["echo", "ef", "ejection_fraction", "measurement", "systolic_function"]),

        ("Fractional shortening (FS)", "Alternative measure of systolic function (easier to measure than EF). FS = (LV end-diastolic dimension - LV end-systolic dimension) / LV end-diastolic dimension × 100. Normal FS 25-45%. FS <25% = systolic dysfunction. Quick bedside assessment. Less accurate than EF (ignores radial motion, only measures longaxis). Less commonly used now (prefer EF for standardization).", ["echo", "fractional_shortening", "systolic_function", "measurement", "alternative"]),

        # Segmental abnormalities
        ("Segmental wall motion abnormality patterns", "LAD territory (anterior, anteroseptal, apex): anterior wall hypokinesis/akinesis. RCA territory (inferior, inferoseptal): inferior wall hypokinesis/akinesis. LCx territory (lateral, posterolateral): lateral wall hypokinesis/akinesis. Apex (involves all): apical ballooning (stress cardiomyopathy), apical clot risk. Global hypokinesis = diffuse process (cardiomyopathy, shock, sepsis). Assessing segmental pattern helps localize coronary lesion or identify specific etiology.", ["echo", "wall_motion", "segmental_abnormality", "coronary_territory", "ami"]),

        # Diastolic function
        ("E/A ratio and diastolic function", "Peak E velocity (early diastolic filling rate) and peak A velocity (atrial contraction contribution). E/A ratio: normal 1-2, E/A >2 = restrictive filling (rapid passive filling, stiff ventricle). E/A <1 (E/A ratio <1) = impaired relaxation (slow early filling, dependent on atrial kick). Reversal of E/A to <1 = diastolic dysfunction pattern consistent with impaired relaxation. E/A ratio most impacted by loading (interpretation context-dependent).", ["echo", "e_a_ratio", "diastolic_function", "assessment", "patterns"]),

        ("Tissue Doppler for diastolic assessment", "Measures myocardial tissue velocities rather than blood flow. E' (early diastolic tissue velocity) and A' (atrial tissue velocity). E/e' ratio correlates with LV filling pressure: normal <8, E/e' 8-14 = intermediate, E/e' >14 = elevated PAWP. e' reduced in diastolic dysfunction/aging. e' <10 cm/s = diastolic dysfunction likely. Septal e' often used (technical reasons). Less loader-dependent than E/A.", ["echo", "tissue_doppler", "diastolic_function", "filling_pressure", "assessment"]),

        # Valves
        ("Mitral valve assessment", "Anterior and posterior leaflets. Morphology: normal leaflets, thickened (rheumatic), degenerative (flail, prolapse). Severity: mitral stenosis (MS area <1 cm2 is critical), mitral regurgitation (MR). MR graded 1-4 (trace/mild/moderate/severe). Echo shows: leaflet motion, mean gradient (MS), regurgitant jet size (MR), LA size (chronic MR), LV function. Color Doppler shows regurgitant jet. Mechanism = structural (degenerative, rheumatic) vs functional (LV dilation, annular dilation).", ["echo", "mitral_valve", "stenosis", "regurgitation", "assessment"]),

        ("Aortic valve assessment", "Leaflets: normal tricuspid, bicuspid (congenital), thickened (calcific), vegetations (endocarditis). AS (aortic stenosis): valve area <1 cm2 critical. Mean gradient >40 mmHg = significant. AR (aortic regurgitation): graded 1-4 (mild/moderate/severe). AR shows diastolic color flow into LV. Severity: jet width ratio (width of jet / LVOT width), PHT (pressure half-time), regurgitant volume/fraction. Mechanism = structural (calcific, rheumatic) vs functional (aortic root dilation).", ["echo", "aortic_valve", "stenosis", "regurgitation", "assessment"]),

        ("Tricuspid and Pulmonary valves", "Tricuspid regurgitation (TR): very common, spectrum from trace/benign to severe. TR jet velocity allows RV pressure estimation: RV systolic pressure ~4×(TR velocity)² + estimated RA pressure. Pulmonary regurgitation (PR): less common clinically. TR severity based on: jet width, PHT, hepatic vein flow reversal, RV/RA size. Tricuspid stenosis rare (rheumatic, endocarditis, carcinoid). Pulmonary stenosis (congenital, prosthetic dysfunction).", ["echo", "tricuspid_valve", "pulmonary_valve", "regurgitation", "rv_pressure"]),

        # Specific conditions
        ("Pulmonary hypertension assessment", "Estimated via TR jet velocity (RVSP = 4V² + estimated RAP). Echo shows: RV enlargement (RV dilation, flattened septum, increased RV/LV ratio), increased RA area, reduced RV function. Diastolic PA pressure: estimated from PR jet (if present). Helpful confirmatory imaging but not diagnostic (requires right heart catheterization). Supports clinical suspicion. Trends useful for progression/response to therapy.", ["echo", "pulmonary_hypertension", "rvsp", "rv_dysfunction", "assessment"]),

        ("Pericardial effusion and tamponade", "Effusion: fluid in pericardial sac (echo shows anechoic collection around heart). Size graded: trivial (<1 cm), small (1-2 cm), moderate (2-3 cm), large (>3 cm). Tamponade physiology: diastolic RA collapse (>1/3 of RA cycle), diastolic RV collapse, respiratory variation >30% in inflow velocities, dilated IVC. Swinging heart (heart moves with respiration) seen in large effusions. Requires pericardiocentesis emergently if tamponade. May be loculated post-cardiac surgery.", ["echo", "pericardial_effusion", "tamponade", "RA_collapse", "emergency"]),

        ("Acute mitral regurgitation pathophysiology", "Papillary muscle rupture (post-MI): flail leaflet, large regurgitant jet, acute pulmonary edema. Ruptured chordae tendineae: prolapsing leaflet, severe MR. Endocarditis: vegetation on leaflet, perforation, abscess. Acute rheumatic fever: leaflet swelling, restricted motion. Echo findings: abnormal leaflet motion, severe MR on Doppler, elevated LAP, pulmonary edema (Kerley B lines may appear). Acute MR = emergency (cardiogenic shock, hypoxemia). Often requires surgical repair.", ["echo", "acute_mr", "papillary_muscle", "chordae", "emergency"]),

        ("Acute VSD (Ventricular Septal Defect)", "Post-MI septal rupture: sudden holosystolic murmur, step-up in oxygen saturation (PA >RA saturation), cardiogenic shock. Echo shows: septal defect (dropout in B-mode), left-to-right shunt (color Doppler), increased flow across PV. Continuous wave Doppler shows high-velocity jet (pressure gradient between LV and RV). Timing post-MI (usually day 2-7). Emergency: IABP, vasodilators, urgent surgery. High mortality (50%) even with surgery.", ["echo", "acute_vsd", "septal_rupture", "mi", "emergency"]),

        # Advanced assessment
        ("Stress echocardiography for ischemia", "Induces stress (exercise or dobutamine) while imaging wall motion. Normal: uniform wall thickening throughout ventricle. Ischemia: wall motion abnormality (hypokinesis/akinesis) develops with stress in territory of stenotic vessel. Positive test = territory with ischemia. Sensitivity ~85%, specificity ~80% for CAD. Used for: risk stratification pre-operative, diagnosis of CAD in intermediate-risk patients, viability assessment (stunned myocardium may improve with revascularization).", ["echo", "stress_echo", "ischemia", "cad_diagnosis", "viability"]),

        ("Cardiac output assessment via echo", "Stroke volume = LVOT VTI (velocity time integral) × LVOT area. CO = SV × HR. LVOT VTI measured with PW Doppler (pulsed wave at LVOT), LVOT area from diameter measured in parasternal long-axis (A = π r²). Normal CO ~4-6 L/min. Low CO states may show reduced SV and/or HR. Trends useful. Less accurate than thermodilution but non-invasive. Helps guide fluid/inotrope therapy.", ["echo", "cardiac_output", "sv", "lvot", "assessment"]),

        ("3D echocardiography", "Real-time 3D imaging of entire cardiac structure. Improved accuracy for: EF measurement (avoids geometric assumptions), chamber volume, complex anatomy (post-op, congenital, vegetations). Better visualization of ASD, PFO, VSD. Valve assessment more detailed. Surgical planning (complex lesions, prosthetic placement). Requires experienced operator. Takes longer to acquire/analyze. Increasing availability. Becoming standard for detailed assessment.", ["echo", "3d_echo", "advanced_imaging", "accuracy", "surgical_planning"]),
    ]

    for idx, (topic, text, tags) in enumerate(facts):
        units.append(create_unit(
            text=text,
            topic=topic,
            topic_tags=tags,
            module_name=module,
            index=idx,
            section="Cardiac Imaging & Echocardiography"
        ))

    return units

def main():
    """Generate Phase 5 units and consolidate with existing phases"""
    print("Generating Phase 5: Advanced Cardiac & Hemodynamics...")

    # Generate all modules
    all_units = []

    print("  1/8: ACLS & Resuscitation...")
    all_units.extend(generate_acls_units())

    print("  2/8: Advanced Arrhythmia Management...")
    all_units.extend(generate_arrhythmia_units())

    print("  3/8: Invasive Hemodynamic Monitoring...")
    all_units.extend(generate_hemodynamic_monitoring_units())

    print("  4/8: Shock Physiology Deep Dive...")
    all_units.extend(generate_shock_units())

    print("  5/8: Inotropes, Vasopressors, Vasodilators...")
    all_units.extend(generate_inotrope_vasopressor_units())

    print("  6/8: Advanced Ventilation & ARDS...")
    all_units.extend(generate_ventilation_units())

    print("  7/8: Mechanical Circulatory Support & ECMO...")
    all_units.extend(generate_mcs_ecmo_units())

    print("  8/8: Cardiac Imaging & Echocardiography...")
    all_units.extend(generate_echo_units())

    print(f"\nGenerated {len(all_units)} Phase 5 units")

    # Load existing phases
    existing_json_path = r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.json"
    with open(existing_json_path, "r") as f:
        existing_units = json.load(f)

    print(f"Loaded {len(existing_units)} existing units from Phase 1-4")

    # Consolidate
    consolidated = existing_units + all_units

    # Save consolidated JSON
    consolidated_json_path = r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.json"
    with open(consolidated_json_path, "w") as f:
        json.dump(consolidated, f, indent=2)
    print(f"Saved consolidated JSON ({len(consolidated)} total units)")

    # Save consolidated JSONL
    consolidated_jsonl_path = r"C:\Users\Dean\anesthesia_attending\data\cumulative_all_phases.jsonl"
    with open(consolidated_jsonl_path, "w") as f:
        for unit in consolidated:
            f.write(json.dumps(unit) + "\n")
    print(f"Saved consolidated JSONL ({len(consolidated)} total units)")

    # Generate summary
    print("\n" + "="*70)
    print("PHASE 5 GENERATION SUMMARY")
    print("="*70)
    print(f"Total units generated in Phase 5: {len(all_units)}")
    print(f"Cumulative units (Phase 1-5): {len(consolidated)}")
    print()

    module_counts = {}
    for unit in all_units:
        module = unit["metadata"]["module"]
        module_counts[module] = module_counts.get(module, 0) + 1

    modules = [
        ("ACLS & Resuscitation", "acls"),
        ("Advanced Arrhythmias", "arrhythmia"),
        ("Hemodynamic Monitoring", "hemodynamic"),
        ("Shock Physiology", "shock"),
        ("Inotropes/Vasopressors", "inotropes"),
        ("Advanced Ventilation", "ventilation"),
        ("Mechanical Circulatory Support", "mcs"),
        ("Cardiac Imaging & Echo", "echo"),
    ]

    for name, key in modules:
        count = module_counts.get(key, 0)
        print(f"  {name:.<45} {count:>3} units")

    print(f"\n{'TOTAL':.<45} {len(all_units):>3} units")
    print("="*70)

if __name__ == "__main__":
    main()
