use std::io::{self, Read};

const CHUNK_HEIGHTS: [usize; 3] = [3, 4, 5];
const STRIPE_WIDTHS: [usize; 3] = [3, 4, 5];
const BOTTOM_STRIP_HEIGHTS: [usize; 3] = [3, 4, 5];

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Dir {
    U,
    D,
    L,
    R,
}

impl Dir {
    fn ch(self) -> char {
        match self {
            Dir::U => 'U',
            Dir::D => 'D',
            Dir::L => 'L',
            Dir::R => 'R',
        }
    }
}

#[derive(Clone)]
struct Input {
    n: usize,
    desired: Vec<u8>,
    food: Vec<u8>,
}

#[derive(Clone, Copy)]
struct Rect {
    top: usize,
    bottom: usize,
    left: usize,
    right: usize,
}

impl Rect {
    fn height(self) -> usize {
        self.bottom - self.top + 1
    }

    fn width(self) -> usize {
        self.right - self.left + 1
    }
}

#[derive(Clone, Copy)]
enum Corner {
    TL,
    TR,
    BR,
    BL,
}

#[derive(Clone)]
struct LocalBoard {
    h: usize,
    w: usize,
    food: Vec<u8>,
}

#[derive(Clone)]
struct StripePlan {
    width: usize,
    score: i32,
    route: Vec<usize>,
    exit_top: bool,
}

#[derive(Clone, Copy)]
struct InnerPrev {
    prev_rows: usize,
    prev_side: usize,
    height: usize,
    use_row: bool,
}

#[derive(Clone, Copy)]
struct OuterPrev {
    prev_cols: usize,
    prev_side: usize,
    width: usize,
}

fn cell(stride: usize, r: usize, c: usize) -> usize {
    r * stride + c
}

fn prefix_route(n: usize) -> Vec<usize> {
    let mut route = Vec::new();
    for r in 5..n {
        route.push(cell(n, r, 0));
    }
    route
}

fn build_food_prefix(input: &Input) -> Vec<Vec<usize>> {
    let mut pref = vec![vec![0usize; input.n + 1]; input.n + 1];
    for r in 0..input.n {
        for c in 0..input.n {
            let add = usize::from(input.food[cell(input.n, r, c)] != 0);
            pref[r + 1][c + 1] = pref[r + 1][c] + pref[r][c + 1] - pref[r][c] + add;
        }
    }
    pref
}

fn foods_in_rect(pref: &[Vec<usize>], rect: Rect) -> usize {
    pref[rect.bottom + 1][rect.right + 1] - pref[rect.top][rect.right + 1] - pref[rect.bottom + 1][rect.left] + pref[rect.top][rect.left]
}

fn count_foods_on_cells(food: &[u8], cells: &[usize]) -> usize {
    cells.iter().filter(|&&p| food[p] != 0).count()
}

fn count_matches_on_cells(food: &[u8], desired: &[u8], start_idx: usize, cells: &[usize]) -> i32 {
    let mut idx = start_idx;
    let mut score = 0;
    for &p in cells {
        let color = food[p];
        if color == 0 {
            continue;
        }
        if idx < desired.len() && color == desired[idx] {
            score += 1;
        }
        idx += 1;
    }
    score
}

fn build_chunk_route_bottom(stride: usize, row_lo: usize, height: usize, col_lo: usize, start_right: bool, use_row: bool) -> Vec<usize> {
    let mut route = Vec::with_capacity(height * 3);
    if use_row {
        for i in 0..height {
            let r = row_lo + (height - 1 - i);
            if !start_right {
                if i % 2 == 0 {
                    for dc in 0..3 {
                        route.push(cell(stride, r, col_lo + dc));
                    }
                } else {
                    for dc in (0..3).rev() {
                        route.push(cell(stride, r, col_lo + dc));
                    }
                }
            } else if i % 2 == 0 {
                for dc in (0..3).rev() {
                    route.push(cell(stride, r, col_lo + dc));
                }
            } else {
                for dc in 0..3 {
                    route.push(cell(stride, r, col_lo + dc));
                }
            }
        }
    } else if !start_right {
        for i in 0..3 {
            let c = col_lo + i;
            if i % 2 == 0 {
                for dr in 0..height {
                    let r = row_lo + (height - 1 - dr);
                    route.push(cell(stride, r, c));
                }
            } else {
                for dr in 0..height {
                    let r = row_lo + dr;
                    route.push(cell(stride, r, c));
                }
            }
        }
    } else {
        for i in 0..3 {
            let c = col_lo + (2 - i);
            if i % 2 == 0 {
                for dr in 0..height {
                    let r = row_lo + (height - 1 - dr);
                    route.push(cell(stride, r, c));
                }
            } else {
                for dr in 0..height {
                    let r = row_lo + dr;
                    route.push(cell(stride, r, c));
                }
            }
        }
    }
    route
}

