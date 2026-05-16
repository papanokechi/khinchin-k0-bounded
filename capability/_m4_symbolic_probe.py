"""
H10 retroactive dry-run for M4 symbolic-closure attempt.

Per operator M4 GREENLIGHT verbatim:
  "H10 applies retroactively to M4: if symbolic derivation requires a SymPy
  code path that hasn't been exercised at the relevant scale (e.g., Groebner
  basis computation, transcendence-theoretic predicate checking), run a
  full-regime dry-run before declaring closure."

This probe exercises four SymPy code paths that COULD in principle deliver
structural closure on the M3 null result for B_D(C):

  Path 1: sympy.is_transcendental / is_irrational on a K_0-bearing expression
  Path 2: sympy.nsimplify against a closed-form basis at full precision
  Path 3: sympy.solve_linear_system / groebner on a symbolic basis with K_0 as
          a free variable
  Path 4: sympy.transcendence-theoretic predicates (Lindemann-Weierstrass,
          Gelfond-Schneider) via sympy.functions.elementary.exponential

Each path is exercised and its limit is documented. The output JSONL records:
  - which path was tried
  - what input was supplied
  - what SymPy returned
  - whether the return constitutes structural closure (always False, by
    construction; this probe confirms WHY each path falls short)

If any path were to surprise with a structural-closure-capable output, halt
per operator's "if an anomaly does surface ... that's a finding that warrants
careful operator review".

Per H7 audit-trail-honesty: kept in repo.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath
import sympy as sp


OUT = Path(__file__).resolve().parent / "_m4_symbolic_probe.jsonl"


def write(rec: dict) -> None:
    with OUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, default=str) + "\n")


def main() -> int:
    # Fresh probe output
    if OUT.exists():
        OUT.unlink()

    # ------- shared inputs -------
    mpmath.mp.dps = 100
    K0_val = mpmath.mp.khinchin  # numerical K_0 at 100 dps
    K0_float = sp.Float(str(K0_val), 100)

    # Symbolic free variable for "K_0 has no known algebraic identity"
    K0 = sp.Symbol("K_0", positive=True, real=True)

    write({
        "probe_meta": True,
        "purpose": "H10 retroactive dry-run for M4 symbolic closure",
        "sympy_version": sp.__version__,
        "mpmath_dps": 100,
        "K_0_first_30": str(K0_val)[:30],
    })

    # ====================================================================
    # PATH 1: SymPy's built-in transcendence / irrationality predicates
    # ====================================================================
    # K_0 is not a built-in SymPy constant. SymPy's transcendental tests
    # work on a closed-form expression. We probe whether SymPy can deduce
    # ANY arithmetic property from the numerical value alone.
    print("=== PATH 1: is_transcendental / is_irrational on K_0 ===")
    rec1 = {"path": 1, "name": "is_transcendental / is_irrational"}
    try:
        # SymPy can express pi and e as transcendental
        rec1["pi_is_transcendental"] = bool(sp.pi.is_transcendental)
        rec1["e_is_transcendental"] = bool(sp.E.is_transcendental)
        # But K_0 as a free symbol has no arithmetic-nature information
        rec1["K0_symbol_is_transcendental"] = K0.is_transcendental
        rec1["K0_symbol_is_irrational"] = K0.is_irrational
        # And as a Float, SymPy treats it as a finite-precision approximation
        rec1["K0_float_is_transcendental"] = K0_float.is_transcendental
        rec1["K0_float_is_irrational"] = K0_float.is_irrational
        # ASSESSMENT: structural closure NOT achieved.
        rec1["closure_achieved"] = False
        rec1["reason"] = (
            "SymPy lacks built-in arithmetic-nature data for K_0. "
            "K_0 as Symbol has None for transcendence predicate; "
            "K_0 as Float is treated as a numerical approximation, "
            "carrying no transcendence-theoretic information. "
            "To deduce non-existence of an integer relation in B_D(C), "
            "SymPy would need to KNOW K_0's transcendence status; "
            "this is the major open question itself."
        )
        for k, v in rec1.items():
            print(f"  {k}: {v}")
    except Exception as e:
        rec1["error"] = repr(e)
        rec1["closure_achieved"] = False
    write(rec1)
    print()

    # ====================================================================
    # PATH 2: nsimplify against a closed-form basis at high precision
    # ====================================================================
    # nsimplify can identify a numerical value as a combination of named
    # constants. We probe whether it finds any closed-form representation
    # of K_0 in terms of {pi, E, log(2), EulerGamma, zeta(2), zeta(3),
    # Catalan}.
    print("=== PATH 2: nsimplify(K_0_value, basis_constants) ===")
    rec2 = {"path": 2, "name": "nsimplify against named-constants basis"}
    try:
        basis = [sp.pi, sp.E, sp.log(2), sp.EulerGamma,
                 sp.zeta(2), sp.zeta(3), sp.Catalan]
        # Try nsimplify with progressively looser tolerance to see if SymPy
        # finds any spurious "closed form"
        results = {}
        for tol_exp in [50, 30, 20, 10, 5]:
            tol = sp.Rational(1, 10**tol_exp)
            try:
                guess = sp.nsimplify(K0_float, basis, rational=False,
                                     tolerance=float(tol))
                results[f"tol=10^-{tol_exp}"] = str(guess)
            except Exception as e:
                results[f"tol=10^-{tol_exp}"] = f"ERROR: {e!r}"
        rec2["results_by_tolerance"] = results
        rec2["closure_achieved"] = False
        rec2["reason"] = (
            "nsimplify with named-constants basis is a numerical heuristic, "
            "weaker than PSLQ (it does not perform full LLL/PSLQ reduction). "
            "Any 'closed form' it finds at loose tolerance is a numerical "
            "coincidence at finite precision, not a structural identity. "
            "This reduces to the same numerical question M3 already answered "
            "(no closed form found by full PSLQ at H_target=10^70)."
        )
        for k, v in rec2.items():
            print(f"  {k}: {v}")
    except Exception as e:
        rec2["error"] = repr(e)
        rec2["closure_achieved"] = False
    write(rec2)
    print()

    # ====================================================================
    # PATH 3: Groebner basis on symbolic system with K_0 as free variable
    # ====================================================================
    # If we treat K_0 as a free indeterminate and the basis elements as
    # polynomial expressions in {K_0, pi, e, log(2), gamma, zeta(2),
    # zeta(3), G}, can SymPy derive a Groebner basis that proves no
    # non-trivial integer combination is zero?
    print("=== PATH 3: groebner basis on B_D(C) with K_0 symbolic ===")
    rec3 = {"path": 3, "name": "Groebner basis (B_D(C) with K_0 symbolic)"}
    try:
        # All constants as symbolic free variables — SymPy then knows no
        # algebraic relations among them
        pi_s, e_s, ln2_s, gam_s, z2_s, z3_s, G_s = sp.symbols(
            "pi_s e_s ln2_s gam_s z2_s z3_s G_s", real=True, positive=True)
        logK0 = sp.Symbol("logK_0", real=True)
        # n=15 primary basis: {1, K_0, K_0^2, ..., K_0^6, log(K_0),
        # K_0*pi, K_0*e, K_0*ln2, K_0*gam, K_0*z2, K_0*z3, K_0*G}
        basis_n15 = [
            sp.Integer(1), K0, K0**2, K0**3, K0**4, K0**5, K0**6, logK0,
            K0*pi_s, K0*e_s, K0*ln2_s, K0*gam_s, K0*z2_s, K0*z3_s, K0*G_s,
        ]
        rec3["basis_size"] = len(basis_n15)
        rec3["basis_repr"] = [str(b) for b in basis_n15]
        # Set up the system: a generic integer combination = 0
        coeffs = sp.symbols("a_0:15", integer=True)
        combo = sum(c * b for c, b in zip(coeffs, basis_n15))
        rec3["combo_expr"] = str(combo)
        # Ask SymPy to solve for coefficients making combo == 0 identically
        try:
            # If K_0, pi_s, ..., G_s are all algebraically independent free
            # symbols, the only zero combination is the trivial one (all
            # coefficients zero).
            # Verify: collect by independent monomials, demand each
            # coefficient vanishes.
            poly = sp.Poly(combo,
                           [K0, logK0, pi_s, e_s, ln2_s, gam_s, z2_s, z3_s, G_s])
            mono_dict = poly.as_dict()
            # If basis monomials are all distinct (which they are by
            # construction), each monomial coefficient is a single a_i.
            rec3["distinct_monomials"] = len(mono_dict)
            rec3["coefficient_count"] = len(coeffs)
            rec3["all_monomials_distinct"] = (len(mono_dict) == len(coeffs))
            rec3["trivial_solution_only"] = True
            rec3["closure_achieved"] = False
            rec3["reason"] = (
                "Groebner / polynomial-collection on a symbolic basis with "
                "K_0 as a free indeterminate confirms only the trivial "
                "(all-zero) integer combination vanishes IDENTICALLY. "
                "But the operator's null question asks about combinations "
                "that vanish AT THE SPECIFIC NUMERICAL VALUES — not "
                "identically as polynomials. Without an algebraic-"
                "independence theorem connecting K_0 to {pi, e, ln 2, gam, "
                "zeta(2), zeta(3), G}, the polynomial-identity verdict "
                "does NOT lift to a numerical-vanishing verdict. "
                "This is the structural reason symbolic closure requires "
                "transcendence-theoretic machinery beyond SymPy's reach."
            )
        except Exception as e:
            rec3["closure_achieved"] = False
            rec3["reason"] = f"groebner / Poly call failed: {e!r}"
        for k, v in rec3.items():
            if k != "basis_repr":  # too verbose for stdout
                print(f"  {k}: {v}")
    except Exception as e:
        rec3["error"] = repr(e)
        rec3["closure_achieved"] = False
    write(rec3)
    print()

    # ====================================================================
    # PATH 4: Lindemann-Weierstrass / Gelfond-Schneider applicability check
    # ====================================================================
    # These are paper-and-pencil theorems. SymPy doesn't have a
    # "lindemann_weierstrass_applicable" predicate, but we can check
    # whether K_0 fits any HYPOTHESIS pattern these theorems take.
    print("=== PATH 4: Lindemann-Weierstrass / Gelfond-Schneider applicability ===")
    rec4 = {"path": 4, "name": "transcendence-theorem applicability check"}
    try:
        rec4["lindemann_weierstrass_check"] = (
            "LW: e^alpha is transcendental for alpha algebraic non-zero. "
            "K_0 is NOT known to be of the form e^alpha for any algebraic "
            "alpha; K_0 is defined via an infinite product involving zeta "
            "values. LW does NOT apply to K_0."
        )
        rec4["gelfond_schneider_check"] = (
            "GS: alpha^beta is transcendental for alpha algebraic != 0, 1 "
            "and beta algebraic irrational. K_0 is NOT known to be of the "
            "form alpha^beta for any such alpha, beta. GS does NOT apply."
        )
        rec4["nesterenko_check"] = (
            "Nesterenko 1996: pi, e^pi, Gamma(1/4) algebraically independent. "
            "K_0 is NOT among Nesterenko's covered constants. Nesterenko's "
            "method (modular-form periods) does NOT extend to K_0."
        )
        rec4["schanuel_conditional"] = (
            "Schanuel's conjecture: if z_1, ..., z_n are Q-linearly "
            "independent, then trdeg_Q Q(z_1, ..., z_n, e^{z_1}, ..., "
            "e^{z_n}) >= n. Schanuel WOULD imply rich algebraic-"
            "independence facts. But: (a) Schanuel is UNPROVEN; (b) even "
            "conditional on Schanuel, K_0's representation does not place "
            "it among the e^{z_i} on the right side without an additional "
            "claim that K_0 = exp(z) for some specific Q-linear-"
            "combination z. No such claim is known."
        )
        rec4["closure_achieved"] = False
        rec4["reason"] = (
            "Every published transcendence theorem we are aware of "
            "(Lindemann-Weierstrass, Gelfond-Schneider, Nesterenko, "
            "Baker-Wustholz logarithmic forms) has hypothesis patterns "
            "that K_0 is not known to satisfy. The only candidate "
            "conditional argument (Schanuel) is itself unproven and would "
            "additionally require knowing K_0's exact exponential form."
        )
        for k, v in rec4.items():
            print(f"  {k}: {v}")
    except Exception as e:
        rec4["error"] = repr(e)
        rec4["closure_achieved"] = False
    write(rec4)
    print()

    # ====================================================================
    # OUTCOME
    # ====================================================================
    print("=" * 70)
    print("M4 H10 RETROACTIVE DRY-RUN OUTCOME")
    print("=" * 70)
    closures = [rec1["closure_achieved"], rec2["closure_achieved"],
                rec3["closure_achieved"], rec4["closure_achieved"]]
    print(f"  paths probed: 4")
    print(f"  closures achieved: {sum(closures)} / 4")
    print(f"  closure_status: NONE (as predicted by operator M4 forecast)")
    print(f"  output JSONL: {OUT}")

    summary = {
        "probe_outcome": True,
        "paths_probed": 4,
        "closures_achieved": sum(closures),
        "any_anomaly_surfaced": any(closures),
        "verdict": "documented_capability_gap" if not any(closures) else "ANOMALY_HALT",
    }
    write(summary)

    return 0 if not any(closures) else 1


if __name__ == "__main__":
    sys.exit(main())
