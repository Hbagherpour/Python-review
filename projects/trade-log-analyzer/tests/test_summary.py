#Write at least 3 tests in tests/test_summary.py: one for value_per_ticker, one for biggest_trade, and one for an edge case (for example, an empty list).

#An edge case: biggest_trade([]) should return None, and value_per_ticker([]) should return {}.

import pytest
from analyzer.summary import value_per_ticker, biggest_trade    

def test_value_per_ticker():
    trades = [
        {"ticker": "AAPL", "price": 100, "quantity": 10},
        {"ticker": "AAPL", "price": 105, "quantity": 5},
        {"ticker": "GOOGL", "price": 2000, "quantity": 2}
    ]
    expected = {"AAPL": 1525.0, "GOOGL": 4000.0}
    assert value_per_ticker(trades) == expected

def test_biggest_trade():
    trades = [
        {"ticker": "AAPL", "price": 100, "quantity": 10},
        {"ticker": "AAPL", "price": 105, "quantity": 5},
        {"ticker": "GOOGL", "price": 2000, "quantity": 2}
    ]
    expected = {"ticker": "GOOGL", "price": 2000, "quantity": 2}
    assert biggest_trade(trades) == expected

def test_value_per_ticker_empty_list():
    assert value_per_ticker([]) == {}

def test_biggest_trade_none():
    assert biggest_trade([]) is None