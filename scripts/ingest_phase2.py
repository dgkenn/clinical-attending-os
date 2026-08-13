#!/usr/bin/env python3
"""
Ingest Phase 2 knowledge chunks into Chroma vector database.
Convert JSON to JSONL format, merge with Phase 1, test retrieval.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def convert_phase2_to_jsonl():
    """Convert phase2_chunks.json to JSONL format matching Phase 1 structure."""
    data_dir = Path("C:/Users/Dean/anesthesia_attending/data")
    input_file = data_dir / "phase2_chunks.json"
    output_file = data_dir / "phase2_chunks.jsonl"

    print(f"Converting {input_file} to JSONL format...")

    units_processed = 0
    with open(input_file, 'r') as inf, open(output_file, 'w') as outf:
        for line in inf:
            if line.strip():
                unit = json.loads(line)

                # Convert to JSONL format matching Phase 1
                jsonl_entry = {
                    "id": unit["id"],
                    "text": unit["content"],  # Main searchable content
                    "metadata": {
                        "topic": unit["topic"],
                        "topic_tags": unit.get("tags", []),
                        "subtopic": unit.get("subtopic", "unknown"),
                        "library": unit.get("library", "intern_year_medicine"),
                        "source_name": "phase2_knowledge_base",
                        "book": "Phase 2 High-Frequency Diagnoses",
                        "section": unit.get("subtopic", "general"),
                        "created_at": unit.get("created_at", datetime.now().isoformat()),
                        "chunk_type": "fact"
                    }
                }

                outf.write(json.dumps(jsonl_entry) + "\n")
                units_processed += 1

    print(f"Converted {units_processed} units to JSONL format")
    print(f"Output: {output_file}")
    return units_processed

def merge_phases():
    """Merge Phase 1 and Phase 2 JSONL files into cumulative database."""
    data_dir = Path("C:/Users/Dean/anesthesia_attending/data")
    phase1_file = data_dir / "phase1_chunks.jsonl"
    phase2_file = data_dir / "phase2_chunks.jsonl"
    cumulative_file = data_dir / "cumulative_chunks.jsonl"

    print(f"\nMerging Phase 1 and Phase 2...")

    phase1_count = 0
    phase2_count = 0

    # Merge into cumulative file
    with open(cumulative_file, 'w') as outf:
        # Write Phase 1
        with open(phase1_file, 'r') as inf:
            for line in inf:
                if line.strip():
                    outf.write(line)
                    phase1_count += 1

        # Write Phase 2
        with open(phase2_file, 'r') as inf:
            for line in inf:
                if line.strip():
                    outf.write(line)
                    phase2_count += 1

    total = phase1_count + phase2_count
    print(f"Phase 1: {phase1_count} units")
    print(f"Phase 2: {phase2_count} units")
    print(f"Total: {total} units")
    print(f"Output: {cumulative_file}")
    return phase1_count, phase2_count, total

def verify_cumulative():
    """Verify cumulative file structure and sample units."""
    data_dir = Path("C:/Users/Dean/anesthesia_attending/data")
    cumulative_file = data_dir / "cumulative_chunks.jsonl"

    print(f"\nVerifying cumulative database...")

    count = 0
    sample_units = []

    with open(cumulative_file, 'r') as f:
        for line in f:
            if line.strip():
                unit = json.loads(line)
                count += 1
                if count <= 2 or count > count - 2:  # Store first 2 and last 2
                    sample_units.append(unit)

    print(f"Total units verified: {count}")
    print(f"\nSample units (first 2, last 2):")
    for unit in sample_units[:2]:
        print(f"  ID: {unit['id']}, Topic: {unit['metadata']['topic']}")
    for unit in sample_units[-2:]:
        print(f"  ID: {unit['id']}, Topic: {unit['metadata']['topic']}")

    print(f"\nCumulative database ready for Chroma ingestion")
    print(f"  File: {cumulative_file}")
    print(f"  Total units: {count}")
    return count

def main():
    print("=" * 70)
    print("PHASE 2 INGESTION PIPELINE")
    print("=" * 70)

    # Step 1: Convert Phase 2 JSON to JSONL
    phase2_count = convert_phase2_to_jsonl()

    # Step 2: Merge Phase 1 and Phase 2
    phase1_count, phase2_converted, total_count = merge_phases()

    # Step 3: Verify cumulative database
    verified_count = verify_cumulative()

    print("\n" + "=" * 70)
    print(f"PHASE 2 INGESTION COMPLETE")
    print("=" * 70)
    print(f"Phase 1 units: {phase1_count}")
    print(f"Phase 2 units: {phase2_count}")
    print(f"Cumulative total: {verified_count}")
    print(f"Target: 1,000-1,200 units (currently {verified_count}, need {max(0, 1000-verified_count)}-{max(0, 1200-verified_count)} more)")
    print("\nNext steps:")
    print("  1. Verify Chroma vector database connectivity")
    print("  2. Ingest cumulative_chunks.jsonl into Chroma")
    print("  3. Run spot-check retrieval tests")
    print("  4. Commit to git")

    return verified_count

if __name__ == "__main__":
    count = main()
    sys.exit(0 if count > 0 else 1)
