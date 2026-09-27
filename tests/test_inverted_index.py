"""Smoke tests for inverted_index."""
import unittest

from finance_quant_indexer import inverted_index


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(inverted_index, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(inverted_index) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
