# Agent Health Score — methodology

**Purpose.** Specify the four-axis Agent Health Score numerator / denominator definitions, the principles each axis encodes, and the machine-checkable procedure for re-deriving each value from the repository at any point in a mission's lifecycle.

**Relation to other files.**

- `handoff/agent_health_score.md` is the *concrete-data* view: it carries the actual M6 values (5/65, 20/20, 2/2, 4/4) computed from this mission's `gold/M5`-plus-`e0defff` state.
- This file is the *methodological substrate* for that document. The values in `agent_health_score.md` are re-derivable using the recipes here.
- `paper/main.tex` §Appendix B (lines ~1050–1066) is the *prose-summary* surface that reports the score in the manuscript.
- For the AEAL methodology paper that may follow this mission's Zenodo deposit, this file is the canonical definitional reference; the four axes here are framed for re-use across SIARC missions, not for one-shot M6 application.

**Audit-replicability invariant.** Every numerator and denominator below is computable by a non-author auditor with access to the repository at a specific tag, using only standard CLI tools (grep, jq, ls, wc, git). No author judgment enters except where explicitly flagged as honest-self-assessment input (Axis 3 suspected-gap term).

---

## Common preliminaries

**Scope of an Agent Health Score computation.** A score is computed against a *mission state* — a (repository, tag-or-commit) pair. The recommended snapshot points are the gold tags: `gold/M1` through `gold/M(N)` where `N` is the closure milestone. The score may also be computed at an intermediate commit for in-flight diagnostics; in that case the commit hash and the JST timestamp are reported as part of the snapshot identifier.

**Snapshot identifier conventions.**

```
snapshot: {repo}@{tag-or-commit} [{JST timestamp if not tag-level}]
```

Example: `papanokechi/khinchin-k0-bounded@e0defff [2026-05-16 13:32 JST]`.

**Score-line format.** Each axis reports as:

```
Axis N: <numerator> / <denominator> = <ratio> [target = <target>, direction = <higher-or-lower-is-better>]
```

**Aggregate verdict.** No collapse to a single scalar. The four axes are reported and interpreted independently; an honest score with mixed verdicts (e.g., 100% on three axes and a low-ratio on Axis 1) is preferred to a synthetic combined number that obscures the trade-offs.

---

## Axis 1 — Claim-to-sweep ratio

### Definition

```
Axis 1 = (number of manuscript-level claims) / (number of sweep tests run in support)
target: low (≪ 1)
direction: lower is better
```

### Numerator: what counts as a manuscript-level claim

A *manuscript-level claim* is a single load-bearing assertion that the manuscript's §Results or §Discussion makes about the empirical or theoretical state of the world. The unit is "what the abstract would lose if this assertion were redacted."

A claim is manuscript-level iff **all** of the following hold:

| Criterion | Concrete check |
|---|---|
| Asserted in §Results or §Discussion (not §Methods, not §Appendix) | `paper/main.tex` section-header scan. §Methods describes the apparatus; §Appendix replicates; only §Results and §Discussion carry claims. |
| Cited by the §Abstract or by the §Introduction's contribution paragraph | If the claim is not surfaced in §Abstract or §Introduction-contribution, it is *supporting* (counted toward denominator if it is also a sweep-test record), not *claim-level*. |
| Carries a precision class — one of `proven_corollary`, `field_standard_practice`, `documented_capability_gap`, `empirical_observation` — under the H9 verification-class taxonomy (`literature/_m2.3_calibration_anchor.md` §7.7) | The precision class must be the claim's *own* class, not inherited from a citation. |
| Survives a precision-class downgrade test: would the abstract still cite this claim if its precision class were reduced one tier? If yes, it is claim-level. If no, it is sweep-level. | Author judgment, but recorded with rationale in `paper/preflight_compliance.md`. |

**Counting rule.** Each manuscript-level claim is counted *once*, even if it is restated in multiple §Results paragraphs. A claim with two-tier reporting (e.g., a rigorous bound paired with an empirical bound) is **two** claims if both tiers are individually load-bearing in the abstract; **one** claim if only the joint two-tier statement is load-bearing.

### Denominator: what counts as a sweep test

A *sweep test* is a single record in the canonical sweep output that contributes evidence toward a claim. The unit is "one row of an evidence-bearing JSONL file."

