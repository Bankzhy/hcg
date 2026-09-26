#!/usr/bin/env bash
set -euo pipefail

PACKAGE_DIR="$(cd "$(dirname "$0")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  exec python3 "$PACKAGE_DIR/serve.py" "$@"
fi

echo "Python 3 is required to run HCG." >&2
exit 1
