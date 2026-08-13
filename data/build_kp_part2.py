#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kps = []

def kp(id_, topic, domain, discipline, stem, answer, rationale, bloom, sources, confusable=''):
    return {
        'id': id_, 'topic': topic, 'domain': domain, 'discipline': discipline,
        'stem': stem, 'answer': answer, 'rationale': rationale,
        'bloom': bloom, 'source': sources, 'confusable_with': confusable
    }

def script(topic, discipline, enabling, patho, time_course, key_features, consequence):
    return {
        '_type': 'illness_script', 'topic': topic, 'discipline': discipline,
        'enabling_conditions': enabling, 'pathophysiology': patho,
        'time_course': time_course, 'key_features': key_features,
        'consequence_if_missed': consequence
    }

def pair(a, b, discriminator):
    return {'_type': 'confusable_pair', 'topic_a': a, 'topic_b': b, 'discriminator': discriminator}

# ===== [66] MODS =====
t='Multiorgan Dysfunction Syndrome (MODS)'
d='Internal medicine: ICU & critical care'
disc='Critical Care'
kps += [
    kp('mods-1',t,d,disc,
       'What defines the transition to multiorgan dysfunction syndrome (MODS) in a septic patient, and what is the expected mortality?',
       'MODS: organ dysfunction of 2 or more organs despite high-dose vasoactive administration; mortality up to 75%',
       'Progressive inflammatory mediator release overwhelms compensatory mechanisms causing irreversible end-organ failure',
       'recall',[{'book':'StatPearls: StatPearls   Sepsis & septic shock','page':4}],''),
    kp('mods-2',t,d,disc,
       'What is the terminal end of the SIRS-to-MODS continuum?',
       'MODS (multiorgan dysfunction syndrome) followed by death; sepsis falls on a continuum from SIRS through septic shock to MODS',
       'SIRS reflects early inflammation; MODS represents collapse of the host inflammatory response to maintain organ perfusion',
       'recall',[{'book':'StatPearls: StatPearls   Sepsis & septic shock','page':3}],''),
    kp('mods-3',t,d,disc,
       'Why does a patient in early septic shock appear warm and hyperdynamic with bounding pulses?',
       'Inflammatory mediators (histamine, serotonin) increase capillary permeability and reduce SVR, causing distributive shock; tachycardia compensates initially',
       'Low afterload plus third-spacing reduces preload; compensatory HR elevation maintains CO producing the warm, hyperdynamic, high-output state',
       'apply',[{'book':'StatPearls: StatPearls   Sepsis & septic shock','page':4}],'Cardiogenic shock'),
    kp('mods-4',t,d,disc,
       'Per Morgan & Mikhail, how is MODS defined in relation to sepsis?',
       'Dysfunction of two or more organ systems associated with sepsis',
       'Each additional failing organ substantially increases mortality; MODS is the sum of individual organ failures that compound each other',
       'recall',[{'book':'Morgan & Mikhail','page':2147}],''),
    kp('mods-5',t,d,disc,
       'Which lab values identify organ dysfunction variables in sepsis by the SCCM/ACCP criteria?',
       'PaO2/FiO2 <300 (lung), oliguria <0.5 mL/kg/h (kidney), creatinine rise >0.5 mg/dL, INR >1.5 or aPTT >60 s (coag), platelets <100k, bilirubin >4 mg/dL, lactate >1 mmol/L',
       'Each variable reflects failure of a distinct perfusion-dependent function and identifies a target for intervention',
       'apply',[{'book':'Morgan & Mikhail','page':2147}],''),
    kp('mods-6',t,d,disc,
       'US sepsis hospitalizations rose from 600,000 to over how many per year from 2000-2008, and what fraction of total hospital costs did sepsis represent in 2009?',
       'Over 1,000,000 hospitalizations/year; sepsis was the most expensive condition in 2009, 5% of total US hospital costs',
       'Rising incidence reflects aging and immunocompromised populations; compounding healthcare expenditure drives guideline-driven bundle care',
       'recall',[{'book':'StatPearls: StatPearls   Sepsis & septic shock','page':3}],''),
]
kps.append(script(t,disc,
    'Sepsis with inadequate source control, immunosuppression, delayed antibiotics',
    'Uncontrolled inflammatory mediator release causes capillary leak, microvascular thrombosis, mitochondrial dysfunction',
    'Hours to days after septic insult; MODS develops over 24-72 h if resuscitation inadequate',
    'Hyperdynamic warm state evolving to cold shock; sequential organ failure (lung first, then renal, hepatic, coagulation); mortality rises 15-20% per additional organ failed',
    'Death; mortality 30-75% once 3+ organs involved'))

# ===== [67] Myasthenia Gravis =====
t='Myasthenia Gravis'
d='Internal medicine: neurology'
disc='Neurology'
kps += [
    kp('mg-1',t,d,disc,
       'What is the immunological mechanism of weakness in myasthenia gravis?',
       'IgG autoantibodies destroy or inactivate postsynaptic nicotinic acetylcholine receptors at the NMJ, reducing receptor numbers and causing complement-mediated end-plate damage',
       'Fewer functional AChRs means reduced EPSP amplitude; patients fatigue because remaining receptors are overwhelmed with repetitive activity',
       'recall',[{'book':'Morgan & Mikhail','page':1028}],'Lambert-Eaton myasthenic syndrome'),
    kp('mg-2',t,d,disc,
       'AChR antibodies are found in what percentage of generalized versus ocular myasthenia gravis patients?',
       '85-90% of generalized MG; 50-70% of ocular MG',
       'Seronegative patients may have anti-MuSK or anti-LRP4 antibodies; antibody status guides therapy decisions',
       'recall',[{'book':'Morgan & Mikhail','page':1028}],''),
    kp('mg-3',t,d,disc,
       'What thymic pathology is found in MG and at what frequency?',
       '10-15% develop thymoma; approximately 70% show thymic lymphoid follicular hyperplasia',
       'The thymus presents self-AChR antigens and activates self-reactive T cells; thymectomy is beneficial in generalized AChR-antibody positive MG',
       'recall',[{'book':'Morgan & Mikhail','page':1028}],''),
    kp('mg-4',t,d,disc,
       'Which preoperative features predict need for postoperative ventilation after thymectomy in MG patients?',
       'Disease duration >6 years, concomitant pulmonary disease, peak inspiratory pressure < -25 cm H2O (e.g., -20 cm H2O), vital capacity <4 mL/kg, pyridostigmine dose >750 mg/day',
       'These factors reflect pre-existing respiratory muscle weakness that will be further impaired by anesthesia and surgical stress',
       'apply',[{'book':'Morgan & Mikhail','page':1035}],''),
    kp('mg-5',t,d,disc,
       'What is a cholinergic crisis and how is it distinguished from myasthenic crisis?',
       'Cholinergic crisis: excess anticholinesterase causes weakness PLUS muscarinic effects (salivation, diarrhea, miosis, bradycardia); edrophonium test worsens cholinergic but improves myasthenic crisis',
       'Both present with weakness; cholinergic crisis has SLUDGE signs from muscarinic excess; distinguishing them is critical because treatment is opposite',
       'apply',[{'book':'Morgan & Mikhail','page':1032}],'Myasthenic crisis'),
    kp('mg-6',t,d,disc,
       'What is the anesthetic implication of MG regarding nondepolarizing NMBs?',
       'MG patients are exquisitely sensitive to nondepolarizing neuromuscular blockers; use lowest effective dose with TOF monitoring',
       'Fewer functional AChRs means a smaller margin before clinical block; standard doses cause prolonged paralysis and postoperative ventilatory failure',
       'apply',[{'book':'Morgan & Mikhail','page':1024}],''),
    kp('mg-7',t,d,disc,
       'What neonatal complication can occur in infants born to mothers with myasthenia gravis?',
       'Transient neonatal myasthenia lasting 1-3 weeks from transplacental transfer of maternal AChR antibodies; may require intubation',
       'Maternal IgG crosses the placenta, transiently blocking neonatal NMJ until antibodies are cleared by the infant',
       'apply',[{'book':'Morgan & Mikhail','page':1035}],''),
]
kps.append(script(t,disc,
    'Young women (3rd decade) or older men (6th decade); thymic abnormality; other autoimmune disease (thyroid, RA, SLE)',
    'IgG attack on postsynaptic AChRs + complement-mediated end-plate destruction reduces receptor density; NMJ transmission fails with repetitive activity',
    'Gradual onset of fatigable ptosis, diplopia, dysarthria, dysphagia; crisis may develop acutely with infection, surgery, or missed medication',
    'Fatigable proximal weakness worse with activity, bulbar symptoms, ptosis; AChR Ab+; decremental response on 3-Hz RNS; vital capacity for respiratory risk',
    'Myasthenic crisis with respiratory failure; aspiration pneumonia from bulbar weakness'))

# ===== [68] NSTI =====
t='Necrotizing Skin & Soft Tissue Infections (NSTI)'
d='Internal medicine: infectious disease'
disc='Infectious Disease / Surgery'
kps += [
    kp('nsti-1',t,d,disc,
       'A patient with suspected cellulitis has pain disproportionate to skin findings, wooden subcutaneous tissue, and crepitus. What syndrome is this and what is the required intervention?',
       'Necrotizing fasciitis (NSTI); requires urgent surgical debridement — antibiotics alone are insufficient',
       'NSTIs track along fascial planes destroying tissue; delay of even hours dramatically increases mortality; no antimicrobial penetrates necrotic fascia',
       'apply',[{'book':'Society Guideline: Guideline   IDSA 2014 SSTI','page':21}],'Severe cellulitis'),
    kp('nsti-2',t,d,disc,
       'What is the typical polymicrobial bacteriology of Type I necrotizing fasciitis?',
       'Average of 5 pathogens per wound; mixed aerobes and anaerobes from bowel/genitourinary flora (coliforms, Bacteroides)',
       'Aerobe-anaerobe synergy: aerobes reduce tissue oxygen tension enabling anaerobes; combined toxin production accelerates tissue destruction',
       'recall',[{'book':'Society Guideline: Guideline   IDSA 2014 SSTI','page':21}],''),
    kp('nsti-3',t,d,disc,
       'What organisms cause monomicrobial (Type II) necrotizing fasciitis, and in what settings?',
       'Group A Streptococcus (most common), community-acquired MRSA, Aeromonas hydrophila (freshwater exposure), Vibrio vulnificus (saltwater/oysters, especially in liver disease)',
       'Monomicrobial NSTIs tend to be more rapidly progressive; Vibrio specifically in liver disease plus saltwater exposure is a classic high-risk scenario',
       'recall',[{'book':'Society Guideline: Guideline   IDSA 2014 SSTI','page':19}],''),
    kp('nsti-4',t,d,disc,
       'What six clinical features distinguish necrotizing fasciitis from simple cellulitis?',
       '(1) Pain disproportionate to findings; (2) failure to respond to initial antibiotics; (3) wooden feel of subcutaneous tissue; (4) systemic toxicity/AMS; (5) edema/tenderness beyond erythema; (6) crepitus or bullae',
       'Each feature signals extension below the dermis into fascia/muscle where antibiotics cannot penetrate and surgical debridement is the only effective intervention',
       'apply',[{'book':'Society Guideline: Guideline   IDSA 2014 SSTI','page':21}],'Cellulitis'),
    kp('nsti-5',t,d,disc,
       'Per IDSA 2014 SSTI guideline, what initial approach applies to all variants of NSTI regardless of microbial type?',
       'Early diagnosis, broad-spectrum antibiotics, and urgent surgical debridement; the approach is similar for all forms and more important than identifying the specific NSTI variant',
       'Fascial planes allow rapid spread; surgical source control is the only definitive intervention; antimicrobials address systemic sepsis but cannot reverse tissue necrosis',
       'apply',[{'book':'Society Guideline: Guideline   IDSA 2014 SSTI','page':19}],''),
]
kps.append(script(t,disc,
    'Diabetes, peripheral vascular disease, IV drug use, recent surgery, immunosuppression, obesity, perineal trauma',
    'Bacterial toxins plus synergistic aero-anaerobic activity destroy fascial tissue; small-vessel thrombosis causes rapid ischemia and irreversible spread',
    'Rapid: hours to 1-2 days from cellulitis appearance to frank necrosis; mortality rises sharply with each 12-hour delay to surgery',
    'Severe pain disproportionate to exam, woody induration, crepitus, gray necrotic tissue at surgery, gas on CT, systemic toxicity (fever, AMS, hemodynamic instability)',
    'Death from septic shock; limb loss; mortality 25-35% even with appropriate surgery'))
