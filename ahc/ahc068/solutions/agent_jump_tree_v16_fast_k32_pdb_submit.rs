mod solver {
    #![allow(dead_code)]

    use std::collections::{HashSet, VecDeque};
    use std::fmt::Write as _;
    use std::io::{self, Read};
    use std::time::Instant;

    const SEARCH_SECONDS: f64 = 1.02;
    const SEARCH_MOVE_LIMIT: usize = 20_000;
    const CHECK_INTERVAL: usize = 20;
    const CHECKPOINT_LIMIT: usize = 5;
    const ZERO_BEAM_WIDTH: usize = 200;
    const ZERO_BEAM_DEPTH: usize = 14;
    const ZERO_LINE_EXPANSION_LIMIT: usize = 240_000;
    const ZERO_TOTAL_EXPANSION_LIMIT: usize = 14_400_000;

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
        /// Extend a longest line jump across up to four adjacent lines and price
        /// every moved card by its change in tree distance.
        ThickDelta,
    }

    impl JumpPolicy {
        fn max_jump(self) -> usize {
            match self {
                Self::V8Edge => 3,
                Self::Distance | Self::ThickDelta => 10,
            }
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
                        let max_offset = match policy {
                            JumpPolicy::V8Edge => 0,
                            JumpPolicy::Distance | JumpPolicy::ThickDelta => jump - 1,
                        };
                        let mut best_window = None;
                        for offset in 0..=max_offset {
                            let Some(line_op) = jump_operation_with_offset(
                                path[at],
                                first_direction,
                                jump,
                                offset,
                                n,
                            ) else {
                                continue;
                            };
                            let max_thickness = if matches!(policy, JumpPolicy::ThickDelta) {
                                4
                            } else {
                                1
                            };
                            for thickness in 1..=max_thickness {
                                for perpendicular_offset in 0..thickness {
                                    let Some(op) = thicken_jump_operation(
                                        line_op,
                                        path[at],
                                        thickness,
                                        perpendicular_offset,
                                        n,
                                    ) else {
                                        continue;
                                    };
                                    if swapped_cell(op, path[at], n) != Some(path[at + jump])
                                        || !jump_window_active(op, &active, n)
                                        || !rectangle_open(
                                            op.r, op.c, op.h, op.w, vertical, horizontal,
                                        )
                                    {
                                        continue;
                                    }
                                    let key = jump_window_key(
                                        policy,
                                        op,
                                        offset,
                                        perpendicular_offset,
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
                            }
                        }
                        if let Some((_, op)) = best_window {
                            selected = Some((jump, op));
                            break;
                        }
                    }
                    let (jump, op) = selected.expect("the adjacent tree edge is a legal jump");
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

    /// Extends a legal line jump perpendicular to its direction while retaining
    /// the focus line.  `perpendicular_offset` is the number of added lines above
    /// (for H) or to the left (for V) of the focus card.
    fn thicken_jump_operation(
        line_op: Operation,
        focus: usize,
        thickness: usize,
        perpendicular_offset: usize,
        n: usize,
    ) -> Option<Operation> {
        if thickness == 0 || perpendicular_offset >= thickness {
            return None;
        }
        let (focus_r, focus_c) = (focus / n, focus % n);
        match line_op.direction {
            b'H' if line_op.r == focus_r && focus_r >= perpendicular_offset => {
                let r = focus_r - perpendicular_offset;
                (r + thickness <= n).then_some(Operation {
                    r,
                    h: thickness,
                    ..line_op
                })
            }
            b'V' if line_op.c == focus_c && focus_c >= perpendicular_offset => {
                let c = focus_c - perpendicular_offset;
                (c + thickness <= n).then_some(Operation {
                    c,
                    w: thickness,
                    ..line_op
                })
            }
            _ => None,
        }
    }

    /// Returns where a cell lands under a block-exchange operation.  Cells
    /// outside the rectangle are intentionally reported as `None` so candidate
    /// generation can explicitly prove the focus-card landing condition.
    fn swapped_cell(op: Operation, cell: usize, n: usize) -> Option<usize> {
        let (r, c) = (cell / n, cell % n);
        if r < op.r || r >= op.r + op.h || c < op.c || c >= op.c + op.w {
            return None;
        }
        if op.direction == b'H' {
            let half = op.w / 2;
            let local = c - op.c;
            Some(if local < half {
                cell + half
            } else {
                cell - half
            })
        } else {
            let half = op.h / 2;
            let local = r - op.r;
            Some(if local < half {
                cell + half * n
            } else {
                cell - half * n
            })
        }
    }

    fn jump_window_key(
        policy: JumpPolicy,
        op: Operation,
        offset: usize,
        perpendicular_offset: usize,
        jump: usize,
        board: &[usize],
        tree_distances: &[u16],
        active: &[bool],
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> (i32, i32, i32, i32, i32, usize, usize) {
        if matches!(policy, JumpPolicy::V8Edge) {
            return (0, 0, 0, 0, 0, offset, perpendicular_offset);
        }
        let distance_delta = delta(op, board, tree_distances, n);
        let (balanced_clearance, total_clearance) =
            jump_window_clearance(op, active, n, vertical, horizontal);
        let center_penalty = ((2 * offset + 1) as isize - jump as isize).unsigned_abs() as i32;
        match policy {
            JumpPolicy::V8Edge => unreachable!(),
            JumpPolicy::Distance => (
                distance_delta,
                0,
                -(balanced_clearance as i32),
                -(total_clearance as i32),
                center_penalty,
                offset,
                perpendicular_offset,
            ),
            JumpPolicy::ThickDelta => (
                distance_delta,
                -((op.h * op.w) as i32),
                -(balanced_clearance as i32),
                -(total_clearance as i32),
                center_penalty,
                offset,
                perpendicular_offset,
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
            let mut c = op.c;
            while c > 0
                && (op.r..op.r + op.h).all(|r| active[r * n + c - 1] && vertical[r][c - 1] == b'0')
            {
                before += 1;
                c -= 1;
            }
            let mut c = op.c + op.w;
            while c < n
                && (op.r..op.r + op.h).all(|r| active[r * n + c] && vertical[r][c - 1] == b'0')
            {
                after += 1;
                c += 1;
            }
        } else {
            let mut r = op.r;
            while r > 0
                && (op.c..op.c + op.w)
                    .all(|c| active[(r - 1) * n + c] && horizontal[r - 1][c] == b'0')
            {
                before += 1;
                r -= 1;
            }
            let mut r = op.r + op.h;
            while r < n
                && (op.c..op.c + op.w).all(|c| active[r * n + c] && horizontal[r - 1][c] == b'0')
            {
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

    fn zero_augment_matching(
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
                || zero_augment_matching(
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

    /// Edge-colors the source-column/target-column bipartite multigraph.  Cards
    /// with the same color form one intermediate row containing every target
    /// column exactly once.
    fn zero_intermediate_rows(initial: &[usize], n: usize) -> Vec<usize> {
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
                assert!(zero_augment_matching(
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
                assigned_row[card] = row;
            }
        }
        assert!(assigned_row.iter().all(|&row| row != usize::MAX));
        assigned_row
    }

    #[derive(Clone, Copy)]
    struct ZeroBeamState {
        keys: [u8; 20],
        moves: [u16; ZERO_BEAM_DEPTH],
        move_count: u8,
        cost: i32,
        key: u128,
    }

    fn zero_line_cost(keys: &[u8]) -> i32 {
        let len = keys.len();
        let breakpoints = i32::from(keys[0] != 0)
            + i32::from(keys[len - 1] as usize + 1 != len)
            + keys
                .windows(2)
                .map(|pair| i32::from(pair[1] != pair[0] + 1))
                .sum::<i32>();
        let displacement = keys
            .iter()
            .enumerate()
            .map(|(index, &key)| index.abs_diff(key as usize))
            .sum::<usize>();
        100 * breakpoints + displacement as i32
    }

    fn zero_line_key(keys: &[u8]) -> u128 {
        keys.iter().enumerate().fold(0, |result, (index, &key)| {
            result | (key as u128) << (5 * index)
        })
    }

    /// Deterministic beam search for adjacent equal-length block exchanges.
    /// Work is bounded by fixed depth, width, per-line expansion count, and a
    /// global expansion count; it never observes wall-clock time.
    fn zero_line_moves(
        initial_keys: &[u8],
        remaining_expansions: &mut usize,
    ) -> Vec<(usize, usize)> {
        let length = initial_keys.len();
        let mut keys = [0u8; 20];
        keys[..length].copy_from_slice(initial_keys);
        let initial_key = zero_line_key(initial_keys);
        let initial = ZeroBeamState {
            keys,
            moves: [0; ZERO_BEAM_DEPTH],
            move_count: 0,
            cost: zero_line_cost(initial_keys),
            key: initial_key,
        };
        if initial.cost == 0 || *remaining_expansions == 0 {
            return Vec::new();
        }

        let mut best = initial;
        let mut beam = vec![initial];
        let mut seen = HashSet::from([initial_key]);
        let mut line_expansions = 0usize;
        for _ in 0..ZERO_BEAM_DEPTH {
            if best.cost == 0
                || *remaining_expansions == 0
                || line_expansions == ZERO_LINE_EXPANSION_LIMIT
            {
                break;
            }
            let mut next = Vec::new();
            'expand: for state in &beam {
                for start in 0..length {
                    for half in 1..=(length - start) / 2 {
                        if *remaining_expansions == 0
                            || line_expansions == ZERO_LINE_EXPANSION_LIMIT
                        {
                            break 'expand;
                        }
                        *remaining_expansions -= 1;
                        line_expansions += 1;
                        let mut child = *state;
                        for offset in 0..half {
                            child.keys.swap(start + offset, start + half + offset);
                        }
                        child.key = zero_line_key(&child.keys[..length]);
                        if !seen.insert(child.key) {
                            continue;
                        }
                        child.moves[child.move_count as usize] =
                            start as u16 | ((half as u16) << 5);
                        child.move_count += 1;
                        child.cost = zero_line_cost(&child.keys[..length]);
                        if child.cost < best.cost {
                            best = child;
                        }
                        next.push(child);
                    }
                }
            }
            next.sort_unstable_by_key(|state| (state.cost, state.key));
            next.truncate(ZERO_BEAM_WIDTH);
            if next.is_empty() {
                break;
            }
            beam = next;
        }

        best.moves[..best.move_count as usize]
            .iter()
            .map(|&encoded| ((encoded & 31) as usize, (encoded >> 5) as usize))
            .collect()
    }

    fn zero_sort_line(
        cells: &[usize],
        desired: &[usize],
        board: &mut [usize],
        position: &mut [usize],
        n: usize,
        remaining_expansions: &mut usize,
        output: &mut Vec<Operation>,
    ) {
        let initial_keys: Vec<u8> = cells
            .iter()
            .map(|&cell| desired[board[cell]] as u8)
            .collect();
        for (start, half) in zero_line_moves(&initial_keys, remaining_expansions) {
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

        // The beam normally solves a line outright.  Fixed work limits may stop
        // it early, so insertion by adjacent swaps makes every phase exact and
        // gives the zero-wall branch an unconditional completion guarantee.
        for target in 0..n {
            let mut at = target;
            while at < n && desired[board[cells[at]]] != target {
                at += 1;
            }
            assert_ne!(at, n);
            while at > target {
                let op = adjacent_operation(cells[at - 1], cells[at], n);
                apply(op, board, position, n);
                output.push(op);
                at -= 1;
            }
        }
    }

    /// Exact column-row-column routing for a completely open board.
    fn deterministic_zero_route(initial: &[usize], n: usize) -> Vec<Operation> {
        let size = n * n;
        let intermediate_row = zero_intermediate_rows(initial, n);
        let target_column: Vec<usize> = (0..size).map(|card| card % n).collect();
        let target_row: Vec<usize> = (0..size).map(|card| card / n).collect();
        let mut board = initial.to_vec();
        let mut position = vec![0usize; size];
        for (cell, &card) in board.iter().enumerate() {
            position[card] = cell;
        }
        let mut operations = Vec::new();
        let mut remaining_expansions = ZERO_TOTAL_EXPANSION_LIMIT;
        for (vertical, desired) in [
            (true, intermediate_row.as_slice()),
            (false, target_column.as_slice()),
            (true, target_row.as_slice()),
        ] {
            for line in 0..n {
                let cells: Vec<usize> = if vertical {
                    (0..n).map(|at| at * n + line).collect()
                } else {
                    (0..n).map(|at| line * n + at).collect()
                };
                zero_sort_line(
                    &cells,
                    desired,
                    &mut board,
                    &mut position,
                    n,
                    &mut remaining_expansions,
                    &mut operations,
                );
            }
        }
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
        for policy in [JumpPolicy::Distance, JumpPolicy::ThickDelta] {
            let long_raw =
                plan.complete_jump(checkpoint, n, prefer_larger, vertical, horizontal, policy);
            let long = compress_fallback(&long_raw, n, vertical, horizontal);
            if replay_sorted(checkpoint, &long, n, vertical, horizontal) && long.len() < best.len()
            {
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
        let wall_count = vertical
            .iter()
            .chain(horizontal.iter())
            .map(|row| row.iter().filter(|&&wall| wall == b'1').count())
            .sum::<usize>();
        let fully_open = wall_count == 0;
        if fully_open {
            let mut result = deterministic_zero_route(&initial, n);
            if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
                const ZERO_FALLBACK_ORDER: [usize; 4] = [0, 1, 2, 3];
                let center = (n / 2) * n + n / 2;
                let plan = TreePlan::new(n, center, &ZERO_FALLBACK_ORDER, &vertical, &horizontal);
                result = choose_completion(&plan, &initial, n, false, &vertical, &horizontal);
            }
            assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
            let mut output = String::new();
            for op in result {
                writeln!(
                    output,
                    "{} {} {} {} {}",
                    op.direction as char, op.r, op.c, op.h, op.w
                )
                .unwrap();
            }
            return output;
        }
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
            if mesh.len() < result.len()
                && replay_sorted(&initial, &mesh, n, &vertical, &horizontal)
            {
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
    // Shared implementation for the three V12 beam-width wrappers.
    //
    // This file is included after agent_jump_tree_v11_thick_delta.rs, inside the
    // same module, so it deliberately reuses that solver's private data types and
    // helpers.  The wrappers differ only in the const generic BEAM_WIDTH.

    impl TreePlan {
        /// Reproduces V10's line-only Clearance policy. V11 replaced that enum
        /// variant with ThickDelta, so the V10 policy is kept here as a separate
        /// method in order to make the first-stage score exactly V10-compatible.
        fn complete_jump_clearance_v12(
            &self,
            initial: &[usize],
            n: usize,
            prefer_larger: bool,
            vertical: &[Vec<u8>],
            horizontal: &[Vec<u8>],
        ) -> Vec<Operation> {
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
                let mut at = 0;
                while at + 1 < path.len() {
                    let first_direction = direction_between(path[at], path[at + 1], n);
                    let mut straight = 1;
                    while straight < 10 && at + straight + 1 < path.len() {
                        if direction_between(path[at + straight], path[at + straight + 1], n)
                            != first_direction
                        {
                            break;
                        }
                        straight += 1;
                    }

                    let mut selected = None;
                    for jump in (1..=straight).rev() {
                        let mut best_window = None;
                        for offset in 0..jump {
                            let Some(op) = jump_operation_with_offset(
                                path[at],
                                first_direction,
                                jump,
                                offset,
                                n,
                            ) else {
                                continue;
                            };
                            if !jump_window_active(op, &active, n)
                                || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                            {
                                continue;
                            }
                            let distance_delta = delta(op, &board, &self.distance, n);
                            let (balanced_clearance, total_clearance) =
                                jump_window_clearance(op, &active, n, vertical, horizontal);
                            let center_penalty =
                                ((2 * offset + 1) as isize - jump as isize).unsigned_abs() as i32;
                            let key = (
                                -(balanced_clearance as i32),
                                -(total_clearance as i32),
                                distance_delta,
                                center_penalty,
                                offset,
                            );
                            if best_window
                                .as_ref()
                                .is_none_or(|(best_key, _)| key < *best_key)
                            {
                                best_window = Some((key, op));
                            }
                        }
                        if let Some((_, op)) = best_window {
                            selected = Some((jump, op));
                            break;
                        }
                    }
                    let (jump, op) = selected.expect("the adjacent tree edge is a legal jump");
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

    /// Exact first-stage completion used by V10: old, V8Edge, Distance and
    /// Clearance, including the same compression and replay guards.
    fn choose_v10_completion_v12(
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
        let distance_raw = plan.complete_jump(
            checkpoint,
            n,
            prefer_larger,
            vertical,
            horizontal,
            JumpPolicy::Distance,
        );
        let distance = compress_fallback(&distance_raw, n, vertical, horizontal);
        if replay_sorted(checkpoint, &distance, n, vertical, horizontal)
            && distance.len() < best.len()
        {
            best = distance;
        }

        let clearance_raw =
            plan.complete_jump_clearance_v12(checkpoint, n, prefer_larger, vertical, horizontal);
        let clearance = compress_fallback(&clearance_raw, n, vertical, horizontal);
        if replay_sorted(checkpoint, &clearance, n, vertical, horizontal)
            && clearance.len() < best.len()
        {
            best = clearance;
        }
        best
    }

    #[derive(Clone, Copy)]
    struct BeamCandidateV12 {
        cheap_total: usize,
        root_index: usize,
        order_index: usize,
        checkpoint_index: usize,
    }

    fn solve_beam_delta_v12<const BEAM_WIDTH: usize>(input: &str) -> String {
        assert!(BEAM_WIDTH > 0);
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
        let wall_count = vertical
            .iter()
            .chain(horizontal.iter())
            .map(|row| row.iter().filter(|&&wall| wall == b'1').count())
            .sum::<usize>();
        let fully_open = wall_count == 0;
        if fully_open {
            let mut result = deterministic_zero_route(&initial, n);
            if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
                const ZERO_FALLBACK_ORDER: [usize; 4] = [0, 1, 2, 3];
                let center = (n / 2) * n + n / 2;
                let plan = TreePlan::new(n, center, &ZERO_FALLBACK_ORDER, &vertical, &horizontal);
                result =
                    choose_v10_completion_v12(&plan, &initial, n, false, &vertical, &horizontal);
            }
            assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
            return render_operations_v12(&result);
        }

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

        // Preserve V10's macro-prefix generation exactly. The second-stage beam
        // below is deterministic and performs exactly min(BEAM_WIDTH, states)
        // ThickDelta completions for the checkpoints produced by this loop.
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

        // Stage 1: enumerate the actual 9 * 8 * checkpoints.len() states and
        // score every one with the exact V10 completion portfolio. Retain the
        // global V10 winner unconditionally as the monotonic safety floor.
        let mut ranked = Vec::with_capacity(roots.len() * ORDERS.len() * checkpoints.len());
        let mut baseline_result: Option<Vec<Operation>> = None;
        for (root_index, &root) in roots.iter().enumerate() {
            for (order_index, order) in ORDERS.iter().enumerate() {
                let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
                let prefer_larger = (root_index + order_index) % 2 == 1;
                for (checkpoint_index, checkpoint) in checkpoints.iter().enumerate() {
                    let fallback = choose_v10_completion_v12(
                        &plan,
                        &checkpoint.board,
                        n,
                        prefer_larger,
                        &vertical,
                        &horizontal,
                    );
                    let total = checkpoint.prefix.len() + fallback.len();
                    if total > 100_000 {
                        continue;
                    }
                    ranked.push(BeamCandidateV12 {
                        cheap_total: total,
                        root_index,
                        order_index,
                        checkpoint_index,
                    });
                    if baseline_result
                        .as_ref()
                        .is_none_or(|best| total < best.len())
                    {
                        let mut complete = checkpoint.prefix.clone();
                        complete.extend(fallback);
                        baseline_result = Some(complete);
                    }
                }
            }
        }

        ranked.sort_by_key(|state| {
            (
                state.cheap_total,
                state.root_index,
                state.order_index,
                state.checkpoint_index,
            )
        });
        let baseline_result = baseline_result.expect("a safe exact V10 candidate exists");
        assert!(replay_sorted(
            &initial,
            &baseline_result,
            n,
            &vertical,
            &horizontal
        ));
        let mut result = baseline_result.clone();

        // Stage 2: only the cheap-score beam receives the expensive ThickDelta
        // completion. Invalid or longer candidates are ignored; the exact V10
        // result above therefore remains a per-instance monotonic guard.
        for state in ranked.iter().take(BEAM_WIDTH) {
            let root = roots[state.root_index];
            let order = &ORDERS[state.order_index];
            let checkpoint = &checkpoints[state.checkpoint_index];
            let prefer_larger = (state.root_index + state.order_index) % 2 == 1;
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let raw = plan.complete_jump(
                &checkpoint.board,
                n,
                prefer_larger,
                &vertical,
                &horizontal,
                JumpPolicy::ThickDelta,
            );
            let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
            if !replay_sorted(&checkpoint.board, &fallback, n, &vertical, &horizontal) {
                continue;
            }
            let total = checkpoint.prefix.len() + fallback.len();
            if total < result.len() && total <= 100_000 {
                let mut complete = checkpoint.prefix.clone();
                complete.extend(fallback);
                if replay_sorted(&initial, &complete, n, &vertical, &horizontal) {
                    result = complete;
                }
            }
        }

        // A release-build replay guard retains the known-valid V10 result even if
        // a future edit accidentally invalidates the selected ThickDelta output.
        if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
            result = baseline_result;
        }
        assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
        assert!(result.len() <= 100_000);
        render_operations_v12(&result)
    }

    fn render_operations_v12(operations: &[Operation]) -> String {
        let mut output = String::new();
        for op in operations {
            writeln!(
                output,
                "{} {} {} {} {}",
                op.direction as char, op.r, op.c, op.h, op.w
            )
            .unwrap();
        }
        output
    }

    pub fn run_v12<const BEAM_WIDTH: usize>() {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input).unwrap();
        print!("{}", solve_beam_delta_v12::<BEAM_WIDTH>(&input));
    }
    // V14 keeps V12 K16's mandatory V10 portfolio, but shortens the macro phase,
    // validates completion candidates lazily, and makes ThickDelta an optional,
    // deadline-aware stage. This file is included after the V11 ThickDelta engine
    // and the V12 shared implementation, so it can reuse their private helpers.

    use std::time::Duration;

    const V14_SEARCH_SECONDS: f64 = 0.80;
    const V14_BEAM_WIDTH: usize = 32;
    const V14_OPTIONAL_START: Duration = Duration::from_millis(1_600);
    const V14_OPTIONAL_DEADLINE: Duration = Duration::from_millis(1_690);

    impl TreePlan {
        /// ThickDelta with the exact V11 candidate order and key, but with two
        /// implementation changes:
        ///
        /// - distance deltas for the seven possible perpendicular lines are
        ///   cached and summed, which is exactly equivalent to evaluating the
        ///   whole rectangle because a block exchange acts independently on each
        ///   line;
        /// - the optional completion may abort without affecting the mandatory
        ///   baseline when the solve-wide deadline is reached.
        fn complete_jump_thick_delta_v14(
            &self,
            initial: &[usize],
            n: usize,
            prefer_larger: bool,
            vertical: &[Vec<u8>],
            horizontal: &[Vec<u8>],
            solve_start: &Instant,
        ) -> Option<Vec<Operation>> {
            const MAX_THICKNESS: usize = 4;
            const CACHE_RADIUS: usize = MAX_THICKNESS - 1;
            const CACHE_SIZE: usize = 2 * CACHE_RADIUS + 1;

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
                if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                    return None;
                }

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
                let mut at = 0;
                while at + 1 < path.len() {
                    if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                        return None;
                    }

                    let first_direction = direction_between(path[at], path[at + 1], n);
                    let mut straight = 1;
                    while straight < JumpPolicy::ThickDelta.max_jump()
                        && at + straight + 1 < path.len()
                    {
                        if direction_between(path[at + straight], path[at + straight + 1], n)
                            != first_direction
                        {
                            break;
                        }
                        straight += 1;
                    }

                    let focus = path[at];
                    let focus_cross = if first_direction.0 == 0 {
                        focus / n
                    } else {
                        focus % n
                    };
                    let mut selected = None;

                    for jump in (1..=straight).rev() {
                        let mut best_window = None;
                        for offset in 0..jump {
                            if solve_start.elapsed() >= V14_OPTIONAL_DEADLINE {
                                return None;
                            }

                            let Some(line_op) =
                                jump_operation_with_offset(focus, first_direction, jump, offset, n)
                            else {
                                continue;
                            };

                            // A thickness <= 4 containing the focus line can only
                            // touch focus_cross-3 .. focus_cross+3. Cache each
                            // single-line delta once for this longitudinal window.
                            let mut line_deltas = [0i32; CACHE_SIZE];
                            for (cache_index, slot) in line_deltas.iter_mut().enumerate() {
                                let relative = cache_index as isize - CACHE_RADIUS as isize;
                                let cross = focus_cross as isize + relative;
                                if !(0..n as isize).contains(&cross) {
                                    continue;
                                }
                                let single = if line_op.direction == b'H' {
                                    Operation {
                                        r: cross as usize,
                                        h: 1,
                                        ..line_op
                                    }
                                } else {
                                    Operation {
                                        c: cross as usize,
                                        w: 1,
                                        ..line_op
                                    }
                                };
                                *slot = delta(single, &board, &self.distance, n);
                            }

                            for thickness in 1..=MAX_THICKNESS {
                                for perpendicular_offset in 0..thickness {
                                    let Some(op) = thicken_jump_operation(
                                        line_op,
                                        focus,
                                        thickness,
                                        perpendicular_offset,
                                        n,
                                    ) else {
                                        continue;
                                    };
                                    if swapped_cell(op, focus, n) != Some(path[at + jump])
                                        || !jump_window_active(op, &active, n)
                                        || !rectangle_open(
                                            op.r, op.c, op.h, op.w, vertical, horizontal,
                                        )
                                    {
                                        continue;
                                    }

                                    let cache_start = CACHE_RADIUS - perpendicular_offset;
                                    let distance_delta = line_deltas
                                        [cache_start..cache_start + thickness]
                                        .iter()
                                        .sum::<i32>();
                                    let (balanced_clearance, total_clearance) =
                                        jump_window_clearance(op, &active, n, vertical, horizontal);
                                    let center_penalty = ((2 * offset + 1) as isize - jump as isize)
                                        .unsigned_abs()
                                        as i32;
                                    let key = (
                                        distance_delta,
                                        -((op.h * op.w) as i32),
                                        -(balanced_clearance as i32),
                                        -(total_clearance as i32),
                                        center_penalty,
                                        offset,
                                        perpendicular_offset,
                                    );
                                    if best_window
                                        .as_ref()
                                        .is_none_or(|(best_key, _)| key < *best_key)
                                    {
                                        best_window = Some((key, op));
                                    }
                                }
                            }
                        }
                        if let Some((_, op)) = best_window {
                            selected = Some((jump, op));
                            break;
                        }
                    }

                    let (jump, op) = selected.expect("the adjacent tree edge is a legal jump");
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
                remaining -= 1;
                for &to in &self.tree[leaf] {
                    if active[to] {
                        degree[to] -= 1;
                    }
                }
                degree[leaf] = 0;
            }

            assert!(board.iter().enumerate().all(|(cell, &card)| cell == card));
            Some(operations)
        }
    }

    /// Builds the exact four V10 completion candidates in the original priority
    /// order. A stable length sort preserves the original strict-`<` tie behavior:
    /// old, V8Edge, Distance, then Clearance. Only candidates that can actually
    /// win are replayed; an invalid shortest candidate falls through safely.
    fn choose_v10_completion_v14(
        plan: &TreePlan,
        checkpoint: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Vec<Operation> {
        let old_raw = plan.complete(checkpoint, n, prefer_larger);
        let old = compress_fallback(&old_raw, n, vertical, horizontal);

        let v8_raw = plan.complete_jump(
            checkpoint,
            n,
            prefer_larger,
            vertical,
            horizontal,
            JumpPolicy::V8Edge,
        );
        let v8 = compress_fallback(&v8_raw, n, vertical, horizontal);

        let distance_raw = plan.complete_jump(
            checkpoint,
            n,
            prefer_larger,
            vertical,
            horizontal,
            JumpPolicy::Distance,
        );
        let distance = compress_fallback(&distance_raw, n, vertical, horizontal);

        let clearance_raw =
            plan.complete_jump_clearance_v12(checkpoint, n, prefer_larger, vertical, horizontal);
        let clearance = compress_fallback(&clearance_raw, n, vertical, horizontal);

        let mut candidates = [old, v8, distance, clearance];
        candidates.sort_by_key(Vec::len);
        candidates
            .into_iter()
            .find(|candidate| replay_sorted(checkpoint, candidate, n, vertical, horizontal))
            .expect("at least the exact old completion is replay-valid")
    }

    #[derive(Clone, Copy)]
    struct BeamCandidateV14 {
        cheap_total: usize,
        root_index: usize,
        order_index: usize,
        checkpoint_index: usize,
    }

    fn solve_fast_k16_v14(input: &str) -> String {
        let solve_start = Instant::now();
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
        let wall_count = vertical
            .iter()
            .chain(horizontal.iter())
            .map(|row| row.iter().filter(|&&wall| wall == b'1').count())
            .sum::<usize>();
        let fully_open = wall_count == 0;

        if fully_open {
            let mut result = deterministic_zero_route(&initial, n);
            if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
                const ZERO_FALLBACK_ORDER: [usize; 4] = [0, 1, 2, 3];
                let center = (n / 2) * n + n / 2;
                let plan = TreePlan::new(n, center, &ZERO_FALLBACK_ORDER, &vertical, &horizontal);
                result =
                    choose_v10_completion_v14(&plan, &initial, n, false, &vertical, &horizontal);
            }
            assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
            return render_operations_v12(&result);
        }

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

        let macro_start = Instant::now();
        while prefix.len() < SEARCH_MOVE_LIMIT
            && macro_start.elapsed().as_secs_f64() < V14_SEARCH_SECONDS
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

        // Mandatory stage: always finish the exact V10 portfolio and retain its
        // global winner before any deadline-controlled ThickDelta work begins.
        let mut ranked = Vec::with_capacity(roots.len() * ORDERS.len() * checkpoints.len());
        let mut baseline_result: Option<Vec<Operation>> = None;
        for (root_index, &root) in roots.iter().enumerate() {
            for (order_index, order) in ORDERS.iter().enumerate() {
                let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
                let prefer_larger = (root_index + order_index) % 2 == 1;
                for (checkpoint_index, checkpoint) in checkpoints.iter().enumerate() {
                    let fallback = choose_v10_completion_v14(
                        &plan,
                        &checkpoint.board,
                        n,
                        prefer_larger,
                        &vertical,
                        &horizontal,
                    );
                    let total = checkpoint.prefix.len() + fallback.len();
                    if total > 100_000 {
                        continue;
                    }
                    ranked.push(BeamCandidateV14 {
                        cheap_total: total,
                        root_index,
                        order_index,
                        checkpoint_index,
                    });
                    if baseline_result
                        .as_ref()
                        .is_none_or(|best| total < best.len())
                    {
                        let mut complete = checkpoint.prefix.clone();
                        complete.extend(fallback);
                        baseline_result = Some(complete);
                    }
                }
            }
        }

        ranked.sort_by_key(|state| {
            (
                state.cheap_total,
                state.root_index,
                state.order_index,
                state.checkpoint_index,
            )
        });
        let baseline_result = baseline_result.expect("a safe exact V10 candidate exists");
        assert!(replay_sorted(
            &initial,
            &baseline_result,
            n,
            &vertical,
            &horizontal
        ));
        let mut result = baseline_result.clone();

        // Optional stage: no new completion starts at or after 1.60 s. A running
        // completion is itself abortable at 1.69 s, leaving the mandatory baseline
        // and the final replay/output reserve untouched.
        for state in ranked.iter().take(V14_BEAM_WIDTH) {
            if solve_start.elapsed() >= V14_OPTIONAL_START {
                break;
            }
            let root = roots[state.root_index];
            let order = &ORDERS[state.order_index];
            let checkpoint = &checkpoints[state.checkpoint_index];
            let prefer_larger = (state.root_index + state.order_index) % 2 == 1;
            let plan = TreePlan::new(n, root, order, &vertical, &horizontal);
            let Some(raw) = plan.complete_jump_thick_delta_v14(
                &checkpoint.board,
                n,
                prefer_larger,
                &vertical,
                &horizontal,
                &solve_start,
            ) else {
                break;
            };
            let fallback = compress_fallback(&raw, n, &vertical, &horizontal);
            let total = checkpoint.prefix.len() + fallback.len();
            if total >= result.len() || total > 100_000 {
                continue;
            }
            if !replay_sorted(&checkpoint.board, &fallback, n, &vertical, &horizontal) {
                continue;
            }
            let mut complete = checkpoint.prefix.clone();
            complete.extend(fallback);
            if replay_sorted(&initial, &complete, n, &vertical, &horizontal) {
                result = complete;
            }
        }

        // Release-build guard: every printed operation sequence receives a final
        // full replay, with the already-validated mandatory baseline as fallback.
        if !replay_sorted(&initial, &result, n, &vertical, &horizontal) {
            result = baseline_result;
        }
        assert!(replay_sorted(&initial, &result, n, &vertical, &horizontal));
        assert!(result.len() <= 100_000);
        render_operations_v12(&result)
    }

    pub fn run_v14_fast_k16() {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input).unwrap();
        print!("{}", solve_fast_k16_v14(&input));
    }

    // V15 retains V14 Fast K16 verbatim as its mandatory baseline, then applies
    // an optional semantics-preserving short-line peephole pass. This file is
    // included after the V14 implementation and deliberately reuses its private
    // parser, operation, replay, and rendering helpers.

    const V15_MAX_LINE_LENGTH: usize = 8;
    const V15_MAX_WINDOW_OPERATIONS: usize = 24;
    const V15_POSTPROCESS_START_MS: u128 = 1_780;
    const V15_POSTPROCESS_DEADLINE_MS: u128 = 1_840;

    struct LinePdbV15 {
        parent: Vec<usize>,
        action: Vec<(u8, u8)>,
    }

    #[derive(Clone, Copy, PartialEq, Eq)]
    struct ThinLineV15 {
        direction: u8,
        line: usize,
        start: usize,
        length: usize,
    }

    fn factorial_v15(n: usize) -> usize {
        (1..=n).product()
    }

    fn permutation_rank_v15(permutation: &[u8; V15_MAX_LINE_LENGTH], length: usize) -> usize {
        let mut rank = 0;
        for i in 0..length {
            let smaller = (i + 1..length)
                .filter(|&j| permutation[j] < permutation[i])
                .count();
            rank += smaller * factorial_v15(length - 1 - i);
        }
        rank
    }

    fn encode_permutation_v15(permutation: &[u8; V15_MAX_LINE_LENGTH], length: usize) -> u32 {
        let mut code = 0u32;
        for (i, &value) in permutation.iter().take(length).enumerate() {
            code |= (value as u32) << (3 * i);
        }
        code
    }

    fn decode_permutation_v15(code: u32, length: usize) -> [u8; V15_MAX_LINE_LENGTH] {
        let mut permutation = [0u8; V15_MAX_LINE_LENGTH];
        for (i, value) in permutation.iter_mut().take(length).enumerate() {
            *value = ((code >> (3 * i)) & 7) as u8;
        }
        permutation
    }

    fn build_line_pdb_v15(length: usize, solve_start: &Instant) -> Option<LinePdbV15> {
        let states = factorial_v15(length);
        let mut parent = vec![usize::MAX; states];
        let mut action = vec![(0u8, 0u8); states];
        let identity = std::array::from_fn(|i| i as u8);
        let mut queue = VecDeque::with_capacity(states);
        parent[0] = 0;
        queue.push_back(encode_permutation_v15(&identity, length));
        let mut expansions = 0usize;

        while let Some(code) = queue.pop_front() {
            expansions += 1;
            if expansions & 255 == 0
                && solve_start.elapsed().as_millis() >= V15_POSTPROCESS_DEADLINE_MS
            {
                return None;
            }
            let permutation = decode_permutation_v15(code, length);
            let current_rank = permutation_rank_v15(&permutation, length);
            for start in 0..length {
                for block in 1..=(length - start) / 2 {
                    let mut next = permutation;
                    for offset in 0..block {
                        next.swap(start + offset, start + block + offset);
                    }
                    let next_rank = permutation_rank_v15(&next, length);
                    if parent[next_rank] != usize::MAX {
                        continue;
                    }
                    parent[next_rank] = current_rank;
                    action[next_rank] = (start as u8, (2 * block) as u8);
                    queue.push_back(encode_permutation_v15(&next, length));
                }
            }
        }

        debug_assert!(parent.iter().all(|&value| value != usize::MAX));
        Some(LinePdbV15 { parent, action })
    }

    fn shortest_line_actions_v15(
        pdb: &LinePdbV15,
        permutation: &[u8; V15_MAX_LINE_LENGTH],
        length: usize,
    ) -> Vec<(usize, usize)> {
        let mut rank = permutation_rank_v15(permutation, length);
        let mut reversed = Vec::new();
        while rank != 0 {
            let (start, width) = pdb.action[rank];
            reversed.push((start as usize, width as usize));
            rank = pdb.parent[rank];
        }
        reversed.reverse();
        reversed
    }

    fn thin_line_v15(op: Operation) -> Option<ThinLineV15> {
        if op.direction == b'H' && op.h == 1 {
            Some(ThinLineV15 {
                direction: op.direction,
                line: op.r,
                start: op.c,
                length: op.w,
            })
        } else if op.direction == b'V' && op.w == 1 {
            Some(ThinLineV15 {
                direction: op.direction,
                line: op.c,
                start: op.r,
                length: op.h,
            })
        } else {
            None
        }
    }

    fn line_span_open_v15(
        direction: u8,
        line: usize,
        start: usize,
        length: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> bool {
        if direction == b'H' {
            rectangle_open(line, start, 1, length, vertical, horizontal)
        } else {
            rectangle_open(start, line, length, 1, vertical, horizontal)
        }
    }

    fn net_line_permutation_v15(
        operations: &[Operation],
        span_start: usize,
        span_length: usize,
    ) -> [u8; V15_MAX_LINE_LENGTH] {
        let mut permutation = std::array::from_fn(|i| i as u8);
        for &op in operations {
            let thin = thin_line_v15(op).expect("window contains only thin line operations");
            let start = thin.start - span_start;
            let block = thin.length / 2;
            for offset in 0..block {
                permutation.swap(start + offset, start + block + offset);
            }
        }
        debug_assert!(span_length <= V15_MAX_LINE_LENGTH);
        permutation
    }

    fn line_operation_v15(
        direction: u8,
        line: usize,
        span_start: usize,
        local_start: usize,
        width: usize,
    ) -> Operation {
        if direction == b'H' {
            Operation {
                direction,
                r: line,
                c: span_start + local_start,
                h: 1,
                w: width,
            }
        } else {
            Operation {
                direction,
                r: span_start + local_start,
                c: line,
                h: width,
                w: 1,
            }
        }
    }

    fn parse_operations_v15(output: &str) -> Option<Vec<Operation>> {
        let mut tokens = output.split_whitespace();
        let mut operations = Vec::new();
        while let Some(direction) = tokens.next() {
            let direction = *direction.as_bytes().first()?;
            let r = tokens.next()?.parse().ok()?;
            let c = tokens.next()?.parse().ok()?;
            let h = tokens.next()?.parse().ok()?;
            let w = tokens.next()?.parse().ok()?;
            operations.push(Operation {
                direction,
                r,
                c,
                h,
                w,
            });
        }
        Some(operations)
    }

    fn short_line_postprocess_v15(
        baseline: &[Operation],
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
        solve_start: &Instant,
    ) -> Option<Vec<Operation>> {
        let operation_count = baseline.len();
        let mut pdbs: Vec<Option<LinePdbV15>> = (0..=V15_MAX_LINE_LENGTH).map(|_| None).collect();
        let mut cost = vec![usize::MAX; operation_count + 1];
        let mut previous = vec![usize::MAX; operation_count + 1];
        let mut replacement: Vec<Option<Vec<Operation>>> =
            (0..=operation_count).map(|_| None).collect();
        cost[0] = 0;

        for begin in 0..operation_count {
            if solve_start.elapsed().as_millis() >= V15_POSTPROCESS_DEADLINE_MS {
                return None;
            }
            if cost[begin] + 1 < cost[begin + 1] {
                cost[begin + 1] = cost[begin] + 1;
                previous[begin + 1] = begin;
                replacement[begin + 1] = None;
            }

            let Some(first) = thin_line_v15(baseline[begin]) else {
                continue;
            };
            let mut span_start = first.start;
            let mut span_end = first.start + first.length;
            let window_limit = operation_count.min(begin + V15_MAX_WINDOW_OPERATIONS);
            for end in begin + 1..window_limit {
                let Some(next) = thin_line_v15(baseline[end]) else {
                    break;
                };
                if next.direction != first.direction || next.line != first.line {
                    break;
                }
                span_start = span_start.min(next.start);
                span_end = span_end.max(next.start + next.length);
                let span_length = span_end - span_start;
                if span_length > V15_MAX_LINE_LENGTH {
                    break;
                }
                if !line_span_open_v15(
                    first.direction,
                    first.line,
                    span_start,
                    span_length,
                    vertical,
                    horizontal,
                ) {
                    continue;
                }
                if pdbs[span_length].is_none() {
                    pdbs[span_length] = Some(build_line_pdb_v15(span_length, solve_start)?);
                }
                let permutation =
                    net_line_permutation_v15(&baseline[begin..=end], span_start, span_length);
                let actions = shortest_line_actions_v15(
                    pdbs[span_length].as_ref().unwrap(),
                    &permutation,
                    span_length,
                );
                let original_length = end + 1 - begin;
                if actions.len() >= original_length {
                    continue;
                }
                let candidate: Vec<Operation> = actions
                    .into_iter()
                    .map(|(local_start, width)| {
                        line_operation_v15(
                            first.direction,
                            first.line,
                            span_start,
                            local_start,
                            width,
                        )
                    })
                    .collect();
                let next_index = end + 1;
                let candidate_cost = cost[begin] + candidate.len();
                if candidate_cost < cost[next_index] {
                    cost[next_index] = candidate_cost;
                    previous[next_index] = begin;
                    replacement[next_index] = Some(candidate);
                }
            }
        }

        if cost[operation_count] >= operation_count {
            return Some(baseline.to_vec());
        }
        let mut chunks = Vec::new();
        let mut at = operation_count;
        while at > 0 {
            let before = previous[at];
            debug_assert_ne!(before, usize::MAX);
            if let Some(candidate) = replacement[at].take() {
                chunks.push(candidate);
            } else {
                debug_assert_eq!(before + 1, at);
                chunks.push(vec![baseline[before]]);
            }
            at = before;
        }
        chunks.reverse();
        Some(chunks.into_iter().flatten().collect())
    }

    fn solve_short_line_pdb_v15(input: &str) -> String {
        let solve_start = Instant::now();
        let baseline_text = solve_fast_k16_v14(input);
        if solve_start.elapsed().as_millis() >= V15_POSTPROCESS_START_MS {
            return baseline_text;
        }

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
        let Some(baseline) = parse_operations_v15(&baseline_text) else {
            return baseline_text;
        };
        let Some(candidate) =
            short_line_postprocess_v15(&baseline, &vertical, &horizontal, &solve_start)
        else {
            return baseline_text;
        };
        if candidate.len() >= baseline.len()
            || solve_start.elapsed().as_millis() >= V15_POSTPROCESS_DEADLINE_MS
            || !replay_sorted(&initial, &candidate, n, &vertical, &horizontal)
        {
            return baseline_text;
        }
        render_operations_v12(&candidate)
    }

    pub fn run_v15_short_line_pdb() {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input).unwrap();
        print!("{}", solve_short_line_pdb_v15(&input));
    }
}

fn main() {
    solver::run_v15_short_line_pdb();
}
