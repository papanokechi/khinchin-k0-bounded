# khinchin-k0-bounded

A bounded-attack mission on the arithmetic nature of Khinchin's constant $K_0$,
operated under the **AEAL v1** (Agent Epistemic Accountability Layer) discipline.

> **Bounded sub-question (M1.2 form, post-U-MISSION-G refinement).**
> Test, at 500 dps via PSLQ with cascading-precision verification, for integer
> relations among the hybrid basis
> $$B_D(\mathcal{C}) = \{1,\ K_0,\ K_0^2,\ \ldots,\ K_0^D,\ \log K_0\} \;\cup\; \{K_0 \cdot c : c \in \mathcal{C}\}$$
> where $\mathcal{C}$ is a finite named-constant set (concrete members pinned at
> M2.3; anticipated subset of $\{\pi, e, \log 2, \zeta(2), \zeta(3), G, \gamma\}$),
> degree bound $D \le 6$, height bound $H$ specified in M2.3.

**Out of scope (explicit exclusion):** the signature-statistic coordinate family
$\{S_n,\ \log S_n,\ S_n - K_0,\ \log n\}$ on $\pi$'s continued-fraction
partial-quotient sequence was tested under AEAL discipline in operator's prior
work [`papanokechi/khinchin-signature-pslq`](https://github.com/papanokechi/khinchin-signature-pslq)
(Apr 2026, MIT). The present mission implements the natural extension that the
signature paper's Discussion section identified as *out-of-scope-but-open*.

## Mission framing

- **Six milestones M1–M6**, one Gold Freeze per milestone, on a six-week DAG.
- **AEAL discipline:** no claim without a 7-field JSON entry in `claims/`;
  capability gaps are first-class deliverables; negative results are
  publishable.
- **No "breakthrough" / "novel" / "first" / "solved" language.** All language
  is "extends" / "rules out" / "formalizes" / "verifies in range".

See `targets/selected.md` for the full bounded sub-question, falsifiability
analysis, and M2.3 refinement clause. See `methodology/heuristics.md` for the
seven heuristics (H1–H7) that govern execution-cadence decisions under AEAL.

## Directory layout (M1.3 freeze inventory)

```
khinchin-k0-bounded/
├── README.md                    # this file
├── LICENSE                      # MIT (code)
├── LICENSE-DOCS                 # CC-BY 4.0 (documentation, data, figures)
├── .gitignore
├── .gitattributes               # (if added during M2+)
├── _M1.0_first_action_log.md    # AEAL audit trail of M1.0 first action
├── targets/                     # M1 process artefacts (frozen at gold/M1)
│   ├── triage.json              # 28-row M1.1 candidate problem triage
│   ├── triage_schema.json       # JSON Schema for triage rows
│   ├── triage_validator.py
│   ├── build_triage_m1_1.py
│   ├── _M1.1_triage_metadata.json
│   ├── _M1.1_construction_log.md
│   ├── survey_set.md
│   ├── literature_recheck_18_levy_constant.md
│   ├── overlap_audit_23_stanley_plane_partition.md
│   ├── overlap_audit_26_gauss_kuzmin.md
│   ├── overlap_audit_khinchin_signature_pslq_prior_work.md
│   ├── M1.2_scoring.json
│   ├── M1.2_shortlists.md
│   ├── build_m1_2_shortlists.py
│   └── selected.md              # the M1.2 target lock — IMMUTABLE post gold/M1
├── capability/                  # H7-mandated functional-verification records
│   ├── probe_results_20260515.md         # v1 (with §AMENDED block)
│   ├── probe_results_20260515_v2.md      # v2 (supersedes v1 on PARI/GP row)
│   ├── machinery_base_confirmed.md
│   ├── independent_second_library.gap.md # U-MISSION-H trigger (resolved by H1 install)
│   ├── pari_gp.available.md
│   ├── mpmath.available.md
│   ├── gmpy2.available.md
│   ├── numpy.available.md
│   ├── sympy.available.md
│   ├── lean_lake.available.md
│   └── mathlib4.available.md
├── methodology/
│   └── heuristics.md            # H1–H7, subordinated to Brief and AEAL
├── mutation_log/
│   ├── m1.0_to_m1.1_operator_amendments_20260515.md
│   ├── m1.1_to_m1.2_shortlist_construction_20260515.md
│   ├── m1.2_to_m1.3_brief_fidelity_correction.md
│   └── m1.3_pari_gp_install_20260515.md
├── seeds/                       # parked future-work candidates
│   ├── README.md
│   └── 26_gauss_kuzmin_reframings_future_work.md
├── env/
│   └── M1.lock                  # environment snapshot at gold/M1
├── claims/                      # (empty at M1.3; populates from M3.1 onward)
├── literature/                  # (empty at M1.3; populates at M2.1)
├── harness/                     # (empty at M1.3; populates at M3.1)
├── symbolic/                    # (empty at M1.3; populates at M4)
└── lean/                        # (empty at M1.3; populates at M5)
```

## Machinery base (H7-verified, 2026-05-15)

Confirmed AVAILABLE with functional verification:

| Capability | Version | Verification example |
|---|---|---|
| Python | 3.12.10 | — |
| mpmath | 1.3.0 | 500-dps $\pi$ first 80 digits match official |
| gmpy2 | 2.3.0 | $F_5 \bmod 641 = 0$ recovers Euler's factor |
| numpy | 2.4.4 | $\det\begin{pmatrix}1&2\\3&4\end{pmatrix} = -2$ |
| sympy | 1.14.0 | `factor(expand((x+1)**3)) == (x+1)**3` |
| **PARI/GP** | 2.18.1 (development snapshot, May 10 2026) | `lindep([1, √2, 3-2√2]) = [3,-2,-1]~` |
| Lean | 4.29.1 (commit f72c35b) | `lean --version` |
| Lake | 5.0.0-src+f72c35b | `lake --version` |
| Mathlib4 | cached locally at master + v4.14.0 | operator's existing projects' `.lake/packages/mathlib` |

Confirmed NOT AVAILABLE (hard filters): python-flint/arb, fpylll, cypari2,
SageMath, scipy, mpsolve.

See `capability/probe_results_20260515_v2.md` and individual
`capability/<technique>.available.md` files for full functional-verification
details.

## Reproducibility

The full environment snapshot at G1 is at `env/M1.lock`. Each
`capability/<technique>.available.md` file includes a `## Reproduce command`
section.

## Citation

Cite the Zenodo deposit minted at M6 (DOI added to this section at the M6 Gold
Freeze).

## License

- **Code** (`*.py`, `*.lean`, build/config files): MIT — see `LICENSE`.
- **Documentation and data** (markdown, JSON outputs, figures, prose):
  CC-BY 4.0 — see `LICENSE-DOCS`.