fn build_chunk_route(stride: usize, row_lo: usize, height: usize, col_lo: usize, start_top: bool, start_right: bool, use_row: bool) -> Vec<usize> {
    if !start_top {
        return build_chunk_route_bottom(stride, row_lo, height, col_lo, start_right, use_row);
    }
    let mut route = Vec::with_capacity(height * 3);
    for &p in &build_chunk_route_bottom(stride, 0, height, col_lo, start_right, use_row) {
        let local_r = p / stride;
        let c = p % stride;
        let actual_r = row_lo + (height - 1 - local_r);
        route.push(cell(stride, actual_r, c));
    }
    route
}

fn next_inner_side(start_side: usize, height: usize, use_row: bool) -> usize {
    if use_row {
        if height % 2 == 1 {
            1 - start_side
        } else {
            start_side
        }
    } else {
        1 - start_side
    }
}

fn end_is_top(stride: usize, route: &[usize]) -> bool {
    let last = *route.last().unwrap();
    last / stride == 0
}

fn best_width3_stripe(board: &LocalBoard, desired: &[u8], desired_start: usize, col_lo: usize, start_top: bool) -> Vec<StripePlan> {
    let mut row_food_prefix = vec![0usize; board.h + 1];
    for used in 0..board.h {
        let r = if !start_top { board.h - 1 - used } else { used };
        let mut add = 0usize;
        for dc in 0..3 {
            if board.food[cell(board.w, r, col_lo + dc)] != 0 {
                add += 1;
            }
        }
        row_food_prefix[used + 1] = row_food_prefix[used] + add;
    }

    let neg_inf = -1_000_000_000i32;
    let mut dp = vec![vec![neg_inf; 2]; board.h + 1];
    let mut prev = vec![vec![None; 2]; board.h + 1];
    dp[0][0] = 0;

    for used in 0..=board.h {
        for side in 0..2 {
            if dp[used][side] == neg_inf {
                continue;
            }
            for &height in &CHUNK_HEIGHTS {
                if used + height > board.h {
                    continue;
                }
                let row_lo = if !start_top { board.h - (used + height) } else { used };
                for &use_row in &[false, true] {
                    let route = build_chunk_route(board.w, row_lo, height, col_lo, start_top, side == 1, use_row);
                    let score = count_matches_on_cells(&board.food, desired, desired_start + row_food_prefix[used], &route);
                    let next_side = next_inner_side(side, height, use_row);
                    let cand = dp[used][side] + score;
                    if cand > dp[used + height][next_side] {
                        dp[used + height][next_side] = cand;
                        prev[used + height][next_side] = Some(InnerPrev {
                            prev_rows: used,
                            prev_side: side,
                            height,
                            use_row,
                        });
                    }
                }
            }
        }
    }

    if dp[board.h][1] == neg_inf {
        return Vec::new();
    }
    let mut parts = Vec::new();
    let mut used = board.h;
    let mut side = 1usize;
    while used > 0 {
        let Some(info) = prev[used][side] else {
            return Vec::new();
        };
        let row_lo = if !start_top { board.h - (info.prev_rows + info.height) } else { info.prev_rows };
        let route = build_chunk_route(board.w, row_lo, info.height, col_lo, start_top, info.prev_side == 1, info.use_row);
        parts.push(route);
        used = info.prev_rows;
        side = info.prev_side;
    }
    parts.reverse();

    let mut route = Vec::with_capacity(3 * board.h);
    for part in parts {
        route.extend(part);
    }
    vec![StripePlan {
        width: 3,
        score: dp[board.h][1],
        exit_top: end_is_top(board.w, &route),
        route,
    }]
}

fn build_column_snake(board: &LocalBoard, col_lo: usize, width: usize, start_top: bool) -> StripePlan {
    let mut route = Vec::with_capacity(board.h * width);
    for dc in 0..width {
        let c = col_lo + dc;
        let downward = if !start_top { dc % 2 == 0 } else { dc % 2 == 1 };
        if downward {
            for r in 0..board.h {
                let rr = board.h - 1 - r;
                route.push(cell(board.w, rr, c));
            }
        } else {
            for r in 0..board.h {
                route.push(cell(board.w, r, c));
            }
        }
    }
    StripePlan {
        width,
        score: 0,
        exit_top: end_is_top(board.w, &route),
        route,
    }
}

