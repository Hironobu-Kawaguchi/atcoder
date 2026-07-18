use std::collections::{HashSet, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};

const WILDCARD: u8 = 31;
const LINE_BEAM: usize = 128;
const LINE_DEPTH: usize = 14;
const ASSIGNMENT_RESTARTS: usize = 32;

struct Scanner<'a>(std::str::SplitWhitespace<'a>);

impl<'a> Scanner<'a> {
    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.0.next().unwrap().parse().unwrap()
    }
}

#[derive(Clone, Copy, Debug)]
struct Operation {
    direction: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

fn apply(op: Operation, board: &mut [usize], position: &mut [usize], n: usize) {
    let mut swap = |a: usize, b: usize| {
        board.swap(a, b);
        position[board[a]] = a;
        position[board[b]] = b;
    };
    if op.direction == b'H' {
        for dr in 0..op.h {
            for dc in 0..op.w / 2 {
                swap(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + dr) * n + op.c + op.w / 2 + dc,
                );
            }
        }
    } else {
        for dr in 0..op.h / 2 {
            for dc in 0..op.w {
                swap(
                    (op.r + dr) * n + op.c + dc,
                    (op.r + op.h / 2 + dr) * n + op.c + dc,
                );
            }
        }
    }
}

fn rectangle_open(op: Operation, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> bool {
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
    true
}

fn legal(op: Operation, n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> bool {
    op.h > 0
        && op.w > 0
        && op.r + op.h <= n
        && op.c + op.w <= n
        && ((op.direction == b'H' && op.w % 2 == 0) || (op.direction == b'V' && op.h % 2 == 0))
        && rectangle_open(op, vertical, horizontal)
}

fn replay_sorted(
    initial: &[usize],
    operations: &[Operation],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> bool {
    if operations.len() > 100_000 {
        return false;
    }
    let mut board = initial.to_vec();
    let mut position = vec![0; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    for &op in operations {
        if !legal(op, n, vertical, horizontal) {
            return false;
        }
        apply(op, &mut board, &mut position, n);
    }
    board.iter().enumerate().all(|(cell, &card)| cell == card)
}

fn horizontal_segments(n: usize, vertical: &[Vec<u8>]) -> (Vec<Vec<usize>>, Vec<usize>) {
    let mut segments = Vec::new();
    let mut id = vec![usize::MAX; n * n];
    for r in 0..n {
        let mut start = 0;
        for c in 0..n {
            if c + 1 == n || vertical[r][c] == b'1' {
                let index = segments.len();
                let cells: Vec<usize> = (start..=c).map(|x| r * n + x).collect();
                for &cell in &cells {
                    id[cell] = index;
                }
                segments.push(cells);
                start = c + 1;
            }
        }
    }
    (segments, id)
}

fn vertical_segments(n: usize, horizontal: &[Vec<u8>]) -> (Vec<Vec<usize>>, Vec<usize>) {
    let mut segments = Vec::new();
    let mut id = vec![usize::MAX; n * n];
    for c in 0..n {
        let mut start = 0;
        for r in 0..n {
            if r + 1 == n || horizontal[r][c] == b'1' {
                let index = segments.len();
                let cells: Vec<usize> = (start..=r).map(|x| x * n + c).collect();
                for &cell in &cells {
                    id[cell] = index;
                }
                segments.push(cells);
                start = r + 1;
            }
        }
    }
    (segments, id)
}

fn feasibility_masks(
    initial: &[usize],
    n: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
) -> (Vec<u32>, Vec<Vec<usize>>) {
    let size = n * n;
    let mut initial_position = vec![0; size];
    for (cell, &card) in initial.iter().enumerate() {
        initial_position[card] = cell;
    }
    let mut masks = vec![0u32; size];
    let mut cards_by_source = vec![Vec::with_capacity(n); n];
    for card in 0..size {
        let source = initial_position[card];
        let source_column = source % n;
        let target_column = card % n;
        cards_by_source[source_column].push(card);
        for middle_row in 0..n {
            let first = middle_row * n + source_column;
            let second = middle_row * n + target_column;
            if vertical_id[source] == vertical_id[first]
                && horizontal_id[first] == horizontal_id[second]
                && vertical_id[second] == vertical_id[card]
            {
                masks[card] |= 1u32 << middle_row;
            }
        }
    }
    (masks, cards_by_source)
}

struct KuhnContext<'a> {
    cards_by_source: &'a [Vec<usize>],
    feasible: &'a [u32],
    used: &'a [bool],
    middle_row: usize,
}

fn augment_row(
    source: usize,
    context: &KuhnContext<'_>,
    seen_target: &mut [bool],
    matched_source: &mut [usize],
    chosen_card: &mut [usize],
    n: usize,
) -> bool {
    for &card in &context.cards_by_source[source] {
        if context.used[card] || context.feasible[card] & (1u32 << context.middle_row) == 0 {
            continue;
        }
        let target = card % n;
        if seen_target[target] {
            continue;
        }
        seen_target[target] = true;
        let previous = matched_source[target];
        if previous == usize::MAX
            || augment_row(
                previous,
                context,
                seen_target,
                matched_source,
                chosen_card,
                n,
            )
        {
            matched_source[target] = source;
            chosen_card[source] = card;
            return true;
        }
    }
    false
}

fn rotated_order(n: usize, shift: usize, reverse: bool) -> Vec<usize> {
    let mut order: Vec<usize> = (0..n).map(|i| (i + shift) % n).collect();
    if reverse {
        order.reverse();
    }
    order
}

/// Assigns a feasible C-R-C middle row to as many cards as possible.  Each
/// restart is deterministic and uses a different row/source/card ordering.
fn constrained_middle_rows(
    initial: &[usize],
    n: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
) -> Vec<usize> {
    let size = n * n;
    let (feasible, base_cards) = feasibility_masks(initial, n, horizontal_id, vertical_id);
    let mut best = vec![usize::MAX; size];
    let mut best_count = 0;
    for restart in 0..ASSIGNMENT_RESTARTS {
        let mut cards_by_source = base_cards.clone();
        for (source, cards) in cards_by_source.iter_mut().enumerate() {
            cards.sort_unstable_by_key(|&card| {
                let salt = (restart as u64 + 1).wrapping_mul(0x9e37_79b9_7f4a_7c15);
                (card as u64)
                    .wrapping_mul(0xbf58_476d_1ce4_e5b9)
                    .wrapping_add((source as u64).wrapping_mul(0x94d0_49bb_1331_11eb))
                    ^ salt
            });
        }
        let rows = rotated_order(n, (restart * 7) % n, restart & 1 != 0);
        let sources = rotated_order(n, (restart * 11) % n, restart & 2 != 0);
        let mut used = vec![false; size];
        let mut assigned = vec![usize::MAX; size];
        let mut count = 0;
        for middle_row in rows {
            let mut matched_source = vec![usize::MAX; n];
            let mut chosen_card = vec![usize::MAX; n];
            let context = KuhnContext {
                cards_by_source: &cards_by_source,
                feasible: &feasible,
                used: &used,
                middle_row,
            };
            for &source in &sources {
                let mut seen_target = vec![false; n];
                augment_row(
                    source,
                    &context,
                    &mut seen_target,
                    &mut matched_source,
                    &mut chosen_card,
                    n,
                );
            }
            for card in chosen_card.into_iter().filter(|&card| card != usize::MAX) {
                debug_assert!(!used[card]);
                used[card] = true;
                assigned[card] = middle_row;
                count += 1;
            }
        }
        if count > best_count {
            best_count = count;
            best = assigned;
        }
    }
    best
}

#[derive(Clone, Copy)]
struct LineState {
    keys: [u8; 20],
    moves: [u16; LINE_DEPTH],
    move_len: u8,
    cost: i32,
}

fn line_key(keys: &[u8]) -> u128 {
    keys.iter()
        .enumerate()
        .fold(0, |result, (i, &key)| result | (key as u128) << (5 * i))
}

/// Wildcards are genuinely indistinguishable: they have no target, no
/// displacement, and break adjacency chains rather than receiving fake slots.
fn line_cost(keys: &[u8]) -> i32 {
    let mut misplaced = 0;
    let mut displacement = 0;
    let mut breakpoints = 0;
    let mut previous: Option<(usize, u8)> = None;
    for (i, &key) in keys.iter().enumerate() {
        if key == WILDCARD {
            previous = None;
            continue;
        }
        misplaced += i32::from(key as usize != i);
        displacement += i.abs_diff(key as usize) as i32;
        if let Some((previous_i, previous_key)) = previous {
            if i == previous_i + 1 && key != previous_key + 1 {
                breakpoints += 1;
            }
        }
        previous = Some((i, key));
    }
    256 * misplaced + 16 * breakpoints + displacement
}

fn solve_line(keys: &[u8]) -> Vec<(usize, usize)> {
    let len = keys.len();
    if len < 2 || line_cost(keys) == 0 {
        return Vec::new();
    }
    let mut initial = [WILDCARD; 20];
    initial[..len].copy_from_slice(keys);
    let mut beam = vec![LineState {
        keys: initial,
        moves: [0; LINE_DEPTH],
        move_len: 0,
        cost: line_cost(keys),
    }];
    let mut best = beam[0];
    let mut seen = HashSet::from([line_key(keys)]);
    for _ in 0..LINE_DEPTH {
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..len {
                for half in 1..=(len - start) / 2 {
                    let mut child = *state;
                    for offset in 0..half {
                        child.keys.swap(start + offset, start + half + offset);
                    }
                    if !seen.insert(line_key(&child.keys[..len])) {
                        continue;
                    }
                    child.moves[child.move_len as usize] = start as u16 | ((half as u16) << 5);
                    child.move_len += 1;
                    child.cost = line_cost(&child.keys[..len]);
                    if child.cost < best.cost {
                        best = child;
                    }
                    next.push(child);
                }
            }
        }
        next.sort_unstable_by_key(|state| state.cost);
        next.truncate(LINE_BEAM);
        if next.is_empty() || best.cost == 0 {
            break;
        }
        beam = next;
    }
    best.moves[..best.move_len as usize]
        .iter()
        .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
        .collect()
}

fn line_operation(cells: &[usize], start: usize, half: usize, n: usize) -> Operation {
    let first = cells[0];
    if cells.len() <= 1 || cells[1] == first + 1 {
        Operation {
            direction: b'H',
            r: first / n,
            c: first % n + start,
            h: 1,
            w: 2 * half,
        }
    } else {
        Operation {
            direction: b'V',
            r: first / n + start,
            c: first % n,
            h: 2 * half,
            w: 1,
        }
    }
}

fn route_segment(
    cells: &[usize],
    desired: &[usize],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    output: &mut Vec<Operation>,
) {
    let len = cells.len();
    if len < 2 {
        return;
    }
    let horizontal = cells[1] == cells[0] + 1;
    let base = if horizontal {
        cells[0] % n
    } else {
        cells[0] / n
    };
    let mut keys = vec![WILDCARD; len];
    let mut wanted = vec![usize::MAX; len];
    for (i, &cell) in cells.iter().enumerate() {
        let card = board[cell];
        let target = desired[card];
        if target != usize::MAX && target >= base && target < base + len {
            let offset = target - base;
            if wanted[offset] == usize::MAX {
                wanted[offset] = card;
                keys[i] = offset as u8;
            }
        }
    }

    for (start, half) in solve_line(&keys) {
        let op = line_operation(cells, start, half, n);
        apply(op, board, position, n);
        output.push(op);
    }

    // The beam is an accelerator, not a correctness dependency.  Only now give
    // the wildcard cards the still-free slots, in their current stable order,
    // and finish the resulting permutation with adjacent swaps.
    let mut completion_target = vec![usize::MAX; board.len()];
    for (target, &card) in wanted.iter().enumerate() {
        if card != usize::MAX {
            completion_target[card] = target;
        }
    }
    let remaining: Vec<usize> = wanted
        .iter()
        .enumerate()
        .filter_map(|(target, &card)| (card == usize::MAX).then_some(target))
        .collect();
    let mut next_remaining = 0;
    for &cell in cells {
        let card = board[cell];
        if completion_target[card] == usize::MAX {
            completion_target[card] = remaining[next_remaining];
            next_remaining += 1;
        }
    }
    for target in 0..len {
        let mut at = target;
        while completion_target[board[cells[at]]] != target {
            at += 1;
        }
        while at > target {
            let op = line_operation(cells, at - 1, 1, n);
            apply(op, board, position, n);
            output.push(op);
            at -= 1;
        }
    }
}

fn route_segments(
    segments: &[Vec<usize>],
    desired: &[usize],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    output: &mut Vec<Operation>,
) {
    let mut order: Vec<usize> = (0..segments.len()).collect();
    order.sort_unstable_by_key(|&i| std::cmp::Reverse(segments[i].len()));
    for index in order {
        route_segment(&segments[index], desired, board, position, n, output);
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

fn all_tree_distances(tree: &[Vec<usize>]) -> Vec<u16> {
    let size = tree.len();
    let mut distance = vec![u16::MAX; size * size];
    for source in 0..size {
        let mut queue = VecDeque::from([source]);
        distance[source * size + source] = 0;
        while let Some(cell) = queue.pop_front() {
            let next = distance[source * size + cell] + 1;
            for &to in &tree[cell] {
                if distance[source * size + to] == u16::MAX {
                    distance[source * size + to] = next;
                    queue.push_back(to);
                }
            }
        }
    }
    distance
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
        while let Some(cell) = queue.pop_front() {
            for &direction in order {
                let Some(to) = neighbor(cell, direction, n, vertical, horizontal) else {
                    continue;
                };
                if parent[to] != usize::MAX {
                    continue;
                }
                parent[to] = cell;
                depth[to] = depth[cell] + 1;
                add_edge(&mut tree, cell, to);
                queue.push_back(to);
            }
        }
        assert!(parent.iter().all(|&p| p != usize::MAX));
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

    fn complete(&self, initial: &[usize], n: usize, reverse_tie: bool) -> Vec<Operation> {
        self.complete_impl(initial, n, reverse_tie, None, None)
    }

    fn complete_jump(
        &self,
        initial: &[usize],
        n: usize,
        reverse_tie: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
        self.complete_impl(initial, n, reverse_tie, Some(vertical), Some(horizontal))
    }

    fn complete_impl(
        &self,
        initial: &[usize],
        n: usize,
        reverse_tie: bool,
        vertical: Option<&[Vec<u8>]>,
        horizontal: Option<&[Vec<u8>]>,
    ) -> Vec<Operation> {
        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut output = Vec::new();
        for _ in 1..size {
            let mut leaf = usize::MAX;
            let mut best_distance = u16::MAX;
            for candidate in 0..size {
                if !active[candidate] || degree[candidate] != 1 {
                    continue;
                }
                let distance = self.distance[position[candidate] * size + candidate];
                let tie = distance == best_distance
                    && (leaf == usize::MAX
                        || (reverse_tie && candidate > leaf)
                        || (!reverse_tie && candidate < leaf));
                if distance < best_distance || tie {
                    best_distance = distance;
                    leaf = candidate;
                }
            }
            assert_ne!(leaf, usize::MAX);
            let path = self.path(position[leaf], leaf);
            let mut at = 0;
            while at + 1 < path.len() {
                let direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1;
                if vertical.is_some() {
                    while straight < 3 && at + straight + 1 < path.len() {
                        if direction_between(path[at + straight], path[at + straight + 1], n)
                            != direction
                        {
                            break;
                        }
                        straight += 1;
                    }
                }
                let mut selected = None;
                for jump in (1..=straight).rev() {
                    let Some(op) = jump_operation(path[at], direction, jump, n) else {
                        continue;
                    };
                    let walls_open = vertical.is_none()
                        || rectangle_open(op, vertical.unwrap(), horizontal.unwrap());
                    if jump_window_active(op, &active, n) && walls_open {
                        selected = Some((jump, op));
                        break;
                    }
                }
                let (jump, op) = selected.expect("an adjacent tree edge is always legal");
                apply(op, &mut board, &mut position, n);
                debug_assert_eq!(position[leaf], path[at + jump]);
                output.push(op);
                at += jump;
            }
            debug_assert_eq!(board[leaf], leaf);
            active[leaf] = false;
            degree[leaf] = 0;
            for &to in &self.tree[leaf] {
                if active[to] {
                    degree[to] -= 1;
                }
            }
        }
        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        output
    }
}

fn direction_between(a: usize, b: usize, n: usize) -> (isize, isize) {
    let (ar, ac) = ((a / n) as isize, (a % n) as isize);
    let (br, bc) = ((b / n) as isize, (b % n) as isize);
    (br - ar, bc - ac)
}

fn jump_operation(
    start: usize,
    direction: (isize, isize),
    jump: usize,
    n: usize,
) -> Option<Operation> {
    let (r, c) = (start / n, start % n);
    match direction {
        (0, 1) if c + 2 * jump <= n => Some(Operation {
            direction: b'H',
            r,
            c,
            h: 1,
            w: 2 * jump,
        }),
        (0, -1) if c >= jump && c + jump <= n => Some(Operation {
            direction: b'H',
            r,
            c: c - jump,
            h: 1,
            w: 2 * jump,
        }),
        (1, 0) if r + 2 * jump <= n => Some(Operation {
            direction: b'V',
            r,
            c,
            h: 2 * jump,
            w: 1,
        }),
        (-1, 0) if r >= jump && r + jump <= n => Some(Operation {
            direction: b'V',
            r: r - jump,
            c,
            h: 2 * jump,
            w: 1,
        }),
        _ => None,
    }
}

fn jump_window_active(op: Operation, active: &[bool], n: usize) -> bool {
    (op.r..op.r + op.h).all(|r| (op.c..op.c + op.w).all(|c| active[r * n + c]))
}

fn compress_adjacent(
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
            let mut selected: Vec<Operation> = batch
                .iter()
                .copied()
                .filter(|op| op.direction == direction)
                .collect();
            if direction == b'H' {
                selected.sort_unstable_by_key(|op| (op.c, op.r));
            } else {
                selected.sort_unstable_by_key(|op| (op.r, op.c));
            }
            let mut at = 0;
            while at < selected.len() {
                let first = selected[at];
                let mut end = at + 1;
                while end < selected.len() {
                    let previous = selected[end - 1];
                    let next = selected[end];
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
                output.push(if direction == b'H' {
                    Operation {
                        direction,
                        r: first.r,
                        c: first.c,
                        h: end - at,
                        w: 2,
                    }
                } else {
                    Operation {
                        direction,
                        r: first.r,
                        c: first.c,
                        h: 2,
                        w: end - at,
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
        if op.h * op.w > 2 {
            flush(&mut batch, &mut output, vertical, horizontal);
            occupied.fill(false);
            output.push(op);
            continue;
        }
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

fn choose_completion(
    plan: &TreePlan,
    board: &[usize],
    n: usize,
    reverse_tie: bool,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    let raw = plan.complete(board, n, reverse_tie);
    let compressed_exact = compress_adjacent(&raw, n, vertical, horizontal);
    let exact = if replay_sorted(board, &compressed_exact, n, vertical, horizontal) {
        compressed_exact
    } else {
        raw
    };
    let jump_raw = plan.complete_jump(board, n, reverse_tie, vertical, horizontal);
    let jump = compress_adjacent(&jump_raw, n, vertical, horizontal);
    if jump.len() < exact.len() && replay_sorted(board, &jump, n, vertical, horizontal) {
        jump
    } else {
        exact
    }
}

#[derive(Clone)]
struct Checkpoint {
    board: Vec<usize>,
    prefix: Vec<Operation>,
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

    let (horizontal_segments, horizontal_id) = horizontal_segments(n, &vertical);
    let (vertical_segments, vertical_id) = vertical_segments(n, &horizontal);
    let middle = constrained_middle_rows(&initial, n, &horizontal_id, &vertical_id);
    let target_column: Vec<usize> = (0..size)
        .map(|card| {
            (middle[card] != usize::MAX)
                .then_some(card % n)
                .unwrap_or(usize::MAX)
        })
        .collect();
    let target_row: Vec<usize> = (0..size)
        .map(|card| {
            (middle[card] != usize::MAX)
                .then_some(card / n)
                .unwrap_or(usize::MAX)
        })
        .collect();

    let mut board = initial.clone();
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut prefix = Vec::new();
    let mut checkpoints = vec![Checkpoint {
        board: board.clone(),
        prefix: Vec::new(),
    }];
    let stages: [(&[Vec<usize>], &[usize]); 3] = [
        (&vertical_segments, &middle),
        (&horizontal_segments, &target_column),
        (&vertical_segments, &target_row),
    ];
    for (segments, desired) in stages {
        route_segments(segments, desired, &mut board, &mut position, n, &mut prefix);
        checkpoints.push(Checkpoint {
            board: board.clone(),
            prefix: prefix.clone(),
        });
    }

    const ORDERS: [[usize; 4]; 4] = [[0, 1, 2, 3], [1, 2, 3, 0], [0, 3, 2, 1], [3, 2, 1, 0]];
    let roots = [(n / 2) * n + n / 2, 0, n - 1, (n - 1) * n, size - 1];
    let mut best: Option<Vec<Operation>> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            for checkpoint in &checkpoints {
                let completion = choose_completion(
                    &plan,
                    &checkpoint.board,
                    n,
                    (root_index + order_index) & 1 != 0,
                    &vertical,
                    &horizontal,
                );
                let total = checkpoint.prefix.len() + completion.len();
                if total > 100_000 || best.as_ref().is_some_and(|answer| answer.len() <= total) {
                    continue;
                }
                let mut candidate = checkpoint.prefix.clone();
                candidate.extend(completion);
                if replay_sorted(&initial, &candidate, n, &vertical, &horizontal) {
                    best = Some(candidate);
                }
            }
        }
    }
    let answer = best.expect("the initial exact-tree checkpoint is always safe");
    assert!(answer.len() <= 100_000);
    assert!(replay_sorted(&initial, &answer, n, &vertical, &horizontal));
    let mut output = String::new();
    for op in answer {
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
