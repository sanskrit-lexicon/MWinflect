
### lexnorm-all2.txt

Begin with a copy of [lexnorm-all2.txt](https://github.com/funderburkjim/MWlexnorm/blob/master/step2/lexnorm-all2.txt).

This is a csv format file (separator the tab character).
Fields:
* L = cologne record id for a record in Cologne digitization of Monier-Williams Sanskrit-English dictionary
* key1 = headword in citation form
* key2 = headword with compound-marking using '-'.
* lexnorm = inflection information in one of two forms:
  * 1: LEXID=X,STEM=Y[...]    for pronouns, cardinal numbers, etc.
  * 2: m:f#X:n   gender information, along with stem hints  


### removals from lexnorm-all2

Declensions for these records require special logic; also, the
identification of stem,models is simplified by this separation.

#### lexnorm-all2-part.txt
A list of headwords which should be declined as participles.
These have been removed from lexnorm-all2.txt.
This includes words already marked as LEXID=prap and LEXID=fap.
   How to generate the declensions and to identify the model?

#### lexnorm-all2-proncpd.txt
   4 compounds with the pronoun Bavat
   How to generate the declensions and to identify the model?

#### lexnorm-all2-inflectid.txt
   records marked with INFLECTID=...
   In these cases, the citation form in MW is a nominative dual or plural.
   How to generate the declensions and to identify the model?
   

### edit_lexnorm-all2.txt

These are the changes (shown as old/new pairs) made to the original
lexnorm-all2.txt.

### stem-model files
```
python3 stem_model.py lexnorm-all2.txt 
```
Separates  the declension information into files with names of two forms:

* X.txt for type 1 lexnorm, with X = pron, card, etc.
* ind.txt for type 2 lexnorm, for indeclineables
* X_Y.txt for type 2 lexnorm, where
  * X is gender (m,f,n) 
  * Y is model specification.  This varies.
The information 



# add pada information ('-') to cardinal stems when present in key2
cp lexnorm-all2.txt lexnorm-all2-20181004.txt
python card-stem.py lexnorm-all2-20181004.txt lexnorm-all2.txt card-stem-log.txt
# now redo stem_model
(197653, 'read from', 'lexnorm-all2-20181004.txt')
(114, 'records changed')

temporary program:
python card-merge.py card.txt m_card.txt f_card.txt n_card.txt

note: eka appears as both a cardinal and an 'mfn' in lexnorm-all2.txt
   The lgtab1b data has both declensions.
   This needs examination.

Utility program: analyze_f
 python analyze_f.py slp1 lexnorm-all2.txt analyze_f.txt 
 python analyze_f.py roman lexnorm-all2.txt analyze_f_iast.txt 

 