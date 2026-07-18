use std::collections::VecDeque;
use std::io::{self, Read};
use std::time::Instant;

const BEAM_END_SEC: f64 = 1.18;
const SEARCH_END_SEC: f64 = 1.72;
const PREFIX_LIMIT: usize = 12_000;
const BEAM_WIDTH: usize = 8;
const BRANCH_WIDTH: usize = 3;
const SAMPLE_SIZE: usize = 1_400;
const ROLLOUT_WIDTH: usize = 18;

struct Scanner<'a>(std::str::SplitWhitespace<'a>);

impl<'a> Scanner<'a> {
    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.0.next().unwrap().parse().unwrap()
    }
}

#[derive(Clone, Copy)]
struct Operation {
    d: char,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn add_edge(graph: &mut [Vec<usize>], a: usize, b: usize) {
    graph[a].push(b);
    graph[b].push(a);
}

fn swap_cells(a: usize, b: usize, board: &mut [usize], position: &mut [usize]) {
    let x = board[a];
    let y = board[b];
    board.swap(a, b);
    position[x] = b;
    position[y] = a;
}

fn apply(op: Operation, board: &mut [usize], position: &mut [usize], n: usize) {
    if op.d == 'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                swap_cells(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                    board,
                    position,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                swap_cells(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                    board,
                    position,
                );
            }
        }
    }
}

fn energy_delta(op: Operation, board: &[usize], distance: &[Vec<i32>], n: usize) -> i32 {
    let mut result = 0;
    if op.d == 'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                let a = (op.r + i) * n + op.c + j;
                let b = (op.r + op.h / 2 + i) * n + op.c + j;
                let x = board[a];
                let y = board[b];
                result += distance[b][x] + distance[a][y] - distance[a][x] - distance[b][y];
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                let a = (op.r + i) * n + op.c + j;
                let b = (op.r + i) * n + op.c + op.w / 2 + j;
                let x = board[a];
                let y = board[b];
                result += distance[b][x] + distance[a][y] - distance[a][x] - distance[b][y];
            }
        }
    }
    result
}

fn all_pairs_distance(graph: &[Vec<usize>]) -> Vec<Vec<i32>> {
    let size = graph.len();
    let inf = i32::MAX / 4;
    let mut distance = vec![vec![inf; size]; size];
    for source in 0..size {
        let mut queue = VecDeque::from([source]);
        distance[source][source] = 0;
        while let Some(v) = queue.pop_front() {
            for &to in &graph[v] {
                if distance[source][to] == inf {
                    distance[source][to] = distance[source][v] + 1;
                    queue.push_back(to);
                }
            }
        }
    }
    distance
}

