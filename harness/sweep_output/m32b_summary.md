# M3.2b Empirical Sweep — Summary

**Mission:** unsolved-relay / Khinchin K_0 bounded sub-question
**Phase:** M3 / M3.2b canonical empirical sweep (post U-MISSION-N resolution)
**Predicate anchor:** `literature/_m2.3_calibration_anchor.md` §7 (locked at `gold/M2`, commit `ca9c989`)
**Execution authority:** operator M3.2b GREENLIGHT (2026-05-16 ~10:00 JST, ratified post-M3.2a) + operator U-MISSION-N RESOLUTION (2026-05-16 ~11:10 JST, R1+R2.β+H10 install)
**Run:** `python -u harness/sweep.py --full --m32-full-greenlighted`
**Wall-clock:** 2026-05-16 11:37:23 → 12:26:59 JST · 2977.80 s · 49.6 min
**Canonical output:** `harness/sweep_output/m32b_empirical_sweep.jsonl` (363,709 B; 67 lines = 1 meta header + 65 candidate records + 1 meta footer)
**Audit harness:** `harness/_audit_m32b_summary.py` · raw output `harness/sweep_output/_m32b_audit_output.txt`

---

## §1 Headline aggregate verdict — CLEAN NULL ACROSS ALL 65 SUB-BASES

| Metric | Threshold (per §7 predicate) | Measured | Status |
|---|---|---|---|
| All candidates `cascade.verdict == cascade_stable_null` | 65/65 | **65/65** | ✅ PASS |
| primary_full bit-for-bit reproduction of M3.2a (K, final_norm, H_rigorous at P/2P/4P) | identical to 71 digits | **identical** at all 3 precisions | ✅ PASS |
| primary_full verification_class | `proven_corollary` (H9 rigorous tier) | `proven_corollary` | ✅ PASS |
| 64 empirical sub-bases verification_class | `field_standard_practice` (H9 empirical tier) | 64/64 `field_standard_practice` | ✅ PASS |
| gp_lindep second leg on every candidate | confirms null (returns relation > H_empirical OR returns no relation) | 65/65 `gp_noise_relation_above_H_empirical_confirms_null` | ✅ PASS |
| H10 pre-canonical dry-run prerequisite | clean across all 65 sub-bases | clean (commit `5d75072`, 113s wall-clock, all 65 cascade_stable_null) | ✅ PASS |
| §7 acceptance criteria (4) on primary_full | all pass | **all 4 pass** (cascade verdict + H_rig ≥ 10^70 + gp_verdict in accept-set + residual_check N/A or pass) | ✅ PASS |

**No anomalies surfaced. No halt conditions triggered.**

---

## §2 Primary_full reproducibility (M3.2a vs M3.2b) — bit-for-bit at 71 digits

The operator-mandated determinism check (U-MISSION-N RESOLUTION: *"If it doesn't reproduce, halt and surface — that would indicate non-determinism in mpmath.pslq that affects M3.2a's verification_class assignment"*) PASSES at every cascade leg.

| P (dps) | M3.2a K | M3.2b K | K match | M3.2a final_norm vs M3.2b | H_rigorous M3.2a | H_rigorous M3.2b | H match |
|---:|---:|---:|---|---|---|---|---|
| 2160 | 29363 | 29363 | YES | identical (71-digit int) | 1.0361e+72 | 1.0361e+72 | YES |
| 4320 | 29363 | 29363 | YES | identical (71-digit int) | 1.0361e+72 | 1.0361e+72 | YES |
| 8640 | 29363 | 29363 | YES | identical (71-digit int) | 1.0361e+72 | 1.0361e+72 | YES |

`final_norm` value (identical across all 6 cascade legs):
```
10360617603511610161191925406371857820825757133185306086265338548597674
```
(71 decimal digits.)

