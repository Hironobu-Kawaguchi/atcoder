use std::collections::VecDeque;
use std::io::{self, Read};
use std::time::Instant;

const SEARCH_LIMIT_SEC: f64 = 1.45;
const SHORTLIST_SIZE: usize = 12;
const MAX_PREFIX_LENGTH: usize = 128;

struct Scanner<'a> {
    it: std::str::SplitWhitespace<'a>,
}

impl<'a> Scanner<'a> {
    fn new(s: &'a str) -> Self {
        Self {
            it: s.split_whitespace(),
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.it.next().unwrap().parse().unwrap()
    }
}

#[derive(Clone, Copy, PartialEq, Eq)]
enum Direction {
    V,
    H,
}

#[derive(Clone, Copy)]
struct Operation {
    d: Direction,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn apply(board: &mut [usize], positions: &mut [usize], op: Operation, n: usize) {
    let mut swap_cells = |a: usize, b: usize| {
        board.swap(a, b);
        positions[board[a]] = a;
        positions[board[b]] = b;
    };
    match op.d {
        Direction::V => {
            let dh = op.h / 2;
            for x in 0..dh {
                for y in 0..op.w {
                    let a = (op.r + x) * n + op.c + y;
                    let b = (op.r + dh + x) * n + op.c + y;
                    swap_cells(a, b);
                }
            }
        }
        Direction::H => {
            let dw = op.w / 2;
            for x in 0..op.h {
                for y in 0..dw {
                    let a = (op.r + x) * n + op.c + y;
                    let b = (op.r + x) * n + op.c + dw + y;
                    swap_cells(a, b);
                }
            }
        }
    }
}

fn rectangle_is_clear(
    r: usize,
    c: usize,
    h: usize,
    w: usize,
    vertical_walls: &[Vec<bool>],
    horizontal_walls: &[Vec<bool>],
) -> bool {
    for row in r..r + h {
        for col in c..c + w.saturating_sub(1) {
            if vertical_walls[row][col] {
                return false;
            }
        }
    }
    for row in r..r + h.saturating_sub(1) {
        for col in c..c + w {
            if horizontal_walls[row][col] {
                return false;
            }
        }
    }
    true
}

fn rectangle_candidates(
    n: usize,
    vertical_walls: &[Vec<bool>],
    horizontal_walls: &[Vec<bool>],
) -> Vec<Operation> {
    let mut result = Vec::new();
    for r in 0..n {
        for c in 0..n {
            for h in 1..=n - r {
                for w in 1..=n - c {
                    if h * w < 4
                        || !rectangle_is_clear(r, c, h, w, vertical_walls, horizontal_walls)
                    {
                        continue;
                    }
                    if h % 2 == 0 {
                        result.push(Operation {
                            d: Direction::V,
                            r,
                            c,
                            h,
                            w,
                        });
                    }
                    if w % 2 == 0 {
                        result.push(Operation {
                            d: Direction::H,
                            r,
                            c,
                            h,
                            w,
                        });
                    }
                }
            }
        }
    }
    result
}

fn wall_graph(
    n: usize,
    vertical_walls: &[Vec<bool>],
    horizontal_walls: &[Vec<bool>],
) -> Vec<Vec<usize>> {
    let mut graph = vec![Vec::new(); n * n];
    for r in 0..n {
        for c in 0..n {
            let v = r * n + c;
            if c + 1 < n && !vertical_walls[r][c] {
                graph[v].push(v + 1);
                graph[v + 1].push(v);
            }
            if r + 1 < n && !horizontal_walls[r][c] {
                graph[v].push(v + n);
                graph[v + n].push(v);
            }
        }
    }
    graph
}

fn all_pairs_distances(graph: &[Vec<usize>]) -> Vec<Vec<u16>> {
    let k = graph.len();
    let mut distances = vec![vec![u16::MAX; k]; k];
    for source in 0..k {
        let mut queue = VecDeque::new();
        distances[source][source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            let next_distance = distances[source][v] + 1;
            for &to in &graph[v] {
                if distances[source][to] == u16::MAX {
                    distances[source][to] = next_distance;
                    queue.push_back(to);
                }
            }
        }
    }
    distances
}

fn cell_cost(tile: usize, at: usize, distances: &[Vec<u16>]) -> i32 {
    let distance = distances[tile][at];
    assert_ne!(distance, u16::MAX, "tile is outside its goal component");
    4 * i32::from(distance) + i32::from(tile != at)
}

fn heuristic_improvement(board: &[usize], op: Operation, n: usize, distances: &[Vec<u16>]) -> i32 {
    let mut delta = 0;
    let mut add_pair = |a: usize, b: usize| {
        delta += cell_cost(board[a], a, distances) + cell_cost(board[b], b, distances)
            - cell_cost(board[a], b, distances)
            - cell_cost(board[b], a, distances);
    };
    match op.d {
        Direction::V => {
            let dh = op.h / 2;
            for x in 0..dh {
                for y in 0..op.w {
                    add_pair((op.r + x) * n + op.c + y, (op.r + dh + x) * n + op.c + y);
                }
            }
        }
        Direction::H => {
            let dw = op.w / 2;
            for x in 0..op.h {
                for y in 0..dw {
                    add_pair((op.r + x) * n + op.c + y, (op.r + x) * n + op.c + dw + y);
                }
            }
        }
    }
    delta
}

struct ForestPlan {
    parent: Vec<usize>,
    depth: Vec<usize>,
    component: Vec<usize>,
    order: Vec<usize>,
}

impl ForestPlan {
    fn new(graph: &[Vec<usize>]) -> Self {
        let k = graph.len();
        let mut parent = vec![usize::MAX; k];
        let mut depth = vec![usize::MAX; k];
        let mut component = vec![usize::MAX; k];
        let mut roots = vec![false; k];
        let mut queue = VecDeque::new();
        for root in 0..k {
            if depth[root] != usize::MAX {
                continue;
            }
            roots[root] = true;
            parent[root] = root;
            depth[root] = 0;
            component[root] = root;
            queue.push_back(root);
            while let Some(v) = queue.pop_front() {
                for &to in &graph[v] {
                    if depth[to] == usize::MAX {
                        parent[to] = v;
                        depth[to] = depth[v] + 1;
                        component[to] = root;
                        queue.push_back(to);
                    }
                }
            }
        }
        let mut order: Vec<usize> = (0..k).filter(|&v| !roots[v]).collect();
        order.sort_unstable_by_key(|&v| std::cmp::Reverse(depth[v]));
        Self {
            parent,
            depth,
            component,
            order,
        }
    }
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        Operation {
            d: Direction::H,
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        Operation {
            d: Direction::V,
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
}

/// Applies the exact leaf-elimination fallback and returns its operation count.
/// `emit` is a no-op during candidate evaluation and records operations only for
/// the final chosen state.
fn run_fallback<F: FnMut(Operation)>(
    board: &mut [usize],
    positions: &mut [usize],
    plan: &ForestPlan,
    n: usize,
    mut emit: F,
) -> usize {
    let mut count = 0;
    let mut left = Vec::with_capacity(2 * n);
    let mut right = Vec::with_capacity(2 * n);
    for &target in &plan.order {
        let source = positions[target];
        assert_eq!(plan.component[source], plan.component[target]);
        let (mut a, mut b) = (source, target);
        left.clear();
        right.clear();
        while plan.depth[a] > plan.depth[b] {
            left.push(a);
            a = plan.parent[a];
        }
        while plan.depth[b] > plan.depth[a] {
            right.push(b);
            b = plan.parent[b];
        }
        while a != b {
            left.push(a);
            right.push(b);
            a = plan.parent[a];
            b = plan.parent[b];
        }
        left.push(a);
        right.reverse();

        let mut previous = left[0];
        for &next in left.iter().skip(1).chain(right.iter()) {
            let op = adjacent_operation(previous, next, n);
            apply(board, positions, op, n);
            emit(op);
            count += 1;
            previous = next;
        }
        debug_assert_eq!(board[target], target);
    }
    assert!(board.iter().enumerate().all(|(at, &tile)| at == tile));
    count
}

fn exact_fallback_count(
    board: &[usize],
    positions: &[usize],
    plan: &ForestPlan,
    n: usize,
) -> usize {
    let mut trial_board = board.to_vec();
    let mut trial_positions = positions.to_vec();
    run_fallback(&mut trial_board, &mut trial_positions, plan, n, |_| {})
}

fn add_to_shortlist(shortlist: &mut Vec<(i32, Operation)>, score: i32, op: Operation) {
    if score <= 0 {
        return;
    }
    if shortlist.len() < SHORTLIST_SIZE {
        shortlist.push((score, op));
        return;
    }
    let (worst_index, worst_score) = shortlist
        .iter()
        .enumerate()
        .min_by_key(|(_, (s, _))| *s)
        .map(|(i, (s, _))| (i, *s))
        .unwrap();
    if score > worst_score {
        shortlist[worst_index] = (score, op);
    }
}

fn main() {
    let started = Instant::now();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut scanner = Scanner::new(&input);
    let n: usize = scanner.next();
    assert_eq!(n, 20);

    let raw_board: Vec<usize> = (0..n * n).map(|_| scanner.next()).collect();
    let offset = usize::from(raw_board.iter().copied().min() == Some(1));
    let mut board: Vec<usize> = raw_board.into_iter().map(|x| x - offset).collect();
    let vertical_walls: Vec<Vec<bool>> = (0..n)
        .map(|_| {
            scanner
                .next::<String>()
                .bytes()
                .map(|b| b == b'1')
                .collect()
        })
        .collect();
    let horizontal_walls: Vec<Vec<bool>> = (0..n - 1)
        .map(|_| {
            scanner
                .next::<String>()
                .bytes()
                .map(|b| b == b'1')
                .collect()
        })
        .collect();

    let mut positions = vec![0; n * n];
    for (at, &tile) in board.iter().enumerate() {
        positions[tile] = at;
    }

    let graph = wall_graph(n, &vertical_walls, &horizontal_walls);
    let distances = all_pairs_distances(&graph);
    let plan = ForestPlan::new(&graph);
    let candidates = rectangle_candidates(n, &vertical_walls, &horizontal_walls);
    let initial_fallback_count = exact_fallback_count(&board, &positions, &plan, n);
    let mut current_fallback_count = initial_fallback_count;
    let mut best_prefix = Vec::new();

    while best_prefix.len() < MAX_PREFIX_LENGTH
        && started.elapsed().as_secs_f64() < SEARCH_LIMIT_SEC
    {
        let mut shortlist = Vec::with_capacity(SHORTLIST_SIZE);
        for (index, &op) in candidates.iter().enumerate() {
            if index % 256 == 0 && started.elapsed().as_secs_f64() >= SEARCH_LIMIT_SEC {
                break;
            }
            let score = heuristic_improvement(&board, op, n, &distances);
            add_to_shortlist(&mut shortlist, score, op);
        }
        shortlist.sort_unstable_by_key(|&(score, _)| std::cmp::Reverse(score));

        let mut choice: Option<(usize, Operation)> = None;
        for (_, op) in shortlist {
            if started.elapsed().as_secs_f64() >= SEARCH_LIMIT_SEC {
                break;
            }
            let mut trial_board = board.clone();
            let mut trial_positions = positions.clone();
            apply(&mut trial_board, &mut trial_positions, op, n);
            let count = run_fallback(&mut trial_board, &mut trial_positions, &plan, n, |_| {});
            let total = 1 + count;
            if total < current_fallback_count
                && choice.map_or(true, |(best_count, _)| count < best_count)
            {
                choice = Some((count, op));
            }
        }

        let Some((next_fallback_count, op)) = choice else {
            break;
        };
        apply(&mut board, &mut positions, op, n);
        best_prefix.push(op);
        current_fallback_count = next_fallback_count;
    }

    let mut answer = best_prefix;
    run_fallback(&mut board, &mut positions, &plan, n, |op| answer.push(op));
    assert!(answer.len() <= initial_fallback_count);
    assert!(answer.len() <= 100_000);

    let mut output = String::new();
    for op in answer {
        let d = if op.d == Direction::V { 'V' } else { 'H' };
        output.push_str(&format!("{} {} {} {} {}\n", d, op.r, op.c, op.h, op.w));
    }
    print!("{output}");
}
