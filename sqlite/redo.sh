for dbname in lgtab1 lgtab2 vlgtab1 vlgtab2 
do
 cd $dbname
 sh redo_$dbname.sh
 cd ../
done