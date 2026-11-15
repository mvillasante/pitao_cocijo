# TODO

Execution order for the release/versioning workflow and the generated README. See `AGENTS.md` for the decisions behind each step.


## 1. Add info to README
- [ ] Agregar el dato de la última lluvia
- [ ] Agregar el dato de la lluvia acumulada del año hasta la fecha (puede ser en la figura)
- [ ] Agregar el total de lluvia de cada año (puede ser que sea en la figura)
- [ ] Mejorar las secciones "Antes de empezar" en adelante. REAMDE debe ser primeramente informativo con respecto al estado de la precipitación. Las secciones posteriores deben mostrar información de como usar el paquete.

## 2. Technical debt
- [ ] @cocijo/cli.py should import `__version___` not all `cocijo`
- [ ] On cocijo/__init__.py import only the public interface 

## 3. CI release workflow

- [ ] Read `__version__` on push to `develop`.
- [ ] Validate the semver format.
- [ ] Require a `## [X.Y.Z]` section in `CHANGELOG.md`.
- [ ] Create `vX.Y.Z` only if absent; never force-push it.
- [ ] Refuse to move `latest` backwards.
- [ ] Regenerate the README before the figure check; commit the generated README and plots.
- [ ] Create/move tags only after the generated commits.
- [ ] Make re-runs idempotent (existing tag means no-op).
- [ ] Remove the unused hardcoded `codecov_token` from `Makefile`; CI uses `secrets.CODECOV_TOKEN`.

## 4. Documentation

- [ ] Create `CONTRIBUTING.md` with the semver policy table.
- [ ] Add a `0.2.0` entry to `CHANGELOG.md` covering `update-readme`.
- [ ] Point `pyproject.toml` `home-page` at `https://github.com/mvillasante/pitao_cocijo` instead of the `IslasGECI/module` template URL.
- [ ] Replace the `cocijo/__init__.py` docstring "A template Python module".

## Deferred

- [ ] Decide whether the changelog is authored manually or generated (currently manual).
- [ ] Revisit a deliberate `1.0.0` once the command set stabilizes.