`H_rigorous` (= 100 × final_norm per `harness/rigorous_bound.py` FBA T1 derivation, identical across all 6 cascade legs):
```
1036061760351161016119192540637185782082575713318530608626533854859767400
```
(73 decimal digits = `1.0361e+72`.)

**mpmath.pslq determinism is empirically confirmed under our build (mpmath 1.3.0 + Python 3.12) at n=15 over a 4× precision range (P=2160 → 4P=8640) and across two independent executions (M3.2a 2026-05-16 ~08:31 JST commit `d55ffbc`; M3.2b 2026-05-16 ~11:37 JST commit pending).**

---

## §3 Per-family aggregate

| Family | n | count | Σ wall-clock (s) | avg (s) | H_rigorous range | Verification class |
|---|---:|---:|---:|---:|---|---|
| `primary_full` | 15 | 1 | 2693.8 | 2693.78 | 1.04e+72 (single) | proven_corollary |
| `complement_plus_K0_k` (k=0..6) | 9 | 7 | 229.8 | 32.82 | 3.50e+15 ... 9.06e+16 (median 1.26e+16) | field_standard_practice |
| `full_complement` | 8 | 1 | 27.0 | 27.01 | 1.16e+21 (single) | field_standard_practice |
| `triplet_log_*` | 3 | 21 | 21.4 | 1.02 | 1.01e+72 ... 2.38e+72 (median 1.17e+72) | field_standard_practice |
| `pair_bilinear_*` | 2 | 21 | 3.5 | 0.17 | 1.12e+72 ... 3.55e+73 (median 2.38e+72) | field_standard_practice |
| `pair_log_*` | 2 | 14 | 2.3 | 0.17 | 1.00e+72 ... 1.36e+73 (median 2.34e+72) | field_standard_practice |
| **TOTAL** | — | **65** | **2977.8** | — | — | — |

**Wall-clock observations:**
- Primary cascade dominates total: 90.5 % of wall-clock on the 1 rigorous-tier candidate.
- 64 empirical candidates aggregate to **283.9 s = 4.7 min** (9.5 % of wall-clock).
- Total 49.6 min is ~30 % under the operator's 70-90 min estimate.

**H_rigorous distribution observations:**
- Small-n candidates (n=2, n=3) terminate fast (K ≈ 90 for n=2, K ≈ 280 for n=3) with high cancellation-norm; FBA T1 bound = 100 × final_norm yields H_rigorous in 10^72 range.
- n=8, n=9 candidates run with maxsteps=2000 limiter; cancellation occurs late with weaker norm growth; FBA T1 bound in 10^15-10^21 range, **below** H_empirical=10^70. These candidates are correctly classified `field_standard_practice` (empirical tier) — the rigorous tier is materially weaker at this maxsteps budget for mid-n bases.
- primary_full (n=15) at maxsteps=(100k, 80k, 50k) reaches K=29363 with rigorous bound 10^72 > 10^70 BBC parity → `proven_corollary`.

---

## §4 Per-candidate verdict table (65 rows)

Embedded from `_m32b_table.md`; row order matches sweep execution order; `noise>H_emp_OK_null` abbreviates `gp_noise_relation_above_H_empirical_confirms_null`.

