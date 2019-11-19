echo "remaking vlgtab1_input.txt..."
cat ../vlgtab1/data/*.txt > vlgtab1_input0.txt
wc -l vlgtab1_input0.txt
echo "Adjust some lines for parentheses"
python vlgtab1_parenadj.py vlgtab1_input0.txt vlgtab1_input.txt
rm vlgtab1.sqlite
echo "remaking vlgtab1 sqlite table..."
sqlite3 vlgtab1.sqlite < vlgtab1.sql
