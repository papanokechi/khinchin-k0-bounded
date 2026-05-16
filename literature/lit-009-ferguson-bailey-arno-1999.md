# lit-009 — Ferguson, Bailey, & Arno (1999), "Analysis of PSLQ"

**Status:** paper_read_verified · **Class:** primary_paper
**Verified at:** 2026-05-15 ~21:30 JST via direct PDF retrieval and pypdf extraction (U-MISSION-K halt, M2.3 H8 trigger)
**Canonical PSLQ algorithm reference.**

## Citation
Ferguson, H. R. P., Bailey, D. H., and Arno, S. (1999). _Analysis of PSLQ, an integer relation finding algorithm._ Mathematics of Computation **68** (225), pp. 351–369. DOI `10.1090/S0025-5718-99-00995-3`.

Preprint dated 03 July 1997; published 1999. Bailey's archive copy at `https://www.davidhbailey.com/dhbpapers/cpslq.pdf` is the canonical preprint of the Math. Comp. paper.

## §1 Verification provenance

| Field | Value |
|---|---|
| Source URL | `https://www.davidhbailey.com/dhbpapers/cpslq.pdf` |
| Local cache | `harness/_pslq_candidates/cpslq.pdf` |
| File size | 218,997 bytes |
| SHA-256 | `3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5` |
| Pages | 26 |
| Extraction | `pypdf.PdfReader().pages[i].extract_text()`; 51,322 chars; saved at `harness/_pslq_candidates/fba1999_text.txt` |
| Retrieval timestamp | 2026-05-15 ~21:30 JST |
| Trigger | M2.3 U-MISSION-K step 2: H8 paper-read of PSLQ confidence-relation source |

## §2 What the paper actually proves (theorem-grade)

**Theorem 1** (p.10): For x ≠ 0 ∈ K^n, with H = AH_xQ the lower-trapezoidal matrix at iteration k of PSLQ, the smallest possible relation norm satisfies
```
M_x  ≥  1 / max_i |h_{i,i}(k)|
```
This is the **rigorous per-iteration certificate**.

**Theorem 3** (p.15): For γ > √(4/3) (real) or γ > √2 (complex), any relation `m` found by PSLQ(τ) has norm
```
|m|  ≤  γ^{n-2} M_x
```
i.e., PSLQ-found relations overshoot the smallest by at most γ^{n-2}.

**Corollary 2** (p.14): PSLQ(τ) terminates in
```
< (n choose 2) · log_τ(γ^{n-1} · M_x)  iterations
```
i.e., polynomial-time in n and log M_x.

**Parameters (Def. 5, §3):** γ > 2/√3 ≈ 1.1547 (real case); γ > √2 ≈ 1.4142 (complex); γ = ∞ (quaternion).

**Algorithm class** (SIAM "Top 10 Algorithms of the 20th Century", 2000).

## §3 What the paper does NOT contain (heuristic-grade)

Direct text search across the full 51,322-char extraction for any literal statement of:

> **"At precision P, PSLQ certifies absence of integer relations with coefficient height ≲ 10^{P/dim}"**

returned **no theorem-grade match.** What the paper does say about precision (§8 Computer Implementation, p.18):

> "Using double precision (i.e., 64-bit) arithmetic, relations of two or three digits in size can be recovered for n up to five or so. Beyond this level, precision is quickly exhausted, and recovered relations and norm bounds are meaningless."

This is **descriptive empirical observation**, not a stated theorem. The folklore `H ≈ 10^{P/n}` heuristic is an empirical scaling of Theorem 1's `max|h_{i,i}|` against precision P at typical PSLQ convergence — consistent with FBA 1999's framework but **not stated as a theorem.**

## §4 Pre-paper-read claim corrected

**Previous claim (now corrected):** "Algorithm bounds: at precision P, PSLQ certifies absence of integer relations with coefficient height ≲ 10^(P/dim)."

**Status of previous claim:** correct as **empirical heuristic** (folklore); misleading as theorem citation (FBA 1999 does NOT state this as a theorem).

**Post-paper-read claim class:** `empirical_heuristic`, NOT `rigorous_theorem`. This claim class distinction is load-bearing for M2.3 (see `harness/precision_budget.md` §7 halt-class finding).

## §5 Mission role — REVISED

