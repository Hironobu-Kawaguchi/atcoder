# Tree exact V5: alternating maximal-segment crossbar routing

## Main change from V4

V4 greedily selected one rectangle at a time. V5 treats every maximal
horizontal or vertical wall-free segment as a crossbar switch and routes all
cards on that switch simultaneously. Tree leaf fixing is retained only as an
exact completion and safety certificate after the batch-routing phase.

Every cell is the incidence point of one horizontal and one vertical maximal
segment. Alternating horizontal and vertical switch permutations therefore
moves cards through the bipartite segment-incidence graph. This generalizes the
row-column-row construction from a completely open mesh to arbitrary walls:
full rows and columns are large switches, while shorter segments provide local
transfer switches around walls.

## One crossbar sweep

For a segment containing cards `x_i` and port cells `p_j`, V5 builds the cost

`cost(i,j) = wall_graph_distance(target(x_i), p_j)`.

The Hungarian algorithm finds the minimum-cost perfect assignment of every
card to a distinct port in `O(L^3)` for segment length `L<=20`. The current
arrangement is itself feasible, so the assignment is applied only when its
total distance is strictly smaller.

The assigned permutation is realized within the open segment by:

1. greedily exchanging adjacent equal-length blocks (`1 x 2k` or `2k x 1`)
   whenever one block operation removes at least two inversions; then
2. adjacent insertion swaps to realize the remaining exact permutation.

The remaining insertion count equals the inversion count. Thus every selected
block macro provably reduces the number of output lines relative to immediately
using insertion, directly addressing V4's dominant 1D residual cost.

Thus one segment decision batch-routes all its cards instead of selecting a
single favorable rectangle.

## Alternating routing and checkpointing

V5 runs two deterministic trajectories, one horizontal-first and one
vertical-first. Each performs at most 20 half-sweeps and stops after both
orientations make no improvement. Total wall-graph distance strictly decreases
whenever a segment is changed, preventing cycles.

After every improving sweep, the state is evaluated by a center-rooted exact
completion. The six best values of

`crossbar prefix length + quick exact completion length`

are retained. Finally, every retained state is completed with 72 tree plans
(nine roots, eight neighbor orders, alternating leaf ties), and the smallest
exact total is emitted. The empty prefix is always introduced as a candidate.

Before serialization, V5 replays the selected operations from the original
board, rechecks every rectangle boundary, and verifies complete sorting. Any
failure falls back to the uncompressed safe center-tree completion.

## Dependency-DAG fallback scheduling

The raw exact completion is represented as an adjacent-swap event DAG. For
each cell, only the original order of events touching that cell is a dependency;
events on disjoint cells commute. Consequently every topological ready layer is
a matching. V5 reschedules by these layers and fuses horizontal ready swaps on
consecutive rows into `H r c h 2`, or vertical ready swaps on consecutive
columns into `V r c 2 w`, whenever the full combined rectangle is wall-free.
This can group swaps separated widely in the original leaf-fixing sequence and
is stronger than V4's consecutive-batch fusion.

## Correctness

A maximal segment contains no wall on its one-dimensional interior. Every
block or adjacent operation emitted by its segment permutation is therefore
legal. Hungarian assignment is a permutation of the segment ports, and the
1D insertion phase realizes it exactly, so the maintained board matches the
internally planned state after every sweep.

The exact completion repeatedly selects an active tree leaf and moves its
desired card along the unique active wall-free path. Fixed leaves are removed
and never touched again. The remaining active vertices stay connected; after
all but one cards are fixed, the last is correct by permutation uniqueness.
Therefore every evaluated prefix plus completion fully sorts the board.

The DAG retains the order of every pair of noncommuting, same-cell events.
Every reordered pair is disjoint and commutes. Each fused operation performs
exactly its layer's disjoint swaps, with legality checked across the entire
rectangle, so DAG scheduling preserves the exact permutation.

The empty-prefix tree completion uses at most
`400*399/2 = 79,800` operations. It remains available unless replaced by
checkpoints with a strictly smaller quick exact total, and that quick plan is
among the final plans. Candidates above 100,000 are ignored. Hence a completely
sorted, output-limit-safe candidate always exists.

## Complexity and two-second bound

There are at most 400 horizontal and 400 vertical segments, each of length at
most 20. Two trajectories use at most 40 sweeps in total. Hungarian work is
bounded by `O(40 * number_of_segments * N^3)` with very small `N=20`; 1D
routing is `O(N^3)` per changed segment in the conservative bound. No
wall-clock-dependent unbounded loop is used.

At most six checkpoints times 72 tree completions are evaluated. Each tree
completion and its distance table use `O((N^2)^2)` time and memory. The fixed
candidate budget is designed for the two-second limit.

## Assumptions

- Cards are `0..N^2-1` with row-major targets.
- Wall character `0` is passable and `1` is blocked.
- The wall-free cell graph is connected.
- Output coordinates are zero-based with no count header.
