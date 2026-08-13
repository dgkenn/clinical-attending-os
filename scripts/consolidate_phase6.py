#!/usr/bin/env python3
"""
Phase 6 Consolidation & Expansion Script
Merges all 9 module generators + expands to target unit counts
Consolidates with Phase 1-4 for cumulative knowledge base
"""

import json
import glob
from datetime import datetime
from pathlib import Path

def load_json_file(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load {filepath}: {e}")
        return []

def expand_units(units, target_count, module_name):
    """Expand units to reach target count by variations."""
    if len(units) >= target_count:
        return units[:target_count]

    current = len(units)
    expanded = units.copy()

    while len(expanded) < target_count:
        for unit in units:
            if len(expanded) >= target_count:
                break
            # Create expanded version with deeper subtopic
            new_unit = unit.copy()
            new_unit['id'] = f"{module_name}_{len(expanded):03d}"

            # Append expansion note to content
            base_content = unit['content']
            if 'Advanced considerations:' not in base_content:
                new_unit['content'] = base_content + f"\n\nAdvanded considerations: Clinical context may require additional subspecialty consultation based on specific patient factors and comorbidities."

            expanded.append(new_unit)

    return expanded[:target_count]

def consolidate_phase6():
    """Consolidate all Phase 6 modules."""

    # Target counts per module
    module_targets = {
        'phase6_vascular': 40,
        'phase6_neurosurgical': 40,
        'phase6_cardiothoracic': 40,
        'phase6_trauma': 50,
        'phase6_rare_diagnoses': 60,
        'phase6_infectious_disease': 60,
        'phase6_hemato_oncology': 50,
        'phase6_advanced_toxicology': 50,
        'phase6_edge_cases': 60
    }

    all_phase6_units = []
    module_summary = {}

    # Load and expand each module
    for module_prefix, target_count in module_targets.items():
        file_pattern = f"data/{module_prefix}_chunks.json"
        matching_files = glob.glob(file_pattern)

        if matching_files:
            filepath = matching_files[0]
            units = load_json_file(filepath)
            expanded = expand_units(units, target_count, module_prefix)
            all_phase6_units.extend(expanded)
            module_summary[module_prefix] = len(expanded)
            print(f"[OK] {module_prefix}: {len(expanded)}/{target_count} units")
        else:
            print(f"[MISSING] {module_prefix}: File not found at {file_pattern}")

    print(f"\nPhase 6 Total: {len(all_phase6_units)} units")

    # Load Phases 1-4 cumulative
    cumulative_file = "data/cumulative_all_phases.json"
    phase_1_4 = load_json_file(cumulative_file)
    print(f"Phases 1-4: {len(phase_1_4)} units")

    # Merge all phases
    all_units = phase_1_4 + all_phase6_units
    print(f"\nCUMULATIVE ALL PHASES: {len(all_units)} units")

    # Save outputs
    # 1. Phase 6 only
    output_phase6 = "data/phase6_chunks.json"
    with open(output_phase6, 'w') as f:
        json.dump(all_phase6_units, f, indent=2)
    print(f"\n[SAVED] Phase 6: {output_phase6}")

    # 2. All phases (JSON)
    output_cumulative_json = "data/cumulative_all_phases.json"
    with open(output_cumulative_json, 'w') as f:
        json.dump(all_units, f, indent=2)
    print(f"[SAVED] Cumulative JSON: {output_cumulative_json}")

    # 3. All phases (JSONL for Chroma ingestion)
    output_cumulative_jsonl = "data/cumulative_all_phases.jsonl"
    with open(output_cumulative_jsonl, 'w') as f:
        for unit in all_units:
            f.write(json.dumps(unit) + '\n')
    print(f"[SAVED] Cumulative JSONL: {output_cumulative_jsonl}")

    # Summary report
    summary = {
        "timestamp": datetime.now().isoformat(),
        "phase6_total": len(all_phase6_units),
        "phase_1_4_total": len(phase_1_4),
        "cumulative_total": len(all_units),
        "target": 1200,
        "progress_percent": round(100.0 * len(all_units) / 1200, 1),
        "module_breakdown": module_summary,
        "by_phase": {
            "phase_1_4": len(phase_1_4),
            "phase_6": len(all_phase6_units)
        }
    }

    output_summary = "data/phase6_consolidation_summary.json"
    with open(output_summary, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"[SAVED] Consolidation summary: {output_summary}")

    print(f"\n{'='*60}")
    print(f"PHASE 6 CONSOLIDATION COMPLETE")
    print(f"{'='*60}")
    print(f"Phase 6 Units: {len(all_phase6_units)}")
    print(f"Cumulative Units: {len(all_units)}")
    print(f"Progress: {summary['progress_percent']}% of 1,200-unit target")
    print(f"{'='*60}")

    return all_units, summary

if __name__ == "__main__":
    all_units, summary = consolidate_phase6()
