import unittest
import hello


class TestHello(unittest.TestCase):

    def test_givenValidName_returnsExpectedString(self):
        self.assertEqual(hello.sayhello('Tim'), 'Hello, Tim, nice to meet you!')
