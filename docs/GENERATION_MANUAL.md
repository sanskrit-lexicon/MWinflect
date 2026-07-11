# MWinflect Generation Pipeline Manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

The operator manual for MWinflect: generating full declension and conjugation
tables for MW1899 headwords through the four-stage chain (nominals → verbs →
sqlite → web), regenerating any single stage, and understanding how this repo
relates to its extension, [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect).
Written so a new operator runs the pipeline from this document alone.

Companion metadoc: [docs/GENERATION_MANUAL.meta.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/docs/GENERATION_MANUAL.meta.md).

---

## 1. Cheat-sheet — the whole pipeline on one screen

```bash
# full rebuild, from the repo root:
sh redo.sh                  # = nominals/redo.sh -> verbs/redo.sh -> sqlite/redo.sh

# single stages (each directory is self-contained):
cd nominals && sh redo.sh   # stems -> tables  -> pysanskritv2/tables/calc_tables.txt
cd verbs    && sh redo.sh   # inputs -> bases -> models -> tables  (⚠️ see §5 row 1
                            #   — bases runs BEFORE models but reads models' output)
cd sqlite   && sh redo.sh   # lgtab1 lgtab2 vlgtab1 vlgtab2 -> sqlite/db/*.sqlite
                            #   (lgmodel is NOT in the loop — rebuild it manually:)
cd sqlite/lgmodel && sh redo_lgmodel.sh

# web lookup app (PHP, expects ../sqlite/db/ populated):
cd web && php -S localhost:8080
```

