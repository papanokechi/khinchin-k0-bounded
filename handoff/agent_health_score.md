# Agent Health Score — full-mission retrospective (M1–M6)

**Repository:** `papanokechi/khinchin-k0-bounded` @ `origin/main`
**Snapshot HEAD:** `e0defff` (paper byline applied; M6 Step 2 amendment)
**Gold tags ratified:** `gold/M1` (`15b216f`), `gold/M2` (`ca9c989`), `gold/M3` (`9c2702d`), `gold/M4` (`fd13eeb`), `gold/M5` (`208f6fc`).
`gold/M6` deferred per Brief §M6.2 (post-Zenodo deposit).
**Drafting status:** M6 Step 2 manuscript halted for operator review at `e0defff`. Steps 3–6 not yet executed.

This document is the concrete-data view of the four health-score axes named in Brief §M6.3 and previewed in the manuscript's §B.3 (`paper/main.tex` lines 1050–1066). It is intended as the audit substrate the operator can quote from, both for `handoff/summary.md` and for any external referee or replication review.

The four axes:

1. **Claim-to-sweep ratio** — how many load-bearing claims are made, vs. how many candidates are tested? (Low ratio = manuscript is conservative; many candidates examined, few claims made.)
2. **Reproduce-command coverage** — what fraction of canonical claims carry an executable reproduce command?
3. **Capability-gap honesty** — what fraction of encountered capability gaps were documented as such, vs. papered over with workaround numerics?
4. **Literature-fidelity honesty** — how many fidelity catches were surfaced, and how were they resolved?

Axis values reported below as integer counts (not normalized) so they can be re-derived from the repository at any time.

---

## Axis 1 — Claim-to-sweep ratio

### Numerator: load-bearing claims in `paper/main.tex`

The manuscript carries **5 load-bearing claims** in the §Results / §Discussion sense:

| # | Claim | Section | Status |
|---|---|---|---|
| C1 | M3.2 cascade-stable null on the primary `B_D(C)` at `n=15`. | §3.2 (lines 649–695) | tested ✓ |
| C2 | Empirical-tier bound `H_empop ≈ 7.997 × 10^69` at the primary, cap-inactive. | §3.2, §2.2 (lines 303–351) | tested ✓ |
| C3 | Rigorous-tier bound `H_rig = 1.0361 × 10^72` as Euclidean-norm lower bound, with implied coefficient-height `H_rig/√n ≈ 2.676 × 10^71`. | §3.2 (lines 668–690), §2.2 Tier 2 | proven_corollary ✓ |
| C4 | Bit-for-bit reproducibility M3.2a ↔ M3.2b at primary cascade. | §3.1 (lines 612–648), §3.6 (lines 752–766) | tested ✓ |
| C5 | M4 capability gap is fundamental, not contingent. | §4.3 (lines 837–887) | structurally argued via 7-candidate survey + 4-path SymPy probe ✓ |

### Denominator: candidate sub-bases tested

Per `harness/sweep_output/m32b_empirical_sweep.jsonl` (frozen at `gold/M3` = `9c2702d`):

| Family | n | sub-basis count |
|---|---|---|
| `primary_full` (the `B_D(C)` at D=6) | 15 | 1 |
| `complement_plus_K0_k` | 9 | 7 |
| `full_complement` | 8 | 1 |
| `triplet_log_*` | 3 | 21 |
| `pair_bilinear_*` | 2 | 21 |
| `pair_log_*` | 2 | 14 |
| **Total candidates tested** | — | **65** |

Plus the M3.2a primary cascade JSONL (`m32a_primary_cascade.jsonl`, 1 record with full cascade triple at P, 2P, 4P) which is the verification-class promoted (`pc`) record.

Plus a PARI/GP `lindep` independent corroboration leg per candidate (65 second-leg runs in the same JSONL).

### Ratio

| Quantity | Value |
|---|---|
| Load-bearing claims | 5 |
| Sub-basis candidates tested | 65 |
| Independent-leg PARI/GP verifications | 65 |
| **Claim-to-sweep ratio** | **5 / 65 ≈ 0.077** |

**Interpretation.** A *low* claim-to-sweep ratio is the desirable direction here: the manuscript makes very few load-bearing claims, but each is calibrated against a much larger empirical population than the claim itself uses. This is the opposite of the failure mode where a manuscript over-generalizes from a small sample. The 5/65 ratio is conservative by design.

The matching prose in `paper/main.tex` §B.3 (line 1054) states the ratio as approximately 5/65; this document is the source-of-truth for that approximation.

---

## Axis 2 — Reproduce-command coverage

### Source-of-truth: `literature/claims.jsonl`

Per the AEAL schema (`literature/_schema.md`), every entry in `claims.jsonl` carries a non-empty `reproduce_command` field giving a one-shot command (or short script invocation) sufficient to retrieve the cited primary source.

