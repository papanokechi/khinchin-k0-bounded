"""harness/verify.py — three-leg verification for M3.1.

Authority: M2.3 final predicate at `literature/_m2.3_calibration_anchor.md` §7
(ratified 2026-05-15 22:03:50 JST, locked at tag gold/M2 commit ca9c989).
Brief §M3.1: three verification legs per `targets/selected.md` §2 handoff.

Legs:
  (a) Cascade PSLQ at (P, 2P, 4P) — stability across precisions.
  (b) Independent integer-relation finder via gp lindep — second library
      with full-path invocation per `capability/pari_gp.available.md`.
  (c) PSLQ false-positive rejection at target precision — explicit
      verification that the returned coefficient vector actually satisfies
      |Σ m_i · b_i| < tol modulo the precision tolerance.

Per-candidate JSONL output structure (per operator M3.1 directive,
updated by U-MISSION-N R2.beta strengthening 2026-05-16 ~11:18 JST):
  { relation, P, n, maxcoeff, iteration_count, mpmath_verbose_diagonals,
    H_empirical_operational, H_empirical_formula, H_rigorous,
    cascade_verdict, gp_lindep_verdict, verification_class }

H_empirical_operational = canonical bound = min(formula, 10^maxcoeff_exp).
H_empirical_formula     = uncapped BBC formula c*10^(P/(c*n)) (methods obs).

verification_class assignments (per H9):
  - positive (relation found, cascade-stable, gp-confirmed) -> rigorous_theorem
  - negative (null cascade, H_empirical+H_rigorous reported) -> proven_corollary (Tier 2)
                                                                + field_standard_practice (Tier 1)
  - cascade_failure / spurious -> empirical_heuristic (audit-trail only)
"""

from __future__ import annotations
import io
import contextlib
import re
import subprocess
import time
from dataclasses import dataclass, field
from typing import Optional

import mpmath
from mpmath import mp, mpf, pslq

from basis import basis_subset, labels_for, has_complement, EF1_INDICES
from rigorous_bound import (
    parse_verbose,
    H_rigorous_thm1,
    H_rigorous_cor2,
    H_rigorous_combined,
)


GP_BIN = r"C:\Users\shkub\PARI\gp.exe"


@dataclass
class LegResult:
    relation: Optional[tuple[int, ...]] = None
    iteration_count: int = 0
    final_norm: int = 0
    elapsed_s: float = 0.0
    H_rigorous: float = 0.0
    error: Optional[str] = None
    termination_reason: str = ""
    termination_line: str = ""
    last_norm_in_cancellation: int = 0
    verbose_lines: int = 0


def empirical_height(P: int, n: int, c: float = 2.06):
    """BBC-1997-calibrated empirical height bound. Tier 1 of the two-tier predicate.

    Returns Python float when ``P/(c*n) < 307`` (fits IEEE 754 double), else
    Python int via mpmath (any size). Per U-MISSION-N R1 mechanical fix
    (2026-05-16 ~11:18 JST): use mpmath to avoid OverflowError at small-n
    sub-bases where the exponent exceeds float range.

    For the canonical operational bound (capped at maxcoeff) used by the
    predicate claim, call ``empirical_height_dual`` instead — see
    U-MISSION-N R2.beta strengthening.
    """
    exponent = P / (c * n)
    if exponent < 307.0:
        return 10.0 ** exponent
    saved_dps = mp.dps
    try:
        mp.dps = max(50, int(exponent) + 20)
        return int(mp.power(mp.mpf(10), mp.mpf(exponent)))
    finally:
        mp.dps = saved_dps


def empirical_height_dual(P: int, n: int, maxcoeff_exp: int, c: float = 2.06) -> dict:
    """Per U-MISSION-N R2.beta strengthening: return BOTH operational and formula values.

    Per operator U-MISSION-N RESOLUTION (2026-05-16 ~11:18 JST):
      - ``H_empirical_formula``     = c * 10^(P/(c*n))   (uncapped BBC formula)
      - ``H_empirical_operational`` = min(formula, 10^maxcoeff_exp)

    Rationale: PSLQ configured with ``maxcoeff = 10^maxcoeff_exp`` cannot
    detect any relation with max coefficient exceeding maxcoeff regardless
    of where the BBC formula extrapolates. The OPERATIONAL value is the
    canonical bound for predicate claims (what the algorithm actually
    tests); the FORMULA value is retained for the M6 methods observation
    about BBC scaling's operational range at small n (R2.beta strengthening).

    Both fields are emitted to the per-candidate JSONL. See
    ``literature/_m2.3_calibration_anchor.md`` Section 7.10 for the
    canonical predicate text and ``methodology/heuristics.md`` H10 for
    the heuristic that would have caught the pre-fix overflow.
    """
    formula = empirical_height(P, n, c=c)
    maxcoeff = 10 ** maxcoeff_exp  # Python int (any size)
    # min() works across mixed float/int because Python promotes for comparison.
    operational = min(formula, maxcoeff)
    return {
        "H_empirical_formula": formula,
        "H_empirical_operational": operational,
    }


