# Static selector V6

## Data used

The selector was fitted only from the already recorded official-100 run
`20260718T070646Z/details.csv` and input-derived wall features.  No solution was
run while creating V6.

The three relevant per-case winners were:

- `tree_exact_v4`: 49 cases;
- `region_router_v5`: 36 cases;
- `greedy_rect_v5`: 15 cases, including every one of the nine zero-wall cases.

Candidate features were wall count, full rows/columns, maximal passable segment
length, mean segment length, and maximum completely wall-free rectangle area.
To avoid fitting a fragile classifier to only 100 cases, V6 uses two predicates
and no permutation-dependent feature:

```text
wall_count == 0             -> GreedyZero
maximum_open_rectangle <= 98 -> Region
otherwise                    -> Tree
```

The maximum-open-rectangle threshold was unusually stable: when refitting the
single tree/region threshold in leave-one-out fashion on the 91 nonzero-wall
cases, 90 folds selected 98 and one selected 96.  Leave-one-out regret against
the per-case tree/region oracle was 13,905 operations in total.

On the stored run, without rerunning any solver, this static choice corresponds
to 59 tree, 32 region, and 9 greedy-zero cases.  Selecting the recorded outputs
would total 415,249 operations and 480,273,064 score, versus tree V4's 431,680
operations and 465,482,389 score.  These figures describe the stored data, not
a new evaluation of V6.

## Runtime implementation

Input analysis counts walls and computes maximum open rectangle area in a small
`N=20` dynamic row-band scan.  It then executes exactly one expensive prefix
family:

- **GreedyZero:** column-row-column routing.  Twenty bipartite matchings assign
  intermediate rows; width-200 equal-block line beams construct the prefix.
- **Region:** room decomposition, in-room routing, doorway batches, and the
  bounded region macro phase from `region_router_v5`.
- **Tree:** no prefix search; directly evaluate the nine-root/eight-order exact
  tree family from `tree_exact_v4`.

All branches retain exact tree completion and commuting-adjacent-swap fusion.
Region and GreedyZero also retain the empty-prefix candidate, so their routing
cannot remove the safe solution.

## Correctness and safety

Tree leaf fixing repeatedly moves the desired card to an active leaf along the
unique active-tree path and removes that leaf.  The remaining tree stays
connected, so induction completely sorts the board.  Fusion replaces only
pairwise-disjoint commuting adjacent swaps and checks the resulting rectangle
against every internal wall.

The final operation sequence is replayed from the input.  Every operation is
checked for bounds, parity, and walls, and the final board must be the identity.
If a routed candidate fails, the independently constructed emergency tree
completion is emitted.  The raw tree bound is at most 79,800 operations.

V6 was formatted and compiled with standalone optimized `rustc`.  It was not
executed on official or generated contest input.
