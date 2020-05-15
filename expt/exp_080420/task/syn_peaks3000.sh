#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcnb4"
SEED=20
NUMREQ=3000
RESULTSFILE=results_syn_peaks3000_030.csv
LOGFILE=log_syn_peaks3000_030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=150
MAXW=303
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3000_025.csv
LOGFILE=log_syn_peaks3000_025.txt
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=150
MAXW=253
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3000_020.csv
LOGFILE=log_syn_peaks3000_020.txt
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=200
MAXW=353
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


# gr no 0.25, 0.2

echo $SERVER done

