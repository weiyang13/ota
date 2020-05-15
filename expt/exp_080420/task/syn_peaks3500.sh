#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcnb5"
SEED=20
NUMREQ=3500
RESULTSFILE=results_syn_peaks3500_others030.csv
LOGFILE=log_syn_peaks3500_others030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=150
MAXW=253
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3500_gr030.csv
LOGFILE=log_syn_peaks3500_gr030.txt
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=300
MAXW=353
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3500_025.csv
LOGFILE=log_syn_peaks3500_025.txt
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=200
MAXW=303
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3500_others020.csv
LOGFILE=log_syn_peaks3500_others020.txt
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=250
MAXW=303
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_syn_peaks3500_rk020.csv
LOGFILE=log_syn_peaks3500_rk020.txt
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=350
MAXW=403
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=peaks

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

#gr no 0.2, 0.25
echo $SERVER done

