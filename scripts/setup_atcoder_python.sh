#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cache_dir="$repo_root/.uv-cache"
python_dir="$repo_root/.uv-python"
cling_lib="$repo_root/.venv/lib/python3.13/site-packages/cppyy_backend/lib/libCling.so"

export UV_CACHE_DIR="$cache_dir"

cd "$repo_root"

uv python install --install-dir "$python_dir" --no-bin 3.13.7
export UV_PYTHON_INSTALL_DIR="$python_dir"
uv sync

if [[ "$(uname -s)" == "Darwin" && "$(uname -m)" == "arm64" && -f "$cling_lib" && -f /opt/homebrew/lib/libzstd.1.dylib ]]; then
  if otool -L "$cling_lib" | grep -q '/opt/local/lib/libzstd.1.dylib'; then
    install_name_tool \
      -change /opt/local/lib/libzstd.1.dylib /opt/homebrew/lib/libzstd.1.dylib \
      "$cling_lib"
  fi
fi
