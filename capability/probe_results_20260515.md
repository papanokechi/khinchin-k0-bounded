# Capability probe — 2026-05-15 ~17:38 JST

**Trigger:** Operator request 2026-05-15 ~17:38 JST in response to U-MISSION-C: *"run capability probe first. `python -c "import arb, flint, fpylll, cypari2"` plus `which gp` and `lean --version`. Return probe output."*

**AEAL framing:** this probe is the empirical resolution of U-MISSION-C. It supersedes the abstract machinery list inferred by CLI in the M1.0 §9 deliverable.

## Reproduce command

```powershell
cd C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\siarc\unsolved-relay-staging
# the script that was run is embedded inline; see the powershell session 2026-05-15 ~17:38 JST
# minimum reproduction:
python --version
python -c "import mpmath, sympy, numpy, gmpy2; print('core stack: OK')"
python -c "import flint" 2>&1   # expect ModuleNotFoundError
python -c "import fpylll" 2>&1  # expect ModuleNotFoundError
python -c "import cypari2" 2>&1 # expect ModuleNotFoundError
python -c "import sage.all" 2>&1 # expect ModuleNotFoundError
Get-Command gp
Get-Command lean
Get-Command lake
lean --version
python -c "from mpmath import mp, pi; mp.dps=500; print(str(pi)[-30:])"
python -c "from mpmath import pslq, mp, mpf; mp.dps=50; print(pslq([mpf(1), mpf('3.141592653589793238462')]))"
```

## Probe results (verbatim summary)

| Component | Status | Detail |
|---|---|---|
| Python | ✅ | 3.12.10 |
| mpmath | ✅ | 1.3.0, 500-dps π tail verified |
| sympy | ✅ | 1.14.0 |
| numpy | ✅ | 2.4.4 |
| gmpy2 | ✅ | 2.3.0 |
| **python-flint / arb** | ❌ | `ModuleNotFoundError: No module named 'flint'` |
| **fpylll** | ❌ | `ModuleNotFoundError: No module named 'fpylll'` |
| **cypari2** | ❌ | `ModuleNotFoundError: No module named 'cypari2'` |
| **sagemath (python)** | ❌ | `ModuleNotFoundError: No module named 'sage'` |
| scipy | ❌ | `ModuleNotFoundError: No module named 'scipy'` |
| mpsolve | ❌ | `ModuleNotFoundError: No module named 'mpsolve'` |
| **PARI/GP binary** | ✅ | `gp` on PATH (binary FOUND) |
| PARI binary | ❌ | `pari` not on PATH (this is normal; `gp` is the canonical name) |
| sagemath binary | ❌ | not on PATH |
| **Lean** | ✅ | `lean.exe` at `C:\Users\shkub\.elan\bin\lean.exe`, version 4.29.1 commit f72c35b |
| **Lake** | ✅ | `lake.exe` at `C:\Users\shkub\.elan\bin\lake.exe`, version 5.0.0-src+f72c35b |
| mpmath PSLQ (built-in) | ✅ | `pslq([1, π_50dps])` returned `None` (correct — no rational relation at this length) |

## Implications for the AEAL machinery base

### Available — confirmed by direct probe

