# M5 — Lean 4 Skeleton for the Khinchin K₀ Bounded Null

**Authority:** operator M5 GREENLIGHT 2026-05-16 ~14:52 JST after M4 CLOSED
(commit `fd13eeb` = `gold/M4`). Brief §M5 deliverable.

**Toolchain:** `leanprover/lean4:v4.14.0` (operator's cached Mathlib pin).

**Mathlib pin:** `leanprover-community/mathlib4 @ v4.14.0` — see
`lake-manifest.json`.

## Build

```
cd m5
lake build M5
```

H10-mandated dry-run wall-clock (recorded 2026-05-16 ~15:34 JST,
operator's machine, simplified-import version): **218.1 s** (≈ 3.6 min)
to `exit 0` from a clean `.lake/build/` tree, using the cached
`.lake/packages/` snapshot (junctioned to a sibling project's cache).

## Three-target scope (operator-recalibrated)

| File | Role | Lines |
|---|---|---|
| `M5/Definitions.lean` | Target A — `basisDC`, `HasIntegerRelation`, bounds | ~135 |
| `M5/Result.lean` | Target B — `m3_null_at_rigorous_bound` + 3 sibling theorems | ~92 |
| `M5/Axioms.lean` | Target C — 4 axioms encoding FBA, M3, BBC, M4-gap evidence | ~123 |
| `M5.lean` | Aggregator | ~35 |
| **Total** | | **~385** |

All within operator's "~200-400 lines total" envelope.

## `#print axioms` reproducibility check

Run:
```
lake env lean PrintAxioms.lean
```
Expected output: `_print_axioms_output.txt` (committed) — each of the
four mission theorems is shown to depend on:

* **Lean core:** `propext`, `Classical.choice`, `Quot.sound`
* **Mission constants (opaque axioms):** `K0`, `catalanConst`,
  `eulerMascheroni`, `logK0`, `realE`, `realLn2`, `realPi`, `zeta2`, `zeta3`
* **Evidence axioms:** `pslq_cascade_implies_no_integer_relation`
  (rigorous tier, FBA T1+Cor2 black-box), and/or
  `bbc_empirical_implies_no_integer_relation` (empirical tier, BBC c-parity
  black-box), as theorem-appropriate
* **M4 gap axiom:** `M4_fundamental_gap` (used only by
  `m3_null_depends_on_M4_gap`)

No unexpected leaks. Re-running `lake env lean PrintAxioms.lean`
post-edit should reproduce `_print_axioms_output.txt` byte-for-byte.

## Simplified-imports note

Mathlib v4.14.0 does not include `Real.catalan`, `Real.eulerMascheroni`,
or `Real.zeta3`. To keep the M5 build self-contained on the cached
package snapshot, we declared `realPi`, `realE`, `realLn2`, `zeta2`, and
`logK0` as opaque `axiom` declarations (rather than pulling
`Mathlib.Data.Real.Pi.Bounds` / `Mathlib.Analysis.SpecialFunctions.{Log,Exp}`
which would extend the dependency closure beyond the cached set). The
operator's M5 directive specifies "axioms stand for the numerical
evidence the FBA + M3 + M4 work establishes externally" — these constant
axioms are consistent with that directive. The Lean structure remains
correct: the basis is constructed from named real-valued constants; any
downstream consumer can re-bind those axioms to concrete `Real.pi` /
`Real.exp 1` / `Real.log 2` definitions by adding the relevant imports
and proving the `axiom` declarations as `theorem`s (a strictly-additive
extension).

## H8 status (load-bearing reminder)

`pslq_cascade_implies_no_integer_relation` is declared as an `axiom` —
the Lean file does **NOT formalize the FBA Theorem 1 + Corollary 2
statement at the Lean level**. Per operator M5 GREENLIGHT directive,
this means H8 paper-read on Bailey 1998 / Ferguson-Bailey-Arno 1999
**remains M6-deferred** under the prior U-MISSION-L conditional. If a
future M6 revision opts for statement-level formalization of FBA T1+Cor2
in Lean, H8 must fire at that point per operator's directive
("H8 applies to FBA T1+Cor2 formalization if Target B includes
statement-level formalization").

## H10 dry-run status

This `lake build` run **is** the H10-mandated full-regime dry-run for
the M5 Lean toolchain — see `mutation_log/m5_lean_skeleton_20260516.md`
for the install-event-log entry. Per H10, any future M5 modification
that meaningfully extends the Mathlib import surface requires a fresh
H10 dry-run before canonical execution.

## Files

```
m5/
├── lakefile.lean              -- Lake config (Mathlib v4.14.0 require)
├── lean-toolchain             -- leanprover/lean4:v4.14.0
├── lake-manifest.json         -- copied verbatim from operator's siarc-lean4
├── M5.lean                    -- root aggregator
├── M5/
│   ├── Definitions.lean       -- Target A
│   ├── Result.lean            -- Target B
│   └── Axioms.lean            -- Target C
├── PrintAxioms.lean           -- #print axioms reproducibility script
├── _print_axioms_output.txt   -- committed canonical output of PrintAxioms.lean
├── README.md                  -- this file
└── .gitignore                 -- excludes .lake/build/ + .lake/packages/
```

`.lake/packages/` is a per-machine NTFS junction to the operator's
cached Mathlib snapshot at `claude-chat/lean4/.lake/packages`. Not in
git; re-create per machine via `lake update` or junction equivalent.
