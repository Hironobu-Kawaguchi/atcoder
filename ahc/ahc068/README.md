# AHC068 workspace

Contest: [estie Programming Contest 2026 (AtCoder Heuristic Contest 068)](https://atcoder.jp/contests/ahc068)

- Start: 2026-07-18 15:00 JST
- End: 2026-07-18 19:00 JST
- Duration: 4 hours
- Language scaffold: Rust (standard library only)

## Before the contest

- [x] Add the mandatory AHC generative-AI instruction to `AGENTS.md`.
- [x] Prepare a release build, formatter, linter, tests, local I/O, and solution snapshots.
- [x] Confirm Rust as the contest language.
- [x] Open the task and download the official local tools after the contest begins.

## Start checklist

1. Read the entire statement, constraints, output validity rules, score formula, and time limit. (done)
2. Fill in `NOTES.md` before coding. (done)
3. Implement three independent candidates under `solutions/`. (done)
4. Compile all candidates without executing them. (done)
5. Run `make evaluate` once on all 100 official inputs.
6. Report the results and stop before any result-driven change, as required by the AHC AI rules.

## Commands

```sh
make test
make check
make build
make run CASE=sample
make snapshot NAME=baseline_v001
make evaluate JOBS=16 TIMEOUT=3.0
```

`make run CASE=sample` reads `in/sample.txt` and writes `out/sample.txt`.

## Four-hour rhythm

- 0:00-0:20 — statement, score, constraints, baseline design
- 0:20-0:50 — valid baseline and official-tool validation
- 0:50-2:30 — measured improvements, one idea per snapshot
- 2:30-3:20 — tune robust parameters on multiple seeds
- 3:20-3:45 — simplify, validate, and prepare final submission
- 3:45-4:00 — final submission buffer; avoid risky rewrites

Record each deliberate comparison in `experiments.csv`. Keep diagnostic output on stderr so stdout remains a valid submission.
