"""
harness/rigorous_bound.py — Rigorous M_x lower bound from mpmath.pslq verbose outputs.

Per U-MISSION-L (operator 2026-05-15 ~21:36 JST):
    "Investigate FBA Theorem 1 + Corollary 2 yield given only the outputs mpmath.pslq
    actually exposes. Produce harness/rigorous_bound.py with the derivation. If the
    rigorous bound is meaningfully better than trivial (e.g., H_rigorous >= 10^10),
    include in the two-tier predicate. If the rigorous bound is trivial or zero,
    report honestly and the M6 manuscript becomes empirical-only — but with the
    investigation documented as a contribution attempt."

----------------------------------------------------------------------------------
FINDING — the rigorous bound IS meaningfully available from mpmath outputs.
----------------------------------------------------------------------------------

Inspection of `mpmath.identification.pslq` source (mpmath 1.3.0) reveals that
mpmath internally maintains a Theorem-1-style lower bound on M_x:

    recnorm = max(abs(h) for h in H.values())          # max over ALL entries of H
    norm = ((1 << (2*prec)) // recnorm) >> prec        # = floor(1 / max|H|)
    norm //= 100                                       # 100x safety factor
    ...
    if verbose:
        print("%i/%i:  Error: %s   Norm: %i" % (REP, maxsteps, ..., norm))
    ...
    if norm >= maxcoeff:
        break

The reported `norm` is printed at every iteration in verbose=True mode, and is
captureable via stdout redirection (see `run_pslq_capture()` below).

By FBA-1999 Theorem 1 (M_x >= 1 / max_j |h_{j,j}|) combined with the elementary
inequality `max_{i,j} |H[i,j]| >= max_j |h_{j,j}|`, we have:

    M_x  >=  1 / max_j |h_{j,j}|  >=  1 / max_{i,j} |H[i,j]|

mpmath's reported `norm = floor(1 / max|H|) // 100`, so:

    100 * reported_norm  <=  1 / max|H|  <=  M_x

i.e., **M_x >= 100 * reported_norm** is rigorously guaranteed by FBA 1999 Theorem 1
(modulo the 4 divergences listed below).

This is the rigorous-tier H_rigorous derivation that the two-tier M2.3 predicate
will use.

----------------------------------------------------------------------------------
4 divergences from FBA 1999 — flagged for operator transparency.
----------------------------------------------------------------------------------

D1. max-over-all-entries vs max-over-diagonal-only.
    mpmath uses max_{i,j} |H[i,j]| over ALL entries; FBA 1999 Theorem 1 states
    max_j |h_{j,j}| over the diagonal only. Since |H[i,j]| >= 0 and max over more
    elements >= max over fewer, max|H| >= max|h_{j,j}|, so 1/max|H| <= 1/max|h_{j,j}|.
    mpmath's bound is **rigorous but strictly weaker than FBA T1's optimal form**.
    Practical impact: H_rigorous from mpmath is at most equal to (and typically
    several decades smaller than) the optimal FBA T1 bound from the same H matrix.

D2. gamma = sqrt(4/3) exact vs gamma > sqrt(4/3) strict.
    mpmath uses g = sqrt(4/3) exactly (line `g = sqrt_fixed((4<<prec)//3, prec)`);
    FBA 1999 Definition 5 specifies gamma > sqrt(4/3) STRICT for the real case
    Theorem-3 conclusion. The boundary case is treated in Bailey 1998 expository
    paper (mpmath's stated source per docstring), where gamma = sqrt(4/3) is the
    OPTIMAL choice. **Practical impact: rigorous-tier predicate citing Theorem 3
    overshoot would need Bailey-1998 H8 paper-read.** Theorem 1 and Corollary 2
    are unaffected by this boundary distinction (they use gamma >= sqrt(4/3) only
    via Lemma 8, which holds at the boundary by continuity of the bound).
    **STATUS (2026-05-16 ~19:50 JST, stage-2 paper-read refinement): D2
    cleared by paper-read on Bailey 1998 §2 (lit-010). FBA 1999 §3-§4 does
    not contain a continuity argument; T2's proof requires τ > 1 strictly
    per Lemma 9. Boundary clearance for the iteration-count contrapositive
    is provided by Bailey 1998's γ-range-independent re-presentation, not
    by FBA continuity. See literature/_fidelity_findings.md §8.1 and
    lit-009 §9 boundary-case scope note.**

D3. mpmath cites Bailey 1998, NOT FBA 1999.
    mpmath docstring: "This is a fairly direct translation to Python of the
    pseudocode given by David Bailey, 'The PSLQ Integer Relation Algorithm':
    http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html"
    Bailey 1998 is an expository re-presentation of FBA 1992/1999; treating
    mpmath's bound as "FBA-1999-derived" requires either (a) verifying Bailey
    1998 preserves the FBA T1 / Cor 2 statements (HIGH a-priori confidence —
    Bailey was a coauthor of FBA 1999 and the 1998 paper is canonical PSLQ
    pedagogy), or (b) treating Bailey 1998 as the operative source. The
    rigorous-tier predicate is most defensible if Bailey 1998 enters the
    H8 dependency chain via paper-read. **Forward-flagged: Bailey 1998 H8
    paper-read recommended before M3.1 harness implementation if rigorous tier
    is load-bearing in the M2.3 predicate.**
    **STATUS (2026-05-16 ~15:55 JST): CLEARED per H8 paper-read on Bailey 1998
    (lit-010 upgraded fidelity_watch -> verified). Algorithm chain
    mpmath -> Bailey 1998 §2 -> FBA 1999 verified structurally consistent;
    Bailey 1998 §2 pseudocode Step 5 norm-bound certificate is equivalent to
    FBA 1999 Theorem 1 in conservative form. See
    literature/_fidelity_findings.md §8.2.**

D4. 100x integer-division safety factor.
    mpmath applies `norm //= 100` after computing 1/max|H|. This integer-division
    truncation has two effects: (i) the reported norm is always a strict lower
    bound on the FBA T1 bound (conservative — does not harm rigor); (ii) for early
    iterations when 1/max|H| is small (e.g., between 1 and 99), the reported norm
    is 0, which under-reports the FBA T1 certificate. **Practical impact: the
    rigorous bound from mpmath is `H_rigorous = 100 * reported_norm`, which is
    rigorous for all reported_norm > 0 and uninformative for reported_norm = 0.**

----------------------------------------------------------------------------------
Corollary 2 (FBA 1999) iteration-based bound — independent check.
----------------------------------------------------------------------------------

FBA 1999 Corollary 2 (page 14, verbatim): "PSLQ(tau) will construct some O(K)^n
relation for x in no more than 2 * (dim_R K) * (n^3 + n^2 log M_x) iterations."

Contrapositive: If PSLQ ran K iterations without termination, then any relation
that exists has

    M_x  >  exp( (K - 2 * dim_R * n^3) / (2 * dim_R * n^2) )

For the real case (dim_R = 1):

    M_x_lb_cor2(K, n)  =  exp( (K - 2*n^3) / (2*n^2) )

This gives a second, independent rigorous lower bound on M_x using iteration
count alone (no H-matrix internals). For n = 15:

    K_critical(M_x = 1)        =  2*n^3              =  6,750 iterations
    K_critical(M_x = 10^10)    =  2*n^3 + 2*n^2*23  =  17,100 iterations
    K_critical(M_x = 10^70)    =  2*n^3 + 2*n^2*161 =  79,200 iterations

Both bounds (Theorem 1 via norm, Corollary 2 via K) are rigorous lower bounds on
M_x; the M2.3 predicate uses MAX of the two.

----------------------------------------------------------------------------------
Public API.
----------------------------------------------------------------------------------
"""
from __future__ import annotations

