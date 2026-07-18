use std::collections::{HashSet, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const LINE_BEAM_WIDTH: usize = 200;
const LINE_ROUTE_SECONDS: f64 = 0.48;

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

fn apply(op: Operation, board: &mut [usize], position: &mut [usize], n: usize) {
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

fn rectangle_open(
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

fn all_distances(graph: &[Vec<usize>]) -> Vec<u16> {
    let size = graph.len();
    let mut distances = vec![u16::MAX; size * size];
    let mut queue = VecDeque::with_capacity(size);
    for source in 0..size {
        distances[source * size + source] = 0;
        queue.push_back(source);
        while let Some(v) = queue.pop_front() {
            let next = distances[source * size + v] + 1;
            for &to in &graph[v] {
                let index = source * size + to;
                if distances[index] == u16::MAX {
                    distances[index] = next;
                    queue.push_back(to);
                }
            }
        }
    }
    distances
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
        let mut depth = vec![0usize; size];
        parent[root] = root;
        let mut queue = VecDeque::from([root]);
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
                let d = self.distance[position[candidate] * size + candidate];
                let tie = d == best_distance
                    && (leaf == usize::MAX
                        || (prefer_larger && candidate > leaf)
                        || (!prefer_larger && candidate < leaf));
                if d < best_distance || tie {
                    best_distance = d;
                    leaf = candidate;
                }
            }
            assert_ne!(leaf, usize::MAX);
            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&v| active[v]));
            for edge in path.windows(2) {
                let op = adjacent_operation(edge[0], edge[1], n);
                apply(op, &mut board, &mut position, n);
                operations.push(op);
            }
            active[leaf] = false;
            remaining -= 1;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
            degree[leaf] = 0;
        }
        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
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

fn augment_matching(
    source_row: usize,
    cards_by_row: &[Vec<usize>],
    used_card: &[bool],
    seen_target: &mut [bool],
    matched_source: &mut [usize],
    chosen_card: &mut [usize],
    n: usize,
) -> bool {
    for &card in &cards_by_row[source_row] {
        if used_card[card] {
            continue;
        }
        let target_row = card / n;
        if seen_target[target_row] {
            continue;
        }
        seen_target[target_row] = true;
        let previous = matched_source[target_row];
        if previous == usize::MAX
            || augment_matching(
                previous,
                cards_by_row,
                used_card,
                seen_target,
                matched_source,
                chosen_card,
                n,
            )
        {
            matched_source[target_row] = source_row;
            chosen_card[source_row] = card;
            return true;
        }
    }
    false
}

fn line_key(card: usize, mode: usize, assigned_column: &[usize], n: usize) -> usize {
    match mode {
        0 => assigned_column[card],
        1 => card / n,
        _ => card % n,
    }
}

fn sort_line(
    cells: &[usize],
    mode: usize,
    assigned_column: &[usize],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    output: &mut Vec<Operation>,
) {
    loop {
        let mut best_delta = 0isize;
        let mut best = None;
        for start in 0..n {
            for half in 2..=(n - start) / 2 {
                let mut value = 0isize;
                for offset in 0..half {
                    let a = start + offset;
                    let b = start + half + offset;
                    let x = line_key(board[cells[a]], mode, assigned_column, n);
                    let y = line_key(board[cells[b]], mode, assigned_column, n);
                    value += b.abs_diff(x) as isize + a.abs_diff(y) as isize
                        - a.abs_diff(x) as isize
                        - b.abs_diff(y) as isize;
                }
                if value < best_delta {
                    best_delta = value;
                    best = Some((start, half));
                }
            }
        }
        let Some((start, half)) = best else { break };
        let first = cells[0];
        let op = if cells[1] == first + 1 {
            Operation {
                direction: b'H',
                r: first / n,
                c: start,
                h: 1,
                w: 2 * half,
            }
        } else {
            Operation {
                direction: b'V',
                r: start,
                c: first % n,
                h: 2 * half,
                w: 1,
            }
        };
        apply(op, board, position, n);
        output.push(op);
    }
    for target in 0..n {
        let mut at = target;
        while line_key(board[cells[at]], mode, assigned_column, n) != target {
            at += 1;
        }
        while at > target {
            let op = adjacent_operation(cells[at - 1], cells[at], n);
            apply(op, board, position, n);
            output.push(op);
            at -= 1;
        }
    }
}

