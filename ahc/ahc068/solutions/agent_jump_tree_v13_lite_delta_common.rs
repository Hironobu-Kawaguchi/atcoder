// Capped post-pass shared by the V13 lite-delta wrappers.
//
// This file is included after agent_jump_tree_v11_thick_safe.rs in the same
// module.  V11 ThickSafe is evaluated first and remains the unconditional
// per-instance result.  The post-pass reuses only its winning plan/checkpoint.

const V13_MAX_THICKNESS: usize = 4;
const V13_THICK_EVALUATION_LIMIT: usize = 8_000;
const V13_POSTPASS_START_SECONDS: f64 = 1.55;
const V13_POSTPASS_THICK_STOP_SECONDS: f64 = 1.72;

impl TreePlan {
    /// Completes one selected checkpoint with a cheap ThickDelta variant.
    ///
    /// For each routed straight run, all legal one-line offsets are priced
    /// first and exactly one thin winner is retained.  Only that winner is
    /// widened.  Raw ThickDelta instead widens every offset.  The explicit
    /// evaluation counter and total-time stop bound the optional work; after
    /// either stop, legal thin moves continue until the board is complete.
    fn complete_jump_lite_delta_v13(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        solve_started: &Instant,
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
        let mut thick_evaluations = 0usize;

        while remaining > 1 {
            let mut leaf = usize::MAX;
            let mut best_distance = u16::MAX;
            for candidate in 0..size {
                if !active[candidate] || degree[candidate] != 1 {
                    continue;
                }
                let distance = self.distance[position[candidate] * size + candidate];
                let tie = distance == best_distance
                    && (leaf == usize::MAX
                        || (prefer_larger && candidate > leaf)
                        || (!prefer_larger && candidate < leaf));
                if distance < best_distance || tie {
                    best_distance = distance;
                    leaf = candidate;
                }
            }
            assert_ne!(leaf, usize::MAX);

            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&cell| active[cell]));
            let mut at = 0usize;
            while at + 1 < path.len() {
                let direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1usize;
                while straight < 10 && at + straight + 1 < path.len() {
                    if direction_between(path[at + straight], path[at + straight + 1], n)
                        != direction
                    {
                        break;
                    }
                    straight += 1;
                }

                let mut selected = None;
                for jump in (1..=straight).rev() {
                    // Stage 1: rank every legal one-line offset, without any
                    // thick candidates multiplying this enumeration.
                    let mut best_thin = None;
                    for offset in 0..jump {
                        let Some(op) =
                            jump_operation_with_offset(path[at], direction, jump, offset, n)
                        else {
                            continue;
                        };
                        if !jump_window_active(op, &active, n)
                            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                        {
                            continue;
                        }
                        let key = v13_lite_delta_key(
                            op,
                            offset,
                            0,
                            jump,
                            &board,
                            &self.distance,
                            &active,
                            n,
                            vertical,
                            horizontal,
                        );
                        if best_thin
                            .as_ref()
                            .is_none_or(|(best_key, _, _)| key < *best_key)
                        {
                            best_thin = Some((key, op, offset));
                        }
                    }

                    let Some((mut best_key, thin_op, thin_offset)) = best_thin else {
                        continue;
                    };
                    let mut best_op = thin_op;

                    // Stage 2: widen only the winning thin window.  Checking
                    // the elapsed time changes only whether optional candidates
                    // are considered; the exact thin completion is unaffected.
                    'thickness: for thickness in 2..=V13_MAX_THICKNESS.min(n) {
                        for perpendicular_offset in 0..thickness {
                            if thick_evaluations == V13_THICK_EVALUATION_LIMIT
                                || solve_started.elapsed().as_secs_f64()
                                    >= V13_POSTPASS_THICK_STOP_SECONDS
                            {
                                break 'thickness;
                            }
                            thick_evaluations += 1;
                            let Some(op) = v13_thicken_operation(
                                thin_op,
                                path[at],
                                thickness,
                                perpendicular_offset,
                                n,
                            ) else {
                                continue;
                            };
                            if v13_swapped_cell(op, path[at], n) != Some(path[at + jump])
                                || !jump_window_active(op, &active, n)
                                || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                            {
                                continue;
                            }
                            let key = v13_lite_delta_key(
                                op,
                                thin_offset,
                                perpendicular_offset,
                                jump,
                                &board,
                                &self.distance,
                                &active,
                                n,
                                vertical,
                                horizontal,
                            );
                            if key < best_key {
                                best_key = key;
                                best_op = op;
                            }
                        }
                    }
                    selected = Some((jump, best_op));
                    break;
                }

