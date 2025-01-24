import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk = Runner('testwalk')
        for i in range(10):
            walk.walk()
        unittest.TestCase.assertEqual(self, walk.distance,50,'wawa')
    def test_run(self):
        run = Runner('testrun')
        for i in range(10):
            run.run()
        unittest.TestCase.assertEqual(self, run.distance,100,'wawa')
    def test_challenge(self):
        first_runner = Runner('f')
        second_runner = Runner('s')
        for i in range(10):
            first_runner.walk()
            second_runner.run()
        unittest.TestCase.assertNotEqual(self, first_runner.distance, second_runner.distance, 'wawa')



class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return str([self.name, self.distance])
