#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna6"
SEED=30
NUMREQ=600
RESULTSFILE=results_brooklyn_090615.csv
LOGFILE=log_brooklyn_090615.txt
REQUESTSFILE=./data/brooklyn_090615.csv
DURATION=8
MIND=0.2
MAXD=0.31
INCRD=0.05
MINW=150
MAXW=510
INCRW=50
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

echo $SERVER done

