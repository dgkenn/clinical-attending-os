import sys, json
sys.path.insert(0, '.')
from src.student_model import conn, initialize_database
from src.retrieval import hybrid_search
initialize_database()
with conn() as db:
    rows = db.execute('''
        SELECT topic, domain, discipline, priority_tier, category, is_critical_care
        FROM curriculum
        WHERE topic NOT IN (SELECT DISTINCT topic FROM kp_catalog)
        ORDER BY (CASE WHEN category='presentation' THEN 0 ELSE 1 END),
                 is_critical_care DESC, priority_tier ASC,
                 (CASE WHEN discipline='medicine' THEN 0 ELSE 1 END), topic
    ''').fetchall()
topics = [dict(r) for r in rows]
print(f'[dump-full] {len(topics)} remaining topics', flush=True)
out = []
for i, r in enumerate(topics):
    try:
        s, _ = hybrid_search(r['topic'], max_results=8)
        chunks = [{'book': x.book or x.filename or '?', 'page': x.page or 0, 'text': (x.text or '')[:900]} for x in s]
    except Exception as e:
        chunks = []
        print(f'[dump-full] err {r["topic"]}: {e}', flush=True)
    out.append({'topic': r['topic'], 'domain': r['domain'], 'discipline': r['discipline'],
                'priority_tier': r['priority_tier'], 'category': r['category'],
                'is_critical_care': r['is_critical_care'], 'chunks': chunks})
    if (i + 1) % 50 == 0:
        print(f'[dump-full] {i+1}/{len(topics)}', flush=True)
json.dump(out, open('data/_kp_retrieval_full.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(f'[dump-full] DONE -> data/_kp_retrieval_full.json ({len(out)} topics)', flush=True)
