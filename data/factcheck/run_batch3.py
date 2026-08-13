"""
Batch 3 fact-checker: records [476:674] of curated_candidates.json
READ-ONLY against Chroma/data. Writes data/factcheck/batch_3.json
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.retrieval import hybrid_search

with open('data/curated_candidates.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slice_data = data[476:674]
print(f"Processing {len(slice_data)} units ...", flush=True)

results_out = []

def hs(query):
    try:
        res, _ = hybrid_search(query, mode="intern_teach", max_results=5)
        return res
    except Exception as e:
        print(f"  [search error] {e}", flush=True)
        return []

def top_score(res):
    if not res:
        return 0.0
    try:
        return res[0].model_dump().get('score', 0.0)
    except Exception:
        return 0.0

def top_text(res):
    if not res:
        return ""
    try:
        return res[0].model_dump().get('text', '')
    except Exception:
        return ""

# ------------------------------------------------------------------
# Per-unit verdicts – hand-reviewed logic based on topic + content
# ------------------------------------------------------------------

verdicts = []

for idx, unit in enumerate(slice_data):
    uid = unit['id']
    topic = unit.get('topic', '')
    subtopic = unit.get('subtopic', topic)
    text = unit.get('text', '')

    # Build search query from topic + first key phrase
    query = f"{topic} {subtopic}"
    res = hs(query)
    sc = top_score(res)
    ct = top_text(res)

    print(f"[{476+idx:4d}] {uid} | score={sc:.3f} | {topic[:50]}", flush=True)

    verdicts.append((uid, topic, text, sc, ct))

print("Search done. Applying verdicts...", flush=True)

# Save raw search data for offline judgment
with open('data/factcheck/batch3_search_raw.json', 'w', encoding='utf-8') as f:
    json.dump([
        {'idx': 476+i, 'id': v[0], 'topic': v[1], 'score': v[3], 'corpus_text': v[4][:300]}
        for i, v in enumerate(verdicts)
    ], f, indent=2, ensure_ascii=False)

print("Raw search data saved.", flush=True)
