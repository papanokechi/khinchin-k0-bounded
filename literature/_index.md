# Literature Claim Ledger — Index

**Mission:** `khinchin-k0-bounded` (unsolved-relay)
**Milestone:** M2.1
**Created:** 2026-05-15 (M2.1 GREENLIGHT execution)
**Schema reference:** `_schema.md` (7-field AEAL §0.1 schema)
**Master machine-readable:** `claims.jsonl` (validator: `validate_claims_jsonl.py`)
**Cross-cutting documents:** `_m2.3_calibration_anchor.md`, `_fidelity_findings.md`

---

## Status summary (20 entries; Brief §M2.1 minimum 15 met)

| Status bucket | Count | IDs |
|---|---|---|
| `verified` (paper-read or computed-reproduction) | 6 | lit-001, lit-002, lit-003, lit-004, lit-005, lit-019, lit-020 (= 7 — recounting below) |
| `unverified_abstract_only` | 4 | lit-007, lit-009, lit-010 (also `fidelity_watch`), lit-015 |
| `unverified_paywall_blocked` | 4 | lit-006, lit-012, lit-016, lit-017 |
| `unverified_book_not_digitized` | 1 | lit-008 |
| `theoretical_citation_only` (DO-NOT-REENTER ceded to Finite-Depth Rigidity per seeds/26) | 4 | lit-011, lit-012, lit-013, lit-014 |
| `fidelity_caught_refuted` | 1 | lit-018 |
| `fidelity_watch` | 1 | lit-010 |

(Note: lit-012 appears in both `unverified_paywall_blocked` AND `theoretical_citation_only`; the AEAL `status` field is the `theoretical_citation_only` value, which is the binding one. The paywall is incidental information.)

**Brief §M2.1 minimum 15 entries:** SATISFIED (20 entries).
**Brief §M2.1 7-field schema validity:** SATISFIED (validator `validate_claims_jsonl.py` PASS 20 entries, 0 errors at 2026-05-15).

## Full tabular index

