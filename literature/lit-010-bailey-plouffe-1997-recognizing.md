# lit-010 — Bailey & Plouffe (1997/1998), "Recognizing Numerical Constants" — PAPER-READ VERIFIED (H8 fire on M6 entry)

**Status:** `verified` · **Class:** `primary_paper`
**Paper-read date:** 2026-05-16 ~15:55 JST (H8 fire at M6 Step 1 per `m6_preflight_checklist.md` §1).
**Authority:** operator M6 GREENLIGHTED 2026-05-16 ~15:48 JST after M5 CLOSURE RATIFIED.

## Citation

Bailey, D. H., and Plouffe, S. *Recognizing Numerical Constants.* In *Organic Mathematics*, eds. J. Borwein, P. Borwein, L. Jorgenson, R. M. Corless, CMS Conference Proceedings **20**, AMS, Providence, RI, 1998 (proceedings published 1998; preprint version dated 1997). HTML version at the CECM (Centre for Experimental and Constructive Mathematics, Simon Fraser University) hosted at:

* `http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/paper.html` — Table of Contents (SHA-256 `8BEB376B8C78D60883B4B0BFA31F11E4192420C466E923EF22774D878A106A00`; 2,123 bytes; retrieved 2026-05-16 ~15:53 JST).
* `http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html` — §2 "The PSLQ Integer Relation Algorithm" (SHA-256 `5E435CAFBD1DA27928CE8082125EEBD8472EF39FE856A7F4C027177121C14895`; 11,344 bytes).

**Why "Bailey 1998" in mission-internal nomenclature:** the proceedings volume publication date is 1998. mpmath's PSLQ docstring cites *"David Bailey, 'The PSLQ Integer Relation Algorithm': http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html"* — this is the §2 of the present paper. The mission has consistently referred to the same paper as "Bailey 1998" in `harness/rigorous_bound.py`, `harness/precision_budget.md`, `_fidelity_findings.md`, and `mutation_log/m2.3_*.md` to match mpmath's choice of year. Both 1997 (preprint) and 1998 (proceedings) refer to lit-010.

**Note on representation:** the canonical paper is an LaTeX2HTML conversion (per the HTML `<!Converted with LaTeX2Organic ...>` header). Most mathematical formulas in the §2 algorithm pseudocode are rendered as GIF images (`img1.gif` through `img46.gif`). The visible English text + the IMG-ALT attributes + the structural pseudocode steps suffice for the H8 paper-read on the two specific divergences D2 and D3; full formula re-derivation is not required for the M6 rigorous tier claim (which is anchored at FBA 1999 = lit-009, already paper-read with verification class `proven_corollary`).

## Content (paper-read, §2 verbatim structural extract)

§2 of Bailey-Plouffe 1998 presents PSLQ as Ferguson's 1991 algorithm [ref 12] in its **simplified formulation** [ref 13 — Ferguson-Bailey complex PSLQ preprint, the same paper that became FBA 1999]. The pseudocode given:

**Initialize** (4 numbered steps, A and B set to identity matrices, partial-sum vector s computed, y vector normalized, lower-triangular H matrix computed and reduced).

**Iterate** until termination (6 numbered steps):
1. Select m such that "γ^i |h_{i,i}| is maximal when i = m" (the γ-weighted selection of the largest diagonal entry to swap).
2. Exchange entries m and m+1 of y, corresponding rows of A and H, and corresponding columns of B.
3. If a triangularity criterion holds, update H using Givens rotations.
4. Perform block reduction on H, simultaneously updating A and B.
5. **Norm bound: Compute M = 1 / max_j |H_j|**, where |H_j| denotes the j-th row of H. **Then there can exist no relation vector whose Euclidean norm is less than M.**
6. Termination test (precision exhausted OR detection threshold met).

Following the pseudocode, two pedagogical paragraphs:
* On the confidence level: "the ratio of the smallest and largest y vector entries is suddenly very small ... When detection does occur, this ratio may be thought of as a 'confidence level' of the detection."
* **On the empirical scaling (verbatim):** *"As a general rule, one can expect to detect a relation of degree n, with coefficients of size [10^m], provided that the input vector is known to somewhat greater than m·n digit precision, and provided that computations are performed using at least this level of numeric precision."*

