# AGENTS.md

Guidance for AI agents and contributors working in this repository.

## Project

**Pitao Cocijo** visualizes daily and cumulative rainfall for San Pablo Villa de Mitla, Oaxaca.

- Data: `data/registro_lluvias.csv` (`Fecha,mm`); 99 rainy days, 2024-02-17 to 2026-10-09. No zero entries.
- Package: `cocijo/`; flit backend, `module = "cocijo"`, `requires-python >= 3.9`. `pyproject.toml` has no `version`; flit reads `cocijo.__version__`.
- CLI: Typer app in `cocijo/cli.py`; entrypoint `cocijo` (`[tool.flit.scripts]`). A `typer.Option()` with no default is required.
- Plots: `cocijo/plot_series.py` (matplotlib; Spanish month labels via Babel).
- Web UI: `cocijo/streamlit_app.py`; reads `data/registro_lluvias.csv` relative to CWD, so run it from the repo root.
- CI: `.github/workflows/actions.yml`, only on `develop`; builds `mvillasante/cocijo:latest` and runs the checks inside that image.

## Versioning and release policy
- `CHANGELOG.md` follows Keep a Changelog.
- No container registry publishing and no GitHub Releases; images are build-only.
### Source of truth

`cocijo/__init__.py` `__version__` is the single editable version. Flit reads it at build time. CI verifies it is valid semver, matches the release tag, and has a matching changelog section.

### Tags

- Each release gets an **immutable** `vX.Y.Z` tag. Never force-push or reuse one.
- `latest` is a **moving alias** pointing at the newest `vX.Y.Z` tag.
- A release is cut automatically when a version bump is pushed to `develop`.

### Semver rules (CLI commands are the public API)

| Change | Bump |
| --- | --- |
| Add a CLI command or an optional flag | MINOR |
| Remove/rename a command, remove a flag, make a flag required, change output format | MAJOR |
| Bug fix, data refresh, dependency patch | PATCH |
| New Streamlit view | MINOR |
| Cosmetic UI change | PATCH |

Pre-1.0: stay on `0.x` and bump **MINOR** for breaking changes. A deliberate `1.0.0` comes later, once the command set stabilizes.

### Release guardrails

- `__version__` must be valid semver.
- Create `vX.Y.Z` only if it does not already exist; never force-push it.
- Refuse to move `latest` to a lower version.
- Require a `## [X.Y.Z]` section in `CHANGELOG.md` (Keep a Changelog format).

### Explicitly out of scope

- No container registry publishing — images are build-only.
- No GitHub Releases — git tags only.
- Plot auto-commit behavior stays as-is (regenerate, commit, then tag).

## Commands

- `make check` — black (line length 100), flake8, mypy. `.flake8` ignores E501, so black alone enforces line length.
- `make tests` — `pytest --verbose`.
- `make coverage` — runs `setup` (`clean` + editable install) first, then pytest with `coverage.xml`.
- `make mutants` — also runs `setup` first.
- `make green` / `red` / `refactor` — auto-commit source and test changes; `refactor` uses `$m`, which expands empty.
- `make clean` — removes caches and `coverage.xml`, but not images that tests write under `tests/`.

## Testing quirks

- `tests/test_plot_series.py::tests_plot_yearly_rain` is collected: pytest's default `test*` prefix also matches `tests_`.
- `tests/test_streamlit_app.py` hardcodes `/workdir/cocijo/streamlit_app.py`; it only passes inside the container or at `/workdir`.
- The plot tests write `tests/lluvia_*.png`; these are untracked and survive `make clean`.
- CLI and plot tests read `tests/data/registro_lluvias_for_test.csv`.

## Public interface

The public API is the CLI commands; `cocijo/plot_series.py` functions are internal. `DOCS.md` should list the elements and does not exist yet.


## Working agreements

- Update `CHANGELOG.md` for user-visible changes.
- Commit messages use emoji prefixes; Conventional Commits are not required.
- Run `make check` and `make tests` before committing.
- `README.md` will be generated from a template; see `TODO.md`.

## Open decisions

- Changelog authoring stays manual for now; CI only checks that a version section exists.
- The semver policy should also be published in `CONTRIBUTING.md` (not yet created).

