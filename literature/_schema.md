# literature/ — M2.1 Literature Claim Ledger Schema

**Brief reference:** §M2.1 (literature claim ledger ≥ 15 entries, AEAL §0.1 seven-field schema).
**Locked at:** M2.1 entry (one-time scaffold per process-to-content rule).
**Subordinate to:** Brief §M2.1, AEAL §0.1, `methodology/heuristics.md` H7 (functional verification on computational claims that the M3.1 harness will depend on).

## 7-field AEAL §0.1 schema (applied to literature + deposit claims)

Each entry in `claims.jsonl` is a single JSON object with EXACTLY these seven fields:

| Field | Type | Description |
|---|---|---|
| `id` | string | Class-dispatched: `lit-NNN-slug` (literature-class) OR `deposit-CLASS-NNN-slug` with CLASS ∈ {`hal`, `zenodo`, `osf`, `preprint-server`, `institutional-repo`} (deposit-class). Zero-padded 3-digit, kebab-case slug. The id prefix is the validator's class dispatcher. |
| `statement` | string | The verifiable assertion about prior work being recorded. Quoted text wins over paraphrase. |
| `evidence_class` | string | Class-dispatched. Literature-class set: `primary_paper`, `secondary_paper`, `book`, `survey`, `tertiary_aggregator`, `oeis`, `numerical_record`, `literature_fidelity_catch`, `theoretical_obstruction_citation_only`. Deposit-class set: `primary_deposit_receipt`. |
| `precision_or_dependencies` | object | Concrete quantitative parameters (precision, degree D, height H, basis size, year, DOI). For non-computational claims, document key non-numerical parameters. For deposit-class claims, includes repository identifiers + deposit metadata (e.g. `hal_id`, `zenodo_relation_type`, `pdf_sha256`). |
| `reproduce_command` | string | A concrete command or URL that lets a future reader retrieve the same artifact. For paywalled papers, the DOI URL + author-host mirror URL. For OEIS, the OEIS URL. For book references, the citation + library lookup string. For deposit-class, the repository portal action + audit-trail URLs. |
| `independent_verifier_result` | object | Structured. Required keys: `verified: bool` (literature-class) / `bool \| null` (deposit-class pre-audit), `method: enum` (class-dispatched: literature-class methods OR deposit-class methods), optional `paywall_blocker: string`, optional `notes: string`, optional `verification_class`/`audit_slot` (deposit-class convention). |
| `status` | string | Class-agnostic flat enum. One of: `verified`, `unverified_abstract_only`, `unverified_paywall_blocked`, `unverified_book_not_digitized`, `fidelity_watch`, `fidelity_caught_refuted`, `theoretical_citation_only`, `pending_verification`. The `pending_verification` value is the natural pre-audit state for deposit-class claims (paired with `verified: null`). |

> **Class-dispatch architecture (slot-217 cycle 2026-05-16):** the validator dispatches
> on the `id` prefix to a class-specific rule set — see the "Authorized exceptions
> ledger" entry below for the full architecture write-up + the in-scope/out-of-scope
> boundary. The seven-field top-level schema is class-agnostic; only the per-field
> bindings diverge between literature-class and deposit-class.

### `independent_verifier_result.method` enum

Per H7 (functional verification on capability claims; the principle applies analogously to literature claims):

- `paper_read_verified` — the full paper PDF/HTML was retrieved and the specific cited
  text was read. **For computational claims that the M3.1 harness will depend on, this
  is the H7 minimum bar.**
- `abstract_only_unverified` — only the abstract / journal landing page was accessible.
  Sufficient for orientation citations; **insufficient for the M2.3 success predicate** —
  any harness dependence on the claim must be re-verified.
- `paywall_blocked` — even the abstract was behind a paywall, or the journal landing
  page is dynamic and unreadable to web_fetch. Must record `paywall_blocker` string
  naming the publisher/access barrier.
- `book_not_digitized` — book/monograph references where the relevant pages are not
  available in any digital form accessible to this session. Cite the canonical book
  reference + ISBN.
- `oeis_or_tertiary_aggregator_verified` — verified against OEIS, MathWorld, Wikipedia,
  or similar tertiary source. Useful for orientation; NOT sufficient for the M2.3
  success predicate without an upstream primary check.
- `computed_reproduction` — the claim was reproduced via local computation (mpmath /
  gp / sympy / etc.). Highest verification level; reserved for numerical-value claims.