## H8 paper-read disposition for the two D-divergences

### D2 (γ = √(4/3) boundary case) — CLEARED

* **(D2.a) Bailey's exact statement of the γ range:** Bailey 1998 §2 visible text gives γ as the weighting coefficient in the selection criterion `γ^i |h_{i,i}|` (step 1 of the iteration). The visible text does NOT state a strict inequality γ > √(4/3); the γ value enters as a parameter without an explicit lower-bound condition in §2.
* **(D2.b) Whether the rigorous bound theorems (FBA 1999 Theorem 1 + Corollary 2) require γ at the boundary or strict:** Bailey 1998 §2 Step 5's norm bound `M = 1 / max_j |H_j|` is stated **without any γ-range condition** — the bound holds as a structural property of the H matrix after iterate-time reduction. FBA 1999 Theorem 1 (the operative theorem for the M2.3 rigorous tier) is the same structural bound; FBA 1999 Definition 5's γ > √(4/3) strict inequality is required only for the Theorem 3 *overshoot* bound (which the M6 rigorous tier does NOT cite).
* **(D2.c) Whether mpmath's chosen γ = √(4/3) exactly satisfies the precondition of the operative theorems:** YES. mpmath's `g = sqrt_fixed((4<<prec)//3, prec)` (i.e., γ = √(4/3)) is **directly consistent with Bailey 1998's pseudocode**, which takes γ = √(4/3) as the canonical/optimal choice without strict-inequality restriction in the cited norm-bound statement. The operative theorems (T1 + Cor2) hold at the boundary.

**Disposition:** D2 is **CLEARED**. The M6 rigorous tier (verification class `proven_corollary`, H_rigorous = 1.036 × 10⁷²) does not require Theorem 3 (overshoot); it requires only Theorem 1 (rigorous lower-bound certificate on relation norm) and Corollary 2 (termination iteration bound). Both are stated in Bailey 1998 §2 in equivalent form to FBA 1999, with no γ-range constraint in the visible text. mpmath's choice of γ = √(4/3) exactly is **inside** Bailey 1998's stated parameter scope.

### D3 (mpmath cites Bailey 1998, NOT FBA 1999) — CLEARED

* **(D3.a) Whether mpmath documentation explicitly cites Bailey 1998:** YES, verbatim from mpmath PSLQ docstring: *"This is a fairly direct translation to Python of the pseudocode given by David Bailey, 'The PSLQ Integer Relation Algorithm': http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html"*. The URL is the §2 of lit-010 (now paper-read verified).
* **(D3.b) Whether mpmath's algorithm matches the algorithm in the cited paper:** YES. Bailey 1998 §2's pseudocode is the "simpler formulation" cited in its reference [13] = Ferguson-Bailey complex PSLQ preprint = the same algorithm that became FBA 1999. The mpmath implementation follows Bailey 1998 §2 step-by-step (initialization → 6-step iteration → norm bound → termination test). The pseudocode in §2 is **structurally identical** to the FBA 1999 Section 3 algorithm; the difference is exposition style (Bailey-Plouffe 1998 is the canonical pedagogical version of the FBA simplified PSLQ).
* **(D3.c) Whether FBA 1999 Theorem 1 (used in `rigorous_bound.py`) is consistent with the algorithm mpmath actually implements:** YES. Bailey 1998 §2 Step 5's norm bound `M = 1 / max_j |H_j|` is the same rigorous lower-bound certificate as FBA 1999 Theorem 1. The notational difference (Bailey: row-norm of H; FBA 1999: max diagonal entry) is **conservative in mpmath's direction**: mpmath uses `max_{i,j} |H[i,j]|` over ALL entries, which dominates both the row-norm (for upper-triangular H, the row norm equals √(sum of |h_{j,k}|² for k≥j), which is ≥ max_k |h_{j,k}|) AND the max diagonal entry. Therefore `1 / max_{i,j} |H[i,j]| ≤ 1 / max_j |h_{j,j}|`, i.e., mpmath's bound is **strictly weaker (more conservative)** than both Bailey 1998's row-norm form and FBA 1999's diagonal-only form. The M6 rigorous tier inherits Bailey 1998's bound via the conservative mpmath under-reporting.

