"""
validate_claims_jsonl.py — One-time scaffold per process-to-content rule.

Validates literature/claims.jsonl against AEAL §0.1 seven-field schema.

Per `methodology/heuristics.md` H5 / H7 and the M1.1→M1.2 process-to-content binding rule,
this validator is written ONCE at M2.1 entry and is NOT iterated. It enforces field presence
and basic type checks; semantic verification is the operator's job at gold/M2 freeze.

Exit codes:
  0 — all entries pass.
  1 — at least one entry fails. Stderr lists the failures.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "id": str,
    "statement": str,
    "evidence_class": str,
    "precision_or_dependencies": dict,
    "reproduce_command": str,
    "independent_verifier_result": dict,
    "status": str,
}

ALLOWED_EVIDENCE_CLASSES = {
    "primary_paper",
    "secondary_paper",
    "book",
    "survey",
    "tertiary_aggregator",
    "oeis",
    "numerical_record",
    "literature_fidelity_catch",
    "theoretical_obstruction_citation_only",
}

ALLOWED_STATUSES = {
    "verified",
    "unverified_abstract_only",
    "unverified_paywall_blocked",
    "unverified_book_not_digitized",
    "fidelity_watch",
    "fidelity_caught_refuted",
    "theoretical_citation_only",
}

ALLOWED_METHODS = {
    "paper_read_verified",
    "abstract_only_unverified",
    "paywall_blocked",
    "book_not_digitized",
    "oeis_or_tertiary_aggregator_verified",
    "computed_reproduction",
    "search_aggregated_unverified",
}


def validate_entry(idx: int, e: dict) -> list[str]:
    errs: list[str] = []

    for field, typ in REQUIRED_FIELDS.items():
        if field not in e:
            errs.append(f"missing field: {field}")
            continue
        if not isinstance(e[field], typ):
            errs.append(f"field {field!r} has wrong type "
                        f"(expected {typ.__name__}, got {type(e[field]).__name__})")

    extra = set(e.keys()) - set(REQUIRED_FIELDS.keys())
    if extra:
        errs.append(f"extra fields not allowed: {sorted(extra)}")

    if errs:
        return errs

    if not e["id"].startswith("lit-"):
        errs.append(f"id must start with 'lit-': got {e['id']!r}")

    if e["evidence_class"] not in ALLOWED_EVIDENCE_CLASSES:
        errs.append(f"evidence_class must be one of {sorted(ALLOWED_EVIDENCE_CLASSES)}; "
                    f"got {e['evidence_class']!r}")

    if e["status"] not in ALLOWED_STATUSES:
        errs.append(f"status must be one of {sorted(ALLOWED_STATUSES)}; "
                    f"got {e['status']!r}")

    ivr = e["independent_verifier_result"]
    if "verified" not in ivr:
        errs.append("independent_verifier_result missing 'verified' key")
    elif not isinstance(ivr["verified"], bool):
        errs.append("independent_verifier_result.verified must be bool")

    if "method" not in ivr:
        errs.append("independent_verifier_result missing 'method' key")
    elif ivr["method"] not in ALLOWED_METHODS:
        errs.append(f"independent_verifier_result.method must be one of "
                    f"{sorted(ALLOWED_METHODS)}; got {ivr['method']!r}")

    if ivr.get("method") == "paywall_blocked" and "paywall_blocker" not in ivr:
        errs.append("method=paywall_blocked requires 'paywall_blocker' field")

    if not e["statement"].strip():
        errs.append("statement must be non-empty")

    if not e["reproduce_command"].strip():
        errs.append("reproduce_command must be non-empty")

    return errs


def main() -> int:
    path = Path(__file__).parent / "claims.jsonl"
    if not path.exists():
        print(f"ERROR: {path} does not exist", file=sys.stderr)
        return 1

    total_errors = 0
    seen_ids: set[str] = set()
    n = 0

    with path.open(encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"line {idx}: JSON parse error: {exc}", file=sys.stderr)
                total_errors += 1
                continue

            n += 1
            errs = validate_entry(idx, entry)
            if entry.get("id") in seen_ids:
                errs.append(f"duplicate id: {entry.get('id')!r}")
            else:
                seen_ids.add(entry.get("id", ""))

            for e in errs:
                print(f"line {idx} (id={entry.get('id', '?')!r}): {e}",
                      file=sys.stderr)
            total_errors += len(errs)

    if total_errors == 0:
        print(f"validate_claims_jsonl: PASS  {n} entries, 0 errors")
        return 0
    else:
        print(f"validate_claims_jsonl: FAIL  {n} entries, {total_errors} errors",
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
