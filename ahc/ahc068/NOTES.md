# AHC068 notes

## Statement digest

- Input: `N=20`, a `20 x 20` permutation, 20 vertical-wall strings of length 19, and 19 horizontal-wall strings of length 20.
- Required output: zero or more lines `d r c h w`; `d=V` swaps a rectangle's top/bottom halves and `d=H` swaps its left/right halves.
- Validity conditions: the rectangle is inside the board, its split dimension is even, and every adjacency inside it is wall-free.
- Constraints: at most 100,000 operations; all cells are connected through wall-free adjacencies.
- Time limit: 2 seconds.
- Score formula: if `E=0`, `N^2 + round(10^6 log2(10^5/T))`; otherwise `N^2-E`.
- Interactive: no.
- Official local corpus: seeds 0 through 99 (100 inputs).

## Baseline

- Always-valid construction: build a spanning tree of wall-free cell adjacencies, route each leaf's target card through the active tree, and remove the fixed leaf.
- Complexity: at most `400*399/2 = 79,800` adjacent swaps.
- Expected weakness: adjacent-only swaps do not exploit a large rectangle's ability to move many cards in one operation.

## Candidate improvements

1. Exact tree leaf-fixing baseline.
2. Large wall-free rectangle greedy pass followed by exact tree completion.
3. Graph-distance best improvement with adjacent and 2x2 operations followed by exact tree completion.

## Parameters

| Name | Meaning | Initial value | Range |
|---|---|---:|---:|
| greedy operation cap | Maximum large-rectangle prefix | 10,000 | fixed for first evaluation |
| hybrid operation cap | Maximum distance-improvement prefix | 18,000 | fixed for first evaluation |
| hybrid time | Time allotted to improvement prefix | 0.75 s | fixed for first evaluation |

## Submissions

