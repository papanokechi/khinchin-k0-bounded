"""one-off script — adds verification_class sub-key to load-bearing claims.jsonl entries per H9 retroactive binding."""
import json
from pathlib import Path

p = Path("literature/claims.jsonl")
entries = [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

verification_class_for = {
    "lit-001-papanokechi-signature-pslq-2026": "field_standard_practice",
    "lit-002-bailey-borwein-crandall-1997":     "field_standard_practice",
    "lit-003-oeis-a002210":                     "field_standard_practice",
    "lit-009-ferguson-bailey-arno-1999":        "proven_corollary",
    "lit-018-fidelity-no-prior-k0-pslq-refuted": "field_standard_practice",
}

h9_notes = {
    "lit-001-papanokechi-signature-pslq-2026":
        "H9 verification_class: field_standard_practice. The cited scope-distinction passage from the signature paper's Discussion section is a literature handoff (not a quantitative bound); classified as community-validated empirical practice (operator's own prior published work). Load-bearing on M2.3 predicate via EF2 (signature-paper-grandfathered S_n family).",
    "lit-002-bailey-borwein-crandall-1997":
        "H9 verification_class: field_standard_practice. BBC 1997's 7350-dps PSLQ null on K_0 pure powers and the c ~ 2.06 confidence factor are community-validated experimental-mathematics empirics (BBP-class); NOT a stated theorem. Load-bearing on M2.3 predicate as the empirical-tier calibration anchor (H_empirical = 10^70 at P=2160 dps, n=15).",
    "lit-003-oeis-a002210":
        "H9 verification_class: field_standard_practice. OEIS A002210 numerical value of K_0 is the field's canonical numerical record (cross-checked against mpmath.khinchin at 500 dps per M2.2 capability audit). Load-bearing on M2.3 predicate as the K_0 value used in the B_D(C) basis.",
    "lit-009-ferguson-bailey-arno-1999":
        "H9 verification_class: proven_corollary (multi-class entry; see precision_budget.md §7 and methodology/heuristics.md H9 for the per-statement breakdown). FBA 1999 Theorem 1 (M_x >= 1/max|h_jj|) is rigorous_theorem; Theorem 3 (overshoot |m| <= gamma^{n-2} M_x) is rigorous_theorem with D2-boundary caveat; Corollary 2 (iteration bound) is proven_corollary; the folklore H ~ 10^{P/n} is field_standard_practice and is NOT stated in this paper. M2.3 predicate's rigorous tier derives from this paper's Theorem 1 + Corollary 2 via harness/rigorous_bound.py.",
    "lit-018-fidelity-no-prior-k0-pslq-refuted":
        "H9 verification_class: field_standard_practice. The literature-fidelity catch (no prior K_0 PSLQ paper exists on the mission's specific basis B_D(C)) is established via paper-reads of lit-001 (operator's signature paper) and lit-002 (BBC 1997); the conclusion is a field-survey claim, not a theorem. Load-bearing on M6 manuscript's scope-positioning story (two-anchored legitimacy per `_m2.3_calibration_anchor.md` §6.6).",
}

updated_ids = []
for e in entries:
    if e["id"] in verification_class_for:
        ivr = e["independent_verifier_result"]
        ivr["verification_class"] = verification_class_for[e["id"]]
        prior = ivr.get("notes", "")
        if "H9 verification_class:" not in prior:
            sep = " " if prior and not prior.endswith(".") else ""
            ivr["notes"] = (prior + sep + " --- " + h9_notes[e["id"]]).strip()
        updated_ids.append(e["id"])

with p.open("w", encoding="utf-8") as f:
    for e in entries:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")

print(f"Updated entries with H9 verification_class field (placed in independent_verifier_result):")
for i in updated_ids:
    print(f"  {i}")
print(f"\nTotal entries: {len(entries)}; updated: {len(updated_ids)}")
