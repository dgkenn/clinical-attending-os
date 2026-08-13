#!/usr/bin/env python3
"""
Consolidate ALL phases (1-4) into unified knowledge base
"""

import json
from pathlib import Path
import sys
import io

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def consolidate():
    """Load all phase data and merge."""

    units = []

    # Load cumulative (Phase 1-3)
    cumulative_path = Path("data") / "cumulative_chunks_all_phases.json"
    if cumulative_path.exists():
        with cumulative_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            units.extend(data)
            print(f"[+] Loaded Phase 1-3: {len(data)} units")

    # Load Phase 4 comprehensive
    phase4_comp = Path("data") / "phase4_comprehensive.json"
    if phase4_comp.exists():
        with phase4_comp.open("r", encoding="utf-8") as f:
            data = json.load(f)
            units.extend(data)
            print(f"[+] Loaded Phase 4 comprehensive: {len(data)} units")

    # Load Phase 4 final
    phase4_final = Path("data") / "phase4_final.json"
    if phase4_final.exists():
        with phase4_final.open("r", encoding="utf-8") as f:
            data = json.load(f)
            units.extend(data)
            print(f"[+] Loaded Phase 4 final: {len(data)} units")

    # Dedup by ID
    seen = set()
    deduped = []
    for unit in units:
        uid = unit.get("id")
        if uid not in seen:
            seen.add(uid)
            deduped.append(unit)

    print(f"\n[OK] Consolidated {len(deduped)} unique units (after dedup)")

    # Save consolidated
    output = Path("data") / "all_phases_consolidated.json"
    with output.open("w", encoding="utf-8") as f:
        json.dump(deduped, f, indent=2, ensure_ascii=False)

    # Statistics
    by_library = {}
    by_section = {}
    for unit in deduped:
        meta = unit.get("metadata", {})
        lib = meta.get("library", "unknown")
        section = meta.get("section", "unknown")
        by_library[lib] = by_library.get(lib, 0) + 1
        by_section[section] = by_section.get(section, 0) + 1

    print("\nBy Library:")
    for lib, count in sorted(by_library.items()):
        print(f"  {lib}: {count}")

    print(f"\nBy Section (top 15):")
    for section, count in sorted(by_section.items(), key=lambda x: -x[1])[:15]:
        print(f"  {section}: {count}")

    print(f"\nTotal Units: {len(deduped)}")
    print(f"Output: {output}")

    return deduped


if __name__ == "__main__":
    consolidate()
