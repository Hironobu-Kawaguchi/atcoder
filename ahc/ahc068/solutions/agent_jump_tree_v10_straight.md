# Jump Tree V10 Straight: jump-aware shortest-path trees

## Purpose

V9 made a tree-path edge cheap when it belongs to a long straight run, but its
tree portfolio was still built by first-discovery BFS. Direction order decided
each parent without explicitly considering turns, corridor length, or how leaf
removal erodes the remaining two-dimensional active region.

This candidate changes only half of the existing 72 tree plans. It is intended
for direct official-100 comparison with the unchanged `agent_jump_tree_v9.rs`;
it does not claim a per-case V9 dominance guard because four mirrored V9 BFS
families are replaced rather than added.

## Straight-priority tree construction

For each of the nine roots, order indices 0--3 retain the exact V9 BFS tree.
Order indices 4--7 use a deterministic shortest-layer dynamic program:

1. Ordinary BFS computes the minimum grid-edge distance from the root.
2. Every cell chooses a parent only from the preceding BFS layer. Therefore
   every root path is still a shortest-edge path and no detour is introduced.
3. Parent candidates are ordered by:
   - minimum number of turns on the already selected root path;
   - maximum current straight-run length;
   - maximum forward wall-free corridor length;
   - maximum perpendicular wall-free clearance;
   - the original deterministic direction-order rank.

Parents always lie in the previous layer, so the result is an acyclic connected
spanning tree with exactly `N*N-1` edges. The construction has no random or
elapsed-time-dependent choice.

## Jump-aware leaf ordering and active-region preservation

For each straight tree, an all-pairs potential is computed in fixed
`O((N*N)^2)` work. The potential counts ideal `k<=10` straight jumps along the
unique tree path: a direction change or the eleventh consecutive edge starts a
new ideal jump. During long-tail completion this replaces raw edge distance as
the primary leaf-order key.

When two candidate leaves have the same ideal jump distance, the leaf with the
smaller number of currently active, physically adjacent grid neighbors is
removed first. Those degrees are initialized once and updated in `O(deg)` per
removal. This peels exposed boundary cells before interior cells and aims to
avoid punching early holes that turn the remaining active region into thin,
broken corridors. The original index preference remains the final stable tie
break.

The same ideal-jump matrix is passed to V9's window `delta` evaluator on these
trees. Thus each offset still measures the total collateral change over all
moved cards, but the potential now matches the number of future long jumps
rather than adjacent tree edges. No extra window scan is added.

## Work budget

The portfolio remains exactly 9 roots times 8 trees. The 36 retained BFS trees
still evaluate all four V9 tails: adjacent, V8, distance, and clearance. Each of
the 36 straight trees evaluates adjacent, V8, and one long tail; even order
indices use distance and odd indices use clearance. Consequently completion
count falls from 288 to 252 (12.5%) and pays for the fixed jump-potential
precomputation without increasing the wall-clock search budget.

No new timer, restart, plan, checkpoint, or input-dependent work cutoff is
introduced. V9's existing prefix timer is unchanged.

## Correctness guards

Every checkpoint/tree pair still generates and replays:

- the adjacent completion after fallback compression;
- the V8 completion after fallback compression; and
- one or two long-jump completions, depending on tree style.

The adjacent and V8 guards are asserted valid. A long tail is accepted only if
replay-valid and shorter. Long windows still require bounds, parity, wall,
active-cell, and exact landing checks. The winning prefix plus tail is replayed
again from the original board before output.

## Verification scope

Per the experiment protocol, no official or generated solver input was run
during implementation. Verification was limited to `rustfmt`, standalone
`rustc -O`, source diff review, and static inspection of the plan count,
progress fallback, and replay paths. Score and runtime conclusions must come
from the parent official-100 evaluation.
