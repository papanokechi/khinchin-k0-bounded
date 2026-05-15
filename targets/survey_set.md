# Unsolved-Relay — M1.1 candidate survey set (NO SCORING)

**Mission Brief §9 deliverable (c).**
**Author:** Copilot CLI under operator Papanokechi
**Date staged:** 2026-05-15 ~17:30 JST
**Status:** AWAITING OPERATOR APPROVAL before any M1.2 scoring / M1.1 triage row construction.

---

## How this survey was built

**Source list:** [Wikipedia: List of unsolved problems in mathematics](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics).

**Hard filter applied per Mission Brief §M1.1 sentence 3:** *"Do NOT include problems whose 'machinery required' includes anything you have not previously deployed successfully ... This is a hard filter, not a preference."*

**Operator's verified machinery base (per Brief §M1.2):**
- PSLQ integer-relation finder at 130–500 dps
- `mpmath` arbitrary-precision arithmetic at 130–500 dps
- Lean 4 + Mathlib4 (Tunnell-CNP track demonstrates working facility)
- PCF spectral fingerprint framework
- Painlevé / Stokes / sub-leading-Stokes tooling

**Inferred-available adjuncts:** Python sieves, `sympy` symbolic / CAS basics, modular `crt`, basic combinatorial enumeration, interval arithmetic via mpmath, `arb`/`flint` if exposed.

**Excluded (machinery NOT previously deployed by operator):**
- Algebraic geometry over schemes (étale cohomology, motivic cohomology, perfectoid spaces)
- Modular-forms machinery beyond q-expansion-and-evaluate
- Hyperbolic geometry / Teichmüller theory
- Low-dimensional topology / Khovanov homology / Heegaard Floer
- Fluid mechanics / PDE-of-physics
- PCP / interactive-proof / fine-grained complexity
- Riemannian geometry / Ricci flow
- Mathematical logic beyond elementary
- Spherical-harmonic / representation-theoretic decompositions

**Independence from active R1 / Painlevé III queue (per §M1.2):** the survey deliberately under-weights PCF-and-Painlevé-direct problems even though they are best-fit machinery, because operator wants a SEPARATE track. Painlevé/Stokes machinery is invoked here primarily where a transfer-operator or asymptotic-constants angle applies, not where it would compete with R1.

**Categories represented:** number_theory, diophantine_approximation, transcendence, partition_theory, combinatorics, dynamics. (5+ per §M1.1.)

**Survey-set size:** 30 problems (exceeds §M1.1 minimum of 25).

**What is NOT in this file (per §9 "no scoring yet"):** no tractability score, no machinery-fit score, no publishability score, no AEAL-risk score. Those land at M1.1 triage row construction AFTER operator approval.

---

## Survey set

Each entry: `(N) Problem name — Wikipedia anchor / canonical reference. One-line bounded entry point (descriptive, not scored).`

### A. Number theory — Diophantine equations (5)

1. **Erdős–Straus conjecture** (4/n = 1/x + 1/y + 1/z for all n ≥ 2). Wikipedia "List … § Number theory". Bounded entry point: extend computational verification range beyond the current bound via residue-class CRT covers + targeted decomposition for the remaining classes.

2. **Brocard's problem** (n! + 1 = m² for n > 7?). Bounded entry point: extend computational search past 10^9 with mpmath; rule out new Brown numbers in range.

3. **Erdős–Moser equation** (1^k + 2^k + ⋯ + (m−1)^k = m^k, nontrivial integer solutions?). Bounded entry point: extend the von Staudt–Clausen / p-adic exclusion lower bound (currently m > 10^9 or thereabouts) with mpmath.

4. **Brun–Titchmarsh / Pillai-style gap conjectures** for consecutive perfect powers below extended bound. Bounded entry point: extend the perfect-power gap-statistics table; identify new high-gap candidates.

5. **Beal's conjecture** for fixed (p, q, r) signature classes. Bounded entry point: for one specific (p, q, r) triple where no proof exists, extend the computational A^p + B^q = C^r enumeration with high-precision sieving.

### B. Number theory — multiplicative / primes (5)

