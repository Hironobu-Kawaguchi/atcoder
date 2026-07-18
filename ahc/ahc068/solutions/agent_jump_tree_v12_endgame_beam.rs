// Thin derivative of V11 ThickSafe.  Keeping the proven implementation in one
// included module makes the V12 delta reviewable; flatten this include before
// submitting a single source file to AtCoder.
mod v11 {
    #![allow(dead_code)]

    include!("agent_jump_tree_v11_thick_safe.rs");

    const ENDGAME_ACTIVE: usize = 24;
    const ENDGAME_BEAM_WIDTH: usize = 8;
    const ENDGAME_BRANCHING: usize = 3;
    const ENDGAME_TRANSITION_LIMIT: usize = 552;

    #[derive(Clone, Copy)]
    enum V12CompletionMode {
        Adjacent,
        V8Edge,
        Distance,
        ThickSafe,
    }

    impl V12CompletionMode {
        fn jump_policy(self) -> Option<JumpPolicy> {
            match self {
                Self::Adjacent => None,
                Self::V8Edge => Some(JumpPolicy::V8Edge),
                Self::Distance => Some(JumpPolicy::Distance),
                Self::ThickSafe => Some(JumpPolicy::ThickSafe),
            }
        }

        fn max_jump(self) -> usize {
            self.jump_policy().map_or(1, JumpPolicy::max_jump)
        }

        fn parallel_service(self) -> usize {
            if matches!(self, Self::ThickSafe) {
                4
            } else {
                1
            }
        }
    }

    struct V12CompletionChoice {
        operations: Vec<Operation>,
        mode: V12CompletionMode,
    }

    struct V12PortfolioChoice {
        prefix: Vec<Operation>,
        fallback: V12CompletionChoice,
        checkpoint_board: Vec<usize>,
        root: usize,
        order: [usize; 4],
        prefer_larger: bool,
    }

    #[derive(Clone)]
    struct V12EndgameState {
        board: Vec<usize>,
        position: Vec<usize>,
        active: Vec<bool>,
        degree: Vec<usize>,
        remaining: usize,
        operations: Vec<Operation>,
        fingerprint: u128,
    }

