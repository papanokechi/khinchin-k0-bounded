# capability/mpmath.available.md — mpmath arbitrary-precision arithmetic + PSLQ

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Version:** mpmath 1.3.0 (Python 3.12.10).
**Role in harness:** Primary engine. M3.1 harness Leg 1 (cascading-precision PSLQ at {130, 260, 520} dps); 500-dps arithmetic for K_0 evaluation; mpf-class precision arithmetic across all M3+ work.

## Minimal working examples

### Example 1: 500-dps π — first 80 digits match official
```python
from mpmath import mp, pi
mp.dps = 500
val = +pi  # re-eval at current dps
assert str(val)[:82] == '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
print('mpmath 500-dps π first 80 digits verified.')
```
**Result (2026-05-15 19:25 JST):** ✓ matches official Pi digits.

### Example 2: PSLQ minimal — no relation between π and log 2
```python
from mpmath import mp, mpf, pi, log, pslq
mp.dps = 50
r = pslq([+pi, log(2)], tol=mpf('1e-30'))
assert r is None  # no integer relation exists at this length / precision
print('pslq([pi, log2]) at tol=1e-30 correctly returns None.')
```
**Result (2026-05-15 19:25 JST):** ✓ returns None (correct).

### Example 3: PSLQ minimal — known relation among polynomial-in-π
```python
from mpmath import mp, mpf, pi, pslq
mp.dps = 50
# 1, pi, pi^2 — no integer relation should exist (pi is transcendental)
r1 = pslq([mpf(1), pi, pi**2], tol=mpf('1e-40'))
# 1, pi, 2*pi - 1 — relation: 1*1 + -2*pi + 1*(2*pi - 1) = 0
r2 = pslq([mpf(1), pi, 2*pi - 1], tol=mpf('1e-40'))
print('1,pi,pi^2:', r1)
print('1,pi,2pi-1:', r2)
```

## Harness role

- M3.1 Leg 1 (cascading-precision PSLQ): `mp.dps = N`, `pslq([…], tol=mpf(f'1e-{N//2}'))`, escalate to 2N, 4N per H1.
- Per Brief §M3.1, this is the primary integer-relation finder; gp lindep is the independent reimplementation leg.

## Verification log

- 2026-05-15 19:25 JST: 500-dps π first 80 digits match official ✓
- 2026-05-15 19:25 JST: pslq([pi, log2]) returns None at tol=1e-30 ✓
- Version confirmed: 1.3.0 ✓

## Reproduce command

```powershell
python -c "from mpmath import mp, pi; mp.dps=500; val=str(+pi); print(val[:82])"
# Expected: '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899'
```
