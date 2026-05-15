# Survey-set #26 (Gauss–Kuzmin) — Reframings Parked as Future Work

**Park date:** 2026-05-15 ~18:00 JST
**Park reason:** Operator-instructed park (U-MISSION-A-FOLLOWUP, 2026-05-15 ~18:00 JST). Direct version of #26 was DROPPED at M1.1 due to severe content overlap with `Finite-Depth Transient Rigidity` manuscript (active SIARC track) — same GKW transfer operator; same eigenfunction-rigidity question family.
**Audit reference:** `targets/overlap_audit_26_gauss_kuzmin.md`
**Binding rule:** **DO NOT re-enter this mission cycle.** See `seeds/README.md`.

---

## Why these reframings exist

The audit for #26 found that the *direct* problem (Gauss–Kuzmin convergence rate
constant identification + sharper second-order asymptotics for the Gauss map's
transfer operator) overlapped on the **content axis** with operator's active
`Finite-Depth Transient Rigidity` manuscript, not just on machinery. A positive
result on the direct problem would muddy attribution between the two tracks.

Two reframings were drafted during the audit that *would* sidestep the overlap.
Operator declined to ride either reframing this cycle and instructed parking.

---

## R-1: Non-Gauss CF map (nearest-integer CF, slow CF, by-excess CF)

**Statement.** Investigate the transfer-operator spectrum and convergence-rate
constants for a continued fraction map T_α : [0,1) → [0,1) where T_α is **not**
the standard Gauss map x ↦ {1/x}. Candidates:

- T_NI (nearest-integer CF): x ↦ |1/x − ⌊1/x⌉|. Transfer operator differs from
  Gauss-Kuzmin-Wirsing (GKW); known eigenvalue λ_NI ≠ λ_GKW.
- T_slow (Farey / slow CF map): x ↦ x/(1−x) on [0,1/2], x ↦ (1−x)/x on [1/2,1).
  Different spectral theory; ergodicity properties known but constants are not
  PSLQ-fingerprinted in the literature.
- T_by-excess: x ↦ ⌈1/x⌉ − 1/x. Transfer operator has different invariant
  density than Gauss; convergence rate constant uncatalogued.

**Why this dodges the overlap with FDR.** FDR studies the *Gauss* GKW operator
on a *finite-depth* eigenfunction sub-space. R-1 changes the operator entirely.
Different transfer operator ⇒ different invariant density ⇒ different rigidity
question ⇒ no shared-content collision.

**Why parked, not pursued.** Three reasons:
1. Each of T_NI, T_slow, T_by-excess has its own literature that operator has not
   yet surveyed at M2.1 depth. A future cycle should treat R-1 as a fresh M1.1
   candidate with its own machinery audit.
2. The connection to operator's PSLQ machinery is solid (constants are real
   numbers; FP-rejection well-defined) but the connection to operator's PCF /
   Painlevé tooling is weaker than for some other M1.1 entries. Reusability
   would land at 6–7, not 9.
3. Selecting R-1 within the current cycle would functionally re-instate #26 via
   a syntactic dodge, even though the spirit of operator's "drop #26" directive
   was to take CF-map dynamics off the table this cycle. Honest read: park.

**Future-cycle re-entry condition.** R-1 may be considered in a *later* relay
mission *if and only if* the FDR manuscript is either accepted or formally
withdrawn (i.e., the attribution-muddying risk is resolved). Until then,
operator should treat R-1 as on a hold parallel to the GK direct problem.

---

## R-2: Large-deviation bounds on partial-quotient sums

**Statement.** Investigate large-deviation upper bounds for sums of partial
quotients S_n(x) = a_1(x) + a_2(x) + … + a_n(x) of the regular continued
fraction expansion of x ∈ [0,1).

Known: Khinchin (1924) proved S_n / (n log n) → 1/log 2 in probability (NOT
almost-sure; the almost-sure limit does not exist). Diamond–Vaaler (1986) gave
refined moments. Recent: Kesseböhmer–Slassi (2008) and others have studied
fluctuations.

**Falsifiable sub-question.** For a specific class of irrationals (e.g., those
of constant type, or those satisfying a Brjuno-type condition), can one prove a
*concrete* large-deviation rate function I : ℝ_+ → ℝ_+ such that
ℙ(S_n / (n log n) > 1/log 2 + δ) ≤ exp(−n I(δ))? PSLQ-fingerprint candidate
values of I at specific δ against special-value bases (Catalan G, ζ(3), log
constants).

**Why this dodges the overlap with FDR.** FDR studies eigenfunctions / spectral
gaps of the GKW operator. R-2 studies *distributional* properties of partial
quotients viewed as random variables under the Gauss measure. Different
operator-theoretic vs ergodic-theoretic question; the techniques are related
(transfer-operator perturbation methods) but the *content* is large-deviation
theory not rigidity.

**Why parked, not pursued.** Three reasons:
1. Large-deviation theory uses Legendre transforms and Cramér-type analyses
   that are NOT in operator's confirmed machinery base (post-probe). Operator
   would need to deploy a fresh capability or rely on PSLQ alone, which only
   FP-rejects rate values rather than proving rate-function structure.
2. The "specific class of irrationals" sub-question scope-creeps quickly:
   constant-type → Brjuno-type → Roth-type → … each is a distinct project.
   M1.2 within-cycle scope-creep risk is high.
3. The connection to FDR via "transfer-operator perturbation methods" is
   tighter than R-1's connection; even though the *question* is different, the
   *technique* family is closer and reviewers may conflate them. Honest read:
   higher overlap risk than R-1, lower upside, definitely park.

**Future-cycle re-entry condition.** R-2 may be considered in a *later* relay
mission *if and only if* (a) FDR attribution risk is resolved and (b) operator
has deployed at least one large-deviation-theoretic tool in a separate cycle
(so reusability scores credibly land ≥ 6).

---

## Joint disposition

Both R-1 and R-2 are *legitimate* future-work candidates. Neither is appropriate
for the current cycle. They are recorded here to:

- Prevent operator's "drop #26" instruction from being later misremembered as a
  permanent drop when in fact the direct problem was dropped but reframings
  were considered and parked.
- Preserve the intellectual trail in case future M1.1 surveys revive them.
- Document the audit-and-park process as a reusable pattern for future overlap-
  audit-fail entries (a parked reframing is a possible disposition class).

**No further action this cycle.** Do not score these in M1.2. Do not include
them in the primary or contrast shortlists. Do not advance them to M2.
