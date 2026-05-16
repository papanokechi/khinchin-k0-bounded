# Handoff packet — unsolved-relay mission on Khinchin's constant K₀

**Status:** **STRUCTURE-ONLY PRE-POPULATION.**
This file is the Brief §M6.3 handoff substrate, pre-populated against the manuscript draft at `paper/main.tex` HEAD `e0defff`. The plain-language summary and the recommended-next-venue block are placeholders; they will be filled in only after operator review of the M6 manuscript and operator decision on the venue axis.

The completed companion document is `handoff/agent_health_score.md`, which carries the concrete four-axis health-score data.

---

## §1 Plain-language summary

> **[STRUCTURE-PLACEHOLDER]**
> This subsection is intentionally not pre-drafted. It will be authored by the operator (or by the CLI under explicit operator direction) after the M6 manuscript receives operator-visible ratification or revision.
>
> Target length: ~300–400 words, accessible to a mathematically literate reader without specialist PSLQ or transcendence-theory background. The substrate available for drafting:
>
> - Bounded sub-question: see `targets/selected.md` §1 (frozen at `gold/M1`) — "is there a PSLQ-detectable integer relation in the hybrid basis `B_D(C) = {1, K_0, K_0^2, …, K_0^6, log K_0} ∪ {K_0·c : c ∈ C}` at D ≤ 6, dps ≥ 500, with C = {π, e, ln 2, γ, ζ(2), ζ(3), G}?"
> - Result (one sentence): every one of the 65 sub-bases tested under the M3.1 two-tier predicate returns a cascade-stable null at H_rig = 1.0361 × 10⁷² (FBA Theorem 1 + Corollary 2 derived; verification class `pc`).
> - Bounded scope distinction (the apples-to-stronger-apples framing): see `m6_preflight_checklist.md` §2 and `paper/main.tex` §1 lines 114–267. This sub-question is a *complement-scope* extension of BBC 1997's primary-tier and is *not* a competitor to the signature paper or to BBP-class results.
> - Capability gap (the M4 outcome): `K_0`'s transcendence status is the major open question; the mission documents this and does not paper over it.
>
> Drafting guidance: avoid "we prove" / "we show that K_0 is …" phrasing; use "the mission documents …" / "the bounded sub-question's answer at this scope is …" framing.

---

## §2 Agent Health Score retrospective

The concrete-data view is `handoff/agent_health_score.md`. The four axes per Brief §M6.3:

| Axis | Score | Source |
|---|---|---|
| 1. Claim-to-sweep ratio | 5 load-bearing claims / 65 candidates ≈ 0.077 (conservative) | `agent_health_score.md` Axis 1 |
| 2. Reproduce-command coverage | 100 % (20 / 20 literature; every §3 numerical claim) | `agent_health_score.md` Axis 2 |
| 3. Capability-gap-documentation rate | 100 % (2 gaps documented; 0 concealed) | `agent_health_score.md` Axis 3 |
| 4. Literature-fidelity surfacing rate | 100 % (4 catches surfaced + resolved; 0 concealed) | `agent_health_score.md` Axis 4 |
| (aux.) Halt-and-flag rate | 100 % (6 halts surfaced; 6 heuristics installed) | `agent_health_score.md` "Halt-and-flag retrospective" |

**Top-line:** the four honesty axes are at the design ceiling. The single soft observation is the M4 FUNDAMENTAL capability gap; this is a *finding*, not a process failure.

---

## §3 Recommended next-venue assessment

> **[OPERATOR-DECIDES — DO NOT FILL]**
> This block is intentionally not pre-drafted by the CLI. Per Brief §M6.3 and per the operator's M6 Step 2 pre-population directive (2026-05-16 ~17:11 JST): *"Do not fill the venue recommendation; operator decides. Structure only."*
>
> The operator will fill this block after reviewing the manuscript at `paper/main.tex` HEAD `e0defff`. Substrate available to the operator:
>
> - Slot 216 Opus consultation verdict on venue ceiling (in `siarc/control-center/prompts/216_...EXECUTED.txt` §9, Acta Arith / JNT / Ramanujan J band; NOT Bull AMS / Compositio).
> - SIARC submission ledger (`siarc/submitted/submission_log.txt`) — Item 28 JNT (rejected 2026-05-15) and Item 31 RMSB (rejected 2026-05-16) both cover the *spectral-classes* manuscript and are NOT in unsolved-relay scope; their rejection signals (`comparative_priority`, `external_validation_deficit`, `scope_fit`) inform but do not dictate the K₀-bounded venue.
> - The Khinchin K₀ manuscript is structurally different from the spectral-classes manuscript: it is a *bounded-null* result with two-tier (rigorous + empirical) predicate calibration and Lean 4 statement-shape encoding; this profile fits *experimental-mathematics* and *computational-number-theory* venues better than pure-number-theory venues.
> - Candidate venues (operator can endorse, modify, or replace):
>   - *Mathematics of Computation* — BBP's natural home, paper-read-verified bibliographically (`lit-002`, `lit-009`).
>   - *Experimental Mathematics* — bounded-null + reproducibility-appendix natural fit.
>   - *Journal of Number Theory* — already explored at Item 28; operator may want to defer to allow a citation gap.
>   - *Integers: Electronic Journal of Combinatorial Number Theory* — open-access, lower citation barrier, fast turnaround.
>   - Zenodo deposit + arXiv preprint (operator pseudonymity stance: see §5 below) — venue-independent, often the right first step before formal journal submission.