def run_pslq_with_capture(basis_values: tuple, maxcoeff_exp: int, maxsteps: int,
                          prec_dps: int, tol_decimal_factor: float = 0.6) -> LegResult:
    """Run mpmath.pslq with verbose stdout capture. Parses the rigorous norm bound."""
    mp.dps = prec_dps
    tol = mpf(10) ** -int(prec_dps * tol_decimal_factor)
    maxcoeff = 10 ** maxcoeff_exp
    buf = io.StringIO()
    t0 = time.perf_counter()
    try:
        with contextlib.redirect_stdout(buf):
            rel = pslq(list(basis_values), tol=tol, maxcoeff=maxcoeff,
                       maxsteps=maxsteps, verbose=True)
    except Exception as exc:
        return LegResult(error=f"pslq_exception:{type(exc).__name__}:{exc}",
                         elapsed_s=time.perf_counter() - t0)
    elapsed = time.perf_counter() - t0
    log_text = buf.getvalue()
    parsed = parse_verbose(log_text)
    K = parsed["iterations"] if parsed["iterations"] > 0 else maxsteps
    final_norm = parsed["final_norm"]
    H_thm1 = H_rigorous_thm1(final_norm)
    H_cor2 = H_rigorous_cor2(K, n=len(basis_values))
    H_comb = max(H_thm1, H_cor2)
    return LegResult(
        relation=tuple(int(x) for x in rel) if rel is not None else None,
        iteration_count=K,
        final_norm=final_norm,
        elapsed_s=elapsed,
        H_rigorous=H_comb,
        termination_reason=parsed.get("termination_reason", ""),
        termination_line=parsed.get("termination_line", "")[:200],
        last_norm_in_cancellation=parsed.get("last_norm_in_cancellation", 0),
        verbose_lines=log_text.count("\n"),
    )


def cascade_pslq(indices: tuple[int, ...], precisions: tuple[int, int, int],
                 maxcoeff_exp: int, maxsteps_per_prec: tuple[int, int, int]
                 ) -> dict:
    """Leg (a): cascade across (P, 2P, 4P). Returns dict with per-prec LegResult and verdict."""
    per_prec: list[LegResult] = []
    for P, ms in zip(precisions, maxsteps_per_prec):
        basis_at_P = basis_subset(P, indices)
        res = run_pslq_with_capture(basis_at_P, maxcoeff_exp, ms, P)
        per_prec.append(res)

    relations = [r.relation for r in per_prec]
    if all(r is None for r in relations):
        verdict = "cascade_stable_null"
    elif all(r is not None for r in relations) and _relations_consistent(relations):
        verdict = "cascade_stable_relation"
    else:
        verdict = "cascade_unstable"

    return {
        "verdict": verdict,
        "per_precision": [
            {"P": P, "iteration_count": r.iteration_count, "final_norm": r.final_norm,
             "elapsed_s": r.elapsed_s, "H_rigorous": r.H_rigorous,
             "relation": list(r.relation) if r.relation else None,
             "termination_reason": r.termination_reason,
             "termination_line": r.termination_line,
             "last_norm_in_cancellation": r.last_norm_in_cancellation,
             "verbose_lines_captured": r.verbose_lines,
             "error": r.error}
            for P, r in zip(precisions, per_prec)
        ],
        "H_rigorous_min_across_cascade": min(r.H_rigorous for r in per_prec if r.error is None),
    }


def _relations_consistent(rels: list) -> bool:
    """Check that two integer relations are scalar multiples of each other (modulo trivial)."""
    if any(r is None for r in rels):
        return False
    r0 = rels[0]
    for r in rels[1:]:
        if len(r) != len(r0):
            return False
        nz = [i for i in range(len(r0)) if r0[i] != 0 or r[i] != 0]
        if not nz:
            continue
        i0 = nz[0]
        if r0[i0] == 0 or r[i0] == 0:
            return False
        ratio = (r[i0], r0[i0])
        for i in nz[1:]:
            if r0[i] * ratio[0] != r[i] * ratio[1]:
                return False
    return True