6. **Lehmer's totient problem** (does φ(n) | n − 1 imply n prime?). Bounded entry point: extend the current lower-bound prime-omega count beyond ω(n) ≥ 14 via mpmath factorization.

7. **Cunningham project unfactored cofactors** (specific small bases, large exponents). Bounded entry point: pick ONE base/exponent class where the cofactor is unfactored; document a precision-and-method audit of why current ECM / NFS attempts have stalled (negative-result framing: "this cofactor resists deployed methods to depth D"). NB: NFS is NOT in operator's machinery; entry would be marked machinery_available_locally=false at M1.1 triage and dropped from M1.2 selection.

8. **Mertens-function sign-change density** (asymptotic frequency of sign changes of M(n)). Bounded entry point: extend tabulation of sign-change positions to N = 10^14 with mpmath; compare against Lévy/Riemann-style predictions.

9. **Repunit primality density extension** (R_n = (10^n − 1)/9 prime for which n?). Bounded entry point: extend testing to n in a new range using probable-prime tests; document any new R_n promotions.

10. **Odd perfect numbers** lower-bound extension. Bounded entry point: extend the known lower bound for an odd perfect number's smallest prime factor or its largest prime factor via constraint-propagation enumeration. NB: existing extremal bounds use specialized prime-factor-pattern analysis; the entry point here is a documented bounded sweep that MAY hit a capability gap.

### C. Continued fractions & Diophantine approximation (5; NON-PCF)

11. **Zaremba's conjecture** (every q has a CF expansion of q/p with all partial quotients ≤ A_5, A_5 = 5). Bounded entry point: extend the current Bourgain–Kontorovich-style density to a new q-range with the operator's CF machinery; document any q in the open range where the bound fails.

12. **Markov spectrum gap structure** between 3 and Freiman's constant. Bounded entry point: extend the known table of Markov triples in a bounded range; tabulate gap-residual statistics for the open region.

13. **Lagrange spectrum past Freiman's constant** (~4.5278…). Bounded entry point: extend computational enumeration of Lagrange-spectrum values above Freiman's bound with bounded-CF tools.

14. **Stern–Brocot tree gap distribution** at large levels. Bounded entry point: at level n in the open range, compute the gap-distribution histogram with mpmath; test against conjectural Gauss-Kuzmin-style asymptotic.

15. **Khinchin's constant rationality / algebraicity**. Bounded entry point: extend PSLQ false-positive certification of K_0 ≈ 2.6854520010… at 500 dps against all algebraic relations of degree ≤ D and height ≤ H; expand D, H past current published bounds.

### D. Transcendence / irrationality (5; PSLQ-driven) (5)

16. **Catalan's constant** G ≈ 0.9159655941… — irrationality / algebraicity open. Bounded entry point: PSLQ false-positive scan at 500 dps over expanded D × H grid; document any near-relations.

17. **Apéry-extension witnesses** for ζ(5), ζ(7), ζ(9). Bounded entry point: extend the Ball–Rivoal / Zudilin-style witness search at 200 dps; document any new dense-relation candidates.

18. **Lévy's constant rationality** β = π² / (12 log 2). Bounded entry point: PSLQ false-positive scan at 500 dps. NB: β is provably transcendental? — verify status at M1.1 (entry survives only if status is genuinely open).

19. **Glaisher–Kinkelin generalized constants** (higher-rank A_k). Bounded entry point: PSLQ relation search across the family at fixed precision; promote any high-confidence relations to symbolic proof attempt.

20. **Periods identification** (Kontsevich–Zagier sense, bounded class). Bounded entry point: take a specific physically-arising constant whose period status is open (e.g., a specific Feynman-amplitude residue or a specific lattice-Green's-function value); PSLQ-screen against known period bases; promote candidate periods to symbolic verification.

### E. Partition theory & combinatorics (5)

21. **Andrews–Beck conjecture analogues** for higher-rank statistics. Bounded entry point: extend the computational verification of an Andrews–Beck-style identity to a new modulus class at moderate N.

22. **Andrews's spt-function congruences** (Ramanujan-type spt(n) ≡ 0 mod m). Bounded entry point: pick one modulus where the congruence pattern is conjectured but unproven; extend the computational verification by an order of magnitude in N. NB: full proof typically needs mock-modular machinery (NOT in operator's kit); entry must be bounded to VERIFICATION not PROOF.