**Dependencies outside this repo:** none at run time — the MW-derived inputs
(`lexnorm-all2.txt`, `verb_cp_orig.txt`, `mw_genuine_roots.txt`) are committed
snapshots (provenance: [funderburkjim/MWlexnorm](https://github.com/funderburkjim/MWlexnorm)
and MW1899's `cp` class-pada data from `csl-orig`). Refreshing *them* is an
upstream act, not a pipeline stage.

## 2. What this repo is — and how csl-inflect relates

MWinflect generates inflection tables **from MW1899 alone**, using the
declension/conjugation engines descended from
[funderburkjim/elispsanskrit](https://github.com/funderburkjim/elispsanskrit):
`nominals/pydecl` (declension algorithms), `verbs/pysanskritv1/test2.py` (the
complicated but working conjugator, kept only so `bases_test2.py` can mine it),
and the `pysanskritv2` simplification (bases × ending-tables).

[csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) shares this
entire skeleton and **extends** it; when you touch shared logic, check whether
the fix belongs in both. The load-bearing differences:

| Aspect | MWinflect (this repo) | csl-inflect |
|---|---|---|
| Verb tense coverage | `root_model.py` modes 1–2 (present-system core) | per-tense mode-5 batteries: aor/prf/fut/ben/inj/cnd/ppf… |
| Huet data | none | `huetdata/` import + 678-entry root-spelling crosswalk feeding `manual/` tables |
| Nominal corrections layer | none — `decline_file.py` output is final | `corrections.py` + `correction_inventory.txt` after declension |
| Verb stage order in `redo.sh` | `inputs bases models tables` (⚠️ defect, §5) | `inputs models bases tables` (fixed) |
| sqlite driver | loop omits `lgmodel` | loop includes `lgmodel` |
| Operator manual | this document | [csl-inflect docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md) |

License split (root [README](https://github.com/sanskrit-lexicon/MWinflect/blob/main/README.md)):
code GPL-3.0, data CC-BY-SA-4.0.

## 3. Data-flow diagram

```
MW1899 (csl-orig)  — upstream, snapshotted into committed inputs
│
├─ nominals/pysanskritv2/inputs/lexnorm-all2.txt   (MWlexnorm step2 export:
│      L-number · headword · compound-marked form · gender/stem hints)
│    │  stems/redo.sh: stems.py → remove_dups.py → remove_gdups.py
│    │                 → stem_model_diff.py   (each dedup writes a *_log.txt)
│    ▼
│  stems/calc_stems.txt
│    │  tables/redo.sh: decline_file.py       (pydecl algorithms)
│    ▼
│  nominals/pysanskritv2/tables/calc_tables.txt      (model·stem·refs·24 forms)
│
├─ verbs/pysanskritv2/inputs/verb_cp_orig.txt  (MW cp class-pada data)
│    │  inputs/redo.sh: genuine_filter.py (vs mw_genuine_roots.txt) → clean.py
│    ▼
│  inputs/verb_cp.txt   (root : MW Lrefs : class-voice list, e.g. BU:151456:1a,1m)
│    │  models/redo.sh: root_model.py modes 1,2 → cat → calc_models.txt
│    │  bases/redo.sh:  bases_test2.py (mines pysanskritv1/test2.py)
│    │  tables/redo.sh: conjugate_from_bases.py
│    ▼
│  verbs/pysanskritv2/tables/calc_tables.txt         (model·stem·refs·9 forms)
│
▼  sqlite/redo.sh  (each: sqlite3 <name>.sqlite < <name>.sql, tab .import,
│                   prints count(*) — watch it — then mv into sqlite/db/)
sqlite/db/{lgtab1,lgtab2,vlgtab1,vlgtab2}.sqlite  + lgmodel.sqlite (manual)
│      *tab2 = form → (model, stem) inversion built by each dir's make_input.py
▼
web/  (PHP: index.php → getWord.php → dal.php, path hardcoded ../sqlite/db)
      lookup: inflected form → *tab2 → full table from *tab1 → Kale ref via lgmodel
```

Transliteration support lives in two places: root
[transcode/](https://github.com/sanskrit-lexicon/MWinflect/tree/main/transcode)
(`transcoder.py` + XML maps — imported by the `nominals/pysanskritv2/analysis`
scripts) and `web/utilities/transcoder` (the PHP side used by `getWord.php`).

## 4. Step-by-step operator walkthrough

### 4.1 Nominals

```bash
cd nominals && sh redo.sh
```

Stage 1 (`stems/`): `stems.py` derives stem+model candidates from
`lexnorm-all2.txt`; two dedup passes (same model + un-hyphenated stem;
feminine same-stem) each leave an audit `*_log.txt`; `stem_model_diff.py`
splits problem cases into `stems_problem.txt` → **`calc_stems.txt`**.
Stage 2 (`tables/`): `decline_file.py` declines every stem per its model →
**`calc_tables.txt`**. There is no corrections layer here — a wrong declension
means fixing the model assignment or the pydecl algorithm (or porting
csl-inflect's corrections mechanism, backlog item).

### 4.2 Verbs

```bash
cd verbs && sh redo.sh    # after reading §5 row 1
```

1. **`inputs/`** — `genuine_filter.py` keeps roots present in
   `mw_genuine_roots.txt`, `clean.py` normalizes → **`verb_cp.txt`**.
   (`clean.py` was Python-3-fixed in
   [PR #50](https://github.com/sanskrit-lexicon/MWinflect/pull/50) — the
   engines are py2-era code progressively ported; expect more such fixes.)
2. **`models/`** — `root_model.py` modes `1` and `2` over `verb_cp.txt` →
   `calc_models_1.txt` + `calc_models_2.txt` → `cat` → **`calc_models.txt`**.
3. **`bases/`** — `bases_test2.py` mines conjugation bases out of
   `pysanskritv1/test2.py` for each model → **`calc_bases.txt`**.
4. **`tables/`** — `conjugate_from_bases.py` combines bases with ending
   tables → **`calc_tables.txt`**.

**The driver runs these as `inputs bases models tables`** — see §5 row 1 for
why that order is wrong and how to run correctly
(`inputs → models → bases → tables`, each directory's `redo.sh` by hand, or
fix the driver).

`pysanskrit_work/` is an unfinished rewrite used by nothing — don't build on
it. `pysanskritv1/` exists only to feed `bases_test2.py`.

### 4.3 SQLite load

```bash
cd sqlite && sh redo.sh          # lgtab1 lgtab2 vlgtab1 vlgtab2
cd lgmodel && sh redo_lgmodel.sh # lgmodel — NOT in the driver loop
```

Per database: drop old file, `sqlite3 <name>.sqlite < <name>.sql`
(tab-separated `.import` of the source `calc_tables.txt`; the printed
`count(*)` is the stage's only self-check), `mv` into `sqlite/db/`. The
`*tab2` databases first run their `make_input.py` to invert the table data
into a form → (model, stem) index. `sqlite/db/` is not a committed directory —
create it on a fresh clone before the first load. Sources per
[sqlite/readme.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/sqlite/readme.md)
(NB its title says "csl-inflect/sqlite" — shared-ancestry artifact, this is
MWinflect's copy).

### 4.4 Web lookup

`web/` is the same no-framework PHP app as csl-inflect's: `index.php` (UI) →
`getWord.php` (`?word=` in any transliteration → SLP1 via
`utilities/transcoder`; also CLI-runnable: `php getWord.php rAmaH`) →
`dal.php` (hardcoded `../sqlite/db/{name}.sqlite`). `prephelp.py` regenerates
`lgmodel_input.html` from `lgmodel_input.txt` (the model → Kale
*Higher Sanskrit Grammar* reference table). Local run:
`cd web && php -S localhost:8080`.

## 5. Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| Fresh-clone `verbs/redo.sh` fails in `bases/` (or silently uses stale data) | **Driver ordering defect**: [verbs/pysanskritv2/redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/main/verbs/pysanskritv2/redo.sh) loops `inputs bases models tables`, but `bases_test2.py` reads `../models/calc_models.txt`, produced by the *models* stage. Runs "work" only because a committed/stale `calc_models.txt` is lying around | Run stages by hand in `inputs → models → bases → tables` order, or fix the loop (csl-inflect's copy already has the fixed order) |
| `clean.py` step does nothing / `python: command not found` | [inputs/redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/main/verbs/pysanskritv2/inputs/redo.sh) mixes `python3` (line 1) and bare `python` (line 2), and there is no `set -e` — the failure scrolls past | Run `python3 clean.py verb_cp_orig_1.txt verb_cp.txt` yourself; or normalize the script |
| `clean.py` SyntaxError on tuple-parameter lambda | Pre-[PR #50](https://github.com/sanskrit-lexicon/MWinflect/pull/50) checkout (py2-era syntax) | Pull master; more py2 residue may surface in the less-travelled engines — port as found |
| `sqlite/redo.sh` ran green but `lgmodel.sqlite` is stale/missing | `lgmodel` is not in the driver loop | `cd sqlite/lgmodel && sh redo_lgmodel.sh` (§4.3) |
| `mv: cannot move ... ../db/` during sqlite load | `sqlite/db/` doesn't exist on a fresh clone | `mkdir sqlite/db` once |
| A `count(*)` printed during the load is 0/tiny | Upstream `calc_tables.txt` missing or truncated — `.import` loads whatever is there | Rebuild the owning chain (§4.1/§4.2), re-load |
| Web app renders but lookups return nothing | `sqlite/db/*.sqlite` absent (never built here / fresh clone) | Run §4.3; `dal.php`'s `../sqlite/db` path is hardcoded |
| Hand-edit to a `calc_*` file vanished | `calc_` = recomputed by contract; `models/redo.sh`-style stages regenerate them wholesale | Change the stage's *inputs* or scripts, never `calc_` outputs |
| Wrong declension for an irregular stem | No corrections layer in this repo (§4.1) | Fix model assignment/algorithm, or port csl-inflect's `corrections.py` mechanism (backlog #2) |
| `sh` scripts misbehave under PowerShell | They are Bourne-shell scripts | Run from Git Bash |

## 6. Glossary

| Term | Meaning |
|---|---|
| MW1899 | Monier-Williams Sanskrit-English Dictionary, the sole headword source (via csl-orig) |
| lexnorm | MWlexnorm's per-headword inflection hints (gender/stem info; `LEXID=` for pronouns/numerals) |
| cp / class-voice | MW's conjugation-class + pada data (`1a,1m` = class 1 active + middle) |
| model | Paradigm code naming how a stem inflects; `lgmodel` maps each to a Kale page ref |
| Kale | M. R. Kale, *A Higher Sanskrit Grammar* — the cited reference grammar |
| base | The verb-chain intermediate a tense's ending table attaches to (mined from `test2.py`) |
| `calc_*` | "Computed — never hand-edit"; any stage may delete and rewrite them |
| 24-form / 9-form table | Nominals: 8 cases × 3 numbers; verbs: 3 persons × 3 numbers |
| `*tab1` / `*tab2` | Table store vs inverted form→(model,stem) index (`lg` nominal, `vlg` verb) |
| SLP1 | The ASCII transliteration all data files use (`BU` = bhū) |
| elispsanskrit | funderburkjim's Emacs-Lisp-era Sanskrit engine, ancestor of pydecl + pysanskritv1 |

## 7. Maintainer appendix

- **Invariants:** committed MW-derived inputs are snapshots (refreshing them
  is upstream work); every computed file is `calc_*` and disposable; the
  sqlite `count(*)` outputs are the only load-time self-check; `web/` couples
  to the pipeline solely through `../sqlite/db`.
- **Observed defects** (found 11-07-2026 while writing this manual — csl-inflect
  comparisons per its [PIPELINE_MANUAL](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md)):
  1. the `inputs bases models tables` ordering bug in
     `verbs/pysanskritv2/redo.sh` (§5 row 1) — already fixed in csl-inflect's
     copy, never back-ported;
  2. `python3`/`python` mix in `verbs/pysanskritv2/inputs/redo.sh` with no
     `set -e`;
  3. `lgmodel` missing from `sqlite/redo.sh`'s loop;
  4. `sqlite/readme.md` titled "csl-inflect/sqlite" (wrong repo name —
     shared-ancestry copy);
  5. `sqlite/db/` target directory not present on a fresh clone.
- **Fix-here-or-there rule:** engine fixes (pydecl, test2.py mining,
  root_model modes 1–2, the analysis scripts) likely apply to csl-inflect
  too — cross-check its copy in the same pass; csl-inflect-only layers
  (huetdata crosswalk, corrections, per-tense manual tables) do NOT exist
  here and should not be "synced back" without a decision.
- **Ancestry:** `pydecl` and `pysanskritv1` descend from
  [funderburkjim/elispsanskrit](https://github.com/funderburkjim/elispsanskrit);
  `pysanskrit_work/` is an abandoned rewrite (unused).
- **Issue taxonomy:** processing-tool category — see
  [CLAUDE.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/CLAUDE.md).
  The 48 open issues (40 enhancement / 8 question, snapshot 2026-05-29) are
  largely per-model coverage requests — exactly the work §4's stage map
  routes.

---

_Dr. Mārcis Gasūns_
