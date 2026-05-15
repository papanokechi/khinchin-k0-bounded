# capability/gmpy2.available.md — gmpy2 bignum arithmetic

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Version:** gmpy2 2.3.0 (Python 3.12.10).
**Role in harness:** Bignum integer arithmetic for PSLQ coefficient-bound bookkeeping (H1 height-precision regime), modular arithmetic for sanity checks (e.g., Fermat-factor cross-checks if M3 surfaces a candidate involving a known small factor), and any high-precision integer ops mpmath doesn't directly expose.

## Minimal working example: known Fermat-factor identity

`F_5 = 2^32 + 1 = 4294967297 = 641 × 6700417` (Euler, 1732).

```python
import gmpy2
F5 = gmpy2.mpz(2)**32 + 1
assert F5 == gmpy2.mpz(4294967297)
assert F5 % 641 == 0
assert F5 // 641 == 6700417
```
**Result (2026-05-15 19:25 JST):** ✓ F_5 = 4294967297; F_5 mod 641 = 0; quotient = 6700417.

## Verification log

- 2026-05-15 19:25 JST: F_5 = 2^32+1 mod 641 = 0 (verifies known small factor) ✓
- 2026-05-15 19:25 JST: gmpy2.version() returned 2.3.0 ✓

## Reproduce command

```powershell
python -c "import gmpy2; F5 = gmpy2.mpz(2)**32 + 1; print('F_5 % 641 =', F5 % 641)"
# Expected: F_5 % 641 = 0
```
