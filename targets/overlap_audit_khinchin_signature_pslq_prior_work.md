# Overlap Audit — Prior Work: `papanokechi/khinchin-signature-pslq`

**Date:** 2026-05-15 ~18:32 JST (late catch — should have surfaced at M1.2)
**Trigger:** Pre-freeze enumeration of operator's GitHub namespace turned up `papanokechi/khinchin-signature-pslq` (created 2026-04-17, public, MIT, AEAL-framed).
**Severity:** Medium — **not** a hard duplicate of the M1.2 K_0 sub-question, but in the **same research program** with the **same machinery + AEAL framing**. Reviewer-attribution risk is real.
**Audit class:** This is a §M1.2-class overlap audit (analogous to the #26 Gauss-Kuzmin overlap_audit that recommended drop). It is late but worth doing before `gold/M1` locks `targets/selected.md`.

---

## §1 The prior work

**Repo:** `papanokechi/khinchin-signature-pslq` (public, MIT, default `main`, created 2026-04-17, last pushed 2026-04-17)
**Title:** "A Precision-Controlled Null Result for a Khinchin-Signature PSLQ Family"
**Abstract verbatim (paper/khinchin_signature_expmath_note.tex):**

> We test whether simple low-dimensional integer relations occur among coordinates derived from the empirical Khinchin-signature statistic $S_n$, evaluated on the continued-fraction partial quotients of $\pi$. Using agreement across 256-, 512-, and 1024-bit runs, we isolate the maximal certified segment $n=1,\ldots,91$ and perform PSLQ searches on six fixed 3D/4D templates at 300-digit working precision with 600-digit confirmation. Under the conservative bound `maxcoeff=10^3` and residual threshold $10^{-20}$, all 546 template-specific attempts are unsupported. A wide-cap diagnostic rerun with `maxcoeff=10^6` yields only high-coefficient fits, concentrated almost entirely in the 4-dimensional template, and these disappear completely when the conservative cap is restored. The outcome is therefore a reproducible, precision-controlled null result for the tested coordinate family rather than evidence of hidden arithmetic dependence.

**Coordinate family tested:** $\{S_n,\ \log S_n,\ S_n - K_0,\ \log n\}$
**Constant referenced:** Khinchin constant $K_0$ appears as a reference offset (in $S_n - K_0$), NOT as the target of the PSLQ search.
**Outcome:** precision-controlled null result (extended FP-rejection range — exactly the shape of unsolved-relay's negative terminal).

## §2 What the prior paper EXPLICITLY leaves open

From the prior paper's Discussion section (verbatim):

> The null result is deliberately local in scope. It does not rule out relations involving richer nonlinear functions of the index, alternative normalizations, or coordinate families augmented by additional constants or transforms. **For instance, templates involving $n^{1/2}$, $n^2$, or algebraic combinations of $K_0$ with other known constants lie entirely outside the tested family and remain open.** [emphasis added]

The italicized fragment matches the unsolved-relay M1.2 K_0 sub-question almost exactly: "algebraic combinations of $K_0$ with other known constants" is a near-restatement of "PSLQ-detectable algebraic relation of $K_0$ at degree ≤ D, height ≤ H against a named-constant basis."

## §3 Overlap analysis (3-axis)

### §3.1 Content overlap

| Aspect | Prior signature paper | Unsolved-relay K_0 sub-question | Overlap? |
|---|---|---|---|
| Target object | Signature statistic $S_n$ on $\pi$'s CF (per-n quantity) | Khinchin constant $K_0$ (single quantity) | **No** — different objects |
| Search dimension | 3D/4D template among $\{S_n, \log S_n, S_n-K_0, \log n\}$ | Univariate or low-D in $K_0$ alone + named-constant basis $\{1, \log 2, \zeta(2), \zeta(3), G, …\}$ | **Partial** — both PSLQ scans, different basis sets |
| Precision | 300 dps (600 dps confirm), maxcoeff=10³ | 500 dps (1000/2000 dps cascade), maxcoeff=H (to be set in M2.3) | **No** — different precision regime |
| Constant family touched | $K_0$ used as offset in coordinates, NOT searched on | $K_0$ is the search target | **Distinct uses of $K_0$** |
| Result class | Null result (FP-rejection range) | Both terminals (positive PSLQ hit OR null result) acceptable | **Partial** — null-result tier is the same |

**Content overlap verdict:** the two questions are **technically distinct**. The signature paper does NOT test polynomials in $K_0$ alone, nor does it scan $K_0$ against a basis of named constants. The K_0 sub-question is a clean downstream extension that the signature paper Discussion explicitly identified as open.

### §3.2 Machinery overlap

| Aspect | Prior | Unsolved-relay | Overlap? |
|---|---|---|---|
| PSLQ at multi-precision | Yes | Yes | **Yes** |
| Cascading precision check | 300 → 600 dps | 500 → 1000 → 2000 dps | **Same pattern, different baseline** |
| AEAL discipline | Yes (seven-field claim schema; provenance manifest) | Yes (same seven-field schema) | **Yes** |
| Author | Papanokechi | Papanokechi | **Yes** |

**Machinery overlap verdict:** **High.** Same author + same machinery class + same AEAL framing. This is expected (and good — it means operator's pipeline is well-characterized) but also reviewer-relevant.

### §3.3 Attribution-muddiness risk

Reviewers reading the unsolved-relay K_0 paper will likely also encounter (or cite, or be cited by) the signature paper. Three scenarios:

(a) **Best case:** the unsolved-relay K_0 paper cites the signature paper as immediate prior art, explicitly identifies the gap it extends ("algebraic combinations of $K_0$" left open in the signature paper Discussion), and the two papers form a clean tandem. **This is achievable.**

(b) **Neutral case:** reviewers note the prior signature paper but accept the K_0 sub-question as a distinct downstream effort. Modest attribution-muddiness but not blocking.

(c) **Worst case:** reviewers conflate the two papers ("you already did PSLQ on Khinchin-adjacent quantities; what's new here?"). This is unlikely if the sub-question and bibliography make the distinction explicit. **Mitigable by careful framing.**

## §4 The Brief-§0 `congruent-relay` clone reference is moot

Separate finding from the namespace check: **`papanokechi/congruent-relay` does NOT exist** on GitHub. The Mission Brief §0 said "Repository: create new repo `papanokechi/unsolved-relay` (clone structure from `papanokechi/congruent-relay`)". Operator's earlier instruction "match congruent-relay if it diverges" was made under the assumption that congruent-relay existed.

**Nearest-template options for the unsolved-relay repo structure:**
- `papanokechi/khinchin-signature-pslq` (best match: AEAL framing, paper/code/artifacts/aeal/ structure, MIT)
- `papanokechi/tunnell-cnp-lean4` (Lean-4 focused)
- `papanokechi/pcf-spectral-classes` (research repo)

CLI default if not redirected: clone the `khinchin-signature-pslq` directory shape (paper/ + code/ + artifacts/ + aeal/) but with unsolved-relay's existing staging structure preserved (targets/ + capability/ + claims/ + mutation_log/ + seeds/ + methodology/) — the two are compatible and complementary.

## §5 Recommendation

The K_0 sub-question is **substantively distinct** from the signature paper's content (§3.1 verdict), but the machinery + author + AEAL framing overlaps are **high enough to merit explicit framing** in `targets/selected.md`. Three paths forward, in order of CLI preference:

### Option A (recommended): RETAIN K_0 target; REFINE the sub-question explicitly

Refine the M1.2 bounded sub-question in `targets/selected.md` to read:

> Does Khinchin's constant $K_0$ admit a PSLQ-detectable algebraic relation of degree ≤ D and integer-coefficient height ≤ H at 500 dps, expressed as a polynomial in $K_0$ alone *or* a low-dimensional integer relation against the named-constant basis $\{1, \log 2, \zeta(2), \zeta(3), \log_2 e, G, K_0^{-1}, …\}$, **distinct from the coordinate family $\{S_n, \log S_n, S_n - K_0, \log n\}$ tested in `papanokechi/khinchin-signature-pslq` (Apr 2026)**, with (D, H) operator-fixed in the M2.3 success predicate?

This is a **tightening refinement** per heuristic H5 (no mutation_log entry needed by H5's definition) but should be documented in `selected.md` §5 as a refinement record. The M2.1 literature ledger MUST then cite `khinchin-signature-pslq` as primary-tier prior art.

### Option B: SWITCH target to Apéry ζ(5)/ζ(7)/ζ(9) (primary shortlist #2)

C_primary = 34 (tied with K_0 but with widest P_pos-P_neg gap = +3). No apparent prior-work collision in operator's namespace (verified: no `apery-*` or `zeta-*` repos under papanokechi). This switch would require a mutation_log entry (target change is scope-class).

### Option C: SWITCH target to Lévy β (contrast shortlist #3)

C_contrast = 33. No prior-work collision (no `levy-*` repo). Same mutation_log requirement as Option B.

**CLI recommendation: Option A.** Reasons:
- The K_0 selection has operator-explicit endorsement (U-MISSION-F).
- The signature paper's Discussion *explicitly* identifies "algebraic combinations of K_0" as the natural extension — Option A *literally executes* the prior paper's stated open direction.
- Citation hygiene (M2.1 must include `khinchin-signature-pslq`) is the standard mitigation for same-author-prior-work and is sufficient here.
- Switching target after operator approval is more disruptive than refining the sub-question scope.

## §6 What I should have done at M1.2

The M1.2 scoring should have included a "prior work in operator's repo namespace" check as part of the I (independence) axis. I scored I=9 for K_0 on the grounds of "zero overlap with R1 / Painlevé III queue" — but `khinchin-signature-pslq` is neither R1 nor Painlevé III, so it didn't trigger my filter. **In hindsight, I=9 should have been I=7** for K_0 (and Apéry might have surfaced as primary #1).

This is a **process miss**, not a content miss. Logged as a self-correction note here. Future M1.2-class scoring should expand the "I" axis to include a `gh repo list <operator>` enumeration as a default check.

## §7 Operator decision required

**U-MISSION-G (NEW, gates the M1.3 freeze):**

- (G1) Approve Option A (RETAIN + REFINE sub-question + cite prior in M2.1)?
- (G2) Approve Option B (SWITCH target to Apéry, with mutation_log entry)?
- (G3) Approve Option C (SWITCH target to Lévy β, with mutation_log entry)?
- (G4) Override audit; the overlap is acceptable as-is; proceed to freeze with current `selected.md` unchanged?

**Pending operator selection.** CLI HOLDS at filesystem staging. **No `gh repo create` executed.** No `gold/M1` tag. No env/M1.lock generation. The fact-block `selected.md` exists locally but has NOT been promoted to the GitHub repo.
