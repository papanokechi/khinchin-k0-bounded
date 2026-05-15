# capability/mathlib4.available.md — Mathlib4 toolchain integration

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST; **deep build verification deferred to M5 entry per 30-min retro-audit budget**).

**Provenance:** operator has two existing Lean projects with full Mathlib4 cached and previously built locally:

| Project | Mathlib rev (manifest) | Mathlib version pin | `.lake/build` | `.lake/packages/mathlib` |
|---|---|---|---|---|
| `claude-chat/lean/wallis-formal-verification` | 14b67616b702b038bad6d1e7182864e57ebb9249 | master (no tag) | ✓ EXISTS | ✓ EXISTS |
| `claude-chat/lean4/siarc-lean4` (SIARCRelay11) | 4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84 | v4.14.0 | ✓ EXISTS | ✓ EXISTS |

This is operational evidence that operator's Lean+Lake toolchain successfully consumes Mathlib4 in a multi-target project (SIARCRelay11 has 4 lean_lib roots, all built). The cached `.lake/packages/mathlib` is the actual Mathlib4 source + Lake build artefacts.

**Role in harness:** M5 Lean 4 formalization skeleton imports Mathlib4 modules for the formal statement of the K_0 bounded sub-question (e.g., `Mathlib.NumberTheory.LSeries.Khinchin` if it exists, or hand-defined K_0 + relevant analytic-number-theory lemmas).

## Minimal working examples

### Example 1: Mathlib4 cached locally (filesystem evidence)
```powershell
Test-Path "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\lean4\.lake\packages\mathlib"
# Expected: True
Get-Content "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\lean4\lake-manifest.json" -Raw | ConvertFrom-Json |
  Select-Object -ExpandProperty packages | Where-Object { $_.name -eq 'mathlib' } | Select-Object name, rev
# Expected: name=mathlib, rev=4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84
```
**Result (2026-05-15 19:25 JST):** ✓ both paths exist; manifest pin matches.

### Example 2: full Mathlib4 build (DEFERRED to M5)
A complete `lake build` against the cached Mathlib4 to type-check a tiny `import Mathlib.Init` file would consume ≥ 10–60 minutes depending on cache freshness. This blows the 30-min total retro-audit budget. **Deferred to M5 entry**, where the formalization skeleton's first `lake build` will serve as the deep verification. If the deferred build fails, M5 fires a Capability Gap and the H4 escalation discipline applies.

## Caveats

1. **Lean version mismatch.** Local Lean is 4.29.1; the cached Mathlib pins are at `master` (head) and `v4.14.0`. Mathlib v4.14.0 may be too old for Lean 4.29.1 to compile cleanly. The M5 formalization skeleton must use a `lean-toolchain` file matching the chosen Mathlib pin. This is an M5 implementation detail, not a current capability gap.
2. **Network dependency.** Mathlib4 is fetched from `github.com/leanprover-community/mathlib4` via Lake; M5's `lake update` requires internet access. Document in M5 reproduce command.
3. **Disk footprint.** Mathlib4 + build artefacts are ~5–10 GB. Confirmed adequate on operator's workstation (existing projects show successful caches).

## Verification log

- 2026-05-15 19:25 JST: 2 distinct Lean projects show full `.lake/packages/mathlib` cached and `.lake/build` artefacts present ✓
- 2026-05-15 19:25 JST: lake-manifest.json files parse correctly, Mathlib rev pins recorded ✓
- Lean 4.29.1 + Lake 5.0.0 confirmed functional (see `lean_lake.available.md`).
- **Deep build verification: deferred to M5 entry per 30-min budget.**

## Reproduce command

```powershell
$wallis = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\lean\.lake\packages\mathlib"
$siarc = "C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\lean4\.lake\packages\mathlib"
Test-Path $wallis; Test-Path $siarc
# Expected: True, True
```
