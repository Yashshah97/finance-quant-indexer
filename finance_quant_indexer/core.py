"""
Module: finance_quant_indexer.core
===============================

Main domain logic and public entry points for the Finance Quant Search Indexer.

Classes:
    TimeSeriesIndexer
    RiskMetricsIndexer

Functions:
    search_time_series
    search_risk_metrics
"""

class TimeSeriesIndexer:
    """Inverted index of market time series data."""

    def __init__(self):
        self.index = {}

    def add(self, symbol, data):
        """Add time series data to the index."""
        if symbol not in self.index:
            self.index[symbol] = []
        self.index[symbol].append(data)

    def search(self, query):
        """Search for time series data by query."""
        results = {}
        for symbol, data in self.index.items():
            if query in str(data).lower():
                results[symbol] = data
        return results


class RiskMetricsIndexer:
    """Inverted index of risk metrics."""

    def __init__(self):
        self.index = {}

    def add(self, symbol, data):
        """Add risk metrics to the index."""
        if symbol not in self.index:
            self.index[symbol] = []
        self.index[symbol].append(data)

    def search(self, query):
        """Search for risk metrics by query."""
        results = {}
        for symbol, data in self.index.items():
            if query in str(data).lower():
                results[symbol] = data
        return results


def search_time_series(index, query):
    """
    Search time series data using the given index.

    Args:
        index (TimeSeriesIndexer): Inverted index of market time series data.
        query: Query string to search for.

    Returns:
        dict: Time series data matching the query.
    """
    return index.search(query)


def search_risk_metrics(index, query):
    """
    Search risk metrics using the given index.

    Args:
        index (RiskMetricsIndexer): Inverted index of risk metrics.
        query: Query string to search for.

    Returns:
        dict: Risk metrics matching the query.
    """
    return index.search(query)
