echo "remaking vlgtab2_input.txt..."
python vlgtab2_input.py vlgtab1_input.txt vlgtab2_input.txt vlgtab2_prob.txt
wc -l vlgtab2_input.txt
rm vlgtab2.sqlite
echo "remaking vlgtab2 sqlite table..."
sqlite3 vlgtab2.sqlite < vlgtab2.sql
