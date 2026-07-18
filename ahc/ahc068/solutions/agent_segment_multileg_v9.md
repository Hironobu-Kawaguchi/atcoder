# Segment Multi-leg V9

## Goal

This candidate replaces the wall-blind global C-R-C assignment with a direct
three-leg reachability test. It then applies the transposed R-C-R construction
to the residual cards before using an exact tree completion. The implementation
is intentionally deterministic: it has no wall-clock cutoff and no random
source.

## Segment-aware assignment

Every cell receives both a maximal horizontal-segment ID and a maximal
vertical-segment ID. For a card at `(sr, sc)` with target `(tr, tc)`, an
intermediate row `mr` is eligible for C-R-C exactly when:

1. `(sr, sc)` and `(mr, sc)` have the same vertical-segment ID;
2. `(mr, sc)` and `(mr, tc)` have the same horizontal-segment ID; and
3. `(mr, tc)` and `(tr, tc)` have the same vertical-segment ID.

For each intermediate row, a Kuhn matching chooses at most one card per source
column and per target column. Used cards are removed before the next row. Sixteen
deterministic permutations of row, source, and edge order are tried, and the
assignment routing the most cards is retained.

R-C-R is the exact transpose. Its intermediate-column feasibility requires
horizontal, vertical, and horizontal segment-ID equality for the three legs,
and each layer matches source rows to target rows.

Cards already at their target are protected. A protected cell cannot be used as
an intermediate endpoint, and the protected card is installed as a real fixed
target in every line permutation. After C-R-C, protection is recomputed from the
actual board with `board[cell] == cell`; R-C-R therefore works only on the
remaining cards and restores every C-R-C success after each line.

## Wildcard line routing

Inside a wall-bounded segment, selected and protected cards carry their unique
local target coordinate. Every other card is represented by the same wildcard
label. The beam objective sums displacement and breakpoints only for real
labels, so it does not spend search effort arranging deferred cards. State keys
use all 100 available bits of `u128` (`20 * 5`), including the wildcard value
31.

The beam has width 144 and depth 14. All line beams share a fixed budget of
12,000,000 generated children. If the beam does not finish a requested partial
permutation (or the work budget is exhausted), remaining wildcard labels are
assigned in their current stable order and adjacent swaps finish the line
exactly. This cleanup is independent of elapsed time, remains inside the same
wall-free segment, and is bounded by 190 swaps per line.

## Checkpoints and exact fallback

Three checkpoints are retained:

1. the original board;
2. after segment-aware C-R-C; and
3. after residual R-C-R.

Each checkpoint is completed with nine BFS roots, eight deterministic neighbor
orders, and both tie directions. For every plan the solver generates both:

- the original adjacent-only leaf elimination; and
- active-window jump elimination with the largest legal `k <= 3`.

Previously fixed tree leaves are excluded from an entire jump window. Rectangle
bounds and every wall are checked before applying it. Non-adjacent operations
pass through the conservative disjoint-swap compressor without reordering.

Both raw/compressed tails are replayed from their checkpoint. Every full
prefix-plus-tail candidate is then replayed from the original input, including
non-improving candidates; only a replay-valid candidate below 100,000 operations
can replace the current best. The empty-prefix adjacent tree completion is the
unconditional emergency answer.

## Deliberate MVP limitations

- The constrained assignment is a sequence of maximum bipartite matchings, not
  a globally maximum three-dimensional matching across all intermediate lines.
- It supports only direct C-R-C and R-C-R paths. It does not search a general
  multi-round segment graph or move a card through several doorway segments.
- Protecting already-correct cards reduces matching capacity. A stronger engine
  could allow them to move while enforcing their restoration globally.
- The exact line cleanup can reintroduce adjacent operations if the fixed-work
  beam misses a solution. It is a correctness fallback, not the intended fast
  path.
- The tree portfolio is exact and guarded, but this file does not duplicate the
  time-dependent macro-prefix search from `agent_jump_tree_v8`.

No official or generated contest input was run while creating this candidate.
Validation was limited to `rustfmt`, optimized standalone compilation, and
static inspection, as required by the active AHC generative-AI rule workflow.
