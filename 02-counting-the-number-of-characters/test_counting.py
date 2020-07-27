import unittest
import counting


class TestHello(unittest.TestCase):

    def test_givenValidString_returnsExpectedCount(self):
        self.assertEqual(counting.charcount('Tim'), 3)

    def test_givenLongerString_returnsExpectedCount(self):
        self.assertEqual(counting.charcount('Situation'), 9)

    def test_givenUntrimmedString_returnsTrimmedCount(self):
        self.assertEqual(counting.charcount('   Tim   '), 3)

    def test_givenStringWithWhitespace_returnsCharacterCountOnly(self):
        self.assertEqual(counting.charcount('   Tim    Cooke  '), 8)