A record counts iff **all** of the following hold:

| Criterion | Concrete check |
|---|---|
| The record lives in a file under `harness/sweep_output/` or `M5/` (Lean) or `capability/_*_probe.py`-output that is committed at the snapshot tag | `git ls-tree -r <tag> -- harness/sweep_output/` lists the file |
| The record's precision tier is at least the working-precision floor declared in `harness/precision_budget.md` | one-off low-precision probes do not count as sweep records |
| The record's JSONL row has a non-empty `sub_basis` / `template` / `family` field (i.e., the row identifies *what* was tested, not just that the test ran) | jq filter: `select(.sub_basis != null and .sub_basis != "")` or analogous schema-specific filter |
| The record was generated by a canonical-tier execution (`H10`-dry-run-cleared, with a corresponding entry in `_audit_*.md`) | grep `mutation_log/` for the corresponding canonical-execution audit entry |

**Independent-leg corroboration.** A `mpmath`-leg record and a PARI/GP `lindep`-leg record on the same sub-basis count as **two** denominator units. The two legs are *independent* verifications and the denominator is meant to capture the breadth of evidence brought against each claim.

**Cascade records.** A primary-cascade record at (P, 2P, 4P) precision counts as **one** denominator unit per precision tier (i.e., three units for a 3-tier cascade), unless the cascade is bit-for-bit redundant by H10 design — in which case it counts as one. This is the only case where author judgment enters the denominator; the rationale must be recorded in `paper/preflight_compliance.md`.

### Why low ratios are good — the consolidation principle

The Agent Health Score's Axis 1 is the only axis where a *low* numerator-to-denominator ratio is the desirable direction. The intent is to surface the *consolidation* principle: a manuscript is in good calibration when its claim graph is much narrower than its evidence graph. Concretely:

1. **Failure mode penalty.** The opposite failure mode — many claims, few sweep records — is the classical *over-generalization* pathology where a manuscript reads "we have shown that [strong general statement]" while the underlying empirical population is too small to support the generality. A high Axis 1 ratio (claims ≈ records) signals exactly this pathology.
2. **Conservation principle.** When a mission discovers a stronger empirical fact than the abstract claims (e.g., a null result over 65 sub-bases when the manuscript only claims a null at the primary `B_D(C)`), the *honest* response is to keep the abstract narrow and report the broader null as supporting evidence in §Results / §Discussion. This *narrows* the claim and *broadens* the support — pushing the ratio down.
3. **Replicability anchor.** A low ratio means each claim is anchored to a wide replication base. An auditor can pick any one of the 65 sweep records, re-run it, and check that the claim still holds against that specific record. With a high ratio, no such replication test exists for most claims.

### Machine-checkable procedure

```bash
# Numerator: count manuscript-level claims
git show <tag>:paper/main.tex | \
  grep -E '^(\\section\*?{|\\subsection\*?{).*(Results|Discussion)' | \
  # then manually identify claims meeting all 4 criteria, recording in paper/preflight_compliance.md
  
# Denominator: count sweep records
for f in $(git ls-tree -r <tag> -- harness/sweep_output/ | awk '{print $4}'); do
  git show <tag>:$f | jq -c 'select(.sub_basis != null and .sub_basis != "")' | wc -l
done | awk '{s+=$1} END {print s}'
```

### Reporting requirements

The §Appendix B paragraph quoting Axis 1 must:

- State the numerator and denominator as integers (not as a decimal ratio alone).
- Cite `harness/sweep_output/` JSONL filenames and their record counts.
- Cite `paper/preflight_compliance.md` for the manuscript-level claim list.
- Acknowledge the *consolidation interpretation* explicitly — i.e., that the low ratio is the desirable direction, not a sign that the manuscript is light on results.

---

## Axis 2 — Reproduce-command coverage

### Definition

```
Axis 2 = (claims with non-empty reproduce_command field) / (total claims in literature ledger)
target: 100%
direction: higher is better
```

### Numerator

`literature/claims.jsonl` entries where the `reproduce_command` field is present and non-empty. The exact jq filter:

```bash
jq -c 'select(.reproduce_command != null and .reproduce_command != "")' \
  literature/claims.jsonl | wc -l
```

