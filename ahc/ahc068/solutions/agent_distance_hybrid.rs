use std::collections::VecDeque;
use std::io::{self, Read};
use std::time::Instant;

const HEURISTIC_OPERATION_LIMIT: usize = 18_000;
const HEURISTIC_TIME_LIMIT_SEC: f64 = 0.75;

struct Scanner<'a> {
    iter: std::str::SplitWhitespace<'a>,
}

impl<'a> Scanner<'a> {
    fn new(input: &'a str) -> Self {
        Self {
            iter: input.split_whitespace(),
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.iter.next().unwrap().parse().unwrap()
    }
}

#[derive(Clone, Copy)]
struct Operation {
    direction: char,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn add_edge(graph: &mut [Vec<usize>], a: usize, b: usize) {
    graph[a].push(b);
    graph[b].push(a);
}

fn apply_operation(operation: Operation, board: &mut [usize], position: &mut [usize], n: usize) {
    let Operation {
        direction,
        r,
        c,
        h,
        w,
    } = operation;
    if direction == 'V' {
        for dr in 0..h / 2 {
            for dc in 0..w {
                let a = (r + dr) * n + c + dc;
                let b = (r + h / 2 + dr) * n + c + dc;
                let x = board[a];
                let y = board[b];
                board.swap(a, b);
                position[x] = b;
                position[y] = a;
            }
        }
    } else {
        for dr in 0..h {
            for dc in 0..w / 2 {
                let a = (r + dr) * n + c + dc;
                let b = (r + dr) * n + c + w / 2 + dc;
                let x = board[a];
                let y = board[b];
                board.swap(a, b);
                position[x] = b;
                position[y] = a;
            }
        }
    }
}

fn affected_pairs(operation: Operation, n: usize) -> Vec<(usize, usize)> {
    let mut pairs = Vec::new();
    if operation.direction == 'V' {
        for dr in 0..operation.h / 2 {
            for dc in 0..operation.w {
                pairs.push((
                    (operation.r + dr) * n + operation.c + dc,
                    (operation.r + operation.h / 2 + dr) * n + operation.c + dc,
                ));
            }
        }
    } else {
        for dr in 0..operation.h {
            for dc in 0..operation.w / 2 {
                pairs.push((
                    (operation.r + dr) * n + operation.c + dc,
                    (operation.r + dr) * n + operation.c + operation.w / 2 + dc,
                ));
            }
        }
    }
    pairs
}

fn operation_delta(operation: Operation, board: &[usize], distances: &[Vec<i32>], n: usize) -> i32 {
    affected_pairs(operation, n)
        .into_iter()
        .map(|(a, b)| {
            let x = board[a];
            let y = board[b];
            distances[b][x] + distances[a][y] - distances[a][x] - distances[b][y]
        })
        .sum()
}

fn all_pairs_distances(graph: &[Vec<usize>]) -> Vec<Vec<i32>> {
    let size = graph.len();
    let mut answer = vec![vec![i32::MAX / 4; size]; size];
    for source in 0..size {
        let mut queue = VecDeque::new();
        answer[source][source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            for &to in &graph[v] {
                if answer[source][to] == i32::MAX / 4 {
                    answer[source][to] = answer[source][v] + 1;
                    queue.push_back(to);
                }
            }
        }
    }
    answer
}

fn make_candidates(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Operation> {
    let mut candidates = Vec::new();
    for r in 0..n {
        for c in 0..n - 1 {
            if vertical[r][c] == b'0' {
                candidates.push(Operation {
                    direction: 'H',
                    r,
                    c,
                    h: 1,
                    w: 2,
                });
            }
        }
    }
    for r in 0..n - 1 {
        for c in 0..n {
            if horizontal[r][c] == b'0' {
                candidates.push(Operation {
                    direction: 'V',
                    r,
                    c,
                    h: 2,
                    w: 1,
                });
            }
        }
    }

    // A 2x2 block is usable only when all four internal adjacencies are open.
    for r in 0..n - 1 {
        for c in 0..n - 1 {
            let open = vertical[r][c] == b'0'
                && vertical[r + 1][c] == b'0'
                && horizontal[r][c] == b'0'
                && horizontal[r][c + 1] == b'0';
            if open {
                candidates.push(Operation {
                    direction: 'V',
                    r,
                    c,
                    h: 2,
                    w: 2,
                });
                candidates.push(Operation {
                    direction: 'H',
                    r,
                    c,
                    h: 2,
                    w: 2,
                });
            }
        }
    }
    candidates
}

fn spanning_forest(graph: &[Vec<usize>]) -> (Vec<Vec<usize>>, Vec<Vec<usize>>) {
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
    (tree, components)
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        Operation {
            direction: 'H',
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        Operation {
            direction: 'V',
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
}

fn tree_path(start: usize, goal: usize, tree: &[Vec<usize>], active: &[bool]) -> Vec<usize> {
    let size = tree.len();
    let mut parent = vec![usize::MAX; size];
    let mut queue = VecDeque::from([start]);
    parent[start] = start;
    while let Some(v) = queue.pop_front() {
        if v == goal {
            break;
        }
        for &to in &tree[v] {
            if active[to] && parent[to] == usize::MAX {
                parent[to] = v;
                queue.push_back(to);
            }
        }
    }
    assert_ne!(parent[goal], usize::MAX, "target token left its component");
    let mut path = vec![goal];
    while *path.last().unwrap() != start {
        path.push(parent[*path.last().unwrap()]);
    }
    path.reverse();
    path
}

fn finish_on_tree(
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    graph: &[Vec<usize>],
    operations: &mut Vec<Operation>,
) {
    let (tree, components) = spanning_forest(graph);
    let mut active = vec![true; board.len()];
    for component in components {
        let mut remaining = component.len();
        while remaining > 1 {
            let leaf = component
                .iter()
                .copied()
                .find(|&v| active[v] && tree[v].iter().filter(|&&to| active[to]).count() <= 1)
                .unwrap();
            let source = position[leaf];
            let path = tree_path(source, leaf, &tree, &active);
            for edge in path.windows(2) {
                let operation = adjacent_operation(edge[0], edge[1], n);
                apply_operation(operation, board, position, n);
                operations.push(operation);
            }
            debug_assert_eq!(board[leaf], leaf);
            active[leaf] = false;
            remaining -= 1;
        }
    }
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner::new(input);
    let n: usize = scanner.next();
    let size = n * n;
    let mut board = (0..size)
        .map(|_| scanner.next::<usize>())
        .collect::<Vec<_>>();
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

    let distances = all_pairs_distances(&graph);
    let candidates = make_candidates(n, &vertical, &horizontal);
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }

    let start = Instant::now();
    let mut operations = Vec::new();
    while operations.len() < HEURISTIC_OPERATION_LIMIT
        && start.elapsed().as_secs_f64() < HEURISTIC_TIME_LIMIT_SEC
    {
        let best = candidates
            .iter()
            .copied()
            .map(|operation| (operation_delta(operation, &board, &distances, n), operation))
            .min_by_key(|&(delta, _)| delta);
        let Some((delta, operation)) = best else {
            break;
        };
        if delta >= 0 {
            break;
        }
        apply_operation(operation, &mut board, &mut position, n);
        operations.push(operation);
    }

    finish_on_tree(&mut board, &mut position, n, &graph, &mut operations);
    debug_assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
    assert!(operations.len() <= 100_000);

    let mut output = String::new();
    for operation in operations {
        output.push_str(&format!(
            "{} {} {} {} {}\n",
            operation.direction, operation.r, operation.c, operation.h, operation.w
        ));
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