| idx | family | n | verdict | class | H_emp_op | H_rig | gp_verdict | elapsed_s |
|---|---|---:|---|---|---|---|---|---:|
| 1 | `primary_full` | 15 | cascade_stable_null | proven_corollary | 8.00e+69 | 1.04e+72 | noise>H_emp_OK_null | 2693.78 |
| 2 | `full_complement` | 8 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.16e+21 | noise>H_emp_OK_null | 27.01 |
| 3 | `complement_plus_K0_0` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 5.47e+15 | noise>H_emp_OK_null | 34.09 |
| 4 | `complement_plus_K0_1` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.12e+16 | noise>H_emp_OK_null | 36.27 |
| 5 | `complement_plus_K0_2` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.43e+16 | noise>H_emp_OK_null | 30.64 |
| 6 | `complement_plus_K0_3` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.50e+15 | noise>H_emp_OK_null | 31.51 |
| 7 | `complement_plus_K0_4` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.26e+16 | noise>H_emp_OK_null | 33.47 |
| 8 | `complement_plus_K0_5` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 6.18e+15 | noise>H_emp_OK_null | 32.19 |
| 9 | `complement_plus_K0_6` | 9 | cascade_stable_null | field_standard_practice | 1.00e+70 | 9.06e+16 | noise>H_emp_OK_null | 31.61 |
| 10 | `pair_log_1` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.02e+72 | noise>H_emp_OK_null | 0.16 |
| 11 | `pair_log_K_0` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 7.02e+72 | noise>H_emp_OK_null | 0.17 |
| 12 | `pair_log_K_0^2` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.93e+72 | noise>H_emp_OK_null | 0.16 |
| 13 | `pair_log_K_0^3` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.36e+73 | noise>H_emp_OK_null | 0.16 |
| 14 | `pair_log_K_0^4` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.34e+72 | noise>H_emp_OK_null | 0.16 |
| 15 | `pair_log_K_0^5` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.65e+72 | noise>H_emp_OK_null | 0.16 |
| 16 | `pair_log_K_0^6` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 9.60e+72 | noise>H_emp_OK_null | 0.16 |
| 17 | `pair_log_K_0*pi` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.31e+72 | noise>H_emp_OK_null | 0.21 |
| 18 | `pair_log_K_0*e` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.57e+72 | noise>H_emp_OK_null | 0.17 |
| 19 | `pair_log_K_0*ln2` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.59e+72 | noise>H_emp_OK_null | 0.16 |
| 20 | `pair_log_K_0*gamma` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.24e+72 | noise>H_emp_OK_null | 0.16 |
| 21 | `pair_log_K_0*zeta(2)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.33e+72 | noise>H_emp_OK_null | 0.20 |
| 22 | `pair_log_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.46e+72 | noise>H_emp_OK_null | 0.16 |
| 23 | `pair_log_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.00e+72 | noise>H_emp_OK_null | 0.16 |
| 24 | `pair_bilinear_K_0*pi_K_0*e` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.12e+72 | noise>H_emp_OK_null | 0.16 |
| 25 | `pair_bilinear_K_0*pi_K_0*ln2` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.82e+73 | noise>H_emp_OK_null | 0.16 |
| 26 | `pair_bilinear_K_0*pi_K_0*gamma` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.79e+72 | noise>H_emp_OK_null | 0.16 |
| 27 | `pair_bilinear_K_0*pi_K_0*zeta(2)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.18e+72 | noise>H_emp_OK_null | 0.16 |
| 28 | `pair_bilinear_K_0*pi_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.67e+72 | noise>H_emp_OK_null | 0.17 |
| 29 | `pair_bilinear_K_0*pi_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.06e+72 | noise>H_emp_OK_null | 0.17 |
| 30 | `pair_bilinear_K_0*e_K_0*ln2` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.51e+73 | noise>H_emp_OK_null | 0.15 |
| 31 | `pair_bilinear_K_0*e_K_0*gamma` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.38e+72 | noise>H_emp_OK_null | 0.17 |
| 32 | `pair_bilinear_K_0*e_K_0*zeta(2)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.94e+72 | noise>H_emp_OK_null | 0.16 |
| 33 | `pair_bilinear_K_0*e_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.09e+72 | noise>H_emp_OK_null | 0.17 |
| 34 | `pair_bilinear_K_0*e_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.40e+72 | noise>H_emp_OK_null | 0.17 |
| 35 | `pair_bilinear_K_0*ln2_K_0*gamma` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.27e+72 | noise>H_emp_OK_null | 0.18 |
| 36 | `pair_bilinear_K_0*ln2_K_0*zeta(2)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.57e+72 | noise>H_emp_OK_null | 0.16 |
| 37 | `pair_bilinear_K_0*ln2_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.13e+72 | noise>H_emp_OK_null | 0.17 |
| 38 | `pair_bilinear_K_0*ln2_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 5.13e+72 | noise>H_emp_OK_null | 0.17 |
| 39 | `pair_bilinear_K_0*gamma_K_0*zeta(2)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.55e+73 | noise>H_emp_OK_null | 0.16 |
| 40 | `pair_bilinear_K_0*gamma_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.64e+72 | noise>H_emp_OK_null | 0.16 |
| 41 | `pair_bilinear_K_0*gamma_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.72e+72 | noise>H_emp_OK_null | 0.16 |
| 42 | `pair_bilinear_K_0*zeta(2)_K_0*zeta(3)` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.28e+72 | noise>H_emp_OK_null | 0.17 |
| 43 | `pair_bilinear_K_0*zeta(2)_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.83e+72 | noise>H_emp_OK_null | 0.16 |
| 44 | `pair_bilinear_K_0*zeta(3)_K_0*G` | 2 | cascade_stable_null | field_standard_practice | 1.00e+70 | 3.13e+72 | noise>H_emp_OK_null | 0.21 |
| 45 | `triplet_log_K_0*pi_K_0*e` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.17e+72 | noise>H_emp_OK_null | 1.01 |
| 46 | `triplet_log_K_0*pi_K_0*ln2` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.14e+72 | noise>H_emp_OK_null | 0.99 |
| 47 | `triplet_log_K_0*pi_K_0*gamma` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.01e+72 | noise>H_emp_OK_null | 1.05 |
| 48 | `triplet_log_K_0*pi_K_0*zeta(2)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.51e+72 | noise>H_emp_OK_null | 1.06 |
| 49 | `triplet_log_K_0*pi_K_0*zeta(3)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.05e+72 | noise>H_emp_OK_null | 1.07 |
| 50 | `triplet_log_K_0*pi_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.11e+72 | noise>H_emp_OK_null | 1.02 |
| 51 | `triplet_log_K_0*e_K_0*ln2` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.12e+72 | noise>H_emp_OK_null | 1.07 |
| 52 | `triplet_log_K_0*e_K_0*gamma` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.20e+72 | noise>H_emp_OK_null | 1.10 |
| 53 | `triplet_log_K_0*e_K_0*zeta(2)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.80e+72 | noise>H_emp_OK_null | 1.03 |
| 54 | `triplet_log_K_0*e_K_0*zeta(3)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.93e+72 | noise>H_emp_OK_null | 0.97 |
| 55 | `triplet_log_K_0*e_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 2.38e+72 | noise>H_emp_OK_null | 1.13 |
| 56 | `triplet_log_K_0*ln2_K_0*gamma` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.05e+72 | noise>H_emp_OK_null | 1.08 |
| 57 | `triplet_log_K_0*ln2_K_0*zeta(2)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.15e+72 | noise>H_emp_OK_null | 0.95 |
| 58 | `triplet_log_K_0*ln2_K_0*zeta(3)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.25e+72 | noise>H_emp_OK_null | 0.93 |
| 59 | `triplet_log_K_0*ln2_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.08e+72 | noise>H_emp_OK_null | 1.02 |
| 60 | `triplet_log_K_0*gamma_K_0*zeta(2)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.17e+72 | noise>H_emp_OK_null | 0.93 |
| 61 | `triplet_log_K_0*gamma_K_0*zeta(3)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.02e+72 | noise>H_emp_OK_null | 1.09 |
| 62 | `triplet_log_K_0*gamma_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.28e+72 | noise>H_emp_OK_null | 0.92 |
| 63 | `triplet_log_K_0*zeta(2)_K_0*zeta(3)` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.71e+72 | noise>H_emp_OK_null | 0.91 |
| 64 | `triplet_log_K_0*zeta(2)_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.40e+72 | noise>H_emp_OK_null | 0.99 |
| 65 | `triplet_log_K_0*zeta(3)_K_0*G` | 3 | cascade_stable_null | field_standard_practice | 1.00e+70 | 1.06e+72 | noise>H_emp_OK_null | 1.05 |

---

## §5 Anomalies — none

The operator-named halt categories from M3.2b GREENLIGHT (*"cascade instability, gp/mpmath disagreement, anomalous K_iter pattern, anomalous verification_class"*) all return clean:

| Anomaly class | Threshold | Observed | Status |
|---|---|---|---|
| Cascade instability | any candidate with verdict ≠ `cascade_stable_null` | 0 of 65 | ✅ clean |
| gp/mpmath disagreement | any candidate where gp leg reports relation within H_empirical while mpmath cascade reports null | 0 of 65 (all gp `gp_noise_relation_above_H_empirical_confirms_null`) | ✅ clean |
| Anomalous K_iter pattern | K_iter that varies across P/2P/4P at the same candidate | 0 of 65 (K identical across cascade per candidate; verified manually for primary_full + by `cascade_stable_null` verdict for the rest) | ✅ clean |
| Anomalous verification_class | empirical_heuristic on a sub-basis where field_standard_practice was expected | 0 of 65 (1 proven_corollary + 64 field_standard_practice, all per H9 rules) | ✅ clean |
| Primary_full reproduction failure | M3.2b primary_full record differs from M3.2a at K, final_norm, or H_rigorous | 0 (identical at 71 digits across all 3 precisions) | ✅ clean |

**No halt-and-flag invocation required.**

---

## §6 Verification class distribution

Per H9 (4-class taxonomy, installed at `methodology/heuristics.md` H9 in commit `ca9c989`):

| Class | Count | Candidates |
|---|---:|---|
| `rigorous_theorem` | 0 | (would require relation-discovery + gp confirmation + residual pass; none observed; consistent with the bounded sub-question being a NULL claim) |
| `proven_corollary` | 1 | `primary_full` (n=15, K=29363, H_rigorous=1.04e+72 > 10^70 BBC parity; FBA T1+Cor 2 derivable from mpmath verbose-output per `harness/rigorous_bound.py`) |
| `field_standard_practice` | 64 | all 64 empirical sub-bases (BBC-calibrated empirical scaling H ≈ c·10^{P/(c·n)} capped at 10^maxcoeff_exp per U-MISSION-N R2.β; cascade stability across P/2P/4P) |
| `empirical_heuristic` | 0 | — |

Per operator H9 verbatim: *"Load-bearing classification. Any claim cited in M2.3 predicate, M3.1 harness, or M6 manuscript must carry a verification_class in its JSONL entry."* All 65 records carry `verification_class`.

---

## §7 Dual-field empirical reporting (post U-MISSION-N R2.β)

Per U-MISSION-N R2.β (installed in `harness/verify.py` commit `978c4ae`; documented in `_m2.3_calibration_anchor.md` §7.10 commit `eae8742`):

| Field | Source | Cap-active count | Cap-inactive count |
|---|---|---:|---:|
| `H_empirical_formula` | BBC scaling formula c·10^{P/(c·n)} verbatim | n/a | n/a |
| `H_empirical_operational` | `min(formula, 10^maxcoeff_exp)` | 64 (small n with formula > 10^70) | 1 (primary_full at n=15 with formula = 7.997e+69 ≤ 10^70) |

All 65 records contain both fields. The canonical §Results table in M6 uses `H_empirical_operational`. The §Discussion methods observation uses the formula-vs-operational contrast at small n per `m6_preflight_checklist.md` §3.4.

**Sanity check on R2.β:** primary_full (the only candidate at the full mission n=15) has formula = operational = 7.997e+69 — confirming the n=15 BBC-parity comparison is preserved unchanged by the R2.β extension. The R2.β cap activates only on the 64 empirical sub-bases at n ∈ {2, 3, 8, 9}.

---

## §8 H10 retrospective — would the H10 pre-canonical dry-run have surfaced this run's findings?

The H10-mandated full-regime dry-run (`harness/sweep.py --m31-extended-dry-run`, committed `5d75072` at 2026-05-16 ~11:34 JST, 113s wall-clock, 65 candidates clean) was the exact pre-canonical exercise that H10 prescribes.

| Finding class | Surfaced by H10 dry-run? | Notes |
|---|---|---|
| OverflowError on n ≤ 3 in `empirical_height` (the original M3.2b crash) | **YES** — the original H10 dry-run would have surfaced the OverflowError exactly because it exercises the same code path at canonical precision (P=2160) across all 65 sub-bases. R1 was applied before this dry-run, so the post-R1 dry-run ran clean. | H10 working as designed. |
| Bit-for-bit primary_full reproduction | NO — dry-run uses synthetic candidates with no PSLQ execution; cannot test mpmath determinism. | Out of H10's design scope; this is a M3.2-specific check. |
| Field_standard_practice vs proven_corollary assignment | YES — dry-run records `verification_class` per H9; all 65 dry-run candidates correctly returned `field_standard_practice` (rigorous_tier=False on dry-run, by construction). | H10 working as designed. |

**Verdict: H10 functioned exactly as designed.** The H10-mandated pre-canonical dry-run would have surfaced the original M3.2b OverflowError if it had existed; it did exist for ~1 hour pre-R1; once R1 was applied, the H10 dry-run was clean; and the canonical re-run then ran clean.

This validates the U-MISSION-N RESOLUTION sequence (R1 mechanical fix → R2.β semantic refinement → H10 install → §7.10 predicate addendum → 9th mutation_log → H10 dry-run → canonical re-run).

---

## §9 Authority chain (commits on `main`)

The M3.2b clean-null result is supported by the following commits, all on `papanokechi/khinchin-k0-bounded` `main`:

| Commit | Date (JST) | Purpose |
|---|---|---|
| `ca9c989` | 2026-05-15 ~23:00 | gold/M2 tag at U-MISSION-L two-tier predicate (M2.3 predicate locked) |
| `e038902` | 2026-05-15 ~late | M3.1 harness implementation |
| `0815db8` | 2026-05-16 ~08:25 | U-MISSION-M3.2 phase split + pre-execution corrections (gp dps + 4-mode argparse) |
| `d55ffbc` | 2026-05-16 ~09:38 | M3.2a canonical primary cascade output (clean null at H_rig=1.04e+72) |
| `66ca169` | 2026-05-16 ~10:00 | M6 preflight checklist (H8 Bailey 1998 forward-flag + apples-to-stronger-apples framing) |
| `4fa7ee9` | 2026-05-16 ~10:50 | M3.2b HALT (U-MISSION-N catch: OverflowError at n=2; FAILED_PARTIAL JSONL preserved) |
| `16aaad6` | 2026-05-16 ~11:00 | U-MISSION-N Step 1: R1 mpmath fallback for `empirical_height` overflow |
| `978c4ae` | 2026-05-16 ~11:15 | U-MISSION-N Step 2: R2.β dual-field JSONL output |
| `eae8742` | 2026-05-16 ~11:25 | U-MISSION-N Steps 3-5: §7.10 predicate addendum + H10 install + 9th mutation_log + M6 preflight §3.4 |
| `8045bf8` | 2026-05-16 ~11:30 | U-MISSION-N Step 6 prep: extend `--m31-extended-dry-run` to full 65-candidate regime per H10 |
| `5d75072` | 2026-05-16 ~11:35 | U-MISSION-N Step 6 DONE: H10-mandated full-regime dry-run CLEAN across all 65 sub-bases |
| *(pending)* | 2026-05-16 ~12:30 | M3.2b canonical re-run output + this summary |

---

## §10 AEAL discipline notes

- **Mutation budget at M2 milestone-block: 0/1 still consumed.** Per operator U-MISSION-N RESOLUTION verbatim: R1 + R2.β + H10 install are field-map updates per U-MISSION-L + U-MISSION-J precedents; NOT a hypothesis mutation. The hypothesis ("test for integer relations in B_D(C)") is unchanged; only the empirical-reporting structure was extended.
- **Halt count this segment: 0.** Operator U-MISSION-N forecast (*"If --m31-extended-dry-run surfaces additional findings: halt and surface before canonical re-run"*) gave the halt-condition explicitly; dry-run cleared 65/65, canonical re-run cleared 65/65, no halt invoked.
- **AEAL maturation curve (updated):**
  | Milestone | Halts |
  |---|---|
  | M1 | 4 |
  | M2.1 | 1 |
  | M2.2 | 0 |
  | M2.3 | 1 (Catch #2 resolved) |
  | M3.1 implementation | 0 |
  | M3.2a execution | 0 |
  | M3.2b execution (first attempt) | 1 (Catch #3 / U-MISSION-N OverflowError) |
  | U-MISSION-N resolution + M3.2b re-run | 0 |

  Total mission-life halts: **6**. Halt-and-flag pattern preserved throughout; operator's M2.1 GREENLIGHT framing (*"the back half runs cleaner"*) continues to be validated.

- **Process-to-content ratio for this commit batch:** the JSONL output (350 KB canonical data) + this summary (~25 KB analysis with embedded per-candidate table) are content. The audit harness and console log are audit-trail artifacts. The plan.md 17th addendum is the process companion. Strongly content-side.

- **Rule 6 audit:**
  - Zero portal interactions during M3.2b canonical re-run.
  - One planned `git push` for canonical output + summary + plan.md update.
  - No `selected.md` edits (frozen at gold/M1).
  - No `_m2.3_calibration_anchor.md` §7.1-§7.9 edits (frozen at gold/M2; §7.10 was authorized by U-MISSION-N RESOLUTION Step 3).
  - No `methodology/heuristics.md` edits (H10 already installed at `eae8742`; nothing further needed).

---

## §11 Operator decision surface — single decision: M3 closure

Per the operator's M3.2b GREENLIGHT verbatim (*"If summary shows all 64 clean null with no anomalies: M3 closes cleanly, M4 ready for greenlight on operator review of summary"*):

- **Aggregate verdict:** all 64 empirical sub-bases clean null + primary_full bit-for-bit reproduction (so technically 65, including the rigorous tier).
- **Verification class distribution:** 1 proven_corollary + 64 field_standard_practice — exactly the two-tier structure the predicate prescribes.
- **No anomalies surfaced.**

**Recommendation: M3 CLOSES CLEANLY at this commit.** M4 (Brief §M4: synthesis-and-staging — symbolic-side companion analysis + manuscript-preparation prep) ready for greenlight on operator review of this summary.

### Forward-flagged, non-blocking:

- **Bailey 1998 H8 paper-read** remains deferred conditional on M6 outcome per `m6_preflight_checklist.md` §1 (since M6 will cite the rigorous tier as proof-of-bound per the proven_corollary classification of primary_full).
- **Apples-to-stronger-apples framing** for M6 §Introduction/§Results — primary_full H_rigorous = 10^72 beats BBC's H = 10^70 by 2 orders, **but on the complement (EF1-excluded) basis** — `m6_preflight_checklist.md` §2.
- **Operational-bound capping methodology observation** for M6 §Discussion — `m6_preflight_checklist.md` §3.4 (added this U-MISSION-N segment).
- **Mathlib4 deep-build verification** for any Lean formalization in M4-M5 — deferred per H7 risk-acknowledgement at gold/M1.

---

*Summary generated 2026-05-16 ~12:40 JST. Audit script: `harness/_audit_m32b_summary.py`. Raw audit output: `harness/sweep_output/_m32b_audit_output.txt`. Per-candidate table source: `harness/sweep_output/_m32b_table.md`.*