| Quantity | Value |
|---|---|
| Total `claims.jsonl` entries | 20 |
| Entries with non-empty `reproduce_command` | 20 |
| Entries with empty / missing `reproduce_command` | 0 |
| **Reproduce-command coverage on literature claims** | **20 / 20 = 100 %** |

### Manuscript-side reproduce-command coverage

Per `paper/main.tex` Appendix A (lines 891–957), every numerical result in §3 has a corresponding canonical command:

| Manuscript claim | Canonical reproduce command | Appendix A line |
|---|---|---|
| M3.2 primary cascade JSONL | `python harness/sweep.py --regime primary_full --output m32a_primary_cascade.jsonl` | A pseudocode block ~907 |
| M3.2b empirical sweep JSONL | `python harness/sweep.py --regime empirical_sweep --output m32b_empirical_sweep.jsonl` | A pseudocode block ~907 |
| M3.2b summary audit | `python harness/_audit_m32b_summary.py` | mentioned at ~946 |
| H10 extended dry-run | `python harness/sweep.py --m31-extended-dry-run` | A pseudocode block ~907 |
| Lean 4 #print axioms | `cd m5 && lake env lean M5/Result.lean` (+ `#print axioms`) | A pseudocode block (~925) |

Plus the SHA-256 hash table for paper-read primary sources (Appendix A): `lit-001` signature paper, `lit-002` BBC 1997, `lit-009` FBA 1999, `lit-010` Bailey 1998 — all bound to canonical-PDF hashes for byte-level reproducibility verification.

| Quantity | Value |
|---|---|
| Numerical results in §3 with a canonical reproduce command | every one |
| Paper-read primary sources with SHA-256 hash bound | 4 / 4 |
| **Manuscript reproduce-command coverage** | **100 %** |

---

## Axis 3 — Capability-gap honesty

### Capability gaps documented in `capability/` directory

| File | Gap class | Resolution | Status at `gold/M5` |
|---|---|---|---|
| `independent_second_library.gap.md` | M2.2 (PARI/GP install not yet verified at M2 entry) | resolved at U-MISSION-J / M2.3 via H7 functional verification | RESOLVED |
| `symbolic_closure.gap.md` | M4 (symbolic closure of M3 null beyond available machinery) | classified FUNDAMENTAL; 7-candidate survey + 4-path SymPy probe with verdict `documented_capability_gap` | DOCUMENTED |

### Capability gaps surfaced and surfaced-as-such (not papered over)

| Mission stage | Gap | What concealment would have looked like | What was actually done |
|---|---|---|---|
| M2.2 | PARI/GP install state on operator's machine unverified | proceed to M3 with `mpmath`-only single-leg empirical sweep | H7 installed; functional verification before declaring; PARI/GP confirmed; dual-leg ran in M3.2 |
| M4 | structural closure of M3 null requires Mahler / transcendence / Galois machinery beyond declared stack | extend M3.2 to a larger sweep and frame the larger null as "structural" | 7 candidate structural arguments surveyed against `K_0`'s known properties; each shown to fail at one of (i) hypothesis-unsatisfied (LW, Schanuel, Nesterenko), (ii) algebraicity-required (Mahler, Galois, height theory), (iii) scope-ceded (CF-theoretic per `seeds/26` DO-NOT-REENTER); 4-path SymPy probe (transcendence query, nsimplify on named-constants basis, Groebner with `K_0` symbolic, LW/GS/Nesterenko/Schanuel applicability) all return False; FUNDAMENTAL classification |

### Capability availability files (positive capability statements)

For completeness — every claimed capability was also functionally verified per H7 (not just name-resolved):

| File | What was verified | Method |
|---|---|---|
| `gmpy2.available.md` | mpmath's high-precision backend | functional smoke + version pin |
| `lean_lake.available.md` | Lean 4.14.0 + Lake build | `lean --version`, `lake env lean M5/Result.lean` |
| `mathlib4.available.md` | Mathlib v4.14.0 import-closure cache | `Replayed` cache hits on M5 imports |
| `mpmath.available.md` | mpmath.pslq + .mpf | `python -c "import mpmath; print(mpmath.__version__)"` + smoke compute |
| `numpy.available.md` | numpy (not load-bearing but transitively imported) | version pin |
| `pari_gp.available.md` | PARI/GP `gp -q` + `lindep` | full-precision smoke at `_smoke_gp_full_precision.py` |
| `sympy.available.md` | SymPy 1.14.0 (M4 symbolic probe) | `_m4_symbolic_probe.py` invocation log |
| `machinery_base_confirmed.md` | M2.2 capability-base summary | overall pass at M2.2 → M2.3 |
| `probe_results_20260515.md` / `probe_results_20260515_v2.md` | M2.2 probe runs | each documented with full invocation, output, signature |

