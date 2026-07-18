# V4: stochastic macro-rectangle beam with exact portfolio completion

## Different principle

Earlier versions repeatedly optimized a small rectangle or a discontinuous
single-tree fallback count.  V4 instead treats the half-swap as a genuinely
parallel move.  Since a 1x2 swap and a 20x20 half-swap both cost one output line,
the macro score is the **total** progress of every moved card and is deliberately
not divided by area.

The energy is

```text
8 * sum(wall-graph distance from each card to its goal)
  + 3 * number of misplaced cards.
```

Thus a large rectangle which improves twenty cards receives roughly twenty
times the credit of a comparable adjacent swap.

## Segment routing, then macro beam

Before stochastic search, V4 performs a row -> column -> row sequence inspired
by permutation routing.  It extracts every legal 1x(2k) operation from open row
segments and every legal (2k)x1 operation from open column segments.  In each
pass it repeatedly applies the equal-block exchange with the greatest total
card-distance gain.  These exhaustive one-dimensional passes directly exploit
long passable segments (including completely open rows and columns), while
remaining valid on a board that is not globally wall-free.  Each pass endpoint
is an exact checkpoint, so an unhelpful routing pass is automatically discarded.

## Macro beam / tabu / temperature

Every legal wall-free rectangle, including dimensions up to 20x20, is generated
and shuffled deterministically.  A width-4 beam is run for at most 64 levels.
For each beam state, 3,072 consecutive shuffled candidates plus 1,536 random
probes are scored.  The best eight become children.  Immediate reversal is tabu.
A decreasing random temperature perturbs beam ranking, so a temporarily worse
child can survive when it offers a different large-rectangle sequence.  Board
hashes remove duplicate states.

Every eight macro levels, the two strongest beam states are measured using a
complete count-only fallback and retained among ten exact checkpoints.  After
the macro phase, the lowest-energy beam state is polished using all wall-free
rectangles up to 4x4 until the search deadline.  Exact checkpoints are added
every 32 polishing moves.  The empty prefix is always retained.

## Exact completion portfolio

Five BFS spanning forests use corner and center roots with two neighbor orders.
Their leaf elimination dynamically fixes the active leaf whose target card is
nearest in that tree.  At the end, every saved checkpoint is completed in
count-only mode by every forest.  V4 emits the exact minimum of

```text
prefix length + complete fallback length.
```

This separates exploratory macro moves from correctness: beam, tabu, temperature,
or the deadline can never prevent completion.

## Correctness and bounds

Generated rectangles are accepted only when all internal adjacencies are free
of walls and the swapped dimension is even, so every prefix operation is legal.
For fallback, fixing a leaf routes its target card through the active spanning
tree using legal adjacent swaps.  Removed leaves remain fixed; induction sorts
each component completely.

The empty checkpoint with the primary fallback is always a candidate.  A tree
component of size `s` needs at most `s(s-1)/2` swaps, hence at most 79,800 for
400 cells.  The selected total is no larger than this initial candidate and is
therefore below 100,000.

## Complexity and time control

With `K=400`, `R` legal rectangles, beam width `B=4`, sample `Q=4,608`, macro
depth `D=64`, and ten checkpoints:

- all-pairs distances and each tree distance table: `O(K(K+E))`;
- macro search: `O(D*B*Q*average moved cells)`;
- local polishing: full scans of the bounded 4x4 candidate set;
- one exact fallback: `O(K^2)` leaf scans and at most `O(K^2)` swaps;
- final portfolio: at most 50 exact fallback simulations.

Segment routing stops at 0.30 seconds, macro search at 0.82 seconds, and all
heuristic work at 1.18 seconds,
reserving the remainder of the two-second limit for the exact portfolio,
materialization, and output.  The RNG seed is fixed for reproducibility.
