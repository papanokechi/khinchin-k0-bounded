"""Sanity-test the U-MISSION-N R2.beta dual-field empirical_height."""
from verify import empirical_height_dual, empirical_height

cases = [
    ("primary_full",         2160, 15, 70),
    ("full_complement",      2160, 8,  70),
    ("complement_plus_K0_k", 2160, 9,  70),
    ("triplet_log_xy",       2160, 3,  70),
    ("pair_log_x",           2160, 2,  70),
    ("pair_bilinear_ij",     2160, 2,  70),
]
print(f"{'family':28s} {'n':>3s}  {'formula':>22s}  {'operational':>22s}  type(form)  type(op)")
print("-" * 110)
for fam, P, n, mexp in cases:
    d = empirical_height_dual(P, n, maxcoeff_exp=mexp)
    f = d["H_empirical_formula"]
    o = d["H_empirical_operational"]
    f_disp = f"{float(f):>22.4e}" if isinstance(f, float) or (isinstance(f, int) and f < 10**300) else f"int(10^{len(str(f))-1})"
    o_disp = f"{float(o):>22.4e}" if isinstance(o, float) or (isinstance(o, int) and o < 10**300) else f"int(10^{len(str(o))-1})"
    print(f"{fam:28s} {n:>3d}  {f_disp}  {o_disp}  {type(f).__name__:10s} {type(o).__name__}")

print()
print("Test that single-arg empirical_height still works (M3.2a back-compat):")
print(f"  empirical_height(2160, 15) = {empirical_height(2160, 15)!r}  type={type(empirical_height(2160, 15)).__name__}")
print()
print("Test JSON serializability of return dict:")
import json
d = empirical_height_dual(2160, 2, maxcoeff_exp=70)
serial = json.dumps(d, default=str)
print(f"  Serialized length: {len(serial)} bytes")
print(f"  Serialized excerpt: {serial[:120]}...")