A `reproduce_command` is non-empty iff it is a string of length ≥ 1 character that, when executed (or visited as a URL), would let a future reader retrieve the same artifact the original claim was based on. The `literature/_schema.md` enumerates acceptable patterns:

| Pattern | Example |
|---|---|
| `Invoke-WebRequest -Uri <URL> -OutFile <local>` | for primary-paper PDFs hosted on author or repository archives |
| `https://doi.org/<DOI>` or `https://oeis.org/<sequence>` | for DOI-anchored sources and OEIS sequences |
| `python <script.py>` or `gh api repos/...` | for computational artifacts |
| `Cite as standard reference; consult <publisher> <year> ISBN <ISBN>` | for books not digitized |
| `Invoke-WebRequest -Uri ... -OutFile <file>; Get-FileHash <file> -Algorithm SHA256` | required when the cited artifact is load-bearing on a `proven_corollary`-class claim (H8 paper-read SHA-256 binding) |

An empty `reproduce_command` would surface as a JSON `null`, an empty string, or a string containing only whitespace.

### Denominator

Total `claims.jsonl` line count (one claim per line):

```bash
wc -l literature/claims.jsonl
```

### Why 100% is the target

Every literature citation enters the manuscript with an implicit promise: *this claim about prior work can be checked*. The `reproduce_command` field operationalizes that promise. An entry without a `reproduce_command` is an unfalsifiable citation: a future reader cannot independently retrieve the artifact the claim is based on. Such entries fail the H7 functional-verification principle as applied to literature.

The 100% target is not aspirational; it is enforced at validator time: `literature/validate_claims_jsonl.py` rejects any entry with empty `reproduce_command`. A mission whose `claims.jsonl` passes the validator necessarily reports Axis 2 = 100%.

### Manuscript-side extension

For numerical results in §Results, the analogue is the §Appendix A "canonical reproduce commands" table. The Axis 2 score is computed independently for the literature ledger and for the manuscript Appendix A; both must hit 100% for the axis to read 100%.

The §Appendix A table coverage is computed manually by:

1. Enumerating each numerical result cited in §Results (e.g., "65/65 cascade-stable null", "H_rig = 1.0361 × 10^72").
2. Checking that §Appendix A's pseudocode block or hash-table covers that result.
3. Marking coverage gaps explicitly in `paper/preflight_compliance.md`.

### Machine-checkable procedure

```bash
# Literature side
NUMER=$(jq -c 'select(.reproduce_command != null and .reproduce_command != "" and (.reproduce_command | test("\\S")))' \
        literature/claims.jsonl | wc -l)
DENOM=$(wc -l < literature/claims.jsonl)
echo "Axis 2 (literature): $NUMER / $DENOM"

# Manuscript side: walk §Results numerical claims (manual; not automatable from prose).
# Each must have a §Appendix A reproducer; record outcomes in paper/preflight_compliance.md.
```

---

## Axis 3 — Capability-gap documentation rate

### Definition

```
Axis 3 = (gaps documented in capability/*.gap.md or capability/*_gap.md)
         / (gaps documented + gaps suspected-but-undocumented)
target: 100%
direction: higher is better
```

### Numerator: documented gaps

Files in the `capability/` directory whose name matches `*.gap.md` or `*_gap.md` (case-insensitive). Both naming conventions are acceptable per the existing repository history (`independent_second_library.gap.md` and `symbolic_closure.gap.md` use the dot variant; future entries may use either).

```bash
find capability/ -type f \( -iname '*.gap.md' -o -iname '*_gap.md' \) | wc -l
```

A documented-gap file must contain at least the following sections to count:

- A statement of what was attempted and what failed
- A *gap classification* (FUNDAMENTAL / CONTINGENT / SCOPE-CEDED at minimum)
- A description of what concealment would have looked like (i.e., what the workaround pathway would have been)
- An explicit statement of why the gap is being documented rather than worked around

Files that do not include all four sections are *partial documents* and count as **0.5** units toward the numerator (with a corresponding 0.5 unit in the suspected-but-undocumented denominator term). This is the only fractional-counting rule in the four-axis methodology; it forces honest accounting of partial documentation.

### Denominator: documented + suspected-but-undocumented

The denominator has two terms:

1. **Documented gaps** — same count as the numerator. Trivially included to make the ratio a proper fraction with target 100%.
2. **Suspected-but-undocumented gaps** — gaps that may exist but for which no `*_gap.md` file was created during the mission. This term requires *honest self-assessment* by the mission's authoring agent.

### Suspected-gap honest self-assessment procedure

This is the only place in the four-axis methodology where author judgment enters the score in a way that cannot be machine-replicated from repository content. The procedure is:

The authoring agent (CLI + operator pair) walks the following five-question checklist at score-computation time, and for **each `yes`** answer that does NOT have a corresponding `*_gap.md` file, adds **1** to the suspected-but-undocumented count.

**Question 1: Capability silently treated as verified.**

> Did the mission encounter a step where forward progress could only continue by treating an unverified capability as verified, with no `*_gap.md` documenting the unverified state?

Concrete check: walk every `capability/*.available.md` file and ask: was this capability *functionally verified* per H7 before the first downstream commit that depended on it, or was the file written *after the fact* to retroactively legitimize a step that had already shipped? If the latter, and no `*_gap.md` was created for the interim unverified state, answer `yes`.

**Question 2: Precision / scaling limit silently worked around.**

> Did the mission encounter a precision-budget exhaustion, a runtime ceiling, a memory ceiling, or a `maxcoeff` numerical-overflow event that was worked around (by lowering scope, by switching variants, or by accepting a noisier output) without a `*_gap.md` documenting the limit?

Concrete check: review `harness/precision_budget.md` and `mutation_log/` entries for any rephrasing of the precision target between M2.3 and the canonical execution. Each unexplained tightening of scope is a `yes`.

**Question 3: Empirical sweep silently extended past stated stopping criterion.**

> Did the empirical sweep grow beyond the size declared in `targets/selected.md` or `harness/precision_budget.md` without the extension being a documented gap response?

Concrete check: compare the declared sweep size at M2.3 entry with the realized sweep size at `gold/M3`. A larger realized size is acceptable when the rationale is "the data was already collected and recording it is free"; a `yes` is triggered when the extension was *triggered by an unfavorable boundary case* that would have prompted a gap doc if accepted.

**Question 4: Open subgoal silently folded into manuscript as resolved.**

> Did the manuscript fold a subgoal that the mission did NOT resolve, into §Results or §Discussion, in a way that reads as resolved?

Concrete check: walk every load-bearing claim per Axis 1's numerator definition, and for each, check that its evidence chain (claims.jsonl → harness output → manuscript paragraph) does not contain a `theoretical_citation_only` entry being represented as `proven_corollary` or as `field_standard_practice`. A precision-class downgrade between source and manuscript that is not flagged is a `yes`.

**Question 5: Scope cession silently re-entered.**

> Did the mission revisit a scope-ceded area (e.g., a `seeds/N` DO-NOT-REENTER class) without acknowledging it as a scope question?

Concrete check: grep `mutation_log/` and `harness/` for any reference to a scope-ceded topic (per `seeds/README.md` DO-NOT-REENTER list). Each such reference, if not accompanied by a `*_gap.md` re-entry justification, is a `yes`.

### Why 100% is the target

The Axis 3 score is *not* a measure of how few capability gaps a mission encountered; it is a measure of how honestly each encountered gap was surfaced. A mission that encountered ten gaps and documented all ten scores 100%; a mission that encountered one gap and documented zero scores 0%. The number of gaps a mission encounters is determined by the mission's difficulty; the number it documents is determined by the AEAL discipline.

The 100% target is preferred to a "minimize gaps" target because the latter would create an incentive to conceal gaps rather than to surface them. The five-question honest-self-assessment is the audit defense against this concealment incentive.

### Reporting requirements

When Axis 3 is reported, the document MUST include:

- The list of documented `*_gap.md` files
- The five-question self-assessment record (yes/no for each question + brief rationale)
- The arithmetic: `documented / (documented + suspected) = ratio`

The §Appendix B prose may summarize this as a single ratio with a footnote pointing to the methodology document.

### Machine-checkable procedure (partial)

