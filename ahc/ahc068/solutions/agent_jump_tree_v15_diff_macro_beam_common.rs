// A deliberately small, optional macro beam layered after V14 Fast K16.
// V14 is completed first and is therefore an unconditional quality/safety
// floor. The beam re-optimizes a short suffix using one mutable board,
// involutive apply/undo transitions, incremental Zobrist hashing, and a
// tree-of-operations; no child owns or clones a board.

use std::collections::HashSet as HashSetV15;
use std::time::Duration as DurationV15;

const V15_PREFIX_KEEP: usize = 24;
const V15_POOL_SIZE: usize = 24;
const V15_BEAM_WIDTH: usize = 16;
const V15_BEAM_DEPTH: usize = 6;
const V15_EXPANSION_CAP: usize = 1_536;
const V15_START_LIMIT: DurationV15 = DurationV15::from_millis(1_600);
const V15_BEAM_DEADLINE: DurationV15 = DurationV15::from_millis(1_680);
const V15_COMPLETION_DEADLINE: DurationV15 = DurationV15::from_millis(1_720);

#[derive(Clone, Copy)]
struct MacroNodeV15 {
    parent: usize,
    op: Operation,
    depth: u8,
    energy: i32,
    hash: u64,
}

#[derive(Clone, Copy)]
struct MacroChildV15 {
    parent: usize,
    op: Operation,
    energy: i32,
    hash: u64,
}

fn same_operation_v15(a: Operation, b: Operation) -> bool {
    a.direction == b.direction && a.r == b.r && a.c == b.c && a.h == b.h && a.w == b.w
}

fn splitmix64_v15(mut x: u64) -> u64 {
    x = x.wrapping_add(0x9e37_79b9_7f4a_7c15);
    x = (x ^ (x >> 30)).wrapping_mul(0xbf58_476d_1ce4_e5b9);
    x = (x ^ (x >> 27)).wrapping_mul(0x94d0_49bb_1331_11eb);
    x ^ (x >> 31)
}

fn zobrist_table_v15(size: usize) -> Vec<u64> {
    (0..size * size)
        .map(|index| splitmix64_v15(index as u64 ^ 0x68_15_15_15_15_15_15_15))
        .collect()
}

fn board_hash_v15(board: &[usize], zobrist: &[u64]) -> u64 {
    let size = board.len();
    board
        .iter()
        .enumerate()
        .fold(0, |hash, (cell, &card)| hash ^ zobrist[cell * size + card])
}

fn for_each_swapped_pair_v15(mut op: Operation, n: usize, mut visit: impl FnMut(usize, usize)) {
    if op.direction == b'V' {
        op.h /= 2;
        for i in 0..op.h {
            for j in 0..op.w {
                visit((op.r + i) * n + op.c + j, (op.r + op.h + i) * n + op.c + j);
            }
        }
    } else {
        op.w /= 2;
        for i in 0..op.h {
            for j in 0..op.w {
                visit((op.r + i) * n + op.c + j, (op.r + i) * n + op.c + op.w + j);
            }
        }
    }
}

/// Applying an AHC068 operation twice is the identity. This routine updates
/// both inverse positions and the board hash, so it is also the undo routine.
fn apply_hashed_v15(
    op: Operation,
    board: &mut [usize],
    position: &mut [usize],
    hash: &mut u64,
    zobrist: &[u64],
    n: usize,
) {
    let size = board.len();
    for_each_swapped_pair_v15(op, n, |a, b| {
        let x = board[a];
        let y = board[b];
        *hash ^= zobrist[a * size + x]
            ^ zobrist[b * size + y]
            ^ zobrist[a * size + y]
            ^ zobrist[b * size + x];
        board.swap(a, b);
        position[x] = b;
        position[y] = a;
    });
}

