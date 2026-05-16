"""Audit the H10-mandated extended dry-run output."""
import json
import sys
from pathlib import Path

f = Path("harness/sweep_output/m31_extended_dryrun_20260516_113214.jsonl")
recs = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines()]
meta = [r for r in recs if "_meta" in r]
cands = [r for r in recs if "_meta" not in r]
print(f"meta records: {len(meta)} (header+footer expected = 2)")
print(f"candidate records: {len(cands)} (expected 65)")
print(f"all dry_run? {all(r.get('_dry_run', False) for r in cands)}")
print(f"verdicts: {set(r['cascade']['verdict'] for r in cands)}")
print(f"classes:  {set(r['verification_class'] for r in cands)}")
print(f"distinct n values: {sorted(set(r['n'] for r in cands))}")
print()
print("Sample one record per n value:")
seen_n = set()
for r in cands:
    n = r["n"]
    if n in seen_n: continue
    seen_n.add(n)
    op = r["H_empirical_operational"]
    fm = r["H_empirical_formula"]
    op_str = f"{float(op):.4e}" if isinstance(op, float) or (isinstance(op, int) and op < 10**300) else f"int(10^{len(str(op))-1})"
    fm_str = f"{float(fm):.4e}" if isinstance(fm, float) or (isinstance(fm, int) and fm < 10**300) else f"int(10^{len(str(fm))-1})"
    cap_active = "YES" if op != fm else "no"
    print(f"  n={n:2d}  family={r['family'][:36]:36s}  op={op_str}  formula={fm_str}  cap_active={cap_active}")

print()
print("Footer record:")
print(json.dumps(meta[-1] if meta else None, indent=2, default=str)[:600])
