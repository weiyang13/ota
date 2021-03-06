#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna15"
SEED=20
NUMREQ=3500
RESULTSFILE=results_syn_peakt3500_030.csv
LOGFILE=log_syn_peakt3500_030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=350
MAXW=503
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peakt

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peakt3500_025.csv
LOGFILE=log_syn_peakt3500_025.txt
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=400
MAXW=503
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peakt

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peakt3500_020.csv
LOGFILE=log_syn_peakt3500_020.txt
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=450
MAXW=503
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peakt

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


echo $SERVER done

