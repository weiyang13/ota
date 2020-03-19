import argparse

from ota_io import extractRequests
from ota_io import JsonAssignmentWriter

from ota_strategy import getAllStrategies

import ota_request_generation
import ota_worker_generation

def run(args):
    jsonAssignmentWriter = JsonAssignmentWriter(args.assignmentsFile)
    if args.expType == "real":
        requests = extractRequests(args.requestsFile)
        duration = (max(requests, key = lambda r : r.time)).time
    elif args.expType == "syn":
        if args.rdist == "unif":
            requests = ota_request_generation.generate_uniform(args.numRequests, args.duration,
                                                           args.seed + 1, args.dimX, args.dimY)
        elif args.rdist == "peaks":
            requests = ota_request_generation.generate_peaks(args.numRequests, args.duration,
                                                           args.seed + 1, args.dimX, args.dimY)
        duration = args.duration
    else:
        print("invalid expType")
        return

    requests.sort(key=lambda r: r.time)
    workers = ota_worker_generation.generate_uniform(args.numWorkers, args.seed + 2, args.dimX, args.dimY)
    for strategy in getAllStrategies():
        if type(strategy).__name__ == args.strategy:
            assignments = strategy.getAssignments(workers, requests, args.seed, args.maxD)
            jsonAssignmentWriter.write(assignments)

def main():
    parser = argparse.ArgumentParser()
    ##
    # Arguments:
    #  For both types of experiments
    #       expType: experiment type (real or synthetic data)
    #       numWorkers: to determine numbers of workers to use for run
    #       maxD: used to set maximum delay parameter in run
    #       seed: seed used to derive seeds for random generation of data and random assignment
    #       assignmentsFile: filename of output results file
    #       dimX, dimY: to set range of locations workers are generated in
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
        "--strategy", help="Greedy or Random or Ranking or HighestRedundancy", required=True, type=str
    )
    parser.add_argument(
        "--numWorkers", help="number of workers to generate", required=True, type=int
    )
    parser.add_argument(
        "--numRequests", help="number of requests to generate in synthetic dataset", required=False, type=int
    )
    parser.add_argument(
        "--duration", help="time period of requests in synthetic dataset", required=False, type=float
    )
    parser.add_argument(
        "--maxD", help="maximum delay parameter", required=True, type=float
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
        "--assignmentsFile", help="filename of output assignments file", required=True, type=str
    )
    parser.add_argument(
        "--rdist", help="request distribution (peaks, unif)", required=False, type=str
    )
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()