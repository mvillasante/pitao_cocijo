# TODO

Execution order for the release/versioning workflow and the generated README. See `AGENTS.md` for the decisions behind each step.


## 1. README templating

- [X] Add `jinja2` to `pyproject.toml` dependencies.
- [X] Create `src/README.md` from the current `README.md`.
- [X] Add a `get_five_number_summary(data)` helper (e.g. `cocijo/summary.py`) returning `min`, `q1`, `median`, `q3`, `max`, `years`.
- [X] Implement `cocijo update-readme` in `cocijo/cli.py`:
  - [X] `--data-path` (required)
  - [X] `--template-path` (default `docs/README.md.jinja`)
  - [X] `--output-path` (default `README.md`)
- [X] Add the `## Resumen de cinco números` table to the template.
- [X] Tests:
  - [X] context values and number formatting (`2`, `3.25`, `8`, `16.25`, `70`)
  - [X] rendered README contains the Spanish labels
- [X] Add to the CI an step to regenerate `README.md` and commit it with the latest numbers.

## 2. CI release workflow

- [ ] Read `__version__` on push to `develop`.
- [ ] Validate the semver format.
- [ ] Require a `## [X.Y.Z]` section in `CHANGELOG.md`.
- [ ] Create `vX.Y.Z` only if absent; never force-push it.
- [ ] Refuse to move `latest` backwards.
- [ ] Regenerate the README before the figure check; commit the generated README and plots.
- [ ] Create/move tags only after the generated commits.
- [ ] Make re-runs idempotent (existing tag means no-op).
- [ ] Remove the unused hardcoded `codecov_token` from `Makefile`; CI uses `secrets.CODECOV_TOKEN`.

## 3. Documentation

- [ ] Create `CONTRIBUTING.md` with the semver policy table.
- [ ] Add a `0.2.0` entry to `CHANGELOG.md` covering `update-readme`.
- [ ] Point `pyproject.toml` `home-page` at `https://github.com/mvillasante/pitao_cocijo` instead of the `IslasGECI/module` template URL.
- [ ] Replace the `cocijo/__init__.py` docstring "A template Python module".

## Deferred

- [ ] Decide whether the changelog is authored manually or generated (currently manual).
- [ ] Revisit a deliberate `1.0.0` once the command set stabilizes.
