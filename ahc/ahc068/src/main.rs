// Remove this once the statement-specific parser and search use these helpers.
#![allow(dead_code)]

use std::io::{self, Read};
use std::time::Instant;

const TIME_LIMIT_SEC: f64 = 1.8; // Replace after reading the statement.

struct Scanner<'a> {
    tokens: std::str::SplitWhitespace<'a>,
}

impl<'a> Scanner<'a> {
    fn new(input: &'a str) -> Self {
        Self {
            tokens: input.split_whitespace(),
        }
    }

    fn next<T: std::str::FromStr>(&mut self) -> T
    where
        T::Err: std::fmt::Debug,
    {
        self.tokens
            .next()
            .expect("unexpected end of input")
            .parse()
            .expect("failed to parse token")
    }
}

struct Timer {
    start: Instant,
    limit_sec: f64,
}

impl Timer {
    fn new(limit_sec: f64) -> Self {
        Self {
            start: Instant::now(),
            limit_sec,
        }
    }

    fn elapsed(&self) -> f64 {
        self.start.elapsed().as_secs_f64()
    }

    fn is_over(&self) -> bool {
        self.elapsed() >= self.limit_sec
    }
}

#[derive(Clone)]
struct XorShift64 {
    state: u64,
}

impl XorShift64 {
    fn new(seed: u64) -> Self {
        assert_ne!(seed, 0);
        Self { state: seed }
    }

    fn next_u64(&mut self) -> u64 {
        let mut x = self.state;
        x ^= x << 7;
        x ^= x >> 9;
        self.state = x;
        x
    }

    fn gen_range(&mut self, range: std::ops::Range<usize>) -> usize {
        assert!(range.start < range.end);
        range.start + self.next_u64() as usize % (range.end - range.start)
    }

    fn gen_f64(&mut self) -> f64 {
        (self.next_u64() >> 11) as f64 / (1_u64 << 53) as f64
    }
}

fn solve(input: &str) -> String {
    let _scanner = Scanner::new(input);
    let _timer = Timer::new(TIME_LIMIT_SEC);
    let _rng = XorShift64::new(68);

    // TODO: Parse the input and implement the first valid baseline.
    String::new()
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .expect("failed to read stdin");
    print!("{}", solve(&input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rng_is_deterministic() {
        let mut a = XorShift64::new(68);
        let mut b = XorShift64::new(68);
        for _ in 0..100 {
            assert_eq!(a.next_u64(), b.next_u64());
        }
    }

    #[test]
    fn rng_range_stays_in_bounds() {
        let mut rng = XorShift64::new(1);
        for _ in 0..1000 {
            assert!((3..11).contains(&rng.gen_range(3..11)));
            assert!((0.0..1.0).contains(&rng.gen_f64()));
        }
    }

    #[test]
    fn timer_starts_below_limit() {
        let timer = Timer::new(1.0);
        assert!(!timer.is_over());
    }
}
