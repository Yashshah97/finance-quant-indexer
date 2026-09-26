import unittest
from finance_quant_indexer import data_loaders
import tempfile
import os

class TestDataLoaders(unittest.TestCase):

    def test_load_time_series_data(self):
        with tempfile.NamedTemporaryFile(suffix='.csv') as f:
            f.write(b'symbol,date,value\n')
            f.write(b'A,2022-01-01,10.0\n')
            f.write(b'B,2022-01-02,20.0\n')
            f.seek(0)
            data = data_loaders.load_time_series_data(f.name)
            self.assertEqual(data['A'], [('2022-01-01', 10.0)])
            self.assertEqual(data['B'], [('2022-01-02', 20.0)])

    def test_load_risk_metrics_data(self):
        with tempfile.NamedTemporaryFile(suffix='.csv') as f:
            f.write(b'symbol,value\n')
            f.write(b'A,10.0\n')
            f.write(b'B,20.0\n')
            f.seek(0)
            data = data_loaders.load_risk_metrics_data(f.name)
            self.assertEqual(data['A'], [10.0])
            self.assertEqual(data['B'], [20.0])

if __name__ == '__main__':
    unittest.main()
