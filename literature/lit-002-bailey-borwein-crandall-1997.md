# lit-002 — Bailey, Borwein, Crandall (1997), "On the Khintchine Constant"

**Status:** verified · **Class:** primary_paper · **Method:** paper_read_verified
**Verified at:** 2026-05-15 ~19:50 JST via direct PDF retrieval and pypdf extraction
**Mission role:** SINGLE MOST IMPORTANT LITERATURE ANCHOR. Determines the M2.3 success-predicate calibration — see `_m2.3_calibration_anchor.md`.

---

## 1. Citation (canonical)

Bailey, D. H., Borwein, J. M., and Crandall, R. E. (1997). _On the Khintchine Constant._ Mathematics of Computation **66** (217), pp. 417–431. AMS. **DOI:** `10.1090/S0025-5718-97-00800-4`.

Cross-references: OEIS A002210 (Khinchin's constant decimal expansion) lists this as the standard high-precision computational reference.

> **Fidelity watch:** an AI-aggregated web search at 2026-05-15 ~19:50 JST reported a DOI of `10.1090/S0025-5718-97-00830-5` (one digit off — `00830` instead of `00800`) and quoted a passage that does not appear in the actual paper. See `_fidelity_findings.md` for the full audit trail and `lit-018` for the AEAL-schema entry. The canonical DOI above was confirmed by direct retrieval and matches the OEIS A002210 cross-reference list.

## 2. Computational record

| Parameter | Value |
|---|---|
| Constants computed | K_0 (geometric Khinchin mean) and K_{-1} (harmonic Khinchin mean) |
| Precision achieved | **7350 decimal digits** for both K_0 and K_{-1} |
| Method | Fast-converging series via Riemann zeta values (built on Shanks–Wrench 1959, lit-006) |
| Verification | "Complete agreement with Gosper's 2217 digits" (§5) |
| Hölder means tabulated | K_p for p = −2, −3, −4, −5 at **50 digits** each (§5 Table) |

## 3. PSLQ integer-relation tests (§4, paper-read-verified verbatim)

### Test 1 — pure-power algebraicity

> "A question implicitly asked in the previous section is whether K_0 or K_{-1} is algebraic. … This algorithm [PSLQ], when applied to power vectors generated from our computed values of K_0 or K_{-1}, found no relations for either. On the contrary, we obtained the following result: **if K_0 satisfies a polynomial of the form
>
> 0 = a_0 + a_1 α + a_2 α² + a_3 α³ + … + a_50 α^50
>
> in the variable α, then the magnitude of some integer coefficient a_k exceeds 10^{70}.** The same was found to be true for K_{-1}."

- **Basis:** {1, α, α², …, α^50} for α ∈ {K_0, K_{-1}}
- **Degree bound D:** 50
- **Height lower bound H:** 10^70
- **Precision:** 7350 dps
- **Outcome:** NULL (no relation found; any such relation must have coefficient magnitude exceeding the height bound)

### Test 2 — log-multiplicative

> "In a second experiment using these high-precision values, we showed, again using PSLQ, that **neither K_0 nor K_{-1} satisfies a relation of the form
>
> 0 = a_0 log α + Σ_{k=1}^{15} a_k log p_k + a_{16} log π + a_{17} log e + a_{18} log γ + a_{19} log ζ(3) + a_{20} log log 2
>
> with integer coefficients a_k of absolute value 10^{20} or less.**"

- **Basis:** 21-dimensional log-multiplicative basis: {log α} ∪ {log p_k : k = 1..15 (first 15 primes)} ∪ {log π, log e, log γ, log ζ(3), log log 2}
- **Basis size:** 21
- **Height bound H:** 10^20
- **Outcome:** NULL

### Open problems explicitly named (§4 close, verbatim)

> "There are many other tests that might be applied. For example, further work might be to **rule out the possibility that log K_0, (log K_0)(log 2), or one of many other forms involving K_0 be an algebraic number of low degree.**"

This sentence is the **specific structural anchor** for the present mission's M1.2 sub-question.

## 4. Implications for the present mission (M2.3 calibration)

The operator's M1.2 hybrid basis is

```
B_D(C)  =  {1, K_0, K_0², ..., K_0^D, log K_0}  ∪  {K_0·c : c ∈ C}
```

with `D ≤ 6` and a specified height bound `H` (to be fixed in M2.3), at 500 dps.

Comparing this with BBC 1997's Test 1 and Test 2:

| Sub-family of B_D(C) | BBC 1997 status | Mission novelty? |
|---|---|---|
| `{1, K_0, K_0², …, K_0^D}` for D ≤ 6 | **Grandfathered**: BBC tested at D = 50, H = 10^70, 7350 dps (Test 1). Operator's D ≤ 6, H = TBD ≤ 10^? at 500 dps is **strictly weaker** on this sub-family. | **NO** — silent re-run of BBC at weaker parameters unless M2.3 calibration prevents this. |
| `log K_0` row | BBC's Test 2 included `log K_0` (as `log α` with α = K_0) within a log-multiplicative basis. **However, BBC §4 close explicitly named "log K_0, (log K_0)(log 2), or one of many other forms involving K_0" as OPEN.** A pure `log K_0`-vs-K_0-pure-powers basis was NOT BBC's Test 2 basis. | **YES** — operator's basis isolates log K_0 with pure-power K_0^k coordinates, a basis BBC did not test. |
| `{K_0·c : c ∈ C}` bilinear products | BBC tested **log-form** (Σ a_k log c_k) at H = 10^20. **Bilinear-form (K_0 times c)** is structurally different from log-form (log K_0 + log c). | **YES** — bilinear products with named constants are a clean novelty axis. |

**See `_m2.3_calibration_anchor.md` for the full M2.3 success-predicate calibration consequences.**

## 5. Verification provenance

| Step | Detail |
|---|---|
| 1. Source URL | `https://www.davidhbailey.com/dhbpapers/khinchin.pdf` (author's personal archive at LBNL) |
| 2. Retrieval timestamp | 2026-05-15 ~19:50 JST |
| 3. File size | 172,853 bytes |
| 4. SHA-256 | `7dd18d84b93a36b85f4f94d23671a202258cb6517ccbaa5794edeadd0e793793` |
| 5. Extraction method | `pypdf.PdfReader().pages[i].extract_text()` (pypdf builtin, lossy on equations; symbol-level math reconstructed below) |
| 6. Extracted text size | 36,179 characters, 19 pages |
| 7. §4 read range | Lines 720–790 of extracted text |
| 8. Cross-check | DOI confirmed against OEIS A002210 reference list (canonical `00800-4`, NOT the hallucinated `00830-5`) |

### pypdf extraction caveats (transparency)

pypdf's text extraction does NOT preserve TeX math symbols cleanly. Specifically:
- Subscripts in `K_{-1}` rendered as `K−1` (the underscore-brace is lost; only the `−1` survives).
- Exponents in `10^70` rendered variously as `10**70`, `10 70`, or `1070` depending on the PDF's internal TeX encoding.
- Greek letters in basis names (α, γ, π) survive as plain characters.

The quoted passages in §3 above are reconstructed by reading the surrounding text and the published rendering on the AMS canonical page; the math symbols are inserted by hand based on context. The character-level pypdf output is at `C:\Users\shkub\AppData\Local\Temp\bbc_khinchin_text.txt` and remains the on-disk evidence.

## 6. Re-verification path (for any milestone that requires fresh confirmation)

```powershell
Invoke-WebRequest `
  -Uri https://www.davidhbailey.com/dhbpapers/khinchin.pdf `
  -OutFile khinchin.pdf
Get-FileHash khinchin.pdf -Algorithm SHA256
# Expected: 7dd18d84b93a36b85f4f94d23671a202258cb6517ccbaa5794edeadd0e793793

python -c "from pypdf import PdfReader; r=PdfReader('khinchin.pdf'); print(''.join(p.extract_text() for p in r.pages))" > khinchin.txt
Select-String -Path khinchin.txt -Pattern 'whether K0|integer coefficient|log K0'
```

## 7. AEAL discipline notes

- This entry is **load-bearing for M2.3**. Any change in BBC's reported parameters (D = 50, H = 10^70, 7350 dps for Test 1; 21-dim basis, H = 10^20 for Test 2) would invalidate the M2.3 calibration anchor. Re-verification SHOULD be repeated at M2.2 and again at M2.3 against the same SHA-256.
- The "open problems explicitly named" passage in §4 close is the warrant against scope-collapse onto BBC's already-tested basis.
- This is the entry that catches the operator's predicted M2 risk class. See `_fidelity_findings.md`.
