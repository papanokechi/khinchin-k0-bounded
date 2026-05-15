# seeds/

Purpose: parking area for future-work candidates that were considered, audited, and
deferred *during* the current mission cycle but which carry enough structural
interest to revisit in a later cycle.

## What lives here

- Reframings of dropped problems that operator explicitly instructed to park (e.g.,
  alternative CF maps for the Gauss–Kuzmin entry whose direct version was dropped
  for content overlap with `Finite-Depth Transient Rigidity`).
- Promising directions that surfaced during literature audits but did not meet
  the M1.1 hard-filter criteria.

## What does NOT live here

- M1.2 candidates (those are in `targets/triage.json`).
- Capability gaps (those are in `capability/*.gap.md`).
- Active claims (those are in `claims/`).

## Binding rule

Entries in `seeds/` are **NOT to be re-entered into the current mission cycle.**
They are recorded for a *future* relay or a *separate* mission only. Re-entering
a parked entry within the same cycle requires:

1. An explicit operator mutation_log directive lifting the park.
2. A re-audit (overlap, literature, machinery) demonstrating the original
   park-condition no longer holds.
3. Treatment as a fresh M1.1 candidate, not as a revival.

This rule exists to prevent the parking area from being used as a back-door
hypothesis-mutation slot — the AEAL anti-thrashing discipline (Brief §7) covers
within-cycle thrashing; this README covers across-park-boundary thrashing.

## Current contents

- `26_gauss_kuzmin_reframings_future_work.md` — two reframings (R-1: non-Gauss
  CF map; R-2: large-deviation partial-quotient sums) parked per operator
  directive 2026-05-15 ~18:00 JST. DO NOT re-enter this cycle.
