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

**IMPORTANT:** Editorial Manager compiles the LaTeX source ZIP into a PDF itself for peer review. **Do NOT upload `main.pdf` separately** — the portal will reject it as redundant or use it ambiguously against the source build. Verbatim portal instruction (captured 2026-05-17 10:16 JST):

> "It's best if your manuscript — including all text, figures and tables — is in one editable file. Upload your manuscript in an editable format for peer review (maximum 2GB). This will be either: a Word document … or LaTeX documents with figures and tables compressed into a .zip format. We will compile these into a PDF for peer review."

A pre-built archive is staged at `submission_log/ramanujan_submission_packet.zip`.

Files to upload at portal:

| Order | File | Path | Purpose |
|---|---|---|---|
| 1 | `ramanujan_submission_packet.zip` | `submission_log/ramanujan_submission_packet.zip` | ZIP containing `main.tex` + `references.bib` + `main.bbl` (24,048 B; flat structure, no subfolders inside). **Portal compiles this into the peer-review PDF.** |
| 2 | Cover letter | `submission_log/ramanujan_journal_cover_letter.pdf` (117,599 B; typeset from `ramanujan_journal_cover_letter.tex`) | Uploaded to the portal's "Cover Letter" file slot. Operator-finalized 2026-05-17 ~10:58 JST. Plain-text record preserved in `ramanujan_journal_cover_letter.md`. |

**Files NOT uploaded:**
- `paper/main.pdf` — portal generates the review PDF from the ZIP; do not upload separately
- Supplementary materials — none; the Zenodo deposit (concept DOI `10.5281/zenodo.20246707`) is cited from the manuscript's Data Availability statement per RJ's encouraged archiving pattern

**ZIP contents (flat, no subfolders per RJ guidelines):**

| Filename | Uncompressed | Compressed | Purpose |
|---|---|---|---|
| `main.tex` | 58,120 B | 20,010 B | LaTeX source (article class; longtable + standard packages) |
| `references.bib` | 5,665 B | 2,373 B | BibTeX bibliography (9 entries; DOIs as full URLs per RJ §3) |
| `main.bbl` | 2,538 B | 1,355 B | Pre-compiled bibliography (insurance against portal BibTeX issues; portal may regenerate, harmless if so) |

**Patch log:**
- 2026-05-17 ~10:48 JST — `\texorpdfstring` patch applied to `paper/main.tex` line 376 (`\subsection{Algorithm-chain citation and {\boldmath$\gamma$} boundary case}` → wrapped math with `\texorpdfstring{{\boldmath$\gamma$}}{gamma}`) to silence the hyperref "Token not allowed in PDF string" warning identified during EM portal upload-check. Cosmetic only; no semantic change. PDF rebuilt 683,629 B; ZIP rebuilt 24,048 B. Previous ZIP backed up as `submission_log/ramanujan_submission_packet.zip.bak_before_texorpdfstring` (24,020 B).

**Source dependency audit:**
- No `\input` / `\include` directives — manuscript is monolithic
- No `\includegraphics` — no figures (all tables are typeset directly via `longtable`)
- Non-standard packages: only `longtable` (present in every TeX distribution)
- All bibliography rendering controlled by `\bibliographystyle{plain}` + `references.bib`

**Submission directory structure (per RJ guidelines):** No subfolders inside ZIP.

**Rebuilding the ZIP** (if `paper/main.tex` or `paper/references.bib` is edited):
```powershell
# From repo root, after PDF rebuild has refreshed main.bbl:
$staging = "submission_log\_staging_rj_packet"
New-Item -Path $staging -ItemType Directory -Force | Out-Null
Copy-Item paper\main.tex, paper\references.bib, paper\main.bbl $staging\
Compress-Archive -Path "$staging\*" -DestinationPath submission_log\ramanujan_submission_packet.zip -Force
Remove-Item $staging -Recurse -Force
```
Note: regenerate `main.bbl` first via `pdflatex main; bibtex main; pdflatex main; pdflatex main` in `paper/` if bib was edited.

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
10. Upload files in order from §C: **upload ONLY `submission_log/ramanujan_submission_packet.zip` in the manuscript-upload field. The portal compiles the ZIP into a peer-review PDF itself — do NOT upload `paper/main.pdf` separately.** Portal instruction verbatim 2026-05-17: "LaTeX documents with figures and tables compressed into a .zip format. We will compile these into a PDF for peer review."
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
| Submission ID | `d824d5ae-683f-4c50-98ec-3622c05fcfa0` (Springer Snapp UUID; not classic `RAMA-D-YY-NNNN`) |
| Submission version | v.1.0 |
| EM tracking number | (Snapp portal — not classic Editorial Manager; UUID above serves as primary tracking key) |
| Submission date (JST) | 2026-05-17 ~11:10 JST |
| Submission date (UTC) | 2026-05-17 ~02:10 UTC |
| Acknowledgement email received | (pending — operator to confirm receipt) |
| Editor assigned | (pending — Technical check in progress as of capture) |
| Initial decision (typical: 4–8 weeks for RJ) | — |
| Manuscript HEAD at submission | `fb47df5c20c73b6645664bd9eeb3265985165282` (`fb47df5`, msg "Stream S.2 Data Availability Statement substrate (portal field)") **with uncommitted working-tree changes** for the `\texorpdfstring` patch (`paper/main.tex`, rebuilt `paper/main.pdf`, rebuilt `submission_log/ramanujan_submission_packet.zip` 24,048 B, operator-finalized cover letter MD/TeX/PDF, this §H update). Operator to commit working-tree post-capture for a single canonical submission commit. |
| Manuscript File uploaded | `ramanujan_submission_packet.zip` (24,048 B; contains `main.tex` 58,120 B + `references.bib` 5,665 B + `main.bbl` 2,538 B; flat structure) |
| Cover letter uploaded | `ramanujan_journal_cover_letter.pdf` (117,599 B; typeset from `ramanujan_journal_cover_letter.tex`) |
| Portal status snapshot at capture | Submission received: **complete**. Technical check: **in progress**. |
| Submission title (portal-confirmed) | "A bounded two-tier null result for integer relations on a hybrid Khinchin-K₀ basis, with a documented capability gap and a Lean 4 statement-shape encoding" |
| Submission type (portal-confirmed) | research |
| Journal (portal-confirmed) | The Ramanujan Journal |

