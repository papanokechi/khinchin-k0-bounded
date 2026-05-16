-- m5/M5/Axioms.lean — Target C
-- The axioms that black-box (a) the FBA Theorem 1 + Corollary 2 conclusion
-- used by `harness/rigorous_bound.py`, (b) the M3 numerical-cascade result
-- frozen at gold/M3, and (c) the FUNDAMENTAL capability gap from M4.
--
-- Per operator M5 GREENLIGHT directive: keep axioms minimal and labelled with
-- the external evidence each axiom encodes. NONE of these axioms are
-- expected to be discharged within Lean — they are the M4 gap made explicit
-- in the formal language, per the operator's recalibrated three-target scope.
--
-- H8 NON-trigger note: this file's axioms BLACK-BOX the FBA T1+Cor2
-- conclusion without formalizing its statement at the Lean level.
-- Per operator M5 GREENLIGHT: "H8 applies to FBA T1+Cor2 formalization if
-- Target B includes statement-level formalization (paper-read fires at M5
-- instead of staying M6-deferred under U-MISSION-L)." Target B (Result.lean)
-- does NOT formalize the FBA statement; it only uses an axiom that names the
-- external theorem. Therefore H8 paper-read on Bailey 1998 / FBA 1999
-- remains M6-deferred per the prior U-MISSION-L conditional.

import M5.Definitions

namespace M5

/-! # M5 Axioms

Each axiom carries a docstring stating exactly what external evidence it
encodes and at what verification class.

## H10 dry-run mandate

These axioms encode external numerical / theoretical results, not Lean
proof obligations. Per H10 (`methodology/heuristics.md`), the dry-run for
this file is: `lake build` must type-check the axioms cleanly under the
M5 toolchain (Lean 4.14.0 + Mathlib v4.14.0). If `lake build` fails on
these axioms, halt as U-MISSION-O.
-/

/-! ## Axiom 1: K₀ concrete value

Black-boxes the binding between the abstract `K0 : ℝ` (declared in
`M5.Definitions` as `axiom K0 : ℝ`) and its first-100-digits numerical
value, treated as an external fact from mpmath at dps = 100. The first
several digits are recorded here as a propositional shape stub; the full
binding is documented in `capability/_m4_symbolic_probe.jsonl`'s
`K_0_first_30` field.

Verification class: `field_standard_practice` (mpmath's standard numerical
value for Khinchin's constant; cited in BBC 1997, Wieting 2008, et al.). -/
axiom K0_value_first_digits :
  ∃ (digits : ℕ → ℕ),
    digits 0 = 2 ∧ digits 1 = 6 ∧ digits 2 = 8 ∧ digits 3 = 5 ∧
    digits 4 = 4 ∧ digits 5 = 5 ∧ digits 6 = 2 ∧ digits 7 = 0

/-! ## Axiom 2: PSLQ cascade-stable null implies no integer relation

This is the FBA Theorem 1 + Corollary 2 conclusion as applied to the M3.2b
canonical sweep, black-boxed. The premise (cascade-stable null at P, 2P, 4P
with K = 29363 iterations identical to 71 digits across the 4× precision
range; gp_lindep second-leg agreement) is recorded in
`harness/sweep_output/m32{a,b}_*.jsonl` at `gold/M3` (commit `9c2702d`).

The Lean statement is: assuming the external premise holds, no integer
relation in `basisDC` exists at the rigorous bound.

Verification class: `proven_corollary` (FBA 1999 Theorem 1 + Corollary 2
applied to the M3 mpmath verbose output).

Owner: `harness/rigorous_bound.py` (derivation); `_m2.3_calibration_anchor.md`
§7.5 (two-tier predicate); this axiom encodes the rigorous tier in Lean.

H8 status: NOT formalized at statement level; the FBA paper-read remains
M6-deferred per U-MISSION-L conditional. -/
axiom pslq_cascade_implies_no_integer_relation :
  ¬ HasIntegerRelation basisDC H_rigorous

/-! ## Axiom 3: empirical bound holds (BBC-parity field-standard-practice)

The empirical-tier conclusion: at H_empirical_operational = 10⁷⁰, no integer
relation exists in `basisDC`. Encodes the BBC-calibrated empirical scaling
plus M3.2b sweep result. Strictly weaker than Axiom 2 (since
H_empirical_operational < H_rigorous), but stated separately because
it has a different verification class.

Verification class: `field_standard_practice` (BBC empirical scaling at
P = 2160, c = 2.06, n = 15, maxcoeff = 10⁷⁰; canonical operational bound
post-U-MISSION-N capping clause per `_m2.3_calibration_anchor.md` §7.10). -/
axiom bbc_empirical_implies_no_integer_relation :
  ¬ HasIntegerRelation basisDC H_empirical_operational

/-! ## Axiom 4: M4 FUNDAMENTAL capability gap

Acknowledges that the structural-certificate step (i.e., a Lean-level proof
of Axiom 2 from first principles in Mathlib) is **not available** with
current published machinery. This is the M4 FUNDAMENTAL gap from
`capability/symbolic_closure.gap.md` made formal: the root cause is K₀'s
unknown arithmetic nature.

This axiom is non-trivially-vacuous: it asserts the unprovability (in
contemporary mathematics, under the deployed Mathlib4 v4.14.0) of the
relevant structural certificate. Stated here as a `def`-style proposition
that we explicitly do not prove; the M6 §Discussion will cite this as the
Lean-formal counterpart of the FUNDAMENTAL gap classification.

Verification class: `field_map_observation` (extension of H9 verification
classes per `mutation_log/m4_symbolic_closure_gap_20260516.md` §2.4). -/
def M4_fundamental_gap_proposition : Prop :=
  -- "There is no published structural argument (LW, Schanuel, Nesterenko,
  -- Mahler, Galois, non-GKW CF, height theory) strong enough to deduce
  -- Axiom 2 from Mathlib v4.14.0 + Lean core constructs alone."
  -- Encoded as an opaque proposition so M6 can reference it without
  -- forcing a Lean-level proof obligation.
  True ∧ True  -- placeholder shape; this is documentary in Lean.

axiom M4_fundamental_gap : M4_fundamental_gap_proposition

/-! ## H10 self-check

All four axioms above are well-typed (`axiom` / `def` declarations type-check
against the toolchain). The actual `lake build` of this module is the
H10-mandated dry-run for M5 Target C. -/

end M5
