-- m5/M5/Result.lean — Target B
-- The main M5 theorem: the M3 null at H_rigorous, conditional on the
-- M5.Axioms axioms (which black-box the FBA + PSLQ numerical evidence and
-- the M4 FUNDAMENTAL capability gap).
--
-- Per operator M5 GREENLIGHT recalibrated scope: this file states the
-- main theorem at the rigorous tier and a corollary at the empirical
-- tier, plus the M4-gap-disclaimer remark. Total target: ~70-90 lines.
--
-- H8 NON-trigger: the theorem statement here does NOT formalize FBA T1+Cor2;
-- it merely uses `pslq_cascade_implies_no_integer_relation` (an axiom)
-- as a black-box. Per operator M5 GREENLIGHT, H8 paper-read remains
-- M6-deferred under U-MISSION-L.

import M5.Definitions
import M5.Axioms

namespace M5

/-! # M5 Result

The mission-level theorem: the EF1-complement basis B_D(C) at D = 6, |C| = 7
(n = 15) admits no integer relation at H ≤ H_rigorous = 1.036 × 10⁷². The
proof reduces to the rigorous-tier axiom in `M5.Axioms`.

This is the Lean-formal counterpart of the JSONL verdict at
`harness/sweep_output/m32{a,b}_*.jsonl` at `gold/M3` (commit `9c2702d`).
-/

/-! ## Main theorem (rigorous tier, `proven_corollary` class)

The 65-cascade-stable-null result at P/2P/4P with FBA-derived rigorous bound
H_rigorous = 1.036 × 10⁷². No integer relation exists in `basisDC` at
heights up to this bound. -/
theorem m3_null_at_rigorous_bound :
    ¬ HasIntegerRelation basisDC H_rigorous := by
  exact pslq_cascade_implies_no_integer_relation

/-! ## Corollary (empirical tier, `field_standard_practice` class)

At the strictly-weaker BBC-empirical operational bound H_empirical_operational
= 10⁷⁰, the same non-existence holds. This corollary follows from Axiom 3
directly (and would also follow from the rigorous tier by monotonicity if we
had a height-monotonicity lemma, which the present skeleton does not assert).
-/
theorem m3_null_at_empirical_bound :
    ¬ HasIntegerRelation basisDC H_empirical_operational := by
  exact bbc_empirical_implies_no_integer_relation

/-! ## Two-tier predicate as a single bundled proposition

The two-tier predicate from `_m2.3_calibration_anchor.md` §7.5: M3 ratifies
BOTH the empirical and rigorous claims simultaneously. We bundle them as
a single `Prop` for downstream M6 citation. -/
def m3_two_tier_predicate : Prop :=
  (¬ HasIntegerRelation basisDC H_empirical_operational) ∧
  (¬ HasIntegerRelation basisDC H_rigorous)

theorem m3_two_tier_predicate_holds : m3_two_tier_predicate := by
  refine ⟨?_, ?_⟩
  · exact m3_null_at_empirical_bound
  · exact m3_null_at_rigorous_bound

/-! ## M4-gap acknowledgement remark

Lean does NOT prove `pslq_cascade_implies_no_integer_relation` from
Mathlib4 + first principles. It is an axiom. The reason is the M4
FUNDAMENTAL capability gap from `capability/symbolic_closure.gap.md`:
no published structural argument is strong enough to discharge this axiom
within the deployed stack. This remark is the formal counterpart to the
M6 §Discussion paragraph at `m6_preflight_checklist.md` §4 + §4.1.
-/
theorem m3_null_depends_on_M4_gap : M4_fundamental_gap_proposition :=
  M4_fundamental_gap

/-! ## #print axioms self-check

Downstream M6 reproducibility check: the canonical axiom set used by
`m3_null_at_rigorous_bound` is exactly the four axioms in `M5.Axioms`
(plus Lean core: `Classical.choice`, propositional extensionality, and
quotient axioms inherited from Mathlib4's foundational layer).

To run the check externally:
```
#print axioms m3_null_at_rigorous_bound
```
should report only `M5.pslq_cascade_implies_no_integer_relation` plus
Lean core axioms. Any additional axiom in the report indicates a leak
that should be diagnosed before M6 manuscript submission. -/

end M5
