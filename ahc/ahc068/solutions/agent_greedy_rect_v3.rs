use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const SEARCH_TIME_SEC: f64 = 1.10;
const MAX_PREFIX: usize = 20_000;
const ROLLOUT_WIDTH: usize = 8;
const CHECK_INTERVAL: usize = 32;
const SAVED_STATES: usize = 8;

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
    d: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

#[derive(Clone)]
struct Candidate {
    op: Operation,
    pairs: Vec<(usize, usize)>,
}

fn swap_cells(a: usize, b: usize, board: &mut [usize], positions: &mut [usize]) {
    board.swap(a, b);
    positions[board[a]] = a;
    positions[board[b]] = b;
}

fn apply(candidate: &Candidate, board: &mut [usize], positions: &mut [usize]) {
    for &(a, b) in &candidate.pairs {
        swap_cells(a, b, board, positions);
    }
}

fn apply_operation(op: Operation, board: &mut [usize], positions: &mut [usize], n: usize) {
    if op.d == b'V' {
        for x in 0..op.h / 2 {
            for y in 0..op.w {
                swap_cells(
                    (op.r + x) * n + op.c + y,
                    (op.r + op.h / 2 + x) * n + op.c + y,
                    board,
                    positions,
                );
            }
        }
    } else {
        for x in 0..op.h {
            for y in 0..op.w / 2 {
                swap_cells(
                    (op.r + x) * n + op.c + y,
                    (op.r + x) * n + op.c + op.w / 2 + y,
                    board,
                    positions,
                );
            }
        }
    }
}

fn graph_from_walls(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut graph = vec![Vec::new(); n * n];
    for r in 0..n {
        for c in 0..n {
            let v = r * n + c;
            if c + 1 < n && vertical[r][c] == b'0' {
                graph[v].push(v + 1);
                graph[v + 1].push(v);
            }
            if r + 1 < n && horizontal[r][c] == b'0' {
                graph[v].push(v + n);
                graph[v + n].push(v);
            }
        }
    }
    graph
}

fn all_pairs_distance(graph: &[Vec<usize>]) -> Vec<u16> {
    let k = graph.len();
    let mut result = vec![u16::MAX; k * k];
    let mut queue = VecDeque::with_capacity(k);
    for source in 0..k {
        result[source * k + source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            let next = result[source * k + v] + 1;
            for &to in &graph[v] {
                if result[source * k + to] == u16::MAX {
                    result[source * k + to] = next;
                    queue.push_back(to);
                }
            }
        }
    }
    result
}

