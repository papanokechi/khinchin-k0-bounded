# harness/_pslq_candidates/ — paper-read provenance cache

This directory holds local PDF + text-extraction caches of papers paper-read for H8 verification.

**The binary files (.pdf, .txt) are gitignored** — provenance lives in:
1. The SHA-256 hashes recorded in the relevant ledger entry (e.g., `literature/lit-009-ferguson-bailey-arno-1999.md` §1)
2. The retrieval URL recorded in the ledger entry's `reproduce_command` field of `literature/claims.jsonl`
3. The relevant section of `harness/precision_budget.md` (or other consuming document) that quotes the paper-read content

## Files cached locally (gitignored)

| Filename | Source URL | SHA-256 | Pages | Bytes | Used by |
|---|---|---|---|---|---|
| `cpslq.pdf` | `https://www.davidhbailey.com/dhbpapers/cpslq.pdf` | `3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5` | 26 | 218,997 | Ferguson-Bailey-Arno 1999 (lit-009 paper-read, M2.3 U-MISSION-K) |
| `pslq.pdf` | `https://www.davidhbailey.com/dhbpapers/pslq.pdf` | `C9E1670C9288B6F3887A734ADE97AC9A8AA44AE221BA09C84865F37F6062B7A2` | 14 | 113,279 | Ferguson-Bailey 1992 (RNR-91-032 precursor; not currently in M3.1 dep chain) |
| `fba1999_text.txt` | (derived from `cpslq.pdf` via pypdf) | n/a | n/a | 51,322 chars | Search/quote target during paper-read |

## Re-verification

To reproduce the FBA 1999 paper-read evidence:

```powershell
Invoke-WebRequest -Uri https://www.davidhbailey.com/dhbpapers/cpslq.pdf -OutFile harness/_pslq_candidates/cpslq.pdf
Get-FileHash harness/_pslq_candidates/cpslq.pdf -Algorithm SHA256
# Expected: 3E330BC11697DBB122D9ADC7357405E7D318DCEE9258CE09BFFD2D47612890B5
```

Then re-extract text:

```powershell
python -c "from pypdf import PdfReader; r = PdfReader('harness/_pslq_candidates/cpslq.pdf'); open('harness/_pslq_candidates/fba1999_text.txt','w',encoding='utf-8').write(''.join('=== PAGE '+str(i+1)+' ===\n'+(p.extract_text() or '')+'\n\n' for i,p in enumerate(r.pages)))"
```

## AEAL discipline

- PDFs in this directory are **evidence cache only**, not authority. Authority lives in the canonical journal version (DOI-resolved). When discrepancies arise between the cached PDF and the AMS canonical version, the AMS canonical wins.
- PDFs in this directory are **not committed to the repo** because they are reproducible from the URL + SHA-256 stamp. Committing them would bloat history with ~330 KB of binary content per paper.
- The SHA-256 in the consuming document (e.g., `lit-009-...md` §1) is the cryptographic anchor; if a future fetch returns a different SHA-256, that itself is evidence (URL drift / paper revision / cache poisoning).
