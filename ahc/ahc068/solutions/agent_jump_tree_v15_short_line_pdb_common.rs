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
        if expansions & 255 == 0 && solve_start.elapsed().as_millis() >= V15_POSTPROCESS_DEADLINE_MS
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
                    line_operation_v15(first.direction, first.line, span_start, local_start, width)
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