/// Move the single mutable board between two nodes by undoing to their LCA
/// and applying the other branch. Tree depth is intentionally at most six.
fn move_board_v15(
    nodes: &[MacroNodeV15],
    mut from: usize,
    mut to: usize,
    board: &mut [usize],
    position: &mut [usize],
    hash: &mut u64,
    zobrist: &[u64],
    n: usize,
) {
    let mut down = [usize::MAX; V15_BEAM_DEPTH];
    let mut down_len = 0usize;
    while nodes[from].depth > nodes[to].depth {
        apply_hashed_v15(nodes[from].op, board, position, hash, zobrist, n);
        from = nodes[from].parent;
    }
    while nodes[to].depth > nodes[from].depth {
        down[down_len] = to;
        down_len += 1;
        to = nodes[to].parent;
    }
    while from != to {
        apply_hashed_v15(nodes[from].op, board, position, hash, zobrist, n);
        from = nodes[from].parent;
        down[down_len] = to;
        down_len += 1;
        to = nodes[to].parent;
    }
    for index in (0..down_len).rev() {
        let node = down[index];
        apply_hashed_v15(nodes[node].op, board, position, hash, zobrist, n);
    }
}

fn node_operations_v15(nodes: &[MacroNodeV15], mut node: usize) -> Vec<Operation> {
    let mut result = Vec::with_capacity(nodes[node].depth as usize);
    while nodes[node].parent != usize::MAX {
        result.push(nodes[node].op);
        node = nodes[node].parent;
    }
    result.reverse();
    result
}

fn parse_operations_v15(output: &str) -> Vec<Operation> {
    let mut tokens = output.split_whitespace();
    let mut result = Vec::new();
    while let Some(direction) = tokens.next() {
        result.push(Operation {
            direction: direction.as_bytes()[0],
            r: tokens.next().unwrap().parse().unwrap(),
            c: tokens.next().unwrap().parse().unwrap(),
            h: tokens.next().unwrap().parse().unwrap(),
            w: tokens.next().unwrap().parse().unwrap(),
        });
    }
    result
}

