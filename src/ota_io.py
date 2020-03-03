import csv

from ota_lang import Worker
from ota_lang import Request
from ota_lang import Location


# Not in use
#def extractWorkers(fileName):
#    file = open(fileName, "r")
#    return yaml.load(file)

# Extract requests from csv file
def extractRequests(fileName):
    f = open(filename, 'w')
    with open(src) as csv_file:
        csv_reader = csv.reader(csv_file)
        requests = [Request(Location(float(row[1]), float(row[2])),
                            Location(float(row[3]), float(row[4])),
                            float(row[0])) for row in csv_reader]
        return requests

class Logger:
    def fine(self, string):
        if self.level == "fine":
            self.log(string)

    def info(self, string):
        if self.level == "fine" or self.level == "info":
            self.log(string)

    def warning(self, string):
        if self.level == "fine" or self.level == "info" or self.level == "warning":
            self.log(string)

    def newExp(self, numWorkers, numRequests, max, duration, strategy):
        self.info("\n" + "============================================")
        self.info("Experiment: " + str(numWorkers) + " workers, "
                        + str(numRequests) + " requests, over duration "
                        + str(duration) + " for max waiting time of "
                        + str(max) + " using strategy " + str(strategy))
        self.info("============================================")

    def log(self, string):
        self.file.write(string + "\n")

    def logAssignment(self, worker, request):
        self.fine("Assign " + str(worker) + " to " + str(request) + ". Wait= " + str(worker.arrivalDelay(request)))

    def append(self):
        self.file = open(self.filename, "a")

    def close(self):
        self.file.close()

    def __init__(self, filename, level):
        self.level = level
        self.filename = filename
        self.file = open(filename, "w")


class Results:
    def record(self, statistics):
        self.writer.writerow(statistics.getRow())

    def close(self):
        self.file.close()

    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w", newline = "")
        self.writer = csv.writer(self.file, delimiter=',')
        self.writer.writerow(["strat", "max", "num workers", "num req",
                              "dur", "seed", "avg wt", "max wt", "num failed"])
