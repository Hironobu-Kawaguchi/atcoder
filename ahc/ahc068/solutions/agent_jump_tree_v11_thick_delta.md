# jump_tree_v11_thick_delta

## Intent

This candidate keeps `agent_jump_tree_v10_zero.rs` unchanged everywhere except
for the fourth guarded tree-completion policy. The zero-wall deterministic C-R-C
branch is byte-for-byte equivalent in behavior. On wall-bearing inputs the old
`Clearance` completion candidate is replaced by `ThickDelta`; the `old`, `V8Edge`,
and `Distance` completion guards remain available and the shortest replay-valid
completion is still selected per checkpoint and tree.

## ThickDelta policy

For each focus card and straight tree-path run:

1. Preserve V9's longest-feasible-jump-first rule (`k <= 10`).
2. Enumerate every longitudinal offset for that `k`.
3. For the resulting legal line jump, enumerate thickness `1..=4` and every
   perpendicular placement that contains the focus card's row or column.
4. Reject a rectangle unless all cells are active, the full rectangle is
   wall-free, and an explicit coordinate mapping proves that the focus card
   lands at `path[at + k]`.
5. Rank candidates lexicographically by:
   - minimum total change in tree distance over every moved card;
   - maximum rectangle area;
   - maximum balanced and total open/active clearance along the motion axis;
   - the pre-existing center and deterministic offset tie-breakers.

Thickness one is always present, so the policy retains a legal line-jump
fallback. Enumeration is fixed (`sum(1..=4) = 10` perpendicular placements per
line window at most) and adds no wall-clock-dependent search or candidate
pipeline.

## Safety and validation

- The final full replay validation is unchanged.
- `old`, `V8Edge`, and `Distance` monotonic guards are unchanged.
- The zero-wall early C-R-C branch is unchanged.
- Formatted with `rustfmt`.
- Compiled successfully with `rustc -O`.
- No official or generated input was executed while implementing this candidate;
  comparative scoring is intentionally left to the parent evaluation process.

### Four-direction landing audit

Let the focus cell be `(r, c)`, the longitudinal offset be `o < k`, and the
block half-length be `k`. Extending perpendicular to the motion direction does
not change these longitudinal coordinates.

| Path direction | Rectangle origin on motion axis | Focus half/index | Mapped destination |
|---|---:|---:|---:|
| right | `c - o` | first / `o` | `(r, c + k)` |
| left | `c - k - o` | second / `k + o` | `(r, c - k)` |
| down | `r - o` | first / `o` | `(r + k, c)` |
| up | `r - k - o` | second / `k + o` | `(r - k, c)` |

Candidate generation also checks this identity through `swapped_cell` before
considering active cells, walls, or ranking, and `complete_jump` asserts the
same destination again after applying the selected operation.
