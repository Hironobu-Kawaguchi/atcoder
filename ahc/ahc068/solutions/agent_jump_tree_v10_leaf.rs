use std::collections::VecDeque;
use std::fmt::Write as _;
use std::io::{self, Read};
use std::time::Instant;

const SEARCH_SECONDS: f64 = 1.02;
const SEARCH_MOVE_LIMIT: usize = 20_000;
const CHECK_INTERVAL: usize = 20;
const CHECKPOINT_LIMIT: usize = 5;

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

/// Long thin rectangles perform block routing; small two-dimensional
/// rectangles provide local cleanup. Both families are deterministic.
fn macro_candidates(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Operation> {
    let mut result = Vec::new();
    for h in 1..=n {
        for w in 1..=n {
            if h * w == 1 {
                continue;
            }
            let local = h <= 8 && w <= 8;
            let allow_v = h % 2 == 0 && (w <= 4 || local);
            let allow_h = w % 2 == 0 && (h <= 4 || local);
            if !allow_v && !allow_h {
                continue;
            }
            for r in 0..=n - h {
                for c in 0..=n - w {
                    if !rectangle_open(r, c, h, w, vertical, horizontal) {
                        continue;
                    }
                    if allow_v {
                        result.push(Operation {
                            direction: b'V',
                            r,
                            c,
                            h,
                            w,
                        });
                    }
                    if allow_h {
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

fn delta(op: Operation, board: &[usize], distances: &[u16], n: usize) -> i32 {
    let size = board.len();
    let mut result = 0i32;
    let mut add_pair = |a: usize, b: usize| {
        let x = board[a];
        let y = board[b];
        result += i32::from(distances[x * size + b]) + i32::from(distances[y * size + a])
            - i32::from(distances[x * size + a])
            - i32::from(distances[y * size + b]);
    };
    if op.direction == b'V' {
        for i in 0..op.h / 2 {
            for j in 0..op.w {
                add_pair(
                    (op.r + i) * n + op.c + j,
                    (op.r + op.h / 2 + i) * n + op.c + j,
                );
            }
        }
    } else {
        for i in 0..op.h {
            for j in 0..op.w / 2 {
                add_pair(
                    (op.r + i) * n + op.c + j,
                    (op.r + i) * n + op.c + op.w / 2 + j,
                );
            }
        }
    }
    result
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

#[derive(Clone, Copy)]
enum JumpPolicy {
    /// The exact V8 rule: try k=3,2,1 and keep the card at offset zero.
    V8Edge,
    /// Prefer the least harmful window among all offsets of the longest jump.
    Distance,
    /// Choose the leaf by estimated jump count, then score every (k, offset)
    /// window by the total tree-distance potential change of all moved cards.
    JumpAware,
}

impl JumpPolicy {
    fn max_jump(self) -> usize {
        match self {
            Self::V8Edge => 3,
            Self::Distance | Self::JumpAware => 10,
        }
    }
}

/// O(1) active, wall-free line-segment queries used by the jump-aware leaf
/// estimator. `n <= 20`, so the changing active set of each row/column fits in
/// one `u64`; removing a fixed leaf only clears two bits.
struct ActiveCorridors {
    n: usize,
    row_left: Vec<usize>,
    row_right: Vec<usize>,
    col_top: Vec<usize>,
    col_bottom: Vec<usize>,
    row_active: Vec<u64>,
    col_active: Vec<u64>,
}

impl ActiveCorridors {
    fn new(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Self {
        assert!(n < 64);
        let size = n * n;
        let mut row_left = vec![0usize; size];
        let mut row_right = vec![0usize; size];
        for r in 0..n {
            let mut left = 0;
            for c in 0..n {
                if c + 1 == n || vertical[r][c] == b'1' {
                    for x in left..=c {
                        row_left[r * n + x] = left;
                        row_right[r * n + x] = c;
                    }
                    left = c + 1;
                }
            }
        }
        let mut col_top = vec![0usize; size];
        let mut col_bottom = vec![0usize; size];
        for c in 0..n {
            let mut top = 0;
            for r in 0..n {
                if r + 1 == n || horizontal[r][c] == b'1' {
                    for x in top..=r {
                        col_top[x * n + c] = top;
                        col_bottom[x * n + c] = r;
                    }
                    top = r + 1;
                }
            }
        }
        let active = (1u64 << n) - 1;
        Self {
            n,
            row_left,
            row_right,
            col_top,
            col_bottom,
            row_active: vec![active; n],
            col_active: vec![active; n],
        }
    }

    fn range_mask(left: usize, right: usize) -> u64 {
        ((1u64 << (right + 1)) - 1) & !((1u64 << left) - 1)
    }

    /// Returns the active subsegment containing `cell`. Static walls provide
    /// the outer bounds; already-fixed cells are dynamic separators.
    fn bounds(&self, cell: usize, direction: (isize, isize)) -> (usize, usize) {
        let (r, c) = (cell / self.n, cell % self.n);
        let (mut left, mut right, coordinate, active_mask) = if direction.0 == 0 {
            (
                self.row_left[cell],
                self.row_right[cell],
                c,
                self.row_active[r],
            )
        } else {
            (
                self.col_top[cell],
                self.col_bottom[cell],
                r,
                self.col_active[c],
            )
        };
        let inactive = !active_mask & Self::range_mask(left, right);
        let before = inactive & ((1u64 << coordinate) - 1);
        if before != 0 {
            left = (u64::BITS - 1 - before.leading_zeros()) as usize + 1;
        }
        let through_coordinate = (1u64 << (coordinate + 1)) - 1;
        let after = inactive & !through_coordinate;
        if after != 0 {
            right = after.trailing_zeros() as usize - 1;
        }
        debug_assert!(left <= coordinate && coordinate <= right);
        (left, right)
    }

    fn offset_range(
        &self,
        cell: usize,
        direction: (isize, isize),
        jump: usize,
    ) -> Option<(usize, usize)> {
        let coordinate = if direction.0 == 0 {
            cell % self.n
        } else {
            cell / self.n
        };
        let (left, right) = self.bounds(cell, direction);
        let (minimum_offset, maximum_offset) = if direction.0 > 0 || direction.1 > 0 {
            (
                (coordinate + 2 * jump).saturating_sub(right + 1),
                (jump - 1).min(coordinate - left),
            )
        } else {
            if coordinate < left + jump {
                return None;
            }
            (
                (coordinate + jump).saturating_sub(right + 1),
                (jump - 1).min(coordinate - jump - left),
            )
        };
        (minimum_offset <= maximum_offset).then_some((minimum_offset, maximum_offset))
    }

    fn can_jump(&self, cell: usize, direction: (isize, isize), jump: usize) -> bool {
        self.offset_range(cell, direction, jump).is_some()
    }

    fn span(&self, cell: usize, direction: (isize, isize)) -> usize {
        let (left, right) = self.bounds(cell, direction);
        right - left + 1
    }

    fn remove(&mut self, cell: usize) {
        let (r, c) = (cell / self.n, cell % self.n);
        self.row_active[r] &= !(1u64 << c);
        self.col_active[c] &= !(1u64 << r);
    }
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

    fn estimated_jump_operations(path: &[usize], n: usize, corridors: &ActiveCorridors) -> usize {
        if path.len() <= 1 {
            return 0;
        }
        debug_assert!(path.len() <= 400);
        let mut dp = [u16::MAX; 400];
        dp[path.len() - 1] = 0;
        for at in (0..path.len() - 1).rev() {
            let direction = direction_between(path[at], path[at + 1], n);
            let mut straight = 1;
            while straight < 10 && at + straight + 1 < path.len() {
                if direction_between(path[at + straight], path[at + straight + 1], n) != direction {
                    break;
                }
                straight += 1;
            }
            for jump in 1..=straight {
                if corridors.can_jump(path[at], direction, jump) {
                    dp[at] = dp[at].min(1 + dp[at + jump]);
                }
            }
            debug_assert_ne!(dp[at], u16::MAX);
        }
        usize::from(dp[0])
    }

    /// Restricts the expensive path estimate to the eight leaves preferred by
    /// the old unit-distance rule. The primary key is the exact minimum count
    /// in a small path DP using all feasible k<=10 jumps. Only ties evaluate
    /// the full-card potential of the first operation; corridor span rewards
    /// leaves whose later offset choices are less constrained.
    #[allow(clippy::too_many_arguments)]
    fn select_jump_aware_leaf(
        &self,
        board: &[usize],
        position: &[usize],
        active: &[bool],
        degree: &[usize],
        corridors: &ActiveCorridors,
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> usize {
        const SHORTLIST: usize = 8;
        let size = board.len();
        let mut shortlist: Vec<(u16, usize)> = (0..size)
            .filter(|&candidate| active[candidate] && degree[candidate] == 1)
            .map(|candidate| {
                (
                    self.distance[position[candidate] * size + candidate],
                    candidate,
                )
            })
            .collect();
        shortlist.sort_unstable_by(|&(da, a), &(db, b)| {
            da.cmp(&db)
                .then_with(|| if prefer_larger { b.cmp(&a) } else { a.cmp(&b) })
        });
        shortlist.truncate(SHORTLIST);
        assert!(!shortlist.is_empty());

        let mut measured = Vec::with_capacity(shortlist.len());
        let mut best_operations = usize::MAX;
        for &(distance, candidate) in &shortlist {
            let path = self.path(position[candidate], candidate);
            debug_assert!(path.iter().all(|&v| active[v]));
            let operations = Self::estimated_jump_operations(&path, n, corridors);
            best_operations = best_operations.min(operations);
            measured.push((candidate, distance, operations, path));
        }

        let mut best: Option<((usize, i32, usize, u16, usize), usize)> = None;
        for (candidate, distance, operations, path) in measured {
            if operations != best_operations {
                continue;
            }
            let (potential, span) = if path.len() <= 1 {
                (0, usize::MAX)
            } else {
                let direction = direction_between(path[0], path[1], n);
                let mut straight = 1;
                while straight < 10 && straight + 1 < path.len() {
                    if direction_between(path[straight], path[straight + 1], n) != direction {
                        break;
                    }
                    straight += 1;
                }
                let mut potential = i32::MAX;
                for jump in 1..=straight {
                    let Some((minimum_offset, maximum_offset)) =
                        corridors.offset_range(path[0], direction, jump)
                    else {
                        continue;
                    };
                    for offset in minimum_offset..=maximum_offset {
                        let Some(op) =
                            jump_operation_with_offset(path[0], direction, jump, offset, n)
                        else {
                            continue;
                        };
                        debug_assert!(jump_window_active(op, active, n));
                        debug_assert!(rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal));
                        potential = potential.min(delta(op, board, &self.distance, n));
                    }
                }
                debug_assert_ne!(potential, i32::MAX);
                (potential, corridors.span(path[0], direction))
            };
            let stable_id = if prefer_larger {
                usize::MAX - candidate
            } else {
                candidate
            };
            let key = (
                operations,
                potential,
                usize::MAX - span,
                distance,
                stable_id,
            );
            if best.as_ref().is_none_or(|(best_key, _)| key < *best_key) {
                best = Some((key, candidate));
            }
        }
        best.unwrap().1
    }

    fn complete_jump(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        policy: JumpPolicy,
    ) -> Vec<Operation> {
        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0usize; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut corridors = matches!(policy, JumpPolicy::JumpAware)
            .then(|| ActiveCorridors::new(n, vertical, horizontal));
        let mut degree: Vec<usize> = self.tree.iter().map(Vec::len).collect();
        let mut remaining = size;
        let mut operations = Vec::new();
        while remaining > 1 {
            let leaf = if matches!(policy, JumpPolicy::JumpAware) {
                self.select_jump_aware_leaf(
                    &board,
                    &position,
                    &active,
                    &degree,
                    corridors.as_ref().unwrap(),
                    n,
                    prefer_larger,
                    vertical,
                    horizontal,
                )
            } else {
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
                leaf
            };
            assert_ne!(leaf, usize::MAX);
            let path = self.path(position[leaf], leaf);
            debug_assert!(path.iter().all(|&v| active[v]));
            let mut at = 0;
            while at + 1 < path.len() {
                let first_direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1;
                while straight < policy.max_jump() && at + straight + 1 < path.len() {
                    if direction_between(path[at + straight], path[at + straight + 1], n)
                        != first_direction
                    {
                        break;
                    }
                    straight += 1;
                }

                let mut selected = None;
                for jump in (1..=straight).rev() {
                    let (minimum_offset, maximum_offset) = match policy {
                        JumpPolicy::V8Edge => (0, 0),
                        JumpPolicy::Distance => (0, jump - 1),
                        JumpPolicy::JumpAware => {
                            let Some(range) = corridors.as_ref().unwrap().offset_range(
                                path[at],
                                first_direction,
                                jump,
                            ) else {
                                continue;
                            };
                            range
                        }
                    };
                    let mut best_window = None;
                    for offset in minimum_offset..=maximum_offset {
                        let Some(op) =
                            jump_operation_with_offset(path[at], first_direction, jump, offset, n)
                        else {
                            continue;
                        };
                        if matches!(policy, JumpPolicy::JumpAware) {
                            debug_assert!(jump_window_active(op, &active, n));
                            debug_assert!(rectangle_open(
                                op.r, op.c, op.h, op.w, vertical, horizontal
                            ));
                        } else if !jump_window_active(op, &active, n)
                            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                        {
                            continue;
                        }
                        let key = jump_window_key(
                            policy,
                            op,
                            offset,
                            jump,
                            &board,
                            &self.distance,
                            &active,
                            n,
                            vertical,
                            horizontal,
                        );
                        if best_window
                            .as_ref()
                            .is_none_or(|(best_key, _)| key < *best_key)
                        {
                            best_window = Some((key, op));
                        }
                    }
                    if let Some((key, op)) = best_window {
                        if matches!(policy, JumpPolicy::JumpAware) {
                            if selected
                                .as_ref()
                                .is_none_or(|(best_key, _, _)| key < *best_key)
                            {
                                selected = Some((key, jump, op));
                            }
                        } else {
                            selected = Some((key, jump, op));
                            break;
                        }
                    }
                }
                let (_, jump, op) = selected.expect("the adjacent tree edge is a legal jump");
                debug_assert_eq!(board[path[at]], leaf);
                apply(op, &mut board, &mut position, n);
                assert_eq!(
                    position[leaf],
                    path[at + jump],
                    "jump must land the desired card on its tree path"
                );
                operations.push(op);
                at += jump;
            }
            assert_eq!(board[leaf], leaf);
            active[leaf] = false;
            if let Some(corridors) = &mut corridors {
                corridors.remove(leaf);
            }
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

fn direction_between(a: usize, b: usize, n: usize) -> (isize, isize) {
    let (ar, ac) = ((a / n) as isize, (a % n) as isize);
    let (br, bc) = ((b / n) as isize, (b % n) as isize);
    (br - ar, bc - ac)
}

fn jump_operation_with_offset(
    start: usize,
    direction: (isize, isize),
    jump: usize,
    offset: usize,
    n: usize,
) -> Option<Operation> {
    if jump == 0 || offset >= jump {
        return None;
    }
    let (r, c) = (start / n, start % n);
    let op = match direction {
        (0, 1) if c >= offset && c - offset + 2 * jump <= n => Operation {
            direction: b'H',
            r,
            c: c - offset,
            h: 1,
            w: 2 * jump,
        },
        (0, -1) if c >= jump + offset && c + jump - offset <= n => Operation {
            direction: b'H',
            r,
            c: c - jump - offset,
            h: 1,
            w: 2 * jump,
        },
        (1, 0) if r >= offset && r - offset + 2 * jump <= n => Operation {
            direction: b'V',
            r: r - offset,
            c,
            h: 2 * jump,
            w: 1,
        },
        (-1, 0) if r >= jump + offset && r + jump - offset <= n => Operation {
            direction: b'V',
            r: r - jump - offset,
            c,
            h: 2 * jump,
            w: 1,
        },
        _ => return None,
    };
    Some(op)
}

fn jump_window_key(
    policy: JumpPolicy,
    op: Operation,
    offset: usize,
    jump: usize,
    board: &[usize],
    tree_distances: &[u16],
    active: &[bool],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> (i32, i32, i32, i32, usize) {
    if matches!(policy, JumpPolicy::V8Edge) {
        return (0, 0, 0, 0, offset);
    }
    let distance_delta = delta(op, board, tree_distances, n);
    let (balanced_clearance, total_clearance) =
        jump_window_clearance(op, active, n, vertical, horizontal);
    let center_penalty = ((2 * offset + 1) as isize - jump as isize).unsigned_abs() as i32;
    match policy {
        JumpPolicy::V8Edge => unreachable!(),
        JumpPolicy::Distance => (
            distance_delta,
            -(balanced_clearance as i32),
            -(total_clearance as i32),
            center_penalty,
            offset,
        ),
        JumpPolicy::JumpAware => (
            distance_delta,
            -(jump as i32),
            -(balanced_clearance as i32),
            -(total_clearance as i32),
            offset,
        ),
    }
}

/// Counts active, open cells immediately before and after a legal line window.
/// The first component rewards balanced room on both sides; the second breaks
/// ties in favor of the longer containing corridor.
fn jump_window_clearance(
    op: Operation,
    active: &[bool],
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> (usize, usize) {
    let (mut before, mut after) = (0usize, 0usize);
    if op.direction == b'H' {
        debug_assert_eq!(op.h, 1);
        let mut c = op.c;
        while c > 0 && active[op.r * n + c - 1] && vertical[op.r][c - 1] == b'0' {
            before += 1;
            c -= 1;
        }
        let mut c = op.c + op.w;
        while c < n && active[op.r * n + c] && vertical[op.r][c - 1] == b'0' {
            after += 1;
            c += 1;
        }
    } else {
        debug_assert_eq!(op.w, 1);
        let mut r = op.r;
        while r > 0 && active[(r - 1) * n + op.c] && horizontal[r - 1][op.c] == b'0' {
            before += 1;
            r -= 1;
        }
        let mut r = op.r + op.h;
        while r < n && active[r * n + op.c] && horizontal[r - 1][op.c] == b'0' {
            after += 1;
            r += 1;
        }
    }
    (before.min(after), before + after)
}

fn jump_window_active(op: Operation, active: &[bool], n: usize) -> bool {
    (op.r..op.r + op.h).all(|r| (op.c..op.c + op.w).all(|c| active[r * n + c]))
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
        if op.h * op.w > 2 {
            flush(&mut batch, &mut output, vertical, horizontal);
            occupied.fill(false);
            output.push(op);
            continue;
        }
        debug_assert_eq!(op.h * op.w, 2);
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
    let mut position = vec![0usize; board.len()];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    for &op in operations {
        if op.r + op.h > n
            || op.c + op.w > n
            || op.h == 0
            || op.w == 0
            || (op.direction == b'H' && op.w % 2 != 0)
            || (op.direction == b'V' && op.h % 2 != 0)
            || (op.direction != b'H' && op.direction != b'V')
            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
        {
            return false;
        }
        apply(op, &mut board, &mut position, n);
    }
    board.iter().enumerate().all(|(cell, &card)| cell == card)
}

fn choose_completion(
    plan: &TreePlan,
    checkpoint: &[usize],
    n: usize,
    prefer_larger: bool,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    let old_raw = plan.complete(checkpoint, n, prefer_larger);
    let old = compress_fallback(&old_raw, n, vertical, horizontal);
    assert!(replay_sorted(checkpoint, &old, n, vertical, horizontal));

    let v8_raw = plan.complete_jump(
        checkpoint,
        n,
        prefer_larger,
        vertical,
        horizontal,
        JumpPolicy::V8Edge,
    );
    let v8 = compress_fallback(&v8_raw, n, vertical, horizontal);
    assert!(replay_sorted(checkpoint, &v8, n, vertical, horizontal));

    let mut best = if v8.len() < old.len() { v8 } else { old };
    for policy in [JumpPolicy::Distance, JumpPolicy::JumpAware] {
        let long_raw =
            plan.complete_jump(checkpoint, n, prefer_larger, vertical, horizontal, policy);
        let long = compress_fallback(&long_raw, n, vertical, horizontal);
        if replay_sorted(checkpoint, &long, n, vertical, horizontal) && long.len() < best.len() {
            best = long;
        }
    }
    best
}

#[derive(Clone)]
struct Checkpoint {
    estimate: usize,
    board: Vec<usize>,
    prefix: Vec<Operation>,
}

fn save_checkpoint(
    saved: &mut Vec<Checkpoint>,
    board: &[usize],
    prefix: &[Operation],
    quick_plan: &TreePlan,
    n: usize,
) {
    if saved.iter().any(|state| state.prefix.len() == prefix.len()) {
        return;
    }
    let checkpoint = Checkpoint {
        estimate: prefix.len() + quick_plan.complete(board, n, false).len(),
        board: board.to_vec(),
        prefix: prefix.to_vec(),
    };
    if saved.len() < CHECKPOINT_LIMIT {
        saved.push(checkpoint);
    } else {
        let (worst, worst_value) = saved
            .iter()
            .enumerate()
            .max_by_key(|(_, state)| state.estimate)
            .map(|(i, state)| (i, state.estimate))
            .unwrap();
        if checkpoint.estimate < worst_value {
            saved[worst] = checkpoint;
        }
    }
}

fn solve(input: &str) -> String {
    let mut scanner = Scanner(input.split_whitespace());
    let n: usize = scanner.next();
    let size = n * n;
    let mut board: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
    let initial = board.clone();
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
    let mesh_candidate = fully_open.then(|| mesh_route(&board, n));
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
    let candidates = macro_candidates(n, &vertical, &horizontal);
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

    let start = Instant::now();
    while prefix.len() < SEARCH_MOVE_LIMIT && start.elapsed().as_secs_f64() < SEARCH_SECONDS {
        let mut best_delta = 0i32;
        let mut best = None;
        for &op in &candidates {
            let value = delta(op, &board, &distances, n);
            if value < best_delta {
                best_delta = value;
                best = Some(op);
            }
        }
        let Some(op) = best else { break };
        apply(op, &mut board, &mut position, n);
        prefix.push(op);
        if prefix.len() % CHECK_INTERVAL == 0 || best_delta <= -12 {
            save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);
        }
    }
    save_checkpoint(&mut checkpoints, &board, &prefix, &quick_plan, n);

    let roots = [
        center,
        0,
        n - 1,
        (n - 1) * n,
        n * n - 1,
        n / 2,
        (n - 1) * n + n / 2,
        (n / 2) * n,
        (n / 2) * n + n - 1,
    ];
    let mut best_result: Option<(Vec<Operation>, Vec<Operation>)> = None;
    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            for checkpoint in &checkpoints {
                let fallback = choose_completion(
                    &plan,
                    &checkpoint.board,
                    n,
                    (root_index + order_index) % 2 == 1,
                    &vertical,
                    &horizontal,
                );
                let total = checkpoint.prefix.len() + fallback.len();
                if total > 100_000 {
                    continue;
                }
                let improves = match &best_result {
                    None => true,
                    Some((p, f)) => total < p.len() + f.len(),
                };
                if improves {
                    best_result = Some((checkpoint.prefix.clone(), fallback));
                }
            }
        }
    }
    let (mut result, fallback) = best_result.expect("a safe exact candidate exists");
    result.extend(fallback);
    if let Some(mesh) = mesh_candidate {
        if mesh.len() < result.len() && replay_sorted(&initial, &mesh, n, &vertical, &horizontal) {
            result = mesh;
        }
    }
    assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
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
