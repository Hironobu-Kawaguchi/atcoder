// https://www.terry-u16.net/entry/ahc001-how-to
use std::time::Instant;
use std::fmt;
use rand::prelude::*;
use regex::internal::Inst;

const MAP_SIZE: u32 = 10000;

#[derive(Copy, Clone, Debug)]
struct Request {
    row: u32,
    col: u32,
    area: u32
}

impl Request {
    fn new(row: u32, col: u32, area: u32) -> Self { Self { row, col, area } }
}

#[derive(Clone, Debug)]
struct Input {
    count: usize,
    requests: Vec<Request>,
    since: Instant
}

impl Input {
    fn new(count: usize, requests: Vec<Request>) -> Self { 
        Self { 
            count, requests, since: Instant::now()
        } 
    }
}

struct Advertisement {
    row0: u32,
    col0: u32,
    row1: u32,
    col1: u32
}

impl Advertisement {
    fn new(row0: u32, col0: u32, row1: u32, col1: u32) -> Self { 
        debug_assert!(row0 < row1);
        debug_assert!(col0 < col1);
        debug_assert!(row1 < MAP_SIZE);
        debug_assert!(col1 < MAP_SIZE);
        Self { row0, col0, row1, col1 } 
    }

    fn from(row: u32, col: u32, height: u32, width: u32) -> Self { 
        Self::new(row, col, row + height, col + width)
    }

    fn intersects(&self, other: &Advertisement) -> bool {
        self.row0.max(other.row0) < self.row1.min(other.row1) && self.col0.max(other.col0) < self.col1.min(other.col1)
    }

    fn contains(&self, row: u32, col: u32) -> bool {
        self.row0 <= row && row <= self.row1 + 1 && self.col0 <= col && col <= self.col1 + 1
    }

    fn width(&self) -> u32 {
        self.row1 - self.row0
    }

    fn height(&self) -> u32 {
        self.col1 - self.col0
    }

    fn area(&self) -> u32 {
        self.width() * self.height()
    }
}

impl fmt::Display for Advertisement {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} {} {} {}", self.row0, self.col0, self.row1, self.col1)
    }
}


fn main() {
    proconio::input! {
        n: usize,
        requests: [(u32, u32, u32);n]
    };

    let input = Input::new(n, requests.iter().map(|r| Request::new(r.0, r.1, r.2)).collect());
    let results = random_expand(input);

    for ad in results {
        println!("{}", ad);
    }
}

// 時間いっぱい大きくしようとする
fn random_expand(input: Input) -> Vec<Advertisement> {
    let mut rng = rand_pcg::Pcg64Mcg::new(42);
    let mut results = input.requests.iter()
        .map(|r| Advertisement::new(r.row, r.col, r.row + 1, r.col + 1))
        .collect::<Vec<_>>();
    let mut iter = 0;
    let mut time = Instant::now();
    const TIME_LIMIT: f64 = 4.98;

    'main: while (time - input.since).as_secs_f64() / TIME_LIMIT < 1.0 {
        iter += 1;

        if iter % 100 == 0 {
            time = Instant::now();
        }

        let index = rng.gen_range(0, input.count);
        let last = &results[index];

        let (r0, c0, r1, c1) = match rng.gen_range(0, 4) {
            0 => { (last.row0.wrapping_sub(1), last.col0, last.row1, last.col1) },
            1 => { (last.row0, last.col0.wrapping_sub(1), last.row1, last.col1) },
            2 => { (last.row0, last.col0, last.row1 + 1, last.col1) },
            3 => { (last.row0, last.col0, last.row1, last.col1 + 1) },
            _ => unreachable!("arienai!")
        };

        if r0 >= MAP_SIZE || c0 >= MAP_SIZE || r1 >= MAP_SIZE || c1 >= MAP_SIZE {
            continue;
        }

        let new = Advertisement::new(r0, c0, r1, c1);

        for (i, ad) in results.iter().enumerate() {
            if i != index && ad.intersects(&new) {
                continue 'main;
            }
        }

        if new.area() <= input.requests[index].area {
            results[index] = new;
        }
    }

    eprintln!("");
    eprintln!("iter: {}", iter);
    eprintln!("score: {}", calc_score(&input, &results));
    eprintln!("");

    results
}

fn calc_score(input: &Input, ads: &Vec<Advertisement>) -> i32 {
    fn round(x: f64) -> i32 {
        (((x * 2.0) as i32) + 1) >> 1
    }
    
    let mut score = 0.0;

    for (req, ad) in input.requests.iter().zip(ads) {
        score += calc_score_each(req, ad);
    }

    round(1e9 * score / (input.count as f64))
}

fn calc_score_each(req: &Request, ad: &Advertisement) -> f64 {
    if ad.contains(req.row, req.col) {
        let area = ad.area();
        let x = 1.0 - (req.area.min(area) as f64) / (req.area.max(area) as f64);
        1.0 - x * x
    } else {
        0.0
    }
}