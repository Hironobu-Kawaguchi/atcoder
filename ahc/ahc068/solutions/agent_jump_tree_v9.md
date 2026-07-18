# Jump Tree V9: long jumps with movable source offsets

## Goal

V8 caps each tree-path jump at `k=3` and always places the routed card at
offset zero within its source half. V9 preserves that exact completion as a
guard, then adds deterministic `k<=10` completions that enumerate every legal
source offset. No wall-clock-dependent search is added.

## Window enumeration

For a straight path run of length `s`, V9 tries jump lengths
`min(s,10),...,1`. For a jump of length `k`, the routed card may occupy any
offset `o in [0,k)` in its source half. If its current row/column coordinate is
`x`, the line-window origin is:

- right/down: `x-o`;
- left/up: `x-k-o`.

The operation has length `2k`, so exchanging its equal halves moves the card
exactly `k` cells along the path for every enumerated offset. A candidate is
retained only when the whole window is in bounds, active, and wall-free.
`k=1,o=0` is the original adjacent tree edge, so completion always progresses.

Jump length remains the first priority: V9 selects a window only among the
longest currently feasible `k`. It constructs two deterministic long-jump
tails with different offset tie-breaking:

1. **Distance policy:** minimize the operation's change in the sum of all
   cards' tree distances, then prefer balanced active clearance.
2. **Clearance policy:** first center the window within its containing active,
   wall-free corridor, then minimize tree-distance damage.

Both finally prefer the routed card nearer the center of its half and use the
smallest offset as a stable last tie-break. The policies differ only in window
placement; both use the same longest-feasible-jump rule.

## V8 and V4 guards

For every unchanged checkpoint/tree pair, selection independently builds and
replays:

1. the original adjacent V4 completion plus fallback compression;
2. the exact V8 `k<=3,o=0` completion plus compression;
3. the V9 distance-policy completion plus compression; and
4. the V9 clearance-policy completion plus compression.

The V4 and V8 tails are asserted replay-valid. Each V9 tail is replayed from
the exact checkpoint board and is adopted only when valid and strictly shorter
than the best guarded tail. Thus a poor offset heuristic cannot worsen the
selected completion for that checkpoint/tree pair. The chosen prefix and tail
are replayed once more from the original input before serialization.

## Correctness

Leaf choice and active-tree maintenance are unchanged from V8. Every selected
window touches active cells only, so it cannot disturb a previously fixed
leaf. The routed card moves to the path vertex exactly `k` edges ahead; repeated
jumps put it at its target leaf. Removing that leaf preserves active-tree
connectedness, and induction sorts the entire permutation.

Arbitrary offsets do not change this argument: a half swap maps offset `o` in
one half to the same offset in the other half. Bounds, parity, walls, active
cells, landing position, and final sortedness are all checked by the existing
simulator/replay path.

## Runtime and reproducibility

The prefix search, checkpoints, roots, tree orders, and time budget are
unchanged. V9 adds fixed deterministic completion work: at most ten offsets
for each of at most ten jump lengths, on two new tails. Candidate scoring
touches only the at-most-20-cell line window plus a length-20 clearance scan.
It adds no new elapsed-time cutoff, random restart, or machine-dependent branch.

Official or generated inputs were not executed during implementation. Only
formatting, optimized standalone compilation, and static source inspection are
permitted for this candidate before the parent evaluation stage.
