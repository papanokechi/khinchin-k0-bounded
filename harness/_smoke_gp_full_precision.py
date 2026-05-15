"""Smoke test: gp_lindep at primary precision (P=2160) on n=15 mission basis.

Confirms the precision-override correction (dps = primary_P, not primary_P//2)
works end-to-end and produces a sensible wall-clock for the M3.2a measurement.
"""
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import mpmath
from mpmath import mp

from basis import build_basis
from verify import gp_lindep_verify

# Warm up the basis cache first (cold-cache amortized over sweep per benchmark).
print("[smoke] precomputing n=15 basis at P=2160 ...", flush=True)
t0 = time.perf_counter()
basis = build_basis(2160)
t_basis = time.perf_counter() - t0
print(f"[smoke] basis ready in {t_basis:.1f}s, n={len(basis)}", flush=True)

# Now call gp_lindep at full P=2160 with a generous timeout.
print(f"[smoke] gp_lindep at dps=2160 (full P) on n=15 basis ...", flush=True)
t0 = time.perf_counter()
res = gp_lindep_verify(basis, dps=2160, maxcoeff_exp=70, timeout_s=1800)
t_gp = time.perf_counter() - t0
print(f"[smoke] gp_lindep done in {t_gp:.1f}s", flush=True)
print(f"[smoke] relation: {res['relation']}")
print(f"[smoke] error:    {res['error']}")
print(f"[smoke] stdout_tail: {res.get('stdout_tail', '')[:300]}")
print(f"[smoke] stderr_tail: {res.get('stderr_tail', '')[:300]}")
print()
print(f"[smoke] basis_build_s={t_basis:.1f}  gp_lindep_s={t_gp:.1f}")
