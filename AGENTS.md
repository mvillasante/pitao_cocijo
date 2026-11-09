# AGENTS.md

Guidance for AI agents and contributors working in this repository.

## Project

**Pitao Cocijo** visualizes daily and cumulative rainfall for San Pablo Villa de Mitla, Oaxaca.

- Data: `data/registro_lluvias.csv` (`Fecha,mm`). It only lists days with rain — there are no zero entries.
- Package: `cocijo/`, built with flit (`module = "cocijo"`).
- CLI: Typer app in `cocijo/cli.py`, entrypoint `cocijo` (`[tool.flit.scripts]`).
- Plots: `cocijo/plot_series.py` (matplotlib; Spanish month labels via Babel).
- Web UI: `cocijo/streamlit_app.py` (Streamlit).
- Tests: `pytest` under `tests/`; quality gate `make check` (black, flake8, mypy).
- CI: `.github/workflows/actions.yml`, runs on every push to `develop`.

## Versioning and release policy

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
| Changes to `cocijo/plot_series.py` internals | PATCH (not public API) |

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

## README generation

`README.md` is generated output from a Jinja2 template:

```
cocijo update-readme --data-path data/registro_lluvias.csv
```

- Template: `docs/README.md.jinja` (resolved relative to the repo root).
- Output: `README.md` (committed; CI regenerates and commits changes).
- Command options: `--data-path` (required), `--template-path` (default `docs/README.md.jinja`), `--output-path` (default `README.md`).
- Context dict: `min`, `q1`, `median`, `q3`, `max`, `count`, `start`, `end`, `years`, `unit`.
- Five-number summary: daily `mm`, all years pooled; Spanish labels (`Resumen de cinco números`, `Mínimo`, `Cuartil 1 (Q1)`, `Mediana`, `Cuartil 3 (Q3)`, `Máximo`).
- Numbers: up to 2 decimals, trailing zeros trimmed (e.g. `2`, `3.25`, `8`, `16.25`, `70`).
- Placement: before the plots, under `## Resumen de cinco números`.

## Working agreements

- Do not bundle unrelated changes into release commits (for example, the pending `docker-compose.yml` edit).
- Update `CHANGELOG.md` for every user-visible change.
- Run `make check` and `make tests` before committing.
- Commit messages use emoji prefixes; Conventional Commits are not required.
- The release workflow may push generated commits, so its tagging step must be idempotent.

## Open decisions

- Changelog authoring stays manual for now; CI only checks that a version section exists.
- The semver policy should also be published in `CONTRIBUTING.md` (not yet created).