23. **Stanley's plane-partition asymptotic constants**. Bounded entry point: PSLQ-identify the asymptotic constant in a fixed plane-partition family against known special-value bases (Glaisher–Kinkelin, Catalan, ζ-values).

24. **Brown–Erdős–Sós conjecture** (linear 3-uniform hypergraphs without (k, k+r)-configurations). Bounded entry point: enumerate extremal configurations for fixed small (k, r) past the current bound via constraint-SAT-style branching.

25. **Crank-moment congruences** beyond Ramanujan's original. Bounded entry point: tabulate moments mod small primes in extended N-range; flag any new congruence candidates. (Same caveat as #22: proof requires mock-modular machinery; deliverable is VERIFICATION + FLAG, not proof.)

### F. Dynamics & ergodic theory (5; NON-Painlevé-III-overlapping) (5)

26. **Gauss–Kuzmin effective error terms.** Bounded entry point: tighten the constant in the known O(q^{-n}) error term for a specific class of irrationals via mpmath transfer-operator iteration at high precision. NB: borderline with Finite-Depth Rigidity work — entry survives only if a clean axis-separation can be drawn at M1.1.

27. **Mahler's question on simultaneously badly approximable pairs** in specific number fields. Bounded entry point: extend the bounded-pair enumeration in a fixed cubic field with mpmath; flag any new candidates against conjectural density.

28. **Hurst-exponent estimation** for arithmetic dynamical sequences (Stern, Calkin–Wilf, Thomae). Bounded entry point: compute estimated H for each sequence to 6 decimals at varying window lengths; test against conjectural rational/irrational values.

29. **Sárközy-type pattern-avoidance conjectures** in sumset dynamics. Bounded entry point: extend the known maximum-density-set tables for a fixed small "forbidden pattern" via greedy + lattice methods.

30. **Brjuno function / Diophantine condition** statistics at the irrational rotation boundary. Bounded entry point: compute the Brjuno function on a dense grid of irrationals in a fixed interval; tabulate against conjectural Hausdorff dimension of the Brjuno-set. NB: this is dynamics-adjacent to Painlevé III only at a structural level, NOT at the chart-map content level — independence is preserved.

---

## Notes flagged for operator review

- **Entries 7, 22, 25:** explicitly flagged as having pieces of required machinery NOT in operator's verified base. These survive in the SURVEY set only as candidates for explicit deprecation at M1.1 triage (`machinery_available_locally=false`); they will not advance to M1.2 selection per the hard filter. They are included here so the operator can confirm the filter behaves as expected on edge cases.
- **Entries 10, 26:** borderline machinery-fit; explicit operator confirmation requested before M1.1 triage.
- **Entry 18:** transcendence status of Lévy's constant may already be settled — flagging for M1.1 literature-check.
- **Entries 23, 26:** mild overlap with active SIARC work (paper14, Finite-Depth Rigidity). Independence-clean axis-separation will be drawn at M1.1 IF entries advance.

## What this list deliberately omits

- **Solved-since-Wikipedia-edit** problems: cross-checked but not exhaustively re-verified. M1.1 includes a "still open?" literature pass per entry.
- **Conjectures requiring full automorphy / Galois-rep machinery** (Sato–Tate, BSD, Modular forms congruences beyond q-expansion).
- **Combinatorial conjectures requiring extremal-graph-theory infrastructure** beyond enumeration (e.g., Hadwiger–Nelson lower-bound extension).
- **PDE conjectures.** Out by hard filter.
- **Algorithmic complexity conjectures** (P vs NP, fine-grained reductions). Out by hard filter.
- **Geometric / topological conjectures** (Tate, Hodge, Smooth Poincaré in dim 4). Out by hard filter.

---

**Operator action required:**
- (i) Approve / amend / reject this survey set as the M1.1 input.
- (ii) Approve / decline creation of repo `papanokechi/unsolved-relay` (gh repo create + clone structure from `papanokechi/congruent-relay`). Rule 6 / Tier 3b: repo creation is portal-class and operator-gated.
- (iii) On approval, M1.1 triage proceeds: each surviving problem gets a full schema-valid `targets/triage.json` row.

