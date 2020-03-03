import argparse

from ota_strategy import getAllStrategies

from ota_io import Results
from ota_io import Logger
from ota_io import extractRequests

import ota_request_generation
import ota_worker_generation
import copy
import numpy as np

def exp(args):
    results = Results(args.resultsFile)
    logger = Logger(args.loggerFile, args.logLevel)
    if args.expType == "real":
        requests = extractRequests(args.requestsFile)
        duration = (max(requests, key = lambda r : r.time)).time
    elif args.expType == "syn":
        requests = ota_request_generation.generate_uniform(args.numRequests, args.duration,
                                                           args.seed + 1, args.dimX, args.dimY)
        duration = args.duration
    else:
        logger.warning("exp type error")
        logger.close()
        results.close()
        return

    requests.sort(key=lambda r: r.time)

    for i in range(args.minWorkers, args.maxWorkers + 1, args.incrWorkers):
        workers = ota_worker_generation.generate_uniform(i, args.seed + 2, args.dimX, args.dimY)
        for strategy in getAllStrategies():
            for maxDelay in np.arange(args.minMaxD, args.maxMaxD, args.incrMaxD):
                workersCopy = copy.deepcopy(workers)
                strategy.run(workersCopy, requests, args.seed, maxDelay, duration, logger, results)
                if strategy.isDelayInsensitive():  #strategy that does not change with different delay values
                    # break
                    pass
    logger.close()
    results.close()

def main():
    parser = argparse.ArgumentParser()
    ##
    # Arguments:
    #  For both types of experiments
    #       expType: experiment type (real or synthetic data)
    #       minWorkers, maxWorkers, incrWorkers: to determine numbers of workers to use for experiment
    #       minMaxD, maxMaxD, incrMaxD: used to set range of maximum delay parameter in experiments
    #       seed: seed used to derive seeds for random generation of data and random assignment
    #       resultsFile: filename of output results file
    #       loggerFile: filename of output logger file
    #       logLevel: intensity level of logging (fine, info, warning, off)
    #  For real dataset experiments:
    #       requests file: filename of real dataset for requests
    #  For synthetic dataset experiments:
    #       numRequests: number of requests to generate
    #       duration: time period of requests (generated or not)
    ##
    parser.add_argument(
        "--expType", help="real for real request dataset, syn for synthetic dataset", required=True, type=str
    )
    parser.add_argument(
        "--minWorkers", help="min number of workers to generate", required=True, type=int
    )
    parser.add_argument(
        "--maxWorkers", help="max number of workers to generate", required=True, type=int
    )
    parser.add_argument(
        "--incrWorkers", help="increment for number of workers to generate", required=True, type=int
    )
    parser.add_argument(
        "--numRequests", help="number of requests to generate in synthetic dataset", required=False, type=int
    )
    parser.add_argument(
        "--duration", help="time period of requests in synthetic dataset", required=False, type=float
    )
    parser.add_argument(
        "--minMaxD", help="minimum maximum delay parameter", required=True, type=float
    )
    parser.add_argument(
        "--maxMaxD", help="maximum maximum delay parameter", required=True, type=float
    )
    parser.add_argument(
        "--incrMaxD", help="increment of maximum delay parameter", required=True, type=float
    )
    parser.add_argument(
        "--dimX", help="maximum x coordinate for generating workers", required=True, type=float
    )
    parser.add_argument(
        "--dimY", help="maximum y coordinate for generating workers", required=True, type=float
    )
    parser.add_argument(
        "--seed", help="random seed", required=True, type=int
    )
    parser.add_argument(
        "--requestsFile", help="filename of input real request data", required=False, type=str
    )
    parser.add_argument(
        "--resultsFile", help="filename of output results file", required=True, type=str
    )
    parser.add_argument(
        "--loggerFile", help="filename of output log file", required=True, type=str
    )
    parser.add_argument(
        "--logLevel", help="intensity level of logging (fine, info, warning, off)", required=True, type=str
    )
    args = parser.parse_args()
    exp(args)

if __name__ == "__main__":
    main()