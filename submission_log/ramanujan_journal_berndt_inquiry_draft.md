# Pre-submission inquiry email — substrate draft

**Purpose:** Resolve Stream S.3 pseudonymity policy ambiguity BEFORE firing the Editorial Manager submission. The Ramanujan Journal author guidelines (paper-read 2026-05-17) explicitly exclude LLM authorship but are silent on whether human pseudonymous authors are accepted. A pre-submission policy clarification from the Editor-in-Chief avoids a desk-rejection scenario or post-submission disclosure complication.

**Status:** SUBSTRATE — operator finalizes wording, decides whether to send, and selects which of the three S.3 paths to default to in the email.

**Per Stream S directive:** CLI does NOT decide pseudonymity. CLI prepares substrate; operator owns the email content and the send decision.

---

## Recipient & metadata

| Field | Value |
|---|---|
| To | Bruce C. Berndt, Editor-in-Chief, The Ramanujan Journal |
| Email | (operator looks up via journal masthead at https://link.springer.com/journal/11139/editors or direct U. Illinois contact) |
| Subject (option) | "Pre-submission policy inquiry: pseudonymous authorship for an independent-researcher submission" |
| From | Papanokechi (ORCID 0009-0000-6192-8273) |
| Recommended timing | Before Editorial Manager submission fire; expect 3-10 business days for editorial reply |

---

## Substrate text (operator revises voice + final wording)

> Dear Professor Berndt,
>
> I am preparing a manuscript for submission to The Ramanujan Journal and wish to clarify the journal's policy on a single matter before submitting via Editorial Manager.
>
> **Background.** I am an independent researcher with no institutional affiliation, and I publish under the pseudonym "Papanokechi" with ORCID 0009-0000-6192-8273. The pseudonym is consistent across all my prior publications and Zenodo deposits, and the ORCID provides a stable scholarly identity. I have read the Ramanujan Journal author guidelines, which explicitly support independent-researcher submissions but do not directly address the question of pseudonymous human authorship (the exclusion in the guidelines is specifically on LLM-as-author).
>
> **Inquiry.** Could you let me know which of the following the Ramanujan Journal would accept for a submission of an original research manuscript?
>
> 1. Submission under the pseudonym "Papanokechi" with ORCID 0009-0000-6192-8273 as the published byline, with no additional disclosure required to the editor.
> 2. Submission under the pseudonym "Papanokechi" on the published byline, with the editor (yourself or the assigned handling editor) confidentially informed of my legal name. The legal-name information would not appear in the published paper.
> 3. Submission requires the legal name to appear on the published byline; pseudonymous publication is not accepted.
>
> **Manuscript context (for relevance assessment).** The manuscript reports a bounded two-tier null result for integer relations on a hybrid basis built from Khinchin's constant K_0, conducted using cascading-precision PSLQ with rigorous-tier bounds derived from Ferguson-Bailey-Arno 1999. The work also includes a documented capability gap at the symbolic-closure stage (K_0's unresolved transcendence status) and a Lean 4 statement-shape encoding. All canonical artefacts (manuscript source, empirical sweep outputs, environment lock file, literature claims, and the Lean 4 encoding) are deposited at Zenodo under concept DOI 10.5281/zenodo.20246707 and the source repository is publicly available at https://github.com/papanokechi/khinchin-k0-bounded.
>
> I am happy to provide additional information about the manuscript or about my publication track if useful to your assessment of which option above is appropriate.
>
> Thank you for your time on this question.
>
> Sincerely,
> Papanokechi
> ORCID: 0009-0000-6192-8273
> Yokohama, Japan
> Repository: https://github.com/papanokechi/khinchin-k0-bounded

---

## Operator decisions before sending

| Decision | Options |
|---|---|
| Default preferred option to indicate in the email (if asked) | (1) pseudonym-only / (2) pseudonym + editor-disclosed legal name / "no preference, awaiting your guidance" |
| Whether to attach the manuscript PDF as preview | Attach (gives editor immediate context for assessment) / Do not attach (keep inquiry crisp; editor can request) |
| Whether to send at all | Send now (resolves S.3 before submission) / Skip inquiry (submit under pseudonym + handle disclosure post-rejection if any) |

## Post-reply handling

- If reply confirms option 1 (pseudonym-only accepted): proceed with Editorial Manager submission as-is; close S.3 in `submission_log/ramanujan_journal_submission_2026.md` §D.
- If reply confirms option 2 (pseudonym + editor-disclosed legal name): submit via Editorial Manager and disclose legal name to handling editor via portal cover-letter field or follow-up email. Operator decides whether option 2 is acceptable.
- If reply states option 3 (legal name on byline required): operator decides redirect (per Stream S directive: candidate redirect targets in order = JNT → Exp Math → Integers per redirect protocol in `handoff/summary.md` §3).
- If no reply within 10 business days: operator decides whether to proceed under option 1 assumption or escalate.

---

*Substrate prepared 2026-05-17. Update operator-finalized version inline above and remove this footer when ready to send.*
