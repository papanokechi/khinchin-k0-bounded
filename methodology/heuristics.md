# methodology/heuristics.md — Informal Aids, Subordinated to AEAL

**Status.** This file is a small set of operational heuristics for execution
efficiency within Mission Brief constraints. It is **NOT** an amendment to the
Brief and **NOT** a rule set.

**Authority hierarchy.** Mission Brief §0–§9  >  AEAL seven-field claim schema  >
**These heuristics.**

**Conflict resolution.** If a heuristic conflicts with the Brief or with AEAL,
**the Brief / AEAL wins** automatically. Any conflict event encountered during
execution MUST be logged in `mutation_log/` with the offending heuristic, the
authority that overrode it, and the resolution.

**Operator-issued scope** (2026-05-15 ~18:16 JST, in declining the "embedded
AI-breakthrough logic" framing):

- ≤ 2 pages.
- Subordinated frame mandatory.
- No "structural gaps", "forced invariants", "consistency-driven conjecture
  generation", or other unfalsifiable mechanisms-of-discovery framing.
- Heuristics, not rules.

---

## What this file is NOT

- NOT a rule set (the Brief is the rule set).
- NOT a license to loosen AEAL constraints.
- NOT a substitute for the seven-field claim schema (`id`, `statement`,
  `evidence_class`, `precision_or_dependencies`, `reproduce_command`,
  `independent_verifier_result`, `status`).
- NOT a source of breakthrough-prediction logic or non-AEAL inference rules.

## What this file IS

- A small (≤ 7 entries) catalog of execution-efficiency aids that **defer**
  to the Brief on every load-bearing decision.

---

## H1 — PSLQ cascading-precision triage

**Intent:** decide quickly whether a candidate relation merits the cost of the
full M3.1 cascading-precision check (which can consume significant wall-clock).

**Heuristic.** At base precision N dps, when PSLQ returns a candidate
relation with coefficient max-magnitude C_max:

- If `C_max < 10^(N/4)`: PROCEED to 2N dps re-verification (likely-true regime).
- If `10^(N/4) ≤ C_max < 10^(N/2)`: flag as **height-precision marginal**; still
  run 2N dps but ALSO log the coefficient growth ratio in `claims/<id>.json`
  under the `precision_or_dependencies` field.
- If `C_max ≥ 10^(N/2)`: treat as **likely false positive** at this precision;
  do NOT escalate to 2N dps; document in the candidate's `claims/` entry as
  `status: refuted (height-precision overshoot at N=...)`.

**Defers to:** Brief §M3.1 cascading-precision check. The precision-doubling
schedule (N → 2N → 4N) is **Brief-mandated**; H1 only specifies an *entry
condition* on the schedule.

**Conflict path:** if Brief §M3.1 is revised to mandate the cascade regardless
of coefficient magnitude, H1 is overridden. Log in `mutation_log/`.

---

## H2 — Literature-ledger prioritization for M2.1

**Intent:** populate `literature/claims.json` to the Brief §M2.1 minimum of
15 entries with the highest-information-density set.

**Heuristic.**

- **Primary tier (count toward 15 with `verified_independently=true`):**
  papers with a stated theorem about the target constant AND either a
  computational record reproducible in the M3.1 harness OR a transcendence-
  theoretic technique applicable to PSLQ-detection rejection. Operator must
  have read the paper in full.
- **Secondary tier (count toward 15 with `verified_independently=false`):**
  papers cited by a primary-tier paper but not independently read; entry is
  permitted but the flag must be honest.
- **Excluded (do NOT count toward 15):** survey papers without new technique;
  pure expository accounts; blog posts; AI-generated summaries; abstracts
  not backed by a read of the full paper.

**Defers to:** Brief §M2.1 minimum-15 + the `verified_independently` honesty
flag. H2 only specifies the *tier definitions*; the count and flag are
Brief-mandated.

---

## H3 — Stall-diagnostic timing within Brief §M3.2

**Intent:** structure the 8-hour stall window so the `stall_diagnostic.md`
deliverable is actually ready when the cap fires, rather than scrambled-
together at hour 8.

**Heuristic.**

| Window (h since last verified claim) | Action |
|---|---|
| 0–4 | Normal execution. No diagnostic action. |
| 4–6 | If iteration rate has dropped > 50% from baseline (t=0), BEGIN drafting `stall_diagnostic.md`. **Do not commit the draft yet.** |
| 6–8 | If still no new verified claim, FINALIZE the draft. Document the hypothesis class that stalled, the precision regime, the iteration cap reached. |
| ≥ 8 | **STOP** per Brief §M3.2. Commit `stall_diagnostic.md`. No further computation. No retry without operator-approved `mutation_log/` entry. |

**Defers to:** Brief §M3.2 hard 8-hour stall cap and 96h wall-clock budget.
H3 only structures the *drafting cadence*; the STOP at 8h is Brief-mandated
and non-negotiable.

---

## H4 — Capability-gap escalation discipline

**Intent:** ensure no missing-machinery problem is silently substituted by a
sweep, per Brief §0.2 and operator U-MISSION-D declination.

**Heuristic.**

- If a milestone step requires arb / flint interval arithmetic or
  fpylll-class LLL, and `gp lindep` shell-out cannot substitute:
  1. Write `capability/<technique>.gap.md` per Brief §M2.2 schema.
  2. STOP that step. Do not redirect compute to a different hypothesis
     within the same step (that would be Searcher's-Fatigue substitution
     of one sweep for another).
  3. Per U-MISSION-D: do **NOT** attempt to install the missing tool
     retroactively. The capability gap is the deliverable for that step.
- If two *consecutive* milestone steps produce capability gaps, the mission
  TERMINATES at the second gap (Brief §7 anti-thrashing rule). The negative
  result + the two capability audits IS the mission deliverable.

**Defers to:** Brief §0.2 + §7 + operator U-MISSION-D directive.

---

## H5 — Mutation-log entry discipline

**Intent:** keep within Brief §7's "one hypothesis mutation per milestone"
budget while distinguishing genuine mutations from boundary directives.

**Heuristic.**

- **Counts as a mutation:** any in-milestone change to the bounded
  sub-question, the success predicate, the hypothesis class being explored,
  or the precision/iteration caps.
- **Does NOT count as a mutation:** operator-issued directives received at
  milestone boundaries (precedent: `m1.0_to_m1.1_operator_amendments_20260515.md`
  and `m1.1_to_m1.2_shortlist_construction_20260515.md`, both 0-mutation in-
  milestone events).
- **U-MISSION-F's refinement allowance** (M2.1 literature can refine the
  K_0 sub-question): a *tightening* refinement (smaller D, smaller H, same
  question shape) does NOT count; a *scope-changing* refinement (different
  ansatz class, different verification harness, different success predicate
  shape) DOES count and requires a `mutation_log/` entry.
