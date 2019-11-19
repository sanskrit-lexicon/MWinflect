dbname="lgtab2"
dbfile="$dbname.sqlite"
smfile="../../outputs/nominals/stem_model_tab.txt"
if [ -f "$dbfile" ]; then
 rm $dbfile
fi
python3 make_input.py  $smfile temp_input.txt
echo "remaking $dbfile ..."
sqlite3 $dbfile < $dbname.sql
mv $dbfile ../db/

