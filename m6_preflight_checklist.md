# M6 Preflight Checklist

Pre-M6-drafting items scheduled during M3.2b execution per operator
U-MISSION-M3.2b-RATIFICATION (2026-05-16 ~10:00 JST).

**Purpose:** ensure no scheduled-but-deferred work is forgotten when M6
manuscript drafting begins. Each item below carries trigger conditions,
provenance, and the §section in M6 it will land in.

**Status convention:** `pending` until M6 drafting starts; `in_progress`
when actively being addressed; `done` when reflected in M6 manuscript
draft and verified via the heuristic class indicated.

**Authority:** these items DO NOT consume mutation budget (they are
field-map updates and framing requirements, not hypothesis changes).
Mutation budget at M2 milestone-block remains 0/1 consumed.

---

## §1 — Bailey 1998 H8 paper-read (rigorous-tier proof-of-bound)

**Status:** `pending` — DO NOT EXECUTE DURING M3 OR M4. Execute during M6 drafting.

**Trigger condition (MUST execute when ALL true):**
- M6 manuscript will cite the rigorous tier (`verification_class = proven_corollary`, H_rigorous = 1.036 × 10⁷²) as proof-of-bound for the EF1-complement null result.
- This is the deferral condition specified in U-MISSION-L: "If M3 produces a result that M6 will cite the rigorous tier as proof-of-bound, then H8 fires on Bailey 1998 before M6 submission."
- Per M3.2a outcome (commit `d55ffbc`), the rigorous tier is established and M6 will cite it. **Trigger is armed; execution is scheduled for M6 drafting phase.**

**H8 paper-read requirements (verbatim from U-MISSION-J H8 wording):**
- Direct reading of the primary source (paper, preprint, supplementary material). Web aggregators, citation databases, and LLM-mediated summaries are not sufficient.
- For paywalled or non-digitized primary sources, mark `verified_independently: false` with the specific blocker and do not propagate the claim into the predicate.

**Specific paper-read scope (two distinct claims):**

### §1.D2 — γ = √(4/3) boundary-case claim

Bailey 1998 (or successor) is the canonical citation for PSLQ's threshold parameter γ ∈ (1, √(4/3)] and the boundary case γ = √(4/3) ≈ 1.1547. The mission's empirical scope claim and rigorous bound derivation both depend on γ being at-or-near the boundary; mpmath's PSLQ implementation chooses γ internally. Paper-read must verify:
- (D2.a) Bailey's exact statement of the γ range.
- (D2.b) Whether the rigorous bound theorems (FBA 1999 Theorem 1 + Corollary 2 invoked in `harness/rigorous_bound.py`) require γ = √(4/3) strictly, γ < √(4/3) strictly, or any γ in the stated range.
- (D2.c) Whether mpmath's chosen γ value (whatever it is internally — needs separate code-trace verification against mpmath sources) satisfies the precondition of FBA Theorem 1 + Corollary 2 as Bailey stated them.

If (D2.c) fails or is ambiguous, the rigorous tier must be downgraded to `field_standard_practice` for the M6 manuscript and the §Discussion must surface the reason.

### §1.D3 — mpmath-cited-source claim

`harness/rigorous_bound.py` derives H_rigorous from observed mpmath verbose-output behavior using FBA Theorem 1 + Corollary 2 as the underlying theorem. mpmath's PSLQ documentation may cite Bailey 1998 as its source paper, OR may cite an FBA 1999 paper, OR neither. Paper-read must verify:
- (D3.a) Whether mpmath documentation explicitly cites Bailey 1998 (and which version — original, errata-corrected, or successor paper).
- (D3.b) Whether mpmath's algorithm matches the algorithm described in the cited paper (or, if cited paper differs from FBA 1999, whether the gap matters for the rigorous bound derivation).
- (D3.c) Whether the FBA 1999 theorem (used in `rigorous_bound.py`) and the algorithm mpmath actually implements are consistent at the level needed for the bound to hold.

