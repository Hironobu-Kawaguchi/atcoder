# Rectangle-aware lookahead + exact fallback count (V2)

## Motivation

V1 accepted every rectangle that improved a Manhattan/misplacement energy.  A
locally attractive large swap can nevertheless make the fixed spanning-tree
completion longer.  V2 therefore optimizes the quantity that ultimately matters:
the number of output operations produced by its exact fallback.

## Search strategy

The wall-free adjacent-cell graph is built first.  BFS from every cell provides
wall-graph distances, which are more informative than Manhattan distance when
walls force detours.  Every valid wall-free rectangle of area at least four is a
candidate.

At each depth-1 search step:

1. Compute the inexpensive delta of
   `4 * sum(wall-graph distance) + misplaced-cell count` for all candidates.
2. Retain only the 12 candidates with the largest positive delta.
3. For each retained candidate, clone the current permutation, apply that one
   operation, and run the exact spanning-forest fallback in count-only mode.
4. Accept the candidate with the smallest fallback count only when
   `1 + new_fallback_count < current_fallback_count`.

Thus every accepted prefix operation strictly reduces the final total
`prefix length + exact fallback length`.  The current prefix is consequently
always the best prefix encountered; no speculative state needs to be retained.
The prefix is capped at 128 operations.  Search also stops at a soft 1.45-second
deadline, leaving margin under the two-second limit for fallback materialization
and output.  Once search stops for any reason, the exact fallback is always run.

## Exact fallback and correctness

For each wall-connected component, V2 builds a BFS tree.  Non-root vertices are
processed in decreasing depth.  When vertex `v` is processed, all descendants
are already fixed and removed, so `v` is a leaf of the active tree.  Its target
tile cannot be in a removed vertex, because removed vertices contain their own
final tiles.  The tile is routed along the unique active-tree path to `v` using
wall-free adjacent swaps (`H r c 1 2` or `V r c 2 1`) and `v` is then fixed.
Induction fixes every non-root vertex, after which each component root is also
correct.  This proves complete sorting for every component-feasible input.

The same deterministic routine is used both for count-only lookahead and final
output, so the evaluated count is exact rather than an estimate.  The fallback
alone needs at most `K(K-1)/2 = 79,800` operations for `K=400`.  Since every
accepted prefix strictly reduces `prefix + fallback`, V2 never outputs more
operations than its initial fallback and therefore remains below 100,000.

## Complexity

Let `K=N^2`, `R` be the number of rectangle candidates, `S=12` the shortlist
size, and `P<=128` the accepted prefix length.

- All-pairs wall distances: `O(K(K+E))`, with grid edges `E=O(K)`.
- Rectangle enumeration and all cheap delta scans: `O(P*N^6)` in a loose bound.
- One exact count-only fallback: `O(K^2)` swaps in the worst case.
- Exact shortlist evaluation: `O(P*S*K^2)` worst case, additionally bounded by
  the wall-clock deadline.
- Memory: `O(K^2 + R)` plus the output.

The algorithm is deterministic and uses no random seed.
