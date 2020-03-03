import random
import argparse
import csv
import json

from ota_lang import Request
from ota_lang import Location


def generate_uniform(n, t, seed, maxX, maxY):
    random.seed(seed)
    requests = [Request(i, Location(random.random() * maxX, random.random() * maxY),
                        Location(random.random() * maxX, random.random() * maxY),
                        random.random() * t) for i in range(n)]
    return requests