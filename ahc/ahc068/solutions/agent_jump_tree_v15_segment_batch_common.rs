// A bounded segment-transition pre-round raced against V14's mandatory,
// replay-valid V10/tree floor. This file is included after the V14
// implementation and reuses its private tree-completion and replay helpers
// without changing the shared V14 sources.

const V15_SEGMENT_MACRO_LIMIT: usize = 16;
const V15_SEGMENT_RACER_DEADLINE: Duration = Duration::from_millis(1_440);
const V15_OPTIONAL_WIDTH: usize = 8;
const V15_OPTIONAL_START: Duration = Duration::from_millis(1_520);
const V15_OPTIONAL_DEADLINE: Duration = Duration::from_millis(1_630);

#[derive(Clone)]
struct SegmentLineV15 {
    cells: Vec<usize>,
    horizontal: bool,
}

#[derive(Clone)]
struct SegmentRoundV15 {
    operations: Vec<Operation>,
    total_gain: i32,
    improved_cards: usize,
}

fn horizontal_segments_v15(n: usize, vertical: &[Vec<u8>]) -> (Vec<SegmentLineV15>, Vec<usize>) {
    let mut lines = Vec::new();
    let mut id = vec![usize::MAX; n * n];
    for r in 0..n {
        let mut start = 0;
        for c in 0..n {
            if c + 1 == n || vertical[r][c] == b'1' {
                let index = lines.len();
                let cells: Vec<_> = (start..=c).map(|column| r * n + column).collect();
                for &cell in &cells {
                    id[cell] = index;
                }
                lines.push(SegmentLineV15 {
                    cells,
                    horizontal: true,
                });
                start = c + 1;
            }
        }
    }
    (lines, id)
}

fn vertical_segments_v15(n: usize, horizontal: &[Vec<u8>]) -> (Vec<SegmentLineV15>, Vec<usize>) {
    let mut lines = Vec::new();
    let mut id = vec![usize::MAX; n * n];
    for c in 0..n {
        let mut start = 0;
        for r in 0..n {
            if r + 1 == n || horizontal[r][c] == b'1' {
                let index = lines.len();
                let cells: Vec<_> = (start..=r).map(|row| row * n + c).collect();
                for &cell in &cells {
                    id[cell] = index;
                }
                lines.push(SegmentLineV15 {
                    cells,
                    horizontal: false,
                });
                start = r + 1;
            }
        }
    }
    (lines, id)
}

fn segment_graph_distances_v15(
    horizontal_count: usize,
    vertical_count: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
) -> Vec<u16> {
    let mut graph = vec![Vec::new(); horizontal_count + vertical_count];
    for cell in 0..horizontal_id.len() {
        let h = horizontal_id[cell];
        let v = horizontal_count + vertical_id[cell];
        add_edge(&mut graph, h, v);
    }
    all_distances(&graph)
}

fn segment_distance_to_target_v15(
    node: usize,
    card: usize,
    node_count: usize,
    horizontal_count: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    distances: &[u16],
) -> u16 {
    let target_h = horizontal_id[card];
    let target_v = horizontal_count + vertical_id[card];
    distances[node * node_count + target_h].min(distances[node * node_count + target_v])
}

fn line_operation_v15(line: &SegmentLineV15, start: usize, half: usize, n: usize) -> Operation {
    let first = line.cells[0];
    if line.horizontal {
        Operation {
            direction: b'H',
            r: first / n,
            c: first % n + start,
            h: 1,
            w: 2 * half,
        }
    } else {
        Operation {
            direction: b'V',
            r: first / n + start,
            c: first % n,
            h: 2 * half,
            w: 1,
        }
    }
}

fn segment_macro_score_v15(
    op: Operation,
    board: &[usize],
    horizontal_round: bool,
    horizontal_count: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    distances: &[u16],
    n: usize,
) -> Option<(i32, usize, usize)> {
    let node_count =
        distances.len() / (horizontal_count + vertical_id.iter().copied().max().unwrap_or(0) + 1);
    let mut total_gain = 0i32;
    let mut improved = 0usize;
    let mut score_pair = |from: usize, to: usize| {
        let card = board[from];
        let old_node = if horizontal_round {
            horizontal_count + vertical_id[from]
        } else {
            horizontal_id[from]
        };
        let new_node = if horizontal_round {
            horizontal_count + vertical_id[to]
        } else {
            horizontal_id[to]
        };
        let old_distance = segment_distance_to_target_v15(
            old_node,
            card,
            node_count,
            horizontal_count,
            horizontal_id,
            vertical_id,
            distances,
        );
        let new_distance = segment_distance_to_target_v15(
            new_node,
            card,
            node_count,
            horizontal_count,
            horizontal_id,
            vertical_id,
            distances,
        );
        total_gain += i32::from(old_distance) - i32::from(new_distance);
        if new_node != old_node && new_distance < old_distance {
            improved += 1;
        }
    };

    if op.direction == b'H' {
        for offset in 0..op.w / 2 {
            let left = op.r * n + op.c + offset;
            let right = left + op.w / 2;
            score_pair(left, right);
            score_pair(right, left);
        }
    } else {
        for offset in 0..op.h / 2 {
            let top = (op.r + offset) * n + op.c;
            let bottom = top + (op.h / 2) * n;
            score_pair(top, bottom);
            score_pair(bottom, top);
        }
    }
    (improved >= 2 && total_gain > 0).then_some((total_gain, improved, op.h * op.w))
}

