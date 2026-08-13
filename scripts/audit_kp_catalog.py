"""Fidelity audit for data/kp_catalog.json — structural + grounding checks.

Checks:
  A. Schema: required fields present, valid bloom, source format.
  B. Duplicates: duplicate ids; near-duplicate stems within a topic.
  C. Empties: blank answer/stem/rationale.
  D. Telegraphing: disease-topic stems that name the diagnosis.
  E. Source fidelity: cited book must be a real corpus book.
  F. Grounding: for topics we still have a retrieval dump for, the KP's cited
     book must appear among that topic's retrieved chunks.
  G. Coverage: per-topic KP counts; thin topics (<3).
Prints a report and writes flagged items to data/_kp_audit_flags.json.
"""
import json, re, glob, os, sys
from collections import Counter, defaultdict

CAT = "data/kp_catalog.json"
DUMPS = ["data/_kp_retrieval.json", "data/_kp_retrieval_full.json"]

REQ = ["id", "topic", "stem", "answer", "rationale", "bloom", "source", "discipline"]
BLOOM_OK = {"recall", "apply", "analyze", "evaluate", "transfer"}

def norm(s): return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def main():
    cat = json.load(open(CAT, encoding="utf-8"))
    kps = [e for e in cat if not e.get("_type")]
    scripts = [e for e in cat if e.get("_type") == "illness_script"]
    pairs = [e for e in cat if e.get("_type") == "confusable_pair"]

    # Build per-topic chunk-book map + global book set from any dumps present
    topic_books = {}      # topic -> set(books)
    all_books = set()
    for d in DUMPS:
        if os.path.exists(d):
            for t in json.load(open(d, encoding="utf-8")):
                bs = {c.get("book", "") for c in t.get("chunks", [])}
                topic_books.setdefault(t["topic"], set()).update(bs)
                all_books.update(bs)

    flags = defaultdict(list)
    ids = Counter()
    by_topic = defaultdict(list)

    for k in kps:
        ids[k.get("id")] += 1
        by_topic[k.get("topic")].append(k)
        # A. schema
        miss = [f for f in REQ if not k.get(f)]
        if miss: flags["missing_fields"].append({"id": k.get("id"), "missing": miss})
        if k.get("bloom") not in BLOOM_OK: flags["bad_bloom"].append({"id": k.get("id"), "bloom": k.get("bloom")})
        src = k.get("source")
        if not (isinstance(src, list) and src and isinstance(src[0], dict) and src[0].get("book")):
            flags["bad_source_format"].append({"id": k.get("id"), "source": src})
        # C. empties
        for f in ("answer", "stem", "rationale"):
            if not (k.get(f) or "").strip(): flags["empty_"+f].append(k.get("id"))
        # E. source fidelity (cited book exists in corpus book set)
        if all_books and isinstance(src, list) and src and src[0].get("book"):
            b = src[0]["book"]
            if b not in all_books:
                flags["unknown_source_book"].append({"id": k.get("id"), "book": b})
        # F. grounding: cited book among this topic's retrieved chunk books
        tb = topic_books.get(k.get("topic"))
        if tb and isinstance(src, list) and src and src[0].get("book"):
            if src[0]["book"] not in tb:
                flags["source_not_in_topic_chunks"].append({"id": k.get("id"), "topic": k.get("topic"), "book": src[0]["book"]})
        # D. telegraphing — disease topics only (skip 'Approach to' presentations)
        topic = k.get("topic", "")
        if not topic.lower().startswith("approach to"):
            tnorm = norm(topic)
            head = tnorm.split()[0] if tnorm else ""
            # flag if a distinctive topic word (>=5 chars) appears verbatim in the stem
            distinctive = [w for w in tnorm.split() if len(w) >= 6][:2]
            stem = norm(k.get("stem"))
            if distinctive and any(w in stem for w in distinctive):
                flags["possible_telegraph"].append({"id": k.get("id"), "topic": topic})

    # B. duplicate ids
    dup_ids = {i: n for i, n in ids.items() if n > 1}
    # near-duplicate stems within topic
    for t, ks in by_topic.items():
        seen = {}
        for k in ks:
            ns = norm(k.get("stem"))
            if ns in seen: flags["dup_stem_in_topic"].append({"topic": t, "ids": [seen[ns], k.get("id")]})
            else: seen[ns] = k.get("id")

    # G. coverage
    counts = {t: len(ks) for t, ks in by_topic.items()}
    thin = sorted([t for t, n in counts.items() if n < 3])

    print("="*64)
    print(f"KP CATALOG AUDIT — {len(kps)} KPs | {len(scripts)} illness scripts | {len(pairs)} confusable pairs")
    print(f"topics with KPs: {len(by_topic)} | median KPs/topic: {sorted(counts.values())[len(counts)//2] if counts else 0}")
    print("="*64)
    def rate(n): return f"{n} ({100*n/max(1,len(kps)):.1f}%)"
    print(f"  duplicate ids:            {len(dup_ids)}")
    print(f"  missing required fields:  {rate(len(flags['missing_fields']))}")
    print(f"  invalid bloom:            {rate(len(flags['bad_bloom']))}")
    print(f"  bad source format:        {rate(len(flags['bad_source_format']))}")
    print(f"  empty answer/stem/rat:    {len(flags['empty_answer'])}/{len(flags['empty_stem'])}/{len(flags['empty_rationale'])}")
    print(f"  unknown source book:      {rate(len(flags['unknown_source_book']))}")
    print(f"  source not in topic chunks: {rate(len(flags['source_not_in_topic_chunks']))}  (grounding flag)")
    print(f"  possible telegraph:       {rate(len(flags['possible_telegraph']))}")
    print(f"  dup stems within topic:   {len(flags['dup_stem_in_topic'])}")
    print(f"  thin topics (<3 KPs):     {len(thin)}")
    print(f"  known corpus books:       {len(all_books)}")
    if all_books:
        print("  source-book distribution (top):")
        bc = Counter(k['source'][0]['book'] for k in kps if isinstance(k.get('source'), list) and k['source'] and k['source'][0].get('book'))
        for b, n in bc.most_common(8): print(f"    {n:>5}  {b[:48]}")
    print("\n  sample flagged (grounding):", [f['id'] for f in flags['source_not_in_topic_chunks'][:5]])
    print("  sample thin topics:", thin[:8])
    json.dump({k: v for k, v in flags.items()}, open("data/_kp_audit_flags.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n  full flags -> data/_kp_audit_flags.json")

if __name__ == "__main__":
    main()
