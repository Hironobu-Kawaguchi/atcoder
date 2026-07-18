use std::io::{self, Read};
use std::time::Instant;

mod tree_v4 {
    use std::collections::VecDeque;
    use std::fmt::Write as _;
    use std::io::{self, Read};
    use std::time::Instant;

    const SEARCH_SECONDS: f64 = 0.52;
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
}

mod region_v5 {
    use std::collections::{HashSet, VecDeque};
    use std::fmt::Write as _;
    use std::io::{self, Read};
    use std::time::Instant;

    const BEAM_WIDTH: usize = 200;
    const ROOM_SECONDS: f64 = 0.15;
    const LINE_SECONDS: f64 = 0.0025;
    const DOOR_SECONDS: f64 = 0.055;
    const MACRO_SECONDS: f64 = 0.28;

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
        let (moves, final_cards) =
            beam_line(&initial, cells, vertical_line, room.id, owner, n, timer);
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

    fn replay(
        initial: &[usize],
        operations: &[Op],
        n: usize,
        v: &[Vec<u8>],
        h: &[Vec<u8>],
    ) -> bool {
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

    pub fn solve(input: &str) -> String {
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

        let mut board = initial.clone();
        let mut pos = vec![0; m];
        for (cell, &card) in board.iter().enumerate() {
            pos[card] = cell;
        }
        let mut checkpoints = vec![(board.clone(), Vec::<Op>::new())];
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
        let roots = [(n / 2) * n + n / 2, 0, n - 1, (n - 1) * n, m - 1];
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
}

mod zero_v6 {
    use std::collections::{HashSet, VecDeque};
    use std::fmt::Write as _;
    use std::io::{self, Read};
    use std::time::Instant;

    const SEARCH_SECONDS: f64 = 0.34;
    const SEARCH_MOVE_LIMIT: usize = 20_000;
    const CHECK_INTERVAL: usize = 20;
    const CHECKPOINT_LIMIT: usize = 5;
    const LINE_BEAM_WIDTH: usize = 200;
    const LINE_BEAM_DEPTH: usize = 14;
    const LINE_ROUTE_SECONDS: f64 = 0.68;

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
        let safe_result = result.clone();
        if let Some(mesh) = mesh_candidate {
            if mesh.len() < result.len() {
                result = mesh;
            }
        }
        if !validates(&initial_cards, &result, n, &vertical, &horizontal) {
            result = safe_result;
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

#[derive(Clone, Copy)]
struct ReplayOp {
    d: u8,
    r: usize,
    c: usize,
    h: usize,
    w: usize,
}

struct Problem {
    n: usize,
    initial: Vec<usize>,
    vertical: Vec<Vec<u8>>,
    horizontal: Vec<Vec<u8>>,
    wall_count: usize,
}

fn parse_problem(input: &str) -> Problem {
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let initial = (0..n * n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let vertical: Vec<Vec<u8>> = (0..n)
        .map(|_| tokens.next().unwrap().as_bytes().to_vec())
        .collect();
    let horizontal: Vec<Vec<u8>> = (0..n - 1)
        .map(|_| tokens.next().unwrap().as_bytes().to_vec())
        .collect();
    let wall_count = vertical
        .iter()
        .chain(horizontal.iter())
        .map(|row| row.iter().filter(|&&x| x == b'1').count())
        .sum();
    Problem {
        n,
        initial,
        vertical,
        horizontal,
        wall_count,
    }
}

fn parse_operations(output: &str) -> Option<Vec<ReplayOp>> {
    let mut result = Vec::new();
    for line in output.lines() {
        let mut fields = line.split_whitespace();
        let d = fields.next()?.as_bytes();
        if d.len() != 1 {
            return None;
        }
        let op = ReplayOp {
            d: d[0],
            r: fields.next()?.parse().ok()?,
            c: fields.next()?.parse().ok()?,
            h: fields.next()?.parse().ok()?,
            w: fields.next()?.parse().ok()?,
        };
        if fields.next().is_some() {
            return None;
        }
        result.push(op);
    }
    Some(result)
}

fn replay(problem: &Problem, output: &str) -> bool {
    let Some(operations) = parse_operations(output) else {
        return false;
    };
    if operations.len() > 100_000 {
        return false;
    }
    let n = problem.n;
    let mut board = problem.initial.clone();
    for op in operations {
        if op.r + op.h > n
            || op.c + op.w > n
            || op.h == 0
            || op.w == 0
            || (op.d != b'H' && op.d != b'V')
            || (op.d == b'H' && op.w % 2 != 0)
            || (op.d == b'V' && op.h % 2 != 0)
        {
            return false;
        }
        for r in op.r..op.r + op.h {
            for c in op.c..op.c + op.w.saturating_sub(1) {
                if problem.vertical[r][c] == b'1' {
                    return false;
                }
            }
        }
        for r in op.r..op.r + op.h.saturating_sub(1) {
            for c in op.c..op.c + op.w {
                if problem.horizontal[r][c] == b'1' {
                    return false;
                }
            }
        }
        if op.d == b'H' {
            for dr in 0..op.h {
                for dc in 0..op.w / 2 {
                    board.swap(
                        (op.r + dr) * n + op.c + dc,
                        (op.r + dr) * n + op.c + op.w / 2 + dc,
                    );
                }
            }
        } else {
            for dr in 0..op.h / 2 {
                for dc in 0..op.w {
                    board.swap(
                        (op.r + dr) * n + op.c + dc,
                        (op.r + op.h / 2 + dr) * n + op.c + dc,
                    );
                }
            }
        }
    }
    board.iter().enumerate().all(|(cell, &card)| cell == card)
}

fn consider(best: &mut Option<String>, candidate: String, problem: &Problem) {
    if !replay(problem, &candidate) {
        return;
    }
    let length = candidate.lines().count();
    let improves = match best {
        None => true,
        Some(saved) => length < saved.lines().count(),
    };
    if improves {
        *best = Some(candidate);
    }
}

fn solve(input: &str) -> String {
    let problem = parse_problem(input);
    let started = Instant::now();
    let mut best = None;

    if problem.wall_count == 0 {
        consider(&mut best, zero_v6::solve(input), &problem);
        if best.is_none() {
            consider(&mut best, tree_v4::solve(input), &problem);
        }
    } else {
        consider(&mut best, tree_v4::solve(input), &problem);
        // Portfolio search is allowed only while enough of the real 2-second
        // budget remains. Heavy-wall cases favor the region route strongly,
        // so they receive it even near the soft cutoff.
        if started.elapsed().as_secs_f64() < 0.82 || problem.wall_count >= 80 {
            consider(&mut best, region_v5::solve(input), &problem);
        }
    }
    best.expect("at least the safe tree candidate must replay")
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    print!("{}", solve(&input));
}
