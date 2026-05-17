# Ramanujan Journal — EM Portal Abstract Field (paste-ready)

**Purpose:** Plain-text Unicode abstract for direct paste into the Editorial Manager "Abstract" Details-screen field. Overrides the EM auto-extractor's broken extraction of the LaTeX abstract source (which strips multi-line inline-math, leaves macros + cite keys raw, and drops the entire H_rig rigorous-tier clause).

**Status:** Operator-finalized 2026-05-17 ~11:06 JST in response to operator-reported portal extraction breakage.

**Word count:** 249 words (RJ guideline band: 150–250).

**Critical ordering:** The EM auto-extractor re-runs on every manuscript-file upload. Paste this text into the Abstract field **AFTER** the final ZIP upload and **BEFORE** pressing "Run checks". Do not re-upload the manuscript after pasting, or the extractor will overwrite this text again.

---

## Paste-ready abstract text

```
We test for integer relations on the hybrid basis B_{D,C} = {1, K_0, K_0^2, …, K_0^D, log K_0} ∪ {K_0·c : c ∈ C} at D=6 and C = {π, e, log 2, γ, ζ(2), ζ(3), G} (dimension n=15). A cascading-precision PSLQ harness based on mpmath.pslq at P=2160 dps with cascade legs at 2P and 4P returns a cascade-stable null on all 65 scanned sub-bases, independently corroborated by a PARI/GP lindep second leg. We report the null at two complementary tiers under an explicit verification-class taxonomy (field-standard-practice, proven-corollary): the empirical tier bounds the coefficient height H_emp^op ≈ 7.997 × 10^69 at the Bailey–Borwein–Crandall (1997) confidence calibration, classified field-standard-practice per the Bailey–Plouffe (1998) "general rule" for PSLQ detection; the rigorous tier bounds the relation Euclidean norm H_rig = 1.0361 × 10^72 via the Ferguson–Bailey–Arno (1999) Theorem 1 and Corollary 2 overshoot-free framework, classified proven-corollary (implying max_i |m_i| ≥ H_rig / √n ≈ 2.676 × 10^71). Three Excluded Families delineate this bounded scope from (EF1) the BBC 1997 pure-power null, (EF2) the operator's prior signature-statistic null on π's continued fraction, and (EF3) Gauss–Kuzmin–Wirsing spectral-method imports. A symbolic-closure attempt in SymPy surveying seven candidate structural arguments (Lindemann–Weierstrass, Schanuel, Nesterenko, Mahler-measure, Galois, non-GKW CF-theoretic, height theory) plus a four-path probe returned a documented fundamental capability gap, rooted in K_0's unresolved transcendence status. The result statement is additionally encoded in Lean 4 with an explicit auxiliary-axiom trust boundary; the encoding type-checks against Mathlib4 v4.14.0 but is not a first-principles formal proof.
```

## Paste-ready title text

```
A bounded two-tier null result for integer relations on a hybrid Khinchin-K₀ basis, with a documented capability gap and a Lean 4 statement-shape encoding
```

Title length: 28 words. Uses Unicode subscript-zero `K₀` (U+2080). Confirm EM Details screen renders this correctly; fall back to `K_0` only if EM mangles the subscript.

## Source-vs-portal cross-walk (macros + math segments)

Reference for why this paste is necessary — what the LaTeX source contains that the portal extractor loses:

| Source token (paper/main.tex) | Plain-text expansion in this paste-ready version |
|---|---|
| `\K` | `K_0` |
| `\BDC` | `B_{D,C}` |
| `\Hempop` | `H_emp^op` |
| `\Hrig` | `H_rig` |
| `\fsp{}` | `field-standard-practice` |
| `\pc{}` | `proven-corollary` |
| `~\cite{bbc1997}` | `Bailey–Borwein–Crandall (1997)` (already in surrounding prose) |
| `~\cite{bailey1998}` | `Bailey–Plouffe (1998)` (already in surrounding prose) |
| `~\cite{fba1999}` | `Ferguson–Bailey–Arno (1999)` (already in surrounding prose) |
| `~\cite{papanokechi2026signature}` | `operator's prior signature-statistic null on π's continued fraction` (already in surrounding prose) |
| Inline math `$\BDC = \{...\}$` (line 81, wrapped) | Spelled out in paste-ready text |
| Inline math `$C=\{\pi, e, \log 2, \gamma, \zeta(2), \zeta(3), G\}$` (line 83) | Spelled out with Unicode |
| Inline math `$P=2160$~dps with cascade legs at $2P$ and $4P$` (line 86) | Spelled out |
| Inline math `$\Hrig = 1.0361 \times 10^{72}$` clause (lines 97–99) | Spelled out — this is the entire rigorous-tier bound clause that the extractor dropped |

*Created 2026-05-17 ~11:06 JST as the canonical paste-ready substrate for the EM Abstract + Title Details-screen fields.*
