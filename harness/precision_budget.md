# harness/precision_budget.md

# M2.3 precision-budget derivation — STATUS: U-MISSION-L TWO-TIER PREDICATE INSTALLED

**Mission:** unsolved-relay
**Milestone:** M2.3 (success-predicate calibration)
**Authority:** Operator U-MISSION-K (2026-05-15 ~21:14 JST) + U-MISSION-L (2026-05-15 ~21:36 JST)
**Sequence position:** U-MISSION-K Step 1 + U-MISSION-L Steps 1-3 complete; Step 4 (predicate draft in `literature/_m2.3_calibration_anchor.md` §7) executed in same commit batch. **HALT for operator ratification before M3.1 implementation.**
**Subordinate to:** Brief §M2.3; H7 (capability functional verification); H8 (paper-read on dependency literature claims); H9 (theorem-vs-heuristic classification, **installed at U-MISSION-L**)

---

## §1 Scope and mandate

Per operator U-MISSION-K, this document:

- Derives the basis dimension `n` for B_D(C) at D=6, |C|=7, with explicit inclusion/exclusion of the constant-1 row and log K_0 row.
- Applies H8 paper-read to the PSLQ confidence relation source (claimed primary: Ferguson–Bailey–Arno 1999).
- Reports wall-clock estimates for mpmath PSLQ at dim=15 across precisions P ∈ {500, 1000, 2000, 4000} dps.
- Commits to a specific (P, H_target) pair for the M2.3 success predicate **conditional on operator resolution of the H8 finding surfaced below.**
- Surfaces a halt-class finding to operator (Step 2 of the U-MISSION-K sequence).

**This document does NOT yet commit to a final (P, H_target) pair.** Three candidate pairs are recorded in §6 with their assumptions; operator selects after resolving the §7 halt.

---

## §2 Basis dimension derivation

The bounded sub-question from `targets/selected.md` §2 (frozen at gold/M1) is:

```
B_D(C) = { 1, K_0, K_0^2, …, K_0^D, log K_0 } ∪ { K_0 · c : c ∈ C }
```

with D ≤ 6 and C ⊆ { π, e, log 2, γ, ζ(2), ζ(3), G } (the 7-element C-set ratified by operator U-MISSION-K).

### §2.1 Element count

| Subset | Members | Count |
|---|---|---|
| Constant row | `1` | 1 |
| Pure powers (non-trivial) | `K_0, K_0^2, K_0^3, K_0^4, K_0^5, K_0^6` (D=6) | 6 |
| log row | `log K_0` | 1 |
| Bilinear rows | `K_0 · π, K_0 · e, K_0 · ln 2, K_0 · γ, K_0 · ζ(2), K_0 · ζ(3), K_0 · G` | 7 |
| **Total dimension n** | (with constant + with log K_0) | **15** |

### §2.2 Variants explicitly considered

