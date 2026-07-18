// Shared implementation for the three V12 beam-width wrappers.
//
// This file is included after agent_jump_tree_v11_thick_delta.rs, inside the
// same module, so it deliberately reuses that solver's private data types and
// helpers.  The wrappers differ only in the const generic BEAM_WIDTH.

impl TreePlan {
    /// Reproduces V10's line-only Clearance policy. V11 replaced that enum
    /// variant with ThickDelta, so the V10 policy is kept here as a separate
    /// method in order to make the first-stage score exactly V10-compatible.
    fn complete_jump_clearance_v12(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
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
                        let Some(op) =
                            jump_operation_with_offset(path[at], first_direction, jump, offset, n)
                        else {
                            continue;
                        };
                        if !jump_window_active(op, &active, n)
                            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                        {
                            continue;
                        }
                        let distance_delta = delta(op, &board, &self.distance, n);
                        let (balanced_clearance, total_clearance) =
                            jump_window_clearance(op, &active, n, vertical, horizontal);
                        let center_penalty =
                            ((2 * offset + 1) as isize - jump as isize).unsigned_abs() as i32;
                        let key = (
                            -(balanced_clearance as i32),
                            -(total_clearance as i32),
                            distance_delta,
                            center_penalty,
                            offset,
                        );
                        if best_window
                            .as_ref()
                            .is_none_or(|(best_key, _)| key < *best_key)
                        {
                            best_window = Some((key, op));
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
        operations
    }
}

/// Exact first-stage completion used by V10: old, V8Edge, Distance and
/// Clearance, including the same compression and replay guards.
fn choose_v10_completion_v12(
    plan: &TreePlan,
    checkpoint: &[usize],
    n: usize,
    prefer_larger: bool,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    let old_raw = plan.complete(checkpoint, n, prefer_larger);
    let old = compress_fallback(&old_raw, n, vertical, horizontal);
    assert!(replay_sorted(checkpoint, &old, n, vertical, horizontal));

    let v8_raw = plan.complete_jump(
        checkpoint,
        n,
        prefer_larger,
        vertical,
        horizontal,
        JumpPolicy::V8Edge,
    );
    let v8 = compress_fallback(&v8_raw, n, vertical, horizontal);
    assert!(replay_sorted(checkpoint, &v8, n, vertical, horizontal));

    let mut best = if v8.len() < old.len() { v8 } else { old };
    let distance_raw = plan.complete_jump(
        checkpoint,
        n,
        prefer_larger,
        vertical,
        horizontal,
        JumpPolicy::Distance,
    );
    let distance = compress_fallback(&distance_raw, n, vertical, horizontal);
    if replay_sorted(checkpoint, &distance, n, vertical, horizontal) && distance.len() < best.len()
    {
        best = distance;
    }

    let clearance_raw =
        plan.complete_jump_clearance_v12(checkpoint, n, prefer_larger, vertical, horizontal);
    let clearance = compress_fallback(&clearance_raw, n, vertical, horizontal);
    if replay_sorted(checkpoint, &clearance, n, vertical, horizontal)
        && clearance.len() < best.len()
    {
        best = clearance;
    }
    best
}

#[derive(Clone, Copy)]
struct BeamCandidateV12 {
    cheap_total: usize,
    root_index: usize,
    order_index: usize,
    checkpoint_index: usize,
}

fn solve_beam_delta_v12<const BEAM_WIDTH: usize>(input: &str) -> String {
    assert!(BEAM_WIDTH > 0);
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

    // Preserve V10's macro-prefix generation exactly. The second-stage beam
    // below is deterministic and performs exactly min(BEAM_WIDTH, states)
    // ThickDelta completions for the checkpoints produced by this loop.
    let start = Instant::now();
    while prefix.len() < SEARCH_MOVE_LIMIT && start.elapsed().as_secs_f64() < SEARCH_SECONDS {
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

    // Stage 1: enumerate the actual 9 * 8 * checkpoints.len() states and
    // score every one with the exact V10 completion portfolio. Retain the
    // global V10 winner unconditionally as the monotonic safety floor.
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

    // Stage 2: only the cheap-score beam receives the expensive ThickDelta
    // completion. Invalid or longer candidates are ignored; the exact V10
    // result above therefore remains a per-instance monotonic guard.
    for state in ranked.iter().take(BEAM_WIDTH) {
        let root = roots[state.root_index];
        let order = &ORDERS[state.order_index];
        let checkpoint = &checkpoints[state.checkpoint_index];
        let prefer_larger = (state.root_index + state.order_index) % 2 == 1;
        let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
        let raw = plan.complete_jump(
            &checkpoint.board,
            n,
            prefer_larger,
            &vertical,
            &horizontal,
            JumpPolicy::ThickDelta,
        );
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

    // A release-build replay guard retains the known-valid V10 result even if
    // a future edit accidentally invalidates the selected ThickDelta output.
    if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
        result = baseline_result;
    }
    assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
    assert!(result.len() <= 100_000);
    render_operations_v12(&result)
}

fn render_operations_v12(operations: &[Operation]) -> String {
    let mut output = String::new();
    for op in operations {
        writeln!(
            output,
            "{} {} {} {} {}",
            op.direction as char, op.r, op.c, op.h, op.w
        )
        .unwrap();
    }
    output
}

pub fn run_v12<const BEAM_WIDTH: usize>() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_beam_delta_v12::<BEAM_WIDTH>(&input));
}