1. **Arbitrary-precision real / complex arithmetic at 130–500 dps** — `mpmath`
2. **PSLQ integer-relation finder** — `mpmath.pslq` (built-in)
3. **Symbolic computation / CAS basics** — `sympy` (Gröbner, simplify, nsimplify, polynomial algebra, special functions, exact rationals)
4. **Bignum integer / rational arithmetic** — `gmpy2`, Python `int`, `sympy.Rational`
5. **Numerical-array primitives** — `numpy` (FFT, linear algebra over float64; NOT high-precision)
6. **PARI/GP** — via shell-out only (no `cypari2` Python bridge). Available functions of interest: `lindep` (PARI's integer-relation finder, an independent leg for the M3.1 harness), `factor` (NFS-class factorization for small-to-moderate cofactors), `nfinit` / `bnfinit` (number-field arithmetic, useful for #27 cubic-field entry), `qflll` (LLL on integer lattices — substitutes for fpylll at moderate dimensions)
7. **Lean 4.29.1 + Lake 5.0.0 + Mathlib4** — operator confirms working facility per Tunnell-CNP track + congruent-relay repository
8. **(operator-specific machinery)** PCF spectral fingerprint framework, Painlevé / Stokes / sub-leading-Stokes tooling — NOT externally probable; operator-attested only

### Not available — confirmed by direct probe

1. **`python-flint` / `arb` Python bindings** — rigorous interval / ball arithmetic NOT available through Python. PARI/GP's interval arithmetic exists but is weaker and shell-out only.
2. **`fpylll`** — LLL via Python bridge NOT available. PARI's `qflll` is the only substitute (shell-out only).
3. **`cypari2`** — PARI Python bridge NOT available. All PARI access must be via the `gp` binary as a subprocess.
4. **SageMath (any flavor)** — full CAS / number-theory toolkit NOT available.
5. **`scipy`** — numerical analysis (integrate, optimize, special) NOT available. `sympy` has analytic versions; `mpmath.quad` exists; FFT in `numpy` only.
6. **`mpsolve`** — high-precision root-finding NOT available. `mpmath.polyroots` is the substitute.

### Structural consequences for the M3.1 verification harness

The Brief §M3.1 names *"mpmath + Arb, or SymPy + Sage"* as the canonical two-library verification pair. With **arb and sage both unavailable**, the harness cannot use the canonical pair. The honest substitutes:

- **Leg 1 (primary):** `mpmath` PSLQ + cascading-precision at {130, 260, 520} dps
- **Leg 2 (independent):** shell-out to `gp` running `lindep` on the same vector at PARI's default precision (operator can extend with `\p <prec>`)
- **Leg 3 (sanity, weak):** `sympy.nsimplify(value, [basis...])` as a "does sympy see this relation?" cross-check; weaker than PSLQ, so only used as a tie-breaker

This is a **documented constraint, not a capability gap** — the harness can still discharge the §M3.1 three-step certification (cascading precision → independent reimpl → FP rejection); it simply uses different second-library tooling than the Brief example phrasing suggested.

**If** the operator wants the harness to use the canonical `mpmath + arb` pair, that requires installing `python-flint` (the canonical Python binding to FLINT/Arb on Windows). This is a discretionary install; flagged for operator decision but NOT proposed by CLI.

### Implications for specific survey-set entries

- **Entries #15, #16, #17, #18, #19, #20** (transcendence / PSLQ-driven): full PSLQ pipeline AVAILABLE; second-library leg via `gp lindep` AVAILABLE. M3.1 harness can certify. `machinery_available_locally = true`. AEAL-risk: MEDIUM (was LOW pre-probe) because the second-library leg uses `gp` shell-out rather than `arb` ball arithmetic; FP rejection is therefore weaker than canonical.
- **Entry #27** (Mahler badly-approximable pairs in cubic fields): cubic-field arithmetic AVAILABLE via `gp nfinit` shell-out. `machinery_available_locally = true`. AEAL-risk: MEDIUM (shell-out parsing fragility).
- **Entry #7** (Cunningham unfactored cofactors): NFS NOT in kit; PARI's `factor` works only up to moderate size. `machinery_available_locally = false`. **Drops at M1.1** per hard filter.
- **Entries #22, #25** (mock-modular / spt / crank): mock-modular machinery NOT in kit. `machinery_available_locally = false`. **Drops at M1.1** per hard filter.

### Implications for the Brief's Lean-formalization target (M5)

- Lean 4.29.1 + Mathlib4 confirmed via working `lean.exe` / `lake.exe` on PATH.
- Mathlib4 version compatibility with Lean 4.29.1 is operator-attested via the congruent-relay track; not independently probed here.
- M5 is unaffected by the arb/fpylll/sage gaps.

## Operator decision NOW RESOLVED

**U-MISSION-C — confirmed machinery base:**

> Primary: mpmath 1.3.0 (130–500 dps), sympy 1.14.0, numpy 2.4.4, gmpy2 2.3.0, mpmath.pslq, Lean 4.29.1 + Lake 5.0.0 + Mathlib4, PARI/GP shell-out (lindep, factor, nfinit, qflll), PCF spectral fingerprint framework (operator-attested), Painlevé/Stokes tooling (operator-attested).
>
> Excluded: python-flint / arb, fpylll, cypari2, sagemath, scipy, mpsolve, NFS-class factorization, mock-modular forms.

This machinery base is now BINDING on M1.1 triage-row construction (every `machinery_required` field references items from this list only; every `machinery_available_locally` value derives from this list).


---

## §AMENDED (2026-05-15 19:30 JST)

**Append by directive U-MISSION-H Option H1 + retroactive H7 (functional verification on capability claims).** Do not delete original rows above this block — false positives in the audit trail are evidence.

### What was wrong

The row in the Probe results table reading:

> | **PARI/GP binary** | ✅ | gp on PATH (binary FOUND) |

was a **false positive**. The probe used `Get-Command gp` to detect the binary. `Get-Command gp` on Windows PowerShell resolves to the built-in **alias** `gp -> Get-ItemProperty` (a PowerShell cmdlet alias for `Get-ItemProperty`), NOT to the PARI/GP binary. The probe interpreted "name resolves to something" as "PARI/GP binary on PATH". No actual gp.exe existed on the system at the time of the v1 probe.

This was caught at 2026-05-15 ~18:50 JST while collecting versions for `env/M1.lock` (routine `gp --version` failed with "term 'gp.exe' is not recognized"). Documented in `capability/independent_second_library.gap.md`; resolved by operator U-MISSION-H Option H1.

### Why it matters

The faulty row caused:
1. The probe's §3 ("Structural consequences for the M3.1 verification harness") proposed Leg 2 = `gp lindep` shell-out — under the false premise that gp was available. With gp absent, Leg 2 was empty, and the M3.1 harness's three-leg certification was actually only one-leg (mpmath PSLQ + cascading precision). This was about to be locked into the M1.3 freeze as a Brief-§M3.1-compliant harness when it was not.
2. Operator's U-MISSION-D decision ("DECLINE python-flint install. gp lindep substitute is sufficient.") rested on the false premise. The decision's substantive content (prefer gp over flint) stands; the antecedent assumption (gp is present) was wrong.

### Corrected status

After U-MISSION-H Option H1 + functional verification, PARI/GP **IS** now available:
- Binary: `C:\Users\shkub\PARI\gp.exe` (snapshot 2.18.1 development build, May 10 2026)
- Functional test 1: `lindep([1.0, 2.0, 3.0])` → `[-1, -1, 1]~` ✓
- Functional test 2: `lindep([1, sqrt(2), 3 - 2*sqrt(2)])` → `[3, -2, -1]~` ✓
- PATH wire-up: User scope, persistent. PowerShell alias shadow note: documented.

The corrected v2 record is at `capability/probe_results_20260515_v2.md`. **v2 supersedes v1 on the PARI/GP row.** All other rows in v1 have been retroactively re-verified per H7 (see v2 §2-§7); none of the other rows needed correction (the original v1 verdicts on mpmath, gmpy2, numpy, sympy, Lean, Lake stand).

### Generalized lesson (codified as H7 in `methodology/heuristics.md`)

**Name resolution ≠ functional verification.** PowerShell aliases, shell builtins, dead symlinks, stub binaries, and similar can all resolve a name without providing the function. H7 (added to heuristics 2026-05-15 19:30 JST) mandates that every capability_available claim must be backed by a use of the capability, not a name-resolution check. Retroactively binding on this file; forward-binding on M2.2 capability audit.

### Audit trail preservation

The original v1 rows remain above this §AMENDED block. The v1 record is preserved as evidence of the false positive — the audit trail is more valuable than a clean record. Future readers of this file should treat the v1 PARI/GP row as documentation of how name-resolution alone can fail H7 verification.

---

**END OF §AMENDED block.**

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
