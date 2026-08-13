#!/usr/bin/env python3
"""
TASK 2: Final Retrieval Validation
Test retrieval across ALL 4 phases with diverse queries
"""

import sys
import io

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.retrieval import hybrid_search

test_queries = [
    # Phase 1: Foundations
    ('NIHSS stroke severity assessment', 'Phase 1'),
    ('seizure lorazepam first-line treatment', 'Phase 1'),
    ('meningitis empiric antibiotics age-stratified', 'Phase 1'),

    # Phase 2: High-frequency
    ('pneumonia CURB-65 severity scoring', 'Phase 2'),
    ('ACS troponin STEMI diagnosis criteria', 'Phase 2'),
    ('PE Wells score D-dimer interpretation', 'Phase 2'),
    ('GI bleeding variceal octreotide dosing', 'Phase 2'),
    ('COPD exacerbation bronchodilator therapy', 'Phase 2'),
    ('DKA diabetic ketoacidosis fluid treatment', 'Phase 2'),
    ('hypothyroidism levothyroxine dosing', 'Phase 2'),
    ('AKI prerenal intrinsic postrenal', 'Phase 2'),

    # Phase 3: High-acuity ICU
    ('sepsis qSOFA score first-hour bundle', 'Phase 3'),
    ('ARDS lung-protective ventilation PEEP', 'Phase 3'),
    ('heart failure decompensation diuretics', 'Phase 3'),
    ('hypertensive emergency end-organ damage', 'Phase 3'),
    ('DIC disseminated intravascular coagulation', 'Phase 3'),
    ('liver failure encephalopathy management', 'Phase 3'),
    ('pancreatitis necrosis complications', 'Phase 3'),
    ('intracranial hypertension ICP management', 'Phase 3'),
    ('status epilepticus anesthetic induction', 'Phase 3'),
    ('MOF multiple organ failure SOFA', 'Phase 3'),

    # Phase 4: Remaining essentials
    ('acetaminophen toxicity N-acetylcysteine', 'Phase 4'),
    ('opioid overdose naloxone dosing', 'Phase 4'),
    ('alcohol withdrawal seizures benzodiazepines', 'Phase 4'),
    ('trauma ABCDE primary survey', 'Phase 4'),
    ('hemorrhage control tourniquet resuscitation', 'Phase 4'),
    ('central venous catheter placement complications', 'Phase 4'),
    ('preeclampsia magnesium sulfate eclampsia', 'Phase 4'),
    ('pediatric resuscitation CPR compression', 'Phase 4'),
    ('geriatric delirium CAM-ICU', 'Phase 4'),
    ('breaking bad news SPIKES framework', 'Phase 4'),
    ('root cause analysis medical error', 'Phase 4'),
]

print("=" * 80)
print("RETRIEVAL VALIDATION ACROSS ALL PHASES")
print("=" * 80)

results = []
passed = 0
failed = 0

for query, phase in test_queries:
    try:
        hits, _ = hybrid_search(query, mode='intern_teach', max_results=3)
        success = len(hits) >= 3 and hits[0].score >= 0.70

        if success:
            passed += 1
            status = "[OK]"
        else:
            failed += 1
            status = "[FAIL]"

        results.append({
            'phase': phase,
            'query': query,
            'success': success,
            'hits': len(hits),
            'top_score': hits[0].score if hits else 0.0
        })

        print(f"{status} {phase:8s} | {len(hits):1d} results (score={hits[0].score:.2f if hits else 0:.2f}) | {query}")

    except Exception as e:
        failed += 1
        results.append({
            'phase': phase,
            'query': query,
            'success': False,
            'hits': 0,
            'error': str(e)
        })
        print(f"[ERROR] {phase:8s} | {query} | {str(e)[:50]}")

# Summary
pass_rate = passed / len(results) * 100 if results else 0
print("\n" + "=" * 80)
print(f"SUMMARY: {passed}/{len(results)} queries passed ({pass_rate:.1f}%)")
print(f"Target: >=95% pass rate")
print(f"Status: {'PASS' if pass_rate >= 95 else 'WARN - consider re-indexing or expanding knowledge base'}")
print("=" * 80)

# Stats by phase
phase_stats = {}
for r in results:
    phase = r['phase']
    if phase not in phase_stats:
        phase_stats[phase] = {'passed': 0, 'total': 0}
    phase_stats[phase]['total'] += 1
    if r['success']:
        phase_stats[phase]['passed'] += 1

print("\nBy Phase:")
for phase in ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4']:
    if phase in phase_stats:
        p = phase_stats[phase]['passed']
        t = phase_stats[phase]['total']
        pct = p/t*100 if t > 0 else 0
        print(f"  {phase}: {p}/{t} ({pct:.0f}%)")
