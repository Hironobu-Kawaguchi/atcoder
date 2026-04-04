#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Snapshot source, outputs, and scores for one AHC063 experiment.")
    parser.add_argument("--name", default="manual", help="Short experiment label")
    parser.add_argument("--limit", type=int, default=100, help="Number of official inputs to evaluate")
    parser.add_argument("--jobs", type=int, default=1, help="Parallel workers for batch evaluation")
    parser.add_argument("--toolchain", help="Optional rustup toolchain for submission check")
    return parser.parse_args()


def slugify(name: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in name.strip())
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    return cleaned or "manual"


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    args = parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    official_case_count = len(list((root / "tools" / "in").glob("*.txt")))
    if args.limit != official_case_count:
        print(
            f"record_experiment requires full evaluation: limit={args.limit}, official_cases={official_case_count}",
            file=sys.stderr,
        )
        return 1
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    exp_id = f"{timestamp}-{slugify(args.name)}"
    exp_dir = root / "experiments" / exp_id
    src_dir = exp_dir / "source"
    out_dir = exp_dir / "out"
    src_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    active_solution_rel = (root / "ACTIVE_SOLUTION").read_text(encoding="utf-8").strip()
    active_solution = root / active_solution_rel

    shutil.copy2(root / "Cargo.toml", src_dir / "Cargo.toml")
    (src_dir / "src").mkdir()
    shutil.copy2(root / "src" / "main.rs", src_dir / "src" / "main.rs")
    (src_dir / "solutions").mkdir()
    shutil.copy2(active_solution, src_dir / "solutions" / active_solution.name)
    shutil.copy2(root / "ACTIVE_SOLUTION", src_dir / "ACTIVE_SOLUTION")

    submission_report = exp_dir / "submission_check.json"
    check_cmd = [
        sys.executable,
        str(root / "scripts" / "check_submission.py"),
        "--report-path",
        str(submission_report),
    ]
    if args.toolchain:
        check_cmd.extend(["--toolchain", args.toolchain])
    check = subprocess.run(check_cmd, cwd=root, check=False)
    if check.returncode != 0:
        return check.returncode

    scores_csv = exp_dir / "scores.csv"
    summary_json = exp_dir / "summary.json"
    batch_cmd = [
        sys.executable,
        str(root / "scripts" / "batch_eval.py"),
        "--limit",
        str(args.limit),
        "--jobs",
        str(args.jobs),
        "--out-dir",
        str(out_dir),
        "--csv-path",
        str(scores_csv),
        "--summary-path",
        str(summary_json),
    ]
    batch = subprocess.run(batch_cmd, cwd=root, check=False)
    if batch.returncode not in (0, 2):
        return batch.returncode
    summary = json.loads(summary_json.read_text(encoding="utf-8"))

    git_head = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    git_status = subprocess.run(
        ["git", "-C", str(root), "status", "--short", "ahc/ahc063"],
        capture_output=True,
        text=True,
        check=False,
    )

    metadata = {
        "experiment_id": exp_id,
        "name": args.name,
        "created_at": timestamp,
        "limit": args.limit,
        "jobs": args.jobs,
        "active_solution": active_solution_rel,
        "local_total_score": summary["total_score"],
        "local_average_score": summary["average_score"],
        "local_failed": summary["failed"],
        "local_average_elapsed_ms": summary["average_elapsed_ms"],
        "local_max_elapsed_ms": summary["max_elapsed_ms"],
        "local_max_elapsed_case": summary["max_elapsed_case"],
        "cargo_toml_sha256": sha256(root / "Cargo.toml"),
        "main_rs_sha256": sha256(root / "src" / "main.rs"),
        "active_solution_sha256": sha256(active_solution),
        "git_head": git_head.stdout.strip(),
        "git_status_ahc063": git_status.stdout.strip().splitlines(),
        "submission_check_path": str(submission_report),
        "scores_csv_path": str(scores_csv),
        "summary_json_path": str(summary_json),
        "implementation_summary": "TODO",
        "next_ideas": ["TODO"],
        "submission": None,
    }
    (exp_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

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

    print(f"experiment : {exp_id}")
    print(f"dir        : {exp_dir}")
    print(f"scores     : {scores_csv}")
    print(f"summary    : {summary_json}")
    return batch.returncode


if __name__ == "__main__":
    raise SystemExit(main())
