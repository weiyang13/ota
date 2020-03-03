import random
import numpy as np

from ota_analysis import Statistics

class Strategy:
    def run(self, agents, requests, seed, maxDelay, duration, logger, results):
        self.agents = agents
        self.requests = requests
        self.seed = seed
        self.maxDelay = maxDelay
        self.duration = duration
        self.logger = logger
        self.results = results

        logger.newExp(len(agents), len(requests), maxDelay, duration, type(self).__name__)
        statistics = Statistics(maxDelay, len(agents), len(requests), duration, seed, type(self).__name__)

        self.initialize()
        for request in requests:
            agent = self.assign(request)
            logger.logAssignment(agent, request)
            statistics.record(agent, request)
            agent.assign(request)

        results.record(statistics)
        logger.info(str(statistics))

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
        return min(self.agents, key=lambda a: a.arrivalDelay(request))


class Ranking(Strategy):
    def initialize(self):
        random.seed(self.seed)
        random.shuffle(self.agents)  # random permutation independent of parsing for ranking
        for i in range(len(self.agents)):  # assign id for printing
            self.agents[i].setId(i)

    def assign(self, request):
        validAgents = valid(self.agents, request, self.maxDelay)
        return validAgents[0] if len(validAgents) > 0 \
            else min(self.agents, key=lambda a: a.arrivalDelay(request))

class Random(Strategy):
    def initialize(self):
        random.seed(self.seed)

    def assign(self, request):
        validAgents = valid(self.agents, request, self.maxDelay)
        return random.choice(validAgents) if len(validAgents) > 0 \
            else min(self.agents, key=lambda a: a.arrivalDelay(request))

class HighestRedundancy(Strategy):
    def initialize(self):
        self.threshold = self.maxDelay / 2
        self.adjacencyMatrix = [[1 if self.agents[i].location.distance(self.agents[j].location) < self.threshold
                                 else 0 for i in range(len(self.agents))]
                                for j in range(len(self.agents))]
        self.redundancyMatrix = [sum(self.adjacencyMatrix[i]) for i in range(len(self.agents))]
        pass

    def assign(self, request):
        validAgents = valid(self.agents, request, self.maxDelay)
        agent = max(validAgents, key=lambda a: self.redundancyMatrix[a.id]) if len(validAgents) > 0 \
            else min(self.agents, key=lambda a: a.arrivalDelay(request))
        self.updateMatrices(agent, request)
        return agent

    def updateMatrices(self, agent, request):
        id = agent.id
        newLocation = request.end
        for i in range(len(self.agents)):
            distance = self.agents[i].location.distance(newLocation)
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

def valid(agents, request, max):  # return array of agents that can fulfill request within max time constraint
    return [agent for agent in agents if agent.arrivalDelay(request) <= max]

def getAllStrategies():
    return [Greedy(), Ranking(), Random(), HighestRedundancy()]
