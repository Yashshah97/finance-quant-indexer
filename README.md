# Finance Quant Search Indexer

This project enables fast and efficient searching of financial market data by creating a comprehensive index of time series and risk metrics, allowing users to quickly retrieve relevant information from vast datasets. Built entirely in Python for ease of use and customization, this search engine leverages an inverted-index approach with ranking capabilities. With accompanying tests and documentation, it provides a robust and reliable solution for finance professionals and data analysts.

## What makes it unique

Combines market time series and risk metrics with an inverted-index search engine with ranking — a niche where few ready-made tools exist.

## Features

- **`finance_quant_indexer/search_indexer.py`** — Main entry point for the search indexer
- **`finance_quant_indexer/inverted_index.py`** — Implementation of the inverted index data structure
- **`finance_quant_indexer/ranking.py`** — Ranking algorithm implementation (e.g. BM25)
- **`finance_quant_indexer/data_loaders.py`** — Load and preprocess time series and risk metrics data
- **`finance_quant_indexer/test_search_indexer.py`** — Unit tests for the search indexer module
- **`finance_quant_indexer/core.py`** — main domain logic and public entry points

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/finance-quant-indexer.git
cd finance-quant-indexer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
finance-quant-indexer/
├── finance_quant_indexer/
│   ├── search_indexer.py
│   ├── inverted_index.py
│   ├── ranking.py
│   ├── data_loaders.py
│   ├── test_search_indexer.py
│   ├── core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **finance-quant** · Archetype: **indexer** ·
Built autonomously by JARVIS on 2026-09-26. MIT licensed.
