#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run solver on one AHC063 case.")
    parser.add_argument("--case", default="0000", help="Case id under tools/in, e.g. 0000")
    parser.add_argument("--input", help="Override input file path")
    parser.add_argument("--output", help="Override output file path")
    parser.add_argument("--vis", action="store_true", help="Run official visualizer")
    return parser.parse_args()


def run() -> int:
    args = parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    solver_bin = root / "target" / "release" / "main"
    tools_dir = root / "tools"
    vis_bin = tools_dir / "target" / "release" / "vis"

    if not solver_bin.exists():
        print(f"solver binary not found: {solver_bin}", file=sys.stderr)
        print("run `make build` first", file=sys.stderr)
        return 1

    input_path = pathlib.Path(args.input) if args.input else tools_dir / "in" / f"{args.case}.txt"
    output_path = pathlib.Path(args.output) if args.output else root / "out" / f"{args.case}.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("rb") as fin, output_path.open("wb") as fout:
        completed = subprocess.run([str(solver_bin)], stdin=fin, stdout=fout)
    if completed.returncode != 0:
        return completed.returncode

    print(f"wrote {output_path}")

    if not args.vis:
        return 0

    if not vis_bin.exists():
        print(f"visualizer binary not found: {vis_bin}", file=sys.stderr)
        print("run `make tools-build` first", file=sys.stderr)
        return 1

    vis_completed = subprocess.run(
        [str(vis_bin), str(input_path), str(output_path)],
        cwd=tools_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    sys.stdout.write(vis_completed.stdout)
    sys.stderr.write(vis_completed.stderr)
    if vis_completed.returncode != 0:
        return vis_completed.returncode

    generated_html = tools_dir / "vis.html"
    if generated_html.exists():
        html_path = output_path.with_suffix(".html")
        shutil.move(str(generated_html), str(html_path))
        print(f"wrote {html_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
