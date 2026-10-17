import json
import re
import sys

def main():
    with open("workspace/translation/localdat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    # Also check HELPLOCALDAT
    with open("workspace/translation/helplocaldat_ja_ko_aligned.jsonl", "r", encoding="utf-8") as f:
        help_records = [json.loads(line) for line in f if line.strip()]

    all_records = records + help_records

    findings = []
    typo_patterns = [
        (r"않되", "안 되"),
        (r"않돼", "안 돼"),
        (r"안돼요", "안 돼요"),
        (r"됫", "됐"),
        (r"파해치", "파헤치"),
        (r"어떻해", "어떡해"),
        (r"웬지", "왠지"),
        (r"바램", "바람"),
        (r"이럴수가", "이럴 수가"),
        (r"어쩔수가", "어쩔 수가"),
        (r"할수\b", "할 수"),
        (r"볼수\b", "볼 수"),
        (r"갈수\b", "갈 수"),
        (r"있을수\b", "있을 수"),
        (r"없을수\b", "없을 수"),
        (r"고장난", "고장 난"),
        (r"한시간", "한 시간"),
        (r"몇가지", "몇 가지"),
        (r"두번째", "두 번째"),
        (r"세번째", "세 번째"),
        (r"첫번째", "첫 번째"),
        (r"눈을 감어", "눈을 감아"),
        (r"얻으려도", "얻으려고"),
        (r"좋도록 해", "마음대로 해"),
        (r"아빠예요", "아빠에요"),
        (r"작동불능", "작동 불능"),
    ]

    for r in all_records:
        kid = r.get("ko_id")
        ko = r.get("ko_text", "")
        ja = r.get("ja_text", "")
        cat = r.get("category", "")

        for pat, fix in typo_patterns:
            if re.search(pat, ko):
                findings.append({
                    "id": kid,
                    "cat": cat,
                    "pattern": pat,
                    "fix": fix,
                    "ko": ko,
                    "ja": ja
                })

    out_file = "workspace/translation/scan_issues.json"
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(findings, out, ensure_ascii=False, indent=2)

    print(f"Total findings: {len(findings)}. Saved to {out_file}")

if __name__ == "__main__":
    main()