kps.append(pair('Necrotizing Skin & Soft Tissue Infections (NSTI)','Severe cellulitis',
    'NSTI: pain out of proportion, woody subcutaneous texture, crepitus, gas on CT, systemic toxicity, no antibiotic response; cellulitis: no deep tissue involvement, responds to antibiotics'))

# ===== [69] Neurocritical Care Essentials =====
t='Neurocritical Care Essentials'
d='Internal medicine: neurology'
disc='Neurology / Critical Care'
kps += [
    kp('neurocc-1',t,d,disc,
       'What is neuroprognostication and why is premature pessimism dangerous?',
       'Neuroprognostication estimates recovery from consciousness disorders after severe brain injury; premature pessimism leads to self-fulfilling prophecy via withdrawal of life-sustaining treatment',
       'Withdrawal of care is the leading cause of death after brain injury in many ICUs; multimodal assessment (exam, EEG, imaging, evoked potentials) is required before prognosticating',
       'apply',[{'book':'MGH Housestaff Manual','page':204}],''),
    kp('neurocc-2',t,d,disc,
       'Clazosentan (endothelin antagonist) was studied for SAH vasospasm; what was its outcome in subsequent RCTs?',
       'Clazosentan reduced angiographic vasospasm but showed no clinical benefit (no improvement in functional outcomes or mortality) in subsequent trials; it is not standard of care',
       'Angiographic vasospasm and delayed cerebral ischemia are distinct; vessel narrowing does not equal ischemia; collateral flow and autoregulation confound clinical outcome',
       'recall',[{'book':'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)','page':10}],''),
]

# ===== [70] NMS =====
t='Neuroleptic Malignant Syndrome (NMS)'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Neurology'
kps += [
    kp('nms-1',t,d,disc,
       'A patient on haloperidol develops hyperthermia, lead-pipe rigidity, altered consciousness, and autonomic lability. What syndrome is this and what is the trigger?',
       'Neuroleptic malignant syndrome (NMS); triggered by dopamine receptor blockade from antidopaminergic agents',
       'Central D2 receptor blockade in the hypothalamus disrupts temperature regulation; striatal blockade causes extrapyramidal rigidity; autonomic nuclei involvement causes lability',
       'recall',[{'book':'Morgan & Mikhail','page':1993}],'Serotonin syndrome'),
    kp('nms-2',t,d,disc,
       'Besides typical high-potency antipsychotics, what other drug classes can precipitate NMS?',
       'Low-potency and atypical antipsychotics, antiemetics (metoclopramide), tricyclic antidepressants, lithium; also rapid withdrawal of dopaminergic drugs (levodopa, amantadine)',
       'Any agent blocking D2 receptors or abruptly removing dopaminergic tone can trigger NMS; rapid switching of Parkinson medications is also associated',
       'recall',[{'book':'StatPearls: StatPearls   Neuroleptic Malignant Syndrome (NMS)','page':2}],''),
    kp('nms-3',t,d,disc,
       'What medications are used for refractory NMS?',
       'Bromocriptine mesylate (dopamine agonist) and dantrolene sodium (muscle relaxant); if due to dopaminergic drug withdrawal, rapid re-institution of the drug may improve symptoms',
       'Bromocriptine restores dopaminergic tone to reverse the D2 blockade; dantrolene reduces peripheral muscle rigidity and hyperthermia by blocking sarcoplasmic Ca2+ release',
       'apply',[{'book':'StatPearls: StatPearls   Neuroleptic Malignant Syndrome (NMS)','page':2}],''),
    kp('nms-4',t,d,disc,
       'Why does NMS NOT require avoidance of succinylcholine, unlike malignant hyperthermia?',
       'NMS pathogenesis (dopamine receptor blockade) is completely different from MH (ryanodine receptor mutation); succinylcholine is safe in NMS patients',
       'MH involves abnormal sarcoplasmic calcium release via RYR1 on triggering; NMS is a central dopaminergic deficiency syndrome with no underlying myopathy susceptibility',
       'analyze',[{'book':'Morgan & Mikhail','page':335}],'Malignant hyperthermia'),
    kp('nms-5',t,d,disc,
       'What four cardinal features define NMS?',
       'Hyperthermia, lead-pipe muscle rigidity with extrapyramidal signs (dyskinesia), altered consciousness, and autonomic lability',
       'All four features reflect dopamine pathway dysfunction: hypothalamus (temperature), striatum (rigidity), cortex (consciousness), and autonomic centers (lability)',
       'recall',[{'book':'Morgan & Mikhail','page':1993}],''),
]
kps.append(script(t,disc,
    'Antipsychotic initiation/dose escalation or antiemetic use; levodopa withdrawal; precipitated by dehydration, agitation, restraints',
    'Central D2 receptor blockade causes loss of hypothalamic temperature regulation and extrapyramidal muscle hypertonicity leading to hyperthermia and rhabdomyolysis',
    'Hours to days after drug initiation or dose change; typically evolves over 24-72 h; slower than serotonin syndrome',
    'FEVER mnemonic: Fever, Encephalopathy, Vitals unstable, Enzyme elevation (CK), Rigidity; leukocytosis; mortality 10-20%',
    'Death from hyperthermia, rhabdomyolysis, renal failure, respiratory failure, DIC'))
kps.append(pair('Neuroleptic Malignant Syndrome (NMS)','Serotonin syndrome',
    'NMS: lead-pipe rigidity, slow onset (days), antidopaminergic drugs; serotonin syndrome: clonus/hyperreflexia, rapid onset (hours), serotonergic drugs'))

# ===== [71] NMJ Weakness Localization =====
t='Neuromuscular Weakness: Localization'
d='Internal medicine: neurology'
disc='Neurology'
kps += [
    kp('nmwl-1',t,d,disc,
       'What is the gold standard electrodiagnostic test for NMJ disorders and its sensitivity?',
       'Single-fiber EMG (SFEMG) is the gold standard; sensitivity up to 99% for NMJ disorders',
       'SFEMG measures jitter (variability in time between paired fiber action potentials); increased jitter and blocking reflect impaired NMJ transmission',
       'recall',[{'book':'StatPearls: StatPearls   Neuromuscular Weakness  Localization','page':4}],''),
    kp('nmwl-2',t,d,disc,
       'How does repetitive nerve stimulation pattern differ between MG and LEMS?',
       'MG: decremental CMAP on low-frequency (3-Hz) RNS; LEMS: post-exercise facilitation with >200% increase in CMAP amplitude on brief maximal contraction or high-frequency RNS',
       'MG: too few AChRs, repetitive stimulation depletes ACh effect; LEMS: impaired presynaptic Ca2+-dependent ACh release, facilitated by Ca2+ accumulation at higher stimulation rates',
       'analyze',[{'book':'StatPearls: StatPearls   Neuromuscular Weakness  Localization','page':4}],'Lambert-Eaton'),
    kp('nmwl-3',t,d,disc,
       'How does LEMS differ from MG in clinical presentation and cancer association?',
       'LEMS: less common bulbar/ocular weakness, diffuse proximal limb weakness, strongly associated with small cell lung carcinoma; MG: frequent bulbar and extraocular weakness, associated with thymoma',
       'LEMS is caused by P/Q-type VGCC antibodies (paraneoplastic or autoimmune); MG is caused by AChR or MuSK antibodies; both are NMJ disorders but at different sites (pre- vs postsynaptic)',
       'apply',[{'book':'StatPearls: StatPearls   Neuromuscular Weakness  Localization','page':2}],'Myasthenia gravis'),
    kp('nmwl-4',t,d,disc,
       'How are UMN versus LMN signs distinguished on examination?',
       'UMN: spasticity, hyperreflexia, positive Babinski, weakness in extensor pattern (arms) / flexor pattern (legs); LMN: fasciculations, atrophy, hyporeflexia, flaccidity',
       'UMN lesions disinhibit lower motor neurons (spasticity); LMN lesions cause denervation atrophy and flaccid paralysis',
       'recall',[{'book':'MGH Housestaff Manual','page':203}],''),
    kp('nmwl-5',t,d,disc,
       'A SFEMG shows MCD >100 microseconds. What does this indicate and what conditions also cause this finding?',
       'Markedly prolonged jitter indicating NMJ disorder; also seen in reinnervation (immature nerve endings) from motor neuron disease and myopathies -- SFEMG is sensitive but not specific for MG',
       'Reinnervation produces immature NMJs with inconsistent transmission; SFEMG cannot distinguish between NMJ disease and immature NMJs from reinnervation',
       'apply',[{'book':'StatPearls: StatPearls   Neuromuscular Weakness  Localization','page':4}],''),
]
kps.append(pair('Myasthenia gravis','Lambert-Eaton Myasthenic Syndrome',
    'MG: AChR Ab, ocular/bulbar onset, decremental RNS at 3 Hz, thymoma association; LEMS: VGCC Ab, proximal limb onset, incremental RNS at high frequency, SCLC association'))

# ===== [72] NIV =====
t='Noninvasive Ventilation (NIV)'
d='Internal medicine: ICU & critical care'
disc='Pulmonology / Critical Care'
kps += [
    kp('niv-1',t,d,disc,
       'In acute COPD exacerbation with respiratory acidosis, what is the preferred initial ventilation mode per GOLD 2024?',
       'NIV is preferred over invasive ventilation (intubation) as initial mode; RCT success rate 80-85%; reduces intubation rate, VAP, length of stay, and mortality',
       'NIV augments alveolar ventilation and reduces work of breathing without endotracheal intubation, preserving airway defense and avoiding intubation complications',
       'apply',[{'book':'Society Guideline: Guideline   GOLD 2024 COPD Full Report','page':121}],'High-flow nasal cannula'),
    kp('niv-2',t,d,disc,
       'What are the absolute contraindications to NIV?',
       'Facial trauma or burns (prevents mask fitting), fixed upper airway obstruction, active vomiting (aspiration risk), respiratory or cardiac arrest (requires immediate invasive support)',
       'These conditions prevent safe mask application or effective ventilation delivery through an external interface; immediate intubation is required',
       'recall',[{'book':'StatPearls: StatPearls   Noninvasive Ventilation (NIV)','page':4}],''),
    kp('niv-3',t,d,disc,
       'What complications of NIV are distinct from endotracheal intubation?',
       'Gastric insufflation and aspiration, facial skin breakdown from mask pressure, excessively high tidal volumes, patient discomfort limiting oral intake and phonation',
       'NIV delivers pressure through an external interface; loss of seal and patient-ventilator dyssynchrony are unique failure modes not seen with intubated patients',
       'apply',[{'book':'Society Guideline','page':36}],''),
    kp('niv-4',t,d,disc,
       'How does HFNC compare to NIV in reducing work of breathing?',
       'HFNC: up to 60 L/min, FiO2 95-100%, warms/humidifies, washes nasopharyngeal dead space, provides modest PEEP; HFNC is less effective than NIV at reducing work of breathing',
       'NIV delivers positive pressure inspiration directly reducing inspiratory muscle load; HFNC primarily improves oxygenation and clears CO2-rich dead space',
       'analyze',[{'book':'Society Guideline','page':36}],'NIV (BiPAP/CPAP)'),
    kp('niv-5',t,d,disc,
       'What relative contraindications make NIV higher risk but potentially acceptable with close monitoring?',
       'Recent facial/upper GI surgery, life-threatening hypoxemia, inability to protect airway, hemodynamic instability (hypotensive shock), acute MI',
       'These conditions raise NIV failure risk; intubation must be immediately available; failure to respond within 1-2 hours should trigger escalation to intubation',
       'apply',[{'book':'StatPearls: StatPearls   Noninvasive Ventilation (NIV)','page':4}],''),
    kp('niv-6',t,d,disc,
       'When should conversion from NIV to endotracheal intubation be planned?',
       'Clinical deterioration, ventilatory failure (worsening hypercapnia/acidosis despite NIV), intolerance to NIV (agitation, secretions), hemodynamic instability',
       'NIV failure requires prompt recognition; delayed intubation in failing NIV patients increases mortality and complicates subsequent airway management',
       'apply',[{'book':'StatPearls: StatPearls   Noninvasive Ventilation (NIV)','page':2}],''),
]

