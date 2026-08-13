import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/Dean/anesthesia_attending/scripts/kp_batch7.json", "r", encoding="utf-8") as f:
    kps = json.load(f)

print("Loaded", len(kps), "from batch7")

# ============================================================
# Validate: check for duplicate ids, required fields
# ============================================================
all_ids = set()
duplicate_ids = []
missing_fields = []
kp_count = 0
script_count = 0
pair_count = 0

required_kp_fields = {"id","topic","domain","discipline","stem","answer","rationale","bloom","source","confusable_with"}

for i, item in enumerate(kps):
    if "_type" in item:
        if item["_type"] == "illness_script":
            script_count += 1
        elif item["_type"] == "confusable_pair":
            pair_count += 1
        continue

    kp_count += 1
    # Check required fields
    missing = required_kp_fields - set(item.keys())
    if missing:
        missing_fields.append((item.get("id","?"), missing))

    # Check duplicate id
    item_id = item.get("id","")
    if item_id in all_ids:
        duplicate_ids.append(item_id)
    else:
        all_ids.add(item_id)

print(f"KPs: {kp_count}, illness_scripts: {script_count}, confusable_pairs: {pair_count}")
print(f"Duplicate ids: {duplicate_ids}")
print(f"Missing fields: {missing_fields[:5]}")

# Count topics covered
topics_covered = set()
for item in kps:
    if "_type" not in item:
        topics_covered.add(item.get("topic",""))
    elif item.get("_type") == "illness_script":
        topics_covered.add(item.get("topic",""))
print(f"Topics covered: {len(topics_covered)}")

# Write final output
output_path = "C:/Users/Dean/anesthesia_attending/data/kp_redeep_part_1.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(kps, f, ensure_ascii=False, indent=2)

# Verify it parses back correctly
with open(output_path, "r", encoding="utf-8") as f:
    verify = json.load(f)

print(f"Output written: {len(verify)} items total")
print(f"Parse OK: True")
print(f"\nFINAL SUMMARY:")
print(f"  Topics: {len(topics_covered)}")
print(f"  KPs: {kp_count}")
print(f"  Scripts: {script_count}")
print(f"  Pairs: {pair_count}")
print(f"  Total items: {len(verify)}")
