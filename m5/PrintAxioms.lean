-- m5/PrintAxioms.lean
-- One-off audit-trail script: prints the axiom set behind each M5 theorem.
-- Run via: lake env lean PrintAxioms.lean > _print_axioms_output.txt 2>&1
--
-- Per Result.lean §`#print axioms self-check`, the expected output for
-- `m3_null_at_rigorous_bound` is exactly:
--   M5.pslq_cascade_implies_no_integer_relation
-- plus Lean core axioms (`Classical.choice`, `propext`, `Quot.sound`).
--
-- Any additional axiom in any of the four prints below indicates an
-- unexpected leak; reproducibility check fails and should be diagnosed
-- before M6 manuscript submission.

import M5

open M5

#print axioms m3_null_at_rigorous_bound
#print axioms m3_null_at_empirical_bound
#print axioms m3_two_tier_predicate_holds
#print axioms m3_null_depends_on_M4_gap
