# M3.1 / M3.2 Harness — Sweep Output

This directory contains per-sweep JSONL output from `harness/sweep.py`.

**M3.2 phase split** (installed 2026-05-16 ~08:22 JST per operator U-MISSION-M3.2):

| Mode | Filename | Gating | Wall-clock | dry_run |
|---|---|---|---|---|
| `--dry-run` | `m31_dryrun_<TS>.jsonl` | ungated | < 1 min | true |
| `--m31-extended-dry-run` | `m31_extended_dryrun_<TS>.jsonl` | ungated | ~10-15 min | true |
| `--m32-primary-measurement` | `m32a_primary_cascade.jsonl` | `--m32-primary-greenlighted` | ~90-110 min | false (canonical) |
| `--full` | `m32b_empirical_sweep.jsonl` | `--m32-full-greenlighted` + prior M3.2a | ~3 hours | false (canonical) |

Canonical M3.2a/M3.2b output filenames are fixed (no timestamp) and the harness REFUSES TO OVERWRITE an existing canonical file — single canonical execution per operator. To re-run, the operator must explicitly remove the existing file first.

**Per-candidate record schema** (top-level keys, post-2026-05-16):

| Key | Type | Meaning |
|---|---|---|
| `family` | str | Sub-basis family (e.g. `pair_log_K_0*pi`) |
| `indices` | list[int] | Indices into `basis.BASIS_LABELS` |
| `labels` | list[str] | Human-readable labels |
| `n` | int | Sub-basis dimension |
| `maxcoeff_exp` | int | log10 of PSLQ `maxcoeff` |
| `precisions` | list[int] | Cascade precision triple |
| `maxsteps_per_prec` | list[int] | PSLQ iteration cap per precision |
| `rigorous_tier` | bool | True for primary_full (rigorous Tier 2 reporting) |
| `H_empirical` | float | BBC c≈2.06 calibrated empirical height at primary P |
| `H_rigorous_min` | float | min over cascade levels of FBA T1+Cor2 H_rigorous |
| `cascade` | dict | Per-precision PSLQ results (see below) |
| `gp_lindep` | dict | gp lindep second-leg result (see below) |
| `pslq_residual_check` | dict | False-positive rejection check (if a relation was found) |
| `verification_class` | str | H9 class |
| `ef1_only` | bool | True if indices ⊂ EF1 (BBC-grandfathered subset) — enforced False |
| `has_complement` | bool | True if indices ∩ COMPLEMENT_INDICES non-empty — enforced True |
| `_candidate_elapsed_s` | float | Wall-clock for this candidate |
| `_dry_run` | bool | Mirrors header `dry_run` |

**`cascade` dict:**

```
cascade: {
  verdict: "cascade_stable_null" | "cascade_stable_relation" | "cascade_unstable",
  per_precision: [
    {P, iteration_count, final_norm, elapsed_s, H_rigorous, relation,
     termination_reason, termination_line, last_norm_in_cancellation,
     verbose_lines_captured, error}
  ],
  H_rigorous_min_across_cascade: float
}
```

`termination_reason` is one of: `relation_found`, `maxcoeff_reached`, `precision_exhausted`, `maxsteps_or_norm_break`, `unknown`. This is mpmath's reported termination behavior parsed from the `verbose=True` stdout — it satisfies the operator's "mpmath verbose H-matrix diagonals summary" surfacing requirement (mpmath does not expose H-matrix internals directly per `rigorous_bound.py` D1; `final_norm` is the captured max-all-entries proxy).

**`gp_lindep` dict:**

```
gp_lindep: {
  relation: [a, b, c, ...] | null,
  error: null | str,
  max_abs_coefficient: int | null,
  within_empirical_bound: bool | null,   // max|m_i| <= H_empirical
  gp_verdict: str,                       // one of:
                                         //   "gp_returned_no_relation_confirms_null"
                                         //   "gp_noise_relation_above_H_empirical_confirms_null"
                                         //   "gp_claims_relation_within_bound_CASCADE_DISAGREES"
                                         //   "gp_relation_within_bound_pending_consistency_check"
                                         //   "gp_relation_above_H_empirical_CASCADE_DISAGREES"
                                         //   "skipped" | "gp_error:..."
  stdout_tail: str,
  stderr_tail: str
}
```

PARI/GP `lindep` performs LLL and always returns a "best approximate" integer combination, even when no genuine relation exists within bound. The `within_empirical_bound` flag is the practical interpretation: `max|m_i| <= H_empirical` ⇒ gp claims a relation within the publishable bound; otherwise gp returned noise (confirms no relation within bound).

Per the 2026-05-16 operator correction (U-MISSION-M3.2), gp_lindep runs at `dps = primary_P` (not `primary_P // 2`). Second leg must be at equal-or-higher precision than primary to function as a real independence check.

**Mode wall-clock estimates (warm-cache, per `precision_budget.md` §6.4):**

| Mode | Candidates | PSLQ wall-clock | gp_lindep | Total |
|---|---|---|---|---|
| `--dry-run` | 3 (small precision) | < 1 s | skipped | < 1 s |
| `--m31-extended-dry-run` | 1 (n=15, reduced precisions 540/1080/2160) | ~3-5 min | ~5 s | ~10-15 min (cold cache) |
| `--m32-primary-measurement` | 1 (n=15, rigorous tier P=2160/4320/8640) | ~91 min | ~5-20 s | ~90-110 min (cold cache) |
| `--full` | 65 (1 primary + 64 empirical) | ~3 h | ~3-5 min total | ~3 hours |

**Evidence committed in this directory:**

- `m3.1_sweep_dry-run_20260515_225716.jsonl` — first end-to-end pipeline validation (pre-phase-split; legacy schema).
- `m31_dryrun_<TS>.jsonl` — pipeline mechanics dry-run output (post-phase-split, may be deleted at operator discretion).
- `m32a_primary_cascade.jsonl` — **CANONICAL M3.2a measurement** (single execution, M6 rigorous tier input).
- `m32b_empirical_sweep.jsonl` — **CANONICAL M3.2b measurement** (single execution, only after clean M3.2a; M6 empirical-tier sub-basis structure).

