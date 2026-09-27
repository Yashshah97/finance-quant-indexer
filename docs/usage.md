# Usage

```python
import finance_quant_indexer
```

Each module is self-contained; see docstrings for the API:

- `finance_quant_indexer.search_indexer` — Main entry point for the search indexer
- `finance_quant_indexer.inverted_index` — Implementation of the inverted index data structure
- `finance_quant_indexer.ranking` — Ranking algorithm implementation (e.g. BM25)
- `finance_quant_indexer.data_loaders` — Load and preprocess time series and risk metrics data
- `finance_quant_indexer.test_search_indexer` — Unit tests for the search indexer module
- `finance_quant_indexer.core` — main domain logic and public entry points
