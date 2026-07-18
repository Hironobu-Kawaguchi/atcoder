# Line routing V5: column-row-column matching route

## Route construction

This candidate implements the requested column-row-column permutation route.
Treat every card as an edge between its current source column and its target
column.  This is a 20-regular bipartite multigraph.  Twenty augmenting-path
perfect matchings edge-color it; matching number `k` assigns intermediate row
`k` to every selected card.  Consequently, on a wall-free mesh:

1. sorting each source column by assigned intermediate row gives every row one
   card for every target column;
2. sorting each row by target column places cards in their target columns;
3. sorting each column by target row finishes the permutation.

The matching construction is exact and deterministic.

## Equal-block line beam

Every line sort is performed with legal equal-block swaps.  A state contains
the current line permutation and its block-swap history.  All operations
`[start, start+k) <-> [start+k, start+2k)` are expanded.  The best 200 unique
states survive each depth, up to depth 64.

The score is

`100 * breakpoints + sum(position displacement)`.

Breakpoints dominate displacement, encouraging long correctly ordered runs
that later block swaps can move together.  State identity is a deterministic
128-bit hash of the line permutation.  The route phase has a conservative
0.48-second cutoff because local development hardware is substantially faster
than the judge.

## Walls and wildcards

Each row or column is split into maximal passable segments.  A block operation
never crosses a wall.  If a card's requested position for the current routing
stage lies outside its present segment, that card is a wildcard: it contributes
neither breakpoints nor displacement and is deferred to exact completion.

Thus walls may make the three routing stages incomplete, but can never make an
emitted line operation illegal.  The stages remain column, row, column even on
partially blocked boards.

## Safe completion

The routed board and the original board are both completed under 40 exact tree
plans: five roots, eight neighbor orders, and alternating leaf tie orders.  Raw
adjacent swaps are compressed by fusing commuting swaps across the same wall-
free strip.  The shorter routed or initial completion is retained.  A fully
open board additionally competes with the existing exact matching-based mesh
route.

Tree leaf fixing is a correctness certificate.  Removing a leaf leaves the
active tree connected, and moving its desired card along the unique active path
does not touch earlier fixed leaves.  Induction sorts every card.

## Replay verification

Before output, the chosen operation list is replayed from the original board.
For every operation the verifier checks:

- bounds;
- the required even split dimension;
- every internal wall of the rectangle;
- and, after replay, complete row-major sorting.

If any routed candidate check fails, the solver falls back to the independently
constructed initial-board safe completion and verifies that result again.
Output is also required to remain below 100,000 operations.

No official or generated contest case was executed while creating this file.
Verification is limited to `rustfmt`, standalone `rustc -O`, and textual diff
checks.
