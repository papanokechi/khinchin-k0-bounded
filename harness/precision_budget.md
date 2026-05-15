# harness/precision_budget.md

# M2.3 precision-budget derivation — STATUS: HALT-CLASS FINDING SURFACED (FBA-1999 heuristic-vs-theorem)

**Mission:** unsolved-relay
**Milestone:** M2.3 (success-predicate calibration)
**Authority:** Operator U-MISSION-K (2026-05-15 ~21:14 JST)
**Sequence position:** Step 1 of non-collapsible 4-step sequence; HALT triggered at Step 2 (H8 paper-read of PSLQ confidence-relation source)
**Subordinate to:** Brief §M2.3; H8 (paper-read on dependency literature claims)

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

## §5 mpmath.pslq's actual return contract

The M3.1 harness uses `mpmath.pslq(x, tol=..., maxcoeff=..., maxsteps=...)`. Functional verification at M2.2 capability audit (§2) confirmed:
- Returns an integer tuple if a relation is found within `maxsteps` iterations with `|coefficients| ≤ maxcoeff` at tolerance `tol`.
- Returns `None` otherwise.

**mpmath.pslq does NOT expose the rigorous certificate** `M_x ≥ 1/max|h_{i,i}|` from FBA 1999 Theorem 1. The diagonal entries of the internal H matrix are NOT returned to the caller.

Therefore, the harness's negative-result claim is structurally:
> "After at most `maxsteps` iterations, with required tolerance `tol` and coefficient cap `maxcoeff`, no integer relation was found."

This is **weaker than the rigorous Theorem-1 certificate** in two ways:
1. The `maxsteps` cutoff is artificial; the rigorous certificate would only require that PSLQ has *terminated* (not just been stopped after k steps).
2. The `maxcoeff` cap restricts the search, but mpmath does NOT then certify `M_x ≥ maxcoeff` — it just reports "did not find a relation matching constraints".

**Consequence:** the M3.1 harness's "no relation up to H_target" claim CANNOT be backed by FBA-1999 Theorem 1 rigorously **without exposing the H-matrix diagonals**. The claim must instead be backed by **empirical confidence calibration** against BBC 1997 (c ≈ 2.06 at matching P/n), with explicit AEAL flag that this is a **folklore-grade certificate**, not a theorem-grade certificate.

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

### §6.2 Provisional (P, H_target) candidate pairs

Three candidates, each conditional on operator's H8 resolution (§7):

| Option | P (dps) | H_target (BBC c=2.06) | Wall (single run) | Confidence framing |
|---|---:|---:|---:|---|
| α — BBC strict parity | 2160 | 10^70 | ~18 s | Match BBC 1997 §4 Test 1 confidence-per-dimension exactly |
| β — Modest aspiration | 2000 | 10^60 (c≈2.4) | ~16 s | Slightly more conservative than BBC; round-number P |
| γ — Conservative | 1500 | 10^48 (c≈2.06) | ~10 s | Lower budget; same c as BBC; tighter H_target |

CLI default recommendation (subject to operator override): **Option β** — round-number P=2000 dps + H_target=10^60 with c≈2.4 buffer over BBC. Rationale: 10^60 is a clean cap; c=2.4 is more conservative than BBC's c=2.06; wall-clock budget comfortable.

**All three options assume the H ≈ 10^{P/n} heuristic is operationally adopted as the empirical confidence relation.** Per §7 below, this adoption itself is the halt-pending decision.

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

### §7.3 Two resolution options for operator

#### Option A — Accept empirical heuristic with explicit AEAL labeling