/// Routes any permutation on a completely open mesh in row-column-row stages.
fn mesh_route(initial: &[usize], n: usize) -> Vec<Operation> {
    let size = n * n;
    let mut cards_by_row = vec![Vec::with_capacity(n); n];
    for row in 0..n {
        cards_by_row[row].extend_from_slice(&initial[row * n..(row + 1) * n]);
    }
    let mut used_card = vec![false; size];
    let mut assigned_column = vec![usize::MAX; size];
    for column in 0..n {
        let mut matched_source = vec![usize::MAX; n];
        let mut chosen_card = vec![usize::MAX; n];
        for source_row in 0..n {
            let mut seen_target = vec![false; n];
            assert!(augment_matching(
                source_row,
                &cards_by_row,
                &used_card,
                &mut seen_target,
                &mut matched_source,
                &mut chosen_card,
                n,
            ));
        }
        for card in chosen_card {
            assert_ne!(card, usize::MAX);
            used_card[card] = true;
            assigned_column[card] = column;
        }
    }

    let mut board = initial.to_vec();
    let mut position = vec![0usize; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut operations = Vec::new();
    for row in 0..n {
        let cells: Vec<usize> = (0..n).map(|c| row * n + c).collect();
        sort_line(
            &cells,
            0,
            &assigned_column,
            &mut board,
            &mut position,
            n,
            &mut operations,
        );
    }
    for column in 0..n {
        let cells: Vec<usize> = (0..n).map(|r| r * n + column).collect();
        sort_line(
            &cells,
            1,
            &assigned_column,
            &mut board,
            &mut position,
            n,
            &mut operations,
        );
    }
    for row in 0..n {
        let cells: Vec<usize> = (0..n).map(|c| row * n + c).collect();
        sort_line(
            &cells,
            2,
            &assigned_column,
            &mut board,
            &mut position,
            n,
            &mut operations,
        );
    }
    assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
    assert!(operations.len() <= 100_000);
    operations
}

/// A maximal consecutive set of pairwise-disjoint swaps may be reordered.
/// Parallel swaps are fused only when the entire resulting rectangle is open.
fn compress_fallback(
    operations: &[Operation],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    fn flush(
        batch: &mut Vec<Operation>,
        output: &mut Vec<Operation>,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) {
        for direction in [b'H', b'V'] {
            let mut indices: Vec<usize> = (0..batch.len())
                .filter(|&i| batch[i].direction == direction)
                .collect();
            if direction == b'H' {
                indices.sort_unstable_by_key(|&i| (batch[i].c, batch[i].r));
            } else {
                indices.sort_unstable_by_key(|&i| (batch[i].r, batch[i].c));
            }
            let mut at = 0;
            while at < indices.len() {
                let first = batch[indices[at]];
                let mut end = at + 1;
                while end < indices.len() {
                    let previous = batch[indices[end - 1]];
                    let next = batch[indices[end]];
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
                        direction,
                        r: first.r,
                        c: first.c,
                        h: length,
                        w: 2,
                    }
                } else {
                    Operation {
                        direction,
                        r: first.r,
                        c: first.c,
                        h: 2,
                        w: length,
                    }
                });
                at = end;
            }
        }
        batch.clear();
    }

    let mut output = Vec::new();
    let mut batch = Vec::new();
    let mut occupied = vec![false; n * n];
    for &op in operations {
        debug_assert!(op.h * op.w == 2);
        let a = op.r * n + op.c;
        let b = if op.direction == b'H' { a + 1 } else { a + n };
        if occupied[a] || occupied[b] {
            flush(&mut batch, &mut output, vertical, horizontal);
            occupied.fill(false);
        }
        occupied[a] = true;
        occupied[b] = true;
        batch.push(op);
    }
    flush(&mut batch, &mut output, vertical, horizontal);
    output
}

fn augment_column_matching(
    source_column: usize,
    cards_by_column: &[Vec<usize>],
    used_card: &[bool],
    seen_target: &mut [bool],
    matched_source: &mut [usize],
    chosen_card: &mut [usize],
    n: usize,
) -> bool {
    for &card in &cards_by_column[source_column] {
        if used_card[card] {
            continue;
        }
        let target_column = card % n;
        if seen_target[target_column] {
            continue;
        }
        seen_target[target_column] = true;
        let previous = matched_source[target_column];
        if previous == usize::MAX
            || augment_column_matching(
                previous,
                cards_by_column,
                used_card,
                seen_target,
                matched_source,
                chosen_card,
                n,
            )
        {
            matched_source[target_column] = source_column;
            chosen_card[source_column] = card;
            return true;
        }
    }
    false
}

