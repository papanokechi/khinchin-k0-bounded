# Ramanujan Journal — Submission Log

**Manuscript:** A bounded two-tier null result for integer relations on a hybrid Khinchin-$K_0$ basis, with a documented capability gap and a Lean 4 statement-shape encoding
**Operator:** Papanokechi (ORCID 0009-0000-6192-8273)
**Stream:** Post-M6 Stream S — submission cycle initiation
**Created:** 2026-05-17

---

## §A — Pre-submission state

| Item | State |
|---|---|
| Repository | `papanokechi/khinchin-k0-bounded` (public) |
| Repo HEAD at packet prep | post-`8f070ed` on `main` (after gold/M6 = `67655c0`) |
| Zenodo concept DOI | `10.5281/zenodo.20246707` |
| Zenodo version DOI | `10.5281/zenodo.20246708` |
| Paper PDF size / pages | 683,604 bytes / 15 pp |
| Word count (abstract) | 249 words (within RJ 150-250 range) |
| Statements & Declarations section | Present (`paper/main.tex`, before bibliography) |
| Keywords block | Present (6 keywords) |
| MSC2020 block | Present (Primary 11Y60; Secondary 11J81, 11J72, 68W30) |
| Author affiliation | "Independent researcher, Yokohama, Japan" |

## §B — Submission portal target

| Field | Value |
|---|---|
| Journal | The Ramanujan Journal (Springer) |
| Electronic ISSN | 1572-9303 |
| Print ISSN | 1382-4090 |
| Editor-in-Chief | Bruce C. Berndt (University of Illinois at Urbana-Champaign) |
| Submission portal | https://www.editorialmanager.com/rama/ |
| Maintenance window to avoid | Mon May 18 2026, 15:00–17:00 EST (per Editorial Manager notice) |
| Author guidelines source | https://www.springer.com/journal/11139/submission-guidelines (paper-read 2026-05-17) |

## §C — Submission packet manifest

Files to upload at portal (Author Guidelines: source `.tex` + `.bib` MANDATORY; PDF for review build):

| Order | File | Path | Purpose |
|---|---|---|---|
| 1 | `main.tex` | `paper/main.tex` | LaTeX source |
| 2 | `references.bib` | `paper/references.bib` | BibTeX bibliography |
| 3 | `main.pdf` | `paper/main.pdf` | Compiled PDF for editorial review |
| 4 | Cover letter | (operator-drafted) | Submitted via portal "Cover Letter" field |

**Supplementary materials:** None uploaded directly to portal. Manuscript Data Availability statement cites Zenodo concept DOI `10.5281/zenodo.20246707` per RJ's encouraged archiving pattern. The Zenodo deposit holds the eight canonical artifacts (`main.pdf`, `main.tex`, `references.bib`, `preflight_compliance.md`, `M1.lock`, `m32a_primary_cascade.jsonl`, `m32b_empirical_sweep.jsonl`, `claims.jsonl`; ~1.16 MB total).

**Submission directory structure (per RJ guidelines):** No subfolders.

## §D — Pre-submission operator decisions still pending

| ID | Decision | Status | CLI substrate |
|---|---|---|---|
| S.2a | Template — Option A (no reformat) vs Option B (Springer Nature `sn-jnl.cls`) | CLI defaulted to Option A; awaiting operator confirmation | Manuscript currently uses `article` class. Reformat = 4–8 h work + nonzero risk of regression. RJ guidelines permit general format. |
| S.2d | Keywords — final 4-6 selection from 16 candidates | CLI-proposed 6 in manuscript; operator may swap | See §F below for full 16-keyword candidate list with CLI rationale |
| S.3 | Pseudonymity disclosure — pseudonym-only / editor-disclosed legal name / decline-and-redirect | Awaiting operator | RJ author guidelines silent on human pseudonyms; only LLM-authorship excluded. Pre-submission inquiry email substrate drafted at `submission_log/ramanujan_journal_berndt_inquiry_draft.md`. |
| — | Cover letter | Operator drafts (per directive: CLI does NOT draft cover letters) | Content checklist in §G below |
| — | Suggested referees (2-3, if portal requests) | Awaiting operator | D-216-3 PROMOTED coauthor candidate list is one input source |

## §E — Submission portal flow (operator walkthrough)

