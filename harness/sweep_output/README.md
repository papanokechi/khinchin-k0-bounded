# M3.1 Harness — Sweep Output

This directory contains per-sweep JSONL output from `harness/sweep.py`.

**File naming convention:** `m3.1_sweep_<mode>_<YYYYMMDD>_<HHMMSS>.jsonl`

- `<mode>` ∈ `{dry-run, primary-only, full}`
- One JSONL line per candidate sub-basis (+ a `_meta: true` header line and footer line)

**Per-candidate record schema** (top-level keys):

| Key | Type | Meaning |
|---|---|---|
| `family` | str | Sub-basis family (e.g. `pair_log_K_0*pi`) |
| `indices` | list[int] | Indices into `basis.BASIS_LABELS` |
| `labels` | list[str] | Human-readable labels for the indices |
| `n` | int | Sub-basis dimension |
| `maxcoeff_exp` | int | log10 of PSLQ `maxcoeff` |
| `precisions` | list[int] | Cascade precision triple (P, 2P, 4P) |
| `maxsteps_per_prec` | list[int] | PSLQ iteration cap per precision |
| `rigorous_tier` | bool | True for primary_full (rigorous Tier 2 reporting) |
| `H_empirical` | float | BBC c≈2.06 calibrated empirical height at primary P |
| `H_rigorous_min` | float | min over cascade levels of FBA T1+Cor2 H_rigorous |
| `cascade` | dict | Per-precision PSLQ results (see below) |
| `gp_lindep` | dict | gp lindep second-leg result (or `{relation: null, error: 'skipped'}`) |
| `pslq_residual_check` | dict | False-positive rejection check (if a relation was found) |
| `verification_class` | str | H9 class: `rigorous_theorem`/`proven_corollary`/`field_standard_practice`/`empirical_heuristic` |
| `ef1_only` | bool | True if indices ⊂ EF1 (BBC-grandfathered subset) — should be False after construction filter |
| `has_complement` | bool | True if indices ∩ COMPLEMENT_INDICES is non-empty — enforced True by `basis.enumerate_sub_bases` |
| `_candidate_elapsed_s` | float | Wall-clock for this candidate |

**Cascade dict structure:**

```
cascade: {
  verdict: "cascade_stable_null" | "cascade_stable_relation" | "cascade_unstable",
  per_precision: [
    {P, iteration_count, final_norm, elapsed_s, H_rigorous, relation, error}
  ],
  H_rigorous_min_across_cascade: float
}
```

**Mode wall-clock estimates (per `precision_budget.md` §6.4):**

| Mode | Candidates | Wall-clock estimate |
|---|---|---|
| `--dry-run` | 3 (small-precision sentinels) | < 1 s |
| `--primary-only` | 1 (primary_full n=15 rigorous tier at P=2160/4320/8640) | ~90 min |
| `--full` (gated by `--m32-greenlighted`) | 65 (1 primary + 64 empirical sub-bases) | ~3 hours |

**Evidence committed in this directory:**

- `m3.1_sweep_dry-run_20260515_225716.jsonl` — first end-to-end pipeline validation
  (3 candidates: 1 cascade_unstable demo + 2 cascade_stable_null demo; gp leg skipped per dry-run config; H9 verification_class assignment verified)

Future M3.2 measurement output (`m3.1_sweep_full_*.jsonl`) is committed at M3 close; intermediate dry-runs may be deleted by operator at discretion.
