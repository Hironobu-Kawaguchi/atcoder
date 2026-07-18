# jump_tree_v13_lite_delta

This experiment keeps the full V11 ThickSafe result as an unconditional,
replay-verified floor.  It then revisits only that result's winning
tree/checkpoint instead of applying ThickDelta to a top-K list.

For each straight routing step, the post-pass first chooses one legal thin
window by total tree-distance delta.  It widens only that winner to at most four
lines and uses the raw ThickDelta ordering: total distance delta, larger area,
balanced clearance, total clearance, centering, and deterministic offsets.
This reduces the worst candidate multiplication from roughly 10 offsets times
10 thickness placements to 10 thin evaluations plus 9 thick evaluations.

Optional work is bounded twice:

- at most 8,000 thick candidates per completion;
- no post-pass starts after 1.55 seconds, and thick enumeration stops at 1.72
  seconds while the legal thin completion is allowed to finish.

`agent_jump_tree_v13_lite_delta.rs` evaluates the selected V11 preference only.
`agent_jump_tree_v13_lite_delta_prefer_sweep.rs` changes the const generic from
`false` to `true`, adding the opposite `prefer_larger` order only when the same
1.55-second start gate still has room.  The two wrappers otherwise share the
same implementation.

No candidate can replace V11 unless it is shorter, at most 100,000 operations,
and independently replays to the exact target board.  A final release-build
guard restores the original V11 operations on any legality or monotonicity
failure.
