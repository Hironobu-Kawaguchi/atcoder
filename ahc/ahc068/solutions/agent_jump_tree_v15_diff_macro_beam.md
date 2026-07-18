# V15 Differential Macro Beam (MVP)

This isolated candidate keeps `V14 Fast K16` as an unconditional baseline,
then spends only remaining time on a bounded tail-rerouting experiment.

- The first 24 operations of the V14 winner are retained.
- A fixed pool of 24 legal area-4..80 macro operations is selected at that
  boundary by exact graph-distance delta.
- Width 16, depth 6, and at most 1,536 transitions are explored.
- One mutable board is moved around the search tree using the fact that every
  operation is an involution. Children never clone a board or replay a full
  prefix.
- A 400x400 deterministic Zobrist table provides incremental deduplication.
- Only the best three leaves receive terminal exact completion, over at most
  six tree configurations.
- The stage starts only if V14 finishes before 1.60 s, stops expanding at
  1.68 s, stops starting completions at 1.72 s, and always min-guards against
  the fully materialized V14 result.
- The selected result receives a final full legality/sortedness replay.

This keeps only the first 24 operations of the V14 winner and reroutes most of
its remaining tail; it is not a small edit near the end of the operation list.
The public maximum observed V14 runtime was about 1.678 s, so slow judge cases
will often skip this optional stage at the 1.60 s start gate. That is intended:
the non-abortable terminal completion, replay, and rendering retain at least a
280 ms wall-clock reserve.

This is intentionally an MVP rather than the full segment-normal-form router.
Its pool is chosen once, its depth is short, and it does not model segment
breakpoints. The experiment tests whether differential macro branching has
measurable marginal value without reviving V12's per-child copying/TLE mode.

Per the contest AI rule, this file has only been formatted and compiled. It
has not been executed on an input; evaluation must wait for a later explicit
user instruction.
