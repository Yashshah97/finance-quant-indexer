"""Demo for Finance Quant Search Indexer."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import finance_quant_indexer

print("Finance Quant Search Indexer", "v" + finance_quant_indexer.__version__)
print("modules:", [m for m in dir(finance_quant_indexer) if not m.startswith('_')])
