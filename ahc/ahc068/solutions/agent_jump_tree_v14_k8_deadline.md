# Jump Tree V14 K8 Deadline

This candidate is the time-defensive retry of V12 Beam Delta K8.

## Mandatory baseline

- Wall-bearing inputs use the V10 candidate portfolio: old adjacent-tree,
  V8Edge, Distance, and line-only Clearance completions for all retained
  checkpoint/root/order states.
- The shortest complete candidate is retained and replayed before optional work.
- Macro-prefix search is shortened from 1.02 seconds to 0.80 seconds. This
  intentionally trades some prefix quality for postprocessing and hidden-case
  runtime margin.
- Zero-wall inputs retain the deterministic C-R-C line-beam route and its exact
  replay guard.

## Optional ThickDelta

- States are ranked exactly as in V12 by their V10 total operation count.
- Only the best eight states may receive ThickDelta.
- Time is measured from entry to the solver, including parsing and all setup.
- ThickDelta is not started when mandatory work finishes at or after 1.56 s.
- Its completion checks an absolute 1.69 s soft deadline at leaf, path, and
  offset boundaries. A timeout returns `None`; its partial local board and
  operations are discarded.
- A raw completion finishing after 1.69 s is also discarded before compression.

The 310 ms interval from the optional deadline to the contest's 2 s limit is
reserved for compression already in progress, replay, rendering, scheduler
noise, and hidden-case variation. This is a soft wall-clock defense, not a
formal operating-system runtime guarantee.

## Correctness guards

- The V10 baseline is complete before any optional search.
- Every completed fallback is replayed from its checkpoint.
- An improving ThickDelta candidate is replayed from the original input.
- The final selected operation list is replayed again. Failure restores the
  independently replayed V10 baseline.

## Verification scope

The implementation turn performs formatting and optimized standalone
compilation only. No official or generated solver input is executed.

The `.rs` wrapper uses local `include!` files so the experiment remains easy
to review. It must be flattened into one standalone source before submission
to AtCoder.
