"""harness/sweep.py — M3.1 driver.

Authority: M2.3 final predicate at `literature/_m2.3_calibration_anchor.md` §7
(ratified 2026-05-15 22:03:50 JST, locked at tag gold/M2 commit ca9c989).

Enumerates the focused sub-basis sweep from harness/basis.py.enumerate_sub_bases
(65 sub-bases: 1 primary rigorous + 64 empirical, all containing at least one
complement element per operator M3.1 directive). Runs harness/verify.py
three-leg verification on each. Writes per-candidate JSONL output.

Invocation modes:
  --dry-run         Run 3 small-precision smoke-test candidates only.
                    Confirms the pipeline works end-to-end.
                    Wall-clock: ~30 seconds.
  --primary-only    Run only the primary cascade (n=15 at P=2160/4320/8640
                    with rigorous-tier maxsteps=100k).
                    Wall-clock: ~90 minutes; produces the publishable measurement.
  --full            Run the full 65-sub-basis sweep at the M2.3 ratified
                    parameters. Wall-clock: ~3 hours estimated per
                    precision_budget.md §6.4.
                    NOTE: --full requires a SEPARATE OPERATOR GREENLIGHT (M3.2).
                    Default mode does NOT run --full; sweep.py rejects --full
                    unless --m32-greenlighted flag is also set.
  --m32-greenlighted  Acknowledge that M3.2 execution gate has been passed by
                      the operator. Required to combine with --full.

Output: harness/sweep_output/m3.1_sweep_<timestamp>.jsonl
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from typing import Iterable

from basis import enumerate_sub_bases, sweep_summary
from verify import verify_candidate


PRIMARY_PRECISIONS = (2160, 4320, 8640)
EMPIRICAL_PRECISIONS = (2160, 4320, 8640)

MAXCOEFF_EXP = 70

PRIMARY_MAXSTEPS = (100000, 80000, 50000)
EMPIRICAL_MAXSTEPS = (2000, 2000, 2000)

DRY_RUN_PRECISIONS = (50, 100, 200)
DRY_RUN_MAXSTEPS = (500, 500, 500)
DRY_RUN_MAXCOEFF_EXP = 20


def _candidates_for_dry_run() -> Iterable[tuple[str, tuple[int, ...]]]:
    """Tiny representative subset for the dry-run smoke test."""
    n_yielded = 0
    for family, indices in enumerate_sub_bases():
        if family == "primary_full":
            continue
        if family == "full_complement":
            yield (family, indices)
            n_yielded += 1
        elif family.startswith("pair_log_K_0") and family.endswith("K_0^2") is False:
            yield (family, indices)
            n_yielded += 1
        elif family.startswith("pair_bilinear") and "_pi_" in family:
            yield (family, indices)
            n_yielded += 1
        if n_yielded >= 3:
            return


def run_sweep(mode: str, output_dir: Path) -> Path:
    """Execute the sweep in the chosen mode. Returns path of JSONL output."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"m3.1_sweep_{mode}_{timestamp}.jsonl"

    header = {
        "_meta": True,
        "mode": mode,
        "started_at": timestamp,
        "primary_precisions": list(PRIMARY_PRECISIONS),
        "empirical_precisions": list(EMPIRICAL_PRECISIONS),
        "maxcoeff_exp": MAXCOEFF_EXP,
        "primary_maxsteps": list(PRIMARY_MAXSTEPS),
        "empirical_maxsteps": list(EMPIRICAL_MAXSTEPS),
        "sweep_summary": sweep_summary(),
        "authority": "M2.3 predicate (gold/M2 commit ca9c989); M3.1 implementation greenlit "
                     "post-cascade-arithmetic 2026-05-15 22:03:50 JST",
        "predicate_anchor": "literature/_m2.3_calibration_anchor.md §7",
    }

    print(f"[sweep] mode={mode}  output={out_path}")
    print(f"[sweep] header: {json.dumps(header, indent=2)}")

    if mode == "dry-run":
        candidates = list(_candidates_for_dry_run())
        precisions = DRY_RUN_PRECISIONS
        maxsteps = DRY_RUN_MAXSTEPS
        maxcoeff_exp = DRY_RUN_MAXCOEFF_EXP
        rigorous_for = lambda fam: False
        run_gp = lambda fam: False
    elif mode == "primary-only":
        candidates = [(f, i) for (f, i) in enumerate_sub_bases() if f == "primary_full"]
        precisions = PRIMARY_PRECISIONS
        maxsteps = PRIMARY_MAXSTEPS
        maxcoeff_exp = MAXCOEFF_EXP
        rigorous_for = lambda fam: True
        run_gp = lambda fam: True
    elif mode == "full":
        candidates = list(enumerate_sub_bases())
        precisions = EMPIRICAL_PRECISIONS
        maxsteps = EMPIRICAL_MAXSTEPS
        maxcoeff_exp = MAXCOEFF_EXP
        rigorous_for = lambda fam: fam == "primary_full"
        run_gp = lambda fam: True
    else:
        raise ValueError(f"unknown mode: {mode}")

    with out_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(header) + "\n")

        t_start = time.perf_counter()
        for i, (family, indices) in enumerate(candidates):
            print(f"[sweep] {i + 1}/{len(candidates)}  family={family}  n={len(indices)}")
            t0 = time.perf_counter()
            if mode == "primary-only" or (mode == "full" and family == "primary_full"):
                ms = PRIMARY_MAXSTEPS
            elif mode == "full":
                ms = EMPIRICAL_MAXSTEPS
            else:
                ms = maxsteps
            result = verify_candidate(
                family=family,
                indices=indices,
                precisions=precisions,
                maxcoeff_exp=maxcoeff_exp,
                maxsteps_per_prec=ms,
                rigorous_tier=rigorous_for(family),
                run_gp_leg=run_gp(family),
            )
            result["_candidate_elapsed_s"] = time.perf_counter() - t0
            f.write(json.dumps(result, default=str) + "\n")
            f.flush()
            print(f"[sweep]     verdict={result['cascade']['verdict']}  "
                  f"class={result['verification_class']}  "
                  f"elapsed={result['_candidate_elapsed_s']:.2f}s")

        total = time.perf_counter() - t_start
        f.write(json.dumps({"_meta": True, "completed_at": time.strftime("%Y%m%d_%H%M%S"),
                           "total_elapsed_s": total, "n_candidates": len(candidates)}) + "\n")

    print(f"[sweep] DONE  output={out_path}  total_elapsed={total:.2f}s")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="M3.1 sweep driver")
    ap.add_argument("--dry-run", action="store_true",
                    help="Run 3-candidate smoke test at tiny precision (~30s).")
    ap.add_argument("--primary-only", action="store_true",
                    help="Run only the primary n=15 cascade at rigorous tier (~90min).")
    ap.add_argument("--full", action="store_true",
                    help="Run the full 65-sub-basis sweep. Requires --m32-greenlighted.")
    ap.add_argument("--m32-greenlighted", action="store_true",
                    help="Acknowledge M3.2 execution gate has been passed.")
    ap.add_argument("--output-dir", type=Path, default=Path("harness/sweep_output"),
                    help="Where to write the JSONL output.")
    args = ap.parse_args()

    if sum([args.dry_run, args.primary_only, args.full]) != 1:
        ap.error("Exactly one of --dry-run / --primary-only / --full is required.")
    if args.full and not args.m32_greenlighted:
        ap.error("--full requires --m32-greenlighted (M3.2 execution gate per operator).")

    if args.dry_run:
        mode = "dry-run"
    elif args.primary_only:
        mode = "primary-only"
    else:
        mode = "full"

    run_sweep(mode, args.output_dir)


if __name__ == "__main__":
    main()
