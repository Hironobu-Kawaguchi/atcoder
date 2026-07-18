# Tree leaf-fixing exact solver V2

## Motivation

The original exact solver used one center-rooted BFS tree and fixed leaves in
FIFO order. It completed all 100 official cases, but the fixed tree and leaf
order can force a desired card to travel farther than necessary. V2 retains
the same exact, adjacent-swap-only foundation while selecting both the tree and
the leaf order from the actual input.

## Candidate generation

V2 uses the Cartesian product of:

- 25 deterministic roots at rows and columns
  `{0, N/4, N/2, 3N/4, N-1}`; and
- 8 clockwise/counterclockwise rotations of the four-neighbor priority.

This produces 200 deterministic BFS spanning-tree candidates for `N=20`.
Alternating candidates prefer the smaller or larger cell index when leaf
distances tie, adding limited ordering diversity without doubling the search.

## Candidate simulation

For each tree:

1. Precompute all-pairs tree distances.
2. Keep the active connected subtree and its current leaves.
3. For every active leaf `v`, look up the distance from the current position of
   card `v` to `v`.
4. Fix the minimum-distance leaf by moving its card along the unique tree path
   with legal two-cell swaps.
5. Remove the fixed leaf and continue until one vertex remains.

Each candidate is simulated independently from the original permutation. V2
retains the complete operation list of the candidate with the fewest swaps and
prints only that list. Candidate evaluation does not rely on randomness,
wall-clock timing, or external tuning.

Larger rectangle operations are deliberately not introduced: adjacent swaps
preserve the simple exactness proof, and every candidate remains below the
output limit regardless of which one wins.

## Correctness

For any candidate, the BFS tree uses only wall-free grid edges. A vertical tree
edge is emitted as a `V r c 2 1` operation and a horizontal edge as
`H r c 1 2`, so every operation is a legal rectangle exchange.

Inductively, all removed leaves contain their final cards, and the active
vertices induce a connected tree. The desired card of an active leaf cannot be
in a removed vertex because every removed vertex already contains its own
distinct card. Therefore the desired card lies in the active tree. Its unique
tree path to the leaf also lies entirely in that active connected subtree.
Swapping along the path fixes the leaf without touching any previously fixed
vertex. Removing a leaf preserves connectivity and the invariant.

When one vertex remains, all other distinct cards are fixed, so the final card
must also be correct. Thus every simulated candidate completely sorts the
board. Selecting one of these complete candidates by operation count preserves
that guarantee.

## Operation bound

With `k` active vertices, a tree path has at most `k-1` edges. For
`M=N^2=400`, every candidate therefore emits at most

`(M-1)+(M-2)+...+1 = M(M-1)/2 = 79,800`

operations, safely below the 100,000-line limit.

## Complexity and candidate budget

Let `M=N^2` and `C=200`.

- Building a BFS tree: `O(M)` per candidate.
- All-pairs tree distances: `O(M^2)` per candidate.
- Scanning active leaves over all fixing steps: `O(M^2)` per candidate.
- Path simulation: at most `O(M^2)` per candidate.
- Total: `O(C*M^2)` time and `O(M^2)` working memory, plus the winning
  operation list.

At `M=400`, the fixed 200-candidate budget is intentionally modest for the
two-second contest limit. Only one candidate's data is live at a time.

## Assumptions

- Card labels are `0..N^2-1`, with target `r*N+c` at `(r,c)`.
- Wall character `0` means passable and `1` means blocked.
- The wall-free graph is connected.
- Output coordinates are zero-based and no operation-count header is printed.
