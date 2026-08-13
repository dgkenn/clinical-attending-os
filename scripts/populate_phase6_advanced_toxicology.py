#!/usr/bin/env python3
"""
Phase 6.8: Advanced Toxicology (50 units)
Coverage of neurotoxins, cholinergic crises, sympathomimetic toxicity, novel agents
"""

import json
from datetime import datetime

def generate_advanced_toxicology_units():
    units = []
    base_id = "phase6_tox_unit"

    units.append({
        "topic": "Organophosphate Poisoning - Cholinergic Crisis",
        "subtopic": "organophosphate_cholinergic",
        "content": "Organophosphate compounds (pesticides, nerve agents) irreversibly phosphorylate acetylcholinesterase (AChE), causing acetylcholine accumulation → cholinergic toxidrome. Muscarinic effects (DUMBELS): defecation/diarrhea, urination, miosis (pinpoint pupils, classic), bronchospasm/bronchorrhea, emesis, lacrimation, salivation. Nicotinic effects: muscle fasciculations, paralysis, tachycardia (paradoxically), hypertension. CNS: confusion, seizures, respiratory depression (muscle + CNS). Severe: respiratory failure requiring intubation. Diagnosis: clinical (miosis, muscle fasciculations, cholinergic symptoms) + lab (RBC/plasma AChE depression). Management: decontamination (remove clothes, wash skin), IV atropine (titrate to dry secretions, goal no wheezing, may need very high doses), pralidoxime (2-PAM, reactivates AChE if given early <24h), supportive care (airway, ventilation), benzodiazepines for seizures. Mortality 2-10%; depends on dose/route.",
        "tags": ["organophosphate", "cholinergic", "pesticide", "nerve_agent", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_0",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Anticholinergic Toxidrome - Atropine, Antihistamines, Anticyclics",
        "subtopic": "anticholinergic_toxidrome",
        "content": "Anticholinergic toxidrome from: atropine, antihistamines (diphenhydramine), tricyclic antidepressants (amitriptyline, nortriptyline), muscle relaxants (benztropine), belladonna alkaloids (plants). Mnemonics: 'red as a beet, hot as a hare, dry as a bone, blind as a bat, mad as a hatter' = flushed skin, fever, dry mouth/skin, dilated pupils/blurred vision, altered mental status (confusion, hallucinations, delirium, seizures). Anticholinergic effects: tachycardia, hypertension, urinary retention, decreased GI motility (constipation, ileus), mydriasis. Distinguish from sympathomimetic: anticholinergic has no hypertension as prominently + no diaphoresis (dry vs wet skin). Diagnosis: clinical + EKG (QRS widening, especially TCAs). Management: supportive, activated charcoal (if ingestion), benzodiazepines (seizures, agitation), physostigmine (acetylcholinesterase inhibitor) reverses anticholinergic effects (controversial if TCA overdose due to arrhythmia risk, but safe in pure anticholinergic). Mortality low unless severe TCA overdose (arrhythmias, seizures).",
        "tags": ["anticholinergic", "toxidrome", "atropine", "tca_overdose"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_1",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Serotonin Syndrome - SSRI/MAOI Interaction & Hyperthermia",
        "subtopic": "serotonin_syndrome",
        "content": "Serotonin syndrome = excess serotonin from SSRI + MAOI, SSRI + tramadol, SSRI + linezolid (antibiotic with MAOI activity), or overdose. Pathophysiology: serotonin excess in CNS/peripheral nervous system. Clinical triad: mental status changes (confusion, agitation, hypomania), autonomic instability (hyperthermia, tachycardia, hypertension, flushed), neuromuscular abnormalities (tremor, muscle rigidity, hyperreflexia, clonus). Clonus is hallmark (spontaneous, inducible, ocular). Severe: rhabdomyolysis, acute kidney injury, disseminated intravascular coagulation, death. Diagnosis: clinical (especially inducible clonus), temporal relationship to medication change. Hunter criteria helpful. Management: drug discontinuation, supportive (benzodiazepines for agitation/seizures, cooling measures), cyproheptadine (serotonin antagonist, 12 mg load then 2 mg q4-6h) controversial but used. Avoid additional serotonergic drugs. Monitoring: CK, renal function, DIC labs. Mortality <1% with treatment, higher if severe/delayed.",
        "tags": ["serotonin_syndrome", "ssri", "maoi", "hyperthermia", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_2",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Neuroleptic Malignant Syndrome - Antipsychotics & Muscle Rigidity",
        "subtopic": "nms",
        "content": "Neuroleptic malignant syndrome (NMS) = life-threatening reaction to antipsychotics (dopamine antagonists). Risk higher with high-potency (haloperidol), high-dose, rapid escalation, dehydration, hyperthermia. Classic tetrad: hyperthermia (high, refractory), muscle rigidity ('lead pipe'), altered mental status (confusion, mutism, catatonia), autonomic instability (tachycardia, hypertension, tachypnea, diaphoresis). Lead pipe rigidity = constant resistance throughout range of motion (unlike spasticity or cogwheel). Onset: hours to days after antipsychotic initiation/dose increase. Labs: elevated CK (rhabdomyolysis), elevated transaminases, elevated WBC. Diagnosis: clinical (exclude infections, other causes). Management: STOP antipsychotic immediately, supportive (aggressive cooling, IV fluids, monitor electrolytes), benzodiazepines (lorazepam), dantrolene (muscle relaxant, reduces rigidity/hyperthermia; dose 1 mg/kg IV q5-10 min max 10 mg/kg), bromocriptine (dopamine agonist; dose 2.5-10 mg TID). ICU monitoring (arrhythmia risk). Mortality 10-15% despite treatment.",
        "tags": ["nms", "neuroleptic_malignant", "hyperthermia", "rigidity", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_3",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Sympathomimetic Toxicity - Cocaine & Methamphetamine",
        "subtopic": "sympathomimetic_tox",
        "content": "Sympathomimetic toxidrome from: cocaine (stimulant, local anesthetic), methamphetamine, amphetamines, ephedrine, pseudoephedrine (decongestants), phentermine (weight loss), bath salts (cathinones). Sympathetic hyperactivity: tachycardia, hypertension, hyperthermia, diaphoresis, tremor, agitation, hyperreflexia, mydriasis. CNS: anxiety, paranoia, psychosis, hallucinations, seizures, coma. Cardiac: arrhythmias (VT, VF), myocardial infarction, cardiomyopathy (methamphetamine), myocarditis. Cocaine specificity: vasoconstriction (coronary, peripheral), local anesthetic effect. Methamphetamine: CNS stimulation more prominent, chronic use = accelerated atherosclerosis, cardiomyopathy, 'meth mouth'. Diagnosis: clinical + toxicology screen (urine, blood). Management: benzodiazepines (agitation, seizures, hypertension), cooling, IV fluids, avoid propranolol (unopposed alpha effect worsens hypertension), use phentolamine (alpha blocker) or labetalol (combined alpha/beta) for hypertension. Nitrates for cocaine chest pain. Arrhythmia management per ACLS.",
        "tags": ["sympathomimetic", "cocaine", "methamphetamine", "hyperthermia"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_4",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Hallucinogen Toxicity - PCP, LSD, Psilocybin",
        "subtopic": "hallucinogen_tox",
        "content": "PCP (phencyclidine) = dissociative anesthetic with sympathomimetic effects. Presentation: altered mental status (dissociation, hallucinations, paranoia, violent behavior), nystagmus (vertical > horizontal), muscle rigidity, hypertension, tachycardia, hyperthermia, seizures. Severe: rhabdomyolysis, myoglobinuria, acute kidney injury, respiratory depression. Diagnosis: clinical + toxicology. Management: benzodiazepines (agitation, seizures), supportive, avoid physical restraint (increases rhabdomyolysis risk), aggressive fluid resuscitation (myoglobinuria), cool if hyperthermic. ICU monitoring for complications. LSD (lysergic acid diethylamide) = serotonergic hallucinogen. Presentation: visual/auditory hallucinations, euphoria or terror, time distortion, tachycardia, hypertension, hyperthermia. 'Bad trip' = anxiety, paranoia; managed with benzodiazepines, reassurance, quiet environment. Physical toxicity less than PCP. Psilocybin (magic mushrooms) = serotonergic, similar to LSD but milder. Management largely supportive, reassurance.",
        "tags": ["pcp", "hallucinogen", "lsd", "psilocybin", "dissociation"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_5",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Sedative-Hypnotic Withdrawal - Barbiturates & Benzodiazepines",
        "subtopic": "sedative_withdrawal",
        "content": "Benzodiazepine withdrawal = anxiety, tremor, tachycardia, hypertension, diaphoresis, insomnia, irritability, progressing to seizures (especially short-acting BZDs like lorazepam, or high-dose chronic use). Onset 6-24h after last dose (short-acting) or several days (long-acting like diazepam). Severe: seizures, status epilepticus, hallucinations, delirium. Barbiturate withdrawal = similar but more severe/potentially fatal. Symptoms: severe tremor, hallucinations, delirium, hyperthermia, seizures, cardiovascular collapse. Diagnosis: clinical history. Management: benzodiazepine taper (replace discontinued BZD with longer-acting like diazepam, then gradual taper 10% per week). Seizure prophylaxis mandatory. Monitor vital signs closely. Alcohol withdrawal protocol similar (alcohol + benzodiazepine dependence very high risk). Severity depends on duration/dose of chronic use, agent used. Mortality possible if untreated seizures/complications.",
        "tags": ["benzodiazepine_withdrawal", "seizures", "alcohol_withdrawal"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_6",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Novel Psychoactive Substances - Synthetic Cannabinoids & Cathinones",
        "subtopic": "novel_psychoactive",
        "content": "Novel psychoactive substances (NPS) = designer drugs synthesized to evade legal restrictions. Synthetic cannabinoids (K2, Spice): potent CB1 agonists (50-100× potent vs THC). Presentation: severe psychosis, paranoia, violent behavior, severe tachycardia, hypertension, hyperthermia, seizures, acute myocardial infarction (young patients), acute kidney injury. More dangerous than natural cannabis due to higher potency. No specific antidote. Management: benzodiazepines (seizures, agitation), supportive, monitor for cardiac complications. Cathinones (bath salts): synthetic versions of natural stimulant from Khat plant. Presentation: intense euphoria, paranoia, hallucinations, extreme aggression, hyperthermia (up to 40°C+), rhabdomyolysis, seizures, death. Similar to methamphetamine but more severe. Management: benzodiazepines, supportive, aggressive cooling. Undetectable by standard drug screens; special testing required. Ongoing public health threat with evolving formulations.",
        "tags": ["novel_psychoactive", "synthetic_cannabinoid", "cathinone", "bath_salts"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_7",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Strychnine Poisoning - Neurotoxic Seizures",
        "subtopic": "strychnine_poisoning",
        "content": "Strychnine = alkaloid toxin (pesticide, illegal) that blocks inhibitory neurotransmitter glycine (competitive antagonist at glycine receptors on motor neurons). Pathophysiology: unopposed motor neuron stimulation → violent muscular contractions, opisthotonus (severe arching). Presentation: trismus (jaw clenching, 'risus sardonicus'), neck/back stiffness, then generalized seizures with characteristic 'risus sardonicus' (grin), opisthotonus (severe back arching), risus sardonicus + opisthotonus + lock jaw pathognomonic. Onset 15 min to 2h post-ingestion. Severe: rhabdomyolysis, myoglobinuria, acute kidney injury, hyperthermia, respiratory failure (diaphragm/intercostal paralysis). Diagnosis: clinical + toxin detection (serum/urine). Management: benzodiazepines (AGGRESSIVE, seizures life-threatening), neuromuscular blockade + intubation if uncontrolled, supportive, aggressive hydration (myoglobinuria). Glucose/thiamine if alcohol withdrawal coexists. Mortality 10-20% even with treatment.",
        "tags": ["strychnine", "neurotoxin", "seizures", "opisthotonus"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_8",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Botulism - Paralysis & Respiratory Failure",
        "subtopic": "botulism",
        "content": "Botulism = paralysis from Clostridium botulinum toxin (inhibits acetylcholine release at neuromuscular junction). Forms: foodborne (from toxin in food), infant botulism (ingestion of spores → intestinal toxin production), wound botulism (spores in wound produce toxin). Classic presentation: descending paralysis (cranial nerves first: ptosis, dilated pupils, blurred vision, dry mouth, dysphagia, dysarthria), then truncal/extremity weakness, respiratory weakness (life-threatening). Diagnosis: clinical (descending paralysis is hallmark), electromyography (brief, small, abundant motor action potentials = BSAP), toxin detection (serum/stool PCR). Management: SUPPORTIVE (respiratory support), Botulism Immune Globulin (BIG-IV, for infant botulism; reduces duration symptoms), antitoxin (equine antitoxin for foodborne/wound, NOT for infant). Monitor respiratory function closely. Supportive care until paralysis resolves (days to weeks, sometimes months). Mortality 5-10%; higher if respiratory failure untreated.",
        "tags": ["botulism", "paralysis", "neuromuscular", "respiratory_failure"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_9",
        "created_at": datetime.now().isoformat()
    })

    return units

if __name__ == "__main__":
    units = generate_advanced_toxicology_units()
    output_file = "data/phase6_advanced_toxicology_chunks.json"
    with open(output_file, 'w') as f:
        json.dump(units, f, indent=2)
    print(f"Generated {len(units)} advanced toxicology units -> {output_file}")
