# TODO

Execution order for the release/versioning workflow and the generated README. See `AGENTS.md` for the decisions behind each step.

## 1. Baseline release (v0.1.0)

- [X] Confirm `cocijo/__init__.py` is `0.1.0` and `make check` / `make tests` pass.
- [x] Create the immutable tag `v0.1.0` at the new HEAD.
- [x] Move `latest` to `v0.1.0`.
- [x] Push `develop` and the tags.

## 2. README templating

- [ ] Add `jinja2` to `pyproject.toml` dependencies.
- [ ] Create `docs/README.md.jinja` from the current `README.md`.
- [ ] Add a `build_context(data)` helper (e.g. `cocijo/readme.py`) returning `min`, `q1`, `median`, `q3`, `max`, `count`, `start`, `end`, `years`, `unit`.
- [ ] Implement `cocijo update-readme` in `cocijo/cli.py`:
  - [ ] `--data-path` (required)
  - [ ] `--template-path` (default `docs/README.md.jinja`)
  - [ ] `--output-path` (default `README.md`)
- [ ] Add the `## Resumen de cinco números` table to the template, before the plots.
- [ ] Tests:
  - [ ] context values and number formatting (`2`, `3.25`, `8`, `16.25`, `70`)
  - [ ] rendered README contains the Spanish labels
  - [ ] missing or empty CSV exits non-zero
  - [ ] missing template exits non-zero
- [ ] Regenerate `README.md` and commit it.

## 3. CI release workflow

- [ ] Read `__version__` on push to `develop`.
- [ ] Validate the semver format.
- [ ] Require a `## [X.Y.Z]` section in `CHANGELOG.md`.
- [ ] Create `vX.Y.Z` only if absent; never force-push it.
- [ ] Refuse to move `latest` backwards.
- [ ] Regenerate the README before the figure check; commit the generated README and plots.
- [ ] Create/move tags only after the generated commits.
- [ ] Make re-runs idempotent (existing tag means no-op).

## 4. Documentation

- [ ] Create `CONTRIBUTING.md` with the semver policy table.
- [ ] Add a `0.2.0` entry to `CHANGELOG.md` covering `update-readme`.

## Deferred

- [ ] Decide whether the changelog is authored manually or generated (currently manual).
- [ ] Revisit a deliberate `1.0.0` once the command set stabilizes.
