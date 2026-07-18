use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const BEAM_WIDTH: usize = 4;
const BRANCH_WIDTH: usize = 8;
const SAMPLE_SIZE: usize = 3072;
const MACRO_DEPTH: usize = 64;
const LINE_TIME: f64 = 0.30;
const MACRO_TIME: f64 = 0.82;
const SEARCH_TIME: f64 = 1.18;
const CHECKPOINTS: usize = 10;

struct Scanner<'a>(std::str::SplitWhitespace<'a>);
impl<'a> Scanner<'a> {
    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.0.next().unwrap().parse().unwrap()
    }
}

#[derive(Clone)]
struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x << 7;
        x ^= x >> 9;
        self.0 = x;
        x
    }
    fn range(&mut self, end: usize) -> usize {
        self.next() as usize % end
    }
    fn unit(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1_u64 << 53) as f64
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

fn swap_cells(a: usize, b: usize, board: &mut [usize], pos: &mut [usize]) {
    board.swap(a, b);
    pos[board[a]] = a;
    pos[board[b]] = b;
}

fn apply_candidate(c: &Candidate, board: &mut [usize], pos: &mut [usize]) {
    for &(a, b) in &c.pairs {
        swap_cells(a, b, board, pos);
    }
}

fn apply_operation(op: Operation, board: &mut [usize], pos: &mut [usize], n: usize) {
    if op.d == b'V' {
        for x in 0..op.h / 2 {
            for y in 0..op.w {
                swap_cells(
                    (op.r + x) * n + op.c + y,
                    (op.r + op.h / 2 + x) * n + op.c + y,
                    board,
                    pos,
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
                    pos,
                );
            }
        }
    }
}

fn graph(n: usize, v_wall: &[Vec<u8>], h_wall: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut g = vec![Vec::new(); n * n];
    for r in 0..n {
        for c in 0..n {
            let x = r * n + c;
            if c + 1 < n && v_wall[r][c] == b'0' {
                g[x].push(x + 1);
                g[x + 1].push(x);
            }
            if r + 1 < n && h_wall[r][c] == b'0' {
                g[x].push(x + n);
                g[x + n].push(x);
            }
        }
    }
    g
}

fn all_distances(g: &[Vec<usize>]) -> Vec<u16> {
    let k = g.len();
    let mut d = vec![u16::MAX; k * k];
    let mut q = VecDeque::with_capacity(k);
    for s in 0..k {
        d[s * k + s] = 0;
        q.push_back(s);
        while let Some(x) = q.pop_front() {
            let nd = d[s * k + x] + 1;
            for &to in &g[x] {
                if d[s * k + to] == u16::MAX {
                    d[s * k + to] = nd;
                    q.push_back(to);
                }
            }
        }
    }
    d
}