# ===== [73] Pneumonia Special Populations =====
t='Pneumonia: Special Populations & Organisms'
d='Internal medicine: infectious disease'
disc='Infectious Disease'
kps += [
    kp('pneu-sp-1',t,d,disc,
       'Which organism, particularly in its methicillin-resistant form, is a common cause of hospital-acquired and ventilator-associated pneumonia?',
       'Staphylococcus aureus, especially MRSA, is a common cause of HAP/VAP; MRSA nasal screening has NPV 96-99% for ruling out MRSA pneumonia',
       'S. aureus produces leukocidin toxins damaging alveolar epithelium; MRSA pneumonia requires vancomycin or linezolid coverage when risk factors are present',
       'recall',[{'book':'StatPearls: StatPearls   Pneumonia  Special Populations & Organisms','page':2}],''),
]

# ===== [74] Polymyositis & Dermatomyositis =====
t='Polymyositis & dermatomyositis'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('dm-1',t,d,disc,
       'What are the two pathognomonic skin findings of dermatomyositis?',
       'Gottron papules (erythematous/violaceous papules over dorsal MCP and IP joints) and heliotrope rash (periorbital violaceous discoloration with edema)',
       'These skin findings reflect perivascular inflammatory infiltrate from complement-mediated vascular injury; they are absent in polymyositis and inclusion body myositis',
       'recall',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':4}],'Polymyositis'),
    kp('dm-2',t,d,disc,
       'What is the pathological mechanism underlying perifascicular atrophy in dermatomyositis?',
       'C3 activation forms MAC (C5b-C9) that deposits on muscle capillary walls causing vascular inflammation; perifascicular muscle fibers undergo hypoxic injury and atrophy first (most remote from blood supply)',
       'Complement-mediated microangiopathy is the primary mechanism in dermatomyositis, distinguishing it from polymyositis (T-cell direct cytotoxicity) and IBM (degenerative)',
       'analyze',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':3}],'Polymyositis'),
    kp('dm-3',t,d,disc,
       'Dermatomyositis in adults carries a strong association with malignancy; which clinical features predict cancer?',
       'Predictors of underlying malignancy: male sex, older age at onset, dysphagia, absence of interstitial lung disease',
       'Age-appropriate cancer screening (CT, pelvic/breast/testicular/rectal exam) is mandatory at diagnosis; immune response may be a paraneoplastic phenomenon targeting shared antigens',
       'apply',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':5}],''),
    kp('dm-4',t,d,disc,
       'What initial diagnostic tests should be ordered in suspected dermatomyositis?',
       'Muscle enzymes: CK, aldolase, LDH, AST, ALT; myositis-specific autoantibodies; EMG; skin and muscle biopsy if diagnosis uncertain',
       'Elevated CK reflects ongoing muscle necrosis; specific antibodies (anti-Mi2, anti-Jo-1, anti-MDA5) guide prognosis, organ involvement, and cancer risk',
       'apply',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':5}],''),
    kp('dm-5',t,d,disc,
       'Anti-Mi2 antibody is associated with what clinical dermatomyositis presentation?',
       'Acute onset dermatomyositis with V-neck sign (erythema in V-distribution on anterior chest) and shawl rash (posterior shoulder/neck erythema)',
       'Anti-Mi2 targets a nuclear helicase; its presence predicts classical skin findings and is associated with a generally favorable prognosis with treatment',
       'recall',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':5}],''),
    kp('dm-6',t,d,disc,
       'How does inclusion body myositis differ from dermatomyositis in treatment response?',
       'Inclusion body myositis shows characteristic rimmed vacuoles and inclusion bodies on biopsy and is refractory to corticosteroid treatment; dermatomyositis responds to steroids',
       'IBM is a degenerative disease with protein aggregation (TDP-43, amyloid); distinct pathogenesis from immune-mediated inflammatory myopathies explains steroid refractoriness',
       'analyze',[{'book':'StatPearls: StatPearls   Polymyositis & dermatomyositis','page':10}],'Dermatomyositis'),
]
kps.append(script(t,disc,
    'Adults 40-60 years, female predominance; underlying malignancy (especially in older adults with dermatomyositis)',
    'Complement-mediated microangiopathy (dermatomyositis) or T-cell direct muscle cytotoxicity (polymyositis) causes proximal muscle inflammation and atrophy',
    'Subacute onset over weeks to months; skin changes may precede, follow, or coincide with muscle weakness',
    'Symmetric proximal weakness (deltoids, hip flexors, neck flexors), Gottron papules, heliotrope rash, elevated CK, ILD may coexist',
    'Respiratory failure from diaphragm/intercostal weakness; aspiration from pharyngeal weakness; missed occult malignancy'))
kps.append(pair('Dermatomyositis','Polymyositis',
    'Dermatomyositis: skin findings (Gottron papules, heliotrope), perivascular infiltrate + perifascicular atrophy on biopsy, malignancy risk; Polymyositis: no skin rash, endomysial T-cell infiltrate on biopsy'))

# ===== [75] Post-Cardiac Arrest Care =====
t='Post-Cardiac Arrest Care'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Critical Care'
kps += [
    kp('pcac-1',t,d,disc,
       'What is the leading cause of death after successful cardiac arrest resuscitation, and what does this imply?',
       'Withdrawal of life-sustaining treatment due to perceived neurological injury; this makes neuroprotection (TTM, avoiding hyperthermia/hypoxia) the central focus of post-arrest care',
       'Premature neurological pessimism drives WLST decisions; rigorous multimodal neuroprognostication before 72 hours reduces premature withdrawal',
       'apply',[{'book':'StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)','page':10}],''),
    kp('pcac-2',t,d,disc,
       'What did the TTM2 trial (n=1861) find comparing targeted hypothermia (33 degrees C) to normothermia?',
       'TTM2 found no benefit from 33 degrees C versus targeted normothermia (36-37.5 degrees C) with active fever prevention; recent AHA evidence supports targeting normothermia',
       'Hypothermia reduces cerebral metabolic rate but causes hemodynamic instability and immunosuppression; normothermia with aggressive fever prevention may achieve similar neuroprotection',
       'analyze',[{'book':'StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)','page':11}],''),
    kp('pcac-3',t,d,disc,
       'What does EtCO2 persistently below 10 mmHg indicate during cardiac arrest resuscitation?',
       'Inadequate cardiac output during CPR; EtCO2 <10 mmHg indicates insufficient chest compression quality or true cardiac standstill requiring reassessment',
       'EtCO2 reflects pulmonary blood flow (cardiac output); sudden rise in EtCO2 during CPR suggests ROSC before pulse check confirms it',
       'apply',[{'book':'StatPearls: StatPearls   ACLS  Non Shockable Rhythms (PEA & Asystole)','page':9}],''),
    kp('pcac-4',t,d,disc,
       'After ROSC, what is the initial evaluation sequence in post-cardiac arrest care?',
       'Assess airway, hemodynamics, neurologic status; obtain 12-lead ECG, baseline labs, chest radiograph, brain imaging; evaluate for reversible SCA causes (coronary angiography if STEMI)',
       'Systematic evaluation identifies treatable causes (ACS, electrolyte, PE) and guides organ support; cardiac arrest causes multiorgan dysfunction requiring ICU-level care',
       'apply',[{'book':'StatPearls','page':9}],''),
    kp('pcac-5',t,d,disc,
       'What is the Chain of Survival and the time-critical benchmarks for each link?',
       'Recognition -> early CPR -> early defibrillation -> early ACLS -> post-arrest care; defibrillation within 3-5 min ideal; survival decreases approximately 10% per minute without defibrillation in VF',
       'Each link multiplies survival; bystander CPR bridges to defibrillation; PAD (public access defibrillation) programs dramatically improve OHCA outcomes',
       'recall',[{'book':'Curated Units','page':0}],''),
]

# ===== [76] Psoriatic Arthritis =====
t='Psoriatic arthritis'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('psa-1',t,d,disc,
       'Patients with psoriatic arthritis or ankylosing spondylitis present with low back pain; what distinguishes their presentation from mechanical LBP?',
       'Inflammatory back pain in PsA/AS: extraspinal manifestations (uveitis, skin psoriasis, dactylitis) are usually more prominent; RA spares the spine except for cervical zygapophyseal joints',
       'Spondyloarthropathies involve enthesitis and axial inflammation via HLA-B27 mechanisms; mechanical LBP lacks systemic features and morning stiffness pattern',
       'apply',[{'book':'Morgan & Mikhail','page':1745}],'Mechanical low back pain'),
    kp('psa-2',t,d,disc,
       'Anti-TNF-alpha agents used in psoriatic arthritis; what are two major risks requiring monitoring?',
       'Serious infections (including reactivation tuberculosis) and development of lymphoma; TNF-alpha agents impair granuloma formation and immune surveillance',
       'TNF-alpha is essential for controlling intracellular pathogens (TB, fungi); IGRA/PPD screening and baseline CBC before starting biologics is mandatory',
       'apply',[{'book':'Morgan & Mikhail','page':1745}],''),
    kp('psa-3',t,d,disc,
       'What aortic complication is associated with ankylosing spondylitis (and related spondyloarthropathies)?',
       'Aortic regurgitation from ascending aortic dilation (aortic annular dilation causes AR); chronic aortitis from the inflammatory process dilates the aortic root',
       'AR in AS may be silent until severe; screening echo is warranted in long-standing disease with symptoms; dilation of ascending aorta can also cause dissection',
       'recall',[{'book':'Morgan & Mikhail','page':676}],''),
]

# ===== [77] QTc Prolongation =====
t='QTc Prolongation & Torsades de Pointes'
d='Internal medicine: emergency & acute care'
disc='Cardiology / Emergency Medicine'
kps += [
    kp('qtc-1',t,d,disc,
       'What is the normal QTc upper limit and which correction formulas does the AHA recommend?',
       'Normal QTc: <=460 ms (female), <=450 ms (male); AHA recommends Framingham and Fridericia formulas for best rate correction and mortality prediction',
       'Bazett (QT/sqrt RR) overcorrects at high HR and undercorrects at low HR; Framingham and Fridericia provide superior mortality risk prediction across HR ranges',
       'recall',[{'book':'MGH Housestaff Manual','page':15}],''),
    kp('qtc-2',t,d,disc,
       'Which electrolyte disorders substantially increase risk of drug-induced torsades de pointes?',
       'Hypokalemia (present in 17-70% of drug-induced TdP cases) and hypomagnesemia (contributing factor in numerous published cases)',
       'Hypokalemia reduces IKr conductance, reducing repolarization reserve; hypomagnesemia further destabilizes myocardial repolarization; both exacerbate drug-induced QTc prolongation',
       'apply',[{'book':'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation','page':83}],''),
    kp('qtc-3',t,d,disc,
       'When does ibutilide-associated TdP typically occur, and how long until QTc normalizes?',
       'Most TdP occurs within 30 minutes after last ibutilide dose (rarely up to 2.5 hours); QTc returns to baseline within 2-3 hours',
       'Ibutilide blocks IKr (rapidly-activating delayed rectifier K+ current), prolonging repolarization; the effect is relatively short-lived requiring only brief monitoring',
       'recall',[{'book':'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation','page':83}],''),
    kp('qtc-4',t,d,disc,
       'Why must patients initiating dofetilide be hospitalized?',
       'Dofetilide prolongs QTc with risk of TdP; dose must be adjusted for renal function and QTc monitored for at least 3 days during initiation',
       'Dofetilide is exclusively renally eliminated; dose titration by QTc response under monitored conditions significantly reduces TdP risk; once stable, outpatient continuation is safe',
       'apply',[{'book':'Society Guideline: Guideline   ACC AHA 2023 Atrial Fibrillation','page':79}],''),
    kp('qtc-5',t,d,disc,
       'What ECG finding in hypocalcemia is a risk factor for torsades de pointes?',
       'QTc prolongation; hypocalcemia should prompt ECG to assess for prolonged QT as a risk factor for TdP',
       'Calcium stabilizes the cardiac action potential membrane; hypocalcemia delays ventricular repolarization, extending QT interval and predisposing to early afterdepolarizations',
       'apply',[{'book':'StatPearls: StatPearls   Hypocalcemia  Causes and Management','page':6}],''),
]

# ===== [78] RA: Extra-articular =====
t='RA: extra-articular manifestations'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('ra-eam-1',t,d,disc,
       'What extra-articular manifestations are assessed on exam in reactive arthritis?',
       'Conjunctivitis/uveitis (ocular erythema, photophobia), painless oral ulcers, skin lesions (keratoderma blennorrhagicum, circinate balanitis), dactylitis, enthesitis',
       'Reactive arthritis is a systemic inflammatory response to GU (Chlamydia) or GI infection triggering autoimmunity in HLA-B27+ patients; extraarticular features distinguish it from other arthritides',
       'apply',[{'book':'StatPearls: StatPearls   Reactive arthritis','page':5}],''),
    kp('ra-eam-2',t,d,disc,
       'In reactive arthritis, what testing strategy identifies a causative pathogen and what are the limitations?',
       'Urogenital swabs or urine PCR for Chlamydia trachomatis; pathogen identified in approximately 50% of cases; negative results do not exclude the diagnosis',
       'By the time arthritis develops, the organism may no longer be at the primary site; serology may be the only remaining evidence',
       'apply',[{'book':'StatPearls: StatPearls   Reactive arthritis','page':6}],''),
    kp('ra-eam-3',t,d,disc,
       'What is the classic triad of reactive arthritis (formerly Reiter syndrome)?',
       'Arthritis + urethritis/cervicitis + conjunctivitis/uveitis; keratoderma blennorrhagicum and circinate balanitis may accompany',
       'The full triad is present in a minority of patients; seronegative asymmetric arthritis plus recent GU/GI infection should prompt consideration of reactive arthritis',
       'recall',[{'book':'StatPearls: StatPearls   Reactive arthritis','page':5}],''),
]

# ===== [79] RA: Treatment =====
t='RA: treatment & treat-to-target strategy'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('ra-tx-1',t,d,disc,
       'What is the treat-to-target (T2T) strategy in rheumatoid arthritis?',
       'Achieve remission or low disease activity as measured by validated indices (DAS28, CDAI, SDAI); therapy is escalated at each visit until the target is met',
       'T2T reduces joint destruction and functional disability by minimizing cumulative inflammatory burden; the approach mirrors tight glycemic control in diabetes mellitus',
       'recall',[{'book':'StatPearls: StatPearls   Rheumatoid arthritis  pathogenesis & diagnosis','page':1}],''),
]

# ===== [80] Refractory & Super-Refractory SE =====
t='Refractory & Super-Refractory Status Epilepticus'
d='Internal medicine: neurology'
disc='Neurology / Critical Care'
kps += [
    kp('rse-1',t,d,disc,
       'How is refractory status epilepticus (RSE) defined and what is its mortality?',
       'RSE: SE failure to stop after 2 adequate first + second-line agents; mortality 10-15% overall, rising to 30-50% for RSE',
       'GABA-A receptor internalization during prolonged SE reduces benzodiazepine efficacy over time; early treatment is critical to prevent this pharmacoresistance',
       'recall',[{'book':'Curated Units','page':0}],''),
    kp('rse-2',t,d,disc,
       'What defines super-refractory status epilepticus and what is its mortality?',
       'SE persisting despite anesthesia-level sedation (propofol drip, midazolam drip); mortality exceeds 50%',
       'At anesthesia-level sedation, residual SE may require ketamine, barbiturate coma, or immunotherapy (autoimmune etiology); EEG burst suppression is the target endpoint',
       'recall',[{'book':'Curated Units','page':0}],''),
    kp('rse-3',t,d,disc,
       'What is the first-line agent for convulsive status epilepticus (CSE), and what are the second-line options?',
       'First-line: lorazepam 0.1 mg/kg IV (max 4 mg), repeat once; alternatives: diazepam 0.3 mg/kg IV or intranasal midazolam 0.2 mg/kg. Second-line: fosphenytoin 20 PE/kg IV or levetiracetam 30-60 mg/kg IV',
       'Benzodiazepines enhance GABA-A chloride influx; fosphenytoin blocks voltage-gated Na+ channels; levetiracetam modulates SV2A synaptic vesicle protein reducing excessive firing',
       'apply',[{'book':'Curated Units','page':0}],''),
    kp('rse-4',t,d,disc,
       'What is the role of ketamine in refractory status epilepticus?',
       'Ketamine (NMDA receptor antagonist) is used in RSE; its cardiovascular-sparing profile makes it valuable in patients already hemodynamically compromised by prolonged SE; IV infusions are useful in ICU SE management',
       'As SE progresses, glutamate-mediated excitotoxicity through NMDA receptors dominates; NMDA blockade addresses this mechanism when GABAergic drugs have failed',
       'analyze',[{'book':'Miller/Baby Miller','page':138}],''),
    kp('rse-5',t,d,disc,
       'What is New-Onset Refractory Status Epilepticus (NORSE) and what is its prognosis?',
       'NORSE: refractory SE in a previously healthy individual without clear acute cause; mortality 16-27% in adults; approximately 50% have unknown etiology; significant long-term neurological sequelae common',
       'NORSE may represent autoimmune encephalitis (anti-NMDAR, anti-LGI1) in many patients; empirical immunotherapy is often warranted even before antibody results return',
       'recall',[{'book':'StatPearls','page':1}],''),
    kp('rse-6',t,d,disc,
       'What are the third-line (refractory) treatment options for status epilepticus in the ICU?',
       'Phenobarbital 15-20 mg/kg IV, propofol infusion, or induction of anesthetic coma with intubation; continuous EEG required to confirm seizure cessation',
       'Third-line agents induce EEG burst suppression; non-convulsive SE cannot be assessed clinically -- continuous EEG monitoring is mandatory during anesthetic coma',
       'apply',[{'book':'Curated Units','page':0}],''),
]

# ===== [81] RA: Pathogenesis & Diagnosis =====
t='Rheumatoid arthritis: pathogenesis & diagnosis'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('ra-pd-1',t,d,disc,
       'In psoriatic arthritis, what is the typical temporal relationship between skin disease and arthritis onset?',
       'Skin disease precedes arthritis in 68%; skin and arthritis coincide in ~15%; arthritis precedes skin disease in 17%',
       'Recognizing arthritis-first PsA prevents misdiagnosis as seronegative RA; nail disease (pitting, onycholysis) and dactylitis provide diagnostic clues when skin disease is absent',
       'recall',[{'book':'StatPearls: StatPearls   Psoriatic arthritis','page':4}],'Seronegative RA'),
    kp('ra-pd-2',t,d,disc,
       'What classification criteria are used to diagnose psoriatic arthritis?',
       'CASPAR criteria (Classification Criteria for Psoriatic Arthritis) and ACR/NPF criteria; CASPAR scores psoriasis, nail disease, negative RF, dactylitis, and juxta-articular new bone formation on imaging',
       'CASPAR has ~99% specificity; negative RF helps distinguish PsA from RF-positive RA; the same patient may have both psoriasis and RA (overlap)',
       'apply',[{'book':'StatPearls: StatPearls   Psoriatic arthritis','page':2}],''),
]

