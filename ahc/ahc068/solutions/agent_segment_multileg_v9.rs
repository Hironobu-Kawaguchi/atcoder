use std::collections::{HashSet, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};

const WILDCARD: u8 = 31;
const LINE_BEAM: usize = 144;
const LINE_DEPTH: usize = 14;
const LINE_WORK_LIMIT: usize = 12_000_000;
const MATCHING_VARIANTS: usize = 16;
const JUMP_LIMIT: usize = 3;

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
    let mut exchange = |a: usize, b: usize| {
        board.swap(a, b);
        position[board[a]] = a;
        position[board[b]] = b;
    };
    if op.direction == b'H' {
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

fn add_edge(graph: &mut [Vec<usize>], a: usize, b: usize) {
    graph[a].push(b);
    graph[b].push(a);
}

fn build_graph(n: usize, vertical: &[Vec<u8>], horizontal: &[Vec<u8>]) -> Vec<Vec<usize>> {
    let mut graph = vec![Vec::new(); n * n];
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
    graph
}

fn horizontal_segments(n: usize, vertical: &[Vec<u8>]) -> (Vec<Vec<usize>>, Vec<usize>) {
    let mut segments = Vec::new();
    let mut id = vec![usize::MAX; n * n];
    for r in 0..n {
        let mut start = 0;
        for c in 0..n {
            if c + 1 == n || vertical[r][c] == b'1' {
                let index = segments.len();
                let cells: Vec<_> = (start..=c).map(|x| r * n + x).collect();
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
                let cells: Vec<_> = (start..=r).map(|x| x * n + c).collect();
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

#[derive(Clone, Copy)]
enum RoutingOrder {
    ColumnRowColumn,
    RowColumnRow,
}

fn three_leg_feasible(
    card: usize,
    current: usize,
    middle: usize,
    order: RoutingOrder,
    n: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    protected: &[bool],
) -> bool {
    let target = card;
    match order {
        RoutingOrder::ColumnRowColumn => {
            let source_column = current % n;
            let target_column = target % n;
            let first = middle * n + source_column;
            let second = middle * n + target_column;
            !protected[first]
                && !protected[second]
                && vertical_id[current] == vertical_id[first]
                && horizontal_id[first] == horizontal_id[second]
                && vertical_id[second] == vertical_id[target]
        }
        RoutingOrder::RowColumnRow => {
            let source_row = current / n;
            let target_row = target / n;
            let first = source_row * n + middle;
            let second = target_row * n + middle;
            !protected[first]
                && !protected[second]
                && horizontal_id[current] == horizontal_id[first]
                && vertical_id[first] == vertical_id[second]
                && horizontal_id[second] == horizontal_id[target]
        }
    }
}

fn augment_layer(
    source: usize,
    candidates: &[Vec<(usize, usize)>],
    seen_target: &mut [bool],
    matched_source: &mut [usize],
    chosen_card: &mut [usize],
) -> bool {
    for &(target, card) in &candidates[source] {
        if seen_target[target] {
            continue;
        }
        seen_target[target] = true;
        let previous = matched_source[target];
        if previous == usize::MAX
            || augment_layer(
                previous,
                candidates,
                seen_target,
                matched_source,
                chosen_card,
            )
        {
            matched_source[target] = source;
            chosen_card[source] = card;
            return true;
        }
    }
    false
}

fn one_assignment(
    board: &[usize],
    n: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    protected: &[bool],
    order: RoutingOrder,
    variant: usize,
) -> Vec<Option<usize>> {
    let size = board.len();
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut used = vec![false; size];
    let mut assignment = vec![None; size];
    let strides = [1usize, 3, 7, 9, 11, 13, 17, 19];
    let stride = strides[variant % strides.len()];
    for layer_index in 0..n {
        let mut middle = (layer_index * stride + variant * 7) % n;
        if variant & 1 == 1 {
            middle = n - 1 - middle;
        }
        let mut candidates = vec![Vec::new(); n];
        for card in 0..size {
            if used[card] || protected[card] {
                continue;
            }
            let current = position[card];
            if !three_leg_feasible(
                card,
                current,
                middle,
                order,
                n,
                horizontal_id,
                vertical_id,
                protected,
            ) {
                continue;
            }
            let (source, target) = match order {
                RoutingOrder::ColumnRowColumn => (current % n, card % n),
                RoutingOrder::RowColumnRow => (current / n, card / n),
            };
            candidates[source].push((target, card));
        }
        for list in &mut candidates {
            list.sort_unstable_by_key(|&(target, card)| {
                ((card * 37 + target * 17 + variant * 53) % (size + 1), card)
            });
            if variant & 2 != 0 {
                list.reverse();
            }
        }
        let mut matched_source = vec![usize::MAX; n];
        let mut chosen_card = vec![usize::MAX; n];
        for source_index in 0..n {
            let source = if variant & 4 == 0 {
                (source_index + variant) % n
            } else {
                n - 1 - (source_index + variant) % n
            };
            let mut seen_target = vec![false; n];
            augment_layer(
                source,
                &candidates,
                &mut seen_target,
                &mut matched_source,
                &mut chosen_card,
            );
        }
        for card in chosen_card {
            if card != usize::MAX {
                used[card] = true;
                assignment[card] = Some(middle);
            }
        }
    }
    assignment
}

fn constrained_assignment(
    board: &[usize],
    n: usize,
    horizontal_id: &[usize],
    vertical_id: &[usize],
    protected: &[bool],
    order: RoutingOrder,
) -> Vec<Option<usize>> {
    let mut best = vec![None; board.len()];
    let mut best_count = 0;
    for variant in 0..MATCHING_VARIANTS {
        let candidate = one_assignment(
            board,
            n,
            horizontal_id,
            vertical_id,
            protected,
            order,
            variant,
        );
        let count = candidate.iter().filter(|x| x.is_some()).count();
        if count > best_count {
            best_count = count;
            best = candidate;
        }
    }
    best
}

#[derive(Clone, Copy)]
struct LineState {
    labels: [u8; 20],
    moves: [u16; LINE_DEPTH],
    move_len: u8,
    cost: usize,
}

struct WorkBudget {
    remaining: usize,
}

impl WorkBudget {
    fn spend(&mut self) -> bool {
        if self.remaining == 0 {
            false
        } else {
            self.remaining -= 1;
            true
        }
    }
}

fn line_cost(labels: &[u8]) -> usize {
    let mut displacement = 0;
    let mut breakpoints = 0;
    for (at, &target) in labels.iter().enumerate() {
        if target != WILDCARD {
            displacement += at.abs_diff(target as usize);
        }
    }
    for pair in labels.windows(2) {
        if pair[0] != WILDCARD && pair[1] != WILDCARD && pair[1] != pair[0] + 1 {
            breakpoints += 1;
        }
    }
    100 * breakpoints + displacement
}

fn line_key(labels: &[u8]) -> u128 {
    labels
        .iter()
        .enumerate()
        .fold(0, |key, (i, &x)| key | (x as u128) << (5 * i))
}

fn operation_for_line(cells: &[usize], start: usize, half: usize, n: usize) -> Operation {
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

fn labels_for_line(
    cells: &[usize],
    board: &[usize],
    desired: &[Option<usize>],
    n: usize,
) -> ([u8; 20], usize) {
    let horizontal = cells.len() <= 1 || cells[1] == cells[0] + 1;
    let base = if horizontal {
        cells[0] % n
    } else {
        cells[0] / n
    };
    let mut labels = [WILDCARD; 20];
    let mut occupied = [false; 20];
    let mut real = 0;
    for (at, &cell) in cells.iter().enumerate() {
        let card = board[cell];
        let Some(target) = desired[card] else {
            continue;
        };
        if target >= base && target < base + cells.len() && !occupied[target - base] {
            labels[at] = (target - base) as u8;
            occupied[target - base] = true;
            real += 1;
        }
    }
    (labels, real)
}

fn route_line(
    cells: &[usize],
    desired: &[Option<usize>],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    budget: &mut WorkBudget,
    output: &mut Vec<Operation>,
) {
    if cells.len() < 2 {
        return;
    }
    let len = cells.len();
    let (initial_labels, real) = labels_for_line(cells, board, desired, n);
    if real == 0 || line_cost(&initial_labels[..len]) == 0 {
        return;
    }
    let initial_cost = line_cost(&initial_labels[..len]);
    let mut best = LineState {
        labels: initial_labels,
        moves: [0; LINE_DEPTH],
        move_len: 0,
        cost: initial_cost,
    };
    let mut beam = vec![best];
    let mut seen = HashSet::from([line_key(&initial_labels[..len])]);
    'depth: for _ in 0..LINE_DEPTH {
        let mut next = Vec::new();
        for state in &beam {
            for start in 0..len {
                for half in 1..=(len - start) / 2 {
                    if !budget.spend() {
                        break 'depth;
                    }
                    let mut child = *state;
                    for offset in 0..half {
                        child.labels.swap(start + offset, start + half + offset);
                    }
                    if !seen.insert(line_key(&child.labels[..len])) {
                        continue;
                    }
                    child.moves[child.move_len as usize] = start as u16 | ((half as u16) << 5);
                    child.move_len += 1;
                    child.cost = line_cost(&child.labels[..len]);
                    if (child.cost, child.move_len) < (best.cost, best.move_len) {
                        best = child;
                    }
                    next.push(child);
                }
            }
        }
        if best.cost == 0 || next.is_empty() {
            break;
        }
        next.sort_unstable_by_key(|state| {
            (state.cost, state.move_len, line_key(&state.labels[..len]))
        });
        next.truncate(LINE_BEAM);
        beam = next;
    }

    if best.cost < initial_cost {
        for &encoded in &best.moves[..best.move_len as usize] {
            let start = (encoded & 31) as usize;
            let half = (encoded >> 5) as usize;
            let op = operation_for_line(cells, start, half, n);
            apply(op, board, position, n);
            output.push(op);
        }
    }
    let (labels, _) = labels_for_line(cells, board, desired, n);
    if line_cost(&labels[..len]) == 0 {
        return;
    }

    // Complete the partial permutation only after the don't-care beam. Giving
    // wildcard cards the remaining labels in current order minimizes their
    // own inversions and guarantees that the requested cards reach their slots.
    let mut permutation: Vec<usize> = labels[..len].iter().map(|&x| x as usize).collect();
    let mut used = vec![false; len];
    for &target in &permutation {
        if target != WILDCARD as usize {
            used[target] = true;
        }
    }
    let remaining: Vec<_> = (0..len).filter(|&x| !used[x]).collect();
    let mut next_wildcard = 0;
    for target in &mut permutation {
        if *target == WILDCARD as usize {
            *target = remaining[next_wildcard];
            next_wildcard += 1;
        }
    }
    for target in 0..len {
        let mut at = target;
        while permutation[at] != target {
            at += 1;
        }
        while at > target {
            let op = operation_for_line(cells, at - 1, 1, n);
            apply(op, board, position, n);
            output.push(op);
            permutation.swap(at - 1, at);
            at -= 1;
        }
    }
}

fn route_segments(
    segments: &[Vec<usize>],
    desired: &[Option<usize>],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    budget: &mut WorkBudget,
    output: &mut Vec<Operation>,
) {
    let mut order: Vec<_> = (0..segments.len()).collect();
    order.sort_unstable_by_key(|&index| std::cmp::Reverse(segments[index].len()));
    for index in order {
        route_line(
            &segments[index],
            desired,
            board,
            position,
            n,
            budget,
            output,
        );
    }
}

fn protected_desired(protected: &[bool], n: usize, row_axis: bool) -> Vec<Option<usize>> {
    (0..protected.len())
        .map(|card| protected[card].then_some(if row_axis { card / n } else { card % n }))
        .collect()
}

fn route_three_legs(
    assignment: &[Option<usize>],
    protected: &[bool],
    order: RoutingOrder,
    horizontal_segments: &[Vec<usize>],
    vertical_segments: &[Vec<usize>],
    board: &mut [usize],
    position: &mut [usize],
    n: usize,
    budget: &mut WorkBudget,
    output: &mut Vec<Operation>,
) {
    match order {
        RoutingOrder::ColumnRowColumn => {
            let mut first = protected_desired(protected, n, true);
            let mut second = protected_desired(protected, n, false);
            let mut third = first.clone();
            for card in 0..board.len() {
                if let Some(middle) = assignment[card] {
                    first[card] = Some(middle);
                    second[card] = Some(card % n);
                    third[card] = Some(card / n);
                }
            }
            route_segments(
                vertical_segments,
                &first,
                board,
                position,
                n,
                budget,
                output,
            );
            route_segments(
                horizontal_segments,
                &second,
                board,
                position,
                n,
                budget,
                output,
            );
            route_segments(
                vertical_segments,
                &third,
                board,
                position,
                n,
                budget,
                output,
            );
        }
        RoutingOrder::RowColumnRow => {
            let mut first = protected_desired(protected, n, false);
            let mut second = protected_desired(protected, n, true);
            let mut third = first.clone();
            for card in 0..board.len() {
                if let Some(middle) = assignment[card] {
                    first[card] = Some(middle);
                    second[card] = Some(card / n);
                    third[card] = Some(card % n);
                }
            }
            route_segments(
                horizontal_segments,
                &first,
                board,
                position,
                n,
                budget,
                output,
            );
            route_segments(
                vertical_segments,
                &second,
                board,
                position,
                n,
                budget,
                output,
            );
            route_segments(
                horizontal_segments,
                &third,
                board,
                position,
                n,
                budget,
                output,
            );
        }
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
    fn new(graph: &[Vec<usize>], root: usize, direction_order: &[usize; 4], n: usize) -> Self {
        let size = graph.len();
        let mut tree = vec![Vec::new(); size];
        let mut parent = vec![usize::MAX; size];
        let mut depth = vec![0; size];
        parent[root] = root;
        let mut queue = VecDeque::from([root]);
        while let Some(cell) = queue.pop_front() {
            let mut neighbors = graph[cell].clone();
            neighbors.sort_unstable_by_key(|&to| {
                let direction = if to + n == cell {
                    0
                } else if to == cell + 1 {
                    1
                } else if to == cell + n {
                    2
                } else {
                    3
                };
                direction_order
                    .iter()
                    .position(|&x| x == direction)
                    .unwrap()
            });
            for to in neighbors {
                if parent[to] != usize::MAX {
                    continue;
                }
                parent[to] = cell;
                depth[to] = depth[cell] + 1;
                add_edge(&mut tree, cell, to);
                queue.push_back(to);
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

    fn select_leaf(
        &self,
        active: &[bool],
        degree: &[usize],
        position: &[usize],
        prefer_larger: bool,
    ) -> usize {
        let size = active.len();
        let mut leaf = usize::MAX;
        let mut best_distance = u16::MAX;
        for card in 0..size {
            if !active[card] || degree[card] != 1 {
                continue;
            }
            let d = self.distance[position[card] * size + card];
            let wins_tie = d == best_distance
                && (leaf == usize::MAX
                    || (prefer_larger && card > leaf)
                    || (!prefer_larger && card < leaf));
            if d < best_distance || wins_tie {
                best_distance = d;
                leaf = card;
            }
        }
        assert_ne!(leaf, usize::MAX);
        leaf
    }

    fn remove_leaf(&self, leaf: usize, active: &mut [bool], degree: &mut [usize]) {
        active[leaf] = false;
        for &to in &self.tree[leaf] {
            if active[to] {
                degree[to] -= 1;
            }
        }
        degree[leaf] = 0;
    }

    fn complete(&self, initial: &[usize], n: usize, prefer_larger: bool) -> Vec<Operation> {
        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut degree: Vec<_> = self.tree.iter().map(Vec::len).collect();
        let mut output = Vec::new();
        for _ in 1..size {
            let leaf = self.select_leaf(&active, &degree, &position, prefer_larger);
            for edge in self.path(position[leaf], leaf).windows(2) {
                let op = adjacent_operation(edge[0], edge[1], n);
                apply(op, &mut board, &mut position, n);
                output.push(op);
            }
            self.remove_leaf(leaf, &mut active, &mut degree);
        }
        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        output
    }

    fn complete_jump(
        &self,
        initial: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
        let size = initial.len();
        let mut board = initial.to_vec();
        let mut position = vec![0; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut active = vec![true; size];
        let mut degree: Vec<_> = self.tree.iter().map(Vec::len).collect();
        let mut output = Vec::new();
        for _ in 1..size {
            let leaf = self.select_leaf(&active, &degree, &position, prefer_larger);
            let path = self.path(position[leaf], leaf);
            let mut at = 0;
            while at + 1 < path.len() {
                let direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1;
                while straight < JUMP_LIMIT && at + straight + 1 < path.len() {
                    if direction_between(path[at + straight], path[at + straight + 1], n)
                        != direction
                    {
                        break;
                    }
                    straight += 1;
                }
                let mut selected = None;
                for jump in (1..=straight).rev() {
                    let Some(op) = jump_operation(path[at], direction, jump, n) else {
                        continue;
                    };
                    if jump_window_active(op, &active, n)
                        && rectangle_open(op, vertical, horizontal)
                    {
                        selected = Some((jump, op));
                        break;
                    }
                }
                let (jump, op) = selected.expect("an active tree edge always permits k=1");
                apply(op, &mut board, &mut position, n);
                assert_eq!(position[leaf], path[at + jump]);
                output.push(op);
                at += jump;
            }
            assert_eq!(board[leaf], leaf);
            self.remove_leaf(leaf, &mut active, &mut degree);
        }
        assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
        output
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
            let mut items: Vec<_> = batch
                .iter()
                .copied()
                .filter(|op| op.direction == direction)
                .collect();
            if direction == b'H' {
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
                    let expected = if direction == b'H' {
                        next.c == first.c && next.r == items[end - 1].r + 1
                    } else {
                        next.r == first.r && next.c == items[end - 1].c + 1
                    };
                    let fused = if direction == b'H' {
                        Operation {
                            h: end - at + 1,
                            ..first
                        }
                    } else {
                        Operation {
                            w: end - at + 1,
                            ..first
                        }
                    };
                    if !expected || !rectangle_open(fused, vertical, horizontal) {
                        break;
                    }
                    end += 1;
                }
                output.push(if direction == b'H' {
                    Operation {
                        h: end - at,
                        ..first
                    }
                } else {
                    Operation {
                        w: end - at,
                        ..first
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

fn valid_tail(
    state: &[usize],
    raw: Vec<Operation>,
    n: usize,
    vertical: &[Vec<u8>],
    horizontal: &[Vec<u8>],
) -> Vec<Operation> {
    let compressed = compress_fallback(&raw, n, vertical, horizontal);
    if compressed.len() < raw.len() && replay_sorted(state, &compressed, n, vertical, horizontal) {
        compressed
    } else {
        assert!(replay_sorted(state, &raw, n, vertical, horizontal));
        raw
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
    let graph = build_graph(n, &vertical, &horizontal);
    let (horizontal_lines, horizontal_id) = horizontal_segments(n, &vertical);
    let (vertical_lines, vertical_id) = vertical_segments(n, &horizontal);

    let mut board = initial.clone();
    let mut position = vec![0; size];
    for (cell, &card) in board.iter().enumerate() {
        position[card] = cell;
    }
    let mut budget = WorkBudget {
        remaining: LINE_WORK_LIMIT,
    };
    let mut prefix = Vec::new();
    let mut checkpoints = vec![Checkpoint {
        board: board.clone(),
        prefix: prefix.clone(),
    }];

    let protected_before_crc: Vec<_> = board
        .iter()
        .enumerate()
        .map(|(cell, &card)| cell == card)
        .collect();
    let crc_assignment = constrained_assignment(
        &board,
        n,
        &horizontal_id,
        &vertical_id,
        &protected_before_crc,
        RoutingOrder::ColumnRowColumn,
    );
    route_three_legs(
        &crc_assignment,
        &protected_before_crc,
        RoutingOrder::ColumnRowColumn,
        &horizontal_lines,
        &vertical_lines,
        &mut board,
        &mut position,
        n,
        &mut budget,
        &mut prefix,
    );
    checkpoints.push(Checkpoint {
        board: board.clone(),
        prefix: prefix.clone(),
    });

    // A transpose pass is useful only for the residual. Cards already sorted
    // by CRC (including incidental successes) become explicit fixed targets in
    // every RCR line and block assignment to their intermediate cells.
    let protected_before_rcr: Vec<_> = board
        .iter()
        .enumerate()
        .map(|(cell, &card)| cell == card)
        .collect();
    let rcr_assignment = constrained_assignment(
        &board,
        n,
        &horizontal_id,
        &vertical_id,
        &protected_before_rcr,
        RoutingOrder::RowColumnRow,
    );
    route_three_legs(
        &rcr_assignment,
        &protected_before_rcr,
        RoutingOrder::RowColumnRow,
        &horizontal_lines,
        &vertical_lines,
        &mut board,
        &mut position,
        n,
        &mut budget,
        &mut prefix,
    );
    checkpoints.push(Checkpoint { board, prefix });

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

    // The raw adjacent completion is the unconditional emergency answer.
    let emergency_plan = TreePlan::new(&graph, center, &ORDERS[0], n);
    let emergency_raw = emergency_plan.complete(&initial, n, false);
    assert!(replay_sorted(
        &initial,
        &emergency_raw,
        n,
        &vertical,
        &horizontal
    ));
    let mut best = valid_tail(&initial, emergency_raw, n, &vertical, &horizontal);

    for (root_index, &root) in roots.iter().enumerate() {
        for (order_index, order) in ORDERS.iter().enumerate() {
            let plan = TreePlan::new(&graph, root, order, n);
            let prefer_larger = (root_index + order_index) % 2 == 1;
            for checkpoint in &checkpoints {
                let old = valid_tail(
                    &checkpoint.board,
                    plan.complete(&checkpoint.board, n, prefer_larger),
                    n,
                    &vertical,
                    &horizontal,
                );
                let jump = valid_tail(
                    &checkpoint.board,
                    plan.complete_jump(&checkpoint.board, n, prefer_larger, &vertical, &horizontal),
                    n,
                    &vertical,
                    &horizontal,
                );
                for tail in [old, jump] {
                    let mut candidate = checkpoint.prefix.clone();
                    candidate.extend(tail);
                    // No length-only candidate is trusted: replay the complete
                    // prefix and tail from the actual contest input.
                    if replay_sorted(&initial, &candidate, n, &vertical, &horizontal)
                        && candidate.len() < best.len()
                    {
                        best = candidate;
                    }
                }
            }
        }
    }
    assert!(replay_sorted(&initial, &best, n, &vertical, &horizontal));

    let mut output = String::new();
    for op in best {
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
