"""Weekly study digest for the Clinical Attending tutor.

Pulls the latest progress DB from the private HF state dataset and prints a short
metacognition report: what you did this week, your accuracy, weakest topics, and
what's due. Run:  python deploy/hf/digest.py
Reads the HF token from deploy/hf/.hf_token (or $HF_TOKEN).
"""
import os
import sys
import sqlite3
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN_FILE = ROOT / "deploy" / "hf" / ".hf_token"


def _token() -> str:
    t = os.environ.get("HF_TOKEN", "")
    if not t and TOKEN_FILE.exists():
        t = TOKEN_FILE.read_text(encoding="utf-8").strip()
    if not t:
        sys.exit("No HF token (deploy/hf/.hf_token or $HF_TOKEN).")
    return t


def _q(con, sql, default=None):
    try:
        return con.execute(sql).fetchall()
    except Exception:
        return default if default is not None else []


def main() -> None:
    from huggingface_hub import HfApi, hf_hub_download
    tok = _token()
    api = HfApi(token=tok)
    user = api.whoami()["name"]
    db = hf_hub_download(repo_id=f"{user}/clinical-attending-state",
                         repo_type="dataset", filename="student_model.db", token=tok)
    con = sqlite3.connect(db)

    week = _q(con, "SELECT COUNT(*), COALESCE(SUM(result='correct'),0) "
                   "FROM question_attempts WHERE date >= date('now','-7 days')")
    n, correct = (week[0] if week else (0, 0))
    acc = f"{(correct / n * 100):.0f}%" if n else "n/a"
    due = _q(con, "SELECT COUNT(*) FROM topics WHERE next_review_date <= date('now')")
    due_n = due[0][0] if due else 0
    weak = _q(con, "SELECT topic, COUNT(*) t, SUM(result!='correct') e FROM question_attempts "
                   "WHERE date >= date('now','-14 days') GROUP BY topic HAVING t >= 2 "
                   "ORDER BY (e*1.0/t) DESC LIMIT 5")
    studied = _q(con, "SELECT COUNT(DISTINCT topic) FROM question_attempts")
    studied_n = studied[0][0] if studied else 0
    con.close()

    print("=== Weekly Study Digest — Clinical Attending OS ===")
    print(f"This week: {n} questions answered, {acc} correct")
    print(f"Topics due for review today: {due_n}")
    print(f"Distinct topics studied (all time): {studied_n}")
    if weak:
        print("Weakest topics (last 14 days, fix these first):")
        for topic, total, errors in weak:
            print(f"  - {topic}: {errors}/{total} missed ({(errors/total*100):.0f}% error)")
    else:
        print("No topics with enough recent attempts to flag as weak yet.")
    print("Tip: clear the due reviews first — that's where spaced repetition pays off.")


if __name__ == "__main__":
    main()
