#!/bin/bash

source ./mypyenv/bin/activate

SERVER="xcna8"
SEED=20
NUMREQ=2500
RESULTSFILE=results_syn_unif2500_025.csv
LOGFILE=log_syn_unif2500_025.txt
DURATION=8
MIND=0.25
MAXD=0.251
INCRD=0.05
MINW=150
MAXW=253
INCRW=5
DIMX=0.603
DIMY=0.979
RDIST=unif

python3 src/experiment_driver.py --expType syn --rdist $RDIST --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --duration $DURATION --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning

SEED=30
NUMREQ=600
RESULTSFILE=results_brooklyn_100315_greedy030.csv
LOGFILE=log_brooklyn_100315_greedy030.txt
REQUESTSFILE=./data/brooklyn_100315.csv
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

RESULTSFILE=results_brooklyn_030515_030.csv
LOGFILE=log_brooklyn_030515_030.txt
REQUESTSFILE=./data/brooklyn_030515.csv
DURATION=8
MIND=0.3
MAXD=0.31
INCRD=0.05
MINW=300
MAXW=453
INCRW=5
DIMX=0.603
DIMY=0.979

python3 src/experiment_driver.py --expType real --minWorkers $MINW --maxWorkers $MAXW --incrWorkers $INCRW --numRequests $NUMREQ --minMaxD $MIND --maxMaxD $MAXD --incrMaxD $INCRD --requestsFile $REQUESTSFILE --dimX $DIMX --dimY $DIMY --seed $SEED --resultsFile $RESULTSFILE --loggerFile $LOGFILE --logLevel warning