- **Brief-fidelity corrections** (factual errors in the Brief itself, e.g.
  reference to a non-existent repo) are **frame corrections, NOT mutations**.
  They get a `mutation_log/` entry for traceability but do NOT consume the
  one-mutation-per-milestone budget (precedent: U-MISSION-G resolution
  2026-05-15 18:45 JST; entry
  `m1.2_to_m1.3_brief_fidelity_correction.md`).

**Defers to:** Brief §7 one-mutation-per-milestone cap; U-MISSION-F
refinement clause in `targets/selected.md` §5.

---

## H6 — Namespace audit on independence scoring

**Intent:** prevent the M1.2-class process miss documented in
`targets/overlap_audit_khinchin_signature_pslq_prior_work.md` §6 — the
M1.2 I (independence) axis was scored against the active R1 / Painlevé III
queue only, missing the operator-prior-work overlap with
`papanokechi/khinchin-signature-pslq` (Apr 2026, same machinery class).

**Heuristic.** At any milestone where an independence / non-overlap score
is computed (M1.2 selection, M2.2 capability audit, M5 formalization
scope, M6 venue selection), a *namespace audit* MUST be performed as a
default check before the score is finalized. The namespace audit covers
three layers:

1. **GitHub repo namespace.** `gh repo list <operator> --limit 100`,
   then grep the repo names + descriptions for target-keyword family
   terms (constant name, technique name, machinery class).
