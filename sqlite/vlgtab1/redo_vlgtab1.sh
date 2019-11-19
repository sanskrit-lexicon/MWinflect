dbname="vlgtab1"
dbfile="$dbname.sqlite"
smfile="../../outputs/verbs/stem_model_tab.txt"
if [ -f "$dbfile" ]; then
 rm $dbfile
fi
echo "remaking $dbfile ..."
sqlite3 $dbfile < $dbname.sql
mv $dbfile ../db/

