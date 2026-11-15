# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed
- CI regenerates `README.md` with `cocijo update-readme` and commits it
  when the summary numbers change.

### Fixed

### Removed


## [0.1.0] - 2026-11-09

### Added
- `cocijo` CLI entrypoint (Typer) with `write-daily-rain-plot`,
  `write-cumulative-rain-plot`, and `version` commands.

### Changed
- X-axis month labels in `write-daily-rain-plot` and
  `write-cumulative-rain-plot` output now render in Spanish (`Enero`, ...).

[unreleased]: https://github.com/mvillasante/pitao_cocijo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/mvillasante/pitao_cocijo/releases/tag/v0.1.0