### §H.1 — Capture-time notes

- Portal is **Springer Snapp** (UUID-based submission IDs), not classic Editorial Manager. The pre-submission walkthrough in §E was written assuming classic EM; field-by-field flow was substantially similar but the submission ID format differs.
- Technical check is in progress at capture time. If technical check identifies any issue (e.g. file format, missing field), expect an automated email and a Snapp-side "needs correction" status. Operator will resubmit corrections via the portal Author Tasks queue.
- Cover letter PDF was prepared 2026-05-17 ~10:58 JST per operator override directive ("just prepare cover letter that can be uploaded without edits") which authorized CLI to finalize against the §G operator-approved substrate. Plain-text mirror preserved in `ramanujan_journal_cover_letter.md`.
- Manuscript ZIP was rebuilt 2026-05-17 ~10:49 JST with the `\texorpdfstring{{\boldmath$\gamma$}}{gamma}` patch at `paper/main.tex` line 376 to silence the hyperref "Token not allowed in PDF string" warning. Pre-patch ZIP preserved as `ramanujan_submission_packet.zip.bak_before_texorpdfstring` (24,020 B).
- Abstract field in the Snapp Details screen was overwritten 2026-05-17 ~11:08 JST (operator paste) from `ramanujan_journal_abstract_portal_field.md` to repair the auto-extractor's mangled extraction (3 stripped math segments, raw `\fsp{}`/`\pc{}`/`\K`/`\Hempop`/`\Hrig` macros, raw `\cite{...}` keys, and the entirely-missing H_rig rigorous-tier clause). 249-word Unicode plain-text version posted.
- Research Square preprint toggle: **No** (operator selected per CLI recommendation 2026-05-17 ~10:54 JST; rationale: Zenodo concept DOI already provides priority + permanence + citability).

### §H.1a — Zenodo title divergence: documented (operator-best-choice option b, 2026-05-17 ~12:10 JST)

The Zenodo deposit at concept-DOI `10.5281/zenodo.20246707` (version-DOI `10.5281/zenodo.20246708`, rev 4) carries an older 17-word title:

> "A bounded two-tier null result for integer relations on a hybrid Khinchin-K_0 basis, with a structural gap"

The submitted PDF and the Snapp portal Details screen both carry the current 24-word title:

> "A bounded two-tier null result for integer relations on a hybrid Khinchin-K₀ basis, with a documented capability gap and a Lean 4 statement-shape encoding"

The 24-word title adds the trailing "*and a Lean 4 statement-shape encoding*" clause (post-deposit M5 surfacing) and refines "structural gap" → "documented capability gap" for nomenclatural precision. Substantive content of the work is identical between the two snapshots. Per operator best-choice directive 2026-05-17 ~12:10 JST, **option (b) accept-and-document** is the resolution disposition for v.1.0: the Zenodo deposit is the authoritative substrate snapshot at deposit time; the version-DOI `10.5281/zenodo.20246708` is the cross-platform record of that snapshot; the manuscript's Data Availability statement correctly cites both concept DOI and version DOI. Re-deposit under a new version DOI is deferred unless the eventual RJ revision cycle independently requires a title change at Zenodo. Mint-new-version (option a) and revision-cycle-pairing (option c) remain available; either becomes a Stream S follow-up if surfaced.

### §H.2 — Immediate follow-up checklist

1. ~~Operator commits working-tree to capture the submission state under a single canonical commit.~~ **FIRED 2026-05-17 ~12:11 JST** per operator best-choice directive; canonical commit + `submitted/ramanujan-v1` tag at HEAD.
2. Watch operator email inbox for Snapp acknowledgement (typically within minutes-hours of capture).
3. Watch for Technical-Check completion notice; if "needs correction" status appears, surface in inbox_entries.
4. Update §H "Editor assigned" once initial editor is named (typically 1–3 days for RJ).
5. Snapp-side typical timeline: Technical check → Editor assignment → Reviewer invitations → First decision (RJ historical: 4–8 weeks median).

## §I — Submission hygiene rules (R2 + R3 standing)

- **R2** — Submission-portal events fire ONLY via operator manual click. CLI does not have portal credentials. CLI-prepared substrate + operator-executed submission = "Option β" pattern (analogous to M6 Zenodo deposit).
- **R3** — On portal-submit click, operator updates §H of this log within same session for capture integrity. If §H cannot be filled same-day, operator surfaces partial data + reason for delayed capture.

---

*This log is updated as a single source-of-truth for the Ramanujan Journal 2026 submission cycle. Update via direct edit + commit. No subfolders; this file lives at `submission_log/ramanujan_journal_submission_2026.md`.*
