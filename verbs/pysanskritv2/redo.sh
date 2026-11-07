for DIR in inputs bases models tables
 do
  echo "redo computation in directory $DIR"
  cd $DIR || exit 1
  sh redo.sh
  cd ../
 done