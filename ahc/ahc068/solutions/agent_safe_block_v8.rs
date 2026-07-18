#[allow(dead_code)]
mod safe_portfolio_v7 {
    use std::collections::{HashSet, VecDeque};
    use std::fmt::Write as _;
    use std::io::{self, Read};
    use std::time::Instant;

    const SEARCH_SECONDS: f64 = 1.05;
    const SEARCH_MOVE_LIMIT: usize = 20_000;
    const CHECK_INTERVAL: usize = 20;
    const CHECKPOINT_LIMIT: usize = 5;
    const LINE_BEAM_WIDTH: usize = 200;
    const LINE_BEAM_DEPTH: usize = 14;
    const LINE_ROUTE_SECONDS: f64 = 0.72;
    const REGION_GATE_SECONDS: f64 = 1.16;
    const REGION_DEADLINE_SECONDS: f64 = 1.30;
    const REGION_BEAM_WIDTH: usize = 48;
    const REGION_BEAM_DEPTH: usize = 8;

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

    #[derive(Clone, Copy)]
    struct LineBeamState {
        keys: [u8; 20],
        moves: [u16; LINE_BEAM_DEPTH],
        move_count: u8,
        cost: i32,
    }

    #[derive(Clone, Copy)]
    struct RegionRoom {
        id: usize,
        r: usize,
        c: usize,
        h: usize,
        w: usize,
    }

    #[derive(Clone, Copy)]
    struct RegionState {
        cards: [u16; 20],
        moves: [u16; REGION_BEAM_DEPTH],
        move_count: u8,
        score: i32,
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

    fn intermediate_rows(initial: &[usize], n: usize) -> Vec<usize> {
        let size = n * n;
        let cards_by_column: Vec<Vec<usize>> = (0..n)
            .map(|column| (0..n).map(|row| initial[row * n + column]).collect())
            .collect();
        let mut used_card = vec![false; size];
        let mut assigned_row = vec![usize::MAX; size];
        for row in 0..n {
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
                used_card[card] = true;
                assigned_row[card] = row;
            }
        }
        assigned_row
    }

    fn line_beam_cost(keys: &[u8]) -> i32 {
        let length = keys.len();
        let mut breakpoints =
            i32::from(keys[0] != 0) + i32::from(keys[length - 1] as usize + 1 != length);
        for pair in keys.windows(2) {
            breakpoints += i32::from(pair[1] != pair[0] + 1);
        }
        let displacement: usize = keys
            .iter()
            .enumerate()
            .map(|(index, &key)| index.abs_diff(key as usize))
            .sum();
        100 * breakpoints + displacement as i32
    }

    fn line_beam_key(keys: &[u8]) -> u128 {
        keys.iter().enumerate().fold(0, |result, (index, &key)| {
            result | (key as u128) << (5 * index)
        })
    }

    fn line_beam_moves(initial_keys: &[u8], started: &Instant) -> Vec<(usize, usize)> {
        let length = initial_keys.len();
        let mut keys = [0u8; 20];
        keys[..length].copy_from_slice(initial_keys);
        let initial_cost = line_beam_cost(initial_keys);
        if initial_cost == 0 {
            return Vec::new();
        }
        let initial = LineBeamState {
            keys,
            moves: [0; LINE_BEAM_DEPTH],
            move_count: 0,
            cost: initial_cost,
        };
        let mut beam = vec![initial];
        let mut best = initial;
        let mut seen = HashSet::from([line_beam_key(initial_keys)]);
        for _ in 0..LINE_BEAM_DEPTH {
            if started.elapsed().as_secs_f64() >= LINE_ROUTE_SECONDS {
                break;
            }
            let mut next = Vec::new();
            for state in &beam {
                for start in 0..length {
                    for half in 1..=(length - start) / 2 {
                        let mut child = *state;
                        for offset in 0..half {
                            child.keys.swap(start + offset, start + half + offset);
                        }
                        if !seen.insert(line_beam_key(&child.keys[..length])) {
                            continue;
                        }
                        child.moves[child.move_count as usize] =
                            start as u16 | ((half as u16) << 5);
                        child.move_count += 1;
                        child.cost = line_beam_cost(&child.keys[..length]);
                        if child.cost < best.cost {
                            best = child;
                        }
                        next.push(child);
                    }
                }
            }
            next.sort_unstable_by_key(|state| state.cost);
            next.truncate(LINE_BEAM_WIDTH);
            if next.is_empty() || best.cost == 0 {
                break;
            }
            beam = next;
        }
        best.moves[..best.move_count as usize]
            .iter()
            .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
            .collect()
    }

