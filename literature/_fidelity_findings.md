# Literature-fidelity findings — M2.1 catches

**Created:** 2026-05-15 (M2.1 literature ledger construction)
**Status:** running document; ALL fidelity catches at M2 onwards SHOULD be logged here as they occur
**Companion:** `methodology/heuristics.md` (H1–H7 currently; H8 literature-analog of H7 surfaced as proposal — see §2 below)

---

## 0. Why this document exists

The operator's M2.1 GREENLIGHT directive named the M2 risk class explicitly:

> "M2 will most likely surface a literature-fidelity error — a paper that's widely cited claiming X but on careful reading actually proves Y, or a result that's 'well-known' but never actually published, or a computational record that nobody has independently reproduced. The four M1 halts trained a pattern; M2 is the milestone where that pattern's value compounds, because literature errors get baked into manuscripts and into referee assumptions, and they're much harder to retract than a probe false positive. If the CLI catches one literature-fidelity error in M2.1, that single catch is worth the entire mission's process overhead so far."

This document is the running ledger of those catches. It is content (per the M1.1→M1.2 process-to-content rule): every catch herein is a specific, named, refuted assertion with an audit trail and a paper-read resolution.

---

## 1. Catch #1 (M2.1, 2026-05-15) — "No published PSLQ on K_0" (REFUTED)

**Summary:** an AI-aggregated web search confidently reported that no PSLQ null result on Khinchin's constant K_0 had been published. Direct PDF retrieval of Bailey-Borwein-Crandall 1997 ("On the Khintchine Constant", Math. Comp. 66, 417–431) revealed two explicit PSLQ-null tests on K_0 in §4 of that paper, with documented parameters (D = 50 or basis dim 21, H = 10^70 or 10^20, dps = 7350). Refuted in full.

**Cascade catch:** a second web search confirming the BBC 1997 existence quoted a sentence not in the paper and cited a DOI off by `00830-5` vs canonical `00800-4`. Confirms the AI-aggregator hallucination pattern.

**Mission impact:**
- New primary-tier ledger entry: `lit-002-bailey-borwein-crandall-1997.md`
- New calibration document: `_m2.3_calibration_anchor.md` — establishes that the pure-power sub-basis of B_D(C) is BBC-grandfathered at strictly stronger parameters
- M2.3 success-predicate definition (when operator drafts it) must respect the grandfathering
- New AEAL-schema ledger entry: `lit-018-fidelity-no-prior-k0-pslq-refuted.md` (status: `fidelity_caught_refuted`)

**See:** `lit-018-fidelity-no-prior-k0-pslq-refuted.md` for the full audit trail (search queries, returned answers, DOI hallucination signature, paper-read resolution).

---

## 2. Proposal — H8 literature-analog of H7 (surfaced for operator decision U-MISSION-J)

The U-MISSION-H sequence installed H7 ("functional verification on capability claims: name resolution alone is not function; require minimum working example"). The Catch #1 above is exactly H7's logical structure applied to **literature**, not capabilities. CLI proposes installing H8 in `methodology/heuristics.md` at M2.1 closure (operator-gated):

> **H8 — Paper-read verification on computational literature claims.** For any computational claim about prior published work that the M3.x harness depends on, **direct retrieval and reading of the primary source is required**. AI-aggregated web search results, abstract-only summaries, citation chains through tertiary aggregators (Wikipedia, MathWorld, OEIS commentary), and AI-summarized quote extractions are INSUFFICIENT for verification. They may surface the existence of a claim and orient research but do not verify content. The bar matches H7 for capabilities: the claim must be exercised by direct inspection of the primary source (PDF read, TeX source read, AMS-canonical-URL render check) OR marked `unverified_*` in the AEAL `independent_verifier_result.method` field with the appropriate sub-status (`paywall_blocked`, `book_not_digitized`, `abstract_only_unverified`, `fidelity_watch`). DOI-syntax check against canonical journal URL is required for any AI-aggregator-sourced citation.

