# Maintenance helpers

The [main README](../README.md) is the open-data directory. This small Python
package contains its maintenance scripts.

## Setup and commands

Use Python 3.13+ and [uv](https://docs.astral.sh/uv/). Run these commands from the
repository root:

```sh
make install       # Install dependencies and the local package in .venv
make count-sources # Write count_sources.md and print the counts
make check-links   # Write link-check-report.md (requires network access)
make reports       # Run both helpers
make check         # Lint, check formatting and run offline tests
make format        # Format Python files
make help          # List all targets
```

- `awesome_ogd_switzerland/count_sources.py` counts top-level resource bullets
  with external links, grouped by Markdown heading. Secondary links, nested
  bullets and fenced examples do not add entries. Separate cross-references
  count again; these are not counts of unique datasets or publishers.
- `awesome_ogd_switzerland/link_checker.py` checks unique HTTP(S) URLs using HEAD
  with a streamed GET fallback. It reports reachable, likely broken (404/410)
  and inconclusive results. It does not validate fragments, content or licenses.
  The command exits with status 1 for likely broken links or a missing input;
  inconclusive checks alone do not cause failure.

Both helpers default to `README.md` in the current working directory. Reports
are written there too and are ignored by Git. Override the input or output with:

```sh
uv run --locked count-sources README.md --output /tmp/counts.md
uv run --locked check-links README.md --output /tmp/links.md
make check-links ARGS='README.md --output /tmp/links.md'
```

Use `--help` with either command for options. `make lint`, `make format-check`
and `make test` also work separately. The tests make no network requests.

## Maintenance skill

The repository includes the
[`maintain-swiss-ogd` skill](../.agents/skills/maintain-swiss-ogd/SKILL.md)
for agent-assisted refreshes and targeted audits. It covers discovering and
verifying resources, checking reuse terms, correcting entries and recording
findings. Ask an agent with the skill available to “Use maintain-swiss-ogd to
audit the directory” or to review a specific section. The scripts support that
workflow; HTTP results still need editorial review.