fn build_segment_round_v15(
    lines: &[SegmentLineV15],
    board: &[usize],
    horizontal_round: bool,
    horizontal_count: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    distances: &[u16],
    n: usize,
) -> SegmentRoundV15 {
    let mut selected = Vec::new();
    for line in lines {
        let len = line.cells.len();
        let mut best: Option<((i32, usize, usize), Operation)> = None;
        for start in 0..len {
            for half in 1..=(len - start) / 2 {
                let op = line_operation_v15(line, start, half, n);
                let Some(key) = segment_macro_score_v15(
                    op,
                    board,
                    horizontal_round,
                    horizontal_count,
                    horizontal_id,
                    vertical_id,
                    distances,
                    n,
                ) else {
                    continue;
                };
                if best.as_ref().is_none_or(|(best_key, _)| key > *best_key) {
                    best = Some((key, op));
                }
            }
        }
        if let Some(item) = best {
            selected.push(item);
        }
    }
    selected.sort_by(|a, b| b.0.cmp(&a.0));
    selected.truncate(V15_SEGMENT_MACRO_LIMIT);
    SegmentRoundV15 {
        total_gain: selected.iter().map(|item| item.0 .0).sum(),
        improved_cards: selected.iter().map(|item| item.0 .1).sum(),
        operations: selected.into_iter().map(|item| item.1).collect(),
    }
}

fn replay_prefix_v15(
    initial: &[usize],
    operations: &[Operation],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Option<Vec<usize>> {
    let mut board = initial.to_vec();
    let mut position = vec![0usize; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    for &op in operations {
        if op.r + op.h > n
            || op.c + op.w > n
            || op.h == 0
            || op.w == 0
            || (op.direction == b'H' && op.w % 2 != 0)
            || (op.direction == b'V' && op.h % 2 != 0)
            || (op.direction != b'H' && op.direction != b'V')
            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
        {
            return None;
        }
        apply(op, &mut board, &mut position, n);
    }
    Some(board)
}

fn segment_batch_checkpoint_v15(
    initial: &[usize],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Option<Checkpoint> {
    let (horizontal_lines, horizontal_id) = horizontal_segments_v15(n, vertical);
    let (vertical_lines, vertical_id) = vertical_segments_v15(n, horizontal);
    let segment_distances = segment_graph_distances_v15(
        horizontal_lines.len(),
        vertical_lines.len(),
        &horizontal_id,
        &vertical_id,
    );
    let horizontal_round = build_segment_round_v15(
        &horizontal_lines,
        initial,
        true,
        horizontal_lines.len(),
        &horizontal_id,
        &vertical_id,
        &segment_distances,
        n,
    );
    let vertical_round = build_segment_round_v15(
        &vertical_lines,
        initial,
        false,
        horizontal_lines.len(),
        &horizontal_id,
        &vertical_id,
        &segment_distances,
        n,
    );
    let selected = if (horizontal_round.total_gain, horizontal_round.improved_cards)
        >= (vertical_round.total_gain, vertical_round.improved_cards)
    {
        horizontal_round
    } else {
        vertical_round
    };
    if selected.operations.is_empty() {
        return None;
    }
    let board = replay_prefix_v15(initial, &selected.operations, n, vertical, horizontal)?;
    Some(Checkpoint {
        estimate: usize::MAX,
        board,
        prefix: selected.operations,
    })
}

fn solve_segment_batch_v15(input: &str) -> String {
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
    if wall_count == 0 {
        return solve_fast_k16_v14(input);
    }

    let segment_checkpoint = segment_batch_checkpoint_v15(&initial, n, &vertical, &horizontal);
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
    let baseline_result = baseline_result.expect("a safe exact V10/tree floor exists");
    assert!(replay_sorted(
        &initial,
        &baseline_result,
        n,
        &vertical,
        &horizontal
    ));
    let mut result = baseline_result.clone();

    // The segment prefix is an isolated racer. Only a small fixed tree grid is
    // evaluated, no new expensive completion starts after 1.440 s, and no
    // length-only win is admitted without a complete replay.
    if let Some(checkpoint) = &segment_checkpoint {
        'segment_racer: for (root_index, &root) in roots.iter().take(5).enumerate() {
            for (order_index, order) in ORDERS.iter().take(4).enumerate() {
                if solve_start.elapsed() >= V15_SEGMENT_RACER_DEADLINE {
                    break 'segment_racer;
                }
                let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
                let prefer_larger = (root_index + order_index) % 2 == 1;
                let fallback = choose_v10_completion_v14(
                    &plan,
                    &checkpoint.board,
                    n,
                    prefer_larger,
                    &vertical,
                    &horizontal,
                );
                let total = checkpoint.prefix.len() + fallback.len();
                if total >= result.len() || total > 100_000 {
                    continue;
                }
                let mut complete = checkpoint.prefix.clone();
                complete.extend(fallback);
                if replay_sorted(&initial, &complete, n, &vertical, &horizontal) {
                    result = complete;
                }
            }
        }
    }

    // Eight rather than sixteen ThickDelta completions fund the bounded segment
    // racer. Start/abort limits reserve at least 370 ms for replay and output.
    // V14's completion owns a fixed 1.690 s internal deadline, so shift only
    // the clock passed to it by 60 ms to enforce V15's 1.630 s solve deadline.
    let optional_clock_start = solve_start
        .checked_sub(Duration::from_millis(60))
        .unwrap_or(solve_start);
    for state in ranked.iter().take(V15_OPTIONAL_WIDTH) {
        if solve_start.elapsed() >= V15_OPTIONAL_START {
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
            &optional_clock_start,
        ) else {
            break;
        };
        if solve_start.elapsed() >= V15_OPTIONAL_DEADLINE {
            break;
        }
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

    if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
        result = baseline_result;
    }
    assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
    assert!(result.len() <= 100_000);
    render_operations_v12(&result)
}

pub fn run_v15_segment_batch() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_segment_batch_v15(&input));
}
