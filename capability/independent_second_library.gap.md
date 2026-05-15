# capability/independent_second_library.gap.md — Capability Gap: No second-library leg for M3.1 PSLQ harness

**Date discovered:** 2026-05-15 ~18:50 JST (during M1.3 freeze preparation)
**Discovery context:** version collection for `env/M1.lock`. Routine version probe `gp --version` failed; subsequent diagnosis revealed that `gp` is a PowerShell built-in alias for `Get-ItemProperty`, NOT the PARI/GP binary.

**Status:** OPEN — gates M1.3 freeze. Pending operator U-MISSION-H decision.

---

## §1. The empirical finding

The 17:38 JST capability probe (`capability/probe_results_20260515.md`) recorded:

> | **PARI/GP binary** | ✅ | `gp` on PATH (binary FOUND) |

This was a **false positive**. The probe used `Get-Command gp` to detect the binary. In PowerShell, `Get-Command gp` resolves to:

```
CommandType     Name                                               Source
-----------     ----                                               ------
Alias           gp -> Get-ItemProperty                              (none)
```

`gp` is a built-in PowerShell alias for the `Get-ItemProperty` cmdlet. It has been on every PowerShell installation since v1.0. It is not PARI/GP.

## §2. Empirical verification of absence (2026-05-15 18:46–18:50 JST)

Reproduce command:

```powershell
# 1. Confirm gp is an alias, not a binary
Get-Command gp | Format-List CommandType, Name, ResolvedCommandName, Source
# Expected: CommandType=Alias, ResolvedCommandName=Get-ItemProperty

# 2. cmd.exe `where` returns no match
cmd /c "where gp 2>&1"
cmd /c "where pari 2>&1"
# Expected: "INFO: Could not find files for the given pattern(s)."

# 3. Filesystem search of standard PARI install locations
$candidates = @(
  "C:\Program Files\PARI",
  "C:\Program Files (x86)\PARI",
  "C:\PARI", "C:\pari64", "C:\pari",
  "C:\msys64\mingw64\bin", "C:\msys64\usr\bin",
  "C:\cygwin64\bin", "C:\cygwin\bin"
)
$candidates | ForEach-Object { if (Test-Path $_) { Write-Output "EXISTS: $_" } }
# Expected (this system): empty output — no candidate directory exists

# 4. Recursive search of user profile for gp.exe
Get-ChildItem -Path "C:\Users\shkub" -Filter "gp.exe" -Recurse -ErrorAction SilentlyContinue -Depth 4
# Expected (this system): empty

# 5. WSL fallback
wsl which gp 2>&1
# Expected (this system): "Windows Subsystem for Linux is not installed."
```

**Verdict:** PARI/GP is genuinely absent from this workstation. There is no fallback installation, no WSL with gp, no Conda-env wrapper, no Cygwin/MSYS2 path that contains it.

## §3. Implications

### §3.1 The 17:38 JST capability probe was wrong on one component

The probe record at `capability/probe_results_20260515.md` line 42 is incorrect:

> | **PARI/GP binary** | ✅ | `gp` on PATH (binary FOUND) |

The correct entry would be:

> | **PARI/GP binary** | ❌ | Not installed. `Get-Command gp` returns a PowerShell built-in alias for `Get-ItemProperty`, which masked the absence in the original probe. |

A corrigendum will be appended to `capability/probe_results_20260515.md` at audit close — but only after operator's U-MISSION-H decision (the corrigendum's recommended resolution depends on operator's choice between install / accept-gap / re-scope).

### §3.2 U-MISSION-D's resolution rests on a faulty premise

Operator's U-MISSION-D directive (2026-05-15 ~18:00 JST):

> *"DECLINE python-flint install. gp lindep substitute is sufficient. If a future milestone genuinely requires interval arithmetic that neither mpmath nor gp can provide, log it as a Capability Gap and stop per §0.2; do not retrofit the install."*

