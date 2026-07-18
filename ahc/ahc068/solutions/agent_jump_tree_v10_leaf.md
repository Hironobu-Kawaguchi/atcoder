# Jump Tree V10 Leaf: jump-aware leaf order and full-window potential

## Goal

V9 chooses the next active tree leaf by the unit-edge distance from that
leaf's card to its target. That is only an indirect proxy after long block
jumps become available. This candidate replaces V9's `Clearance` completion
with one deterministic `JumpAware` completion while retaining the V4, exact
V8, and V9 `Distance` guards.

## Jump-aware leaf shortlist

Evaluating every active leaf path at every one of the 399 elimination steps
would consume the remaining runtime margin. The candidate therefore first
sorts leaves by V9's old unit-distance key and retains exactly the best eight.
Only those eight paths are constructed and evaluated.

For each shortlisted path, a backward DP computes the minimum number of legal
`k<=10` line jumps. Every path position tests all straight-ahead lengths. A
jump is legal when some source-half offset gives a `2k` window wholly inside
the current active, wall-free line segment. The estimator answers this in
O(1): static wall segments are precomputed, and the changing active cells of
each row and column are stored in `u64` masks (`N=20`). Thus one leaf estimate
is `O(path length * 10)`, with no search restart or elapsed-time decision.

The estimated operation count is the primary leaf key. If several shortlisted
leaves tie, the candidate compares the best first-operation change in the
full tree-distance potential `Phi` and then prefers the thicker current active
corridor. The potential delta is computed by the ordinary `delta()` routine,
so it includes every one of the `2k` moved cards rather than only the card
being routed. Unit distance and stable leaf ID remain final tie-breakers.

## Choosing jump length and offset

V9 `Distance` fixes the longest feasible `k` first and only compares offsets
for that length. `JumpAware` instead compares every `(k, offset)` pair for the
current straight run, at most

`1 + 2 + ... + 10 = 55`

windows. Its lexicographic key is:

1. minimum total `Delta Phi` for all cards moved by the operation;
2. larger routed distance `k`;
3. larger balanced and total active clearance; and
4. stable smallest offset.

Because each candidate window costs one output operation, total `Delta Phi`
is also `Delta Phi / operation`. Letting `Delta Phi` precede `k` deliberately
permits a shorter jump when the longer swap's collateral displacement is
worse. The exact V9 `Distance` candidate remains available to cover cases
where longest-first is better.

## Guards and correctness

For each unchanged checkpoint/tree pair, selection builds:

1. the adjacent V4 completion;
2. the exact V8 `k<=3, offset=0` completion;
3. V9's longest-first `Distance` completion; and
4. the new `JumpAware` completion.

V4 and V8 are replay-asserted. A long-jump candidate is adopted only after
replay and only when strictly shorter than the guarded result. The final
prefix plus tail is replayed again from the original board before output.

The leaf DP affects ordering only. Actual operations retain the invariant that
the whole window is active and wall-free, and the routed card is asserted to
land on the selected later path vertex. Removing a completed leaf therefore
cannot disturb any fixed leaf, and the usual active-tree induction proves
completion.

## Runtime and reproducibility

The new decisions use fixed shortlist and jump bounds and no new wall-clock
cutoff. `JumpAware` replaces the previous `Clearance` tail rather than being
added as a fifth tail. Its per-step window work is bounded by 55 candidates,
and its leaf estimator uses bit-mask segment queries rather than rectangle
scans. The base V9 prefix-search cutoff is otherwise unchanged so the
candidate is a one-variable comparison against V9.

Official or generated inputs were not executed during implementation. Only
`rustfmt`, optimized standalone compilation, and static source inspection
were used before parent-side evaluation.
