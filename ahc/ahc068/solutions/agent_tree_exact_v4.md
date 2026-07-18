# Tree exact V4: strip routing and commuting-swap fusion

## Goal and departure from V3

V3 reached an average of about 4,967 operations, but its macro phase considered
only rectangles up to 4x4. Its exact phase still charged one output line for
every tree edge traversed by every card. V4 attacks both restrictions:

1. long wall-free strips route blocks of cards in one operation; and
2. independent adjacent swaps from exact completion are fused into a single
   rectangular operation whenever this is algebraically and geometrically
   valid.

For a completely wall-free board, V4 additionally uses constructive mesh
permutation routing rather than tree fixing.

The tree solver remains as a correctness certificate, not as the only source
of output operations.

## Macro routing family

V4 enumerates two complementary deterministic families:

- every wall-free rectangle with thickness at most four in the unsplit
  direction, allowing length up to `N`; and
- every wall-free local rectangle up to 8x8.

For example, `H r c 3 20` exchanges two 3x10 blocks in one line, while a tree
implementation would need many individual card moves to achieve the same
permutation. These long strips act as coarse row/column partition and routing
operations. Local rectangles repair smaller-scale disorder.

The objective is total wall-graph distance from cards to targets. At each step
the legal macro with the largest strict decrease is applied. As in V3, an empty
prefix and up to four additional low-cost checkpoints are retained using exact
center-tree completion as the estimate. Search is capped at 1.02 seconds.

## Exact completion and fusion

Every retained state is completed with 72 distance-prioritized leaf-fixing
plans: nine roots times eight neighbor orders. This guarantees a completely
sorted board.

Before comparing candidates, V4 partitions each adjacent-swap completion into
maximal consecutive batches of pairwise-disjoint swaps. Operations within such
a batch commute. Within a batch:

- horizontal swaps on the same column boundary and consecutive rows become
  one `H r c h 2`; and
- vertical swaps on the same row boundary and consecutive columns become one
  `V r c 2 w`.

Fusion occurs only if the entire combined rectangle is wall-free. Thus a group
of `h` or `w` output lines is replaced by one operation with exactly the same
permutation. Candidate selection uses the compressed count.

## Fully open mesh routing

On a wall-free board, form an `N`-regular bipartite multigraph whose left and
right vertices are source and target rows; every card is an edge. Repeated
bipartite matching decomposes the edges into `N` perfect matchings. A matching
number is used as that card's intermediate column.

The permutation is then routed in three stages:

1. permute every source row by assigned intermediate column;
2. permute every column by target row; and
3. permute every target row by target column.

Each one-dimensional permutation greedily applies distance-decreasing
`1 x 2k` or `2k x 1` equal-block swaps, then uses adjacent insertion swaps for
exact completion. This constructive row-column-row route sorts 400 cards with
only `3N` one-dimensional sorts. V4 constructs both the mesh result and the
general strip/tree result and emits the shorter one.

## Correctness

Macro candidates are emitted only after checking every internal boundary of
their rectangle and checking that the split dimension is even. Hence all macro
prefix operations are legal.

For tree completion, removed leaves are final, and active vertices induce a
connected tree. The desired card for an active leaf remains in that active
tree. Moving it along the unique active path fixes the leaf without touching
an earlier fixed leaf. Repeating leaves only one card, which must also be
correct because the cards form a permutation.

Compression preserves the exact completion permutation. A batch contains only
pairwise-disjoint swaps, so they commute. A fused `H h 2` or `V 2 w` operation
performs precisely the same disjoint cell pairs as its group. The explicit
wall-free rectangle check proves the fused operation legal. Therefore the
prefix followed by compressed completion still ends completely sorted.

For mesh routing, each perfect matching gives every source and target row
exactly one card in each intermediate column. After the first stage, every
column contains one card for every target row, so the second stage puts all
cards into their target rows. Each row then contains one card for every target
column, and the third stage finishes it. Adjacent insertion guarantees each
1D permutation finishes even when no improving block move remains.

## Output bound

Raw leaf fixing needs at most `400*399/2 = 79,800` operations. The empty prefix
is initially checkpointed; it can leave the five-state shortlist only after
states with strictly smaller `prefix + quick completion` replace it. The quick
plan is among the final 72 plans, and compression never increases its length.
Thus at least one final candidate has at most 79,800 lines. Candidates above
100,000 are ignored, so a legal candidate always remains.

## Complexity and two-second budget

For `M=400`, all-pairs graph/tree distances use `O(M^2)` memory. Macro
evaluation is time-capped at 1.02 seconds; strip thickness and local size are
bounded to avoid enumerating every arbitrary large-area rectangle. Exact
evaluation performs at most `5*72=360` completions, each `O(M^2)`, followed by
linear-time batching and fusion. One tree distance table is live at a time.

The fully open branch performs `N` augmenting-path matchings and `3N` small 1D
sorts, negligible at `N=20`.

This fixed postprocessing budget leaves room after the macro phase within the
two-second limit.

## V4 assumptions

- Card labels are `0..N^2-1` and targets are row-major.
- Wall character `0` is passable; `1` is blocked.
- The wall-free cell graph is connected.
- Output is zero-based and has no operation-count header.
