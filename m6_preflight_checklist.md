# M6 Preflight Checklist

Pre-M6-drafting items scheduled during M3.2b execution per operator
U-MISSION-M3.2b-RATIFICATION (2026-05-16 ~10:00 JST).

**Purpose:** ensure no scheduled-but-deferred work is forgotten when M6
manuscript drafting begins. Each item below carries trigger conditions,
provenance, and the §section in M6 it will land in.

**Status convention:** `pending` until M6 drafting starts; `in_progress`
when actively being addressed; `done` when reflected in M6 manuscript
draft and verified via the heuristic class indicated.

**Authority:** these items DO NOT consume mutation budget (they are
field-map updates and framing requirements, not hypothesis changes).
Mutation budget at M2 milestone-block remains 0/1 consumed.

---

## §1 — Bailey 1998 H8 paper-read (rigorous-tier proof-of-bound)

**Status:** `pending` — DO NOT EXECUTE DURING M3 OR M4. Execute during M6 drafting.

**Trigger condition (MUST execute when ALL true):**
- M6 manuscript will cite the rigorous tier (`verification_class = proven_corollary`, H_rigorous = 1.036 × 10⁷²) as proof-of-bound for the EF1-complement null result.
- This is the deferral condition specified in U-MISSION-L: "If M3 produces a result that M6 will cite the rigorous tier as proof-of-bound, then H8 fires on Bailey 1998 before M6 submission."
- Per M3.2a outcome (commit `d55ffbc`), the rigorous tier is established and M6 will cite it. **Trigger is armed; execution is scheduled for M6 drafting phase.**

**H8 paper-read requirements (verbatim from U-MISSION-J H8 wording):**
- Direct reading of the primary source (paper, preprint, supplementary material). Web aggregators, citation databases, and LLM-mediated summaries are not sufficient.
- For paywalled or non-digitized primary sources, mark `verified_independently: false` with the specific blocker and do not propagate the claim into the predicate.

**Specific paper-read scope (two distinct claims):**

### §1.D2 — γ = √(4/3) boundary-case claim

Bailey 1998 (or successor) is the canonical citation for PSLQ's threshold parameter γ ∈ (1, √(4/3)] and the boundary case γ = √(4/3) ≈ 1.1547. The mission's empirical scope claim and rigorous bound derivation both depend on γ being at-or-near the boundary; mpmath's PSLQ implementation chooses γ internally. Paper-read must verify:
- (D2.a) Bailey's exact statement of the γ range.
- (D2.b) Whether the rigorous bound theorems (FBA 1999 Theorem 1 + Corollary 2 invoked in `harness/rigorous_bound.py`) require γ = √(4/3) strictly, γ < √(4/3) strictly, or any γ in the stated range.
- (D2.c) Whether mpmath's chosen γ value (whatever it is internally — needs separate code-trace verification against mpmath sources) satisfies the precondition of FBA Theorem 1 + Corollary 2 as Bailey stated them.

If (D2.c) fails or is ambiguous, the rigorous tier must be downgraded to `field_standard_practice` for the M6 manuscript and the §Discussion must surface the reason.

### §1.D3 — mpmath-cited-source claim

`harness/rigorous_bound.py` derives H_rigorous from observed mpmath verbose-output behavior using FBA Theorem 1 + Corollary 2 as the underlying theorem. mpmath's PSLQ documentation may cite Bailey 1998 as its source paper, OR may cite an FBA 1999 paper, OR neither. Paper-read must verify:
- (D3.a) Whether mpmath documentation explicitly cites Bailey 1998 (and which version — original, errata-corrected, or successor paper).
- (D3.b) Whether mpmath's algorithm matches the algorithm described in the cited paper (or, if cited paper differs from FBA 1999, whether the gap matters for the rigorous bound derivation).
- (D3.c) Whether the FBA 1999 theorem (used in `rigorous_bound.py`) and the algorithm mpmath actually implements are consistent at the level needed for the bound to hold.

If (D3.c) reveals a gap (e.g., mpmath implements PSLQ-PRIMA from a later paper that has different bound-stability properties than FBA 1999 PSLQ), the rigorous tier must be re-derived from the actually-implemented algorithm or downgraded.

**Owner of result:** `_fidelity_findings.md` §7 (new section), and any updates propagated to `harness/rigorous_bound.py` docstring + `_m2.3_calibration_anchor.md` §7.10 (new sub-section, requires mutation_log entry per gold/M2 §7-freeze rule).