- `search_aggregated_unverified` — only an AI-aggregated web search returned the
  claim; the original source was not fetched. Treated as **unverified** until upgraded.
  **Used in this ledger only for the `fidelity_watch` entry**, where two
  search_aggregated_unverified results disagreed and the disagreement itself is the
  content.
- `deposit_receipt_verified` — primary deposit receipt was retrieved from the issuing
  repository (HAL, Zenodo, OSF, institutional repository, preprint server, or other
  primary-deposit issuer) and the recorded identifier/timestamp/DOI matches expectations.
  Reserved for `evidence_class: primary_deposit_receipt` claims. Corroborating modality
  detail (portal screenshot, email confirmation PDF, API response payload, moderation
  outcome notification) is recorded in `independent_verifier_result.notes`, not in the
  method name. Pre-deposit / pre-audit claims pair this method with `status: pending_verification`;
  post-audit claims transition to `status: verified` (or to a fidelity-class status if a
  receipt-vs-expected mismatch surfaces).

## Axes covered (per operator's M2.1 directive)

1. **Khinchin's original 1934/1935 + follow-up irrationality / transcendence on K_0** —
   lit-007 (Khinchin 1935 Compositio Math), lit-008 (Khinchin 1963 book), supported by
   lit-004 (Wikipedia), lit-006 (Shanks-Wrench 1959).

2. **Bailey–Borwein–Plouffe-class PSLQ null results on K_0 or adjacent** — lit-002 is the
   primary-tier paper-read-verified entry: BBC 1997 §4 directly PSLQ-tested K_0 and
   K_{-1} at 7350 dps for both pure-power algebraicity (up to degree 50, height 10^70)
   and a log-multiplicative form (up to height 10^20). Both null. lit-010 covers
   Bailey-Plouffe 1997 "Recognizing Numerical Constants" methodology.

3. **The signature paper `khinchin-signature-pslq` with scope-distinction citation** —
   lit-001. Primary-tier per H6 + the §2.A scope-exclusion in `targets/selected.md`. The
   legitimacy anchor for the M1.2 sub-question's novelty is its Discussion §X passage:
   *"templates involving $n^{1/2}$, $n^2$, or algebraic combinations of $K_0$ with other
   known constants lie entirely outside the tested family and remain open."*

4. **Transcendence partials in the Khinchin family (K_p for p ≠ 0, Lévy constant)** —
   lit-019, lit-020.

5. **Theoretical obstructions — GKW operator (citation only, NOT methodology)** — lit-011
   to lit-014 cite Gauss–Kuzmin–Wirsing operator + Daudé–Flajolet–Vallée + Vallée
   surveys. **Per `seeds/README.md` DO-NOT-REENTER clause and the M1.1 #26 drop, the
   GKW operator is theoretical anchor only; no methodology import. Cited as "why direct
   attack is hard, which is why PSLQ-style numerical evidence is the tractable form."**

6. **Computational records on K_0 precision + published null results** — lit-002 (7350
   digits, BBC 1997), lit-001 (signature paper, 256/512/1024-bit / 300/600-dps), lit-003
   (OEIS A002210, 110 digits + Simó 10^6 terms 2016), lit-006 (Shanks-Wrench 1959), and
   the literature-fidelity catch lit-018.

## Process-to-content rule (binding from M2.1 forward)

This `_schema.md` and `_index.md` are the **only** scaffold files in `literature/`. They
are written ONCE and not iterated on; per the operator's M1.1→M1.2 binding rule, any
further meta-work on the ledger format itself triggers Brief §7 anti-thrashing review.
Every other file under `literature/` is content: a numbered claim entry (`lit-NNN-*.md`),
the JSONL master (`claims.jsonl`), an M2.3 calibration anchor (`_m2.3_calibration_anchor.md`),
or a literature-fidelity-finding document (`_fidelity_findings.md`).

### Authorized exceptions ledger

The process-to-content rule above admits explicit operator-authorized exceptions, each
documented inline below. Adding to this ledger requires the same Brief §7 anti-thrashing
review as any other meta-work — the ledger does not weaken the default rule, it makes
exceptions auditable.

