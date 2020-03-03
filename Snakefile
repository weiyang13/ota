rule run_greedy_test:
    input: "src/test/ota_greedy_test.py"
    shell:
        "python3.7 {input}"

rule expFinal:
    shell:
        "python3.7 src/experiment_driver.py --expType syn --minWorkers 100 --maxWorkers 100 --incrWorkers 1 --numRequests 1000 --duration 100 --minMaxD 0.3 --maxMaxD 0.4 --incrMaxD 0.1 --dimX 2 --dimY 2 --seed 20 --resultsFile results.csv --loggerFile log.txt"

rule deps:
    shell:
        "python3.7 -m pip install --user -r src/requirements.txt"
