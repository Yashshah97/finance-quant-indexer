import unittest
from finance_quant_indexer import inverted_index

class TestInvertedIndex(unittest.TestCase):
    def test_inverted_index_init(self):
        index = inverted_index.InvertedIndex()
        self.assertEqual(index.index, {})

    def test_add_document(self):
        index = inverted_index.InvertedIndex()
        index.add_document("doc1", ["apple"])
        self.assertIn("apple", index.index)
        self.assertEqual(len(index.index["apple"]), 1)

    def test_get_docs(self):
        index = inverted_index.InvertedIndex()
        index.add_document("doc1", ["apple"])
        result = inverted_index.get_docs("apple")
        self.assertEqual(result, ['doc1'])

if __name__ == "__main__":
    unittest.main()