- **2026-05-16, slot-217 audit cycle, SIARC HAL/Episciences pipeline bootstrap — validator class-dispatch architecture.**
  The validator was originally written for a single (implicit) claim class — literature
  claims with `lit-NNN-slug` ids, the literature-class evidence_class enum, the
  literature-class method enum, and a boolean `verified` field. The SIARC HAL/Episciences
  pipeline introduces a second claim class — deposit claims with `deposit-CLASS-NNN-slug`
  ids (CLASS ∈ {hal, zenodo, osf, preprint-server, institutional-repo}), a single-element
  deposit-class evidence_class set (`primary_deposit_receipt`), a single-element
  deposit-class method set (`deposit_receipt_verified`), and a `verified` field that
  takes value `null` while the audit is pre-moderation (paired with `status:
  pending_verification`) before transitioning to a bool at SIARC slot-218 audit close.
  Rather than encode the divergence as enumerated sibling exceptions (one entry per
  enum value or per strict-check fixed), the change is framed as a single architectural
  shift: the validator dispatches on the claim id prefix to a class-specific rule set.

  **In-scope of this entry (applied across commits 9d4c902, 2ca55ad, and the
  class-dispatch refactor commit landing the same day):**

  | Surface | Literature-class binding | Deposit-class binding |
  |---|---|---|
  | id prefix | `lit-` (default) | regex `^deposit-(hal|zenodo|osf|preprint-server|institutional-repo)-\d{3}-` |
  | evidence_class set | `primary_paper`, `secondary_paper`, `book`, `survey`, `tertiary_aggregator`, `oeis`, `numerical_record`, `literature_fidelity_catch`, `theoretical_obstruction_citation_only` | `primary_deposit_receipt` |
  | method set | `paper_read_verified`, `abstract_only_unverified`, `paywall_blocked`, `book_not_digitized`, `oeis_or_tertiary_aggregator_verified`, `computed_reproduction`, `search_aggregated_unverified` | `deposit_receipt_verified` |
  | `verified` field rule | must be bool | bool, OR `null` when `status: pending_verification` (pre-audit state) |
  | status enum | flat enum, class-agnostic | flat enum, class-agnostic; `pending_verification` is the natural pre-audit state for deposit-class |

  Modality detail for deposit-class verification (portal screenshot, email confirmation
  PDF, API response payload, moderation notification) lives in
  `independent_verifier_result.notes`, not in the method enum value — the method names
  the canonical artifact class (deposit receipt), modality describes the corroborating
  evidence shape, which varies by issuing repository. Method name `deposit_receipt_verified`
  chosen over `deposit_receipt_and_portal_screenshot` per operator directive 2026-05-16
  ~21:20 JST ("reconsider method name generality before commit").

  **Out-of-scope (operator-bounded, this entry):** literature-class shape changes; the
  seven-field top-level schema; introduction of a third claim class beyond
  literature + deposit. Any of these would require fresh Brief §7 anti-thrashing review.

  **Forward-compatibility:** new deposit repositories (e.g., extending the regex with
  `arxiv` or `figshare`) extend the prefix pattern; new deposit-class statuses or
  methods extend `DEPOSIT_EVIDENCE_CLASSES` / `DEPOSIT_METHODS` partitions in
  `validate_claims_jsonl.py` without requiring fresh architecture review (those are
  enum-additive within the existing class-dispatch frame). New claim classes (beyond
  literature + deposit) DO require fresh Brief §7 review.

  **Provenance:** slot-217 audit-input package (initial evidence_class extension,
  2026-05-16 ~20:59 JST → commit 9d4c902); slot-217 cycle continuation (status + method
  enum + method-name-generality directive, 2026-05-16 ~21:20 JST → commit 2ca55ad);
  slot-217 cycle continuation round 2 (class-dispatch reframe + id-prefix + verified-null
  + class-conditional enum partitions, 2026-05-16 ~21:35 JST → this commit).

## File layout

```
literature/
├── _schema.md                              # this file (one-time scaffold)
├── _index.md                               # running index, updated as entries are added
├── _m2.3_calibration_anchor.md             # M2.3 success-predicate calibration note
├── _fidelity_findings.md                   # literature-fidelity-error catches (operator's M2 risk class)
├── validate_claims_jsonl.py                # one-time schema validator (not iterated)
├── claims.jsonl                            # machine-readable, 7-field-validated JSON-Lines
└── lit-NNN-*.md                            # human-readable annotations, one per claim
```

## JSON validation

`claims.jsonl` is validated against the AEAL §0.1 schema by running:

```bash
python literature/validate_claims_jsonl.py
```

Validator script lands at M2.1 commit; one-time scaffold; not subject to iterative refinement.
