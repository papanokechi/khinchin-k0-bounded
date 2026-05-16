# M6 Preflight compliance cross-reference

**Purpose:** map every item in `m6_preflight_checklist.md` to the §section in
`paper/main.tex` that addresses it. Per operator M6 GREENLIGHTED directive,
each preflight item §X.Y must have a corresponding §Methods / §Discussion /
§Results passage.

**Compliance status as of draft commit:** see column 4. Status values:
`addressed` (passage exists in `paper/main.tex` and addresses the preflight
requirement), `pending_external` (depends on operator decision outside the
manuscript, e.g.\ Zenodo deposit DOI), `forward_flagged` (manuscript-internal
follow-up before submission).

**Authority chain:**
- preflight specification: `m6_preflight_checklist.md` (commits `d08317c` +
  `de831c0`)
- manuscript: `paper/main.tex` (this commit)
- canonical artifacts: gold/M1=15b216f, gold/M2=ca9c989, gold/M3=9c2702d,
  gold/M4=fd13eeb, gold/M5=208f6fc

---

## §1 — Bailey 1998 H8 paper-read (rigorous-tier proof-of-bound)

| Preflight requirement | Manuscript anchor | Status |
|---|---|---|
| §1.D2 — γ = √(4/3) boundary case | §2.3 ``Algorithm-chain citation and γ boundary case'' explicitly states T1+Cor2 invoked, T3 not invoked (carries γ > √(4/3) strict). | addressed |
| §1.D3 — mpmath-cited-source claim | §2.3 displays the chain `mpmath → Bailey 1998 §2 → FBA 1999` with citation. | addressed |
| §1.D5 — Bailey 1998 ``general rule'' verbatim citation | §2.4 ``The H9 verification-class taxonomy and the Bailey–Plouffe `general rule''' quotes the §2 passage verbatim and uses it as primary-source warrant for the `field_standard_practice` class. | addressed |
| Algorithm-chain note (operator-supplied refinement at M6 Step 2 GREENLIGHT) | §2.3 (single paragraph) | addressed |
| T1+Cor2 specificity (operator-supplied refinement at M6 Step 2 GREENLIGHT) | §2.3 explicitly: ``The rigorous tier of this manuscript invokes [Theorem 1] and [Corollary 2] specifically; it does *not* invoke [Theorem 3]''. | addressed |

---

## §2 — Apples-to-stronger-apples framing (§Introduction + §Results)

| Preflight requirement | Manuscript anchor | Status |
|---|---|---|
| §2.a — Comparative-claim guardrails (what NOT to claim) | §4.1 explicitly: ``We *do not* claim a bound improvement on the BBC 1997 basis. The bases are different; a direct `we improve BBC's 10^70 to 10^72' framing would be apples-to-apples on bases that are not the same and is therefore avoided.'' | addressed |
| §2.a — What the manuscript MUST claim (two-tier reporting on EF1-complement) | Abstract; §1 ``The contribution'' item (a); §3.2 ``The primary cascade and its two-tier bounds''; §4.1. | addressed |
| §2.b — §Introduction order: K_0 problem → prior art (BBC + signature + GKW-cede) → named-open complement → contribution | §1 follows this exact order in the four paragraph blocks ``The bounded sub-question'', ``Prior art and the named-open complement'', ``The contribution''. | addressed |
| §2.c — §Results numerical claims carry basis class + verification class + cascade evidence | Tables 1 (aggregate), 2 (primary cascade), 3 (per-family) all carry verification-class column; §3.1–§3.5 narrative carries basis class and cascade evidence. | addressed |
| §2.d — §Discussion / §Limitations: BBC's EF1 not tested by this mission; bound improvement on different basis | §4.1 final paragraph: ``A future apples-to-apples comparison would test the union basis (EF1 plus EF1-complement, dimension n = 7 + 8 = 22) at H ≥ 10^72''. | addressed |

---

## §3 — Other M6-deferred items

