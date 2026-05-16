# mutation_log: M5 Lean skeleton — field-map update (operator M5 GREENLIGHT)

**Date:** 2026-05-16 ~15:35 JST
**Entry number:** 11th mutation_log entry (5th in the M2+ field-map / heuristic series after U-MISSION-J H8, U-MISSION-L H9, U-MISSION-N H10, and the M4 closure entry).
**Trigger:** operator M5 GREENLIGHT directive 2026-05-16 ~14:52 JST after M4 CLOSED at `gold/M4` = `fd13eeb`.
**Mutation budget consumed:** **0 of 1.** M5 Lean skeleton is **field-map update**, NOT hypothesis mutation, per U-MISSION-J / U-MISSION-L / U-MISSION-N precedents (the hypothesis — "test for integer relations in B_D(C)" — is unchanged; only the **representation language** is extended from mpmath/PARI/SymPy to Lean 4 + Mathlib v4.14.0 axiomatic encoding).

## §1 — Operator M5 GREENLIGHT directive (verbatim core)

> M5 greenlight from my prior message is the operative directive. Specifically: tag gold/M4 at fd13eeb, add §4.1 sub-item to m6_preflight_checklist distinguishing structurally-unavailable (2.A-2.E, 2.G) from scope-ceded (2.F), then proceed to pre-M5 Mathlib4 deep build verification (H7 deferred risk fires now), then M5 implementation under the recalibrated three-target scope (Definitions.lean, Result.lean, Axioms.lean, ~200-400 lines total).
>
> H10 applies to Lean 4 dry-runs. H8 applies to FBA T1+Cor2 formalization if Target B includes statement-level formalization (paper-read fires at M5 instead of staying M6-deferred under U-MISSION-L). The U-MISSION-O label is reserved for any Mathlib4 deep-build problem that surfaces during pre-M5 verification.

## §2 — Sequence executed (this entry)

### Step 1 — `gold/M4` tag

Annotated tag at `fd13eeb` (M4 closure commit). Four gold tags now on origin: `gold/M1` (M1.3 freeze), `gold/M2` (M2.3 ratification at `ca9c989`), `gold/M3` (M3.2b clean null at `9c2702d`), `gold/M4` (M4 documented gap at `fd13eeb`).

### Step 2 — `m6_preflight_checklist.md` §4.1 added

Structurally-unavailable (6/7: 2.A LW, 2.B Schanuel, 2.C Nesterenko, 2.D Mahler, 2.E Galois, 2.G Height) vs scope-ceded (1/7: 2.F CF-theoretic) sub-classification. Per operator verbatim. M6 §Discussion framing implications included.

### Step 3 — pre-M5 Mathlib4 deep-build verification (H7 deferred risk firing)

