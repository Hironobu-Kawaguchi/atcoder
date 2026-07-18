use std::collections::{HashSet, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const BEAM_WIDTH: usize = 200;
const ROOM_SECONDS: f64 = 0.28;
const LINE_SECONDS: f64 = 0.0045;
const DOOR_SECONDS: f64 = 0.10;
const MACRO_SECONDS: f64 = 0.62;
const ZERO_BEAM_DEPTH: usize = 14;
const ZERO_SECONDS: f64 = 1.08;

#[derive(Clone, Copy, PartialEq, Eq)]
enum SolverKind {
    Tree,
    Region,
    GreedyZero,
}

#[derive(Clone, Copy, Debug)]
struct Op {
    d: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

#[derive(Clone, Copy, Debug)]
struct Room {
    id: usize,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

struct Scanner<'a>(std::str::SplitWhitespace<'a>);
impl<'a> Scanner<'a> {
    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.0.next().unwrap().parse().unwrap()
    }
}

fn add_edge(g: &mut [Vec<usize>], a: usize, b: usize) {
    g[a].push(b);
    g[b].push(a);
}

fn rect_open(op: Op, v: &[Vec<u8>], h: &[Vec<u8>]) -> bool {
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

fn legal(op: Op, n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> bool {
    op.r + op.h <= n
        && op.c + op.w <= n
        && ((op.d == b'H' && op.w > 0 && op.w % 2 == 0)
            || (op.d == b'V' && op.h > 0 && op.h % 2 == 0))
        && rect_open(op, v, h)
}

fn apply(op: Op, board: &mut [usize], pos: &mut [usize], n: usize) {
    let mut exchange = |a: usize, b: usize| {
        board.swap(a, b);
        pos[board[a]] = a;
        pos[board[b]] = b;
    };
    if op.d == b'H' {
        for dr in 0..op.h {
            for dc in 0..op.w / 2 {
                exchange(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + dr) * n + op.c + op.w / 2 + dc,
                );
            }
        }
    } else {
        for dr in 0..op.h / 2 {
            for dc in 0..op.w {
                exchange(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + op.h / 2 + dr) * n + op.c + dc,
                );
            }
        }
    }
}

fn all_distances(g: &[Vec<usize>]) -> Vec<u16> {
    let m = g.len();
    let mut d = vec![u16::MAX; m * m];
    for s in 0..m {
        let mut q = VecDeque::from([s]);
        d[s * m + s] = 0;
        while let Some(x) = q.pop_front() {
            let nd = d[s * m + x] + 1;
            for &y in &g[x] {
                if d[s * m + y] == u16::MAX {
                    d[s * m + y] = nd;
                    q.push_back(y);
                }
            }
        }
    }
    d
}

fn op_delta(op: Op, board: &[usize], dist: &[u16], n: usize) -> i32 {
    let m = board.len();
    let mut ans = 0;
    let mut pair = |a: usize, b: usize| {
        let x = board[a];
        let y = board[b];
        ans += i32::from(dist[x * m + b]) + i32::from(dist[y * m + a])
            - i32::from(dist[x * m + a])
            - i32::from(dist[y * m + b]);
    };
    if op.d == b'H' {
        for dr in 0..op.h {
            for dc in 0..op.w / 2 {
                pair(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + dr) * n + op.c + op.w / 2 + dc,
                );
            }
        }
    } else {
        for dr in 0..op.h / 2 {
            for dc in 0..op.w {
                pair(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + op.h / 2 + dr) * n + op.c + dc,
                );
            }
        }
    }
    ans
}

