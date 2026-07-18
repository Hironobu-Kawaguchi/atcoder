use std::collections::VecDeque;
use std::io::{self, Read};
use std::time::Instant;

const SEARCH_LIMIT: usize = 18_000;
const SEARCH_TIME_SEC: f64 = 1.35;
const CHECK_INTERVAL: usize = 16;

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

fn swap_cells(a: usize, b: usize, board: &mut [usize], position: &mut [usize]) {
    let x = board[a];
    let y = board[b];
    board.swap(a, b);
    position[x] = b;
    position[y] = a;
}

fn delta(op: Operation, board: &[usize], distance: &[Vec<i32>], n: usize) -> i32 {
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

fn candidates(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Operation> {
    let mut result = Vec::new();
    // All wall-free rectangles up to 4x4.  This includes adjacent and 2x2 swaps,
    // plus useful 1x4, 4x1, 2x4, and 4x2 moves.
    for h in 1..=4 {
        for w in 1..=4 {
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

struct Fallback {
    tree: Vec<Vec<usize>>,
    components: Vec<Vec<usize>>,
}

impl Fallback {
    fn new(graph: &[Vec<usize>]) -> Self {
        let size = graph.len();
        let mut tree = vec![Vec::new(); size];
        let mut components = Vec::new();
        let mut seen = vec![false; size];
        for root in 0..size {
            if seen[root] {
                continue;
            }
            seen[root] = true;
            let mut component = Vec::new();
            let mut queue = VecDeque::from([root]);
            while let Some(v) = queue.pop_front() {
                component.push(v);
                for &to in &graph[v] {
                    if !seen[to] {
                        seen[to] = true;
                        add_edge(&mut tree, v, to);
                        queue.push_back(to);
                    }
                }
            }
            components.push(component);
        }
        Self { tree, components }
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
                let leaf = component
                    .iter()
                    .copied()
                    .find(|&v| {
                        active[v] && self.tree[v].iter().filter(|&&to| active[to]).count() <= 1
                    })
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
        let mut copied_board = board.to_vec();
        let mut copied_position = position.to_vec();
        self.run(&mut copied_board, &mut copied_position, n, None)
    }
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
    let candidate = candidates(n, &vertical, &horizontal);
    let fallback = Fallback::new(&graph);
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }

    let mut prefix = Vec::new();
    let mut best_board = board.clone();
    let mut best_position = position.clone();
    let mut best_prefix = Vec::new();
    let mut best_total = fallback.count(&board, &position, n);
    let start = Instant::now();

    while prefix.len() < SEARCH_LIMIT && start.elapsed().as_secs_f64() < SEARCH_TIME_SEC {
        let Some((best_delta, best_op)) = candidate
            .iter()
            .copied()
            .map(|op| (delta(op, &board, &distance, n), op))
            .min_by_key(|&(value, _)| value)
        else {
            break;
        };
        if best_delta >= 0 {
            break;
        }
        apply(best_op, &mut board, &mut position, n);
        prefix.push(best_op);

        // Exact look-ahead to the deterministic completion.  Strong moves are
        // checked immediately; all other states are sampled at a fixed cadence.
        if prefix.len() % CHECK_INTERVAL == 0 || best_delta <= -8 {
            let total = prefix.len() + fallback.count(&board, &position, n);
            if total < best_total {
                best_total = total;
                best_board.clone_from(&board);
                best_position.clone_from(&position);
                best_prefix.clone_from(&prefix);
            }
        }
    }

    // Check the final local-optimum/time-limit state too, then discard every
    // suffix after the best measured prefix.
    let total = prefix.len() + fallback.count(&board, &position, n);
    if total < best_total {
        best_board = board;
        best_position = position;
        best_prefix = prefix;
        best_total = total;
    }

    let mut operations = best_prefix;
    fallback.run(
        &mut best_board,
        &mut best_position,
        n,
        Some(&mut operations),
    );
    debug_assert!(best_board
        .iter()
        .enumerate()
        .all(|(cell, &card)| cell == card));
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
