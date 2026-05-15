# lit-018 — Literature-fidelity catch: "no prior PSLQ on K_0" claim refuted

**Status:** fidelity_caught_refuted · **Class:** literature_fidelity_catch · **Method:** paper_read_verified
**Logged:** 2026-05-15 ~19:50 JST
**Mission role:** evidence-of-discipline artifact; demonstrates H7-analog applied to literature claims; **single highest-value M2.1 finding by the operator's own framing** of the M2 risk class.

---

## 1. The catch (one-paragraph summary)

An AI-aggregated web search of the form "Has anyone published a PSLQ null result on K_0?" returned a **confident NEGATIVE answer** ("There is no published, explicit PSLQ null result for any algebraic equation satisfied by Khinchin's constant K_0 by Bailey, Borwein, Plouffe, or other leading experimental mathematicians"). A second web search 5 minutes later, with a slightly different prompt, returned a **confident POSITIVE answer** that BBC 1997 had tested K_0 — but quoted a sentence that does not appear in the actual paper, and cited a DOI off-by-one-digit from canonical. **Direct PDF retrieval of BBC 1997** (canonical DOI `10.1090/S0025-5718-97-00800-4`; cross-referenced via OEIS A002210) revealed that BBC 1997 §4 **did** PSLQ-test K_0 in two explicit experiments — refuting search-result-1 entirely, and showing search-result-2 was confabulating quote and DOI even while it was correct about the paper's existence.

This is exactly the operator's named M2 risk class (literature-fidelity errors: well-known X but actually Y; widely-cited result but actually-not; computational record cited but never independently reproduced).

## 2. Audit trail (full reproducibility)

### Search query 1 — false negative

- **Timestamp:** 2026-05-15 ~19:45 JST
- **Tool:** `web_search` with prompt: "Has anyone published a PSLQ null result for Khinchin's constant K_0 specifically? I'm looking for prior published PSLQ-based integer-relation searches on K_0 by Bailey, Borwein, Plouffe, or anyone else."
- **Aggregated answer (paraphrased):** "There is no published, explicit PSLQ null result for any algebraic equation satisfied by Khinchin's constant K_0 by Bailey, Borwein, Plouffe, or other leading experimental mathematicians. Existing PSLQ work focuses on π, e, γ, ζ(3), Catalan G, and the Bailey-Borwein-Plouffe formula family. K_0 is on the open-problem list and has not been the subject of a published PSLQ sweep."
- **Sources cited:** various Wikipedia ("Integer relation algorithm" — lit-005, "Khinchin's constant" — lit-004), MathWorld, Bailey-Plouffe "Recognizing Numerical Constants" 1997 (lit-010 — but only by abstract, not paper-read).

### Search query 2 — confident-but-wrong-quote

- **Timestamp:** 2026-05-15 ~19:50 JST
- **Tool:** `web_search` with prompt: "Bailey Borwein Crandall 1997 Khinchin constant Math Comp PSLQ integer relation test results"
- **Aggregated answer (paraphrased):** "Bailey, Borwein, and Crandall (1997) in 'On the Khintchine Constant', Math. Comp. 66 (1997), pp. 417–431, computed K_0 to 7350 digits and PSLQ-tested K_0 directly. They reported '_no integer relation of moderate height was found for K_0 against {1, π, e, log 2, γ}_' [QUOTED INVENTED — not in the paper]. DOI 10.1090/S0025-5718-97-00830-5 [DOI WRONG by one digit]."
- **What was right:** the paper exists; the authorship is correct; the venue and pages are correct; the precision (7350 digits) is correct; the existence of PSLQ tests on K_0 is correct.
- **What was wrong:** the quoted sentence does not appear in the paper; the DOI is off by `30` ↔ `00` and `5` ↔ `4` (canonical is `00800-4`, hallucinated is `00830-5`); the specific basis quoted ({1, π, e, log 2, γ}) is not what BBC actually used.

### Resolution — direct PDF read (H7 analog)

