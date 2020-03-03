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