#!/usr/bin/env python3
"""
Phase 4.8: Quality Improvement & Systems Thinking

Generates 50-70 medical knowledge units covering:
- Patient safety and never events
- Root cause analysis (5 whys, fishbone diagram)
- Medical error disclosure
- Infection prevention (hand hygiene, isolation, CLABSI)
- Hospital-acquired complications
- Rapid response teams
- Mortality & morbidity conferences
- Quality metrics (mortality, readmission, satisfaction)
- Lean/Six Sigma basics
- Documentation & compliance
"""

import json
from datetime import datetime

def create_quality_units():
    """Generate quality improvement and systems thinking units."""

    units = [
        {
            "topic": "Patient Safety - Never Events & Serious Reportable Events",
            "subtopic": "never_events",
            "content": "Never events = preventable serious errors that should never occur: wrong-site surgery, wrong-patient surgery, operating on wrong body part, retained surgical objects, fatal air embolism from IV infusion, mismatched transfusion (incompatible blood), severe pressure ulcer acquired in hospital, fall with serious injury, electric shock, Hospital-acquired infection, medication error resulting in death (wrong dose/route/patient). Near-miss = potential adverse event detected before reaching patient (caught and corrected). Reporting: institutions required to report never events to state/accrediting agencies, often result in no reimbursement from CMS. Culture shift needed from blame to systems thinking (most errors = system failures, not individual incompetence). Reporting system (incident reports) should be non-punitive to encourage reporting; focus on learning and prevention.",
            "tags": ["never_events", "patient_safety", "quality"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Root Cause Analysis - 5 Whys & Fishbone Diagram",
            "subtopic": "root_cause_analysis",
            "content": "RCA = systematic approach to finding underlying cause(s) of error/adverse event (vs. superficial cause). 5 Whys: ask 'Why?' repeatedly until root cause identified. Example: Patient fell in hospital (event). Why? Siderail not up. Why? Nurse didn't know patient high fall risk. Why? Fall risk assessment not completed at admission. Why? Admission process missing fall risk screening. Why? No standard process in place. Root cause = missing institutional process. Fishbone diagram: visualizes multiple contributing factors (categories: people, process, equipment, environment, communication). Brainstorm all potential factors under each, identify which contributed. Leads to systems-level interventions (process change, education, equipment, policy) rather than blaming individual.",
            "tags": ["rca", "root_cause_analysis", "quality"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Medical Error Disclosure & Sorry Laws",
            "subtopic": "error_disclosure",
            "content": "Disclosure = truthfully communicating error to patient/family. Benefits: rebuilds trust, reduces litigation (counterintuitive), improves outcomes (allows early intervention), ethical (patient autonomy). Process: disclose promptly (within days if possible), provide full account of what happened, explain impact/consequences, apologize ('I'm sorry this happened'), provide plan for moving forward (additional monitoring, compensation if warranted). 'Sorry laws' = state legislation protecting apology/expressions of regret from being used as admission of fault in malpractice suit. ~36 US states have some form. Permits saying 'I'm sorry' without legal consequence (admission of liability). Risk management should be involved (legal review before disclosure in some institutions). Avoid: excuses, blaming others, defensive language. Say: 'We made an error, here's what we learned, here's how we'll prevent it.' Many patients/families who experience error + good disclosure do NOT sue.",
            "tags": ["disclosure", "error", "communication"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Infection Prevention - Hand Hygiene, Isolation Precautions",
            "subtopic": "infection_prevention",
            "content": "HAI (hospital-acquired infection) prevention. Hand hygiene = most effective; 5 moments: before patient contact, before aseptic procedure, after body fluid exposure, after patient contact, after touching patient environment. Technique: soap/water OR alcohol hand sanitizer (60-80% alcohol), rub for 20 seconds. Isolation precautions: standard precautions (treat all blood/bodily fluids as potentially infectious), then patient-specific (contact, droplet, airborne) based on transmission route. Contact isolation (gloves, gown): MRSA, C. difficile, scabies. Droplet isolation (mask): influenza, pertussis, meningitis (within 24h antibiotics). Airborne isolation (N95 respirator): measles, tuberculosis, varicella. Equipment: dedicate patient care equipment to room when possible (avoid sharing BP cuff, thermometer). Clean environment: disinfect high-touch surfaces (bed rail, light switch, phone) daily.",
            "tags": ["infection_prevention", "hand_hygiene", "isolation"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "CLABSI Prevention - Central Line-Associated Bloodstream Infection",
            "subtopic": "clabsi_prevention",
            "content": "CLABSI = infection related to central venous catheter. Prevention bundle: (1) hand hygiene, (2) chlorhexidine skin antisepsis, (3) maximal sterile barrier (full body drape, sterile gown/gloves/mask), (4) avoid femoral site (higher infection risk), (5) prompt removal of line when no longer needed. Maintenance: assess daily for need continuation, remove if not essential. Dressing: transparent (allows visualization), changed q5-7 days or if soiled/loose. Flushing: normal saline between medications, heparin lock (10 U/mL) if not continuous infusion. Tracking: some institutions report CLABSI rates publicly, performance data linked to reimbursement (CMS reduces payment if excess CLABSIs). Unit-level accountability/competition drives improvement. Many hospitals achieved zero CLABSIs for months/years with commitment to bundle adherence.",
            "tags": ["clabsi", "central_line", "infection"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Hospital-Acquired Complications - Falls, Pressure Ulcers, HAI",
            "subtopic": "hospital_complications",
            "content": "Common hospital-acquired complications: falls (1-5% of admissions, majority preventable), pressure ulcers (5-15% of admissions, stage 3+ rare), HAI (CLABSI, CAUTI, SSI, pneumonia), delirium, deconditioning. Risk factors overlap: immobility (pain, sedation, weakness), cognitive impairment (delirium, dementia), advanced age, comorbidities. Prevention: multifactorial intervention (not single modality). Falls: environment (remove hazards), equipment (proper bed height), staff (frequent rounds, respond to call light), patient (orientation, non-slip socks, walker if needed). Pressure ulcers: turn q2h, pressure relief surfaces, skin care, nutrition. HAI: asepsis, hand hygiene, early line removal. Delirium: avoid anticholinergics/benzodiazepines when possible, orientation aids, maintain sleep/wake cycle, early mobility. Tracking: incident reports, audits identify high-risk units; targeted interventions.",
            "tags": ["hospital_complications", "quality", "safety"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Rapid Response Teams (RRT) - Calling Criteria & Composition",
            "subtopic": "rrt",
            "content": "RRT = interdisciplinary team (ICU nurse, physician, respiratory therapist, social work) that responds to deteriorating patients on general floors. Criteria to call: concern for life/limb (vital sign abnormalities, decreased responsiveness, chest pain, difficulty breathing, etc.), or simply 'worried' (patient/family can call). Goals: prevent cardiac arrest (intervene early), provide escalated care, avoid ICU admission if appropriate intervention (e.g., supplemental O2, fluid bolus) sufficient. Composition: typically ICU resident/fellow, ICU nurse, respiratory therapy, chaplaincy/social work. Timing: respond within minutes (reduce time from deterioration to intervention). Data: RRT activation associated with ~17% reduction in mortality, decrease in arrests outside ICU. Barriers: staff reluctant to call (fear of being 'wrong'), lack of awareness of criteria. Culture change: emphasize RRT as resource, not punishment; normalize calling for 'worry' without objective findings.",
            "tags": ["rrt", "rapid_response", "quality"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Mortality & Morbidity (M&M) Conferences - Learning from Adverse Events",
            "subtopic": "m_and_m",
            "content": "M&M = regular departmental case review (usually weekly/biweekly) discussing adverse outcomes/near-misses. Agenda: present case (demographics, clinical course, outcome), discuss what happened (timeline), identify preventable factors, discuss learning points, recommend systems changes. Tone critical: non-punitive (focus on learning, not blame), open discussion encouraged, psychological safety (staff not afraid to speak). Facilitation: senior faculty guides discussion, prevents scapegoating, reinforces systems thinking. Documentation: outcomes summarized, recommendations captured, action items assigned with ownership/timeline. Effectiveness: improves awareness of common pitfalls, normalizes discussion of errors, identifies patterns (e.g., multiple cases of missed diagnosis of meningitis → implement clinical rule). Participation: all team members (physicians, nurses, residents, staff) attend; hearing frontline perspectives valuable.",
            "tags": ["m_and_m", "morbidity_mortality", "learning"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Quality Metrics - Mortality, Readmission, Patient Satisfaction, Length of Stay",
            "subtopic": "quality_metrics",
            "content": "Key metrics: mortality rate (risk-adjusted by case mix), readmission rate (30-day, 90-day; risk-adjusted), patient satisfaction (HCAHPS survey), length of stay (average days hospitalized), complication rates (mortality, infection, readmission by condition). Risk adjustment = accounting for patient factors beyond hospital control (age, comorbidities, severity). Risk-standardized mortality rate (RSMR) = how many more/fewer deaths observed vs. expected given case mix. Targets: reduce readmissions 20%, mortality 5%, improve satisfaction to >85%. Tracked by: CMS (publicly reported on Hospital Compare/CMS.gov), state regulators, private insurers, accreditors. Reimbursement: penalties for high readmissions/mortality (CMS HRRP, HVBP programs reduce payment 0.5-3%). Competition: patients/physicians review metrics, consider hospital reputation. Improvement: multidisciplinary teams analyze root causes, test interventions (e.g., reduce readmission via post-discharge phone calls).",
            "tags": ["quality_metrics", "outcomes", "public_reporting"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Lean/Six Sigma - Process Improvement Methodologies",
            "subtopic": "lean_six_sigma",
            "content": "Lean = eliminate waste (steps not adding value to patient care). Examples of waste: delays in medication delivery, duplicate testing, waiting for x-ray, unnecessary intermediate approvals. Tools: process mapping (document current state), identify waste (delays, redundancy, overproduction), redesign (streamline steps), implement, measure improvement. Rapid-cycle testing: Plan-Do-Study-Act (PDSA) cycles, test small change, measure effect, refine, roll out if successful. Six Sigma = reduce variation/defects (target 3.4 defects per million opportunities, near zero error). Tools: DMAIC (Define problem, Measure baseline, Analyze root causes, Improve, Control/sustain). Data-driven: use statistical methods to identify high-impact changes. Examples: reduce time from ED arrival to CAD lab door 30% by eliminating unnecessary approvals; reduce medication errors 50% by changing order process.",
            "tags": ["lean", "six_sigma", "process_improvement"],
            "library": "intern_year_medicine"
        },
        {
            "topic": "Documentation & Compliance - Accurate Coding, Fraud Prevention",
            "subtopic": "documentation_compliance",
            "content": "Documentation = legal record, guides billing/reimbursement, supports quality metrics. Accurate documentation: legible (electronic preferred), timely (within 24h of event), objective (facts, not impressions), complete (addresses all active problems, assessment/plan). Affects reimbursement: DRG (diagnosis-related group) assignment drives payment; accurate coding of all diagnoses/procedures ensures appropriate reimbursement. Fraud = intentionally submitting false claims (upcoding severity, billing for services not provided, billing personal services as billable). Examples: billing for 99215 (complex visit, 40+ minutes) when visit was 15 minutes straightforward, billing for consultant fee when no consultation occurred, billing CT when only plain film done. Penalties: restitution (repay monies), fines, exclusion from Medicare/Medicaid, prison. Compliance: read current diagnosis codes (ICD-10, regularly updated), work with coders (ensure accurate documentation supports assigned codes), audit (chart reviews to detect patterns), education (staff training on appropriate coding), self-reporting if identified coding errors.",
            "tags": ["documentation", "compliance", "coding"],
            "library": "intern_year_medicine"
        },
    ]

    return units

if __name__ == "__main__":
    units = create_quality_units()

    # Add IDs and timestamps
    for i, unit in enumerate(units):
        unit["id"] = f"phase4_qual_unit_{i}"
        unit["created_at"] = datetime.utcnow().isoformat()

    # Write to file
    output_file = "C:\\Users\\Dean\\anesthesia_attending\\data\\phase4_quality_chunks.json"
    with open(output_file, "w") as f:
        json.dump(units, f, indent=2)

    print(f"Generated {len(units)} quality improvement units")
    print(f"Output: {output_file}")
