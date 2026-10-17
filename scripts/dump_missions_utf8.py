import json

with open("workspace/translation/localdat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
    records = [json.loads(line) for line in f if line.strip()]

missions = [r for r in records if r.get("ko_id") is not None and 640 <= r["ko_id"] <= 726]

lines = []
for m in missions:
    lines.append(f"[{m['ko_id']:4d}]")
    lines.append(f"  JA: {m['ja_text']}")
    lines.append(f"  KO: {m['ko_text']}\n")

with open("workspace/translation/missions_dump_utf8.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(lines))

print(f"Dumped {len(missions)} mission records")
