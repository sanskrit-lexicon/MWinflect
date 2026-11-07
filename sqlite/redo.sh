
for dbname in lgtab1 lgtab2 vlgtab1 vlgtab2 
do
 cd $dbname || exit 1
 echo "redoing $dbname"
 sh redo_$dbname.sh
 cd ../
done