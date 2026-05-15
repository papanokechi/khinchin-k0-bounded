# Machinery base — CONFIRMED 2026-05-15 ~17:39 JST

This file is the AEAL canonical reference for `machinery_required` and `machinery_available_locally` fields in `targets/triage.json`. Source: `capability/probe_results_20260515.md` (direct empirical probe, not inference).

## Available (use these strings only in `machinery_required` for `available=true` rows)

| Capability string | Provided by | Verified |
|---|---|---|
| `python_3.12` | Python 3.12.10 | ✅ |
| `mpmath_500dps` | mpmath 1.3.0 | ✅ (500-dps π tail) |
| `mpmath_pslq` | mpmath.pslq | ✅ |
| `sympy_cas` | sympy 1.14.0 | ✅ |
| `numpy` | numpy 2.4.4 | ✅ |
| `gmpy2` | gmpy2 2.3.0 | ✅ |
| `pari_gp_shellout` | gp binary on PATH | ✅ (binary found) |
| `pari_lindep_shellout` | gp via subprocess | ✅ (function exists in PARI) |
| `pari_factor_moderate` | gp `factor` for small/moderate ints | ✅ (NOT NFS-scale) |
| `pari_nfinit_shellout` | gp `nfinit`/`bnfinit` | ✅ (number-field arithmetic) |
| `pari_qflll_shellout` | gp `qflll` | ✅ (LLL substitute) |
| `lean_4.29.1` | lean.exe | ✅ |
| `lake_5.0.0` | lake.exe | ✅ |
| `mathlib4` | operator-attested via congruent-relay | ⚪ (operator-attested) |
| `pcf_spectral_fingerprint` | operator-specific framework | ⚪ (operator-attested) |
| `painleve_stokes_tooling` | operator-specific | ⚪ (operator-attested) |
| `sympy_nsimplify_weak` | sympy.nsimplify | ✅ (limited algebraic-relation finder) |
| `mpmath_quad` | mpmath.quad | ✅ (high-precision integration) |
| `mpmath_polyroots` | mpmath.polyroots | ✅ (root-finder, mpsolve substitute) |
| `numpy_fft` | numpy.fft | ✅ (low-precision FFT; for #28 Hurst-exponent estimation) |

## Not available (do NOT cite these as `available=true`)

| Capability string | Reason | Implication |
|---|---|---|
| `arb_ball_arithmetic` | python-flint not installed | M3.1 harness 2nd-leg uses gp lindep instead |
| `fpylll_lll` | fpylll not installed | LLL via gp qflll shell-out (moderate dims only) |
| `cypari2_bridge` | cypari2 not installed | PARI access only via subprocess to gp |
| `sagemath` | sage not installed | Any sage-specific functions unavailable |
| `scipy` | scipy not installed | mpmath.quad / numpy substitutes only |
| `mpsolve` | mpsolve not installed | mpmath.polyroots substitute |
| `nfs_factorization` | not in kit | Large-cofactor factorization OUT (Cunningham #7 drops) |
| `mock_modular_forms` | not in kit | spt-function full proof OUT (#22, #25 drop) |

## Discretionary install candidates (NOT proposed, flagged for operator)

If the operator wants the harness 2nd-leg to use the canonical `arb` ball arithmetic per Brief §M3.1 phrasing:
- `pip install python-flint` (canonical Python binding to FLINT/Arb)
  - Risk: Windows wheels may not be available for all versions; may require Visual Studio build tools
  - Benefit: rigorous interval arithmetic for FP-rejection step

If the operator wants LLL bridges from Python:
- `pip install fpylll`
  - Risk: similar Windows-build issues; this is a Cython wrapper around fplll
  - Benefit: lattice-reduction in pipeline (matters for #16 Catalan G near-relation searches at high D×H)

If the operator wants the full Sage stack:
- Not via pip; SageMath on Windows is via WSL2 or Sage-Windows binaries
  - Risk: large install footprint + integration friction
  - Benefit: closes many gaps at once

**CLI does NOT recommend any of these installs as part of M1 work.** The M1–M6 deliverable is bounded by the machinery base AS-IS. If a milestone hits a gap that one of these tools would close, the gap gets a `capability/<x>.gap.md` per Brief §0.2 and the mission stops — that IS the AEAL-compliant outcome.

## Cross-reference

- `capability/probe_results_20260515.md` — empirical source for this file
- `_M1.0_first_action_log.md` — pre-probe machinery inference (now superseded)
- `targets/triage.json` — consumer (will reference capability strings from the "Available" table)
- `mutation_log/m1.0_to_m1.1_operator_amendments_20260515.md` — records the machinery-base refinement as part of the M1.0 → M1.1 transition