```bash
# Numerator (machine-checkable)
DOCUMENTED=$(find capability/ -type f \( -iname '*.gap.md' -o -iname '*_gap.md' \) | wc -l)
# Audit each gap file for the 4 required sections (manual; 0.5 unit penalty if any missing)

# Suspected-but-undocumented term (human self-assessment; see five-question procedure)
SUSPECTED=<honest self-assessment integer>

echo "Axis 3: $DOCUMENTED / $((DOCUMENTED + SUSPECTED))"
```

---

## Axis 4 — Literature-fidelity surfacing rate

### Definition

```
Axis 4 = (paper-read catches + verified literature claims)
         / (total claims that depend on literature)
target: 100%
direction: higher is better
```

### Numerator: paper-read catches + verified literature claims

Two terms summed:

1. **Paper-read catches.** Entries numbered in `literature/_fidelity_findings.md` as "Catch #N" — each entry represents a literature-fidelity error that the mission caught (typically by performing an H8 paper-read on a claim that an aggregator had reported). Each Catch #N counts as 1.
2. **Verified literature claims.** `claims.jsonl` entries with `status == "verified"` AND `independent_verifier_result.method == "paper_read_verified"`. The intersection — claims where a paper-read both happened and confirmed the cited content — counts as 1 each.

```bash
CATCHES=$(grep -E '^### Catch #[0-9]+' literature/_fidelity_findings.md | wc -l)
VERIFIED=$(jq -c 'select(.status == "verified" and .independent_verifier_result.method == "paper_read_verified")' \
           literature/claims.jsonl | wc -l)
NUMER=$((CATCHES + VERIFIED))
```

Note: A paper-read catch and a paper-read-verified claim **on the same source paper** are counted **once**, not twice. The Catch # entry typically *creates* the verified claim entry, so the double-count is the same source-of-evidence appearing in two ledger surfaces. To avoid double-counting, the implementation rule is:

> A Catch # entry that produced a new `claims.jsonl` entry contributes 1 unit (the catch). The resulting `claims.jsonl` entry's `paper_read_verified` status is part of the catch's resolution, not a separate unit.
>
> A `claims.jsonl` entry with `paper_read_verified` status that did NOT originate from a fidelity catch contributes 1 unit (the verified claim).

In aggregate: Axis 4 numerator = (number of *distinct* primary sources that received an H8 paper-read).

### Denominator: total claims that depend on literature

`claims.jsonl` entries whose `evidence_class` is one of `primary_paper`, `secondary_paper`, `survey`, or `book` — i.e., entries that represent the mission's dependence on a published external work.

Excluded: `oeis`, `tertiary_aggregator`, `numerical_record`, and `theoretical_obstruction_citation_only` — these are *cross-checks* or *orientation* entries, not load-bearing literature dependencies.

```bash
DENOM=$(jq -c 'select(.evidence_class == "primary_paper" or .evidence_class == "secondary_paper" or .evidence_class == "survey" or .evidence_class == "book")' \
        literature/claims.jsonl | wc -l)
```

Plus a special term: **claims that depend on literature without a corresponding `claims.jsonl` entry**. This would be a literature dependency the manuscript carries but that was never registered in the ledger. A mission with this term ≥ 1 has an under-counted denominator and a Axis 4 score that is inflated relative to reality. The audit procedure to detect this term is:

> Walk every literature citation in `paper/main.tex` `\cite{...}` and check that each citation key has a corresponding `lit-NNN-*.md` annotation and a `claims.jsonl` entry. Each missing pair contributes 1 to this term.

A mission with all citations covered scores 0 on this term.

### Why 100% is the target

Same logic as Axis 2 / Axis 3: the 100% target measures *honesty*, not *absence of fidelity issues*. A mission with zero literature dependencies trivially scores 100%; a mission with 20 literature dependencies all paper-read-verified also scores 100%; a mission with 4 fidelity catches all surfaced as numbered entries in `_fidelity_findings.md` and 16 paper-read-verified claims also scores 100%. The shape of the literature dependency graph does not affect the target; only the discipline of surfacing every dependency does.

The 100% target is enforced at the H8 paper-read heuristic level: any `claims.jsonl` entry that the manuscript cites as load-bearing on a `proven_corollary`-class result MUST carry `paper_read_verified` status. The mutation log records the install of H8 at U-MISSION-J (M2.1) and its application history through M6 Step 1.

