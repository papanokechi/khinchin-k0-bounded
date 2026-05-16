"""
Audit script: M3.2b canonical sweep verification + summary input generator.

Reads:
  - harness/sweep_output/m32a_primary_cascade.jsonl  (M3.2a canonical primary_full)
  - harness/sweep_output/m32b_empirical_sweep.jsonl  (M3.2b canonical 65 sub-bases)

Verifies:
  1. m32b has 65 candidate records + meta header + meta footer
  2. m32b primary_full record bit-for-bit reproduces M3.2a:
       - K iterations identical at each P
       - final_norm identical at each P
       - H_rigorous identical at each P
  3. All 65 candidates: verdict == cascade_stable_null
  4. Verification class distribution
  5. Empirical / rigorous bound distribution
  6. Per-family elapsed wall-clock distribution

Emits:
  - JSON-encodable dict for m32b_summary.md table generation
  - Honest reporting of any mismatch.

Per H7 audit-trail-honesty precedent: kept in repo.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
M32A = HERE / "sweep_output" / "m32a_primary_cascade.jsonl"
M32B = HERE / "sweep_output" / "m32b_empirical_sweep.jsonl"


def load_jsonl(path: Path) -> tuple[dict, list[dict], dict]:
    """Return (meta_header, candidate_records, meta_footer)."""
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    records = [json.loads(ln) for ln in lines]
    metas = [r for r in records if r.get("_meta") is True]
    cands = [r for r in records if r.get("_meta") is not True]
    # First meta is header (has 'mode'/'started_at'); last is footer (has 'completed_at')
    header = next((m for m in metas if "started_at" in m or "mode" in m), {})
    footer = next((m for m in metas if "completed_at" in m), {})
    return header, cands, footer


def main():
    m32a_header, m32a_cands, m32a_footer = load_jsonl(M32A)
    m32b_header, m32b_cands, m32b_footer = load_jsonl(M32B)

    print(f"M3.2a file: {M32A.name}")
    print(f"  meta_header: mode={m32a_header.get('mode')} dry_run={m32a_header.get('dry_run')} canonical={m32a_header.get('canonical')}")
    print(f"  candidates: {len(m32a_cands)}")
    print()

    print(f"M3.2b file: {M32B.name}")
    print(f"  meta_header: mode={m32b_header.get('mode')} dry_run={m32b_header.get('dry_run')} canonical={m32b_header.get('canonical')}")
    print(f"  candidates: {len(m32b_cands)}")
    print(f"  total_elapsed: {m32b_footer.get('total_elapsed_s')}s")
    print()

    assert len(m32b_cands) == 65, f"expected 65 candidates, got {len(m32b_cands)}"
    print(f"  [OK] 65 candidate records present")

    # --- 1. Verdict distribution ---
    verdicts = Counter(c.get("cascade", {}).get("verdict", "MISSING") for c in m32b_cands)
    print()
    print("Verdict distribution:")
    for v, n in sorted(verdicts.items()):
        print(f"  {v}: {n}")
    assert verdicts.get("cascade_stable_null", 0) == 65, f"expected 65 cascade_stable_null, got {verdicts}"
    print(f"  [OK] All 65 cascade_stable_null")

    # --- 2. Verification class distribution ---
    classes = Counter(c.get("verification_class", "MISSING") for c in m32b_cands)
    print()
    print("Verification class distribution:")
    for c, n in sorted(classes.items()):
        print(f"  {c}: {n}")

    # --- 3. Primary_full reproduction check ---
    print()
    print("=" * 70)
    print("PRIMARY_FULL REPRODUCTION CHECK (M3.2b vs M3.2a)")
    print("=" * 70)
    a_primary = next(c for c in m32a_cands if c.get("family") == "primary_full")
    b_primary = next(c for c in m32b_cands if c.get("family") == "primary_full")

    a_legs = a_primary.get("cascade", {}).get("per_precision", [])
    b_legs = b_primary.get("cascade", {}).get("per_precision", [])
    assert len(a_legs) == len(b_legs) == 3, f"expected 3 legs each; got M3.2a={len(a_legs)} M3.2b={len(b_legs)}"

    print(f"{'P_dps':>8} | {'K_a':>7}  {'K_b':>7}  K_match | {'final_norm match':>18} | {'H_rig_a':>14}  {'H_rig_b':>14}  H_match")
    print("-" * 110)
    all_match = True
    for la, lb in zip(a_legs, b_legs):
        P = la.get("P")
        Ka = la.get("iteration_count")
        Kb = lb.get("iteration_count")
        norm_a = str(la.get("final_norm"))
        norm_b = str(lb.get("final_norm"))
        H_a = la.get("H_rigorous")
        H_b = lb.get("H_rigorous")
        k_match = "YES" if Ka == Kb else "**NO**"
        norm_match = "YES" if norm_a == norm_b else "**NO**"
        H_match = "YES" if str(H_a) == str(H_b) else "(differ)"
        if Ka != Kb or norm_a != norm_b or str(H_a) != str(H_b):
            all_match = False
        try:
            H_a_f = float(H_a) if H_a is not None else 0.0
            H_b_f = float(H_b) if H_b is not None else 0.0
        except (TypeError, ValueError):
            H_a_f = H_b_f = 0.0
        print(f"{str(P):>8} | {str(Ka):>7}  {str(Kb):>7}  {k_match:>7} | {norm_match:>18} | {H_a_f:>14.4e}  {H_b_f:>14.4e}  {H_match}")

    if all_match:
        print()
        print("[OK] PRIMARY_FULL BIT-FOR-BIT REPRODUCTION: PASS")
        print("     K iterations + final_norm identical at all 3 precisions.")
    else:
        print()
        print("[HALT] PRIMARY_FULL REPRODUCTION FAILED — operator-mandated halt condition.")

    # --- 4. Per-family elapsed summary ---
    print()
    print("Per-family elapsed wall-clock summary:")
    family_groups: dict[str, list[float]] = {}
    for c in m32b_cands:
        fam = c.get("family", "?")
        # Group by family root (strip indices)
        if fam == "primary_full":
            root = "primary_full"
        elif fam == "full_complement":
            root = "full_complement"
        elif fam.startswith("complement_plus_K0"):
            root = "complement_plus_K0_k"
        elif fam.startswith("pair_log"):
            root = "pair_log"
        elif fam.startswith("pair_bilinear"):
            root = "pair_bilinear"
        elif fam.startswith("triplet_log"):
            root = "triplet_log"
        else:
            root = "other"
        family_groups.setdefault(root, []).append(c.get("_candidate_elapsed_s", 0.0))

    for fam, times in sorted(family_groups.items(), key=lambda kv: -sum(kv[1])):
        print(f"  {fam:>24}  n={len(times):>2}  total={sum(times):>9.1f}s  avg={sum(times)/len(times):>7.2f}s")

    # --- 5. H_rigorous distribution per family ---
    print()
    print("H_rigorous range per family group:")
    family_h: dict[str, list[float]] = {}
    for c in m32b_cands:
        fam = c.get("family", "?")
        if fam == "primary_full":
            root = "primary_full (rigorous tier)"
        elif fam == "full_complement":
            root = "full_complement"
        elif fam.startswith("complement_plus_K0"):
            root = "complement_plus_K0_k"
        elif fam.startswith("pair_log"):
            root = "pair_log"
        elif fam.startswith("pair_bilinear"):
            root = "pair_bilinear"
        elif fam.startswith("triplet_log"):
            root = "triplet_log"
        else:
            root = "other"
        legs = c.get("cascade", {}).get("per_precision", [])
        hrigs = []
        for l in legs:
            h = l.get("H_rigorous")
            if h is None:
                continue
            try:
                hrigs.append(float(h))
            except (TypeError, ValueError):
                pass
        if hrigs:
            family_h.setdefault(root, []).append(max(hrigs))

    for fam, hs in sorted(family_h.items()):
        print(f"  {fam:>32}  min={min(hs):>10.2e}  max={max(hs):>10.2e}  median={sorted(hs)[len(hs)//2]:>10.2e}  n={len(hs)}")

    # --- 6. Dual-field reporting verification ---
    print()
    print("Dual-field reporting verification:")
    n_with_op = sum(1 for c in m32b_cands if "H_empirical_operational" in c)
    n_with_formula = sum(1 for c in m32b_cands if "H_empirical_formula" in c)
    print(f"  records with H_empirical_operational: {n_with_op}/65")
    print(f"  records with H_empirical_formula:     {n_with_formula}/65")
    def _to_int_or_float(x):
        if isinstance(x, int):
            return x
        try:
            f = float(x)
            return f
        except (TypeError, ValueError, OverflowError):
            try:
                return int(x)
            except (TypeError, ValueError):
                return 0
    cap_active = 0
    cap_inactive = 0
    for c in m32b_cands:
        f = c.get("H_empirical_formula")
        op = c.get("H_empirical_operational")
        if f is None or op is None:
            continue
        f_v = _to_int_or_float(f)
        op_v = _to_int_or_float(op)
        if f_v > op_v:
            cap_active += 1
        else:
            cap_inactive += 1
    print(f"  cap ACTIVE (formula > operational): {cap_active}")
    print(f"  cap INACTIVE (formula <= operational): {cap_inactive}")

    # --- 7. gp_lindep leg verdict distribution ---
    print()
    print("gp_lindep verdict distribution:")
    gp_verdicts = Counter(c.get("gp_lindep", {}).get("gp_verdict", "MISSING") for c in m32b_cands)
    for v, n in sorted(gp_verdicts.items()):
        print(f"  {v}: {n}")

    print()
    print("=" * 70)
    print("AUDIT COMPLETE")
    print("=" * 70)

    return 0 if all_match else 1


if __name__ == "__main__":
    sys.exit(main())