    fn beam_mesh_prefix(initial: &[usize], n: usize) -> (Vec<usize>, Vec<Operation>) {
        let size = n * n;
        let middle_row = intermediate_rows(initial, n);
        let target_column: Vec<usize> = (0..size).map(|card| card % n).collect();
        let target_row: Vec<usize> = (0..size).map(|card| card / n).collect();
        let mut board = initial.to_vec();
        let mut position = vec![0; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut output = Vec::new();
        let started = Instant::now();
        for (vertical, desired) in [
            (true, middle_row.as_slice()),
            (false, target_column.as_slice()),
            (true, target_row.as_slice()),
        ] {
            for line in 0..n {
                if started.elapsed().as_secs_f64() >= LINE_ROUTE_SECONDS {
                    return (board, output);
                }
                let cells: Vec<usize> = if vertical {
                    (0..n).map(|at| at * n + line).collect()
                } else {
                    (0..n).map(|at| line * n + at).collect()
                };
                let keys: Vec<u8> = cells
                    .iter()
                    .map(|&cell| desired[board[cell]] as u8)
                    .collect();
                for (start, half) in line_beam_moves(&keys, &started) {
                    let op = if vertical {
                        Operation {
                            direction: b'V',
                            r: start,
                            c: line,
                            h: 2 * half,
                            w: 1,
                        }
                    } else {
                        Operation {
                            direction: b'H',
                            r: line,
                            c: start,
                            h: 1,
                            w: 2 * half,
                        }
                    };
                    apply(op, &mut board, &mut position, n);
                    output.push(op);
                }
            }
        }
        (board, output)
    }

    fn region_decompose(
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> (Vec<RegionRoom>, Vec<usize>) {
        let mut rectangles = Vec::new();
        for h in 2..=n {
            for w in 2..=n {
                for r in 0..=n - h {
                    for c in 0..=n - w {
                        if rectangle_open(r, c, h, w, vertical, horizontal) {
                            rectangles.push((h * w, r, c, h, w));
                        }
                    }
                }
            }
        }
        rectangles.sort_unstable_by(|a, b| b.cmp(a));
        let mut owner = vec![usize::MAX; n * n];
        let mut rooms = Vec::new();
        for &(_, r, c, h, w) in &rectangles {
            if h * w < 12
                || !(r..r + h).all(|rr| (c..c + w).all(|cc| owner[rr * n + cc] == usize::MAX))
            {
                continue;
            }
            let id = rooms.len();
            for rr in r..r + h {
                for cc in c..c + w {
                    owner[rr * n + cc] = id;
                }
            }
            rooms.push(RegionRoom { id, r, c, h, w });
        }
        for cell in 0..n * n {
            if owner[cell] == usize::MAX {
                let id = rooms.len();
                owner[cell] = id;
                rooms.push(RegionRoom {
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

    fn region_score(
        cards: &[u16],
        cells: &[usize],
        vertical: bool,
        room: usize,
        owner: &[usize],
        n: usize,
    ) -> i32 {
        let mut score = 0;
        let mut previous = None;
        for (i, &raw_card) in cards.iter().enumerate() {
            let card = raw_card as usize;
            if owner[card] != room {
                previous = None;
                continue;
            }
            let target = if vertical { card / n } else { card % n };
            let here = if vertical { cells[i] / n } else { cells[i] % n };
            score += here.abs_diff(target) as i32;
            if previous.map_or(target != here, |last| target != last + 1) {
                score += 100;
            }
            previous = Some(target);
        }
        score
    }

    fn region_key(cards: &[u16], universe: &[u16]) -> u128 {
        cards.iter().enumerate().fold(0, |key, (i, card)| {
            let rank = universe.iter().position(|x| x == card).unwrap();
            key | (rank as u128) << (5 * i)
        })
    }

    fn region_line_moves(
        initial: &[usize],
        cells: &[usize],
        vertical: bool,
        room: usize,
        owner: &[usize],
        n: usize,
        global: &Instant,
    ) -> Vec<(usize, usize)> {
        let len = initial.len();
        if len < 2 || global.elapsed().as_secs_f64() >= REGION_DEADLINE_SECONDS {
            return Vec::new();
        }
        let mut cards = [0u16; 20];
        for (i, &card) in initial.iter().enumerate() {
            cards[i] = card as u16;
        }
        let universe = cards[..len].to_vec();
        let first_score = region_score(&cards[..len], cells, vertical, room, owner, n);
        let initial_state = RegionState {
            cards,
            moves: [0; REGION_BEAM_DEPTH],
            move_count: 0,
            score: first_score,
        };
        let mut beam = vec![initial_state];
        let mut best = initial_state;
        let mut seen = HashSet::from([region_key(&cards[..len], &universe)]);
        for _ in 0..REGION_BEAM_DEPTH {
            if global.elapsed().as_secs_f64() >= REGION_DEADLINE_SECONDS {
                break;
            }
            let mut next = Vec::new();
            for state in &beam {
                for start in 0..len {
                    for half in 1..=(len - start) / 2 {
                        let mut child = *state;
                        for offset in 0..half {
                            child.cards.swap(start + offset, start + half + offset);
                        }
                        if !seen.insert(region_key(&child.cards[..len], &universe)) {
                            continue;
                        }
                        child.moves[child.move_count as usize] =
                            start as u16 | ((half as u16) << 5);
                        child.move_count += 1;
                        child.score =
                            region_score(&child.cards[..len], cells, vertical, room, owner, n);
                        if child.score < best.score {
                            best = child;
                        }
                        next.push(child);
                    }
                }
            }
            next.sort_unstable_by_key(|state| state.score);
            next.truncate(REGION_BEAM_WIDTH);
            if next.is_empty() {
                break;
            }
            beam = next;
        }
        if best.score >= first_score {
            return Vec::new();
        }
        best.moves[..best.move_count as usize]
            .iter()
            .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
            .collect()
    }

    fn reduced_region_prefix(
        initial: &[usize],
        n: usize,
        vertical_walls: &[Vec<u8>],
        horizontal_walls: &[Vec<u8>],
        distances: &[u16],
        global: &Instant,
    ) -> (Vec<usize>, Vec<Operation>) {
        let (rooms, owner) = region_decompose(n, vertical_walls, horizontal_walls);
        let mut board = initial.to_vec();
        let mut position = vec![0; board.len()];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut output = Vec::new();
        for stage in 0..3 {
            for &room in &rooms {
                if room.h * room.w < 12 || global.elapsed().as_secs_f64() >= REGION_DEADLINE_SECONDS
                {
                    continue;
                }
                let vertical = stage != 1;
                let line_count = if vertical { room.w } else { room.h };
                for line in 0..line_count {
                    let cells: Vec<usize> = if vertical {
                        (room.r..room.r + room.h)
                            .map(|r| r * n + room.c + line)
                            .collect()
                    } else {
                        (room.c..room.c + room.w)
                            .map(|c| (room.r + line) * n + c)
                            .collect()
                    };
                    let initial_line: Vec<usize> = cells.iter().map(|&cell| board[cell]).collect();
                    for (start, half) in region_line_moves(
                        &initial_line,
                        &cells,
                        vertical,
                        room.id,
                        &owner,
                        n,
                        global,
                    ) {
                        let first = cells[start];
                        let op = if vertical {
                            Operation {
                                direction: b'V',
                                r: first / n,
                                c: first % n,
                                h: 2 * half,
                                w: 1,
                            }
                        } else {
                            Operation {
                                direction: b'H',
                                r: first / n,
                                c: first % n,
                                h: 1,
                                w: 2 * half,
                            }
                        };
                        apply(op, &mut board, &mut position, n);
                        output.push(op);
                    }
                }
            }
        }
        // A small doorway family; no full region macro phase is run in V7.
        let mut doors = Vec::new();
        for c in 0..n - 1 {
            for top in 0..n {
                for bottom in top + 1..=n {
                    let op = Operation {
                        direction: b'H',
                        r: top,
                        c,
                        h: bottom - top,
                        w: 2,
                    };
                    if (top..bottom).all(|r| owner[r * n + c] != owner[r * n + c + 1])
                        && rectangle_open(op.r, op.c, op.h, op.w, vertical_walls, horizontal_walls)
                    {
                        doors.push(op);
                    }
                }
            }
        }
        for r in 0..n - 1 {
            for left in 0..n {
                for right in left + 1..=n {
                    let op = Operation {
                        direction: b'V',
                        r,
                        c: left,
                        h: 2,
                        w: right - left,
                    };
                    if (left..right).all(|c| owner[r * n + c] != owner[(r + 1) * n + c])
                        && rectangle_open(op.r, op.c, op.h, op.w, vertical_walls, horizontal_walls)
                    {
                        doors.push(op);
                    }
                }
            }
        }
        while global.elapsed().as_secs_f64() < REGION_DEADLINE_SECONDS && output.len() < 256 {
            let mut choice = None;
            let mut best_delta = 0;
            for &op in &doors {
                let value = delta(op, &board, distances, n);
                if value < best_delta {
                    best_delta = value;
                    choice = Some(op);
                }
            }
            let Some(op) = choice else { break };
            apply(op, &mut board, &mut position, n);
            output.push(op);
        }
        (board, output)
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

    fn validates(
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
            let dimensions_are_valid = op.h > 0
                && op.w > 0
                && op.r + op.h <= n
                && op.c + op.w <= n
                && ((op.direction == b'V' && op.h % 2 == 0)
                    || (op.direction == b'H' && op.w % 2 == 0));
            if !dimensions_are_valid
                || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
            {
                return false;
            }
            apply(op, &mut board, &mut position, n);
        }
        board.iter().enumerate().all(|(cell, &card)| cell == card)
    }

    pub fn solve(input: &str) -> String {
        let global_started = Instant::now();
        let mut scanner = Scanner(input.split_whitespace());
        let n: usize = scanner.next();
        let size = n * n;
        let mut board: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
        let initial_cards = board.clone();
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
        let beam_mesh_candidate = fully_open.then(|| beam_mesh_prefix(&board, n));
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
        if let Some((beam_board, beam_prefix)) = &beam_mesh_candidate {
            save_checkpoint(&mut checkpoints, beam_board, beam_prefix, &quick_plan, n);
        }

        let start = Instant::now();
        while !fully_open
            && prefix.len() < SEARCH_MOVE_LIMIT
            && start.elapsed().as_secs_f64() < SEARCH_SECONDS
        {
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
                    let raw =
                        plan.complete(&checkpoint.board, n, (root_index + order_index) % 2 == 1);
                    let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
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
            if mesh.len() < result.len() {
                result = mesh;
            }
        }
        // The complete V4/V6 result above is retained unconditionally. Region work
        // starts from the original board and is admitted only through full replay.
        if !fully_open && global_started.elapsed().as_secs_f64() < REGION_GATE_SECONDS {
            let (region_board, region_prefix) = reduced_region_prefix(
                &initial_cards,
                n,
                &vertical,
                &horizontal,
                &distances,
                &global_started,
            );
            if global_started.elapsed().as_secs_f64() < REGION_DEADLINE_SECONDS {
                let raw_tail = quick_plan.complete(&region_board, n, false);
                let tail = compress_fallback(&raw_tail, n, &vertical, &horizontal);
                let mut region_candidate = region_prefix;
                region_candidate.extend(tail);
                if region_candidate.len() < result.len()
                    && validates(&initial_cards, &region_candidate, n, &vertical, &horizontal)
                {
                    result = region_candidate;
                }
            }
        }
        if !validates(&initial_cards, &result, n, &vertical, &horizontal) {
            // Uncompressed adjacent swaps from the empty prefix are the emergency
            // path: no fusion or heuristic prefix is involved.
            result = quick_plan.complete(&initial_cards, n, false);
        }
        assert!(result.len() <= 100_000);
        assert!(validates(
            &initial_cards,
            &result,
            n,
            &vertical,
            &horizontal
        ));
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
}

#[allow(dead_code)]
mod block_compress_v7 {
    use std::cmp::Reverse;
    use std::collections::{BinaryHeap, VecDeque};
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

    fn macro_matches(
        labels: &[usize],
        op: Operation,
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> bool {
        if !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal) {
            return false;
        }
        if op.direction == b'H' {
            let half = op.w / 2;
            for dr in 0..op.h {
                for dc in 0..op.w {
                    let destination = (op.r + dr) * n + op.c + dc;
                    let source_dc = if dc < half { dc + half } else { dc - half };
                    let expected = (op.r + dr) * n + op.c + source_dc;
                    if labels[destination] != expected {
                        return false;
                    }
                }
            }
        } else {
            let half = op.h / 2;
            for dr in 0..op.h {
                for dc in 0..op.w {
                    let destination = (op.r + dr) * n + op.c + dc;
                    let source_dr = if dr < half { dr + half } else { dr - half };
                    let expected = (op.r + source_dr) * n + op.c + dc;
                    if labels[destination] != expected {
                        return false;
                    }
                }
            }
        }
        true
    }

    /// Replaces a contiguous adjacent-swap network by the one equal-block exchange
    /// having exactly the same cell permutation.  The inversion-count equality is
    /// a cheap filter: swapping two length-k blocks minimally needs k^2 adjacent
    /// transpositions per line.
    fn block_compress_raw(
        raw: &[Operation],
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
        const MAX_WINDOW: usize = 2_000;
        let size = n * n;
        let mut output = Vec::new();
        let mut begin = 0;
        while begin < raw.len() {
            debug_assert!(raw[begin].h * raw[begin].w == 2);
            let direction = raw[begin].direction;
            let mut labels = (0..size).collect::<Vec<_>>();
            let mut positions = (0..size).collect::<Vec<_>>();
            let mut min_r = n;
            let mut max_r = 0;
            let mut min_c = n;
            let mut max_c = 0;
            let mut best = None;
            for end in begin..raw.len().min(begin + MAX_WINDOW) {
                let adjacent = raw[end];
                if adjacent.direction != direction || adjacent.h * adjacent.w != 2 {
                    break;
                }
                min_r = min_r.min(adjacent.r);
                min_c = min_c.min(adjacent.c);
                max_r = max_r.max(adjacent.r + adjacent.h - 1);
                max_c = max_c.max(adjacent.c + adjacent.w - 1);
                apply(adjacent, &mut labels, &mut positions, n);

                let length = end - begin + 1;
                if length <= 1 {
                    continue;
                }
                let height = max_r - min_r + 1;
                let width = max_c - min_c + 1;
                let candidate = if direction == b'H' && width % 2 == 0 {
                    let half = width / 2;
                    (height * half * half == length).then_some(Operation {
                        direction,
                        r: min_r,
                        c: min_c,
                        h: height,
                        w: width,
                    })
                } else if direction == b'V' && height % 2 == 0 {
                    let half = height / 2;
                    (width * half * half == length).then_some(Operation {
                        direction,
                        r: min_r,
                        c: min_c,
                        h: height,
                        w: width,
                    })
                } else {
                    None
                };
                if let Some(op) = candidate {
                    if macro_matches(&labels, op, n, vertical, horizontal) {
                        best = Some((end + 1, op));
                    }
                }
            }
            if let Some((end, op)) = best {
                output.push(op);
                begin = end;
            } else {
                output.push(raw[begin]);
                begin += 1;
            }
        }
        output
    }

    /// Operations touching a common cell retain their original order; all other
    /// adjacent swaps commute.  Any topological order of this cell-dependency DAG
    /// therefore has exactly the same permutation.  Geometry-prioritized ready
    /// selection tends to place parallel layers of a block-swap network together.
    fn dependency_reorder(raw: &[Operation], n: usize) -> Vec<Operation> {
        let mut successors = vec![Vec::new(); raw.len()];
        let mut indegree = vec![0usize; raw.len()];
        let mut last = vec![usize::MAX; n * n];
        for (index, &op) in raw.iter().enumerate() {
            debug_assert!(op.h * op.w == 2);
            let a = op.r * n + op.c;
            let b = if op.direction == b'H' { a + 1 } else { a + n };
            let mut dependencies = [last[a], last[b]];
            dependencies.sort_unstable();
            for &previous in &dependencies {
                if previous != usize::MAX && (successors[previous].last().copied() != Some(index)) {
                    successors[previous].push(index);
                    indegree[index] += 1;
                }
            }
            last[a] = index;
            last[b] = index;
        }

        let key = |index: usize| {
            let op = raw[index];
            if op.direction == b'H' {
                (0usize, op.c, op.r, index)
            } else {
                (1usize, op.r, op.c, index)
            }
        };
        let mut ready = BinaryHeap::new();
        for (index, &degree) in indegree.iter().enumerate() {
            if degree == 0 {
                ready.push(Reverse(key(index)));
            }
        }
        let mut result = Vec::with_capacity(raw.len());
        while let Some(Reverse((_, _, _, index))) = ready.pop() {
            result.push(raw[index]);
            for &next in &successors[index] {
                indegree[next] -= 1;
                if indegree[next] == 0 {
                    ready.push(Reverse(key(next)));
                }
            }
        }
        assert_eq!(result.len(), raw.len());
        result
    }

    /// Retains V4's commuting-swap fusion on adjacent portions around the newly
    /// found block macros.
    fn compress_mixed(
        operations: &[Operation],
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
        let mut output = Vec::new();
        let mut adjacent = Vec::new();
        let flush = |chunk: &mut Vec<Operation>, out: &mut Vec<Operation>| {
            if !chunk.is_empty() {
                out.extend(compress_fallback(chunk, n, vertical, horizontal));
                chunk.clear();
            }
        };
        for &op in operations {
            if op.h * op.w == 2 {
                adjacent.push(op);
            } else {
                flush(&mut adjacent, &mut output);
                output.push(op);
            }
        }
        flush(&mut adjacent, &mut output);
        output
    }

    fn legal_operation(
        op: Operation,
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> bool {
        op.h > 0
            && op.w > 0
            && op.r + op.h <= n
            && op.c + op.w <= n
            && ((op.direction == b'H' && op.w % 2 == 0) || (op.direction == b'V' && op.h % 2 == 0))
            && rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
    }

    fn replay(
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
            if !legal_operation(op, n, vertical, horizontal) {
                return false;
            }
            apply(op, &mut board, &mut position, n);
        }
        board.iter().enumerate().all(|(cell, &card)| cell == card)
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

    pub fn solve(input: &str) -> String {
        let mut scanner = Scanner(input.split_whitespace());
        let n: usize = scanner.next();
        let size = n * n;
        let mut board: Vec<usize> = (0..size).map(|_| scanner.next()).collect();
        let initial_cards = board.clone();
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
        // Keep the best few *original V4* candidates unchanged.  Block detection is
        // deliberately postponed until after V4 ranking, avoiding an expensive
        // quadratic scan for all 360 plan/checkpoint combinations.
        let mut tree_candidates: Vec<(usize, Vec<Operation>, Vec<Operation>, Vec<Operation>)> =
            Vec::new();
        for (root_index, &root) in roots.iter().enumerate() {
            for (order_index, order) in ORDERS.iter().enumerate() {
                let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
                for checkpoint in &checkpoints {
                    let raw =
                        plan.complete(&checkpoint.board, n, (root_index + order_index) % 2 == 1);
                    let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
                    let total = checkpoint.prefix.len() + fallback.len();
                    if total > 100_000 {
                        continue;
                    }
                    tree_candidates.push((total, checkpoint.prefix.clone(), raw, fallback));
                    tree_candidates.sort_unstable_by_key(|candidate| candidate.0);
                    tree_candidates.truncate(4);
                }
            }
        }
        let (_, prefix, _, fallback) = tree_candidates
            .first()
            .expect("a safe exact candidate exists");
        let mut result = prefix.clone();
        result.extend(fallback.iter().copied());
        if let Some(mesh) = mesh_candidate {
            if mesh.len() < result.len() {
                result = mesh;
            }
        }

        // A replacement is admitted only after full replay from the contest input.
        // The untouched V4 result above remains the fallback candidate.
        for (_, prefix, raw, _) in &tree_candidates {
            let reordered = dependency_reorder(raw, n);
            for source in [raw.as_slice(), reordered.as_slice()] {
                let blocks = block_compress_raw(source, n, &vertical, &horizontal);
                let tail = compress_mixed(&blocks, n, &vertical, &horizontal);
                if prefix.len() + tail.len() >= result.len() {
                    continue;
                }
                let mut candidate = prefix.clone();
                candidate.extend(tail);
                if replay(&initial_cards, &candidate, n, &vertical, &horizontal) {
                    result = candidate;
                }
            }
        }
        assert!(result.len() <= 100_000);
        assert!(replay(&initial_cards, &result, n, &vertical, &horizontal));
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
}

use std::io::{self, Read};

fn has_any_wall(input: &str) -> bool {
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    for _ in 0..n * n {
        tokens.next().unwrap();
    }
    for _ in 0..n + n - 1 {
        if tokens.next().unwrap().as_bytes().contains(&b'1') {
            return true;
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let output = if has_any_wall(&input) {
        block_compress_v7::solve(&input)
    } else {
        safe_portfolio_v7::solve(&input)
    };
    print!("{output}");
}