2. **Manuscript / preprint namespace.** Operator's submitted-manuscripts
   directory listing (if exposed), arXiv author search, Zenodo deposit
   listing, Scholar author profile — grep for target-keyword family terms.
3. **Active-queue namespace.** Operator's stated active work queue (e.g.,
   the R1 / Painlevé III chart-map closure, the JNT Item 28 referee thread,
   any other in-flight submissions). This is the only layer that was
   actually checked at M1.2; layers 1 and 2 were missed.

If any of the three layers returns a non-empty hit, an
`overlap_audit_<finding>.md` MUST be written (same shape as
`targets/overlap_audit_26_gauss_kuzmin.md` or
`targets/overlap_audit_khinchin_signature_pslq_prior_work.md`) BEFORE
the independence score is committed. The audit must verdict each
3-axis dimension (content overlap, machinery overlap, attribution
muddiness) and recommend an Option A/B/C/D-class disposition.

**Effective immediately and retroactively binding on M2 onward**
(operator directive, U-MISSION-G resolution 2026-05-15 18:45 JST).
Retroactive scope: any M2+ step that introduces a new independence /
non-overlap decision must run the namespace audit before committing
the decision. M1.2's selection of Khinchin K_0 is grandfathered (the
audit was retroactively run via U-MISSION-G; outcome was a §5.A
refinement of `selected.md`).

**Defers to:** Brief §M1.2 independence-from-R1 framing (extends, does
not replace); Brief §M2.2 capability audit schema; Brief §M5
formalization scope; Brief §M6 venue selection. Heuristic does not
authorize loosening the independence requirement; it adds a *check*
that the requirement is actually being applied to the full namespace.

**Conflict path:** if a future Brief amendment restricts the audit to
only the active-queue layer (i.e., declares layers 1–2 out of scope),
H6 is overridden. Log in `mutation_log/`.

---

## H7 — Functional verification on capability claims

**Intent:** prevent the M1.3-class probe-false-positive documented in
`mutation_log/m1.3_pari_gp_install_20260515.md` — the 17:38 JST capability
probe recorded PARI/GP as "binary FOUND on PATH" based on `Get-Command gp`
resolving to a PowerShell built-in alias (`gp -> Get-ItemProperty`), not
to an actual `gp.exe` binary. Name resolution alone is insufficient
evidence; functional verification is required.

**Heuristic.** Any `capability_available` claim — whether in
`capability/<technique>.available.md`, `capability/probe_results_*.md`, or
inline in a `claims/<id>.json` `precision_or_dependencies` field — MUST be
backed by a **minimal working example that exercises the specific function
the harness will use**, NOT by a name-resolution check.

Name-resolution-class probes that are INSUFFICIENT under H7 (each can
silently false-positive):

- **PowerShell aliases.** `Get-Command gp` returns the built-in alias
  `gp -> Get-ItemProperty` regardless of whether PARI/GP is installed.
  Other PowerShell aliases that shadow real binaries: `curl -> Invoke-WebRequest`,
  `wget -> Invoke-WebRequest`, `diff -> Compare-Object`, `tee -> Tee-Object`,
  `where -> Where-Object`, `cat -> Get-Content`, `ls -> Get-ChildItem`, etc.
- **Shell builtins.** Bash builtins like `time`, `which`, `type` may resolve a
  name without exec'ing a binary.
- **Dead symlinks.** Symlinks to deleted targets still satisfy `Test-Path`-like checks.
- **Stub binaries.** Installers sometimes drop a stub `.exe` that prints
  "please install component X" — passes existence but fails functional use.
- **Python import success without functional use.** `import sympy` succeeds
  even if a specific submodule needed by the harness is broken; the
  minimal example should exercise the specific function.