import io
import contextlib
import math
import re
from dataclasses import dataclass
from typing import Optional

import mpmath
from mpmath import mp, mpf, pslq


VERIFICATION_CLASSES = (
    "rigorous_theorem",
    "proven_corollary",
    "field_standard_practice",
    "empirical_heuristic",
)


@dataclass
class PSLQRun:
    """Captured outputs of a verbose mpmath.pslq invocation."""
    n: int
    dps: int
    maxcoeff: int
    maxsteps: int
    iterations: int                  # K — PSLQ main-loop iteration count at termination
    final_norm: int                  # mpmath's reported "Norm" at termination
    relation: Optional[list]         # the relation if found, else None
    termination_reason: str          # 'relation_found' | 'norm_exceeds_maxcoeff' |
                                     # 'maxsteps_reached' | 'precision_exhausted'
    elapsed_seconds: float
    verbose_lines: int               # for evidence trail


# -------------------------------------------------------------------------- core


def H_rigorous_thm1(reported_norm: int) -> int:
    """FBA-1999 Theorem 1 rigorous lower bound on M_x, derived from mpmath's
    reported norm (accounting for the 100x safety factor in mpmath's internal
    division — see divergence D4 in module docstring).

    Returns 100 * reported_norm. M_x >= H_rigorous_thm1(reported_norm) is
    rigorously guaranteed by FBA 1999 Theorem 1 (modulo divergences D1-D4).
    """
    if reported_norm < 0:
        raise ValueError(f"reported_norm must be non-negative; got {reported_norm}")
    return 100 * reported_norm