| Time (JST) | Submission | Language | Score | Result | Exec time | Memory | Source |
|---|---|---|---:|---|---:|---:|---|
| 2026-07-18 15:19 | [77555795](https://atcoder.jp/contests/ahc068/submissions/77555795) | Rust 1.89.0 | 549,491,896 | AC | 19 ms | 3,780 KiB | `solutions/agent_greedy_rect.rs` |
| 2026-07-18 15:27 | [77556184](https://atcoder.jp/contests/ahc068/submissions/77556184) | Rust 1.89.0 | 606,834,676 | AC | 238 ms | 3,672 KiB | `solutions/agent_distance_hybrid_v2.rs` |
| 2026-07-18 15:35 | [77556593](https://atcoder.jp/contests/ahc068/submissions/77556593) | Rust 1.89.0 | 660,157,392 | AC | 883 ms | 4,784 KiB | `solutions/agent_distance_hybrid_v3.rs` |
| 2026-07-18 15:54 | [77557083](https://atcoder.jp/contests/ahc068/submissions/77557083) | Rust 1.89.0 | 696,150,197 | AC | 472 ms | 5,628 KiB | `solutions/agent_tree_exact_v4.rs` (local 100-case projection ~698M) |
| 2026-07-18 16:2x | [77558149](https://atcoder.jp/contests/ahc068/submissions/77558149) | Rust 1.89.0 | 699,979,307 | AC | 876 ms | 22,892 KiB | `portfolio_v6` (local projection 718-721M — 2.6% generalization gap, first time budget-dependent behavior shipped) |
| 2026-07-18 16:23 | [77558327](https://atcoder.jp/contests/ahc068/submissions/77558327) | Rust 1.89.0 | 696,150,197 | AC | 845 ms | 22,796 KiB | `agent_hybrid_zero_v6.rs` (exactly tied tree v4; judge-time line beam yielded no score gain) |
| 2026-07-18 16:4x | [77558720](https://atcoder.jp/contests/ahc068/submissions/77558720) | Rust 1.89.0 | 779,633,766 | AC | 738 ms | 6,040 KiB | `jump_tree_v8` (+79.65M / +11.38% vs portfolio_v6; local projection 781.7M, error -0.26% — predictor calibration restored) |
| 2026-07-18 16:5x | [77559540](https://atcoder.jp/contests/ahc068/submissions/77559540) | Rust 1.89.0 | 852,893,124 | AC | 1,604 ms | 6,296 KiB | `agent_jump_tree_v9.rs` (+73.26M / +9.40% vs v8; calibrated prediction 856.1M, error -0.37%; 100W-0L vs v8 locally; area-2 share 41.4%->26.9%, k>=4 jumps 29.3%; judge runtime margin only ~396 ms) |
| 2026-07-18 17:3x | [77560476](https://atcoder.jp/contests/ahc068/submissions/77560476) | Rust 1.89.0 | 858,963,367 | AC | 1,666 ms | 24,420 KiB | `agent_jump_tree_v10_zero.rs` (+6.07M vs v9; zero-wall branch 666.1 ops avg; walled cases identical to v9; prediction 864.5M, ~52% of projected gain realized — hidden set likely has fewer zero-wall cases; judge margin 334 ms) |
| 2026-07-18 18:0x | [77561094](https://atcoder.jp/contests/ahc068/submissions/77561094) | Rust 1.89.0 | 862,408,754 | AC | 1,771 ms | 24,328 KiB | V11 ThickSafe (+3.45M vs v10_zero; prediction 862.63M, error -0.025%; judge factor recalibrated to 1.56x from local max 1,138 ms) |
| 2026-07-18 18:1x | [77561310](https://atcoder.jp/contests/ahc068/submissions/77561310) | Rust 1.89.0 | 0 (TLE) | TLE | >2,000 ms | 24,456 KiB | V11 ThickDelta — TLE consistent with 1.56x factor (~2.33 s implied). Banked best unaffected (best submission counts). Raw ThickDelta excluded from candidates. |
| 2026-07-18 18:25 | [77563125](https://atcoder.jp/contests/ahc068/submissions/77563125) | Rust 1.89.0 | 864,416,510 | AC | 1,678 ms | 24,584 KiB | V14 Fast K16 (+2.01M vs ThickSafe; public-100 local 583,469,344; hard optional-stage deadline removed the old K16 TLE while preserving its public outputs) |
| 2026-07-18 18:38 | (18:38:29) | Rust 1.89.0 | 864,750,492 | AC | 1,699 ms | 24,488 KiB | `agent_jump_tree_v11_thick_delta_capped.rs` (+0.33M vs V14 K16; local 583,960,075 best-of-day; thin-first-then-thicken restructure; judge factor only 1.325x — capped path ran safer than feared) |
| 2026-07-18 18:43 | (18:43:32) | Rust 1.89.0 | 864,829,484 | AC | 1,705 ms | 24,448 KiB | `agent_jump_tree_v14_fast_k32_submit.rs` (+78,992 vs capped ThickDelta — hidden-set variance favored K32 despite lower local total 583,713,826; judge factor 1.304x, deadline guard held) |
| 2026-07-18 18:48 | (18:48:33) | Rust 1.89.0 | 865,243,095 | AC | 1,707 ms | 24,584 KiB | `agent_jump_tree_v15_short_line_pdb_submit.rs` (+413,611 vs K32 — short-line pattern-database line sorts on top of the v14 framework) |
| 2026-07-18 18:5x | [77564643](https://atcoder.jp/contests/ahc068/submissions/77564643) | Rust 1.89.0 | 865,650,389 | AC | 1,815 ms | 24,644 KiB | `agent_jump_tree_v15_short_line_pdb_k32_submit.rs` (K32+PDB, built and smoked in the final 5 minutes; +407,294 vs K16+PDB — the K32 and PDB gains added almost exactly. FINAL BEST) |

## Negative results worth remembering (17:3x JST)

- JumpAware (choosing (k, offset) by total delta-Phi incl. bystanders): 0W-68T-26L vs v9 on 94 completed cases. Greedy immediate delta-Phi biases toward short jumps with good side effects over long jumps with neutral ones; the true currency is ops-to-completion, for which longest-jump-first is the better proxy. Phi/op is emergent, not a good direct target inside this completion architecture.
- Straight-preferring tree: 16W-33L, net ~-0.34M. The v9 tree + longest-jump-first is stronger than architectural intuition suggested.
- v10_leaf variants: better mean ops (1,845-1,898) but 6/100 TLE at 2s — unsubmittable; leaf-order search does not fit the remaining compute budget.

## CRITICAL correction (17:4x JST): the v10_leaf "gain" was survivorship bias

- v10_leaf/leaf_zero means (1,845-1,898) exclude the 6 TLE cases, which are exactly the heaviest boards (seeds 0037/0039/0050/0054/0062/0092, walls 86-129, v10_zero ops 2,633-3,857). On the IDENTICAL 94-case subset v10_zero (1,842.7 mean ops) BEATS v10_leaf_zero (1,845.7). Leaf-order search won 0 completed walled cases (0W-61T-24L). Anytime-restructure EV measured at -0.2M local: DO NOT BUILD.
- The bystander-pairing window tie-break is ALREADY SHIPPED: JumpPolicy::Distance (v9 lines 377-442, 509-545) = longest-jump-first with total tree-distance-delta tie-break, raced vs V8Edge/Clearance per checkpoint. Instrumented measurement: ~1.1 legal windows at max k, only ~3% of selections have residual ties (avg 1.05) — the tree-completion search is SATURATED. No further ops exist in tie-breaking or plan search.
- Never compare mean ops across runs with different valid_case counts.
- Remaining ops are structural only: line routing (666) vs tree completion (1,429 at 1-40 walls / 2,613 at 81+). Only claimable by racing a wall-tolerant line-router candidate behind a per-case min(ops)+replay-validation guard.
- Endgame plan: lock v10_zero as the final build; optional low-confidence (~0.2-0.3) probe = race the zero-wall line router on low-wall boards behind the strict guard; stop all experiments at T-20min.

## SA/beam quantification (17:4x JST)

- One completion replay costs 0.29-0.56 ms local (measured, instrumented v10_zero copy). Leftover budget = 400-2,000 plan evaluations per case — 1-2 orders below where temperature-based SA beats greedy acceptance on a deterministic plateau-heavy integer objective. SA has NO fit in this problem; op-sequence SA structurally impossible (no snapshots, every mutation = full replay).
- The correct "SA slot" filler: ILS hill-climb over (root x all-400-cells, order x all-24-perms, prefer_larger bit, checkpoint) with accept-equal sideways, budgeted by a deterministic completion counter, per-bucket caps (~400 heavy / ~1,200 light). ~25 min build, +0.5-1.5M, near-zero risk. Note prefer_larger is currently welded to (root+order)%2 — sweep it independently.
- v10_zero endgame data (12-seed replay): the pure area-2 tail NO LONGER EXISTS (0-4 ops); last-30-cards phase costs mean 64 ops (2.13/card); residual is scattered across full row/column bands (full-board state mandatory for any endgame solver).
- Endgame tail-replacement beam (misplaced<=30, fixed 5,000 expansions ~80-120ms judge, moves = adjacent + 1x2k jumps from misplaced cards, eval = ops + 0.55*axes_off + 0.15*misplaced, strict never-worse guard): +1.0-1.7M conservative. Build only if >=45 min remain after ILS validates.
- Construction-level plan beam (W=B=4, eval = ops + remaining_path/3.0, NEVER delta-Phi): highest ceiling (+2.0-3.3M) but cannot be built AND validated in remaining time — SKIP.
- One hidden-case TLE = -5.7M, erasing any gain above; no submission without full 100-case rerun at 0.66s local-equivalent budgets.

## Predictor calibration failure (16:30 JST)

| Submission | Local projection | Actual | Relative error |
|---|---:|---:|---:|
| distance hybrid v3 | 663.2M | 660.2M | -0.45% |
| tree exact v4 | ~698M | 696.2M | -0.3% |
| portfolio v6 | 718-721M | 700.0M | about -2.6% |

- The first large systematic prediction error appeared when the submitted binary began choosing among pipelines under wall-clock deadlines. On the slower judge, fewer pipelines or shallower searches can finish than on the M4 Max, so the local per-case minimum is not the same algorithmic behavior as the submitted binary.
- Treat this as a broken predictor, not sampling noise alone. Before trusting another time-dependent portfolio, rerun its official 100-case evaluation with local time budgets scaled to about one third (2 s judge ~= 0.66 s local-equivalent hypothesis).
- Preferred permanent repair: replace wall-clock decisions with fixed work counts (iterations, candidate evaluations, beam expansions). If timing remains necessary, calibrate once at startup with a small benchmark and scale all budgets consistently.
- `hybrid_zero_v6` tying v4 exactly despite strong public zero-wall gains is additional evidence that judge-speed-dependent beam completion/selection is unreliable.

## Remaining-contest operating principles

1. Restore predictor calibration before using local score gains as a submission criterion.
2. Stop expanding selectors and portfolios. Spend effort on the generator for walled cases, especially the adjacent-swap tail.
3. Preserve the current 699,979,307-point submission as the floor. Submit only when the calibrated local result wins clearly, the validator is 100/100, and the measured runtime has roughly 3x safety margin.
4. Target final experimental submission by 18:40 JST; freeze new changes after that point.
5. Prefer deterministic work budgets and monotone guards that keep the complete v4 candidate and select a new candidate only when it is independently replay-valid and shorter.

## Immediate implementation order

1. Calibrate `portfolio_v6` with approximately one-third wall-clock budgets and check whether its 100-case score approaches 467M (x1.5 ~= 700M).
2. Build jump-compressed tree completion: generate both legacy and jump completions per checkpoint, explicitly require every cell in the full `2k` window to remain active, and choose only the shorter replay-valid candidate.
3. Ensure the fallback compressor passes through non-area-2 operations.
4. Add consecutive identical-operation cancellation; each operation is an involution.
5. Consider transposed-instance diversification only after deterministic calibration and jump compression are stable.

## Calibration and jump-completion result (16:3x JST)

Official 100-case evaluation, parallelism 8, 2.0 s process timeout:

| Candidate | Total score | Mean operations | Max local time | Exact |
|---|---:|---:|---:|---:|
| tree exact v4 | 465,482,389 | 4,316.80 | 475 ms | 100/100 |
| portfolio v6 | 480,109,200 | 4,058.59 | 989 ms | 100/100 |
| portfolio calibrated v8 (deadlines / 3) | 469,518,076 | 4,172.95 | 757 ms | 100/100 |
| deterministic/transposed v8 | 465,599,716 | 4,315.29 | 616 ms | 100/100 |
| jump tree v8 | **521,134,370** | **2,839.12** | 662 ms | 100/100 |

- Calibration hypothesis confirmed: `469.518M * 1.5 = 704.277M`, much closer to the actual portfolio submission's `699.979M` than the unscaled local projection (`~720M`). Use the one-third deadline profile for predicting time-dependent binaries.
- Jump completion beats v4 on all 100 cases, with no ties or losses: +55,651,981 local score (+11.96%), 147,768 fewer operations total, and 34.23% fewer operations on average.
- Mean operation counts by wall bucket, v4 -> jump: zero `1892.8 -> 1752.3`, 1-40 `2979.1 -> 2008.0`, 41-80 `4023.2 -> 2684.6`, 81+ `6232.6 -> 3862.8`. The gain grows with wall complexity, matching the score-mass diagnosis.
- `jump_tree_v8` preserves the legacy completion and selects jump output only after legality and full-sort replay, so the observed improvement is monotone on the public corpus. No post-evaluation solution changes were made.

## Top-tier strategy analysis (16:00 JST)

- Measured v3 profile (100 official seeds, parallelism 8): T_geomean 4,669; 89.2% of all ops are area-2 adjacent swaps; the last 30% of every output is 100% adjacent swaps (tree completion). Phi-reduction ~1.1/op vs winner-grade ~5/op.
- Recommended structure (3 of 4 independent designs converged): 3-phase column/row/column permutation routing. Phase A: permute within each column (staging rows via 20x bipartite matching / edge coloring). Phase B: permute within each row to reach target column. Phase C: permute within each column to reach target row. Each of the 60 line sorts uses block-swap ops `H r c 1 2k` / `V r c 2k 1` solved by beam search (verified in simulation: mean 12.25 ops/line, max 14, width 200, heuristic = breakpoints*100 + displacement).
- Expected T_geomean ~1,250-1,500 => ~900-930M. Wall-infeasible cards deferred as wildcards, fixed by existing tree completion (E=0 guaranteed).
- Critical implementation notes: beam-state dedup needs u128 (100 bits), NOT u64; replay self-verifier before printing (no system test => an invalid op is unrecoverable); judge is ~3x slower than local M4 Max; measure locally at parallelism 8.

## Wall-bucket score-mass analysis (16:25 JST)

- Ensemble (per-case min of v4/greedy_v5/region_v5) verified: 487,751,952 local; ens5 over all five is IDENTICAL (tree_v5/line_v5 never strictly win a case).
- Score mass is in walled buckets: 41-80 walls (n=44, ens geomean T 3,792) and 81+ (n=30, T 5,637). Bringing both to T=2000 is worth ~+128M projected; wall-free bucket (666 ops) has NO remaining positive mass — stop investing there.
- v4 adjacent-swap mass: 88.5% of all ops (381,854/431,680), serial chains mean length 2.98; measured compression model: exact 2x tail compression = +123.2M projected, 3x = +187.4M.
- Top recommendation: jump-compressed tree completion (straight-run block swaps in TreePlan::complete, dual-completion min(raw,jump) guard => per-case never worse). Audited EV +40-75M, ~60-75 min build. Gotchas: explicit active[] check on window cells beyond the landing point (fixed-cell corruption otherwise); compress_fallback debug_assert(h*w==2) must pass through non-area-2 ops; k<=2 cap variant as low-risk fallback.
- Cheap laterals: transposed-instance portfolio (~25 lines, +5-15M, zero risk); consecutive-identical-op cancellation (involution, provably safe); time-boxed RNG-perturbed restarts of v4's selection loop.
- Skip in this window: full wall-aware 3-leg matching + R-C-R residual rebuild of greedy_v5 (real build 2.5-3h, EV ~+30-60M at ~40% success); trimmed matching+wildcard version only as stretch.

## Retry audit (18:05 JST)

- ThickDelta quality confirmed real: 583,779,848 local vs ThickSafe 582,268,861 (+1.51M, 70W-18L), overhead mean +124ms / max +359ms. TLE was budget-only. Work-capped version (thin-first-then-thicken restructure of v11_thick_delta.rs lines 396-456, deterministic counters, local max <=1,138ms gate) estimated ~583.74M local — beats beam K16 (+267K) and edges K32 (+22K). Build as the beam-TLE hedge.
- Beam rung timings are marginal: K16 1,153ms local x1.63 = ~1,879ms; K32 1,181ms x1.63 = ~1,925ms (comfort line 1,855ms). Ladder cheapest-first is correct; each TLE costs only a slot.
- Straight tree: the 16W-33L test was confounded (v10_straight REPLACED the 4 mirrored ORDERS families). True additive residual vs ThickSafe: only 8 wins / +0.23M scaled, mostly 81+ walls — parked unless everything else lands early.
- prefer_larger still welded at thick_safe.rs line 1516 — genuinely untested freedom; 5-10 min de-weld funded by dropping the 4 edge-midpoint roots (frees 44% of walled tail). Decide by one local run.
- Consecutive-op cancellation: 3-min grep diagnostic on existing outputs first; build only on a hit.
- Stay dead: uncapped ThickDelta, line routing on walls, segment CRC/multileg, JumpAware, leaf-order search, transposed portfolio (no compute funding), anything raising SEARCH_SECONDS.

## Past-AHC research verdict (18:18 JST)

- Nothing displaces the queued plan (K16/K32 ladder + capped ThickDelta + prefer_larger de-weld). Every "implementable now" research idea fails either the zero-remaining-score-mass filter (zero-wall beam tweaks) or the no-compute-funding filter (extra racers at the 1,855ms ceiling).
- Theory validation: Christie's block-interchange bound (n+1-c)/2 gives ~197 unconstrained floor for random 400-perms; leader's ~890 geomean is near the constrained optimum — today's gap was constant-factor, not structural. 3-phase RCR routing is provably the right zero-wall structure; longest-jump-first block compression is the correct per-line primitive (each op kills ~k^2 inversions).

## Post-contest lessons (for the next grid/op-count AHC)

1. Day-1 lower-bound calibration (cycle-count oracle (len+1-c)/2, O(n)) decides early whether to chase structure or constants.
2. Build every hard-TL beam as Chokudai search + Zobrist dedup (u128 when state >64 bits) + tree-of-ops storage: 10-100x effective width.
3. Endgame IDA* (optionally bidirectional — ops here are involutions) once <=8-10 items misplaced; design op enumeration + wall legality as a reusable hook from day 1.
4. Involution portfolio (solve inverse instance, reverse op list) is a free decorrelated racer — but budget compute for it structurally, not as a late add.
5. Exact-T destroy-and-rebuild of op-sequence windows (accept iff final T drops) needs cheap snapshot-replay — another day-1 hook. Differs from dead delta-Phi proxies because acceptance is exact.
6. Potential shaping: flat Manhattan potentials stall beams; add structural terms (disjoint 2-cycle bonus etc.).
7. High-context problems favor greedy+portfolio+racing over SA (validated); score-mass-by-bucket tracking from the first submission was the single most valuable decision filter today.

## Post-contest: writer solution analysis (wata_orz, submission 77554960, 1,059,231,525 = T_geomean ~750)

Source: https://atcoder.jp/contests/ahc068/submissions/77554960 (25KB Rust, max 1,438ms, submitted pre-contest 14:28)

Algorithm — "FlexRect + retroactive op riding":
1. Fix cards ONE at a time. Order = BFS from the board center over the wall graph, REVERSED — far cells fixed first, active region shrinks toward the center.
2. Every emitted op is stored not as a concrete rectangle but as a FlexRect: a FAMILY of legal rectangles (slide interval x perpendicular-extent interval) that all act IDENTICALLY on already-fixed cards. freedom_score = number of remaining concrete choices. Commitment is delayed to the very end (representative() picks one member at output time).
3. To route the next card, run a lexicographic 0-1 BFS over states (cell q, timeline index t): (a) RIDE an existing op by specializing its family so it carries the card k cells (cost = freedom lost, low 32 bits); (b) stay put by restricting the family to exclude the card (also just freedom loss); (c) INSERT a new op at time t (cost 1<<32, dominant term). Minimizes (#new ops, freedom loss).
4. New ops only need clearance from FIXED cards — unfixed cards are freely displaced. After 1.9s, "hurry" mode stops inserting mid-timeline ops.

Why it reaches ~750: op SHARING. ~400 cards x ~4-5 moves each ~= 1,700+ card-moves realized in ~750 ops (~2.3 moves/op). Our jump tree appends ops serving mostly one card each (T~1,830); wata makes sharing the primary objective and uses AMBIGUITY (uncommitted families) as the mechanism. Our jump compression was a first-order shadow of this (bystanders rode for free but unpriced and unplanned).

Meta-detail worth stealing: his get_time() multiplies elapsed by 0.9 under a "local" feature flag — judge/local speed calibration baked into the library. The exact lesson we re-derived the hard way at 16:30.

Final standings context: winner PrussianBlue 1,046.66M (T~794); writer beats the field. Our final: 865,650,389 (T~1,830), 341st.

## Submission checklist

- [ ] Release build succeeds.
- [ ] Output passes the official validator on all checked cases.
- [ ] No debug text is written to stdout.
- [ ] Time limit includes a safety margin.
- [ ] Fixed seed or seed policy is intentional.
- [ ] The submitted source matches the recorded snapshot.
