# jump_tree_v11_large_macro

## Objective

Test whether the prefix optimizer is leaving useful multi-line moves unused.
`jump_tree_v10_zero` admits long thin rectangles and local rectangles up to
8x8, but excludes rectangles that are large in both dimensions. This variant
adds those moves without increasing the number of candidates evaluated in one
complete scan.

The zero-wall early route and every tree-completion policy are unchanged from
V10 zero. Only the wall-present prefix candidate set is different.

## Fixed candidate budget

- Let `L` be the number of legal V10 prefix candidates on the instance.
- The new total is at most `min(L, 12_000)`. It can therefore never exceed the
  old per-scan candidate count on the same board.
- At most one fifth of those slots, and never more than 2,400 slots, are
  assigned to new large rectangles. A large rectangle can only replace a
  nonessential legacy slot.
- The remaining slots retain V10 candidates. One-line operations and
  operations of area at most 8 are preserved first. Other candidates are
  sampled evenly in the old deterministic generation order.
- Across the entire prefix search, calls to the graph-distance `delta`
  evaluator are capped at 24,000,000. A scan is only started when its complete
  candidate set fits in the remaining budget, avoiding order-biased partial
  scans.
- `SEARCH_SECONDS` remains 1.02 seconds and `SEARCH_MOVE_LIMIT` remains 20,000.

## New rectangle family

A new candidate is outside the V10 family, wall-free, has minimum side at
least 5, area at least 48, and has an even split dimension for its direction.
This includes the requested rectangles with both `h > 8` and `w > 8` whenever
they exist, as well as moderately thick rectangles that are more likely to
survive sparse walls.

The new pool is ranked by:

1. descending area;
2. descending shorter side;
3. descending movement-direction span;
4. deterministic direction, position, and shape tie-breaks.

Selection is round-robin over direction and a 4x4 grid of rectangle centers.
The 32 buckets prevent the top-ranked set from consisting only of overlapping
rectangles in one region or one direction. New rectangles are appended after
legacy candidates, so a tied total-graph `delta` retains V10's choice.

## Safety and expected trade-off

Legality still uses the existing full-rectangle wall check, and scoring still
uses the exact total graph-distance delta over every swapped card. Output
replay validation and the exact completion fallback are unchanged.

Large candidates cost more per delta evaluation because they move more cards.
The fixed candidate and evaluation ceilings bound that risk, but the unchanged
wall-clock cutoff can still yield fewer prefix moves. This is intentionally an
experimental comparison candidate rather than a replacement selected without
official-sample evaluation.

## Verification restriction

Per delegation instructions, this implementation must only be checked with
`rustfmt`, optimized compilation, and static review before handoff. It must not
be executed on contest inputs by its implementing agent.