If (D3.c) reveals a gap (e.g., mpmath implements PSLQ-PRIMA from a later paper that has different bound-stability properties than FBA 1999 PSLQ), the rigorous tier must be re-derived from the actually-implemented algorithm or downgraded.

**Owner of result:** `_fidelity_findings.md` §7 (new section), and any updates propagated to `harness/rigorous_bound.py` docstring + `_m2.3_calibration_anchor.md` §7.10 (new sub-section, requires mutation_log entry per gold/M2 §7-freeze rule).

**Halt-and-flag class:** if H8 paper-read on Bailey 1998 surfaces a gap, halt M6 drafting and surface as U-MISSION-N (new mission letter) before manuscript submission.

---

## §2 — Apples-to-stronger-apples framing care (M6 §Introduction + §Results)

**Status:** `pending` — DO NOT DRAFT M6 §INTRODUCTION/§RESULTS WITHOUT THIS GUARDRAIL.

**Provenance:** operator U-MISSION-M3.2b-RATIFICATION 2026-05-16 ~10:00 JST verbatim:

> The M6 manuscript framing for H_rigorous = 10⁷² vs BBC H = 10⁷⁰ must be apples-to-stronger-apples, not apples-to-apples. BBC tested EF1 (pure-power, grandfathered) at 10⁷⁰ empirical. This mission tests the EF1-complement at 10⁷⁰ empirical AND 10⁷² rigorous. The contribution is two-tier reporting on a novel basis, not bound-beating on the same basis.

### §2.a — Comparative-claim guardrails

**WHAT THE M6 MANUSCRIPT MUST NOT CLAIM:**

- ❌ "We improve on BBC's bound by 2 orders of magnitude" (this would be apples-to-apples on the same basis; BBC and this mission tested *different* bases).
- ❌ "We extend BBC's null result to higher heights" on the EF1-pure-power basis (we did not test the EF1 basis at all — it is grandfathered out per `selected.md` §2.A).
- ❌ "Our bound exceeds BBC's bound" without naming the basis distinction (creates ambiguity that a reviewer will flag).

**WHAT THE M6 MANUSCRIPT MUST CLAIM:**

- ✅ Two-tier reporting (`field_standard_practice` empirical at H = 10⁷⁰ + `proven_corollary` rigorous at H = 1.036 × 10⁷²) on the **EF1-complement** basis (log K_0, bilinear K_0·c_i for c_i ∈ C, hybrid log+bilinear).
- ✅ The novel-basis contribution: BBC 1997 §4 explicitly named log K_0, (log K_0)(log 2), and "many other forms involving K_0" as **open**. This mission's basis tests entries from that named-open complement.
- ✅ The methodological contribution: two-tier verification class structure under H9 (rigorous + empirical) is novel — BBC's null was empirical-only at the time of publication.
- ✅ The basis-class boundary is explicit. EF1 (pure-power) is BBC-grandfathered prior art; EF1-complement is mission scope.

### §2.b — §Introduction framing requirements

