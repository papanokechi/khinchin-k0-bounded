"""Quick smoke test for verify.gp_lindep_verify — exercises gp subprocess path on a trivial relation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import mpmath
from mpmath import mp, mpf
from verify import gp_lindep_verify

mp.dps = 100

trivial = (mpf("1.0"), mpf("2.0"), mpf("3.0"))
print("Test 1: trivial [1, 2, 3] integer relation")
res = gp_lindep_verify(trivial, dps=50, maxcoeff_exp=10)
print(f"  result: {res}")
expected = [-1, -1, 1]
if res["relation"] == expected:
    print(f"  PASS  (matches expected {expected})")
else:
    print(f"  ?     expected {expected}, got {res['relation']}")

print()
print("Test 2: algebraic identity [1, sqrt(2), 3-2*sqrt(2)]")
sqrt2 = mp.sqrt(2)
basis = (mpf(1), sqrt2, mpf(3) - 2 * sqrt2)
res = gp_lindep_verify(basis, dps=80, maxcoeff_exp=10)
print(f"  result: {res}")
if res["relation"] is not None and len(res["relation"]) == 3:
    a, b, c = res["relation"]
    if a == 3 and b == -2 and c == -1:
        print(f"  PASS")
    else:
        print(f"  ?     got {res['relation']}; expected [3, -2, -1]")
