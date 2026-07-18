# Rectangle-aware greedy + spanning-tree completion

## Strategy

The program first enumerates every wall-free rectangle.  A rectangle is a
candidate for `V` when its height is even and for `H` when its width is even.
Rectangles of area below four are omitted from this phase so that ordinary
adjacent swaps are left to the completion phase.

Candidates are visited once in decreasing area order.  For each candidate, the
program computes the exact change in

```text
E = 4 * sum(Manhattan distance from every tile to its goal)
    + number of misplaced tiles.
```

The operation is accepted only when it strictly decreases `E`.  Thus a single
large operation can move many tiles toward their goals, while an unproductive
rectangle is never used.  The phase is capped at 10,000 operations.

The greedy phase is not expected to finish every instance.  Once all candidates
have been considered (or the cap is reached), the program unconditionally
switches to an exact adjacent-swap fallback.

## Exact fallback and correctness

All cells and all wall-free adjacent pairs form a graph.  The implementation
builds a BFS spanning forest and processes the non-root vertices of every tree
in decreasing tree depth.

When processing a vertex `v`, all descendants of `v` have already been fixed and
removed, so `v` is a leaf of the active tree.  The tile whose goal is `v` is
located in the active tree: every previously removed cell contains its own final
tile, hence it cannot contain `v`'s tile.  Routing that tile along the unique
active-tree path to `v` uses only wall-free adjacent swaps.  Cell `v` is then
fixed and removed.  Induction shows that every removed cell remains correct.
After all non-root cells of a component are removed, the remaining tile must be
its root tile.  Consequently, the board is completely sorted.  This proof only
requires the necessary feasibility condition that every tile starts in the same
wall-connected component as its goal; it does not require the whole board graph
to be connected.

An adjacent horizontal edge is emitted as `H r c 1 2`, and an adjacent vertical
edge as `V r c 2 1`; both are valid special cases of the allowed rectangle
operation.  The proof assumes the wall graph is connected, as required for an
arbitrary permutation to be sortable.

The tree fallback uses at most
`1 + 2 + ... + (N^2 - 1) = N^2(N^2-1)/2` swaps.  For `N=20`, this is 79,800.
Together with the greedy cap, the output has at most 89,800 operations, safely
below the 100,000-line limit.

## Complexity

Let `K=N^2` and let `R` be the number of valid rectangle candidates.

- Candidate generation and wall checks: `O(N^6)` in the loose bound (small for
  `N=20`).
- Candidate sorting: `O(R log R)`.
- Greedy delta evaluation: `O(sum(area(candidate)))`, at most `O(N^6)`.
- Spanning-tree completion: at most `O(K^2)` swaps.  The straightforward BFS
  used to recover each active-tree path also costs `O(K^2)` total.
- Memory: `O(R + K)` excluding the output list.

The method is deterministic and has no tuning seed.
