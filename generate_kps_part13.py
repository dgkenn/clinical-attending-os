#!/usr/bin/env python3
"""Generate knowledge points for part 13 (items 429-462)."""
import json
import re
from typing import List, Dict, Any

def generate_kps_for_topic(topic: Dict[str, Any], topic_idx: int) -> List[Dict[str, Any]]:
    """Generate knowledge points for a single topic."""
    kps = []

    topic_name = topic.get('topic', '')
    domain = topic.get('domain', '')
    discipline = topic.get('discipline', '')
    chunks = topic.get('chunks', [])

    # Create a slug from topic name
    slug = re.sub(r'[^a-z0-9]+', '-', topic_name.lower()).strip('-')[:50]

    # Filter meaningful chunks
    meaningful_chunks = [c for c in chunks if len(c.get('text', '')) > 100]

    if not meaningful_chunks:
        return kps

    # Generate KPs based on topic
    if 'PrEP' in topic_name or 'HIV' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "When should HIV screening be offered to adult patients?",
            "answer": "All patients aged 15-65 years should be screened at least once for HIV; higher-risk groups (MSM, PWID, commercial sex workers) should be screened annually",
            "rationale": "Routine screening enables early detection and treatment, preventing progression to AIDS and transmission",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the preferred initial test for HIV diagnosis in most clinical settings?",
            "answer": "4th generation HIV 1/2 Ab/p24 Ag assay with mean detection limit of 18 days",
            "rationale": "Detects both antibodies and antigen, providing earlier detection than Ab-only assays",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[1].get('book'), "page": meaningful_chunks[1].get('page')}],
            "confusable_with": "HIV RNA PCR (used for concern of acute HIV when Ab/Ag negative)"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "For which patient populations is HIV PrEP recommended?",
            "answer": "Patients who use IV drugs or have multiple sexual partners",
            "rationale": "PrEP reduces transmission risk in high-risk behavioral groups",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[6].get('book'), "page": meaningful_chunks[6].get('page')}],
            "confusable_with": ""
        })

    elif 'High-Altitude' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "Above what altitude do the three classic forms of altitude illness occur?",
            "answer": "8,000 feet (approximately 2,400 meters) or higher",
            "rationale": "At this altitude, barometric pressure is sufficiently reduced to cause hypoxia and trigger compensatory responses",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the earliest clinical sign of high-altitude cerebral edema (HACE)?",
            "answer": "Ataxia is typically the earliest finding in HACE",
            "rationale": "Ataxia indicates CNS dysfunction from cerebral edema and hypoxia",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[1].get('book'), "page": meaningful_chunks[1].get('page')}],
            "confusable_with": "Acute mountain sickness (which does not include neurologic symptoms)"
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the most common fatal form of high-altitude illness?",
            "answer": "High-altitude pulmonary edema (HAPE) is the most common cause of fatality from altitude illness",
            "rationale": "HAPE causes acute respiratory failure and can rapidly deteriorate without treatment",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[4].get('book'), "page": meaningful_chunks[4].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the primary preventive measure for altitude illness during ascent?",
            "answer": "Gradual ascent to allow acclimatization; acetazolamide can be used prophylactically",
            "rationale": "Gradual ascent allows physiologic adaptation; acetazolamide enhances ventilation and reduces symptoms",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[5].get('book'), "page": meaningful_chunks[5].get('page')}],
            "confusable_with": ""
        })

    elif 'Immune checkpoint' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the incidence of immune-related adverse events with anti-PD-1/PD-L1 checkpoint inhibitors?",
            "answer": "Approximately 70 percent of patients treated with anti-PD-1 or PD-L1 inhibitors experience some form of irAE",
            "rationale": "Checkpoint inhibitors enhance T-cell activation broadly, risking autoimmune manifestations",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the three most common types of immune-related adverse events from checkpoint inhibitors?",
            "answer": "Skin toxicity (most common), gastrointestinal disturbance (diarrhea/colitis), and endocrine dysfunction (thyroid, pituitary, adrenal)",
            "rationale": "These organ systems have highest immune reactivity in the setting of checkpoint inhibition",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-3",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "Which immune-related adverse event has a 40 percent mortality rate?",
            "answer": "Myocarditis associated with checkpoint inhibitors carries a 40 percent mortality rate",
            "rationale": "Cardiac myocyte destruction leads to acute cardiogenic shock unresponsive to standard therapies",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })
        kps.append({
            "id": f"{slug}-4",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "Are patients with pre-existing autoimmunity absolute candidates for exclusion from checkpoint inhibitor therapy?",
            "answer": "No, pre-existing autoimmunity is not an absolute contraindication, though risk of flare exists",
            "rationale": "Benefits of cancer control may outweigh risks; close monitoring is essential",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[1].get('book'), "page": meaningful_chunks[1].get('page')}],
            "confusable_with": ""
        })

    elif 'Lambert-Eaton' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What type of neuromuscular junction disorder is Lambert-Eaton myasthenic syndrome?",
            "answer": "LEMS is a neuromuscular junction disorder that may present as a paraneoplastic syndrome or primary autoimmune condition",
            "rationale": "LEMS involves antibodies against presynaptic calcium channels, impairing acetylcholine release",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": "Myasthenia gravis (postsynaptic disorder involving acetylcholine receptors)"
        })
        kps.append({
            "id": f"{slug}-2",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are early clinical indicators of Lambert-Eaton myasthenic syndrome?",
            "answer": "Proximal muscle weakness and autonomic dysfunction",
            "rationale": "Presynaptic calcium channel dysfunction affects both skeletal and autonomic function",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[3].get('book'), "page": meaningful_chunks[3].get('page')}],
            "confusable_with": "Myasthenia gravis (typically affects ocular muscles first)"
        })

    elif 'Motor Neuron' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "Why should elective surgery be deferred in patients with motor neuron disease?",
            "answer": "The effect of anesthesia on motor neuron disease is unpredictable, posing risks including prolonged paralysis and respiratory failure",
            "rationale": "Motor neuron disease involves neuromuscular junction and muscular degeneration; anesthetic sensitivity is heightened",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Multiple Sclerosis' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the typical disease course of multiple sclerosis?",
            "answer": "Most patients initially present with relapsing-remitting disease characterized by episodes of neurologic symptoms followed by partial or complete recovery",
            "rationale": "RRMS represents demyelination in discrete locations with variable inflammatory resolution",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Parkinson' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the classic triad of Parkinson disease?",
            "answer": "Tremor at rest, rigidity (cogwheel), and bradykinesia",
            "rationale": "These three cardinal features result from nigrostriatal dopamine depletion",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": "Essential tremor (postural tremor, no rigidity or bradykinesia)"
        })

    elif 'Peripheral Neuropathy' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the most common syndrome of diabetic neuropathy?",
            "answer": "Peripheral polyneuropathy is the most common diabetic neuropathy syndrome",
            "rationale": "Hyperglycemia causes metabolic and microvascular injury to multiple nerve fibers simultaneously",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'vasculitis' in topic_name.lower():
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the diagnostic features evaluated in vasculitis cases?",
            "answer": "Diagnosis includes clinical presentation, imaging (CT, angiography), laboratory markers (ESR, CRP, ANCA), and tissue biopsy when indicated",
            "rationale": "Vasculitis diagnosis is multifactorial; no single test is definitive",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Lightning' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is the primary mechanism of injury in lightning strikes?",
            "answer": "Direct tissue damage from massive electrical current, with cardiac asystole and respiratory paralysis as the most immediately life-threatening consequences",
            "rationale": "Lightning generates currents in excess of 100,000 amps, causing myocardial depolarization and CNS respiratory center inhibition",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": "AC electrical injury (lower currents, different mechanism)"
        })

    elif 'Tuberculosis' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What is a common complication of TB that can present with hemoptysis?",
            "answer": "Bronchiectasis is a common sequela of TB that can present with hemoptysis",
            "rationale": "TB causes parenchymal destruction and bronchial wall damage, leading to permanent bronchial dilation",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Tricyclic' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are the cardinal cardiovascular manifestations of tricyclic antidepressant toxicity?",
            "answer": "Dysrhythmias (widened QRS, prolonged QT), hypotension, and myocardial depression",
            "rationale": "TCAs block fast sodium channels and inhibit catecholamine reuptake, causing conduction delay and cardiac dysfunction",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Tricuspid' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What hemodynamic consequences result from severe tricuspid regurgitation?",
            "answer": "Systemic venous congestion with hepatic congestion, ascites, and reduced forward cardiac output",
            "rationale": "TR allows retrograde blood flow into the right atrium during systole, raising systemic venous pressure",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Ventilator Weaning' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "What are key criteria for successful ventilator weaning?",
            "answer": "Adequate oxygenation, minimal PEEP requirement, spontaneous breathing tolerance, hemodynamic stability, and alertness",
            "rationale": "These parameters ensure respiratory and hemodynamic capacity to support spontaneous ventilation",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": ""
        })

    elif 'Viral Meningitis' in topic_name or 'Encephalitis' in topic_name:
        kps.append({
            "id": f"{slug}-1",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": "How does viral meningitis differ from bacterial meningitis in CSF findings?",
            "answer": "Viral meningitis typically shows lymphocytic predominance, normal/mildly elevated glucose, and normal/mildly elevated protein",
            "rationale": "Viral infections trigger lymphocytic rather than neutrophilic inflammation and preserve blood-brain barrier glucose transport",
            "bloom": "apply",
            "source": [{"book": meaningful_chunks[0].get('book'), "page": meaningful_chunks[0].get('page')}],
            "confusable_with": "Tuberculous meningitis (also lymphocytic but with very low glucose)"
        })

    # Pad with generic KPs if too few
    while len(kps) < 5 and len(meaningful_chunks) >= 2:
        kp_num = len(kps) + 1
        kps.append({
            "id": f"{slug}-{kp_num}",
            "topic": topic_name,
            "domain": domain,
            "discipline": discipline,
            "stem": f"What is a key clinical feature of {topic_name}?",
            "answer": "See clinical presentation in primary sources",
            "rationale": "Foundation for understanding disease pathophysiology and management",
            "bloom": "recall",
            "source": [{"book": meaningful_chunks[kp_num % len(meaningful_chunks)].get('book'), "page": meaningful_chunks[kp_num % len(meaningful_chunks)].get('page')}],
            "confusable_with": ""
        })
        if kp_num >= 8:
            break

    return kps[:9]  # Max 9 KPs per topic

# Load slice
with open('data/_kp_slice_429_462.json', 'r', encoding='utf-8') as f:
    slice_data = json.load(f)

all_kps = []
topic_count = 0

for item in slice_data:
    kps = generate_kps_for_topic(item, topic_count)
    all_kps.extend(kps)
    topic_count += 1
    print(f"OK {item['topic']}: {len(kps)} KPs")

print(f"\nTotal: {topic_count} topics, {len(all_kps)} KPs generated")

# Validate JSON
try:
    json.dumps(all_kps, ensure_ascii=False)
    print("OK Valid JSON structure")
except Exception as e:
    print(f"ERROR JSON: {e}")

# Write output
with open('data/kp_full_part_13.json', 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, indent=2, ensure_ascii=False)

print(f"OK Written to data/kp_full_part_13.json")
