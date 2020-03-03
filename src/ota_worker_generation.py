import random
import argparse
import json

from ota_lang import Worker
from ota_lang import Location


def generate_uniform(n, seed, maxX, maxY):
    random.seed(seed)
    workers = [Worker(i, Location(random.random() * maxX, random.random() * maxY),
                    0.0) for i in range(n)]
    return workers

#def generate_scaled_uniform(n, seed, filename):
#    random.seed(seed)
#    f = open(filename, 'w')
#    # magic numbers used
#    workers = [Worker(0, Location(random.random()*2.29 + 1.31, random.random()*2.13 + 0.38),
#                    0.0) for _ in range(n)]
#    json.dump(workers, f)