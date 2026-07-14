# GENERATION_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/GENERATION_MANUAL.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/docs/GENERATION_MANUAL.md).

## Purpose

The operator manual for the MWinflect generation pipeline: the four-stage
chain (nominals → verbs → sqlite → web), single-stage regeneration, and the
divergence map against csl-inflect (which shares and extends this skeleton).

## Audience

- An operator rebuilding the tables after an input or engine change.
- A contributor fixing engine code who must decide whether the fix also
  belongs in csl-inflect (§7's fix-here-or-there rule).
- A maintainer triaging the enhancement backlog (per-model coverage).

## Provenance

Authored 11-07-2026 by Fable 5 (`claude-fable-5`) under handoff
[H511-Fable_MWinflect_generation_pipeline_manual_10.07.26](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H511-Fable_MWinflect_generation_pipeline_manual_10.07.26.md)
(the H501–H531 per-repo manuals programme, Litpam-Indexator MANUAL.md gold
standard). Every command read from the actual `redo.sh` chain and stage
scripts; the csl-inflect comparison drawn against its
[PIPELINE_MANUAL](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md)
(H507, same programme) — none invented. The five §7 defects were observed in
the committed scripts.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Fix the `inputs bases models tables` stage-ordering bug in [verbs/pysanskritv2/redo.sh](https://github.com/sanskrit-lexicon/MWinflect/blob/main/verbs/pysanskritv2/redo.sh) (back-port csl-inflect's corrected order) | open |
| 2 | Port csl-inflect's nominal corrections layer (`corrections.py` + inventory) or document the deliberate absence | open |
| 3 | Add `lgmodel` to `sqlite/redo.sh`'s loop + ensure `sqlite/db/` exists (mkdir in the driver) | open |
| 4 | Normalize `python3` vs `python` + add `set -e` across the `redo.sh` chain | open |
| 5 | Retitle `sqlite/readme.md` (says "csl-inflect/sqlite") | open |
| 6 | Sweep the engines for remaining Python-2 residue (PR #50 pattern) | open |

## Known limitations

- `root_model.py` mode semantics beyond modes 1–2 are csl-inflect territory;
  this manual documents only what this repo runs.
- The pydecl/test2.py algorithm internals are not decoded — the scripts and
  `verbs/pysanskritv2/readme.md` remain the reference.
- Refreshing the committed MW-derived inputs (lexnorm-all2, verb_cp_orig,
  mw_genuine_roots) is upstream (MWlexnorm / csl-orig) work, out of scope.

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/README.md) — repo overview + license split (GPL-3.0 code / CC-BY-SA-4.0 data)
- Per-directory readmes: [nominals](https://github.com/sanskrit-lexicon/MWinflect/blob/main/nominals/readme.md) · [verbs](https://github.com/sanskrit-lexicon/MWinflect/blob/main/verbs/readme.md) · [sqlite](https://github.com/sanskrit-lexicon/MWinflect/blob/main/sqlite/readme.md)
- [csl-inflect docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/csl-inflect/blob/main/docs/PIPELINE_MANUAL.md) — the extension's manual (H507); §2's divergence table is the bridge
- [CLAUDE.md](https://github.com/sanskrit-lexicon/MWinflect/blob/main/CLAUDE.md) — issue taxonomy

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial version (H511) | Fable 5 (`claude-fable-5`) |

---

_Dr. Mārcis Gasūns_
