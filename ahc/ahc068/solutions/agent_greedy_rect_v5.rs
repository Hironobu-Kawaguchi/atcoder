use std::collections::{HashMap, HashSet, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const LINE_BEAM: usize = 200;
const LINE_DEPTH: usize = 14;
const ROUTING_TIME: f64 = 1.08;

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
struct Op {
    d: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn swap_cells(a: usize, b: usize, board: &mut [usize], pos: &mut [usize]) {
    board.swap(a, b);
    pos[board[a]] = a;
    pos[board[b]] = b;
}

fn apply(op: Op, board: &mut [usize], pos: &mut [usize], n: usize) {
    if op.d == b'H' {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                swap_cells(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                    board,
                    pos,
                );
            }
        }
    } else {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                swap_cells(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                    board,
                    pos,
                );
            }
        }
    }
}

fn graph(n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut g = vec![Vec::new(); n * n];
    for r in 0..n {
        for c in 0..n {
            let x = r * n + c;
            if c + 1 < n && v[r][c] == b'0' {
                g[x].push(x + 1);
                g[x + 1].push(x);
            }
            if r + 1 < n && h[r][c] == b'0' {
                g[x].push(x + n);
                g[x + n].push(x);
            }
        }
    }
    g
}

fn horizontal_segments(n: usize, wall: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut result = Vec::new();
    for r in 0..n {
        let mut start = 0;
        for c in 0..n {
            if c + 1 == n || wall[r][c] == b'1' {
                result.push((start..=c).map(|x| r * n + x).collect());
                start = c + 1;
            }
        }
    }
    result
}

fn vertical_segments(n: usize, wall: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut result = Vec::new();
    for c in 0..n {
        let mut start = 0;
        for r in 0..n {
            if r + 1 == n || wall[r][c] == b'1' {
                result.push((start..=r).map(|x| x * n + c).collect());
                start = r + 1;
            }
        }
    }
    result
}

fn augment(
    source: usize,
    cards: &[Vec<usize>],
    used: &[bool],
    target_axis: &[usize],
    seen: &mut [bool],
    matched_source: &mut [usize],
    chosen: &mut [usize],
) -> bool {
    for &card in &cards[source] {
        if used[card] {
            continue;
        }
        let target = target_axis[card];
        if seen[target] {
            continue;
        }
        seen[target] = true;
        let old = matched_source[target];
        if old == usize::MAX || augment(old, cards, used, target_axis, seen, matched_source, chosen)
        {
            matched_source[target] = source;
            chosen[source] = card;
            return true;
        }
    }
    false
}

// Edge-colors the regular bipartite multigraph (current column, target column).
fn intermediate_rows(board: &[usize], n: usize) -> Vec<usize> {
    let k = n * n;
    let cards: Vec<Vec<usize>> = (0..n)
        .map(|c| (0..n).map(|r| board[r * n + c]).collect())
        .collect();
    let target_column: Vec<usize> = (0..k).map(|card| card % n).collect();
    let mut used = vec![false; k];
    let mut row = vec![usize::MAX; k];
    for color in 0..n {
        let mut matched_source = vec![usize::MAX; n];
        let mut chosen = vec![usize::MAX; n];
        for source in 0..n {
            let mut seen = vec![false; n];
            assert!(augment(
                source,
                &cards,
                &used,
                &target_column,
                &mut seen,
                &mut matched_source,
                &mut chosen,
            ));
        }
        for card in chosen {
            used[card] = true;
            row[card] = color;
        }
    }
    row
}

#[derive(Clone, Copy)]
struct LineState {
    cards: [u8; 20],
    moves: [u16; LINE_DEPTH],
    move_len: u8,
    cost: i32,
}

fn line_cost(keys: &[u8]) -> i32 {
    let len = keys.len();
    let mut breakpoints = i32::from(keys[0] != 0) + i32::from(keys[len - 1] as usize + 1 != len);
    for pair in keys.windows(2) {
        breakpoints += i32::from(pair[1] != pair[0] + 1);
    }
    let displacement: usize = keys
        .iter()
        .enumerate()
        .map(|(i, &key)| i.abs_diff(key as usize))
        .sum();
    100 * breakpoints + displacement as i32
}

fn line_key(keys: &[u8]) -> u128 {
    keys.iter()
        .enumerate()
        .fold(0, |result, (i, &value)| result | (value as u128) << (5 * i))
}

