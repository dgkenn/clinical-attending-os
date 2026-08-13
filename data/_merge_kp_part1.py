import json

all_kps = []
for i in range(1, 8):
    fname = f'data/_kp_batch{i}.json'
    with open(fname, 'r', encoding='utf-8') as f:
        batch = json.load(f)
    all_kps.extend(batch)
    print(f'Batch {i}: {len(batch)} items')

print(f'Total before dedup: {len(all_kps)}')

# Validate: check for duplicate ids among KP items
ids = [x['id'] for x in all_kps if 'id' in x]
dupes = [x for x in ids if ids.count(x) > 1]
if dupes:
    print(f'DUPLICATE IDs: {set(dupes)}')
else:
    print('No duplicate IDs')

# Count by type
scripts = [x for x in all_kps if x.get('_type') == 'illness_script']
pairs = [x for x in all_kps if x.get('_type') == 'confusable_pair']
kps = [x for x in all_kps if 'id' in x]

print(f'KPs: {len(kps)}, scripts: {len(scripts)}, pairs: {len(pairs)}')

# Count unique topics
topics = set(x.get('topic', '') for x in kps)
print(f'Topics covered: {len(topics)}')
for t in sorted(topics):
    print(f'  {t[:70]}')

# Write final output
out_path = 'data/kp_full_part_1.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

# Verify parses
with open(out_path, 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f'Parses OK: {len(verify)} items written')
print(f'FINAL: {len(topics)} topics, {len(kps)} KPs, {len(scripts)} scripts, {len(pairs)} pairs')
