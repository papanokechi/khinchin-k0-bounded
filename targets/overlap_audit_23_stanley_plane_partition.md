# Overlap audit — Survey entry #23 (Stanley plane-partition asymptotic constants)

**Trigger:** Operator request 2026-05-15 ~17:38 JST per U-MISSION-A: *"Hold #23, #26 pending one-paragraph `overlap_audit.md` each. The risk isn't that they overlap with paper14 / Finite-Depth Rigidity; it's that they overlap *enough that a positive result would muddy attribution* between the two tracks."*

**Survey-set entry:**
> 23. **Stanley's plane-partition asymptotic constants**. Bounded entry point: PSLQ-identify the asymptotic constant in a fixed plane-partition family against known special-value bases (Glaisher–Kinkelin, Catalan, ζ-values).

## Active SIARC tracks to audit against

1. **paper14** — coauthorship-probe paper (current understanding: Mazzocco-track polynomial CF + Lean preprint companion). Content axis: polynomial continued fractions + hypergeometric spectral classes.
2. **Finite-Depth Transient Rigidity** — small-value continued fraction dynamics rigidity (Item 26 JSC active, Item 30 ETDS rejected). Content axis: CF dynamics at small partial-quotient bound, transient → asymptotic rigidity.
3. **R1 chart-map closure / Painlevé III** — active queue item per operator's existing roadmap. Content axis: monodromy / chart maps for Painlevé III tau-functions.
4. **PCF spectral fingerprint framework** — operator's working machinery for polynomial CF density / spectral identification.

## Content-axis analysis for #23

Stanley plane-partition constants arise from the **MacMahon-style box-counting generating function** for boxed plane partitions and its asymptotic behavior. The canonical example is the constant `A` in
```
M(q) = ∏_{n≥1} 1/(1-q^n)^n   (MacMahon generating function)
```
whose asymptotic behavior involves the **Glaisher–Kinkelin constant** A_GK = 1.2824271... and ζ'(-1), in conjunction with `ζ(3)`. Stanley's higher-rank analogues introduce additional constants whose closed-form identification is open.

**Machinery overlap:**
- PSLQ at 500 dps — same machinery as paper14's spectral fingerprint identification ✅ (overlap)
- Glaisher–Kinkelin / Catalan / ζ-value bases — these are standard PSLQ bases, used widely
- mpmath at high precision — same machinery as Finite-Depth Rigidity ✅ (overlap)

**Content overlap:**
- Plane partitions are NOT continued fractions. The MacMahon generating function lives in a different combinatorial domain.
- The asymptotic constants are NOT continued-fraction-derived. They come from saddle-point analysis of `M(q)` near q → 1.
- Painlevé III / monodromy / chart-map structure does NOT appear in MacMahon's analysis.
- The PCF spectral fingerprint framework — to the extent it can identify any high-precision constant against a standard special-value basis — could in principle be POINTED at a plane-partition constant, but doing so does not invoke any of the PCF *content* (no polynomial CF, no hypergeometric monodromy, no Mazzocco-track machinery).

## Attribution-muddiness assessment

**A positive result on #23 would look like:** "Using PSLQ at 500 dps against a basis containing {A_GK, Catalan G, ζ(3), ζ(5), log 2, ...} we identify the Stanley higher-rank plane-partition asymptotic constant as (some closed-form expression)."

**Does this muddy attribution with active SIARC tracks?**
- vs paper14: NO. paper14's content is polynomial CF + hypergeometric spectral classes. A plane-partition constant identification is in a different combinatorial domain with no shared theorems or constants. The shared *machinery* (PSLQ + high-precision arithmetic) is generic infrastructure, not paper14-specific.
- vs Finite-Depth Rigidity: NO. Finite-Depth Rigidity is about CF dynamics + transfer operator behavior; plane partitions are not in that domain.
- vs R1 / Painlevé III: NO. R1 is about monodromy / chart maps; plane partitions are not.
- vs PCF spectral fingerprint framework: NO. The framework would be USED here (as a constant-identifier), but its content (polynomial CF densities) is not the subject of the inquiry. This is analogous to using `mpmath` — a tool, not a co-attribution risk.

**Verdict:** the overlap is at the MACHINERY level (PSLQ + special-value bases) but NOT at the CONTENT level. A positive result on #23 would cite Stanley's combinatorial framework + the closed-form basis, not paper14 or Finite-Depth Rigidity. Attribution would be CLEAN.

## Disposition

**#23 PASSES the overlap audit. SURVIVES to M1.1 triage-row construction.**

**Caveat for M1.1 row:** the `falsifiable_sub_question` should specify the Stanley plane-partition family explicitly (NOT just "plane partitions") to keep the bounded scope precise. Suggested form: *"PSLQ-identify the leading asymptotic constant of MacMahon-style box-counted plane partitions of fixed shape σ as N → ∞, scanned at 500 dps against the basis {A_GK, Catalan G, ζ(3), ζ(5), log 2, log 3, π², π³, 1} for shapes σ in a small enumerated set; either (a) a relation candidate that survives gp lindep certification at 1.5× precision, OR (b) documented absence of relation."*

**AEAL compliance:** MEDIUM. Risk that the "small enumerated set" of shapes expands under Searcher's Fatigue; M1.1 row will fix the set explicitly (≤ 5 shapes) to bound the sweep.

## Operator action

Entry #23 advances to M1.1 triage-row construction. Audit conclusion: KEEP.
