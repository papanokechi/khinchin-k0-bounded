# lit-011 — Gauss-Kuzmin distribution and the GKW transfer operator (classical)

**Status:** theoretical_citation_only · **Class:** theoretical_obstruction_citation_only

## Foundational citations
- **Kuzmin, R. O.** (1928). "On a problem of Gauss." _Atti del Congresso Internazionale dei Matematici_, Bologna, **6**, pp. 83–89.
- **Lévy, P.** (1929). "Sur les lois de probabilité dont dépendent les quotients complets et incomplets d'une fraction continue." _Bulletin de la Société Mathématique de France_ **57**, pp. 178–194.
- **Wirsing, E.** (1974). See lit-012 for the Frobenius-Perron treatment determining the second eigenvalue.

## Content
The Gauss-Kuzmin distribution describes the limiting distribution of partial quotients in a regular continued fraction:

$$P(a_n = k) \to \log_2\left(\frac{(k+1)^2}{k(k+2)}\right)$$

The Gauss-Kuzmin-Wirsing (GKW) transfer operator acts on density functions as

$$(\mathcal{T} f)(x) = \sum_{k=1}^\infty \frac{1}{(k+x)^2} f\!\left(\frac{1}{k+x}\right)$$

Khinchin's theorem is the ergodic-theory consequence of the GKW operator's ergodicity for the Gauss measure $d\mu = \frac{1}{\ln 2} \frac{dx}{1+x}$.

## DO-NOT-REENTER (binding clause)
Per `seeds/26_gauss_kuzmin_reframings_future_work.md` (operator U-MISSION-A-FOLLOWUP confirmed drop of survey #26), **GKW-operator methodology is ceded to the Finite-Depth Rigidity track and is NOT imported as method into this mission's harness**. This entry exists ONLY as theoretical context — to anchor the citation chain "why direct attack on K_0 transcendence is hard, therefore PSLQ-style numerical evidence on the algebraic-relation question is the tractable form."

## Mission role
Theoretical-context citation only. Cited in the M2.3 calibration anchor (`_m2.3_calibration_anchor.md`) only as "the structural reason BBC 1997 chose PSLQ over a direct transcendence proof attempt."

## Sub-citations
- lit-012 (Wirsing 1974): second-eigenvalue determination
- lit-013, lit-014 (Vallée surveys): modern spectral-theory treatments
