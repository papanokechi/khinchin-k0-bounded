"""
Unsolved-Relay triage validator — Mission Brief §M1.1 deliverable (b).

Validates targets/triage.json against targets/triage_schema.json.

Two-mode operation:
  (1) PRIMARY: uses `jsonschema` library if available — full Draft 2020-12 validation.
  (2) FALLBACK: pure-stdlib structural check covering all field constraints in the
      schema. Used when the environment lacks `jsonschema`. The fallback is intentionally
      conservative: it raises on anything the schema would flag PLUS a few AEAL extras
      (e.g., a row with machinery_available_locally=false advancing to M1.2 selection).

Usage:
    python triage_validator.py targets/triage.json
    python triage_validator.py --strict targets/triage.json   # also fail on warnings
    python triage_validator.py --self-test                    # runs unit checks on a fixture

Exit codes:
    0 — all rows valid
    1 — at least one row invalid (or schema not found)
    2 — usage / IO error
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE / "triage_schema.json"

ALLOWED_CATEGORIES = {
    "number_theory", "combinatorics", "dynamics", "analysis", "discrete_geometry",
    "transcendence", "diophantine_approximation", "partition_theory",
}
ALLOWED_PUB = {"high", "medium", "low"}
ALLOWED_RISK = {"low", "medium", "high"}

REQUIRED_FIELDS = {
    "problem", "category", "known_partial_results_url", "machinery_required",
    "machinery_available_locally", "falsifiable_sub_question",
    "estimated_compute_to_partial_result_hours",
    "publishability_of_negative_result", "AEAL_compliance_risk",
}

URI_RE = re.compile(r"^https?://[^\s]+$")


def validate_row_fallback(row: dict[str, Any], index: int, strict: bool = False) -> list[str]:
    errs: list[str] = []
    prefix = f"[row {index}]"
    if not isinstance(row, dict):
        return [f"{prefix} not an object"]
    missing = REQUIRED_FIELDS - set(row.keys())
    if missing:
        errs.append(f"{prefix} missing fields: {sorted(missing)}")
    extra = set(row.keys()) - REQUIRED_FIELDS
    if extra:
        errs.append(f"{prefix} unexpected fields: {sorted(extra)}")
    p = row.get("problem")
    if not (isinstance(p, str) and len(p) >= 3):
        errs.append(f"{prefix} problem must be a string of length >= 3")
    c = row.get("category")
    if c not in ALLOWED_CATEGORIES:
        errs.append(f"{prefix} category {c!r} not in {sorted(ALLOWED_CATEGORIES)}")
    u = row.get("known_partial_results_url")
    if not isinstance(u, str) or (u != "" and not URI_RE.match(u)):
        errs.append(f"{prefix} known_partial_results_url must be empty or http(s):// URL")
    mreq = row.get("machinery_required")
    if not (isinstance(mreq, list) and len(mreq) >= 1
            and all(isinstance(x, str) and len(x) >= 2 for x in mreq)
            and len(set(mreq)) == len(mreq)):
        errs.append(f"{prefix} machinery_required must be a non-empty unique string list")
    ml = row.get("machinery_available_locally")
    if not isinstance(ml, bool):
        errs.append(f"{prefix} machinery_available_locally must be boolean")
    fsq = row.get("falsifiable_sub_question")
    if not (isinstance(fsq, str) and len(fsq) >= 30):
        errs.append(f"{prefix} falsifiable_sub_question must be a string of length >= 30")
    eh = row.get("estimated_compute_to_partial_result_hours")
    if not (isinstance(eh, (int, float)) and not isinstance(eh, bool) and eh > 0 and eh <= 840):
        errs.append(f"{prefix} estimated_compute_to_partial_result_hours must be a number in (0, 840]")
    pub = row.get("publishability_of_negative_result")
    if pub not in ALLOWED_PUB:
        errs.append(f"{prefix} publishability_of_negative_result {pub!r} not in {sorted(ALLOWED_PUB)}")
    risk = row.get("AEAL_compliance_risk")
    if risk not in ALLOWED_RISK:
        errs.append(f"{prefix} AEAL_compliance_risk {risk!r} not in {sorted(ALLOWED_RISK)}")
    # AEAL extras (warnings in non-strict; errors in strict):
    if isinstance(ml, bool) and ml is False:
        msg = f"{prefix} machinery_available_locally=false — row MUST NOT advance to M1.2 selection"
        if strict:
            errs.append(msg)
        else:
            errs.append("WARN " + msg)
    if isinstance(risk, str) and risk == "high":
        msg = f"{prefix} AEAL_compliance_risk=high — re-justify before advancing"
        if strict:
            errs.append(msg)
        else:
            errs.append("WARN " + msg)
    return errs


def validate_with_jsonschema(data: Any, schema: dict) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []
    try:
        Validator = jsonschema.Draft202012Validator
    except AttributeError:
        Validator = jsonschema.Draft7Validator
    if isinstance(data, dict):
        rows = [data]
    elif isinstance(data, list):
        rows = data
    else:
        return ["top-level JSON must be an object or array"]
    out: list[str] = []
    for i, row in enumerate(rows):
        for err in Validator(schema).iter_errors(row):
            path = ".".join(str(p) for p in err.absolute_path) or "<root>"
            out.append(f"[row {i}] {path}: {err.message}")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate targets/triage.json against schema.")
    ap.add_argument("path", nargs="?", help="Path to triage.json (one object or array of objects)")
    ap.add_argument("--strict", action="store_true",
                    help="Treat AEAL warnings (machinery_unavailable, high-risk) as errors")
    ap.add_argument("--self-test", action="store_true",
                    help="Run a built-in fixture and exit")
    args = ap.parse_args(argv)

    if args.self_test:
        good = {
            "problem": "Erdős–Straus conjecture",
            "category": "number_theory",
            "known_partial_results_url": "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture",
            "machinery_required": ["mpmath at 50 dps", "sieve of Eratosthenes", "modular CRT"],
            "machinery_available_locally": True,
            "falsifiable_sub_question": "Extend computational verification range from N <= 10^14 to N <= 10^15 with a reproducible script and a Lean 4 statement of the verified range.",
            "estimated_compute_to_partial_result_hours": 96,
            "publishability_of_negative_result": "medium",
            "AEAL_compliance_risk": "low",
        }
        bad_missing = {k: v for k, v in good.items() if k != "category"}
        bad_machinery = dict(good); bad_machinery["machinery_available_locally"] = False
        bad_hours = dict(good); bad_hours["estimated_compute_to_partial_result_hours"] = 1000
        cases = [("good", good, 0), ("missing", bad_missing, 1),
                 ("warn-machinery", bad_machinery, 0),
                 ("warn-machinery-strict", bad_machinery, 1),
                 ("bad-hours", bad_hours, 1)]
        any_fail = False
        for name, row, expected_errs_strict in cases:
            strict = name.endswith("-strict")
            errs = validate_row_fallback(row, 0, strict=strict)
            hard = [e for e in errs if not e.startswith("WARN ")]
            ok = (len(hard) > 0) == (expected_errs_strict > 0)
            print(f"  [{name}] hard_errs={len(hard)} warn={len(errs)-len(hard)} expected_fail={expected_errs_strict>0} OK={ok}")
            if not ok:
                any_fail = True
                for e in errs:
                    print(f"      {e}")
        print("self-test:", "FAIL" if any_fail else "PASS")
        return 1 if any_fail else 0

    if not args.path:
        ap.error("path is required unless --self-test is given")
    p = Path(args.path)
    if not p.exists():
        print(f"ERROR: file not found: {p}", file=sys.stderr)
        return 2
    if not SCHEMA_PATH.exists():
        print(f"ERROR: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 1
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        rows = [data]
    elif isinstance(data, list):
        rows = data
    else:
        print("ERROR: top-level JSON must be an object or array of objects", file=sys.stderr)
        return 1

    js_errors = validate_with_jsonschema(data, schema)
    if js_errors:
        mode = "jsonschema"
    else:
        mode = "fallback"
    print(f"Validating {len(rows)} row(s) via {mode}.")

    all_errs: list[str] = list(js_errors)
    for i, row in enumerate(rows):
        all_errs.extend(validate_row_fallback(row, i, strict=args.strict))

    hard = [e for e in all_errs if not e.startswith("WARN ")]
    warn = [e for e in all_errs if e.startswith("WARN ")]

    for e in hard:
        print("ERROR " + e)
    for w in warn:
        print(w)

    if hard:
        print(f"\nFAIL: {len(hard)} hard error(s); {len(warn)} warning(s).")
        return 1
    print(f"\nOK: {len(rows)} row(s) valid; {len(warn)} warning(s).")
    if args.strict and warn:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
