#!/usr/bin/env python3
"""Compile and evaluate all AHC068 candidates on the official 100 inputs once."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOLUTIONS = (
    ROOT / "solutions" / "agent_tree_exact.rs",
    ROOT / "solutions" / "agent_greedy_rect.rs",
    ROOT / "solutions" / "agent_distance_hybrid.rs",
)


@dataclass(frozen=True)
class CaseResult:
    solution: str
    case: str
    status: str
    score: int | None
    operations: int | None
    elapsed_ms: float
    output_path: str
    log_path: str
    message: str


def run_checked(command: list[str], *, cwd: Path = ROOT) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def compile_programs(solutions: tuple[Path, ...], bin_dir: Path) -> dict[str, Path]:
    bin_dir.mkdir(parents=True, exist_ok=True)
    binaries: dict[str, Path] = {}
    for source in solutions:
        if not source.is_file():
            raise FileNotFoundError(source)
        name = source.stem
        binary = bin_dir / name
        run_checked(["rustc", "--edition=2021", "-O", str(source), "-o", str(binary)])
        binaries[name] = binary

    run_checked(
        [
            "cargo",
            "build",
            "--release",
            "--manifest-path",
            str(ROOT / "evaluator" / "Cargo.toml"),
        ]
    )
    return binaries


def evaluate_case(
    solution: str,
    binary: Path,
    case_path: Path,
    run_dir: Path,
    timeout_sec: float,
) -> CaseResult:
    case = case_path.stem
    output_path = run_dir / "outputs" / solution / f"{case}.txt"
    log_path = run_dir / "logs" / solution / f"{case}.log"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()

    try:
        with case_path.open("rb") as input_file, output_path.open("wb") as output_file:
            process = subprocess.run(
                [str(binary)],
                stdin=input_file,
                stdout=output_file,
                stderr=subprocess.PIPE,
                timeout=timeout_sec,
                check=False,
            )
    except subprocess.TimeoutExpired as error:
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        message = f"solver timeout after {timeout_sec:.3f}s"
        if error.stderr:
            message += "\n" + error.stderr.decode(errors="replace")
        log_path.write_text(message + "\n", encoding="utf-8")
        return CaseResult(solution, case, "timeout", None, None, elapsed_ms, str(output_path), str(log_path), message)

    elapsed_ms = (time.perf_counter() - started) * 1000.0
    stderr = process.stderr.decode(errors="replace")
    if process.returncode != 0:
        message = f"solver exited with code {process.returncode}"
        log_path.write_text(message + "\n" + stderr, encoding="utf-8")
        return CaseResult(solution, case, "runtime_error", None, None, elapsed_ms, str(output_path), str(log_path), message)

    scorer = ROOT / "evaluator" / "target" / "release" / "ahc068-scorer"
    scored = subprocess.run(
        [str(scorer), str(case_path), str(output_path)],
        capture_output=True,
        text=True,
        timeout=30.0,
        check=False,
    )
    scorer_text = scored.stdout.strip()
    log_path.write_text(stderr + scored.stderr, encoding="utf-8")
    if scored.returncode != 0:
        message = scored.stderr.strip() or f"scorer exited with code {scored.returncode}"
        return CaseResult(solution, case, "invalid", None, None, elapsed_ms, str(output_path), str(log_path), message)

    match = re.fullmatch(r"(-?\d+),(\d+)", scorer_text)
    if match is None:
        message = f"unexpected scorer output: {scorer_text!r}"
        return CaseResult(solution, case, "scorer_error", None, None, elapsed_ms, str(output_path), str(log_path), message)

    score, operations = map(int, match.groups())
    return CaseResult(solution, case, "ok", score, operations, elapsed_ms, str(output_path), str(log_path), "")


def write_reports(results: list[CaseResult], run_dir: Path) -> None:
    results.sort(key=lambda value: (value.solution, value.case))
    detail_path = run_dir / "details.csv"
    with detail_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CaseResult.__dataclass_fields__.keys())
        writer.writeheader()
        writer.writerows(asdict(result) for result in results)

    summary_rows = []
    for solution in sorted({result.solution for result in results}):
        rows = [result for result in results if result.solution == solution]
        valid = [result for result in rows if result.status == "ok"]
        scores = [result.score for result in valid if result.score is not None]
        operations = [result.operations for result in valid if result.operations is not None]
        elapsed = [result.elapsed_ms for result in rows]
        summary_rows.append(
            {
                "solution": solution,
                "cases": len(rows),
                "valid_cases": len(valid),
                "exact_cases": sum(score >= 400 for score in scores),
                "total_score": sum(scores),
                "mean_score": f"{sum(scores) / len(scores):.3f}" if scores else "",
                "min_score": min(scores, default=""),
                "max_score": max(scores, default=""),
                "mean_operations": f"{sum(operations) / len(operations):.3f}" if operations else "",
                "max_operations": max(operations, default=""),
                "mean_elapsed_ms": f"{sum(elapsed) / len(elapsed):.3f}" if elapsed else "",
                "max_elapsed_ms": f"{max(elapsed):.3f}" if elapsed else "",
            }
        )

    summary_path = run_dir / "summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=summary_rows[0].keys())
        writer.writeheader()
        writer.writerows(summary_rows)

    print(summary_path.read_text(encoding="utf-8"), end="")
    print(f"details: {detail_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=int, default=min(os.cpu_count() or 1, 16))
    parser.add_argument("--timeout", type=float, default=3.0, help="solver timeout per case in seconds")
    parser.add_argument("--solution", type=Path, action="append", dest="solutions")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.jobs < 1 or args.timeout <= 0:
        raise ValueError("jobs and timeout must be positive")
    solutions = tuple(path.resolve() for path in (args.solutions or DEFAULT_SOLUTIONS))
    cases = tuple(sorted((ROOT / "tools" / "in").glob("*.txt")))
    if len(cases) != 100:
        raise RuntimeError(f"expected 100 official cases, found {len(cases)}")

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = ROOT / "results" / run_id
    binaries = compile_programs(solutions, run_dir / "bin")
    metadata = {
        "run_id": run_id,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "jobs": args.jobs,
        "timeout_sec": args.timeout,
        "cases": len(cases),
        "solutions": [str(path) for path in solutions],
        "git_commit": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip(),
        "rustc": subprocess.run(["rustc", "--version"], capture_output=True, text=True, check=True).stdout.strip(),
    }
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    futures = []
    results: list[CaseResult] = []
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        for solution, binary in binaries.items():
            for case_path in cases:
                futures.append(executor.submit(evaluate_case, solution, binary, case_path, run_dir, args.timeout))
        for completed, future in enumerate(as_completed(futures), start=1):
            results.append(future.result())
            if completed % 25 == 0 or completed == len(futures):
                print(f"completed {completed}/{len(futures)}", flush=True)

    write_reports(results, run_dir)


if __name__ == "__main__":
    main()
