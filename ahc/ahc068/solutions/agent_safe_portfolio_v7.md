# Safe portfolio V7

## Non-negotiable baseline

V7 first generates and retains the complete `tree_exact_v4` candidate. Its
1.05-second macro search, checkpoint policy, 72-tree portfolio, leaf ordering,
and commuting-swap compression are unchanged.  No experimental state is shared
with this baseline.

For a zero-wall board, V7 retains the V6 behavior instead: the legacy exact mesh
route and the width-200 column-row-column beam checkpoint are compared with the
safe tree candidates.

## Slack-only region candidate

The region candidate is considered only when at least one wall exists and global
elapsed time is below 1.16 seconds after the baseline has been completed.  If the
gate is missed, V7 immediately returns the already-built baseline.

The reduced candidate independently restarts from the original permutation:

1. greedily tile the board with large non-overlapping wall-free rectangles;
2. run a width-48, depth-8 breakpoint beam on each room's strips in V-H-V order;
3. treat cards targeting another room as wildcards;
4. greedily apply only a small family of wall-free doorway `k x 2` / `2 x k`
   batch exchanges;
5. attach the established quick exact tree completion and compress it.

All region work has a global 1.30-second deadline.  There is no full region macro
phase and no second tree portfolio, keeping the optional branch small enough for
parallel local jobs and leaving judge margin.

## Candidate admission and safety

The baseline remains stored throughout.  The region candidate replaces it only
if both conditions hold:

- its operation count is strictly smaller;
- an independent replay from the original board verifies every bound, even
  dimension, internal wall, and final sorted position.

The selected answer is replayed once more before serialization.  If that check
fails, V7 discards all prefixes and emits an uncompressed empty-prefix exact tree
completion.  Consequently optional work can improve operation count but cannot
degrade validity, completeness, or the 100,000-operation guarantee.

## Complexity

The mandatory branch has exactly the V4 asymptotic cost.  Optional room discovery
enumerates `O(N^4)` rectangles; each length-`L<=20` strip beam is bounded by
`O(8 * 48 * L^3)`.  The reduced doorway scan is polynomial and deadline-bounded.
Memory is dominated by the existing tree-distance tables and short beam layers.