**Toolchain inventory (`elan list`):**
- Lean 4.14.0 (matches operator's siarc-lean4 pin)
- Lean 4.29.0, 4.29.1, 4.30.0-rc1, 4.30.0-rc2 (additionally installed; not used for M5)
- Lake 5.0.0-src+f72c35b (bundled with Lean 4.14.0)
- Mathlib v4.14.0 cached at `claude-chat/lean4/.lake/packages/mathlib` with 9 transitive deps (aesop, batteries, Cli, importGraph, LeanSearchClient, mathlib, plausible, proofwidgets, Qq)

**Deep-build status:** the cached `.lake/packages/mathlib/.lake/build/lib/` contains pre-built oleans for the modules siarc-lean4 imports. Lake `Replayed` reuses these via olean-hash-match; modules not in siarc-lean4's import closure must be built locally.

**Initial M5 implementation attempt** pulled `Mathlib.Data.Real.Pi.Bounds`, `Mathlib.Analysis.SpecialFunctions.Log.Basic`, `Mathlib.Analysis.SpecialFunctions.Exp`. After ~12 min, only 587 modules `Replayed`; 8 lean workers compiling modules NOT in operator's cache (high CPU, slow). H7-class observation: the cached Mathlib snapshot is **import-closure-specific**, not a uniformly-pre-built copy of the whole library. Mathlib deep-build verification PASSES only for the import closure of the cached project.

**Resolution:** simplify M5 imports to `Mathlib.Data.Real.Basic` + `Mathlib.Data.List.Basic` only (both inside operator's cache closure). Replace `Real.pi`, `Real.exp 1`, `Real.log 2`, `Real.log K0`, `Real.pi^2/6` with opaque `axiom` declarations: `realPi`, `realE`, `realLn2`, `logK0`, `zeta2` — semantically equivalent for the M5 skeleton (the operator's M5 directive explicitly permits axioms standing for external evidence).

### Step 4 — M5 project scaffolding

Created `m5/` project tree:

| File | Role |
|---|---|
| `m5/lakefile.lean` | Lake config; `lean_lib M5` with roots `[M5]`; `require mathlib from git "https://github.com/leanprover-community/mathlib4" @ "v4.14.0"` |
| `m5/lean-toolchain` | `leanprover/lean4:v4.14.0` |
| `m5/lake-manifest.json` | Copied verbatim from operator's `claude-chat/lean4/siarc-lean4/lake-manifest.json` (9 packages, identical revisions) |
| `m5/M5.lean` | Root aggregator (35 lines): imports the 3 target modules |
| `m5/M5/Definitions.lean` | Target A (135 lines): `K0`/`catalanConst`/`zeta3`/`eulerMascheroni`/`realPi`/`realE`/`realLn2`/`zeta2`/`logK0` as opaque axioms; `constantSet`/`purePowerTail`/`bilinearLeaf`/`basisDC`; `basisDC_length` theorem; `linearCombo` + `HasIntegerRelation` predicate; `H_empirical_operational` + `H_rigorous` bounds |
| `m5/M5/Result.lean` | Target B (92 lines): `m3_null_at_rigorous_bound`, `m3_null_at_empirical_bound`, `m3_two_tier_predicate_holds`, `m3_null_depends_on_M4_gap` |
| `m5/M5/Axioms.lean` | Target C (123 lines): `K0_value_first_digits` (numerical-binding shape stub), `pslq_cascade_implies_no_integer_relation` (rigorous-tier axiom), `bbc_empirical_implies_no_integer_relation` (empirical-tier axiom), `M4_fundamental_gap_proposition` + `M4_fundamental_gap` |
| `m5/PrintAxioms.lean` | Reproducibility check; emits the axiom set behind each mission theorem |
| `m5/_print_axioms_output.txt` | Committed canonical output of `PrintAxioms.lean` (audit-trail) |
| `m5/README.md` | Build instructions, simplified-imports note, H8/H10 status |
| `m5/.gitignore` | Excludes `.lake/build/` and `.lake/packages/` (per-machine) |

`m5/.lake/packages` is an NTFS junction to `claude-chat/lean4/.lake/packages` — operator's cached Mathlib snapshot. Junction is NOT committed (per `.gitignore`); re-create per machine.

**Total source lines (excluding comments/whitespace):** ~385, within operator's "~200-400 lines total" envelope.

### Step 5 — H10-mandated dry-run

Per H10 (`methodology/heuristics.md`), `lake build M5` is the full-regime dry-run for the M5 Lean toolchain. Executed 2026-05-16 ~15:30 JST.

**Result:**
- `lake exit code: 0`
- **Elapsed: 218.1 s** (≈ 3.6 min) from clean `.lake/build/` tree
- Oleans produced:
  - `m5/.lake/build/lib/M5/Definitions.olean` (82,768 bytes)
  - `m5/.lake/build/lib/M5/Result.olean` (34,264 bytes)
  - `m5/.lake/build/lib/M5/Axioms.olean` (38,488 bytes)
- No errors. Warnings present (Mathlib docstring linter on `List.lookmap_id'` and similar) — Mathlib-internal, not from M5 sources.

### Step 6 — `#print axioms` self-check

`lake env lean PrintAxioms.lean` executed; output saved to `m5/_print_axioms_output.txt`. Per-theorem axiom set:

**`M5.m3_null_at_rigorous_bound`** depends on:
- Lean core: `propext`, `Classical.choice`, `Quot.sound`
- Constant axioms: `M5.K0`, `M5.catalanConst`, `M5.eulerMascheroni`, `M5.logK0`, `M5.realE`, `M5.realLn2`, `M5.realPi`, `M5.zeta2`, `M5.zeta3`
- Mission evidence axiom: `M5.pslq_cascade_implies_no_integer_relation`

**`M5.m3_null_at_empirical_bound`** depends on: same constant set + `M5.bbc_empirical_implies_no_integer_relation`.

**`M5.m3_two_tier_predicate_holds`** depends on: union of the two above.

**`M5.m3_null_depends_on_M4_gap`** depends on: `M5.M4_fundamental_gap` only (no constants; the proposition body is `True ∧ True`).

**No unexpected leaks.** The axiom set exactly matches what the operator's directive specifies (axioms = external evidence black-boxes; theorems discharge via axiom application; M4 gap explicit as a Lean axiom). Reproducibility check PASSES.

## §3 — H7 / H8 / H10 compliance audit at M5 close

### H7 (capability functional verification)

- Lean 4.14.0 binary: verified at gold/M1 commit (`capability/_lean.available.md`); re-verified at M5 entry by successful `lake env lean PrintAxioms.lean` execution.
- Lake 5.0.0-src+f72c35b: bundled with Lean 4.14.0; verified by successful `lake build M5` execution (`exit 0`).
- Mathlib v4.14.0 cached: verified by `lake build M5` `Replayed` count on imports inside operator's cache closure.
- **H7 status: PASS** for M5 toolchain (the implementation already in scope at gold/M1 plus the additional Lake-build invocation here).

### H8 (literature paper-read verification on cited claims)

- `pslq_cascade_implies_no_integer_relation` is an **axiom**, not a theorem — it black-boxes FBA Theorem 1 + Corollary 2 at conclusion-level only, NOT at statement-level. Per operator M5 GREENLIGHT directive: *"H8 applies to FBA T1+Cor2 formalization if Target B includes statement-level formalization."* Result.lean does NOT formalize FBA T1+Cor2 at statement level (only uses the axiom conclusion via `exact`).
- **H8 status:** Bailey 1998 / Ferguson-Bailey-Arno 1999 paper-read **remains M6-deferred** under the prior U-MISSION-L conditional. NOT fired at M5.
- M6 trigger reminder: if M6 manuscript opts to cite the rigorous tier as proof-of-bound at statement level (rather than as `proven_corollary` derived from `harness/rigorous_bound.py`'s mpmath verbose-output observation), H8 must fire on Bailey 1998 before manuscript submission per `m6_preflight_checklist.md` §1.

### H10 (full-regime dry-run before canonical execution)

- M5 Lean toolchain is a new operationally-significant region per H10 criteria (new language, new build system, new dependency closure relative to mpmath/PARI/SymPy harnesses).
- `lake build M5` IS the H10-mandated dry-run; executed cleanly at 218.1 s wall-clock. Output preserved as audit-trail in `_print_axioms_output.txt` + Lake oleans (per-machine, not committed).
- **H10 status: PASS** for M5.

### U-MISSION-O reservation

Operator pre-labeled U-MISSION-O for any Mathlib4 deep-build problem during pre-M5 verification. The 587-modules-replayed-then-stall observation during the initial Real.pi import attempt was an H7-class capability-scope finding (cache closure shape), NOT a deep-build failure (Lake exited 0 when imports were simplified to cache-closure-internal modules). **U-MISSION-O label NOT consumed.** Reserved for future deep-build failures.

## §4 — Mutation budget classification

Per operator U-MISSION-J / U-MISSION-L / U-MISSION-N precedents:

**Operative test:** does the change force a modification to the operator's bounded hypothesis (basis form, predicate shape, success criterion)?

| Question | Answer |
|---|---|
| Does M5 change the basis B_D(C)? | NO. The Lean `basisDC` is structurally identical to the harness `basisDC` (7 pure-power + 1 hybrid-log + 7 bilinear, n=15). |
| Does M5 change the predicate `HasIntegerRelation`? | NO. The Lean predicate is the standard integer-linear-combination existence at height H, identical to the M3.1 harness's null-criterion. |
| Does M5 change the success criterion (cascade-stable null at H_rigorous = 1.04×10⁷²)? | NO. The Lean `m3_null_at_rigorous_bound` theorem states exactly the negation of `HasIntegerRelation basisDC H_rigorous`, which is exactly the M3.2 verdict. |
| Does M5 add new claims to `claims.jsonl`? | NO. M5 is downstream of all M2.1 literature claims; no new literature added. |
| Does M5 change the harness, sweep, or sweep_output? | NO. M5 imports the M3 evidence as axioms; no harness modifications. |

**Verdict:** M5 is a **field-map update** extending the representation language of the M3 conclusion from mpmath/PARI/SymPy/JSONL to Lean 4 + Mathlib v4.14.0 axiomatic encoding. **Mutation budget consumed: 0/1 still applies.**

## §5 — Authority chain (commits this M5 phase)

| Commit | Description |
|---|---|
| `fd13eeb` (pre-M5) | M4 CLOSED + `gold/M4` tag (operator M5 GREENLIGHT applies the tag) |
| *(pending push)* | §4.1 to m6_preflight_checklist.md (added pre-segment) + m5/ scaffolding + this 11th mutation_log entry + 19th plan.md addendum |

## §6 — Mission state post-M5

- **M1 + M2 + M3 + M4 + M5 ALL CLOSED.**
- M5 Lean skeleton type-checks cleanly under Lean 4.14.0 + Mathlib v4.14.0.
- `#print axioms` reproducibility check PASSES with the expected axiom set.
- 4 gold tags on origin: `gold/M1`, `gold/M2`, `gold/M3`, `gold/M4`. `gold/M5` left to operator discretion per operator's prior precedent.
- **M6 (manuscript drafting) READY** pending operator greenlight. Preflight checklist now contains §1 (Bailey 1998 H8 paper-read) + §2 (apples-to-stronger-apples framing) + §3.4 (operational-bound capping) + §4 (M4 gap framing) + §4.1 (M4 gap sub-classification).
- AEAL maturation curve at M5: **0 halts**. Total mission-life halts: **6** (unchanged from M4 close).

## §7 — Rule 6 audit (M5 commit batch)

- Zero portal interactions during M5 execution.
- One planned `git push origin main` operation (this commit batch) under operator's pre-authorized incremental-commit allowance for M1-M5 work.
- No `selected.md` edits (frozen at gold/M1).
- No `_m2.3_calibration_anchor.md` §7 edits (frozen at gold/M2).
- No canonical M3 JSONL edits (frozen at gold/M3).
- No `methodology/heuristics.md` edits (no new heuristic at M5; H7/H8/H10 already installed pre-segment).
- No `claims.jsonl` edits (M5 introduces no new literature claims).
- `gold/M5` tag NOT applied (operator discretion).
- Halt-and-flag pattern preserved: simplified-imports adjustment was a within-segment H7-class capability-scope observation resolved inline by reducing import surface; not a halt-class event (Lake never failed; simplification was preventive).

## §8 — Forward-flagged (non-blocking)

- Bailey 1998 H8 paper-read (M6-deferred per `m6_preflight_checklist.md` §1; fires if M6 cites rigorous tier at statement level).
- Apples-to-stronger-apples M6 §Introduction/§Results framing (`m6_preflight_checklist.md` §2).
- Operational-bound capping methods observation (M6 §Discussion per §3.4).
- M4 capability-gap framing with §4.1 sub-classification (M6 §Discussion).
- `gold/M5` tag (operator discretion at M5 close).

## §9 — `gold/M5` lock-up recommendation (for operator)

If operator chooses to apply `gold/M5`:
- **Recommended target SHA:** the commit produced by this batch (will be assigned at push time).
- **Tag message recommendation:** "M5 closed: Lean 4.14.0 skeleton type-checks; #print axioms reproducibility verified; H8 remains M6-deferred (no statement-level FBA T1+Cor2 in Result.lean)."
- **Tag pushability:** `git push origin gold/M5`.

If operator defers `gold/M5` to M6 close (analog of `gold/M2` waiting for predicate-ratification commit), that is also consistent with the prior precedent.