// Turn a wall-bounded segment into a complete local permutation. Reachable,
// unique real targets are fixed first; all other cards are stable wildcards.
fn wildcard_assignment(
    cards: &[usize],
    cells: &[usize],
    desired: &[usize],
    n: usize,
) -> HashMap<usize, usize> {
    let horizontal = cells.len() <= 1 || cells[1] == cells[0] + 1;
    let base = if horizontal {
        cells[0] % n
    } else {
        cells[0] / n
    };
    let mut assignment = HashMap::new();
    let mut used = vec![false; cards.len()];
    for &card in cards {
        let target = desired[card];
        if target >= base && target < base + cards.len() && !used[target - base] {
            used[target - base] = true;
            assignment.insert(card, target - base);
        }
    }
    let remaining: Vec<usize> = used
        .iter()
        .enumerate()
        .filter_map(|(i, &taken)| (!taken).then_some(i))
        .collect();
    let mut at = 0;
    for &card in cards {
        if let std::collections::hash_map::Entry::Vacant(entry) = assignment.entry(card) {
            entry.insert(remaining[at]);
            at += 1;
        }
    }
    assignment
}

fn solve_line(
    cells: &[usize],
    board: &[usize],
    desired: &[usize],
    n: usize,
    started: &Instant,
) -> Vec<(usize, usize)> {
    let len = cells.len();
    if len < 2 || started.elapsed().as_secs_f64() >= ROUTING_TIME {
        return Vec::new();
    }
    let initial_cards: Vec<usize> = cells.iter().map(|&cell| board[cell]).collect();
    let assignment = wildcard_assignment(&initial_cards, cells, desired, n);
    let mut initial_keys = [0u8; 20];
    for (i, card) in initial_cards.iter().enumerate() {
        initial_keys[i] = assignment[card] as u8;
    }
    let initial_cost = line_cost(&initial_keys[..len]);
    if initial_cost == 0 {
        return Vec::new();
    }
    let mut beam = vec![LineState {
        cards: initial_keys,
        moves: [0; LINE_DEPTH],
        move_len: 0,
        cost: initial_cost,
    }];
    let mut best = beam[0];
    let mut best_objective = initial_cost;
    let mut seen = HashSet::from([line_key(&initial_keys[..len])]);
    for _ in 0..LINE_DEPTH {
        if started.elapsed().as_secs_f64() >= ROUTING_TIME {
            break;
        }
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..len {
                for half in 1..=(len - start) / 2 {
                    let mut child = *state;
                    for i in 0..half {
                        child.cards.swap(start + i, start + half + i);
                    }
                    let hash = line_key(&child.cards[..len]);
                    if !seen.insert(hash) {
                        continue;
                    }
                    child.moves[child.move_len as usize] = start as u16 | ((half as u16) << 5);
                    child.move_len += 1;
                    child.cost = line_cost(&child.cards[..len]);
                    let objective = child.cost;
                    if objective < best_objective {
                        best_objective = objective;
                        best = child;
                    }
                    next.push(child);
                }
            }
        }
        next.sort_unstable_by_key(|state| state.cost);
        next.truncate(LINE_BEAM);
        if next.is_empty() {
            break;
        }
        beam = next;
        if best_objective == 0 {
            break;
        }
    }
    if best_objective < initial_cost {
        best.moves[..best.move_len as usize]
            .iter()
            .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
            .collect()
    } else {
        Vec::new()
    }
}

fn route_segments(
    segments: &[Vec<usize>],
    desired: &[usize],
    board: &mut [usize],
    pos: &mut [usize],
    n: usize,
    output: &mut Vec<Op>,
    started: &Instant,
) {
    // Long segments first: they provide the largest equal-block moves.
    let mut order: Vec<usize> = (0..segments.len()).collect();
    order.sort_unstable_by_key(|&i| std::cmp::Reverse(segments[i].len()));
    for index in order {
        let cells = &segments[index];
        let horizontal = cells.len() <= 1 || cells[1] == cells[0] + 1;
        for (start, half) in solve_line(cells, board, desired, n, started) {
            let first = cells[0];
            let op = if horizontal {
                Op {
                    d: b'H',
                    r: first / n,
                    c: first % n + start,
                    h: 1,
                    w: 2 * half,
                }
            } else {
                Op {
                    d: b'V',
                    r: first / n + start,
                    c: first % n,
                    h: 2 * half,
                    w: 1,
                }
            };
            apply(op, board, pos, n);
            output.push(op);
        }
    }
}

fn all_tree_distances(tree: &[Vec<usize>]) -> Vec<u16> {
    let k = tree.len();
    let mut d = vec![u16::MAX; k * k];
    for s in 0..k {
        let mut q = VecDeque::from([s]);
        d[s * k + s] = 0;
        while let Some(x) = q.pop_front() {
            let nd = d[s * k + x] + 1;
            for &to in &tree[x] {
                if d[s * k + to] == u16::MAX {
                    d[s * k + to] = nd;
                    q.push_back(to);
                }
            }
        }
    }
    d
}

