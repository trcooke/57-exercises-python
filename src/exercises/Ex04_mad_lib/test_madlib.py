import unittest
from exercises.Ex04_mad_lib import madlib


class TestQuotes(unittest.TestCase):

    def test_givenNounVerbAdjectiveAdverb_returnStory(self):
        self.assertEqual(madlib.story('dog', 'walk', 'blue', 'quickly'),
                         "Do you walk your blue dog quickly? That's hilarious!")
