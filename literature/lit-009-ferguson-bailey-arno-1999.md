# lit-009 — Ferguson, Bailey, & Arno (1999), "Analysis of PSLQ"

**Status:** unverified_abstract_only · **Class:** primary_paper
**Canonical PSLQ algorithm reference.**

## Citation
Ferguson, H. R. P., Bailey, D. H., and Arno, S. (1999). _Analysis of PSLQ, an integer relation finding algorithm._ Mathematics of Computation **68** (225), pp. 351–369. DOI `10.1090/S0025-5718-99-00995-3`.

## Content (standard, abstract-attested)
- Definitive simplified PSLQ algorithm with complete correctness proof and coefficient bounds.
- Algorithm bounds: at precision P, PSLQ certifies absence of integer relations with coefficient height ≲ 10^(P/dim).
- Originally developed Ferguson-Bailey 1992 (preprint form); 1999 paper is the journal-archived canonical version.
- Selected as one of the "Top 10 Algorithms of the 20th Century" (SIAM, 2000).

## Mission role
Algorithm semantics for any PSLQ-derived claim. **The M3.1 harness does NOT require a paper-read of this entry** — algorithm semantics are codified in `mpmath.pslq` (which traces back to this paper). For algorithm-correctness arguments, mpmath's documentation + this citation is sufficient.

## Watch-list status
On lit-018 `_fidelity_findings.md` §3 watch list IF any M3.x manuscript ever cites a specific PSLQ bound from this paper. Until then, abstract-only is sufficient.