| Preflight requirement | Manuscript anchor | Status |
|---|---|---|
| §3.1 — selected.md re-anchor (citation consistency with gold/M1) | Manuscript cites the signature paper as legitimacy anchor (§1, lit-001), consistent with `targets/selected.md` §2.A (frozen at gold/M1). | addressed |
| §3.2 — Reproducibility appendix | Appendix A ``Reproducibility'' has commands, environment, paper-read SHA-256 hashes, wall-clock, canonical artifact paths. | addressed |
| §3.3 — JSONL data deposit decision | Zenodo deposit deferred per operator directive; halt for operator review before deposit step. | pending_external |
| §3.4 — Operational-bound capping methods observation | §4.2 ``Operational-bound capping observation'' (full paragraph; matches preflight §3.4 draft text closely, with explicit grounding in Bailey 1998's ``somewhat greater than'' hedge per D5 finding). | addressed |

---

## §4 — M4 capability-gap framing (§Discussion or §Limitations)

| Preflight requirement | Manuscript anchor | Status |
|---|---|---|
| §4 — Required M6 §Discussion paragraph on M4 FUNDAMENTAL gap (7-candidate survey + 4-path probe + root cause = K_0 transcendence status) | §4.3 ``Capability gap: symbolic closure of the null result is fundamental'' (full subsection). | addressed |
| §4.1 — Structurally-unavailable (6/7) vs scope-ceded (1/7) sub-classification | §4.3 ``Sub-classification of the failure modes'' paragraph: ``Six of seven are structurally unavailable on external grounds alone... The seventh (non-GKW CF-theoretic) is internally scope-ceded under a mission-procedural binding, but is also structurally unavailable externally...'' | addressed |
| §4.1 — What we are NOT claiming (no structural non-existence, no structural closure) | §4.3 final paragraph: ``We are not claiming structural non-existence of integer relations on B_D(C), nor a structural closure of the M3 null.'' | addressed |

---

## §5 — M5 Lean 4 statement-shape scope

| Preflight requirement | Manuscript anchor | Status |
|---|---|---|
| §5.0 — Distinction table: statement-shape machine-checkable IS / formally verified is NOT | §2.6 ``What the encoding IS and is NOT'' paragraph. | addressed |
| §5.1 — Auxiliary-axiom trust boundary enumeration (9 constant + 2 evidence + 1 acknowledgement + 1 stub) | §2.6 ``Auxiliary-axiom enumeration'' paragraph (full enumeration; cites `m5/_print_axioms_output.txt`). | addressed |
| §5.2 — Mandatory §Methods language (use ``statement-shape machine-checkable''; avoid ``formally verified'') | §2.6 ``What the encoding IS and is NOT'' explicitly uses ``statement-shape machine-checkable'' and ``avoids the phrasing `formally verified in Lean 4'''. | addressed |
| §5.1 sub-item — Mathlib cache import-closure-specific operational note | §2.6 ``Mathlib cache operational note'' paragraph. | addressed |

---

## Out-of-band items (operator-supplied at M6 Step 2 GREENLIGHT, 2026-05-16 ~16:00 JST)

| Item | Manuscript anchor | Status |
|---|---|---|
| D5 incorporation — Bailey 1998 §2 ``general rule'' verbatim as primary-source warrant for `field_standard_practice` | §2.4 (full quoted passage). | addressed |
| Algorithm chain note — `mpmath → Bailey 1998 → FBA 1992 preprint → FBA 1999` (forestall referee confusion about 1998 vs 1999) | §2.3. | addressed |
| T1+Cor2 specificity note — rigorous tier cites T1+Cor2 only; T3 not invoked; γ = √(4/3) boundary by continuity | §2.3 explicitly. | addressed |

---

## Brief §M6.1 mandated sections

| Brief §M6.1 section | Manuscript anchor | Status |
|---|---|---|
| §Introduction (bounded sub-question + two-anchored legitimacy + EF1/EF2/EF3 scope distinction) | §1. | addressed |
| §Methods (basis construction, two-tier predicate, M3.1 harness mpmath + PARI/GP, H9 taxonomy with Bailey 1998 anchor, algorithm chain note, T1+Cor2 specificity, M5 statement-shape scope) | §2. | addressed |
| §Results (M3.2 65/65 null, two-tier bounds, bit-for-bit reproducibility, gp_lindep corroboration) | §3. | addressed |
| §Discussion (M4 gap + 7-candidate survey + sub-classification, operational-bound capping, apples-to-stronger-apples) | §4. | addressed |
| §Reproducibility appendix (env lock, expected runtime, repo URL, gold tag commit hashes, paper-read SHA-256) | Appendix A. | addressed |
| §Appendix B (AEAL methodology note — 6 halts, 10 heuristics, bidirectional property, health-score retrospective) | Appendix B. | addressed |

---

## AEAL methodology cross-reference

| AEAL component | Manuscript anchor | Status |
|---|---|---|
| H1 PSLQ cascading-precision triage | §2.5 ``Harness architecture'' + Appendix B H1 entry. | addressed |
| H2 Literature-ledger prioritization | Appendix B H2 entry. | addressed |
| H3 Stall-diagnostic timing | Appendix B H3 entry. | addressed |
| H4 Capability-gap escalation | §4.3 (M4 gap as instance) + Appendix B H4 entry. | addressed |
| H5 Mutation-log discipline | Appendix B H5 entry. | addressed |
| H6 Namespace audit | Appendix B H6 entry. | addressed |
| H7 Functional verification on capability claims | Appendix B H7 entry. | addressed |
| H8 Paper-read verification on literature claims | §2.3 (algorithm chain) + §2.4 (Bailey 1998 quote) + Appendix B H8 entry. | addressed |
| H9 Theorem-vs-heuristic classification | §2.4 (full taxonomy) + Tables 1–3 (verification-class column) + Appendix B H9 entry. | addressed |
| H10 Full-regime dry-run mandate | Table 1 (H10 pre-canonical row) + Appendix A (`--m31-extended-dry-run` command) + Appendix B H10 entry. | addressed |
| Bidirectional-verification property | Appendix B §B.2. | addressed |
| 6-halt-event count + health-score retrospective | Appendix B §B.3. | addressed |

---

## Halt-and-flag triggers (to monitor during operator review of the draft)

The following preflight items are armed for halt-and-flag if violated by the
draft text. CLI judgment of current draft: no operator-visible halts
triggered.

**Internal review note (rubber-duck critique pass, 2026-05-16):** prior to
operator review, a rubber-duck pass over the draft identified two
factual issues that were caught and resolved before commit: (i) the
rigorous tier $\Hrig$ was originally stated as a coefficient-height
bound rather than a Euclidean-norm bound (FBA T1 and Bailey 1998 §2
Step 5 both bound the Euclidean norm); (ii) the primary $n=15$
empirical operational bound was originally stated as $10^{70}$ when the
formula yields $\approx 7.997\times 10^{69}$ (the cap is inactive at
$n=15$). Both are corrected in the committed draft. This is the
halt-and-flag pattern working as designed at internal review: catch
before commit, no operator halt required.

| Preflight halt class | Trigger condition | Current draft status |
|---|---|---|
| §1 halt-and-flag | H8 paper-read on Bailey 1998 surfaces a gap | NOT TRIGGERED (D2 + D3 cleared; D5 strengthens) |
| §2 halt-and-flag | M6 claims ``we improved on BBC's bound'' without basis-class distinction | NOT TRIGGERED (§4.1 explicitly avoids this framing) |
| §4 halt-and-flag (a) | M6 treats 2.F's scope-ceded status as primary basis for FUNDAMENTAL | NOT TRIGGERED (§4.3 ``primarily on the structural unavailability of the six external candidates, with the seventh as a double-blocked corroborating case'') |
| §4 halt-and-flag (b) | M6 claims ``we proved structural non-existence'' or ``we close the M3 null structurally'' | NOT TRIGGERED (§4.3 explicitly: ``We are not claiming structural non-existence...'') |
| §5 halt-and-flag | §Methods omits trust-boundary enumeration | NOT TRIGGERED (§2.6 ``Auxiliary-axiom enumeration'' is the full trust boundary) |
| Drafting-discipline halt | §Results or §Discussion contains a claim without paper-read citation or canonical JSONL entry | NOT TRIGGERED (rubber-duck pass surfaced two pre-commit factual issues; both fixed before commit; no claims without canonical backing remain) |
| Norm-vs-height halt | Rigorous tier $\Hrig$ stated as coefficient-height bound when FBA T1 only bounds Euclidean norm | NOT TRIGGERED in committed draft (caught at rubber-duck; abstract / §2.2 / §3.2 / §4.1 / §4.3 now phrase Tier 2 as Euclidean-norm bound with explicit implied height $\Hrig/\sqrt{n}$) |

---

## Final note

This compliance cross-reference is intended to be re-read by the operator
during paper/main.tex review. If any row above transitions from
``addressed'' to ``regression'' during operator review (e.g., the operator
requests a §Methods passage edit that removes the T1+Cor2 specificity
note), the row should be re-marked and the manuscript text adjusted.

The full operator-review halt point is at M6 Step 3: Zenodo deposit
decision is deferred until the operator has reviewed `paper/main.tex` end
to end. This compliance file is a checklist support artifact for that
review; it is not a substitute.
