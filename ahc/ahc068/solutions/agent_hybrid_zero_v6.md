# Hybrid zero-wall V6

## Selection rule

V6 is deliberately conservative:

- If at least one wall exists, it executes the `tree_exact_v4` search,
  checkpoint, 72-tree portfolio, and fallback compression unchanged.
- If every wall bit is zero, it additionally builds the V5 column-row-column
  routing candidate.  The old V4 open-mesh candidate and safe tree candidates
  remain available, and the shortest complete candidate is selected internally.

This isolates the new method to the regime where the official comparison showed
a clear advantage, while retaining the established wall-case result exactly.

## Zero-wall routing

The 20-regular bipartite multigraph between current columns and target columns
is decomposed into 20 perfect matchings.  Matching color gives each card an
intermediate row.  The routing stages are:

1. column permutations by intermediate row;
2. row permutations by target column;
3. column permutations by target row.

Each line permutation uses every legal adjacent equal-block exchange.  A
width-200, depth-14 beam minimizes

```text
100 * breakpoint count + total displacement.
```

Line states use fixed `[u8; 20]` storage, fixed operation arrays, and exact
100-bit `u128` keys.  This avoids per-child allocation and hash collisions.  The
beam prefix is retained as a normal checkpoint and completed by the same exact
tree portfolio, so a line that does not finish within depth or time remains safe.
The legacy exact open-mesh route is also generated and compared.

Zero-wall line routing has a 0.72-second cutoff.  The V4 heuristic loop is skipped
only in this branch, reserving its former search budget for the beam; wall cases
retain the original V4 timing.

## Correctness and safety

Every tree completion fixes active leaves and therefore sorts the permutation.
The empty-prefix tree candidate is always present.  Before output, V6 replays the
selected operations from the original board and checks:

- operation count at most 100,000;
- bounds and required even dimension;
- absence of every internal wall;
- complete row-major sorting.

If replay fails, V6 discards the selected candidate and uses the already-built
safe tree result, which is replayed and asserted again.

## Complexity

Perfect-matching decomposition is `O(N^4)`.  A length-`L` line beam is bounded by
`O(14 * 200 * L^3)`, with `L=20`.  Exact completion and the V4 portfolio retain
their `O((N^2)^2)`-scale bounds.  Memory is dominated by tree distance tables and
beam children.  The implementation is deterministic.
