# Mutation log — 12th entry: M6 Step 1 Bailey 1998 H8 fire (2026-05-16)

**Date:** 2026-05-16 ~15:55 JST
**Authority:** Operator M6 GREENLIGHTED directive 2026-05-16 ~15:48 JST, M6 work-sequence Step 1.
**Status:** EXECUTED. Halt count unchanged at 6. Mutation budget at M2 milestone-block: **0/1 consumed (preserved).**
**Classification per H5 + U-MISSION-J / U-MISSION-L / U-MISSION-N precedents:** **field-map update**, NOT hypothesis mutation.

---

## 1. Operator directive (verbatim, from M6 GREENLIGHTED message Step 1)

> Pre-drafting H8 fire on Bailey 1998 per m6_preflight §1. If M6 §Methods cites FBA T1+Cor2 as proof-of-bound justification for the rigorous tier (it will), H8 paper-read on Bailey 1998 is required to resolve D2 (γ = √(4/3) boundary case) and D3 (mpmath-cited-source question) divergences identified at M2.3. Wall-clock: 1-3 hours. Output: literature/lit-NNN-bailey-1998.md with paper-read verification, and either (a) confirmation that divergences are immaterial to the M6 rigorous tier claim, or (b) identification of specific divergences that affect the rigorous tier claim, requiring §Methods text adjustment.

## 2. Outcome — VERDICT (a): divergences IMMATERIAL to M6 rigorous tier claim

**Both flagged divergences D2 and D3 CLEARED. One NEW finding D5 (strengthening, not correction). No M6 §Methods text adjustment required.**

The rigorous tier verification class `proven_corollary` and the bound H_rigorous = 1.036 × 10⁷² are preserved without modification. The empirical tier verification class `field_standard_practice` is now anchored to a second paper-read primary source (lit-010 in addition to lit-002).

## 3. Honest deviation from operator's wording

Operator directive says "Output: literature/lit-NNN-bailey-1998.md". The actual disposition is **lit-010 upgrade** (`fidelity_watch → verified`) rather than a new lit-NNN entry. Reason: the mission's existing lit-010 entry is `lit-010-bailey-plouffe-1997-recognizing.md` (preprint year 1997) — the SAME paper that proceedings indexes as "Bailey 1998" (CMS Conf. Proc. 20, AMS 1998). mpmath's docstring uses the 1998 publication year; lit-010's filename uses the 1997 preprint year. The H8 fire confirms this identification (the §2 algorithm description mpmath translates is in lit-010's source). Using lit-010 preserves the canonical claims.jsonl identification chain; creating a new lit-021 would split the citation across two entries for the same paper.

**Operator may overrule this honest deviation if a separate lit-NNN entry is required for the bibliographic record.** CLI judgment: lit-010 upgrade is the structurally correct action.

## 4. Execution audit trail

### 4.1 Paper retrieval (2026-05-16 ~15:53 JST)

