import unittest
import quotes


class TestQuotes(unittest.TestCase):

    def test_givenPlainQuote_returnQuotationOutput(self):
        self.assertEqual(quotes.quotation('Michael Barry', 'If in doubt, git checkout'),
                         "Michael Barry says, \"If in doubt, git checkout\"")
