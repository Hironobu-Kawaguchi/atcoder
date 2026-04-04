SHELL := /bin/zsh

ROOT := $(abspath .)
OUT_DIR := $(ROOT)/out
LOG_DIR := $(ROOT)/logs
SOLVER_MANIFEST := $(ROOT)/Cargo.toml
SOLVER_BIN := $(ROOT)/target/release/main

TOOLS_DIR := $(ROOT)/tools
TOOLS_BIN_DIR := $(TOOLS_DIR)/target/release
VIS_BIN := $(TOOLS_BIN_DIR)/vis
GEN_BIN := $(TOOLS_BIN_DIR)/gen

CASE ?= 0000
LIMIT ?= 100
JOBS ?= 1
NAME ?= manual
TOOLCHAIN ?=
SOLUTION ?=

.PHONY: sync build tools-build run vis batch gen submit-check record annotate-submission rebuild-submission-log use-solution new-solution list-solutions clean

sync:
	python3 $(ROOT)/scripts/solution_manager.py sync

build: sync
	source $$HOME/.zshrc >/dev/null 2>&1 || true; cargo build -r --manifest-path $(SOLVER_MANIFEST)

tools-build:
	source $$HOME/.zshrc >/dev/null 2>&1 || true; cd $(TOOLS_DIR) && cargo build -r --bins

run: build
	mkdir -p $(OUT_DIR)
	$(SOLVER_BIN) < $(TOOLS_DIR)/in/$(CASE).txt > $(OUT_DIR)/$(CASE).txt
	wc -l $(OUT_DIR)/$(CASE).txt

vis: build tools-build
	python3 $(ROOT)/scripts/run_case.py --case $(CASE) --vis

batch: build tools-build
	mkdir -p $(LOG_DIR)
	python3 $(ROOT)/scripts/batch_eval.py --limit $(LIMIT) --jobs $(JOBS)

gen: tools-build
	cd $(TOOLS_DIR) && $(GEN_BIN) seeds.txt

submit-check:
	python3 $(ROOT)/scripts/solution_manager.py sync
	source $$HOME/.zshrc >/dev/null 2>&1 || true; python3 $(ROOT)/scripts/check_submission.py $(if $(TOOLCHAIN),--toolchain $(TOOLCHAIN),)

record: build tools-build submit-check
	source $$HOME/.zshrc >/dev/null 2>&1 || true; python3 $(ROOT)/scripts/record_experiment.py --name "$(NAME)" --limit $(LIMIT) --jobs $(JOBS) $(if $(TOOLCHAIN),--toolchain $(TOOLCHAIN),)

annotate-submission:
	python3 $(ROOT)/scripts/annotate_submission.py $(if $(EXPERIMENT),--experiment "$(EXPERIMENT)",) --result "$(RESULT)" --score $(SCORE) --exec-time-ms $(TIME_MS) $(if $(SUBMISSION_ID),--submission-id "$(SUBMISSION_ID)",)

rebuild-submission-log:
	python3 $(ROOT)/scripts/rebuild_submission_log.py

use-solution:
	python3 $(ROOT)/scripts/solution_manager.py activate "$(SOLUTION)"

new-solution:
	python3 $(ROOT)/scripts/solution_manager.py create "$(SOLUTION)" --activate

list-solutions:
	python3 $(ROOT)/scripts/solution_manager.py list

clean:
	rm -rf $(ROOT)/target
	rm -rf $(OUT_DIR)/*
	rm -rf $(LOG_DIR)/*
	rm -f $(TOOLS_DIR)/vis.html
