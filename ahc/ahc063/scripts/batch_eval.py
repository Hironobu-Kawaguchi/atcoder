#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor


SCORE_RE = re.compile(r"Score = (\d+)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Batch-evaluate AHC063 solutions with official vis.")
    parser.add_argument("--limit", type=int, default=100, help="Number of inputs from tools/in to evaluate")
    parser.add_argument("--jobs", type=int, default=1, help="Parallel workers")
    parser.add_argument("--out-dir", help="Directory to store solver outputs")
    parser.add_argument("--csv-path", help="Path to write per-case scores as CSV")
    parser.add_argument("--summary-path", help="Path to write summary as JSON")
    return parser.parse_args()


def evaluate_case(case_path: pathlib.Path, solver_bin: pathlib.Path, vis_bin: pathlib.Path, out_dir: pathlib.Path) -> dict[str, object]:
    case_name = case_path.stem
    output_path = out_dir / f"{case_name}.txt"

    start = time.perf_counter()
    with case_path.open("rb") as fin, output_path.open("wb") as fout:
        solver = subprocess.run([str(solver_bin)], stdin=fin, stdout=fout, check=False)
    elapsed = time.perf_counter() - start

    result = {
        "case": case_name,
        "score": 0,
        "elapsed_ms": round(elapsed * 1000, 3),
        "status": "ok" if solver.returncode == 0 else f"solver_exit_{solver.returncode}",
    }
    if solver.returncode != 0:
        return result

    with tempfile.TemporaryDirectory() as workdir:
        vis = subprocess.run(
            [str(vis_bin), str(case_path), str(output_path)],
            cwd=workdir,
            capture_output=True,
            text=True,
            check=False,
        )
        stdout = vis.stdout.strip()
        if vis.returncode != 0:
            result["status"] = f"vis_exit_{vis.returncode}"
            return result
        match = SCORE_RE.search(stdout)
        if match is None:
            result["status"] = "score_parse_failed"
            return result
        result["score"] = int(match.group(1))
        if "Score = 0" in stdout and stdout != "Score = 0":
            result["status"] = stdout.splitlines()[0]
    return result


def main() -> int:
    args = parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    solver_bin = root / "target" / "release" / "main"
    vis_bin = root / "tools" / "target" / "release" / "vis"
    in_dir = root / "tools" / "in"
    out_dir = pathlib.Path(args.out_dir) if args.out_dir else root / "out"
    log_dir = root / "logs"

    if not solver_bin.exists():
        print(f"solver binary not found: {solver_bin}", file=sys.stderr)
        print("run `make build` first", file=sys.stderr)
        return 1
    if not vis_bin.exists():
        print(f"visualizer binary not found: {vis_bin}", file=sys.stderr)
        print("run `make tools-build` first", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    case_paths = sorted(in_dir.glob("*.txt"))[: args.limit]
    if not case_paths:
        print(f"no inputs found under {in_dir}", file=sys.stderr)
        return 1

    started_at = time.strftime("%Y%m%d-%H%M%S")
    worker_count = max(1, args.jobs)

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        results = list(executor.map(lambda path: evaluate_case(path, solver_bin, vis_bin, out_dir), case_paths))

    results.sort(key=lambda row: row["case"])
    total_score = sum(int(row["score"]) for row in results)
    avg_score = total_score / len(results)
    avg_elapsed = sum(float(row["elapsed_ms"]) for row in results) / len(results)
    max_elapsed_row = max(results, key=lambda row: float(row["elapsed_ms"]))
    failed = [row for row in results if row["status"] != "ok"]
    worst = sorted(results, key=lambda row: int(row["score"]), reverse=True)[:5]

    csv_path = pathlib.Path(args.csv_path) if args.csv_path else log_dir / f"batch-{started_at}.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["case", "score", "elapsed_ms", "status"])
        writer.writeheader()
        writer.writerows(results)

    summary = {
        "created_at": started_at,
        "cases": len(results),
        "total_score": total_score,
        "average_score": avg_score,
        "average_elapsed_ms": avg_elapsed,
        "max_elapsed_ms": float(max_elapsed_row["elapsed_ms"]),
        "max_elapsed_case": max_elapsed_row["case"],
        "failed": len(failed),
        "csv_path": str(csv_path),
        "out_dir": str(out_dir),
        "worst": worst,
    }
    if args.summary_path:
        summary_path = pathlib.Path(args.summary_path)
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        with summary_path.open("w") as fh:
            json.dump(summary, fh, indent=2)

    print(f"cases     : {len(results)}")
    print(f"total     : {total_score}")
    print(f"average   : {avg_score:.2f}")
    print(f"avg time  : {avg_elapsed:.3f} ms")
    print(f"max time  : {max_elapsed_row['elapsed_ms']} ms ({max_elapsed_row['case']})")
    print(f"failed    : {len(failed)}")
    print(f"log       : {csv_path}")
    print("worst 5   :")
    for row in worst:
        print(f"  {row['case']} score={row['score']} time={row['elapsed_ms']}ms status={row['status']}")

    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
