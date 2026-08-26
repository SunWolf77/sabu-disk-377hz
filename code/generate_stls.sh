#!/usr/bin/env bash
# Generate approximate Sabu-form + null-twin STLs (Python stdlib only).
# Usage (from repo root):
#   bash code/generate_stls.sh
#   bash code/generate_stls.sh 0.25 STL
#   bash code/generate_stls.sh 0.5 STL
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
SCALE="${1:-0.25}"
OUT="${2:-STL}"
mkdir -p "$OUT"
python3 code/export_stl_approx.py --scale "$SCALE" --out "$OUT"
echo
echo "Verify before slicing:"
ls -la "$OUT"/*.stl
echo
echo "Checklist"
echo "  [ ] two files: sabu_approx_*.stl and null_twin_*.stl"
echo "  [ ] Sabu mesh shows three kidney openings + central bore in the slicer"
echo "  [ ] null twin is a plain bowl + hub (no kidneys)"
echo "  [ ] bowl-up orientation; do not fill kidneys with supports"
echo "Next: docs/REPLICA.md → templates/print_log.csv → docs/NULL_TEST.md"
