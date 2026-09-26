import unittest
from finance_quant_indexer import SearchIndexer

class TestSearchIndexer(unittest.TestCase):

    def test_empty_index(self):
        indexer = SearchIndexer()
        self.assertEqual(indexer.search(''), [])

    def test_single_match(self):
        indexer = SearchIndexer()
        indexer.add_document('AAPL', 'Apple Inc.')
        result = indexer.search('AAPL')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ('AAPL', 'Apple Inc.'))

    def test_multiple_matches(self):
        indexer = SearchIndexer()
        indexer.add_document('AAPL', 'Apple Inc.')
        indexer.add_document('GOOG', 'Alphabet Inc.')
        result = indexer.search('AP')
        self.assertEqual(len(result), 2)
        self.assertIn(('AAPL', 'Apple Inc.'), result)

    def test_no_matches(self):
        indexer = SearchIndexer()
        result = indexer.search('XYZ')
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
