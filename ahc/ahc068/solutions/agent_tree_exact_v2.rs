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

fn neighbor(
    cell: usize,
    direction: usize,
    n: usize,
    vertical_walls: &[Vec<u8>],
    horizontal_walls: &[Vec<u8>],
) -> Option<usize> {
    let (r, c) = (cell / n, cell % n);
    match direction {
        0 if r > 0 && horizontal_walls[r - 1][c] == b'0' => Some(cell - n),
        1 if c + 1 < n && vertical_walls[r][c] == b'0' => Some(cell + 1),
        2 if r + 1 < n && horizontal_walls[r][c] == b'0' => Some(cell + n),
        3 if c > 0 && vertical_walls[r][c - 1] == b'0' => Some(cell - 1),
        _ => None,
    }
}

/// Builds one deterministic BFS spanning tree using the specified direction order.
fn build_spanning_tree(
    n: usize,
    root: usize,
    direction_order: &[usize; 4],
    vertical_walls: &[Vec<u8>],
    horizontal_walls: &[Vec<u8>],
) -> (Vec<Vec<usize>>, Vec<usize>, Vec<usize>) {
    let vertex_count = n * n;
    let mut tree = vec![Vec::new(); vertex_count];
    let mut parent = vec![usize::MAX; vertex_count];
    let mut depth = vec![0usize; vertex_count];
    let mut queue = VecDeque::new();
    parent[root] = root;
    queue.push_back(root);

    while let Some(v) = queue.pop_front() {
        for &direction in direction_order {
            let Some(to) = neighbor(v, direction, n, vertical_walls, horizontal_walls) else {
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

    assert!(
        parent.iter().all(|&p| p != usize::MAX),
        "the wall-free cell graph must be connected"
    );
    (tree, parent, depth)
}

/// Precomputes all tree distances in O(M^2), where M=N^2.
fn all_tree_distances(tree: &[Vec<usize>]) -> Vec<u16> {
    let vertex_count = tree.len();
    let mut distances = vec![u16::MAX; vertex_count * vertex_count];
    let mut queue = VecDeque::with_capacity(vertex_count);

    for source in 0..vertex_count {
        distances[source * vertex_count + source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            let next_distance = distances[source * vertex_count + v] + 1;
            for &to in &tree[v] {
                let index = source * vertex_count + to;
                if distances[index] == u16::MAX {
                    distances[index] = next_distance;
                    queue.push_back(to);
                }
            }
        }
    }
    distances
}

/// Returns the unique tree path from start to goal using rooted-tree parents.
fn tree_path(start: usize, goal: usize, parent: &[usize], depth: &[usize]) -> Vec<usize> {
    let (mut a, mut b) = (start, goal);
    let mut left = vec![a];
    let mut right = vec![b];

    while depth[a] > depth[b] {
        a = parent[a];
        left.push(a);
    }
    while depth[b] > depth[a] {
        b = parent[b];
        right.push(b);
    }
    while a != b {
        a = parent[a];
        b = parent[b];
        left.push(a);
        right.push(b);
    }

    left.extend(right[..right.len() - 1].iter().rev().copied());
    left
}

/// Simulates exact leaf fixing and returns its adjacent-swap edge sequence.
fn simulate_candidate(
    initial_cards: &[usize],
    tree: &[Vec<usize>],
    parent: &[usize],
    depth: &[usize],
    distances: &[u16],
    prefer_larger_leaf_on_tie: bool,
) -> Vec<(usize, usize)> {
    let vertex_count = initial_cards.len();
    let mut card_at = initial_cards.to_vec();
    let mut position = vec![usize::MAX; vertex_count];
    for (cell, &card) in card_at.iter().enumerate() {
        position[card] = cell;
    }

    let mut active = vec![true; vertex_count];
    let mut degree: Vec<usize> = tree.iter().map(Vec::len).collect();
    let mut remaining = vertex_count;
    let mut operations = Vec::new();

    while remaining > 1 {
        let mut chosen_leaf = usize::MAX;
        let mut chosen_distance = u16::MAX;
        for leaf in 0..vertex_count {
            if !active[leaf] || degree[leaf] != 1 {
                continue;
            }
            let distance = distances[position[leaf] * vertex_count + leaf];
            let tie_is_better = distance == chosen_distance
                && (chosen_leaf == usize::MAX
                    || (prefer_larger_leaf_on_tie && leaf > chosen_leaf)
                    || (!prefer_larger_leaf_on_tie && leaf < chosen_leaf));
            if distance < chosen_distance || tie_is_better {
                chosen_distance = distance;
                chosen_leaf = leaf;
            }
        }
        assert_ne!(chosen_leaf, usize::MAX, "an active tree must have a leaf");

        let source = position[chosen_leaf];
        assert!(active[source]);
        let path = tree_path(source, chosen_leaf, parent, depth);
        debug_assert!(path.iter().all(|&v| active[v]));
        for edge in path.windows(2) {
            let (a, b) = (edge[0], edge[1]);
            card_at.swap(a, b);
            position[card_at[a]] = a;
            position[card_at[b]] = b;
            operations.push((a, b));
        }
        debug_assert_eq!(card_at[chosen_leaf], chosen_leaf);

        active[chosen_leaf] = false;
        remaining -= 1;
        for &to in &tree[chosen_leaf] {
            if active[to] {
                degree[to] -= 1;
            }
        }
        degree[chosen_leaf] = 0;
    }

    debug_assert!(
        card_at.iter().enumerate().all(|(cell, &card)| cell == card),
        "leaf fixing must finish in row-major order"
    );
    assert!(operations.len() <= 100_000, "operation limit exceeded");
    operations
}

fn emit_adjacent_swap(output: &mut String, a: usize, b: usize, n: usize) {
    let (ar, ac) = (a / n, a % n);
    let (br, bc) = (b / n, b % n);
    if ac == bc {
        debug_assert_eq!(ar.abs_diff(br), 1);
        writeln!(output, "V {} {} 2 1", ar.min(br), ac).unwrap();
    } else {
        debug_assert_eq!(ar, br);
        debug_assert_eq!(ac.abs_diff(bc), 1);
        writeln!(output, "H {} {} 1 2", ar, ac.min(bc)).unwrap();
    }
}

fn root_candidates(n: usize) -> Vec<usize> {
    let coordinates = [0, n / 4, n / 2, 3 * n / 4, n - 1];
    let mut roots = Vec::new();
    for &r in &coordinates {
        for &c in &coordinates {
            let root = r * n + c;
            if !roots.contains(&root) {
                roots.push(root);
            }
        }
    }
    roots
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner::new(input);
    let n: usize = scanner.next();
    let vertex_count = n * n;

    let mut initial_cards = vec![0usize; vertex_count];
    let mut seen_card = vec![false; vertex_count];
    for card in &mut initial_cards {
        *card = scanner.next();
        assert!(*card < vertex_count, "card number is outside 0..N^2");
        assert!(!seen_card[*card], "card numbers must be unique");
        seen_card[*card] = true;
    }

    let vertical_walls: Vec<Vec<u8>> = (0..n)
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    let horizontal_walls: Vec<Vec<u8>> = (0..n.saturating_sub(1))
        .map(|_| scanner.next::<String>().into_bytes())
        .collect();
    for row in &vertical_walls {
        assert_eq!(row.len(), n.saturating_sub(1));
    }
    for row in &horizontal_walls {
        assert_eq!(row.len(), n);
    }

    if vertex_count <= 1 {
        return String::new();
    }

    // Eight cyclic/reversed cardinal preferences provide meaningfully
    // different BFS trees without making candidate search too expensive.
    const DIRECTION_ORDERS: [[usize; 4]; 8] = [
        [0, 1, 2, 3],
        [1, 2, 3, 0],
        [2, 3, 0, 1],
        [3, 0, 1, 2],
        [0, 3, 2, 1],
        [3, 2, 1, 0],
        [2, 1, 0, 3],
        [1, 0, 3, 2],
    ];

    let roots = root_candidates(n);
    let mut best_operations: Option<Vec<(usize, usize)>> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, direction_order) in DIRECTION_ORDERS.iter().enumerate() {
            let (tree, parent, depth) =
                build_spanning_tree(n, root, direction_order, &vertical_walls, &horizontal_walls);
            let distances = all_tree_distances(&tree);
            let operations = simulate_candidate(
                &initial_cards,
                &tree,
                &parent,
                &depth,
                &distances,
                (root_index + order_index) % 2 == 1,
            );
            let improves = match &best_operations {
                None => true,
                Some(best) => operations.len() < best.len(),
            };
            if improves {
                best_operations = Some(operations);
            }
        }
    }

    let best_operations = best_operations.expect("at least one candidate is generated");
    let mut output = String::new();
    for (a, b) in best_operations {
        emit_adjacent_swap(&mut output, a, b, n);
    }
    output
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .expect("failed to read stdin");
    print!("{}", solve(&input));
}