fn assign_intermediate_rows(initial: &[usize], n: usize) -> Vec<usize> {
    let size = n * n;
    let mut cards_by_column = vec![Vec::with_capacity(n); n];
    for r in 0..n {
        for c in 0..n {
            cards_by_column[c].push(initial[r * n + c]);
        }
    }
    let mut used_card = vec![false; size];
    let mut assigned_row = vec![usize::MAX; size];
    for intermediate_row in 0..n {
        let mut matched_source = vec![usize::MAX; n];
        let mut chosen_card = vec![usize::MAX; n];
        for source_column in 0..n {
            let mut seen_target = vec![false; n];
            assert!(augment_column_matching(
                source_column,
                &cards_by_column,
                &used_card,
                &mut seen_target,
                &mut matched_source,
                &mut chosen_card,
                n,
            ));
        }
        for card in chosen_card {
            assert_ne!(card, usize::MAX);
            used_card[card] = true;
            assigned_row[card] = intermediate_row;
        }
    }
    assigned_row
}

#[derive(Clone)]
struct LineState {
    cards: Vec<usize>,
    operations: Vec<(usize, usize)>,
    score: usize,
}

fn line_target(card: usize, stage: usize, assigned_row: &[usize], n: usize) -> usize {
    match stage {
        0 => assigned_row[card],
        1 => card % n,
        _ => card / n,
    }
}

fn line_score(
    cards: &[usize],
    segment_start: usize,
    stage: usize,
    assigned_row: &[usize],
    n: usize,
) -> usize {
    let segment_end = segment_start + cards.len();
    let mut displacement = 0;
    let mut breakpoints = 0;
    let mut previous: Option<usize> = None;
    for (offset, &card) in cards.iter().enumerate() {
        let target = line_target(card, stage, assigned_row, n);
        if !(segment_start..segment_end).contains(&target) {
            previous = None; // a wildcard separates constrained runs
            continue;
        }
        displacement += (segment_start + offset).abs_diff(target);
        if let Some(value) = previous {
            if target != value + 1 {
                breakpoints += 1;
            }
        } else if target != segment_start + offset {
            breakpoints += 1;
        }
        previous = Some(target);
    }
    breakpoints * 100 + displacement
}

fn line_hash(cards: &[usize]) -> u128 {
    let mut a = 0x6a09e667f3bcc909_u64;
    let mut b = 0xbb67ae8584caa73b_u64;
    for (index, &card) in cards.iter().enumerate() {
        a ^= (card as u64).wrapping_add((index as u64) << 32);
        a = a.rotate_left(13).wrapping_mul(0x9e3779b185ebca87);
        b ^= a.wrapping_add(card as u64 * 0x100000001b3);
        b = b.rotate_left(17).wrapping_mul(0xc2b2ae3d27d4eb4f);
    }
    ((a as u128) << 64) | b as u128
}

fn beam_sort_segment(
    initial: &[usize],
    segment_start: usize,
    stage: usize,
    assigned_row: &[usize],
    n: usize,
    timer: &Instant,
) -> Vec<(usize, usize)> {
    if initial.len() < 2 || timer.elapsed().as_secs_f64() >= LINE_ROUTE_SECONDS {
        return Vec::new();
    }
    let initial_score = line_score(initial, segment_start, stage, assigned_row, n);
    let mut best = LineState {
        cards: initial.to_vec(),
        operations: Vec::new(),
        score: initial_score,
    };
    let mut beam = vec![best.clone()];
    let mut seen = HashSet::new();
    seen.insert(line_hash(initial));
    let max_depth = (initial.len() * initial.len()).min(64);
    for _ in 0..max_depth {
        if timer.elapsed().as_secs_f64() >= LINE_ROUTE_SECONDS || best.score == 0 {
            break;
        }
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..state.cards.len() {
                for half in 1..=(state.cards.len() - start) / 2 {
                    let mut cards = state.cards.clone();
                    for offset in 0..half {
                        cards.swap(start + offset, start + half + offset);
                    }
                    if !seen.insert(line_hash(&cards)) {
                        continue;
                    }
                    let score = line_score(&cards, segment_start, stage, assigned_row, n);
                    let mut operations = state.operations.clone();
                    operations.push((start, half));
                    next.push(LineState {
                        cards,
                        operations,
                        score,
                    });
                }
            }
        }
        if next.is_empty() {
            break;
        }
        next.sort_unstable_by_key(|state| (state.score, state.operations.len()));
        next.truncate(LINE_BEAM_WIDTH);
        if next[0].score < best.score {
            best = next[0].clone();
        }
        beam = next;
    }
    if best.score < initial_score {
        best.operations
    } else {
        Vec::new()
    }
}