### Reporting requirements

When Axis 4 is reported, the document MUST include:

- The numbered Catch list from `_fidelity_findings.md`
- The `claims.jsonl` status distribution (verified, unverified_paywall_blocked, etc.)
- The mutation-log entries that record H8 paper-read installations and applications

### Machine-checkable procedure

```bash
# Numerator — distinct primary sources that received an H8 paper-read
NUMER=$(jq -c 'select(.independent_verifier_result.method == "paper_read_verified")' \
        literature/claims.jsonl | wc -l)

# Denominator — claims depending on literature, plus uncovered \cite{} keys
LIT_DEPS=$(jq -c 'select(.evidence_class == "primary_paper" or .evidence_class == "secondary_paper" or .evidence_class == "survey" or .evidence_class == "book")' \
           literature/claims.jsonl | wc -l)
UNCOVERED=<count of \cite{} keys in paper/main.tex without a matching lit-NNN-*.md>
DENOM=$((LIT_DEPS + UNCOVERED))

echo "Axis 4: $NUMER / $DENOM"
```

---

## Cross-axis interactions and reporting

### Bidirectional verification

The four-axis design is intended to be applied *bidirectionally* — to both agent output and operator framing. The H8 paper-read heuristic, in particular, was installed at U-MISSION-J in response to a literature-fidelity catch that originated in *operator-supplied framing* (the "no prior K_0 PSLQ" claim that turned out to be refuted by BBC 1997 §4). The Axis 4 numerator counts agent-side and operator-side catches identically — the discipline does not distinguish source.

This bidirectional property is what makes the Agent Health Score a methodological claim, not just a self-assessment. A mission whose score is high on all four axes when applied to operator framing as well as to agent output has demonstrated the discipline at scale; a mission whose score is high only on agent-output catches has a one-sided application that warrants noting.

### Halt-and-flag auxiliary axis

The four primary axes are sometimes supplemented with an auxiliary halt-and-flag rate:

```
Auxiliary axis: (halts surfaced + heuristics installed) / (halts encountered)
target: 100%
direction: higher is better
```

A halt is *surfaced* if it appears in `paper/preflight_compliance.md` "halt-event" list and is *resolved* if it produced a heuristic entry in `methodology/heuristics.md`. A mission that encountered halts but did not surface them would score below 100%.

The halt-and-flag axis is auxiliary because halts are a *process* signal whereas the four primary axes are *content* signals. A mission that produced excellent content with no halts is fine; a mission that hid halts is not.

### Aggregation rule

There is no single-scalar aggregation. The four axes are reported as a 4-tuple plus the auxiliary axis, with each axis cited as `<numerator>/<denominator>` rather than as a normalized ratio alone. Mixed verdicts are preferred to averaged ones.

When a §Appendix B prose summary cites a single sentence (e.g., "the mission scored at the design ceiling on all four axes"), the citation must be backed by the full 4-tuple in a footnote or in a referenced data document like `handoff/agent_health_score.md`.

---

## Re-use across SIARC missions

This methodology is intended to apply unchanged to future SIARC missions whose AEAL discipline is comparable to this mission's. Mission-specific values (the 5/65 / 20/20 / 2/2 / 4/4 from M6) belong in each mission's `handoff/agent_health_score.md`; the definitions here belong in a single canonical methodology file.

For a future AEAL methodology paper, this file is the reference for the following claims:

