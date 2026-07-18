# jump_tree_v12 beam-pruned ThickDelta

V12 turns the expensive V11 ThickDelta portfolio into a deterministic
two-stage beam over the actual tree-plan/checkpoint states.

1. Enumerate all `9 roots x 8 orders x checkpoints.len()` states.
2. Evaluate every state with the exact V10 completion portfolio: old tree,
   V8 edge jumps, Distance windows, and line-only Clearance windows.
3. Keep the exact global V10 winner as an unconditional safety floor.
4. Rank states by `prefix length + V10 completion length`, with stable
   structural tie-breaking, and run ThickDelta only for the best K states.
5. Select the shortest replay-valid result, with a final fallback to the
   replay-valid V10 winner.

The three wrappers use `K = 8, 16, 32`. The beam work is fixed for a given
checkpoint set; V10's existing 1.02-second macro-prefix guard is intentionally
unchanged so the first stage remains behavior-compatible with V10.

The wrappers use Rust `include!` to avoid three drifting copies of a long
contest solver. They compile directly from this directory, but an AtCoder
single-file submission must be flattened by expanding the two included files.
