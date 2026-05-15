# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**MWinflect** generated Sanskrit declension and conjugation tables for words in the Monier-Williams dictionary. **This repository is superseded by `csl-inflect`** (as of November 2019); active development continues there.

## Architecture

| Directory | Purpose |
|---|---|
| `verbs/` | Verb conjugation generation (pysanskrit-based) |
| `nominals/` | Nominal declension generation |
| `web/` | Web display of inflection tables |
| `transcode/` | Transcoding utilities for inflection output |
| `sqlite/` | SQLite storage for inflection tables |

### Pipeline overview

1. Extract stem-model pairs from MW1899 digitization
2. For each stem+model: generate inflected forms using pySanskrit
3. Store in SQLite; serve via web display

### Migration note

All active work has moved to the `csl-inflect` repository. This repo is archived reference material.

## Dependencies

- **Python 3**
- **pySanskrit** — Sanskrit morphology library
- **MW dictionary** source from `csl-orig`
