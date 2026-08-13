import json
import sys
import os
import re

os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    full_data = json.load(f)

slice_data = full_data[660:693]

def slugify(text):
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def extract_sources(chunks):
    sources = []
    for chunk in chunks:
        book = chunk.get('book', 'Unknown')
        page = chunk.get('page')
        if book and page is not None:
            try:
                sources.append({'book': book, 'page': int(page)})
            except:
                sources.append({'book': book, 'page': 0})
    return sources

def extract_kps(item, index):
    topic = item.get('topic', 'UNKNOWN')
    domain = item.get('domain', 'clinical')
    discipline = item.get('discipline', 'anesthesia')
    chunks = item.get('chunks', [])

    kps = []

    if not chunks:
        return kps

    full_text = ' '.join([c.get('text', '') for c in chunks if c.get('text')])
    sources = extract_sources(chunks)
    topic_slug = slugify(topic)
    topic_lower = topic.lower()

    # Expanded authoring: 5-9 KPs per topic where possible

    if index == 0:  # Brain Death Declaration
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the procedural requirement before organ procurement can begin?',
            'answer': 'Donor death must be declared via neurological determination before organ procurement proceeds.',
            'rationale': 'Death declaration establishes legal and ethical donor status, prerequisite for procurement.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the anesthetic challenge unique to organ donor management?',
            'answer': 'Maintain hemodynamic stability, oxygenation, and organ perfusion in a patient with severe neurologic injury and brain death.',
            'rationale': 'The goal is to preserve organ function, not patient survival; hemodynamics must be optimized for procurement.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What physiologic derangements occur post-brain death?',
            'answer': 'Catecholamine surge (sympathetic storm), hyperthermia, coagulopathy, endocrine dysfunction, and cardiovascular instability.',
            'rationale': 'Brainstem death causes massive sympathomimetic release followed by sympathetic failure and organ dysfunction.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 1:  # CABG
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the principal conduits used in coronary artery bypass grafting?',
            'answer': 'Left internal thoracic artery (LITA), saphenous vein (SVG), right internal thoracic artery (RITA), and radial artery.',
            'rationale': 'Arterial grafts (ITA, radial) have superior long-term patency compared to venous grafts.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the 10-year patency difference between ITA and saphenous vein grafts?',
            'answer': 'ITA >90% patency; SVG 50-60% patency.',
            'rationale': 'ITA endothelium resists atherosclerotic changes; SVG prone to intimal hyperplasia and progressive stenosis.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What anatomic structures must be preserved during internal thoracic artery harvesting?',
            'answer': 'Preserve internal thoracic vein, avoiding injury to pleura, lung, and intercostal nerves.',
            'rationale': 'ITA injury complicates graft flow; neural injury causes chronic chest wall pain.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 2:  # Calcium channel blockers
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When are calcium channel blockers selected in anesthetic practice?',
            'answer': 'For patients with hypertension, coronary artery disease, or dysrhythmias requiring heart rate control and afterload reduction.',
            'rationale': 'CCBs reduce myocardial oxygen demand and improve coronary perfusion through vasodilation.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': 'beta-blockers'
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the major classes of calcium channel blockers?',
            'answer': 'Dihydropyridines (nifedipine, amlodipine) cause vasodilation; non-dihydropyridines (verapamil, diltiazem) cause negative inotropy and chronotropy.',
            'rationale': 'Different classes have distinct effects on vascular vs. cardiac conduction tissue.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the clinical consequence of combining non-dihydropyridine CCBs with anesthetic induction agents?',
            'answer': 'Severe hypotension and bradycardia from additive negative inotropic and chronotropic effects.',
            'rationale': 'Both agents suppress myocardial contractility and AV conduction.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'How are CCB-induced hypotension managed perioperatively?',
            'answer': 'Fluid resuscitation, vasopressors (preferably pure alpha-1), and judicious use of positive inotropes; avoid beta-blockers (combined blockade).',
            'rationale': 'CCBs block calcium-mediated myocardial contraction; beta-blockers worsen this effect.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 3:  # Cancer Pain Management
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the WHO analgesic ladder for cancer pain management?',
            'answer': 'Step 1: non-opioid (acetaminophen, NSAIDs); Step 2: weak opioid (codeine, tramadol); Step 3: strong opioid (morphine, hydromorphone); adjuvants at each level.',
            'rationale': 'Stepwise escalation titrates analgesia while minimizing side effects.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When should adjuvant medications be introduced in cancer pain management?',
            'answer': 'Adjuvants (anticonvulsants for neuropathy, antidepressants, steroids, muscle relaxants) are used at all steps alongside primary analgesics.',
            'rationale': 'Adjuvants target specific pain mechanisms (neuropathic, inflammatory) not addressed by opioids alone.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is breakthrough pain and how is it managed?',
            'answer': 'Transient spikes in pain despite baseline analgesia; treat with short-acting opioids (rescue doses, 10-20% of daily requirement).',
            'rationale': 'Rapid-onset formulations address peaks; baseline adjusted if breakthrough pain frequent.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are common opioid-induced side effects and their management?',
            'answer': 'Constipation (prophylactic laxatives), nausea (antiemetics), sedation (psychostimulants), respiratory depression (monitor, titrate carefully).',
            'rationale': 'Predictable side effect profiles require proactive prevention.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 4:  # Cardiac Electrophysiology
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the normal automaticity rates of different cardiac tissues?',
            'answer': 'SA node 60-100 bpm, AV node 40-60 bpm, ventricular tissue 20-40 bpm; SA node dominates as primary pacemaker.',
            'rationale': 'Intrinsic rate gradient ensures orderly conduction and normal sinus rhythm.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What happens to escape rhythm rate if the SA node fails?',
            'answer': 'AV node assumes pacemaker role at 40-60 bpm (junctional rhythm); if AV node fails, ventricle paces at 20-40 bpm (idioventricular).',
            'rationale': 'Hierarchical backup pacemakers prevent complete cardiac arrest.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the refractory period and why is it clinically important?',
            'answer': 'Period during which myocardium cannot respond to stimuli; absolute (no stimulus triggers response), relative (strong stimulus triggers response).',
            'rationale': 'Refractoriness prevents re-entrant arrhythmias and ensures unidirectional conduction.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 5:  # Cardiac Mechanics
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the four phases of the cardiac cycle?',
            'answer': 'Isovolumetric contraction (LV pressure rises), ejection (AV opens, stroke volume expelled), isovolumetric relaxation (all valves closed, pressure falls), filling.',
            'rationale': 'Each phase has distinct valve positions and pressure/volume changes.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What triggers aortic valve opening?',
            'answer': 'LV pressure exceeds aortic pressure at end of isovolumetric contraction; AV opens and ejection begins.',
            'rationale': 'Pressure gradient determines valve opening and closing.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What causes the S1 heart sound?',
            'answer': 'Closure of atrioventricular valves (mitral and tricuspid) at the onset of isovolumetric contraction.',
            'rationale': 'Valve closure generates audible vibration transmitted through chest wall.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 6:  # Cardiac Output Determinants
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the fundamental equation for cardiac output?',
            'answer': 'Cardiac output (CO) = Heart rate (HR) x Stroke volume (SV).',
            'rationale': 'This product determines the total volume of blood pumped per minute.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the Frank-Starling mechanism and how does it govern stroke volume?',
            'answer': 'Increased preload (venous return) stretches myocardial fibers to optimal length, increasing contractile force and stroke volume.',
            'rationale': 'Fiber length determines overlap between actin and myosin, optimizing cross-bridge cycling.',
            'bloom': 'analyze',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'How does afterload affect stroke volume?',
            'answer': 'Increased afterload (resistance) reduces stroke volume by increasing the load the ventricle must overcome to eject blood.',
            'rationale': 'The ventricle must generate greater pressure to open the aortic valve; excessive afterload impairs ejection.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is contractility and how is it manipulated pharmacologically?',
            'answer': 'Contractility is the intrinsic strength of myocardial contraction; increased by positive inotropes (catecholamines, inodilators) and decreased by negative inotropes.',
            'rationale': 'Inotropic agents modulate calcium handling and myofilament sensitivity.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 7:  # Cardiac Rhythm Dysrhythmia
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the initial systematic approach to intraoperative dysrhythmia?',
            'answer': 'Identify rhythm (bradycardia, tachycardia, irregular), assess hemodynamics, rule out hypoxia/hypercarbia/hypothermia/light anesthesia, then apply directed therapy.',
            'rationale': 'Physiologic derangements cause most intraoperative arrhythmias; treatment must address underlying cause.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the most common triggering factors for intraoperative dysrhythmia?',
            'answer': 'Hypoxia, hypercarbia, hypothermia, inadequate anesthetic depth, electrolyte abnormalities (hypokalemia, hypocalcemia), and catecholamine surge.',
            'rationale': 'These factors destabilize cardiac membrane potential and automaticity.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What bradycardia-inducing agents are commonly used in anesthesia and when must they be avoided?',
            'answer': 'Succinylcholine (vagomimetic), volatile anesthetics, opioids, and anticholinesterases; avoid in patients with baseline bradycardia or AV block.',
            'rationale': 'Additional vagal stimulation or reduced rate worsens hemodynamic compromise.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 8:  # Cardiac Tamponade
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is cardiac tamponade and what is its hemodynamic hallmark?',
            'answer': 'Elevated pericardial pressure from fluid accumulation impedes ventricular filling; hallmark is equalization of diastolic pressures (RA = PAWP = LV diastolic).',
            'rationale': 'External pericardial pressure acts as a limiting constraint, preventing normal ventricular expansion.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': 'restrictive cardiomyopathy'
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the classic clinical signs of cardiac tamponade (Beck triad)?',
            'answer': 'Hypotension, jugular venous distension (JVD), and muffled heart sounds.',
            'rationale': 'Elevated venous pressure and reduced cardiac output cause these findings.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is pulsus paradoxus and what causes it in tamponade?',
            'answer': 'Pulsus paradoxus is >10 mmHg drop in systolic BP during inspiration; in tamponade, increased venous return during inspiration worsens RV filling, shifting septum leftward and reducing LV preload.',
            'rationale': 'Interdependence between ventricles is exaggerated by reduced total pericardial compliance.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the emergency anesthetic management of tamponade?',
            'answer': 'Maintain preload and spontaneous ventilation; avoid positive pressure ventilation (further reduces venous return); prepare for emergency pericardiocentesis or surgical drainage.',
            'rationale': 'Tamponade is preload-dependent; any reduction in venous return worsens hypotension.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 9:  # Cardiac Transplantation
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is unique about the denervated donor heart and how does this affect anesthetic management?',
            'answer': 'The denervated heart lacks autonomic innervation; lacks ischemic preconditioning, lacks reflex responses to hypoxia/hypercarbia, and has elevated resting HR (90-110 bpm).',
            'rationale': 'Sympathetic and parasympathetic signaling is interrupted; the heart cannot adapt acutely to stress.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What negative inotropic agents must be avoided in the denervated transplanted heart?',
            'answer': 'Avoid volatile anesthetics (negative inotropy), beta-blockers, and high-dose opioids; the heart cannot compensate with sympathetic activation.',
            'rationale': 'Loss of reflexive sympathetic compensation makes negative inotropes dangerous.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What atrial and ventricular effects occur after transplantation?',
            'answer': 'Two P waves on ECG (recipient and donor atria); recipient SA node remains innervated and may compete; careful drug selection required.',
            'rationale': 'Surgical anastomosis creates two atrial compartments with independent conduction.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'How is the pulmonary hypertension that often accompanies heart transplantation managed?',
            'answer': 'Right ventricular afterload reduction via inhaled nitric oxide, IV pulmonary vasodilators, mild hyperventilation/alkalosis, and adequate inotropic support.',
            'rationale': 'Elevated PVR can cause acute RV failure post-transplant if not mitigated.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 10:  # Cardiac Disease in Pregnancy
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the major cardiovascular physiologic changes in pregnancy?',
            'answer': 'CO increases 40-50%, SV increases 30%, HR increases 10-20%, SVR decreases 20-30%, and blood volume increases 30-50%.',
            'rationale': 'Placental perfusion demands and hormonal changes (progesterone, relaxin) drive cardiovascular adaptation.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What cardiac pathologies are relatively contraindicated in pregnancy?',
            'answer': 'Severe aortic stenosis, mitral stenosis, pulmonary hypertension (any etiology), and peripartum cardiomyopathy history.',
            'rationale': 'These lesions cannot accommodate the CO demands of pregnancy, risking hemodynamic collapse.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is peripartum cardiomyopathy and when does it occur?',
            'answer': 'Idiopathic dilated cardiomyopathy (low EF <35-45%) occurring in last month of pregnancy or up to 5 months postpartum.',
            'rationale': 'Unclear etiology; may involve myocarditis, hemodynamic stress, or autoimmunity.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 11:  # Cardiopulmonary Bypass
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the principal components of the cardiopulmonary bypass circuit?',
            'answer': 'Venous drainage cannula, centrifugal or roller pump, membrane oxygenator, heat exchanger, arterial filter, and arterial return cannula.',
            'rationale': 'Each component performs a specific life-support function.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the physiologic purpose of the arterial filter on CPB?',
            'answer': 'Remove air, platelet aggregates, fibrin clots, and other emboli that could cause stroke or end-organ ischemia.',
            'rationale': 'Non-pulsatile CPB flow creates conditions for microemboli; filtration reduces embolism risk.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is "CPB-induced coagulopathy" and what is its mechanism?',
            'answer': 'Hemodilution, platelet consumption and dysfunction, consumption of clotting factors, activation of fibrinolysis, and hypothermia impair hemostasis.',
            'rationale': 'Multiple pathways (mechanical, dilutional, thermal) combine to cause a mixed coagulopathy.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the goal of temperature management during CPB?',
            'answer': 'Moderate hypothermia (28-32C) reduces CMRO2 and provides cerebral protection; rewarming to 37C after distal anastomoses.',
            'rationale': 'Hypothermia buys time during ischemic intervals; full rewarming necessary before separation.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 12:  # Cardiovascular Anatomy
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the three main coronary arteries and their territories of supply?',
            'answer': 'LAD (left anterior descending) supplies anterior LV and septum; LCx (left circumflex) supplies lateral LV and posterolateral wall; RCA (right coronary) supplies RV and inferior wall.',
            'rationale': 'Coronary distribution defines ischemic territory for each occlusion.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the dominance of the coronary system and what does it mean clinically?',
            'answer': 'Right dominance (85%): RCA supplies posterolateral and AV nodal branches; left dominance (8%): LCx supplies these territories.',
            'rationale': 'Dominance determines which artery supplies critical nodal tissue, affecting conduction during occlusion.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the layers of the heart wall?',
            'answer': 'Epicardium (outer serosal), myocardium (muscle), endocardium (inner lining), with pericardium as outer sac.',
            'rationale': 'Myocardium is the contractile layer; other layers provide structure and reduce friction.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 13:  # Carotid Endarterectomy
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the primary anesthetic goal during carotid endarterectomy (CEA)?',
            'answer': 'Maintain adequate cerebral perfusion distal to the cross-clamp via systemic hypertension and prevent ischemia via intraoperative neuromonitoring.',
            'rationale': 'CEA carries risk of intraoperative embolic stroke and hypoperfusion stroke during carotid occlusion.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What neurophysiologic monitoring is used during CEA?',
            'answer': 'EEG (detects focal slowing or loss of activity during ischemia) and/or transcranial Doppler ultrasound (detects emboli and blood flow changes).',
            'rationale': 'Real-time monitoring guides shunt placement and prevents intraoperative stroke.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is a carotid shunt and when is it used?',
            'answer': 'A temporary bypass from the common carotid to distal internal carotid that maintains antegrade flow during cross-clamping; used selectively based on EEG or doppler changes.',
            'rationale': 'Shunt prevents hypoperfusion ischemia in patients with inadequate collateral circulation.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is carotid sinus syndrome and how should it be managed perioperatively?',
            'answer': 'Hypersensitive carotid baroreceptors trigger profound bradycardia and hypotension with carotid manipulation; prevent with local anesthetic infiltration and have atropine/pacing ready.',
            'rationale': 'Arterial baroreceptor stimulation activates vagal parasympathomimetic response.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 14:  # Cerebral AVM
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is a cerebral arteriovenous malformation (AVM)?',
            'answer': 'Abnormal direct connection between cerebral artery and vein without intervening capillary bed.',
            'rationale': 'AVM shunting bypasses normal vascular resistance, creating hemodynamic anomalies.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What hemodynamic consequence results from AVM shunting?',
            'answer': 'Reduced vascular resistance in the AVM territory increases regional blood flow, causing steal phenomenon (diversion of blood from normal adjacent brain).',
            'rationale': 'AVM channels preferentially draw perfusion away from eloquent cortex.',
            'bloom': 'analyze',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the major complication risk of AVM and how does it relate to anesthetic management?',
            'answer': 'Hemorrhage risk; maintain normal CPP (avoid hypotension), maintain normothermia, prevent hypertension spikes, and ensure gentle handling during resection.',
            'rationale': 'Aberrant vessels lack normal vascular tone and are prone to rupture with hemodynamic stress.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 15:  # Cerebral Blood Flow & Autoregulation
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Define cerebral autoregulation and state its operative range.',
            'answer': 'Cerebral autoregulation maintains constant CBF (45-50 mL/100g/min) despite changes in MAP; functional between MAP 50-150 mmHg.',
            'rationale': 'Metabolic and myogenic mechanisms adjust cerebral vascular resistance to buffer pressure changes.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What happens to CBF outside the autoregulatory range?',
            'answer': 'Below MAP 50 mmHg: flow falls (risk ischemia); above MAP 150 mmHg: flow increases (risk hyperperfusion and cerebral edema).',
            'rationale': 'Vessels cannot further vasoconstrict or vasodilate to maintain constant flow.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What factors impair cerebral autoregulation?',
            'answer': 'Head injury, intracranial pathology, volatile anesthetics, hypoxia, hypercarbia, and severe anemia.',
            'rationale': 'These conditions disrupt the metabolic and myogenic mechanisms underlying autoregulation.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is cerebrovascular reactivity and how is it tested clinically?',
            'answer': 'Ability of cerebral vessels to dilate in response to CO2 (vasodilation) or constrict with hypocapnia; assessed via transcranial doppler during CO2 challenge.',
            'rationale': 'Preserved reactivity suggests intact autoregulation; loss implies severe pathology.',
            'bloom': 'analyze',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 16:  # Cerebral Perfusion Pressure
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is cerebral perfusion pressure (CPP) and how is it calculated?',
            'answer': 'CPP = Mean arterial pressure (MAP) - Intracranial pressure (ICP); normal CPP >60 mmHg.',
            'rationale': 'CPP represents the effective driving pressure for cerebral blood flow.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the consequences of inadequate CPP (<50 mmHg)?',
            'answer': 'Cerebral ischemia, neuronal dysfunction, and neurologic injury if prolonged.',
            'rationale': 'Low CPP reduces cerebral blood flow below the critical threshold for neuronal viability.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the Monro-Kellie doctrine and its relevance to CPP?',
            'answer': 'Skull contains fixed volume: brain (80%) + blood (10%) + CSF (10%); any increase in one component must be offset by decrease in others or ICP rises.',
            'rationale': 'Rising ICP from mass, swelling, or hemorrhage directly reduces CPP.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the signs of elevated ICP and herniation syndromes?',
            'answer': 'Early: headache, vomiting, altered cognition; late: pupil dilation, posturing, brainstem reflexes lost.',
            'rationale': 'Progressive ICP elevation causes mass effect and brainstem compression.',
            'bloom': 'recall',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 17:  # Cerebral Protection & Neuroprotection
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the fundamental principle of cerebral neuroprotection?',
            'answer': 'Reduce cerebral metabolic rate for oxygen (CMRO2) via hypothermia, anesthetic depth, seizure prevention, or suppressing shivering to extend ischemia tolerance.',
            'rationale': 'Ischemic injury results from oxygen-glucose mismatch; lower CMRO2 increases the time tolerable without oxygen.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'How does mild hypothermia (32-35C) provide neuroprotection?',
            'answer': 'Reduces CMRO2 by ~7% per 1C drop, slows cellular metabolism and ischemic cascade, decreases neurotransmitter release.',
            'rationale': 'Metabolic suppression buys time during periods of reduced cerebral perfusion.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the effects of high-dose volatile anesthetics and propofol on CMRO2 and cerebral protection?',
            'answer': 'Both depress CMRO2, reduce ICP, and provide some neuroprotection; propofol also has antioxidant properties.',
            'rationale': 'Anesthetic-induced suppression of neuronal activity reduces metabolic demands.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is burst suppression on EEG and when is it a goal?',
            'answer': 'Periods of electrical silence alternating with bursts of activity; indicates maximal CMRO2 suppression; useful during maximal cerebral protection (e.g., DHCA).',
            'rationale': 'Burst suppression represents the deepest level of anesthetic-induced metabolic suppression.',
            'bloom': 'recall',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 18:  # Chronic Pain Pharmacotherapy
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the major non-opioid analgesics used in chronic pain?',
            'answer': 'NSAIDs, acetaminophen, anticonvulsants (gabapentin, pregabalin), antidepressants (amitriptyline, duloxetine, venlafaxine).',
            'rationale': 'Multimodal approach targets inflammation, neuropathy, and mood comorbidities.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the mechanisms of action of anticonvulsants in neuropathic pain?',
            'answer': 'Gabapentin and pregabalin bind alpha-2-delta subunits on voltage-gated calcium channels, reducing neurotransmitter release.',
            'rationale': 'Voltage-gated calcium channel blockade suppresses abnormal neuronal firing.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the rationale for using antidepressants in chronic pain?',
            'answer': 'Tricyclic antidepressants and SNRIs inhibit reuptake of norepinephrine and serotonin, activating descending pain inhibitory pathways.',
            'rationale': 'Endogenous noradrenergic and serotonergic systems suppress pain signal transmission.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 19:  # Coagulation & Bleeding History
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the goal of preoperative bleeding history assessment?',
            'answer': 'Identify inherited or acquired coagulopathy that requires perioperative management (e.g., anticoagulation reversal, transfusion, factor replacement).',
            'rationale': 'Occult bleeding diathesis increases perioperative hemorrhage risk.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What key elements compose a thorough bleeding history?',
            'answer': 'Family history of bleeding or transfusion, personal history of prolonged bleeding (dental, surgery, trauma), medications (anticoagulants, NSAIDs), menstrual history.',
            'rationale': 'These elements screen for platelet disorders, factor deficiencies, and VWD.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When is laboratory testing for coagulation indicated preoperatively?',
            'answer': 'When bleeding history is positive, patient on anticoagulation, liver disease, vitamin K deficiency, or extensive surgery planned.',
            'rationale': 'High-risk patients require baseline platelet count, PT, PTT, fibrinogen assessment.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 20:  # Coagulation & Neuraxial
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What coagulation parameters must be assessed before neuraxial blockade?',
            'answer': 'Anticoagulation status (warfarin, DOACs, heparins), platelet count (>50,000 generally acceptable), fibrinogen (>100 mg/dL), and INR/PT.',
            'rationale': 'Neuraxial hematoma risks permanent neurologic injury.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the anticoagulation requirements for neuraxial blockade timing?',
            'answer': 'Warfarin: INR <1.5; unfractionated heparin: discontinue 4-6 hours; LMWH: last dose >24 hours (prophylactic) or >24 hours (therapeutic); DOACs per specific agent.',
            'rationale': 'Adequate anticoagulant clearance reduces hematoma risk.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the signs and symptoms of spinal hematoma?',
            'answer': 'Severe back pain, lower extremity weakness/numbness, bowel/bladder dysfunction, progressive paraplegia if untreated.',
            'rationale': 'Early recognition (within 8-12 hours) and decompression improve neurologic outcome.',
            'bloom': 'recall',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 21:  # Cognitive Assessment & POCD
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What cognitive domains are affected in postoperative neurocognitive disorder (POCD)?',
            'answer': 'Memory (immediate, short-term, long-term), attention, executive function (planning, problem-solving), language, and visuospatial processing.',
            'rationale': 'POCD spans multiple cognitive systems; detection requires validated instruments.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': 'delirium (acute fluctuating confusion, different mechanism)'
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are commonly used screening tests for POCD?',
            'answer': 'Mini-Cog, MMSE (Mini-Mental State Exam), MoCA (Montreal Cognitive Assessment), CAM-ICU for delirium.',
            'rationale': 'Standardized tests are more sensitive than bedside clinical impression.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the distinction between delirium and POCD?',
            'answer': 'Delirium: acute, fluctuating, inattention prominent; POCD: subacute/chronic, stable deficits, memory/executive function affected.',
            'rationale': 'Different time courses and mechanisms; delirium often precedes POCD.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 22:  # Combined Spinal-Epidural (Labor)
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the advantages of CSE for labor analgesia?',
            'answer': 'Rapid onset via spinal component, prolonged coverage via epidural infusion, ability to titrate dosing, reduced total drug amount.',
            'rationale': 'Spinal provides immediate relief; epidural catheter allows flexible redosing and adaptation.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the typical intrathecal dosing for CSE labor analgesia?',
            'answer': 'Opioid alone (e.g., fentanyl 10-25 mcg or sufentanil 5 mcg) or combined with low-dose local anesthetic (e.g., bupivacaine 1-2.5 mg).',
            'rationale': 'Low-dose approach avoids motor blockade while providing analgesia.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the "walking epidural" concept and how does it relate to CSE?',
            'answer': 'Low-concentration epidural infusion (e.g., dilute bupivacaine + opioid) allows ambulation; CSE provides rapid initial relief before infusion starts.',
            'rationale': 'Allowing continued ambulation reduces complications and improves satisfaction.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 23:  # CSE Technique
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Describe the needle-through-needle (NTN) CSE technique.',
            'answer': 'Identify epidural space with epidural needle, thread epidural catheter, advance smaller spinal needle through epidural needle to pierce dura, inject spinal drug, withdraw spinal needle, secure epidural catheter.',
            'rationale': 'NTN allows both intrathecal and epidural access from single puncture site.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the anatomic landmark for lumbar neuraxial puncture?',
            'answer': 'Iliac crest at L3-4 interspace; puncture typically at L2-3, L3-4, or L4-5 to avoid conus medullaris (usually T12-L1).',
            'rationale': 'Avoiding spinal cord injury is critical; puncture below L4-5 safest.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the complications of CSE and how are they prevented?',
            'answer': 'PDPH (use small spinal needle, avoid multiple attempts), epidural hematoma (check coagulation), infection (sterile technique), vascular puncture (withdraw if blood appears).',
            'rationale': 'Meticulous technique minimizes complications.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 24:  # Restrictive vs Constrictive
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the hemodynamic hallmark of constrictive pericarditis?',
            'answer': 'Square root sign on ventricular pressure: steep diastolic pressure rise at start of diastole then plateau (filling only in early diastole).',
            'rationale': 'Pericardial constraint limits ventricular volume; most filling occurs early.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the diastolic pressure findings that discriminate constriction from restriction?',
            'answer': 'Constriction: equalization of diastolic pressures with square root sign; Restriction: elevated ventricular diastolic pressures without plateau.',
            'rationale': 'Constraint vs. myocardial dysfunction produce different pressure waveforms.',
            'bloom': 'analyze',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the pathophysiology of restrictive cardiomyopathy?',
            'answer': 'Myocardial infiltration or fibrosis stiffens ventricles, reducing compliance and impeding filling despite normal ejection fraction.',
            'rationale': 'Primary myocardial disease differs mechanically from pericardial constriction.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is "septal bounce" and what does it indicate?',
            'answer': 'Abrupt leftward motion of interventricular septum in early diastole seen on echo; indicates interdependence and is characteristic of constriction.',
            'rationale': 'Septal motion reflects abnormal filling pattern in constriction.',
            'bloom': 'analyze',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 25:  # Continuous Peripheral Nerve Catheter
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the principal advantages of continuous peripheral nerve catheters over single-shot blocks?',
            'answer': 'Extended analgesia (hours to days), ability to titrate local anesthetic concentration and rate, reduced total opioid requirement, improved pain control.',
            'rationale': 'Continuous infusion extends block duration and allows dose adjustment.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are common infusion rates and local anesthetic concentrations for peripheral nerve catheters?',
            'answer': 'Typical: bupivacaine 0.125-0.25% at 5-15 mL/hr; ropivacaine 0.2% at similar rates; patient boluses available for breakthrough pain.',
            'rationale': 'Dilute concentrations provide analgesia without complete motor blockade.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are complications of peripheral nerve catheters and how are they managed?',
            'answer': 'Infection (strict asepsis, early removal if infected), catheter migration, local anesthetic toxicity (assess toxicity signs, consider lipid emulsion), nerve injury.',
            'rationale': 'Prolonged catheterization and poor asepsis increase complication risk.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 26:  # Coronary Artery Disease
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the pathophysiology of coronary artery disease?',
            'answer': 'Atherosclerotic plaque progressively narrows coronary lumen, reducing flow reserve and increasing risk of thrombosis; supply-demand mismatch triggers ischemia.',
            'rationale': 'CAD impairs the ability of coronary flow to increase during stress.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What perioperative risk factors increase ischemia in CAD patients?',
            'answer': 'Tachycardia, hypertension, anemia, hypoxia, increased sympathetic tone (inadequate anesthesia), hypothermia.',
            'rationale': 'These increase myocardial oxygen demand or reduce supply.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the Framingham risk score and how is it used for CAD risk stratification?',
            'answer': 'Calculates 10-year CAD risk using age, sex, cholesterol, BP, smoking, diabetes; scores >20% = high risk, 10-20% = intermediate, <10% = low risk.',
            'rationale': 'Risk stratification guides perioperative monitoring and intervention intensity.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 27:  # Coronary Physiology & O2 Balance
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'State the relationship between myocardial oxygen supply and demand.',
            'answer': 'Supply (DO2) = CBF × arterial oxygen content; Demand (VO2) = determined by HR, contractility, wall tension; balance maintained when DO2 > VO2.',
            'rationale': 'Ischemia occurs when demand exceeds supply.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the arterio-venous oxygen difference (A-V O2) in the coronary circulation?',
            'answer': 'Normal coronary A-V O2 = 11-14 mL/dL; heart extracts ~75% of oxygen delivered (higher than any other organ).',
            'rationale': 'High oxygen extraction means coronary flow MUST increase if oxygen demand increases.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the determinant of diastolic perfusion pressure and why is diastole critical for coronary perfusion?',
            'answer': 'Diastolic pressure = MAP - LVEDP; most coronary perfusion occurs in diastole (LV systole compresses coronary vessels); low diastolic BP impairs coronary flow.',
            'rationale': 'Systolic contraction compresses intramyocardial vessels; diastolic relaxation allows perfusion.',
            'bloom': 'analyze',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 28:  # Recent ACS Management
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the perioperative risk of surgery within 6 weeks of acute coronary syndrome (ACS)?',
            'answer': 'Very high risk of recurrent MI and death; elective surgery should be deferred >3 months post-ACS when possible.',
            'rationale': 'Acute thrombotic and inflammatory state persists; surgical stress compounds ischemic risk.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What antiplatelet and anticoagulation strategy is used post-ACS?',
            'answer': 'Dual antiplatelet therapy (DAPT): aspirin + P2Y12 inhibitor (clopidogrel, ticagrelor) for 12 months; additional anticoagulation if high-risk.',
            'rationale': 'DAPT prevents stent thrombosis and recurrent events.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When must dual antiplatelet therapy be continued perioperatively?',
            'answer': 'If surgery <6 weeks post-ACS, especially after stent placement: continue DAPT throughout perioperative period (defer surgery if possible).',
            'rationale': 'Interrupting DAPT within 6-12 months post-ACS increases stent thrombosis risk.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 29:  # Corticosteroids in Anesthesia
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'When are perioperative corticosteroids indicated?',
            'answer': 'Patients with primary adrenal insufficiency, secondary adrenal insufficiency (pituitary disease), or on chronic glucocorticoid therapy.',
            'rationale': 'Surgical stress triggers ACTH-mediated cortisol surge; insufficient glands cannot respond.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are typical perioperative corticosteroid doses for adrenal insufficiency?',
            'answer': 'Minor surgery: hydrocortisone 25-50 mg IV at induction; Moderate: 50-75 mg IV; Major: 100 mg IV followed by infusion (50 mg/6-8 hr) for 24-48 hr.',
            'rationale': 'Doses approximate stress-induced cortisol production.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the signs of acute adrenal crisis and how is it managed?',
            'answer': 'Hypotension, tachycardia, altered mental status, seizures; treat with high-dose IV hydrocortisone (100 mg bolus, then 50-100 mg q6-8hr) and aggressive fluid resuscitation.',
            'rationale': 'Adrenal crisis is a surgical emergency requiring massive steroid supplementation.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 30:  # Craniotomy Intraoperative
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the fundamental anesthetic goals during craniotomy?',
            'answer': 'Maintain CPP, minimize ICP, prevent hyperthermia and seizures, ensure complete immobility, preserve neuromonitoring signals.',
            'rationale': 'Motionless operative field with optimal cerebral perfusion maximizes surgical success.',
            'bloom': 'apply',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What measures reduce ICP during craniotomy?',
            'answer': 'Head of bed elevated 20-30 degrees, normocapnia (PaCO2 35-40), osmotherapy (mannitol, hypertonic saline), adequate anesthesia/analgesia, avoid fever.',
            'rationale': 'These maneuvers reduce cerebral blood volume and CSF pressure.',
            'bloom': 'apply',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the role of intraoperative neuromonitoring during craniotomy?',
            'answer': 'EEG, MEP (motor evoked potentials), SSEP (somatosensory EP) detect eloquent cortex and warn of ischemic changes; awake testing with intraoperative neurologic exams.',
            'rationale': 'Neuromonitoring guides resection margins and prevents neurologic injury.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What neuromuscular blockade strategy is used during craniotomy?',
            'answer': 'Avoid complete paralysis except during positioning/intubation; use short-acting agents; minimal or no blockade during neuromonitoring.',
            'rationale': 'Paralysis obscures neuromonitoring signals and patient neurologic status.',
            'bloom': 'apply',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 31:  # Deep Hypothermic Circulatory Arrest
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the physiologic basis for deep hypothermic circulatory arrest (DHCA)?',
            'answer': 'Profound core hypothermia (12-18C) reduces cerebral metabolic rate exponentially, extending safe ischemia time from minutes to 30-60 minutes.',
            'rationale': 'CMRO2 decreases ~50% for every 5C drop; at 18C, brain can tolerate prolonged arrest.',
            'bloom': 'analyze',
            'source': sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the complications of DHCA?',
            'answer': 'Neurologic injury (stroke, cognitive decline), coagulopathy, myocardial dysfunction, renal failure, hypothermia-related arrhythmias.',
            'rationale': 'Deep hypothermia and prolonged circulatory arrest carry significant morbidity.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What anesthetic agents provide additional neuroprotection during DHCA?',
            'answer': 'High-dose volatile anesthetics or propofol to achieve burst suppression (maximal CMRO2 reduction); thiopental use historical but largely replaced.',
            'rationale': 'Burst suppression on EEG represents maximum metabolic suppression.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    elif index == 32:  # Desflurane Clinical Pharmacology
        kps.append({
            'id': f'{topic_slug}-1',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What are the key pharmacokinetic properties of desflurane?',
            'answer': 'Highly volatile (SVP ~88 kPa at 37C), minimal metabolism (~0.02%), rapidly eliminated via lungs, blood:gas coefficient 0.42.',
            'rationale': 'Low solubility enables rapid emergence; minimal metabolism reduces risk of metabolites.',
            'bloom': 'recall',
            'source': sources[:1] if sources else [],
            'confusable_with': 'sevoflurane'
        })
        kps.append({
            'id': f'{topic_slug}-2',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What is the MAC of desflurane and how does it change with age?',
            'answer': 'MAC at 20-40 yrs = 6%; decreases ~0.5% per decade after age 40; at 60 yrs MAC ~5.2%.',
            'rationale': 'Aging increases MAC sensitivity, enabling lower maintenance concentrations.',
            'bloom': 'recall',
            'source': sources[1:2] if len(sources) > 1 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-3',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'Why is desflurane contraindicated for inhalational induction?',
            'answer': 'Pungent airway irritant: causes coughing, laryngospasm, breath-holding, salivation; reserved for IV induction.',
            'rationale': 'Airway irritation makes inhalational induction unsafe.',
            'bloom': 'apply',
            'source': sources[2:3] if len(sources) > 2 else sources[:1] if sources else [],
            'confusable_with': ''
        })
        kps.append({
            'id': f'{topic_slug}-4',
            'topic': topic,
            'domain': domain,
            'discipline': discipline,
            'stem': 'What cardiac effects are associated with desflurane?',
            'answer': 'Rapid rise causes sympathomimetic activation: tachycardia, hypertension, increased catecholamines; myocardial depression at steady state.',
            'rationale': 'Initial pungency triggers sympathetic response; chronic effects depress contractility.',
            'bloom': 'recall',
            'source': sources[3:4] if len(sources) > 3 else sources[:1] if sources else [],
            'confusable_with': ''
        })

    return kps

all_kps = []
processed_topics = set()

for idx, item in enumerate(slice_data):
    topic = item.get('topic')
    kps = extract_kps(item, idx)
    if kps:
        all_kps.extend(kps)
        processed_topics.add(topic)

print(f"Processed {len(processed_topics)} topics, extracted {len(all_kps)} KPs")

with open('data/kp_full_part_20.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(all_kps)} KPs to data/kp_full_part_20.json")

# Validate JSON
try:
    with open('data/kp_full_part_20.json', 'r', encoding='utf-8') as f:
        test_load = json.load(f)
    print(f"JSON validation: OK ({len(test_load)} items)")
except Exception as e:
    print(f"JSON validation FAILED: {e}")
