# capability/numpy.available.md — numpy numerical-array primitives

**Status:** AVAILABLE (verified per H7 functional-verification heuristic, 2026-05-15 19:25 JST).

**Version:** numpy 2.4.4 (Python 3.12.10).
**Role in harness:** Linear-algebra primitives over float64 for low-precision sanity (NOT high-precision; mpmath handles 130+ dps). FFT if any sequence-analysis comes up. Array reshaping for PSLQ coefficient-matrix bookkeeping.

## Minimal working example: 2x2 determinant

```python
import numpy as np
A = np.array([[1.0, 2.0], [3.0, 4.0]])
det = np.linalg.det(A)
# det = 1*4 - 2*3 = -2
assert abs(det - (-2.0)) < 1e-10
```
**Result (2026-05-15 19:25 JST):** ✓ det = -2.0000000000000004 (correct to float64 precision; deviation < 1e-15 is normal LU-decomposition residual).

## Harness role caveat

numpy is **NOT** a substitute for mpmath at any precision regime the harness cares about. It is used only for:
- Float64-precision sanity checks (e.g., "does the candidate basis vector approximately sum to zero at machine precision before we escalate to 500 dps PSLQ?").
- Array reshaping / iteration utilities.
- Reading/writing numerical fixtures.

Any high-precision arithmetic uses `mpmath`. Any rigorous bound uses `gp lindep` (Leg 2). numpy never appears in a `claims/` `precision_or_dependencies` field at higher than `dps=15.95` (float64).

## Verification log

- 2026-05-15 19:25 JST: det([[1,2],[3,4]]) = -2.0000000000000004 (≈ -2 within float64) ✓
- Version confirmed: 2.4.4 ✓

## Reproduce command

```powershell
python -c "import numpy as np; A = np.array([[1.0,2.0],[3.0,4.0]]); print(np.linalg.det(A))"
# Expected: ≈ -2.0 (float64)
```
