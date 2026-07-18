# V12 Endgame Beam

## Intent

This is a conservative, fixed-work tail optimizer layered on V11 ThickSafe.
The V11 portfolio still evaluates every root/order/checkpoint/completion-mode
candidate and selects its exact best result first.  Only that selected
provenance is replayed for a second candidate.

## Search boundary

- Reproduce the selected completion mode greedily until 24 active tree cells
  remain.
- Search only the final 23 leaf placements.
- Beam width: 8.
- Branches per state: 3 (the original greedy leaf plus two cheap alternatives).
- Hard transition limit: 552.  With one initial state, the implemented maximum
  is `3 + 22 * 8 * 3 = 531` transitions.
- Work is deterministic and never depends on elapsed time.

The rank combines operations already emitted with a small tree-distance tail
estimate.  It is only a beam-ordering heuristic; final selection uses exact
compressed operation count and full replay.

## Safety

The original V11 result is retained unchanged.  The beam candidate replaces it
only when it is strictly shorter and a full replay from the original board
proves every operation legal and the final board sorted.  Failure, exhaustion,
or a non-improvement returns the baseline.

Deduplication uses a 128-bit fingerprint only as a lookup hint, followed by
exact comparison of board, active mask, degrees, and remaining count.  Hash
collisions therefore cannot merge distinct states.

## Integration note

The source includes `agent_jump_tree_v11_thick_safe.rs` as a module so the V12
delta stays reviewable and no existing file is modified.  It compiles directly
from this directory.  Before AtCoder submission, flatten the include into one
self-contained source file.  No input case or solver evaluation was run while
creating this candidate; only a compile check is permitted at this stage.
