# Distance hybrid V5: structured segment routing

## Motivation

V4's unrestricted rectangle beam was both slower and worse than V3.  V5 drops
global rectangle search completely.  It constructs its prefix from long
one-dimensional equal-block swaps inside maximal wall-free row and column
segments, then uses the proven compressed tree completion from `tree_exact_v4`.

This targets the observed bottleneck directly: most previous output lines were
adjacent swaps, while a single `H 1 2k` or `V 2k 1` operation can perform `k`
pair swaps and route a whole block across a segment.

## Structured routing phase

For every maximal passable row segment, enumerate all adjacent equal-length
block pairs.  Choose the block swap that most decreases the sum of absolute
current-column to target-column errors of its cards.  Ties prefer a larger net
increase in exactly placed cards and then a larger block.  Repeat to a local
optimum.  Column segments use the symmetric target-row objective.

Horizontal operations never change card rows, and vertical operations never
change card columns.  Therefore optimizing one coordinate leaves the other
coordinate error unchanged.  Alternating the dimensions also changes which
wall-delimited segments cards occupy, allowing later phases to make progress
that was impossible earlier.

V5 constructs both schedules:

- row, column, row, column, ...;
- column, row, column, row, ... .

Each runs for at most six rounds.  The board after each phase is an exact
completion checkpoint.  Only the six checkpoints with the best quick
`prefix + tree completion` estimates survive, including the empty prefix.

The structured potential is lexicographic:

1. total target-row plus target-column absolute error;
2. negative number of exactly placed cards.

Every accepted segment operation strictly improves this potential.  Hence the
phase cannot cycle.  A hard 16,000-prefix-operation bound is an additional
safety guard.

## Exact completion and operation fusion

Each retained checkpoint is completed under 72 BFS spanning-tree variants
(nine roots and eight neighbor orders).  Leaf fixing moves the desired card to
an active tree leaf, fixes that leaf, and removes it.  The raw adjacent-swap
stream is partitioned into commuting disjoint batches.  Consecutive horizontal
swaps across one column boundary are fused into `H r c h 2`; consecutive
vertical swaps across one row boundary are fused into `V r c 2 w`, but only
when the fused rectangle is wall-free.

For a completely wall-free board, V5 also retains the exact constructive
row-column-row mesh route: bipartite edge coloring assigns intermediate
columns, followed by one-dimensional block sorting in all rows, columns, and
rows.  The shorter legal result is emitted.

## Correctness and limits

Every routing operation stays inside one maximal wall-free segment, has an even
split length, and is therefore legal.  Every fused completion operation is
checked against all internal walls and represents exactly the same set of
commuting swaps.

For tree completion, deleting a leaf preserves connectivity of the active
tree.  Its desired card can be moved along the unique active path without
touching fixed leaves.  Induction sorts the entire board.  The empty prefix is
always retained unless replaced by a strictly better quick completion, and
that quick tree is among final candidates.  Thus a result no longer than the
safe raw bound `400*399/2 = 79,800` always exists, below 100,000.

The segment construction is deterministic and bounded by `N=20`, six rounds,
and 16,000 moves.  Final evaluation uses only six checkpoints, keeping the
`6*72` completion budget close to the already safe tree solver and leaving
substantial margin under two seconds.  There is no unstructured rectangle beam
or wall-clock-fragile stochastic loop.

V5 was not run on any official or generated input.  Verification is limited to
formatting and standalone optimized compilation.