- **Action:** download canonical PDF, verify SHA-256, extract text, grep for actual passages.
- **Source URL:** `https://www.davidhbailey.com/dhbpapers/khinchin.pdf` (David Bailey's personal LBNL archive).
- **SHA-256:** `7dd18d84b93a36b85f4f94d23671a202258cb6517ccbaa5794edeadd0e793793`
- **File size:** 172,853 bytes.
- **Extraction:** `pypdf` text extraction → 36,179 characters, 19 pages.
- **§4 read at lines 720–790** of extracted text; results recorded in full in `lit-002-bailey-borwein-crandall-1997.md` §3.
- **What BBC actually tested:** Two PSLQ experiments. Test 1: pure-power basis {1, K_0, K_0², …, K_0^50}, height bound 10^70, null. Test 2: log-multiplicative basis {log K_0, log p_1, …, log p_15, log π, log e, log γ, log ζ(3), log log 2}, height bound 10^20, null.
- **Both nulls.** Both at 7350 dps.

## 3. The DOI hallucination signature (worth naming)

The DOI `10.1090/S0025-5718-97-00830-5` differs from the canonical `10.1090/S0025-5718-97-00800-4` by:
- `830` → `800` (one inter-digit swap of `3` for `0`)
- `5` → `4` (final check-digit mismatch)

This is a **classic AI-aggregator hallucination pattern**: confident-syntax-correct-DOI, plausible-numeric-shape, but failed real-world existence check. Any future M2.x or M3.x literature claim that arrives via AI aggregator **must be DOI-cross-checked against the actual journal page** (AMS Math. Comp. canonical URL: `https://www.ams.org/journals/mcom/...`) or against an independent reference list (OEIS, the author's own archive, Wikipedia's reference section, etc.).

## 4. H7 analog for literature claims (installed by this catch)

The operator's H7 heuristic for capabilities ("name resolution is not function; require minimum working example") generalizes to literature claims as follows:

> **H7-literature analog (proposed for M2.1 closure):** For any computational claim about prior work that the M3.x harness depends on, **paper-read verification is required**. AI-aggregated web search results, abstract-only summaries, and citation chains through tertiary aggregators (Wikipedia, MathWorld) are INSUFFICIENT for verification. They may surface the existence of a claim but do not verify its content. The bar matches H7 for capabilities: the literature claim must be exercised by direct inspection of the cited primary source, OR marked `unverified_*` in the AEAL `independent_verifier_result.method` field with the appropriate sub-status (`paywall_blocked`, `book_not_digitized`, `abstract_only_unverified`, `fidelity_watch`).

This is not yet a formal H8 in `methodology/heuristics.md` — that would require an operator decision (akin to H7's surfacing in U-MISSION-H). Surfacing the proposal here as a possible **U-MISSION-J** for operator review at M2.1 closure.

## 5. Mission impact

- **Lit-018 itself:** documented as `fidelity_caught_refuted` (status), not as `verified` (which would imply the catch is the load-bearing claim) or `pending` (which would imply the catch is unresolved).
- **Lit-002 (BBC 1997):** entry exists because of this catch and serves as the **single most important load-bearing primary source for M2.3 calibration**.
- **`_m2.3_calibration_anchor.md`:** exists because of this catch and captures the BBC-grandfathering implications.
- **Downstream M2 entries:** all `unverified_abstract_only` or `paywall_blocked` entries are now formally marked **`fidelity_watch`** if they would feed any computational claim into the M3.1 harness. The operator's M2-risk-class framing is now installed mission discipline.

## 6. Methodological postmortem (honest)

If this catch had not occurred, the consequences would have been:
- If search-result-1 had been accepted: the mission would have proceeded as if K_0 had never been PSLQ-tested at high precision, and a M2.3 success predicate based on "find a relation OR prove no relation at D ≤ 6, H ≤ 10^? at 500 dps" would have either (a) silently re-discovered BBC's grandfathered nulls without proper credit, or (b) made the bounded sub-question appear novel when it was structurally a strict-weakening of BBC's already-published Test 1.
- If search-result-2 had been accepted with its hallucinated quote: the mission would have cited BBC 1997 in M2.1 ledger but with the WRONG basis ({1, π, e, log 2, γ}) and the WRONG DOI, propagating an unverifiable claim into the Zenodo deposit at M6 and the eventual public manuscript.

Either path would have leaked into the M6 deposit. The catch at M2.1 averts that. This is precisely the value the operator predicted in the M2.1 greenlight directive:

> "If the CLI catches one literature-fidelity error in M2.1, that single catch is worth the entire mission's process overhead so far."

This entry IS that catch.

## 7. AEAL escalation question RESOLVED — operator U-MISSION-J 2026-05-15 ~21:00 JST

**Halt-status decision: CONFIRMED no 5th-class halt.** Operator verbatim:

> "Halt-status: CONFIRMED no 5th-class halt. BBC-1997 finding confirms M1.2 sub-question scope rather than contradicting it. `selected.md` remains frozen."

**U-MISSION-J H8 install: APPROVED.** See `methodology/heuristics.md` H8 entry (installed with operator-verbatim wording, extended scope covering M2.3 / M3.1 / M6 dependency triad).

**M2.3 binding requirement added by operator:** the M2.3 success predicate must explicitly exclude the pure-power family {1, K_0, K_0², …, K_0^D} as BBC-grandfathered prior art. See `_m2.3_calibration_anchor.md` §6.5.

**M6 scope-positioning note added by operator:** the manuscript has a "two-anchored legitimacy story" — operator's signature paper handoff (Anchor 1) + BBC §4 close handoff (Anchor 2) — to be cited explicitly in M6 §Introduction within the first three paragraphs. See `_m2.3_calibration_anchor.md` §6.6.

**Mutation budget ratification (operator):** lit-018 catch is correctly classified as a documentation event, NOT a hypothesis mutation. §7 budget consumption is reserved for changes to the operator's hypothesis. Refinements to the prior-work field map under H6/H8 are field-map updates, not hypothesis mutations.

This entry's `status` REMAINS `fidelity_caught_refuted` (the catch itself stands as documented; the operator-decision metadata is captured here in §7 rather than altering the AEAL-schema status field).
