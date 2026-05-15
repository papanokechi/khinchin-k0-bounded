#!/usr/bin/env python3
"""
build_triage_m1_1.py — M1.1 triage.json constructor for unsolved-relay mission.

Trigger: operator amendment 2026-05-15 ~17:38 JST + audits/recheck completed by CLI same date.

Inputs:
    targets/survey_set.md (30-problem survey)
    targets/literature_recheck_18_levy_constant.md (#18 cleared)
    targets/overlap_audit_23_stanley_plane_partition.md (#23 cleared)
    targets/overlap_audit_26_gauss_kuzmin.md (#26 recommended-drop)
    capability/machinery_base_confirmed.md (canonical machinery list)

Output:
    targets/triage.json (28 schema-valid rows)
    stdout: per-row validation + summary

Hard-filter behavior (per Brief §M1.1 sentence 3):
    Entries with machinery NOT in capability/machinery_base_confirmed.md are EXPLICITLY
    included with machinery_available_locally=false, so the filter behavior is auditable.
    Brief example: Cunningham #7 (NFS), spt #22 / crank #25 (mock-modular).

Reproduce:
    cd siarc\\unsolved-relay-staging\\targets
    python build_triage_m1_1.py
    python triage_validator.py triage.json --strict
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Schema constants (mirror triage_schema.json)
# ---------------------------------------------------------------------------
REQUIRED_FIELDS = [
    "problem", "category", "known_partial_results_url",
    "machinery_required", "machinery_available_locally",
    "falsifiable_sub_question", "estimated_compute_to_partial_result_hours",
    "publishability_of_negative_result", "AEAL_compliance_risk",
]
CATEGORY_ENUM = {
    "number_theory", "combinatorics", "dynamics", "analysis", "discrete_geometry",
    "transcendence", "diophantine_approximation", "partition_theory",
}
RISK_ENUM = {"low", "medium", "high"}
PUB_ENUM = {"low", "medium", "high"}

# ---------------------------------------------------------------------------
# Machinery capability strings (mirror capability/machinery_base_confirmed.md)
# Only strings in this set may appear in machinery_required for available=true.
# ---------------------------------------------------------------------------
AVAILABLE_CAPS = {
    "python_3.12", "mpmath_500dps", "mpmath_pslq", "sympy_cas", "numpy", "numpy_fft",
    "gmpy2", "pari_gp_shellout", "pari_lindep_shellout", "pari_factor_moderate",
    "pari_nfinit_shellout", "pari_qflll_shellout", "lean_4.29.1", "lake_5.0.0",
    "mathlib4", "pcf_spectral_fingerprint", "painleve_stokes_tooling",
    "sympy_nsimplify_weak", "mpmath_quad", "mpmath_polyroots",
}
UNAVAILABLE_CAPS = {
    "arb_ball_arithmetic", "fpylll_lll", "cypari2_bridge", "sagemath",
    "scipy", "mpsolve", "nfs_factorization", "mock_modular_forms",
}

# ---------------------------------------------------------------------------
# 28 entries advancing to M1.1 per mutation_log/m1.0_to_m1.1_operator_amendments_20260515.md
#   * 26 unconditional (operator-instructed)
#   * #18 cleared after literature recheck (PASS)
#   * #23 cleared after overlap audit (PASS)
#   * #26 NOT in this list (CLI recommends DROP after overlap audit)
#   * #10 NOT in this list (operator-dropped)
# ---------------------------------------------------------------------------
ROWS = [
    # ---- #1 Erdős-Straus ----
    {
        "problem": "Erdős–Straus conjecture",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "sympy_cas"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend computational verification of 4/n = 1/x + 1/y + 1/z to N > 10^17 (current bound) "
            "via residue-class CRT covers + targeted decomposition for residue classes not covered "
            "by the standard 4-cover; either (a) verify N up to 10^18 with cover working, OR (b) document "
            "a residue class in [10^17, 10^18] that escapes all known covers."
        ),
        "estimated_compute_to_partial_result_hours": 72,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #2 Brocard ----
    {
        "problem": "Brocard's problem (n! + 1 = m²)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Brocard%27s_problem",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "sympy_cas"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend computational search for n! + 1 = m² past current N = 10^9 to N = 10^{10}–10^{11}; "
            "either (a) find a new Brown number (n, m) with n > 7, OR (b) verify absence in extended "
            "range using modular sieving + factorial-tail Legendre-residue analysis."
        ),
        "estimated_compute_to_partial_result_hours": 50,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "low",
    },
    # ---- #3 Erdős-Moser ----
    {
        "problem": "Erdős–Moser equation (1^k + 2^k + ... + (m-1)^k = m^k)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Moser_equation",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "sympy_cas"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the von Staudt–Clausen + p-adic exclusion lower bound past current m > 10^9 "
            "to m > 10^{10}; document any near-failures of the exclusion argument in the extended "
            "range and the smallest m for which exclusion certifies absence of nontrivial solution."
        ),
        "estimated_compute_to_partial_result_hours": 90,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #4 Pillai-gap (perfect-power gaps) ----
    {
        "problem": "Pillai-style consecutive perfect-power gap conjectures",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Pillai%27s_conjecture",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the perfect-power gap-statistics enumeration up to N = 10^{19}; identify any new "
            "high-gap candidates exceeding the current record, with each candidate independently "
            "verified by recomputation in a separate session."
        ),
        "estimated_compute_to_partial_result_hours": 45,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "low",
    },
    # ---- #5 Beal signature ----
    {
        "problem": "Beal conjecture for fixed signature (p, q, r)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Beal_conjecture",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "For one specific signature (p, q, r) where no proof exists (e.g., (4, 5, 6) or (5, 5, 7)), "
            "extend A^p + B^q = C^r enumeration past max(A, B, C) > 10^7 to 10^9 with high-precision "
            "sieving over coprime triples; either find a counterexample (signature-specific Beal disproof) "
            "or document absence in extended range."
        ),
        "estimated_compute_to_partial_result_hours": 60,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #6 Lehmer totient ----
    {
        "problem": "Lehmer's totient problem (φ(n) | n − 1 ⇒ n prime?)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Lehmer%27s_totient_problem",
        "machinery_required": [
            "python_3.12", "mpmath_500dps", "gmpy2", "pari_gp_shellout", "pari_factor_moderate"
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the lower bound ω(n) ≥ 14 (smallest prime-omega count of a non-prime n satisfying "
            "φ(n) | n − 1) via mpmath/gmpy2 sieving + PARI gp factor at moderate cofactor depths up to "
            "D = 10^{20}; document any candidate n in the extended range that survives the test."
        ),
        "estimated_compute_to_partial_result_hours": 95,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #7 Cunningham (machinery-gap candidate, included to test filter) ----
    {
        "problem": "Cunningham project unfactored cofactor (fixed base, exponent class)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Cunningham_project",
        "machinery_required": ["nfs_factorization", "pari_factor_moderate"],
        "machinery_available_locally": False,
        "falsifiable_sub_question": (
            "Pick one base/exponent class where the cofactor is unfactored and document a "
            "precision-and-method audit of why current ECM/NFS attempts have stalled (capability-gap "
            "framing). NB: NFS is NOT in confirmed machinery base; this row is included to test the "
            "hard-filter behaviour — should be DROPPED at M1.2 selection per Brief §M1.1 sentence 3."
        ),
        "estimated_compute_to_partial_result_hours": 0.5,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "high",
    },
    # ---- #8 Mertens sign-change ----
    {
        "problem": "Mertens function sign-change density",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Mertens_function",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "numpy"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the tabulation of sign-change positions of M(n) = Σ_{k=1}^n μ(k) up to N = 10^{14} "
            "(current bound around 10^{13}); compute the sign-change density and compare against "
            "Lévy/Riemann-type predictions; document any sign-change cluster exceeding 3σ from expected."
        ),
        "estimated_compute_to_partial_result_hours": 80,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #9 Repunit primality ----
    {
        "problem": "Repunit primality density extension (R_n = (10^n − 1)/9)",
        "category": "number_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Repunit",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "sympy_cas"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Apply BPSW probable prime test (sympy.isprime) to R_n for n in a new range past the current "
            "verified bound; identify any new probable-prime R_n candidates and document the test trace "
            "at high precision to support promotion to deterministic primality verification."
        ),
        "estimated_compute_to_partial_result_hours": 55,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "low",
    },
    # ---- #11 Zaremba A_5 ----
    {
        "problem": "Zaremba's conjecture for alphabet A_5 = {1, 2, 3, 4, 5}",
        "category": "diophantine_approximation",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Zaremba%27s_conjecture",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "sympy_cas"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the Bourgain–Kontorovich density estimate of integers q with CF(q/p) bounded by "
            "A_5 = 5 to a new q-range [10^7, 10^9]; either find a q without such a p (Zaremba-disproof "
            "for A_5 at that q) or extend the density estimate with a documented lower bound."
        ),
        "estimated_compute_to_partial_result_hours": 50,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #12 Markov spectrum gaps ----
    {
        "problem": "Markov spectrum gap structure between 3 and Freiman's constant",
        "category": "diophantine_approximation",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Markov_spectrum",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend the tabulation of Markov triples (and corresponding spectrum values) past the "
            "current computational record; compute gap-residual statistics in the open region "
            "[3, F] where F ≈ 4.5278 is Freiman's constant; flag any apparent gap clusters."
        ),
        "estimated_compute_to_partial_result_hours": 50,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #13 Lagrange spectrum past Freiman ----
    {
        "problem": "Lagrange spectrum values past Freiman's constant",
        "category": "diophantine_approximation",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Lagrange_spectrum",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend computational enumeration of Lagrange-spectrum values above Freiman's constant "
            "(~4.5278) to resolution 10^{-6} on [4.5278, 4.6]; document the distribution and flag any "
            "candidate transition points (accumulation points beyond known structure)."
        ),
        "estimated_compute_to_partial_result_hours": 60,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
    # ---- #14 Stern-Brocot gap distribution ----
    {
        "problem": "Stern–Brocot tree gap distribution at large levels",
        "category": "diophantine_approximation",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "At Stern–Brocot tree level n ∈ [20, 30], compute the empirical gap-distribution histogram "
            "at fine resolution and test against a conjectural Gauss–Kuzmin-style asymptotic density; "
            "document goodness-of-fit (KS statistic) and any deviation exceeding 3σ."
        ),
        "estimated_compute_to_partial_result_hours": 30,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "low",
    },
    # ---- #15 Khinchin's constant rationality ----
    {
        "problem": "Khinchin's constant K_0 — rationality / algebraicity",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Khinchin%27s_constant",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
            "sympy_nsimplify_weak",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "PSLQ false-positive scan of K_0 ≈ 2.685452... at 500 dps over an expanded (D, H) grid with "
            "D ≤ 8 and log H ≤ 200; certify any near-relation candidate with gp lindep at 750 dps as "
            "second-library independent leg; document the FP-rejection range as a transcendence-evidence "
            "computational record."
        ),
        "estimated_compute_to_partial_result_hours": 14,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #16 Catalan G ----
    {
        "problem": "Catalan's constant G — irrationality / algebraicity",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Catalan%27s_constant",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "PSLQ false-positive scan of G ≈ 0.9159655941... at 500 dps over an expanded (D, H) grid "
            "(D ≤ 10, log H ≤ 250) against basis {1, π, log 2, ζ(3), π²/8, G, ...}; certify all "
            "near-relations with gp lindep at 750 dps; document the FP-rejection range."
        ),
        "estimated_compute_to_partial_result_hours": 18,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #17 Apéry-extension witnesses ----
    {
        "problem": "Apéry-extension witnesses for ζ(5), ζ(7), ζ(9)",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Particular_values_of_the_Riemann_zeta_function",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend Ball–Rivoal–Zudilin-style irrationality-witness search for ζ(5), ζ(7), ζ(9) at "
            "200–300 dps; PSLQ-screen each against {1, ζ(2), ζ(3), ζ(4), π^k, log 2, ...} for relations "
            "of (D ≤ 6, log H ≤ 100); certify with gp lindep; document the FP-rejection scope."
        ),
        "estimated_compute_to_partial_result_hours": 28,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #18 Lévy's β (cleared via literature recheck) ----
    {
        "problem": "Lévy's constant β = π² / (12 log 2) — rationality / transcendence",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/L%C3%A9vy%27s_constant",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "PSLQ false-positive scan of β = π²/(12 log 2) ≈ 1.18656911... at 500 dps over an expanded "
            "(D, H) grid against basis {1, π, π², log 2, ζ(2), ζ(3), G, ...} for D ≤ 8 and log H ≤ 200; "
            "certify near-relations with gp lindep at 750 dps; document FP-rejection range as advance "
            "over prior published bounds."
        ),
        "estimated_compute_to_partial_result_hours": 16,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #19 Glaisher-Kinkelin generalized A_k ----
    {
        "problem": "Glaisher–Kinkelin generalized constants A_k (higher rank)",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Glaisher%E2%80%93Kinkelin_constant",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
            "sympy_cas",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "For higher-rank Glaisher–Kinkelin-type constants A_k (k ∈ {2, 3, 4}), compute at 200 dps "
            "via mpmath and PSLQ-search for integer relations among {A_GK, A_2, A_3, A_4, ζ(3), ζ(5), "
            "log 2, π, γ}; promote any high-confidence near-relation to a sympy-attempted symbolic "
            "identification."
        ),
        "estimated_compute_to_partial_result_hours": 22,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #20 Periods (Kontsevich-Zagier bounded class) ----
    {
        "problem": "Periods (Kontsevich–Zagier sense) — bounded physically-arising constant",
        "category": "transcendence",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Period_(algebraic_geometry)",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "mpmath_quad", "pari_gp_shellout",
            "pari_lindep_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Pick one specific period-status-open constant (e.g., Z² simple-cubic lattice Green's "
            "function at the origin OR a fixed 2-loop Feynman residue); compute at 200 dps via "
            "mpmath.quad; PSLQ-screen against known period bases {ζ(k), L(χ_4, k), Catalan, log p, ...}; "
            "promote candidate to symbolic verification."
        ),
        "estimated_compute_to_partial_result_hours": 32,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "high",
    },
    # ---- #21 Andrews-Beck higher-rank ----
    {
        "problem": "Andrews–Beck higher-rank partition-statistic identities",
        "category": "partition_theory",
        "known_partial_results_url": "https://arxiv.org/abs/2102.10342",
        "machinery_required": ["python_3.12", "sympy_cas", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Extend computational verification of one Andrews–Beck-style higher-rank identity at "
            "modulus m ∈ {7, 11} to N ≥ 10^5 using sympy partition enumeration; document any "
            "counterexample candidate; if none, extend the verified range and report the bound."
        ),
        "estimated_compute_to_partial_result_hours": 22,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "low",
    },
    # ---- #22 spt-function (machinery-gap candidate, included to test filter) ----
    {
        "problem": "Andrews's spt(n) function congruences (verification only, proof needs mock-modular)",
        "category": "partition_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Spt_function",
        "machinery_required": ["python_3.12", "sympy_cas", "gmpy2", "mock_modular_forms"],
        "machinery_available_locally": False,
        "falsifiable_sub_question": (
            "VERIFICATION-ONLY (not proof): extend the computational verification of an spt(n) ≡ 0 "
            "mod m congruence pattern for one m in the conjectured-but-unproven class to N ≥ 10^5; "
            "document verified range. NB: full proof requires mock-modular machinery NOT in confirmed "
            "kit; this row is a hard-filter-dropout test — should be DROPPED at M1.2 per §M1.1 sentence 3."
        ),
        "estimated_compute_to_partial_result_hours": 30,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "high",
    },
    # ---- #23 Stanley plane-partition (cleared via overlap audit) ----
    {
        "problem": "Stanley's plane-partition asymptotic constants (PSLQ-identify against special-value basis)",
        "category": "partition_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Plane_partition",
        "machinery_required": [
            "mpmath_500dps", "mpmath_pslq", "pari_gp_shellout", "pari_lindep_shellout",
            "sympy_cas",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "PSLQ-identify the leading asymptotic constant of MacMahon-style box-counted plane "
            "partitions of fixed shape σ as N → ∞, scanned at 500 dps against the basis {A_GK, Catalan G, "
            "ζ(3), ζ(5), log 2, log 3, π², π³, 1} for shapes σ in an explicitly enumerated set of ≤ 5 "
            "shapes; either flag a relation candidate (certified with gp lindep at 750 dps) or document "
            "absence of relation."
        ),
        "estimated_compute_to_partial_result_hours": 26,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #24 Brown-Erdős-Sós ----
    {
        "problem": "Brown–Erdős–Sós conjecture for linear 3-uniform hypergraphs",
        "category": "combinatorics",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Brown%E2%80%93Erd%C5%91s%E2%80%93S%C3%B3s_conjecture",
        "machinery_required": ["python_3.12", "sympy_cas", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "For fixed (k, r) ∈ {(3, 1), (4, 1)}, enumerate extremal 3-uniform hypergraph configurations "
            "avoiding (k, k+r)-subhypergraphs at vertex bound n ≤ 50 via constraint-SAT-style branching "
            "with explicit branching budget; document maximum edge count and compare against conjectured "
            "bound for each (k, r)."
        ),
        "estimated_compute_to_partial_result_hours": 90,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #25 Crank-moment (machinery-gap candidate, included to test filter) ----
    {
        "problem": "Crank-moment congruences beyond Ramanujan's (verification only, proof needs mock-modular)",
        "category": "partition_theory",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Crank_of_a_partition",
        "machinery_required": ["python_3.12", "sympy_cas", "gmpy2", "mock_modular_forms"],
        "machinery_available_locally": False,
        "falsifiable_sub_question": (
            "VERIFICATION-ONLY: tabulate crank moments mod {5, 7, 11, 13} for partitions of n ≤ 10^4 "
            "via sympy partition enumeration; flag any new congruence pattern candidates. NB: full "
            "proof requires mock-modular machinery NOT in confirmed kit; this row is a hard-filter "
            "dropout test — should be DROPPED at M1.2 per §M1.1 sentence 3."
        ),
        "estimated_compute_to_partial_result_hours": 25,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "high",
    },
    # ---- #27 Mahler badly-approximable pairs ----
    {
        "problem": "Mahler badly-approximable pairs in a fixed cubic number field",
        "category": "diophantine_approximation",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Mahler%27s_compactness_theorem",
        "machinery_required": [
            "python_3.12", "mpmath_500dps", "gmpy2", "pari_gp_shellout", "pari_nfinit_shellout",
            "pari_qflll_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "In Q(α) where α³ = α + 1 (smallest Pisot), enumerate simultaneously-badly-approximable "
            "pairs (β, γ) up to height H = 10^4 using gp nfinit + qflll lattice search; document the "
            "count of pairs found and compare against conjectural density; flag any pair violating "
            "conjectural bound."
        ),
        "estimated_compute_to_partial_result_hours": 42,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #28 Hurst-exponent for arithmetic sequences ----
    {
        "problem": "Hurst-exponent estimation for arithmetic dynamical sequences (Stern, Calkin–Wilf, Thomae)",
        "category": "dynamics",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Hurst_exponent",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2", "numpy", "numpy_fft"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Compute estimated H (R/S statistic + rescaled-range analysis) for Stern, Calkin–Wilf, "
            "Thomae sequences at window lengths n ∈ {10^3, 10^4, 10^5, 10^6} using numpy; test against "
            "conjectured rational/irrational H values per sequence; document any deviation from the "
            "log-periodic noise expected from arithmetic structure."
        ),
        "estimated_compute_to_partial_result_hours": 16,
        "publishability_of_negative_result": "low",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #29 Sárközy patterns ----
    {
        "problem": "Sárközy-type pattern-avoidance density in sumset dynamics",
        "category": "combinatorics",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/S%C3%A1rk%C3%B6zy%27s_theorem",
        "machinery_required": [
            "python_3.12", "sympy_cas", "gmpy2", "pari_gp_shellout", "pari_qflll_shellout",
        ],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "For fixed small forbidden pattern P (e.g., {n, n+d, n+2d} arithmetic progression, OR a "
            "specific quadratic pattern), extend the maximum-density-set table for P on [1, N] for "
            "N up to 10^5 via greedy + qflll lattice search; document density at each N step and "
            "compare against conjectural asymptotic."
        ),
        "estimated_compute_to_partial_result_hours": 55,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "medium",
    },
    # ---- #30 Brjuno function statistics ----
    {
        "problem": "Brjuno function B(α) statistics at the irrational-rotation boundary",
        "category": "dynamics",
        "known_partial_results_url": "https://en.wikipedia.org/wiki/Brjuno_number",
        "machinery_required": ["python_3.12", "mpmath_500dps", "gmpy2"],
        "machinery_available_locally": True,
        "falsifiable_sub_question": (
            "Compute Brjuno function B(α) = Σ log(q_{n+1})/q_n on a dense grid of α in [0, 1] at "
            "resolution 10^{-6}, truncated at n = 50 CF convergents per α; tabulate empirical "
            "Brjuno-set Hausdorff-dimension estimates against conjectural dimension; document any "
            "deviation exceeding the resolution-induced uncertainty."
        ),
        "estimated_compute_to_partial_result_hours": 52,
        "publishability_of_negative_result": "medium",
        "AEAL_compliance_risk": "low",
    },
]

# ---------------------------------------------------------------------------
def validate_row(row: dict, idx: int) -> list[str]:
    """Return a list of validation errors for one row."""
    errors = []
    # required fields
    for f in REQUIRED_FIELDS:
        if f not in row:
            errors.append(f"row[{idx}] missing required field: {f}")
    # category enum
    if row.get("category") not in CATEGORY_ENUM:
        errors.append(f"row[{idx}] category invalid: {row.get('category')}")
    # risk + pub enums
    if row.get("publishability_of_negative_result") not in PUB_ENUM:
        errors.append(f"row[{idx}] publishability_of_negative_result invalid: "
                      f"{row.get('publishability_of_negative_result')}")
    if row.get("AEAL_compliance_risk") not in RISK_ENUM:
        errors.append(f"row[{idx}] AEAL_compliance_risk invalid: "
                      f"{row.get('AEAL_compliance_risk')}")
    # url shape (light check)
    url = row.get("known_partial_results_url", "")
    if not (url.startswith("http://") or url.startswith("https://")):
        errors.append(f"row[{idx}] known_partial_results_url not http(s): {url}")
    # machinery_required type
    mr = row.get("machinery_required")
    if not isinstance(mr, list) or not all(isinstance(s, str) for s in mr):
        errors.append(f"row[{idx}] machinery_required not list[str]")
    else:
        # consistency: every required cap must be in AVAILABLE_CAPS or UNAVAILABLE_CAPS
        for cap in mr:
            if cap not in AVAILABLE_CAPS and cap not in UNAVAILABLE_CAPS:
                errors.append(f"row[{idx}] unknown machinery string: {cap}")
        # consistency: machinery_available_locally must reflect machinery_required content
        any_unavailable = any(cap in UNAVAILABLE_CAPS for cap in mr)
        if any_unavailable and row.get("machinery_available_locally", False):
            errors.append(f"row[{idx}] inconsistent: requires unavailable capability "
                          f"but machinery_available_locally=true")
    # falsifiable_sub_question min length
    sq = row.get("falsifiable_sub_question", "")
    if len(sq) < 30:
        errors.append(f"row[{idx}] falsifiable_sub_question too short ({len(sq)} chars)")
    # hours bound
    h = row.get("estimated_compute_to_partial_result_hours")
    if not isinstance(h, (int, float)):
        errors.append(f"row[{idx}] hours not numeric: {h}")
    elif not (0 <= h <= 840):
        errors.append(f"row[{idx}] hours out of [0, 840]: {h}")
    return errors


def main() -> int:
    here = Path(__file__).resolve().parent
    out = here / "triage.json"

    all_errors: list[str] = []
    for i, row in enumerate(ROWS):
        all_errors.extend(validate_row(row, i))

    if all_errors:
        print("VALIDATION FAILED:")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    # Write triage.json as a JSON array of rows (per Brief §M1.1 "one row per candidate problem")
    # so that triage_validator.py can validate directly.
    with open(out, "w", encoding="utf-8") as f:
        json.dump(ROWS, f, indent=2, ensure_ascii=False)

    # Write companion metadata sidecar (NOT validated by schema).
    sidecar = here / "_M1.1_triage_metadata.json"
    metadata = {
        "schema": "triage_schema.json",
        "builder": "build_triage_m1_1.py",
        "built_at_utc": datetime.now(tz=__import__("datetime").timezone.utc).isoformat(),
        "built_at_jst_local": "2026-05-15 ~17:42 JST (operator-time)",
        "mutation_log": "mutation_log/m1.0_to_m1.1_operator_amendments_20260515.md",
        "row_count": len(ROWS),
        "operator_clear_count_target": 27,
        "actual_advancing_count": len(ROWS),
        "count_explanation": (
            "Operator instructed 'proceed on 27 clear entries'; #18 cleared via literature "
            "recheck (in operator's 27), #23 cleared via overlap audit (ADDED, not in operator's "
            "27), #26 recommended-drop via overlap audit (NOT included). Net = 26 unconditional "
            "+ #18 + #23 = 28."
        ),
        "machinery_gap_rows": [
            {"row_idx": 6, "problem": "Cunningham #7", "reason": "NFS not in kit"},
            {"row_idx": 21, "problem": "spt #22", "reason": "mock-modular not in kit"},
            {"row_idx": 24, "problem": "crank-moment #25", "reason": "mock-modular not in kit"},
        ],
    }
    with open(sidecar, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"WROTE: {sidecar}")
    print(f"WROTE: {out}")
    print(f"  rows: {len(ROWS)}")
    print(f"  available=true: {sum(1 for r in ROWS if r['machinery_available_locally'])}")
    print(f"  available=false (filter-test rows): "
          f"{sum(1 for r in ROWS if not r['machinery_available_locally'])}")
    print(f"  high AEAL risk: {sum(1 for r in ROWS if r['AEAL_compliance_risk'] == 'high')}")
    print(f"  medium AEAL risk: {sum(1 for r in ROWS if r['AEAL_compliance_risk'] == 'medium')}")
    print(f"  low AEAL risk: {sum(1 for r in ROWS if r['AEAL_compliance_risk'] == 'low')}")
    print(f"  total estimated CPU-hours (sum): "
          f"{sum(r['estimated_compute_to_partial_result_hours'] for r in ROWS):.1f}")
    print(f"  max single-problem CPU-hours: "
          f"{max(r['estimated_compute_to_partial_result_hours'] for r in ROWS):.1f}")
    cats = {}
    for r in ROWS:
        cats[r['category']] = cats.get(r['category'], 0) + 1
    print(f"  category distribution:")
    for c, n in sorted(cats.items()):
        print(f"    {c}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
