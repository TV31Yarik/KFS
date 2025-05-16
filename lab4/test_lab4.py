import unittest
from lab4 import simulate_lorenz

class TestLorenzModel(unittest.TestCase):
    def test_same_initial_conditions(self):
        t1, sol1 = simulate_lorenz([1.0, 1.0, 1.0])
        t2, sol2 = simulate_lorenz([1.0, 1.0, 1.0])
        diff = (sol1 - sol2).max()
        self.assertAlmostEqual(diff, 0, places=5)

    def test_small_difference(self):
        t1, sol1 = simulate_lorenz([1.0, 1.0, 1.0])
        t2, sol2 = simulate_lorenz([1.001, 1.0, 1.0])
        self.assertGreater(abs(sol1[0][-1] - sol2[0][-1]), 1.0)

unittest.main()