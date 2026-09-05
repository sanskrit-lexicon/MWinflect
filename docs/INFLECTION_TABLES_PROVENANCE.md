# Inflection tables (calc_tables.txt) provenance — H695

_Created: 11-07-2026 · Last updated: 11-07-2026_

Answers the [Uprava/DATA_LAYERS_CENSUS.md](https://github.com/gasyoun/Uprava/blob/main/DATA_LAYERS_CENSUS.md)
§2 row for `MWinflect/nominals/pysanskritv2/tables/calc_tables.txt` (96 MB,
local-only, untracked — `.gitignore:17` excludes `calc*`): **generated,
verified reproducible.**

## Builder

- Script: [nominals/pysanskritv2/tables/decline_file.py](https://github.com/sanskrit-lexicon/MWinflect/blob/master/nominals/pysanskritv2/tables/decline_file.py)
- Input: [nominals/pysanskritv2/stems/calc_stems.txt](https://github.com/sanskrit-lexicon/MWinflect/blob/master/nominals/pysanskritv2/stems/calc_stems.txt) (288,844 rows — `<model>\t<key2>\t<refs>`)
- Invocation ([redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/master/nominals/pysanskritv2/tables/redo.sh)):
  ```
  cd nominals/pysanskritv2/tables
  python3 decline_file.py ../stems/calc_stems.txt calc_tables.txt
  ```
- Also documented at the pipeline level in [docs/GENERATION_MANUAL.md](https://github.com/sanskrit-lexicon/MWinflect/blob/master/docs/GENERATION_MANUAL.md) §Stage 2 (nominals: stems → tables).
- `decline_file.py` dispatches each row to a per-model `Decline_*` class in the
  sibling `pydecl` package (`decline.py`/`decline_f.py`); output is 4
  tab-delimited fields (`model`, `key2`, `refs`, `inflect` — a 24-field
  `:`-delimited declension table). No corrections layer runs after this stage.

## Verification

Regenerated three bounded subsets of `calc_stems.txt` with the exact
`decline_file.py` invocation above (never touching the committed 96 MB file
itself) and diffed the output against the corresponding line range of the
existing `calc_tables.txt`:

| Subset | Rows | Range | Diff result |
|---|---|---|---|
| Head | 500 | lines 1–500 | byte-identical (`diff` exit 0) |
| Mid | 301 | lines 150,000–150,300 | byte-identical (`diff` exit 0) |
| Bulk | 20,000 | lines 1–20,000 | byte-identical (`diff` exit 0) |

**Verdict: reproducible.** Environment: Python 3.14.4, Windows. `decline_file.py`
raises two `DeprecationWarning`s (`codecs.open` — stdlib deprecation, no
functional effect on output) but exits 0 and reproduces the file exactly.

## Regeneration cost

20,000 rows took ~3.0 s wall-clock (single-threaded, includes interpreter
startup). Linearly extrapolated, the full 288,844-row `calc_stems.txt` costs
well under a minute to regenerate from scratch.

## Census disposition

`MWinflect/…/tables/calc_tables.txt` (96 MB) → **generated, recipe
documented, safe to exclude from any backup/dedup pass** — it reproduces
byte-for-byte from `calc_stems.txt` via `decline_file.py` in under a minute.

_Dr. Mārcis Gasūns_
