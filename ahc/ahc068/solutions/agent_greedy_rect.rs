use std::collections::VecDeque;
use std::io::{self, Read};

const GREEDY_OPERATION_LIMIT: usize = 10_000;

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

impl Operation {
    fn area(self) -> usize {
        self.h * self.w
    }
}

fn cell_cost(tile: usize, at: usize, n: usize) -> i32 {
    let tr = tile / n;
    let tc = tile % n;
    let r = at / n;
    let c = at % n;
    4 * (tr.abs_diff(r) + tc.abs_diff(c)) as i32 + i32::from(tile != at)
}

fn improvement(board: &[usize], op: Operation, n: usize) -> i32 {
    let mut old_cost = 0;
    let mut new_cost = 0;
    match op.d {
        Direction::V => {
            let dh = op.h / 2;
            for x in 0..dh {
                for y in 0..op.w {
                    let a = (op.r + x) * n + op.c + y;
                    let b = (op.r + dh + x) * n + op.c + y;
                    old_cost += cell_cost(board[a], a, n) + cell_cost(board[b], b, n);
                    new_cost += cell_cost(board[a], b, n) + cell_cost(board[b], a, n);
                }
            }
        }
        Direction::H => {
            let dw = op.w / 2;
            for x in 0..op.h {
                for y in 0..dw {
                    let a = (op.r + x) * n + op.c + y;
                    let b = (op.r + x) * n + op.c + dw + y;
                    old_cost += cell_cost(board[a], a, n) + cell_cost(board[b], b, n);
                    new_cost += cell_cost(board[a], b, n) + cell_cost(board[b], a, n);
                }
            }
        }
    }
    old_cost - new_cost
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

fn make_rectangle_candidates(
    n: usize,
    vertical_walls: &[Vec<bool>],
    horizontal_walls: &[Vec<bool>],
) -> Vec<Operation> {
    let mut candidates = Vec::new();
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
                        candidates.push(Operation {
                            d: Direction::V,
                            r,
                            c,
                            h,
                            w,
                        });
                    }
                    if w % 2 == 0 {
                        candidates.push(Operation {
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
    candidates.sort_unstable_by(|a, b| {
        b.area()
            .cmp(&a.area())
            .then_with(|| b.h.max(b.w).cmp(&a.h.max(a.w)))
    });
    candidates
}

fn adjacent_operation(a: usize, b: usize, n: usize) -> Operation {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ar == br {
        debug_assert_eq!(ac.abs_diff(bc), 1);
        Operation {
            d: Direction::H,
            r: ar,
            c: ac.min(bc),
            h: 1,
            w: 2,
        }
    } else {
        debug_assert_eq!(ar.abs_diff(br), 1);
        debug_assert_eq!(ac, bc);
        Operation {
            d: Direction::V,
            r: ar.min(br),
            c: ac,
            h: 2,
            w: 1,
        }
    }
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

/// Sorts any feasible permutation on the wall graph using only adjacent swaps.
///
/// A BFS tree is peeled from its deepest leaves.  Before removing a leaf, its
/// final token is routed to it along the still-active part of the tree.
fn finish_on_spanning_forest(
    board: &mut [usize],
    positions: &mut [usize],
    graph: &[Vec<usize>],
    n: usize,
    answer: &mut Vec<Operation>,
) {
    let vertices = n * n;
    let mut tree = vec![Vec::new(); vertices];
    let mut depth = vec![usize::MAX; vertices];
    let mut component = vec![usize::MAX; vertices];
    let mut is_root = vec![false; vertices];
    let mut queue = VecDeque::new();
    for root in 0..vertices {
        if depth[root] != usize::MAX {
            continue;
        }
        is_root[root] = true;
        depth[root] = 0;
        component[root] = root;
        queue.push_back(root);
        while let Some(v) = queue.pop_front() {
            for &to in &graph[v] {
                if depth[to] == usize::MAX {
                    depth[to] = depth[v] + 1;
                    component[to] = root;
                    tree[v].push(to);
                    tree[to].push(v);
                    queue.push_back(to);
                }
            }
        }
    }

    let mut order: Vec<usize> = (0..vertices).filter(|&v| !is_root[v]).collect();
    order.sort_unstable_by_key(|&v| std::cmp::Reverse(depth[v]));
    let mut active = vec![true; vertices];

    for target in order {
        let source = positions[target];
        assert_eq!(
            component[source], component[target],
            "instance is not sortable within its wall components"
        );
        let mut previous = vec![usize::MAX; vertices];
        let mut bfs = VecDeque::new();
        previous[source] = source;
        bfs.push_back(source);
        while let Some(v) = bfs.pop_front() {
            if v == target {
                break;
            }
            for &to in &tree[v] {
                if active[to] && previous[to] == usize::MAX {
                    previous[to] = v;
                    bfs.push_back(to);
                }
            }
        }
        assert_ne!(previous[target], usize::MAX);

        let mut reversed_path = vec![target];
        while *reversed_path.last().unwrap() != source {
            reversed_path.push(previous[*reversed_path.last().unwrap()]);
        }
        reversed_path.reverse();
        for edge in reversed_path.windows(2) {
            let op = adjacent_operation(edge[0], edge[1], n);
            apply(board, positions, op, n);
            answer.push(op);
        }
        debug_assert_eq!(board[target], target);
        active[target] = false;
    }
    assert!(board.iter().enumerate().all(|(i, &tile)| i == tile));
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut scanner = Scanner::new(&input);
    let n: usize = scanner.next();
    assert_eq!(n, 20);

    let raw_board: Vec<usize> = (0..n * n).map(|_| scanner.next()).collect();
    let offset = usize::from(raw_board.iter().copied().min() == Some(1));
    let mut board: Vec<usize> = raw_board.into_iter().map(|x| x - offset).collect();
    assert!(board.iter().all(|&x| x < n * n));

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
    let mut answer = Vec::new();

    // Consider each large, wall-free rectangle once, largest first.  This is a
    // deliberately bounded construction phase; the tree phase below guarantees
    // completion even if this greedy pass reaches a local optimum.
    for op in make_rectangle_candidates(n, &vertical_walls, &horizontal_walls) {
        if answer.len() == GREEDY_OPERATION_LIMIT {
            break;
        }
        if improvement(&board, op, n) > 0 {
            apply(&mut board, &mut positions, op, n);
            answer.push(op);
        }
    }

    let graph = wall_graph(n, &vertical_walls, &horizontal_walls);
    finish_on_spanning_forest(&mut board, &mut positions, &graph, n, &mut answer);
    assert!(answer.len() <= 100_000);

    let mut output = String::new();
    for op in answer {
        let d = if op.d == Direction::V { 'V' } else { 'H' };
        output.push_str(&format!("{} {} {} {} {}\n", d, op.r, op.c, op.h, op.w));
    }
    print!("{output}");
}
