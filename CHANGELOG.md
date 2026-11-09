# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Fixed

### Removed

## [0.1.0] - 2026-11-09

### Added
- `cocijo` CLI entrypoint (Typer) with `write-daily-rain-plot`,
  `write-cumulative-rain-plot`, and `version` commands.
- Streamlit app (`cocijo/streamlit_app.py`) for annual and cumulative
  rainfall, plus a `streamlit` service in `docker-compose.yml` (port 8501).


### Changed
- X-axis month labels now rendered in Spanish via Babel (`Enero`, ...).
- Docker image installs the package with `make install`.
- Version bumped from 0.0.1 to 0.1.0.


[unreleased]: https://github.com/mvillasante/pitao_cocijo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/mvillasante/pitao_cocijo/releases/tag/v0.1.0
