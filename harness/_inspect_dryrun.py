import json
import sys
from pathlib import Path

p = sorted(Path("harness/sweep_output").glob("m3.1_sweep_dry-run_*.jsonl"))[-1]
print(f"reading: {p}")
print()
for i, line in enumerate(open(p, encoding="utf-8")):
    rec = json.loads(line)
    if rec.get("_meta"):
        continue
    print(f"--- candidate {i} family={rec['family']} n={rec['n']} ---")
    print(f"  cascade verdict: {rec['cascade']['verdict']}")
    for pp in rec["cascade"]["per_precision"]:
        print(f"    P={pp['P']}: K={pp['iteration_count']}, rel={pp['relation']}, elapsed={pp['elapsed_s']:.4f}s")
    print(f"  H_empirical: {rec['H_empirical']:.2e}")
    print(f"  H_rigorous_min: {rec['H_rigorous_min']:.2e}")
    print(f"  pslq_residual_check: {rec['pslq_residual_check']}")
    print(f"  verification_class: {rec['verification_class']}")
    print(f"  has_complement: {rec['has_complement']}")
    print()
