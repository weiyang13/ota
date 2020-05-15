#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna3"
SEED=30
NUMREQ=600
RESULTSFILE=results_brooklyn_140415_greedy030.csv
LOGFILE=log_brooklyn_140415_greedy030.txt
REQUESTSFILE=./data/brooklyn_140415.csv
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=400
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


RESULTSFILE=results_brooklyn_140415_others030.csv
LOGFILE=log_brooklyn_140415_others030.txt
REQUESTSFILE=./data/brooklyn_140415.csv
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=250
MAXW=353
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_140415_025.csv
LOGFILE=log_brooklyn_140415_025.txt
REQUESTSFILE=./data/brooklyn_140415.csv
DURATION=8
MIND=0.25
MAXD=0.26
INCRD=0.05
MINW=300
MAXW=403
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_140415_020.csv
LOGFILE=log_brooklyn_140415_020.txt
REQUESTSFILE=./data/brooklyn_140415.csv
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=450
MAXW=503
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

#ranking, greedy does not work for 0.30; greedy does not work for 0.25

echo $SERVER done

