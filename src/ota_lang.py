from scipy.spatial import distance

class Location:
    def __init__(self, x, y):
        self.x = x  # float value for x-coordinate
        self.y = y  # float value for y-coordinate

    def distance(self, loc):
        return distance.euclidean([self.x, self.y], [loc.x, loc.y])

    def getJsonDict(self):
        return {
            "x" : self.x,
            "y" : self.y
        }

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Worker:
    def __init__(self, id, location, timeAvailable):
        self.id = id # integer value for id
        self.location = location # Location value for location of worker at timeAvailable
        self.timeAvailable = timeAvailable # float value for time at which worker is available
        self.speed = 1

    def assign(self, request):
        travelTime = self.location.distance(request.start) / self.speed
        arrivalTime = max(self.timeAvailable, request.time) + travelTime
        self.timeAvailable = arrivalTime + request.distance() / self.speed
        self.location = request.end

    def arrivalDelay(self, request):
        startDelay = max(self.timeAvailable, request.time) - request.time
        travelTime = self.location.distance(request.start) / self.speed
        return startDelay + travelTime

    def distanceFrom(self, worker):
        return self.location.distance(worker.location)

    def setId(self, id):
        self.id = id

    def getJsonDict(self):
        return {
            "id" : self.id,
            "velocity" : self.speed,
            "timeavailable" : self.timeAvailable,
            "lastlocation" : self.location.getJsonDict()
        }

    def __str__(self):
        return "[Worker " + str(self.id) + " at " + str(self.location) + " free at " + str(self.timeAvailable) + "]"

class Request:
    def __init__(self, id, start, end, time):
        self.id = id # integer value for id
        self.start = start # Location value for start location of request
        self.end = end # Location value for start location of request
        self.time = time # float value for time at which request is created

    def distance(self):
        return self.start.distance(self.end)

    def getJsonDict(self):
        return {
            "id" : self.id,
            "start" : self.start.getJsonDict(),
            "end" : self.end.getJsonDict(),
            "time" : self.time
        }

    def __str__(self):
        return "[Request from " + str(self.start) + " to " + str(self.end) + " created at " + str(self.time) + "]"