This directive **presumes gp is already installed**. The "no retrofit" clause governs what to do if gp+mpmath together prove insufficient for some specific need. It does not address the antecedent question of whether gp is even available. The capability-probe false positive is what fed operator the assumption.

### §3.3 The M3.1 verification harness loses its independent-reimpl leg

The Brief §M3.1 names *"mpmath + Arb, or SymPy + Sage"* as the canonical two-library verification pair. The probe document at §3 ("Structural consequences for the M3.1 verification harness") proposed:

- **Leg 1 (primary):** mpmath PSLQ + cascading-precision at {130, 260, 520} dps
- **Leg 2 (independent):** shell-out to `gp` running `lindep` on the same vector
- **Leg 3 (sanity, weak):** `sympy.nsimplify` tie-breaker

**With gp unavailable, Leg 2 is empty.** The harness now has:

- Leg 1: mpmath PSLQ + cascading-precision (intact)
- Leg 2: **empty** — no independent integer-relation finder
- Leg 3: `sympy.nsimplify` (intact, but weaker than PSLQ and not a true independent reimpl)

Per Brief §M3.1: *"Independent reimplementation in a second library (mpmath + Arb, or SymPy + Sage) where applicable."* — the harness CANNOT discharge this step at current capability.

### §3.4 `targets/selected.md` §2 currently contains a now-incorrect claim

`selected.md` §2 (post-U-MISSION-G refinement, 2026-05-15 18:45 JST) reads, in part:

> *"Second-leg verification via `gp lindep` shell-out (per U-MISSION-D's declination of python-flint, `gp lindep` is the canonical 2nd library here)."*

This claim was true under the false-probe premise. It is no longer true. If the M1.3 freeze tags `gold/M1` with this text intact, the gold-frozen `selected.md` will be empirically wrong.

## §4. Disposition options (U-MISSION-H)

Per Brief §0.2 ("If a step requires machinery you cannot deploy ... you write a `capability_gap.md` entry under that claim and stop"), the present file is the required gap entry. Per Brief §0.2 and U-MISSION-D, CLI does not have authority to install machinery autonomously. Operator selects one of:

### Option H1 — Install PARI/GP for Windows
The PARI Group distributes a Windows binary at <http://pari.math.u-bordeaux.fr/download.html> (~30–50 MB, self-contained `.exe` installer). This is consistent with U-MISSION-D's *spirit* ("use gp not flint") but conflicts with U-MISSION-D's *letter* on the "no retrofit" clause. Operator can override the letter to honor the spirit. CLI handles install + PATH wire-up + post-install probe verification.

### Option H2 — Install `python-flint` (override U-MISSION-D)
Restores the canonical `mpmath + arb` harness pair. `python-flint` provides Python bindings to FLINT (which includes Arb for rigorous interval arithmetic). U-MISSION-D explicitly DECLINED this. Re-opens that decision.

### Option H3 — Accept the capability gap
Document in this file. Update `selected.md` §2 to remove the `gp lindep` reference and weaken the M3.1 harness commitment to "single-library cascading-precision certification + `sympy.nsimplify` cross-check". The harness's M3.1 step-(2) ("independent reimplementation") becomes a documented capability gap. Brief §M3.1 must be either (a) loosened by operator amendment, or (b) treated as an immediate STOP at the M3.1 step per Brief §0.2 (in which case M3.1 fires the FIRST capability gap of the mission and the H4 heuristic clock starts).

