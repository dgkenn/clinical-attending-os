#!/usr/bin/env python3
"""
Consolidate all Phase 2 knowledge chunks into single master file.
Verify structure, assign IDs, count by module/subtopic.
"""

import json
from pathlib import Path
from collections import defaultdict

def consolidate_phase2():
    """Read all phase2_*.json files, consolidate, assign unique IDs."""
    data_dir = Path("C:/Users/Dean/anesthesia_attending/data")
    phase2_files = sorted(data_dir.glob("phase2_*_chunks.json"))

    print(f"Found {len(phase2_files)} Phase 2 module files:")
    for f in phase2_files:
        print(f"  - {f.name}")

    all_units = []
    unit_id_counter = 0
    module_counts = defaultdict(int)
    subtopic_counts = defaultdict(int)

    # Read all phase2 module files
    for module_file in phase2_files:
        print(f"\nProcessing {module_file.name}...")
        with open(module_file, 'r') as f:
            for line in f:
                if line.strip():
                    unit = json.loads(line)
                    # Extract module name from filename
                    module_name = module_file.stem.replace("phase2_", "").replace("_chunks", "")
                    module_counts[module_name] += 1
                    subtopic = unit.get("subtopic", "unknown")
                    subtopic_counts[subtopic] += 1

                    # Reassign global ID
                    unit["id"] = f"phase2_unit_{unit_id_counter}"
                    unit_id_counter += 1
                    all_units.append(unit)

    # Write consolidated master file
    output_file = data_dir / "phase2_chunks.json"
    print(f"\nWriting {len(all_units)} consolidated units to {output_file}...")
    with open(output_file, 'w') as f:
        for unit in all_units:
            f.write(json.dumps(unit) + "\n")

    # Print statistics
    print(f"\n=== PHASE 2 CONSOLIDATION COMPLETE ===")
    print(f"Total units: {len(all_units)}")
    print(f"\nBy Module:")
    for module, count in sorted(module_counts.items()):
        print(f"  {module}: {count}")

    print(f"\nBy Subtopic (top 15):")
    for subtopic, count in sorted(subtopic_counts.items(), key=lambda x: -x[1])[:15]:
        print(f"  {subtopic}: {count}")

    print(f"\nVerification checks:")
    # Check all required fields
    missing_fields = defaultdict(int)
    for unit in all_units:
        if "id" not in unit:
            missing_fields["id"] += 1
        if "topic" not in unit:
            missing_fields["topic"] += 1
        if "content" not in unit:
            missing_fields["content"] += 1
        if "subtopic" not in unit:
            missing_fields["subtopic"] += 1
        if "tags" not in unit:
            missing_fields["tags"] += 1
        if "library" not in unit:
            missing_fields["library"] += 1

    if missing_fields:
        print(f"  WARNING: Missing fields detected:")
        for field, count in missing_fields.items():
            print(f"    {field}: {count} units")
    else:
        print(f"  All required fields present in all units")

    # Check for duplicate IDs
    ids = [u["id"] for u in all_units]
    if len(ids) != len(set(ids)):
        print(f"  ERROR: Duplicate IDs detected!")
    else:
        print(f"  No duplicate IDs")

    # Sample a few units
    print(f"\nSample units (first 2, last 2):")
    for unit in all_units[:2] + all_units[-2:]:
        print(f"  ID: {unit['id']}, Topic: {unit['topic']}, Subtopic: {unit['subtopic']}")

    print(f"\nConsolidated Phase 2 file ready: {output_file}")
    return len(all_units)

if __name__ == "__main__":
    count = consolidate_phase2()
    print(f"\nSUCCESS: {count} Phase 2 units consolidated")
