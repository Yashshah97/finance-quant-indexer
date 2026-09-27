import unittest
from finance_quant_indexer import core

class TestCore(unittest.TestCase):
    def test_time_series_indexer_add(self):
        indexer = core.TimeSeriesIndexer()
        data = "some data"
        symbol = "AAPL"
        indexer.add(symbol, data)
        self.assertIn(symbol, indexer.index)

    def test_time_series_indexer_search(self):
        indexer = core.TimeSeriesIndexer()
        data1 = "some data 1"
        data2 = "some data 2"
        symbol1 = "AAPL"
        symbol2 = "GOOG"
        indexer.add(symbol1, data1)
        indexer.add(symbol2, data2)
        query = "data"
        results = core.search_time_series(indexer, query)
        self.assertIn(symbol1, results)

    def test_risk_metrics_indexer_add(self):
        indexer = core.RiskMetricsIndexer()
        data = "some risk metrics"
        symbol = "AAPL"
        indexer.add(symbol, data)
        self.assertIn(symbol, indexer.index)

    def test_risk_metrics_indexer_search(self):
        indexer = core.RiskMetricsIndexer()
        data1 = "some risk metrics 1"
        data2 = "some risk metrics 2"
        symbol1 = "AAPL"
        symbol2 = "GOOG"
        indexer.add(symbol1, data1)
        indexer.add(symbol2, data2)
        query = "risk"
        results = core.search_risk_metrics(indexer, query)
        self.assertIn(symbol1, results)

if __name__ == '__main__':
    unittest.main()
