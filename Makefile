.DEFAULT_GOAL := help

UV ?= uv
ARGS ?=

.PHONY: help install lint format format-check test check count-sources check-links reports

help:
	@echo "install        Install Python dependencies and local helpers with uv"
	@echo "lint           Check Python code with Ruff"
	@echo "format         Format Python code with Ruff"
	@echo "format-check   Check formatting without changing files"
	@echo "test           Run offline regression tests"
	@echo "check          Run lint, formatting checks and tests"
	@echo "count-sources  Count README resource entries"
	@echo "check-links    Check README HTTP links (uses the network)"
	@echo "reports        Run both helpers"
	@echo "Pass script options with ARGS='…'"

install:
	$(UV) sync --locked

lint:
	$(UV) run --locked ruff check src tests

format:
	$(UV) run --locked ruff format src tests

format-check:
	$(UV) run --locked ruff format --check src tests

test:
	$(UV) run --locked python -m unittest discover -s tests -v

check: lint format-check test

count-sources:
	$(UV) run --locked count-sources $(ARGS)

check-links:
	$(UV) run --locked check-links $(ARGS)

reports: count-sources check-links
