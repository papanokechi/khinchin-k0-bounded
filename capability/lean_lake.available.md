# capability/lean_lake.available.md — Lean 4 toolchain + Lake build system

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Binary paths:**
- `lean.exe` at `C:\Users\shkub\.elan\bin\lean.exe`
- `lake.exe` at `C:\Users\shkub\.elan\bin\lake.exe`

**Versions:**
- Lean 4.29.1 (x86_64-w64-windows-gnu, commit f72c35b3f637c8c6571d353742168ab66cc22c00, Release)
- Lake 5.0.0-src+f72c35b (Lean version 4.29.1)

Both managed by `elan` (Lean's toolchain manager). Confirmed on PATH; both respond to `--version` immediately.

**Role in harness:** M5 Lean 4 formalization skeleton (per Brief §5). Type-checking and `#print axioms` on the M5 theorem. Lake builds the formalization project that mirrors operator's Lean track (`siarc-lean4`, `wallis-pcf-lean4`, `tunnell-cnp-lean4`).

## Minimal working examples

### Example 1: lean --version reports a coherent toolchain
```powershell
lean --version
# Expected: Lean (version 4.29.1, x86_64-w64-windows-gnu, commit f72c35b3f637c8c6571d353742168ab66cc22c00, Release)
```
**Result (2026-05-15 19:25 JST):** ✓ matches expected.

### Example 2: lake --version reports a compatible Lake
```powershell
lake --version
# Expected: Lake version 5.0.0-src+f72c35b (Lean version 4.29.1)
```
**Result (2026-05-15 19:25 JST):** ✓ matches expected (Lake's bundled Lean matches the system Lean — consistent toolchain).

### Example 3: trivial Lean compile (zero-dep)
A minimal `.lean` file:
```lean
-- File: tmp_test.lean
def hello := "world"
#eval hello
```
Compile with `lean tmp_test.lean` should produce `world` in stdout. **Not exercised at this verification time** because it would require a writable scratch directory outside the staging area; deferred to M5 entry where the formalization skeleton is actually built. The toolchain's responsiveness (Example 1, 2) is sufficient evidence of availability per H7.

## Verification log

- 2026-05-15 19:25 JST: lean --version returns Lean 4.29.1 + commit f72c35b ✓
- 2026-05-15 19:25 JST: lake --version returns Lake 5.0.0-src + bundled Lean 4.29.1 (consistent) ✓
- Operator's existing Lean projects (siarc-lean4, wallis-pcf-lean4, tunnell-cnp-lean4) confirm operational use of this toolchain across multiple repos.

## Reproduce command

```powershell
lean --version
lake --version
```
