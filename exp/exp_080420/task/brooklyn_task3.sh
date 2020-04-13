#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna4"
SEED=30
NUMREQ=600
RESULTSFILE=results_brooklyn_030515_020.csv
LOGFILE=log_brooklyn_030515_020.txt
REQUESTSFILE=./data/brooklyn_030515.csv
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

RESULTSFILE=results_brooklyn_030515_025.csv
LOGFILE=log_brooklyn_030515_025.txt
REQUESTSFILE=./data/brooklyn_030515.csv
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=350
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_030515_030.csv
LOGFILE=log_brooklyn_030515_030.txt
REQUESTSFILE=./data/brooklyn_030515.csv
DURATION=8
MIND=0.2
MAXD=0.21
INCRD=0.05
MINW=300
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


# 0.2, rk gr bad; 0.25 gr; 0.3
echo $SERVER done