| Quantity | Value |
|---|---|
| Documented capability gaps | 2 |
| Concealed capability gaps (gaps known to operator+CLI but not entered into `capability/`) | 0 |
| Functionally-verified positive capabilities | 9 |
| **Capability-gap-documentation rate** | **2 / 2 = 100 %** |

**Interpretation.** No gap encountered during the mission was concealed. The M4 gap is the load-bearing one: it could have been papered over with an additional ~10⁴-candidate empirical sweep at a slightly higher precision, which would have inflated the apparent rigor of the manuscript without changing the load-bearing claim's evidence class. The FUNDAMENTAL classification, with explicit narration of why each of 7 candidate structural arguments is insufficient, is the honest-gap-documentation outcome.

---

## Axis 4 — Literature-fidelity honesty

### Fidelity catches in `literature/_fidelity_findings.md`

Per `_fidelity_findings.md` (running document, updated through M6 Step 1):

| # | Catch | Surfaced at | Resolution |
|---|---|---|---|
| 1 | "No published PSLQ on `K_0`" — AI-aggregated web-search summary; refuted by paper-read of BBC 1997 §4 Tests 1+2 | M2.1 (2026-05-15) | `lit-018-fidelity-no-prior-k0-pslq-refuted.md` + new primary entry `lit-002-bailey-borwein-crandall-1997.md`; H8 paper-read heuristic installed at U-MISSION-J |
| 2 | "FBA 1999 states `H ≈ 10^{P/n}` as a theorem" — folklore-grade not theorem-grade | M2.3 (2026-05-15) | paper-read of FBA 1999 (full text via institutional access); H9 verification-class taxonomy installed at U-MISSION-L; two-tier predicate adopted |
| 3 | mpirical_height float overflow at n ≤ 3 + `H_empirical` ↔ `maxcoeff` semantic question | M3.2b (2026-05-16) | U-MISSION-N two-field reporting (`H_empfo` formula + `H_empop` capped); operational-bound capping clause `§7.10`; H10 full-regime dry-run heuristic installed |
| 4 | Bailey 1998 H8 fire — D2 (γ = √(4/3) boundary), D3 (mpmath cited source), D5 ("general rule" wording for fsp class) | M6 Step 1 (2026-05-16) | D2 + D3 cleared as immaterial to rigorous tier; D5 surfaced new primary-source warrant for `fsp` class; `lit-010` upgraded `fidelity_watch → verified`; `§7.11` calibration anchor |

### `claims.jsonl` status distribution

| status field | count |
|---|---|
| `verified` (paper-read or canonical-source confirmed) | 9 |
| `theoretical_citation_only` (cited as informational; not load-bearing) | 4 |
| `unverified_paywall_blocked` (paper-read attempt blocked by paywall; documented as such) | 3 |
| `unverified_abstract_only` (abstract-only access; documented as such) | 2 |
| `fidelity_caught_refuted` (claim refuted by paper-read; logged for traceability) | 1 |
| `unverified_book_not_digitized` (Khinchin 1963 book; documented as such) | 1 |
| **Total** | **20** |

### Method-of-verification distribution

| method | count |
|---|---|
| `paper_read_verified` (H8 paper-read) | 6 |
| `tertiary_aggregator` (OEIS / Wikipedia for cross-checks only) | 2 |
| explicit `unverified_*` status (with reason) | 9 |
| theoretical-only / not-load-bearing | 3 |

### `mutation_log/` audit trail

| Quantity | Value |
|---|---|
| Mutation-log entries M1.0 → M6 Step 1 | 12 |
| Mutation-budget consumption at M2 milestone-block | 0 / 1 (still consumed; all 12 entries are field-map updates per H5, not hypothesis mutations) |

The 12 entries: `m1.0_to_m1.1_operator_amendments`, `m1.1_to_m1.2_shortlist_construction`, `m1.2_to_m1.3_brief_fidelity_correction`, `m1.3_pari_gp_install`, `m2.1_to_m2.2_u_mission_j_h8_install`, `m2.2_to_m2.3_pslq_certificate_halt`, `m2.3_u_mission_l_two_tier_predicate`, `m3.2_phase_split`, `m3.2b_u_mission_n_resolution`, `m4_symbolic_closure_gap`, `m5_lean_skeleton`, `m6_step1_bailey_1998_h8_fire`.

| Quantity | Value |
|---|---|
| Surfaced fidelity catches | 4 |
| Concealed fidelity catches (catches known to operator+CLI but not entered into `_fidelity_findings.md`) | 0 |
| Mutation-log entries with audit trail | 12 |
| `claims.jsonl` entries with status field present | 20 / 20 |
| **Literature-fidelity surfacing rate** | **4 / 4 = 100 %** |