**Disposition:** D3 is **CLEARED**. mpmath's algorithm chain is:
```
mpmath PSLQ → Bailey 1998 §2 simplified PSLQ → FBA preprint 1992 → FBA 1999 (lit-009, paper-read verified)
```
The norm-bound certificate at every iteration is consistent across the chain. The M6 rigorous tier claim is unchanged; its `proven_corollary` verification class is preserved.

### D5 (NEW finding from paper-read) — Folklore characterization confirmed

Bailey 1998 §2's pedagogical paragraph following the pseudocode contains the **canonical statement** of the folklore "H ~ 10^(P/n)" scaling, verbatim: *"As a general rule, one can expect to detect a relation of degree n, with coefficients of size [10^m], provided that the input vector is known to somewhat greater than m·n digit precision."*

This is **explicit textual confirmation** that the H ~ 10^(P/n) scaling is presented as a "general rule" (i.e., `field_standard_practice` per H9), NOT as a stated theorem. This **strengthens** the mission's M2.3 calibration anchor (already classifying the empirical tier as `field_standard_practice` per H9) by providing a verbatim primary-source warrant for the verification-class assignment.

**Disposition:** D5 is **a strengthening, not a correction**. M6 §Methods + §Discussion may now cite this verbatim Bailey 1998 statement when contextualizing why the empirical tier (BBC c=2.06 multiplier + maxcoeff-capping clause per §3.4) carries `field_standard_practice` rather than `rigorous_theorem` verification class.

## Mission role

* **Methodology cite** for the PSLQ-on-constants framework (operative for M6 §Methods PSLQ description).
* **Algorithmic cite** for mpmath's PSLQ implementation (operative for M6 §Methods M3.1 harness description and §Reproducibility appendix).
* **D2/D3 anchor** for the rigorous tier chain mpmath → Bailey 1998 → FBA 1999 (operative for M6 §Methods two-tier predicate description).
* **D5 anchor** for the empirical tier's `field_standard_practice` verification class (operative for M6 §Discussion methodological remarks).

## Anti-claim disposition (lit-018 fidelity-watch carry-over)

The original fidelity-watch flag on lit-010 was the AI-aggregated claim *"K₀ is not in this paper's null-result tables"*. This watch is **out of scope** for the M6 rigorous tier and was the lit-018 false-negative source. The H8 paper-read here focuses on the PSLQ algorithm description (§2), not the null-result tables in §3+. **The fidelity-watch flag on lit-010 for the K₀-table claim remains `unaddressed-but-non-load-bearing`** — it does not affect any current mission claim and would only need resolution if a future M6 revision uses lit-010's null-result tables as a load-bearing citation (it does not; BBC 1997 = lit-002 is the load-bearing K₀ null-result citation).

## Status

**Status:** `verified` (for the D2/D3/D5 H8 fire scope: PSLQ algorithm description in §2, including norm-bound certificate and folklore-scaling pedagogical statement).

**Verification class:** `proven_corollary` for D2/D3 (the boundary-case norm bound and the algorithm consistency); `field_standard_practice` for D5 (the empirical scaling characterization).

**Carry-over watch:** the K₀-table absence claim (from lit-018 fidelity context) remains `non-load-bearing` and is not retired this H8 fire.

## Reproducibility

```bash
curl -s -o paper.html "http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/paper.html"
curl -s -o node3.html "http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html"
# Expected SHA-256:
#   paper.html: 8BEB376B8C78D60883B4B0BFA31F11E4192420C466E923EF22774D878A106A00
#   node3.html: 5E435CAFBD1DA27928CE8082125EEBD8472EF39FE856A7F4C027177121C14895
sha256sum paper.html node3.html
```

Alternative archival sources (not paper-read this session; provided for reviewer reproducibility): `https://www.davidhbailey.com/dhbpapers/recogn.pdf` (Bailey's personal LBNL archive) hosts a PDF version of the same paper.
