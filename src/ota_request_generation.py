import random
import argparse
import csv
import json
import numpy as np

from ota_lang import Request
from ota_lang import Location


def generate_uniform(n, t, seed, maxX, maxY):
    random.seed(seed)
    requests = [Request(i, Location(random.random() * maxX, random.random() * maxY),
                        Location(random.random() * maxX, random.random() * maxY),
                        random.random() * t) for i in range(n)]
    return requests

def generate_peaks(n, t, seed, maxX, maxY):
    np.random.seed(seed)
    requests = [Request(i, Location(random.random() * maxX, random.random() * maxY),
                        Location(random.random() * maxX, random.random() * maxY),
                        random.random() * t) for i in range(n)]
    requests = [generate_request_peaks(i, t, maxX, maxY) for i in range(n)]
    return requests

def generate_request_peaks(id, t, maxX, maxY):
    mean1 = [0.25 * maxX, 0.25 * maxY]
    mean2 = [0.75 * maxX, 0.75 * maxY]
    cov = [[0.0625 * maxX, 0], [0, 0.0625 * maxY]]
    rand = np.random.uniform()
    if rand < 0.6:
        return Request(id, Location(np.random.uniform(high=maxX), np.random.uniform(high=maxY)),
                       Location(np.random.uniform(high=maxX), np.random.uniform(high=maxY)),
                       np.random.uniform(high=t))
    elif rand < 0.8:
        return Request(id, normal_location_in_range(maxX, maxY, mean1, cov),
                       normal_location_in_range(maxX, maxY, mean2, cov),
                       np.random.uniform(low=t*0.2, high=t*0.4))
    else:
        return Request(id, normal_location_in_range(maxX, maxY, mean2, cov),
                       normal_location_in_range(maxX, maxY, mean1, cov),
                       np.random.uniform(low=t*0.6, high=t*0.8))


def normal_location_in_range(maxX, maxY, mean, cov):
    while(True):
        location = np.random.multivariate_normal(mean, cov)
        if location[0] >= 0 and location[0] <= maxX and location[1] >= 0 and location[1] <= maxY:
            return Location(location[0], location[1])
