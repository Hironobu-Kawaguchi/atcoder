# AHC068 workspace

Contest: [estie Programming Contest 2026 (AtCoder Heuristic Contest 068)](https://atcoder.jp/contests/ahc068)

- Start: 2026-07-18 15:00 JST
- End: 2026-07-18 19:00 JST
- Duration: 4 hours
- Language scaffold: Rust (standard library only)

## Before the contest

- [x] Add the mandatory AHC generative-AI instruction to `AGENTS.md`.
- [x] Prepare a release build, formatter, linter, tests, local I/O, and solution snapshots.
- [ ] Confirm the language/runtime selection on AtCoder.
- [ ] Open the task and download the official local tools after the contest begins.

## Start checklist

1. Read the entire statement, constraints, output validity rules, score formula, and time limit.
2. Fill in `NOTES.md` before coding.
3. Replace `TIME_LIMIT_SEC` and the placeholder parser in `src/main.rs`.
4. Implement the simplest always-valid baseline first.
5. Save the first baseline with `make snapshot NAME=baseline_v001`.
6. Put official sample or generated cases under `in/` and official tools under `tools/`.
7. Validate every output with the official tester before comparing scores.

## Commands

```sh
make test
make check
make build
make run CASE=sample
make snapshot NAME=baseline_v001
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