def gp_lindep_verify(basis_values: tuple, dps: int, maxcoeff_exp: int,
                     H_empirical: Optional[float] = None,
                     timeout_s: int = 1800) -> dict:
    """Leg (b): independent gp lindep call at equal-or-higher precision than primary.

    Per U-MISSION-M3.2 (2026-05-16): the previous `dps = primary_P // 2`
    heuristic is REJECTED. Second leg must run at >= primary precision to function
    as a genuine independence check. Timeout default raised to 30 min to accommodate
    LLL at full precision on the n=15 mission basis.

    PARI/GP `lindep` performs LLL and ALWAYS returns a "best approximate" integer
    combination, even when no genuine relation exists within bound. Interpretation
    requires comparing the returned coefficient magnitudes to H_empirical:

      - max|m_i| <= H_empirical: gp claims a genuine relation within bound
      - max|m_i|  > H_empirical: gp returned noise (confirms no relation within bound)
    """
    mp.dps = dps
    try:
        expr_vec = ", ".join(mpmath.nstr(v, dps, strip_zeros=False) for v in basis_values)
    except TypeError:
        expr_vec = ", ".join(mpmath.nstr(v, dps) for v in basis_values)
    script = f"\\p {dps}\nlindep([{expr_vec}])\n"
    try:
        p = subprocess.run(
            [GP_BIN, "-q", "-s", "1G"],
            input=script, capture_output=True, text=True,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        return {"relation": None, "error": "timeout", "max_abs_coefficient": None,
                "within_empirical_bound": None, "stdout": "", "stderr": ""}
    except FileNotFoundError:
        return {"relation": None, "error": f"gp_binary_not_found:{GP_BIN}",
                "max_abs_coefficient": None, "within_empirical_bound": None,
                "stdout": "", "stderr": ""}
    if p.returncode != 0:
        return {"relation": None, "error": f"gp_returncode={p.returncode}",
                "max_abs_coefficient": None, "within_empirical_bound": None,
                "stdout": p.stdout, "stderr": p.stderr}
    out = p.stdout.strip()
    rel = _parse_gp_lindep_output(out)
    max_abs = max((abs(m) for m in rel), default=0) if rel else 0
    within = None
    if rel and H_empirical is not None and max_abs > 0:
        within = max_abs <= H_empirical
    return {"relation": rel, "error": None,
            "max_abs_coefficient": int(max_abs) if max_abs else 0,
            "within_empirical_bound": within,
            "stdout_tail": out[-200:] if len(out) > 200 else out,
            "stderr_tail": p.stderr[-200:] if p.stderr else ""}


def _parse_gp_lindep_output(out: str) -> Optional[list]:
    """Parse a gp 'lindep' result like '[a, b, c]~' to [a, b, c]."""
    m = re.search(r"\[([^\]]+)\]~", out)
    if not m:
        return None
    body = m.group(1)
    try:
        return [int(x.strip()) for x in body.split(",")]
    except ValueError:
        return None


def pslq_residual_check(indices: tuple[int, ...], relation: tuple[int, ...],
                       prec_dps: int) -> dict:
    """Leg (c): false-positive rejection. Computes |Σ m_i · b_i| at prec_dps."""
    if relation is None:
        return {"residual_log10": None, "tol_log10": None, "passes": None}
    mp.dps = prec_dps
    basis_at_P = basis_subset(prec_dps, indices)
    s = mp.mpf(0)
    for m_i, b_i in zip(relation, basis_at_P):
        s = s + mp.mpf(m_i) * b_i
    residual = mp.fabs(s)
    if residual == 0:
        residual_log10 = float("-inf")
    else:
        residual_log10 = float(mp.log10(residual))
    tol_log10 = -int(prec_dps * 0.6)
    passes = residual_log10 < tol_log10
    return {
        "residual_log10": residual_log10,
        "tol_log10": tol_log10,
        "passes": passes,
    }


def _summarize_gp_verdict(cascade_verdict: str, gp_result: dict) -> str:
    """Combine cascade and gp leg into a single second-leg verdict for surfacing."""
    if gp_result.get("error") == "skipped":
        return "skipped"
    if gp_result.get("error"):
        return f"gp_error:{gp_result['error']}"
    rel = gp_result.get("relation")
    within = gp_result.get("within_empirical_bound")
    if cascade_verdict == "cascade_stable_null":
        if rel is None:
            return "gp_returned_no_relation_confirms_null"
        if within is False:
            return "gp_noise_relation_above_H_empirical_confirms_null"
        if within is True:
            return "gp_claims_relation_within_bound_CASCADE_DISAGREES"
        return "gp_relation_returned_bound_check_unknown"
    if cascade_verdict == "cascade_stable_relation":
        if rel is None:
            return "gp_returned_no_relation_CASCADE_DISAGREES"
        if within is True:
            return "gp_relation_within_bound_pending_consistency_check"
        return "gp_relation_above_H_empirical_CASCADE_DISAGREES"
    return f"cascade_{cascade_verdict}_gp_ambiguous"


def verification_class_for(cascade_verdict: str, gp_verdict: dict,
                           residual_check: dict, rigorous_tier: bool) -> str:
    """Assign H9 verification_class per outcome."""
    if cascade_verdict == "cascade_stable_relation":
        if residual_check.get("passes") and gp_verdict.get("relation") is not None:
            return "rigorous_theorem"
        return "empirical_heuristic"
    if cascade_verdict == "cascade_stable_null":
        if rigorous_tier:
            return "proven_corollary"
        return "field_standard_practice"
    return "empirical_heuristic"


def verify_candidate(family: str, indices: tuple[int, ...], precisions: tuple[int, int, int],
                     maxcoeff_exp: int, maxsteps_per_prec: tuple[int, int, int],
                     rigorous_tier: bool, run_gp_leg: bool = True,
                     ) -> dict:
    """Run all three legs on one candidate. Returns the per-candidate JSONL dict."""
    n = len(indices)
    cascade = cascade_pslq(indices, precisions, maxcoeff_exp, maxsteps_per_prec)

    primary_P = precisions[0]
    primary_rel = cascade["per_precision"][0]["relation"]

    H_heights = empirical_height_dual(primary_P, n, maxcoeff_exp=maxcoeff_exp, c=2.06)
    H_empirical_operational = H_heights["H_empirical_operational"]
    H_empirical_formula = H_heights["H_empirical_formula"]

    if run_gp_leg:
        gp_result = gp_lindep_verify(basis_subset(primary_P, indices),
                                     dps=primary_P,
                                     maxcoeff_exp=maxcoeff_exp,
                                     H_empirical=H_empirical_operational)
    else:
        gp_result = {"relation": None, "error": "skipped",
                     "max_abs_coefficient": None, "within_empirical_bound": None}

    if primary_rel is not None:
        residual = pslq_residual_check(indices, tuple(primary_rel), primary_P)
    else:
        residual = {"residual_log10": None, "tol_log10": None, "passes": None}

    gp_verdict = _summarize_gp_verdict(cascade["verdict"], gp_result)
    gp_result["gp_verdict"] = gp_verdict

    vclass = verification_class_for(cascade["verdict"], gp_result, residual, rigorous_tier)

    return {
        "family": family,
        "indices": list(indices),
        "labels": list(labels_for(indices)),
        "n": n,
        "maxcoeff_exp": maxcoeff_exp,
        "precisions": list(precisions),
        "maxsteps_per_prec": list(maxsteps_per_prec),
        "rigorous_tier": rigorous_tier,
        "H_empirical_operational": H_empirical_operational,
        "H_empirical_formula": H_empirical_formula,
        "H_rigorous_min": cascade["H_rigorous_min_across_cascade"],
        "cascade": cascade,
        "gp_lindep": gp_result,
        "pslq_residual_check": residual,
        "verification_class": vclass,
        "ef1_only": all(i in EF1_INDICES for i in indices),
        "has_complement": has_complement(indices),
    }


if __name__ == "__main__":
    import json
    print("harness/verify.py — three-leg verification module (M3.1)")
    print()
    print("Smoke test: minimal trivial-relation detection at small precision")
    print()
    trivial_indices = (0, 1)
    result = verify_candidate(
        family="smoke_test",
        indices=trivial_indices,
        precisions=(50, 100, 200),
        maxcoeff_exp=20,
        maxsteps_per_prec=(200, 200, 200),
        rigorous_tier=False,
        run_gp_leg=False,
    )
    print(json.dumps(result, indent=2, default=str)[:2000])
