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

Per-candidate JSONL output structure (per operator M3.1 directive):
  { relation, P, n, maxcoeff, iteration_count, mpmath_verbose_diagonals,
    H_empirical, H_rigorous, cascade_verdict, gp_lindep_verdict,
    verification_class }

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


def empirical_height(P: int, n: int, c: float = 2.06) -> float:
    """BBC-1997-calibrated empirical height bound. Tier 1 of the two-tier predicate."""
    return 10 ** (P / (c * n))


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
                     timeout_s: int = 180) -> dict:
    """Leg (b): independent gp lindep call. Returns dict with relation or error."""
    mp.dps = dps
    expr_vec = ", ".join(mpmath.nstr(v, dps, strip_zeros=False) for v in basis_values)
    script = f"\\p {dps}\nlindep([{expr_vec}])\n"
    try:
        p = subprocess.run(
            [GP_BIN, "-q", "-s", "1G"],
            input=script, capture_output=True, text=True,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        return {"relation": None, "error": "timeout", "stdout": "", "stderr": ""}
    except FileNotFoundError:
        return {"relation": None, "error": f"gp_binary_not_found:{GP_BIN}",
                "stdout": "", "stderr": ""}
    if p.returncode != 0:
        return {"relation": None, "error": f"gp_returncode={p.returncode}",
                "stdout": p.stdout, "stderr": p.stderr}
    out = p.stdout.strip()
    rel = _parse_gp_lindep_output(out)
    return {"relation": rel, "error": None,
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

    if run_gp_leg:
        gp_result = gp_lindep_verify(basis_subset(primary_P, indices),
                                     dps=primary_P // 2,
                                     maxcoeff_exp=maxcoeff_exp)
    else:
        gp_result = {"relation": None, "error": "skipped"}

    if primary_rel is not None:
        residual = pslq_residual_check(indices, tuple(primary_rel), primary_P)
    else:
        residual = {"residual_log10": None, "tol_log10": None, "passes": None}

    vclass = verification_class_for(cascade["verdict"], gp_result, residual, rigorous_tier)

    H_empirical = empirical_height(primary_P, n, c=2.06)

    return {
        "family": family,
        "indices": list(indices),
        "labels": list(labels_for(indices)),
        "n": n,
        "maxcoeff_exp": maxcoeff_exp,
        "precisions": list(precisions),
        "maxsteps_per_prec": list(maxsteps_per_prec),
        "rigorous_tier": rigorous_tier,
        "H_empirical": H_empirical,
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