**Interpretation.** Every fidelity catch encountered was surfaced as a numbered entry in `_fidelity_findings.md` with a paper-read resolution. Three of the four catches led to a heuristic installation (H8, H9, H10); the fourth (Bailey 1998 H8 fire) surfaced a new finding (D5 "general rule" wording) that strengthened the manuscript's H9 paragraph rather than weakening it. The bidirectional-verification property — H8 applied to operator framing as well as to agent output — is documented in `paper/main.tex` Appendix §B.2 (lines 1034–1049).

---

## Halt-and-flag retrospective

Per `paper/preflight_compliance.md`: 6 mission-life halt events.

| # | Mission stage | Trigger | Heuristic installed |
|---|---|---|---|
| 1 | M1.0 | first-action operator amendments per `_M1.0_first_action_log.md` | (foundational H1-H5 ratified) |
| 2 | M1.1 | target-shortlist overlap audit on E-MEAN / Wieting / Vallée families | H6 (namespace audit on independence scoring) |
| 3 | M1.3 | PARI/GP install-state false positive | H7 (functional verification on capability claims) |
| 4 | M2.1 | `lit-018` "no prior K_0 PSLQ" refuted by paper-read | H8 (paper-read verification on dependency literature claims) |
| 5 | M2.3 | "`H ≈ 10^{P/n}` as theorem" — folklore-grade catch | H9 (theorem-vs-heuristic classification on cited bounds) |
| 6 | M3.2b | first-execution `mpirical_height` float overflow + `H_empirical` ↔ `maxcoeff` semantic question | H10 (full-regime dry-run mandatory before canonical execution) |

| Stage | Halt count |
|---|---|
| M1 | 3 (M1.0, M1.1, M1.3) |
| M2 | 2 (M2.1, M2.3) |
| M3.2b | 1 |
| M4, M5, M6 Step 1, M6 Step 2 drafting | 0 each |
| **Total** | **6** |

**Back-half-running-cleaner property.** M1 + M2 + M3.2b account for all 6 halts; M4 onwards has been halt-free. This is the property the AEAL discipline was designed to produce: early-mission halts install heuristics that prevent later-mission halts.

The M6 Step 2 *pre-commit* rubber-duck pass identified 2 BLOCKER + 4 MAJOR + 4 MINOR findings that were caught and fixed *before* commit; these did not register as halt events because the operator-visible threshold was not crossed. They are noted in `paper/preflight_compliance.md` as "internal review note" rather than as halt-class triggers, consistent with the halt-and-flag definition.

---

## Aggregate health score (single-line summary)

| Axis | Numerator | Denominator | Score | Verdict |
|---|---|---|---|---|
| 1. Claim-to-sweep ratio | 5 claims | 65 candidates | 5 / 65 ≈ 0.077 | conservative (low ratio = good) |
| 2. Reproduce-command coverage | 20 / 20 lit claims + every §3 numerical result | 20 / 20 + every §3 | 100 % | full |
| 3. Capability-gap-documentation rate | 2 gaps documented | 2 gaps encountered | 100 % | full |
| 4. Literature-fidelity surfacing rate | 4 catches surfaced | 4 catches encountered | 100 % | full |
| (auxiliary) Halt-and-flag rate | 6 halts surfaced + 6 heuristics installed | 6 halts encountered | 100 % | full |

**Top-line:** 4-axis health score is at the design ceiling for AEAL-discipline missions (no axis below 100 % on the honesty axes; claim-to-sweep ratio at the conservative end of the band). The single soft observation is the M4 FUNDAMENTAL capability gap, which is a *finding* (not a process failure) — the gap stands because `K_0`'s transcendence status is the major open question in this corner of the literature, not because the mission failed to surface a known resolution.

---

## Source files for re-derivation

If any number in this document is questioned, the source-of-truth chain is:

| Axis | Re-derive from |
|---|---|
| 1 | `paper/main.tex` lines 1052–1066 (claim-to-sweep narrative); `harness/sweep_output/m32b_empirical_sweep.jsonl` (count records); `harness/sweep_output/m32a_primary_cascade.jsonl` (primary record). |
| 2 | `literature/claims.jsonl` (one record per line; grep `"reproduce_command":\s*"[^"]+"`); `paper/main.tex` Appendix A. |
| 3 | `capability/` directory listing (`*.gap.md` for gaps; `*.available.md` for positives). |
| 4 | `literature/_fidelity_findings.md` (numbered Catch entries); `literature/claims.jsonl` (group by `status`); `mutation_log/` directory listing. |
| Halt count | `paper/preflight_compliance.md` ("6-halt-event count"); `methodology/heuristics.md` H6–H10 install-context paragraphs. |

This document is intended to be re-derivable from the repository at `gold/M5` + the in-flight `e0defff` paper-byline amendment. No proprietary state.
