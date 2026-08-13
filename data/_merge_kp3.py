import json, sys
sys.stdout.reconfigure(encoding='utf-8')

parts = [
    'data/_kp_part3_a.json',
    'data/_kp_part3_b.json',
    'data/_kp_part3_c.json',
    'data/_kp_part3_d.json',
    'data/_kp_part3_e.json',
    'data/_kp_part3_f.json',
    'data/_kp_part3_g.json',
    'data/_kp_part3_h.json',
    'data/_kp_part3_i.json',
    'data/_kp_part3_j.json',
    'data/_kp_part3_k.json',
    'data/_kp_part3_l.json',
    'data/_kp_part3_m.json',
    'data/_kp_part3_n.json',
    'data/_kp_part3_o.json',
    'data/_kp_part3_p.json',
    'data/_kp_part3_q.json',
]

all_kps = []
for p in parts:
    with open(p,'r',encoding='utf-8') as f:
        data = json.load(f)
    all_kps.extend(data)

# Count by type
kp_items = [x for x in all_kps if '_type' not in x]
scripts = [x for x in all_kps if x.get('_type') == 'illness_script']
pairs = [x for x in all_kps if x.get('_type') == 'confusable_pair']

# Check unique ids
ids = [x.get('id') for x in kp_items]
dupes = [i for i in ids if ids.count(i) > 1]
if dupes:
    print('DUPLICATE IDs:', set(dupes))

# Count topics
topics = sorted(set(x.get('topic','') for x in kp_items))

print(f'Total items: {len(all_kps)}')
print(f'KPs: {len(kp_items)}')
print(f'illness_scripts: {len(scripts)}')
print(f'confusable_pairs: {len(pairs)}')
print(f'Topics covered: {len(topics)}')
for t in topics:
    count = sum(1 for x in kp_items if x.get('topic') == t)
    print(f'  {t}: {count} KPs')

# Validate JSON serialization
try:
    json_str = json.dumps(all_kps, ensure_ascii=False)
    reparsed = json.loads(json_str)
    assert len(reparsed) == len(all_kps)
    print('JSON validation: OK')
except Exception as e:
    print('JSON validation FAILED:', e)

# Write output
with open('data/kp_full_part_3.json','w',encoding='utf-8') as f:
    json.dump(all_kps, f, ensure_ascii=False, indent=2)

print(f'Written to data/kp_full_part_3.json')
print(f'part 3: {len(topics)} topics, {len(kp_items)} KPs, {len(scripts)} scripts, {len(pairs)} pairs, parses OK')
