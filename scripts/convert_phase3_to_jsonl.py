#!/usr/bin/env python3
"""
Convert Phase 3 chunks from simple JSON format to Chroma-compatible JSONL format.

Converts Phase 3 units to match the format expected by the ingest pipeline:
- "text" field (content)
- "metadata" dict with topic, tags, library, etc.
"""

import json
from datetime import datetime

def convert_phase3_to_chroma_format():
    """Convert Phase 3 chunks to Chroma JSONL format."""

    # Read Phase 3 consolidated JSON
    with open("data/phase3_chunks.json", 'r', encoding='utf-8') as f:
        units = json.load(f)

    converted_units = []

    for unit in units:
        # Convert to Chroma format
        chroma_unit = {
            "id": unit.get('id', ''),
            "text": unit.get('content', ''),
            "metadata": {
                "topic": unit.get('topic', ''),
                "subtopic": unit.get('subtopic', ''),
                "topic_tags": unit.get('tags', []),
                "library": unit.get('library', 'intern_year_medicine'),
                "source_name": "phase3_knowledge_base",
                "book": "Phase 3 High-Acuity ICU Diagnoses",
                "section": unit.get('subtopic', ''),
                "created_at": unit.get('created_at', datetime.now().isoformat()),
                "chunk_type": "fact",
                "training_phase": "phase3"
            }
        }
        converted_units.append(chroma_unit)

    # Write to JSONL
    with open("data/phase3_chunks_chroma.jsonl", 'w', encoding='utf-8') as f:
        for unit in converted_units:
            f.write(json.dumps(unit, ensure_ascii=False) + '\n')

    print(f"Converted {len(converted_units)} Phase 3 units to Chroma format")
    print(f"Output: data/phase3_chunks_chroma.jsonl")

    # Sample output
    if converted_units:
        print(f"\nSample unit:")
        print(json.dumps(converted_units[0], indent=2, ensure_ascii=False))

if __name__ == "__main__":
    convert_phase3_to_chroma_format()