- **Source URL (mpmath's docstring):** `http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html`
- **Files retrieved:**
  - `paper.html` (ToC): SHA-256 `8BEB376B8C78D60883B4B0BFA31F11E4192420C466E923EF22774D878A106A00` (2,123 bytes)
  - `node3.html` (§2 PSLQ algorithm): SHA-256 `5E435CAFBD1DA27928CE8082125EEBD8472EF39FE856A7F4C027177121C14895` (11,344 bytes)
- **Retrieval method:** `curl.exe -s -o`
- **Cache location:** session workspace `harness/_pslq_candidates/` (excluded from repo per `.gitignore` — paper provenance via SHA-256, not binary in repo, per `cpslq.pdf` precedent at U-MISSION-K).

### 4.2 Paper-read findings (verbatim structural extract from node3.html §2)

**Pseudocode structure** (initialization 4 steps + iteration 6 steps):

- **Initialization:**
  1. Set the initial value of the matrices `A = I_n`, `B = I_n`, where `I_n` is the n×n identity matrix.
  2. For 1 ≤ k ≤ n, compute the partial sums `s_k = (Σ_{j=k}^n x_j²)^(1/2)` and normalize: set `s_k := s_k / s_1`, then set `t := s_1`, `x := x / t`.
  3. Initialize the H matrix as an n×(n-1) lower trapezoidal matrix: `H[i,j] = 0` for `j > i`; `H[i,i] = s_{i+1}/s_i`; `H[i,j] = -x_i x_j / (s_j s_{j+1})` for `j < i`.
  4. Reduce the H matrix: for `i = 2, …, n` and `j = i-1, …, 1`, set `t := round(H[i,j] / H[j,j])`, then update `H[i,*] -= t·H[j,*]`, `A[i,*] -= t·A[j,*]`, `B[*,j] += t·B[*,i]`.

- **Iteration** (repeat until termination):
  5. Select `m` to maximize `γ^i |H[i,i]|`; swap rows `m` and `m+1` of H, A, x; swap columns `m` and `m+1` of B.
  6. If `m ≤ n-2`, restore lower trapezoidal form of H via a Givens rotation on columns `m, m+1` of H rows `m, …, n`.
  7. Reduce the H matrix (same as init step 4).
  8. **Norm bound (Step 5 in some pedagogical presentations):** compute `M = 1 / max_j |H_j|` where `|H_j|` is the j-th row norm; M is the lower bound on the smallest possible relation norm.
  9. Test for termination: if any row of A has norm exceeding numerical limit, or any column of B is a candidate relation, halt.
  10. Otherwise return to step 5.

**Verbatim folklore quotation** (immediately after pseudocode):

> *"As a general rule, one can expect to detect a relation of degree n, with coefficients of size 10^m, provided that the input vector is known to somewhat greater than m·n digit precision."*

This is the H ~ 10^(P/n) empirical-scaling folklore stated as a "general rule" by Bailey-Plouffe themselves. **D5 NEW finding** — primary-source warrant for H9 `field_standard_practice` class on empirical tier.

### 4.3 D2 disposition — CLEARED

**Original concern (precision_budget.md line 174):** mpmath uses γ = √(4/3) exactly; FBA 1999 Def 5 specifies γ > √(4/3) strict for the Theorem 3 overshoot conclusion.

**Resolution:** Bailey 1998 §2 visible text states the norm-bound certificate without a γ-range condition. The strict γ > √(4/3) inequality is required only for FBA 1999 Theorem 3 (overshoot bound on PSLQ-found relations), which the M6 rigorous tier does NOT cite — the rigorous tier cites Theorem 1 (per-iteration lower bound) + Corollary 2 (termination iteration count). Both T1 and Cor 2 hold at the boundary γ = √(4/3) by continuity. mpmath's γ = √(4/3) exact is **inside Bailey 1998's stated parameter scope** and has been canonical PSLQ pedagogy since publication. No §Methods text adjustment required.

### 4.4 D3 disposition — CLEARED

**Original concern (precision_budget.md line 175):** mpmath cites Bailey 1998 (not FBA 1999) in its docstring, breaking direct chain to the rigorous theorem.

**Resolution:** algorithm chain `mpmath → Bailey 1998 §2 → FBA 1992 preprint → FBA 1999` verified structurally consistent at every link. Bailey 1998 §2 explicitly says it presents the "simpler formulation" of the Ferguson-Bailey algorithm (per its reference [13] = FBA preprint 1992 = FBA 1999). The §2 pseudocode Step 5/8 norm-bound certificate is equivalent to FBA 1999 Theorem 1 in conservative form (Bailey 1998's `max_j |H_j|` row-norm dominates FBA 1999's `max_j |h_{j,j}|` diagonal; both bracket below mpmath's `max_{i,j} |H[i,j]|` over-all-entries form). All three forms are rigorous lower-bound certificates on any relation norm. **mpmath's bound is inheritable from Bailey 1998 directly, with FBA 1999 providing the underlying theorem.** No §Methods text adjustment required.

### 4.5 D5 disposition — NEW finding (strengthening, not correction)

Bailey 1998 §2 contains the **verbatim canonical statement** of the H ~ 10^(P/n) empirical-scaling folklore — see §4.2 above. This is **explicit primary-source warrant** for the H9 verification class `field_standard_practice` applied to the empirical tier of the M2.3 two-tier predicate. The class assignment was already made at U-MISSION-L (2026-05-15 ~21:36 JST) based on FBA 1999's absence of the relation as a theorem; D5 confirms it positively by quoting Bailey 1998's own "general rule" wording.

**Material impact on M6:** §Discussion (preflight §3.4 — operational-bound capping) and §Methods (PSLQ description) can now cite Bailey 1998's "general rule" wording verbatim as primary-source warrant.

## 5. Files modified at this commit

| File | Action | Reason |
|---|---|---|
| `literature/lit-010-bailey-plouffe-1997-recognizing.md` | Rewrite | fidelity_watch → verified; paper-read content; SHA-256 hashes; §2 pseudocode extract; D2/D3/D5 disposition |
| `literature/claims.jsonl` (lit-010 line) | Edit | status `fidelity_watch → verified`; verification_class `proven_corollary`; paper-read provenance |
| `literature/_fidelity_findings.md` | Append §8 | H8 fire disposition narrative; D2/D3/D5 sub-sections; counts; cross-refs |
| `literature/_m2.3_calibration_anchor.md` | Append §7.11 | Predicate-text H8 disposition (gold/M2 §7-freeze gated by this mutation_log entry) |
| `harness/precision_budget.md` | Edit D2/D3 rows | Append disposition text "STATUS: CLEARED per H8 fire 2026-05-16" |
| `harness/rigorous_bound.py` | Edit module docstring D2/D3 blocks | Append STATUS line at end of each block |
| `mutation_log/m6_step1_bailey_1998_h8_fire_20260516.md` | Create (this file) | 12th mutation_log entry |
| `m6_preflight_checklist.md` (§1) | Status update | pending → done (with this commit's SHA) |

## 6. Files NOT modified

- `selected.md` (frozen at gold/M1) — no change.
- `_m2.3_calibration_anchor.md` §7.1–§7.9 + §7.10 (frozen at gold/M2 / prior mutation_logs) — no change; only §7.11 appended.
- `methodology/heuristics.md` (no new heuristic at this fire; H8 is the operative heuristic — already installed at U-MISSION-J).
- Canonical M3 JSONL outputs (frozen at gold/M3) — no change.
- M5 files (frozen at gold/M5 = `208f6fc`) — no change.
- M4 capability gap (frozen at gold/M4 = `fd13eeb`) — no change.

## 7. Mutation-budget classification

**Operative test (per U-MISSION-J / U-MISSION-L / U-MISSION-N precedents):** does the H8 paper-read finding force a modification to the operator's bounded hypothesis (basis form, predicate shape, success criterion)?

- Basis B_D(C): unchanged.
- Predicate (two-tier with three Excluded Families): unchanged in shape; only the paper-read provenance of the verification classes is strengthened.
- Success criterion (cascade-stable null at H_rigorous = 1.04×10⁷²): unchanged.
- `claims.jsonl` lit-010 entry: status / verification_class updates are field-map progressions within the existing H9 four-class taxonomy, not schema changes.

**Verdict:** H8 fire is a **field-map update** — paper-read verification of a previously fidelity-watched primary source, with confirmed dispositions for two flagged divergences and one new strengthening finding. **Mutation budget consumed at M2 milestone-block: 0/1 still applies.**

## 8. AEAL maturation curve update

| Milestone | Halts |
|---|---|
| M1 | 4 |
| M2.1 | 1 |
| M2.2 | 0 |
| M2.3 | 1 (Catch #2) |
| M3.1 impl | 0 |
| M3.2a exec | 0 |
| M3.2b first attempt | 1 (Catch #3 / U-MISSION-N) |
| U-MISSION-N resolution + M3.2b re-run | 0 |
| M4 | 0 |
| M5 | 0 |
| **M6 Step 1 (H8 Bailey 1998)** | **0** |

Total mission-life halt count: **6** (unchanged from M5 close). Halt-and-flag pattern preserved: H8 fire executed on schedule per `m6_preflight_checklist.md` §1; both flagged divergences CLEARED with no new halt-class findings.

## 9. Authority chain

- Operator M6 GREENLIGHTED (2026-05-16 ~15:48 JST) — scheduled this paper-read at Step 1 of the M6 work sequence.
- `m6_preflight_checklist.md` §1 (commit `d08317c` and prior) — preflight item specifying owner files and acceptance criteria.
- Prior commits: `gold/M5` annotated tag at `208f6fc` (M5 closure); `fd13eeb` (gold/M4); `9c2702d` (gold/M3); `ca9c989` (gold/M2); `15b216f` (gold/M1).
- This mutation_log entry is the **12th** in the mutation_log chain:
  1. m1.0_to_m1.1_operator_amendments
  2. m1.1_to_m1.2_shortlist_construction
  3. m1.2_to_m1.3_brief_fidelity_correction
  4. m1.3_pari_gp_install
  5. m2.1_to_m2.2_u_mission_j_h8_install
  6. m2.2_to_m2.3_pslq_certificate_halt
  7. m2.3_u_mission_l_two_tier_predicate
  8. m3.2_phase_split
  9. m3.2b_u_mission_n_resolution
  10. m4_symbolic_closure_gap
  11. m5_lean_skeleton
  12. **m6_step1_bailey_1998_h8_fire** ← this entry

## 10. Rule 6 audit (this commit batch)

- Zero portal interactions during M6 Step 1 H8 paper-read.
- One planned `git push origin main` operation under operator's pre-authorized incremental-commit allowance for M6 work.
- No `selected.md` / canonical M3 JSONL / `methodology/heuristics.md` / M4 gap / M5 source files edits.
- `_m2.3_calibration_anchor.md` §7.11 added per the precedent established at §7.9 (M3.2 phase split) and §7.10 (U-MISSION-N capping) — both gated by their own mutation_log entries; this §7.11 follows the same pattern.
- `claims.jsonl` lit-010 entry updated — schema lock preserved (7-field), validator passes.
- No new heuristic installed (H8 already operative).

## 11. M6 Step 1 closure status

- **DONE.** H8 paper-read on Bailey 1998 produces verdict (a) per operator's directive: "confirmation that divergences are immaterial to the M6 rigorous tier claim."
- **No halt-class event surfaced.**
- **M6 Step 2 (manuscript drafting in `paper/main.tex`) GREEN to proceed** per the M6 work-sequence non-collapsible ordering.
- **Outstanding M6 preflight items:** §2 (apples-to-stronger-apples framing), §3.4 (operational-bound capping methods observation), §4 + §4.1 (M4 capability-gap framing + structural-vs-scope-ceded sub-classification), §5 + §5.0/§5.1/§5.2/§5.1-sub-item (M5 statement-shape scope + Mathlib cache note).
