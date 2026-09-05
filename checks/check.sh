#!/usr/bin/env bash
# One command that reproduces CI locally. Run from the skill root:
#
#     bash checks/check.sh
#
# Uses your local `tsc` if present, otherwise a cached copy via npx
# (nothing is installed on your system).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if command -v tsc >/dev/null 2>&1; then
  TSC="tsc"
else
  TSC="npx -y -p typescript tsc"
fi

echo "==> structure, links, and index parity"
python3 "$ROOT/checks/validate.py"
python3 "$ROOT/checks/gen_index.py" --check

echo "==> generating example files from rules"
cd "$ROOT/checks"
python3 gen.py

echo "==> compile-checking Good examples"
# tsc exits non-zero when examples error; the baseline gate below decides pass/fail.
$TSC --noEmit --strict --exactOptionalPropertyTypes --noUncheckedIndexedAccess \
  --erasableSyntaxOnly --verbatimModuleSyntax --module esnext \
  --moduleResolution bundler --target es2024 --pretty false \
  examples/ambient.d.ts examples/*.ts > check.log 2>&1 || true

echo "==> gating against the baseline"
python3 analyze.py check.log --check-baseline baseline.txt

echo "All checks passed."