fn build_row_snake(board: &LocalBoard, col_lo: usize, width: usize, start_top: bool) -> Option<StripePlan> {
    let mut route = Vec::with_capacity(board.h * width);
    for i in 0..board.h {
        let r = if !start_top { board.h - 1 - i } else { i };
        if i % 2 == 0 {
            for dc in 0..width {
                route.push(cell(board.w, r, col_lo + dc));
            }
        } else {
            for dc in (0..width).rev() {
                route.push(cell(board.w, r, col_lo + dc));
            }
        }
    }
    if route.last().copied().unwrap() % board.w != col_lo + width - 1 {
        return None;
    }
    Some(StripePlan {
        width,
        score: 0,
        exit_top: end_is_top(board.w, &route),
        route,
    })
}

fn evaluate_plan(mut plan: StripePlan, board: &LocalBoard, desired: &[u8], desired_start: usize) -> StripePlan {
    plan.score = count_matches_on_cells(&board.food, desired, desired_start, &plan.route);
    plan
}

fn stripe_plans(board: &LocalBoard, desired: &[u8], desired_start: usize, col_lo: usize, width: usize, start_top: bool) -> Vec<StripePlan> {
    let mut plans = Vec::new();
    if width == 3 {
        plans.extend(best_width3_stripe(board, desired, desired_start, col_lo, start_top));
    }
    plans.push(evaluate_plan(build_column_snake(board, col_lo, width, start_top), board, desired, desired_start));
    if let Some(plan) = build_row_snake(board, col_lo, width, start_top) {
        plans.push(evaluate_plan(plan, board, desired, desired_start));
    }
    plans.sort_by_key(|plan| (plan.width, plan.exit_top, plan.route.clone()));
    plans.dedup_by(|a, b| a.exit_top == b.exit_top && a.route == b.route);
    plans
}

fn remaining_foods_prefix_by_cols(board: &LocalBoard) -> Vec<usize> {
    let mut pref = vec![0usize; board.w + 1];
    for c in 0..board.w {
        let mut add = 0usize;
        for r in 0..board.h {
            if board.food[cell(board.w, r, c)] != 0 {
                add += 1;
            }
        }
        pref[c + 1] = pref[c] + add;
    }
    pref
}

fn solve_local_lr(board: &LocalBoard, desired: &[u8], desired_start: usize) -> Vec<usize> {
    if board.w == 0 {
        return Vec::new();
    }
    let rem_food_pref = remaining_foods_prefix_by_cols(board);
    let width_total = board.w;

    let neg_inf = -1_000_000_000i32;
    let mut dp = vec![vec![neg_inf; 2]; width_total + 1];
    let mut prev = vec![vec![None; 2]; width_total + 1];
    let mut plans = vec![vec![None; 2]; width_total + 1];
    dp[0][0] = 0;

    for used in 0..=width_total {
        for side in 0..2 {
            if dp[used][side] == neg_inf {
                continue;
            }
            for &width in &STRIPE_WIDTHS {
                if used + width > width_total {
                    continue;
                }
                let local_col_lo = used;
                let local_desired_start = desired_start + rem_food_pref[used];
                for plan in stripe_plans(board, desired, local_desired_start, local_col_lo, width, side == 1) {
                    let next_side = plan.exit_top as usize;
                    let cand = dp[used][side] + plan.score;
                    if cand > dp[used + width][next_side] {
                        dp[used + width][next_side] = cand;
                        prev[used + width][next_side] = Some(OuterPrev {
                            prev_cols: used,
                            prev_side: side,
                            width,
                        });
                        plans[used + width][next_side] = Some(plan);
                    }
                }
            }
        }
    }

    let mut best_side = 0usize;
    if dp[width_total][1] > dp[width_total][0] {
        best_side = 1;
    }

    let mut stripes = Vec::new();
    let mut used = width_total;
    let mut side = best_side;
    while used > 0 {
        let info = prev[used][side].expect("route decomposition failed");
        let plan = plans[used][side].clone().expect("missing stripe plan");
        debug_assert_eq!(plan.width, info.width);
        stripes.push(plan);
        used = info.prev_cols;
        side = info.prev_side;
    }
    stripes.reverse();

    let mut route = Vec::new();
    for stripe in stripes {
        route.extend(stripe.route);
    }
    route
}