The M6 §Introduction must establish, in this order:
1. The Khinchin-K_0 algebraic-relations problem (general).
2. Prior art:
   a. BBC 1997 §4 Test 1 — pure-power null at H ≤ 10⁷⁰ (EF1; grandfathered prior art).
   b. khinchin-signature-pslq (operator's 2026-04-17 paper) — algebraic-combination relations on the S_n family (EF2; grandfathered prior art).
   c. GKW-method-ceded prior art per `seeds/26 DO-NOT-REENTER` (EF3).
3. The named-open complement: log K_0 row, bilinear K_0·c rows, hybrid log+bilinear combinations (this mission's scope, EF1+EF2+EF3 complement).
4. This mission's contribution: two-tier null on the complement, with rigorous tier exceeding BBC's empirical bound by 2 orders.

The two-tier structure (§3) and the basis-class distinction (§2) must be visible in the abstract, not buried in §Methods.

### §2.c — §Results framing requirements

The §Results numerical claims must always carry:
- The basis class explicit (e.g., "On the EF1-complement basis B_D(C) at D=6, |C|=7, n=15...").
- The verification class explicit (`field_standard_practice` for H_empirical, `proven_corollary` for H_rigorous).
- The PSLQ/lindep stability evidence summary (cascade verdict, identical K iteration count across 4× precision range, gp_lindep agreement).

The §Results should NOT compare to BBC's H = 10⁷⁰ as if it were the same measurement; it must compare as "stronger basis-coverage at equal-or-better bound" with the basis-class footnote.

### §2.d — §Discussion (or §Limitations) requirements

Must explicitly state:
- BBC's EF1 basis was not tested by this mission (grandfathered).
- BBC's algorithm + precision were comparable but not identical to mpmath's PSLQ (mpmath internals depend on H8 paper-read in §1).
- The bound improvement (10⁷⁰ → 10⁷²) is on a different basis, not on the same basis at higher precision.
- Future work: testing EF1+EF1-complement union basis (n=22) at H ≥ 10⁷² would close the apples-to-apples gap, with wall-clock cost increasing as ~22³/15³ ≈ 3.16× per cascade step.

**Owner of result:** M6 manuscript files (when authored). Cross-reference back to this checklist in M6 §Introduction footnote and §Results footnote.

**Halt-and-flag class:** if M6 drafting attempts to claim "we improved on BBC's bound" without the basis-class distinction, halt drafting and re-read this §2 before continuing.

---

## §3 — Other M6-deferred items (open list)

### §3.1 — selected.md re-anchor (if applicable)

If M6 cites `selected.md` §2.A (S_n grandfathered family) as prior art, verify that the `selected.md` content reflects the operator's 2026-04-17 paper as the authoritative citation. `selected.md` is frozen at gold/M1; any citation in M6 must match the frozen content.

**Status:** `pending`.

### §3.2 — Reproducibility appendix

M6 reviewers will likely request reproducibility instructions. Compose appendix referencing:
- Repository commit `d55ffbc` (M3.2a) and the M3.2b commit (TBD when sweep completes).
- Exact command: `python harness/sweep.py --m32-primary-measurement --m32-primary-greenlighted` (M3.2a) and `python harness/sweep.py --full --m32-full-greenlighted` (M3.2b).
- Wall-clock observed: 66.5 min (M3.2a) + (TBD) min (M3.2b).
- mpmath version, Python version, PARI/GP version (capture during M3.2b run for completeness).

**Status:** `pending`.

### §3.3 — JSONL data deposit

If M6 venue requires data deposit (Zenodo, Dryad, or similar), upload the canonical JSONL files (m32a + m32b) with a versioned identifier matched to the M6 submission.

**Status:** `pending`.

---

## Maintenance protocol

When an item activates:
1. Update item `Status:` from `pending` to `in_progress`.
2. Open a corresponding SQL todo in this session's database.
3. Execute the work, citing the section number in commit messages.
4. When done, update `Status:` to `done` with a short result summary and commit hash citation.

When a new pre-M6 item is identified (during M3.2b review, M4, or M5):
1. Add as a new §X.N sub-section here (NOT in mutation_log/, unless it's a hypothesis change).
2. Cite the operator directive that scheduled it (or the heuristic that surfaced it).
3. Set initial `Status: pending`.

---

**Provenance footer:**
- Created: 2026-05-16 ~10:05 JST during M3.2b execution.
- Authority: operator U-MISSION-M3.2b-RATIFICATION 2026-05-16 ~10:00 JST.
- Predicate anchor: `literature/_m2.3_calibration_anchor.md` §7 (M2.3 ratified at gold/M2, commit `ca9c989`).
- Heuristic anchors: H8 (paper-read verification), H9 (verification classes), H6 (no-double-counting prior art).
