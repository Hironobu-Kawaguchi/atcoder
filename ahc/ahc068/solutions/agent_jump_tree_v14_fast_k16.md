# jump_tree_v14 fast K16

This is a timeout-repair candidate based on V12 beam-delta K16. Existing
solver files are not modified.

## Changes

- The macro-prefix wall-clock budget is reduced from 1.02 seconds to 0.80
  seconds.
- The mandatory first stage still evaluates the same 9 roots, 8 orders, up to
  5 checkpoints, and the same V10 completion portfolio.
- All four V10 completion vectors are built in the original priority order.
  A stable length sort then replays only the shortest candidate, falling
  through to the next candidate only if validation fails. For valid candidates
  this preserves V12's strict-`<` tie behavior exactly.
- ThickDelta caches the distance delta of the at most seven perpendicular
  lines touched by a thickness-at-most-four rectangle. Rectangle delta is the
  exact sum of those independent line deltas, so candidate keys and normal
  outputs are unchanged.
- K is fixed at 16.
- ThickDelta is optional: no candidate starts at or after 1.60 seconds, and an
  in-progress completion aborts at 1.69 seconds. The completed V10 baseline is
  retained on every abort.
- The selected output receives a final full replay before rendering.

## Time caveat

The 1.60/1.69-second checks are solve-wide wall-clock safety fuses. Therefore
the number of optional ThickDelta candidates completed on unusually slow
machines may differ. The mandatory baseline remains deterministic for a given
0.80-second macro-prefix result, but that macro prefix itself remains
wall-clock-budgeted as in earlier versions.

## Validation status

- Static formatting and compilation checks are permitted.
- Per the AHC generative-AI rule, no solver/input execution is performed in
  this implementation turn.
