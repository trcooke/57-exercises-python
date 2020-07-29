import unittest
import quotes


class TestQuotes(unittest.TestCase):

    def test_givenPlainQuote_returnQuotationOutput(self):
        self.assertEqual(quotes.quotation('Michael Barry', 'If in doubt, git checkout'),
                         "Michael Barry says, \"If in doubt, git checkout\"")

    def test_givenTextWithQuotes_returnQuotationOutput(self):
        self.assertEqual(quotes.quotation('Obi-Wan Kenobi', 'These aren\'t the droids you\'re looking for.'),
                         "Obi-Wan Kenobi says, \"These aren\'t the droids you\'re looking for.\"")
