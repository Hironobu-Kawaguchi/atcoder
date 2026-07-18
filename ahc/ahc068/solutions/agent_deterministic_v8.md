# Deterministic low-risk V8

## Mandatory baseline

V8 runs `agent_tree_exact_v4` unchanged as its mandatory candidate: the same
time-limited heuristic, checkpoints, roots, direction orders, exact completions,
and fallback compression are used.  This complete candidate is retained before
any optional work starts.

## Zero-risk involution cancellation

Every legal rectangle half-swap is an involution.  Therefore two adjacent,
completely identical operations have no net effect in any board state.  V8 runs
a stack reduction over each completed candidate:

```text
if stack.top == operation: pop
else:                      push operation
```

The reduction also discovers newly adjacent equal pairs after an inner pair is
removed.  It changes neither legality nor final output and can only shorten the
operation list.

## Fixed-work transposition portfolio

The optional candidate transposes all problem semantics, not only the matrix:

- cell `(r,c)` becomes `(c,r)`;
- card target `(tr,tc)` becomes `(tc,tr)`;
- original horizontal walls become transposed vertical walls;
- original vertical walls become transposed horizontal walls;
- `H r c h w` maps back to `V c r w h`, and vice versa.

The same V4 solver is then run with a deterministic reduced budget:

- exactly up to 96 heuristic iterations, with no elapsed-time stopping rule;
- three roots;
- two direction orders.

Thus optional work is bounded by candidate evaluations and portfolio size rather
than machine-dependent timing.  The transposed result is inverse-transposed,
stack-reduced, and admitted only when it is shorter than the retained baseline.

## Replay safety

Both reduced candidates are independently replayed on the original instance.
Replay checks the 100,000-operation bound, rectangle bounds, required even
dimension, every internal wall, and final row-major sortedness.  The mandatory
V4 candidate is asserted valid before optional work.  An invalid transpose
candidate is simply ignored, so it cannot degrade correctness or score.

## Complexity

The baseline has exactly V4's complexity.  Stack reduction and replay are linear
in emitted operations times moved rectangle area.  Optional heuristic work is
`96 * R` candidate evaluations for `R` V4 rectangles, followed by a fixed
`3 * 2` exact-tree portfolio.  Memory remains dominated by V4 distance tables.
