python3 stem_model.py lexnorm-all2.txt temp_stem_model_0.txt
# two types of duplicates are removed.
# First, those where the model and (un-hyphenated) stems are the same
python3 remove_dups.py temp_stem_model_0.txt temp_stem_model_1.txt  stem_model_dup.txt >  stem_model_dup_log.txt
# Second, feminines where the (un-hyphenated) stems are the same
# Note the log file which identifies these cases
python3 remove_gdups.py temp_stem_model_1.txt stem_model.txt  stem_model_gdup.txt > stem_model_gdup_log.txt
