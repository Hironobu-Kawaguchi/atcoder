# Tree exact V3: rectangle prefix with multi-checkpoint tree completion

## Difference from V2

V2 starts leaf fixing immediately and evaluates 200 BFS trees on the initial
permutation. Its dynamic minimum-distance leaf order improves the exact
baseline, but every emitted operation still swaps only two adjacent cards.

V3 adds a legal rectangle prefix before exact completion. A single rectangle
operation can move several cards toward their targets simultaneously. Rather
than committing to one locally generated prefix, V3 retains up to six promising
prefix checkpoints and jointly selects the checkpoint, spanning tree, and leaf
tie order by the final exact operation count.

## Rectangle prefix

The heuristic energy is the sum of wall-graph shortest-path distances from
each card to its target. All wall-free rectangles up to 4x4 with an even
height or width are precomputed. At each iteration V3 applies the operation
with the largest strict energy decrease. Search stops at a local optimum,
18,000 moves, or 1.05 seconds.

The empty prefix, every 16th prefix, unusually strong moves, and the terminal
prefix are evaluated with a quick center-rooted exact tree completion. Only the
six smallest values of

`prefix length + quick exact completion length`

are retained. This rollback scheme prevents a long locally improving suffix
from being forced into the final output.

## Exact multi-tree completion

Each retained checkpoint is completed with 72 deterministic tree plans:

- nine roots: the center, four corners, and four edge midpoints;
- eight clockwise/counterclockwise neighbor orders; and
- alternating low/high cell-index tie breaking.

Within each plan, all tree distances are precomputed. At every step, V3 chooses
the active leaf whose desired card is currently closest in that tree, moves the
card along the unique active-tree path with adjacent swaps, fixes the leaf, and
removes it. The checkpoint/tree combination with the fewest total operations
is emitted.

Compared with V2's 200 trees on one state, V3 spends its exact-evaluation
budget across up to six meaningfully different states. The 72-tree set still
contains the quick center-rooted plan used to rank checkpoints.

## Correctness

Every prefix rectangle is checked to contain no internal wall, and its selected
dimension is even, so every prefix operation is legal.

For any tree completion, removed leaves contain their final cards and the
active vertices induce a connected tree. The desired card for an active leaf
cannot be in a removed vertex, because removed vertices contain their own
distinct cards. It is therefore in the active tree, and the unique path from
the card to the leaf contains only active, wall-free edges. Adjacent swaps along
that path fix the leaf without disturbing earlier fixed leaves. Removing a leaf
preserves the invariant. The last card is correct because all other cards of
the permutation are fixed.

Thus every prefix/tree candidate ends completely sorted. V3 only selects among
such exact candidates.

## Operation-limit guarantee

An exact tree completion alone needs at most

`400*399/2 = 79,800`

adjacent swaps. The empty checkpoint is initially available, and a checkpoint
can displace it from the six-entry shortlist only if its prefix plus completion
under the quick tree is smaller. That quick tree is also one of the final 72
plans. Consequently at least one evaluated candidate has at most 79,800 total
operations. V3 ignores candidates above 100,000 and selects a safe candidate,
so the output limit is guaranteed.

## Complexity and timing

For `M=N^2=400`, graph/tree all-pairs distances use `O(M^2)` memory. Rectangle
search scans a fixed set of constant-area operations until the 1.05-second cap.
Afterward, at most `6*72=432` exact completions are evaluated. Each completion
uses `O(M^2)` leaf scanning plus at most `O(M^2)` path swaps. Only one tree's
distance table is live at a time.

The 1.05-second heuristic cap leaves the remainder of the two-second limit for
checkpoint evaluation, multi-tree completion, and serialization. The candidate
counts are fixed and deterministic; only the heuristic prefix length is
time-capped.

## Assumptions

- Card labels are `0..N^2-1`, targeting row-major cells.
- `0` is a passable boundary and `1` is a wall.
- The wall-free graph is connected.
- Output coordinates are zero-based and no operation-count header is printed.
