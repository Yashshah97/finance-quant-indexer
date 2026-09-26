# Architecture Plan

- `finance_quant_indexer/search_indexer.py` — Main entry point for the search indexer
- `finance_quant_indexer/inverted_index.py` — Implementation of the inverted index data structure
- `finance_quant_indexer/ranking.py` — Ranking algorithm implementation (e.g. BM25)
- `finance_quant_indexer/data_loaders.py` — Load and preprocess time series and risk metrics data
- `finance_quant_indexer/test_search_indexer.py` — Unit tests for the search indexer module
- `finance_quant_indexer/core.py` — main domain logic and public entry points