def H_rigorous_cor2(K: int, n: int, dim_R: int = 1) -> mpf:
    """FBA-1999 Corollary 2 rigorous lower bound on M_x, derived from PSLQ
    iteration count K and basis dimension n. Real case has dim_R = 1; complex
    case has dim_R = 2 (Corollary 2 verbatim p. 14).

    Returns exp( (K - 2*dim_R*n^3) / (2*dim_R*n^2) ).
    Result is the rigorous lower bound on M_x assuming PSLQ ran K iterations
    without finding a relation. Returns 0 (or float < 1) when K is too small
    for a non-trivial integer-relation bound.
    """
    if K < 0:
        raise ValueError(f"K must be non-negative; got {K}")
    if n < 2:
        raise ValueError(f"n must be >= 2; got {n}")
    exponent_num = K - 2 * dim_R * (n ** 3)
    exponent_den = 2 * dim_R * (n ** 2)
    with mp.workdps(50):
        return mpmath.exp(mpf(exponent_num) / mpf(exponent_den))


def H_rigorous_combined(reported_norm: int, K: int, n: int, dim_R: int = 1) -> mpf:
    """Combined rigorous lower bound = max(Thm1-derived, Cor2-derived). Both
    bounds are rigorous; the M2.3 predicate uses their maximum."""
    h1 = mpf(H_rigorous_thm1(reported_norm))
    h2 = H_rigorous_cor2(K, n, dim_R)
    return mpmath.mpf(max(h1, h2))


def K_critical_for_M_x(M_x_target: float, n: int, dim_R: int = 1) -> int:
    """Inverse of H_rigorous_cor2: how many iterations K are required for FBA
    Corollary 2 to certify M_x >= M_x_target? Useful for M3.1 budget planning."""
    if M_x_target < 1:
        return 2 * dim_R * (n ** 3)
    return int(math.ceil(2 * dim_R * ((n ** 3) + (n ** 2) * math.log(M_x_target))))


# --------------------------------------------------------------------- parsers


_VERBOSE_ITER_LINE = re.compile(
    r"(\d+)/(\d+):\s+Error:\s+(\S+)\s+Norm:\s+(\d+)"
)


def parse_verbose(verbose_text: str) -> dict:
    """Parse mpmath.pslq verbose=True stdout into structured data.

    Returns dict with keys:
        - 'iterations': K (last iteration index seen + 1; matches mpmath internal counting)
        - 'final_norm': int (mpmath's reported Norm at final printed iteration)
        - 'termination_line': str (the final "FOUND" or "CANCELLING" line)
        - 'termination_reason': enum string
        - 'last_norm_in_cancellation': int (parsed from "Norm bound:" line if present)
    """
    last_iter = -1
    last_norm = 0
    termination_line = ""
    termination_reason = "unknown"
    last_norm_cancel = None

    for line in verbose_text.splitlines():
        m = _VERBOSE_ITER_LINE.match(line)
        if m:
            last_iter = int(m.group(1))
            last_norm = int(m.group(4))
            continue
        if line.startswith("FOUND"):
            termination_line = line
            termination_reason = "relation_found"
        elif line.startswith("CANCELLING"):
            termination_line = line
            termination_reason = "maxsteps_or_norm_break"
        elif "Norm bound:" in line:
            mm = re.search(r"Norm bound:\s+(-?\d+)", line)
            if mm:
                last_norm_cancel = int(mm.group(1))
                if last_norm_cancel >= 0:
                    last_norm = last_norm_cancel

    return {
        "iterations": last_iter + 1,
        "final_norm": last_norm,
        "termination_line": termination_line,
        "termination_reason": termination_reason,
        "last_norm_in_cancellation": last_norm_cancel,
    }


# --------------------------------------------------------------------- runner


