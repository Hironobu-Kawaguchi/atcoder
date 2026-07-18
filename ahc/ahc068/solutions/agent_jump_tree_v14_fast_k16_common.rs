// V14 keeps V12 K16's mandatory V10 portfolio, but shortens the macro phase,
// validates completion candidates lazily, and makes ThickDelta an optional,
// deadline-aware stage. This file is included after the V11 ThickDelta engine
// and the V12 shared implementation, so it can reuse their private helpers.

use std::time::Duration;

const V14_SEARCH_SECONDS: f64 = 0.80;
const V14_BEAM_WIDTH: usize = 16;
const V14_OPTIONAL_START: Duration = Duration::from_millis(1_600);
const V14_OPTIONAL_DEADLINE: Duration = Duration::from_millis(1_690);

impl TreePlan {
    /// ThickDelta with the exact V11 candidate order and key, but with two
    /// implementation changes:
    ///
    /// - distance deltas for the seven possible perpendicular lines are
    ///   cached and summed, which is exactly equivalent to evaluating the
    ///   whole rectangle because a block exchange acts independently on each
    ///   line;
    /// - the optional completion may abort without affecting the mandatory
    ///   baseline when the solve-wide deadline is reached.
    fn complete_jump_thick_delta_v14(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        solve_start: &Instant,
    ) -> Option<Vec<Operation>> {
        const MAX_THICKNESS: usize = 4;
        const CACHE_RADIUS: usize = MAX_THICKNESS - 1;
        const CACHE_SIZE: usize = 2 * CACHE_RADIUS + 1;

        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0usize; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut remaining = size;
        let mut operations = Vec::new();

        while remaining > 1 {
            if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                return None;
            }

            let mut leaf = usize::MAX;
            let mut best_distance = u16::MAX;
            for candidate in 0..size {
                if !active[candidate] || degree[candidate] != 1 {
                    continue;
                }
                let d = self.distance[position[candidate] * size + candidate];
                let tie = d == best_distance
                    && (leaf == usize::MAX
                        || (prefer_larger && candidate > leaf)
                        || (!prefer_larger && candidate < leaf));
                if d < best_distance || tie {
                    best_distance = d;
                    leaf = candidate;
                }
            }
            assert_ne!(leaf, usize::MAX);

            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&v| active[v]));
            let mut at = 0;
            while at + 1 < path.len() {
                if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                    return None;
                }

                let first_direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1;
                while straight < JumpPolicy::ThickDelta.max_jump() && at + straight + 1 < path.len()
                {
                    if direction_between(path[at + straight], path[at + straight + 1], n)
                        != first_direction
                    {
                        break;
                    }
                    straight += 1;
                }

                let focus = path[at];
                let focus_cross = if first_direction.0 == 0 {
                    focus / n
                } else {
                    focus % n
                };
                let mut selected = None;

                for jump in (1..=straight).rev() {
                    let mut best_window = None;
                    for offset in 0..jump {
                        if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                            return None;
                        }

                        let Some(line_op) =
                            jump_operation_with_offset(focus, first_direction, jump, offset, n)
                        else {
                            continue;
                        };

                        // A thickness <= 4 containing the focus line can only
                        // touch focus_cross-3 .. focus_cross+3. Cache each
                        // single-line delta once for this longitudinal window.
                        let mut line_deltas = [0i32; CACHE_SIZE];
                        for (cache_index, slot) in line_deltas.iter_mut().enumerate() {
                            let relative = cache_index as isize - CACHE_RADIUS as isize;
                            let cross = focus_cross as isize + relative;
                            if !(0..n as isize).contains(&cross) {
                                continue;
                            }
                            let single = if line_op.direction == b'H' {
                                Operation {
                                    r: cross as usize,
                                    h: 1,
                                    ..line_op
                                }
                            } else {
                                Operation {
                                    c: cross as usize,
                                    w: 1,
                                    ..line_op
                                }
                            };
                            *slot = delta(single, &board, &self.distance, n);
                        }

                        for thickness in 1..=MAX_THICKNESS {
                            for perpendicular_offset in 0..thickness {
                                let Some(op) = thicken_jump_operation(
                                    line_op,
                                    focus,
                                    thickness,
                                    perpendicular_offset,
                                    n,
                                ) else {
                                    continue;
                                };
                                if swapped_cell(op, focus, n) != Some(path[at + jump])
                                    || !jump_window_active(op, &active, n)
                                    || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                                {
                                    continue;
                                }

                                let cache_start = CACHE_RADIUS - perpendicular_offset;
                                let distance_delta = line_deltas
                                    [cache_start..cache_start + thickness]
                                    .iter()
                                    .sum::<i32>();
                                let (balanced_clearance, total_clearance) =
                                    jump_window_clearance(op, &active, n, vertical, horizontal);
                                let center_penalty = ((2 * offset + 1) as isize - jump as isize)
                                    .unsigned_abs()
                                    as i32;
                                let key = (
                                    distance_delta,
                                    -((op.h * op.w) as i32),
                                    -(balanced_clearance as i32),
                                    -(total_clearance as i32),
                                    center_penalty,
                                    offset,
                                    perpendicular_offset,
                                );
                                if best_window
                                    .as_ref()
                                    .is_none_or(|(best_key, _)| key < *best_key)
                                {
                                    best_window = Some((key, op));
                                }
                            }
                        }
                    }
                    if let Some((_, op)) = best_window {
                        selected = Some((jump, op));
                        break;
                    }
                }

                let (jump, op) = selected.expect("the adjacent tree edge is a legal jump");
                debug_assert_eq!(board[path[at]], leaf);
                apply(op, &mut board, &mut position, n);
                assert_eq!(
                    position[leaf],
                    path[at + jump],
                    "jump must land the desired card on its tree path"
                );
                operations.push(op);
                at += jump;
            }

            assert_eq!(board[leaf], leaf);
            active[leaf] = false;
            remaining -= 1;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
            degree[leaf] = 0;
        }

        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        Some(operations)
    }
}

