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

**Status:** `done` — H8 fire EXECUTED 2026-05-16 ~15:55 JST. Verdict: D2 + D3 CLEARED; D5 new finding (strengthening). No §Methods text adjustment required. Output: `literature/lit-010-bailey-plouffe-1997-recognizing.md` upgraded `fidelity_watch → verified`. Audit trail: `literature/_fidelity_findings.md` §8 + `mutation_log/m6_step1_bailey_1998_h8_fire_20260516.md` (12th entry). Commit hash: to be filled at commit time.

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

### §4.1 — Sub-classification of failure modes (structurally-unavailable vs scope-ceded)

**Authority:** operator M5 GREENLIGHT 2026-05-16 ~14:52 JST: *"add §4.1 sub-item to m6_preflight_checklist distinguishing structurally-unavailable (2.A-2.E, 2.G) from scope-ceded (2.F)."*

**Purpose:** the seven candidate structural arguments surveyed in M4 (`capability/symbolic_closure.gap.md` §2) fail for two qualitatively different reasons. §4 reports the aggregate "FUNDAMENTAL gap" verdict; §4.1 makes the substructure explicit so M6 §Discussion can frame the gap honestly without conflating the two failure modes.

**Sub-class A — Structurally-unavailable (6 of 7 candidates):**

| Candidate | Why structurally-unavailable |
|---|---|
| 2.A Lindemann–Weierstrass | Hypothesis `K_0 = e^α` for algebraic α is **not known to hold** (no such representation published; K_0's defining infinite product over Khinchin weights does not collapse to an algebraic exponent). |
| 2.B Schanuel | Conjecture itself is **unproven**; even conditional on Schanuel, the required `K_0 = exp(z)` for an explicit ℚ-linear z is **not known**. |
| 2.C Nesterenko 1996 | K_0 is **not among** the constants Nesterenko's modular-form-period method covers (π, e^π, Γ(1/4)); no published extension to Khinchin-class. |
| 2.D Mahler measure | Method applies to **algebraic numbers**; K_0's algebraic status is the major open question. |
| 2.E Galois | Requires K_0 algebraic with known minimal polynomial; K_0's algebraicity is **unknown**. |
| 2.G Height theory | Requires K_0 algebraic; same blocker as 2.E. |

**Common root:** all six are blocked by the **same external unknown** — K_0's arithmetic nature (transcendence + algebraic-independence-class membership). No published theorem resolves this unknown. Closure via any of 2.A, 2.B, 2.C, 2.D, 2.E, 2.G would require **new mathematics** in transcendence theory, not new machinery deployment. **This is the FUNDAMENTAL part of the gap.**

**Sub-class B — Scope-ceded (1 of 7 candidates):**

| Candidate | Why scope-ceded |
|---|---|
| 2.F Non-GKW CF-theoretic | Method-import from the GKW spectral family is **off-limits per `seeds/26 DO-NOT-REENTER` binding** (overlap with operator's active "Finite-Depth Transient Rigidity" manuscript would muddy attribution; theoretical-citation permitted, method-import prohibited). Independently, **no non-GKW CF-theoretic result strong enough is published**; lifting the binding alone would not yield closure. |

**Disposition:** the scope-ceded sub-class would be **partially-contingent** if the DO-NOT-REENTER binding were the only blocker, but the second clause (no non-GKW alternative published) renders 2.F equivalent to a structurally-unavailable candidate. **The scope-ceded labeling reflects mission-internal discipline, not external mathematical contingency.**

**M6 §Discussion framing implications:**

- The §Discussion paragraph in §4 should be read with §4.1 in mind: "FUNDAMENTAL" is the correct aggregate verdict because **6 of 7 candidates are structurally unavailable** AND **the 7th (CF-theoretic) is double-blocked** (scope-ceded internally + structurally-unavailable externally). The FUNDAMENTAL label is not weakened by 2.F's scope-ceded status because the same candidate also fails the external test.
- If a reviewer challenges the FUNDAMENTAL classification specifically on the CF-theoretic axis ("why didn't you try CF-theoretic methods?"), the §Discussion response is the §4.1 second clause: even setting aside the seeds/26 binding, no non-GKW CF-theoretic result is published that constrains integer-relation existence in B_D(C). The internal scope-cede and the external unavailability are independent facts that both hold.
- If a reviewer challenges the FUNDAMENTAL classification on the broader "machinery vs theorem" axis ("transcendence theorems exist; you just didn't deploy them"), the §Discussion response is the §4.1 Sub-class A common root: the machinery is in principle available (LW is elementary, Nesterenko is published, Mahler-measure tooling exists in pari/sage), but the THEOREMS do not apply because K_0 is not known to satisfy their preconditions.

**Anchor:** `capability/symbolic_closure.gap.md` §2 (candidate survey detail) + §4 (fundamental-vs-contingent classification with sensitivity analysis).

**Halt-and-flag class:** if M6 drafting treats 2.F's scope-ceded status as the primary basis for FUNDAMENTAL (it isn't; the structural unavailability of the other six candidates is the primary basis), halt drafting and re-read §4.1.

**Halt-and-flag class:** if M6 drafting attempts to claim "we proved structural non-existence" or "we close the M3 null structurally" without acknowledging the §4 fundamental gap, halt drafting and re-read this §4 + `capability/symbolic_closure.gap.md` before continuing.

**Trigger to fire:** at M6 drafting (during §Discussion or §Limitations writing).

---

## §5 — M5 Lean 4 statement-shape scope (NEW)

**Authority:** operator M5 CLOSURE RATIFIED 2026-05-16 ~15:48 JST: *"§5 (NEW): M5 Lean 4 formalization scope statement. The M6 §Methods text must distinguish 'statement-shape machine-checkable in Lean 4' from 'formally verified in Lean 4.' The current M5 scope is the former."*

**Anchor:** `m5/M5/{Definitions,Result,Axioms}.lean` at `gold/M5` = `208f6fc`; canonical axiom set in `m5/_print_axioms_output.txt`.

### §5.0 — The distinction (mandatory §Methods language)

| Concept | What M5 IS | What M5 is NOT |
|---|---|---|
| **Statement-shape machine-checkable in Lean 4** ✓ | The result *statement* (`m3_null_at_rigorous_bound : ¬ HasIntegerRelation basisDC H_rigorous`) is well-typed; Lean 4 + Mathlib4 confirms the predicate, basis, and bound have consistent types. | Lean does not prove this theorem from Mathlib4 + first principles. |
| **Formally verified in Lean 4** ✗ | (would require Lean-level proof of `pslq_cascade_implies_no_integer_relation` from Mathlib core, which the M4 FUNDAMENTAL gap forecloses) | The M5 theorem discharges via `exact pslq_cascade_implies_no_integer_relation` — an `axiom` declaration, not a proof. |

### §5.1 — Auxiliary-axiom trust boundary (mandatory §Methods enumeration)

The M5 result theorem is **structurally conditional**: given the auxiliary axioms enumerated below, the M3 null statement type-checks at `H_rigorous`. The §Methods text must enumerate this trust boundary explicitly.

**(a) Constant axioms (9 declarations in `m5/M5/Definitions.lean`).** The named real-valued constants `π`, `e`, `ln 2`, `ζ(2)`, `ζ(3)`, `γ`, `G`, `K₀`, and `log K₀` are encoded as opaque `axiom` declarations (`realPi`, `realE`, `realLn2`, `zeta2`, `zeta3`, `eulerMascheroni`, `catalanConst`, `K0`, `logK0`). They are NOT imported from Mathlib4's full constructions (`Real.pi` from `Mathlib.Data.Real.Pi.Bounds`, `Real.exp` from `Mathlib.Analysis.SpecialFunctions.Exp`, etc.). This is a **scope simplification** — Mathlib does provide `Real.pi`, `Real.exp`, and `Real.log` but NOT `Real.catalan`, `Real.eulerMascheroni`, or `Real.zeta3` at v4.14.0 (see §5.1 sub-item below for the cache rationale).

**(b) Evidence axioms (2 declarations in `m5/M5/Axioms.lean`).** The two load-bearing mission claims are encoded as axioms, not proven:

- `pslq_cascade_implies_no_integer_relation : ¬ HasIntegerRelation basisDC H_rigorous` — encodes the FBA Theorem 1 + Corollary 2 conclusion applied to the M3.2 cascade-stable null. Justified informally by FBA T1+Cor2 (paper-read fires at H8 in M6 drafting per §1) but **not proven from first principles in Lean 4**.
- `bbc_empirical_implies_no_integer_relation : ¬ HasIntegerRelation basisDC H_empirical_operational` — encodes the BBC-derived empirical-tier non-existence at the operational bound (post-§3.4 capping).

**(c) Acknowledgement axiom (1 declaration in `m5/M5/Axioms.lean`).** `M4_fundamental_gap : True ∧ True` is a documentary placeholder; its role is to provide a Lean-level handle for the M4 FUNDAMENTAL gap proposition that M6 §Discussion can cite. It is not load-bearing for the M5 result theorem.

**Numerical-binding shape stub (1 declaration).** `K0_value_first_digits` asserts the existence of a function recording the first 8 digits of K₀ (2.6854520…). Not used by the M5 result theorem; documentary only.

**Canonical audit-trail location:** `m5/_print_axioms_output.txt` (committed at `208f6fc`) shows the exact axiom dependency set for each of the four mission theorems, generated by `lake env lean PrintAxioms.lean`. Reproducibility check: re-running `PrintAxioms.lean` post-edit must reproduce this file byte-for-byte; any divergence indicates a trust-boundary leak.

### §5.2 — Mandatory §Methods language patterns

**Use** (correct):
- *"The result statement is encoded in Lean 4 with documented auxiliary axioms; the encoding type-checks against Mathlib v4.14.0; full formal verification requires further development beyond this mission's scope."*
- *"The Lean 4 skeleton (~385 source lines) makes the result's dependency structure machine-readable: the axiom set behind `m3_null_at_rigorous_bound` is exactly {`pslq_cascade_implies_no_integer_relation`} plus 9 opaque constant axioms plus Lean core (`propext`, `Classical.choice`, `Quot.sound`)."*
- *"Statement-shape Lean encoding with explicit trust boundary is a methodological contribution distinct from the numerical-and-rigorous-bound K₀ result: it makes the implicit assumptions of the two-tier predicate explicit and machine-checkable."*

**Avoid** (overclaims):
- ~~"formally verified in Lean 4"~~ (false — the proof is axiom application, not derivation)
- ~~"Lean 4 proof of the null result"~~ (false — there is no Lean-level proof, only a type-checked statement)
- ~~"machine-checked theorem"~~ (ambiguous in a way that misleads — the *statement* is machine-checked; the *theorem* is conditional)
- ~~"verified using Lean 4"~~ (verb "verified" implies first-principles derivation; this is not that)

**Operator's framing principle (verbatim):** *"This is not a weakening of the contribution. Statement-shape Lean 4 encoding with explicit trust boundary is a legitimate methodological contribution — it makes the result's dependency structure machine-readable. Honest framing strengthens the contribution; overclaiming weakens it."*

### §5.1 sub-item — Operational note on Mathlib cache import-closure-specific shape (mandatory §Methods footnote/paragraph)

**Authority:** operator M5 CLOSURE RATIFIED 2026-05-16 ~15:48 JST: *"§5.1 (sub-item): M6 §Methods should also note the operational fact discovered at pre-M5: the operator's Mathlib4 cache is import-closure-specific rather than uniformly pre-built. This is not a flaw in the mission's work; it's an honest operational note that informs why M5 chose the simplified import scope. One paragraph in §Methods."*

**The observation (one §Methods paragraph):** The Mathlib4 v4.14.0 package cache available to this mission was a build snapshot from a sibling project (`siarc-lean4`) on the operator's machine. Lake's `Replayed` mechanism re-uses pre-built `.olean` files when their cryptographic trace-hash matches the expected hash; this is fast (sub-second per module). However, the cache contains only the **import closure** of the sibling project's source files, not the full Mathlib library uniformly built. When the initial M5 implementation imported `Mathlib.Data.Real.Pi.Bounds` plus `Mathlib.Analysis.SpecialFunctions.{Log.Basic, Exp}`, 587 modules `Replayed` (matching the sibling project's import set) and then Lake began compiling modules outside that closure from scratch (8 parallel workers, observable in `lake build` log). This is not a deep-build failure — Lake operated correctly; the cache simply did not extend to the requested imports. The mission resolved the operational scope by simplifying M5 imports to `Mathlib.Data.Real.Basic` + `Mathlib.Data.List.Basic` (both inside the cache closure) and encoding `π`, `e`, `ln 2`, `log K₀`, `ζ(2)` as opaque axioms instead of Mathlib's full constructions. The resulting `lake build M5` completed in 218.1 s wall-clock from a clean `.lake/build/` tree. The choice to use opaque axioms for these named constants is therefore **not a defect of the formalization** — it is an operationally-honest adaptation to the available cache closure, consistent with the §5 scope statement above (statement-shape verification, not formal verification).

**Disposition:** §Methods should include this paragraph (or its equivalent) to pre-empt any reviewer question about why Mathlib's `Real.pi` was not imported.

**Halt-and-flag class:** if M6 drafting omits the §5 trust-boundary enumeration entirely (e.g., §Methods describes M5 as "Lean 4 formalization" without listing the auxiliary axioms), halt drafting and re-read this §5 before continuing.

**Trigger to fire:** at M6 drafting (during §Methods §M5-formalization-scope sub-section writing).

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