fn solve_diff_macro_beam_v15(input: &str) -> String {
    let solve_start = Instant::now();

    // The complete V14 result is materialized before any experimental work.
    let baseline_text = solve_fast_k16_v14(input);
    if solve_start.elapsed() >= V15_START_LIMIT {
        return baseline_text;
    }
    let baseline = parse_operations_v15(&baseline_text);

    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let size = n * n;
    let initial: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
    let vertical: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    if vertical
        .iter()
        .chain(horizontal.iter())
        .all(|row| row.iter().all(|&wall| wall == b'0'))
    {
        return baseline_text;
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
    if solve_start.elapsed() >= V15_BEAM_DEADLINE {
        return baseline_text;
    }
    let keep = V15_PREFIX_KEEP.min(baseline.len());
    let fixed_prefix = &baseline[..keep];
    let mut board = initial.clone();
    let mut position = vec![0usize; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    for &op in fixed_prefix {
        apply(op, &mut board, &mut position, n);
    }

    // The pool is scored once at the re-optimization boundary. Restricting
    // area bounds child work and excludes the adjacent-swap tail this beam is
    // not intended to rediscover.
    let mut scored_pool: Vec<(i32, usize, Operation)> = macro_candidates(n, &vertical, &horizontal)
        .into_iter()
        .filter(|op| (4..=80).contains(&(op.h * op.w)))
        .map(|op| {
            (
                delta(op, &board, &distances, n),
                usize::MAX - op.h * op.w,
                op,
            )
        })
        .collect();
    scored_pool.sort_by_key(|&(value, area_key, _)| (value, area_key));
    scored_pool.truncate(V15_POOL_SIZE);
    let pool: Vec<Operation> = scored_pool.into_iter().map(|(_, _, op)| op).collect();
    if pool.is_empty() || solve_start.elapsed() >= V15_BEAM_DEADLINE {
        return baseline_text;
    }

    let zobrist = zobrist_table_v15(size);
    let mut hash = board_hash_v15(&board, &zobrist);
    let initial_energy = board
        .iter()
        .enumerate()
        .map(|(cell, &card)| i32::from(distances[card * size + cell]))
        .sum();
    let dummy = Operation {
        direction: b'H',
        r: 0,
        c: 0,
        h: 1,
        w: 2,
    };
    let mut nodes = vec![MacroNodeV15 {
        parent: usize::MAX,
        op: dummy,
        depth: 0,
        energy: initial_energy,
        hash,
    }];
    let mut frontier = vec![0usize];
    let mut current = 0usize;
    let mut expansions = 0usize;

    for depth in 0..V15_BEAM_DEPTH {
        if solve_start.elapsed() >= V15_BEAM_DEADLINE || expansions >= V15_EXPANSION_CAP {
            break;
        }
        let mut children = Vec::with_capacity(frontier.len() * pool.len());
        for &parent in &frontier {
            move_board_v15(
                &nodes,
                current,
                parent,
                &mut board,
                &mut position,
                &mut hash,
                &zobrist,
                n,
            );
            current = parent;
            for &op in &pool {
                if expansions >= V15_EXPANSION_CAP || solve_start.elapsed() >= V15_BEAM_DEADLINE {
                    break;
                }
                if nodes[parent].parent != usize::MAX && same_operation_v15(nodes[parent].op, op) {
                    continue;
                }
                let change = delta(op, &board, &distances, n);
                apply_hashed_v15(op, &mut board, &mut position, &mut hash, &zobrist, n);
                children.push(MacroChildV15 {
                    parent,
                    op,
                    energy: nodes[parent].energy + change,
                    hash,
                });
                apply_hashed_v15(op, &mut board, &mut position, &mut hash, &zobrist, n);
                expansions += 1;
            }
        }
        if children.is_empty() {
            break;
        }
        children.sort_by_key(|child| (child.energy, child.hash));
        let mut seen = HashSetV15::with_capacity(children.len());
        frontier.clear();
        for child in children {
            if !seen.insert(child.hash) {
                continue;
            }
            let index = nodes.len();
            nodes.push(MacroNodeV15 {
                parent: child.parent,
                op: child.op,
                depth: depth as u8 + 1,
                energy: child.energy,
                hash: child.hash,
            });
            frontier.push(index);
            if frontier.len() == V15_BEAM_WIDTH {
                break;
            }
        }
    }

    frontier.sort_by_key(|&node| (nodes[node].energy, nodes[node].hash));
    let orders = [[0, 1, 2, 3], [3, 2, 1, 0]];
    let roots = [(n / 2) * n + n / 2, 0, n - 1, (n - 1) * n, n * n - 1];
    let mut result = baseline.clone();

    // Only three beam leaves and at most six tree configurations are priced.
    // Exact completion is intentionally terminal-only, never per child.
    'terminal: for &node in frontier.iter().take(3) {
        move_board_v15(
            &nodes,
            current,
            node,
            &mut board,
            &mut position,
            &mut hash,
            &zobrist,
            n,
        );
        current = node;
        let macro_ops = node_operations_v15(&nodes, node);
        for config in 0..6 {
            if solve_start.elapsed() >= V15_COMPLETION_DEADLINE {
                break 'terminal;
            }
            let root = roots[config % roots.len()];
            let order = &orders[(config / roots.len()) % orders.len()];
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let fallback = choose_v10_completion_v14(
                &plan,
                &board,
                n,
                config % 2 == 1,
                &vertical,
                &horizontal,
            );
            let total = fixed_prefix.len() + macro_ops.len() + fallback.len();
            if total >= result.len() || total > 100_000 {
                continue;
            }
            let mut candidate = Vec::with_capacity(total);
            candidate.extend_from_slice(fixed_prefix);
            candidate.extend_from_slice(&macro_ops);
            candidate.extend(fallback);
            if replay_sorted(&initial, &candidate, n, &vertical, &horizontal) {
                result = candidate;
            }
        }
    }

    // A final whole-sequence replay plus the already validated V14 fallback
    // is the release-build safety guard.
    if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
        result = baseline;
    }
    render_operations_v12(&result)
}

pub fn run_v15_diff_macro_beam() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve_diff_macro_beam_v15(&input));
}
