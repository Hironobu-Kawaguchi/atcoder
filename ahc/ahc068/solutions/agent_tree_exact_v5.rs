use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};

const HALF_SWEEP_LIMIT: usize = 20;
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
    d: u8,
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
    let mut swap = |a: usize, b: usize| {
        board.swap(a, b);
        position[board[a]] = a;
        position[board[b]] = b;
    };
    if op.d == b'V' {
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

fn adjacent(a: usize, b: usize, n: usize) -> Operation {
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

fn all_distances(graph: &[Vec<usize>]) -> Vec<u16> {
    let size = graph.len();
    let mut result = vec![u16::MAX; size * size];
    for source in 0..size {
        let mut queue = VecDeque::from([source]);
        result[source * size + source] = 0;
        while let Some(v) = queue.pop_front() {
            let next = result[source * size + v] + 1;
            for &to in &graph[v] {
                let index = source * size + to;
                if result[index] == u16::MAX {
                    result[index] = next;
                    queue.push_back(to);
                }
            }
        }
    }
    result
}

fn horizontal_segments(n: usize, vertical: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut result = Vec::new();
    for r in 0..n {
        let mut start = 0;
        for c in 0..n - 1 {
            if vertical[r][c] == b'1' {
                result.push((start..=c).map(|x| r * n + x).collect());
                start = c + 1;
            }
        }
        result.push((start..n).map(|x| r * n + x).collect());
    }
    result
}

fn vertical_segments(n: usize, horizontal: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut result = Vec::new();
    for c in 0..n {
        let mut start = 0;
        for r in 0..n - 1 {
            if horizontal[r][c] == b'1' {
                result.push((start..=r).map(|x| x * n + c).collect());
                start = r + 1;
            }
        }
        result.push((start..n).map(|x| x * n + c).collect());
    }
    result
}

/// Minimum-cost perfect assignment, row (card) -> column (segment port).
fn hungarian(cost: &[Vec<i32>]) -> (i32, Vec<usize>) {
    let n = cost.len();
    let mut u = vec![0i32; n + 1];
    let mut v = vec![0i32; n + 1];
    let mut p = vec![0usize; n + 1];
    let mut way = vec![0usize; n + 1];
    for i in 1..=n {
        p[0] = i;
        let mut j0 = 0;
        let mut minv = vec![i32::MAX / 4; n + 1];
        let mut used = vec![false; n + 1];
        loop {
            used[j0] = true;
            let i0 = p[j0];
            let mut delta = i32::MAX / 4;
            let mut j1 = 0;
            for j in 1..=n {
                if !used[j] {
                    let cur = cost[i0 - 1][j - 1] - u[i0] - v[j];
                    if cur < minv[j] {
                        minv[j] = cur;
                        way[j] = j0;
                    }
                    if minv[j] < delta {
                        delta = minv[j];
                        j1 = j;
                    }
                }
            }
            for j in 0..=n {
                if used[j] {
                    u[p[j]] += delta;
                    v[j] -= delta;
                } else {
                    minv[j] -= delta;
                }
            }
            j0 = j1;
            if p[j0] == 0 {
                break;
            }
        }
        loop {
            let j1 = way[j0];
            p[j0] = p[j1];
            j0 = j1;
            if j0 == 0 {
                break;
            }
        }
    }
    let mut assignment = vec![0usize; n];
    for j in 1..=n {
        assignment[p[j] - 1] = j - 1;
    }
    (-v[0], assignment)
}

/// Realizes an arbitrary permutation within one open segment. Equal-block
/// exchanges reduce displacement first; insertion swaps guarantee completion.
fn permute_segment(
    cells: &[usize],
    desired_slot: &[usize],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    output: &mut Vec<Operation>,
) {
    let length = cells.len();
    let inversion_count = |keys: &[usize]| -> usize {
        let mut count = 0;
        for i in 0..keys.len() {
            for j in i + 1..keys.len() {
                count += usize::from(keys[i] > keys[j]);
            }
        }
        count
    };
    loop {
        let keys: Vec<usize> = cells
            .iter()
            .map(|&cell| desired_slot[board[cell]])
            .collect();
        let current_inversions = inversion_count(&keys);
        let mut best_inversions = current_inversions;
        let mut best = None;
        for start in 0..length {
            for half in 2..=(length - start) / 2 {
                let mut next = keys.clone();
                for k in 0..half {
                    next.swap(start + k, start + half + k);
                }
                let value = inversion_count(&next);
                if value < best_inversions {
                    best_inversions = value;
                    best = Some((start, half));
                }
            }
        }
        // One block operation must save at least two eventual adjacent swaps.
        if best_inversions + 1 >= current_inversions {
            break;
        }
        let Some((start, half)) = best else { break };
        let first = cells[0];
        let op = if cells.len() == 1 || cells[1] == first + 1 {
            Operation {
                d: b'H',
                r: first / n,
                c: first % n + start,
                h: 1,
                w: 2 * half,
            }
        } else {
            Operation {
                d: b'V',
                r: first / n + start,
                c: first % n,
                h: 2 * half,
                w: 1,
            }
        };
        apply(op, board, position, n);
        output.push(op);
    }
    for target in 0..length {
        let mut at = target;
        while desired_slot[board[cells[at]]] != target {
            at += 1;
        }
        while at > target {
            let op = adjacent(cells[at - 1], cells[at], n);
            apply(op, board, position, n);
            output.push(op);
            at -= 1;
        }
    }
}

fn crossbar_sweep(
    segments: &[Vec<usize>],
    board: &mut [usize],
    position: &mut [usize],
    distances: &[u16],
    n: usize,
    output: &mut Vec<Operation>,
) -> bool {
    let size = board.len();
    let mut changed = false;
    let mut desired_slot = vec![usize::MAX; size];
    for cells in segments {
        if cells.len() <= 1 {
            continue;
        }
        let cards: Vec<usize> = cells.iter().map(|&cell| board[cell]).collect();
        let cost: Vec<Vec<i32>> = cards
            .iter()
            .map(|&card| {
                cells
                    .iter()
                    .map(|&cell| i32::from(distances[card * size + cell]))
                    .collect()
            })
            .collect();
        let old_cost: i32 = cards
            .iter()
            .zip(cells)
            .map(|(&card, &cell)| i32::from(distances[card * size + cell]))
            .sum();
        let (new_cost, assignment) = hungarian(&cost);
        if new_cost >= old_cost {
            continue;
        }
        changed = true;
        for (index, &card) in cards.iter().enumerate() {
            desired_slot[card] = assignment[index];
        }
        permute_segment(cells, &desired_slot, board, position, n, output);
    }
    changed
}

fn tree_neighbor(
    cell: usize,
    d: usize,
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Option<usize> {
    let (r, c) = (cell / n, cell % n);
    match d {
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
    distance: Vec<u16>,
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
        let mut depth = vec![0; size];
        parent[root] = root;
        let mut queue = VecDeque::from([root]);
        while let Some(v) = queue.pop_front() {
            for &d in order {
                if let Some(to) = tree_neighbor(v, d, n, vertical, horizontal) {
                    if parent[to] == usize::MAX {
                        parent[to] = v;
                        depth[to] = depth[v] + 1;
                        add_edge(&mut tree, v, to);
                        queue.push_back(to);
                    }
                }
            }
        }
        assert!(parent.iter().all(|&p| p != usize::MAX));
        let distance = all_distances(&tree);
        Self {
            tree,
            parent,
            depth,
            distance,
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

    fn complete(&self, initial: &[usize], n: usize, reverse_tie: bool) -> Vec<Operation> {
        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut result = Vec::new();
        for _ in 1..size {
            let mut leaf = usize::MAX;
            let mut best = u16::MAX;
            for v in 0..size {
                if active[v] && degree[v] == 1 {
                    let d = self.distance[position[v] * size + v];
                    if d < best || (d == best && (leaf == usize::MAX || reverse_tie == (v > leaf)))
                    {
                        best = d;
                        leaf = v;
                    }
                }
            }
            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&v| active[v]));
            for edge in path.windows(2) {
                let op = adjacent(edge[0], edge[1], n);
                apply(op, &mut board, &mut position, n);
                result.push(op);
            }
            active[leaf] = false;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
            degree[leaf] = 0;
        }
        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        result
    }
}

/// Reschedules adjacent swaps by preserving only same-cell dependencies.
/// Every ready layer is a matching, so parallel swaps can be fused safely.
fn schedule_and_fuse(
    raw: &[Operation],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    fn pair(op: Operation, n: usize) -> (usize, usize) {
        let a = op.r * n + op.c;
        (a, if op.d == b'H' { a + 1 } else { a + n })
    }
    fn emit_layer(
        layer: &[usize],
        raw: &[Operation],
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        output: &mut Vec<Operation>,
    ) {
        for direction in [b'H', b'V'] {
            let mut ops: Vec<Operation> = layer
                .iter()
                .map(|&i| raw[i])
                .filter(|op| op.d == direction)
                .collect();
            if direction == b'H' {
                ops.sort_unstable_by_key(|op| (op.c, op.r));
            } else {
                ops.sort_unstable_by_key(|op| (op.r, op.c));
            }
            let mut at = 0;
            while at < ops.len() {
                let first = ops[at];
                let mut end = at + 1;
                while end < ops.len() {
                    let previous = ops[end - 1];
                    let next = ops[end];
                    let extends = if direction == b'H' {
                        next.c == first.c
                            && next.r == previous.r + 1
                            && horizontal[previous.r][first.c] == b'0'
                            && horizontal[previous.r][first.c + 1] == b'0'
                    } else {
                        next.r == first.r
                            && next.c == previous.c + 1
                            && vertical[first.r][previous.c] == b'0'
                            && vertical[first.r + 1][previous.c] == b'0'
                    };
                    if !extends {
                        break;
                    }
                    end += 1;
                }
                let length = end - at;
                output.push(if direction == b'H' {
                    Operation {
                        d: direction,
                        r: first.r,
                        c: first.c,
                        h: length,
                        w: 2,
                    }
                } else {
                    Operation {
                        d: direction,
                        r: first.r,
                        c: first.c,
                        h: 2,
                        w: length,
                    }
                });
                at = end;
            }
        }
    }

    let mut outgoing = vec![Vec::new(); raw.len()];
    let mut indegree = vec![0usize; raw.len()];
    let mut last = vec![usize::MAX; n * n];
    for (event, &op) in raw.iter().enumerate() {
        debug_assert_eq!(op.h * op.w, 2);
        let (a, b) = pair(op, n);
        let (pa, pb) = (last[a], last[b]);
        if pa != usize::MAX {
            outgoing[pa].push(event);
            indegree[event] += 1;
        }
        if pb != usize::MAX && pb != pa {
            outgoing[pb].push(event);
            indegree[event] += 1;
        }
        last[a] = event;
        last[b] = event;
    }
    let mut ready: Vec<usize> = (0..raw.len()).filter(|&i| indegree[i] == 0).collect();
    let mut output = Vec::new();
    let mut processed = 0;
    while !ready.is_empty() {
        let layer = std::mem::take(&mut ready);
        emit_layer(&layer, raw, vertical, horizontal, &mut output);
        processed += layer.len();
        for event in layer {
            for &to in &outgoing[event] {
                indegree[to] -= 1;
                if indegree[to] == 0 {
                    ready.push(to);
                }
            }
        }
    }
    assert_eq!(processed, raw.len());
    output
}

#[derive(Clone)]
struct Checkpoint {
    estimate: usize,
    board: Vec<usize>,
    prefix: Vec<Operation>,
}

fn retain_checkpoint(saved: &mut Vec<Checkpoint>, candidate: Checkpoint) {
    if saved.iter().any(|state| state.board == candidate.board) {
        return;
    }
    if saved.len() < CHECKPOINT_LIMIT {
        saved.push(candidate);
    } else {
        let (worst, value) = saved
            .iter()
            .enumerate()
            .max_by_key(|(_, state)| state.estimate)
            .map(|(i, state)| (i, state.estimate))
            .unwrap();
        if candidate.estimate < value {
            saved[worst] = candidate;
        }
    }
}

fn route_trajectory(
    initial: &[usize],
    first_horizontal: bool,
    horizontal_segments: &[Vec<usize>],
    vertical_segments: &[Vec<usize>],
    distances: &[u16],
    quick: &TreePlan,
    n: usize,
    saved: &mut Vec<Checkpoint>,
) {
    let size = initial.len();
    let mut board = initial.to_vec();
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut prefix = Vec::new();
    let mut unchanged = 0;
    for step in 0..HALF_SWEEP_LIMIT {
        let horizontal = (step % 2 == 0) == first_horizontal;
        let segments = if horizontal {
            horizontal_segments
        } else {
            vertical_segments
        };
        let changed = crossbar_sweep(
            segments,
            &mut board,
            &mut position,
            distances,
            n,
            &mut prefix,
        );
        if changed {
            unchanged = 0;
            let fallback = quick.complete(&board, n, false).len();
            retain_checkpoint(
                saved,
                Checkpoint {
                    estimate: prefix.len() + fallback,
                    board: board.clone(),
                    prefix: prefix.clone(),
                },
            );
        } else {
            unchanged += 1;
            if unchanged == 2 {
                break;
            }
        }
    }
}

fn valid_solution(
    operations: &[Operation],
    initial: &[usize],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> bool {
    let mut board = initial.to_vec();
    let mut position = vec![0; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    for &op in operations {
        if op.r + op.h > n || op.c + op.w > n || op.h == 0 || op.w == 0 {
            return false;
        }
        if (op.d == b'V' && op.h % 2 != 0) || (op.d == b'H' && op.w % 2 != 0) {
            return false;
        }
        for r in op.r..op.r + op.h {
            for c in op.c..op.c + op.w.saturating_sub(1) {
                if vertical[r][c] == b'1' {
                    return false;
                }
            }
        }
        for r in op.r..op.r + op.h.saturating_sub(1) {
            for c in op.c..op.c + op.w {
                if horizontal[r][c] == b'1' {
                    return false;
                }
            }
        }
        apply(op, &mut board, &mut position, n);
    }
    board.iter().enumerate().all(|(cell, &card)| cell == card)
}

fn solve(input: &str) -> String {
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
    assert!(distances.iter().all(|&d| d != u16::MAX));
    let h_segments = horizontal_segments(n, &vertical);
    let v_segments = vertical_segments(n, &horizontal);
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
    let quick = TreePlan::new(n, center, &ORDERS[0], &vertical, &horizontal);
    let mut checkpoints = vec![Checkpoint {
        estimate: quick.complete(&initial, n, false).len(),
        board: initial.clone(),
        prefix: Vec::new(),
    }];
    route_trajectory(
        &initial,
        true,
        &h_segments,
        &v_segments,
        &distances,
        &quick,
        n,
        &mut checkpoints,
    );
    route_trajectory(
        &initial,
        false,
        &h_segments,
        &v_segments,
        &distances,
        &quick,
        n,
        &mut checkpoints,
    );

    let roots = [
        center,
        0,
        n - 1,
        (n - 1) * n,
        size - 1,
        n / 2,
        (n - 1) * n + n / 2,
        (n / 2) * n,
        (n / 2) * n + n - 1,
    ];
    let mut best: Option<Vec<Operation>> = None;
    for (ri, &root) in roots.iter().enumerate() {
        for (oi, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            for checkpoint in &checkpoints {
                let raw_fallback = plan.complete(&checkpoint.board, n, (ri + oi) % 2 == 1);
                let fallback = schedule_and_fuse(&raw_fallback, n, &vertical, &horizontal);
                let total = checkpoint.prefix.len() + fallback.len();
                let already_better = match &best {
                    Some(ops) => ops.len() <= total,
                    None => false,
                };
                if total > 100_000 || already_better {
                    continue;
                }
                let mut result = checkpoint.prefix.clone();
                result.extend(fallback);
                best = Some(result);
            }
        }
    }
    let mut result = best.expect("empty-prefix exact fallback is safe");
    if !valid_solution(&result, &initial, n, &vertical, &horizontal) {
        result = quick.complete(&initial, n, false);
    }
    assert!(valid_solution(&result, &initial, n, &vertical, &horizontal));
    let mut output = String::new();
    for op in result {
        writeln!(
            output,
            "{} {} {} {} {}",
            op.d as char, op.r, op.c, op.h, op.w
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
