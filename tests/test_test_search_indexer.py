import unittest
from finance_quant_indexer import test_search_indexer

class TestTestSearchIndexer(unittest.TestCase):

    def test_import(self):
        self.assertTrue(hasattr(test_search_indexer, 'TestSearchIndexer'))

    def test_class_definition(self):
        self.assertIsInstance(test_search_indexer.TestSearchIndexer, type)

    def test_methods_defined(self):
        expected_methods = ['test_empty_index', 'test_single_match',
                            'test_multiple_matches', 'test_no_matches']
        self.assertEqual(set(dir(test_search_indexer.TestSearchIndexer)), set(expected_methods))

if __name__ == '__main__':
    unittest.main()