**Required form of an H7-compliant capability record:**

`capability/<technique>.available.md` must include:

1. **Binary path or version string** identifying which specific install is being claimed.
2. **At least one minimal working example** that exercises the specific function
   the harness will rely on (e.g., for PARI/GP: a `lindep` call returning a
   verifiable integer-relation vector; for mpmath: a 500-dps `pi` evaluation
   matching official digits; for Lean: a `--version` plus a tiny compile or
   reference to an existing successful build).
3. **The verification date** (when the minimal example was last run).
4. **A reproduce command** that the operator (or a future reader) can re-run
   to confirm the capability is still working.

**Defers to:** Brief §M2.2 (capability audit schema — H7 specifies the *minimum
content* of each capability/*.available.md file but does not override the
Brief's structural requirements). Subordinate; does not loosen Brief §M2.2.

**Supersedes:** the implicit assumption in U-MISSION-D and in
`capability/probe_results_20260515.md` v1 that name resolution constitutes
verification. The v1 record's PARI/GP row is now §AMENDED-flagged as a
false positive caught by H7.

**Retroactively binding on `capability/probe_results_20260515.md`:** every
v1 row claiming a capability is present has been re-verified per H7 in the
audit window 2026-05-15 19:15–19:30 JST. Records: `capability/mpmath.available.md`,
`capability/gmpy2.available.md`, `capability/numpy.available.md`,
`capability/sympy.available.md`, `capability/lean_lake.available.md`,
`capability/mathlib4.available.md`, `capability/pari_gp.available.md`. The
v2 probe record is at `capability/probe_results_20260515_v2.md`.

**Forward-binding on Brief §M2.2 capability audit:** every new capability
claim made during the M2.2 audit (or any subsequent milestone where a
capability is asserted available) must produce an H7-compliant
`capability/<technique>.available.md` file before the audit step is
considered complete.

**Conflict path:** H7 does not override Brief §M2.2's required schema; it
adds a *content* requirement (minimal working example) on top of the
Brief's schema. If a Brief amendment specifies a different verification
modality (e.g., a formal-methods proof of capability), H7 yields to that
modality. Log conflict in `mutation_log/`.

**Sibling to H6, NOT generalization.** H6 covers *independence audit on
the operator-namespace*; H7 covers *functional verification of capability
claims*. Different problem domains, different mechanisms, both binding.
Listed sequentially because both were added by U-MISSION-G/H resolutions
in the same M1.3 freeze cycle. Neither generalizes the other — H6 audits
the *negative* (no prior overlap), H7 verifies the *positive* (the
capability actually works).

---

## Conflict log

| Date | Heuristic | Conflicting authority | Resolution | mutation_log ref |
|---|---|---|---|---|
| — | — | — | — | — |

*(Empty at file creation. Future conflict events append here AND get a full
entry in `mutation_log/`.)*

---

## Three-axis Agent Health Score notes (per Brief §0.4)

These heuristics support but do not replace the three-axis score:

- **(a) Claim-to-sweep ratio:** H4 directly supports by forcing capability-gap
  documentation in place of sweep-substitution.
- **(b) Reproduce-command coverage:** H2 supports by requiring
  reproducibility of primary-tier literature entries.
- **(c) Capability-gap honesty:** H4 enforces honest documentation.

H1, H3, H5 are execution-cadence heuristics that do not directly bear on the
three-axis score but reduce the risk of score-degradation through process
errors (cascading-precision overshoot, stall-draft-scramble, mutation-budget
overspend). H6 directly bears on the **independence** scoring component of
the M1.2 (and any M2+ analogue) decision — it adds a namespace-audit check
that the independence requirement is actually being applied to the full
operator namespace, not just to the active-queue subset. H7 directly bears
on the **capability-gap honesty** axis — it converts name-resolution probes
into functional-verification probes, eliminating an entire class of silent
false positives (e.g., PowerShell-alias shadows on binaries).
