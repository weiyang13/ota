import random
import copy
import numpy as np

from ota_analysis import Statistics

class Strategy:
    def run(self, workers, requests, seed, maxDelay, duration, logger, results):
        self.workers = workers
        self.requests = requests
        self.seed = seed
        self.maxDelay = maxDelay
        self.duration = duration
        self.logger = logger
        self.results = results

        logger.newExp(len(workers), len(requests), maxDelay, duration, type(self).__name__)
        statistics = Statistics(maxDelay, len(workers), len(requests), duration, seed, type(self).__name__)

        self.initialize()
        for request in requests:
            worker = self.assign(request)
            logger.logAssignment(worker, request)
            statistics.record(worker, request)
            worker.assign(request)

        results.record(statistics)
        logger.info(str(statistics))

    def getAssignments(self, workers, requests, seed, maxDelay):
        self.workers = workers
        self.requests = requests
        self.seed = seed
        self.maxDelay = maxDelay

        self.initialize()

        def assignAndReturn(request):
            worker = self.assign(request)
            workerCopy = copy.copy(worker)
            worker.assign(request)
            return {
                "agent" : workerCopy.getJsonDict(),
                "request" : request.getJsonDict(),
                "arrivetime" : workerCopy.arrivalDelay(request) + request.time,
                "finish_time" : workerCopy.arrivalDelay(request) + request.time + request.distance() / workerCopy.speed
            }

        return [assignAndReturn(request) for request in requests]


    def initialize(self):
        pass

    def assign(self, request):
        pass

    def isDelayInsensitive(self):
        return False

# Assignment methods

class Greedy(Strategy):
    def isDelayInsensitive(self):
        return True

    def assign(self, request):
        return min(self.workers, key=lambda a: a.arrivalDelay(request))


class Ranking(Strategy):
    def initialize(self):
        random.seed(self.seed)
        random.shuffle(self.workers)  # random permutation independent of parsing for ranking
        for i in range(len(self.workers)):  # assign id for printing
            self.workers[i].setId(i)

    def assign(self, request):
        validWorkers = valid(self.workers, request, self.maxDelay)
        return validWorkers[0] if len(validWorkers) > 0 \
            else min(self.workers, key=lambda a: a.arrivalDelay(request))

class Random(Strategy):
    def initialize(self):
        random.seed(self.seed)

    def assign(self, request):
        validWorkers = valid(self.workers, request, self.maxDelay)
        return random.choice(validWorkers) if len(validWorkers) > 0 \
            else min(self.workers, key=lambda a: a.arrivalDelay(request))

class HighestRedundancy(Strategy):
    def initialize(self):
        self.threshold = self.maxDelay / 2
        self.adjacencyMatrix = [[1 if self.workers[i].location.distance(self.workers[j].location) < self.threshold
                                 else 0 for i in range(len(self.workers))]
                                for j in range(len(self.workers))]
        self.redundancyMatrix = [sum(self.adjacencyMatrix[i]) for i in range(len(self.workers))]
        pass

    def assign(self, request):
        validWorkers = valid(self.workers, request, self.maxDelay)
        worker = max(validWorkers, key=lambda a: self.redundancyMatrix[a.id]) if len(validWorkers) > 0 \
            else min(self.workers, key=lambda a: a.arrivalDelay(request))
        self.updateMatrices(worker, request)
        return worker

    def updateMatrices(self, worker, request):
        id = worker.id
        newLocation = request.end
        for i in range(len(self.workers)):
            distance = self.workers[i].location.distance(newLocation)
            if distance < self.threshold and self.adjacencyMatrix[i][id] == 0:
                self.adjacencyMatrix[i][id] = 1
                self.adjacencyMatrix[id][i] = 1
                self.redundancyMatrix[i] += 1
            elif distance >= self.threshold and self.adjacencyMatrix[i][id] == 1:
                self.adjacencyMatrix[i][id] = 0
                self.adjacencyMatrix[id][i] = 0
                self.redundancyMatrix[i] -= 1
        self.adjacencyMatrix[id][id] = 1
        self.redundancyMatrix[id] = sum(self.adjacencyMatrix[id])

# Utility methods

def valid(workers, request, max):  # return array of workers that can fulfill request within max time constraint
    return [worker for worker in workers if worker.arrivalDelay(request) <= max]

def getAllStrategies():
    return [Greedy(), Ranking(), Random(), HighestRedundancy()]
