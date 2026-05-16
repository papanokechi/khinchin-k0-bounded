-- m5/M5/Definitions.lean — Target A
-- Definitions for the M5 formalization: K₀ abstract, EF1-complement basis
-- B_D(C), and the HasIntegerRelation predicate.
--
-- Per operator M5 GREENLIGHT recalibrated three-target scope: this file is
-- pure declarative content (no theorems with proof obligations beyond the
-- definitional level). Total target: ~80-100 lines.

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace M5

/-! # M5 Definitions

The EF1-complement basis B_D(C) tested by the M3.2b canonical sweep at
`gold/M3` (commit `9c2702d`).

## Basis structure (n = 15 elements, D = 6, |C| = 7)

* Pure-power tail (7 elements): `1, K₀, K₀², …, K₀⁶`
* Hybrid log: `log K₀`
* Bilinear (7 elements): `K₀ · c` for `c ∈ C = {π, e, ln 2, γ, ζ(2), ζ(3), G}`

The EF1 (pure-power-only at D ≤ 50) BBC-grandfathered subset and the EF2
(S_n signature-paper) family are filtered out at basis construction; EF3
(GKW-method-ceded) is structurally absent from B_D(C) per the
`seeds/26 DO-NOT-REENTER` binding.

## Abstract constants

K₀, Catalan's G, ζ(3), γ, π, e, ln 2, ζ(2), and log K₀ are all declared
opaque reals via `axiom`. We deliberately avoid importing
`Mathlib.Data.Real.Pi.Bounds` / `Mathlib.Analysis.SpecialFunctions.{Log,Exp}`
to keep the M5 skeleton's Mathlib surface minimal and the dry-run build
self-contained on the M5-staging cache snapshot. The numerical values
of these constants are bound externally by mpmath / PARI at canonical
precision (see `harness/sweep_output/m32b_empirical_sweep.jsonl` for the
M3 evidence frozen at `gold/M3`).
-/

/-- Khinchin's constant K₀ ≈ 2.6854520010… treated abstractly as a real.
Its arithmetic nature (irrationality, transcendence) is unknown per the
M4 FUNDAMENTAL capability gap in `capability/symbolic_closure.gap.md`. -/
axiom K0 : ℝ

/-- Catalan's constant G ≈ 0.9159655941…. Mathlib v4.14.0 does not provide
`Real.catalan` as a named constant; declared abstractly here. -/
axiom catalanConst : ℝ

/-- ζ(3) — Apéry's constant ≈ 1.2020569…. Mathlib v4.14.0 lacks a closed
form named constant; declared abstractly. -/
axiom zeta3 : ℝ

/-- Euler–Mascheroni constant γ ≈ 0.5772156…. Declared abstractly. -/
axiom eulerMascheroni : ℝ

/-- π ≈ 3.14159…; declared opaque to avoid the `Real.pi` import chain. -/
axiom realPi : ℝ

/-- e ≈ 2.71828…; declared opaque to avoid the `Real.exp` import chain. -/
axiom realE : ℝ

/-- ln 2 ≈ 0.69314…; declared opaque to avoid the `Real.log` import chain. -/
axiom realLn2 : ℝ

/-- ζ(2) = π² / 6 ≈ 1.64493…; declared opaque (downstream of `realPi`). -/
axiom zeta2 : ℝ

/-- log K₀ ≈ 0.98787…; declared opaque (separately from `Real.log`). -/
axiom logK0 : ℝ

/-! ## The constant set C and the basis B_D(C) -/

noncomputable section

/-- Constant set C = {π, e, ln 2, γ, ζ(2), ζ(3), G} (|C| = 7).
Per `_m2.3_calibration_anchor.md` §7 frozen at gold/M2 = `ca9c989`. -/
def constantSet : List ℝ :=
  [realPi, realE, realLn2, eulerMascheroni, zeta2, zeta3, catalanConst]

/-- The pure-power tail `[1, K₀, K₀², …, K₀^D]` at `D = 6` (7 elements). -/
def purePowerTail (D : ℕ) : List ℝ :=
  (List.range (D + 1)).map (fun k => K0 ^ k)

/-- The bilinear leaf `[K₀ · c : c ∈ C]` (7 elements). -/
def bilinearLeaf : List ℝ :=
  constantSet.map (fun c => K0 * c)

/-- The EF1-complement basis `B_D(C)` at `D = 6`, `|C| = 7`. Total 15 elements:
7 pure-power + 1 hybrid-log + 7 bilinear. -/
def basisDC : List ℝ :=
  purePowerTail 6 ++ [logK0] ++ bilinearLeaf

/-- Sanity: `basisDC.length = 15` is the M3 primary cascade dimension. -/
theorem basisDC_length : basisDC.length = 15 := by
  unfold basisDC purePowerTail bilinearLeaf constantSet
  simp [List.length_range, List.length_map, List.length_append]

/-! ## The integer-relation predicate

We say `basis` admits an integer relation at height `H` if there exist
integer coefficients `a : ℕ → ℤ`, not all zero, with `|a i| ≤ H` for all
`i < basis.length`, such that `∑ i < basis.length, (a i : ℝ) · basis[i] = 0`.
-/

/-- Helper: the integer-linear combination of `basis` with coefficients `a`. -/
def linearCombo (basis : List ℝ) (a : ℕ → ℤ) : ℝ :=
  (List.range basis.length).foldl
    (fun acc i => acc + (a i : ℝ) * (basis.get? i).getD 0) 0

/-- Predicate: `basis` admits an integer relation of height at most `H`. -/
def HasIntegerRelation (basis : List ℝ) (H : ℝ) : Prop :=
  ∃ (a : ℕ → ℤ),
    (∃ i, i < basis.length ∧ a i ≠ 0) ∧
    (∀ i, i < basis.length → (Int.natAbs (a i) : ℝ) ≤ H) ∧
    linearCombo basis a = 0

/-! ## Mission-canonical bounds

* `H_empirical_operational` = 10⁷⁰ (BBC c-parity at P = 2160, c = 2.06, n = 15;
  `field_standard_practice` verification class per H9).
* `H_rigorous`            = 1.036 × 10⁷² (FBA Theorem 1 + Corollary 2;
  `proven_corollary` verification class per H9).
-/

def H_empirical_operational : ℝ := (10 : ℝ) ^ (70 : ℕ)
def H_rigorous : ℝ := (1036 : ℝ) * (10 : ℝ) ^ (69 : ℕ)

end  -- noncomputable section

end M5

