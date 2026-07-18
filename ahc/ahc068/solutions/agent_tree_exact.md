# Tree leaf-fixing exact solver

## Strategy

Treat every cell as a vertex and every wall-free adjacency as an edge. A
`2 x 1` `V` operation exchanges vertically adjacent cells, and a `1 x 2` `H`
operation exchanges horizontally adjacent cells. These two-cell rectangles
have exactly one internal boundary, so choosing only wall-free graph edges
makes every emitted operation legal.

1. Build the wall-free grid graph.
2. Build a BFS spanning tree rooted near the center.
3. Repeatedly choose a leaf of the remaining tree.
4. Find the current position of the card whose number equals that leaf's
   row-major cell index.
5. Move that card to the leaf along the unique active-tree path using adjacent
   swaps, then permanently remove the fixed leaf.
6. Continue until only the root remains.

The implementation maintains both `card_at[cell]` and `position[card]`, so the
source of the next desired card is available in constant time. Paths are found
by BFS in the current tree.

No larger rectangle exchanges are used. They can reduce the line count but
make it harder to preserve fixed cells and to prove exact completion. The
adjacent-only construction is already strictly below the output limit.

## Correctness

Assume the wall-free cell graph is connected, as required for an arbitrary
permutation to be sortable. Its spanning tree is therefore connected.

At the start of an iteration, all removed vertices hold their final cards and
the active vertices induce a connected tree. Consequently, the desired card
for an active leaf cannot be at a removed vertex: every removed vertex already
contains its own distinct desired card. Thus that card is somewhere in the
active tree.

The unique active-tree path from the card to the chosen leaf contains only
wall-free edges. Swapping consecutive vertices along this path moves the card
to the leaf, and every emitted two-cell rectangle is legal. Removing the leaf
does not disturb any earlier fixed vertex, and deleting a leaf preserves
connectivity of the remaining tree. These facts maintain the invariant.

After fixing all but one vertex, every other card is at its unique destination.
Since the cards form a permutation, the sole remaining card must also be the
correct one. Hence the final board is completely sorted in row-major order.

## Bounds

Let `M = N^2` (`M = 400`). When `k` vertices remain, a simple path contains at
most `k - 1` edges, so the total number of emitted operations is at most

`(M - 1) + (M - 2) + ... + 1 = M(M - 1)/2 = 79,800`.

This is below the `100,000` line limit for `N = 20`.

Building the graph and tree costs `O(M)`. Recomputing one active-tree path per
removed leaf costs `O(M^2)` time in total; board/position updates cost at most
`O(M^2)` as well. Memory usage is `O(M)`. With `M = 400`, these bounds are
small and deterministic.

## Assumptions

- Card labels are the permutation `0..N^2-1`, and the target at row `r`, column
  `c` is `r*N+c`.
- A wall character `0` denotes a wall-free boundary.
- The wall-free cell graph is connected.
- Coordinates in output operations are zero-based.

The program intentionally performs no stochastic search and requires no
runtime parameters or seed.
