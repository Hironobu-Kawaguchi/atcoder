# Distance hybrid V4: global macro beam and routing alignment

## Why this is not another local-rectangle extension

V3 was very reliable, but its rectangles had side length at most six and it
followed one prefix until exact one-step rollout.  V4 removes the size bound and
searches several incompatible prefixes simultaneously.  In particular, every
wall-free 1-D block swap in every passable row/column segment is examined at
each beam expansion.  These are precisely the primitives needed by
row/column/row permutation routing on open regions.  Two-dimensional wall-free
rectangles of every size up to 20x20 are also available through deterministic
and random sampling.

## Macro evaluation

For an operation, V4 computes three static gains:

- decrease in total wall-graph distance to target cells;
- increase in cards exactly at their targets;
- increase in cards whose row or column already agrees with their target.

The third term is a routing-specific intermediate objective: a horizontal
block swap can arrange target columns without disturbing row membership, while
a vertical block swap does the symmetric job for target rows.  It gives long
segment swaps useful guidance even when they do not immediately create exact
matches.

All legal wall-free rectangles are enumerated once.  Every proposal call scans
all 1-D row/column operations, plus 1,400 changing deterministic/random samples
of 2-D macros.

## Multi-prefix beam

The first phase maintains eight complete `(board, positions, prefix)` states.
Each state contributes its best three macros.  Successors are deduplicated and
selected under three objectives with different exact-match weights, preserving
distance-oriented, alignment-oriented, and placement-oriented trajectories.

Every fourth depth, each surviving state is connected to a safe completion and
measured by its real `prefix length + exact fallback count`.  The best measured
state is retained independently of the beam.  Beam search stops at 1.18 seconds.

The second phase starts from the best checkpoint.  It evaluates 18 shortlisted
macros by actually applying each one and simulating the residual fallback.  A
move is accepted only if it strictly reduces total emitted operations.  Search
ends at 1.72 seconds, reserving time under the two-second limit for completion
and serialization.

## Safe completion

Five BFS spanning trees use different roots and neighbor orders.  For each
tree, leaf fixing always chooses the active leaf whose desired card is closest
in tree distance.  Exact simulation selects the cheapest tree.

Deleting an active tree leaf leaves the remaining tree connected.  The desired
card can therefore be moved along the unique active path using legal adjacent
rectangle swaps, after which that leaf is never touched again.  Induction fixes
the whole component.  The feasibility condition places every card in the same
wall component as its target.

The empty prefix is measured before search and later checkpoints are retained
only when their exact total is smaller.  Consequently the result is never
longer than the initial leaf-fixing completion, whose worst-case bound is
`400*399/2 = 79,800 < 100,000` operations.

## Complexity

With `S=N^2`, all-pairs wall distances and each exact fallback are
`O(S(S+E))`; distance storage is `O(S^2)`.  There are `O(N^6)` rectangle
descriptions in the loose enumeration bound, but for fixed `N=20` at most all
grid subrectangles are considered and legality is checked only once.  Beam
proposal work is bounded by its fixed widths, samples, and the 1.18-second
cutoff.  Exact rollout is bounded by the 1.72-second cutoff.

V4 was not executed on official or generated contest input.  Only formatting
and standalone optimized compilation are used for verification.
