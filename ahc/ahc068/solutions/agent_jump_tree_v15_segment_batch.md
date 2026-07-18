# `agent_jump_tree_v15_segment_batch.rs`

## Purpose

This is a bounded MVP for a segment-normal-form front end. It does not revive
the old direct C-R-C feasibility test. Instead, it builds the bipartite graph of
horizontal and vertical wall-free segments and performs exactly one transition
round before tree completion.

## Segment batch

For each horizontal line (and independently for each vertical line), the solver
enumerates legal adjacent equal-block exchanges. A moved card is credited only
when its perpendicular segment changes and the new segment is closer in the
segment graph to either target segment. A macro is eligible only when at least
two cards improve and the net segment-distance gain, including bystanders, is
positive.

The best macro from each disjoint line is collected. At most 16 macros are kept,
and the better of the horizontal-to-vertical and vertical-to-horizontal rounds
is replayed to form one checkpoint. Thus this stage groups cards by their shared
source segment and transition phase, while every emitted macro remains a legal
wall-free line operation.

## Safety and time budget

- V14's mandatory replay-valid V10/tree portfolio is still built first and
  retained as the unconditional floor. Because optional ThickDelta width is
  reduced below, this candidate does not claim case-wise preservation of the
  complete V14 Fast K16 result.
- The segment checkpoint is raced on a fixed 5-root by 4-order tree grid and is
  selected only after replaying the full prefix and completion from the input.
  No new segment completion starts at or after 1.440 s.
- The optional ThickDelta beam is reduced from 16 to 8 completions, funding the
  new racer rather than adding unbounded work.
- Optional work starts only before 1.520 s and aborts at 1.630 s, reserving at
  least 370 ms for final replay and output.
- Any final replay failure falls back to the already validated mandatory
  V10/tree floor.

Only formatting and optimized compilation are permitted before the next explicit
evaluation instruction; this candidate was not run on an input while created.
