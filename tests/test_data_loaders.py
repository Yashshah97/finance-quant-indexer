"""Smoke tests for data_loaders."""
import unittest

from finance_quant_indexer import data_loaders


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(data_loaders, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(data_loaders) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
