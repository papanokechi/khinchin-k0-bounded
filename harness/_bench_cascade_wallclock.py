"""Cascade wall-clock benchmark for M2.3 -> M3.1 transition.

Measures single-run wall-clock for mpmath.pslq at the mission basis
(n=15, B_D(C) with D=6, |C|=7) at the three cascade precisions
P=2160, 2P=4320, 4P=8640 dps.

Reports both empirical-tier wall-clock (maxsteps=2000) and an extrapolation
to rigorous-tier wall-clock (maxsteps=100,000 which achieves
H_rigorous=10^70 per precision_budget.md §5.2).

Output flushes line-by-line for progress visibility.
"""

import sys
import time
import mpmath
from mpmath import mp, mpf, pi, e, log, euler, zeta, catalan, khinchin, pslq


def say(s):
    print(s, flush=True)


def build_basis(prec_dps):
    """Construct B_D(C) at given precision. Returns list of n=15 mpf."""
    mp.dps = prec_dps
    K = khinchin
    basis = [mpf(1)]
    K_pow = mpf(1)
    for _ in range(6):
        K_pow = K_pow * K
        basis.append(K_pow)
    basis.append(log(K))
    for c in (pi, e, log(2), euler, zeta(2), zeta(3), catalan):
        basis.append(K * c)
    assert len(basis) == 15
    return basis


def bench_single(prec_dps, maxsteps, maxcoeff_exp=60, label=""):
    """One PSLQ call; returns (build_s, pslq_s, terminated_with_relation)."""
    say(f"  [{label}] P={prec_dps} dps  building basis ...")
    mp.dps = prec_dps
    t0 = time.perf_counter()
    basis = build_basis(prec_dps)
    t1 = time.perf_counter()
    say(f"  [{label}] basis built in {t1-t0:.2f} s; running pslq(maxsteps={maxsteps}) ...")
    rel = pslq(basis, tol=mpmath.mpf(10) ** -int(prec_dps * 0.6),
               maxcoeff=10 ** maxcoeff_exp,
               maxsteps=maxsteps, verbose=False)
    t2 = time.perf_counter()
    say(f"  [{label}] pslq returned {'relation' if rel else 'None'} in {t2-t1:.2f} s")
    return t1 - t0, t2 - t1, rel is not None


def main():
    say("=" * 78)
    say("harness/_bench_cascade_wallclock.py")
    say("M2.3 -> M3.1 cascade wall-clock benchmark, n=15 mission basis")
    say("=" * 78)

    rows = []
    for P in (2160, 4320, 8640):
        build_s, pslq_s, found = bench_single(P, maxsteps=2000, label=f"P={P}")
        rows.append((P, build_s, pslq_s, found))

    say("")
    say("Single-run summary (empirical tier, maxsteps=2000):")
    say(f"  {'P (dps)':>8s} {'build_s':>8s} {'pslq_s':>8s} {'result':>8s}")
    for P, b, p, f in rows:
        say(f"  {P:>8d} {b:>8.2f} {p:>8.2f} {'rel' if f else 'None':>8s}")

    cascade_emp_total = rows[0][2] + rows[1][2] + rows[2][2]
    say("")
    say(f"Cascade(P, 2P, 4P) empirical PSLQ total = {cascade_emp_total:.2f} s")

    say("")
    say("Iteration-cost extrapolation (per precision):")
    rig_total = 0.0
    for P, _, p, _ in rows:
        iters = 2000
        iter_per_s = iters / p
        rig_s = 100000 / iter_per_s
        rig_total += rig_s
        say(f"  P={P}: {iter_per_s:6.0f} iter/s  =>  100k iter ~= {rig_s:8.1f} s = {rig_s/60:5.1f} min")
    say(f"  Rigorous-tier cascade (maxsteps=100k each) total = {rig_total:7.1f} s = {rig_total/60:5.1f} min")

    say("")
    say("=" * 78)
    say("Sweep arithmetic")
    say("=" * 78)
    budget_s = 96 * 3600
    say(f"  Budget (Brief §M3.2): 96h = {budget_s} s")

    n_primary = 1
    n_subbasis = 40
    primary_cost = n_primary * rig_total
    subbasis_cost = n_subbasis * cascade_emp_total
    total_cost = primary_cost + subbasis_cost
    margin = budget_s / total_cost if total_cost > 0 else float("inf")
    say("")
    say(f"  Sweep design (estimate, conservative):")
    say(f"    {n_primary:>3d} primary cascade (rigorous tier, n=15)  = {primary_cost:8.0f} s = {primary_cost/60:5.1f} min")
    say(f"    {n_subbasis:>3d} sub-basis cascades (empirical, n<15)    = {subbasis_cost:8.0f} s = {subbasis_cost/60:5.1f} min")
    say(f"    TOTAL                                          = {total_cost:8.0f} s = {total_cost/60:5.1f} min = {total_cost/3600:.2f} h")
    say("")
    say(f"  Budget margin = {budget_s} / {int(total_cost)} = {margin:.1f}x")
    if margin >= 3:
        say(f"  VERDICT: COMFORTABLE MARGIN ({margin:.1f}x >= 3x) -> proceed to M3.1 implementation")
    elif margin >= 2:
        say(f"  VERDICT: MODERATE MARGIN ({margin:.1f}x in [2x, 3x)) -> proceed but with caution")
    else:
        say(f"  VERDICT: TIGHT MARGIN ({margin:.1f}x < 2x) -> surface U-MISSION-M")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
