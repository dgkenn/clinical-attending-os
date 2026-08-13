#!/usr/bin/env python3
"""Inspect slice 957:990 in detail to author proper KPs."""
import json

with open('data/_kp_retrieval_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slice_data = data[957:990]

# Show first 5 topics with their chunks
for i, item in enumerate(slice_data[:5]):
    print(f"\n{'='*80}")
    print(f"Item {957+i}: {item.get('topic')}")
    print(f"Domain: {item.get('domain')}, Discipline: {item.get('discipline')}")
    print(f"Priority: {item.get('priority_tier')}, Category: {item.get('category')}")
    print(f"Critical Care: {item.get('is_critical_care')}")
    print(f"Number of chunks: {len(item.get('chunks', []))}")

    for j, chunk in enumerate(item.get('chunks', [])[:2]):
        print(f"\n  Chunk {j+1} ({chunk.get('book')} p.{chunk.get('page')}):")
        text = chunk.get('text', '')
        print(f"  {text[:350].replace(chr(10), ' ')[:350]}...")

print(f"\n\nTotal topics in slice: {len(slice_data)}")
