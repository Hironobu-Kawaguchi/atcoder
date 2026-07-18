use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};

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
        self.iter
            .next()
            .expect("unexpected end of input")
            .parse()
            .expect("failed to parse input token")
    }
}

fn add_edge(graph: &mut [Vec<usize>], a: usize, b: usize) {
    graph[a].push(b);
    graph[b].push(a);
}

/// Builds a breadth-first spanning tree of the wall-free cell graph.
fn build_spanning_tree(graph: &[Vec<usize>], root: usize) -> Vec<Vec<usize>> {
    let vertex_count = graph.len();
    let mut tree = vec![Vec::new(); vertex_count];
    let mut seen = vec![false; vertex_count];
    let mut queue = VecDeque::new();
    seen[root] = true;
    queue.push_back(root);

    while let Some(v) = queue.pop_front() {
        for &to in &graph[v] {
            if seen[to] {
                continue;
            }
            seen[to] = true;
            add_edge(&mut tree, v, to);
            queue.push_back(to);
        }
    }

    assert!(
        seen.iter().all(|&visited| visited),
        "the wall-free cell graph must be connected"
    );
    tree
}

/// Returns the unique path in the remaining part of a tree.
fn active_path(tree: &[Vec<usize>], active: &[bool], start: usize, goal: usize) -> Vec<usize> {
    if start == goal {
        return vec![start];
    }

    let vertex_count = tree.len();
    let mut parent = vec![usize::MAX; vertex_count];
    let mut queue = VecDeque::new();
    parent[start] = start;
    queue.push_back(start);

    while let Some(v) = queue.pop_front() {
        for &to in &tree[v] {
            if !active[to] || parent[to] != usize::MAX {
                continue;
            }
            parent[to] = v;
            if to == goal {
                queue.clear();
                break;
            }
            queue.push_back(to);
        }
    }
    assert_ne!(parent[goal], usize::MAX, "active tree path must exist");

    let mut reversed = vec![goal];
    let mut v = goal;
    while v != start {
        v = parent[v];
        reversed.push(v);
    }
    reversed.reverse();
    reversed
}

/// Emits the legal 2-cell rectangle operation corresponding to a tree edge.
fn emit_adjacent_swap(output: &mut String, a: usize, b: usize, n: usize) {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ac == bc {
        debug_assert_eq!(ar.abs_diff(br), 1);
        let r = ar.min(br);
        writeln!(output, "V {r} {ac} 2 1").unwrap();
    } else {
        debug_assert_eq!(ar, br);
        debug_assert_eq!(ac.abs_diff(bc), 1);
        let c = ac.min(bc);
        writeln!(output, "H {ar} {c} 1 2").unwrap();
    }
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner::new(input);
    let n: usize = scanner.next();
    let vertex_count = n * n;

    let mut card_at = vec![0usize; vertex_count];
    let mut position = vec![usize::MAX; vertex_count];
    for cell in 0..vertex_count {
        let card: usize = scanner.next();
        assert!(card < vertex_count, "card number is outside 0..N^2");
        assert_eq!(position[card], usize::MAX, "card numbers must be unique");
        card_at[cell] = card;
        position[card] = cell;
    }

    let vertical_walls: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal_walls: Vec<Vec<u8>> = (0..n.saturating_sub(1))
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();

    let mut graph = vec![Vec::new(); vertex_count];
    for r in 0..n {
        assert_eq!(vertical_walls[r].len(), n.saturating_sub(1));
        for c in 0..n.saturating_sub(1) {
            if vertical_walls[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, r * n + c + 1);
            }
        }
    }
    for r in 0..n.saturating_sub(1) {
        assert_eq!(horizontal_walls[r].len(), n);
        for c in 0..n {
            if horizontal_walls[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, (r + 1) * n + c);
            }
        }
    }

    if vertex_count <= 1 {
        return String::new();
    }

    // A central root tends to keep the BFS tree shallow, although correctness
    // and the 79,800-operation worst-case bound do not depend on this choice.
    let root = (n / 2) * n + n / 2;
    let tree = build_spanning_tree(&graph, root);
    let mut active = vec![true; vertex_count];
    let mut degree: Vec<usize> = tree.iter().map(Vec::len).collect();
    let mut leaves = VecDeque::new();
    for (v, &d) in degree.iter().enumerate() {
        if d == 1 {
            leaves.push_back(v);
        }
    }

    let mut remaining = vertex_count;
    let mut operation_count = 0usize;
    let mut output = String::new();

    while remaining > 1 {
        let leaf = loop {
            let candidate = leaves.pop_front().expect("an active tree has a leaf");
            if active[candidate] && degree[candidate] == 1 {
                break candidate;
            }
        };

        // In row-major target order, card `leaf` belongs to cell `leaf`.
        // Previously removed cells already hold their own cards, so this card
        // is necessarily still inside the active subtree.
        let source = position[leaf];
        assert!(active[source]);
        let path = active_path(&tree, &active, source, leaf);
        for edge in path.windows(2) {
            let a = edge[0];
            let b = edge[1];
            emit_adjacent_swap(&mut output, a, b, n);
            card_at.swap(a, b);
            position[card_at[a]] = a;
            position[card_at[b]] = b;
            operation_count += 1;
        }
        debug_assert_eq!(card_at[leaf], leaf);

        active[leaf] = false;
        remaining -= 1;
        for &to in &tree[leaf] {
            if active[to] {
                degree[to] -= 1;
                if degree[to] == 1 {
                    leaves.push_back(to);
                }
            }
        }
        degree[leaf] = 0;
    }

    debug_assert!(
        card_at.iter().enumerate().all(|(cell, &card)| cell == card),
        "leaf fixing must finish in row-major order"
    );
    assert!(operation_count <= 100_000, "operation limit exceeded");
    output
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .expect("failed to read stdin");
    print!("{}", solve(&input));
}
