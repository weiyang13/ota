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
    requests = [generate_request_peaks(i, t, maxX, maxY) for i in range(n)]
    return requests

def generate_peakt(n, t, seed, maxX, maxY):
    np.random.seed(seed)
    requests = [generate_request_peakt(i, t, maxX, maxY) for i in range(n)]
    return requests

# generate according to brooklyn temporal distribution
def generate_request_peakt(id, t, maxX, maxY):
    probt = [0.276071549, 0.522443469, 0.718191023, 0.830239622, 0.907863652, 0.951400607, 0.979075262, 1]
    return Request(id, Location(np.random.uniform(high=maxX), np.random.uniform(high=maxY)),
                   Location(np.random.uniform(high=maxX), np.random.uniform(high=maxY)),
                   generate_value(probt, t))

# generate according to brooklyn spatial distribution
def generate_request_peaks(id, t, maxX, maxY):
    probstartx = [0.100202429, 0.402496626, 0.761133603, 0.906882591, 0.979419703, 1]
    probstarty = [0.082321188, 0.472334683, 0.840755735, 0.978744939, 0.997300945, 1]
    probendx = [0.127278866, 0.310600945, 0.538825118, 0.753882512, 0.917960837, 1]
    probendy = [0.082321188, 0.472334683, 0.840755735, 0.978744939, 0.997300945, 1]
    return Request(id, Location(generate_value(probstartx, maxX), generate_value(probstarty, maxY)),
                   Location(generate_value(probendx, maxX), generate_value(probendy, maxY)),
                   np.random.uniform(high=t))

# Generate random value in range according to probability distribution specified
# For prob of size n, prob[i] refers to probability that value falls between range/n * i and range/n * (i+1)
def generate_value(prob, max):
    probsize = len(prob)
    interval = max/float(probsize)
    rand = np.random.uniform()
    for i in range(probsize):
        if rand <= prob[i]:
            return np.random.uniform(high=interval) + i * interval
    return max

def generate_request_peaks_normal(id, t, maxX, maxY):
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
