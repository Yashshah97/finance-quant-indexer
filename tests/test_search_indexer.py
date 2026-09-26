import unittest
from finance_quant_indexer import search_indexer


class TestSearchIndexer(unittest.TestCase):

    def test_search_indexer_init(self):
        indexer = search_indexer.SearchIndexer()
        self.assertIsInstance(indexer.index, dict)

    def test_add_document(self):
        indexer = search_indexer.SearchIndexer()
        indexer.add_document('doc1', 'The quick brown fox jumps over the lazy dog')
        self.assertIn('quick', indexer.index)
        self.assertIn('brown', indexer.index)
        self.assertIn('fox', indexer.index)
        self.assertIn('lazy', indexer.index)

    def test_search(self):
        indexer = search_indexer.SearchIndexer()
        indexer.add_document('doc1', 'The quick brown fox jumps over the lazy dog')
        results = indexer.search('quick brown fox')
        self.assertEqual(results, ['doc1'])

if __name__ == '__main__':
    unittest.main()
