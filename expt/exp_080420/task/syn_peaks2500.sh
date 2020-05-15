#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcnb3"
SEED=20
NUMREQ=2500
RESULTSFILE=results_syn_peaks2500_others030.csv
LOGFILE=log_syn_peaks2500_others030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=150
MAXW=203
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks2500_gr030.csv
LOGFILE=log_syn_peaks2500_gr030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=250
MAXW=303
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks2500_025.csv
LOGFILE=log_syn_peaks2500_025.txt
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

RESULTSFILE=results_syn_peaks2500_020.csv
LOGFILE=log_syn_peaks2500_020.txt
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=200
MAXW=303
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


# gr not 0.25, 0.20

echo $SERVER done

