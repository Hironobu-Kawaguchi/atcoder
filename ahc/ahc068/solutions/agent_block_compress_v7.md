# Block compressor V7

## Baseline preservation

V7 retains `tree_exact_v4` unchanged through macro-prefix generation, five
checkpoint selection, 72 tree completions, the original commuting-swap
compression, and the fully open mesh candidate.  The four best original V4
tree candidates are saved together with both their raw adjacent-swap tails and
their original compressed tails.  The best untouched V4 output is always an
eligible final answer.

The new pass is applied only to those four tails, after all normal V4 ranking.
This keeps the additional work bounded and prevents the compressor from
changing V4's search decisions.

## Cell-dependency DAG

Every raw fallback operation is an adjacent transposition.  For each cell, V7
adds a dependency edge between consecutive operations touching that cell.
Operations without a common cell commute, so any topological order of this DAG
has exactly the same permutation as the raw sequence.

V7 tests two equivalent schedules:

- the original raw order;
- a geometry-prioritized topological order which groups ready horizontal swaps
  by column boundary and ready vertical swaps by row boundary.

The latter tends to expose parallel layers of block-exchange networks that were
interleaved with unrelated commuting swaps.

## Exact local-permutation detection

For each contiguous same-direction window, an identity-labelled board is
incrementally replayed.  The bounding rectangle is tracked.  A possible
replacement is considered only at the exact adjacent-transposition lower
bound:

- `H h x 2k` requires `h*k*k` adjacent horizontal swaps;
- `V 2k x w` requires `w*k*k` adjacent vertical swaps.

The complete labelled permutation inside the bounding rectangle is then
compared cell-by-cell with the requested equal-block exchange.  Therefore the
pass detects both one-line operations (`H 1 x 2k`, `V 2k x 1`) and parallel
multi-line operations (`H h x 2k`, `V 2k x w`).  The candidate rectangle must
also be entirely wall-free.  A matching window is replaced by one operation;
otherwise its first adjacent swap is retained.

Adjacent portions remaining around new macros are passed through V4's original
commuting-swap fusion.  Macro boundaries are not crossed, preserving order.

## Validation and correctness

The dependency DAG preserves the order of every pair of noncommuting
operations.  Its reordered stream therefore implements the raw permutation.
Every block replacement is admitted only after exact identity-label replay
proves equality with that window's permutation.  Substitution consequently
preserves the complete fallback permutation.

As a final independent guard, each shortened prefix-plus-tail candidate is
replayed from the actual input.  Bounds, parity, all internal walls, and final
identity are checked.  It replaces the V4 result only when replay succeeds and
its operation count is strictly smaller.  The ultimately selected output is
replayed again.  Thus failure to find a pattern, hash-free scheduling choices,
or an invalid replacement cannot degrade the original V4 answer.

## Cost

Only four raw tails are processed.  Dependency construction is linear in tail
length.  Window scanning is capped at 2,000 operations and stops on a direction
change; the inversion-count equality makes full rectangle comparisons sparse.
At `N=20`, replay uses 400 integer labels.  The existing V4 output limit and
safe tree guarantee remain unchanged.

No official or generated contest input was executed while implementing V7.
Verification is limited to formatting, optimized standalone compilation, and
textual diff checks.
