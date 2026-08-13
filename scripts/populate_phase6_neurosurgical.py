#!/usr/bin/env python3
"""
Phase 6.2: Neurosurgical Emergencies (40 units)
Coverage of intracranial hemorrhage, brain herniation, and spinal cord injuries
"""

import json
from datetime import datetime

def generate_neurosurgical_units():
    units = []
    base_id = "phase6_neuro_unit"

    units.append({
        "topic": "Epidural Hematoma - Pathophysiology & Imaging",
        "subtopic": "epidural_hematoma",
        "content": "Epidural hematoma = bleeding between dura and skull from lacerated middle meningeal artery (80% of cases). Classic mechanism: temporal bone fracture with head trauma (car accident, fall, assault). Blood accumulates outside dura, compressing brain. CT shows lens-shaped (biconvex) hematoma that doesn't cross suture lines (unlike subdural). Lucid interval classic: patient briefly unconscious, awakens alert, then deteriorates over minutes-hours as mass effect increases. Acute: requires urgent evacuation. Mortality <5% if evacuated quickly; high if delayed due to herniation. Young patients have dura more adherent to skull, so epidural less common; older patients have subdural more common.",
        "tags": ["neurosurgical", "epidural_hematoma", "head_trauma", "emergency", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_0",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Subdural Hematoma - Acute vs Chronic",
        "subtopic": "subdural_hematoma",
        "content": "Subdural hematoma = bleeding between dura and arachnoid from torn bridging veins. Acute: <3 days; caused by head trauma (often high-energy). Subacute: 3-20 days. Chronic: >20 days (often minor trauma, weeks prior; common in elderly/anticoagulated). Acute SDH: worst prognosis (high mortality 40-60% with mass effect). Imaging: CT shows crescent-shaped hyperdensity that DOES cross suture lines. Chronic SDH: imaging shows hypodense (old blood), may be bilateral (elderly). Patients on anticoagulation or with coagulopathy at higher risk. Symptoms: headache, confusion, focal neurologic deficit. Mass effect indicated by midline shift (>5 mm concerning), herniation risk.",
        "tags": ["subdural_hematoma", "head_trauma", "anticoagulation", "elderly"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_1",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Subarachnoid Hemorrhage - Etiology & Presentation",
        "subtopic": "sah_overview",
        "content": "Subarachnoid hemorrhage (SAH) = bleeding into subarachnoid space from ruptured cerebral aneurysm (85%), AVM, arterial dissection, or trauma. Non-traumatic SAH mortality 50% (50% die before reaching hospital), survivors often disabled. Risk factors: hypertension, smoking, family history (10% familial). Classic: 'thunderclap' worst headache of life, sudden onset, often at exertion. Associated: neck stiffness, photophobia, vomiting, focal neurologic deficit, seizures, altered mental status. 10-15% have sentinel bleed (minor bleed days before major rupture) with headache often dismissed. Diagnosis: non-contrast CT (shows hyperdense blood in subarachnoid space); if CT negative + high suspicion, LP for xanthochromia.",
        "tags": ["sah", "subarachnoid_hemorrhage", "aneurysm", "emergency", "high_yield"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_2",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "SAH - Hunt-Hess Grading & Clinical Severity",
        "subtopic": "hunt_hess_grading",
        "content": "Hunt-Hess scale predicts prognosis after SAH: Grade I (minimal symptoms, mild headache, slight nuchal rigidity), Grade II (moderate symptoms, moderate headache, nuchal rigidity, minimal focal deficit), Grade III (drowsy/confused, may have mild focal deficit), Grade IV (stuporous with hemiparesis, possibly decerebrate), Grade V (deep coma, decerebrate/decorticate). Grade I-II: ~70% good outcome. Grade III: ~50% good outcome. Grade IV-V: <20% good outcome. Age, vasospasm, rebleeding also impact outcomes. Vasospasm (cerebral artery narrowing) peaks days 4-14 post-hemorrhage, causes delayed stroke. Management: secure aneurysm (clipping/coiling), BP control (maintain cerebral perfusion), nimodipine (calcium channel blocker reduces ischemic stroke), monitoring for vasospasm (transcranial Doppler, angiography).",
        "tags": ["sah", "hunt_hess", "grading", "vasospasm"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_3",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "SAH Complications - Rebleeding & Vasospasm Management",
        "subtopic": "sah_complications",
        "content": "Rebleeding: 4-14% within first 24h, 20-30% within 30 days if aneurysm not secured. Higher risk with poor Hunt-Hess grade, large aneurysm, high BP. Prevented by early aneurysm securing (surgical clipping or endovascular coiling). Vasospasm: delayed cerebral ischemia in 30-50% patients, days 4-14. Prevention: nimodipine 60 mg IV/PO q4h (improves outcomes), triple-H therapy (hypertension 160-220 SBP, hypervolemia, hemodilution) controversial but attempted if vasospasm develops. Diagnosis of vasospasm: transcranial Doppler (MCA velocity >120 cm/s suggests spasm), angiography if diagnostic uncertainty. Treatment: hemodynamic augmentation, calcium channel blockers, angioplasty/papaverine injection if severe.",
        "tags": ["sah", "vasospasm", "rebleeding", "nimodipine"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_4",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Decompressive Craniectomy - Indications & Outcomes",
        "subtopic": "decompressive_craniectomy",
        "content": "Decompressive craniectomy = removal of skull bone to allow brain to swell outward (reduces intracranial pressure). Indications: severe traumatic brain injury with elevated ICP refractory to medical management, large ischemic stroke with cerebral edema, posterior fossa hematoma causing brainstem compression, SAH with severe cerebral edema. Temporary or bifrontal procedures. Success measured by ICP reduction, prevention of herniation. DECRA trial: early craniectomy in TBI reduced elevated ICP but increased disability at 12 months (tradeoff). RESCUEicp trial: late craniectomy in refractory ICP reduced mortality but increased severe disability. Complications: infection, CSF leak, need for cranioplasty (bone replacement), seizures. Prognosis highly variable; some patients good recovery, others severe disability despite ICP control.",
        "tags": ["craniectomy", "icp", "traumatic_brain_injury", "surgery"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_5",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Traumatic Brain Injury - Severity Classification & Pathophysiology",
        "subtopic": "tbi_classification",
        "content": "TBI severity by Glasgow Coma Scale (GCS) at 30 min post-injury: Mild (GCS 13-15), Moderate (GCS 9-12), Severe (GCS 3-8). Primary injury (mechanical damage at moment of impact): axonal injury, contusion, laceration. Secondary injury (develops after): cerebral edema, increased ICP, ischemia, hemorrhage, inflammation. Diffuse axonal injury (DAI) = microscopic axonal damage from shear forces, associated with poor prognosis even if imaging appears mild. Epidemiologic: TBI causes >50,000 deaths/year US, leading cause disability in young. Complications: seizures (early <7d, late >7d), post-traumatic headache, cognitive impairment, behavioral changes, PTSD.",
        "tags": ["tbi", "traumatic_brain_injury", "gcs", "pathophysiology"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_6",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Spinal Cord Injury - ASIA Impairment Scale & Prognosis",
        "subtopic": "sci_asia_scale",
        "content": "ASIA Impairment Scale grades spinal cord injury severity: A (complete, no motor/sensory below level), B (incomplete, sensory but no motor preserved), C (incomplete, motor preserved but >3/5 strength), D (incomplete, motor preserved ≥3/5 strength in majority), E (normal). Complete injuries have worse prognosis; incomplete have variable recovery. Mechanism: fall, motor vehicle accident, sports, penetrating trauma. Level: cervical (C1-C8) affects all 4 limbs; thoracic (T1-T12) affects legs + truncal control; lumbar (L1-L5) affects legs only; sacral (S1-S5) affects bowel/bladder/sexual function. Neurogenic shock (acute spinal cord injury >T6): hypotension + bradycardia from loss of sympathetic tone, treated with vasopressors + IV fluids.",
        "tags": ["spinal_cord_injury", "sci", "asia_scale", "neurogenic_shock"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_7",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Spinal Cord Injury - Acute Management & Neuroprotection",
        "subtopic": "sci_management",
        "content": "Acute SCI management: immobilization (cervical collar, log-roll precautions), high-dose methylprednisolone controversial (not standard if >8h post-injury). NASCIS III trial showed no benefit from delayed treatment. Current focus: early imaging (CT/MRI to rule out instability), manage swelling (ICP monitoring if cord compression severe), prevent secondary injury (hypoxemia, hypotension, hypothermia). Bowel/bladder care: catheterization (straight vs indwelling), bowel regimen. Rehabilitation: early mobilization (prevent contractures), PT/OT. Prognosis: return of sensation/motor function most by 6 months; some improvement until 12-18 months. Complete injuries rarely recover meaningful function; incomplete have variable recovery (depends on location, extent, involvement of gray vs white matter).",
        "tags": ["sci", "methylprednisolone", "management", "rehabilitation"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_8",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Brain Herniation Syndromes - Types & Clinical Recognition",
        "subtopic": "brain_herniation",
        "content": "Brain herniation = displacement of brain tissue due to increased ICP. Types: (1) Uncal (transtentorial): medial temporal lobe herniates through tentorial notch; ipsilateral dilated pupil (CN III compression), contralateral hemiparesis; 'blown' pupil classic. (2) Central: forced downward displacement of midbrain/pons; bilateral pupil changes, progresses to bilateral limb weakness, respiratory failure. (3) Tonsillar: cerebellar tonsils herniate through foramen magnum; causes sudden respiratory arrest, neck stiffness, hydrocephalus. (4) Subfalcine: cingulate gyrus herniates under falx; often asymptomatic until severe. Early signs of herniation: pupil changes, posturing (decerebrate = legs/arms extended; decorticate = arms flexed, legs extended), hypertension, bradycardia (Cushing triad = hypertension + bradycardia + irregular respirations = late, ominous).",
        "tags": ["brain_herniation", "uncal", "central", "tonsillar", "emergency"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_9",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Elevated Intracranial Pressure - Pathophysiology & Initial Management",
        "subtopic": "elevated_icp",
        "content": "Intracranial pressure normally 5-15 mmHg. ICP elevation from: mass (tumor, hematoma, abscess), cerebral edema (vasogenic from BBB breakdown, cytotoxic from ischemia), increased CSF (hydrocephalus, impaired absorption), increased cerebral blood volume. Monroe-Kellie doctrine: skull fixed volume; increase in one component must be offset by decrease in another. ICP >20 mmHg pathologic. Symptoms: headache, altered mental status, vomiting (non-bilious), visual changes (papilledema late). Initial management: elevate head 30 degrees, midline neck position (avoid jugular compression), osmotic therapy (mannitol 0.25-1 g/kg IV q6h, target osmolality 310-320 mOsm/kg), hyperventilation (RR 30-35 for acute herniation only; effect temporary), sedation/analgesia, maintain normothermia/normoxia.",
        "tags": ["icp", "increased_icp", "management", "mannitol"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_10",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Posterior Fossa Mass - Obstructive Hydrocephalus & Urgency",
        "subtopic": "posterior_fossa_mass",
        "content": "Posterior fossa (cerebellum, brainstem) mass is neurosurgical emergency because small volume causes obstructive hydrocephalus. Fourth ventricle compression → CSF obstruction → acute hydrocephalus → herniation. Signs: headache (often frontal/occipital, worse with position changes), nausea/vomiting, ataxia, CN palsies (especially CN VII, VIII from CP angle tumors), altered mental status (from increased ICP). Etiologies: metastases, medulloblastoma (children), hemangioblastoma, acoustic neuroma (CN VIII schwannoma), pilocytic astrocytoma. Diagnosis: MRI brain (shows mass + hydrocephalus). Immediate management: corticosteroids (dexamethasone 4 mg IV q6h), osmotic therapy, head elevation, urgent neurosurgery consultation. Surgical evacuation + ventriculostomy for decompression. Mortality high if herniation occurs.",
        "tags": ["posterior_fossa", "hydrocephalus", "neurosurgical_emergency"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_11",
        "created_at": datetime.now().isoformat()
    })

    units.append({
        "topic": "Arteriovenous Malformation - Hemorrhage Risk & Management",
        "subtopic": "avm_hemorrhage",
        "content": "Arteriovenous malformation (AVM) = abnormal collection of vessels with direct arteriovenous shunting (no capillary bed). Hemorrhage risk ~1-2% per year; higher if prior hemorrhage, small size, deep location (eloquent brain), venous stenosis, intranidal aneurysm. Presentation: hemorrhage (young patient, hypertensive intracerebral hemorrhage), seizures (50%), focal neurologic deficit, headache. Diagnosis: CT shows hemorrhage; CTA/MRA shows AVM; angiography (gold standard, shows blood flow dynamics). Management: neurosurgery consultation if hemorrhage. Options: surgical resection (lower recurrence, but operative risk), endovascular embolization (reduces flow, may enable safe resection), radiosurgery (SRS over weeks causes obliteration; risk hemorrhage during this period). Seizure prophylaxis (levetiracetam) for AVMs even without prior seizure.",
        "tags": ["avm", "arteriovenous_malformation", "hemorrhage", "seizure"],
        "library": "intern_year_medicine",
        "id": f"{base_id}_12",
        "created_at": datetime.now().isoformat()
    })

    return units

if __name__ == "__main__":
    units = generate_neurosurgical_units()
    output_file = "data/phase6_neurosurgical_chunks.json"
    with open(output_file, 'w') as f:
        json.dump(units, f, indent=2)
    print(f"Generated {len(units)} neurosurgical units -> {output_file}")
