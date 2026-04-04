use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();

    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let c: usize = it.next().unwrap().parse().unwrap();

    let mut d = vec![0usize; m];
    for value in &mut d {
        *value = it.next().unwrap().parse().unwrap();
    }

    let mut f = vec![vec![0usize; n]; n];
    for row in &mut f {
        for value in row {
            *value = it.next().unwrap().parse().unwrap();
        }
    }

    let _ = (m, c, d, f);

    let mut ans = Vec::new();

    // Baseline: follow the official sample's vertical zigzag and eat everything.
    for _ in 4..n - 1 {
        ans.push('D');
    }
    for col in 1..n {
        ans.push('R');
        if col % 2 == 1 {
            for _ in 0..n - 1 {
                ans.push('U');
            }
        } else {
            for _ in 0..n - 1 {
                ans.push('D');
            }
        }
    }

    let mut output = String::new();
    for ch in ans {
        output.push(ch);
        output.push('\n');
    }
    print!("{output}");
}
