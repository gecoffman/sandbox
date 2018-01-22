#!/bin/bash

# If this is run from INSIDE the directory with the tests it'll work nicely
export TESTSDIR=`pwd`
export MODULESDIR=`dirname $TESTSDIR`
export PYTHONPATH=${PYTHONPATH}:$TESTSDIR:$MODULESDIR

echo ---test runner---
echo PYTHONPATH is $PYTHONPATH
for testFile in ./test_*.py
do
  echo ----next test: ${testFile}----
  ./$testFile
done
