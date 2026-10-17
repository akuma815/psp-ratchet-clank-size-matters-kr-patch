import json

with open("workspace/translation/localdat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
    records = [json.loads(line) for line in f if line.strip()]

weapons = [r for r in records if r.get("ko_id") is not None and 550 <= r["ko_id"] <= 639]

lines = []
for w in weapons:
    lines.append(f"[{w['ko_id']:4d}]")
    lines.append(f"  JA: {w['ja_text']}")
    lines.append(f"  KO: {w['ko_text']}\n")

with open("workspace/translation/weapons_dump_utf8.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(lines))

print(f"Dumped {len(weapons)} weapon records")