fn map_local_to_global(rect: Rect, corner: Corner, h: usize, w: usize, pos: usize, board_n: usize) -> usize {
    let r = pos / w;
    let c = pos % w;
    let (gr, gc) = match corner {
        Corner::BL => (rect.top + r, rect.left + c),
        Corner::BR => (rect.top + r, rect.right - c),
        Corner::TL => (rect.bottom - r, rect.left + c),
        Corner::TR => (rect.bottom - r, rect.right - c),
    };
    debug_assert!(r < h && c < w);
    cell(board_n, gr, gc)
}

fn build_local_board(input: &Input, rect: Rect, corner: Corner) -> LocalBoard {
    let h = rect.height();
    let w = rect.width();
    let mut food = vec![0u8; h * w];
    for r in 0..h {
        for c in 0..w {
            let global = map_local_to_global(rect, corner, h, w, cell(w, r, c), input.n);
            food[cell(w, r, c)] = input.food[global];
        }
    }
    LocalBoard { h, w, food }
}

fn solve_rect_lr(input: &Input, rect: Rect, corner: Corner, desired_start: usize) -> Vec<usize> {
    let board = build_local_board(input, rect, corner);
    let local_route = solve_local_lr(&board, &input.desired, desired_start);
    local_route
        .into_iter()
        .map(|p| map_local_to_global(rect, corner, board.h, board.w, p, input.n))
        .collect()
}

fn mirror_h(corner: Corner) -> Corner {
    match corner {
        Corner::TL => Corner::TR,
        Corner::TR => Corner::TL,
        Corner::BL => Corner::BR,
        Corner::BR => Corner::BL,
    }
}

fn mirror_v(corner: Corner) -> Corner {
    match corner {
        Corner::TL => Corner::BL,
        Corner::TR => Corner::BR,
        Corner::BL => Corner::TL,
        Corner::BR => Corner::TR,
    }
}

fn map_local_corner(orientation: Corner, local_corner: Corner) -> Corner {
    match orientation {
        Corner::BL => local_corner,
        Corner::BR => mirror_h(local_corner),
        Corner::TL => mirror_v(local_corner),
        Corner::TR => mirror_v(mirror_h(local_corner)),
    }
}

fn route_value(input: &Input, route: &[usize], desired_start: usize) -> i32 {
    10_000 * count_matches_on_cells(&input.food, &input.desired, desired_start, route) - route.len() as i32
}

fn shrink_bottom(rect: Rect, corner: Corner, height: usize) -> Rect {
    match corner {
        Corner::BL | Corner::BR => Rect {
            top: rect.top,
            bottom: rect.bottom - height,
            left: rect.left,
            right: rect.right,
        },
        Corner::TL | Corner::TR => Rect {
            top: rect.top + height,
            bottom: rect.bottom,
            left: rect.left,
            right: rect.right,
        },
    }
}

fn build_bottom_strip_templates(strip_h: usize, width: usize) -> Vec<Vec<usize>> {
    let mut routes = Vec::new();

    if strip_h % 2 == 1 {
        let mut row_snake = Vec::with_capacity(strip_h * width);
        for i in 0..strip_h {
            let r = strip_h - 1 - i;
            if i % 2 == 0 {
                for c in 0..width {
                    row_snake.push(cell(width, r, c));
                }
            } else {
                for c in (0..width).rev() {
                    row_snake.push(cell(width, r, c));
                }
            }
        }
        if row_snake.last().copied() == Some(cell(width, 0, width - 1)) {
            routes.push(row_snake);
        }
    }

    if width % 2 == 1 {
        let mut col_snake = Vec::with_capacity(strip_h * width);
        for c in 0..width {
            if c % 2 == 0 {
                for dr in 0..strip_h {
                    col_snake.push(cell(width, strip_h - 1 - dr, c));
                }
            } else {
                for dr in 0..strip_h {
                    col_snake.push(cell(width, dr, c));
                }
            }
        }
        if col_snake.last().copied() == Some(cell(width, 0, width - 1)) {
            routes.push(col_snake);
        }
    }

    routes.sort();
    routes.dedup();
    routes
}

