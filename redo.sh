echo "Begin calculations in 'nominals' directory"
cd nominals || exit 1
sh redo.sh
cd ../
echo "End calculations in 'nominals' directory"
echo "Begin calculations in 'verbs' directory"
cd verbs || exit 1
sh redo.sh
cd ../
echo "End calculations in 'verbs' directory"
echo "Begin calculations in 'sqlite' directory"
cd sqlite || exit 1
sh redo.sh
echo "End calculations in 'sqlite' directory"