**Halt-and-flag class:** if H8 paper-read on Bailey 1998 surfaces a gap, halt M6 drafting and surface as U-MISSION-N (new mission letter) before manuscript submission.

---

## §2 — Apples-to-stronger-apples framing care (M6 §Introduction + §Results)

**Status:** `pending` — DO NOT DRAFT M6 §INTRODUCTION/§RESULTS WITHOUT THIS GUARDRAIL.

**Provenance:** operator U-MISSION-M3.2b-RATIFICATION 2026-05-16 ~10:00 JST verbatim:

> The M6 manuscript framing for H_rigorous = 10⁷² vs BBC H = 10⁷⁰ must be apples-to-stronger-apples, not apples-to-apples. BBC tested EF1 (pure-power, grandfathered) at 10⁷⁰ empirical. This mission tests the EF1-complement at 10⁷⁰ empirical AND 10⁷² rigorous. The contribution is two-tier reporting on a novel basis, not bound-beating on the same basis.

### §2.a — Comparative-claim guardrails

**WHAT THE M6 MANUSCRIPT MUST NOT CLAIM:**

- ❌ "We improve on BBC's bound by 2 orders of magnitude" (this would be apples-to-apples on the same basis; BBC and this mission tested *different* bases).
- ❌ "We extend BBC's null result to higher heights" on the EF1-pure-power basis (we did not test the EF1 basis at all — it is grandfathered out per `selected.md` §2.A).
- ❌ "Our bound exceeds BBC's bound" without naming the basis distinction (creates ambiguity that a reviewer will flag).

**WHAT THE M6 MANUSCRIPT MUST CLAIM:**

- ✅ Two-tier reporting (`field_standard_practice` empirical at H = 10⁷⁰ + `proven_corollary` rigorous at H = 1.036 × 10⁷²) on the **EF1-complement** basis (log K_0, bilinear K_0·c_i for c_i ∈ C, hybrid log+bilinear).
- ✅ The novel-basis contribution: BBC 1997 §4 explicitly named log K_0, (log K_0)(log 2), and "many other forms involving K_0" as **open**. This mission's basis tests entries from that named-open complement.
- ✅ The methodological contribution: two-tier verification class structure under H9 (rigorous + empirical) is novel — BBC's null was empirical-only at the time of publication.
- ✅ The basis-class boundary is explicit. EF1 (pure-power) is BBC-grandfathered prior art; EF1-complement is mission scope.

### §2.b — §Introduction framing requirements

