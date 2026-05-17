# Ramanujan Journal — Portal Policy Selections

**Purpose:** Canonical record of operator's selections in the Editorial Manager policy/declaration section. Per portal instruction (multiple places): "This replaces any statement written within the manuscript and is the one that we will publish." Portal selections supersede the in-manuscript `\section*{Statements and Declarations}` block for the published RJ version.

**Surfaced to operator:** 2026-05-17 10:32 JST. All eight items surfaced together.

---

## §1. Publishing policy (checkbox)

**Portal text:** "I have read and understood the publishing model policy, and I am submitting according to this policy."

**Recommended action:** ✅ **CHECK**

**Rationale:** Acknowledgement required to proceed. RJ is a hybrid journal — operator can choose between gold OA (with APC) and subscription publishing AT ACCEPTANCE time. Checking this box does NOT commit to a specific route now; it acknowledges understanding of the hybrid model. Submission can proceed without an OA decision.

**Note:** Independent researcher with no external funding → APC affordability check needed if gold OA is chosen at acceptance. Subscription route avoids the APC question entirely. Standard non-funded subscription route is the conventional default for sole-author non-funded mathematics submissions.

---

## §2. Competing interests policy (radio)

**Recommended selection:** ✅ **"No, I declare that the authors have no competing interests..."**

**Rationale:** Consistent with manuscript `\paragraph{Competing Interests.}` paragraph: "The author has no relevant financial or non-financial interests to disclose." No employment / funding / advisory roles / patents / equity holdings in entities related to the manuscript's subject matter. Independent researcher with no institutional affiliations.

---

## §3. Dual publication (radio)

**Recommended selection:** ✅ **"No, the results/data/figures in this manuscript have not been published elsewhere, nor are they under consideration..."**

**Rationale:** The K_0 manuscript itself is NOT under review at any other peer-reviewed journal. Standard Springer policy (and standard mathematics-journal practice): preprint deposits (arXiv, Zenodo, bioRxiv) do NOT constitute "publication elsewhere" — Zenodo deposit at 10.5281/zenodo.20246707 is a preprint and is exempt.

**Caveat to surface (informational, not portal-blocking):** The author has a separate concurrent submission at JDEA (261966792, Trans-stratum continued fractions) — DIFFERENT paper on a different topic; not "results/data/figures from THIS manuscript". Not relevant to this question. If cover letter wants to proactively disclose the existence of other concurrent submissions for editorial transparency, fine; not required at this radio button.

---

## §4. Authorship (checkbox)

**Portal text:** "I confirm the corresponding author has read the journal policies and submit this manuscript in accordance with those policies."

**Recommended action:** ✅ **CHECK**

**Rationale:** Operator IS the corresponding author (sole author). The Ramanujan Journal author guidelines were paper-read 2026-05-17 in Stream S.1 (recorded at `session/files/post_m6_s1_ramanujan_requirements_report.md`). Submission packet (manuscript LaTeX source ZIP, keywords, MSC2020, Statements and Declarations, etc.) follows those policies.

---

## §5. Third party material (radio)

**Recommended selection:** ✅ **"No, all of the material is owned by the authors and/or no permissions are required."**

**Rationale:** Manuscript contains:
- All original author-written text
- No figures (`\includegraphics` audit = zero); no images imported from elsewhere
- No tables imported from other papers (all tables are LaTeX-native, author's own data)
- Standard mathematical equations (not copyrighted)
- Citations to other papers via `\cite{...}` (standard scholarly reference, fair use, not "third party material" in the copyright sense)
- Lean 4 code snippets are author's own work (M5 statement-shape encoding)

No copyrighted figures, images, or supplementary material from other sources.

---

## §6. Data availability (radio)

**Recommended selection:** ✅ **"Yes. I used or generated research data in this study."**

**Rationale:** Manuscript explicitly generates research data:
- 65 PSLQ sub-basis sweep outputs (`m32a_primary_cascade.jsonl`, `m32b_empirical_sweep.jsonl`)
- Literature claims ledger (`claims.jsonl`)
- Lean 4 statement-shape encoding (~385 lines)
- Environment lock (`M1.lock`) for reproducibility

All deposited at Zenodo concept DOI `10.5281/zenodo.20246707`. The manuscript's `\paragraph{Data Availability.}` paragraph in the Statements and Declarations section cites this DOI.

**Portal will likely ask follow-up: "Where is the data available?"** → Answer with the Zenodo concept DOI URL: `https://doi.org/10.5281/zenodo.20246707`

---

## §7. Acknowledgements (optional, free-text)

**Recommended action:** ✅ **LEAVE BLANK**

**Rationale:** Portal explicit guidance: "If you do not have anyone to acknowledge, leave it blank." The manuscript has:
- No co-authors beyond the sole author
- No human collaborators to acknowledge
- No professional writing service providers
- AI-assistance is disclosed in Author Contributions (not standard practice to dual-acknowledge in Acknowledgements; AI is a tool, not an authorship-criteria-meeting contributor)
- Software dependencies (mpmath, PARI/GP, Lean 4, Mathlib4) are cited in references — not the standard place for Acknowledgements

If operator prefers to add tool-dependency acknowledgement, suggested text: *"The author acknowledges the developers of mpmath, PARI/GP, the Lean 4 theorem prover, and the Mathlib community for the open-source mathematical software ecosystem that made this work possible."* But standard practice for mathematics papers is to cite these in references and leave Acknowledgements blank when there are no human collaborators.

---

## §8. Research funding (radio)

**Recommended selection:** ✅ **"No, this research did not receive funding."**

**Rationale:** Consistent with manuscript `\paragraph{Funding.}` paragraph: "This work received no external funding; it was conducted as independent research by the author."

---

## Summary table for portal entry

| # | Field | Selection |
|---|---|---|
| 1 | Publishing policy | ✅ Check |
| 2 | Competing interests | No (none) |
| 3 | Dual publication | No (not published or under consideration elsewhere) |
| 4 | Authorship | ✅ Check |
| 5 | Third party material | No (all original) |
| 6 | Data availability | Yes (Zenodo DOI 10.5281/zenodo.20246707) |
| 7 | Acknowledgements | (blank) |
| 8 | Research funding | No |

---

## Operator finalization

(After completing portal entry, replace the recommendation marks above with selection confirmations if any deviation. If all selected per recommendation, mark this section as confirmed.)

```
[OPERATOR CONFIRMATION: ALL SELECTIONS PER RECOMMENDATION / DEVIATIONS LISTED BELOW]

Date entered: _______
Deviations from recommendation (if any): _______
```

---

*Created 2026-05-17 in response to portal policy/declaration section surfacing.*
