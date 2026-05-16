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

## 2. ~~Proposal — H8 literature-analog of H7~~ → **INSTALLED as H8 (U-MISSION-J approved 2026-05-15 ~21:00 JST)**

**Status:** H8 INSTALLED in `methodology/heuristics.md` with operator-verbatim wording at U-MISSION-J approval 2026-05-15 ~21:00 JST. See `methodology/heuristics.md` H8 entry and `mutation_log/m2.1_to_m2.2_u_mission_j_h8_install_20260515.md`.

The CLI's pre-install proposal text is preserved below for traceability. **The final installed wording extends the CLI draft in three places:**

1. **Dependency triad explicit** (CLI draft had a single target "M3.x harness"): operator's version names (a) M2.3 success predicate, (b) M3.1 harness design, and (c) M6 manuscript scope-distinction story.
2. **"Confident false positives in both directions"** is named explicitly as the failure mode in the operator wording. This captures the dual-direction signature observed in Catch #1 (false-negative AND false-positive within the same query topic).
3. **Retroactive-binding scope tightened** to "entries currently relied on by M2.3 calibration" — operator's version is more permissive than the CLI draft's blanket retroactive binding on all `unverified_*` entries. Entries not yet in the dependency chain may remain in their current state until they enter it.

### Pre-install CLI draft (preserved verbatim for traceability)

The U-MISSION-H sequence installed H7 ("functional verification on capability claims: name resolution alone is not function; require minimum working example"). The Catch #1 above is exactly H7's logical structure applied to **literature**, not capabilities. CLI proposes installing H8 in `methodology/heuristics.md` at M2.1 closure (operator-gated):

> **H8 — Paper-read verification on computational literature claims.** For any computational claim about prior published work that the M3.x harness depends on, **direct retrieval and reading of the primary source is required**. AI-aggregated web search results, abstract-only summaries, citation chains through tertiary aggregators (Wikipedia, MathWorld, OEIS commentary), and AI-summarized quote extractions are INSUFFICIENT for verification. They may surface the existence of a claim and orient research but do not verify content. The bar matches H7 for capabilities: the claim must be exercised by direct inspection of the primary source (PDF read, TeX source read, AMS-canonical-URL render check) OR marked `unverified_*` in the AEAL `independent_verifier_result.method` field with the appropriate sub-status (`paywall_blocked`, `book_not_digitized`, `abstract_only_unverified`, `fidelity_watch`). DOI-syntax check against canonical journal URL is required for any AI-aggregator-sourced citation.

**Operator decision token: U-MISSION-J — RESOLVED 2026-05-15 ~21:00 JST APPROVE with extended scope.**

~~Subordinate to AEAL Brief §M2.1, sibling to H7. Forward-binding on M3.1 harness-dependent literature claims; retroactively binding only on `claims.jsonl` entries with `status` in {`verified`, `unverified_abstract_only`, `unverified_paywall_blocked`, `theoretical_citation_only`, `fidelity_watch`} — confirming or updating their status against the H8 bar.~~

