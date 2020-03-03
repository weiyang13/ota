class Statistics:
    def record(self, worker, request):
        self.numTotal = self.numTotal + 1
        waitingTime = worker.arrivalDelay(request)
        self.numFailed = self.numFailed + 1 if waitingTime > self.max else self.numFailed
        self.maxWaitingTime = max(self.maxWaitingTime, waitingTime)
        self.sumWaitingTime = self.sumWaitingTime + waitingTime

    def getRow(self):
        return [self.strategy, str(self.max), str(self.numWorkers), str(self.numRequests), str(self.duration),
                str(self.seed), str(self.sumWaitingTime / self.numTotal), str(self.maxWaitingTime), str(self.numFailed)]

    def __init__(self, max, numWorkers, numRequests, duration, seed, strategy):
        self.max = max
        self.numWorkers = numWorkers
        self.numRequests = numRequests
        self.strategy = strategy
        self.duration = duration
        self.seed = seed
        self.numTotal = 0
        self.numFailed = 0
        self.sumWaitingTime = 0.0
        self.maxWaitingTime = 0.0

    def __str__(self):
        return "Total requests: " + str(self.numTotal) + "\n" + \
               "Total failed requests: " + str(self.numFailed) + "\n" + \
               "Average waiting time: " + str(self.sumWaitingTime / self.numTotal) + "\n" + \
               "Max waiting time: " + str(self.maxWaitingTime) + "\n" + \
               "Constraint: " + str(self.max)