fn route_segment(
    cells: &[usize],
    segment_start: usize,
    stage: usize,
    assigned_row: &[usize],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    timer: &Instant,
    output: &mut Vec<Operation>,
) {
    let cards = cells.iter().map(|&cell| board[cell]).collect::<Vec<_>>();
    let sequence = beam_sort_segment(&cards, segment_start, stage, assigned_row, n, timer);
    for (start, half) in sequence {
        let first = cells[start];
        let op = if stage == 1 {
            Operation {
                direction: b'H',
                r: first / n,
                c: first % n,
                h: 1,
                w: 2 * half,
            }
        } else {
            Operation {
                direction: b'V',
                r: first / n,
                c: first % n,
                h: 2 * half,
                w: 1,
            }
        };
        apply(op, board, position, n);
        output.push(op);
    }
}

fn line_route(
    initial: &[usize],
    assigned_row: &[usize],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> (Vec<usize>, Vec<Operation>) {
    let mut board = initial.to_vec();
    let mut position = vec![0; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut output = Vec::new();
    let timer = Instant::now();
    for stage in 0..3 {
        if stage == 1 {
            for r in 0..n {
                let mut left = 0;
                while left < n {
                    let mut right = left + 1;
                    while right < n && vertical[r][right - 1] == b'0' {
                        right += 1;
                    }
                    let cells = (left..right).map(|c| r * n + c).collect::<Vec<_>>();
                    route_segment(
                        &cells,
                        left,
                        stage,
                        assigned_row,
                        &mut board,
                        &mut position,
                        n,
                        &timer,
                        &mut output,
                    );
                    left = right;
                }
            }
        } else {
            for c in 0..n {
                let mut top = 0;
                while top < n {
                    let mut bottom = top + 1;
                    while bottom < n && horizontal[bottom - 1][c] == b'0' {
                        bottom += 1;
                    }
                    let cells = (top..bottom).map(|r| r * n + c).collect::<Vec<_>>();
                    route_segment(
                        &cells,
                        top,
                        stage,
                        assigned_row,
                        &mut board,
                        &mut position,
                        n,
                        &timer,
                        &mut output,
                    );
                    top = bottom;
                }
            }
        }
    }
    (board, output)
}

fn legal_operation(op: Operation, n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> bool {
    op.r + op.h <= n
        && op.c + op.w <= n
        && ((op.direction == b'V' && op.h % 2 == 0) || (op.direction == b'H' && op.w % 2 == 0))
        && rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
}

fn replay_valid(
    initial: &[usize],
    operations: &[Operation],
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
        if !legal_operation(op, n, vertical, horizontal) {
            return false;
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
    let fully_open = vertical
        .iter()
        .chain(horizontal.iter())
        .all(|row| row.iter().all(|&wall| wall == b'0'));
    let mesh_candidate = fully_open.then(|| mesh_route(&initial, n));
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
    let assigned_row = assign_intermediate_rows(&initial, n);
    let (routed_board, routed_prefix) =
        line_route(&initial, &assigned_row, n, &vertical, &horizontal);

    let roots = [center, 0, n - 1, (n - 1) * n, n * n - 1];
    let mut safe_result: Option<Vec<Operation>> = None;
    let mut routed_result: Option<Vec<Operation>> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let prefer_larger = (root_index + order_index) % 2 == 1;

            let raw_safe = plan.complete(&initial, n, prefer_larger);
            let compressed_safe = compress_fallback(&raw_safe, n, &vertical, &horizontal);
            if safe_result
                .as_ref()
                .map_or(true, |saved| compressed_safe.len() < saved.len())
            {
                safe_result = Some(compressed_safe);
            }

            let raw_routed = plan.complete(&routed_board, n, prefer_larger);
            let compressed_routed = compress_fallback(&raw_routed, n, &vertical, &horizontal);
            if routed_prefix.len() + compressed_routed.len() <= 100_000 {
                let mut candidate = routed_prefix.clone();
                candidate.extend(compressed_routed);
                if routed_result
                    .as_ref()
                    .map_or(true, |saved| candidate.len() < saved.len())
                {
                    routed_result = Some(candidate);
                }
            }
        }
    }

    let safe_result = safe_result.expect("a safe exact candidate exists");
    let mut result = safe_result.clone();
    if let Some(routed) = routed_result {
        if routed.len() < result.len() {
            result = routed;
        }
    }
    if let Some(mesh) = mesh_candidate {
        if mesh.len() < result.len() {
            result = mesh;
        }
    }
    if !replay_valid(&initial, &result, n, &vertical, &horizontal) {
        result = safe_result;
    }
    assert!(replay_valid(&initial, &result, n, &vertical, &horizontal));
    assert!(result.len() <= 100_000);
    let mut output = String::new();
    for op in result {
        writeln!(
            output,
            "{} {} {} {} {}",
            op.direction as char, op.r, op.c, op.h, op.w
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
