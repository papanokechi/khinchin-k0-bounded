-- m5/M5.lean — root module
-- Aggregator: imports the three M5 target modules.
-- M5 is the operator-greenlit Lean formalization deliverable for Brief §M5,
-- under the recalibrated three-target scope (Definitions / Result / Axioms).
--
-- Authority: operator M5 GREENLIGHT 2026-05-16 ~14:52 JST.
-- Mathlib pin: leanprover-community/mathlib4 @ v4.14.0 (operator's cached pin).
-- Lean toolchain: leanprover/lean4:v4.14.0.

import M5.Definitions
import M5.Result
import M5.Axioms

namespace M5

/-! ## M5 module overview

The M5 formalization is a thin Lean 4 skeleton that:
1. Defines the EF1-complement basis `B_D(C)` (n = 15 elements at D = 6, |C| = 7)
   and the predicate `HasIntegerRelation basis H` ≔ "an integer combination of
   `basis` with max-coefficient ≤ `H` vanishes."
2. States the main M3 null theorem `m3_null_at_rigorous_bound` (the rigorous-tier
   claim from `harness/sweep_output/m32{a,b}_*.jsonl` at `gold/M3`).
3. Discharges the theorem via axioms (M5.Axioms) that black-box the
   PSLQ + FBA Theorem 1 + Corollary 2 numerical evidence. The axioms encode
   what was numerically verified at M3 (cascade-stable null at H_rigorous =
   1.036 × 10⁷²) and what is structurally unavailable at M4 (the FUNDAMENTAL
   capability gap on K₀'s arithmetic nature).

This file's role is purely to import the three targets. All declarative content
lives in the three sub-files.
-/

end M5
