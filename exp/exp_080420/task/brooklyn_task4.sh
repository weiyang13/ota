#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna5"
SEED=30
NUMREQ=600
RESULTSFILE=results_brooklyn_200515_025.csv
LOGFILE=log_brooklyn_200515_025.txt
REQUESTSFILE=./data/brooklyn_200515.csv
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=400
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_200515_025.csv
LOGFILE=log_brooklyn_200515_025.txt
REQUESTSFILE=./data/brooklyn_200515.csv
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=400
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_200515_hr030.csv
LOGFILE=log_brooklyn_200515_hr030.txt
REQUESTSFILE=./data/brooklyn_200515.csv
DURATION=8
MIND=0.30
MAXD=0.301
INCRD=0.05
MINW=450
MAXW=503
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

RESULTSFILE=results_brooklyn_200515_others030.csv
LOGFILE=log_brooklyn_200515_others030.txt
REQUESTSFILE=./data/brooklyn_200515.csv
DURATION=8
MIND=0.30
MAXD=0.31
INCRD=0.05
MINW=350
MAXW=403
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning


#only random at 0.25, greedy not at 0.3, none at 0.2

echo $SERVER done

