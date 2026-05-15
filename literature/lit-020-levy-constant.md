# lit-020 — Lévy's constant β

**Status:** verified · **Class:** secondary_paper · **Method:** computed_reproduction
**Verified at:** 2026-05-15 via mpmath reproduction.

## Citation chain
- Lévy, P. (1936). "Théorie de l'addition des variables aléatoires", Gauthier-Villars, Paris (and earlier 1929 paper on CF distributions, see lit-011).
- Wikipedia "Lévy's constant" (or "Khinchin-Lévy constant"); OEIS A100199.

## Definition and value
Lévy's constant β is the almost-everywhere limit of the geometric-rate of denominator growth in a regular continued fraction:

$$\beta = \lim_{n\to\infty} (q_n)^{1/n} = \exp\!\left(\frac{\pi^2}{12 \ln 2}\right) \approx 3.27582291872\ldots$$

(Lévy 1929/1936, Lebesgue-a.e.)

## Numerical cross-check (paper-read-equivalent via computed reproduction)
```
>>> from mpmath import mp, exp, pi, log; mp.dps = 50
>>> exp(pi**2 / (12 * log(2)))
3.2758229187218111597876818824538438636084755259824
```

Matches OEIS A100199 / Wikipedia value to all 50 dps. **Closed-form-and-computed-verified** — this is the highest verification class achievable without further work.

## Arithmetic nature
The arithmetic nature of β (rationality / irrationality / transcendence) is OPEN. Numerical evidence (e.g., from PSLQ on β against {1, π, e, log 2, γ, ζ(3)}) is presumably the natural attack analog of BBC 1997's K_0 test, but the CLI has not located a published Lévy-β PSLQ-null result. (This is an absence-claim worth keeping on the fidelity-watch list if Lévy-β ever enters this mission's basis.)

## Mission role (namespace audit per H6)
**β is NOT in B_D(C).** This entry exists ONLY as a namespace-audit note: Lévy's constant β is distinct from Khinchin's constant K_0, but older references occasionally call β "the Khinchin-Lévy constant" — a name that could cause confusion. The present mission's bounded sub-question targets K_0 (geometric mean of partial quotients), NOT β (limiting growth rate of denominators).

## H6 compliance
H6 (namespace audit) is satisfied by this entry: no namespace overlap with B_D(C); naming-confusion risk explicitly documented.
