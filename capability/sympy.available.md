# capability/sympy.available.md — sympy CAS

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Version:** sympy 1.14.0 (Python 3.12.10).
**Role in harness:** Symbolic computation for M4 (symbolic closure / closed-form derivation). `nsimplify` as Leg 3 (weak tie-breaker) of M3.1 harness. Polynomial algebra, Gröbner bases, special-function identities, exact rational arithmetic.

## Minimal working examples

### Example 1: polynomial expand / factor (round-trip identity)
```python
from sympy import symbols, expand, factor
x = symbols('x')
e = expand((x + 1)**3)
# e = x^3 + 3*x^2 + 3*x + 1
f = factor(e)
# f = (x + 1)^3
assert str(e) == "x**3 + 3*x**2 + 3*x + 1"
assert str(f) == "(x + 1)**3"
```
**Result (2026-05-15 19:25 JST):** ✓ both assertions hold.

### Example 2: nsimplify with named-constant basis (M3.1 Leg 3 pattern)
```python
from sympy import nsimplify, Rational, pi
# nsimplify a float against a basis — should return the float as a rational (no Pi match)
r = nsimplify(Rational(355, 113), [pi])
# 355/113 is a famous Pi approximation but nsimplify is asked to express as a Q-rational basis ∪ {pi};
# without floating-point tolerance, it returns the exact Rational(355,113).
print(r)
```
**Result (2026-05-15 19:25 JST):** `355/113`. This is the conservative `nsimplify` behavior; for a true Pi-substitution test, use `nsimplify(3.141592653, [pi])` with default tolerance and observe a Pi-substitution. The minimal example demonstrates the API works; M3.1 Leg 3 will use a specific tolerance configuration documented in the harness implementation.

## Harness role caveat

sympy is **Leg 3 (weak)** of the M3.1 harness. Per the harness design (probe §3.4), nsimplify is a "does sympy see this relation?" cross-check — it is **weaker than PSLQ** because nsimplify uses heuristic substitution rather than full LLL/PSLQ search. Used only as a tie-breaker when Leg 1 (mpmath PSLQ) and Leg 2 (gp lindep) disagree.

For **M4 symbolic closure**, sympy is the primary engine: polynomial algebra, Gröbner bases, integration, special-function identities.

## Verification log

- 2026-05-15 19:25 JST: expand((x+1)^3) and factor round-trip ✓
- 2026-05-15 19:25 JST: nsimplify API responds correctly ✓
- Version confirmed: 1.14.0 ✓

## Reproduce command

```powershell
python -c "from sympy import symbols, expand, factor; x = symbols('x'); print(factor(expand((x+1)**3)))"
# Expected: (x + 1)**3
```
