import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("workspace/translation/localdat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
    records = [json.loads(line) for line in f if line.strip()]

# Filter movie cutscenes (ko_id >= 5000)
movies = [r for r in records if r.get("ko_id") is not None and r["ko_id"] >= 5000]

print(f"Total movie records: {len(movies)}")
print(f"ID range: {movies[0]['ko_id']} .. {movies[-1]['ko_id']}")

output_lines = []
for m in movies:
    output_lines.append(f"--- ID {m['ko_id']} (JA ref: {m['ja_id']}) ---")
    output_lines.append(f"JA: {m['ja_text']}")
    output_lines.append(f"KO: {m['ko_text']}")
    output_lines.append("")

with open("workspace/translation/cutscenes_dump.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(output_lines))

print("Dumped to workspace/translation/cutscenes_dump.txt")

