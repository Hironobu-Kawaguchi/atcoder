# Distance hybrid V3: multi-tree exact rollout

## Difference from V2

V2 used one fixed spanning-tree completion and chose rectangle moves mainly by
shortest-path energy.  V3 uses energy only as a fast proposal mechanism.  Its
decisive second phase evaluates candidate moves by the actual quantity to
minimize: one emitted rectangle operation plus an exact residual completion.

The residual completion is also stronger.  Three BFS spanning trees are built
from different roots and neighbor orders.  Within each tree, every elimination
step chooses, among all active leaves, the leaf whose desired card has the
shortest current tree path.  Exact simulation selects the cheapest of the three
trees for each evaluated state.

## Algorithm

1. Build the wall graph and all-pairs wall-graph distances.
2. Enumerate every legal wall-free V/H rectangle with both sides at most 6.
3. During a 0.62-second fast phase, repeatedly take the strict best distance
   energy move.  At regular/strong checkpoints, exactly simulate all three
   fallback plans and retain the smallest `prefix + fallback` state.
4. Roll back to that state.  Rank all rectangles by energy and retain the best
   ten proposals.  For each proposal, apply it on a copy and exactly simulate
   all fallback plans.  Accept the proposal with the smallest exact total only
   if it improves the current best total.  Repeat until no proposal improves or
   1.52 seconds has elapsed.
5. Run the cheapest fallback plan from the final state and emit its operations.

The 1.52-second search cutoff leaves approximately 0.48 seconds of the stated
2-second limit for the final completion and output formatting.

## Correctness

Every proposed rectangle is checked to contain no internal wall and has an even
height for V or even width for H, so each prefix operation is legal.

For a fallback tree, deleting a leaf preserves connectivity of all remaining
vertices.  The card targeted at that leaf is still active and the unique active
tree path to the leaf consists entirely of legal wall edges.  Adjacent swaps
along the path fix the leaf permanently.  Induction fixes all but the last
vertex of each component; the final vertex is correct because cards form a
permutation.  Choosing a different active leaf or a different spanning tree
does not change this argument.

The empty prefix is evaluated first.  Later states are accepted only when their
exact `prefix + fallback` count is smaller.  Therefore rollback and rollout can
never produce more operations than the initial safe fallback.  Its worst-case
bound is `400*399/2 = 79,800`, below 100,000.

## Complexity

Let `S=N^2`, `E` be the wall-graph edge count, and `C=O(S)` the number of
constant-size (at most 6x6) candidates.  Wall distances cost `O(S(S+E))` time
and `O(S^2)` memory.  Candidate ranking costs `O(C log C)` per rollout step.
One fallback simulation costs `O(S(S+E))` with the simple path recovery and
`O(S)` mutable workspace; three simulations are used per exact evaluation.
All search is additionally bounded by the 1.52-second wall-clock cutoff.

No contest input was used to run V3.  Only `rustfmt` and standalone compilation
are performed before handoff.
