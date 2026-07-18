# Greedy rectangle V3: two-ply rollout and multi-fallback checkpoints

## Motivation

V2 evaluated every accepted rectangle directly against one fixed fallback.  The
fallback count is discontinuous: a useful sequence can require a neutral or
temporarily unfavorable first move, so strict one-step acceptance often remains
near the relatively expensive initial tree solution.  V3 restores a long
distance-reducing rectangle prefix, but protects it with exact checkpoint
rollback and substantially improves the completion choice.

## Rectangle search

Two candidate tiers are precomputed, including adjacent swaps.  The core tier
contains all wall-free rectangles up to 4x4 and is scanned on ordinary steps.
Every 32nd step uses a macro tier up to 6x6 instead.  This periodically exposes
larger block moves without paying their larger scan cost on every iteration.
Each operation stores its swapped cell pairs.  The inexpensive gain is

```text
4 * decrease in total wall-graph shortest-path distance
    + decrease in misplaced cells.
```

At every step, the eight candidates with largest positive immediate gain form a
shortlist.  Each possible first move is applied to a temporary board and scored
together with the best compatible second move from the same shortlist.  The
first move of the best two-ply rollout is applied.  This bounded rollout handles
interactions between overlapping rectangles without rescanning the full move set
at every second-ply node.

Search stops after 20,000 prefix moves or at 1.10 seconds.  Every 32 moves, and
at termination, the exact fallback count is measured.  The eight best distinct
checkpoints (including the empty prefix) retain board, positions, and prefix.

## Multiple exact fallbacks

Nine BFS spanning forests are built from corners, edge midpoints, and the center,
with alternating neighbor order.  During leaf elimination, the active leaf whose
target tile is currently nearest in that tree is fixed first.  This dynamic leaf
order generally avoids routing a tile along a long path when a cheaper leaf is
available.

After heuristic search, every saved checkpoint is evaluated with every forest.
The exact minimum of

```text
saved prefix length + complete fallback operation count
```

is selected, and only that prefix/fallback pair is emitted.  The empty prefix is
always among the candidates, so V3 cannot be worse than its initial primary
fallback and stays below the 100,000-operation limit.

## Correctness

Every rectangle candidate is checked to contain no internal wall and to have the
required even dimension.  The fallback repeatedly fixes a leaf of an active
spanning tree.  Its target tile lies in the active tree because removed leaves
already contain their distinct final tiles.  Moving it along the unique tree path
uses only legal adjacent swaps.  Removing the fixed leaf never touches it again.
Induction fixes all non-root cells; the remaining root tile is then forced to be
correct.  Applying this independently to every wall component completely sorts
every feasible input.

## Complexity

For `K=N^2`, `R` candidates, rollout width `B=8`, prefix length `P`, saved states
`C<=8`, and forests `F=9`:

- wall distances: `O(K(K+E))` time and `O(K^2)` memory;
- rectangle search: `O(P * (sum candidate areas + B^2 * max area))`;
- one fallback: at most `O(K^2)` swaps plus `O(K^2)` leaf scans;
- final exact comparison: `O(C * F * K^2)`;
- stored candidates, forests, distances, and checkpoints: `O(R*K + F*K^2)` in
  the loose bound (actual candidate pair lists are bounded by 18 pairs each).

The wall-clock search cutoff reserves time for exact comparison, fallback
materialization, and output serialization.  The algorithm is deterministic.
