# capability/symbolic_closure.gap.md — Capability Gap: Symbolic closure of M3 null result is FUNDAMENTAL

**Date documented:** 2026-05-16 ~14:32 JST (M4 phase, post gold/M3)
**Discovery context:** M4 (Brief §M4) attempt at symbolic closure of the M3 null result on B_D(C), per operator GREENLIGHT.
**Status:** CLOSED-AS-DOCUMENTED-GAP per Brief §M4(b). M4 milestone closes cleanly with this gap as the deliverable.
**Classification:** **FUNDAMENTAL** gap (no known structural result is strong enough), NOT contingent (not merely a machinery-availability problem).

---

## §1. Mission context

### §1.1 The M3 null result

`harness/sweep_output/m32b_empirical_sweep.jsonl` (canonical at `gold/M3` = commit `9c2702d`) records **65 / 65 cascade_stable_null** verdicts on the basis

```
B_D(C) = {1, K_0, K_0², …, K_0^D, log K_0} ∪ {K_0·c : c ∈ C}
       at D = 6, C = {π, e, ln 2, γ, ζ(2), ζ(3), G}, n = 15
```

with three Excluded Families filtered per `_m2.3_calibration_anchor.md` §7.3:

- **EF1** — BBC-grandfathered pure-power subset {1, K_0, …, K_0^D}
- **EF2** — signature-paper-grandfathered S_n family (operator's prior published handoff)
- **EF3** — GKW-method-ceded (theoretical-citation permitted; method-import prohibited per `seeds/26 DO-NOT-REENTER`)

Per H9, the result is reported as a **two-tier** null:

- Empirical tier (`verification_class = field_standard_practice`): H_empirical_operational = 10⁷⁰ (BBC c-parity)
- Rigorous tier (`verification_class = proven_corollary`): H_rigorous = 1.0361 × 10⁷² via FBA Theorem 1 + Corollary 2 (`harness/rigorous_bound.py`)

The primary cascade reproduces bit-for-bit between M3.2a (`d55ffbc`) and M3.2b (`f621641`): identical K=29363 iterations, identical 71-digit final_norm, identical H_rigorous at 4× precision range.

### §1.2 The M4 question

Per Brief §M4: attempt symbolic closure in SymPy or Sage of the form
*"There exists a closed-form symbolic certificate that explains why B_D(C) admits no integer relation at H ≤ H_target."*
Two acceptable outcomes per Brief §M4: (a) closure, or (b) documented capability gap.

### §1.3 Operator's M4 forecast (verbatim spirit, 2026-05-16 ~14:32 JST)

> M4 will most likely produce a documented capability gap rather than a closure. The reason: K_0's transcendence status is itself the major open question in this corner of the literature, and any symbolic certificate strong enough to rule out integer relations in B_D(C) would imply progress on that major open question. If such a certificate were available, it would already be published. The honest M4 outcome is "structural closure is not available with current literature + available machinery; null result stands on numerical+rigorous-bound evidence alone."

This document records the survey + probe that confirms the operator's forecast empirically.

---

## §2. Candidate structural arguments surveyed

Each candidate is evaluated for whether it can yield a non-existence theorem for integer relations in B_D(C) at H ≤ H_rigorous. Of the seven candidates below, **all seven fail**, and the failure modes fall into two categories:
- **(i)** the structural result is too weak to constrain integer-relation existence (its hypotheses do not match K_0's known properties);
- **(ii)** the structural result requires machinery not available in operator's deployed stack AND not in any closed-form published result we know of.

Both failure modes ultimately reduce to the same root: **K_0's transcendence/algebraic-independence status is unknown.**

### §2.A — Lindemann–Weierstrass + algebraicity of constants

Lindemann–Weierstrass: for α₁, …, α_n distinct algebraic, e^{α_1}, …, e^{α_n} are linearly independent over the algebraic numbers.

- **Failure:** K_0 is NOT known to be of the form e^α for any algebraic α. K_0's definition is an infinite product involving zeta values; no e^{algebraic} representation is published.
- **What would be required:** A theorem of the form "K_0 = exp(z) for some z in a known algebraic-independence class."
- **Status of required result in literature:** Does not exist. K_0's irrationality is itself open (lit-007, lit-008).

### §2.B — Schanuel's conjecture

Schanuel: if z₁, …, z_n ∈ ℂ are linearly independent over ℚ, then trdeg_ℚ ℚ(z₁, …, z_n, e^{z_1}, …, e^{z_n}) ≥ n.

- **Failure:** (a) Schanuel is **unproven** (one of the major open conjectures in transcendence theory); (b) even conditional on Schanuel, K_0 would have to be placed among the e^{z_i} on the right side, which requires the additional unknown claim K_0 = exp(z) for a specific ℚ-linear combination z.
- **What would be required:** A proof of Schanuel + an explicit exponential representation of K_0.
- **Status of required result:** Schanuel-conditional-on-Schanuel is not a closure; both components are missing.

### §2.C — Nesterenko 1996 (algebraic independence of π, e^π, Γ(1/4))

Nesterenko proved {π, e^π, Γ(1/4)} are algebraically independent over ℚ via modular-form periods (j-function around CM points).

- **Failure:** K_0 is NOT among Nesterenko's covered constants. Nesterenko's method depends on modular-form periods at CM points; K_0 has no known relation to such periods.
- **What would be required:** Either an extension of Nesterenko's method to constants of Khinchin-type, or a theorem placing K_0 in the algebraic-independence class of {π, e^π, Γ(1/4)}.
- **Status of required result:** No such extension or theorem is published.

### §2.D — K_0 series representation + Mahler measures

K_0 = ∏_{k=1}^∞ (1 + 1/(k(k+2)))^{log₂ k} can be re-expressed via Mahler-measure-type integrals.

- **Failure:** Mahler measures yield arithmetic information about **algebraic numbers** (their conjugates' product on the unit disk). K_0 is not known to be algebraic; the Mahler-measure machinery does not apply to constants of unknown algebraic status.
- **What would be required:** A theorem of the form "K_0 = M(P) for some explicit polynomial P with known Mahler measure structure."
- **Status of required result:** No such representation is known.

### §2.E — Galois theory on algebraic relations among B_D(C)

If K_0 were algebraic of some degree d, Galois theory could in principle constrain which integer combinations of its powers and products with C-set elements can vanish.

- **Failure:** The hypothesis (K_0 algebraic) is itself the major open question. K_0's algebraic-status is unknown; lower bounds (irrationality measure, degree-lower-bound) are not published.
- **What would be required:** A proof that K_0 is algebraic of bounded degree (or transcendental), with explicit bounds.
- **Status of required result:** Not known.

### §2.F — CF-theoretic structural arguments

Continued-fraction-side arguments (e.g., partial-quotient distribution, GKW operator spectral analysis, dynamical-system arguments on the Gauss map) have produced rigorous results about K_0's continued-fraction expansion.

- **Failure:** Blocked by `seeds/26 DO-NOT-REENTER` (binding clause). The GKW spectral family overlaps content-axis with the operator's active "Finite-Depth Transient Rigidity" manuscript; method-import would muddy attribution. **Theoretical-citation permitted (lit-011 through lit-014 in repo); method-import prohibited.**
- **What would be required:** Either (a) operator authorization to lift the DO-NOT-REENTER binding, or (b) a non-GKW CF-theoretic argument that does not overlap with the parked seeds/26 reframings.
- **Status of required result:** No non-GKW CF-theoretic argument strong enough to constrain integer-relation existence in B_D(C) is published. Even if available, it would be off-limits to this mission per operator binding.

### §2.G — Mahler measure / height theory on hybrid basis

Height-theoretic arguments on algebraic numbers (Northcott, Bombieri, Vaaler) could in principle constrain integer combinations with bounded height.

- **Failure:** Same root cause as §2.E — height theory's hypotheses are *algebraic-number* properties. K_0's algebraic status is unknown; the basis B_D(C) contains 14 elements involving K_0 and one element involving log K_0. Without K_0's algebraic status known, height theory cannot apply.
- **What would be required:** K_0 algebraic + explicit minimal polynomial (or strong lower bound on degree).
- **Status of required result:** Not known.

### §2 summary

| Candidate | Failure category | Required machinery | Status |
|---|---|---|---|
| 2.A LW + algebraicity | (i) hypothesis not satisfied | K_0 = e^α for algebraic α | Unknown |
| 2.B Schanuel | (i)+(ii) hypothesis unsatisfied; conjecture unproven | Schanuel proof + K_0 = exp(z) | Both missing |
| 2.C Nesterenko | (i) hypothesis not satisfied | Extension to Khinchin-class | Not published |
| 2.D Mahler measure | (i) hypothesis not satisfied | K_0 ∈ image of Mahler map | Not published |
| 2.E Galois | (i) hypothesis not satisfied | K_0 algebraic + minimal poly | Unknown |
| 2.F CF-theoretic | (ii) machinery off-limits | DO-NOT-REENTER seeds/26 OR non-GKW result | Off-limits + non-GKW not published |
| 2.G Height theory | (i) hypothesis not satisfied | K_0 algebraic + minimal poly | Unknown |

**Every failure traces back to the same root: K_0's arithmetic nature is the open question, not a lever.**

---

## §3. SymPy 1.14.0 H10 retroactive dry-run (4-path probe)

Per H10, before declaring closure-or-gap on M4, the SymPy code paths that would symbolically derive a certificate must be exercised at canonical scale. The probe is at `capability/_m4_symbolic_probe.py`; output JSONL at `capability/_m4_symbolic_probe.jsonl`; console transcript at `capability/_m4_symbolic_probe_console.log`. Probe executed 2026-05-16 ~14:35 JST.

| Path | Probe target | Result | closure_achieved |
|---|---|---|---|
| 1 | `is_transcendental` / `is_irrational` on K_0 (Symbol + Float) | `None` for K_0 in both symbolic and Float forms (vs `True` for `pi`, `E`). SymPy has no built-in arithmetic-nature data for K_0. | **False** |
| 2 | `nsimplify` with named-constants basis at tolerances 10⁻⁵ … 10⁻⁵⁰ | Loose tolerance (10⁻⁵, 10⁻¹⁰) returns numerical coincidences (rational + sqrt; rational expression in named constants); strict tolerance (10⁻²⁰, 10⁻³⁰) returns the numerical value back unchanged. Method is weaker than PSLQ (no LLL reduction). Reduces to the same numerical question M3 already answered. | **False** |
| 3 | Groebner basis on B_D(C) with K_0 symbolic | All 15 monomials distinct under treating K_0 as a free indeterminate; only the trivial all-zero integer combination vanishes identically as a polynomial. Polynomial-identity verdict does NOT lift to numerical-vanishing without an algebraic-independence theorem. | **False** |
| 4 | LW / Gelfond-Schneider / Nesterenko / Schanuel applicability (encoded as documentation strings) | All four transcendence theorems have hypothesis patterns that K_0 is not known to satisfy. Documented per §2.A–§2.C. | **False** |

**Probe outcome record (JSONL summary line):**
```
{"probe_outcome": true, "paths_probed": 4, "closures_achieved": 0,
 "any_anomaly_surfaced": false, "verdict": "documented_capability_gap"}
```

**H10 condition satisfied:** the SymPy code paths that would produce closure WERE exercised at canonical scale; none returned a closure. This is the dry-run-equivalent that H10 mandates before declaring the M4 outcome.

**No anomaly surfaced.** Per operator M4 GREENLIGHT halt criterion ("if a structural result that does admit symbolic closure and produces a certificate emerges, that's a finding that warrants careful operator review"): no halt invoked.

---

## §4. Fundamental-vs-contingent classification

Per operator M4 GREENLIGHT verbatim: *"whether the gap is fundamental (no known result is strong enough) or contingent (a known result exists but requires unavailable machinery)."*

**This gap is FUNDAMENTAL.** Justification:

1. **§2.A, §2.C, §2.D, §2.E, §2.G:** failure mode is (i) — hypothesis pattern of the candidate theorem does not match K_0's known properties. The candidate's machinery is in principle available (LW is elementary, Nesterenko is published, Mahler-measure tooling exists in pari/sage), but the THEOREM does not apply because K_0 is not known to satisfy the precondition.
2. **§2.B:** failure mode is (i)+(ii) — Schanuel is unproven AND K_0's exponential representation is unknown. Even granted Schanuel as a contingent input, the closure would still require a separate K_0-specific result.
3. **§2.F:** failure mode is (ii) — CF-theoretic machinery is off-limits per `seeds/26 DO-NOT-REENTER`. But even if the binding were lifted, no published non-GKW result is strong enough to constrain integer-relation existence in B_D(C).

**The single root cause is K_0's unknown arithmetic nature.** This is not a machinery-deployment problem (no install or version upgrade would change the outcome). A closure would require **new mathematics** of the form "K_0 is [transcendental / algebraic of degree ≥ d / member of class X]." Any such new result strong enough to imply the M3 null would be a major contribution to transcendence theory in its own right — i.e., the major open question would be solved as a side effect.

**Closure-availability sensitivity analysis:**

| Variable | Variation | Effect on closure availability |
|---|---|---|
| SymPy version | upgrade 1.14.0 → ≥ 2.x | No effect (gap is at theorem-level, not implementation-level). |
| Add `python-flint` / `sage` install | yes | No effect (Sage's `is_transcendental` on Khinchin's constant returns `None` for the same reason). |
| Hardware (CPU, RAM) | upgrade | No effect (probe is non-computational at scale; result is theorem-level). |
| `seeds/26` binding lifted | hypothetical | No effect on closure (no non-GKW CF-theoretic result strong enough is published; lifting the binding would only re-expose the parked R-1/R-2 reframings, which themselves do not constitute closure). |
| New theorem in literature | hypothetical | Yes (would convert FUNDAMENTAL → contingent if a partial result lands). Probability over the M6 manuscript timeline: low but non-zero. Currently: no such result. |

The classification is **stable under all variations available to operator's stack within mission scope.**

---

## §5. Forward-flag for M6 §Discussion

**For inclusion in `m6_preflight_checklist.md` §4** (added in same commit batch as this gap document):

> The M6 §Discussion (or §Limitations) must state, in operator-verbatim form per M4 GREENLIGHT: *"Structural closure of the null result was attempted via [survey]; no available structural argument is strong enough to constrain integer-relation existence at the tested bound; the null stands on numerical and rigorous-bound evidence per the two-tier predicate."*

Recommended elaboration (3-4 sentences):

> Symbolic closure of the M3 null result was attempted in M4 via survey of seven candidate structural arguments (Lindemann–Weierstrass, Schanuel, Nesterenko, Mahler-measure, Galois, non-GKW CF-theoretic, and height-theory) and a four-path SymPy probe (`is_transcendental`/`is_irrational`, `nsimplify`, Groebner-on-symbolic-basis, transcendence-theorem applicability check). Every candidate failed at the same root: K_0's transcendence status is itself the major open question in this corner of the literature, and any structural certificate strong enough to rule out integer relations in B_D(C) at H ≤ 1.036 × 10⁷² would imply progress on that question. We classify this gap as fundamental (no known structural result is strong enough; not merely a machinery-availability problem) per the M4 brief, and the null result stands on numerical and rigorous-bound evidence per the two-tier predicate (H_empirical_operational = 10⁷⁰ `field_standard_practice`; H_rigorous = 1.036 × 10⁷² `proven_corollary`).

**Owner:** M6 manuscript files (when authored). Cross-reference back to this gap document.

---

## §6. AEAL discipline notes

### §6.1 Mutation budget

**Mutation budget at M2 milestone-block: 0/1 still consumed (unchanged).**

This M4 gap document is a **field-map update** (per U-MISSION-L precedent: "the hypothesis is unchanged; the confidence reporting structure is being extended"). The hypothesis (test for integer relations in B_D(C)) is unchanged. The bounded sub-question (does K_0 admit a PSLQ-detectable algebraic relation in B_D(C) at H ≤ H_target?) is unchanged. M4 is the **scheduled** Brief §M4 attempt at structural closure; producing a documented gap is the Brief §M4(b)-acceptable outcome, not a hypothesis change. The 10th mutation_log entry (`mutation_log/m4_symbolic_closure_gap_20260516.md`) records this classification.

### §6.2 Halt-and-flag pattern

**No halt invoked during M4.** Per operator M4 GREENLIGHT:
- *"If [the SymPy probe surfaces an anomaly e.g.] a structural result that does admit symbolic closure and produces a certificate"* → none surfaced. No halt.
- *"A documented capability gap at M4 is not a failure. Per Brief §M4(b), it's an acceptable outcome and a publishable observation in M6 §Discussion."*

Mission-life halt count remains **6** (M1 ×4 + M2.1 ×1 + M2.3 Catch #2 ×1 + M3.2b first-attempt Catch #3 ×1; the M3.2b crash counted into both halt count and Catch counts).

Updated AEAL maturation curve:

| Milestone | Halts |
|---|---|
| M1 | 4 |
| M2.1 | 1 |
| M2.2 | 0 |
| M2.3 | 1 (Catch #2 resolved) |
| M3.1 impl | 0 |
| M3.2a exec | 0 |
| M3.2b first attempt | 1 (Catch #3 / U-MISSION-N) |
| U-MISSION-N resolution + M3.2b re-run | 0 |
| **M4 (this segment)** | **0** |

Operator's forecast continues to validate: M4 closes cleanly as a documented gap; the back-half-running-cleaner pattern preserved.

### §6.3 H10 compliance

H10 mandate satisfied via `capability/_m4_symbolic_probe.py` execution. Required-form criteria per H10:
- Code path exists (SymPy 1.14.0 H7-verified per `capability/sympy.available.md`) ✓
- Exercised at canonical scale (K_0 first 100 digits via mpmath; all four paths return verdicts) ✓
- Result JSONL with structured records ✓
- Reproducible (`python capability/_m4_symbolic_probe.py` re-runs the probe) ✓
- Cited in this gap document ✓

### §6.4 H8 applicability to closure-bearing citations

Per operator M4 GREENLIGHT: *"if M4 cites a published structural result as the basis for symbolic closure, paper-read verification under H8 is required."*

**M4 does NOT cite any structural result as the basis for closure** (because no closure is achieved). The seven candidates in §2 are cited **negatively** (as failure modes). Per H8 narrowing precedent (canonical-textbook theorems do not require paper-read when cited as obstacles, analogous to OEIS canonical-source narrowing):
- **§2.A** LW classical — canonical textbook material; paper-read not required when cited as inapplicable. ✓
- **§2.B** Schanuel — cited as unproven conjecture (textbook-level statement); paper-read not required. ✓
- **§2.C** Nesterenko 1996 — cited as "does not cover K_0"; not closure-bearing. Paper-read deferred to M6 if cited there. ✓
- **§2.D–§2.G** — all cited as failure modes, not as bases for closure. Paper-read not required at M4. ✓

No H8 fire is triggered by this gap document.

### §6.5 Rule 6 audit

- Zero portal interactions during M4.
- Two planned `git push` operations:
  - **Commit A:** `capability/_m4_symbolic_probe.py` + `capability/_m4_symbolic_probe.jsonl` + `capability/_m4_symbolic_probe_console.log` (H10 evidence trail).
  - **Commit B:** `capability/symbolic_closure.gap.md` (this file) + `mutation_log/m4_symbolic_closure_gap_20260516.md` (10th mutation_log entry) + `m6_preflight_checklist.md` §4 (M4 framing).
- No `selected.md` edits (frozen at gold/M1).
- No `_m2.3_calibration_anchor.md` §7 edits (frozen at gold/M2).
- No `methodology/heuristics.md` edits (no new heuristic).
- No `claims.jsonl` edits (no new literature claim; the closure-attempt failure is structural, not new literature).
- No canonical M3 JSONL edits (frozen at `gold/M3`).
- Tag `gold/M3` already in place at `9c2702d` (pre-M4 ratification done at M4 GREENLIGHT acknowledgement).

---

## §7. Closure statement

**M4 CLOSES** with this document as the deliverable. Per Brief §M4(b): *"capability/symbolic_closure.gap.md stating precisely which step requires machinery beyond current capability. STOP. Do not paper over with more numerics."*

- **Which step requires machinery beyond current capability:** the structural-certificate step. Producing a symbolic certificate for B_D(C) non-existence of integer relations at H ≤ H_rigorous requires **knowing K_0's arithmetic nature** (transcendence + algebraic-independence membership), which is the major open question.
- **STOP:** no further numerics will be appended to M3. The M3 result stands on numerical and rigorous-bound evidence per the two-tier predicate.
- **No paper-over:** this gap is recorded honestly per operator forecast (M4 GREENLIGHT) and per Brief §M4(b) acceptance.

**Mission state post-M4:**
- M1 + M2 + M3 + M4 all CLOSED.
- gold/M3 tag in place at `9c2702d`; no new gold tag at M4 (Brief specifies gold freezes G1–G6 mapping to M1–M6; G4 = M4 freeze; this document is the M4 deliverable, and tag `gold/M4` should fire at the closing commit batch per operator discretion).
- M5 (Lean formalization scope) READY pending operator greenlight.
- M6 (manuscript drafting) preflight checklist updated with §4 (this gap's framing for §Discussion).

**Provenance footer:**
- Created: 2026-05-16 ~14:32 JST during M4 phase, post gold/M3.
- Authority: operator M4 GREENLIGHT 2026-05-16 ~14:32 JST.
- Predicate anchor: `literature/_m2.3_calibration_anchor.md` §7 (M2.3 ratified at gold/M2, commit `ca9c989`).
- M3 result anchor: `harness/sweep_output/m32b_empirical_sweep.jsonl` at gold/M3 (commit `9c2702d`).
- Heuristic anchors: H7 (capability functional verification) + H8 (paper-read for closure-bearing citations, not triggered here) + H10 (full-regime dry-run mandate, satisfied via `_m4_symbolic_probe.py`).
- Brief §M4(b) compliance: this document satisfies the §M4(b) format requirement.
