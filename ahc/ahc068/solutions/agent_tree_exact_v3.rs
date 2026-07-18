use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const SEARCH_TIME_SEC: f64 = 1.05;
const SEARCH_MOVE_LIMIT: usize = 18_000;
const CHECK_INTERVAL: usize = 16;
const CHECKPOINT_LIMIT: usize = 6;

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
    direction: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn add_edge(graph: &mut [Vec<usize>], a: usize, b: usize) {
    graph[a].push(b);
    graph[b].push(a);
}

fn apply_operation(op: Operation, board: &mut [usize], position: &mut [usize], n: usize) {
    let mut swap = |a: usize, b: usize| {
        board.swap(a, b);
        position[board[a]] = a;
        position[board[b]] = b;
    };
    if op.direction == b'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                swap(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                swap(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                );
            }
        }
    }
}

fn rectangle_is_open(
    r: usize,
    c: usize,
    h: usize,
    w: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> bool {
    for row in r..r + h {
        for col in c..c + w.saturating_sub(1) {
            if vertical[row][col] == b'1' {
                return false;
            }
        }
    }
    for row in r..r + h.saturating_sub(1) {
        for col in c..c + w {
            if horizontal[row][col] == b'1' {
                return false;
            }
        }
    }
    true
}

fn rectangle_candidates(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Operation> {
    let mut result = Vec::new();
    for h in 1..=4.min(n) {
        for w in 1..=4.min(n) {
            if h * w == 1 || (h % 2 == 1 && w % 2 == 1) {
                continue;
            }
            for r in 0..=n - h {
                for c in 0..=n - w {
                    if !rectangle_is_open(r, c, h, w, vertical, horizontal) {
                        continue;
                    }
                    if h % 2 == 0 {
                        result.push(Operation {
                            direction: b'V',
                            r,
                            c,
                            h,
                            w,
                        });
                    }
                    if w % 2 == 0 {
                        result.push(Operation {
                            direction: b'H',
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

fn all_graph_distances(graph: &[Vec<usize>]) -> Vec<u16> {
    let size = graph.len();
    let mut result = vec![u16::MAX; size * size];
    let mut queue = VecDeque::with_capacity(size);
    for source in 0..size {
        result[source * size + source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            let next_distance = result[source * size + v] + 1;
            for &to in &graph[v] {
                let index = source * size + to;
                if result[index] == u16::MAX {
                    result[index] = next_distance;
                    queue.push_back(to);
                }
            }
        }
    }
    result
}

fn operation_delta(op: Operation, board: &[usize], distances: &[u16], n: usize) -> i32 {
    let size = board.len();
    let mut delta = 0i32;
    let mut add_swap = |a: usize, b: usize| {
        let x = board[a];
        let y = board[b];
        delta += i32::from(distances[x * size + b]) + i32::from(distances[y * size + a])
            - i32::from(distances[x * size + a])
            - i32::from(distances[y * size + b]);
    };
    if op.direction == b'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                add_swap(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                add_swap(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                );
            }
        }
    }
    delta
}

fn neighbor(
    cell: usize,
    direction: usize,
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Option<usize> {
    let (r, c) = (cell / n, cell % n);
    match direction {
        0 if r > 0 && horizontal[r - 1][c] == b'0' => Some(cell - n),
        1 if c + 1 < n && vertical[r][c] == b'0' => Some(cell + 1),
        2 if r + 1 < n && horizontal[r][c] == b'0' => Some(cell + n),
        3 if c > 0 && vertical[r][c - 1] == b'0' => Some(cell - 1),
        _ => None,
    }
}

struct TreePlan {
    tree: Vec<Vec<usize>>,
    parent: Vec<usize>,
    depth: Vec<usize>,
    distances: Vec<u16>,
}

impl TreePlan {
    fn new(
        n: usize,
        root: usize,
        order: &[usize; 4],
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Self {
        let size = n * n;
        let mut tree = vec![Vec::new(); size];
        let mut parent = vec![usize::MAX; size];
        let mut depth = vec![0usize; size];
        let mut queue = VecDeque::from([root]);
        parent[root] = root;
        while let Some(v) = queue.pop_front() {
            for &direction in order {
                let Some(to) = neighbor(v, direction, n, vertical, horizontal) else {
                    continue;
                };
                if parent[to] != usize::MAX {
                    continue;
                }
                parent[to] = v;
                depth[to] = depth[v] + 1;
                add_edge(&mut tree, v, to);
                queue.push_back(to);
            }
        }
        assert!(parent.iter().all(|&p| p != usize::MAX));
        let distances = all_graph_distances(&tree);
        Self {
            tree,
            parent,
            depth,
            distances,
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

    fn complete(&self, initial: &[usize], n: usize, prefer_larger: bool) -> Vec<Operation> {
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
                let distance = self.distances[position[candidate] * size + candidate];
                let better_tie = distance == best_distance
                    && (leaf == usize::MAX
                        || (prefer_larger && candidate > leaf)
                        || (!prefer_larger && candidate < leaf));
                if distance < best_distance || better_tie {
                    best_distance = distance;
                    leaf = candidate;
                }
            }
            assert_ne!(leaf, usize::MAX);
            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&v| active[v]));
            for edge in path.windows(2) {
                let (a, b) = (edge[0], edge[1]);
                let op = adjacent_operation(a, b, n);
                apply_operation(op, &mut board, &mut position, n);
                operations.push(op);
            }
            debug_assert_eq!(board[leaf], leaf);
            active[leaf] = false;
            remaining -= 1;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
            degree[leaf] = 0;
        }
        debug_assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        assert!(operations.len() <= size * (size - 1) / 2);
        operations
    }
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        Operation {
            direction: b'H',
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        Operation {
            direction: b'V',
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
}

#[derive(Clone)]
struct Checkpoint {
    estimate: usize,
    board: Vec<usize>,
    prefix: Vec<Operation>,
}

fn retain_checkpoint(checkpoints: &mut Vec<Checkpoint>, checkpoint: Checkpoint) {
    if checkpoints
        .iter()
        .any(|saved| saved.prefix.len() == checkpoint.prefix.len())
    {
        return;
    }
    if checkpoints.len() < CHECKPOINT_LIMIT {
        checkpoints.push(checkpoint);
        return;
    }
    let (worst_index, worst_estimate) = checkpoints
        .iter()
        .enumerate()
        .max_by_key(|(_, state)| state.estimate)
        .map(|(index, state)| (index, state.estimate))
        .unwrap();
    if checkpoint.estimate < worst_estimate {
        checkpoints[worst_index] = checkpoint;
    }
}

fn save_checkpoint(
    checkpoints: &mut Vec<Checkpoint>,
    board: &[usize],
    prefix: &[Operation],
    quick_plan: &TreePlan,
    n: usize,
) {
    let fallback_count = quick_plan.complete(board, n, false).len();
    retain_checkpoint(
        checkpoints,
        Checkpoint {
            estimate: prefix.len() + fallback_count,
            board: board.to_vec(),
            prefix: prefix.to_vec(),
        },
    );
}

fn roots(n: usize) -> Vec<usize> {
    vec![
        (n / 2) * n + n / 2,
        0,
        n - 1,
        (n - 1) * n,
        n * n - 1,
        n / 2,
        (n - 1) * n + n / 2,
        (n / 2) * n,
        (n / 2) * n + n - 1,
    ]
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let size = n * n;
    let mut board: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
    let vertical: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();

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
    let graph_distances = all_graph_distances(&graph);
    assert!(graph_distances.iter().all(|&d| d != u16::MAX));
    let rectangles = rectangle_candidates(n, &vertical, &horizontal);
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

    let search_start = Instant::now();
    while prefix.len() < SEARCH_MOVE_LIMIT && search_start.elapsed().as_secs_f64() < SEARCH_TIME_SEC
    {
        let mut best_delta = 0i32;
        let mut best_operation = None;
        for &operation in &rectangles {
            let delta = operation_delta(operation, &board, &graph_distances, n);
            if delta < best_delta {
                best_delta = delta;
                best_operation = Some(operation);
            }
        }
        let Some(operation) = best_operation else {
            break;
        };
        apply_operation(operation, &mut board, &mut position, n);
        prefix.push(operation);
        if prefix.len() % CHECK_INTERVAL == 0 || best_delta <= -8 {
            save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);
        }
    }
    save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);

    let mut best: Option<(Vec<Operation>, Vec<Operation>)> = None;
    for (root_index, root) in roots(n).into_iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let prefer_larger = (root_index + order_index) % 2 == 1;
            for checkpoint in &checkpoints {
                let fallback = plan.complete(&checkpoint.board, n, prefer_larger);
                let total = checkpoint.prefix.len() + fallback.len();
                if total > 100_000 {
                    continue;
                }
                let improves = match &best {
                    None => true,
                    Some((saved_prefix, saved_fallback)) => {
                        total < saved_prefix.len() + saved_fallback.len()
                    }
                };
                if improves {
                    best = Some((checkpoint.prefix.clone(), fallback));
                }
            }
        }
    }

    let (mut best_prefix, best_fallback) = best.expect("a safe exact candidate exists");
    best_prefix.extend(best_fallback);
    assert!(best_prefix.len() <= 100_000);
    let mut output = String::new();
    for operation in best_prefix {
        writeln!(
            output,
            "{} {} {} {} {}",
            operation.direction as char, operation.r, operation.c, operation.h, operation.w
        )
        .unwrap();
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
