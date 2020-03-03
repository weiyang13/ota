from scipy.spatial import distance
from dataclasses import dataclass, astuple
import random
import argparse

@dataclass(frozen=True)
class Location:
    x: float
    y: float
  
    def distance(self, loc):
        return distance.euclidean(astuple(self), astuple(loc))

@dataclass
class Worker:
    location: Location
    timeAvailable: float
    speed: float = 1.0

    def assign(self, request):
        travelTime = self.location.distance(request.start) / self.speed
        arrivalTime = max(self.timeAvailable, request.startTime) + travelTime
        self.timeAvailable = arrivalTime + request.distance() / self.speed
        self.location = request.end
    
    def arrivalDelay(self, request):
        startDelay = max(self.timeAvailable, request.startTime) - request.startTime
        travelTime = self.location.distance(request.start) / self.speed
        return startDelay + travelTime;
  
@dataclass(frozen=True)
class Request:
    start: Location
    end: Location
    startTime: float

    def distance(self):
        return self.start.distance(self.end)

def rand_location():
    return Location(random.random(), random.random())

def rand_time(period):
    return random.random() * period

def rand_requests(n, period, seed):
    random.seed(seed)
    return [Request(rand_location(), rand_location(), rand_time(period)) for _ in range(n)]

def rand_workers(n, seed):
    random.seed(seed)
    return [Worker(rand_location(), 0.0) for _ in range(n)]

def greedy_assign(workers, requests):
    def assignWorker(request):
        minDelayWorker = min(workers, key = lambda a: a.arrivalDelay(request))
        delay = minDelayWorker.arrivalDelay(request)
        minDelayWorker.assign(request)
        return delay
  
    return [assignWorker(r) for r in requests] 

def run(numTasks, duration, maxWorkers, increment, assign, seed):
    requests = rand_requests(numTasks, duration, seed)
    requests.sort(key = lambda r: r.startTime)
    for i in range(increment, maxWorkers + 1, increment):
        workers = rand_workers(i, seed)
        delays = assign(workers, requests)
        assert len(delays) == len(requests)
        # print(str(numTasks) + "," + str(duration) + "," + str(i) + "," + str(sum(delays) / len(delays)) + "," + str(max(delays)))
        print(numTasks, duration, i, sum(delays)/len(delays), max(delays))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--numTasks", help="number of tasks", required=True, type=int
    )
    parser.add_argument(
        "--duration", help="duration of tasks", required=True, type=int
    )
    parser.add_argument(
        "--maxWorkers", help="maximum number of workers", required=True, type=int
    )
    parser.add_argument(
        "--increment", help="worker increment", required=True, type=int
    )
    parser.add_argument(
        "--seed", help="random seed", required=True, type=int
    )
    args = parser.parse_args()
    run(args.numTasks, args.duration, args.maxWorkers, args.increment, greedy_assign, args.seed)

if __name__ == "__main__":
    main()
