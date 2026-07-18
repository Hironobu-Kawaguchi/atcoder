# Jump Tree V8: active-window block jumps with an unchanged V4 guard

## Baseline preservation

V8 is a direct copy of `agent_tree_exact_v4`. It keeps all baseline search
behavior unchanged:

- `SEARCH_SECONDS = 1.02`;
- the same strip/local macro candidates and greedy prefix;
- the same checkpoint generation and `CHECKPOINT_LIMIT = 5`;
- the same nine roots, eight neighbor orders, and leaf tie rules;
- the original adjacent-only tree completion;
- the original fallback compressor; and
- the fully-open mesh candidate.

For each unchanged checkpoint/tree pair, V8 additionally constructs a jump
completion. The original completion remains a candidate and is selected unless
the jump completion is replay-valid and strictly shorter. This is the V4
minimum guard.

## Jump completion

Leaf selection is identical to V4. After choosing a leaf, find the unique
active-tree path from the desired card to that leaf. At the current position,
inspect the next straight run of path edges and try jump lengths `k=3,2,1`.

For a horizontal run, a jump is `H r c 1 2k`; for a vertical run it is
`V r c 2k 1`. The desired card is placed at a corresponding position in one
half, so exchanging the halves moves it exactly `k` cells along its tree path.
For example, moving right from column `c` uses the window
`[c,c+2k)`, while moving left uses `[c-k,c+k)`.

Before accepting a jump, V8 explicitly checks:

1. the next `k` tree-path edges form one straight unit-direction run;
2. the complete `2k`-cell window is inside the board;
3. every cell in the window is still active, so no fixed cell is touched;
4. every internal boundary of the window is wall-free; and
5. after applying the operation, the maintained position of the desired card
   equals the intended path vertex `k` steps ahead.

The first valid largest `k<=3` is used. `k=1` is exactly the old adjacent swap
and is always legal for an active tree edge, so progress cannot fail.

The block jump changes other active cards, which is allowed. Their maintained
positions are updated by the same operation simulator, and later leaves are
selected from that actual new state.

## Compression and selection

The original V4 compressor is extended conservatively:

- adjacent operations are batched and fused exactly as before;
- an operation with area greater than two flushes the current batch and passes
  through unchanged; and
- batching resumes afterward, so no operation is reordered across a jump.

For every checkpoint/tree pair, V8 generates:

1. original adjacent completion plus original compression; and
2. jump completion plus pass-through-aware compression.

Both tails are replayed from the exact checkpoint board. The original tail is
asserted valid. The jump tail replaces it only when it is valid, completely
sorts the board, and has fewer output operations. Candidate selection then
uses the resulting actual lengths across the unchanged 72 tree plans.

The selected prefix-plus-tail or mesh result is replayed again from the
original input board before serialization.

## Correctness

At every leaf-fixing iteration, previously removed leaves are correct and all
remaining active vertices induce a connected tree. The desired card for the
new leaf is in this active tree. A jump moves it along its unique active path
and touches only active cells; therefore no fixed card is disturbed. Repeating
jumps eventually places the desired card at the leaf, which is then removed.

Deleting a tree leaf preserves connectedness. Induction fixes all but one
card, and the final card is correct by permutation uniqueness. Thus jump
completion, like original completion, sorts the whole board exactly.

Every jump window is bounds-, parity-, active-, and wall-checked. Final replay
independently validates every operation and the completely sorted result.

## Monotonicity and output bound

The exact original V4 completion and compression are generated for every
unchanged candidate. Jump completion is used only if strictly shorter and
valid. Hence each V8 candidate is no longer than its corresponding V4
candidate, and the final minimum cannot be worse than V4 under identical
search behavior.

Original leaf fixing is bounded by `400*399/2 = 79,800` operations. Jump
completion uses at most one operation per traversed path edge and can only
reduce that count. The existing 100,000-line guard and final replay remain.

## Runtime

Prefix search and tree construction are unchanged. Post-search completion work
is approximately doubled because both completion modes are simulated for five
checkpoints and 72 plans. Each simulation is `O((N^2)^2)` with `N^2=400`; jump
validation examines at most six cells (`k<=3`) per emitted jump. This fixed
work is small enough for the time remaining after the unchanged 1.02-second
search, without adding a second heuristic search.

Official inputs were not executed while creating V8. Only `rustfmt`, optimized
standalone compilation, and static diff checks were performed.