The M6 §Introduction must establish, in this order:
1. The Khinchin-K_0 algebraic-relations problem (general).
2. Prior art:
   a. BBC 1997 §4 Test 1 — pure-power null at H ≤ 10⁷⁰ (EF1; grandfathered prior art).
   b. khinchin-signature-pslq (operator's 2026-04-17 paper) — algebraic-combination relations on the S_n family (EF2; grandfathered prior art).
   c. GKW-method-ceded prior art per `seeds/26 DO-NOT-REENTER` (EF3).
3. The named-open complement: log K_0 row, bilinear K_0·c rows, hybrid log+bilinear combinations (this mission's scope, EF1+EF2+EF3 complement).
4. This mission's contribution: two-tier null on the complement, with rigorous tier exceeding BBC's empirical bound by 2 orders.

The two-tier structure (§3) and the basis-class distinction (§2) must be visible in the abstract, not buried in §Methods.

### §2.c — §Results framing requirements

The §Results numerical claims must always carry:
- The basis class explicit (e.g., "On the EF1-complement basis B_D(C) at D=6, |C|=7, n=15...").
- The verification class explicit (`field_standard_practice` for H_empirical, `proven_corollary` for H_rigorous).
- The PSLQ/lindep stability evidence summary (cascade verdict, identical K iteration count across 4× precision range, gp_lindep agreement).

The §Results should NOT compare to BBC's H = 10⁷⁰ as if it were the same measurement; it must compare as "stronger basis-coverage at equal-or-better bound" with the basis-class footnote.

### §2.d — §Discussion (or §Limitations) requirements

Must explicitly state:
- BBC's EF1 basis was not tested by this mission (grandfathered).
- BBC's algorithm + precision were comparable but not identical to mpmath's PSLQ (mpmath internals depend on H8 paper-read in §1).
- The bound improvement (10⁷⁰ → 10⁷²) is on a different basis, not on the same basis at higher precision.
- Future work: testing EF1+EF1-complement union basis (n=22) at H ≥ 10⁷² would close the apples-to-apples gap, with wall-clock cost increasing as ~22³/15³ ≈ 3.16× per cascade step.

**Owner of result:** M6 manuscript files (when authored). Cross-reference back to this checklist in M6 §Introduction footnote and §Results footnote.

**Halt-and-flag class:** if M6 drafting attempts to claim "we improved on BBC's bound" without the basis-class distinction, halt drafting and re-read this §2 before continuing.

---

## §3 — Other M6-deferred items (open list)

### §3.1 — selected.md re-anchor (if applicable)

If M6 cites `selected.md` §2.A (S_n grandfathered family) as prior art, verify that the `selected.md` content reflects the operator's 2026-04-17 paper as the authoritative citation. `selected.md` is frozen at gold/M1; any citation in M6 must match the frozen content.

**Status:** `pending`.

### §3.2 — Reproducibility appendix

M6 reviewers will likely request reproducibility instructions. Compose appendix referencing:
- Repository commit `d55ffbc` (M3.2a) and the M3.2b commit (TBD when sweep completes).
- Exact command: `python harness/sweep.py --m32-primary-measurement --m32-primary-greenlighted` (M3.2a) and `python harness/sweep.py --full --m32-full-greenlighted` (M3.2b).
- Wall-clock observed: 66.5 min (M3.2a) + (TBD) min (M3.2b).
- mpmath version, Python version, PARI/GP version (capture during M3.2b run for completeness).

**Status:** `pending`.

### §3.3 — JSONL data deposit

If M6 venue requires data deposit (Zenodo, Dryad, or similar), upload the canonical JSONL files (m32a + m32b) with a versioned identifier matched to the M6 submission.

**Status:** `pending`.

### §3.4 — Operational-bound capping observation (M6 §Discussion methods contribution)

**Authority:** operator U-MISSION-N RESOLUTION 2026-05-16 ~11:18 JST verbatim:
> "the operational-bound capping observation is a small but genuine methodological contribution. M6 §Discussion should include a paragraph noting that the BBC empirical scaling extrapolates outside the algorithm's maxcoeff bound at small n, and that operational empirical bounds must be reported as min(formula, maxcoeff) to remain testable. This isn't a major contribution — but it's the kind of small methods observation that strengthens the manuscript's overall density."

**Background:** M3.2b at canonical P=2160, c=2.06, maxcoeff=10⁷⁰ surfaced that the BBC empirical scaling `H = c · 10^(P/(c·n))` evaluates to ~10⁵²⁴ at n=2 and ~10³⁴⁹ at n=3 — both far above the algorithm's maxcoeff search bound of 10⁷⁰. PSLQ-with-maxcoeff cannot detect any integer relation whose maximum coefficient exceeds maxcoeff, regardless of the formula's extrapolation. Reporting the uncapped formula as the operational empirical bound at small n is vacuous: the algorithm did not search the formula's claimed range.

**M6 §Discussion paragraph (draft, ~150 words):**

> Across the 64 empirical sub-bases of `m32b_empirical_sweep.jsonl`, the canonical operational empirical bound `H_empirical_operational = min(c·10^(P/(c·n)), 10^maxcoeff_exp)` differs from the uncapped BBC scaling formula `H_empirical_formula = c·10^(P/(c·n))` at every n ≤ 14 sub-basis (at P=2160 dps, c≈2.06, maxcoeff=10⁷⁰, the formula yields ~10⁷⁰ exactly at n≈14.97 ≈ 15). At n=15 (the primary sub-basis), formula ≈ 7.997×10⁶⁹ ≤ maxcoeff and the cap is inactive. At small n (n=2, 3), the formula evaluates well above the maxcoeff bound (10⁵²⁴ and 10³⁴⁹ respectively); reporting these as operational bounds would overclaim the searched range. We retain both values in the JSONL output: `H_empirical_operational` for predicate evaluation and table reporting; `H_empirical_formula` for transparency about where the empirical extrapolation diverges from the searched range. This is a small methodological refinement to BBC-class empirical-tier reporting at parameter regimes where the scaling formula extrapolates outside the algorithm's maxcoeff bound.

**Status:** `pending`.

**Anchor:** `literature/_m2.3_calibration_anchor.md` §7.10 (operational-bound capping clause); `methodology/heuristics.md` H10 (full-regime dry-run mandate that surfaced the underlying gap); `mutation_log/m3.2b_u_mission_n_resolution_20260516.md` (9th mutation_log entry recording the resolution).

**Trigger to fire:** at M6 drafting (during §Discussion writing).

---

## §4 — M4 capability-gap framing (M6 §Discussion or §Limitations)

**Status:** `pending` — DO NOT DRAFT M6 §DISCUSSION WITHOUT THIS PARAGRAPH.

**Authority:** operator M3 CLOSURE + M4 GREENLIGHT 2026-05-16 ~14:32 JST verbatim:
> A documented capability gap at M4 is not a failure. Per Brief §M4(b), it's an acceptable outcome and a publishable observation in M6 §Discussion: "Structural closure of the null result was attempted via [survey]; no available structural argument is strong enough to constrain integer-relation existence at the tested bound; the null stands on numerical and rigorous-bound evidence per the two-tier predicate."

**Background:** M4 (per Brief §M4) attempted symbolic closure of the M3 null result via survey of seven candidate structural arguments (Lindemann–Weierstrass, Schanuel, Nesterenko, Mahler-measure, Galois, non-GKW CF-theoretic, height theory) + a four-path SymPy 1.14.0 probe (`is_transcendental`/`is_irrational`, `nsimplify`, Groebner-on-symbolic-basis, transcendence-theorem applicability check). All seven candidates failed; all four probe paths returned `closure_achieved=False`. M4 closes as a Brief §M4(b)-compliant **FUNDAMENTAL** capability gap. Full record: `capability/symbolic_closure.gap.md` (M4 deliverable); 10th mutation_log entry: `mutation_log/m4_symbolic_closure_gap_20260516.md`.

**Required M6 §Discussion paragraph (operator-anchored, ~150 words, draft):**

> Symbolic closure of the M3 null result was attempted in M4 via survey of seven candidate structural arguments (Lindemann–Weierstrass, Schanuel, Nesterenko, Mahler-measure, Galois, non-GKW continued-fraction-theoretic, and height theory) and a four-path SymPy probe (`is_transcendental`/`is_irrational`, `nsimplify` against a named-constants basis, Groebner basis on the symbolic basis B_D(C), and transcendence-theorem applicability check). Every candidate failed at the same root: K_0's transcendence status is itself the major open question in this corner of the literature, and any structural certificate strong enough to rule out integer relations in B_D(C) at H ≤ 1.036 × 10⁷² would imply progress on that question. We classify this gap as fundamental (no known structural result is strong enough; not merely a machinery-availability problem) per the M4 brief, and the null result stands on numerical and rigorous-bound evidence per the two-tier predicate (H_empirical_operational = 10⁷⁰ `field_standard_practice`; H_rigorous = 1.036 × 10⁷² `proven_corollary`).

**Anchor (cross-references in M6):**
- `capability/symbolic_closure.gap.md` §2 (candidate survey) + §3 (SymPy probe) + §4 (fundamental classification) for full audit trail.
- `capability/_m4_symbolic_probe.py` + `capability/_m4_symbolic_probe.jsonl` for reproducibility of probe.
- `mutation_log/m4_symbolic_closure_gap_20260516.md` for the M4 closure event entry.

**Halt-and-flag class:** if M6 drafting attempts to claim "we proved structural non-existence" or "we close the M3 null structurally" without acknowledging the §4 fundamental gap, halt drafting and re-read this §4 + `capability/symbolic_closure.gap.md` before continuing.

**Trigger to fire:** at M6 drafting (during §Discussion or §Limitations writing).

---

## Maintenance protocol

When an item activates:
1. Update item `Status:` from `pending` to `in_progress`.
2. Open a corresponding SQL todo in this session's database.
3. Execute the work, citing the section number in commit messages.
4. When done, update `Status:` to `done` with a short result summary and commit hash citation.

When a new pre-M6 item is identified (during M3.2b review, M4, or M5):
1. Add as a new §X.N sub-section here (NOT in mutation_log/, unless it's a hypothesis change).
2. Cite the operator directive that scheduled it (or the heuristic that surfaced it).
3. Set initial `Status: pending`.

---

**Provenance footer:**
- Created: 2026-05-16 ~10:05 JST during M3.2b execution.
- Authority: operator U-MISSION-M3.2b-RATIFICATION 2026-05-16 ~10:00 JST.
- Predicate anchor: `literature/_m2.3_calibration_anchor.md` §7 (M2.3 ratified at gold/M2, commit `ca9c989`).
- Heuristic anchors: H8 (paper-read verification), H9 (verification classes), H6 (no-double-counting prior art).
