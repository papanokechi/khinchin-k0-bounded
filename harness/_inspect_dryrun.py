"""Inspect the latest dry-run / canonical JSONL for the verify.py output structure."""
import json
import sys
from pathlib import Path

if len(sys.argv) > 1:
    p = Path(sys.argv[1])
else:
    candidates = (
        sorted(Path('harness/sweep_output').glob('m32a_*.jsonl')) +
        sorted(Path('harness/sweep_output').glob('m31_extended_dryrun_*.jsonl')) +
        sorted(Path('harness/sweep_output').glob('m31_dryrun_*.jsonl'))
    )
    p = candidates[-1] if candidates else None

if p is None or not p.exists():
    print("no JSONL found")
    sys.exit(0)

print(f'reading: {p}')
print()
for line in open(p, encoding='utf-8'):
    rec = json.loads(line)
    if rec.get('_meta'):
        print(f"_meta: mode={rec.get('mode')}  dry_run={rec.get('dry_run')}  "
              f"canonical={rec.get('canonical')}  n_candidates={rec.get('n_candidates')}  "
              f"total_elapsed_s={rec.get('total_elapsed_s')}")
        continue
    print()
    print(f"family={rec['family']}  indices={rec['indices']}  n={rec['n']}")
    print(f"  labels: {rec['labels']}")
    print(f"  cascade.verdict: {rec['cascade']['verdict']}")
    for pp in rec['cascade']['per_precision']:
        print(f"    P={pp['P']}: K={pp['iteration_count']}  final_norm={pp.get('final_norm')}  "
              f"term_reason={pp.get('termination_reason')!r}  "
              f"H_rigorous={pp.get('H_rigorous'):.2e}  elapsed={pp.get('elapsed_s'):.2f}s")
        if pp.get('relation') is not None:
            print(f"      RELATION: {pp['relation']}")
    # Handle both old schema (H_empirical) and new schema (H_empirical_operational / _formula)
    if "H_empirical_operational" in rec:
        op = rec["H_empirical_operational"]
        fm = rec["H_empirical_formula"]
        op_disp = f"{float(op):.4e}" if isinstance(op, float) or (isinstance(op, int) and op < 10**300) else f"int(10^{len(str(op))-1})"
        fm_disp = f"{float(fm):.4e}" if isinstance(fm, float) or (isinstance(fm, int) and fm < 10**300) else f"int(10^{len(str(fm))-1})"
        print(f"  H_empirical_operational (canonical): {op_disp}")
        print(f"  H_empirical_formula     (uncapped):  {fm_disp}")
    elif "H_empirical" in rec:
        print(f"  H_empirical (legacy schema): {rec['H_empirical']:.4e}")
    print(f"  H_rigorous_min:  {rec['H_rigorous_min']:.4e}")
    gp = rec['gp_lindep']
    print(f"  gp_lindep.error:                {gp.get('error')!r}")
    print(f"  gp_lindep.max_abs_coefficient:  {gp.get('max_abs_coefficient')}")
    print(f"  gp_lindep.within_empirical_bound: {gp.get('within_empirical_bound')}")
    print(f"  gp_lindep.gp_verdict:           {gp.get('gp_verdict')!r}")
    print(f"  pslq_residual_check:            {rec['pslq_residual_check']}")
    print(f"  verification_class:             {rec['verification_class']}")
    print(f"  has_complement={rec['has_complement']}  ef1_only={rec['ef1_only']}  "
          f"rigorous_tier={rec['rigorous_tier']}")
