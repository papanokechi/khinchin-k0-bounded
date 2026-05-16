"""harness/sweep.py — M3.1 driver with M3.2a/M3.2b phase split.

Authority: M2.3 final predicate at `literature/_m2.3_calibration_anchor.md` §7
(ratified 2026-05-15 22:03:50 JST, locked at tag gold/M2 commit ca9c989).
M3.2 phase split installed 2026-05-16 ~08:22 JST per operator U-MISSION-M3.2
("M3.2 GREENLIGHT — split into phases M3.2a and M3.2b"). The split is a
procedural extension of the predicate text (methodology refinement), NOT a
hypothesis mutation. Mutation budget unchanged.

Enumerates the focused sub-basis sweep from harness/basis.py.enumerate_sub_bases
(65 sub-bases: 1 primary rigorous + 64 empirical, all containing at least one
complement element per operator M3.1 directive). Runs harness/verify.py
three-leg verification on each. Writes per-candidate JSONL output.

Modes (mutually exclusive):

  --dry-run                    3-candidate tiny-precision smoke test.
                               Ungated; intended for pipeline mechanics check.
                               Wall-clock: < 1 minute. JSONL: dry_run=true.
                               Output filename: m31_dryrun_<timestamp>.jsonl

  --m31-extended-dry-run       FULL-REGIME pre-canonical dry-run per H10
                               mandate (U-MISSION-N RESOLUTION 2026-05-16
                               ~11:18 JST). Enumerates ALL 65 sub-bases
                               (primary_full + 64 empirical) at canonical
                               primary precision range P=540/1080/2160 with
                               reduced maxsteps (5000/3000/2000) and reduced
                               maxcoeff_exp=40. Exercises every (P, n,
                               basis_structure) tuple the canonical M3.2b
                               sweep will touch. Ungated; intended for
                               harness validation only.
                               Wall-clock: ~10-15 minutes (most candidates
                               terminate within seconds at maxcoeff=10^40).
                               JSONL: dry_run=true.
                               Output filename: m31_extended_dryrun_<timestamp>.jsonl

  --m32-primary-measurement    Canonical primary cascade (n=15) at full
                               primary precisions (P=2160/4320/8640, rigorous
                               maxsteps 100k/80k/50k). REQUIRES
                               --m32-primary-greenlighted flag (M3.2a gate).
                               Wall-clock: ~90 minutes (per §6.4 benchmark).
                               JSONL: dry_run=false (CANONICAL M6 input).
                               Output filename: m32a_primary_cascade.jsonl
                               REFUSES TO OVERWRITE an existing canonical file.

  --full                       Full 65-sub-basis sweep. REQUIRES
                               --m32-full-greenlighted flag (M3.2b gate)
                               AND a successful prior M3.2a measurement
                               (m32a_primary_cascade.jsonl present in
                               output_dir with non-meta record(s)).
                               Wall-clock: ~3 hours per §6.4 sweep arithmetic.
                               Output filename: m32b_empirical_sweep.jsonl

Gate flags:

  --m32-primary-greenlighted   Operator-given acknowledgement of M3.2a gate.
  --m32-full-greenlighted      Operator-given acknowledgement of M3.2b gate.

Operator's M3.2 phase semantics (verbatim 2026-05-16 ~08:22 JST):

  "The 6-turn cost of the M3.2a→M3.2b operator turn is cheap insurance against
   discovering a primary-cascade anomaly after the empirical sweep is committed."
  "Halt for M3.2a operator review. If clean null at H_rigorous=10^70 with
   cascade stability and gp agreement: M3.2b greenlighted. If anomaly:
   halt and surface."
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

EXTENDED_DRY_RUN_PRECISIONS = (540, 1080, 2160)
EXTENDED_DRY_RUN_MAXSTEPS = (5000, 3000, 2000)
EXTENDED_DRY_RUN_MAXCOEFF_EXP = 40

CANONICAL_PRIMARY_FILENAME = "m32a_primary_cascade.jsonl"
CANONICAL_FULL_FILENAME = "m32b_empirical_sweep.jsonl"


def _candidates_for_dry_run() -> Iterable[tuple[str, tuple[int, ...]]]:
    """Tiny representative subset for the 3-candidate smoke test."""
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


def _verify_m32a_prereq(output_dir: Path) -> Path:
    """Confirm M3.2a canonical output exists with at least one non-meta record.

    Raises FileNotFoundError if --full is invoked without prior M3.2a.
    """
    m32a_path = output_dir / CANONICAL_PRIMARY_FILENAME
    if not m32a_path.exists():
        raise FileNotFoundError(
            f"--full requires prior M3.2a measurement at {m32a_path}. "
            f"Run with --m32-primary-measurement first."
        )
    record_count = 0
    with m32a_path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
                if not rec.get("_meta"):
                    record_count += 1
            except json.JSONDecodeError:
                continue
    if record_count == 0:
        raise FileNotFoundError(
            f"M3.2a canonical file exists at {m32a_path} but contains no "
            f"per-candidate records. M3.2a appears incomplete."
        )
    return m32a_path


def run_sweep(mode: str, output_dir: Path) -> Path:
    """Execute the sweep in the chosen mode. Returns path of JSONL output."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_dir.mkdir(parents=True, exist_ok=True)

    if mode == "dry-run":
        out_path = output_dir / f"m31_dryrun_{timestamp}.jsonl"
        is_dry_run = True
    elif mode == "m31-extended-dry-run":
        out_path = output_dir / f"m31_extended_dryrun_{timestamp}.jsonl"
        is_dry_run = True
    elif mode == "m32-primary-measurement":
        out_path = output_dir / CANONICAL_PRIMARY_FILENAME
        is_dry_run = False
        if out_path.exists():
            raise FileExistsError(
                f"M3.2a canonical output {out_path} already exists. "
                f"Refusing to overwrite (single canonical execution per operator). "
                f"To re-run, move or remove the existing file first."
            )
    elif mode == "full":
        out_path = output_dir / CANONICAL_FULL_FILENAME
        is_dry_run = False
        if out_path.exists():
            raise FileExistsError(
                f"M3.2b canonical output {out_path} already exists. "
                f"Refusing to overwrite. To re-run, move or remove the existing file first."
            )
    else:
        raise ValueError(f"unknown mode: {mode}")

    if mode == "dry-run":
        candidates = list(_candidates_for_dry_run())
        precisions = DRY_RUN_PRECISIONS
        maxsteps_default = DRY_RUN_MAXSTEPS
        maxcoeff_exp = DRY_RUN_MAXCOEFF_EXP
        rigorous_for = lambda fam: False
        run_gp = lambda fam: False
    elif mode == "m31-extended-dry-run":
        # Per H10 mandate (U-MISSION-N RESOLUTION 2026-05-16 ~11:18 JST):
        # full-regime dry-run enumerates ALL 65 sub-bases at canonical
        # primary precision range, NOT just primary_full. This is the
        # H10-mandated pre-canonical step for M3.2b canonical re-run.
        candidates = list(enumerate_sub_bases())
        precisions = EXTENDED_DRY_RUN_PRECISIONS
        maxsteps_default = EXTENDED_DRY_RUN_MAXSTEPS
        maxcoeff_exp = EXTENDED_DRY_RUN_MAXCOEFF_EXP
        rigorous_for = lambda fam: False
        run_gp = lambda fam: True
    elif mode == "m32-primary-measurement":
        candidates = [(f, i) for (f, i) in enumerate_sub_bases() if f == "primary_full"]
        precisions = PRIMARY_PRECISIONS
        maxsteps_default = PRIMARY_MAXSTEPS
        maxcoeff_exp = MAXCOEFF_EXP
        rigorous_for = lambda fam: True
        run_gp = lambda fam: True
    elif mode == "full":
        candidates = list(enumerate_sub_bases())
        precisions = EMPIRICAL_PRECISIONS
        maxsteps_default = EMPIRICAL_MAXSTEPS
        maxcoeff_exp = MAXCOEFF_EXP
        rigorous_for = lambda fam: fam == "primary_full"
        run_gp = lambda fam: True
    else:
        raise ValueError(f"unknown mode: {mode}")

    header = {
        "_meta": True,
        "mode": mode,
        "dry_run": is_dry_run,
        "canonical": (mode in ("m32-primary-measurement", "full")),
        "started_at": timestamp,
        "primary_precisions": list(PRIMARY_PRECISIONS),
        "empirical_precisions": list(EMPIRICAL_PRECISIONS),
        "precisions_this_run": list(precisions),
        "maxsteps_default": list(maxsteps_default),
        "maxcoeff_exp": maxcoeff_exp,
        "primary_maxsteps": list(PRIMARY_MAXSTEPS),
        "empirical_maxsteps": list(EMPIRICAL_MAXSTEPS),
        "sweep_summary": sweep_summary(),
        "authority": "M2.3 predicate (gold/M2 commit ca9c989); "
                     "M3.2 phase split per operator U-MISSION-M3.2 2026-05-16 ~08:22 JST",
        "predicate_anchor": "literature/_m2.3_calibration_anchor.md §7",
    }

    print(f"[sweep] mode={mode}  output={out_path}")
    print(f"[sweep] dry_run={is_dry_run}  canonical={header['canonical']}")
    print(f"[sweep] n_candidates={len(candidates)}  precisions={precisions}")
    print(f"[sweep] maxsteps_default={maxsteps_default}  maxcoeff_exp={maxcoeff_exp}")

    with out_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(header) + "\n")
        f.flush()

        t_start = time.perf_counter()
        for i, (family, indices) in enumerate(candidates):
            print(f"[sweep] {i + 1}/{len(candidates)}  family={family}  n={len(indices)}", flush=True)
            t0 = time.perf_counter()
            if family == "primary_full":
                ms = PRIMARY_MAXSTEPS if mode in ("m32-primary-measurement", "full") else maxsteps_default
            elif mode == "full":
                ms = EMPIRICAL_MAXSTEPS
            else:
                ms = maxsteps_default
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
            result["_dry_run"] = is_dry_run
            f.write(json.dumps(result, default=str) + "\n")
            f.flush()
            print(f"[sweep]     verdict={result['cascade']['verdict']}  "
                  f"class={result['verification_class']}  "
                  f"H_emp_op={result['H_empirical_operational']:.2e}  H_rig={result['H_rigorous_min']:.2e}  "
                  f"elapsed={result['_candidate_elapsed_s']:.2f}s", flush=True)

        total = time.perf_counter() - t_start
        f.write(json.dumps({"_meta": True, "completed_at": time.strftime("%Y%m%d_%H%M%S"),
                           "total_elapsed_s": total, "n_candidates": len(candidates)}) + "\n")

    print(f"[sweep] DONE  output={out_path}  total_elapsed={total:.2f}s")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="M3.1/M3.2 sweep driver (phase-split)")
    ap.add_argument("--dry-run", action="store_true",
                    help="3-candidate tiny-precision smoke test (ungated, < 1 min).")
    ap.add_argument("--m31-extended-dry-run", dest="m31_extended_dry_run",
                    action="store_true",
                    help="FULL-REGIME pre-canonical dry-run per H10 mandate: all 65 sub-bases at P=540/1080/2160 (ungated, ~10-15 min, dry_run=true).")
    ap.add_argument("--m32-primary-measurement", dest="m32_primary_measurement",
                    action="store_true",
                    help="Canonical primary cascade at full precision (M3.2a, ~90 min). "
                         "Requires --m32-primary-greenlighted.")
    ap.add_argument("--full", action="store_true",
                    help="Full 65-sub-basis sweep (M3.2b, ~3 hours). "
                         "Requires --m32-full-greenlighted AND prior M3.2a output.")
    ap.add_argument("--m32-primary-greenlighted", dest="m32_primary_greenlighted",
                    action="store_true",
                    help="Acknowledge M3.2a execution gate has been passed by operator.")
    ap.add_argument("--m32-full-greenlighted", dest="m32_full_greenlighted",
                    action="store_true",
                    help="Acknowledge M3.2b execution gate has been passed by operator.")
    ap.add_argument("--output-dir", type=Path, default=Path("harness/sweep_output"),
                    help="Where to write the JSONL output.")
    args = ap.parse_args()

    mode_flags = [args.dry_run, args.m31_extended_dry_run,
                  args.m32_primary_measurement, args.full]
    if sum(mode_flags) != 1:
        ap.error("Exactly one of --dry-run / --m31-extended-dry-run / "
                 "--m32-primary-measurement / --full is required.")

    if args.m32_primary_measurement and not args.m32_primary_greenlighted:
        ap.error("--m32-primary-measurement requires --m32-primary-greenlighted "
                 "(M3.2a execution gate per operator).")

    if args.full and not args.m32_full_greenlighted:
        ap.error("--full requires --m32-full-greenlighted "
                 "(M3.2b execution gate per operator).")

    if args.full:
        try:
            prereq_path = _verify_m32a_prereq(args.output_dir)
            print(f"[sweep] M3.2a prereq satisfied: {prereq_path}")
        except FileNotFoundError as e:
            ap.error(str(e))

    if args.dry_run:
        mode = "dry-run"
    elif args.m31_extended_dry_run:
        mode = "m31-extended-dry-run"
    elif args.m32_primary_measurement:
        mode = "m32-primary-measurement"
    else:
        mode = "full"

    run_sweep(mode, args.output_dir)


if __name__ == "__main__":
    main()