**Installed scope (operator's binding wording — see `methodology/heuristics.md` H8 for full text):** Subordinate to Brief §M2.1; sibling to H7. **Retroactively binding only on entries currently relied on by M2.3 calibration** (lit-001, lit-002, lit-003 are all already `paper_read_verified` or canonical-database-verified — all H8-compliant). **Entries not yet relied on may remain in their current verification state until they enter the dependency chain.**

~~If H8 is installed, the heuristic count goes `≤7 → ≤8` and the health-score footer in `methodology/heuristics.md` should attach H8 to the "literature-fidelity-honesty" axis.~~ — DONE.

~~If H8 is NOT installed, the lit-018 catch remains documented as a one-off; H7 remains the only formal verification-discipline heuristic and applies only to capabilities.~~ — not the path taken; H8 installed.

---

## 3. Watch list — entries currently `unverified_*` that COULD have hidden Catch #N

Per the operator's M2-risk-class framing, the following currently-unverified ledger entries are the next-most-likely-to-harbor-a-fidelity-catch candidates and should be paper-read at M2.2 if/when the M3.1 harness develops a dependency on them:

| ID | Status now | Risk class | Why it's on the watch list |
|---|---|---|---|
| lit-006 (Shanks-Wrench 1959) | `unverified_paywall_blocked` | computational-record-cited-but-not-independently-reproduced | First published K_0 high-precision computation; cited transitively via BBC 1997. If M3.1 ever wants to claim 'precision record stands at X' we need to read Shanks-Wrench to know X. |
| lit-007 (Khinchin 1935) | `unverified_abstract_only` | foundational-but-not-read | Original statement of Khinchin's theorem. EuDML may host free PDF; not retrieved this session. |
| ~~lit-009 (Ferguson-Bailey-Arno 1999)~~ → **PROMOTED `verified` 2026-05-15 ~21:30 JST** | ~~`unverified_abstract_only`~~ → `verified` / `paper_read_verified` | ~~algorithm-correctness-claim~~ → **TRIGGER FIRED → Catch #2 surfaced** | M3.1 harness's confidence relation cited from this paper → entered M2.3 dep chain at U-MISSION-K → H8 retroactive-binding triggered → paper-read executed. Result: heuristic-vs-theorem distinction surfaced as Catch #2 (§6 below). |
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
- **`lit-009-ferguson-bailey-arno-1999.md`** — primary source paper-read-verified at U-MISSION-K halt (Catch #2 resolution-pending)
- **`harness/precision_budget.md`** — Catch #2's primary document; H8 paper-read of FBA 1999 + heuristic-vs-theorem finding surfaced
- **`mutation_log/m2.2_to_m2.3_pslq_certificate_halt_20260515.md`** — Catch #2's halt-event log

---

## 6. Catch #2 (M2.3, 2026-05-15 ~21:30 JST) — "FBA 1999 states `H ≈ 10^{P/n}` as a theorem" (REFUTED — folklore-grade not theorem-grade) → **RESOLVED U-MISSION-L 2026-05-15 ~21:36 JST**

**Class:** algorithm-correctness-claim heuristic-vs-theorem distinction (operator-predicted M2.3 finding class)

**Summary:** The previous lit-009 entry asserted that Ferguson-Bailey-Arno (1999), "Analysis of PSLQ", proves "at precision P, PSLQ certifies absence of integer relations with coefficient height ≲ 10^{P/dim}". Direct paper-read of the FBA 1999 preprint (Bailey archive `cpslq.pdf`, SHA-256 `3E330BC1...12890B5`, 26 pages, 218,997 bytes) revealed that no such theorem appears in the paper.

What FBA 1999 actually proves (paper-read verbatim):

- **Theorem 1** (p.10): `M_x ≥ 1 / max_i |h_{i,i}(k)|` — per-iteration rigorous lower-bound certificate on the smallest possible relation norm, parametrized by the running H-matrix diagonals.
- **Theorem 3** (p.15): `|m| ≤ γ^{n-2} M_x` for `γ > 2/√3` (real case) — overshoot bound on PSLQ-found relations.
- **Corollary 2** (p.14): PSLQ(τ) terminates in `< (n choose 2) · log_τ(γ^{n-1} M_x)` iterations — polynomial-time bound.

The folklore `H ≈ 10^{P/n}` is an **empirical scaling** of `max_i |h_{i,i}|` against precision P at typical PSLQ convergence. It is consistent with FBA 1999's framework but is NOT a stated theorem. BBC 1997 (lit-002) calibrates this empirically with `c ≈ 2.06` confidence factor over the bare folklore: at n=51, P=7350 dps, BBC reported H=10^70 versus 10^{7350/51}≈10^144 from the bare folklore — i.e., the BBC-1997 community practice is to use a ~2× more conservative bound than the folklore heuristic.

**Catch #2 resolution (U-MISSION-L, 2026-05-15 ~21:36 JST):**

Operator accepted Option A with strengthening to **two-tier predicate** — empirical (`field_standard_practice` per H9) + rigorous (`proven_corollary` per H9). The originally-feared Option B Capability Gap CG-2 was dissolved by a follow-up source inspection: mpmath.pslq's `verbose=True` mode DOES print a Theorem-1-style rigorous bound at every iteration (the printed "Norm" field, computed internally from `max|H[i,j]|` with 100x safety factor), and this is captureable via stdout redirection — see `harness/rigorous_bound.py` module docstring. Four divergences from FBA 1999 are documented and flagged (D1: max-all-entries vs max-diagonal; D2: γ=√(4/3) exact vs strict; D3: mpmath cites Bailey 1998 not FBA 1999; D4: 100x safety factor) — none invalidates Corollary 2 applicability; D2/D3 are forward-flagged for downstream H8 strengthening if rigorous tier is load-bearing in M6.

The two-tier predicate is drafted in `_m2.3_calibration_anchor.md` §7. (P, H_target) committed: **Option α** — P=2160 dps, H_empirical=10⁷⁰ (BBC strict parity). H_rigorous is reported alongside H_empirical from the same PSLQ run; reaches 10⁷⁰ at K ≈ 50-100k iterations per `precision_budget.md` §5.2.

H9 INSTALLED with four classes (operator-strengthened from CLI-proposed three): `rigorous_theorem`, `proven_corollary`, `field_standard_practice`, `empirical_heuristic`. Documented in `methodology/heuristics.md` H9 entry.

**Mission impact (updated post-U-MISSION-L):**

- lit-009 already promoted to `verified` / `paper_read_verified` at prior commit `7a28604`.
- lit-009 `independent_verifier_result.verification_class = proven_corollary` (the primary cited bound now used in M2.3 predicate is FBA Cor 2, with per-statement breakdown in `methodology/heuristics.md` H9).
- `harness/precision_budget.md` rewritten: §7.3 records U-MISSION-L resolution; §5 revised with rigorous-bound investigation; §6.2 commits Option α; §8 references the predicate draft; §9 marks H9 installed.
- `literature/_m2.3_calibration_anchor.md` §7 NEW — drafts the M2.3 final two-tier predicate with three Excluded Families (EF1-EF3); previous §7 "AEAL discipline note" renamed to §8.
- `harness/rigorous_bound.py` NEW — implements the rigorous-bound derivation (FBA T1 via mpmath verbose; FBA Cor 2 via iteration count); demo output captured at `harness/_rigorous_bound_demo_output.txt`.
- `claims.jsonl` H9 verification_class fields added to 5 load-bearing entries (lit-001, lit-002, lit-003, lit-009, lit-018) via sub-key in `independent_verifier_result` (validator PASS 20 entries 0 errors; schema lock preserved).
- M3.1 implementation **gated on operator ratification** of `_m2.3_calibration_anchor.md` §7 predicate text per U-MISSION-L Step 4.

**Counts:**

- This is the **5th halt-class finding** for the unsolved-relay mission overall.
- This is the **1st halt-class finding within M2** — matching the operator's M2.1-GREENLIGHT prediction: "M2.3 will probably have one finding (likely in the precision_budget.md derivation — PSLQ confidence relations are subtler than the textbook formula suggests)."
- **Catch #2 RESOLVED** at U-MISSION-L without re-halt. The AEAL maturation curve framing was operator-validated: M2.2 had zero findings, M2.3 surfaced exactly one finding in exactly the predicted class.

**See:**

- `harness/precision_budget.md` (full M2.3 derivation + U-MISSION-L two-tier resolution + §6.2 Option α commitment)
- `harness/rigorous_bound.py` (Tier 2 implementation; module docstring documents 4 divergences D1-D4)
- `literature/_m2.3_calibration_anchor.md` §7 (M2.3 final predicate text, drafted, awaiting operator ratification)
- `literature/lit-009-ferguson-bailey-arno-1999.md` (paper-read-verified annotation)
- `methodology/heuristics.md` H9 (four-class verification_class taxonomy)
- `mutation_log/m2.2_to_m2.3_pslq_certificate_halt_20260515.md` (Catch #2 halt-event log; predecessor)
- `mutation_log/m2.3_u_mission_l_two_tier_predicate_20260515.md` (U-MISSION-L resolution log; this resolution's mutation_log entry)
- Operator U-MISSION-K (2026-05-15 ~21:14 JST) directive specifying the non-collapsible four-step sequence
- Operator U-MISSION-L (2026-05-15 ~21:36 JST) directive resolving Catch #2 and approving H9

**AEAL discipline note:** Per operator's U-MISSION-J ratification AND U-MISSION-L re-ratification, **this finding and its resolution do NOT consume the mutation budget**: lit-009's `statement`-field rewrite is a documentation event; the H8 promotion + H9 classification additions are verification-status changes / field-map updates; the two-tier predicate is a confidence-reporting-structure extension, not a hypothesis change. Per U-MISSION-L verbatim: "Classify as field-map update, not hypothesis mutation: the hypothesis (test for integer relations in B_D(C)) is unchanged; the confidence reporting structure is being extended." The mutation budget at M2 milestone-block remains at **0/1 consumed**.



---

## 7. Catch #3 (M3.2b, 2026-05-16 ~10:50 JST) — mpirical_height float overflow at n ≤ 3 + H_empirical-vs-maxcoeff semantic question

**Catch class:** harness-execution defect with predicate-text semantic question attached. Operator anticipated this class explicitly in U-MISSION-M3.2 GREENLIGHT: `The M3.1 implementation phase will likely surface harness-execution findings (mpmath behavior under stress, gp lindep edge cases, basis dimension mismatches at filter boundaries) — those are expected and should be halted as before.''

**Status:** **HALTED** awaiting operator ratification. No fix applied yet. M3.2b NOT re-executed pending operator decision on both findings together.

### 7.1 What surfaced

M3.2b launched at 2026-05-16 10:02:07 JST via `python harness/sweep.py --full --m32-full-greenlighted` (commit `66ca169` HEAD). At candidate **10/65** (`pair_log_1`, n=2), the harness raised:

```
File "harness/verify.py", line 67, in empirical_height
    return 10 ** (P / (c * n))
OverflowError: (34, 'Result too large')
```

Cause: `empirical_height(P=2160, n=2, c=2.06)` computes `10**524.27` in native Python float, which overflows the IEEE 754 double range (max ≈ 1.79e+308). The function is called as `H_empirical = empirical_height(primary_P, n, c=2.06)` in `verify.py` line 301 BEFORE the cascade runs — so the failure aborts the candidate before any PSLQ work happens.

**Affected candidates:** any sub-basis where `P / (c · n) > 307`, i.e. `c·n < P/307 = 7.04`, i.e. `n < 3.42`. At P=2160, c=2.06 this means **n ≤ 3** sub-bases. From the 65-candidate enumeration:

| Family | n | count | Status |
|---|---|---|---|
| primary_full | 15 | 1 | ✅ Completed (3172.5s) — clean null |
| full_complement | 8 | 1 | ✅ Completed (25.2s) — clean null |
| complement_plus_K0_k | 9 | 7 | ✅ Completed (~30s each) — clean null |
| pair_log_x | 2 | 14 | ❌ Would overflow |
| pair_bilinear_ij | 2 | 21 | ❌ Would overflow |
| triplet_log_xy | 3 | 21 | ❌ Would overflow |

**56 of 65 candidates** (every n ≤ 3 sub-basis) would hit this defect. Candidate 10/65 was the first.

### 7.2 Partial-run cascade integrity (the 9 completed candidates)

All 9 completed candidates produced `cascade_stable_null` at P=2160/4320/8640. Their JSONL records are intact and preserved at `harness/sweep_output/m32b_empirical_sweep.FAILED_PARTIAL_n9_overflow.jsonl`:

| Idx | Family | n | Cascade verdict | H_empirical | H_rigorous | verification_class | Elapsed |
|---|---|---|---|---|---|---|---|
| 1 | primary_full | 15 | cascade_stable_null | 8.00e+69 | 1.04e+72 | proven_corollary | 3172.50s |
| 2 | full_complement | 8 | cascade_stable_null | 1.17e+131 | 1.16e+21 | field_standard_practice | 25.15s |
| 3 | complement_plus_K0_0 | 9 | cascade_stable_null | 3.20e+116 | 5.47e+15 | field_standard_practice | 30.58s |
| 4 | complement_plus_K0_1 | 9 | cascade_stable_null | 3.20e+116 | 3.12e+16 | field_standard_practice | 29.84s |
| 5 | complement_plus_K0_2 | 9 | cascade_stable_null | 3.20e+116 | 1.43e+16 | field_standard_practice | 30.31s |
| 6 | complement_plus_K0_3 | 9 | cascade_stable_null | 3.20e+116 | 3.50e+15 | field_standard_practice | 30.41s |
| 7 | complement_plus_K0_4 | 9 | cascade_stable_null | 3.20e+116 | 1.26e+16 | field_standard_practice | 30.82s |
| 8 | complement_plus_K0_5 | 9 | cascade_stable_null | 3.20e+116 | 6.18e+15 | field_standard_practice | 30.52s |
| 9 | complement_plus_K0_6 | 9 | cascade_stable_null | 3.20e+116 | 9.06e+16 | field_standard_practice | 30.32s |

Measurement integrity for the 9 completed candidates is **intact**. The crash is upstream of PSLQ measurement, in the H_empirical computation only.

### 7.3 The secondary semantic question

The float-overflow defect is mechanically trivial to fix (use `mpmath` for the computation, return Python int when value exceeds float range). But the crash surfaces a **legitimate predicate-text question** that should be ratified by operator before re-running:

**Question:** at small n, the BBC formula gives `H_empirical_formula = c · 10^(P/(c·n))` that vastly exceeds `maxcoeff = 10^70`. For the n=2 sub-bases `H_empirical_formula ≈ 10^524`, for n=3 sub-bases `≈ 10^350`. But PSLQ is **configured** with maxcoeff = 10^70 and can not detect any relation with max coefficient > 10^70 regardless of H_empirical_formula. Is the empirical scope claim then:

  **(α) Uncapped** (verbatim BBC formula): `"Null PSLQ at (P, n) implies no integer relation with height ≤ H_empirical_formula"` even when this exceeds maxcoeff. Defensible because the BBC formula describes what PSLQ COULD find given (P, n), and the maxcoeff cap is a separate practical convenience that doesn't change the precision-per-dimension theoretical reach. M6 reporting: `H_empirical = 10^524 at n=2 (P=2160)`. Reviewer-defensible only if explicitly footnoted.

  **(β) maxcoeff-capped**: `H_empirical = min(c · 10^(P/(c·n)), maxcoeff)`. For all n ≤ 3 sub-bases, this gives `H_empirical = 10^70` exactly. Defensible because PSLQ literally cannot find relations with max coefficient > maxcoeff, so claiming a higher empirical bound is unwarranted. M6 reporting: uniform `H_empirical = 10^70` across all sub-bases. Cleaner. Field-standard-practice-aligned.

The operator U-MISSION-K + U-MISSION-L specified `H_empirical = 10^70` for the n=15 primary case at BBC parity. The predicate text (`_m2.3_calibration_anchor.md` §7.3 lines 296-298) anchors the value at n=15 but does NOT define behavior at other n. The M3.2 phase split §7.9 added the M3.2b sweep but did not address the small-n H_empirical question. The question is therefore **unresolved** in the gold/M2 predicate text.

### 7.4 Heuristic-class self-assessment

Per H7 (functional verification of harness techniques): the dry-run path at P=120 → `P/(c·n) ≤ 29` exercised float-only arithmetic safely. The `--m31-extended-dry-run` mode at P=540/1080/2160 with `maxcoeff_exp=40` would have exercised `P/(c·n)` up to `2160/4.12 = 524` at n=2, also overflowing — but extended dry-run was never executed because the harness went directly from minimal dry-run (P=120) to M3.2a (n=15 primary only, n=15 doesn't overflow). The extended dry-run mode was implemented but the operator's M3.2 sequence proceeded directly to M3.2a primary measurement. **H7 functional-verification gap:** the multi-precision `--m31-extended-dry-run` path was implemented but never invoked, so the small-n float overflow was not caught pre-canonical-execution.

Per H9 (verification classes): the H_empirical value is ield_standard_practice regardless of resolution path; this is not a verification-class question.

Per H8 (paper-read): the BBC formula's exact behavior at very small n is not specified in BBC 1997 §4 (which tested n ≈ 50, not n=2). The empirical formula's small-n extrapolation is not paper-read-verified. Resolution α invokes the formula in a domain it was not calibrated for; resolution β sidesteps the question.

### 7.5 Proposed resolutions (CLI surface, operator decides)

**(R1) Mechanical fix to `empirical_height`.** Use mpmath for the power computation; return Python int when exponent > 300, else float. Backward-compat preserved for n=15 (M3.2a-style); int-vs-float type difference in JSONL noted in schema docs. This fix is needed regardless of resolution α-vs-β; the function must not overflow.

**(R2.α) Adopt uncapped BBC formula (verbatim).** Apply R1 only. Re-run M3.2b. JSONL reports `H_empirical ≈ 10^524` at n=2. M6 §Results carries explicit "small-n extrapolation note" alongside per-sub-basis table.

**(R2.β) Adopt maxcoeff-capped variant.** Apply R1 + change `empirical_height` to return `min(c · 10^(P/(c·n)), 10^maxcoeff_exp)`. Re-run M3.2b. JSONL reports `H_empirical = 10^70` uniformly for n ≤ 3 sub-bases. M6 §Results carries one uniform empirical bound across all sub-bases. Cleaner.

**(R2.γ) Other (operator-defined).** E.g. report both values in JSONL (`H_empirical_formula` and `H_empirical_capped`); have M6 §Results discuss both.

**CLI recommendation (operator may override):** R1 + R2.β. Field-standard practice is to report the operational bound; PSLQ-with-maxcoeff cannot exceed maxcoeff. Reporting H_empirical = 10^524 at n=2 will draw a reviewer flag for the M6 submission. Capping at maxcoeff is the conservative, defensible reporting. The BBC formula's small-n extrapolation can be discussed in M6 §Discussion as a methodological note rather than a numerical claim.

### 7.6 Authority + mutation budget

Resolution R1 (mechanical fix) is unambiguously **NOT** a hypothesis mutation — it is a defect fix to the harness. Resolution R2 (α/β/γ) is a **field-map update** that refines the operational meaning of H_empirical at small n; the hypothesis (test for integer relations in B_D(C)) is unchanged. Per U-MISSION-L's precedent ("Classify as field-map update, not hypothesis mutation"), the mutation budget at M2 milestone-block stays **0/1 consumed** regardless of which R2 resolution is adopted.

If R2.β is adopted, the predicate text in `_m2.3_calibration_anchor.md` §7.3 must be augmented with a small-n footnote (this is a §7-text edit post-gold/M2 → requires a new mutation_log entry per the gold/M2 freeze convention, in line with the M3.2 phase split precedent at `mutation_log/m3.2_phase_split_20260516.md`).

### 7.7 Halt-and-flag verdict

**HALTED.** No code changes made. No JSONL committed. Failed partial preserved at `harness/sweep_output/m32b_empirical_sweep.FAILED_PARTIAL_n9_overflow.jsonl` (9 candidates of clean cascade-stable-null evidence). Awaiting operator ratification on (R1) + (R2.α/β/γ) before re-executing M3.2b. **This is U-MISSION-N**: M3.2b harness defect + small-n empirical-height semantics.

### 7.8 Counts

- This is the **6th halt-class finding** for the unsolved-relay mission overall.
- This is the **1st halt-class finding within M3** — matching the operator's U-MISSION-M3.2 prediction: `The M3.1 implementation phase will likely surface harness-execution findings ... those are expected and should be halted as before.`
- AEAL maturation curve update: M1=4 halts → M2.1=1 → M2.2=0 → M2.3=1 (Catch #2 resolved) → M3.1 impl=0 → M3.2a exec=0 → **M3.2b exec=1** (this catch).

### 7.9 Cross-references

- `harness/verify.py` line 65-67 (defective `empirical_height` — to be fixed).
- `harness/sweep_output/m32b_empirical_sweep.FAILED_PARTIAL_n9_overflow.jsonl` (9-candidate audit-trail data, cascade integrity intact).
- `literature/_m2.3_calibration_anchor.md` §7.3 (predicate text anchoring H_empirical at n=15 only; small-n behavior unresolved).
- `literature/_m2.3_calibration_anchor.md` §7.9 (M3.2 phase split methodology refinement; precedent for §7-text edit + mutation_log).
- `mutation_log/m3.2_phase_split_20260516.md` (precedent mutation_log entry for §7 procedural extension).
- Operator U-MISSION-M3.2 (2026-05-16 ~08:22 JST) — anticipated this class of finding verbatim.
- Operator U-MISSION-M3.2b-RATIFICATION (2026-05-16 ~10:00 JST) — greenlit M3.2b that surfaced this.
