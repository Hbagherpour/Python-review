#Write tests for your Portfolio Tracker. In projects/portfolio-tracker/,
#ctest_portfolio.py:
#test_portfolio.py — at minimum:
#test_total_value() — add 2-3 stocks, verify total_value() sums correctly
#test_best_performer() — verify it returns the correct highest-value stock
#test_len() — verify len(portfolio) matches number of holdings added
#test_remove_stock_not_found() — verify removing a nonexistent ticker doesn't crash

from stock import Stock
from portfolio import Portfolio

def test_total_value():
    portfolio = Portfolio()
    portfolio.add_stock(Stock("AAPL", 10, 150))  # position value = 1500
    portfolio.add_stock(Stock("GOOGL", 5, 300))   # position value = 1500
    portfolio.add_stock(Stock("MSFT", 8, 200))    # position value = 1600
    assert portfolio.total_value() == 4600

def test_best_performer():
    portfolio = Portfolio()
    portfolio.add_stock(Stock("AAPL", 10, 150))  # position value = 1500
    portfolio.add_stock(Stock("GOOGL", 5, 300))   # position value = 1500
    portfolio.add_stock(Stock("MSFT", 8, 200))    # position value = 1600
    best_stock = portfolio.best_performer()
    assert best_stock.ticker == "MSFT"
    assert best_stock.position_value() == 1600

def test_len():
    portfolio = Portfolio()
    portfolio.add_stock(Stock("AAPL", 10, 150))
    portfolio.add_stock(Stock("GOOGL", 5, 300))
    assert len(portfolio) == 3, "Portfolio length should match number of holdings added"

def test_remove_stock_not_found():
    portfolio = Portfolio()
    portfolio.add_stock(Stock("AAPL", 10, 150))
    portfolio.remove_stock(Stock("GOOGL", 5, 300))  # GOOGL is not in the portfolio
    assert len(portfolio) == 1  # Ensure the portfolio still has 1 stock
