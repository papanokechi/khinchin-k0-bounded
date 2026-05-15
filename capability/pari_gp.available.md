# capability/pari_gp.available.md — PARI/GP

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Binary path:** `C:\Users\shkub\PARI\gp.exe`
**Version:** GP/PARI Calculator 2.18.1 (development 30880-965aad07f8), amd64 mingw (x86-64/GMP-6.1.2 kernel) 64-bit, compiled May 10 2026.
**Provenance:** snapshot binary from <https://pari.math.u-bordeaux.fr/pub/pari/windows/snapshots/gp64-gmp-git-latest.exe>. Substituted for the stable 2.17.3 installer because the installer's UAC prompt auto-cancelled twice (~123s each) in autopilot. Snapshot is also from `pari.math.u-bordeaux.fr`, also a standalone .exe. See `mutation_log/m1.3_pari_gp_install_20260515.md` §3 for the deviation rationale.

**PATH wire-up:**
- User PATH (HKCU) appended with `C:\Users\shkub\PARI` (2026-05-15 19:20 JST) — persistent across shells.
- **Important caveat:** PowerShell's built-in alias `gp -> Get-ItemProperty` SHADOWS the binary even with PATH set. In PowerShell, invoke via full path or `& "C:\Users\shkub\PARI\gp.exe"`. In `cmd.exe`, Python `subprocess`, and any non-PowerShell shell, `gp` resolves to the binary normally (no alias).

## Minimal working examples (H7-required, exercising the specific harness functions)

### Example 1: `lindep` on a trivial integer relation
```powershell
# Powershell (full-path invocation to avoid alias shadow):
"lindep([1.0, 2.0, 3.0])" | & "C:\Users\shkub\PARI\gp.exe" -q
# Returns: [-1, -1, 1]~     (verifies: -1*1 + -1*2 + 1*3 = 0)
```

### Example 2: `lindep` on an algebraic identity
```powershell
"lindep([1, sqrt(2), 3 - 2*sqrt(2)])" | & "C:\Users\shkub\PARI\gp.exe" -q
# Returns: [3, -2, -1]~     (verifies: 3*1 + -2*sqrt(2) + -1*(3 - 2*sqrt(2)) = 0)
```

### Example 3: Python subprocess shell-out pattern (for M3.1 harness Leg 2)
```python
import subprocess
GP_BIN = r"C:\Users\shkub\PARI\gp.exe"

def gp_lindep(constants, dps=300, maxcoeff=None):
    \"\"\"Run gp lindep on a list of high-precision constants, return the integer-relation vector or None.\"\"\"
    expr_vec = ", ".join(str(c) for c in constants)
    script = f"\\\\p {dps}\nlindep([{expr_vec}])\n"
    p = subprocess.run([GP_BIN, "-q"], input=script, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        return None  # caller should check stderr
    out = p.stdout.strip()
    # parse "[a, b, c]~" -> [a, b, c]
    if out.startswith("[") and "~" in out:
        return [int(x.strip()) for x in out.strip("[]~").split(",")]
    return None
```

## Harness role

This binary serves as **Leg 2 (independent integer-relation finder)** of the M3.1 verification harness per `targets/selected.md` §2. The cascading-precision triage (H1) and the M3.1 cascade (Brief §M3.1 step 1) run on `mpmath.pslq` as Leg 1; `gp lindep` provides the second-library independent reimplementation per Brief §M3.1 step 2.

## Caveats

1. **Daily-build snapshot, not stable release.** 2.18.1 (development 30880-965aad07f8) was built May 10 2026, ~5 days before this install. Operator may want to replace with the stable 2.17.3 installer when convenient; this requires UAC approval. For now, the snapshot is sufficient for harness use.
2. **PowerShell alias shadow.** As noted above.
3. **Stack size.** Default gp stack is 8M; PSLQ-class lindep on high-precision vectors may need `-s 1G` or higher. Document on use in M3.1 harness implementation.

## Verification log

- 2026-05-15 19:25 JST: lindep([1.0, 2.0, 3.0]) → [-1, -1, 1]~ ✓
- 2026-05-15 19:25 JST: lindep([1, sqrt(2), 3-2*sqrt(2)]) → [3, -2, -1]~ ✓
- gp --version returns the version string above ✓

## Reproduce command

```powershell
$gp = "C:\Users\shkub\PARI\gp.exe"
"lindep([1, sqrt(2), 3 - 2*sqrt(2)])" | & $gp -q
# Expected output: [3, -2, -1]~
```
