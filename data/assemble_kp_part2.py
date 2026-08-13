import json, sys, importlib.util, pathlib
sys.stdout.reconfigure(encoding='utf-8')

all_kps = []

for batch_file in [
    'data/gen_kp_part2_batch1.py',
    'data/gen_kp_part2_batch2.py',
    'data/gen_kp_part2_batch3.py',
    'data/gen_kp_part2_batch4.py',
]:
    spec = importlib.util.spec_from_file_location('batch', batch_file)
    mod = importlib.util.module_from_spec(spec)
    # redirect stdout to suppress print statements
    import io
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    spec.loader.exec_module(mod)
    sys.stdout = old_stdout
    all_kps.extend(mod.kps)

# Check for duplicate ids
ids = [k['id'] for k in all_kps if 'id' in k]
dupes = [x for x in ids if ids.count(x) > 1]
if dupes:
    print(f'DUPLICATE IDs found: {set(dupes)}', file=sys.stderr)

# Count by type
kp_count = sum(1 for k in all_kps if 'id' in k)
script_count = sum(1 for k in all_kps if k.get('_type') == 'illness_script')
pair_count = sum(1 for k in all_kps if k.get('_type') == 'confusable_pair')

print(f'Total items: {len(all_kps)}')
print(f'  KPs: {kp_count}')
print(f'  Scripts: {script_count}')
print(f'  Pairs: {pair_count}')

# Count unique topics
topics = set(k.get('topic','') for k in all_kps)
print(f'  Unique topics: {len(topics)}')

# Validate JSON serializability
json_str = json.dumps(all_kps, ensure_ascii=False, indent=2)
# Verify it parses back
parsed = json.loads(json_str)
print(f'  Round-trip parse: OK ({len(parsed)} items)')

# Write output
out_path = 'data/kp_redeep_part_2.json'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(json_str)
print(f'Written to {out_path}')