fn open_rect(
    r: usize,
    c: usize,
    h: usize,
    w: usize,
    v_wall: &[Vec<u8>],
    h_wall: &[Vec<u8>],
) -> bool {
    for i in r..r + h {
        for j in c..c + w.saturating_sub(1) {
            if v_wall[i][j] == b'1' {
                return false;
            }
        }
    }
    for i in r..r + h.saturating_sub(1) {
        for j in c..c + w {
            if h_wall[i][j] == b'1' {
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

fn make_candidates(
    n: usize,
    max_dim: usize,
    v_wall: &[Vec<u8>],
    h_wall: &[Vec<u8>],
) -> Vec<Candidate> {
    let mut result = Vec::new();
    for h in 1..=max_dim.min(n) {
        for w in 1..=max_dim.min(n) {
            if h * w == 1 || (h % 2 == 1 && w % 2 == 1) {
                continue;
            }
            for r in 0..=n - h {
                for c in 0..=n - w {
                    if !open_rect(r, c, h, w, v_wall, h_wall) {
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

fn energy(board: &[usize], distance: &[u16], k: usize) -> i32 {
    board
        .iter()
        .enumerate()
        .map(|(at, &tile)| 8 * i32::from(distance[tile * k + at]) + 3 * i32::from(tile != at))
        .sum()
}

// Positive gain is good. It is deliberately not divided by rectangle area:
// every legal rectangle costs exactly one output operation.
fn gain(c: &Candidate, board: &[usize], distance: &[u16], k: usize) -> i32 {
    let mut value = 0;
    for &(a, b) in &c.pairs {
        let x = board[a];
        let y = board[b];
        value += 8
            * (i32::from(distance[x * k + a]) + i32::from(distance[y * k + b])
                - i32::from(distance[x * k + b])
                - i32::from(distance[y * k + a]));
        value +=
            3 * (i32::from(x != a) + i32::from(y != b) - i32::from(x != b) - i32::from(y != a));
    }
    value
}

fn insert_best(best: &mut Vec<(i32, usize)>, item: (i32, usize)) {
    if best.len() < BRANCH_WIDTH {
        best.push(item);
    } else {
        let worst = best.iter().enumerate().min_by_key(|(_, x)| x.0).unwrap().0;
        if item.0 > best[worst].0 {
            best[worst] = item;
        }
    }
}

fn sampled_moves(
    node: &BeamNode,
    candidates: &[Candidate],
    distance: &[u16],
    k: usize,
    rng: &mut Rng,
) -> Vec<(i32, usize)> {
    let mut best = Vec::with_capacity(BRANCH_WIDTH);
    let len = candidates.len();
    let start = rng.range(len);
    let amount = SAMPLE_SIZE.min(len);
    for offset in 0..amount {
        let index = (start + offset) % len;
        if node.tabu == Some(index) {
            continue;
        }
        insert_best(
            &mut best,
            (gain(&candidates[index], &node.board, distance, k), index),
        );
    }
    // Random probes avoid repeatedly seeing only one contiguous part of the
    // shuffled candidate table.
    for _ in 0..amount / 2 {
        let index = rng.range(len);
        if node.tabu != Some(index) {
            insert_best(
                &mut best,
                (gain(&candidates[index], &node.board, distance, k), index),
            );
        }
    }
    best.sort_unstable_by_key(|x| std::cmp::Reverse(x.0));
    best
}

fn board_hash(board: &[usize]) -> u64 {
    board
        .iter()
        .enumerate()
        .fold(0xcbf29ce484222325, |h, (i, &x)| {
            (h ^ ((x as u64) << 10) ^ i as u64).wrapping_mul(0x100000001b3)
        })
}

#[derive(Clone)]
struct BeamNode {
    board: Vec<usize>,
    pos: Vec<usize>,
    prefix: Vec<Operation>,
    energy: i32,
    tabu: Option<usize>,
}

fn line_pass(
    node: &mut BeamNode,
    candidates: &[Candidate],
    distance: &[u16],
    k: usize,
    direction: u8,
    deadline: f64,
    started: &Instant,
) {
    for _ in 0..128 {
        if started.elapsed().as_secs_f64() >= deadline {
            break;
        }
        let mut best = None;
        for (index, candidate) in candidates.iter().enumerate() {
            if candidate.op.d != direction {
                continue;
            }
            let value = gain(candidate, &node.board, distance, k);
            if value > 0 && best.map_or(true, |(old, _)| value > old) {
                best = Some((value, index));
            }
        }
        let Some((value, index)) = best else {
            break;
        };
        apply_candidate(&candidates[index], &mut node.board, &mut node.pos);
        node.prefix.push(candidates[index].op);
        node.energy -= value;
    }
}

struct Forest {
    tree: Vec<Vec<usize>>,
    parent: Vec<usize>,
    depth: Vec<usize>,
    tree_distance: Vec<u16>,
    components: Vec<Vec<usize>>,
}

impl Forest {
    fn new(g: &[Vec<usize>], preferred_root: usize, reverse: bool) -> Self {
        let k = g.len();
        let mut tree = vec![Vec::new(); k];
        let mut parent = vec![usize::MAX; k];
        let mut depth = vec![0; k];
        let mut components = Vec::new();
        for root in (0..k).cycle().skip(preferred_root).take(k) {
            if parent[root] != usize::MAX {
                continue;
            }
            parent[root] = root;
            let mut component = Vec::new();
            let mut q = VecDeque::from([root]);
            while let Some(x) = q.pop_front() {
                component.push(x);
                let neighbors: Box<dyn Iterator<Item = &usize>> = if reverse {
                    Box::new(g[x].iter().rev())
                } else {
                    Box::new(g[x].iter())
                };
                for &to in neighbors {
                    if parent[to] == usize::MAX {
                        parent[to] = x;
                        depth[to] = depth[x] + 1;
                        tree[x].push(to);
                        tree[to].push(x);
                        q.push_back(to);
                    }
                }
            }
            components.push(component);
        }
        let tree_distance = all_distances(&tree);
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
        pos: &mut [usize],
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
                    .filter(|&x| active[x] && degree[x] <= 1)
                    .min_by_key(|&x| self.tree_distance[pos[x] * k + x])
                    .unwrap();
                let path = self.path(pos[leaf], leaf);
                debug_assert!(path.iter().all(|&x| active[x]));
                for edge in path.windows(2) {
                    let op = adjacent_op(edge[0], edge[1], n);
                    apply_operation(op, board, pos, n);
                    emit(op);
                    count += 1;
                }
                active[leaf] = false;
                degree[leaf] = 0;
                for &to in &self.tree[leaf] {
                    if active[to] {
                        degree[to] -= 1;
                    }
                }
            }
        }
        assert!(board.iter().enumerate().all(|(i, &x)| i == x));
        count
    }

    fn count(&self, board: &[usize], pos: &[usize], n: usize) -> usize {
        let mut b = board.to_vec();
        let mut p = pos.to_vec();
        self.run(&mut b, &mut p, n, |_| {})
    }
}

fn adjacent_op(a: usize, b: usize, n: usize) -> Operation {
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
    pos: Vec<usize>,
    prefix: Vec<Operation>,
}

fn save(states: &mut Vec<Snapshot>, state: Snapshot) {
    states.push(state);
    states.sort_unstable_by_key(|x| x.estimate);
    states.truncate(CHECKPOINTS);
}

fn main() {
    let started = Instant::now();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut scan = Scanner(input.split_whitespace());
    let n: usize = scan.next();
    let k = n * n;
    let board: Vec<usize> = (0..k).map(|_| scan.next()).collect();
    let v_wall: Vec<Vec<u8>> = (0..n).map(|_| scan.next::<String>().into_bytes()).collect();
    let h_wall: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| scan.next::<String>().into_bytes())
        .collect();
    let mut pos = vec![0; k];
    for (i, &x) in board.iter().enumerate() {
        pos[x] = i;
    }
    let g = graph(n, &v_wall, &h_wall);
    let distance = all_distances(&g);
    let mut macro_candidates = make_candidates(n, n, &v_wall, &h_wall);
    let line_candidates: Vec<Candidate> = macro_candidates
        .iter()
        .filter(|candidate| candidate.op.h == 1 || candidate.op.w == 1)
        .cloned()
        .collect();
    let local_candidates = make_candidates(n, 4, &v_wall, &h_wall);
    let mut rng = Rng(0x68_2026_0718);
    for i in (1..macro_candidates.len()).rev() {
        let j = rng.range(i + 1);
        macro_candidates.swap(i, j);
    }

    let roots = [0, n - 1, (n - 1) * n, k - 1, (n / 2) * n + n / 2];
    let forests: Vec<Forest> = roots
        .iter()
        .enumerate()
        .map(|(i, &root)| Forest::new(&g, root, i % 2 == 1))
        .collect();
    let initial_count = forests[0].count(&board, &pos, n);
    let mut states = vec![Snapshot {
        estimate: initial_count,
        board: board.clone(),
        pos: pos.clone(),
        prefix: Vec::new(),
    }];

    let initial = BeamNode {
        energy: energy(&board, &distance, k),
        board,
        pos,
        prefix: Vec::new(),
        tabu: None,
    };
    // A row -> column -> row equal-block routing pass exhaustively considers
    // every 1D operation in the long wall-free segments.
    let mut routed = initial.clone();
    for (pass, direction) in [b'H', b'V', b'H'].into_iter().enumerate() {
        line_pass(
            &mut routed,
            &line_candidates,
            &distance,
            k,
            direction,
            LINE_TIME * (pass + 1) as f64 / 3.0,
            &started,
        );
        let exact = routed.prefix.len() + forests[0].count(&routed.board, &routed.pos, n);
        save(
            &mut states,
            Snapshot {
                estimate: exact,
                board: routed.board.clone(),
                pos: routed.pos.clone(),
                prefix: routed.prefix.clone(),
            },
        );
    }
    let mut beam = vec![initial, routed];
    for depth in 0..MACRO_DEPTH {
        if started.elapsed().as_secs_f64() >= MACRO_TIME {
            break;
        }
        let temperature = 160.0 * (1.0 - depth as f64 / MACRO_DEPTH as f64) + 8.0;
        let mut children: Vec<(f64, u64, BeamNode)> = Vec::new();
        for node in &beam {
            for (gained, index) in sampled_moves(node, &macro_candidates, &distance, k, &mut rng) {
                let mut child = node.clone();
                apply_candidate(&macro_candidates[index], &mut child.board, &mut child.pos);
                child.prefix.push(macro_candidates[index].op);
                child.energy -= gained;
                child.tabu = Some(index);
                let noisy_rank = child.energy as f64 + temperature * (rng.unit() - 0.5);
                children.push((noisy_rank, board_hash(&child.board), child));
            }
        }
        if children.is_empty() {
            break;
        }
        children.sort_by(|a, b| a.0.total_cmp(&b.0));
        let mut hashes = Vec::new();
        beam.clear();
        for (_, hash, child) in children {
            if hashes.contains(&hash) {
                continue;
            }
            hashes.push(hash);
            beam.push(child);
            if beam.len() == BEAM_WIDTH {
                break;
            }
        }
        if depth % 8 == 7 {
            for node in beam.iter().take(2) {
                let exact = node.prefix.len() + forests[0].count(&node.board, &node.pos, n);
                save(
                    &mut states,
                    Snapshot {
                        estimate: exact,
                        board: node.board.clone(),
                        pos: node.pos.clone(),
                        prefix: node.prefix.clone(),
                    },
                );
            }
        }
    }

    let mut current = beam.into_iter().min_by_key(|x| x.energy).unwrap();
    let mut local_steps = 0usize;
    while started.elapsed().as_secs_f64() < SEARCH_TIME && current.prefix.len() < 20_000 {
        let mut best = None;
        for (i, c) in local_candidates.iter().enumerate() {
            let value = gain(c, &current.board, &distance, k);
            if value > 0 && best.map_or(true, |(old, _)| value > old) {
                best = Some((value, i));
            }
        }
        let Some((value, index)) = best else { break };
        apply_candidate(
            &local_candidates[index],
            &mut current.board,
            &mut current.pos,
        );
        current.prefix.push(local_candidates[index].op);
        current.energy -= value;
        local_steps += 1;
        if local_steps % 32 == 0 {
            let exact = current.prefix.len() + forests[0].count(&current.board, &current.pos, n);
            save(
                &mut states,
                Snapshot {
                    estimate: exact,
                    board: current.board.clone(),
                    pos: current.pos.clone(),
                    prefix: current.prefix.clone(),
                },
            );
        }
    }
    let exact = current.prefix.len() + forests[0].count(&current.board, &current.pos, n);
    save(
        &mut states,
        Snapshot {
            estimate: exact,
            board: current.board,
            pos: current.pos,
            prefix: current.prefix,
        },
    );

    let mut best = (usize::MAX, 0, 0);
    for (si, state) in states.iter().enumerate() {
        for (fi, forest) in forests.iter().enumerate() {
            let total = state.prefix.len() + forest.count(&state.board, &state.pos, n);
            if total < best.0 {
                best = (total, si, fi);
            }
        }
    }
    let mut state = states.swap_remove(best.1);
    let mut answer = state.prefix;
    forests[best.2].run(&mut state.board, &mut state.pos, n, |op| answer.push(op));
    assert_eq!(answer.len(), best.0);
    assert!(answer.len() <= initial_count && answer.len() <= 100_000);

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
