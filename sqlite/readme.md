# csl-inflect/sqlite

Scripts to construct various sqlite database files related to inflections.

redo.sh script recreates all the sqlite files.
The resulting sqlite files are in subdirectory 'db'.
The construction inputs for each sqlite file are in separate subdirectories.
Briefly, the sqlite files are:
* lgmodel.sqlite - links from the model codes to Kale Higher Sanskrit Grammar
  * model  the model code
  * descr  description of model
  * ref    reference to page in Kale, in form 'Kale N'
* lgtab1.sqlite - records from the outputs/nominals/stem_model.txt.
  NOTE: We (probably) assume that model-stem duplicates are removed.
  * model 
  * stem
  * refs  - MW sources
  * data  - inflection table (1 for model='ind', 24 for other models)
* lgtab2.sqlite 
  * key -- an inflected form 
  * model
  * stem 
* vlgtab1.sqlite - records from the outputs/verbs/stem_model.txt.
  NOTE: We (probably) assume that model-stem duplicates are removed.
  * model 
  * stem
  * refs  - MW sources
  * data  - inflection table (9)
* vlgtab2.sqlite 
  * key -- an inflected form 
  * model
  * stem 
