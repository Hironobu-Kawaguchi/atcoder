SHELL := /bin/zsh

ROOT := $(abspath .)
BIN := $(ROOT)/target/release/ahc068
CASE ?= sample
NAME ?= baseline
JOBS ?= 16
TIMEOUT ?= 3.0

.PHONY: build test check run snapshot evaluate clean

build:
	cargo build --release --manifest-path $(ROOT)/Cargo.toml

test:
	cargo test --manifest-path $(ROOT)/Cargo.toml

check:
	cargo fmt --manifest-path $(ROOT)/Cargo.toml -- --check
	cargo clippy --manifest-path $(ROOT)/Cargo.toml --all-targets -- -D warnings

run: build
	@test -f $(ROOT)/in/$(CASE).txt || { echo "missing: in/$(CASE).txt" >&2; exit 1; }
	@mkdir -p $(ROOT)/out
	$(BIN) < $(ROOT)/in/$(CASE).txt > $(ROOT)/out/$(CASE).txt
	@echo "wrote out/$(CASE).txt"

snapshot:
	@mkdir -p $(ROOT)/solutions
	@test ! -e $(ROOT)/solutions/$(NAME).rs || { echo "already exists: solutions/$(NAME).rs" >&2; exit 1; }
	cp $(ROOT)/src/main.rs $(ROOT)/solutions/$(NAME).rs
	@echo "saved solutions/$(NAME).rs"

# This runs every candidate on all official inputs. Under the AHC AI rules,
# report the results and stop before making any result-driven code changes.
evaluate:
	python3 $(ROOT)/scripts/evaluate_all.py --jobs $(JOBS) --timeout $(TIMEOUT)

clean:
	cargo clean --manifest-path $(ROOT)/Cargo.toml
	rm -f $(ROOT)/out/*.txt $(ROOT)/logs/*.log