def run_pslq_capture(basis, *, maxcoeff: int, maxsteps: int, dps: int) -> PSLQRun:
    """Run mpmath.pslq with verbose=True and capture stdout. Returns PSLQRun."""
    import time

    n = len(basis)
    old_dps = mp.dps
    try:
        mp.dps = dps
        # Ensure all elements are at current precision
        basis_at_prec = [mpf(b) if not isinstance(b, type(mpf(1))) else b for b in basis]
        buf = io.StringIO()
        t0 = time.time()
        with contextlib.redirect_stdout(buf):
            relation = pslq(basis_at_prec, maxcoeff=maxcoeff,
                            maxsteps=maxsteps, verbose=True)
        elapsed = time.time() - t0
        out = buf.getvalue()
        parsed = parse_verbose(out)

        if relation is not None:
            term_reason = "relation_found"
        elif parsed["iterations"] >= maxsteps:
            term_reason = "maxsteps_reached"
        elif parsed["final_norm"] * 100 >= maxcoeff:
            term_reason = "norm_exceeds_maxcoeff"
        else:
            term_reason = "precision_exhausted"

        return PSLQRun(
            n=n, dps=dps, maxcoeff=maxcoeff, maxsteps=maxsteps,
            iterations=parsed["iterations"],
            final_norm=parsed["final_norm"],
            relation=relation,
            termination_reason=term_reason,
            elapsed_seconds=elapsed,
            verbose_lines=len(out.splitlines()),
        )
    finally:
        mp.dps = old_dps


# --------------------------------------------------------------------- demo


def _bench_mission_basis(dps: int, maxsteps: int, maxcoeff_exp: int = 60) -> PSLQRun:
    """Construct the M3.1 mission basis B_D(C) and run PSLQ at given precision."""
    mp.dps = dps
    K0 = mpmath.khinchin(dps=dps)
    basis = [mpf(1)]
    for k in range(1, 7):
        basis.append(K0 ** k)
    basis.append(mpmath.log(K0))
    cset = [mpmath.pi, mpmath.e, mpmath.log(2), mpmath.euler,
            mpmath.zeta(2), mpmath.zeta(3), mpmath.catalan]
    for c in cset:
        basis.append(K0 * c)
    assert len(basis) == 15
    return run_pslq_capture(basis,
                            maxcoeff=10 ** maxcoeff_exp,
                            maxsteps=maxsteps,
                            dps=dps)


def _print_run(run: PSLQRun, label: str = "") -> None:
    h1 = H_rigorous_thm1(run.final_norm)
    h2 = H_rigorous_cor2(run.iterations, run.n)
    print(f"=== {label or 'pslq run'} ===")
    print(f"  n={run.n}, dps={run.dps}, maxcoeff=10^{int(math.log10(run.maxcoeff))}, "
          f"maxsteps={run.maxsteps}")
    print(f"  iterations(K) = {run.iterations}, final_norm = {run.final_norm}, "
          f"relation = {'FOUND' if run.relation else 'None'}")
    print(f"  termination_reason = {run.termination_reason}, "
          f"elapsed = {run.elapsed_seconds:.2f}s")
    print(f"  H_rigorous(Thm1)  = 100 * {run.final_norm} = {h1} "
          f"(log10 = {math.log10(h1) if h1 > 0 else float('-inf'):.3f})")
    if h2 > 1:
        print(f"  H_rigorous(Cor2)  = exp(({run.iterations} - 2*{run.n}^3)/(2*{run.n}^2)) "
              f"= {mpmath.nstr(h2, 5)} (log10 = {float(mpmath.log10(h2)):.3f})")
    else:
        print(f"  H_rigorous(Cor2)  = trivial (K = {run.iterations} < K_critical = "
              f"{K_critical_for_M_x(1, run.n)})")
    h_combined = mpf(max(h1, float(h2) if h2 < 1e308 else float('inf')))
    print(f"  H_rigorous(combined) = max(Thm1, Cor2) = {mpmath.nstr(h_combined, 5)}")


def demo() -> None:
    """Demonstration of rigorous-bound extraction at three precisions for the
    mission basis B_D(C) at n=15. This is M2.3-scale evidence; the M3.1 harness
    runs the full sweep."""

    print("=" * 78)
    print("harness/rigorous_bound.py demo — M2.3 evidence pass")
    print("FBA-1999 rigorous M_x lower bound via mpmath.pslq verbose outputs")
    print("=" * 78)
    print()

    print(f"K_critical_for_M_x(1, n=15)       = {K_critical_for_M_x(1, 15)} iter")
    print(f"K_critical_for_M_x(10^10, n=15)   = {K_critical_for_M_x(1e10, 15)} iter")
    print(f"K_critical_for_M_x(10^60, n=15)   = {K_critical_for_M_x(1e60, 15)} iter")
    print(f"K_critical_for_M_x(10^70, n=15)   = {K_critical_for_M_x(1e70, 15)} iter")
    print()

    for dps, maxsteps in [(100, 2000), (500, 2000), (500, 5000)]:
        run = _bench_mission_basis(dps=dps, maxsteps=maxsteps)
        _print_run(run, label=f"dps={dps} maxsteps={maxsteps}")
        print()


if __name__ == "__main__":
    demo()