---

## §4 Manuscript review checklist for the operator

When the operator reviews `paper/main.tex` HEAD `e0defff`, the six specific structural reads the operator named are pre-mapped to line ranges:

| # | Read | Section | Line range |
|---|---|---|---|
| 1 | §Intro two-anchor framing (signature paper precedes BBC) | §1 Introduction | 114–267 |
| 2 | §Methods H9 Bailey 1998 §2 "general rule" verbatim | §2.4 | 402–453 |
| 3 | §Results two-tier table (Euclidean-norm + height comparison) | §3.2 | 649–695 |
| 4 | §Discussion M4 capability gap (6 + 1 sub-classification) | §4.3 | 837–887 |
| 5 | §Discussion operational-bound capping (Bailey hedge) | §4.2 | 808–836 |
| 6 | §Appendix B AEAL methodology | App B | 967–1097 |

Additionally, the CLI surfaces one minor counting note for operator attention:

> **Note for operator review.** `paper/main.tex` §B.1 line 1025 currently reads: *"Six of these ten (H6–H10) were installed mid-mission..."*. The interval H6–H10 is **five** heuristics, not six. This appears to be a typo for *"Five of these ten"*. No CLI fix has been applied; per the operator's pattern instruction ("revisions, if any, will arrive as specific delta language"), the CLI surfaces this for operator-directed revision rather than self-applying. If the operator concurs, the delta is `s/Six of these ten/Five of these ten/` at line 1025.

---

## §5 Pre-Zenodo deposit decisions for the operator

The pre-populated Zenodo metadata draft is at `handoff/zenodo_metadata.json`. Two decision points are flagged for the operator before any deposit:

### D-zenodo-orcid-pseudonymity-stance

The just-applied paper byline (commit `e0defff`) includes the operator's ORCID `0009-0000-6192-8273`. The SIARC submission-history precedent (Items 5 / 13 / 28 in `siarc/submitted/submission_log.txt`) shows that prior Zenodo deposits intentionally **omitted** the ORCID. The operator may want to:

- (A) **Include ORCID in Zenodo metadata** to match the paper byline (1:1 byline-deposit parity). This relaxes the prior pseudonymity stance.
- (B) **Omit ORCID from Zenodo metadata** matching prior-deposit precedent, while leaving the paper byline as-is. This preserves a deposit-level pseudonymity layer.
- (C) **Apply consistency in the other direction**: remove ORCID from the paper byline too. This would be a manuscript revision (the `e0defff` byline change would be partially undone), which is operator-directed if desired.

The pre-populated `zenodo_metadata.json` currently includes ORCID with an inline comment flagging the decision. The operator can flip the field by editing one line.

### D-zenodo-related-identifiers

If the operator decides to cross-link this deposit to the SIARC umbrella concept DOI `10.5281/zenodo.19885549` or to any prior operator deposit (Items 5 / 13 / 28), the `related_identifiers` list in `zenodo_metadata.json` should be populated. Currently it is a placeholder array with one entry (the SIARC umbrella) pre-filled but commented as a hint.

---

## §6 What this packet is, and is not

**Is:** the Brief §M6.3 handoff substrate, pre-populated to the structural extent the operator's 2026-05-16 ~17:11 JST directive authorizes (three files; no deposit execution; no venue selection).

**Is not:**
- a Zenodo deposit. No external API or upload call has been made.
- a `gold/M6` tag application. Per Brief §M6.2 the tag is applied *after* the deposit, *and* at operator discretion.
- a final handoff. The plain-language summary and the next-venue block remain operator-fillable placeholders.
- a ratification of the M6 manuscript at `paper/main.tex`. Steps 3 (preflight compliance review) through 6 (handoff packet completion + Zenodo deposit + `gold/M6`) remain operator-gated.

**Operator decision queue, post-this-packet:**

1. Review `paper/main.tex` HEAD `e0defff` against the six structural reads in §4.
2. Either ratify the M6 manuscript (operator surfaces "M6 Step 2 RATIFIED. Proceed to Step 3.") or issue specific delta-language revisions (e.g. `s/Six of these ten/Five of these ten/` at line 1025 of `main.tex`).
3. Decide D-zenodo-orcid-pseudonymity-stance per §5.
4. Decide D-zenodo-related-identifiers per §5.
5. Decide on the next-venue placeholder (§3).
6. Then (post-deposit): apply `gold/M6` tag at operator discretion.

The CLI HALTS here pending operator review of the manuscript and of this packet. No portal interactions, no deposit, no tag. Rule 6 preserved.
