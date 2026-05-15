# lit-019 — Khinchin's Hölder-mean family K_p

**Status:** verified · **Class:** primary_paper
**Verified at:** 2026-05-15 via lit-002 (BBC 1997 §5 paper-read) and lit-004 (Wikipedia).

## Citation chain
- BBC 1997 §5 (lit-002, paper-read-verified) provides the canonical computational table of K_p for p ∈ {−2, −3, −4, −5} at 50 digits each, and K_{-1} (harmonic mean) at 7350 digits.
- Wikipedia "Khinchin's constant" Hölder-mean section (lit-004) gives the closed-form definition.

## Family formula
$$K_p = \left[ \sum_{k=1}^\infty -k^p \log_2\!\left(1 - \frac{1}{(k+1)^2}\right) \right]^{1/p}$$

- Finite for `p < 1`.
- `p = 0` (geometric-mean limit) gives K_0 = 2.685452…
- `p = -1` (harmonic mean) gives K_{-1} = 1.74540566240… (BBC 1997 §5 7350-digit computation).
- `p ≥ 1` divergent (arithmetic-mean and higher diverge because the heavy-tailed distribution of partial quotients makes Σ a_k diverge a.s.).

## Mission role
**Out of scope for the present mission.** `selected.md §2` fixes the target as K_0 (p = 0) specifically. The wider Hölder-mean family is included in this ledger only to:

1. Establish that K_0 is _the_ p = 0 member of a known family (not an isolated curiosity).
2. Document that the arithmetic nature of each K_p (p < 1) is independently open.
3. Ensure the M3.x manuscript does not implicitly claim results about K_p ≠ 0.

## Re-verification path
- BBC 1997 §5 lines 880–885 of extracted text (see `lit-002-bailey-borwein-crandall-1997.md` §6 for the pypdf extraction path) lists K_p values.
- Closed form can be cross-checked: `mpmath.nsum(lambda k: -k**p * log(1 - 1/(k+1)**2, 2), [1, mpmath.inf])**(1/p)` with mp.dps = 50.
