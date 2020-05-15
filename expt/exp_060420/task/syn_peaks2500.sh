#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcnb3"
SEED=20
NUMREQ=2500
RESULTSFILE=results_syn_peaks2500_correct.csv
LOGFILE=log_syn_peaks2500_correct.txt
DURATION=8
MIND=0.2
MAXD=0.31
INCRD=0.05
MINW=150
MAXW=510
INCRW=50
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

echo $SERVER done