fn rectangle_is_open(
    r: usize,
    c: usize,
    h: usize,
    w: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> bool {
    for i in r..r + h {
        for j in c..c + w.saturating_sub(1) {
            if vertical[i][j] == b'1' {
                return false;
            }
        }
    }
    for i in r..r + h.saturating_sub(1) {
        for j in c..c + w {
            if horizontal[i][j] == b'1' {
                return false;
            }
        }
    }
    true
}

fn make_candidates(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Operation> {
    let mut result = Vec::new();
    let side = n;
    for h in 1..=side {
        for w in 1..=side {
            if h * w == 1 || (h % 2 == 1 && w % 2 == 1) {
                continue;
            }
            for r in 0..=n - h {
                for c in 0..=n - w {
                    if !rectangle_is_open(r, c, h, w, vertical, horizontal) {
                        continue;
                    }
                    if h % 2 == 0 {
                        result.push(Operation { d: 'V', r, c, h, w });
                    }
                    if w % 2 == 0 {
                        result.push(Operation { d: 'H', r, c, h, w });
                    }
                }
            }
        }
    }
    result
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        Operation {
            d: 'H',
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        Operation {
            d: 'V',
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
}

struct TreePlan {
    tree: Vec<Vec<usize>>,
    components: Vec<Vec<usize>>,
    tree_distance: Vec<Vec<u16>>,
}

impl TreePlan {
    fn new(graph: &[Vec<usize>], preferred_root: usize, rotation: usize) -> Self {
        let size = graph.len();
        let mut tree = vec![Vec::new(); size];
        let mut components = Vec::new();
        let mut seen = vec![false; size];
        let roots =
            std::iter::once(preferred_root).chain((0..size).filter(|&v| v != preferred_root));
        for root in roots {
            if seen[root] {
                continue;
            }
            seen[root] = true;
            let mut component = Vec::new();
            let mut queue = VecDeque::from([root]);
            while let Some(v) = queue.pop_front() {
                component.push(v);
                let degree = graph[v].len();
                for k in 0..degree {
                    let to = graph[v][(k + rotation) % degree];
                    if !seen[to] {
                        seen[to] = true;
                        add_edge(&mut tree, v, to);
                        queue.push_back(to);
                    }
                }
            }
            components.push(component);
        }

        let mut tree_distance = vec![vec![u16::MAX; size]; size];
        for source in 0..size {
            tree_distance[source][source] = 0;
            let mut queue = VecDeque::from([source]);
            while let Some(v) = queue.pop_front() {
                for &to in &tree[v] {
                    if tree_distance[source][to] == u16::MAX {
                        tree_distance[source][to] = tree_distance[source][v] + 1;
                        queue.push_back(to);
                    }
                }
            }
        }
        Self {
            tree,
            components,
            tree_distance,
        }
    }

    fn path(&self, start: usize, goal: usize, active: &[bool]) -> Vec<usize> {
        let mut parent = vec![usize::MAX; self.tree.len()];
        let mut queue = VecDeque::from([start]);
        parent[start] = start;
        while let Some(v) = queue.pop_front() {
            if v == goal {
                break;
            }
            for &to in &self.tree[v] {
                if active[to] && parent[to] == usize::MAX {
                    parent[to] = v;
                    queue.push_back(to);
                }
            }
        }
        assert_ne!(parent[goal], usize::MAX);
        let mut path = vec![goal];
        while *path.last().unwrap() != start {
            path.push(parent[*path.last().unwrap()]);
        }
        path.reverse();
        path
    }

    fn run(
        &self,
        board: &mut [usize],
        position: &mut [usize],
        n: usize,
        mut output: Option<&mut Vec<Operation>>,
    ) -> usize {
        let mut count = 0;
        let mut active = vec![true; board.len()];
        for component in &self.components {
            let mut remaining = component.len();
            while remaining > 1 {
                // Among all removable leaves, fix the one whose desired card is
                // currently closest in this tree.  Tree distances remain valid
                // because deleting leaves preserves paths between active nodes.
                let leaf = component
                    .iter()
                    .copied()
                    .filter(|&v| {
                        active[v] && self.tree[v].iter().filter(|&&to| active[to]).count() <= 1
                    })
                    .min_by_key(|&v| self.tree_distance[position[v]][v])
                    .unwrap();
                let path = self.path(position[leaf], leaf, &active);
                for edge in path.windows(2) {
                    let op = adjacent_operation(edge[0], edge[1], n);
                    apply(op, board, position, n);
                    if let Some(ref mut operations) = output {
                        operations.push(op);
                    }
                    count += 1;
                }
                debug_assert_eq!(board[leaf], leaf);
                active[leaf] = false;
                remaining -= 1;
            }
        }
        count
    }

    fn count(&self, board: &[usize], position: &[usize], n: usize) -> usize {
        let mut b = board.to_vec();
        let mut p = position.to_vec();
        self.run(&mut b, &mut p, n, None)
    }
}

fn best_fallback(
    plans: &[TreePlan],
    board: &[usize],
    position: &[usize],
    n: usize,
) -> (usize, usize) {
    plans
        .iter()
        .enumerate()
        .map(|(index, plan)| (plan.count(board, position, n), index))
        .min()
        .unwrap()
}

#[derive(Clone)]
struct SearchState {
    board: Vec<usize>,
    position: Vec<usize>,
    prefix: Vec<Operation>,
    energy: i32,
    fixed: i32,
}

struct XorShift64(u64);

impl XorShift64 {
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x << 7;
        x ^= x >> 9;
        self.0 = x;
        x
    }
}

fn exact_count(board: &[usize]) -> i32 {
    board
        .iter()
        .enumerate()
        .filter(|&(cell, &card)| cell == card)
        .count() as i32
}

fn match_delta(op: Operation, board: &[usize], n: usize) -> i32 {
    let mut result = 0;
    let mut account = |a: usize, b: usize| {
        let x = board[a];
        let y = board[b];
        result += (y == a) as i32 + (x == b) as i32 - (x == a) as i32 - (y == b) as i32;
    };
    if op.d == 'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                account(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                account(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                );
            }
        }
    }
    result
}