fn solve_rect_impl(
    input: &Input,
    food_pref: &[Vec<usize>],
    base_rect_foods: usize,
    base_desired_start: usize,
    rect: Rect,
    corner: Corner,
) -> (i32, Vec<usize>) {
    let current_foods = foods_in_rect(food_pref, rect);
    let desired_start = base_desired_start + (base_rect_foods - current_foods);

    let base_route = solve_rect_lr(input, rect, corner, desired_start);
    let mut best_value = route_value(input, &base_route, desired_start);
    let mut best_route = base_route;

    let board = build_local_board(input, rect, corner);
    for &strip_h in &BOTTOM_STRIP_HEIGHTS {
        if strip_h >= board.h {
            continue;
        }
        for local_route in build_bottom_strip_templates(strip_h, board.w) {
            let mut global_route = Vec::with_capacity(local_route.len());
            let row_offset = board.h - strip_h;
            for p in local_route {
                let r = p / board.w + row_offset;
                let c = p % board.w;
                let local_pos = cell(board.w, r, c);
                global_route.push(map_local_to_global(rect, corner, board.h, board.w, local_pos, input.n));
            }
            let strip_foods = count_foods_on_cells(&input.food, &global_route);
            let next_rect = shrink_bottom(rect, corner, strip_h);
            let next_corner = map_local_corner(corner, Corner::BR);
            let (future_value, future_route) =
                solve_rect_impl(input, food_pref, base_rect_foods, base_desired_start, next_rect, next_corner);
            let total_value = route_value(input, &global_route, desired_start) + future_value;
            if total_value > best_value {
                best_value = total_value;
                let mut route = global_route;
                debug_assert_eq!(desired_start + strip_foods, base_desired_start + (base_rect_foods - foods_in_rect(food_pref, next_rect)));
                route.extend(future_route);
                best_route = route;
            }
        }
    }

    (best_value, best_route)
}

fn solve_rect(input: &Input, food_pref: &[Vec<usize>], rect: Rect, corner: Corner, desired_start: usize) -> Vec<usize> {
    let base_rect_foods = foods_in_rect(food_pref, rect);
    solve_rect_impl(input, food_pref, base_rect_foods, desired_start, rect, corner).1
}

fn build_full_route(input: &Input) -> Vec<usize> {
    let prefix = prefix_route(input.n);
    let prefix_foods = count_foods_on_cells(&input.food, &prefix);
    let food_pref = build_food_prefix(input);
    let rect = Rect {
        top: 0,
        bottom: input.n - 1,
        left: 1,
        right: input.n - 1,
    };
    let mut route = prefix;
    route.extend(solve_rect(input, &food_pref, rect, Corner::BL, 5 + prefix_foods));
    route
}

fn truncate_to_last_food(route: &mut Vec<usize>, food: &[u8]) {
    let mut last = None;
    for (i, &p) in route.iter().enumerate() {
        if food[p] != 0 {
            last = Some(i);
        }
    }
    if let Some(i) = last {
        route.truncate(i + 1);
    } else {
        route.clear();
    }
}

fn route_to_dirs(n: usize, route: &[usize]) -> Vec<Dir> {
    let mut cur = cell(n, 4, 0);
    let mut dirs = Vec::with_capacity(route.len());
    for (i, &next) in route.iter().enumerate() {
        let cr = cur / n;
        let cc = cur % n;
        let nr = next / n;
        let nc = next % n;
        let dir = if nr + 1 == cr && nc == cc {
            Dir::U
        } else if nr == cr + 1 && nc == cc {
            Dir::D
        } else if nr == cr && nc + 1 == cc {
            Dir::L
        } else if nr == cr && nc == cc + 1 {
            Dir::R
        } else {
            let lo = i.saturating_sub(3);
            let hi = (i + 3).min(route.len());
            panic!("non-adjacent route step at {i}: {cur} -> {next}, window={:?}", &route[lo..hi]);
        };
        dirs.push(dir);
        cur = next;
    }
    dirs
}

fn solve(input: &Input) -> Vec<Dir> {
    let mut route = build_full_route(input);
    truncate_to_last_food(&mut route, &input.food);
    route_to_dirs(input.n, &route)
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_whitespace();

    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let c: usize = it.next().unwrap().parse().unwrap();

    let mut desired = vec![0u8; m];
    for v in &mut desired {
        *v = it.next().unwrap().parse::<u8>().unwrap();
    }

    let mut food = vec![0u8; n * n];
    for r in 0..n {
        for cc in 0..n {
            food[cell(n, r, cc)] = it.next().unwrap().parse::<u8>().unwrap();
        }
    }

    let _ = c;
    let input = Input { n, desired, food };
    let ans = solve(&input);

    let mut out = String::new();
    for dir in ans {
        out.push(dir.ch());
        out.push('\n');
    }
    print!("{out}");
}