# ===== [82] SLE: Autoantibody Profile =====
t='SLE: autoantibody profile and clinical associations'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('sle-ab-1',t,d,disc,
       'Which autoantibodies are specific for SLE (as opposed to antiphospholipid syndrome alone)?',
       'Anti-double-stranded DNA (anti-dsDNA) and anti-Smith (anti-Sm) antibodies are specific for SLE; ANA is sensitive (98%) but not specific',
       'Anti-dsDNA correlates with lupus nephritis activity and complement consumption; anti-Sm is highly specific for SLE (~25% sensitivity, ~99% specificity)',
       'recall',[{'book':'StatPearls: StatPearls   Antiphospholipid syndrome','page':8}],'Drug-induced lupus'),
    kp('sle-ab-2',t,d,disc,
       'Drug-induced lupus (DIL) differs from idiopathic SLE in autoantibody pattern; what is the key distinguishing antibody?',
       'DIL is most commonly associated with anti-histone antibodies; idiopathic SLE more commonly has anti-dsDNA and anti-Smith; anti-dsDNA is rare in DIL',
       'Drugs (procainamide, hydralazine, INH) induce histone modification causing self-antigen exposure; idiopathic SLE autoantibodies target nuclear antigens through different mechanisms',
       'analyze',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':6}],'Idiopathic SLE'),
    kp('sle-ab-3',t,d,disc,
       'What antiphospholipid antibodies define antiphospholipid syndrome (APS) and what titer and timing requirements must be met?',
       'Lupus anticoagulant, anticardiolipin IgG/IgM, or anti-beta2-glycoprotein I IgG/IgM at moderate-to-high titers (>99th percentile) on 2 occasions at least 12 weeks apart',
       'Persistently positive antibodies are required to distinguish true APS from transient positivity (infection, etc.); low-titer anticardiolipin is found in up to 10% of healthy individuals',
       'apply',[{'book':'StatPearls: StatPearls   Antiphospholipid syndrome','page':9}],''),
    kp('sle-ab-4',t,d,disc,
       'Anti-Ro/SSA antibody is strongly associated with what skin manifestation in drug-induced lupus and SLE?',
       'Photodistributed annular or psoriasiform rashes (subacute cutaneous lupus erythematosus, SCLE); also associated with neonatal lupus and congenital heart block',
       'Anti-Ro targets Ro52/Ro60 ribonucleoprotein; it can cross the placenta causing neonatal lupus in 1-2% of anti-Ro-positive pregnancies including complete heart block requiring pacing',
       'apply',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':5}],''),
    kp('sle-ab-5',t,d,disc,
       'What is the expected clinical course of drug-induced lupus (DIL) after stopping the offending drug?',
       'Clinical improvement usually occurs within weeks of drug withdrawal; most DIL patients do not develop serious complications; renal/neurologic involvement remains uncommon',
       'Autoantibodies may persist for months despite clinical resolution; this temporal relationship to drug withdrawal is the key diagnostic criterion distinguishing DIL from idiopathic SLE',
       'apply',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':8}],''),
]
kps.append(pair('Drug-induced lupus (DIL)','Idiopathic SLE',
    'DIL: anti-histone Ab, musculoskeletal/constitutional symptoms, rare renal/CNS involvement, resolves with drug withdrawal; SLE: anti-dsDNA/anti-Sm, renal and CNS involvement common, chronic progressive'))

# ===== [83] SLE: Classification Criteria =====
t='SLE: classification criteria & pathogenesis'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('sle-cc-1',t,d,disc,
       'Which three autoantibody types are specific for SLE (per antiphospholipid syndrome differential)?',
       'ANA (sensitive, ~98%), anti-double-stranded DNA, and anti-Smith; anti-dsDNA and anti-Sm are SLE-specific',
       'ANA is a screening test; anti-dsDNA and anti-Sm confirm SLE; complement consumption (low C3/C4) with anti-dsDNA elevation signals lupus nephritis flare',
       'recall',[{'book':'StatPearls: StatPearls   Antiphospholipid syndrome','page':8}],''),
    kp('sle-cc-2',t,d,disc,
       'AKI workup in a young woman with positive ANA and anti-dsDNA should evaluate for what renal diagnosis?',
       'Lupus nephritis; ANA and anti-dsDNA are key markers in the AKI differential, particularly for immune-complex glomerulonephritis',
       'Lupus nephritis occurs in up to 50% of SLE patients; immune complex deposition causes inflammatory injury; renal biopsy classifies severity and guides treatment',
       'apply',[{'book':'Morgan & Mikhail','page':1093}],''),
    kp('sle-cc-3',t,d,disc,
       'What interstitial lung disease association exists with SLE and other connective tissue diseases?',
       'CTD-ILD is a major extrapulmonary manifestation; SLE, RA, SSc, polymyositis/dermatomyositis, and Sjogren syndrome are all associated; CTD-ILD tends to respond better to immunosuppression than idiopathic ILD (IPF)',
       'Autoantibody-driven alveolar inflammation can cause progressive fibrosis; anti-Jo-1 (DM/PM) and anti-topoisomerase I (SSc) strongly predict ILD development',
       'apply',[{'book':'StatPearls: StatPearls   Non IPF Interstitial Lung Diseases','page':5}],''),
]

# ===== [84] SLE: Organ Manifestations =====
t='SLE: organ manifestations & monitoring'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('sle-om-1',t,d,disc,
       'How does idiopathic SLE organ involvement differ from drug-induced lupus (DIL)?',
       'Idiopathic SLE: renal (lupus nephritis) and neurologic (neuropsychiatric SLE) involvement is common; DIL: renal and CNS involvement uncommon; musculoskeletal and constitutional symptoms dominate DIL',
       'Anti-dsDNA antibodies and complement deposition drive glomerulonephritis in SLE; neuropsychiatric SLE involves vasculopathy and autoantibody-mediated neurotoxicity -- both rare in DIL',
       'analyze',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':8}],''),
    kp('sle-om-2',t,d,disc,
       'In patients with idiopathic SLE started on TNF inhibitors, what autoimmune complication may occur and how is it managed?',
       'Up to 50% develop new autoantibody formation (DIL-on-SLE); clinical manifestations are usually mild; careful monitoring rather than automatic drug discontinuation is appropriate',
       'TNF inhibitors alter regulatory T-cell function permitting new autoantibody generation; this phenotype differs from true SLE flare in severity and organ involvement',
       'apply',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':8}],''),
    kp('sle-om-3',t,d,disc,
       'Secondary Sjogren syndrome in systemic sclerosis causes dry mouth via what mechanism?',
       'Salivary gland fibrosis secondary to SSc OR secondary inflammatory infiltrates associated with Sjogren syndrome cause dry mouth in SSc patients',
       'SSc-sicca is driven by fibrosis (distinct from primary Sjogren lymphocytic infiltration); treatment targets differ; accurate distinction matters for management',
       'apply',[{'book':'StatPearls: StatPearls   Systemic sclerosis (scleroderma)','page':9}],''),
]

# ===== [85] SLE: Treatment Principles =====
t='SLE: treatment principles'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('sle-tx-1',t,d,disc,
       'What is the backbone maintenance agent for all SLE patients and what are its benefits?',
       'Hydroxychloroquine (antimalarial) is the backbone for all SLE patients without contraindication; it reduces flares, organ damage accumulation, thrombosis risk (via APS), and mortality',
       'Hydroxychloroquine disrupts lysosomal antigen processing and TLR signaling; it is continued indefinitely and provides protection even in remission',
       'apply',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':7}],''),
    kp('sle-tx-2',t,d,disc,
       'What happened to SLE mortality causes over time with improved management?',
       'Deaths from active SLE disease declined 44%; deaths from infection decreased 63%; the mortality pattern shifted from uncontrolled inflammation to treatment-related immunosuppression complications',
       'Modern SLE management with immunosuppressants reduces disease activity but increases infection susceptibility; opportunistic infections and drug toxicity are now leading causes of death',
       'analyze',[{'book':'StatPearls: StatPearls   Lupus nephritis','page':16}],''),
    kp('sle-tx-3',t,d,disc,
       'What guides the treatment of lupus nephritis and what is the initial universal agent?',
       'Treatment is guided by renal biopsy histopathological class (ISN/RPS I-VI); all patients initiate hydroxychloroquine; Class III/IV (proliferative) requires induction with mycophenolate or cyclophosphamide',
       'Class III/IV LN: proliferative crescentic injury requires aggressive induction to prevent progression to ESRD; Class V (membranous) may use calcineurin inhibitors as alternative',
       'apply',[{'book':'StatPearls: StatPearls   Lupus nephritis','page':11}],''),
]

# ===== [86] Salicylate Toxicity =====
t='Salicylate Toxicity'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Toxicology'
kps += [
    kp('salic-1',t,d,disc,
       'What is the characteristic acid-base pattern in salicylate toxicity and its mechanism?',
       'Mixed respiratory alkalosis + anion-gap metabolic acidosis; aspirin stimulates the respiratory center (early respiratory alkalosis) and uncouples oxidative phosphorylation (metabolic acidosis)',
       'The mixed picture is pathognomonic; serum salicylate >60 mg/dL symptomatic, >100 mg/dL severe; chronic toxicity may present insidiously with encephalopathy in elderly',
       'analyze',[{'book':'Curated Units','page':0}],''),
    kp('salic-2',t,d,disc,
       'What are the serum salicylate level thresholds for symptomatic versus severe toxicity?',
       'Symptomatic at >60 mg/dL; severe toxicity at >100 mg/dL; pH and clinical status are better severity guides than level alone, especially in chronic toxicity',
       'Chronic salicylate toxicity may be severe at lower levels (especially in elderly presenting with encephalopathy); always check salicylate in unexplained anion gap acidosis or tachypnea',
       'recall',[{'book':'Curated Units','page':0}],''),
    kp('salic-3',t,d,disc,
       'What is urine alkalinization for salicylate toxicity, and what is the target urine pH?',
       'IV sodium bicarbonate to target urine pH 7.5-8.5; alkaline urine ionizes salicylate as an anion (ion trapping), preventing tubular reabsorption and dramatically increasing renal clearance',
       'Salicylate pKa is approximately 3; alkaline pH converts nearly all drug to the charged ionized form that cannot cross tubular epithelium; each 1-unit rise in urine pH multiplies renal clearance',
       'apply',[{'book':'Curated Units','page':0}],''),
    kp('salic-4',t,d,disc,
       'What are the four indications for hemodialysis in salicylate toxicity?',
       'Salicylate level >100 mg/dL, CNS toxicity (encephalopathy, seizures), non-cardiogenic pulmonary edema, metabolic acidosis refractory to alkalinization, or renal failure',
       'Salicylate has low molecular weight and is easily dialyzable; HD removes drug faster than urinary alkalinization alone in severe cases',
       'apply',[{'book':'Curated Units','page':0}],''),
    kp('salic-5',t,d,disc,
       'Why must potassium be repleted during urine alkalinization for salicylate toxicity?',
       'Hypokalemia causes kidneys to preferentially retain K+ by excreting H+ into urine, acidifying it and preventing effective ion trapping; add KCl 20-40 mEq/L to bicarb infusion if K+ <3.5',
       'Alkalinization cannot succeed without adequate potassium; the alkalinization goal of urine pH 7.5-8.5 is impossible in a hypokalemic patient because the kidney prioritizes K+ retention over Na+ retention',
       'analyze',[{'book':'Curated Units','page':0}],''),
    kp('salic-6',t,d,disc,
       'What pulmonary complication occurs in moderate-severe salicylate toxicity and how is it managed?',
       'Non-cardiogenic pulmonary edema (ARDS-like); management: restrict free water, use hypertonic saline (3%) for alkalinization instead of normal saline, judicious diuretics, PEEP 5-10 cm H2O if intubated',
       'Direct lung toxicity plus fluid overload from aggressive alkalinization combine to cause alveolar flooding; intubation paradoxically worsens outcome by eliminating respiratory compensation for metabolic acidosis',
       'apply',[{'book':'Curated Units','page':0}],''),
]
kps.append(script(t,disc,
    'Aspirin overdose (>150 mg/kg single dose) or chronic high-dose use; elderly on chronic aspirin at risk for insidious encephalopathy',
    'Uncoupling of oxidative phosphorylation causes anion-gap metabolic acidosis; direct respiratory center stimulation causes early respiratory alkalosis',
    'Early: tinnitus, altered mentation, hyperventilation; late: pulmonary edema, severe acidosis, hypoglycemia',
    'Mixed respiratory alkalosis + metabolic acidosis; tinnitus; hyperthermia; altered mental status; elevated anion gap; high serum salicylate level',
    'Death from respiratory failure, cerebral edema, or cardiac arrest; intubation worsens outcome by removing respiratory compensation'))

# ===== [87] Secondary Immunodeficiency =====
t='Secondary immunodeficiency & opportunistic infections'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Infectious Disease / Immunology'
kps += [
    kp('secimm-1',t,d,disc,
       'Specific antibody deficiency is the most prevalent primary immunodeficiency (41%); what type of immunodeficiency is common variable immunodeficiency (CVID)?',
       'CVID is the most common symptomatic primary antibody deficiency requiring treatment; characterized by low IgG, IgA, and/or IgM with impaired specific antibody responses',
       'CVID has normal B-cell numbers but impaired B-cell differentiation into plasma cells; results in recurrent sinopulmonary bacterial infections and risk for lymphoma',
       'recall',[{'book':'StatPearls: StatPearls   Immunodeficiency  primary antibody deficiencies','page':6}],''),
    kp('secimm-2',t,d,disc,
       'What infections characterize leukocyte adhesion deficiency (LAD) syndrome?',
       'Very susceptible to Serratia, Burkholderia, and Aspergillus; recurrent severe bacterial infections without pus formation (absent neutrophil recruitment)',
       'LAD: deficiency of CD18/CD11b prevents neutrophil adhesion to endothelium and migration to infection sites; absent neutrophil trafficking means no pus despite severe infection',
       'recall',[{'book':'StatPearls: StatPearls   Immunodeficiency  primary antibody deficiencies','page':4}],''),
    kp('secimm-3',t,d,disc,
       'DiGeorge anomaly arises from defect in which pharyngeal pouches and causes what immune deficiency?',
       'Defect in 3rd and 4th pharyngeal pouches causes thymic aplasia/hypoplasia leading to T-cell immunodeficiency; also causes hypoparathyroidism and conotruncal cardiac defects',
       'The thymus derives from 3rd/4th pouches; absent thymus prevents T-cell maturation causing severe T-cell deficiency; the cardiac and endocrine defects reflect shared embryological origin',
       'recall',[{'book':'StatPearls: StatPearls   Immunodeficiency  primary antibody deficiencies','page':5}],'SCID'),
    kp('secimm-4',t,d,disc,
       'HIV infection shares overlapping epidemiologic pathways with what other infection categories?',
       'Sexually transmitted infections (hepatitis B/C) and bloodborne infections (needle sharing); coinfection is common and requires coordinated screening and treatment',
       'HIV epidemiology reflects shared transmission routes; HBV/HCV coinfection dramatically accelerates liver disease and complicates antiretroviral therapy (HAART)',
       'apply',[{'book':'StatPearls','page':3}],''),
    kp('secimm-5',t,d,disc,
       'What primary immunodeficiency results from RAG1/RAG2 mutations and what is its inheritance?',
       'Autosomal recessive SCID; RAG1/2 mutations prevent V(D)J recombination, blocking T and B cell receptor development, resulting in absent adaptive immunity',
       'RAG1/2 enzymes catalyze the first step of V(D)J recombination; without functional receptors, no antigen-specific T or B cells develop; fatal without hematopoietic stem cell transplant',
       'recall',[{'book':'StatPearls: StatPearls   Immunodeficiency  primary antibody deficiencies','page':5}],'DiGeorge anomaly'),
]

# ===== [88] BZD Toxicity =====
t='Sedative-Hypnotic & Benzodiazepine Toxicity'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Toxicology'
kps += [
    kp('bzdtox-1',t,d,disc,
       'What is the clinical presentation and most dangerous complication of benzodiazepine overdose?',
       'CNS depression: sedation, ataxia, dysarthria, depressed respiratory drive, hypotension; severe: loss of consciousness, respiratory depression requiring intubation, aspiration risk',
       'Benzodiazepines enhance GABA-A receptor activity; respiratory depression is dose-dependent and the primary life-threatening complication, particularly in mixed overdose',
       'recall',[{'book':'Curated Units','page':0}],'Opioid toxidrome'),
    kp('bzdtox-2',t,d,disc,
       'In sedative-hypnotic overdose, what initial medications should be routinely administered per Morgan & Mikhail?',
       'Naloxone up to 2 mg routinely administered to evaluate for opioid co-ingestion; airway protection is the priority; toxicology specimens (blood, urine, gastric) sent promptly',
       'Mixed overdose is common; empirical naloxone identifies opioid contribution without waiting for toxicology results; response is diagnostic and therapeutic',
       'apply',[{'book':'Morgan & Mikhail','page':2160}],''),
    kp('bzdtox-3',t,d,disc,
       'What is the clinical syndrome of benzodiazepine withdrawal after prolonged use?',
       'Abrupt BZD discontinuation causes agitation, disorientation, hallucinations, and seizures; risk is difficult to predict from duration/dose alone',
       'BZDs upregulate GABA-A receptors; abrupt removal causes GABA deficiency and CNS hyperexcitability, analogous to alcohol withdrawal and potentially fatal if severe',
       'apply',[{'book':'Marino ICU Book','page':678}],'Alcohol withdrawal'),
    kp('bzdtox-4',t,d,disc,
       'A patient on chronic benzodiazepines presents with unexplained encephalopathy; what diagnostic test can confirm BZD toxicity?',
       'Flumazenil (GABA-A BZD receptor antagonist) can reverse encephalopathy to confirm BZD diagnosis; helpful in difficult differential diagnosis situations per hepatic encephalopathy guidelines',
       'Flumazenil competitively antagonizes BZD binding at GABA-A; effect is short-lived (~1-2 hours) and may precipitate withdrawal seizures in dependent patients -- use cautiously',
       'apply',[{'book':'Society Guideline: Guideline   AASLD EASL 2014 Hepatic Encephalopathy','page':56}],'Hepatic encephalopathy'),
    kp('bzdtox-5',t,d,disc,
       'What is the first-line alcohol withdrawal treatment and when is phenobarbital preferred?',
       'First-line: benzodiazepines (symptom-triggered per CIWA protocol); phenobarbital is preferred for severe withdrawal, recent seizures, or BZD cross-tolerance concerns',
       'Phenobarbital acts on the GABA-A barbiturate site (independent of BZD site); useful when BZD tolerance reduces efficacy; phenobarbital has long half-life reducing seizure recurrence risk',
       'apply',[{'book':'MGH Housestaff Manual','page':214}],''),
]

# ===== [89] Seizure Classification =====
t='Seizure Classification & Epilepsy Syndromes'
d='Internal medicine: neurology'
disc='Neurology'
kps += [
    kp('sz-1',t,d,disc,
       'What is the 2017 ILAE definition of epilepsy?',
       'At least 2 unprovoked seizures >24 hours apart, OR 1 unprovoked seizure with >=60% recurrence risk over the next 10 years, OR diagnosis of an epilepsy syndrome; isolated non-recurrent seizures do not constitute epilepsy',
       'Epilepsy requires established predisposition to recurrence; one provoked seizure (hypoglycemia, fever, drugs) does not warrant epilepsy diagnosis or long-term AED therapy',
       'recall',[{'book':'MGH Housestaff Manual','page':202}],''),
    kp('sz-2',t,d,disc,
       'How are focal onset seizures classified by awareness and motor features per 2017 ILAE?',
       'Focal onset: classified as focal aware or focal impaired awareness; may evolve to bilateral tonic-clonic; motor subtypes: tonic (stiffening), clonic (jerking), automatisms; non-motor: autonomic, sensory, cognitive',
       'Focal onset reflects hemispheric localization; impaired awareness suggests mesial temporal or frontal involvement; evolving to bilateral tonic-clonic occurs when discharge spreads across the corpus callosum',
       'recall',[{'book':'MGH Housestaff Manual','page':202}],''),
    kp('sz-3',t,d,disc,
       'What is the definition of status epilepticus by current guidelines?',
       '>=5 minutes of continuous seizure activity, OR 2+ seizures without complete return to baseline consciousness between them',
       'This operational time threshold reflects when spontaneous termination becomes unlikely and neuronal injury begins; treatment at 5 minutes is now standard practice',
       'recall',[{'book':'MGH Housestaff Manual','page':202}],''),
    kp('sz-4',t,d,disc,
       'Which anesthetic agent should be avoided in patients with known epilepsy and why?',
       'Etomidate: reports of seizure activity following administration suggest it is best avoided in patients with epilepsy',
       'Etomidate has excitatory CNS effects including myoclonus and increased cortical excitability; it activates seizure foci on EEG; propofol or ketamine are preferred alternatives',
       'apply',[{'book':'Morgan & Mikhail','page':951}],'Propofol'),
    kp('sz-5',t,d,disc,
       'Barbiturates have four major CNS actions; which is relevant to seizure management?',
       'Anticonvulsant activity; barbiturates produce dose-dependent reductions in CMR and CBF, with anticonvulsant effects culminating in EEG burst suppression at high doses',
       'Barbiturates enhance GABA-A function and reduce Na+ channel activity; at high doses they produce burst suppression used in refractory SE and elevated ICP management',
       'recall',[{'book':'Morgan & Mikhail','page':951}],''),
    kp('sz-6',t,d,disc,
       'What seizure type do focal seizures that subsequently spread bilaterally represent?',
       'Initially focal (localized) seizures can subsequently spread, becoming generalized (bilateral tonic-clonic seizures); these are called focal to bilateral tonic-clonic seizures',
       'Spread of focal discharge across the corpus callosum or through subcortical pathways results in bilateral cortical involvement and generalized motor manifestations',
       'recall',[{'book':'Morgan & Mikhail','page':1002}],'Primary generalized seizure'),
]

# ===== [90] Sepsis =====
t='Sepsis and Septic Shock'
d='ICU Critical Care'
disc='Critical Care / Infectious Disease'
kps += [
    kp('sepsis-1',t,d,disc,
       'What did Sepsis-3 (2016 Third International Consensus) emphasize compared to previous SIRS-based definitions?',
       'Sepsis-3 deemphasized systemic inflammation (SIRS criteria) and emphasized life-threatening organ dysfunction caused by dysregulated host response to infection; SOFA score quantifies organ dysfunction',
       'SIRS criteria (fever, tachycardia, leukocytosis) are non-specific and present in many non-infected patients; organ dysfunction (SOFA) better identifies patients at risk of death from infection',
       'recall',[{'book':'Morgan & Mikhail','page':2153}],'SIRS'),
    kp('sepsis-2',t,d,disc,
       'What hemodynamic and laboratory criteria define septic shock per Morgan & Mikhail?',
       'Septic shock: sepsis + vasopressor requirement to maintain MAP >=65 mmHg despite adequate circulating volume AND serum lactate >2 mmol/L',
       'Persistent hypotension despite fluids identifies vasodilatory shock; lactate elevation confirms inadequate tissue oxygen delivery even when BP appears restored by vasopressors',
       'recall',[{'book':'Morgan & Mikhail','page':2153}],''),
    kp('sepsis-3',t,d,disc,
       'When should vasopressor therapy be initiated in septic shock?',
       'When hypotension (MAP <65 mmHg) or elevated lactate persists following IV fluid administration; norepinephrine is the first-line vasopressor',
       'Fluid resuscitation addresses relative hypovolemia; persistent vasodilation after adequate fluids requires vasopressor support to restore MAP and end-organ perfusion',
       'apply',[{'book':'Morgan & Mikhail','page':2155}],''),
    kp('sepsis-4',t,d,disc,
       'What was the outcome of clinical trials targeting specific inflammatory mediators in septic shock?',
       'Trials of naloxone, fibronectin, anticoagulation inhibitors, and anti-LPS monoclonal antibodies were uniformly disappointing; no mortality benefit despite biological rationale',
       'The complex redundant nature of the septic inflammatory response means targeting single mediators fails; bundled supportive care (fluids, vasopressors, antibiotics, source control) remains standard',
       'analyze',[{'book':'Morgan & Mikhail','page':2156}],''),
    kp('sepsis-5',t,d,disc,
       'Why does early septic shock produce a warm, hyperdynamic state with bounding pulses?',
       'Inflammatory mediators reduce SVR (distributive physiology); compensatory tachycardia and increased cardiac output maintain perfusion pressure initially, producing warm extremities and bounding pulses',
       'As inflammation increases capillary permeability and reduces preload, decompensated cold shock follows with lactic acidosis; the warm phase precedes the cold phase',
       'apply',[{'book':'StatPearls: StatPearls   Sepsis & septic shock','page':4}],'Cardiogenic shock'),
]
kps.append(script(t,disc,
    'Known or suspected infection; immunosuppression, indwelling catheters, recent surgery, chronic disease (DM, CKD, liver disease, malignancy)',
    'Pathogen PAMPs activate innate immunity causing cytokine storm leading to vasodilation, capillary leak, and microvascular thrombosis',
    'Hours to days after infectious insult; septic shock may develop within hours without adequate antimicrobial and source control therapy',
    'Fever or hypothermia, tachycardia, tachypnea, altered mental status, elevated lactate, organ dysfunction (SOFA score increase >=2)',
    'Death from MODS; 25-50% mortality in septic shock; each hour delay to antibiotics independently increases mortality'))

# ===== [91] Septic Shock Adjunctive =====
t='Septic Shock: Adjunctive & Advanced Therapies'
d='Internal medicine: infectious disease'
disc='Critical Care'
kps += [
    kp('ssadj-1',t,d,disc,
       'What is the vasopressor target MAP in septic shock, and which agent is first-line?',
       'Target MAP >=65 mmHg; norepinephrine is first-line vasopressor; permissive hypotension (MAP goal >60 mmHg) may be considered in select younger patients',
       'MAP 65 mmHg provides adequate renal and cerebral perfusion pressure; higher MAP targets do not improve mortality but may increase arrhythmias in older patients',
       'apply',[{'book':'MGH Housestaff Manual','page':66}],''),
    kp('ssadj-2',t,d,disc,
       'What was the FACTT trial finding on fluid management in ALI/sepsis?',
       'Conservative (restrictive) fluid strategy improved outcomes in ALI/sepsis; fluid beyond what is needed can be harmful',
       'Fluid overload increases alveolar flooding and worsens oxygenation; after initial resuscitation, targeting zero or negative fluid balance reduces ventilator days and ICU stay',
       'apply',[{'book':'Miller/Baby Miller','page':764}],''),
    kp('ssadj-3',t,d,disc,
       'The Marik HAT regimen (hydrocortisone + ascorbic acid + thiamine) for septic shock: what does current evidence show?',
       'Initial observational data were promising but subsequent high-quality RCTs did not confirm mortality benefit; HAT remains investigational and is not standard of care',
       'Publication bias and observer effects inflated early results; randomized trials (VITAMINS, ORANGES, ACTS) showed neutral outcomes for HAT in septic shock',
       'analyze',[{'book':'Society Guideline','page':77}],''),
]

# ===== [92] Serotonin Syndrome =====
t='Serotonin Syndrome'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Toxicology'
kps += [
    kp('sert-1',t,d,disc,
       'What drug combinations are classically associated with serotonin syndrome in the perioperative setting?',
       'MAOI + meperidine (most dangerous: hyperthermia, seizures, coma); MAOI + SSRI; St. John wort + serotonergic drugs',
       'Meperidine inhibits serotonin reuptake; combined with MAOIs that prevent serotonin degradation, serotonin accumulates acutely; meperidine is absolutely contraindicated in MAOI patients',
       'apply',[{'book':'Morgan & Mikhail','page':1016}],'Neuroleptic malignant syndrome'),
    kp('sert-2',t,d,disc,
       'What are the clinical features of serotonin syndrome and the specific treatment?',
       'Agitation, hypertension, hyperthermia, tremor, clonus/hyperreflexia, diaphoresis, autonomic instability; treatment: supportive care + cyproheptadine (5-HT2A antagonist)',
       'Serotonin excess activates 5-HT2A receptors causing muscle hyperactivity and autonomic activation; cyproheptadine is the specific antidote but evidence is largely case-report based',
       'apply',[{'book':'Morgan & Mikhail','page':1016}],''),
    kp('sert-3',t,d,disc,
       'How does serotonin syndrome differ from NMS on neurological exam?',
       'Serotonin syndrome: clonus (especially lower extremity), hyperreflexia, rapid onset hours; NMS: lead-pipe rigidity, bradyreflexia, slow onset days',
       'SS: excess 5-HT2A stimulation causes hyperexcitable motor system with clonus; NMS: dopamine block causes extrapyramidal rigidity with normal or reduced reflexes',
       'analyze',[{'book':'Morgan & Mikhail','page':1993}],'Neuroleptic malignant syndrome'),
    kp('sert-4',t,d,disc,
       'What Hunter Toxicity Criteria feature is most specific for serotonin syndrome?',
       'Clonus (spontaneous, inducible, or ocular) in the setting of a serotonergic agent is the most specific finding; onset within 6-24 hours of serotonergic dose change',
       'Hunter criteria: clonus OR agitation + diaphoresis + tremor + hyperreflexia OR hypertonia + fever >38 degrees C + clonus -- the presence of clonus distinguishes SS from other hyperthermic syndromes',
       'apply',[{'book':'StatPearls: StatPearls   Serotonin Syndrome','page':6}],'NMS'),
    kp('sert-5',t,d,disc,
       'What severe complications distinguish serious serotonin syndrome from mild serotonergic side effects?',
       'Severe SS: intravascular coagulation, rhabdomyolysis with highly elevated CK, metabolic acidosis; these require ICU care',
       'Hyperthermia-induced muscle breakdown causes rhabdomyolysis; DIC from widespread endothelial activation can cause multiorgan failure; hyperthermia >41 degrees C is a medical emergency',
       'recall',[{'book':'StatPearls: StatPearls   Serotonin Syndrome','page':6}],''),
]
kps.append(pair('Serotonin Syndrome','Neuroleptic Malignant Syndrome (NMS)',
    'SS: serotonergic drugs (MAOI+meperidine/SSRI), clonus/hyperreflexia, onset hours, tremor, agitation; NMS: antidopaminergic drugs, lead-pipe rigidity, onset days, extrapyramidal signs'))

# ===== [93] Sjogren syndrome =====
t='Sjogren syndrome'
d='Internal medicine: rheumatology, immunology & allergy'
disc='Rheumatology'
kps += [
    kp('sjo-1',t,d,disc,
       'Sjogren syndrome (primary or secondary) can occur with which connective tissue diseases?',
       'SLE, rheumatoid arthritis, systemic sclerosis (scleroderma), polymyositis, dermatomyositis; dry mouth in SSc may be from salivary gland fibrosis or secondary Sjogren inflammatory infiltrates',
       'Primary Sjogren involves lymphocytic infiltration of exocrine glands as the primary process; secondary Sjogren shares the same glandular mechanism within a broader CTD context',
       'recall',[{'book':'StatPearls','page':6}],''),
    kp('sjo-2',t,d,disc,
       'Anti-Ro/SSA antibodies are strongly associated with Sjogren syndrome and what obstetric complication?',
       'Neonatal lupus and congenital heart block from transplacental transfer; anti-Ro targets Ro52/Ro60 ribonucleoprotein expressed in fetal cardiac conducting tissue',
       'Congenital heart block may require pacing; anti-Ro-positive pregnant women need serial fetal cardiac monitoring (echocardiography) at 16-24 weeks',
       'apply',[{'book':'StatPearls: StatPearls   Drug induced lupus','page':5}],''),
    kp('sjo-3',t,d,disc,
       'What is the role of salivary gland ultrasonography in diagnosing Sjogren syndrome?',
       'Salivary gland US differentiates undifferentiated connective tissue disease from Sjogren syndrome; structural gland abnormalities (hypoechoic areas, heterogeneity) support Sjogren diagnosis',
       'Lymphocytic infiltration causes echogenic changes and gland architecture disruption detectable on US; SGUS is incorporated in ACR/EULAR 2016 Sjogren classification criteria',
       'apply',[{'book':'StatPearls','page':5}],''),
]

# ===== [94] Spinal Cord Compression Non-Traumatic =====
t='Spinal Cord Compression: Non-Traumatic'
d='Internal medicine: neurology'
disc='Neurology / Surgery'
kps += [
    kp('scc-1',t,d,disc,
       'What are the major causes of non-traumatic spinal cord compression?',
       'Neoplastic disease (most common non-traumatic cause), epidural hematoma (anticoagulation, spinal procedures), epidural abscess (IVDU, DM, spinal procedures), disk protrusion/spondylosis',
       'Non-traumatic SCC is a medical emergency requiring urgent imaging (MRI); etiology guides definitive treatment (radiation, surgery, antibiotics, reversal of anticoagulation)',
       'recall',[{'book':'StatPearls: StatPearls   Spinal Cord Compression  Non Traumatic','page':1}],''),
    kp('scc-2',t,d,disc,
       'What hemodynamic management goal reduces secondary spinal cord injury in cord compression or vascular compromise?',
       'Maintaining supranormal MAP ensures adequate spinal cord perfusion; hypotension must be avoided during induction, operative decompression, and postoperative period',
       'The injured cord has impaired autoregulation; MAP-dependent perfusion pressure maintenance prevents extension of the ischemic penumbra into salvageable tissue',
       'apply',[{'book':'Morgan & Mikhail','page':1341}],''),
    kp('scc-3',t,d,disc,
       'At which vertebral levels does disk prolapse most commonly occur in adults?',
       'Lumbar: L4-5 and L5-S1 (most common); cervical: C5-6; spondylosis (osteophytic compression) most commonly affects lower cervical spine and afflicts older patients',
       'These levels represent maximum mobility and biomechanical stress zones; disk prolapse and spondylosis at these levels are leading indications for decompressive spinal surgery',
       'recall',[{'book':'Morgan & Mikhail','page':990}],''),
    kp('scc-4',t,d,disc,
       'Why are older adults at greater risk for spinal cord injury from seemingly minor trauma?',
       'Decreased flexibility, greater spondylosis/osteophytes, and reduced spinal canal reserve to accommodate cord edema following even minor trauma',
       'Pre-existing canal stenosis from spondylosis leaves no reserve; minor hyperextension in an elderly patient with cervical spondylosis can cause acute cord injury without bony fracture',
       'apply',[{'book':'Morgan & Mikhail','page':1341}],''),
]
kps.append(script(t,disc,
    'Known malignancy (breast, lung, prostate, myeloma most common); epidural abscess (IVDU, DM, recent spinal procedure); epidural hematoma (anticoagulation, LP, epidural catheter)',
    'Mechanical compression causes venous congestion and ischemia; demyelination and axonal death occur if untreated; edema worsens compression in a vicious cycle',
    'Acute to subacute onset over hours to days; complete motor/sensory deficit may develop within hours once rapid compression begins',
    'Back pain (new or worsening) + bilateral weakness/sensory level + bladder/bowel dysfunction = cord compression until proven otherwise; MRI is diagnostic',
    'Permanent paralysis; cauda equina syndrome is a common medicolegal emergency when diagnosis is delayed'))

# ===== [95] Spinal Cord Injury =====
t='Spinal Cord Injury'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Neurology'
kps += [
    kp('sci-1',t,d,disc,
       'What injury level requires ventilatory support after complete spinal cord transection?',
       'Injuries above C3-5 (diaphragmatic innervation via phrenic nerve) require ventilatory support to survive; C3-4-5 keeps the diaphragm alive',
       'Complete lesions above C3 paralyze both diaphragm and intercostals; below C5, diaphragmatic breathing may be preserved but intercostal and accessory muscles are paralyzed',
       'recall',[{'book':'Morgan & Mikhail','page':1012}],''),
    kp('sci-2',t,d,disc,
       'What are the paraplegia versus quadriplegia level thresholds after spinal cord transection?',
       'Transection above T1 causes quadriplegia (all four limbs); transection at T2 or below causes paraplegia (lower limbs only)',
       'Upper extremity function requires C5-T1 segments; loss above T1 eliminates bilateral arm and leg motor function; C5 injury spares shoulder abduction and elbow flexion',
       'recall',[{'book':'Morgan & Mikhail','page':1012}],''),
    kp('sci-3',t,d,disc,
       'What are the most common vertebral levels of acute spinal cord injury?',
       'C5-6 (cervical) and T12-L1 (thoracolumbar junction)',
       'These levels represent zones of maximum mobility and biomechanical stress where flexion-extension and compression forces are concentrated during trauma',
       'recall',[{'book':'Morgan & Mikhail','page':1012}],''),
    kp('sci-4',t,d,disc,
       'In anesthetic induction of a trauma patient with suspected acute spinal cord injury, why are benzodiazepines, opioids, and propofol potentially life-threatening?',
       'These agents attenuate sympathetic tone; acute spinal cord injury causes neurogenic shock (hypotension from loss of sympathetic outflow) where further SVR reduction causes cardiovascular collapse',
       'Spinal cord injury eliminates sympathetic vasoconstriction below the lesion; any agent reducing central sympathetic drive or vasomotor tone compounds this relative sympathectomy',
       'analyze',[{'book':'Morgan & Mikhail','page':1350}],''),
]

# ===== [96] Stimulant & Sympathomimetic Toxicity =====
t='Stimulant & Sympathomimetic Toxicity'
d='Internal medicine: emergency & acute care'
disc='Emergency Medicine / Toxicology'
kps += [
    kp('stimtox-1',t,d,disc,
       'What toxidrome features characterize sympathomimetic toxicity from cocaine or amphetamines?',
       'Tachycardia, hypertension, hyperthermia, mydriasis, diaphoresis, agitation, psychosis; severe: seizures, STEMI, aortic dissection, intracranial hemorrhage',
       'Catecholamine excess stimulates alpha and beta receptors; hyperthermia from psychomotor agitation is the major driver of end-organ damage, not the drug itself',
       'recall',[{'book':'MGH Housestaff Manual','page':215}],'Anticholinergic toxidrome'),
    kp('stimtox-2',t,d,disc,
       'Ephedrine exhibits tachyphylaxis; what is the mechanism and clinical implication?',
       'Ephedrine acts indirectly by releasing norepinephrine from nerve terminals; repeated dosing depletes NE stores causing progressively less response; switch to direct-acting agent (phenylephrine) when tachyphylaxis occurs',
       'Indirect sympathomimetics depend on presynaptic NE stores; direct agents (phenylephrine, norepinephrine) act on receptors regardless of store depletion and do not exhibit this tachyphylaxis',
       'analyze',[{'book':'Miller/Baby Miller','page':100}],''),
    kp('stimtox-3',t,d,disc,
       'Why should opioid toxidrome be considered even when pupils appear normal in stimulant toxicity?',
       'Normal pupils do not exclude opioid co-ingestion -- sympathomimetic co-ingestion antagonizes miosis; always consider mixed ingestion (speedball = cocaine + opioid)',
       'Pupil examination alone is insufficient for ruling out opioid toxicity in mixed ingestion; toxicology screening and empirical naloxone are appropriate in altered patients',
       'apply',[{'book':'MGH Housestaff Manual','page':215}],''),
]
kps.append(pair('Sympathomimetic toxidrome','Anticholinergic toxidrome',
    'Both: tachycardia, hyperthermia, mydriasis, agitation; key difference: sympathomimetics cause diaphoresis (wet skin); anticholinergics cause anhidrosis (dry skin, urinary retention, ileus)'))

# ===== [97] SAH =====
t='Subarachnoid Hemorrhage (SAH)'
d='Internal medicine: neurology'
disc='Neurology / Neurosurgery'
kps += [
    kp('sah-1',t,d,disc,
       'What is the most common cause of non-traumatic subarachnoid hemorrhage?',
       'Ruptured saccular (berry) aneurysm; accounts for approximately 85% of non-traumatic SAH; SAH and ICH each account for 10% of all strokes',
       'Saccular aneurysms form at bifurcation points of cerebral arteries where the wall is inherently weak; rupture releases arterial-pressure blood into the subarachnoid space',
       'recall',[{'book':'Morgan & Mikhail','page':984}],''),
    kp('sah-2',t,d,disc,
       'What is the classic presentation of aneurysmal SAH?',
       'Thunderclap headache (worst headache of life), nausea, vomiting, meningismus, photophobia; sudden loss of consciousness may occur at ictus from acute ICP surge',
       'Blood in the subarachnoid space irritates meninges (meningismus); sudden ICP spike at rupture causes momentary unconsciousness; LP shows xanthochromia if CT is negative',
       'recall',[{'book':'MGH Housestaff Manual','page':201}],''),
    kp('sah-3',t,d,disc,
       'What are the major early complications of aneurysmal SAH driving mortality?',
       'Rebleeding (highest risk first 24 hours), vasospasm/delayed cerebral ischemia (days 4-14), hydrocephalus, raised ICP, seizures, and cardiac complications',
       'Each complication compounds the initial injury: rebleeding causes acute death; vasospasm causes delayed ischemic stroke; hydrocephalus causes subacute herniation; cardiac dysfunction from catecholamine surge',
       'analyze',[{'book':'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)','page':12}],''),
    kp('sah-4',t,d,disc,
       'What is the time course of cerebral vasospasm after SAH and which treatment is standard?',
       'Vasospasm peaks days 4-14 after SAH; nimodipine (oral calcium channel blocker) is standard and reduces delayed ischemic deficits; clazosentan and statins showed no clinical benefit',
       'Nimodipine is believed to act on brain parenchyma reducing ischemic injury rather than directly reversing vessel spasm; it reduces death and dependency from DCI',
       'apply',[{'book':'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)','page':10}],''),
    kp('sah-5',t,d,disc,
       'What percentage of SAH survivors remain moderately or severely disabled at follow-up?',
       'More than 10% of SAH patients remain moderately or severely disabled; long-term complications include neurocognitive dysfunction, epilepsy, and focal neurological deficits',
       'Even successfully treated aneurysmal SAH causes diffuse brain injury from global ischemia at rupture; secondary brain injury from vasospasm and hydrocephalus compounds disability',
       'recall',[{'book':'StatPearls: StatPearls   Subarachnoid Hemorrhage (SAH)','page':12}],''),
    kp('sah-6',t,d,disc,
       'What determines the decision to extubate at the end of aneurysm surgery?',
       'Young patients conscious preoperatively may be extubated after localized lesion removal; patients with diffuse brain injury or persistent intracranial hypertension remain intubated',
       'Extubation requires intact airway reflexes, adequate respiratory drive, and controlled ICP; ongoing cerebral hypertension requires continued sedation, paralysis, CSF drainage, and head elevation',
       'apply',[{'book':'Morgan & Mikhail','page':984}],''),
]
kps.append(script(t,disc,
    'Cerebral saccular aneurysm (85% of non-traumatic SAH); risk factors: HTN, smoking, connective tissue disease, family history, ADPKD',
    'Arterial wall rupture at aneurysm dome forces blood under arterial pressure into subarachnoid space causing acute ICP spike and meningeal irritation',
    'Instantaneous onset at ictus; vasospasm peaks days 4-14; rebleeding risk highest in first 24 hours; untreated 25% die within 24 hours',
    'Thunderclap headache (worst of life), meningismus, photophobia, altered consciousness; ECG changes (diffuse T-wave inversions) from catecholamine surge',
    'Death or severe disability; rebleeding immediately fatal in 15%; premature aneurysm repair must balance risk of rebleeding versus vasospasm worsening'))

# ===== [98] SVT =====
t='Supraventricular Tachycardias (SVT)'
d='Internal medicine: cardiology'
disc='Cardiology / Electrophysiology'
kps += [
    kp('svt-1',t,d,disc,
       'What is the anatomic definition of supraventricular tachycardia (SVT)?',
       'SVT encompasses all tachyarrhythmias originating at or above the His bundle; most conduct via the normal His-Purkinje system producing a narrow QRS complex (unless aberrant conduction)',
       'His bundle represents the boundary between supra- and infranodal conduction; tachycardias from above use the normal conduction system producing narrow QRS (typically); VT originates below',
       'recall',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':1}],'Ventricular tachycardia'),
    kp('svt-2',t,d,disc,
       'What are the most common SVT subtypes in adults?',
       'Atrial fibrillation and atrial flutter are most common in adults; AVNRT is the most common paroxysmal narrow-complex SVT in patients without structural heart disease',
       'AF involves chaotic atrial firing at 350-600/min with irregular ventricular response; atrial flutter involves a macroreentrant circuit at approximately 300/min; AVNRT uses dual AV nodal pathways',
       'recall',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':1}],''),
    kp('svt-3',t,d,disc,
       'What conduction mechanisms underlie AVNRT versus AVRT?',
       'AVNRT: dual pathways within the AV node (slow pathway antegrade, fast pathway retrograde in typical form); AVRT: accessory bypass tract outside the AV node (pre-excitation, WPW)',
       'AVNRT uses only the AV node for its reentrant circuit; AVRT uses the ventricle as part of the circuit via the bypass tract; ablation targets differ accordingly',
       'analyze',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':1}],''),
    kp('svt-4',t,d,disc,
       'In the EP lab, what finding during SVT excludes AVRT?',
       'AV dissociation (ventricular beats exceeding atrial beats) during SVT excludes AVRT, which requires atrial participation via the bypass tract; also excludes atrial tachycardia',
       'AVRT requires intact AV + bypass tract macro-reentry with each ventricular beat producing an atrial echo; AV dissociation means the ventricle is independent of atria, impossible in AVRT',
       'analyze',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':4}],''),
    kp('svt-5',t,d,disc,
       'If SVT terminates with an atrial event during EP lab pacing maneuvers, what SVT mechanism does this suggest?',
       'Termination with an atrial event suggests atrial tachycardia, as the arrhythmia depends on atrial impulses; AVNRT and AVRT can terminate with either an atrial or ventricular event',
       'AT is driven by atrial automaticity or microreentry; when the atrial impulse fails, the tachycardia terminates at the atrial level; AVNRT/AVRT have bidirectional circuit termination options',
       'analyze',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':6}],'Atrial tachycardia'),
    kp('svt-6',t,d,disc,
       'What is a pseudo-AAV response during entrainment pacing in the EP lab and why is it important?',
       'A pseudo-AAV response is a misidentified pacing response where a preceding A is selected incorrectly; this error leads to wrong SVT classification; calipers should confirm A-A interval matches pacing cycle length',
       'Correct VA vs AV response classification determines SVT mechanism and guides ablation target; pseudo-AAV error is more likely in long-RP tachycardias or when isoproterenol increases junctional automaticity',
       'analyze',[{'book':'StatPearls: StatPearls   Supraventricular Tachycardias (SVT)','page':12}],''),
]
kps.append(pair('AVNRT','AVRT',
    'AVNRT: dual AV nodal pathways, no pre-excitation at rest, RP interval very short (P buried in or just after QRS); AVRT: accessory pathway, may show delta wave at rest (WPW), RP interval longer (P visible after QRS)'))

# --- Validate and write ---
kp_count = sum(1 for k in kps if '_type' not in k)
script_count = sum(1 for k in kps if k.get('_type')=='illness_script')
pair_count = sum(1 for k in kps if k.get('_type')=='confusable_pair')
topic_set = set(k['topic'] for k in kps if '_type' not in k)

print(f'KPs={kp_count}, scripts={script_count}, pairs={pair_count}, topics={len(topic_set)}')

# Validate JSON serialization
json_str = json.dumps(kps, ensure_ascii=False, indent=2)
# Parse back to validate
parsed = json.loads(json_str)
print(f'JSON parses OK, items={len(parsed)}')

with open('data/kp_full_part_2.json', 'w', encoding='utf-8') as f:
    f.write(json_str)

print('Written to data/kp_full_part_2.json')
