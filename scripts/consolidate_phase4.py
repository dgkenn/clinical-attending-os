#!/usr/bin/env python3
"""
Consolidate Phase 4 Modules - Merge All 8 Modules + Phase 1-3

Reads individual Phase 4 module JSON files, combines them,
merges with existing Phase 1-3 cumulative data, and generates:
1. phase4_chunks.json (all Phase 4 units)
2. cumulative_all_phases.json (all Phases 1-4)
3. Logging/summary statistics
"""

import json
import os
from datetime import datetime
from pathlib import Path

def load_json_file(filepath):
    """Load JSON file safely."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []

def consolidate_phase4():
    """Merge all Phase 4 modules into single consolidated file."""

    data_dir = Path("C:\\Users\\Dean\\anesthesia_attending\\data")

    # Phase 4 modules (in order)
    phase4_modules = [
        "phase4_toxicology_chunks.json",
        "phase4_trauma_chunks.json",
        "phase4_procedures_chunks.json",
        "phase4_obstetric_chunks.json",
        "phase4_pediatric_chunks.json",
        "phase4_geriatric_chunks.json",
        "phase4_communication_chunks.json",
        "phase4_quality_chunks.json",
    ]

    all_phase4_units = []
    module_stats = {}

    print("=" * 60)
    print("PHASE 4 CONSOLIDATION")
    print("=" * 60)

    for module_file in phase4_modules:
        filepath = data_dir / module_file
        if filepath.exists():
            units = load_json_file(filepath)
            count = len(units) if isinstance(units, list) else (1 if units else 0)
            module_stats[module_file] = count
            all_phase4_units.extend(units if isinstance(units, list) else [units])
            print(f"[OK] {module_file}: {count} units")
        else:
            print(f"[MISS] {module_file}: NOT FOUND")

    print("\n" + "=" * 60)
    print(f"PHASE 4 TOTAL: {len(all_phase4_units)} units")
    print("=" * 60)

    # Write Phase 4 consolidated file
    phase4_output = data_dir / "phase4_chunks.json"
    with open(phase4_output, 'w') as f:
        json.dump(all_phase4_units, f, indent=2)
    print(f"\n[OK] Phase 4 consolidated: {phase4_output}")

    # Load Phase 1-3 cumulative
    cumulative_p123 = load_json_file(data_dir / "cumulative_chunks_all_phases.json")
    if not cumulative_p123:
        cumulative_p123 = load_json_file(data_dir / "cumulative_chunks.jsonl")
        if isinstance(cumulative_p123, str):
            # JSONL format
            cumulative_p123 = []
            with open(data_dir / "cumulative_chunks.jsonl", 'r') as f:
                for line in f:
                    if line.strip():
                        cumulative_p123.append(json.loads(line))

    if not cumulative_p123:
        cumulative_p123 = []

    print(f"[OK] Phase 1-3 cumulative: {len(cumulative_p123)} units")

    # Combine all phases
    all_cumulative = cumulative_p123 + all_phase4_units

    # Ensure all units have IDs
    for i, unit in enumerate(all_cumulative):
        if "id" not in unit:
            unit["id"] = f"cumulative_unit_{i}"
        if "created_at" not in unit:
            unit["created_at"] = datetime.utcnow().isoformat()

    # Write cumulative all phases
    cumulative_output = data_dir / "cumulative_all_phases.json"
    with open(cumulative_output, 'w') as f:
        json.dump(all_cumulative, f, indent=2)
    print(f"[OK] Cumulative all phases: {cumulative_output}")

    # Also write JSONL version for Chroma ingestion
    cumulative_jsonl = data_dir / "cumulative_all_phases.jsonl"
    with open(cumulative_jsonl, 'w') as f:
        for unit in all_cumulative:
            f.write(json.dumps(unit) + '\n')
    print(f"[OK] Cumulative JSONL: {cumulative_jsonl}")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(f"Phase 1-3 Total: {len(cumulative_p123)} units")
    print(f"Phase 4 Total:   {len(all_phase4_units)} units")
    print(f"CUMULATIVE:      {len(all_cumulative)} units")
    print(f"TARGET:          1,200 units")
    print(f"Progress:        {len(all_cumulative)}/1200 ({100*len(all_cumulative)/1200:.1f}%)")

    # Breakdown by phase
    print("\nPhase 4 Module Breakdown:")
    for module, count in sorted(module_stats.items()):
        print(f"  {module:40s}: {count:3d} units")

    # Breakdown by topic (sample from phase 4)
    print("\nPhase 4 Topics Covered:")
    topics = set()
    for unit in all_phase4_units:
        if "topic" in unit:
            topics.add(unit["topic"])
    for i, topic in enumerate(sorted(topics)[:20], 1):
        print(f"  {i:2d}. {topic}")
    if len(topics) > 20:
        print(f"  ... and {len(topics)-20} more topics")

    return all_cumulative

def ingest_to_chroma():
    """Optional: ingest cumulative chunks to Chroma vector DB."""
    try:
        import chromadb
        from pathlib import Path

        data_dir = Path("C:\\Users\\Dean\\anesthesia_attending\\data")

        # Load chunks
        with open(data_dir / "cumulative_all_phases.jsonl", 'r') as f:
            chunks = [json.loads(line) for line in f if line.strip()]

        # Initialize Chroma
        client = chromadb.Client()
        collection = client.get_or_create_collection(
            name="clinical_attending_os",
            metadata={"hnsw:space": "cosine"}
        )

        # Prepare documents
        documents = []
        metadatas = []
        ids = []

        for chunk in chunks:
            doc = f"{chunk.get('topic', '')} - {chunk.get('content', '')}"
            documents.append(doc)
            metadatas.append({
                "topic": chunk.get("topic", ""),
                "subtopic": chunk.get("subtopic", ""),
                "library": chunk.get("library", ""),
                "tags": ",".join(chunk.get("tags", []))
            })
            ids.append(chunk.get("id", ""))

        # Add to collection
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        print(f"\n[OK] Ingested {len(chunks)} units to Chroma")
        return True

    except Exception as e:
        print(f"\n[FAIL] Chroma ingestion failed: {e}")
        return False

if __name__ == "__main__":
    cumulative = consolidate_phase4()

    # Optional: ingest to Chroma
    # ingest_to_chroma()

    print("\n" + "=" * 60)
    print("CONSOLIDATION COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review cumulative_all_phases.json for completeness")
    print("2. Run test queries to verify retrieval")
    print("3. Ingest to production Chroma if verified")
    print("4. Commit changes to git")