fn rectangle_open(
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

fn make_candidate(op: Operation, n: usize) -> Candidate {
    let mut pairs = Vec::new();
    if op.d == b'V' {
        for x in 0..op.h / 2 {
            for y in 0..op.w {
                pairs.push((
                    (op.r + x) * n + op.c + y,
                    (op.r + op.h / 2 + x) * n + op.c + y,
                ));
            }
        }
    } else {
        for x in 0..op.h {
            for y in 0..op.w / 2 {
                pairs.push((
                    (op.r + x) * n + op.c + y,
                    (op.r + x) * n + op.c + op.w / 2 + y,
                ));
            }
        }
    }
    Candidate { op, pairs }
}

fn candidates(
    n: usize,
    max_dimension: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Candidate> {
    let mut result = Vec::new();
    for h in 1..=max_dimension.min(n) {
        for w in 1..=max_dimension.min(n) {
            if h * w == 1 || (h % 2 == 1 && w % 2 == 1) {
                continue;
            }
            for r in 0..=n - h {
                for c in 0..=n - w {
                    if !rectangle_open(r, c, h, w, vertical, horizontal) {
                        continue;
                    }
                    if h % 2 == 0 {
                        result.push(make_candidate(
                            Operation {
                                d: b'V',
                                r,
                                c,
                                h,
                                w,
                            },
                            n,
                        ));
                    }
                    if w % 2 == 0 {
                        result.push(make_candidate(
                            Operation {
                                d: b'H',
                                r,
                                c,
                                h,
                                w,
                            },
                            n,
                        ));
                    }
                }
            }
        }
    }
    result
}

// Positive means that the operation reduces wall distance and misplacements.
fn gain(candidate: &Candidate, board: &[usize], distance: &[u16], k: usize) -> i32 {
    let mut result = 0;
    for &(a, b) in &candidate.pairs {
        let x = board[a];
        let y = board[b];
        let before = 4 * (u32::from(distance[x * k + a]) + u32::from(distance[y * k + b]))
            + u32::from(x != a)
            + u32::from(y != b);
        let after = 4 * (u32::from(distance[x * k + b]) + u32::from(distance[y * k + a]))
            + u32::from(x != b)
            + u32::from(y != a);
        result += before as i32 - after as i32;
    }
    result
}

fn top_candidates(
    candidates: &[Candidate],
    board: &[usize],
    distance: &[u16],
    k: usize,
) -> Vec<(i32, usize)> {
    let mut best = Vec::<(i32, usize)>::with_capacity(ROLLOUT_WIDTH);
    for (index, candidate) in candidates.iter().enumerate() {
        let value = gain(candidate, board, distance, k);
        if value <= 0 {
            continue;
        }
        if best.len() < ROLLOUT_WIDTH {
            best.push((value, index));
        } else {
            let worst = best
                .iter()
                .enumerate()
                .min_by_key(|(_, (score, _))| *score)
                .map(|(i, _)| i)
                .unwrap();
            if value > best[worst].0 {
                best[worst] = (value, index);
            }
        }
    }
    best.sort_unstable_by_key(|&(score, _)| std::cmp::Reverse(score));
    best
}

// Select the first move by a depth-2 rollout over the current shortlist.
fn rollout_choice(
    shortlist: &[(i32, usize)],
    candidates: &[Candidate],
    board: &[usize],
    positions: &[usize],
    distance: &[u16],
    k: usize,
) -> Option<usize> {
    let mut choice = None;
    let mut best_two_step_gain = i32::MIN;
    for &(first_gain, first) in shortlist {
        let mut trial_board = board.to_vec();
        let mut trial_positions = positions.to_vec();
        apply(&candidates[first], &mut trial_board, &mut trial_positions);
        let second_gain = shortlist
            .iter()
            .filter(|(_, second)| *second != first)
            .map(|&(_, second)| gain(&candidates[second], &trial_board, distance, k))
            .max()
            .unwrap_or(0)
            .max(0);
        let score = first_gain + second_gain;
        if score > best_two_step_gain {
            best_two_step_gain = score;
            choice = Some(first);
        }
    }
    choice
}

struct ForestPlan {
    tree: Vec<Vec<usize>>,
    parent: Vec<usize>,
    depth: Vec<usize>,
    tree_distance: Vec<u16>,
    components: Vec<Vec<usize>>,
}

impl ForestPlan {
    fn new(graph: &[Vec<usize>], preferred_root: usize, reverse_neighbors: bool) -> Self {
        let k = graph.len();
        let mut tree = vec![Vec::new(); k];
        let mut parent = vec![usize::MAX; k];
        let mut depth = vec![0; k];
        let mut components = Vec::new();
        let roots = (0..k).cycle().skip(preferred_root).take(k);
        for root in roots {
            if parent[root] != usize::MAX {
                continue;
            }
            parent[root] = root;
            let mut component = Vec::new();
            let mut queue = VecDeque::from([root]);
            while let Some(v) = queue.pop_front() {
                component.push(v);
                if reverse_neighbors {
                    for &to in graph[v].iter().rev() {
                        if parent[to] == usize::MAX {
                            parent[to] = v;
                            depth[to] = depth[v] + 1;
                            tree[v].push(to);
                            tree[to].push(v);
                            queue.push_back(to);
                        }
                    }
                } else {
                    for &to in &graph[v] {
                        if parent[to] == usize::MAX {
                            parent[to] = v;
                            depth[to] = depth[v] + 1;
                            tree[v].push(to);
                            tree[to].push(v);
                            queue.push_back(to);
                        }
                    }
                }
            }
            components.push(component);
        }
        let tree_distance = all_pairs_distance(&tree);
        Self {
            tree,
            parent,
            depth,
            tree_distance,
            components,
        }
    }

    fn path(&self, start: usize, goal: usize) -> Vec<usize> {
        let (mut a, mut b) = (start, goal);
        let mut left = vec![a];
        let mut right = vec![b];
        while self.depth[a] > self.depth[b] {
            a = self.parent[a];
            left.push(a);
        }
        while self.depth[b] > self.depth[a] {
            b = self.parent[b];
            right.push(b);
        }
        while a != b {
            a = self.parent[a];
            b = self.parent[b];
            left.push(a);
            right.push(b);
        }
        left.extend(right[..right.len() - 1].iter().rev().copied());
        left
    }

    fn run<F: FnMut(Operation)>(
        &self,
        board: &mut [usize],
        positions: &mut [usize],
        n: usize,
        mut emit: F,
    ) -> usize {
        let k = board.len();
        let mut active = vec![true; k];
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut count = 0;
        for component in &self.components {
            for _ in 1..component.len() {
                let leaf = component
                    .iter()
                    .copied()
                    .filter(|&v| active[v] && degree[v] <= 1)
                    .min_by_key(|&v| self.tree_distance[positions[v] * k + v])
                    .unwrap();
                let path = self.path(positions[leaf], leaf);
                debug_assert!(path.iter().all(|&v| active[v]));
                for edge in path.windows(2) {
                    let op = adjacent_operation(edge[0], edge[1], n);
                    apply_operation(op, board, positions, n);
                    emit(op);
                    count += 1;
                }
                debug_assert_eq!(board[leaf], leaf);
                active[leaf] = false;
                degree[leaf] = 0;
                for &to in &self.tree[leaf] {
                    if active[to] {
                        degree[to] -= 1;
                    }
                }
            }
        }
        assert!(board.iter().enumerate().all(|(cell, &tile)| cell == tile));
        count
    }

    fn count(&self, board: &[usize], positions: &[usize], n: usize) -> usize {
        let mut copied_board = board.to_vec();
        let mut copied_positions = positions.to_vec();
        self.run(&mut copied_board, &mut copied_positions, n, |_| {})
    }
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        Operation {
            d: b'H',
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        Operation {
            d: b'V',
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
}

#[derive(Clone)]
struct Snapshot {
    estimate: usize,
    board: Vec<usize>,
    positions: Vec<usize>,
    prefix: Vec<Operation>,
}

fn save_snapshot(states: &mut Vec<Snapshot>, snapshot: Snapshot) {
    states.push(snapshot);
    states.sort_unstable_by_key(|state| state.estimate);
    states.dedup_by_key(|state| state.prefix.len());
    states.truncate(SAVED_STATES);
}

fn main() {
    let started = Instant::now();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let k = n * n;
    let mut board: Vec<usize> = (0..k).map(|_| scanner.next()).collect();
    let vertical: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let mut positions = vec![0; k];
    for (cell, &tile) in board.iter().enumerate() {
        positions[tile] = cell;
    }

    let graph = graph_from_walls(n, &vertical, &horizontal);
    let distance = all_pairs_distance(&graph);
    let core_candidates = candidates(n, 4, &vertical, &horizontal);
    let macro_candidates = candidates(n, 6, &vertical, &horizontal);
    let root_cells = [
        0,
        n - 1,
        (n - 1) * n,
        k - 1,
        (n / 2) * n + n / 2,
        n / 2,
        (n - 1) * n + n / 2,
        (n / 2) * n,
        (n / 2) * n + n - 1,
    ];
    let mut plans = Vec::new();
    for (i, &root) in root_cells.iter().enumerate() {
        plans.push(ForestPlan::new(&graph, root, i % 2 == 1));
    }

    let mut prefix = Vec::new();
    let mut states = Vec::new();
    let initial_count = plans[0].count(&board, &positions, n);
    save_snapshot(
        &mut states,
        Snapshot {
            estimate: initial_count,
            board: board.clone(),
            positions: positions.clone(),
            prefix: Vec::new(),
        },
    );

    while prefix.len() < MAX_PREFIX && started.elapsed().as_secs_f64() < SEARCH_TIME_SEC {
        let active_candidates = if prefix.len() % CHECK_INTERVAL == 0 {
            &macro_candidates
        } else {
            &core_candidates
        };
        let shortlist = top_candidates(active_candidates, &board, &distance, k);
        let Some(chosen) = rollout_choice(
            &shortlist,
            active_candidates,
            &board,
            &positions,
            &distance,
            k,
        ) else {
            break;
        };
        apply(&active_candidates[chosen], &mut board, &mut positions);
        prefix.push(active_candidates[chosen].op);

        if prefix.len() % CHECK_INTERVAL == 0 {
            let fallback = plans[0].count(&board, &positions, n);
            save_snapshot(
                &mut states,
                Snapshot {
                    estimate: prefix.len() + fallback,
                    board: board.clone(),
                    positions: positions.clone(),
                    prefix: prefix.clone(),
                },
            );
        }
    }
    let fallback = plans[0].count(&board, &positions, n);
    save_snapshot(
        &mut states,
        Snapshot {
            estimate: prefix.len() + fallback,
            board,
            positions,
            prefix,
        },
    );

    let mut best: Option<(usize, usize, usize)> = None;
    for (state_index, state) in states.iter().enumerate() {
        for (plan_index, plan) in plans.iter().enumerate() {
            let total = state.prefix.len() + plan.count(&state.board, &state.positions, n);
            if best.map_or(true, |(best_total, _, _)| total < best_total) {
                best = Some((total, state_index, plan_index));
            }
        }
    }
    let (best_total, state_index, plan_index) = best.unwrap();
    let mut state = states.swap_remove(state_index);
    let mut answer = state.prefix;
    plans[plan_index].run(&mut state.board, &mut state.positions, n, |op| {
        answer.push(op)
    });
    assert_eq!(answer.len(), best_total);
    assert!(answer.len() <= initial_count);
    assert!(answer.len() <= 100_000);

    let mut output = String::new();
    for op in answer {
        writeln!(
            output,
            "{} {} {} {} {}",
            op.d as char, op.r, op.c, op.h, op.w
        )
        .unwrap();
    }
    print!("{output}");
}
