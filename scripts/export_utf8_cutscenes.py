import json

with open("workspace/translation/localdat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
    records = [json.loads(line) for line in f if line.strip()]

movies = [r for r in records if r.get("ko_id") is not None and r["ko_id"] >= 5000]

lines = [f"[{m['ko_id']:4d}] {m['ko_text']}" for m in movies]
with open("workspace/translation/all_ko_cutscenes_utf8.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Wrote {len(lines)} lines to all_ko_cutscenes_utf8.txt")

