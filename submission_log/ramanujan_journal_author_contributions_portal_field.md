# Ramanujan Journal — Author Contributions Statement (portal field)

**Purpose:** Author Contributions Statement entered into Editorial Manager portal at submission time. Per portal instruction (verbatim 2026-05-17 10:29 JST): "This replaces any statement written within the manuscript and is the one that we will publish."

**Implication:** Whatever is pasted into the portal supersedes the `\paragraph{Author Contribution.}` block inside `paper/main.tex` `\section*{Statements and Declarations}`. The published-by-RJ version uses the portal text; the Zenodo deposit version (immutable) retains the manuscript paragraph. Small known divergence; acceptable.

**Per Springer authorship policy:** https://www.springernature.com/gp/authors/journal-policies/authorship-principles
- Authorship requires substantial contribution + accountability
- Use initials to refer to each author's contribution
- Specify who did what
- LLMs are NOT authors (current Springer/Ramanujan Journal policy)

**Sole-author convention (this manuscript):** initial "P." (single-letter from "Papanokechi"). AI-assistance is a research tool, not an author.

---

## OPTION A — Minimal sole-author statement (recommended)

> P. (Papanokechi) is the sole author of this work. P. designed the study, implemented all software, performed all computations, conducted all analyses, and wrote the manuscript. AI-assisted execution (GitHub Copilot CLI driving an Anthropic Claude language model) was used as a research tool under the AEAL eleven-heuristic accountability discipline documented in the manuscript appendix; the author retains full accountability for all claims, methodology choices, and the final published result.

**Character count:** ~580. Standard sole-author convention; reads naturally.

## OPTION B — CRediT-taxonomy-aligned (more formal)

> P. (Papanokechi) is the sole author and is solely responsible for: Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data Curation, Writing – Original Draft, Writing – Review & Editing, and Visualization. AI-assisted execution (GitHub Copilot CLI driving Anthropic Claude language models) was used as a research tool under the AEAL eleven-heuristic accountability discipline documented in the manuscript appendix; the author retains full accountability for all claims, methodology choices, and the final published result.

**Character count:** ~640. Aligns to Springer's CRediT taxonomy adoption; preferable if RJ portal expects CRediT roles.

## OPTION C — Minimal without AEAL disclosure (if AI-disclosure is preferred elsewhere)

> P. (Papanokechi) is the sole author of this work. P. designed the study, implemented all software, performed all computations, conducted all analyses, wrote the manuscript, and reviewed the final version.

**Character count:** ~225. Cleanest; AI-assistance disclosure moved to a separate portal field (typical Editorial Manager has an explicit "AI-assistance disclosure" question separate from authorship).

---

## Operator selection

(Operator: mark which option was pasted into the portal field, and paste the FINALIZED text below for the canonical record. If operator-edited from one of A/B/C, paste the edited version.)

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
| `ramanujan_journal_berndt_inquiry_draft.md` | S.3 pseudonymity inquiry email substrate |
| `ramanujan_journal_cover_letter.md` | Cover letter (operator-drafted) |
| `ramanujan_journal_author_contributions_portal_field.md` | THIS FILE — Author Contributions portal field substrate |
| `ramanujan_submission_packet.zip` | Source-files ZIP |

*Created 2026-05-17 in response to portal Author Contributions Statement field surfacing.*
