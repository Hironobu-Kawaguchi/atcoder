# Distance hybrid V2: exact best-prefix rollback

## Motivation

V1 always retained its complete distance-improving prefix.  On the first 100
official cases it sorted every case, but the cost of later prefix operations
often exceeded the number of fallback operations they removed.  V2 explicitly
optimizes the quantity that is emitted: `prefix length + exact fallback count`.

## Search and rollback

The energy remains the sum, over all cards, of wall-graph shortest distance to
the target cell.  Each iteration applies the legal rectangle operation with the
largest strict energy decrease.  Candidates now contain every wall-free
rectangle up to 4x4 for which the chosen V or H half-swap is defined.  Thus the
set includes adjacent swaps, 2x2 swaps, 1x4/4x1 moves, and 2x4/4x2 moves.

Before search, every 16 moves, after an especially strong move (energy delta at
most -8), and at search termination, V2 runs a count-only simulation of the
deterministic spanning-tree fallback.  It saves the board, card positions, and
prefix whenever

`prefix length + exact simulated fallback count`

strictly improves.  After search, all moves following the best checkpoint are
discarded.  The real fallback starts from that saved state.  Consequently a
long but counterproductive energy prefix cannot make the result worse than the
initial fallback.

Search is capped at 18,000 moves and 1.35 seconds, leaving time within the
2-second limit for final fallback construction and output serialization.

## Fallback correctness

For each wall-graph component, construct a spanning tree.  Repeatedly choose a
leaf of the active tree and move the card targeted at that leaf along the unique
active-tree path using legal adjacent 1x2 or 2x1 swaps.  Removing a leaf keeps
the remainder connected and no fixed leaf is touched again.  Inductively, every
removed leaf is correct; the last vertex is correct because cards are a
permutation.  The problem's feasibility condition ensures each desired card is
in the same component as its target.

The heuristic candidates are prevalidated to have no internal wall, so every
saved prefix is legal.  Rollback changes only which already-generated prefix is
emitted and therefore does not affect correctness.

## Bounds and complexity

For a component of size `k`, leaf fixing takes at most `k(k-1)/2` swaps.  The
initial fallback is therefore at most `400*399/2 = 79,800` operations.  Since
the empty prefix is the first saved candidate and V2 accepts only a smaller
exact total, final output is at most 79,800 operations (and hence below 100,000).

All-pairs BFS uses `O(S(S+E))` time and `O(S^2)` memory for `S=N^2`.  Each
heuristic iteration scans `O(S)` constant-area rectangles.  One exact fallback
simulation uses `O(S(S+E))` time with the current simple path searches and
`O(S)` temporary memory, in addition to the distance table.  Checkpoint spacing
and the wall-clock cap bound the total search work.

This V2 was not run with contest input.  Only formatting and standalone Rust
compilation checks are performed, as required by the AHC generative-AI rules.
