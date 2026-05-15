"""
M2.3 precision-budget wall-clock benchmark.

mpmath PSLQ at dim=15 (the M3.1 harness basis B_D(C) with D=6, |C|=7, log K_0 row + 1)
at precisions {500, 1000, 2000, 4000} dps.

Records wall-clock time and the negative result (None — no relation up to maxcoeff).
The benchmark uses K_0 and its higher powers + log K_0 + bilinears K_0*c for the
7-constant C-set {pi, e, log 2, gamma, zeta(2), zeta(3), Catalan}, exactly the
basis the M3.1 harness will run.
"""
from mpmath import mp, mpf, pslq, khinchin, log, pi, e, euler, zeta, catalan
import time

def build_basis(dps):
    mp.dps = dps
    K = khinchin
    lnK = log(K)
    Cs = [pi, e, log(2), euler, zeta(2), zeta(3), catalan]
    basis = [mpf(1), K, K**2, K**3, K**4, K**5, K**6, lnK] + [K*c for c in Cs]
    assert len(basis) == 15, "basis length unexpected"
    return basis

if __name__ == "__main__":
    for dps in [500, 1000, 2000, 4000]:
        b = build_basis(dps)
        t0 = time.perf_counter()
        r = pslq(b, tol=mpf(10)**(-int(dps*0.6)), maxcoeff=10**60, maxsteps=2000)
        dt = time.perf_counter() - t0
        if r is None:
            status = "null"
        else:
            status = "hit:" + str(r)[:40]
        print("  dim=15 dps=%5d  wall=%7.2fs  result=%s" % (dps, dt, status), flush=True)
    print("BENCHMARK DONE", flush=True)
