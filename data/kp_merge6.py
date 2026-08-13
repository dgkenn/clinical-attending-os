import json

batches = [
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6a_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6b_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6c_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6d_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6e_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6f_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6g_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6h_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6i_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6j_out.json',
    'C:/Users/Dean/anesthesia_attending/data/kp_batch6k_out.json',
]

all_kps = []
for b in batches:
    with open(b, 'r', encoding='utf-8') as f:
        data = json.load(f)
    all_kps.extend(data)

# Count by type
kp_count = sum(1 for x in all_kps if '_type' not in x)
script_count = sum(1 for x in all_kps if x.get('_type') == 'illness_script')
pair_count = sum(1 for x in all_kps if x.get('_type') == 'confusable_pair')

# Check for unique IDs among KPs
ids = [x['id'] for x in all_kps if '_type' not in x]
assert len(ids) == len(set(ids)), f"Duplicate IDs: {[x for x in ids if ids.count(x) > 1]}"

# Count unique topics covered
topics = set()
for x in all_kps:
    if 'topic' in x:
        topics.add(x['topic'])

print(f"Total entries: {len(all_kps)}")
print(f"KPs: {kp_count}, illness_scripts: {script_count}, confusable_pairs: {pair_count}")
print(f"Unique topics covered: {len(topics)}")

# Validate JSON serialization
json_str = json.dumps(all_kps, ensure_ascii=False, indent=2)
parsed = json.loads(json_str)
assert len(parsed) == len(all_kps), "Parse mismatch"
print("JSON parse: OK")

outpath = 'C:/Users/Dean/anesthesia_attending/data/kp_full_part_6.json'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(json_str)
print(f"Written to {outpath}")
print(f"part 6: {len(topics)} topics, {kp_count} KPs, {script_count} scripts, {pair_count} pairs, parses OK")
