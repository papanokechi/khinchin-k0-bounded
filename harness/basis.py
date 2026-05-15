"""harness/basis.py — B_D(C) basis construction and sub-basis enumeration for M3.1.

Authority: M2.3 final predicate at `literature/_m2.3_calibration_anchor.md` §7
(ratified 2026-05-15 22:03:50 JST, locked at tag gold/M2 commit ca9c989).

Mission basis (n=15):
  B_D(C) = { 1, K_0, K_0^2, K_0^3, K_0^4, K_0^5, K_0^6 }     # pure powers (EF1)
        ∪ { log K_0 }                                          # log row (complement)
        ∪ { K_0·c : c ∈ {π, e, ln 2, γ, ζ(2), ζ(3), G} }       # bilinear rows (complement)

Excluded Families (per `_m2.3_calibration_anchor.md` §7.3):
  EF1: pure-power subset {1, K_0, ..., K_0^D}. Indices 0..6.
  EF2: signature S_n family — NOT in B_D(C); ceded to khinchin-signature-pslq.
  EF3: GKW methodology — methodological, NOT basis content.

Sub-basis enumeration filters EF1-only sub-bases AT CONSTRUCTION TIME
(per operator M3.1 directive: "not post-hoc"). Every enumerated sub-basis
contains at least one complement element (index ∈ {7, 8..14}).
"""

from __future__ import annotations
from itertools import combinations
from typing import Iterator
import mpmath
from mpmath import mp, mpf, pi, e, log, euler, zeta, catalan, khinchin


BASIS_LABELS = (
    "1", "K_0", "K_0^2", "K_0^3", "K_0^4", "K_0^5", "K_0^6",
    "log(K_0)",
    "K_0*pi", "K_0*e", "K_0*ln2", "K_0*gamma", "K_0*zeta(2)", "K_0*zeta(3)", "K_0*G",
)

N = 15
D_MAX = 6
C_SIZE = 7

EF1_INDICES = frozenset(range(0, 7))
LOG_INDEX = 7
COMPLEMENT_INDICES = frozenset({7, 8, 9, 10, 11, 12, 13, 14})

_BASIS_CACHE: dict[int, tuple] = {}


def build_basis(prec_dps: int) -> tuple:
    """Build B_D(C) at given precision and cache. Returns 15-tuple of mpf values."""
    if prec_dps in _BASIS_CACHE:
        return _BASIS_CACHE[prec_dps]
    mp.dps = prec_dps
    K = khinchin
    out = [mpf(1)]
    K_pow = mpf(1)
    for _ in range(D_MAX):
        K_pow = K_pow * K
        out.append(K_pow)
    out.append(log(K))
    for c in (pi, e, log(2), euler, zeta(2), zeta(3), catalan):
        out.append(K * c)
    assert len(out) == N
    result = tuple(out)
    _BASIS_CACHE[prec_dps] = result
    return result


def basis_subset(prec_dps: int, indices: tuple[int, ...]) -> tuple:
    """Return a sliced basis at given precision, in the order specified by indices."""
    full = build_basis(prec_dps)
    return tuple(full[i] for i in indices)


def labels_for(indices: tuple[int, ...]) -> tuple[str, ...]:
    return tuple(BASIS_LABELS[i] for i in indices)


def is_pure_power_only(indices: tuple[int, ...]) -> bool:
    """Returns True iff ALL indices are in EF1 (pure powers)."""
    return all(i in EF1_INDICES for i in indices)


def has_complement(indices: tuple[int, ...]) -> bool:
    """Returns True iff at least one index is in the complement (log K_0 or K_0·c_i)."""
    return any(i in COMPLEMENT_INDICES for i in indices)


def enumerate_sub_bases() -> Iterator[tuple[str, tuple[int, ...]]]:
    """Yield (family_label, indices_tuple) for the focused M3.1 sweep.

    Every yielded sub-basis satisfies has_complement(indices)==True (EF1-only
    sub-bases are filtered at construction time per operator M3.1 directive).
    The PRIMARY entry is the full n=15 basis flagged for rigorous-tier cascade;
    all others are empirical-tier-only.
    """
    yield ("primary_full", tuple(range(N)))

    yield ("full_complement", (LOG_INDEX,) + tuple(range(8, N)))

    for k in range(0, D_MAX + 1):
        yield (f"complement_plus_K0_{k}", (k, LOG_INDEX) + tuple(range(8, N)))

    for x in range(N):
        if x == LOG_INDEX:
            continue
        yield (f"pair_log_{BASIS_LABELS[x]}", (LOG_INDEX, x))

    for i, j in combinations(range(8, N), 2):
        yield (f"pair_bilinear_{BASIS_LABELS[i]}_{BASIS_LABELS[j]}", (i, j))

    for i, j in combinations(range(8, N), 2):
        yield (f"triplet_log_{BASIS_LABELS[i]}_{BASIS_LABELS[j]}", (LOG_INDEX, i, j))


def sweep_summary() -> dict:
    """Return summary stats of the enumeration (used by sweep.py header)."""
    families: dict[str, int] = {}
    total = 0
    for family, indices in enumerate_sub_bases():
        assert has_complement(indices), f"EF1-only sub-basis leaked into enumeration: {family}"
        fam_prefix = family.split("_")[0] if "_" in family else family
        if family == "primary_full":
            fam_prefix = "primary"
        elif family.startswith("complement_plus"):
            fam_prefix = "complement_plus_K0_k"
        elif family.startswith("pair_log"):
            fam_prefix = "pair_log_x"
        elif family.startswith("pair_bilinear"):
            fam_prefix = "pair_bilinear"
        elif family.startswith("triplet_log"):
            fam_prefix = "triplet_log_xy"
        families[fam_prefix] = families.get(fam_prefix, 0) + 1
        total += 1
    return {"total": total, "by_family": families}


if __name__ == "__main__":
    import json
    print("harness/basis.py — B_D(C) sub-basis enumeration")
    print()
    print("Sweep enumeration summary:")
    summary = sweep_summary()
    print(json.dumps(summary, indent=2))
    print()
    print("First 10 entries:")
    for k, (family, indices) in enumerate(enumerate_sub_bases()):
        if k >= 10:
            break
        print(f"  {k:>3d}  {family:<30s}  n={len(indices):>2d}  indices={indices}")
    print("  ...")
    print()
    print("Construction-time invariant: every sub-basis has has_complement(indices)==True")
    print("  (EF1-only sub-bases are filtered at enumeration per operator M3.1 directive).")
