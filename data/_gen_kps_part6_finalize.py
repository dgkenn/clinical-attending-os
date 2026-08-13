import json

# Load final batch
with open('C:/Users/Dean/anesthesia_attending/data/_kps_batch8.json', 'r', encoding='utf-8') as f:
    kps = json.load(f)

# Count by type
kp_items = [k for k in kps if '_type' not in k]
script_items = [k for k in kps if k.get('_type') == 'illness_script']
pair_items = [k for k in kps if k.get('_type') == 'confusable_pair']

print(f"Total items: {len(kps)}")
print(f"KPs: {len(kp_items)}")
print(f"Illness scripts: {len(script_items)}")
print(f"Confusable pairs: {len(pair_items)}")

# Check ID uniqueness
ids = [k['id'] for k in kp_items]
dupes = [i for i in ids if ids.count(i) > 1]
print(f"Duplicate IDs: {dupes if dupes else 'None'}")

# Check all required fields
required_kp_fields = ['id','topic','domain','discipline','stem','answer','rationale','bloom','source','confusable_with']
missing = []
for k in kp_items:
    for f in required_kp_fields:
        if f not in k:
            missing.append((k.get('id'), f))
print(f"Missing fields: {missing if missing else 'None'}")

# Count topics covered
topics = list(set(k['topic'] for k in kp_items))
print(f"Unique topics covered: {len(topics)}")

# Verify bloom values
bloom_vals = set(k['bloom'] for k in kp_items)
print(f"Bloom values: {bloom_vals}")

# Write final output
output_path = 'C:/Users/Dean/anesthesia_attending/data/kp_redeep_part_6.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Verify it parses back correctly
with open(output_path, 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f"Output file verification: {len(verify)} items, parses OK")
print(f"Output path: {output_path}")

# Final summary line
n_topics = len(topics)
n_kps = len(kp_items)
n_scripts = len(script_items)
n_pairs = len(pair_items)
print(f"\nSUMMARY: part 6: {n_topics} topics, {n_kps} KPs, {n_scripts} scripts, {n_pairs} pairs, parses OK")
