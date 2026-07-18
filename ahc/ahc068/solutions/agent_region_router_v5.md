# Region router V5

## Aim

`tree_exact_v4` spends most of its output on adjacent swaps.  This candidate
adds a spatial hierarchy before exact completion:

1. tile the board with disjoint wall-free rectangular rooms;
2. route cards in bulk inside each room;
3. exchange batches across passable room boundaries (doorways);
4. run the general long-strip macro phase; and
5. finish with a replay-checked exact tree plan.

Every intermediate stage is only a candidate.  The empty prefix is retained,
so a weak room decomposition cannot make the selected answer worse than this
implementation's safe exact fallback.

## Room decomposition

All wall-free rectangles are enumerated and sorted by area.  A rectangle is
accepted when none of its cells has already been claimed.  Remaining cells
become singleton rooms.  Consequently rooms are pairwise disjoint and cover
the board, while the first rooms tend to be the large open areas observed in
the official instances.

The decomposition is geometric rather than a claim that walls define literal
closed chambers.  Cards may have targets in other rooms; those cards are
treated as wildcards during the local phase and are handled by doorway,
strip, and exact routing.

## In-room routing

Each nontrivial room receives column-row-column passes.  A line move exchanges
adjacent equal-length blocks, hence it maps directly to `V 2k x 1` or
`H 1 x 2k`.  Since the entire room is open, all such operations are legal.

A width-200 beam searches the one-dimensional permutations.  Its evaluation
is

```
100 * breakpoints + sum of target-coordinate displacement
```

Only cards whose target cell belongs to the current room contribute; other
cards split constrained runs as wildcards.  A beam result is accepted only
when it also strictly lowers the true wall-graph distance of the affected
cards.

Beam duplicate elimination is collision-free: a line's cards are ranked
`0..L-1` and its complete permutation is packed using five bits per position
into a `u128`.  With `L <= 20`, at most 100 bits are used.  This is not a
probabilistic hash.

The room phase has a 0.28 second global cap and a 4.5 millisecond cap per line.
These caps keep an unlucky line from consuming the complete search budget.

## Doorway batch exchange

For every boundary between different rooms, the solver enumerates every
wall-free consecutive run.  A vertical room boundary yields `H h x 2`; a
horizontal boundary yields `V 2 x w`.  Such an operation exchanges a packed
batch across the doorway in one output line.  The best strictly
distance-decreasing doorway batch is repeatedly applied for at most 0.10
seconds or 80 moves.

The subsequent 0.62 second macro phase generalizes this idea to long open
strips (thickness at most four) and local open rectangles up to 8x8.  It can
therefore move batches across artificial room boundaries which were not useful
in the dedicated doorway pass.

## Exact completion

Four checkpoints are retained: the input, after rooms, after doorways, and
after general macros.  Each is completed using 40 tree variants (five roots,
eight neighbor orders, and alternating leaf tie order).  A leaf is fixed by
moving its desired card along the active tree, then removed.  This proves exact
completion because removing a leaf preserves connectivity of the active tree.

Commuting adjacent swaps in the tail are fused into `H h x 2` or `V 2 x w`
when the fused rectangle is wall-free.  The shortest checkpoint plus tail is
selected.

Before output, every operation is replayed from the original board and checked
for bounds, parity, walls, the 100,000-line limit, and final identity.  If that
candidate fails, the solver emits the replay-checked center-tree completion.
If compression itself were ever faulty, the uncompressed exact completion is
the final emergency fallback.

## Complexity and safety

`N <= 20`, so exhaustive rectangle enumeration and `O(N^4)` all-pairs cell
distances are small.  Beam search is explicitly time-capped.  Exact completion
uses at most 79,800 adjacent operations before compression, below the output
limit.  The implementation uses only Rust's standard library.

This file was formatted and compiled with `rustc -O`.  In accordance with the
contest's generative-AI workflow rule, it was not executed on official inputs
during implementation.
