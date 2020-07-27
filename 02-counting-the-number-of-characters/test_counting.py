import unittest
import counting


class TestHello(unittest.TestCase):

    def test_givenValidString_returnsExpectedCount(self):
        self.assertEqual(counting.charcount('Tim'), 3)

    def test_givenLongerString_returnsExpectedCount(self):
        self.assertEqual(counting.charcount('Situation'), 9)
