# `agent_segment_crc_v9.rs`

## Aim

Replace the wall-blind C-R-C assignment in `agent_greedy_rect_v5.rs` with a
wall-aware partial routing engine.  The engine is always wrapped in exact tree
completion, so a partial or unhelpful C-R-C prefix cannot make the submitted
answer invalid.

## Segment-constrained C-R-C assignment

Every cell receives a horizontal-segment ID and a vertical-segment ID.  For a
card currently at `(sr, sc)`, whose target is `(tr, tc)`, middle row `mr` is
allowed only when all three legs are possible without crossing a wall:

1. `(sr, sc)` and `(mr, sc)` have the same vertical-segment ID.
2. `(mr, sc)` and `(mr, tc)` have the same horizontal-segment ID.
3. `(mr, tc)` and `(tr, tc)` have the same vertical-segment ID.

For each middle row, a Kuhn matching selects at most one card from each source
column and at most one card for each target column.  Used cards are removed
before processing the next row.  Thirty-two fixed, deterministic row/source/card
orders are tried, and the assignment routing the most cards is retained.  This
is fixed work; it does not depend on wall-clock speed.

## True wildcard line routing

Cards rejected by the constrained assignment use key `31`.  In the beam score
they have no target, displacement, or adjacency penalty, and consecutive
wildcards are indistinguishable in the `u128` state key.  Thus the beam does not
spend operations arranging deferred cards into arbitrary fake positions.

The beam is only an accelerator.  After it stops, real targets retain their
required slots, while wildcard cards are assigned the remaining slots in their
then-current stable order.  Adjacent swaps finish that local permutation.  This
guarantees that every assigned card completes the current C-R-C leg even if the
beam does not reach zero cost.

## Safety portfolio

Four checkpoints are considered: empty prefix and the states after C, C-R, and
C-R-C.  For every checkpoint, several deterministic BFS trees generate both:

- ordinary exact adjacent-swap completion, and
- `jump_tree_v8`-style straight jumps of length at most three.

Adjacent-swap compression is replay-checked and falls back to its raw exact
sequence if necessary.  A candidate is admitted only after a full replay from
the original input proves every rectangle legal and the final board sorted.
The empty-prefix exact-tree checkpoint therefore remains an unconditional safe
candidate.

## Build-only verification

The candidate was formatted and optimized-compiled as a standalone Rust 2021
source file.  In accordance with the active AHC generative-AI rule, it was not
executed on any input while being implemented.
