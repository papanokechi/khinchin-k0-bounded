"""Dry-run with gp leg enabled, at small-but-real precision.
Verifies the full three-leg pipeline against a single complement-only sub-basis.
"""
import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from verify import verify_candidate

print("M3.1 harness: integrated three-leg dry-run with gp leg enabled")
print("Sub-basis: (log K_0, K_0*pi) — pair_log_x family, n=2")
print("Precisions: (200, 400, 800) dps; maxsteps 1000/1000/1000; maxcoeff 10^30")
print()

result = verify_candidate(
    family="integrated_dry_run_log_K0pi",
    indices=(7, 8),
    precisions=(200, 400, 800),
    maxcoeff_exp=30,
    maxsteps_per_prec=(1000, 1000, 1000),
    rigorous_tier=False,
    run_gp_leg=True,
)

print(f"family:            {result['family']}")
print(f"indices/labels:    {result['indices']} / {result['labels']}")
print(f"n:                 {result['n']}")
print(f"cascade verdict:   {result['cascade']['verdict']}")
for p in result["cascade"]["per_precision"]:
    print(f"  P={p['P']:>4d}: K={p['iteration_count']:>4d}  rel={p['relation']}  elapsed={p['elapsed_s']:.3f}s")
print(f"H_empirical:       {result['H_empirical']:.2e}")
print(f"H_rigorous_min:    {result['H_rigorous_min']:.2e}")
print(f"gp_lindep:         relation={result['gp_lindep']['relation']}  error={result['gp_lindep']['error']}")
print(f"residual check:    {result['pslq_residual_check']}")
print(f"verification_class: {result['verification_class']}")
print(f"has_complement:    {result['has_complement']}")
print(f"ef1_only:          {result['ef1_only']}")
