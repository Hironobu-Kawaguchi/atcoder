# Safe/block exclusive portfolio V8

## Branch selection

The input is scanned once for wall bits before either solver is called.

```text
all wall bits are 0  -> safe_portfolio_v7 only
at least one bit is 1 -> block_compress_v7 only
```

The two solvers are embedded as independent Rust modules.  The dispatcher calls
exactly one public `solve` function; it does not initialize, time, or partially
execute the other module.  Therefore their elapsed-time budgets and search state
cannot interfere.

## Zero-wall branch

The `safe_portfolio_v7` source is retained unchanged.  Its zero-wall route
compares:

- the width-200 column-row-column beam checkpoint;
- the legacy open-mesh route;
- the safe V4 tree candidates.

The branch retains its own complete replay and emergency empty-prefix tree
fallback.

## Wall branch

The `block_compress_v7` source is retained unchanged.  It first constructs and
keeps the original V4 candidate, then considers dependency reordering and block
compression only for the best raw tree tails.  A replacement is accepted only
after independent replay.  Its original V4 fallback, 100,000-operation check,
and final replay assertion remain intact.

## Safety

Both branches independently verify legality and complete sorting using their
original replay routines.  Since dispatch is exclusive, the combined executable
does not concatenate operation streams or pass a mutated board between solvers.
The selected branch alone produces stdout.

## Maintenance note

Constants and solver logic are copied verbatim from
`agent_safe_portfolio_v7.rs` and `agent_block_compress_v7.rs`.  The only module
adaptation is making each existing `solve` entry point public; all routing,
compression, fallback, timing, and replay code is unchanged.