                let (jump, op) = selected.expect("an adjacent tree edge is a legal jump");
                debug_assert_eq!(board[path[at]], leaf);
                apply(op, &mut board, &mut position, n);
                assert_eq!(
                    position[leaf],
                    path[at + jump],
                    "a lite-delta jump must land the focus card on its tree path"
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

fn v13_thicken_operation(
    thin: Operation,
    focus: usize,
    thickness: usize,
    perpendicular_offset: usize,
    n: usize,
) -> Option<Operation> {
    if thickness == 0 || perpendicular_offset >= thickness {
        return None;
    }
    let (focus_r, focus_c) = (focus / n, focus % n);
    match thin.direction {
        b'H' if thin.r == focus_r && focus_r >= perpendicular_offset => {
            let r = focus_r - perpendicular_offset;
            (r + thickness <= n).then_some(Operation {
                r,
                h: thickness,
                ..thin
            })
        }
        b'V' if thin.c == focus_c && focus_c >= perpendicular_offset => {
            let c = focus_c - perpendicular_offset;
            (c + thickness <= n).then_some(Operation {
                c,
                w: thickness,
                ..thin
            })
        }
        _ => None,
    }
}

fn v13_swapped_cell(op: Operation, cell: usize, n: usize) -> Option<usize> {
    let (r, c) = (cell / n, cell % n);
    if r < op.r || r >= op.r + op.h || c < op.c || c >= op.c + op.w {
        return None;
    }
    if op.direction == b'H' {
        let half = op.w / 2;
        let local = c - op.c;
        Some(if local < half {
            cell + half
        } else {
            cell - half
        })
    } else {
        let half = op.h / 2;
        let local = r - op.r;
        Some(if local < half {
            cell + half * n
        } else {
            cell - half * n
        })
    }
}

/// Raw ThickDelta's objective, evaluated only for the selected thin window:
/// total tree-distance delta first, then moved area and corridor clearance.
fn v13_lite_delta_key(
    op: Operation,
    offset: usize,
    perpendicular_offset: usize,
    jump: usize,
    board: &[usize],
    tree_distances: &[u16],
    active: &[bool],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> (i32, i32, i32, i32, i32, usize, usize) {
    let distance_delta = delta(op, board, tree_distances, n);
    let (balanced_clearance, total_clearance) =
        v13_thick_clearance(op, active, n, vertical, horizontal);
    let center_penalty = ((2 * offset + 1) as isize - jump as isize).unsigned_abs() as i32;
    (
        distance_delta,
        -((op.h * op.w) as i32),
        -(balanced_clearance as i32),
        -(total_clearance as i32),
        center_penalty,
        offset,
        perpendicular_offset,
    )
}

fn v13_thick_clearance(
    op: Operation,
    active: &[bool],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> (usize, usize) {
    let (mut before, mut after) = (0usize, 0usize);
    if op.direction == b'H' {
        let mut c = op.c;
        while c > 0
            && (op.r..op.r + op.h).all(|r| active[r * n + c - 1] && vertical[r][c - 1] == b'0')
        {
            before += 1;
            c -= 1;
        }
        let mut c = op.c + op.w;
        while c < n && (op.r..op.r + op.h).all(|r| active[r * n + c] && vertical[r][c - 1] == b'0')
        {
            after += 1;
            c += 1;
        }
    } else {
        let mut r = op.r;
        while r > 0
            && (op.c..op.c + op.w).all(|c| active[(r - 1) * n + c] && horizontal[r - 1][c] == b'0')
        {
            before += 1;
            r -= 1;
        }
        let mut r = op.r + op.h;
        while r < n
            && (op.c..op.c + op.w).all(|c| active[r * n + c] && horizontal[r - 1][c] == b'0')
        {
            after += 1;
            r += 1;
        }
    }
    (before.min(after), before + after)
}

struct V13Choice {
    prefix: Vec<Operation>,
    fallback: Vec<Operation>,
    checkpoint: Vec<usize>,
    root: usize,
    order: [usize; 4],
    prefer_larger: bool,
}

fn solve_lite_delta_v13<const SWEEP_PREFER_LARGER: bool>(input: &str) -> String {
    let solve_started = Instant::now();
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
        return solve(input);
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
    assert!(distances.iter().all(|&distance| distance != u16::MAX));
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

    // Preserve V11's prefix search exactly.  Its wall-clock cutoff affects only
    // which checkpoints exist, while every saved checkpoint has an exact tree
    // completion.
    let search_started = Instant::now();
    while prefix.len() < SEARCH_MOVE_LIMIT
        && search_started.elapsed().as_secs_f64() < SEARCH_SECONDS
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
    let mut best_choice: Option<V13Choice> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, &order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, &order, &vertical, &horizontal);
            let prefer_larger = (root_index + order_index) % 2 == 1;
            for checkpoint in &checkpoints {
                // This is the complete V11 ThickSafe portfolio: old adjacent,
                // V8, Distance, and ThickSafe.  It is evaluated before any
                // optional lite-delta work and therefore remains the floor.
                let fallback = choose_completion(
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
                if best_choice
                    .as_ref()
                    .is_none_or(|best| total < best.prefix.len() + best.fallback.len())
                {
                    best_choice = Some(V13Choice {
                        prefix: checkpoint.prefix.clone(),
                        fallback,
                        checkpoint: checkpoint.board.clone(),
                        root,
                        order,
                        prefer_larger,
                    });
                }
            }
        }
    }

    let choice = best_choice.expect("V11 ThickSafe always has an exact candidate");
    let mut safe_result = choice.prefix.clone();
    safe_result.extend(choice.fallback.iter().copied());
    assert!(replay_sorted(
        &initial,
        &safe_result,
        n,
        &vertical,
        &horizontal
    ));
    let mut result = safe_result.clone();

    // Slow or adversarial instances keep the already-complete Safe result.
    if solve_started.elapsed().as_secs_f64() < V13_POSTPASS_START_SECONDS {
        let plan = TreePlan::new(n, choice.root, &choice.order, &vertical, &horizontal);
        let mut preferences = [choice.prefer_larger, choice.prefer_larger];
        let preference_count = if SWEEP_PREFER_LARGER {
            preferences[1] = !choice.prefer_larger;
            2
        } else {
            1
        };
        for &prefer_larger in preferences.iter().take(preference_count) {
            if solve_started.elapsed().as_secs_f64() >= V13_POSTPASS_START_SECONDS {
                break;
            }
            let raw = plan.complete_jump_lite_delta_v13(
                &choice.checkpoint,
                n,
                prefer_larger,
                &vertical,
                &horizontal,
                &solve_started,
            );
            let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
            if !replay_sorted(&choice.checkpoint, &fallback, n, &vertical, &horizontal) {
                continue;
            }
            let mut candidate = choice.prefix.clone();
            candidate.extend(fallback);
            if candidate.len() < result.len()
                && candidate.len() <= 100_000
                && replay_sorted(&initial, &candidate, n, &vertical, &horizontal)
            {
                result = candidate;
            }
        }
    }

    // Release-build legality and monotonicity guard.
    if result.len() > safe_result.len()
        || !replay_sorted(&initial, &result, n, &vertical, &horizontal)
    {
        result = safe_result;
    }
    assert!(result.len() <= 100_000);

    let mut output = String::new();
    for op in result {
        writeln!(
            output,
            "{} {} {} {} {}",
            op.direction as char, op.r, op.c, op.h, op.w
        )
        .unwrap();
    }
    output
}

pub fn run_lite_delta_v13<const SWEEP_PREFER_LARGER: bool>() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_lite_delta_v13::<SWEEP_PREFER_LARGER>(&input));
}