1. Navigate to https://www.editorialmanager.com/rama/
2. Register/login as author. ORCID: `0009-0000-6192-8273`
3. Click "Submit New Manuscript"
4. Article type: select "Original Research" (or RJ's nearest equivalent)
5. Title: paste from `paper/main.tex` L64-66 (the 17-word hybrid)
6. Abstract: paste from `paper/main.tex` L76-111 (249 words)
7. Keywords: paste from §F (selected 4-6)
8. MSC2020 codes: Primary 11Y60; Secondary 11J81, 11J72, 68W30
9. Author info: Papanokechi, Independent researcher, Yokohama, Japan, ORCID 0009-0000-6192-8273
10. Upload files in order from §C
11. Statements & Declarations: portal may auto-extract from manuscript, or prompt for re-entry. Re-entry text is verbatim from `paper/main.tex` `\section*{Statements and Declarations}`.
12. Cover letter: paste operator-finalized text
13. Suggested referees: if prompted, enter 2-3 names
14. Review & submit
15. Capture submission ID (typically `RAMA-D-YY-NNNN` format) + EM tracking number + date
16. Update §H below with capture data

## §F — Keywords candidate set (CLI-curated)

**Source:** `handoff/zenodo_metadata.json` `keywords` field (16 entries, deposit 10.5281/zenodo.20246708).

**CLI top-6 selection (currently in `paper/main.tex`):**

1. **Khinchin's constant** — primary mathematical subject; load-bearing for RJ scope-relevance
2. **integer relation detection** — methodology family; distinguishes paper from pure number-theory result
3. **PSLQ** — specific algorithmic method; recognizable to RJ readership via BBC 1997 legacy
4. **two-tier predicate** — distinctive contribution (verification-class taxonomy); CLI-novel terminology
5. **experimental mathematics** — methodological identifier; bridges to Borwein-Bailey-Plouffe tradition
6. **Lean~4** — formal verification angle; signals modern reproducibility discipline

**Other 10 candidates (operator may swap for any of the above):**

7. bounded null result
8. rigorous bound
9. empirical bound
10. Ferguson-Bailey-Arno (citation; less keyword-shaped)
11. Bailey-Plouffe (citation; less keyword-shaped)
12. Mathlib4 (implementation detail of #6)
13. statement-shape verification (sub-aspect of #6)
14. capability gap (mission-narrative term; CLI views as too internal-jargon)
15. AEAL discipline (methodology paper material; not K_0 manuscript)
16. reproducibility (too generic; subsumed by #5)

**To override:** edit `paper/main.tex` keywords block (search for `\noindent\textbf{Keywords:}` between abstract end and `\section{Introduction}`).

## §G — Cover letter content checklist (substrate, not draft)

**Operator drafts; CLI does NOT draft cover letters per Stream S directive.** Useful content elements to include if helpful:

- Brief statement of contribution (1-2 sentences): two-tier verification taxonomy + the bounded null on the hybrid Khinchin-K_0 basis + the structural-gap documentation + the Lean 4 statement-shape encoding
- Suitability for RJ: number-theory result on a constant whose transcendence is a major open question; methodology relevant to experimental number theorists
- Independent-researcher disclosure: matches RJ explicit policy support for non-affiliated researchers
- Data Availability mention: full Zenodo deposit + public repository
- Pseudonymity stance (per S.3 resolution): include disclosure as appropriate to the option operator selects
- Originality + non-concurrent-submission statement (standard journal expectation)

## §H — Post-submission capture (FILL AFTER SUBMISSION FIRES)

| Field | Value |
|---|---|
| Submission ID | — |
| EM tracking number | — |
| Submission date (JST) | — |
| Submission date (UTC) | — |
| Acknowledgement email received | — |
| Editor assigned | — |
| Initial decision (typical: 4–8 weeks for RJ) | — |
| Manuscript HEAD at submission | — |

## §I — Submission hygiene rules (R2 + R3 standing)

- **R2** — Submission-portal events fire ONLY via operator manual click. CLI does not have portal credentials. CLI-prepared substrate + operator-executed submission = "Option β" pattern (analogous to M6 Zenodo deposit).
- **R3** — On portal-submit click, operator updates §H of this log within same session for capture integrity. If §H cannot be filled same-day, operator surfaces partial data + reason for delayed capture.

---

*This log is updated as a single source-of-truth for the Ramanujan Journal 2026 submission cycle. Update via direct edit + commit. No subfolders; this file lives at `submission_log/ramanujan_journal_submission_2026.md`.*
