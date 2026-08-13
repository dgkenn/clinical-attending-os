import json

b1 = json.load(open("data/kp_batch1_out.json", encoding="utf-8"))
b2 = json.load(open("data/kp_batch2_out.json", encoding="utf-8"))
b3 = json.load(open("data/kp_batch3_out.json", encoding="utf-8"))

combined = b1 + b2 + b3
print(f"Total items: {len(combined)}")

# sanity check: count typed items
illness_scripts = [x for x in combined if x.get("_type") == "illness_script"]
confusable_pairs = [x for x in combined if x.get("_type") == "confusable_pair"]
kps_only = [x for x in combined if "_type" not in x]
print(f"  KPs: {len(kps_only)}")
print(f"  illness_scripts: {len(illness_scripts)}")
print(f"  confusable_pairs: {len(confusable_pairs)}")

# Check for duplicate IDs among KPs
ids = [x["id"] for x in kps_only]
dupes = [i for i in ids if ids.count(i) > 1]
if dupes:
    print(f"  DUPLICATE IDs: {set(dupes)}")
else:
    print("  No duplicate IDs")

with open("data/kp_catalog_part_5.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)
print("Written: data/kp_catalog_part_5.json")
