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

- A small (≤ 10 entries) catalog of execution-efficiency aids that **defer**
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

## H8 — Paper-read verification on dependency literature claims

**Intent:** prevent the M2.1-class literature-fidelity error documented in
`literature/lit-018-fidelity-no-prior-k0-pslq-refuted.md` and
`literature/_fidelity_findings.md` Catch #1 — the AI-aggregated web search
that returned both a confident false-negative ("no published K_0-specific
PSLQ null result") AND a confident false-positive (BBC 1997 quoted with a
hallucinated sentence and a DOI off by one digit), both refuted by direct
PDF retrieval of BBC 1997.

**Heuristic (operator wording verbatim, U-MISSION-J 2026-05-15 ~21:00 JST):**

> Any literature claim that the M2.3 success predicate, the M3.1 harness
> design, or the M6 manuscript's scope-distinction story depends on must be
> verified by direct reading of the primary source (paper, preprint,
> supplementary material). Web aggregators, citation databases, and
> LLM-mediated summaries are not sufficient and can produce confident false
> positives in both directions (false existence and false non-existence,
> sometimes both for the same claim). For paywalled or non-digitized
> primary sources, mark `verified_independently: false` with the specific
> blocker and do not propagate the claim into the predicate.

**Sub-rules implied by the operator wording:**

1. **Three dependency targets** define the H8 scope: (a) the M2.3 success
   predicate, (b) the M3.1 harness design, (c) the M6 manuscript's
   scope-distinction story. A literature claim that touches any of these
   three targets is "in the dependency chain" for H8.
2. **Direct primary-source reading** is the required verification mode.
   Acceptable primary sources: the published journal PDF, the publisher's
   canonical HTML render, an author-archived preprint PDF (e.g., from
   `arxiv.org`, `davidhbailey.com`, INRIA HAL), TeX source (with
   author/repo provenance), or supplementary material directly attached to
   the publication.
3. **Insufficient verification modes (H8-rejected):** web aggregator
   summaries (Bing, Google search results pages), citation databases
   (Google Scholar metadata, Semantic Scholar abstracts), tertiary
   encyclopaedias (Wikipedia, MathWorld) when treated as primary, and
   LLM-mediated paper summaries (any AI summarization of a paper without
   verifying against the original).
4. **Confident false positives in both directions** is the named failure
   mode. H8 specifically guards against the AI-aggregator pattern where
   a single query topic can produce both a false-negative ("X does not
   exist") and a false-positive ("X exists and says Y" where Y is
   hallucinated) within minutes. The dual-direction failure is the
   signature of H8-target risk.
5. **Honest paywall / non-digitization** is permitted. If a primary source
   cannot be retrieved (paywall, book not digitized, author-archive
   non-existent), mark `verified_independently: false` in the AEAL
   `independent_verifier_result.method` field with the specific blocker
   (`paywall_blocked`, `book_not_digitized`, `abstract_only_unverified`).
   **Do not propagate the claim into the M2.3 predicate, the M3.1 harness
   design, or the M6 scope-distinction story until the primary source is
   read.** Honest blockage is preferable to propagated unverified claims.

**Scope (operator wording verbatim):**

> Subordinate to Brief §M2.1; sibling to H7. Retroactively binding only on
> entries currently relied on by M2.3 calibration; entries not yet relied
> on may remain in their current verification state until they enter the
> dependency chain.

**Retroactive-binding scope at install:**

The entries currently relied on by M2.3 calibration (per
`literature/_m2.3_calibration_anchor.md` §5) are:

- `lit-001` (Papanokechi 2026 signature paper) — verified, `paper_read_verified`. **H8-compliant.**
- `lit-002` (BBC 1997) — verified, `paper_read_verified` via PDF + pypdf extraction. **H8-compliant.**
- `lit-003` (OEIS A002210) — verified, `oeis_or_tertiary_aggregator_verified` cross-checked against `mpmath.khinchin` at 500 dps. **H8-compliant** (OEIS is the canonical authoritative database for the K_0 numerical-value claim, not a citation aggregator about a paper's content).

All other M2.1 literature entries (lit-004 through lit-017, lit-019,
lit-020) are NOT currently in the dependency chain for M2.3. Per the
operator's retroactive-binding clause, those entries may remain in their
current verification state. If during M3.1 harness design or M6 manuscript
drafting any of those entries enters the dependency chain, an H8
paper-read must be performed at that point.

**Watch-list (`literature/_fidelity_findings.md` §3) maintenance:**

The watch-list of entries flagged as "could enter the dependency chain"
is maintained going forward. Any new H8 paper-read triggered by chain
entry must update both `lit-NNN-<slug>.md` and `_index.md` status fields
and append a brief entry to `_fidelity_findings.md` §1 (new catch) or
§3 (watch-list status update).

**Defers to:** Brief §M2.1 (literature ledger schema and content requirements
— H8 specifies a *verification mode* for the `independent_verifier_result`
field, does not override the Brief's schema). Sibling to H7 (capability
claims) — different problem domain, different mechanism, both binding.

**Sibling to H7, NOT generalization.** H7 covers *functional verification
of capability claims* (does the binary / library actually work?); H8
covers *paper-read verification of literature claims* (does the cited
paper actually say what we are claiming it says?). Different problem
domains, different mechanisms, both binding. Both arose from the same
class of generic failure (confident wrong answer from a surface-level
check) but the mitigations are dissimilar — H7 requires running code, H8
requires reading prose. Listed sequentially because both were added in
the M1→M2 transition cycle. **Neither generalizes the other.**

**Conflict path:** if a Brief amendment specifies a different verification
modality (e.g., a peer-review-style external referee verification on each
load-bearing literature claim), H8 yields to that modality. Log conflict
in `mutation_log/`.

**Forward-binding on M2.2, M3.x, M5, M6:** every new literature claim
introduced after this H8 install date (2026-05-15 ~21:00 JST) that touches
the M2.3 / M3.1 / M6 dependency triad must produce an H8-compliant
verification record (paper-read OR honest blockage flag) before being
committed into the dependency chain.

---

## H9 — Theorem-vs-heuristic classification on cited bounds

**Intent:** prevent the M2.3-class precision-budget error documented in
`harness/precision_budget.md` §7 and `literature/_fidelity_findings.md`
Catch #2 — the H8 paper-read of FBA 1999 revealed that the folklore
relation `H ≈ 10^{P/n}` (which had been quoted as if theorem-grade in
the U-MISSION-K directive's H8 sub-question) is NOT stated as a
theorem in the primary source. FBA 1999 proves Theorem 1, Theorem 3,
and Corollary 2 — distinct, weaker, but still rigorous statements. BBC
1997's empirically-used confidence factor c ≈ 2.06 over the bare
folklore is itself community-validated empirical practice, not
theorem-derived. The same H8 sub-question's framing risk would recur
on any cited quantitative bound whose theorem-grade status was assumed
rather than paper-read-verified.

**Heuristic (operator wording verbatim, U-MISSION-L 2026-05-15 ~21:36 JST):**

> Any claim cited in M2.3 predicate, M3.1 harness, or M6 manuscript must
> carry a `verification_class` in its JSONL entry. Load-bearing classification.

**Four verification classes (operator wording verbatim):**

1. **`rigorous_theorem`** — a stated, proven theorem of the primary source.
   The cited bound is the exact statement of a numbered Theorem in the
   primary source's text. Example: FBA 1999 Theorem 1 statement
   `M_x ≥ 1/max_j |h_{j,j}|`.

2. **`proven_corollary`** — a stated, proven proposition, lemma, or
   corollary of the primary source. The cited bound is a directly
   proven downstream statement, not the bare theorem. Example: FBA
   1999 Corollary 2 statement on iteration count.

3. **`field_standard_practice`** — community-validated empirical methods
   used by the BBC / BBP / Bailey-class experimental-mathematics literature.
   Distinct from agent-derived empirical heuristics: these are methods
   that the field treats as standard (e.g., the H ≈ 10^{P/(c·n)} confidence
   relation with c ≈ 2.06, calibrated empirically across decades of PSLQ
   computations in published Math.Comp. / Experimental Math. papers).
   **Operator strengthening (U-MISSION-L):** this fourth class is distinct
   from `empirical_heuristic` precisely because it carries community
   validation weight. M6 reception in experimental-mathematics venues
   treats `field_standard_practice` claims as default-acceptable; venues
   in pure number theory may not. M6 §Discussion must declare the class.

4. **`empirical_heuristic`** — agent-derived empirical methods (CLI-
   internal observations from running code, scaling rules-of-thumb the
   CLI invented, etc.) that do not have community validation. Lowest
   claim class; must be flagged explicitly in any predicate that uses
   them, and should not be load-bearing on M6 results without explicit
   operator ratification.

**Sub-rules implied by the operator wording:**

1. **Load-bearing rule** is non-discretionary. The three dependency
   targets — M2.3 predicate, M3.1 harness, M6 manuscript — fully define
   the H9 binding scope. Any claim from the M2.1 ledger that enters one
   of those three downstream uses must carry a `verification_class`
   field before the use is committed.

2. **Storage convention.** Per the M2.1 process-to-content rule, the
   `claims.jsonl` 7-field schema is locked and `_schema.md` is a
   one-time scaffold. To honor H9's structural requirement without
   violating the schema lock, `verification_class` is stored as a
   sub-key inside the existing `independent_verifier_result` dict
   (which is a free-form object — only `verified` and `method` are
   validator-checked). The `validate_claims_jsonl.py` validator
   permits arbitrary sub-keys, so no validator change is required.

3. **Class assignment is per-claim, not per-paper.** A single primary
   source can give multiple cited claims at different verification
   classes. Example: FBA 1999 supplies both `rigorous_theorem`
   (Theorem 1's certificate `M_x ≥ 1/max_j|h_{j,j}|`) and the absence
   of any stated `H ≈ 10^{P/n}` theorem — the absence is the source
   of the M2.3 Catch #2. Classes are assigned to the SPECIFIC cited
   statement, not to the paper.

4. **Inheritance rule for harness output claims.** If the M3.1 harness
   produces a confidence claim (e.g., "null PSLQ at P = 2160 dps,
   n = 15, maxcoeff = 10^60") that depends on a literature claim of
   class C, the harness's downstream output inherits class C unless a
   stronger argument is constructed and documented. In particular, a
   `field_standard_practice` empirical input cannot produce a
   `rigorous_theorem` output.

5. **M6 manuscript classification disclosure.** Every quantitative
   confidence claim in M6 must declare its `verification_class` in a
   manuscript table or footnote. Reviewers should be able to inspect
   the predicate's evidence ladder. This is the M6-phase enforcement
   of H9.

**Scope (operator wording verbatim):**

> Subordinate to Brief §M2.3; sibling to H7 (capability-claim functional
> verification) and H8 (literature-claim paper-read verification).
> Forward-binding on M2.3 onward.

**Retroactive-binding scope at install:**

The entries currently relied on by M2.3 calibration that must carry a
`verification_class` at install time:

- `lit-001` (Papanokechi 2026 signature paper) — claim class:
  `field_standard_practice` (the cited scope-distinction passage is a
  standard literature handoff, not a quantitative bound).
- `lit-002` (Bailey-Borwein-Crandall 1997) — multiple claims:
  - The 7350 dps PSLQ null result on K_0 pure powers: `field_standard_practice`
    (community-validated empirical practice; not a stated theorem).
  - The c ≈ 2.06 confidence factor (M2.3 calibration anchor): `field_standard_practice`.
- `lit-003` (OEIS A002210) — claim class: `field_standard_practice`
  (OEIS is the field's canonical numerical-record database).
- `lit-009` (Ferguson-Bailey-Arno 1999) — multiple claims:
  - Theorem 1 (`M_x ≥ 1/max_j|h_{j,j}|`): `rigorous_theorem`.
  - Theorem 3 (overshoot bound): `rigorous_theorem`.
  - Corollary 2 (iteration bound): `proven_corollary`.
  - **Folklore `H ≈ 10^{P/n}`: `field_standard_practice`**
    (Bailey-Borwein-Plouffe / BBC empirical norm; NOT a stated theorem
    of FBA 1999, as paper-read verified per H8 / `_fidelity_findings.md`
    §6 Catch #2).
- `lit-018` (fidelity catch, no prior K_0 PSLQ on the mission's specific
  basis B_D(C)) — claim class: `field_standard_practice` (literature
  fidelity catch documented via paper-reads of lit-001, lit-002).

All other M2.1 entries (lit-004 to lit-008, lit-010 to lit-017, lit-019,
lit-020) are NOT currently in the M2.3 dependency chain. Per the
operator's retroactive-binding scope clause inherited from H8, those
entries may remain without `verification_class` until they enter the
chain.

**Defers to:** Brief §M2.3 (success-predicate definition — H9 specifies a
*classification rule* for the predicate's evidence; does not override the
Brief's predicate content). Sibling to H7 (capability functional
verification — different problem, both binding) and H8 (literature
paper-read verification — different problem, both binding).

**Sibling to H7 and H8, NOT generalization.** H7 covers *functional
verification of capability claims*; H8 covers *paper-read verification of
literature claims*; H9 covers *theorem-vs-heuristic classification of
the verified literature claims when they are cited in load-bearing
contexts*. The three heuristics chain naturally: H7 confirms the
capability runs; H8 confirms the cited paper says what we say it says;
H9 classifies what kind of statement the cited claim IS (theorem vs.
heuristic) for downstream predicate construction. **None generalizes any
other.**

**Conflict path:** if a Brief amendment specifies a different
classification taxonomy (e.g., a peer-review-style external-referee
strength scale), H9 yields to that taxonomy. Log conflict in
`mutation_log/`.

**Forward-binding on M2.3, M3.x, M5, M6:** every new claim citation
introduced after this H9 install date (2026-05-15 ~21:36 JST) that
touches the M2.3 / M3.1 / M6 dependency triad must carry a
`verification_class` in its `independent_verifier_result` sub-key
before being committed into the dependency chain.

---

## H10 — Full-regime dry-run mandatory before canonical execution

**Intent:** prevent the M3.2b-class crash documented in
`literature/_fidelity_findings.md` §7 (Catch #3) and `mutation_log/m3.2b_u_mission_n_resolution_20260516.md`
— `harness/verify.py empirical_height(P=2160, n=2)` overflowed IEEE 754
double on the 10th of 65 candidates after passing all dry-run validation
at P=50/100/200 with no `n=2,P=2160` exercise in any prior smoke-test.
The code path existed but had never been exercised at canonical scale.

**Heuristic.** Any sweep introducing new (P, n, basis_structure, or
other operationally-significant) regions requires a **full-regime
dry-run at canonical precision** before canonical execution. If a
`--m31-extended-dry-run`-equivalent already exists in the codebase, it
MUST be invoked across the full sweep enumeration. If it does not exist
for the new regime, it MUST be built before canonical execution
proceeds.

**What full-regime dry-run means in this mission's harness:**

- Iterates the **full sweep enumeration** (all 65 sub-bases in M3.2's
  case, or whatever the canonical sweep cardinality is) — not a
  3-candidate smoke sample.
- Runs at **canonical precision** (P=2160 dps for the M3.2 cascade
  primary leg) — not at P=50/100/200 dry-run reductions.
- Uses **synthetic-relation or low-`maxsteps` PSLQ** to keep
  wall-clock bounded (a few minutes to ~15 min total) while still
  exercising every code path the canonical sweep will touch at the
  canonical (P, n, maxcoeff_exp) tuple.
- Emits an ungated JSONL clearly marked `dry_run: true`, suitable for
  harness-validation inspection but NOT feeding M6 manuscript claims.

**Insufficient dry-run modes (each can silently false-positive H10):**

- **3-candidate sample.** Catches type errors and trivial logic bugs but
  not regime-specific bugs (overflow at small n, basis-build cold-cache
  costs at large P, gp_lindep timeout at long basis vectors).
- **Single-precision smoke.** Catches arithmetic correctness at one P
  but not behavior across the cascade's full P range.
- **Synthetic basis without small-n.** Catches large-n bugs but misses
  small-n boundary cases like the n=2 pair sub-bases.

**Required form of an H10-compliant pre-canonical dry-run:**

1. Invokes the canonical sweep enumerator (e.g.,
   `harness.basis.enumerate_sub_bases()`) — not a hard-coded subset.
2. Runs at canonical primary precision (the cascade's middle leg is
   acceptable if the highest leg is wall-clock-prohibitive; the dry-run
   inherits H10 from whichever P is canonical for the regime).
3. Produces JSONL with `dry_run: true` in the meta header AND in every
   per-candidate record, so canonical and dry-run outputs are never
   conflated downstream.
4. Surfaces any code-path failure (overflow, timeout, type error,
   subprocess crash, basis build failure) before canonical execution is
   greenlighted.
5. Is invoked explicitly per the canonical sweep's argparse flag (e.g.,
   `--m31-extended-dry-run` for this mission's M3.2 harness).

**Defers to:** Brief §M3.x (canonical sweep execution — H10 specifies a
*pre-execution validation step* but does not override the Brief's
canonical execution structure). Subordinate; does not loosen any Brief
gate.

**Supersedes:** the implicit assumption that the M3.1 `--dry-run` mode
(3 candidates at P=50/100/200) constitutes sufficient pre-canonical
validation for M3.2 (65 candidates at P=2160/4320/8640). H10 makes the
gap between dry-run scope and canonical scope an explicit
verification surface.

**Retroactively binding only on regimes about to be exercised:** the
M3.2a primary cascade at `d55ffbc` (n=15, P=2160) is retroactively
H10-compliant via M3.2a's own clean-null outcome plus its match with
M2.3 §6 wall-clock benchmark coverage at canonical P. The M3.2b sweep
is NOT retroactively H10-compliant — the U-MISSION-N resolution
explicitly mandates a `--m31-extended-dry-run` pass at canonical
precision across all 65 sub-bases before the M3.2b canonical re-run.

**Forward-binding on every subsequent milestone introducing a new
sweep regime:** before any canonical execution that introduces a new
(P, n, basis_structure) region, a full-regime dry-run at canonical
precision is mandatory. Examples in the upstream pipeline: any M4
extension sweep that broadens D or |C|; any M5 Lean-formalization
batch that introduces a new compile-target regime; any M6 manuscript
re-verification sweep that retargets a specific n / P combination.

**Conflict path:** H10 does not override a Brief gate that explicitly
authorizes canonical execution without a dry-run prerequisite (none
currently exists in the Brief). If a future Brief amendment specifies
a different pre-execution validation modality (e.g., a formal-methods
proof of harness correctness), H10 yields to that modality. Log
conflict in `mutation_log/`.

**Sibling to H7, NOT generalization.** H7 covers *functional
verification of capability claims* (does the binary / library actually
work as claimed?); H10 covers *full-regime pre-canonical exercise of
the harness* (does the existing code path actually work at canonical
scale across the full sweep enumeration?). Different problem domains:
H7 catches "tool isn't installed but name resolves"; H10 catches "code
path exists but hasn't been exercised at canonical scale". Different
mechanisms: H7 requires running a tool's minimal example; H10 requires
running the harness's full enumeration at canonical (P, n, basis)
tuples with low-wall-clock synthetic load.

**Forward-binding on M3.2b canonical re-run (immediate):** the
post-U-MISSION-N M3.2b canonical re-run is gated on a successful
`harness/sweep.py --m31-extended-dry-run` pass at P=2160 across the
full 65-sub-basis enumeration. The dry-run must complete with zero
overflows, zero crashes, and zero unexpected verification_class
assignments before `--full --m32-full-greenlighted` is re-authorized.

---

## H11 — Class-of-error exhaustive propagation on bundled fixes

**Intent:** prevent the M6-layer-3-class partial-fix-propagation pattern
documented in the commit transition `8ac5bcf` → `979c613` — the M6
manuscript bundle at `8ac5bcf` displayed the BBC empirical-height formula
as `c · 10^{P/(c·n)}` (residual leading `c`) at seven distinct typeset
locations in `paper/main.tex` plus one substitution-prefix occurrence plus
one paired prose phrase, even though every numerical claim downstream
(`H_emp^op ≈ 7.997 × 10^69`, capping inactive at `n = 15`, threshold check
`n ≈ 14.97` at `10^70`) had already been computed under the corrected
`10^{P/(c·n)}` form. The operator-self-review's Check 2 surfaced six of
the seven leading-`c` sites; an independent-pass (rubber-duck) review
flagged the seventh (`paper/main.tex` line 519 in the §2.5 capping
clause) before the layer-3 commit fired. Without an exhaustive-
propagation discipline, the natural failure mode is "fix the first
occurrence noticed, commit, ratify, then the same class-of-error
resurfaces under later scrutiny at sibling sites."

**Heuristic.** Once a class-of-error pattern is identified at any single
site in an AEAL-bound artifact, the fix-site enumeration MUST be
exhausted **before** the fix bundle is committed — every sibling-class
site of the same error must be either fixed in the same commit or
explicitly catalogued (with rationale) as a deliberate exception.
Partial propagation that addresses only the operator-noticed instances
and leaves sibling-class sites untouched violates H11.

**What exhaustive propagation means in this mission's repository:**

- **Enumerate the class.** Define the error pattern precisely (e.g., for
  the M6 leading-`c` case: "any displayed-math occurrence of
  `c \cdot 10^{P/(c·n)}` in `paper/main.tex`, including substitution
  prefixes and paired prose paraphrases such as 'leading constant
  c ≈ 2.06'").
- **Repository-wide grep.** Run a grep with the class pattern as a
  regex across the full artifact set (`paper/main.tex`,
  `methodology/*.md`, `handoff/*.md`, `claims/*.jsonl`, capability
  records — whatever artifact set the error class could plausibly
  appear in). Include near-miss variants in the regex (different
  spacings of `\cdot`, paraphrased prose, alternative notation).
- **Sibling-site verification.** For each grep hit, decide: fix in the
  current commit, OR catalogue as a deliberate exception with rationale
  recorded in the commit message.
- **Independent-pass review.** Before commit, request an independent
  enumeration pass (rubber-duck agent, or a second operator-self-review
  at a different abstraction level) specifically scoped to "did the
  first-pass enumeration miss any sibling sites?" In the M6 layer-3
  case, this caught one missed site out of seven.

**Insufficient propagation modes (each silently false-positives H11):**

- **Operator-spotted-only fix.** The operator notices the error at one
  location, points it out, the fix is applied there alone, and the same
  error class persists at unnoticed sibling sites.
- **Single-grep-pattern-only fix.** A literal-string grep for one
  phrasing misses paraphrased or near-miss variants (e.g., grepping for
  `c \cdot 10` would miss `c\cdot 10` without space, or a prose phrase
  like "leading constant c ≈ 2.06").
- **Compile-clean-equals-fix-complete.** PDF or build compiling cleanly
  after the first-pass fix proves only that the artifact is well-formed,
  not that the class-of-error is fully eliminated. A residual occurrence
  at a sibling site still compiles cleanly.
- **Manual-scan-without-programmatic-enumeration.** Eyeballing the
  artifact for the error class scales poorly past a few sites; the
  M6 layer-3 case had ≥ 7 sites where manual scanning would predictably
  miss at least one.

**Required form of an H11-compliant fix bundle:**

1. **Class-pattern statement** in the commit message: a precise
   description (or regex) of the error class the bundle addresses.
2. **Enumeration evidence**: line numbers (or equivalent locator
   identifiers) for every sibling site touched by the bundle.
3. **Grep transcript** (in the commit message, the SQL todo description,
   or attached evidence): the pre-commit grep output proving zero
   residual sibling-class matches in the bundle's scope, OR a catalogue
   of deliberate exceptions with rationale.
4. **Independent-pass evidence**: a record that a rubber-duck or
   second-pass review specifically asked "did this enumeration miss any
   sibling sites?" before commit, with the answer documented.

**Defers to:** Brief §M6.2 (manuscript bundle structure — H11 specifies
*how to construct* a layer-N revision bundle but does not override the
Brief's gate structure for layer transitions). Subordinate; does not
loosen any Brief gate.

**Supersedes:** the implicit assumption that a fix is complete when the
operator-noticed sites are addressed. The M6 layer-3 bundle demonstrates
that operator-noticed sites are a *subset* of sibling sites in a
class-of-error, not the full set; H11 makes the gap an explicit
verification surface.

**Retroactively binding on the M6 layer-3 bundle commit `979c613`:**
the bundle was constructed in H11-compliant form ahead of H11's formal
installation — the commit message enumerates all nine edits with file
locations, a post-commit grep transcript was logged (zero residual
`c \cdot 10` or `c\cdot 10` matches in `paper/main.tex`), and the
rubber-duck pass that caught line 519 is documented in this session's
state. H11's formal installation is therefore a *codification* of the
practice already exercised in the bundle, not a new requirement imposed
retrospectively.

**Forward-binding on every subsequent layer-N revision bundle and every
class-of-error fix in any AEAL-bound artifact:** the four-element form
above (class-pattern statement, enumeration evidence, grep transcript,
independent-pass evidence) is mandatory in the commit message (or in a
linked SQL todo description) for any fix bundle that addresses a
class-of-error pattern at ≥ 2 sites. Single-site fixes are exempt from
H11's required form but still benefit from its discipline (a
repository-wide grep takes seconds and catches the case where the
"single site" was actually two or more sites all along).

**Conflict path:** H11 does not override a Brief amendment that
explicitly authorizes single-site fixes without exhaustive propagation
(none currently exists). If a future amendment specifies a different
propagation modality (e.g., automated refactor tools with proven
soundness over the artifact set), H11 yields to that modality. Log
conflict in `mutation_log/`.

**Sibling to H7 and H10, NOT generalization.** H7 covers *functional
verification of capability claims*; H10 covers *full-regime pre-canonical
exercise of the harness*; H11 covers *exhaustive propagation of
class-of-error fixes across sibling sites in an artifact*. Different
problem domains: H7 catches "tool isn't installed but name resolves";
H10 catches "code path exists but hasn't been exercised at canonical
scale"; H11 catches "fix applied at one site but the same class-of-error
persists at sibling sites due to incomplete propagation." Different
mechanisms: H7 requires running a tool's minimal example; H10 requires
running the harness's full sweep enumeration at canonical scale with
low-wall-clock synthetic load; H11 requires running a repository-wide
grep on the error class's pattern (with near-miss variants in the
regex) plus an independent-pass review before commit.

**Installation event:** the operator-self-review on M6 bundle commit
`8ac5bcf` (six-check sweep, Check 2 surfaced two findings); the layer-3
bundle at `979c613` repaired the leading-`c` class-of-error at seven
typeset sites in `paper/main.tex` plus one substitution-prefix
occurrence at line 695 plus one paired prose phrase at lines 434–435.
H11 is installed mid-M6 because the rhetorical framing "eleven
heuristics, the last installed in response to a class-of-error
propagation pattern the mission itself demonstrated" carries the
methodological discipline of AEAL more honestly than a deferred-to-
successor-paper closing.

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
false positives (e.g., PowerShell-alias shadows on binaries). H8 directly
bears on a fourth, M2-emergent axis: **literature-fidelity honesty.** It
converts AI-aggregator summary probes into paper-read probes, eliminating
the dual-direction false-positive failure mode (confident false existence
+ confident false non-existence within the same query topic) that surfaced
as Catch #1 in `literature/_fidelity_findings.md`. H9 extends the
literature-fidelity axis with a **theorem-vs-heuristic classification**
layer (four `verification_class` values: `rigorous_theorem`,
`proven_corollary`, `field_standard_practice`, `empirical_heuristic`),
preventing the implicit theorem-grading of folklore relations that
surfaced as Catch #2. H10 bears on a fifth, M3-emergent axis:
**code-path-exercise honesty.** It catches "code path exists but
hasn't been exercised at canonical scale" — the failure mode that
surfaced as Catch #3 (`empirical_height(P=2160, n=2)` IEEE 754
overflow) when the M3.1 3-candidate dry-run at P=50/100/200 silently
passed validation while the canonical M3.2b sweep at P=2160 across
n∈{2,3,8,9,15} crashed on the 10th of 65 candidates. H10 is sibling
to H7: H7 is "the tool works"; H10 is "the harness works across the
full regime it claims to support".
