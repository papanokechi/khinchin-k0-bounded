"""
validate_claims_jsonl.py — One-time scaffold per process-to-content rule.

Validates literature/claims.jsonl against AEAL §0.1 seven-field schema.

Per `methodology/heuristics.md` H5 / H7 and the M1.1→M1.2 process-to-content binding rule,
this validator is written ONCE at M2.1 entry and is NOT iterated. It enforces field presence
and basic type checks; semantic verification is the operator's job at gold/M2 freeze.

Class-dispatch architecture (slot-217 cycle, 2026-05-16):
  The seven-field schema is class-agnostic; per-class constraints dispatch on the
  claim id prefix:
    - 'lit-NNN-slug'                          → literature-class (default)
    - 'deposit-(hal|zenodo|osf|...)-NNN-slug' → deposit-class
  Each class binds its own evidence_class subset, method subset, and verified-field
  rule. See literature/_schema.md "Authorized exceptions ledger" for the full
  architecture entry.

Exit codes:
  0 — all entries pass.
  1 — at least one entry fails. Stderr lists the failures.
"""
from __future__ import annotations

import json
import re
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
    "primary_deposit_receipt",
}

# Class-dispatch partitions (slot-217 cycle, 2026-05-16; see _schema.md "Authorized exceptions ledger").
LITERATURE_EVIDENCE_CLASSES = {
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
DEPOSIT_EVIDENCE_CLASSES = {
    "primary_deposit_receipt",
}
assert (LITERATURE_EVIDENCE_CLASSES | DEPOSIT_EVIDENCE_CLASSES) == ALLOWED_EVIDENCE_CLASSES
assert (LITERATURE_EVIDENCE_CLASSES & DEPOSIT_EVIDENCE_CLASSES) == set()

ALLOWED_STATUSES = {
    "verified",
    "unverified_abstract_only",
    "unverified_paywall_blocked",
    "unverified_book_not_digitized",
    "fidelity_watch",
    "fidelity_caught_refuted",
    "theoretical_citation_only",
    "pending_verification",
}

ALLOWED_METHODS = {
    "paper_read_verified",
    "abstract_only_unverified",
    "paywall_blocked",
    "book_not_digitized",
    "oeis_or_tertiary_aggregator_verified",
    "computed_reproduction",
    "search_aggregated_unverified",
    "deposit_receipt_verified",
}

# Class-dispatch partitions for method enum.
LITERATURE_METHODS = {
    "paper_read_verified",
    "abstract_only_unverified",
    "paywall_blocked",
    "book_not_digitized",
    "oeis_or_tertiary_aggregator_verified",
    "computed_reproduction",
    "search_aggregated_unverified",
}
DEPOSIT_METHODS = {
    "deposit_receipt_verified",
}
assert (LITERATURE_METHODS | DEPOSIT_METHODS) == ALLOWED_METHODS
assert (LITERATURE_METHODS & DEPOSIT_METHODS) == set()


# Claim-class id-prefix patterns.
LITERATURE_ID_PREFIX = "lit-"
DEPOSIT_ID_PREFIX_PATTERN = re.compile(
    r"^deposit-(hal|zenodo|osf|preprint-server|institutional-repo)-\d{3}-"
)


def get_claim_class(entry: dict) -> str:
    """Dispatch on id prefix. Returns 'literature', 'deposit', or 'unknown'."""
    eid = entry.get("id", "")
    if not isinstance(eid, str):
        return "unknown"
    if eid.startswith(LITERATURE_ID_PREFIX):
        return "literature"
    if DEPOSIT_ID_PREFIX_PATTERN.match(eid):
        return "deposit"
    return "unknown"



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

    # Class dispatch: id prefix → claim_class. Per-class rules diverge from here.
    claim_class = get_claim_class(e)
    if claim_class == "unknown":
        errs.append(
            "id must start with 'lit-' (literature-class) or "
            "'deposit-(hal|zenodo|osf|preprint-server|institutional-repo)-NNN-' (deposit-class); "
            f"got {e['id']!r}"
        )
        return errs  # downstream class-conditional checks cannot run without a known class

    # Class-conditional evidence_class cross-check.
    if claim_class == "literature":
        if e["evidence_class"] not in LITERATURE_EVIDENCE_CLASSES:
            errs.append(
                f"literature-class id requires evidence_class in "
                f"{sorted(LITERATURE_EVIDENCE_CLASSES)}; got {e['evidence_class']!r}"
            )
    elif claim_class == "deposit":
        if e["evidence_class"] not in DEPOSIT_EVIDENCE_CLASSES:
            errs.append(
                f"deposit-class id requires evidence_class in "
                f"{sorted(DEPOSIT_EVIDENCE_CLASSES)}; got {e['evidence_class']!r}"
            )

    # Status enum is class-agnostic (flat enum), but pending_verification is the natural
    # pre-audit state for deposit-class; literature-class entries generally use the
    # unverified_* family for incomplete-verification states.
    if e["status"] not in ALLOWED_STATUSES:
        errs.append(f"status must be one of {sorted(ALLOWED_STATUSES)}; "
                    f"got {e['status']!r}")

    ivr = e["independent_verifier_result"]
    if "verified" not in ivr:
        errs.append("independent_verifier_result missing 'verified' key")
    else:
        verified = ivr["verified"]
        # Class-conditional verified rule.
        if claim_class == "literature":
            if not isinstance(verified, bool):
                errs.append("literature-class: independent_verifier_result.verified must be bool")
        elif claim_class == "deposit":
            if verified is None:
                if e.get("status") != "pending_verification":
                    errs.append(
                        "deposit-class: independent_verifier_result.verified=null is only valid "
                        f"when status='pending_verification'; got status={e.get('status')!r}"
                    )
            elif not isinstance(verified, bool):
                errs.append(
                    "deposit-class: independent_verifier_result.verified must be bool or null "
                    "(null only valid with status='pending_verification')"
                )

    if "method" not in ivr:
        errs.append("independent_verifier_result missing 'method' key")
    else:
        # Class-conditional method-enum check.
        if claim_class == "literature":
            if ivr["method"] not in LITERATURE_METHODS:
                errs.append(
                    f"literature-class: independent_verifier_result.method must be one of "
                    f"{sorted(LITERATURE_METHODS)}; got {ivr['method']!r}"
                )
        elif claim_class == "deposit":
            if ivr["method"] not in DEPOSIT_METHODS:
                errs.append(
                    f"deposit-class: independent_verifier_result.method must be one of "
                    f"{sorted(DEPOSIT_METHODS)}; got {ivr['method']!r}"
                )

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
