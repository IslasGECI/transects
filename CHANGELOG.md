# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Fixed

### Changed

### Removed

## [0.4.0] - 2025-11-04

### Added
- CLI command `write-bird-records-by-group` to filter bird records by the `group` parameter.

### Fixed
- CLI commands `write-bird-densities` and `write-bird-transect-densities` can now handle subspecies names and correctly return names at the species level.

### Changed
- CLI commands `write-bird-densities` and `write-bird-transect-densities` now output the column `species_level_name` instead of `Especie`.


## [0.3.0] - 2024-01-30

### Added
- Typer cli `write-bird-transect-densities`

## [0.2.0] - 2024-01-26

### Added
- Typer cli `write-resident-bird-records`

## [0.1.0] - 2024-01-24

### Added
- Typer clis: `write-bird-densities` and `write-rodent-trapping-success`



[unreleased]: https://github.com/IslasGECI/transects/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/IslasGECI/transects/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/IslasGECI/transects/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/IslasGECI/transects/releases/tag/v0.1.0
