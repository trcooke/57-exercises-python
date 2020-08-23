import unittest
from exercises.Ex05_simple_math import simplemath


class TestSimpleMath(unittest.TestCase):

    def test_givenValidNumbers_returnAdditionOfNumbers(self):
        self.assertEqual(simplemath.addition(10, 5), 15)

    def test_givenValidNumbers_returnDifferenceOfNumbers(self):
        self.assertEqual(simplemath.difference(10, 5), 5)

    def test_givenValidNumbers_returnProductOfNumbers(self):
        self.assertEqual(simplemath.product(10, 5), 50)

    def test_givenValidNumbers_returnQuotientOfNumbers(self):
        self.assertEqual(simplemath.quotient(10, 5), 2)

    def test_givenZeroDenominator_returnFloatInfinity(self):
        self.assertEqual(simplemath.quotient(10, 0), float('inf'))