**Operator decision token: U-MISSION-J.**

Subordinate to AEAL Brief §M2.1, sibling to H7. Forward-binding on M3.1 harness-dependent literature claims; retroactively binding only on `claims.jsonl` entries with `status` in {`verified`, `unverified_abstract_only`, `unverified_paywall_blocked`, `theoretical_citation_only`, `fidelity_watch`} — confirming or updating their status against the H8 bar.

If H8 is installed, the heuristic count goes `≤7 → ≤8` and the health-score footer in `methodology/heuristics.md` should attach H8 to the "literature-fidelity-honesty" axis.

If H8 is NOT installed, the lit-018 catch remains documented as a one-off; H7 remains the only formal verification-discipline heuristic and applies only to capabilities.

---

## 3. Watch list — entries currently `unverified_*` that COULD have hidden Catch #N

Per the operator's M2-risk-class framing, the following currently-unverified ledger entries are the next-most-likely-to-harbor-a-fidelity-catch candidates and should be paper-read at M2.2 if/when the M3.1 harness develops a dependency on them:

| ID | Status now | Risk class | Why it's on the watch list |
|---|---|---|---|
| lit-006 (Shanks-Wrench 1959) | `unverified_paywall_blocked` | computational-record-cited-but-not-independently-reproduced | First published K_0 high-precision computation; cited transitively via BBC 1997. If M3.1 ever wants to claim 'precision record stands at X' we need to read Shanks-Wrench to know X. |
| lit-007 (Khinchin 1935) | `unverified_abstract_only` | foundational-but-not-read | Original statement of Khinchin's theorem. EuDML may host free PDF; not retrieved this session. |
| lit-009 (Ferguson-Bailey-Arno 1999) | `unverified_abstract_only` | algorithm-correctness-claim | PSLQ definitive paper. M3.1 harness uses mpmath.pslq which encapsulates the algorithm; if we ever cite "PSLQ bounds at height H imply…" we need to verify against this paper directly. |
| lit-010 (Bailey-Plouffe 1997) | `fidelity_watch` | absence-claim-from-aggregator | The claim that K_0 is "not in this paper's null-result tables" was the partial source of search-query-1's false negative in Catch #1. Paper-read needed to confirm or refute. |
| lit-013, lit-014 (Vallée surveys) | `theoretical_citation_only` | theoretical-context-not-method | Lower risk because they're not method-load-bearing per the seeds/26 DO-NOT-REENTER clause; but if the operator ever wants to cite a specific statement about GKW spectrum, paper-read needed. |

**Time budget per watch-list entry (H8 analog of H7's 30-minute retroactive verification budget):** ~20 minutes for an open-access paper, longer for paywalled. Total watch-list budget: ~2 hours if all 5 are paper-read at M2.2.

---

## 4. AEAL discipline notes

- This document is **content**, not process-scaffolding. Each catch is a specific refuted assertion, not a meta-claim about how the ledger is structured.
- The document is also append-only at the catch level: future catches added in §1 numbering (Catch #2, Catch #3, …), watch-list updates in §3, H-proposals in §2. Existing catch entries are NEVER deleted or retroactively rewritten — that would itself be an AEAL violation.
- If a catch turns out to be a false alarm (the AI aggregator was correct after all), it stays in §1 with status amended to `false_alarm` and a paragraph explaining the resolution. Honesty bar: same as H7's "false positives in the audit trail are evidence."

---

## 5. Cross-link summary

- **`lit-002-bailey-borwein-crandall-1997.md`** — the primary source paper-read-verified as resolution to Catch #1
- **`lit-018-fidelity-no-prior-k0-pslq-refuted.md`** — Catch #1's AEAL-schema entry with full audit trail
- **`_m2.3_calibration_anchor.md`** — consequence of Catch #1's resolution: M2.3 success predicate must respect BBC 1997 grandfathering
- **`methodology/heuristics.md`** — would receive H8 if operator approves U-MISSION-J at M2.1 closure