1. The Agent Health Score is a four-axis system with numerator and denominator definitions that can be machine-checked from a repository snapshot, with one exception (Axis 3's suspected-gap term, which requires honest self-assessment via a five-question checklist).
2. The score is not collapsed to a single scalar; mixed verdicts are reported as a 4-tuple plus an auxiliary halt-and-flag rate.
3. The score is applied bidirectionally — to operator framing as well as to agent output — making it a methodological discipline, not a self-grading rubric.
4. Three of the four axes have a 100% target; the fourth (claim-to-sweep ratio) has a "much less than 1" target encoding the consolidation principle.

### Future-mission application checklist

When applying this methodology to a new mission, the authoring agent should:

1. At mission-close (last gold tag), snapshot the repo state.
2. Compute Axis 1 numerator from `paper/main.tex` per the four criteria in §Axis 1.
3. Compute Axis 1 denominator from `harness/sweep_output/` per the four criteria in §Axis 1.
4. Compute Axis 2 numerator and denominator from `literature/claims.jsonl` per the jq filters in §Axis 2.
5. Compute Axis 2 manuscript-side numerator from §Appendix A coverage per the manual walk in §Axis 2.
6. Compute Axis 3 documented-gap count from `find capability/ -iname '*.gap.md'` per §Axis 3.
7. Perform the five-question honest-self-assessment from §Axis 3 and record the result with rationale.
8. Compute Axis 4 numerator from paper-read-verified-distinct-source count per §Axis 4.
9. Compute Axis 4 denominator from literature-dependent `claims.jsonl` entries plus uncovered `\cite{}` keys per §Axis 4.
10. Compute the auxiliary halt-and-flag axis from `paper/preflight_compliance.md` and `methodology/heuristics.md`.
11. Report the 4-tuple + auxiliary in `handoff/agent_health_score.md` for that mission, with §Appendix B prose pointing back to it.

---

## Repository file locations referenced by this methodology

| Path | Purpose | Axis dependency |
|---|---|---|
| `paper/main.tex` | Manuscript prose; §Results / §Discussion / §Appendix A / §Appendix B | Axes 1, 2, 4 |
| `paper/preflight_compliance.md` | Halt-event list, manuscript-level-claim list, precision-class downgrade rationales | Axes 1, 3, auxiliary |
| `harness/sweep_output/*.jsonl` | Canonical sweep records | Axis 1 denominator |
| `harness/precision_budget.md` | Working-precision floor and scope declarations | Axis 1 denominator filter, Axis 3 question 2 |
| `literature/claims.jsonl` | One claim per line, 7-field AEAL schema | Axes 2, 4 |
| `literature/_schema.md` | The 7-field schema canonical reference | Axes 2, 4 |
| `literature/_fidelity_findings.md` | Numbered Catch # entries | Axis 4 numerator |
| `literature/lit-NNN-*.md` | Per-claim human-readable annotation | Axis 4 denominator audit |
| `literature/validate_claims_jsonl.py` | Schema validator; enforces Axis 2 100% at literature side | Axis 2 |
| `capability/*.gap.md` (or `*_gap.md`) | Documented capability gaps | Axis 3 numerator |
| `capability/*.available.md` | Documented capability availabilities | Axis 3 question 1 |
| `mutation_log/*.md` | Audit trail; H6-H10 install records | Axis 3 questions, Axis 4 |
| `methodology/heuristics.md` | H1-H10 definitions | Auxiliary halt-and-flag axis |
| `targets/selected.md` | Scope statement; original sweep-size declaration | Axis 3 question 3 |
| `seeds/README.md` | DO-NOT-REENTER scope-cession list | Axis 3 question 5 |

---

## Validator alignment

A future audit script can be assembled from the grep/jq invocations above; recommended name `handoff/_agent_health_score_validator.py`. Such a script is NOT part of the M6 deliverable; the methodology document is sufficient as the audit substrate, and a validator script would be a Layer-2 substrate-prep item if the operator chooses to add it.

The script, if built, should:

- Compute Axes 1 (denominator only), 2, 4 from machine sources.
- For Axis 1 numerator and Axis 3 suspected-but-undocumented term, emit *prompts* for the authoring agent to fill in with rationale, not compute autonomously.
- Output a single JSON record:

```json
{
  "snapshot": "papanokechi/khinchin-k0-bounded@<tag>",
  "axis_1": {"numerator": <int>, "denominator": <int>, "ratio": <float>, "direction": "lower"},
  "axis_2": {"numerator": <int>, "denominator": <int>, "ratio": <float>, "direction": "higher"},
  "axis_3": {"numerator": <int>, "denominator": <int>, "ratio": <float>, "direction": "higher", "suspected_self_assessment_complete": <bool>},
  "axis_4": {"numerator": <int>, "denominator": <int>, "ratio": <float>, "direction": "higher"},
  "auxiliary_halt_and_flag": {"numerator": <int>, "denominator": <int>, "ratio": <float>}
}
```

This output format is suitable for direct citation in `paper/main.tex` §Appendix B and for inclusion in the AEAL methodology paper's reproducibility appendix.
