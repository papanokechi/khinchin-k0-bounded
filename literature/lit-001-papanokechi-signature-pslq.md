# lit-001 — papanokechi/khinchin-signature-pslq (2026)

**Status:** verified · **Class:** primary_paper · **Method:** paper_read_verified
**Verified at:** 2026-05-15 ~19:50 JST
**Mission role:** primary-tier prior art (H6 namespace audit + legitimacy anchor for M1.2 sub-question per `targets/selected.md` §2.A)

---

## 1. Citation

Papanokechi (April 2026 draft). _"A null PSLQ-stable spectrum for the Khinchin signature on π's continued-fraction partial quotients."_ Intended venue: Experimental Mathematics (Taylor & Francis). Draft hosted at `github.com/papanokechi/khinchin-signature-pslq`. License split per repo: MIT (code) / CC-BY 4.0 (docs); Zenodo DOI pending issuance.

Operator's own prior work. Authoring is unblinded for purposes of this internal ledger; for any downstream venue submission the citation will respect that venue's blinding rules.

## 2. Statement (verbatim from `paper/khinchin_signature_expmath_note.tex` Discussion section)

> "Templates involving n^{1/2}, n^2, or algebraic combinations of K_0 with other known constants lie entirely outside the tested family and remain open."

This passage is the **legitimacy anchor** for the present `khinchin-k0-bounded` mission. The mission's bounded sub-question (M1.2 form, refined per U-MISSION-G) studies the hybrid basis B_D(C) = {1, K_0, K_0², …, K_0^D, log K_0} ∪ {K_0·c : c ∈ C}, which is exactly the family the signature paper named as out-of-scope-but-open. The §2.A scope-exclusion clause in `selected.md` (signature statistic S_n family is ceded to this paper) is the reverse direction of the same boundary.

## 3. Computational summary (paper-read-verified)

| Parameter | Value |
|---|---|
| Source constant | π (its regular continued fraction) |
| Coordinate family tested | {S_n, log S_n, S_n - K_0, log n} where S_n = (a_1·a_2·…·a_n)^(1/n) is the Khinchin signature |
| Working precision | 300 dps |
| Confirmation precision | 600 dps |
| `maxcoeff` | 10^3 |
| Residual threshold | 10^{-20} |
| Template count | 6 (fixed 3D and 4D templates) |
| Total PSLQ attempts | 546 (conservative cap) |
| Stability-certified prefix | n = 1..91 |
| Stability check bits | {256, 512, 1024} |
| Result | All 546 attempts UNSUPPORTED at the maxcoeff bound |

## 4. Independent verification audit trail

- **2026-05-15 ~19:50 JST** — Fetched `paper/khinchin_signature_expmath_note.tex` via GitHub MCP `get_file_contents` (raw mode).
- **2026-05-15 ~19:50 JST** — Read the Discussion section in full; the quoted passage (§2 above) confirmed verbatim.
- **2026-05-15 ~19:50 JST** — Read `README.md` and `aeal/methodology.md` of the same repo to triangulate the methodology framing.
- No further computational re-derivation attempted at M2.1 (the M3.1 harness will re-derive a PSLQ residual matching the paper's reported behavior on the K_0-only basis, not the S_n basis, as part of the M3.1 calibration step).

## 5. Independence-overlap audit (H6, namespace check)

- **Coordinate family overlap:** ZERO. The signature paper's family is {S_n, log S_n, S_n − K_0, log n}; the present mission's family is {1, K_0, K_0², …, K_0^D, log K_0, K_0·c}. The single coordinate they could share — K_0 — is the **constant being tested**, not a coordinate of the signature paper's basis (which uses S_n, an _empirical_ geometric mean over a finite prefix, NOT K_0 directly).
- **Methodology overlap:** PSLQ at high precision is shared; this is generic and not exclusive.
- **Conclusion:** clean separation. Citation as primary-tier prior art is structural anchoring, not a competing claim.

## 6. Mission-specific implications

- The signature paper's null result on its coordinate family does NOT constrain the present mission's null/positive search on B_D(C). They are different bases.
- The signature paper's Discussion section having flagged "algebraic combinations of K_0 with other known constants" as open _is_ the publishable warrant for this mission. The present mission produces explicit numerical evidence (null or positive) on a sub-family of those algebraic combinations.
- For Zenodo deposit at M6: cite this paper as `lit-001` primary-tier prior art with the legitimacy-anchor passage quoted.

## 7. M3.1 harness dependencies (if any)

- **Direct dependency:** NONE. The M3.1 harness does not reuse the signature paper's harness code or data.
- **Indirect dependency:** the operator's PSLQ workflow (precision-cascading 300/600 dps, residual threshold, stability-check bit-doubling) is inherited from the signature paper as a calibration template. This will be documented in `capability/mpmath.available.md` updates at M2.2 if the M3.1 harness adopts the same cascade.
