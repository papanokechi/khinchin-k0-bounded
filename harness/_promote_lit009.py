"""
One-off: promote lit-009 in claims.jsonl from unverified_abstract_only -> verified
with paper_read_verified method, post H8 paper-read of FBA 1999 at U-MISSION-K halt.
"""
import json

LIT009_NEW = {
    "id": "lit-009-ferguson-bailey-arno-1999",
    "statement": (
        'Ferguson, Bailey, and Arno (1999), "Analysis of PSLQ, an integer relation finding algorithm", '
        "Mathematics of Computation 68 (1999), pp. 351-369, presents the definitive simplified PSLQ algorithm "
        "and proves: (Theorem 1) the per-iteration rigorous lower-bound certificate M_x >= 1 / max_i |h_{i,i}(k)| "
        "on the smallest possible relation norm; (Theorem 3) any PSLQ-found relation m has norm |m| <= gamma^{n-2} M_x "
        "for gamma > 2/sqrt(3) in the real case; (Corollary 2) PSLQ(tau) terminates in < (n choose 2) * log_tau(gamma^{n-1} M_x) iterations. "
        'The folklore relation "H ~ 10^(P/n)" between working precision P and certified absence of integer relations '
        "with coefficient height <= H is an empirical scaling of max_i |h_{i,i}| against P at typical PSLQ convergence; "
        "it is consistent with FBA 1999 framework but is NOT stated as a theorem in the paper. BBC 1997 (lit-002) "
        "empirically used a c ~ 2.06 confidence factor over the folklore heuristic: at n=51, P=7350 dps, they reported "
        "H = 10^70 versus 10^(7350/51) ~ 10^144 from the bare folklore. The harness M3.1 confidence-claim therefore "
        "inherits empirical_heuristic class (not rigorous_theorem class) unless a future implementation exposes "
        "max_i |h_{i,i}| directly per Theorem 1."
    ),
    "evidence_class": "primary_paper",
    "precision_or_dependencies": {
        "journal": "Mathematics of Computation",
        "volume": 68,
        "year": 1999,
        "pages": "351-369",
        "doi": "10.1090/S0025-5718-99-00995-3",
        "algorithm": "PSLQ (Partial Sum of Least sQuares)",
        "gamma_min_real": "2/sqrt(3) ~ 1.15470",
        "iteration_bound": "(n choose 2) * log_tau(gamma^(n-1) M_x)",
        "rigorous_certificate": "M_x >= 1 / max_i |h_{i,i}(k)|",
        "overshoot_bound": "|m| <= gamma^(n-2) M_x",
        "folklore_heuristic_not_in_paper": "H ~ 10^(P/n) is empirical scaling, NOT a stated theorem",
        "selected_top_10_algorithms_of_century": True,
        "originally_developed": "Ferguson-Bailey 1992",
        "preprint_date": "03 July 1997",
        "paper_read_pdf_sha256": "3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5",
    },
    "reproduce_command": (
        "Invoke-WebRequest -Uri https://www.davidhbailey.com/dhbpapers/cpslq.pdf -OutFile cpslq.pdf; "
        "Get-FileHash cpslq.pdf -Algorithm SHA256  "
        "# Expected: 3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5"
    ),
    "independent_verifier_result": {
        "verified": True,
        "method": "paper_read_verified",
        "notes": (
            "Paper retrieved 2026-05-15 ~21:30 JST from Bailey archive (cpslq.pdf preprint, identical title + authors + abstract "
            'with Math.Comp. 1999 journal version per page-1 "Ref: Mathematics of Computation, to appear (1999)" header). '
            "218,997 bytes; 26 pages; pypdf extraction 51,322 chars. Theorem 1, Theorem 3, Corollary 2, Definition 5 (gamma/tau params), "
            "and Section 8 Computer Implementation all paper-read. M2.3 U-MISSION-K halt-class finding surfaced: previous statement that "
            '"at precision P, PSLQ certifies absence of relations with height ~10^(P/dim)" is NOT a stated theorem in FBA 1999 '
            "(it is folklore consistent with Theorem 1's certificate but not theorem-grade). See harness/precision_budget.md sections 3 and 7 "
            "and _fidelity_findings.md Catch #2 for full audit trail and operator-options."
        ),
    },
    "status": "verified",
}

with open("literature/claims.jsonl", "r", encoding="utf-8") as f:
    lines = list(f)

new_lines = []
replaced = False
for line in lines:
    s = line.strip()
    if not s:
        new_lines.append(line)
        continue
    obj = json.loads(s)
    if obj["id"] == "lit-009-ferguson-bailey-arno-1999":
        new_lines.append(json.dumps(LIT009_NEW, ensure_ascii=False) + "\n")
        replaced = True
    else:
        if not line.endswith("\n"):
            line += "\n"
        new_lines.append(line)

if not replaced:
    raise SystemExit("lit-009 not found in claims.jsonl")

with open("literature/claims.jsonl", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("lit-009 entry updated in claims.jsonl")