- **n = 15** (constant included + log K_0 included) — **primary; this is what the M3.1 harness will use.**
- **n = 14** (constant included, log K_0 excluded — i.e., predicate scope only) — would apply if M2.3 ran the PSLQ scan on the *complement-only* basis. **Rejected**: PSLQ should run on the full basis B_D(C) and the predicate's positive/negative outcomes are then *restricted* to relations not living in Excluded Family 1 (pure-power subset). Running PSLQ on the partial basis would lose the ability to *detect* relations that have nonzero coefficients in Excluded Family 1 (which we want to detect-and-classify-as-grandfathered, not blind-spot).
- **n = 14** (constant excluded, log K_0 included — operator's selected.md §2 literal enumeration) — would apply if the PSLQ basis omits the constant-1 row. **Rejected**: operator's §6.5 binding requirement explicitly names `{1, K_0, K_0², …, K_0^D}` as Excluded Family 1, which presupposes 1 IS in the basis (otherwise nothing to exclude). The constant-1 row is also necessary for PSLQ to detect inhomogeneous relations (a_0 + a_1 K_0 + … = 0 with a_0 ≠ 0).
- **n = 13** (no constant, no log) — rejected for both reasons above.

**Commitment: n = 15.** Documented at `targets/selected.md` §5.A as part of the U-MISSION-G refinement record's "added the explicit constant 1 in B_D(C)" note.

---

## §3 H8 paper-read of PSLQ confidence-relation source

### §3.1 Primary source retrieval and provenance

| Field | Value |
|---|---|
| Citation | Ferguson, H. R. P., Bailey, D. H., and Arno, S. (1999). _Analysis of PSLQ, an integer relation finding algorithm._ Math. Comp. **68** (225), pp. 351–369. |
| DOI | 10.1090/S0025-5718-99-00995-3 |
| Source URL | `https://www.davidhbailey.com/dhbpapers/cpslq.pdf` (Bailey's personal archive at LBNL; canonical preprint for the Math. Comp. paper, dated 03 July 1997, "to appear (1999)" reference at p.1) |
| Local cache | `harness/_pslq_candidates/cpslq.pdf` |
| File size | 218,997 bytes |
| SHA-256 | `3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5` |
| Pages | 26 |
| Extraction method | `pypdf.PdfReader().pages[i].extract_text()`; 51,322 chars; saved to `harness/_pslq_candidates/fba1999_text.txt` |
| Retrieval timestamp | 2026-05-15 ~21:30 JST |

**Title-page match** (page 1 verbatim, pypdf-extracted):
> "ANAL YSIS OF PSLQ, AN INTEGER RELA TION FINDING ALGORITHM
> Helaman R. P. Ferguson, David H. Bailey, Steve Arno
> 03 July 1997
> … Ref: Mathematics of Computation , to appear (1999)"

The SHA-256-stamped PDF IS the primary source for FBA 1999.

### §3.2 What the paper actually proves about precision-vs-relation-norm

**Theorem 1 (rigorous, paper-read verbatim from p.10 / @9607–@9700):**
> "Let x ≠ 0 ∈ K^n. Suppose that for any relation m of x and for any matrix A ∈ GL(n, O(K)) there exists a unitary matrix Q ∈ U(n−1) such that H = AH_xQ is lower trapezoidal and all of the diagonal elements of H[…non-zero…]. Then M_x ≥ 1/max|h_{i,i}|."

That is: **the rigorous lower bound on the smallest relation norm M_x is the inverse of the largest diagonal element of the H matrix at the current PSLQ iteration.** This is a per-iteration certificate.

**Theorem 3 (paper-read verbatim from p.15 / @24130):**
> "Let M_x be the smallest possible norm of any relation for x. Let m be any relation found by PSLQ(τ). For all γ > √(4/3) for real vectors […], |m| ≤ γ^{n−2} M_x."

That is: any relation PSLQ finds is **at most γ^{n−2}** times worse than the smallest possible.

**Corollary 2 (paper-read verbatim from p.14 / @22917):**
> "PSLQ(τ) constructs a relation in less than (n choose 2) · log_τ(γ^{n−1} M_x) iterations."

**Parameter ranges (paper-read verbatim from p.5 / §3 Definition 5):**
> "Fix the real number γ > 2/√3 or γ > √2 or γ = ∞ for the real, complex, and quaternion cases respectively."

For the real case (our case): **γ_min = 2/√3 ≈ 1.15470054**. With n = 15:
- `γ^{n−2}` = `γ^{13}` ≈ 6.49 (Theorem 3 PSLQ-vs-smallest-relation overshoot factor).

### §3.3 What the paper does NOT contain

A direct search for the claimed relation **`H ≈ 10^{P/n}`** (i.e., "at precision P digits, PSLQ certifies absence of integer relations with coefficient height ≤ 10^{P/n}") was performed across the full 51,322 chars of extracted text. **No literal statement of this relation as a theorem appears in FBA 1999.**

What does appear:
- §8 Computer Implementation, p.18 (@29593–@29800): "Using double precision (i.e., 64-bit) arithmetic, relations of two or three digits in size can be recovered for n up to five or so. Beyond this level, precision is quickly exhausted, and recovered relations and norm bounds are meaningless." This is a **descriptive, empirical** statement of the precision-vs-recoverable-relation-size phenomenon. It does NOT formalize `H ≈ 10^{P/n}`.
- Theorem 1's certificate `M_x ≥ 1/max|h_{i,i}|` IS the rigorous statement of the precision-vs-norm-bound relationship. The h_{i,i} diagonal entries decrease as PSLQ iterates, with their magnitudes governed by the floating-point precision P. The folklore `H ≈ 10^{P/n}` is the **empirical scaling** of `max|h_{i,i}|` against P at typical PSLQ convergence — but this scaling is **not proven as a theorem** in FBA 1999.

### §3.4 The lit-009 statement reassessed

Previous lit-009 entry text (`unverified_abstract_only`):
> "Algorithm bounds: at precision P, PSLQ certifies absence of integer relations with coefficient height ≲ 10^(P/dim)."

H8 verdict on this statement:
- **CORRECT as empirical heuristic** (consistent with FBA 1999 framework + BBC 1997 empirical numbers).
- **MISLEADING as theorem citation** (does not appear as a stated theorem in FBA 1999; the rigorous theorem statements are M_x ≥ 1/max|h_{i,i}| and |m| ≤ γ^{n−2} M_x).

The lit-009 statement is **folklore-grade**, not **theorem-grade**. Both labels matter for AEAL claim provenance.

---

## §4 BBC 1997 empirical confidence factor — reconciliation with FBA 1999

From lit-002 (BBC 1997 §4 Test 1, paper-read at M2.1 close):
- n = 51 (basis {1, K_0, K_0², …, K_0^50})
- P = 7350 dps
- H = 10^70 (the reported height bound)

Empirical confidence factor c = P / (n · log₁₀ H) = **7350 / (51 × 70) ≈ 2.0588**

If `H ≈ 10^{P/n}` were a literal certificate, BBC would have stated H = 10^{7350/51} ≈ 10^144. They did NOT — they stated H = 10^70, which is **2.06× more conservative** than the folklore heuristic at the same (P, n).

**This is consistent with FBA 1999 Theorem 3's `γ^{n−2}` overshoot factor** (at n=51, γ_min=1.1547, γ^{49} ≈ 633), but the BBC-1997 reported factor of ~2× is more conservative than even the worst-case Theorem 3 overshoot. The BBC factor likely reflects:
- Numerical-precision safety buffer (PSLQ at floating-point precision P loses some effective digits to roundoff)
- Practical maxsteps cutoff before theoretical convergence
- A choice to report a conservative bound a reader can rely on

The Bailey-Borwein-Plouffe community uses **empirical c-factor calibration** against published examples (BBC 1997 c≈2.06 is the canonical benchmark), NOT a direct invocation of FBA 1999's theorem.

---

## §5 mpmath.pslq's actual return contract — REVISED at U-MISSION-L

**Pre-U-MISSION-L reading (now superseded; preserved for audit):**
> mpmath.pslq does NOT expose the rigorous certificate `M_x ≥ 1/max|h_{i,i}|` from FBA 1999 Theorem 1. The diagonal entries of the internal H matrix are NOT returned to the caller. The harness's negative-result claim is therefore structurally weaker than the rigorous Theorem-1 certificate.

**§5 REVISED (U-MISSION-L investigation, evidenced by `harness/rigorous_bound.py` module docstring and demo output):**

The pre-U-MISSION-L reading was correct that the H-matrix diagonals are not in the return value, but was INCOMPLETE in two respects:

1. **mpmath.pslq's `verbose=True` mode prints a Theorem-1-style lower bound on M_x at every iteration**, computed internally as:

   ```python
   recnorm = max(abs(h) for h in H.values())   # max over ALL entries of H
   norm = ((1 << (2*prec)) // recnorm) >> prec # = floor(1 / max|H|)
   norm //= 100                                # 100x safety factor
   ```

   This is captureable via stdout redirection (`io.StringIO` + `contextlib.redirect_stdout`), parseable via regex, and gives a **rigorous lower bound on M_x = 100 × reported_norm** via FBA 1999 Theorem 1 combined with the elementary inequality `max_{i,j}|H[i,j]| ≥ max_j|h_{j,j}|`.

2. **FBA 1999 Corollary 2 gives a second, independent rigorous lower bound** on M_x derivable from iteration count alone: if PSLQ ran K iterations without termination, then any relation has `M_x > exp((K - 2·dim_R·n^3) / (2·dim_R·n^2))`. For n=15 (real case), Cor 2 becomes non-trivial only when K > 6,750 iterations (the integer-relation lower bound M_x ≥ 1 floor).

**The rigorous bound thus IS available from mpmath outputs** — via `harness/rigorous_bound.py` (verbose-mode stdout capture + parsing for Theorem 1, plus iteration-count formula for Corollary 2). The M3.1 harness can report **both tiers** in its predicate evidence:
- Tier 1 (empirical, `field_standard_practice` per H9): BBC-1997-calibrated `H_empirical ≈ 10^{P/(c·n)}` with c ≈ 2.06.
- Tier 2 (rigorous, `proven_corollary` per H9): `H_rigorous = max(100·reported_norm, exp((K-2·n^3)/(2·n^2)))` per FBA 1999 Theorem 1 / Corollary 2.

### §5.1 Four divergences from FBA 1999 (paper-read derived, see `rigorous_bound.py` module docstring)

| ID | Divergence | Practical impact |
|---|---|---|
| D1 | mpmath uses `max_{i,j} \|H[i,j]\|` (all entries); FBA T1 uses `max_j \|h_{j,j}\|` (diagonal only) | mpmath's bound is rigorous but strictly weaker; H_rigorous is several decades smaller than optimal FBA T1 bound |
| D2 | mpmath uses γ = √(4/3) exactly; FBA Def 5 requires γ > √(4/3) strict | Boundary case covered by Bailey 1998 expository paper (mpmath's stated source); Theorem 1 + Corollary 2 unaffected; Theorem 3 (overshoot) requires Bailey 1998 H8 paper-read if cited |
| D3 | mpmath cites Bailey 1998, NOT FBA 1999, in docstring | Forward-flagged: Bailey 1998 H8 paper-read recommended if rigorous tier is load-bearing in M2.3 predicate |
| D4 | mpmath applies `norm //= 100` safety factor | Conservative (rigor preserved); reported_norm = 0 is uninformative; H_rigorous = 100·reported_norm |

**None of D1-D4 invalidates Corollary 2 applicability.** The two-tier predicate is structurally sound; D2 / D3 are forward-flagged for downstream H8 strengthening at operator discretion.

### §5.2 Achievable rigorous bound regime — empirical (n=15)

Three measured points from `harness/rigorous_bound.py` demo (see `harness/_rigorous_bound_demo_output.txt`):

| K (iter) | dps | Elapsed | final_norm | H_rigorous_Thm1 = 100·norm | H_rigorous_Cor2 |
|---:|---:|---:|---:|---:|---:|
| 2000 | 100 | 2.0 s | 624 | 6.24 × 10⁴ | trivial (K < 6750) |
| 2000 | 500 | 2.5 s | 624 | 6.24 × 10⁴ | trivial (K < 6750) |
| 5000 | 500 | 6.3 s | 1.43 × 10¹⁰ | **1.43 × 10¹²** | trivial (K < 6750) |

**Growth pattern observed:** mpmath's reported norm grows roughly geometrically with iteration count K above the initial integer-truncation floor (norm = 0 for K ≲ 900 at n=15). Extrapolating from K=2000 → 5000 (norm: 624 → 1.43×10¹⁰; growth rate ≈ 1 decade per ~400 iterations), reaching **H_rigorous = 10⁷⁰** at n=15 requires K ≈ 50,000+ iterations.

Wall-clock estimate at dps=500: 50,000 iter × 1.3 ms/iter ≈ **65 s per PSLQ run** to natural termination at H_rigorous = 10⁷⁰. At dps=2160 (BBC parity, Option α): ~2-3× slower → **~150-200 s per run**. 96h budget accommodates several thousand such runs.

**Conclusion: BBC-parity rigorous bound H_rigorous = 10⁷⁰ at n=15 IS achievable in M3.1, contingent on raising mpmath's `maxsteps` from default 100 to ~100,000.** Empirical tier (10⁷⁰ at dps=2160) and rigorous tier (10⁷⁰ at K ≈ 50-100k iter) **converge at the same H_target = 10⁷⁰** in the M3.1 regime — the two-tier predicate is operationally compatible with Option α.

---

## §6 Wall-clock benchmark (mpmath PSLQ at dim=15)

Benchmark script: `harness/_bench_pslq_dim15.py` (executed 2026-05-15 ~21:30 JST).

Basis: `{1, K_0, K_0^2, …, K_0^6, log K_0, K_0·π, K_0·e, K_0·ln2, K_0·γ, K_0·ζ(2), K_0·ζ(3), K_0·G}` — exactly n = 15 as derived in §2.

Parameters: `maxcoeff=10^60`, `maxsteps=2000`, `tol=10^{-int(P·0.6)}` (precision-cascade heuristic per H1).

| P (dps) | Wall-clock (s) | Result | H_target (BBC-parity c=2.06) |
|---:|---:|---|---|
| 500 | 4.16 | null | 10^16.19 |
| 1000 | 5.35 | null | 10^32.38 |
| 2000 | 16.28 | null | 10^64.76 |
| 2160 | (extrapolated) ~18-20 | (would be null) | 10^69.94 ≈ **10^70 (BBC parity)** |
| 4000 | 37.81 | null | 10^129.52 |

### §6.1 Feasibility verdict

96h wall-clock cap (Brief §M3.2) at 38 s per run at P=4000 dps accommodates ~9000 runs. At BBC-parity P=2160 dps: ~17,000 runs. **No infeasibility surfaces. No U-MISSION-K wall-clock surface.**

### §6.2 (P, H_target) COMMITMENT — U-MISSION-L Option α SELECTED

Operator U-MISSION-L (2026-05-15 ~21:36 JST) verbatim:
> "(P, H_target) selection: ADOPT Option α (P=2160, H=10^70 BBC parity) for the empirical scope claim. BBC's exact precision-per-dimension makes M6 directly comparable. Cost differential vs Option β is negligible at 96h budget; legitimacy gain is non-negligible. Option γ rejected. Option β rejected."

**Committed pair for the M2.3 success predicate:**

| Tier | Confidence relation | P (dps) | H_target | c-factor | Verification class (per H9) |
|---|---|---:|---:|---:|---|
| Tier 1 (empirical) | H ≈ 10^{P/(c·n)} | 2160 | **10⁷⁰** | 2.06 (BBC strict parity) | `field_standard_practice` |
| Tier 2 (rigorous) | FBA T1 / Cor 2 via `rigorous_bound.py` | 2160 | **10⁷⁰** (at K ≈ 50–100k iter; see §5.2) | n/a (theorem-derived) | `proven_corollary` |

Wall-clock per single PSLQ run at this (P, H_target):
- Empirical-mode (maxsteps=2000, terminate-on-maxcoeff): ~18 s (§6 table extrapolated)
- Rigorous-mode (maxsteps=100,000, run to natural termination): ~150-200 s (§5.2 extrapolated)

96h budget accommodates ~1700 rigorous-mode runs OR ~17,000 empirical-mode runs. The M3.1 cascade (P, 2P, 4P stability check across the predicate's non-Excluded-Family basis sweeps) is comfortably within budget.

Options β and γ are **rejected per operator**; preserved in §6.3 (historical) for audit only.

### §6.3 Rejected options — preserved for audit trail

| Option | Why rejected | Verbatim operator language |
|---|---|---|
| β — P=2000, H=10⁶⁰, c≈2.4 | "Cost differential vs Option β is negligible at 96h budget; legitimacy gain is non-negligible." | U-MISSION-L |
| γ — P=1500, H=10⁴⁸, c=2.06 | "Option γ rejected." | U-MISSION-L |

CLI default recommendation at §7 was Option β; operator selected α with explicit reasoning (BBC strict-parity → M6 directly comparable). Operator override absorbed; α is the commitment.

### §6.4 Cascade arithmetic — M2.3 ratification follow-up (2026-05-15 ~22:30 JST)

Per operator post-ratification directive (2026-05-15 22:03:50 JST): "Update harness/precision_budget.md §6 with cascade verification wall-clock arithmetic. The negative predicate requires cascade stability at 2P and 4P, which means 3× the single-run wall-clock per candidate null verification."

**Measured cascade benchmark** (`harness/_bench_cascade_wallclock.py`; output: `harness/_bench_cascade_output.txt`).

Per-precision single-run cost at the **n=15 mission basis B_D(C)**, `maxsteps=2000` (empirical tier), warm-cache:

| P (dps) | PSLQ wall-clock | iter/s | Extrapolated maxsteps=100k (rigorous tier) |
|---:|---:|---:|---:|
| 2160 | **12.30 s** | 163 | 615 s = 10.2 min |
| 4320 | **28.20 s** | 71 | 1410 s = 23.5 min |
| 8640 | **69.21 s** | 29 | 3461 s = 57.7 min |

**Empirical-tier cascade total (P + 2P + 4P) = 109.7 s per candidate.** Operator's pre-benchmark estimate "cascade × 3 ≈ 50-60s per candidate" was at the single-precision×3 level; the actual cascade-of-3-precisions is ~2× higher because per-precision wall-clock scales super-linearly in P (mpmath's mpf arithmetic is O(M(P)·log P) where M is multiplication cost).

**Rigorous-tier cascade total = 5486 s = 91.4 min per primary cascade.** This is the cost of running PSLQ to natural termination at H_rigorous=10⁷⁰ across all three cascade precisions for the primary n=15 measurement.

**Cold-cache caveat (operationally important):** First-call basis build at P=8640 = 1080 s = 18 min (mpmath internal cache misses for `zeta(2)`, `zeta(3)`, `log(2)`, `catalan` at high precision). M3.1 harness MUST precompute and cache the basis once per precision level — the sweep amortizes one cold build per cascade tier. Subsequent calls at the same precision: 0.01 s (cached).

**Sweep size estimate.** Post-Excluded-Families filtering, the M3.1 sweep enumerates sub-bases of B_D(C) that contain at least one **complement** element (`log K_0` or `K_0·c_i` for c_i ∈ C); i.e., sub-bases NOT entirely contained in EF1 (BBC-grandfathered pure-power subset). The natural focused enumeration (defined in `harness/sweep.py` at M3.1 implementation):

| Sub-basis family | Construction | Count |
|---|---|---:|
| **Primary** | Full n=15 basis at (P, 2P, 4P) cascade, rigorous tier | 1 |
| **Pairwise log-probe** | {log K_0, x} for x ∈ B \ {log K_0, 1} | 13 |
| **Pairwise bilinear-probe** | {K_0·c_i, K_0·c_j} for i < j (i, j ∈ C) | 21 |
| **Complement-triplet** | {log K_0, K_0·c_i, K_0·c_j} for i < j | 21 |
| **Full-complement** | {log K_0} ∪ {K_0·c : c ∈ C} (n=8) | 1 |
| **Pure-complement-plus-one** | full-complement + K_0^k for k ∈ {0,…,D} | 7 |
| **Total** | (1 rigorous + 63 empirical) | **64** |

Sub-basis enumeration intentionally focused on the complement structure per operator's M3.1 directive ("with the three Excluded Families filtered out at basis construction time, not post-hoc"). 64 is the planning target; final sweep.py may produce ±10 depending on duplicate-pruning and basis-rank checks.

**96h wall-clock arithmetic (Brief §M3.2 budget = 345,600 s):**

```
  1 primary cascade (rigorous tier, n=15)        = 1 × 5486 s = 5,486 s    (91 min)
 63 sub-basis cascades (empirical, n=2..8)        = 63 × ~50 s = 3,150 s   (52 min; smaller n => faster PSLQ)
  cold-cache basis build (one-time, all 3 precs)  = 1203 s                 (20 min)
  ----------------------------------------------------------
  TOTAL ESTIMATE                                   ≈ 9,839 s ≈ 2.7 h
```

**Budget margin = 345,600 / 9,839 ≈ 35×**. Margin is **COMFORTABLY ABOVE 3×** per operator's gate condition.

(Conservative re-estimate using larger n=15 cost for all sub-basis cascades = 41 × 109.7 + 1 × 5486 + 1203 = 11,194 s ⟹ margin = 31×. Still well above 3×.)

**Decision per operator gate:** "If cascade arithmetic confirms comfortable margin (≥ 3×), proceed directly to M3.1 harness implementation." **PROCEEDING TO M3.1 IMPLEMENTATION.**

**U-MISSION-M NOT triggered.** Budget infeasibility check (margin < 2×) is not met. The 96h cap is roughly 35× over the predicted sweep cost, leaving substantial headroom for: (a) sweep size expansion if structural sub-basis families surface that warrant inclusion; (b) cascade-precision deepening (e.g., 8P safety check) on any candidate positive; (c) repeat-cascade verification at the same precision for noise diagnosis; (d) maxsteps elevation beyond 100k if H_rigorous targets at 10⁷⁰ require it.

---

## §7 Halt-class finding surfaced to operator — H8 paper-read of FBA 1999

### §7.1 Finding

The H ≈ 10^{P/n} relation (claimed in lit-009 as "PSLQ certifies absence of integer relations with coefficient height ≲ 10^{P/dim}") is **NOT stated as a theorem in FBA 1999**.

What FBA 1999 actually proves:
- Theorem 1: M_x ≥ 1/max|h_{i,i}(k)| at each PSLQ iteration k. (Rigorous per-iteration certificate.)
- Theorem 3: any relation PSLQ finds has norm |m| ≤ γ^{n−2} M_x. (Overshoot bound on found relation.)
- Corollary 2: PSLQ terminates in ≤ (n choose 2)·log_τ(γ^{n−1} M_x) iterations. (Polynomial-time bound.)

What the H ≈ 10^{P/n} folklore is: an **empirical scaling** of max|h_{i,i}| against precision P at typical PSLQ convergence. It is consistent with the FBA 1999 framework but is not stated as a theorem.

What BBC 1997 empirically used: a confidence factor **c ≈ 2.06** above the folklore heuristic (i.e., reported H = 10^{P/(c·n)}). This is **observational-grade**, not theorem-derived.

### §7.2 Severity classification

**Halt-class finding** per operator's non-collapsible sequence step 2:
> "If primary source paper-read confirms the H ≈ 10^{P/n} relation as stated, propagate. If paper-read reveals a different relation, halt and surface."

Paper-read revealed a different relation (Theorem 1's per-iteration certificate, not a literal H ≈ 10^{P/n} bound). **Halt triggered.**

This is the **5th halt-class finding overall** for the mission and the **1st in M2** — matching operator's prediction in M2.1 GREENLIGHT: "M2.3 will probably have one finding (likely in the precision_budget.md derivation — PSLQ confidence relations are subtler than the textbook formula suggests)."

### §7.3 Resolution — U-MISSION-L OPTION A WITH TWO-TIER STRENGTHENING

Operator U-MISSION-L (2026-05-15 ~21:36 JST) verbatim:

> "Catch #2 resolution: ACCEPT Option A, with strengthening to two-tier predicate (empirical + rigorous). The folklore H ≈ 10^{P/n} relation is field standard practice in experimental mathematics, not theorem-grade — operator-side framing in the previous reply implicitly treated it as theorem-grade and that framing was wrong. H8 caught not just a literature claim but a meta-claim about how to verify literature claims. CLI correctly halted rather than retrofitting."

**Resolution adopted: Option A with two-tier strengthening.** The pre-U-MISSION-L Option A (single-tier empirical) and Option B (rigorous-tier-only with capability-gap declaration) are both subsumed. Both tiers coexist:

| Tier | Confidence relation | Verification class (per H9) | Carried in M3.1 harness output |
|---|---|---|---|
| **Tier 1 — Empirical** | H_empirical = BBC-1997-calibrated `H ≈ c · 10^{P/(c·n)}` with c ≈ 2.06 | `field_standard_practice` | Always (every PSLQ run reports H_empirical from (P, n, c)) |
| **Tier 2 — Rigorous** | H_rigorous = max(FBA T1 via `100·reported_norm`, FBA Cor 2 via `exp((K-2n³)/(2n²))`) | `proven_corollary` | When K is large enough for non-trivial Cor 2 OR `reported_norm > 0` |

**Capability Gap CG-2 (originally Option B's escalation) is NOT declared.** §5 revised: mpmath.pslq's verbose mode DOES expose a rigorous-bound proxy (the printed `Norm` field per iteration), which `harness/rigorous_bound.py` parses into `H_rigorous`. The originally-feared rigid capability gap is dissolved; the two-tier predicate is operationally feasible with the existing mpmath capability.

**Specific predicate language commitments** (drafted in `literature/_m2.3_calibration_anchor.md` §7 in same commit batch):

- Negative arm at Tier 1: "Null PSLQ at (P=2160 dps, n=15, maxcoeff=10⁶⁰) with cascade stability across 2P and 4P implies no integer relation with height ≤ H_empirical = 10⁷⁰ under BBC-1997-calibrated empirical scaling. **Verification class: `field_standard_practice`.**"
- Negative arm at Tier 2: "Per FBA 1999 Theorem 1 and Corollary 2, the same PSLQ run produces H_rigorous = max(100·final_norm, exp((K-2·15³)/(2·15²))) as a rigorous lower bound on the minimum integer-relation norm M_x. **Verification class: `proven_corollary`.** H_rigorous ≥ 10⁷⁰ requires K ≈ 50-100k iterations (§5.2) — feasible at ~150-200 s per run in the M3.1 cascade."
- M6 manuscript discloses both tiers in a confidence-table with H9 class labels.

**Mutation budget at M2 milestone-block:** 0/1 still consumed. Per operator U-MISSION-L verbatim: "Classify as field-map update, not hypothesis mutation: the hypothesis (test for integer relations in B_D(C)) is unchanged; the confidence reporting structure is being extended."

### §7.4 lit-009 promotion — executed at M2.3 Catch #2 commit

Already done (prior commit `7a28604`): lit-009 promoted from `unverified_abstract_only` → `verified` / `paper_read_verified` per H8; statement field rewritten with actual Theorems 1/3/Corollary 2 + explicit folklore-vs-theorem flag; validator PASS 20 entries 0 errors.

At U-MISSION-L (this commit), lit-009's `independent_verifier_result.verification_class` is set per H9 (multiple classes — one per cited statement; see `methodology/heuristics.md` H9 retroactive-binding scope).

---

## §8 M2.3 PREDICATE DRAFT — written in `literature/_m2.3_calibration_anchor.md` §7

Per U-MISSION-L operator non-collapsible Step 3:
> "Update harness/precision_budget.md §7 with the two-tier predicate text and the chosen (P=2160, H_empirical=10⁷⁰) pair, plus whatever H_rigorous emerges from step 2."

Two-tier predicate text is drafted in `literature/_m2.3_calibration_anchor.md` §7 (new section, with existing AEAL discipline note renamed §8) per operator non-collapsible Step 4:
> "Draft M2.3 final predicate text in literature/_m2.3_calibration_anchor.md §7 with three Excluded Families AND two-tier scope claim. Halt for operator ratification before M3.1 implementation."

**Operator ratification is the gate for M3.1 implementation.** This precision_budget.md is the technical anchor; the calibration_anchor.md §7 is the formal predicate text the operator ratifies.

---

## §9 H9 INSTALLED — four verification classes

H9 was proposed at the M2.3 halt-class finding (pre-U-MISSION-L) with three classes. Operator U-MISSION-L approved with strengthening to **four classes**:

> "H9: APPROVE with strengthenings:
> - Four verification classes, not three: rigorous_theorem, proven_corollary, field_standard_practice, empirical_heuristic. field_standard_practice covers community-validated empirical methods (BBC/BBP/Bailey-class) distinct from agent-derived empirical heuristics.
> - Any claim cited in M2.3 predicate, M3.1 harness, or M6 manuscript must carry a verification_class in its JSONL entry. Load-bearing classification."

**Status: installed at `methodology/heuristics.md` H9** in the same commit batch as this update. The four classes:

| Class | Definition | Example (this mission) |
|---|---|---|
| `rigorous_theorem` | Stated, proven theorem of the primary source | FBA 1999 Theorem 1 |
| `proven_corollary` | Stated, proven proposition / lemma / corollary | FBA 1999 Corollary 2; the H_rigorous bound derived from it |
| `field_standard_practice` | Community-validated empirical (BBC/BBP/Bailey-class) | The H ≈ 10^{P/(c·n)} folklore with c ≈ 2.06; BBC 1997 §4 PSLQ nulls |
| `empirical_heuristic` | Agent-derived empirical methods, no community validation | CLI's internal scaling rules-of-thumb (if any are introduced) |

Storage convention: `verification_class` field is placed as a sub-key inside `independent_verifier_result` in `claims.jsonl` (preserves 7-field schema; validator unaffected).

Forward-binding on M2.3, M3.x, M5, M6 per H9 install date. See `methodology/heuristics.md` for full H9 sub-rules.

---

## §10 Provenance — this document

- **Original authoring:** 2026-05-15 ~21:30 JST (U-MISSION-K Step 1, halt at Step 2)
- **U-MISSION-L revision:** 2026-05-15 ~21:36 JST (this revision)
- Author: CLI (papanokechi/khinchin-k0-bounded, mission unsolved-relay)
- Authority: operator U-MISSION-K (M2.3 GREENLIGHT) + U-MISSION-L (two-tier predicate + Option α + H9 install)
- H8 retrieval evidence: §3.1 SHA-256 + saved PDF at `harness/_pslq_candidates/cpslq.pdf`
- Benchmark evidence: `harness/_bench_pslq_dim15.py` + §6 table
- Rigorous-bound investigation evidence: `harness/rigorous_bound.py` + `harness/_rigorous_bound_demo_output.txt`
- Hold status: §7 predicate text DRAFTED at `literature/_m2.3_calibration_anchor.md` §7 — held for operator ratification before M3.1 implementation per U-MISSION-L non-collapsible Step 4.

---

**END — STATUS: U-MISSION-L TWO-TIER PREDICATE INSTALLED; OPERATOR RATIFICATION PENDING ON `_m2.3_calibration_anchor.md` §7 BEFORE M3.1 IMPLEMENTATION**

