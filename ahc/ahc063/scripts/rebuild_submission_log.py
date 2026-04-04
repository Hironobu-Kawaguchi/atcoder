#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib


def root_dir() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def official_case_count(root: pathlib.Path) -> int:
    return len(list((root / "tools" / "in").glob("*.txt")))


def is_full_record(summary: dict, expected_cases: int) -> bool:
    cases = summary.get("cases")
    return isinstance(cases, int) and cases == expected_cases


def load_metadatas(root: pathlib.Path) -> list[dict]:
    records = []
    expected_cases = official_case_count(root)
    for path in sorted((root / "experiments").glob("*/metadata.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        summary = {}
        summary_path = data.get("summary_json_path")
        if summary_path:
            summary_file = pathlib.Path(summary_path)
            if summary_file.exists():
                summary = json.loads(summary_file.read_text(encoding="utf-8"))
        if not is_full_record(summary, expected_cases):
            continue
        data["_summary"] = summary
        records.append(data)
    return records


def fmt(value) -> str:
    return "-" if value in (None, "", []) else str(value)


def fmt_score(value) -> str:
    if value in (None, "", []):
        return "-"
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float) and value.is_integer():
        return f"{int(value):,}"
    return str(value)


def build_markdown(records: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# 提出ログ")
    lines.append("")
    lines.append("全公式ケースでローカル評価した実験のみを掲載。")
    lines.append("")

    if not records:
        lines.append("全件評価済みの実験はまだありません。")
        lines.append("")
        return "\n".join(lines)

    ordered = list(reversed(records))

    lines.append("## 一覧")
    lines.append("")
    lines.append("| 実験 | ローカルスコア | 提出スコア | 結果 | 実行時間 | 実装概要 |")
    lines.append("| --- | ---: | ---: | --- | ---: | --- |")
    for data in ordered:
        summary = data.get("_summary", {})
        submission = data.get("submission") or {}
        exp_id = data.get("experiment_id", "")
        implementation = data.get("implementation_summary") or "TODO"
        lines.append(
            f"| `{exp_id}` | "
            f"{fmt_score(data.get('local_total_score', summary.get('total_score')))} | "
            f"{fmt_score(submission.get('score'))} | "
            f"{fmt(submission.get('result'))} | "
            f"{fmt(submission.get('exec_time_ms'))} ms | "
            f"{implementation} |"
        )
    lines.append("")

    lines.append("## 方針アイデア")
    lines.append("")
    lines.append("- まずは正確な `State` / `apply(dir)` / 採点差分を作る。探索改善より simulator の正しさを優先する。")
    lines.append("- ベースラインは `欲しい色を優先する貪欲 + 安全経路 BFS/A*` にする。手数より `prefix 一致` と `長さ維持` を重く見る。")
    lines.append("- 経路評価では、距離だけでなく「途中で踏む不要な餌」と「bite で回復可能か」を入れる。")
    lines.append("- 次段階は `rolling beam search`。候補行動を数手先まで読み、確定済み prefix を強く評価する。")
    lines.append("- その後に `bad suffix` の削除と再生成を行う局所修復、必要なら焼きなましを足す。")
    lines.append("- 実行時間 2 sec を踏まえ、序盤は安い貪欲、中盤は beam、終盤は局所修復という多段構成を目指す。")
    lines.append("")

    lines.append("## 詳細")
    lines.append("")
    lines.append("| 実験 | 解法ファイル | ローカル平均時間 | ローカル最大時間 | 失敗数 | 提出ID | 記録日時 | 次のアイデア |")
    lines.append("| --- | --- | ---: | --- | ---: | --- | --- | --- |")
    for data in ordered:
        summary = data.get("_summary", {})
        submission = data.get("submission") or {}
        exp_id = data.get("experiment_id", "")
        next_ideas = data.get("next_ideas") or ["TODO"]
        next_text = " / ".join(next_ideas)
        max_elapsed = (
            f"{fmt(data.get('local_max_elapsed_ms', summary.get('max_elapsed_ms')))} ms "
            f"({fmt(data.get('local_max_elapsed_case', summary.get('max_elapsed_case')))})"
        )
        lines.append(
            f"| `{exp_id}` | "
            f"{fmt(data.get('active_solution'))} | "
            f"{fmt(data.get('local_average_elapsed_ms', summary.get('average_elapsed_ms')))} ms | "
            f"{max_elapsed} | "
            f"{fmt(data.get('local_failed', summary.get('failed')))} | "
            f"{fmt(submission.get('submission_id'))} | "
            f"{fmt(submission.get('recorded_at'))} | "
            f"{next_text} |"
        )
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    root = root_dir()
    records = load_metadatas(root)
    target = root / "SUBMISSIONS.md"
    target.write_text(build_markdown(records), encoding="utf-8")
    print(f"rebuilt {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
