# V5: bipartite global routing with breakpoint-beam strip sorting

## Global column-row-column plan

Cards define a 20-regular bipartite multigraph between their current column and
target column. V5 repeatedly finds a perfect matching and thereby edge-colors this
graph with 20 colors. A card's color is its intermediate row. On an open
mesh this gives the classical exact routing:

1. permute every column so each card reaches its intermediate row;
2. permute every row by target column;
3. permute every column by target row.

Each intermediate row contains exactly one card for every target column, so the
row stage is feasible; after it, every column has the correct cards and the final
column stage completes sorting.

With walls, V5 applies the same global assignment independently inside every
maximal passable horizontal or vertical segment. The stages are
`V(mid-row), H(target-column), V(target-row)`. Long
segments are processed first and every stage endpoint is retained for exact
comparison, so partial routing can never make the final answer worse.

## 1D equal-block permutation solver

For a segment of length at most 20, every adjacent equal-block exchange
`[A][B] -> [B][A]`, `|A|=|B|`, is a search edge. A width-200, depth-14 beam searches
sequences rather than accepting the best immediate swap. Its cost is:

- `100 * breakpoint count`;
- plus total displacement from assigned coordinates.

Consequently a long block swap that removes several breakpoints is preferred to
the adjacent-insertion tail that dominated earlier versions. A line permutation
uses an exact 100-bit `u128` key, avoiding hash collisions. At a wall boundary,
unique reachable targets are retained and unavailable or duplicate targets are
filled with stable wildcard cards, producing a complete local permutation.

## Safe completion and compression

Five BFS trees use corner and center roots.  Exact leaf elimination always sorts
the remaining permutation.  Its adjacent swaps are partitioned into maximal
batches of disjoint operations; aligned swaps whose complete 2-by-k or k-by-2
rectangle is wall-free are fused into one rectangle operation.  Every routing
checkpoint is completed by every tree and the exact shortest
`prefix + compressed fallback` is emitted.

The empty checkpoint is always present.  Thus output is no longer than the safe
initial compressed tree completion, is fully sorted, and is below 100,000 lines.
Before serialization, V5 replays the selected answer from the original board,
checking bounds, even dimensions, every internal wall, and final sortedness.  A
failed check replaces the answer with the empty-prefix safe tree completion,
which is replayed and asserted again.

## Complexity and time

Perfect-matching decomposition is `O(N^4)`.  For segment length `L`, the 1D beam
costs `O(depth * beam * L^3)` with `L<=20`.  Routing has a 1.08-second cutoff.
Exact fallback and compression use polynomial `O((N^2)^2)` work; five trees and
at most four checkpoints leave margin inside the two-second limit.  The method is
deterministic and uses no empirical feedback from V5 runs.