/// Builds the exact four V10 completion candidates in the original priority
/// order. A stable length sort preserves the original strict-`<` tie behavior:
/// old, V8Edge, Distance, then Clearance. Only candidates that can actually
/// win are replayed; an invalid shortest candidate falls through safely.
fn choose_v10_completion_v14(
    plan: &TreePlan,
    checkpoint: &[usize],
    n: usize,
    prefer_larger: bool,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    let old_raw = plan.complete(checkpoint, n, prefer_larger);
    let old = compress_fallback(&old_raw, n, vertical, horizontal);

    let v8_raw = plan.complete_jump(
        checkpoint,
        n,
        prefer_larger,
        vertical,
        horizontal,
        JumpPolicy::V8Edge,
    );
    let v8 = compress_fallback(&v8_raw, n, vertical, horizontal);

    let distance_raw = plan.complete_jump(
        checkpoint,
        n,
        prefer_larger,
        vertical,
        horizontal,
        JumpPolicy::Distance,
    );
    let distance = compress_fallback(&distance_raw, n, vertical, horizontal);

    let clearance_raw =
        plan.complete_jump_clearance_v12(checkpoint, n, prefer_larger, vertical, horizontal);
    let clearance = compress_fallback(&clearance_raw, n, vertical, horizontal);

    let mut candidates = [old, v8, distance, clearance];
    candidates.sort_by_key(Vec::len);
    candidates
        .into_iter()
        .find(|candidate| replay_sorted(checkpoint, candidate, n, vertical, horizontal))
        .expect("at least the exact old completion is replay-valid")
}

#[derive(Clone, Copy)]
struct BeamCandidateV14 {
    cheap_total: usize,
    root_index: usize,
    order_index: usize,
    checkpoint_index: usize,
}

