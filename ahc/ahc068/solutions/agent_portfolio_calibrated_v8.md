# Portfolio V8: 3x judge-speed calibration variant

## Purpose

This file is a deterministic calibration copy of `agent_portfolio_v6`.  It is
intended to approximate a judge which executes at roughly one third of the
local Apple M4 throughput.  Candidate algorithms, move limits, checkpoints,
tree counts, selection rules, replay, and fallback behavior are unchanged.
Only wall-clock exploration budgets and phase deadlines are reduced.

## Deadline conversion

Every explicit search deadline was divided by three, retaining six decimal
digits where useful:

| Scope | Portfolio V6 | Calibrated V8 |
|---|---:|---:|
| Tree macro search | 0.520 s | 0.173333 s |
| Region room routing | 0.150 s | 0.050000 s |
| Region per-line beam | 0.002500 s | 0.000833 s |
| Region doorway phase | 0.055 s | 0.018333 s |
| Region macro phase | 0.280 s | 0.093333 s |
| Zero-wall residual search | 0.340 s | 0.113333 s |
| Zero-wall line route | 0.680 s | 0.226667 s |
| Outer Tree→Region soft cutoff | 0.820 s | 0.273333 s |

The heavy-wall exception remains unchanged: boards with at least 80 walls are
still given the Region candidate even when the outer soft cutoff has elapsed.
This is a portfolio policy rather than a time budget.

Integer work caps such as macro move limits, beam widths/depths, checkpoint
limits, and the 100,000-output bound are intentionally unchanged.  They remain
secondary safety bounds and changing them would alter the requested algorithm.

## Optional diagnostics

The source contains:

```rust
const DIAGNOSTICS: bool = false;
```

With the default `false`, stderr output is completely disabled.  Setting it to
`true` prints one deterministic-format record after each generated branch,
including branch name, candidate output-operation count, and elapsed
milliseconds.  Diagnostics do not affect stdout or candidate selection.

## Correctness

Reducing a heuristic deadline can only shorten a prefix search; each embedded
solver still appends its exact tree completion.  The outer portfolio continues
to replay every candidate, verifying syntax, bounds, parity, walls, operation
count, and complete identity sorting.  The safe Tree candidate remains the
fallback for walled inputs and for an invalid specialized candidate.

No official or generated contest input was executed while creating this
variant.  Verification is limited to source inspection, `rustfmt`, standalone
optimized compilation, and textual diff checks.
