# Ramanujan Journal — Data Availability Statement (portal field)

**Purpose:** Data Availability Statement entered into Editorial Manager portal at submission time. Per portal example library (2026-05-17): the K_0 manuscript matches the first example pattern ("Publicly available in a repository"). The Zenodo concept DOI plays the role analogous to the example's GEO accession number.

**Portal field expectation:** Plain text, one paragraph. Will be published in the article and must be consistent with the manuscript's in-text Data Availability paragraph (in the `\section*{Statements and Declarations}` block at `paper/main.tex`).

**Per portal instruction (multiple fields):** "This replaces any statement written within the manuscript and is the one that we will publish."

---

## OPTION A — Comprehensive artefact enumeration (RECOMMENDED, ~620 chars)

> All canonical research artefacts supporting the findings of this study—including the manuscript LaTeX source, the cascading-precision PSLQ sweep outputs (`m32a_primary_cascade.jsonl` for the primary basis, `m32b_empirical_sweep.jsonl` for the 65 sub-bases), the environment lock file (`M1.lock`), the literature claims ledger (`claims.jsonl`), and the Lean 4 statement-shape encoding (Mathlib4 v4.14.0)—are deposited at Zenodo under concept DOI 10.5281/zenodo.20246707 (version DOI 10.5281/zenodo.20246708, CC-BY-4.0) and are publicly available at https://doi.org/10.5281/zenodo.20246707. The complete reproducibility-pinned source repository is additionally available at https://github.com/papanokechi/khinchin-k0-bounded (tag gold/M6).

## OPTION B — Concise paragraph (~480 chars)

> All research artefacts supporting the findings of this study (manuscript LaTeX source, PSLQ sweep outputs, environment lock, literature claims ledger, and Lean 4 statement-shape encoding) are deposited at Zenodo under concept DOI 10.5281/zenodo.20246707 (version DOI 10.5281/zenodo.20246708, CC-BY-4.0) and are publicly available at https://doi.org/10.5281/zenodo.20246707. The source repository with full reproducibility pinning is additionally available at https://github.com/papanokechi/khinchin-k0-bounded (tag gold/M6).

## OPTION C — Minimal, closest to portal example pattern (~290 chars)

> All canonical research artefacts supporting this study were deposited at Zenodo under concept DOI 10.5281/zenodo.20246707 and are available at the following URL: https://doi.org/10.5281/zenodo.20246707. The source repository is publicly available at https://github.com/papanokechi/khinchin-k0-bounded (tag gold/M6).

---

## Comparison to portal example

Portal example (publicly available in a repository):
> "PRO-Seq data were deposited into the Gene Expression Omnibus database under accession number GSE85337 and are available at the following URL: https://identifiers.org/geo:GSE85337."

The K_0 manuscript's parallel is:
- "PRO-Seq data" → "canonical research artefacts" (PSLQ sweep data, claims ledger, environment lock, Lean encoding, LaTeX source)
- "Gene Expression Omnibus database" → "Zenodo"
- "accession number GSE85337" → "concept DOI 10.5281/zenodo.20246707"
- "URL: https://identifiers.org/geo:GSE85337" → "URL: https://doi.org/10.5281/zenodo.20246707"

All three options preserve this DOI-as-accession-number pattern.

---

## Consistency with manuscript

The in-manuscript `\paragraph{Data Availability.}` paragraph (in `paper/main.tex` Statements and Declarations section) reads:

> All canonical artefacts (manuscript LaTeX source, empirical PSLQ sweep outputs, environment lock file, literature claims ledger, and the M5 Lean 4 statement-shape encoding) are deposited at Zenodo under concept DOI 10.5281/zenodo.20246707 (version DOI 10.5281/zenodo.20246708, CC-BY-4.0). The source repository is publicly available at https://github.com/papanokechi/khinchin-k0-bounded (tag gold/M6; SHA-pinned tags gold/M1--gold/M6 snapshot each completed milestone of the mission).

**Option B is the closest match** to this manuscript text with minor adjustments: (1) explicit "publicly available at https://doi.org/..." URL phrase that mirrors the portal example pattern; (2) drops the "gold/M1--gold/M6" milestone-snapshot detail that's manuscript-context-specific.

**Option A** adds the granular file names (m32a/m32b JSONLs) for reviewer transparency.

**Option C** is minimum-form; loses the artefact enumeration.

---

## Recommendation

✅ **OPTION B** for the portal field.

Rationale: Matches portal example pattern with the "publicly available at URL" phrase; lists artefacts at category level (without filenames) for editorial readability; preserves CC-BY-4.0 license disclosure; stays under 500 characters which is comfortable for portal text fields.

If the portal field has a stricter character cap (e.g., 250 chars), fall back to Option C. If the operator prefers maximum reviewer transparency, use Option A.

---

## Operator finalization

```
[OPERATOR-SELECTED OPTION (A / B / C / EDITED): _______]

[FINALIZED PORTAL-PASTED TEXT BELOW]
______________________________________________________________________

______________________________________________________________________
```

---

## Companion submission_log files

| File | Purpose |
|---|---|
| `ramanujan_journal_submission_2026.md` | Master submission log |
| `ramanujan_journal_cover_letter.md` | Cover letter (operator-drafted) |
| `ramanujan_journal_author_contributions_portal_field.md` | Author Contributions portal field substrate |
| `ramanujan_journal_data_availability_portal_field.md` | THIS FILE — Data Availability portal field substrate |
| `ramanujan_journal_portal_policy_selections.md` | 8 policy-section selections |
| `ramanujan_journal_berndt_inquiry_draft.md` | S.3 pseudonymity inquiry substrate |
| `ramanujan_submission_packet.zip` | Source-files ZIP |

*Created 2026-05-17 in response to portal Data Availability Statement examples surfacing.*