fn solve_fast_k16_v14(input: &str) -> String {
    let solve_start = Instant::now();
    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let size = n * n;
    let mut board: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
    let initial = board.clone();
    let vertical: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let wall_count = vertical
        .iter()
        .chain(horizontal.iter())
        .map(|row| row.iter().filter(|&&wall| wall == b'1').count())
        .sum::<usize>();
    let fully_open = wall_count == 0;

    if fully_open {
        let mut result = deterministic_zero_route(&initial, n);
        if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
            const ZERO_FALLBACK_ORDER: [usize; 4] = [0, 1, 2, 3];
            let center = (n / 2) * n + n / 2;
            let plan = TreePlan::new(n, center, &ZERO_FALLBACK_ORDER, &vertical, &horizontal);
            result = choose_v10_completion_v14(&plan, &initial, n, false, &vertical, &horizontal);
        }
        assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
        return render_operations_v12(&result);
    }

    let mut graph = vec![Vec::new(); size];
    for r in 0..n {
        for c in 0..n - 1 {
            if vertical[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, r * n + c + 1);
            }
        }
    }
    for r in 0..n - 1 {
        for c in 0..n {
            if horizontal[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, (r + 1) * n + c);
            }
        }
    }
    let distances = all_distances(&graph);
    assert!(distances.iter().all(|&d| d != u16::MAX));
    let candidates = macro_candidates(n, &vertical, &horizontal);
    const ORDERS: [[usize; 4]; 8] = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 3, 2, 1],
        [3, 2, 1, 0],
        [2, 1, 0, 3],
        [1, 0, 3, 2],
    ];
    let center = (n / 2) * n + n / 2;
    let quick_plan = TreePlan::new(n, center, &ORDERS[0], &vertical, &horizontal);
    let mut position = vec![0usize; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut prefix = Vec::new();
    let mut checkpoints = Vec::new();
    save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);

    let macro_start = Instant::now();
    while prefix.len() < SEARCH_MOVE_LIMIT
        && macro_start.elapsed().as_secs_f64() < V14_SEARCH_SECONDS
    {
        let mut best_delta = 0i32;
        let mut best = None;
        for &op in &candidates {
            let value = delta(op, &board, &distances, n);
            if value < best_delta {
                best_delta = value;
                best = Some(op);
            }
        }
        let Some(op) = best else { break };
        apply(op, &mut board, &mut position, n);
        prefix.push(op);
        if prefix.len() % CHECK_INTERVAL == 0 || best_delta <= -12 {
            save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);
        }
    }
    save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);

    let roots = [
        center,
        0,
        n - 1,
        (n - 1) * n,
        n * n - 1,
        n / 2,
        (n - 1) * n + n / 2,
        (n / 2) * n,
        (n / 2) * n + n - 1,
    ];

    // Mandatory stage: always finish the exact V10 portfolio and retain its
    // global winner before any deadline-controlled ThickDelta work begins.
    let mut ranked = Vec::with_capacity(roots.len() * ORDERS.len() * checkpoints.len());
    let mut baseline_result: Option<Vec<Operation>> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let prefer_larger = (root_index + order_index) % 2 == 1;
            for (checkpoint_index, checkpoint) in checkpoints.iter().enumerate() {
                let fallback = choose_v10_completion_v14(
                    &plan,
                    &checkpoint.board,
                    n,
                    prefer_larger,
                    &vertical,
                    &horizontal,
                );
                let total = checkpoint.prefix.len() + fallback.len();
                if total > 100_000 {
                    continue;
                }
                ranked.push(BeamCandidateV14 {
                    cheap_total: total,
                    root_index,
                    order_index,
                    checkpoint_index,
                });
                if baseline_result
                    .as_ref()
                    .is_none_or(|best| total < best.len())
                {
                    let mut complete = checkpoint.prefix.clone();
                    complete.extend(fallback);
                    baseline_result = Some(complete);
                }
            }
        }
    }

    ranked.sort_by_key(|state| {
        (
            state.cheap_total,
            state.root_index,
            state.order_index,
            state.checkpoint_index,
        )
    });
    let baseline_result = baseline_result.expect("a safe exact V10 candidate exists");
    assert!(replay_sorted(
        &initial,
        &baseline_result,
        n,
        &vertical,
        &horizontal
    ));
    let mut result = baseline_result.clone();

    // Optional stage: no new completion starts at or after 1.60 s. A running
    // completion is itself abortable at 1.69 s, leaving the mandatory baseline
    // and the final replay/output reserve untouched.
    for state in ranked.iter().take(V14_BEAM_WIDTH) {
        if solve_start.elapsed() >= V14_OPTIONAL_START {
            break;
        }
        let root = roots[state.root_index];
        let order = &ORDERS[state.order_index];
        let checkpoint = &checkpoints[state.checkpoint_index];
        let prefer_larger = (state.root_index + state.order_index) % 2 == 1;
        let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
        let Some(raw) = plan.complete_jump_thick_delta_v14(
            &checkpoint.board,
            n,
            prefer_larger,
            &vertical,
            &horizontal,
            &solve_start,
        ) else {
            break;
        };
        let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
        let total = checkpoint.prefix.len() + fallback.len();
        if total >= result.len() || total > 100_000 {
            continue;
        }
        if !replay_sorted(&checkpoint.board, &fallback, n, &vertical, &horizontal) {
            continue;
        }
        let mut complete = checkpoint.prefix.clone();
        complete.extend(fallback);
        if replay_sorted(&initial, &complete, n, &vertical, &horizontal) {
            result = complete;
        }
    }

    // Release-build guard: every printed operation sequence receives a final
    // full replay, with the already-validated mandatory baseline as fallback.
    if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
        result = baseline_result;
    }
    assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
    assert!(result.len() <= 100_000);
    render_operations_v12(&result)
}

pub fn run_v14_fast_k16() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_fast_k16_v14(&input));
}