/// Greedily tiles the board with large, pairwise-disjoint open rectangles.
fn decompose_rooms(n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> (Vec<Room>, Vec<usize>) {
    let mut candidates = Vec::new();
    for height in 1..=n {
        for width in 1..=n {
            if height * width < 2 {
                continue;
            }
            for r in 0..=n - height {
                for c in 0..=n - width {
                    let op = Op {
                        d: if width % 2 == 0 { b'H' } else { b'V' },
                        r,
                        c,
                        h: height,
                        w: width,
                    };
                    if rect_open(op, v, h) {
                        candidates.push((height * width, r, c, height, width));
                    }
                }
            }
        }
    }
    candidates.sort_unstable_by(|a, b| b.cmp(a));
    let mut owner = vec![usize::MAX; n * n];
    let mut rooms = Vec::new();
    for &(_, r, c, height, width) in &candidates {
        let free =
            (r..r + height).all(|rr| (c..c + width).all(|cc| owner[rr * n + cc] == usize::MAX));
        if !free {
            continue;
        }
        let id = rooms.len();
        for rr in r..r + height {
            for cc in c..c + width {
                owner[rr * n + cc] = id;
            }
        }
        rooms.push(Room {
            id,
            r,
            c,
            h: height,
            w: width,
        });
    }
    for cell in 0..n * n {
        if owner[cell] == usize::MAX {
            let id = rooms.len();
            owner[cell] = id;
            rooms.push(Room {
                id,
                r: cell / n,
                c: cell % n,
                h: 1,
                w: 1,
            });
        }
    }
    (rooms, owner)
}

fn state_key(cards: &[usize], universe: &[usize]) -> u128 {
    debug_assert!(cards.len() <= 20);
    let mut key = 0u128;
    for (i, &card) in cards.iter().enumerate() {
        let rank = universe.iter().position(|&x| x == card).unwrap();
        key |= (rank as u128) << (5 * i);
    }
    key
}

fn line_score(
    cards: &[usize],
    cells: &[usize],
    vertical_line: bool,
    room_id: usize,
    owner: &[usize],
    n: usize,
) -> usize {
    let mut displacement = 0usize;
    let mut breakpoints = 0usize;
    let mut previous = None;
    for (i, &card) in cards.iter().enumerate() {
        if owner[card] != room_id {
            previous = None;
            continue;
        }
        let target = if vertical_line { card / n } else { card % n };
        let here = if vertical_line {
            cells[i] / n
        } else {
            cells[i] % n
        };
        displacement += here.abs_diff(target);
        if let Some(last) = previous {
            if target != last + 1 {
                breakpoints += 1;
            }
        } else if target != here {
            breakpoints += 1;
        }
        previous = Some(target);
    }
    breakpoints * 100 + displacement
}

#[derive(Clone)]
struct BeamState {
    cards: Vec<usize>,
    moves: Vec<(usize, usize)>,
    score: usize,
}

fn beam_line(
    initial: &[usize],
    cells: &[usize],
    vertical_line: bool,
    room_id: usize,
    owner: &[usize],
    n: usize,
    global_timer: &Instant,
) -> (Vec<(usize, usize)>, Vec<usize>) {
    if initial.len() < 2 || global_timer.elapsed().as_secs_f64() >= ROOM_SECONDS {
        return (Vec::new(), initial.to_vec());
    }
    let line_timer = Instant::now();
    let first_score = line_score(initial, cells, vertical_line, room_id, owner, n);
    let mut best = BeamState {
        cards: initial.to_vec(),
        moves: Vec::new(),
        score: first_score,
    };
    let mut beam = vec![best.clone()];
    let mut seen = HashSet::new();
    seen.insert(state_key(initial, initial));
    for _ in 0..(initial.len() * 2).min(36) {
        if global_timer.elapsed().as_secs_f64() >= ROOM_SECONDS
            || line_timer.elapsed().as_secs_f64() >= LINE_SECONDS
        {
            break;
        }
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..state.cards.len() {
                for half in 1..=(state.cards.len() - start) / 2 {
                    let mut cards = state.cards.clone();
                    for k in 0..half {
                        cards.swap(start + k, start + half + k);
                    }
                    if !seen.insert(state_key(&cards, initial)) {
                        continue;
                    }
                    let score = line_score(&cards, cells, vertical_line, room_id, owner, n);
                    let mut moves = state.moves.clone();
                    moves.push((start, half));
                    next.push(BeamState {
                        cards,
                        moves,
                        score,
                    });
                }
            }
        }
        if next.is_empty() {
            break;
        }
        next.sort_unstable_by_key(|s| (s.score, s.moves.len()));
        next.truncate(BEAM_WIDTH);
        if (next[0].score, next[0].moves.len()) < (best.score, best.moves.len()) {
            best = next[0].clone();
        }
        beam = next;
    }
    if best.score < first_score {
        (best.moves, best.cards)
    } else {
        (Vec::new(), initial.to_vec())
    }
}