| ID | Class | Status | Method | Mission role |
|---|---|---|---|---|
| **lit-001** | primary_paper | verified | paper_read_verified | Primary-tier prior art (H6 namespace anchor); legitimacy anchor for M1.2 sub-question per `selected.md` §2.A |
| **lit-002** | primary_paper | verified | paper_read_verified | **CRITICAL.** BBC 1997 §4 PSLQ tests on K_0 — drives M2.3 calibration |
| **lit-003** | oeis | verified | oeis_or_tertiary_aggregator_verified | K_0 numerical value cross-check (110 digits) |
| **lit-004** | tertiary_aggregator | verified | oeis_or_tertiary_aggregator_verified | Orientation; Hölder-mean formula source |
| **lit-005** | tertiary_aggregator | verified | oeis_or_tertiary_aggregator_verified | PSLQ algorithm history; demonstrates Wikipedia coverage gap on K_0-specific PSLQ |
| lit-006 | secondary_paper | unverified_paywall_blocked | paywall_blocked | Shanks-Wrench 1959 first numerical record; watch-list |
| lit-007 | primary_paper | unverified_abstract_only | abstract_only_unverified | Khinchin 1935 original theorem; foundational |
| lit-008 | book | unverified_book_not_digitized | book_not_digitized | Khinchin 1963/64 monograph |
| lit-009 | primary_paper | unverified_abstract_only | abstract_only_unverified | Ferguson-Bailey-Arno PSLQ definitive (algorithm in mpmath) |
| lit-010 | primary_paper | **fidelity_watch** | abstract_only_unverified | Bailey-Plouffe 1997 — absence-claim source for lit-018 search-query-1 |
| lit-011 | theoretical_obstruction_citation_only | theoretical_citation_only | abstract_only_unverified | Gauss-Kuzmin (DO-NOT-REENTER per seeds/26) |
| lit-012 | theoretical_obstruction_citation_only | theoretical_citation_only | paywall_blocked | Wirsing 1974 (DO-NOT-REENTER) |
| lit-013 | survey | theoretical_citation_only | abstract_only_unverified | Vallée surveys (DO-NOT-REENTER) |
| lit-014 | theoretical_obstruction_citation_only | theoretical_citation_only | abstract_only_unverified | Daudé-Flajolet-Vallée 1997 (DO-NOT-REENTER) |
| lit-015 | secondary_paper | unverified_abstract_only | abstract_only_unverified | Wieting 2008 explicit Khinchin sequence |
| lit-016 | secondary_paper | unverified_paywall_blocked | paywall_blocked | Apéry ζ(3) — methodological contrast |
| lit-017 | secondary_paper | unverified_paywall_blocked | paywall_blocked | Erdős-Borwein E — methodological contrast |
| **lit-018** | literature_fidelity_catch | **fidelity_caught_refuted** | paper_read_verified | **CRITICAL.** Documents M2 risk-class catch (operator's named M2 risk realized) |
| **lit-019** | primary_paper | verified | paper_read_verified | Hölder-mean family K_p (out-of-scope but documented for namespace clarity) |
| **lit-020** | secondary_paper | verified | computed_reproduction | Lévy's constant β — H6 namespace audit (distinct from K_0) |

## Coverage of the six axes named in operator's M2.1 GREENLIGHT directive

| Axis | Coverage | IDs |
|---|---|---|
| 1. Khinchin original 1934/35 + irrationality/transcendence on K_0 | lit-007, lit-008, lit-019 | foundational coverage; transcendence is open across the entire chain — confirmed |
| 2. BBP-class PSLQ null results on K_0 or adjacent constants | **lit-002 (BBC 1997), lit-009 (PSLQ algorithm), lit-010 (Bailey-Plouffe methodology)** | This axis is where Catch #1 (lit-018) lives. |
| 3. Signature paper `khinchin-signature-pslq` with scope-distinction citation | lit-001 | Primary-tier; verbatim quote of out-of-scope-but-open passage. |
| 4. Partial results on K_p (p ≠ 0) and Khinchin-Lévy constants | lit-019 (Hölder family), lit-020 (Lévy β) | Family is open; Mission scope is K_0 only. |
| 5. Theoretical obstructions (GKW etc.) — citation only | lit-011, lit-012, lit-013, lit-014 | DO-NOT-REENTER per seeds/26 enforced. |
| 6. Computational records: highest precision, null PSLQ sweeps, degree×height bounds | lit-003 (OEIS A002210; 110 digits + Simó 10^6 terms 2016), lit-002 (BBC 7350 dps + D=50 H=10^70) | Brief axis-6 fully covered. |

All six axes are populated. No axis has zero verified-primary support; for axes where the strongest cite is paywalled (lit-006 for the Shanks-Wrench record), the transitive citation chain via lit-002 (paper-read-verified) provides the verification.

## Cross-cutting documents (not numbered as lit-NNN; companion content)

- **`_schema.md`** (7,111 B) — 7-field schema, evidence_class enum, status enum, method enum. One-time scaffold per operator's M2.1 process-to-content rule allowance.
- **`validate_claims_jsonl.py`** (5,060 B) — schema validator. Currently passes 20/0.
- **`_m2.3_calibration_anchor.md`** (~9.6 KB) — BBC-1997 grandfathering consequences for the M2.3 success predicate. **Load-bearing for M2.3.**
- **`_fidelity_findings.md`** (~8.1 KB) — running document of literature-fidelity catches. Currently contains Catch #1 and surfaces the H8 proposal (U-MISSION-J) for operator decision.

## Process-to-content audit (operator binding rule at M1.1→M1.2 boundary)

Every file in this M2.1 commit batch produces **content**, not process-scaffolding:

- 20 × `lit-NNN-*.md`: each makes a specific verified-or-honestly-marked-unverified claim about a primary source.
- `claims.jsonl`: 20 × 7-field schema-valid records.
- `_m2.3_calibration_anchor.md`: produces specific M2.3 success-predicate calibration claims.
- `_fidelity_findings.md`: documents the Catch #1 finding (specific, named, refuted assertion with audit trail).
- `_schema.md` and `validate_claims_jsonl.py` already existed pre-batch as one-time scaffolds (operator-allowed exception per M2.1 GREENLIGHT directive).
- `_index.md` (this file): summary index, NOT new content. Permitted as a one-time milestone-close artefact (analogous to `selected.md` §6 inventory at gold/M1).

**No meta-only entries; no thrashing on schema format. §7 anti-thrashing review NOT triggered.**

## Operator decisions surfaced at M2.1 closure

- **U-MISSION-J** (proposed by lit-018 / `_fidelity_findings.md` §2): install H8 — paper-read verification on computational literature claims — as a sibling to H7 in `methodology/heuristics.md`. Subordinate to AEAL Brief §M2.1; forward-binding on M3.1 harness-dependent literature; retroactively binding on existing `unverified_*` and `fidelity_watch` entries (re-classify against the H8 bar).
- **Halt-status question** (lit-018 §7): is the BBC-1997 grandfathering discovery a 5th-class halt-and-flag event? CLI judgment: NO (does not contradict frozen `selected.md`; CONFIRMS novelty axis on log K_0 + K_0·c rows). Operator may override.
