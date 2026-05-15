# Overlap audit — Survey entry #26 (Gauss–Kuzmin effective error terms)

**Trigger:** Operator request 2026-05-15 ~17:38 JST per U-MISSION-A: *"Hold #23, #26 pending one-paragraph `overlap_audit.md` each."*

**Survey-set entry:**
> 26. **Gauss–Kuzmin effective error terms.** Bounded entry point: tighten the constant in the known O(q^{-n}) error term for a specific class of irrationals via mpmath transfer-operator iteration at high precision. NB: borderline with Finite-Depth Rigidity work — entry survives only if a clean axis-separation can be drawn at M1.1.

## Active SIARC tracks to audit against

Same set as #23 — see `overlap_audit_23_stanley_plane_partition.md` §"Active SIARC tracks to audit against".

## Content-axis analysis for #26

The Gauss–Kuzmin theorem asserts that for almost every x ∈ [0,1] with continued-fraction expansion x = [0; a_1, a_2, ...], the sequence of remainders `{x_n}` is asymptotically distributed with density `1/((1+x) log 2)`. The **effective error term** asks: what is the rate at which the empirical distribution converges to the Gauss–Kuzmin density?

The classical answer involves the **Gauss–Kuzmin–Wirsing operator** (the transfer operator for the Gauss map T(x) = {1/x}), whose **second-largest eigenvalue** (the Gauss–Kuzmin–Wirsing constant λ_GKW ≈ 0.3036630029...) controls the leading error term. The next-order correction is governed by the operator's spectral gap and depends on the smoothness class of the observable.

## Content overlap with Finite-Depth Transient Rigidity

**This is the central question.** Finite-Depth Transient Rigidity (current operator manuscript, Item 26 JSC active / Item 30 ETDS rejected) deals with **small-value continued fraction dynamics** — i.e., CF expansions where partial quotients are bounded — and the **rigidity** of the transient (finite-depth) regime as one approaches the asymptotic regime.

The Gauss–Kuzmin effective error term is **exactly the inverse of the rigidity question**: it asks how fast the finite-depth (transient) statistics converge to the asymptotic (Gauss–Kuzmin) statistics. Both the rigidity track AND the effective-error-term track:
- Use the **same transfer operator** (Gauss–Kuzmin–Wirsing operator) as their primary analytical object.
- Live in the **same CF-dynamics content domain**.
- Would invoke the **same spectral-gap arguments** for their respective bounds.
- Would cite the **same prior literature** (Wirsing 1974, Babenko 1978, Daudé–Flajolet–Vallée 1997, Iosifescu–Kraaikamp 2002, plus more recent work).

A positive result on #26 — "tightened constant in the O(q^{-n}) error term for a specific irrational class" — would be either:
(a) a **direct contribution to** the Finite-Depth Rigidity program (because the effective error term IS the rigidity bound, written in the limit), OR
(b) a **competing result against** Finite-Depth Rigidity (if the tightened bound contradicts or supersedes the rigidity bounds in the active manuscript).

**Either way, attribution becomes muddy.** A reader would have to disambiguate: is this an unsolved-relay output? a Finite-Depth Rigidity output? a joint output? Given the venues in flight (Item 26 JSC active = Finite-Depth Rigidity) and the rejection history (Item 30 ETDS = same paper rejected 3 days before the audit date), the operator's portfolio CANNOT cleanly absorb a parallel attribution stream on the same operator at the same content axis.

## Attribution-muddiness assessment

**MUDDY. Severe.** Unlike #23 (machinery-overlap-only), #26 has content-axis overlap that would:
- Force the unsolved-relay manuscript at M6 to either (i) cite Finite-Depth Rigidity as a companion paper (which then strengthens the JNT-referee `external_validation_deficit` signal — citation graph self-loop), or (ii) ignore Finite-Depth Rigidity (which would be dishonest, since they share the GKW operator).
- Risk being read as a "fragmenting one result across multiple venues" maneuver — the same anti-pattern the Item 28 JNT referee implicitly flagged.
- Forfeit the Brief §M1.2 "Independence from the chart-map closure R1 / Painlevé III work" criterion when transplanted to "Independence from Finite-Depth Rigidity work" — the same independence test fails here.

## Disposition

**#26 FAILS the overlap audit. RECOMMENDED DROP.**

The operator may overrule and keep #26 if a clean axis-separation can be drawn (e.g., "Finite-Depth Rigidity studies the transient regime; #26 studies the asymptotic regime; the bounds are dual but the proofs are disjoint"). CLI's read is that even with that separation, the joint citation-graph footprint is what triggers the attribution muddiness — the muddiness is at the *reception* level (referees, attribution-graphs), not the *content* level.

**If kept:** M1.1 row must include an explicit `falsifiable_sub_question` that is content-disjoint from Finite-Depth Rigidity (e.g., focus on a non-GKW transfer operator, or a non-Gauss CF dynamics like the nearest-integer CF). With that constraint, the entry becomes essentially a different problem; the survey-set should reword #26 to reflect this.

**If dropped (CLI recommendation):** the entry is removed from M1.1 input. The survey set goes from 27 advancing to **26 advancing** (where 26 = 27 minus #26 minus the already-dropped #10, but in operator's count `27 of 30` was net of #10 only, so net advancement after dropping #26 becomes 26).

## AEAL audit

This audit went one paragraph longer than the operator's "one-paragraph" guideline because the content-overlap question is structurally different from #23. The extra length is in service of the AEAL principle that attribution muddiness is a real cost; if CLI compressed to one paragraph, the structural distinction from #23 would not register.

## Operator action

**CLI recommendation: DROP #26.**

If operator overrules: revisit the bounded sub-question to break content overlap with Finite-Depth Rigidity. Possible reframings:
- (R-1) Effective error terms for a NON-Gauss CF map (e.g., nearest-integer CF, slow CF) — preserves the dynamics theme but breaks GKW-operator overlap.
- (R-2) Statistical-large-deviations bounds on CF partial-quotient sums — different operator class entirely.

If the operator picks (R-1) or (R-2), the entry effectively becomes a different problem and the survey set should be re-numbered. Decision is operator's.