fn route_line(
    cells: &[usize],
    vertical_line: bool,
    room: Room,
    owner: &[usize],
    board: &mut [usize],
    pos: &mut [usize],
    dist: &[u16],
    n: usize,
    timer: &Instant,
    output: &mut Vec<Op>,
) {
    let initial: Vec<usize> = cells.iter().map(|&x| board[x]).collect();
    let (moves, final_cards) = beam_line(&initial, cells, vertical_line, room.id, owner, n, timer);
    let m = board.len();
    let before: usize = initial
        .iter()
        .zip(cells)
        .map(|(&card, &cell)| usize::from(dist[card * m + cell]))
        .sum();
    let after: usize = final_cards
        .iter()
        .zip(cells)
        .map(|(&card, &cell)| usize::from(dist[card * m + cell]))
        .sum();
    if after >= before {
        return;
    }
    for (start, half) in moves {
        let first = cells[start];
        let op = if vertical_line {
            Op {
                d: b'V',
                r: first / n,
                c: first % n,
                h: 2 * half,
                w: 1,
            }
        } else {
            Op {
                d: b'H',
                r: first / n,
                c: first % n,
                h: 1,
                w: 2 * half,
            }
        };
        apply(op, board, pos, n);
        output.push(op);
    }
}

/// Column-row-column routing inside each open room. Cards whose destinations
/// lie in another room are wildcards and are left for the doorway/tree stages.
fn route_rooms(
    rooms: &[Room],
    owner: &[usize],
    board: &mut [usize],
    pos: &mut [usize],
    dist: &[u16],
    n: usize,
) -> Vec<Op> {
    let timer = Instant::now();
    let mut out = Vec::new();
    for stage in 0..3 {
        for &room in rooms {
            if room.h * room.w < 4 || timer.elapsed().as_secs_f64() >= ROOM_SECONDS {
                continue;
            }
            if stage == 1 {
                for r in room.r..room.r + room.h {
                    let cells: Vec<_> = (room.c..room.c + room.w).map(|c| r * n + c).collect();
                    route_line(
                        &cells, false, room, owner, board, pos, dist, n, &timer, &mut out,
                    );
                }
            } else {
                for c in room.c..room.c + room.w {
                    let cells: Vec<_> = (room.r..room.r + room.h).map(|r| r * n + c).collect();
                    route_line(
                        &cells, true, room, owner, board, pos, dist, n, &timer, &mut out,
                    );
                }
            }
        }
    }
    out
}

fn doorway_candidates(n: usize, owner: &[usize], v: &[Vec<u8>], h: &[Vec<u8>]) -> Vec<Op> {
    let mut out = Vec::new();
    for c in 0..n - 1 {
        for top in 0..n {
            for bottom in top + 1..=n {
                if (top..bottom).all(|r| owner[r * n + c] != owner[r * n + c + 1]) {
                    let op = Op {
                        d: b'H',
                        r: top,
                        c,
                        h: bottom - top,
                        w: 2,
                    };
                    if rect_open(op, v, h) {
                        out.push(op);
                    }
                }
            }
        }
    }
    for r in 0..n - 1 {
        for left in 0..n {
            for right in left + 1..=n {
                if (left..right).all(|c| owner[r * n + c] != owner[(r + 1) * n + c]) {
                    let op = Op {
                        d: b'V',
                        r,
                        c: left,
                        h: 2,
                        w: right - left,
                    };
                    if rect_open(op, v, h) {
                        out.push(op);
                    }
                }
            }
        }
    }
    out
}

fn greedy_phase(
    candidates: &[Op],
    seconds: f64,
    move_limit: usize,
    board: &mut [usize],
    pos: &mut [usize],
    dist: &[u16],
    n: usize,
) -> Vec<Op> {
    let timer = Instant::now();
    let mut out = Vec::new();
    while out.len() < move_limit && timer.elapsed().as_secs_f64() < seconds {
        let mut choice = None;
        let mut best = 0;
        for &op in candidates {
            let d = op_delta(op, board, dist, n);
            if d < best {
                best = d;
                choice = Some(op);
            }
        }
        let Some(op) = choice else { break };
        apply(op, board, pos, n);
        out.push(op);
    }
    out
}

