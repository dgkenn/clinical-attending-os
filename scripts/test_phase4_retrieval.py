#!/usr/bin/env python3
"""
Test Phase 4 Retrieval - Verify consolidated knowledge base

Loads cumulative_all_phases.json and tests:
1. Total unit count (597 expected)
2. Sample retrievals by topic
3. Tagging structure integrity
4. Phase 4 module distribution
"""

import json
from pathlib import Path
from collections import Counter

def test_phase4_retrieval():
    """Test Phase 4 consolidated knowledge base."""

    data_dir = Path("C:\\Users\\Dean\\anesthesia_attending\\data")
    cumulative_file = data_dir / "cumulative_all_phases.json"

    if not cumulative_file.exists():
        print("[FAIL] cumulative_all_phases.json not found")
        return False

    # Load all units
    with open(cumulative_file, 'r') as f:
        all_units = json.load(f)

    print("=" * 70)
    print("PHASE 4 RETRIEVAL TEST")
    print("=" * 70)

    # Verify count
    total = len(all_units)
    print(f"\n[STAT] Total units loaded: {total}")
    if total < 590:
        print(f"[WARN] Below expected 597 units")
    elif total >= 597:
        print(f"[OK] Target threshold met")

    # Extract phase 4 units (ID pattern phase4_*)
    phase4_units = [u for u in all_units if "id" in u and u["id"].startswith("phase4_")]
    print(f"[STAT] Phase 4 units identified: {len(phase4_units)}")

    # Phase 4 module distribution
    phase4_modules = {}
    for unit in phase4_units:
        unit_id = unit["id"]
        # Extract module name (phase4_<module>_unit_*)
        parts = unit_id.split("_")
        if len(parts) >= 3:
            module = "_".join(parts[1:-2])  # Everything between "phase4" and "unit"
            phase4_modules[module] = phase4_modules.get(module, 0) + 1

    print(f"\n[STAT] Phase 4 Module Distribution:")
    for module, count in sorted(phase4_modules.items(), key=lambda x: -x[1]):
        print(f"  {module:20s}: {count:3d} units")

    # Sample retrieval tests
    print(f"\n[TEST] Sample Retrieval Tests:")

    # Test 1: Toxicology retrieval
    tox_units = [u for u in all_units if "acetaminophen" in u.get("topic", "").lower()]
    print(f"  Toxicology (acetaminophen): {len(tox_units)} units retrieved")

    # Test 2: Trauma retrieval
    trauma_units = [u for u in all_units if "trauma" in u.get("subtopic", "").lower() or "trauma" in ",".join(u.get("tags", [])).lower()]
    print(f"  Trauma: {len(trauma_units)} units retrieved")

    # Test 3: Procedures retrieval
    proc_units = [u for u in all_units if "procedure" in u.get("subtopic", "").lower() or "procedure" in ",".join(u.get("tags", [])).lower()]
    print(f"  Procedures: {len(proc_units)} units retrieved")

    # Test 4: Sepsis retrieval (across phases)
    sepsis_units = [u for u in all_units if "sepsis" in ",".join(u.get("tags", [])).lower()]
    print(f"  Sepsis (all phases): {len(sepsis_units)} units retrieved")

    # Tagging structure integrity
    print(f"\n[TEST] Tagging Structure:")
    units_with_topics = sum(1 for u in all_units if "topic" in u)
    units_with_subtopics = sum(1 for u in all_units if "subtopic" in u)
    units_with_tags = sum(1 for u in all_units if "tags" in u)
    units_with_ids = sum(1 for u in all_units if "id" in u)

    print(f"  Units with topics:    {units_with_topics}/{total} ({100*units_with_topics/total:.1f}%)")
    print(f"  Units with subtopics: {units_with_subtopics}/{total} ({100*units_with_subtopics/total:.1f}%)")
    print(f"  Units with tags:      {units_with_tags}/{total} ({100*units_with_tags/total:.1f}%)")
    print(f"  Units with IDs:       {units_with_ids}/{total} ({100*units_with_ids/total:.1f}%)")

    # Sample Phase 4 units
    print(f"\n[SAMPLE] Phase 4 Units (first 10 topics):")
    for i, unit in enumerate(phase4_units[:10], 1):
        print(f"  {i:2d}. {unit.get('topic', 'N/A')}")

    # Tag frequency analysis (top 20)
    all_tags = []
    for unit in all_units:
        all_tags.extend(unit.get("tags", []))
    tag_freq = Counter(all_tags)

    print(f"\n[STAT] Top 20 Tags (all phases):")
    for i, (tag, count) in enumerate(tag_freq.most_common(20), 1):
        print(f"  {i:2d}. {tag:30s}: {count:3d}")

    print(f"\n[STAT] High-yield units (high_yield tag):")
    high_yield = [u for u in all_units if "high_yield" in u.get("tags", [])]
    print(f"  Count: {len(high_yield)}/{total} ({100*len(high_yield)/total:.1f}%)")

    # Verify cumulative consistency
    print(f"\n[TEST] Cumulative Consistency:")
    library_check = all(u.get("library") == "intern_year_medicine" for u in all_units if "library" in u)
    if library_check:
        print(f"  [OK] All units tagged with 'intern_year_medicine' library")
    else:
        print(f"  [WARN] Some units missing or inconsistent library tag")

    # Check for duplicates
    ids = [u.get("id") for u in all_units]
    duplicates = [id for id in ids if ids.count(id) > 1]
    if not duplicates:
        print(f"  [OK] No duplicate unit IDs")
    else:
        print(f"  [WARN] Found {len(set(duplicates))} duplicate IDs")

    print(f"\n" + "=" * 70)
    print("PHASE 4 RETRIEVAL TEST COMPLETE")
    print("=" * 70)

    return True

if __name__ == "__main__":
    success = test_phase4_retrieval()
    exit(0 if success else 1)