fn alignment_delta(op: Operation, board: &[usize], n: usize) -> i32 {
    let aligned = |cell: usize, card: usize| {
        ((cell / n == card / n) as i32) + ((cell % n == card % n) as i32)
    };
    let mut result = 0;
    let mut account = |a: usize, b: usize| {
        let x = board[a];
        let y = board[b];
        result += aligned(a, y) + aligned(b, x) - aligned(a, x) - aligned(b, y);
    };
    if op.d == 'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                account(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                account(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                );
            }
        }
    }
    result
}

fn board_hash(board: &[usize]) -> u64 {
    let mut hash = 0xcbf29ce484222325_u64;
    for (cell, &card) in board.iter().enumerate() {
        hash ^= (card as u64).wrapping_add((cell as u64) << 32);
        hash = hash.wrapping_mul(0x100000001b3);
    }
    hash
}

fn sampled_proposals(
    state: &SearchState,
    candidates: &[Operation],
    distance: &[Vec<i32>],
    n: usize,
    rng: &mut XorShift64,
    lambda: i32,
    width: usize,
) -> Vec<(i64, i32, i32, Operation)> {
    let take = SAMPLE_SIZE.min(candidates.len());
    let mut proposals = Vec::with_capacity(take + 2_000);
    // Exhaustively consider 1-D block swaps on every passable row/column
    // segment.  These are the row/column routing primitives; random sampling is
    // reserved for the much larger family of two-dimensional rectangles.
    for &op in candidates.iter().filter(|op| op.h == 1 || op.w == 1) {
        let de = energy_delta(op, &state.board, distance, n);
        let dm = match_delta(op, &state.board, n);
        let da = alignment_delta(op, &state.board, n);
        let key = de as i64 * 16 - dm as i64 * lambda as i64 - da as i64 * (8 + lambda as i64 / 2);
        proposals.push((key, de, dm, op));
    }
    // A changing contiguous slice gives deterministic coverage of all macros;
    // random samples prevent consecutive beam states from seeing the same set.
    let start = rng.next() as usize % candidates.len();
    for k in 0..take {
        let index = if k < take / 3 {
            (start + k) % candidates.len()
        } else {
            rng.next() as usize % candidates.len()
        };
        let op = candidates[index];
        let de = energy_delta(op, &state.board, distance, n);
        let dm = match_delta(op, &state.board, n);
        let da = alignment_delta(op, &state.board, n);
        let key = de as i64 * 16 - dm as i64 * lambda as i64 - da as i64 * (8 + lambda as i64 / 2);
        proposals.push((key, de, dm, op));
    }
    proposals.sort_unstable_by_key(|&(key, _, _, _)| key);
    proposals.truncate(width.min(proposals.len()));
    proposals
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let size = n * n;
    let mut board = (0..size).map(|_| scanner.next()).collect::<Vec<usize>>();
    let vertical = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect::<Vec<_>>();
    let horizontal = (0..n - 1)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect::<Vec<_>>();

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

    let distance = all_pairs_distance(&graph);
    let candidates = make_candidates(n, &vertical, &horizontal);
    let roots = [0, n - 1, size / 2 + n / 2, size - n, size - 1];
    let plans = roots
        .into_iter()
        .enumerate()
        .map(|(rotation, root)| TreePlan::new(&graph, root, rotation))
        .collect::<Vec<_>>();

    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let start = Instant::now();

    let initial_energy = board
        .iter()
        .enumerate()
        .map(|(cell, &card)| distance[cell][card])
        .sum::<i32>();
    let initial_fixed = exact_count(&board);
    let mut best_board = board.clone();
    let mut best_position = position.clone();
    let mut best_prefix = Vec::new();
    let (mut best_total, _) = best_fallback(&plans, &board, &position, n);
    let mut rng = XorShift64(0x68_2026_0718);

    // Phase 1: a diverse macro beam.  Different branches reward exact matches
    // by different amounts, so a temporary distance sacrifice can survive when
    // a large rectangle places many cards at once.
    let mut beam = vec![SearchState {
        board: board.clone(),
        position: position.clone(),
        prefix: Vec::new(),
        energy: initial_energy,
        fixed: initial_fixed,
    }];
    let mut depth = 0;
    while start.elapsed().as_secs_f64() < BEAM_END_SEC
        && beam.iter().any(|state| state.prefix.len() < PREFIX_LIMIT)
    {
        let mut expanded = Vec::new();
        for (state_index, state) in beam.iter().enumerate() {
            let lambda = [0, 24, 72][state_index % 3];
            for (_, de, dm, op) in sampled_proposals(
                state,
                &candidates,
                &distance,
                n,
                &mut rng,
                lambda,
                BRANCH_WIDTH,
            ) {
                let mut next = state.clone();
                apply(op, &mut next.board, &mut next.position, n);
                next.prefix.push(op);
                next.energy += de;
                next.fixed += dm;
                expanded.push(next);
            }
        }
        if expanded.is_empty() {
            break;
        }

        // Select under three static objectives and deduplicate identical boards.
        let mut next_beam = Vec::new();
        let mut hashes = Vec::new();
        for lambda in [0_i64, 32, 96] {
            let before = next_beam.len();
            let mut order = (0..expanded.len()).collect::<Vec<_>>();
            order.sort_unstable_by_key(|&i| {
                expanded[i].energy as i64 * 16 - expanded[i].fixed as i64 * lambda
                    + expanded[i].prefix.len() as i64 * 4
            });
            for index in order.into_iter().take(BEAM_WIDTH) {
                let hash = board_hash(&expanded[index].board);
                if !hashes.contains(&hash) {
                    hashes.push(hash);
                    next_beam.push(expanded[index].clone());
                    if next_beam.len() - before >= (BEAM_WIDTH + 2) / 3 {
                        break;
                    }
                }
            }
            if next_beam.len() >= BEAM_WIDTH {
                next_beam.truncate(BEAM_WIDTH);
                break;
            }
        }
        beam = next_beam;
        depth += 1;

        // Exact completion is deliberately sparse; most time is spent exploring
        // macro prefixes rather than repeatedly simulating similar fallbacks.
        if depth % 4 == 0 {
            for state in &beam {
                if start.elapsed().as_secs_f64() >= BEAM_END_SEC {
                    break;
                }
                let (remaining, _) = best_fallback(&plans, &state.board, &state.position, n);
                let total = state.prefix.len() + remaining;
                if total < best_total {
                    best_total = total;
                    best_board.clone_from(&state.board);
                    best_position.clone_from(&state.position);
                    best_prefix.clone_from(&state.prefix);
                }
            }
        }
    }
    // Include the terminal frontier even when its depth is not a checkpoint.
    for state in &beam {
        if start.elapsed().as_secs_f64() >= SEARCH_END_SEC {
            break;
        }
        let (remaining, _) = best_fallback(&plans, &state.board, &state.position, n);
        let total = state.prefix.len() + remaining;
        if total < best_total {
            best_total = total;
            best_board.clone_from(&state.board);
            best_position.clone_from(&state.position);
            best_prefix.clone_from(&state.prefix);
        }
    }

    // Phase 2: exact one-step rollout from the best beam checkpoint.  The
    // proposal set is sampled anew after every accepted macro.
    board = best_board;
    position = best_position;
    let mut prefix = best_prefix;
    while prefix.len() < PREFIX_LIMIT && start.elapsed().as_secs_f64() < SEARCH_END_SEC {
        let state = SearchState {
            board: board.clone(),
            position: position.clone(),
            prefix: prefix.clone(),
            energy: 0,
            fixed: exact_count(&board),
        };
        let shortlist = sampled_proposals(
            &state,
            &candidates,
            &distance,
            n,
            &mut rng,
            48,
            ROLLOUT_WIDTH,
        );

        let mut choice = None;
        for (_, _, _, op) in shortlist {
            if start.elapsed().as_secs_f64() >= SEARCH_END_SEC {
                break;
            }
            let mut next_board = board.clone();
            let mut next_position = position.clone();
            apply(op, &mut next_board, &mut next_position, n);
            let (fallback_count, _) = best_fallback(&plans, &next_board, &next_position, n);
            let total = prefix.len() + 1 + fallback_count;
            let improves_choice = match choice.as_ref() {
                Some(&(old, _, _, _)) => total < old,
                None => true,
            };
            if total < best_total && improves_choice {
                choice = Some((total, op, next_board, next_position));
            }
        }
        let Some((total, op, next_board, next_position)) = choice else {
            break;
        };
        best_total = total;
        board = next_board;
        position = next_position;
        prefix.push(op);
    }

    let (fallback_count, plan_index) = best_fallback(&plans, &board, &position, n);
    assert_eq!(prefix.len() + fallback_count, best_total);
    let mut operations = prefix;
    plans[plan_index].run(&mut board, &mut position, n, Some(&mut operations));
    debug_assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
    assert_eq!(operations.len(), best_total);
    assert!(operations.len() <= 100_000);

    let mut output = String::new();
    for op in operations {
        output.push_str(&format!("{} {} {} {} {}\n", op.d, op.r, op.c, op.h, op.w));
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