- Treat `H ≈ 10^{P/n}` as an **empirical confidence heuristic** consistent with FBA 1999 framework + BBC 1997 calibration data.
- Update lit-009 to clarify: "FBA 1999 proves the rigorous certificate M_x ≥ 1/max|h_{i,i}|; the H ≈ 10^{P/n} folklore is an empirical scaling of this certificate against precision P, calibrated against BBC 1997's c ≈ 2.06 confidence factor; it is NOT a stated theorem in FBA 1999."
- M2.3 success predicate's negative arm uses `H_target` derived from the heuristic, with explicit AEAL claim-class qualifier `heuristic_certificate` (NOT `rigorous_certificate`).
- Proceed to predicate draft (Step 3 of operator's U-MISSION-K sequence).

Trade-off: claim strength is honestly characterized but the predicate's negative arm is folklore-grade, not theorem-grade. The M6 manuscript must declare this explicitly.

#### Option B — Require rigorous certificate; declare capability gap

- Require the M3.1 harness to expose the rigorous `M_x ≥ 1/max|h_{i,i}|` certificate. This requires either:
  - (i) A custom mpmath.pslq wrapper that reads the internal H-matrix diagonals (mpmath's source is patchable but this is non-trivial work, ~hours-to-days).
  - (ii) A different PSLQ implementation that exposes the certificate natively. `arb`/`flint` is the candidate but was DECLINED at U-MISSION-D ("If a future milestone genuinely requires interval arithmetic that neither mpmath nor gp can provide, log it as a Capability Gap and stop per §0.2; do not retrofit the install"). U-MISSION-D's "interval arithmetic" framing is adjacent but not identical to "rigorous PSLQ certificate"; the new gap is specifically the absence of certificate-exposing PSLQ in the mission's capability base.
- Declare new Capability Gap CG-2 (paralleling the U-MISSION-D-declined CG-1 for interval arithmetic). Per Brief §0.2, log and stop.
- The predicate's negative arm would then need either heuristic framing (regressing to Option A) or scope reduction (e.g., positive predicate only, negative reduced to "PSLQ did not find a relation under mpmath's empirical cap" without claiming a height bound).

Trade-off: claim strength is theorem-grade if implemented, but capability gap may halt or scope-reduce M3.1.

#### CLI default recommendation

**Option A.** Rationale:

- The folklore `H ≈ 10^{P/n}` heuristic is what the entire experimental-mathematics community has used for 30+ years; this is the empirical-mathematics standard claim class.
- BBC 1997, Bailey-Borwein-Plouffe 1997, Bailey 1998, and successor papers all use this framing; M6's reception in Math.Comp. / Experimental Mathematics will treat folklore-certificate claims as standard.
- AEAL's seven-field schema can carry the `heuristic_certificate` qualifier cleanly via `verification_class: empirical_heuristic`.
- The mission's stated form is a **bounded negative result**; the bound is a folklore-grade confidence statement, NOT a transcendence proof. Folklore-grade is honestly the right claim class.

**Recommendation: adopt Option A with explicit AEAL labeling.** Decision is operator's.

### §7.4 Sub-question: lit-009 promotion regardless of Option

Independent of which option operator selects:

- **lit-009 must promote** from `unverified_abstract_only` to `paper_read_verified` per H8.
- The promoted entry's content will reflect the heuristic-vs-theorem distinction (§3.2-3.4 above).
- The lit-009 "Mission role" line "The M3.1 harness does NOT require a paper-read of this entry" is **OVERTURNED**: the harness's confidence claim depends on FBA 1999 → enters M2.3 dependency chain → H8 binds → paper-read required.

This sub-step is non-conditional and is executed alongside this document.

---

## §8 Pending §7 predicate draft

Per operator U-MISSION-K sequence step 3, the M2.3 success predicate text in `literature/_m2.3_calibration_anchor.md` §7 (new section) is **NOT DRAFTED** at this commit. It is held pending operator H8 resolution per §7 above.

When operator resolves:
- **If Option A**: §7 predicate text invokes `H_target` from §6.2 (Option α/β/γ pending operator-select) + the three Excluded Families per U-MISSION-K + the AEAL `verification_class: empirical_heuristic` qualifier on the negative arm.
- **If Option B**: §7 predicate text invokes the rigorous certificate; CG-2 declaration triggers per Brief §0.2; mission scope reduces or pauses pending capability resolution.

---

## §9 H-pattern installation candidate (for operator review at §7 resolution)

This finding raised the bar on what "verified confidence relation" means for the mission. A possible H-class heuristic to install:

> **H9 (proposed, pending operator approval) — Theorem-vs-heuristic distinction on cited bounds.** Any quantitative bound cited from a primary source must be classified at one of three claim classes: `rigorous_theorem` (a stated, proven theorem of the source), `proven_corollary` (a stated, proven proposition or corollary of the source), or `empirical_heuristic` (a folklore scaling or rule-of-thumb consistent with the source's framework but not stated as a theorem). The claim's AEAL `verification_class` field must record the classification. M3.1 harness output claims must inherit the claim class of the strongest bound they depend on. Subordinate to Brief §M2.3; sibling to H7 (capability-claim functional verification) and H8 (literature-claim paper-read verification). Forward-binding on M2.3 onward.

**Decision: operator approves H9 or not, at §7 resolution.**

---

## §10 Provenance — this document

- Authored: 2026-05-15 ~21:30 JST
- Author: CLI (papanokechi/khinchin-k0-bounded, mission unsolved-relay)
- Authority: operator U-MISSION-K (M2.3 GREENLIGHT, 2026-05-15 ~21:14 JST)
- H8 retrieval evidence: §3.1 SHA-256 + saved PDF at `harness/_pslq_candidates/cpslq.pdf`
- Benchmark evidence: `harness/_bench_pslq_dim15.py` + §6 table; reproducible in ~70 seconds
- Hold status: §7 predicate draft NOT WRITTEN — held pending operator H8 resolution

---

**END — STATUS: HALT FOR OPERATOR H8 RESOLUTION**