**Until then:** this file is the only M1 artefact. No M1.1 triage, no M1.2 scoring, no M1.3 freeze.

---

## AMENDMENTS APPLIED 2026-05-15 ~17:42 JST (operator review pass)

Operator response 2026-05-15 ~17:38 JST instructed:
- U-MISSION-A: approve 27 of 30. Drop #10 (odd perfect). Hold #18 (Lévy's β) pending literature recheck. Hold #23, #26 pending one-paragraph `overlap_audit.md` each.
- U-MISSION-B: deferred (re-raise after M1.2 target selection).
- U-MISSION-C: run capability probe first; confirm machinery base from probe results.

**Resolutions completed by CLI same date:**

| Survey # | Operator status | CLI resolution | Outcome |
|---|---|---|---|
| #10 (odd perfect) | DROP | accepted | DROPPED — out of M1.1 |
| #18 (Lévy's β) | HOLD pending literature recheck | recheck PASSED — see `literature_recheck_18_levy_constant.md` | CLEARED — in M1.1 |
| #23 (Stanley plane-partition) | HOLD pending overlap audit | audit PASSED — see `overlap_audit_23_stanley_plane_partition.md` | CLEARED — in M1.1 |
| #26 (Gauss–Kuzmin) | HOLD pending overlap audit | audit FAILED — see `overlap_audit_26_gauss_kuzmin.md`; content-axis overlap with Finite-Depth Transient Rigidity manuscript is severe | RECOMMEND DROP — awaiting operator confirmation |

**Capability probe (U-MISSION-C) executed.** Full results: `../capability/probe_results_20260515.md`. Canonical machinery list: `../capability/machinery_base_confirmed.md`.

**Material findings from probe:**
- ❌ python-flint / arb NOT installed → M3.1 harness 2nd-leg uses `gp lindep` shell-out instead of canonical `arb` ball arithmetic
- ❌ fpylll NOT installed → LLL via PARI `qflll` shell-out only
- ❌ sagemath / cypari2 / scipy / mpsolve NOT installed
- ✅ mpmath 1.3.0 at 500 dps + built-in PSLQ
- ✅ PARI/GP binary on PATH (shell-out only)
- ✅ Lean 4.29.1 + Lake 5.0.0

**M1.1 deliverable:** `targets/triage.json` (28 schema-valid rows) + `_M1.1_triage_metadata.json` sidecar.

**Net M1.1 advancement count: 28** entries
- 26 unconditional clear (operator-approved)
- +1 #18 (literature recheck PASS)
- +1 #23 (overlap audit PASS)
- (–1 #26 recommended drop, NOT included)

Of the 28 rows in `triage.json`, 25 have `machinery_available_locally=true` (advancing candidates for M1.2 selection), and 3 (Cunningham #7, spt #22, crank-moment #25) are `available=false` hard-filter-dropout rows explicitly retained to test the filter behavior — `triage_validator.py --strict` correctly errors out on these.

**Total AEAL-compliance risk distribution:** 4 high, 11 medium, 13 low.

**Mutation log:** `../mutation_log/m1.0_to_m1.1_operator_amendments_20260515.md`.

**OPEN OPERATOR DECISIONS (post-amendment):**
- (i) Confirm or overrule CLI's recommended DROP of #26 (Gauss–Kuzmin effective error terms). If overrule, supply rewording to break content-overlap with Finite-Depth Transient Rigidity (see audit file for two reframings R-1, R-2).
- (ii) Reconcile "27 vs 28" arithmetic — CLI's honest post-audit count is 28 because #23 audit PASSED (was held; operator may not have anticipated PASS). Operator can accept 28 or instruct deflation to 27 by dropping a marginal entry.
- (iii) Approve `pip install python-flint` to enable canonical `mpmath + arb` harness 2nd-leg per Brief §M3.1 phrasing? CLI does NOT recommend this install but flags it as a discretionary option.
- (iv) Approve proceed to M1.2 rank-and-select against the 28-row `triage.json`?
- (v) U-MISSION-B (repo creation) — re-raise timing as per operator's deferral; CLI will surface again at M1.2 completion.
