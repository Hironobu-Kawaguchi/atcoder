#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check whether src/main.rs builds like an AtCoder Rust submission.")
    parser.add_argument("--toolchain", help="Exact rustup toolchain to use, e.g. 1.89.0")
    parser.add_argument("--report-path", help="Optional JSON report path")
    return parser.parse_args()


def build_command(toolchain: str | None) -> list[str]:
    if toolchain:
        return ["rustup", "run", toolchain, "cargo", "build", "--release", "--quiet", "--offline"]
    return ["cargo", "build", "--release", "--quiet", "--offline"]


def main() -> int:
    args = parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    source = root / "src" / "main.rs"

    if not source.exists():
        print(f"source file not found: {source}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = pathlib.Path(tmp)
        (tmpdir / "src").mkdir()
        shutil.copy2(source, tmpdir / "src" / "main.rs")
        (tmpdir / "Cargo.toml").write_text(
            "[package]\nname = \"main\"\nversion = \"0.1.0\"\nedition = \"2021\"\n",
            encoding="utf-8",
        )

        command = build_command(args.toolchain)
        completed = subprocess.run(
            command,
            cwd=tmpdir,
            capture_output=True,
            text=True,
            check=False,
        )

        binary_path = tmpdir / "target" / "release" / "main"
        ok = completed.returncode == 0 and binary_path.exists()
        report = {
            "ok": ok,
            "toolchain": args.toolchain or "default",
            "command": command,
            "binary_exists": binary_path.exists(),
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }

        if args.report_path:
            report_path = pathlib.Path(args.report_path)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

        if ok:
            print("submission check: ok")
            print(f"command         : {' '.join(command)}")
            return 0

        print("submission check: failed", file=sys.stderr)
        print(f"command         : {' '.join(command)}", file=sys.stderr)
        if completed.stdout:
            print(completed.stdout, file=sys.stderr, end="")
        if completed.stderr:
            print(completed.stderr, file=sys.stderr, end="")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
