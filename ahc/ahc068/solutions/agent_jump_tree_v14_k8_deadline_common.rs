// Deadline-guarded K=8 ThickDelta portfolio for AHC068.
//
// This file is included after agent_jump_tree_v11_thick_delta.rs and
// agent_jump_tree_v12_beam_delta_common.rs. It reuses V12's exact V10
// completion and rendering helpers, but shortens macro search and makes the
// optional ThickDelta stage safely abortable.

const V14_MACRO_SEARCH_SECONDS: f64 = 0.80;
const V14_OPTIONAL_START_GATE_SECONDS: f64 = 1.56;
const V14_OPTIONAL_SOFT_DEADLINE_SECONDS: f64 = 1.69;
const V14_BEAM_WIDTH: usize = 8;

impl TreePlan {
    /// Reproduces `complete_jump(..., ThickDelta)` unless the process-wide
    /// soft deadline is reached. All mutable state is local, so returning
    /// `None` discards the partial completion without affecting the retained
    /// V10 baseline or any checkpoint.
    fn complete_thick_delta_deadline_v14(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        global_start: &Instant,
    ) -> Option<Vec<Operation>> {
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
            if global_start.elapsed().as_secs_f64() >= V14_OPTIONAL_SOFT_DEADLINE_SECONDS {
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
                if global_start.elapsed().as_secs_f64() >= V14_OPTIONAL_SOFT_DEADLINE_SECONDS {
                    return None;
                }

                let first_direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1;
                while straight < 10 && at + straight + 1 < path.len() {
                    if direction_between(path[at + straight], path[at + straight + 1], n)
                        != first_direction
                    {
                        break;
                    }
                    straight += 1;
                }

                let mut selected = None;
                for jump in (1..=straight).rev() {
                    let mut best_window = None;
                    for offset in 0..jump {
                        // An offset iteration is the largest bounded unit in
                        // ThickDelta (at most ten perpendicular placements).
                        // Checking here makes deadline overshoot small without
                        // putting an Instant call inside every rectangle test.
                        if global_start.elapsed().as_secs_f64()
                            >= V14_OPTIONAL_SOFT_DEADLINE_SECONDS
                        {
                            return None;
                        }
                        let Some(line_op) =
                            jump_operation_with_offset(path[at], first_direction, jump, offset, n)
                        else {
                            continue;
                        };
                        for thickness in 1..=4 {
                            for perpendicular_offset in 0..thickness {
                                let Some(op) = thicken_jump_operation(
                                    line_op,
                                    path[at],
                                    thickness,
                                    perpendicular_offset,
                                    n,
                                ) else {
                                    continue;
                                };
                                if swapped_cell(op, path[at], n) != Some(path[at + jump])
                                    || !jump_window_active(op, &active, n)
                                    || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                                {
                                    continue;
                                }
                                let key = jump_window_key(
                                    JumpPolicy::ThickDelta,
                                    op,
                                    offset,
                                    perpendicular_offset,
                                    jump,
                                    &board,
                                    &self.distance,
                                    &active,
                                    n,
                                    vertical,
                                    horizontal,
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

fn solve_k8_deadline_v14(input: &str) -> String {
    let global_start = Instant::now();
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

    if wall_count == 0 {
        let mut result = deterministic_zero_route(&initial, n);
        if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
            const ZERO_FALLBACK_ORDER: [usize; 4] = [0, 1, 2, 3];
            let center = (n / 2) * n + n / 2;
            let plan = TreePlan::new(n, center, &ZERO_FALLBACK_ORDER, &vertical, &horizontal);
            result = choose_v10_completion_v12(&plan, &initial, n, false, &vertical, &horizontal);
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
        && macro_start.elapsed().as_secs_f64() < V14_MACRO_SEARCH_SECONDS
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

    // Mandatory stage: every state receives the exact replay-guarded V10
    // portfolio. Its global winner is complete before optional work begins.
    let mut ranked = Vec::with_capacity(roots.len() * ORDERS.len() * checkpoints.len());
    let mut baseline_result: Option<Vec<Operation>> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let prefer_larger = (root_index + order_index) % 2 == 1;
            for (checkpoint_index, checkpoint) in checkpoints.iter().enumerate() {
                let fallback = choose_v10_completion_v12(
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
                ranked.push(BeamCandidateV12 {
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

    // Optional stage. The start gate prevents beginning ThickDelta when the
    // mandatory portfolio was already expensive. The inner completion checks
    // the absolute deadline and returns None, never a partial operation list.
    if global_start.elapsed().as_secs_f64() < V14_OPTIONAL_START_GATE_SECONDS {
        for state in ranked.iter().take(V14_BEAM_WIDTH) {
            if global_start.elapsed().as_secs_f64() >= V14_OPTIONAL_SOFT_DEADLINE_SECONDS {
                break;
            }
            let root = roots[state.root_index];
            let order = &ORDERS[state.order_index];
            let checkpoint = &checkpoints[state.checkpoint_index];
            let prefer_larger = (state.root_index + state.order_index) % 2 == 1;
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let Some(raw) = plan.complete_thick_delta_deadline_v14(
                &checkpoint.board,
                n,
                prefer_larger,
                &vertical,
                &horizontal,
                &global_start,
            ) else {
                break;
            };
            // Leave the remaining reserve for compression, replay, rendering,
            // and process teardown instead of accepting a just-finished raw
            // completion after the optional deadline.
            if global_start.elapsed().as_secs_f64() >= V14_OPTIONAL_SOFT_DEADLINE_SECONDS {
                break;
            }
            let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
            if !replay_sorted(&checkpoint.board, &fallback, n, &vertical, &horizontal) {
                continue;
            }
            let total = checkpoint.prefix.len() + fallback.len();
            if total < result.len() && total <= 100_000 {
                let mut complete = checkpoint.prefix.clone();
                complete.extend(fallback);
                if replay_sorted(&initial, &complete, n, &vertical, &horizontal) {
                    result = complete;
                }
            }
        }
    }

    // Final full replay is mandatory. Any unexpected optional-candidate
    // failure restores the independently replayed V10 baseline.
    if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
        result = baseline_result;
    }
    assert!(result.len() <= 100_000);
    render_operations_v12(&result)
}

pub fn run_k8_deadline_v14() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_k8_deadline_v14(&input));
}
