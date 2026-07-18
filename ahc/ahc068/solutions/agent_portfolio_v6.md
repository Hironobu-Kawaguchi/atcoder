# Portfolio V6: Tree V4 + Region V5 + zero-wall mesh routing

## Purpose

Official-case evaluation showed complementary behavior:

- Tree V4: total `465,482,389`, average `4,316.8` operations.
- Region V5: total `457,120,877`, average `4,473.1` operations, but it won 38
  individual cases and was better on heavily walled boards.

Portfolio V6 embeds both implementations in one standalone Rust source,
constructs the applicable candidates on the same input, independently replays
them, and emits the legal completely sorted candidate with the fewest actual
output lines. It does not estimate the winner from heuristic energy.

The implementations are placed in separate Rust modules, including all of
their code; the submission does not depend on `include!`, sibling source files,
external crates, or subprocesses.

## Candidate algorithms

### Tree V4

The tree candidate uses long wall-free strips and local rectangles to reduce
wall-graph distance, retains exact-completion checkpoints, then evaluates
multiple BFS trees with distance-prioritized leaf order. Consecutive commuting
adjacent swaps are fused where a legal rectangular operation has the same
effect.

This remains the general baseline and supplies a deterministic safe exact
completion of at most 79,800 operations.

### Region V5

The region candidate decomposes the board into large wall-free rooms, performs
room-local batch routing, moves cards through wall doorways, applies a final
macro phase, and exactly completes several checkpoints with multiple tree
plans. It is particularly useful when many walls create coherent rooms and
doorways; the official results showed an average improvement from `6,232.6`
to `6,104.6` operations on boards with more than 80 blocked edges.

### Zero-wall V6 route

When `wall_count == 0`, the portfolio uses the dedicated beam-assisted mesh
route. It decomposes the source/target row multigraph through perfect matchings,
routes in row-column-row stages, and solves the resulting length-20 line
permutations with a width-200 block-swap beam. The embedded implementation also
constructs its macro/tree candidate and returns the shorter exact result.

If this specialized result fails portfolio replay, Tree V4 is generated as the
safe replacement.

## Runtime policy

Running the original Tree V4 and Region V5 sequentially averaged roughly
`292 + 449 ms` locally, while the judge may be around three times slower. V6
therefore reduces their internal search budgets:

- Tree macro search: `0.52 s` instead of `1.02 s`.
- Region room routing: `0.15 s`.
- Region per-line routing: `0.0025 s`.
- Region doorway phase: `0.055 s`.
- Region macro phase: `0.28 s`.

For walled inputs, Tree V4 runs first. Region V5 starts if total elapsed time is
below the soft `0.82 s` cutoff. Boards with at least 80 walls always receive
the region candidate because measured results show that this is its strongest
regime; its own reduced hard phase budgets still bound the additional work.

Zero-wall inputs take the specialized branch and do not pay for Region V5.
Its line-routing and residual macro budgets are `0.68 s` and `0.34 s`.

This policy preserves portfolio comparison in the useful overlap while leaving
headroom for exact completion, replay, and output under the two-second limit.

## Independent replay and selection

The outer portfolio does not trust a candidate merely because its internal
solver completed. It parses every output line and checks:

1. exactly five fields and direction `H` or `V`;
2. rectangle bounds and the required even split dimension;
3. every internal vertical and horizontal boundary is wall-free;
4. no more than 100,000 operations;
5. replay from the original board ends with card `i` in cell `i`.

Only candidates passing all checks participate in the line-count comparison.
The emitted string is therefore the shortest validated candidate actually
constructed on that input, not a predicted winner. If a specialized or region
candidate is invalid, it is ignored. Tree V4's exact fallback remains the final
safety path.

## Correctness

Each embedded solver has an exact tree completion: repeatedly fix an active
tree leaf by moving its desired card along the unique active wall-free path,
then remove that leaf. Fixed leaves are never touched again, and the remaining
tree stays connected. The final card is correct by permutation uniqueness.

Heuristic prefixes consist only of prevalidated wall-free rectangle swaps and
therefore preserve reachability. Appending an exact completion produces a fully
sorted candidate. The zero-wall matching route similarly realizes exact line
permutations and verifies its final board.

Finally, outer replay directly verifies legality and completion. Choosing one
of the replay-valid candidates by length cannot weaken correctness.

## Complexity

With `M=N^2=400`, graph and tree distance tables use `O(M^2)` memory. Exact
tree candidate evaluation is `O(C*M^2)` for a fixed small candidate count.
Region and macro searches are wall-clock capped. Replay is linear in the total
number of swapped card pairs and uses `O(M)` extra memory.

The source is intentionally dependency-free and compatible with standalone
`rustc --edition=2021 -O` compilation.
