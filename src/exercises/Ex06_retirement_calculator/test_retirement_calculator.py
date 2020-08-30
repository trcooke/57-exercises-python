import unittest

from exercises.Ex06_retirement_calculator.retirement_calculator import RetirementCalculator


class TestRetirementCalculator(RetirementCalculator):

    def currentyear(self):
        return 2016


class TestRetirementCalculator(unittest.TestCase):
    retirementCalculator = TestRetirementCalculator()

    def test_givenCurrentAge_andRetirementAge_thenCalculateYearsLeft(self):
        self.assertEqual(self.retirementCalculator.yearsleft(25, 65), 40)

    def test_givenCurrentYear_andYearsLeft_thenCalculateRetirementYear(self):
        self.assertEqual(self.retirementCalculator.retirementyear(40), 2056)
