use std::env;
use std::fs;
use std::process::ExitCode;
use tools::{compute_score, parse_input, parse_output};

fn main() -> ExitCode {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("usage: {} <input> <output>", args[0]);
        return ExitCode::from(2);
    }

    let input_text = match fs::read_to_string(&args[1]) {
        Ok(value) => value,
        Err(error) => {
            eprintln!("failed to read input {}: {error}", args[1]);
            return ExitCode::from(2);
        }
    };
    let output_text = match fs::read_to_string(&args[2]) {
        Ok(value) => value,
        Err(error) => {
            eprintln!("failed to read output {}: {error}", args[2]);
            return ExitCode::from(2);
        }
    };

    let input = parse_input(&input_text);
    let output = match parse_output(&input, &output_text) {
        Ok(value) => value,
        Err(error) => {
            eprintln!("{error}");
            return ExitCode::from(1);
        }
    };
    let operations = output.out.len();
    let (score, error) = compute_score(&input, &output);
    if !error.is_empty() {
        eprintln!("{error}");
        return ExitCode::from(1);
    }

    println!("{score},{operations}");
    ExitCode::SUCCESS
}
