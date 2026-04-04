#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import pathlib


FIELDNAMES = [
    "experiment_id",
    "name",
    "created_at",
    "active_solution",
    "local_total_score",
    "local_average_score",
    "local_failed",
    "local_average_elapsed_ms",
    "local_max_elapsed_ms",
    "local_max_elapsed_case",
    "submission_result",
    "submission_score",
    "submission_exec_time_ms",
    "submission_id",
    "submission_recorded_at",
    "main_rs_sha256",
]


def root_dir() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def fmt_score(value) -> str:
    if value in (None, "", []):
        return ""
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float) and value.is_integer():
        return f"{int(value):,}"
    return str(value)


def official_case_count(root: pathlib.Path) -> int:
    return len(list((root / "tools" / "in").glob("*.txt")))


def is_full_record(data: dict, summary: dict, expected_cases: int) -> bool:
    cases = summary.get("cases")
    return isinstance(cases, int) and cases == expected_cases


def load_rows(root: pathlib.Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    expected_cases = official_case_count(root)
    for path in sorted((root / "experiments").glob("*/metadata.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        summary = {}
        summary_path = data.get("summary_json_path")
        if summary_path:
            summary_file = pathlib.Path(summary_path)
            if summary_file.exists():
                summary = json.loads(summary_file.read_text(encoding="utf-8"))
        if not is_full_record(data, summary, expected_cases):
            continue
        submission = data.get("submission") or {}
        rows.append(
            {
                "experiment_id": data.get("experiment_id", ""),
                "name": data.get("name", ""),
                "created_at": data.get("created_at", ""),
                "active_solution": data.get("active_solution", ""),
                "local_total_score": fmt_score(data.get("local_total_score", summary.get("total_score", ""))),
                "local_average_score": fmt_score(data.get("local_average_score", summary.get("average_score", ""))),
                "local_failed": data.get("local_failed", summary.get("failed", "")),
                "local_average_elapsed_ms": data.get("local_average_elapsed_ms", summary.get("average_elapsed_ms", "")),
                "local_max_elapsed_ms": data.get("local_max_elapsed_ms", summary.get("max_elapsed_ms", "")),
                "local_max_elapsed_case": data.get("local_max_elapsed_case", summary.get("max_elapsed_case", "")),
                "submission_result": submission.get("result", ""),
                "submission_score": fmt_score(submission.get("score", "")),
                "submission_exec_time_ms": submission.get("exec_time_ms", ""),
                "submission_id": submission.get("submission_id", ""),
                "submission_recorded_at": submission.get("recorded_at", ""),
                "main_rs_sha256": data.get("main_rs_sha256", ""),
            }
        )
    return rows


def main() -> int:
    root = root_dir()
    rows = load_rows(root)
    index_path = root / "experiments" / "index.csv"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"rebuilt {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
