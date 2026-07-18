# Distance-improvement + spanning-tree leaf fixing

## Strategy

The target cell of card `x` is cell `x` in row-major order.  First construct the
graph whose vertices are cells and whose edges are wall-free horizontal or
vertical adjacencies, then compute all-pairs shortest-path distances by BFS.

The first phase repeatedly chooses the best strict decrease of

`sum(cell p) distance(p, target(board[p]))`.

Its candidates are every legal adjacent swap and both half-swaps of every fully
open 2x2 rectangle.  Thus the search can exploit a small rectangle when moving
two pairs together is better than any individual adjacent swap.  It stops at a
local optimum, after 18,000 operations, or after 0.75 seconds.

The second phase is a deterministic safety fallback.  Build a spanning tree of
each connected component.  Repeatedly select a leaf of the remaining tree, find
the card whose target is that leaf, and move it along the unique active-tree
path using legal 1x2/2x1 swaps.  Remove the fixed leaf and continue.  The final
remaining vertex is then correct automatically.

## Correctness of the fallback

Assume the instance's solvability condition: every card and its target cell lie
in the same wall-graph component.

At each iteration, deleting a leaf leaves the remaining vertices of that tree
connected.  No previously fixed vertex is used again.  The desired card is in
the active tree, so its unique path to the chosen leaf consists only of active,
wall-free edges.  Swapping along that path places the desired card at the leaf;
deleting the leaf therefore preserves all fixed cards.  Induction fixes all but
one vertex in each component.  Since cards are a permutation and all other
vertices in that component are correct, its last vertex is also correct.

Every path step is emitted as `H r c 1 2` or `V r c 2 1`, hence is always a
legal rectangle operation.  The heuristic phase also uses only prevalidated
open rectangles and does not affect the fallback guarantee.

## Operation bound and complexity

For a component of size `k`, a leaf path has length at most `k-1`; summing while
the tree shrinks gives at most `k(k-1)/2` fallback operations.  With 400 cells,
the total is at most `400*399/2 = 79,800`.  Adding at most 18,000 heuristic
operations yields at most 97,800, below the 100,000 limit.

All-pairs BFS costs `O(N^2 (N^2 + E))` time and `O(N^4)` memory.  A heuristic
iteration scans `O(N^2)` constant-size candidates.  The fallback uses simple
BFS path recovery on the tree, for `O(N^6)` loose worst-case time over `N^2`
leaf removals and `O(N^4)` auxiliary memory; at fixed `N=20` this is small.

No solution execution or score-driven modification was performed; only a
standalone `rustc` compilation check is intended.
