# atcoder
atcoder challenge
https://atcoder.jp/users/hkawaguc

## Python environment

As of 2026-04-04, the active AtCoder judge uses `Python (CPython 3.13.7)` and runs submissions with:

```bash
python3.13 -X int_max_str_digits=0 Main.py
```

This repository is configured for `uv` so that the local environment tracks the current AtCoder Python version and package set.

```bash
./scripts/setup_atcoder_python.sh
```

The script installs `Python 3.13.7` into `.uv-python/`, syncs the project into `.venv/`, and applies the macOS-specific `cppyy` fix when needed.

Official sources:

- https://img.atcoder.jp/file/language-update/2025-10/language-list.html
- https://img.atcoder.jp/file/language-update/2025-10/082-3-13_cpython.toml

AtCoder runs on Linux x86_64, so exact binary parity is not always guaranteed on macOS even when package versions are aligned.

## Legacy Docker note

```bash
docker run --name atcoder -it --rm -v $(pwd):/root/library/mydir/ hinamimi/atcoder:latest
```