fn macro_candidates(n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> Vec<Op> {
    let mut out = Vec::new();
    for height in 1..=n {
        for width in 1..=n {
            if height * width == 1 {
                continue;
            }
            let local = height <= 8 && width <= 8;
            let allow_v = height % 2 == 0 && (width <= 4 || local);
            let allow_h = width % 2 == 0 && (height <= 4 || local);
            if !allow_v && !allow_h {
                continue;
            }
            for r in 0..=n - height {
                for c in 0..=n - width {
                    let base = Op {
                        d: b'H',
                        r,
                        c,
                        h: height,
                        w: width,
                    };
                    if !rect_open(base, v, h) {
                        continue;
                    }
                    if allow_h {
                        out.push(base);
                    }
                    if allow_v {
                        out.push(Op { d: b'V', ..base });
                    }
                }
            }
        }
    }
    out
}

fn adjacent(a: usize, b: usize, n: usize) -> Op {
    if a / n == b / n {
        Op {
            d: b'H',
            r: a / n,
            c: (a % n).min(b % n),
            h: 1,
            w: 2,
        }
    } else {
        Op {
            d: b'V',
            r: (a / n).min(b / n),
            c: a % n,
            h: 2,
            w: 1,
        }
    }
}

struct TreePlan {
    tree: Vec<Vec<usize>>,
    parent: Vec<usize>,
    depth: Vec<usize>,
    distance: Vec<u16>,
}

impl TreePlan {
    fn new(g: &[Vec<usize>], root: usize, order: &[usize]) -> Self {
        let m = g.len();
        let mut tree = vec![Vec::new(); m];
        let mut parent = vec![usize::MAX; m];
        let mut depth = vec![0; m];
        let mut q = VecDeque::from([root]);
        parent[root] = root;
        while let Some(x) = q.pop_front() {
            let mut neighbors = g[x].clone();
            neighbors.sort_unstable_by_key(|&y| {
                let direction = if y + 1 == x {
                    0
                } else if y == x + 1 {
                    1
                } else if y > x {
                    2
                } else {
                    3
                };
                order.iter().position(|&d| d == direction).unwrap()
            });
            for y in neighbors {
                if parent[y] != usize::MAX {
                    continue;
                }
                parent[y] = x;
                depth[y] = depth[x] + 1;
                add_edge(&mut tree, x, y);
                q.push_back(y);
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

    fn path(&self, mut a: usize, mut b: usize) -> Vec<usize> {
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

    fn complete(&self, initial: &[usize], n: usize, reverse_tie: bool) -> Vec<Op> {
        let m = initial.len();
        let mut board = initial.to_vec();
        let mut pos = vec![0; m];
        for (cell, &card) in board.iter().enumerate() {
            pos[card] = cell;
        }
        let mut active = vec![true; m];
        let mut degree: Vec<_> = self.tree.iter().map(Vec::len).collect();
        let mut out = Vec::new();
        for _ in 1..m {
            let mut leaf = usize::MAX;
            let mut best = u16::MAX;
            for x in 0..m {
                if active[x] && degree[x] == 1 {
                    let d = self.distance[pos[x] * m + x];
                    let wins_tie = d == best
                        && (leaf == usize::MAX
                            || (reverse_tie && x > leaf)
                            || (!reverse_tie && x < leaf));
                    if d < best || wins_tie {
                        best = d;
                        leaf = x;
                    }
                }
            }
            assert_ne!(leaf, usize::MAX);
            for edge in self.path(pos[leaf], leaf).windows(2) {
                let op = adjacent(edge[0], edge[1], n);
                apply(op, &mut board, &mut pos, n);
                out.push(op);
            }
            active[leaf] = false;
            for &y in &self.tree[leaf] {
                if active[y] {
                    degree[y] -= 1;
                }
            }
            degree[leaf] = 0;
        }
        assert!(board.iter().enumerate().all(|(i, &x)| i == x));
        out
    }
}

/// Fuses commuting adjacent swaps along a wall-free doorway/strip.
fn compress(raw: &[Op], n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> Vec<Op> {
    fn flush(batch: &mut Vec<Op>, out: &mut Vec<Op>, v: &[Vec<u8>], h: &[Vec<u8>]) {
        for d in [b'H', b'V'] {
            let mut items: Vec<_> = batch.iter().copied().filter(|op| op.d == d).collect();
            if d == b'H' {
                items.sort_unstable_by_key(|op| (op.c, op.r));
            } else {
                items.sort_unstable_by_key(|op| (op.r, op.c));
            }
            let mut at = 0;
            while at < items.len() {
                let first = items[at];
                let mut end = at + 1;
                while end < items.len() {
                    let next = items[end];
                    let expected = if d == b'H' {
                        next.c == first.c && next.r == items[end - 1].r + 1
                    } else {
                        next.r == first.r && next.c == items[end - 1].c + 1
                    };
                    let fused = if d == b'H' {
                        Op {
                            h: end - at + 1,
                            ..first
                        }
                    } else {
                        Op {
                            w: end - at + 1,
                            ..first
                        }
                    };
                    if !expected || !rect_open(fused, v, h) {
                        break;
                    }
                    end += 1;
                }
                out.push(if d == b'H' {
                    Op {
                        h: end - at,
                        ..first
                    }
                } else {
                    Op {
                        w: end - at,
                        ..first
                    }
                });
                at = end;
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

fn maximum_open_rectangle(n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> usize {
    let mut best = 1;
    for top in 0..n {
        let mut column_ok = vec![true; n];
        for bottom in top..n {
            if bottom > top {
                for c in 0..n {
                    column_ok[c] &= h[bottom - 1][c] == b'0';
                }
            }
            let mut left = 0;
            for c in 0..n {
                if c > 0 && (top..=bottom).any(|r| v[r][c - 1] == b'1') {
                    left = c;
                }
                if column_ok[c] {
                    best = best.max((bottom - top + 1) * (c - left + 1));
                } else {
                    left = c + 1;
                }
            }
        }
    }
    best
}

fn choose_solver(n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> SolverKind {
    let wall_count = v
        .iter()
        .chain(h.iter())
        .map(|line| line.iter().filter(|&&wall| wall == b'1').count())
        .sum::<usize>();
    if wall_count == 0 {
        SolverKind::GreedyZero
    } else if maximum_open_rectangle(n, v, h) <= 98 {
        SolverKind::Region
    } else {
        SolverKind::Tree
    }
}

fn zero_augment(
    source: usize,
    cards: &[Vec<usize>],
    used: &[bool],
    seen: &mut [bool],
    matched_source: &mut [usize],
    chosen: &mut [usize],
    n: usize,
) -> bool {
    for &card in &cards[source] {
        if used[card] {
            continue;
        }
        let target = card % n;
        if seen[target] {
            continue;
        }
        seen[target] = true;
        let previous = matched_source[target];
        if previous == usize::MAX
            || zero_augment(previous, cards, used, seen, matched_source, chosen, n)
        {
            matched_source[target] = source;
            chosen[source] = card;
            return true;
        }
    }
    false
}

fn zero_intermediate_rows(initial: &[usize], n: usize) -> Vec<usize> {
    let size = n * n;
    let cards = (0..n)
        .map(|c| (0..n).map(|r| initial[r * n + c]).collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let mut used = vec![false; size];
    let mut row = vec![usize::MAX; size];
    for color in 0..n {
        let mut matched_source = vec![usize::MAX; n];
        let mut chosen = vec![usize::MAX; n];
        for source in 0..n {
            let mut seen = vec![false; n];
            assert!(zero_augment(
                source,
                &cards,
                &used,
                &mut seen,
                &mut matched_source,
                &mut chosen,
                n,
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
struct ZeroState {
    keys: [u8; 20],
    moves: [u16; ZERO_BEAM_DEPTH],
    move_count: u8,
    cost: i32,
}

fn zero_line_cost(keys: &[u8]) -> i32 {
    let len = keys.len();
    let mut breakpoints = i32::from(keys[0] != 0)
        + i32::from(keys[len - 1] as usize + 1 != len)
        + keys
            .windows(2)
            .map(|pair| i32::from(pair[1] != pair[0] + 1))
            .sum::<i32>();
    let displacement = keys
        .iter()
        .enumerate()
        .map(|(i, &key)| i.abs_diff(key as usize))
        .sum::<usize>();
    breakpoints *= 100;
    breakpoints + displacement as i32
}

fn zero_line_key(keys: &[u8]) -> u128 {
    keys.iter()
        .enumerate()
        .fold(0, |key, (i, &value)| key | (value as u128) << (5 * i))
}

fn zero_line_moves(initial: &[u8], timer: &Instant) -> Vec<(usize, usize)> {
    let len = initial.len();
    let mut keys = [0; 20];
    keys[..len].copy_from_slice(initial);
    let initial_cost = zero_line_cost(initial);
    let initial_state = ZeroState {
        keys,
        moves: [0; ZERO_BEAM_DEPTH],
        move_count: 0,
        cost: initial_cost,
    };
    let mut best = initial_state;
    let mut beam = vec![initial_state];
    let mut seen = HashSet::from([zero_line_key(initial)]);
    for _ in 0..ZERO_BEAM_DEPTH {
        if timer.elapsed().as_secs_f64() >= ZERO_SECONDS || best.cost == 0 {
            break;
        }
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..len {
                for half in 1..=(len - start) / 2 {
                    let mut child = *state;
                    for offset in 0..half {
                        child.keys.swap(start + offset, start + half + offset);
                    }
                    if !seen.insert(zero_line_key(&child.keys[..len])) {
                        continue;
                    }
                    child.moves[child.move_count as usize] = start as u16 | ((half as u16) << 5);
                    child.move_count += 1;
                    child.cost = zero_line_cost(&child.keys[..len]);
                    if child.cost < best.cost {
                        best = child;
                    }
                    next.push(child);
                }
            }
        }
        next.sort_unstable_by_key(|state| state.cost);
        next.truncate(BEAM_WIDTH);
        if next.is_empty() {
            break;
        }
        beam = next;
    }
    if best.cost < initial_cost {
        best.moves[..best.move_count as usize]
            .iter()
            .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
            .collect()
    } else {
        Vec::new()
    }
}

fn greedy_zero_prefix(initial: &[usize], n: usize) -> (Vec<usize>, Vec<Op>) {
    let size = n * n;
    let middle = zero_intermediate_rows(initial, n);
    let target_column = (0..size).map(|card| card % n).collect::<Vec<_>>();
    let target_row = (0..size).map(|card| card / n).collect::<Vec<_>>();
    let mut board = initial.to_vec();
    let mut pos = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        pos[card] = cell;
    }
    let mut output = Vec::new();
    let timer = Instant::now();
    for (vertical, desired) in [
        (true, middle.as_slice()),
        (false, target_column.as_slice()),
        (true, target_row.as_slice()),
    ] {
        for line in 0..n {
            if timer.elapsed().as_secs_f64() >= ZERO_SECONDS {
                return (board, output);
            }
            let cells = if vertical {
                (0..n).map(|at| at * n + line).collect::<Vec<_>>()
            } else {
                (0..n).map(|at| line * n + at).collect::<Vec<_>>()
            };
            let keys = cells
                .iter()
                .map(|&cell| desired[board[cell]] as u8)
                .collect::<Vec<_>>();
            for (start, half) in zero_line_moves(&keys, &timer) {
                let op = if vertical {
                    Op {
                        d: b'V',
                        r: start,
                        c: line,
                        h: 2 * half,
                        w: 1,
                    }
                } else {
                    Op {
                        d: b'H',
                        r: line,
                        c: start,
                        h: 1,
                        w: 2 * half,
                    }
                };
                apply(op, &mut board, &mut pos, n);
                output.push(op);
            }
        }
    }
    (board, output)
}

fn replay(initial: &[usize], operations: &[Op], n: usize, v: &[Vec<u8>], h: &[Vec<u8>]) -> bool {
    if operations.len() > 100_000 {
        return false;
    }
    let mut board = initial.to_vec();
    let mut pos = vec![0; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        pos[card] = cell;
    }
    for &op in operations {
        if !legal(op, n, v, h) {
            return false;
        }
        apply(op, &mut board, &mut pos, n);
    }
    board.iter().enumerate().all(|(cell, &card)| cell == card)
}

fn solve(input: &str) -> String {
    let mut sc = Scanner(input.split_whitespace());
    let n: usize = sc.next();
    let m = n * n;
    let initial: Vec<usize> = (0..m).map(|_| sc.next()).collect();
    let v: Vec<Vec<u8>> = (0..n).map(|_| sc.next::<String>().into_bytes()).collect();
    let h: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| sc.next::<String>().into_bytes())
        .collect();

    let mut graph = vec![Vec::new(); m];
    for r in 0..n {
        for c in 0..n - 1 {
            if v[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, r * n + c + 1);
            }
        }
    }
    for r in 0..n - 1 {
        for c in 0..n {
            if h[r][c] == b'0' {
                add_edge(&mut graph, r * n + c, (r + 1) * n + c);
            }
        }
    }
    let dist = all_distances(&graph);
    assert!(dist.iter().all(|&x| x != u16::MAX));
    let solver_kind = choose_solver(n, &v, &h);

    let mut board = initial.clone();
    let mut pos = vec![0; m];
    for (cell, &card) in board.iter().enumerate() {
        pos[card] = cell;
    }
    let mut checkpoints = vec![(board.clone(), Vec::<Op>::new())];
    match solver_kind {
        SolverKind::Tree => {}
        SolverKind::GreedyZero => {
            let (zero_board, zero_prefix) = greedy_zero_prefix(&initial, n);
            checkpoints.push((zero_board, zero_prefix));
        }
        SolverKind::Region => {
            let (rooms, owner) = decompose_rooms(n, &v, &h);
            let mut prefix = route_rooms(&rooms, &owner, &mut board, &mut pos, &dist, n);
            checkpoints.push((board.clone(), prefix.clone()));

            let doors = doorway_candidates(n, &owner, &v, &h);
            prefix.extend(greedy_phase(
                &doors,
                DOOR_SECONDS,
                80,
                &mut board,
                &mut pos,
                &dist,
                n,
            ));
            checkpoints.push((board.clone(), prefix.clone()));

            let macros = macro_candidates(n, &v, &h);
            prefix.extend(greedy_phase(
                &macros,
                MACRO_SECONDS,
                20_000,
                &mut board,
                &mut pos,
                &dist,
                n,
            ));
            checkpoints.push((board, prefix));
        }
    }

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
    let mut roots = vec![(n / 2) * n + n / 2, 0, n - 1, (n - 1) * n, m - 1];
    if solver_kind == SolverKind::Tree {
        roots.extend([n / 2, (n - 1) * n + n / 2, (n / 2) * n, (n / 2) * n + n - 1]);
    }
    let emergency_plan = TreePlan::new(&graph, roots[0], &ORDERS[0]);
    let emergency_raw = emergency_plan.complete(&initial, n, false);
    let emergency = compress(&emergency_raw, n, &v, &h);
    let mut best = if replay(&initial, &emergency, n, &v, &h) {
        emergency.clone()
    } else {
        emergency_raw.clone()
    };
    for (ri, &root) in roots.iter().enumerate() {
        for (oi, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(&graph, root, order);
            for (state, pre) in &checkpoints {
                let tail = compress(&plan.complete(state, n, (ri + oi) % 2 == 1), n, &v, &h);
                if pre.len() + tail.len() < best.len() {
                    let mut candidate = pre.clone();
                    candidate.extend(tail);
                    best = candidate;
                }
            }
        }
    }
    if !replay(&initial, &best, n, &v, &h) {
        best = if replay(&initial, &emergency, n, &v, &h) {
            emergency
        } else {
            emergency_raw
        };
    }
    assert!(replay(&initial, &best, n, &v, &h));

    let mut output = String::new();
    for op in best {
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
