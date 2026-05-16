-- m5/lakefile.lean
-- M5 (unsolved-relay-staging): Lean 4 formalization skeleton for M3 null result.
-- Three-target scope per operator M5 GREENLIGHT 2026-05-16 ~14:52 JST:
--   M5.Definitions  (basis B_D(C) + HasIntegerRelation predicate + K_0 abstract)
--   M5.Result       (main M3 null theorem, conditional on M5.Axioms)
--   M5.Axioms       (FBA T1+Cor2 black-box axiom + structural-gap axioms)
-- Mathlib pin matches operator's siarc-lean4 cached state (v4.14.0) so Lake
-- resolves against `.lake/packages` (junction to claude-chat/lean4/.lake/packages)
-- without network fetch.

import Lake
open Lake DSL

package «m5» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4" @ "v4.14.0"

@[default_target]
lean_lib «M5» where
  roots := #[`M5]
