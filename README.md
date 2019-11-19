# MWinflect
Generate declensions and conjugations based upon words in MW1899 dictionary.

The generation is done by python programs. In general terms, the process is:
* use Cologne MW digitization to derive stem-model pairs.
* For a given stem,model:
  * if the model is 'ind' (indeclineable) no inflection required. Just gather.
  * if the model is one of several nominal (noun, adjective) models, derive
    a declension table for the stem,model. The stem is MW headword.
  * if the model is one of several verbal models, derive a conjugation
    table for the stem,model.  The stem is MW headword.

When done, the results will be used to improve the underlying data of the
  [inflected forms display](http://www.sanskrit-lexicon.uni-koeln.de/work/fflexphp/web/index.php) of the Cologne Sanskrit-Lexicon web site.

The progress of this revision will be documented within issue comments.

## Reconstruction

See README-nominals.md 
README-verbs.md
README-sqlite.md
