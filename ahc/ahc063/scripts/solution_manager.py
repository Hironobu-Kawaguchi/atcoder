#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import shutil
import sys


def root_dir() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def active_file(root: pathlib.Path) -> pathlib.Path:
    return root / "ACTIVE_SOLUTION"


def normalize_solution_name(name: str) -> str:
    path = pathlib.Path(name)
    if path.suffix != ".rs":
        path = path.with_suffix(".rs")
    if path.parts and path.parts[0] == "solutions":
        return str(path)
    return str(pathlib.Path("solutions") / path.name)


def read_active_solution(root: pathlib.Path) -> pathlib.Path:
    rel = active_file(root).read_text(encoding="utf-8").strip()
    if not rel:
        raise SystemExit("ACTIVE_SOLUTION is empty")
    return root / rel


def write_active_solution(root: pathlib.Path, rel_path: str) -> None:
    active_file(root).write_text(f"{rel_path}\n", encoding="utf-8")


def sync_active(root: pathlib.Path) -> pathlib.Path:
    src = read_active_solution(root)
    if not src.exists():
        raise SystemExit(f"active solution does not exist: {src}")
    dst = root / "src" / "main.rs"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return src


def cmd_sync(_: argparse.Namespace) -> int:
    root = root_dir()
    src = sync_active(root)
    print(f"synced {src.relative_to(root)} -> src/main.rs")
    return 0


def cmd_activate(args: argparse.Namespace) -> int:
    root = root_dir()
    rel = normalize_solution_name(args.solution)
    src = root / rel
    if not src.exists():
        print(f"solution does not exist: {src}", file=sys.stderr)
        return 1
    write_active_solution(root, rel)
    sync_active(root)
    print(f"active solution: {rel}")
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    root = root_dir()
    new_rel = normalize_solution_name(args.name)
    new_path = root / new_rel
    if new_path.exists():
        print(f"solution already exists: {new_path}", file=sys.stderr)
        return 1

    if args.from_current:
        source = root / "src" / "main.rs"
    elif args.from_solution:
        source = root / normalize_solution_name(args.from_solution)
    else:
        source = read_active_solution(root)

    if not source.exists():
        print(f"base source does not exist: {source}", file=sys.stderr)
        return 1

    new_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, new_path)

    if args.activate:
        write_active_solution(root, new_rel)
        sync_active(root)

    print(f"created {new_rel}")
    return 0


def cmd_list(_: argparse.Namespace) -> int:
    root = root_dir()
    active = read_active_solution(root).resolve()
    for path in sorted((root / "solutions").glob("*.rs")):
        prefix = "*" if path.resolve() == active else " "
        print(f"{prefix} {path.relative_to(root)}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage per-experiment AHC063 solver sources.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("sync", help="Copy the active solution into src/main.rs")

    activate = subparsers.add_parser("activate", help="Set the active solution and sync it")
    activate.add_argument("solution", help="Solution name or path under solutions/")

    create = subparsers.add_parser("create", help="Create a new solution file")
    create.add_argument("name", help="New solution name")
    create.add_argument("--from-solution", help="Clone from a specific solution under solutions/")
    create.add_argument("--from-current", action="store_true", help="Clone from src/main.rs instead of the active solution")
    create.add_argument("--activate", action="store_true", help="Activate the new solution after creation")

    subparsers.add_parser("list", help="List known solutions")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "sync":
        return cmd_sync(args)
    if args.command == "activate":
        return cmd_activate(args)
    if args.command == "create":
        return cmd_create(args)
    if args.command == "list":
        return cmd_list(args)
    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