struct Forest {
    tree: Vec<Vec<usize>>,
    parent: Vec<usize>,
    depth: Vec<usize>,
    distance: Vec<u16>,
}

impl Forest {
    fn new(g: &[Vec<usize>], root: usize, reverse: bool) -> Self {
        let k = g.len();
        let mut tree = vec![Vec::new(); k];
        let mut parent = vec![usize::MAX; k];
        let mut depth = vec![0; k];
        parent[root] = root;
        let mut q = VecDeque::from([root]);
        while let Some(x) = q.pop_front() {
            if reverse {
                for &to in g[x].iter().rev() {
                    if parent[to] == usize::MAX {
                        parent[to] = x;
                        depth[to] = depth[x] + 1;
                        tree[x].push(to);
                        tree[to].push(x);
                        q.push_back(to);
                    }
                }
            } else {
                for &to in &g[x] {
                    if parent[to] == usize::MAX {
                        parent[to] = x;
                        depth[to] = depth[x] + 1;
                        tree[x].push(to);
                        tree[to].push(x);
                        q.push_back(to);
                    }
                }
            }
        }
        assert!(parent.iter().all(|&x| x != usize::MAX));
        let distance = all_tree_distances(&tree);
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

    fn complete(&self, initial: &[usize], n: usize) -> Vec<Op> {
        let k = initial.len();
        let mut board = initial.to_vec();
        let mut pos = vec![0; k];
        for (i, &x) in board.iter().enumerate() {
            pos[x] = i;
        }
        let mut active = vec![true; k];
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut output = Vec::new();
        for _ in 1..k {
            let leaf = (0..k)
                .filter(|&x| active[x] && degree[x] == 1)
                .min_by_key(|&x| self.distance[pos[x] * k + x])
                .unwrap();
            for edge in self.path(pos[leaf], leaf).windows(2) {
                let (a, b) = (edge[0], edge[1]);
                let (ar, ac) = (a / n, a % n);
                let (br, bc) = (b / n, b % n);
                let op = if ar == br {
                    Op {
                        d: b'H',
                        r: ar,
                        c: ac.min(bc),
                        h: 1,
                        w: 2,
                    }
                } else {
                    Op {
                        d: b'V',
                        r: ar.min(br),
                        c: ac,
                        h: 2,
                        w: 1,
                    }
                };
                apply(op, &mut board, &mut pos, n);
                output.push(op);
            }
            active[leaf] = false;
            degree[leaf] = 0;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
        }
        assert!(board.iter().enumerate().all(|(i, &x)| i == x));
        output
    }
}

// Fuse reorderable disjoint adjacent swaps into 2-by-k or k-by-2 rectangles.
fn compress(raw: &[Op], n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> Vec<Op> {
    fn flush(batch: &mut Vec<Op>, out: &mut Vec<Op>, v: &[Vec<u8>], h: &[Vec<u8>]) {
        for d in [b'H', b'V'] {
            let mut a: Vec<Op> = batch.iter().copied().filter(|op| op.d == d).collect();
            if d == b'H' {
                a.sort_unstable_by_key(|op| (op.c, op.r));
            } else {
                a.sort_unstable_by_key(|op| (op.r, op.c));
            }
            let mut i = 0;
            while i < a.len() {
                let first = a[i];
                let mut j = i + 1;
                while j < a.len() {
                    let prev = a[j - 1];
                    let next = a[j];
                    let ok = if d == b'H' {
                        next.c == first.c
                            && next.r == prev.r + 1
                            && h[prev.r][first.c] == b'0'
                            && h[prev.r][first.c + 1] == b'0'
                    } else {
                        next.r == first.r
                            && next.c == prev.c + 1
                            && v[first.r][prev.c] == b'0'
                            && v[first.r + 1][prev.c] == b'0'
                    };
                    if !ok {
                        break;
                    }
                    j += 1;
                }
                out.push(if d == b'H' {
                    Op {
                        d,
                        r: first.r,
                        c: first.c,
                        h: j - i,
                        w: 2,
                    }
                } else {
                    Op {
                        d,
                        r: first.r,
                        c: first.c,
                        h: 2,
                        w: j - i,
                    }
                });
                i = j;
            }
        }
        batch.clear();
    }
    let mut out = Vec::new();
    let mut batch = Vec::new();
    let mut occupied = vec![false; n * n];
    for &op in raw {
        let a = op.r * n + op.c;
        let b = if op.d == b'H' { a + 1 } else { a + n };
        if occupied[a] || occupied[b] {
            flush(&mut batch, &mut out, v, h);
            occupied.fill(false);
        }
        occupied[a] = true;
        occupied[b] = true;
        batch.push(op);
    }
    flush(&mut batch, &mut out, v, h);
    out
}

fn legal(op: Op, n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> bool {
    if op.h == 0 || op.w == 0 || op.r + op.h > n || op.c + op.w > n {
        return false;
    }
    if (op.d == b'H' && op.w % 2 != 0) || (op.d == b'V' && op.h % 2 != 0) {
        return false;
    }
    if op.d != b'H' && op.d != b'V' {
        return false;
    }
    for r in op.r..op.r + op.h {
        for c in op.c..op.c + op.w.saturating_sub(1) {
            if v[r][c] == b'1' {
                return false;
            }
        }
    }
    for r in op.r..op.r + op.h.saturating_sub(1) {
        for c in op.c..op.c + op.w {
            if h[r][c] == b'1' {
                return false;
            }
        }
    }
    true
}

fn validates(initial: &[usize], operations: &[Op], n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> bool {
    if operations.len() > 100_000 {
        return false;
    }
    let mut board = initial.to_vec();
    let mut pos = vec![0; board.len()];
    for (i, &card) in board.iter().enumerate() {
        pos[card] = i;
    }
    for &op in operations {
        if !legal(op, n, v, h) {
            return false;
        }
        apply(op, &mut board, &mut pos, n);
    }
    board.iter().enumerate().all(|(i, &card)| i == card)
}

#[derive(Clone)]
struct Checkpoint {
    board: Vec<usize>,
    prefix: Vec<Op>,
}

fn main() {
    let started = Instant::now();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut scan = Scanner(input.split_whitespace());
    let n: usize = scan.next();
    let k = n * n;
    let initial: Vec<usize> = (0..k).map(|_| scan.next()).collect();
    let v: Vec<Vec<u8>> = (0..n).map(|_| scan.next::<String>().into_bytes()).collect();
    let h: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scan.next::<String>().into_bytes())
        .collect();
    let g = graph(n, &v, &h);
    let roots = [0, n - 1, (n - 1) * n, k - 1, (n / 2) * n + n / 2];
    let forests: Vec<Forest> = roots
        .iter()
        .enumerate()
        .map(|(i, &root)| Forest::new(&g, root, i % 2 == 1))
        .collect();
    let h_segments = horizontal_segments(n, &v);
    let v_segments = vertical_segments(n, &h);
    let middle = intermediate_rows(&initial, n);
    let target_row: Vec<usize> = (0..k).map(|x| x / n).collect();
    let target_col: Vec<usize> = (0..k).map(|x| x % n).collect();

    let mut board = initial.clone();
    let mut pos = vec![0; k];
    for (i, &x) in board.iter().enumerate() {
        pos[x] = i;
    }
    let mut prefix = Vec::new();
    let mut checkpoints = vec![Checkpoint {
        board: board.clone(),
        prefix: Vec::new(),
    }];
    let stages: [(&[Vec<usize>], &[usize]); 3] = [
        (&v_segments, &middle),
        (&h_segments, &target_col),
        (&v_segments, &target_row),
    ];
    for (segments, desired) in stages {
        if started.elapsed().as_secs_f64() >= ROUTING_TIME {
            break;
        }
        route_segments(
            segments,
            desired,
            &mut board,
            &mut pos,
            n,
            &mut prefix,
            &started,
        );
        checkpoints.push(Checkpoint {
            board: board.clone(),
            prefix: prefix.clone(),
        });
    }

    let initial_raw = forests[0].complete(&initial, n);
    let safe_answer = compress(&initial_raw, n, &v, &h);
    let initial_limit = safe_answer.len();
    let mut best: Option<(Vec<Op>, Vec<Op>)> = None;
    for checkpoint in checkpoints {
        for forest in &forests {
            let fallback = compress(&forest.complete(&checkpoint.board, n), n, &v, &h);
            let total = checkpoint.prefix.len() + fallback.len();
            if best
                .as_ref()
                .map_or(true, |(p, f)| total < p.len() + f.len())
            {
                best = Some((checkpoint.prefix.clone(), fallback));
            }
        }
    }
    let (mut answer, fallback) = best.unwrap();
    answer.extend(fallback);
    if !validates(&initial, &answer, n, &v, &h) {
        answer = safe_answer;
    }
    assert!(answer.len() <= initial_limit && answer.len() <= 100_000);
    assert!(validates(&initial, &answer, n, &v, &h));
    let mut out = String::new();
    for op in answer {
        writeln!(out, "{} {} {} {} {}", op.d as char, op.r, op.c, op.h, op.w).unwrap();
    }
    print!("{out}");
}
