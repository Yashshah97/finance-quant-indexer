"""
Module for loading and preprocessing finance quant data.

This module contains functions to load and preprocess time series and risk metrics data.
"""

import csv
from datetime import datetime
from typing import Dict, List

def load_time_series_data(file_path: str) -> Dict[str, List[float]]:
    """
    Load time series data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing time series data.

    Returns:
        A dictionary mapping symbol names to lists of float values representing the time series.
    """
    data = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            symbol, date, value = row
            date = datetime.strptime(date, '%Y-%m-%d')
            if symbol not in data:
                data[symbol] = []
            data[symbol].append((date, float(value)))
    return {symbol: [(date, value) for date, value in values] for symbol, values in data.items()}

def load_risk_metrics_data(file_path: str) -> Dict[str, List[float]]:
    """
    Load risk metrics data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing risk metrics data.

    Returns:
        A dictionary mapping symbol names to lists of float values representing the risk metrics.
    """
    data = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            symbol, value = row
            if symbol not in data:
                data[symbol] = []
            data[symbol].append(float(value))
    return {symbol: values for symbol, values in data.items()}