    fn v12_choose_completion(
        plan: &TreePlan,
        checkpoint: &[usize],
        n: usize,
        prefer_larger: bool,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> V12CompletionChoice {
        let old_raw = plan.complete(checkpoint, n, prefer_larger);
        let old = compress_fallback(&old_raw, n, vertical, horizontal);
        assert!(replay_sorted(checkpoint, &old, n, vertical, horizontal));
        let mut best = V12CompletionChoice {
            operations: old,
            mode: V12CompletionMode::Adjacent,
        };

        for (mode, policy) in [
            (V12CompletionMode::V8Edge, JumpPolicy::V8Edge),
            (V12CompletionMode::Distance, JumpPolicy::Distance),
            (V12CompletionMode::ThickSafe, JumpPolicy::ThickSafe),
        ] {
            let raw =
                plan.complete_jump(checkpoint, n, prefer_larger, vertical, horizontal, policy);
            let candidate = compress_fallback(&raw, n, vertical, horizontal);
            if replay_sorted(checkpoint, &candidate, n, vertical, horizontal)
                && candidate.len() < best.operations.len()
            {
                best = V12CompletionChoice {
                    operations: candidate,
                    mode,
                };
            }
        }
        best
    }

    fn v12_greedy_leaf(plan: &TreePlan, state: &V12EndgameState, prefer_larger: bool) -> usize {
        let size = state.board.len();
        let mut leaf = usize::MAX;
        let mut best_distance = u16::MAX;
        for candidate in 0..size {
            if !state.active[candidate] || state.degree[candidate] != 1 {
                continue;
            }
            let d = plan.distance[state.position[candidate] * size + candidate];
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
        leaf
    }

    fn v12_route_step_estimate(
        plan: &TreePlan,
        state: &V12EndgameState,
        leaf: usize,
        mode: V12CompletionMode,
        n: usize,
    ) -> usize {
        let path = plan.path(state.position[leaf], leaf);
        if matches!(mode, V12CompletionMode::Adjacent) {
            return path.len().saturating_sub(1);
        }
        let max_jump = mode.max_jump();
        let mut result = 0usize;
        let mut at = 0usize;
        while at + 1 < path.len() {
            let direction = direction_between(path[at], path[at + 1], n);
            let mut straight = 1usize;
            while at + straight + 1 < path.len()
                && direction_between(path[at + straight], path[at + straight + 1], n) == direction
            {
                straight += 1;
            }
            result += straight.div_ceil(max_jump);
            at += straight;
        }
        result
    }

    fn v12_leaf_choices(
        plan: &TreePlan,
        state: &V12EndgameState,
        mode: V12CompletionMode,
        prefer_larger: bool,
        n: usize,
    ) -> Vec<usize> {
        // Always retain the original greedy decision as the first branch.
        let greedy = v12_greedy_leaf(plan, state, prefer_larger);
        let size = state.board.len();
        let mut alternatives: Vec<(usize, u16, usize, usize)> = (0..size)
            .filter(|&leaf| leaf != greedy && state.active[leaf] && state.degree[leaf] == 1)
            .map(|leaf| {
                let steps = v12_route_step_estimate(plan, state, leaf, mode, n);
                let distance = plan.distance[state.position[leaf] * size + leaf];
                let tie = if prefer_larger { size - 1 - leaf } else { leaf };
                (steps, distance, tie, leaf)
            })
            .collect();
        alternatives.sort_unstable();
        let mut result = Vec::with_capacity(ENDGAME_BRANCHING);
        result.push(greedy);
        result.extend(
            alternatives
                .into_iter()
                .take(ENDGAME_BRANCHING - 1)
                .map(|entry| entry.3),
        );
        result
    }

    fn v12_route_leaf(
        plan: &TreePlan,
        state: &mut V12EndgameState,
        leaf: usize,
        mode: V12CompletionMode,
        n: usize,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) {
        debug_assert!(state.active[leaf] && state.degree[leaf] == 1);
        let path = plan.path(state.position[leaf], leaf);
        debug_assert!(path.iter().all(|&cell| state.active[cell]));

        if let Some(policy) = mode.jump_policy() {
            let mut at = 0usize;
            while at + 1 < path.len() {
                let first_direction = direction_between(path[at], path[at + 1], n);
                let mut straight = 1usize;
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
                    let max_offset = if matches!(policy, JumpPolicy::V8Edge) {
                        0
                    } else {
                        jump - 1
                    };
                    let mut best_window = None;
                    for offset in 0..=max_offset {
                        let Some(op) =
                            jump_operation_with_offset(path[at], first_direction, jump, offset, n)
                        else {
                            continue;
                        };
                        if !jump_window_active(op, &state.active, n)
                            || !rectangle_open(op.r, op.c, op.h, op.w, vertical, horizontal)
                        {
                            continue;
                        }
                        let key = jump_window_key(
                            policy,
                            op,
                            offset,
                            jump,
                            &state.board,
                            &plan.distance,
                            &state.active,
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
                    if let Some((_, thin_op)) = best_window {
                        let op = if matches!(policy, JumpPolicy::ThickSafe) {
                            thicken_jump_safely(
                                thin_op,
                                &state.board,
                                &plan.distance,
                                &state.active,
                                n,
                                vertical,
                                horizontal,
                            )
                        } else {
                            thin_op
                        };
                        selected = Some((jump, op));
                        break;
                    }
                }
                let (jump, op) = selected.expect("an adjacent tree edge is always legal");
                debug_assert_eq!(state.board[path[at]], leaf);
                apply(op, &mut state.board, &mut state.position, n);
                assert_eq!(state.position[leaf], path[at + jump]);
                state.operations.push(op);
                at += jump;
            }
        } else {
            for edge in path.windows(2) {
                let op = adjacent_operation(edge[0], edge[1], n);
                apply(op, &mut state.board, &mut state.position, n);
                state.operations.push(op);
            }
        }

        assert_eq!(state.board[leaf], leaf);
        state.active[leaf] = false;
        state.remaining -= 1;
        for &to in &plan.tree[leaf] {
            if state.active[to] {
                state.degree[to] -= 1;
            }
        }
        state.degree[leaf] = 0;
        state.fingerprint = v12_state_fingerprint(state);
    }

    fn v12_mix64(mut value: u64) -> u64 {
        value ^= value >> 30;
        value = value.wrapping_mul(0xbf58_476d_1ce4_e5b9);
        value ^= value >> 27;
        value = value.wrapping_mul(0x94d0_49bb_1331_11eb);
        value ^ (value >> 31)
    }

    fn v12_state_fingerprint(state: &V12EndgameState) -> u128 {
        let mut low = 0x243f_6a88_85a3_08d3u64;
        let mut high = 0x1319_8a2e_0370_7344u64;
        for (cell, &card) in state.board.iter().enumerate() {
            let tagged = card as u64
                ^ ((cell as u64) << 10)
                ^ ((state.active[cell] as u64) << 63)
                ^ ((state.degree[cell] as u64) << 48);
            low = v12_mix64(low ^ tagged);
            high = v12_mix64(high.wrapping_add(tagged.rotate_left((cell % 63 + 1) as u32)));
        }
        ((high as u128) << 64) | low as u128
    }

    fn v12_same_state(a: &V12EndgameState, b: &V12EndgameState) -> bool {
        // The u128 value is only an index hint.  Equality of all semantic
        // fields is checked, so a hash collision can never discard a state.
        a.fingerprint == b.fingerprint
            && a.remaining == b.remaining
            && a.board == b.board
            && a.active == b.active
            && a.degree == b.degree
    }

    fn v12_state_rank(
        plan: &TreePlan,
        state: &V12EndgameState,
        mode: V12CompletionMode,
    ) -> (usize, usize, usize, u128) {
        let size = state.board.len();
        let potential = (0..size)
            .filter(|&card| state.active[card])
            .map(|card| plan.distance[state.position[card] * size + card] as usize)
            .sum::<usize>();
        let service = mode.max_jump() * mode.parallel_service();
        let tail_estimate = potential.div_ceil(service.max(1));
        (
            state.operations.len() + tail_estimate,
            state.operations.len(),
            potential,
            state.fingerprint,
        )
    }

    fn v12_endgame_beam_completion(
        plan: &TreePlan,
        checkpoint: &[usize],
        n: usize,
        prefer_larger: bool,
        mode: V12CompletionMode,
        vertical: &[Vec<u8>],
        horizontal: &[Vec<u8>],
    ) -> Option<Vec<Operation>> {
        let size = checkpoint.len();
        let mut position = vec![0usize; size];
        for (cell, &card) in checkpoint.iter().enumerate() {
            position[card] = cell;
        }
        let mut initial_state = V12EndgameState {
            board: checkpoint.to_vec(),
            position,
            active: vec![true; size],
            degree: plan.tree.iter().map(Vec::len).collect(),
            remaining: size,
            operations: Vec::new(),
            fingerprint: 0,
        };

        // Reproduce the selected completion mode exactly until only a small
        // tail remains.  The existing portfolio result is retained separately.
        while initial_state.remaining > ENDGAME_ACTIVE {
            let leaf = v12_greedy_leaf(plan, &initial_state, prefer_larger);
            v12_route_leaf(
                plan,
                &mut initial_state,
                leaf,
                mode,
                n,
                vertical,
                horizontal,
            );
        }
        let common_raw = std::mem::take(&mut initial_state.operations);
        initial_state.fingerprint = v12_state_fingerprint(&initial_state);

        let mut beam = vec![initial_state];
        let mut transitions = 0usize;
        while beam[0].remaining > 1 {
            let mut next: Vec<V12EndgameState> = Vec::new();
            'states: for state in &beam {
                let choices = v12_leaf_choices(plan, state, mode, prefer_larger, n);
                for leaf in choices {
                    if transitions == ENDGAME_TRANSITION_LIMIT {
                        break 'states;
                    }
                    transitions += 1;
                    let mut child = state.clone();
                    v12_route_leaf(plan, &mut child, leaf, mode, n, vertical, horizontal);
                    if let Some(index) = next
                        .iter()
                        .position(|existing| v12_same_state(existing, &child))
                    {
                        if child.operations.len() < next[index].operations.len() {
                            next[index] = child;
                        }
                    } else {
                        next.push(child);
                    }
                }
            }
            if next.is_empty() {
                return None;
            }
            next.sort_unstable_by_key(|state| v12_state_rank(plan, state, mode));
            next.truncate(ENDGAME_BEAM_WIDTH);
            beam = next;
        }
        debug_assert!(transitions <= ENDGAME_TRANSITION_LIMIT);

        let mut best: Option<Vec<Operation>> = None;
        for state in beam {
            if !state
                .board
                .iter()
                .enumerate()
                .all(|(cell, &card)| cell == card)
            {
                continue;
            }
            let mut raw = common_raw.clone();
            raw.extend(state.operations);
            let candidate = compress_fallback(&raw, n, vertical, horizontal);
            if replay_sorted(checkpoint, &candidate, n, vertical, horizontal)
                && best
                    .as_ref()
                    .is_none_or(|current| candidate.len() < current.len())
            {
                best = Some(candidate);
            }
        }
        best
    }

    pub fn solve_v12(input: &str) -> String {
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
            // Preserve the already-specialized zero-wall branch byte-for-byte.
            return solve(input);
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
        assert!(distances.iter().all(|&distance| distance != u16::MAX));
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
        let mut best_choice: Option<V12PortfolioChoice> = None;
        for (root_index, &root) in roots.iter().enumerate() {
            for (order_index, &order) in ORDERS.iter().enumerate() {
                let plan = TreePlan::new(n, root, &order, &vertical, &horizontal);
                let prefer_larger = (root_index + order_index) % 2 == 1;
                for checkpoint in &checkpoints {
                    let fallback = v12_choose_completion(
                        &plan,
                        &checkpoint.board,
                        n,
                        prefer_larger,
                        &vertical,
                        &horizontal,
                    );
                    let total = checkpoint.prefix.len() + fallback.operations.len();
                    if total > 100_000 {
                        continue;
                    }
                    let improves = best_choice.as_ref().is_none_or(|current| {
                        total < current.prefix.len() + current.fallback.operations.len()
                    });
                    if improves {
                        best_choice = Some(V12PortfolioChoice {
                            prefix: checkpoint.prefix.clone(),
                            fallback,
                            checkpoint_board: checkpoint.board.clone(),
                            root,
                            order,
                            prefer_larger,
                        });
                    }
                }
            }
        }

        let choice = best_choice.expect("the V11 portfolio always has an exact candidate");
        let mut result = choice.prefix.clone();
        result.extend(choice.fallback.operations.iter().copied());
        // The original exact V11 result remains the unconditional monotonic
        // guard.  V12 may replace only its selected completion, and only after
        // an independent full replay proves legality and exact sorting.
        let selected_plan = TreePlan::new(n, choice.root, &choice.order, &vertical, &horizontal);
        if let Some(endgame) = v12_endgame_beam_completion(
            &selected_plan,
            &choice.checkpoint_board,
            n,
            choice.prefer_larger,
            choice.fallback.mode,
            &vertical,
            &horizontal,
        ) {
            let mut candidate = choice.prefix;
            candidate.extend(endgame);
            if candidate.len() < result.len()
                && replay_sorted(&initial, &candidate, n, &vertical, &horizontal)
            {
                result = candidate;
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
}

fn main() {
    let mut input = String::new();
    let mut stdin = std::io::stdin();
    std::io::Read::read_to_string(&mut stdin, &mut input).unwrap();
    print!("{}", v11::solve_v12(&input));
}
