# Target Selection — Khinchin's constant K_0

**Mission:** unsolved-relay
**Milestone:** M1.2 (rank-and-select) close
**Selected by:** Operator directive **U-MISSION-F** (2026-05-15 ~18:16 JST)
**Target:** Khinchin's constant K_0
**Source shortlist row:** Primary #3 / Contrast #2 in `targets/M1.2_shortlists.md`
**Score profile (judgment-class):** T=8, R=9, P_pos=8, P_neg=7, I=9 → C_primary=34, C_contrast=33

---

## §1 The problem

Khinchin's constant K_0 ≈ 2.6854520010653064453097148...

is the almost-everywhere geometric-mean limit of the partial quotients of regular
continued-fraction expansions of real numbers (Khinchin 1934): for almost every
irrational x with simple continued fraction [a_0; a_1, a_2, …],

  lim_{n→∞} ( a_1 · a_2 · … · a_n )^{1/n}  =  K_0,

a constant *independent* of x on the full-measure set. Despite the constant being
explicitly computable to thousands of decimal digits via classical product
expansions (Khinchin's original formula; Bailey–Crandall accelerated series), the
**arithmetic nature** of K_0 is **open**. Specifically:

- **Irrationality:** not proved (no published proof of K_0 ∉ ℚ as of M1.2 close).
- **Algebraicity:** not proved (no published proof of K_0 ∉ \overline{ℚ}).
- **Transcendence:** conjectured, not proved.

The standard expectation in the transcendence literature is that K_0 is
transcendental, but every published attack on irrationality (let alone
algebraicity) has stalled at infrastructure questions, not at a clean obstruction.
The M2.1 literature ledger will catalog the state of the art.

---

## §2 Bounded sub-question (M1.2 form, post-U-MISSION-G refinement; subject to further M2.3 tightening)

> **Q.** Test, at 500 dps via PSLQ with the M3.1 cascading-precision harness,
> for integer relations among the hybrid basis
>
>     B_D(C) = { 1, K_0, K_0^2, …, K_0^D, log K_0 } ∪ { K_0 · c : c ∈ C }
>
> where C is a finite named-constant set (concrete members specified in the
> M2.3 success predicate; anticipated subset of { π, e, log 2, ζ(2), ζ(3),
> G, γ }), with degree bound D ≤ 6 and integer-coefficient height bound H
> specified in M2.3.

**Falsifiability and machine-checkability.** For any fixed (D, H, C) within the
Brief §M3.2 caps (96h wall-clock, 1000-iter), the bounded sub-question has
exactly two terminal outcomes:

- **Positive terminal:** PSLQ returns an integer tuple
  (a_0, a_1, …, a_D, a_log, {b_c}_{c∈C}) with max |·| ≤ H satisfying

      a_0 + a_1 K_0 + a_2 K_0^2 + … + a_D K_0^D + a_log · log K_0 + Σ_{c∈C} b_c · (K_0 · c) ≈ 0
      at 500 dps,

  with at least one a_i (i ≥ 1) or a_log or some b_c nonzero. The candidate is then routed through
  the M3.1 cascading-precision harness:
  - Re-verification at 2× and 4× precision (1000 dps, 2000 dps) — H1 entry condition.
  - Second-leg verification via `gp lindep` shell-out (per U-MISSION-D's
    declination of python-flint, `gp lindep` is the canonical 2nd library here).
  - PSLQ false-positive rejection bound at target precision per H1's
    coefficient-magnitude regime.

  Only after all three legs pass does the candidate become a `supported` claim
  in `claims/` under the AEAL seven-field schema.

- **Negative terminal:** at the (D, H, 500 dps, 96h, 1000-iter) caps, PSLQ
  returns no relation surviving the harness. The empirically-rejected (D, H)
  region for K_0 algebraic relations against B_D(C) is then extended, with the
  height-precision overshoot bound recorded per H1. This extension is
  publishable as a ruling-out / FP-rejection result in the Math.Comp /
  Experimental Mathematics tier (Bailey–Borwein literature precedent).

Both terminal outcomes are first-class AEAL deliverables per Brief §0.3.

**Why this is the right scope for AEAL.** A sub-question of the form "does K_0
admit *any* algebraic relation" is unbounded and therefore not falsifiable
under the §M3.2 caps. Bounding by (D, H, C) and naming the hybrid basis
B_D(C) makes the question concrete, the M3.1 verification harness makes the
answer machine-checkable, and the §2.A exclusion below cleanly delineates the
question from operator's prior PSLQ work on the signature-statistic family.

### §2.A Explicit exclusion (non-overlap with prior work)

The signature statistic S_n and its variants { log S_n, S_n − K_0, log n } on
π's continued-fraction partial-quotient sequence are **explicitly excluded
from C** in the basis B_D(C) above. That coordinate family was tested under
AEAL discipline in operator's prior work

    papanokechi/khinchin-signature-pslq    (released 2026-04-17, MIT, public)

which returned a precision-controlled null result at 300 dps base / 600 dps
confirmation, maxcoeff = 10³, 546 attempts, with a wide-cap diagnostic at
maxcoeff = 10⁶ producing only artefacts (T3: 1 hit, T7: 90 hits, vanishing
under conservative cap). The Discussion section of that paper identifies
**algebraic-combination relations of K_0 with other named constants** as the
natural extension that is *out of scope of the signature paper but open for
the field*. The present bounded sub-question implements precisely that
extension under the same AEAL discipline. The signature paper is cited as
the **legitimacy anchor** for this M2–M6 program and will be the primary-tier
prior-art entry in `literature/claims.json` per H6 + the M2.1 literature ledger.

The full 3-axis overlap audit (content / machinery / attribution) is in
`targets/overlap_audit_khinchin_signature_pslq_prior_work.md`. Verdict at
audit close: content DISTINCT, machinery HIGH-overlap, attribution
MITIGABLE-via-citation.

---

## §3 One-paragraph justification

Khinchin K_0 was selected from the M1.2 primary shortlist (rank #3) and is
the second entry in the contrast shortlist (rank #2). Its R=9 reflects exact
fit with the confirmed canonical machinery base (mpmath 500 dps + built-in
PSLQ); its I=9 reflects zero overlap with the R1 / Painlevé III queue (PSLQ
on a real number is operator-orthogonal to PCF spectral fingerprint or
Painlevé III chart-map work); P_pos=8 reflects the high publishability of
any *positive* algebraic relation for K_0 (Acta-adjacent; though unlikely);
P_neg=7 reflects the well-precedented FP-rejection range-extension
publishability (Bailey 1988, Bailey–Borwein 1997, Sebah–Demichel 2008). The
C_primary − C_contrast gap of 1 makes Khinchin a *hedged* bet relative to
Catalan G (C_primary=35, C_contrast=34, gap=1, near-identical hedge but with
G having stronger flagship recognition and Khinchin having stronger CF-track
name-recognition for operator). Operator selected Khinchin over Catalan,
which is consistent with operator's CF-adjacent reputation profile and the
mission's stated independence-from-R1 framing — Khinchin K_0's CF-origin
provides *thematic* coherence with operator's track without *content*
collision (the K_0 numerical value is not a transfer-operator eigenfunction;
no FDR / GKW machinery is touched).

---

## §4 What is NOT being claimed by this selection

- **NOT** claiming K_0 will be proved irrational, algebraic, or transcendental
  in this mission. The mission's scope is bounded by (D, H, 500 dps).
- **NOT** claiming Bailey-class numerical infrastructure parity. Operator has
  mpmath 500 dps + built-in PSLQ + `gp lindep` shell-out. Operator does
  **not** have arb / flint / fpylll / sage (per `capability/machinery_base_confirmed.md`).
  If the M2.3 success predicate requires interval arithmetic that mpmath +
  gp cannot deliver, that triggers a Capability Gap per Brief §0.2 and U-MISSION-D
  declination — **no retrofit install**.
- **NOT** claiming a new K_0 product expansion or numerical formula. The
  mission consumes existing K_0 high-precision computations and probes
  algebraic relations against them.
- **NOT** invoking any "AI-breakthrough logic" / "structural gap" / "forced
  invariant" / "consistency-driven conjecture generation" framing (operator
  rejection 2026-05-15 ~18:16 JST). All inference proceeds under AEAL
  seven-field claim schema; informal heuristics are subordinated per
  `methodology/heuristics.md`.

---

## §5 Refinement clause (per U-MISSION-F) — and refinement record

Operator's U-MISSION-F directive allows the M1.2-form sub-question to be
**refined** if a sharper variant emerges from the M2.1 literature ledger.
Concretely:

- If M2.1 surfaces a *specific* ansatz class (e.g., relations involving K_0
  and ζ(2), or K_0 and log 2, that prior PSLQ attempts have not ruled out
  at extended height), the M2.3 success predicate may target that class.
- If M2.1 surfaces a known PSLQ bound (D*, H*) due to a prior author
  (Bailey, Borwein, Plouffe, etc.), the M2.3 success predicate may set
  (D, H) > (D*, H*) for an extension result.
- If M2.1 surfaces an *irrationality-measure* or *Liouville-bound* hook
  that would let a PSLQ scan certify irrationality conditional on a clean
  failure pattern, the M2.3 success predicate may include such a clause
  *with the conditionality stated explicitly per AEAL*.

Any refinement that **materially changes scope** requires a `mutation_log/`
entry per Brief §7. A purely tightening refinement (smaller D, smaller H,
same shape of question) does NOT require a mutation entry.

### §5.A Refinement record — U-MISSION-G (2026-05-15 ~18:45 JST)

| Field | Value |
|---|---|
| **Refinement event** | Pre-freeze §2 refinement triggered by late-catch overlap audit |
| **Triggering audit** | `targets/overlap_audit_khinchin_signature_pslq_prior_work.md` |
| **Operator authority** | U-MISSION-G selection of Option A (G1) |
| **Refinement class per H5** | Tightening + scope-narrowing (NOT scope-changing) |
| **mutation_log entry needed for §2 refinement?** | **No** (per H5 tightening clause) |
| **What changed in §2** | (a) abstract "algebraic relation of degree ≤ D and height ≤ H" replaced by concrete hybrid basis B_D(C); (b) explicit §2.A exclusion of S_n / log S_n / S_n − K_0 / log n family ceded to prior work; (c) prior paper named as legitimacy anchor for M2–M6. |
| **Operator-proposed wording** | Honored in structural intent (3 required elements: name the basis, name the exclusion, cite the prior paper). CLI amended for technical precision: added the explicit constant `1` in B_D(C) so PSLQ can detect inhomogeneous relations; named anticipated C-elements; stated the linear-form expansion of the relation; specified the harness routing per H1; preserved log K_0 from operator's wording (transcendence-relation-pattern relevance noted in §4 negative-claim list). |
| **What did NOT change** | Target (Khinchin K_0), shape of the question (PSLQ-detectable algebraic relation under (D, H, 500 dps) caps), success predicate placeholder location (M2.3), Brief §M3.2 caps. |

### §5.B Refinement *of the §5.A refinement* — explicit future-action notes

Per operator's U-MISSION-G post-script: in M2.1, `khinchin-signature-pslq` is
to be entered as a **primary-tier** prior-art citation in `literature/claims.json`
with `verified_independently: true` (operator authored the paper). The
signature paper's Discussion section is to be treated as a **structural
anchor** for the M2.3 success predicate, NOT as a competitor.

---

## §6 What lands at M1.3 Gold Freeze G1

Once operator approves the repo-creation step (U-MISSION-B — **APPROVED
2026-05-15 ~18:28 JST**, ratified 18:45 JST), the M1.3 freeze snapshots:

- `targets/triage.json` (28 rows)
- `targets/survey_set.md` (with M1.1 amendments-applied footer)
- `targets/_M1.1_triage_metadata.json`
- `targets/M1.2_scoring.json`, `targets/M1.2_shortlists.md`,
  `targets/build_m1_2_shortlists.py`
- `targets/selected.md` (this file — post-U-MISSION-G refinement)
- `targets/_M1.1_construction_log.md`
- `targets/literature_recheck_18_levy_constant.md`
- `targets/overlap_audit_23_stanley_plane_partition.md`
- `targets/overlap_audit_26_gauss_kuzmin.md`
- `targets/overlap_audit_khinchin_signature_pslq_prior_work.md` (the
  U-MISSION-G audit artefact)
- `targets/triage_schema.json`, `targets/triage_validator.py`,
  `targets/build_triage_m1_1.py`
- `capability/probe_results_20260515.md` (v1 with §AMENDED block;
  preserved per operator directive)
- `capability/probe_results_20260515_v2.md` (v2; supersedes v1 on
  PARI/GP row)
- `capability/machinery_base_confirmed.md`
- `capability/independent_second_library.gap.md` (U-MISSION-H trigger
  artefact; remains in repo as audit trail of the false positive even
  though it is now resolved)
- `capability/pari_gp.available.md`, `capability/mpmath.available.md`,
  `capability/gmpy2.available.md`, `capability/numpy.available.md`,
  `capability/sympy.available.md`, `capability/lean_lake.available.md`,
  `capability/mathlib4.available.md` (H7-mandated retroactive
  capability records, one per claimed-present capability)
- `mutation_log/m1.0_to_m1.1_operator_amendments_20260515.md`
- `mutation_log/m1.1_to_m1.2_shortlist_construction_20260515.md`
- `mutation_log/m1.2_to_m1.3_brief_fidelity_correction.md` (the
  congruent-relay-404 fidelity correction)
- `mutation_log/m1.3_pari_gp_install_20260515.md` (PARI/GP install
  event; non-mutation per H5 Brief-fidelity-corrections clause)
- `seeds/` (R-1, R-2 parked future-work)
- `methodology/heuristics.md` (subordinated frame; H1–H7 including
  H6 namespace-audit per U-MISSION-G and H7 functional-verification
  per U-MISSION-H)
- `_M1.0_first_action_log.md`, `README.md`
- `LICENSE` (MIT, code), `LICENSE-DOCS` (CC-BY 4.0, docs/data)
- `.gitignore`
- `env/M1.lock` (environment snapshot, generated at freeze time,
  including gp 2.18.1 development build identity)

After `tag gold/M1`, `targets/selected.md` becomes IMMUTABLE without a
`mutation_log` entry per Brief §M1.3.

---

## §7 Acknowledgments and traceability

- **Survey-set row:** #15 (Khinchin's constant K_0 — rationality / algebraicity)
  in `targets/survey_set.md`.
- **Triage row index:** 13 (0-indexed) in `targets/triage.json`.
- **Machinery requirement:** `["mpmath_500dps", "PSLQ_builtin",
  "sympy_nsimplify"]` (all `machinery_available_locally=True`).
- **AEAL risk:** medium (transcendence-statement-class; risk arises from
  conflating PSLQ-detection with proof, NOT from machinery; mitigated by the
  bounded (D, H) scope and the §4 negative-claim list).
- **Selection authority:** Operator (per U-MISSION-E + U-MISSION-F).
- **CLI's role:** writer of this file; *not* selector.