### Option H4 — Re-select target away from PSLQ-track entries
The probe's downstream implication (`probe_results_20260515.md` §"Implications for specific survey-set entries") put #15 (Khinchin K_0), #16 (Catalan G), #17 (Apéry), #18 (Lévy β), #19, #20 all at "AEAL-risk MEDIUM (was LOW pre-probe)" under the gp-lindep assumption. With gp absent, all six rise to MEDIUM-HIGH. Operator could revoke U-MISSION-F's selection of Khinchin K_0 and re-select to a non-PSLQ-track target where the single-library issue is less acute. (Survey set entries outside #15–#20 that don't need PSLQ: e.g., the Lean-formalization-only routes for #21-class targets where M3 is short or skipped.)

## §5. CLI recommendation

**Recommend Option H1 (install PARI/GP).** Reasoning:

1. **Honors operator's stated machinery preference.** U-MISSION-D's substantive content was "gp not flint" — installing gp respects that ordering.
2. **The "retrofit" interpretation.** U-MISSION-D's "no retrofit" clause is most naturally read as "no last-minute install of *flint specifically* after a sweep-substitution failure." It is not a blanket prohibition on installing machinery that was wrongly assumed present.
3. **The cost is bounded.** PARI/GP install is ~5 minutes (download installer, run installer, add to PATH, re-probe). It does NOT require building from source.
4. **The freeze is salvageable.** With gp installed and re-probed, `selected.md` §2 is true as written. No mutation_log entry needed.
5. **Preserves M3.1 harness rigor.** Leg 2 (independent integer-relation finder) is restored. AEAL-risk for #15–#20 returns to MEDIUM.

Recommendation alternative (if operator rejects H1): **Option H3 (accept gap)** is preferable to H2 (install flint after declining it). H2 would reopen a resolved operator decision; H3 documents the gap honestly and lets the mission proceed under a reduced harness.

## §6. AEAL discipline note

This is the *fourth* pre-freeze finding to halt the M1.3 sequence:

1. (M1.1, 2026-05-15) Operator amendments: drop #10, hold #18, hold #23, hold #26 (RESOLVED at M1.1 close)
2. (M1.2, 2026-05-15) Process-to-content ratio binding rule (RESOLVED at M1.2 close)
3. (M1.3, 2026-05-15 ~18:32 JST) `khinchin-signature-pslq` overlap audit — U-MISSION-G (RESOLVED at 18:45 JST → Option A)
4. **(M1.3, 2026-05-15 ~18:50 JST) THIS FINDING — capability-probe false positive on PARI/GP**

These halts are AEAL working as intended. Each one prevented a freeze that would have locked in incorrect or under-audited claims. Pattern observation: the 17:38 JST capability probe and the M1.2 namespace audit both missed components that empirical verification would have caught; this is the second cheap-verification miss in 24 hours. **The H6 namespace-audit heuristic should be generalized at next operator decision** to cover capability-claim verification, not only independence-overlap verification.

## §7. Brief-fidelity correction precedent applies

The binding rule installed in `mutation_log/m1.2_to_m1.3_brief_fidelity_correction.md` §3 reads:

> *"When a Brief reference (repo name, prior paper, machinery claim, library availability, version assumption, named-author result) can be empirically verified at <5 minutes of CLI effort, the CLI MUST verify before relying on it."*

The 17:38 JST capability probe's `gp` row is precisely a "machinery claim / library availability" assertion. Under this rule (which I just installed at 18:45 JST and applies retroactively as governance), the probe row should have been verified as "binary actually executes and returns a PARI/GP version string", not as "name resolves to something". This finding is the rule's first material application.

## §8. Status

- This file: created 2026-05-15 ~18:50 JST.
- `targets/selected.md` §2: NOT YET updated. Update depends on operator U-MISSION-H selection.
- `capability/probe_results_20260515.md`: NOT YET corrected. Corrigendum depends on operator H-selection.
- `env/M1.lock`: NOT YET generated. Will record final post-H state.
- `gh repo create`: NOT EXECUTED. Halted pending operator H-decision.
- `gold/M1` tag: NOT APPLIED.
- Mutation budget for M1.3: still 0 hypothesis mutations consumed; this entry is a Capability Gap document (Brief §0.2), not a mutation.

Operator decision on U-MISSION-H gates freeze.

---

**END OF ENTRY.**

Co-authored-by: Copilot &lt;223556219+Copilot@users.noreply.github.com&gt;
