#!/usr/bin/env python3
"""
Phase 3 Consolidation: Merge all Phase 3 modules + integrate with Phase 1-2

Reads:
- Phase 1 chunks: data/phase1_chunks.jsonl (80 units)
- Phase 2 chunks: data/phase2_chunks.jsonl (221 units)
- Phase 3 chunks: 10 module JSON files (400+ units)

Outputs:
- data/phase3_chunks.json: All Phase 3 units with unique IDs
- data/phase3_chunks.jsonl: Phase 3 units in JSONL format
- data/cumulative_chunks_all_phases.jsonl: All 701+ units combined
"""

import json
import os
from datetime import datetime

def consolidate_phase3():
    """Consolidate all Phase 3 modules into single file."""

    phase3_files = [
        "data/phase3_sepsis_chunks.json",
        "data/phase3_ards_chunks.json",
        "data/phase3_heart_failure_chunks.json",
        "data/phase3_hypertensive_crisis_chunks.json",
        "data/phase3_dic_chunks.json",
        "data/phase3_liver_failure_chunks.json",
        "data/phase3_acute_pancreatitis_chunks.json",
        "data/phase3_intracranial_hypertension_chunks.json",
        "data/phase3_status_epilepticus_chunks.json",
        "data/phase3_organ_dysfunction_chunks.json"
    ]

    all_phase3_units = []
    module_stats = {}

    # Load all Phase 3 modules
    for phase3_file in phase3_files:
        if not os.path.exists(phase3_file):
            print(f"Warning: {phase3_file} not found, skipping")
            continue

        with open(phase3_file, 'r', encoding='utf-8') as f:
            units = json.load(f)
            module_name = os.path.basename(phase3_file).replace("phase3_", "").replace("_chunks.json", "")
            module_stats[module_name] = len(units)
            all_phase3_units.extend(units)

    # Assign unique IDs
    for i, unit in enumerate(all_phase3_units):
        unit['id'] = f'phase3_unit_{i}'
        if 'created_at' not in unit:
            unit['created_at'] = datetime.now().isoformat()

    # Validate units
    for unit in all_phase3_units:
        required_fields = {'topic', 'subtopic', 'content', 'tags', 'library', 'id'}
        if not required_fields.issubset(set(unit.keys())):
            print(f"Warning: Unit {unit.get('id')} missing fields: {required_fields - set(unit.keys())}")

    # Save Phase 3 consolidated JSON
    with open("data/phase3_chunks.json", 'w', encoding='utf-8') as f:
        json.dump(all_phase3_units, f, indent=2, ensure_ascii=False)

    # Save Phase 3 JSONL
    with open("data/phase3_chunks.jsonl", 'w', encoding='utf-8') as f:
        for unit in all_phase3_units:
            f.write(json.dumps(unit, ensure_ascii=False) + '\n')

    print(f"\nPhase 3 Consolidation Summary:")
    print(f"Total Phase 3 units: {len(all_phase3_units)}")
    print(f"\nModule breakdown:")
    for module, count in sorted(module_stats.items()):
        print(f"  {module}: {count} units")

    return all_phase3_units

def integrate_all_phases():
    """Integrate Phase 1 + Phase 2 + Phase 3 into cumulative file."""

    all_units = []

    # Load Phase 1
    with open("data/phase1_chunks.jsonl", 'r', encoding='utf-8') as f:
        phase1_units = [json.loads(line) for line in f]
    all_units.extend(phase1_units)
    print(f"Phase 1: {len(phase1_units)} units")

    # Load Phase 2
    with open("data/phase2_chunks.jsonl", 'r', encoding='utf-8') as f:
        phase2_units = [json.loads(line) for line in f]
    all_units.extend(phase2_units)
    print(f"Phase 2: {len(phase2_units)} units")

    # Load Phase 3
    with open("data/phase3_chunks.jsonl", 'r', encoding='utf-8') as f:
        phase3_units = [json.loads(line) for line in f]
    all_units.extend(phase3_units)
    print(f"Phase 3: {len(phase3_units)} units")

    total = len(all_units)
    print(f"\nCumulative total: {total} units")
    print(f"Progress toward 1,200 target: {100*total/1200:.1f}%")

    # Save cumulative JSONL
    with open("data/cumulative_chunks_all_phases.jsonl", 'w', encoding='utf-8') as f:
        for unit in all_units:
            f.write(json.dumps(unit, ensure_ascii=False) + '\n')

    # Save cumulative JSON for reference
    with open("data/cumulative_chunks_all_phases.json", 'w', encoding='utf-8') as f:
        json.dump(all_units, f, indent=2, ensure_ascii=False)

    # Validate
    subtopic_counts = {}
    library_counts = {}
    for unit in all_units:
        subtopic = unit.get('subtopic', 'UNKNOWN')
        library = unit.get('library', 'UNKNOWN')
        subtopic_counts[subtopic] = subtopic_counts.get(subtopic, 0) + 1
        library_counts[library] = library_counts.get(library, 0) + 1

    print(f"\nLibrary distribution:")
    for lib, count in sorted(library_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"  {lib}: {count}")

    return all_units

if __name__ == "__main__":
    print("=" * 80)
    print("PHASE 3 CONSOLIDATION & INTEGRATION")
    print("=" * 80)

    print("\n[Step 1] Consolidating Phase 3 modules...")
    phase3_units = consolidate_phase3()

    print("\n[Step 2] Integrating all phases...")
    all_units = integrate_all_phases()

    print("\n" + "=" * 80)
    print("CONSOLIDATION COMPLETE")
    print("=" * 80)
    print(f"\nOutputs generated:")
    print(f"  - data/phase3_chunks.json (Phase 3 only, JSON)")
    print(f"  - data/phase3_chunks.jsonl (Phase 3 only, JSONL)")
    print(f"  - data/cumulative_chunks_all_phases.json (All phases, JSON)")
    print(f"  - data/cumulative_chunks_all_phases.jsonl (All phases, JSONL)")
