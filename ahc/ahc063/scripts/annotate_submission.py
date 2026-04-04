#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import time


def root_dir() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def latest_experiment(root: pathlib.Path) -> pathlib.Path:
    expected_cases = len(list((root / "tools" / "in").glob("*.txt")))
    dirs = sorted(path for path in (root / "experiments").glob("*") if path.is_dir())
    for exp_dir in reversed(dirs):
        metadata_path = exp_dir / "metadata.json"
        if not metadata_path.exists():
            continue
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        summary_path = metadata.get("summary_json_path")
        if not summary_path:
            continue
        summary_file = pathlib.Path(summary_path)
        if not summary_file.exists():
            continue
        summary = json.loads(summary_file.read_text(encoding="utf-8"))
        if summary.get("cases") == expected_cases:
            return exp_dir
    raise SystemExit("no full-evaluation experiments found")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Attach an AtCoder submission result to an experiment.")
    parser.add_argument("--experiment", help="Experiment id, defaults to the latest one")
    parser.add_argument("--result", default="AC", help="Judge result, e.g. AC")
    parser.add_argument("--score", type=int, help="Submitted score shown by AtCoder")
    parser.add_argument("--exec-time-ms", type=int, help="Submitted execution time in ms")
    parser.add_argument("--submission-id", help="Optional AtCoder submission id")
    parser.add_argument("--implementation", help="Short markdown/plaintext note about the implementation")
    parser.add_argument(
        "--next-idea",
        action="append",
        default=[],
        help="One next-step idea. Can be passed multiple times.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = root_dir()
    exp_dir = (root / "experiments" / args.experiment) if args.experiment else latest_experiment(root)
    metadata_path = exp_dir / "metadata.json"
    if not metadata_path.exists():
        print(f"metadata not found: {metadata_path}", file=sys.stderr)
        return 1

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["submission"] = {
        "result": args.result,
        "score": args.score if args.score is not None else "",
        "exec_time_ms": args.exec_time_ms if args.exec_time_ms is not None else "",
        "submission_id": args.submission_id or "",
        "recorded_at": time.strftime("%Y%m%d-%H%M%S"),
    }
    if args.implementation is not None:
        metadata["implementation_summary"] = args.implementation
    if args.next_idea:
        metadata["next_ideas"] = args.next_idea
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    rebuild = subprocess.run(
        [sys.executable, str(root / "scripts" / "rebuild_index.py")],
        cwd=root,
        check=False,
    )
    if rebuild.returncode != 0:
        return rebuild.returncode

    rebuild_md = subprocess.run(
        [sys.executable, str(root / "scripts" / "rebuild_submission_log.py")],
        cwd=root,
        check=False,
    )
    if rebuild_md.returncode != 0:
        return rebuild_md.returncode

    print(f"annotated {exp_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
