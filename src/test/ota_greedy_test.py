import unittest

from ota_greedy import greedy_assign
from ota_greedy import Worker
from ota_greedy import Request
from ota_greedy import Location

class TestGreedy(unittest.TestCase):
    def test_assignment_idle(self):
        workers = [Worker(Location(0, 0), 0),
                Worker(Location(1, 0), 0)]
        requests = [Request(Location(0.4, 0), Location(0.7, 0.4), 0)]
        greedy_assign(workers, requests)
        self.assertEqual(workers[0].timeAvailable, 0.9)
        self.assertEqual(workers[1].timeAvailable, 0)
        self.assertEqual(workers[0].location, Location(0.7, 0.4))
        self.assertEqual(workers[1].location, Location(1, 0))

    def test_assignment_busy_idle(self):
        workers = [Worker(Location(0, 0), 0),
                Worker(Location(1, 0), 0)]
        requests = [Request(Location(0.4, 0), Location(0.9, 0), 0),
                    Request(Location(0.9, 0), Location(0.5, 0), 0.7)]
        greedy_assign(workers, requests)
        self.assertEqual(workers[0].timeAvailable, 0.9)
        self.assertEqual(workers[1].timeAvailable, 1.2)
        self.assertEqual(workers[0].location, Location(0.9, 0))
        self.assertEqual(workers[1].location, Location(0.5, 0))

    def test_assignment_busy_idle_2(self):
        workers = [Worker(Location(0, 0), 0),
                Worker(Location(1, 0), 0)]
        requests = [Request(Location(0.1, 0), Location(0.4, 0), 0),
                    Request(Location(0.3, 0), Location(0.6, 0), 0.2)]
        greedy_assign(workers, requests)
        self.assertEqual(workers[0].timeAvailable, 0.8)
        self.assertEqual(workers[1].timeAvailable, 0)
        self.assertEqual(workers[0].location, Location(0.6, 0))
        self.assertEqual(workers[1].location, Location(1, 0))

    def test_assignment_busy_busy(self):
        workers = [Worker(Location(0.1, 0.1), 3),
                Worker(Location(0.8, 0.8), 4)]
        requests = [Request(Location(0.49, 0.9), Location(0.5, 0.9), 2),
                    Request(Location(0.5, 1.0), Location(0.5, 0.5), 3),
                    Request(Location(0.8, 1.0), Location(0.4, 0.7), 3.5)]
        greedy_assign(workers, requests)
        self.assertEqual(workers[0].timeAvailable, 4.5)
        self.assertEqual(workers[1].timeAvailable, 4.7)
        self.assertEqual(workers[0].location, Location(0.5, 0.5))
        self.assertEqual(workers[1].location, Location(0.4, 0.7))

if __name__ == "__main__":
    unittest.main()