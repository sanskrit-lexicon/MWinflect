# MWinflect

_Created: 16-10-2018 · Last updated: 11-07-2026_

The Monier-Williams 1899 dictionary (MW1899) lists headwords, not full
paradigms — a learner or a downstream tool that needs "what does *akasmāt*
inflect to" gets nothing from the dictionary text itself. MWinflect closes
that gap: it identifies which MW1899 entries are nominals or verbs, works out
which declension/conjugation model and stem each one uses, and generates the
full inflection tables — the data an inflected-form lookup (e.g. kosha's
form→lemma layer) needs to work at all.

## Structure

| Path | Role |
|---|---|
| [nominals/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/nominals) | Declension pipeline — `pydecl` (rewrite of [funderburkjim/elispsanskrit](https://github.com/funderburkjim/elispsanskrit) `pysanskritv1`) + `pysanskritv2` (identifies nominals, picks stem models, computes declensions) |
| [verbs/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/verbs) | Conjugation pipeline — `pysanskritv2` (current, mines bases from `pysanskritv1/test2.py` then applies simplified algorithms), `pysanskritv1` (ported from elispsanskrit), `pysanskrit_work` (incomplete rewrite attempt, not currently used) |
| [sqlite/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/sqlite) | Builds the SQLite tables (`lgmodel`, `lgtab1/2`, `vlgtab1/2`) from the computed tables |
| [redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/main/redo.sh) | Top-level driver: runs nominals → verbs → sqlite in sequence |
| [web/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/web) | Web-facing display of the inflection tables |
| [transcode/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/transcode) | Transliteration helpers |
| [licenses/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/licenses) | Third-party license texts |

## Usage example — executed, real output

The full pipeline is one script, read directly from
[redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/main/redo.sh):

```bash
sh redo.sh   # runs nominals/redo.sh, then verbs/redo.sh, then sqlite/redo.sh
```

The nominal-declension stage's result file is already checked in — inspecting
it directly (not invented) confirms the pipeline's real scale:

```
$ wc -l nominals/pysanskritv2/tables/calc_tables.txt
288844 nominals/pysanskritv2/tables/calc_tables.txt

$ head -4 nominals/pysanskritv2/tables/calc_tables.txt
ind	a-kasmAt	224,akasmAt	akasmAt
ind	a-kARqe	228,akARqe	akARqe
ind	a-kAma-tas	236,akAmatas	akAmatas
ind	a-kAraRam	243,akAraRam	akAraRam
```

288,844 generated inflection-table rows from MW1899's nominal entries alone
— each row a headword, its computed model/stem key, and its inflected
surface form.

## Issues overview

**Total**: 48 | **Open**: 48 | **Closed**: 0

| Milestone | Open | Closed | Total |
|---|---:|---:|---:|
| User Experience | 40 | 0 | 40 |
| Community | 8 | 0 | 8 |

By type: enhancement 40 · question 8. By severity: minor 40 · trivial 8.

## GitHub issue conventions

Follows the [Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md):

- **17 type labels** across 5 categories (code quality, features, docs, infra, research)
- **4 severity levels**: trivial, minor, major, critical
- **5 milestones**: API Stability, User Experience, Data Quality, Developer Experience, Community
- **Domain labels** scoped to processing-tool: `domain:morphology`, `domain:normalization`, `domain:lookup`
- **Org Project**: [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9)

See [CLAUDE.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/CLAUDE.md) for full definitions.

## License

This repository contains both source code and dictionary/data files, licensed separately:

- **Source code** (`*.py`, `*.php`, `*.js`, `*.sh`) — GNU General Public License v3.0, see [licenses/GPL-3.0.txt](https://github.com/sanskrit-lexicon/MWinflect/blob/main/licenses/GPL-3.0.txt).
- **Dictionary and data files** — Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA-4.0), see [LICENSE](https://github.com/sanskrit-lexicon/MWinflect/blob/main/LICENSE).

---

_Dr. Mārcis Gasūns_