**Previous mission role:** "The M3.1 harness does NOT require a paper-read of this entry."

**REVISED mission role:** **The M3.1 harness DOES depend on this entry** for its confidence-claim semantics. The harness's negative-result claim ("no relation up to H_target exists") inherits the claim class of the precision-vs-height relation it invokes. Per FBA 1999 paper-read:
- The **rigorous** Theorem-1 certificate `M_x ≥ 1/max|h_{i,i}|` is NOT exposed by `mpmath.pslq` (mpmath does not return the H-matrix diagonals).
- The **folklore** `H ≈ 10^{P/n}` heuristic is the practical option; it is consistent with FBA 1999 framework but is `empirical_heuristic` claim class.

**The harness's confidence statement must inherit the empirical_heuristic class** unless operator selects a different resolution path. See `harness/precision_budget.md` §7 for the two operator-options surfaced.

## §6 BBC 1997 confidence-factor consistency check (cross-reference with lit-002)

BBC 1997 §4 Test 1: n = 51, P = 7350 dps, reported H = 10^70.

If folklore `H ≈ 10^{P/n}` were a literal certificate, BBC would have reported H = 10^{7350/51} ≈ 10^144. They reported 10^70, **2.06× more conservative** in the log-height exponent.

This factor c ≈ 2.06 is the **empirical confidence calibration** the experimental-mathematics community uses — derived from observed PSLQ behavior, not from FBA 1999 theorem. M2.3's `H_target` derivation therefore rests on:

1. FBA 1999 Theorem 1 (rigorous framework, theorem-grade)
2. BBC 1997 §4 Test 1 empirical calibration c ≈ 2.06 (observational-grade)
3. The folklore composition: `H_target ≈ 10^{P/(c·n)}` with c ≈ 2 (empirical_heuristic class)

## §7 Watch-list status — TRIGGER FIRED

Previously: "On lit-018 `_fidelity_findings.md` §3 watch list IF any M3.x manuscript ever cites a specific PSLQ bound from this paper. Until then, abstract-only is sufficient."

**As of 2026-05-15 ~21:30 JST: TRIGGER FIRED.** M2.3 `harness/precision_budget.md` cites FBA 1999 in deriving `H_target`. The watch-list condition is met. Promotion to `paper_read_verified` is mandatory per H8 retroactive-binding scope.

This promotion executed in this commit batch.

## §8 AEAL discipline notes

- This entry is **load-bearing for M2.3** (precision-budget derivation) and **load-bearing for M3.1** (harness confidence-claim provenance).
- Any future use of the H ≈ 10^{P/n} relation in M3.1 outputs, M3.2 status calls, or M6 manuscript text MUST carry the `verification_class: empirical_heuristic` qualifier per AEAL §0.1.
- The §5 mission-role revision is itself a **claim-class refinement**, NOT a mutation per operator's U-MISSION-J ratification (lit-018 precedent). It is a field-map update under H8.
- The rigorous certificate option (FBA Theorem 1 with H-matrix diagonal exposure) would require custom mpmath wrapping or a different PSLQ implementation; this is captured as candidate Capability Gap CG-2 in `harness/precision_budget.md` §7 (operator Option B).

## §9 Boundary-case scope (FBA 1999 §7 disclaim; stage-2 paper-read finding, 2026-05-16)

FBA 1999 §7 explicitly states T2 and T3 conclusions "make no sense or have no apparent content" for γ ≤ √(4/3) in the real case. The paper does not extend T2 to γ = √(4/3) by continuity or any other argument.

T1's per-iteration certificate, by contrast, is structurally γ-independent (proof in FBA §3-§4 establishes the bound without invoking γ > √(4/3)) and holds at the boundary directly.

Mission usage at γ = √(4/3) therefore separates as:

- **T1 + Corollary 2** invoked under structural γ-independence (rigorous tier; `paper/main.tex` §2.3 ¶2 as corrected in this commit batch).
- **Iteration-count contrapositive** (M_x → maxsteps inference, used in `harness/rigorous_bound.py`) anchored on Bailey 1998 §2's γ-range-independent re-presentation (lit-010), not on FBA continuity.

This disposition arose from stage-2 paper-read on FBA 1999 §3 (operator commission, 2026-05-16) and resolved a citation-chain misattribution in the M6 manuscript. **Avoided U-MISSION-P halt-class.**

