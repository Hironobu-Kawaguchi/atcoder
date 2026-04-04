# AHC063 Experiment Environment

`/Users/hk/atcoder/ahc/ahc063` contains a minimal local workflow around the official `tools`.

## Layout

- `ACTIVE_SOLUTION`: points to the currently active file under `solutions/`
- `Cargo.toml`: solver crate manifest
- `solutions/*.rs`: per-experiment solver sources
- `src/main.rs`: current solver entry point
- `Makefile`: build and evaluation commands
- `scripts/solution_manager.py`: activate, create, sync, and list solutions
- `scripts/check_submission.py`: local submission-compatibility check
- `scripts/run_case.py`: run one case, optionally with official visualization
- `scripts/batch_eval.py`: evaluate many cases with the official scorer
- `scripts/record_experiment.py`: snapshot source, outputs, and scores
- `scripts/annotate_submission.py`: attach AtCoder submission score and time to an experiment
- `scripts/rebuild_index.py`: rebuild `experiments/index.csv` from metadata
- `scripts/rebuild_submission_log.py`: rebuild `SUBMISSIONS.md` from metadata
- `tools/`: official generator and visualizer
- `out/`: solver outputs
- `logs/`: batch evaluation logs

## Commands

Build the solver:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make build
```

List available solver files:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make list-solutions
```

Activate one solver file and sync it into `src/main.rs`:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make use-solution SOLUTION=baseline
```

Create a new solver file from the active one and activate it:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make new-solution SOLUTION=beam_v001
```

Build the official tools:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make tools-build
```

Run a submission-style compatibility check:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make submit-check
```

Run one predefined case:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make run CASE=0000
```

Run one case and generate official visualization:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make vis CASE=0000
```

Batch-evaluate the first 100 official inputs:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make batch LIMIT=100 JOBS=1
```

Record one experiment snapshot:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make record NAME=beam-v001 LIMIT=100 JOBS=1
```

Attach an AtCoder submission result to the latest experiment:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make annotate-submission RESULT=AC SCORE=24447131 TIME_MS=1
```

Attach a result with implementation notes and next ideas:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
python3 scripts/annotate_submission.py \
  --result AC \
  --score 24447131 \
  --exec-time-ms 1 \
  --implementation "Official sample-equivalent zigzag that eats everything." \
  --next-idea "Implement an exact simulator in Rust." \
  --next-idea "Add a short-horizon beam search."
```

Generate additional inputs from `tools/seeds.txt`:

```zsh
cd /Users/hk/atcoder/ahc/ahc063
make gen
```

## Notes

- The solver is a standalone Rust crate and is independent from the official `tools` crate.
- Each experiment should live in its own file under `solutions/`.
- `src/main.rs` is a synchronized submission copy of the currently active solution.
- `solutions/baseline.rs` is currently a sample baseline equivalent to the official zigzag solution.
- `make submit-check` builds `src/main.rs` in a temporary Cargo project named `main` with `cargo build --release --quiet --offline`, matching AtCoder's published Rust build command.
- If you install Rust `1.89.0` locally, `scripts/check_submission.py --toolchain 1.89.0` can be used for a closer version match.
- `make vis` stores HTML next to the output file, for example `out/0000.html`.
- `make batch` writes a CSV log under `logs/`.
- `make record` stores an immutable snapshot under `experiments/<timestamp>-<name>/` with the active solution file, synchronized `src/main.rs`, outputs, scores, summary, and submission-check metadata.
- `experiments/index.csv` now tracks both local metrics and submitted metrics for each experiment.
- `SUBMISSIONS.md` is the human-readable submission journal, including implementation notes and next ideas.
- Only full official-local evaluations are recorded. Partial runs can still use `make batch`, but they are excluded from `experiments/index.csv` and `SUBMISSIONS.md`.
