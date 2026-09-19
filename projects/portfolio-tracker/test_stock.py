#Write tests for your Portfolio Tracker. In projects/portfolio-tracker/, create test_stock.py:
#test_stock.py — at minimum:
#test_position_value() — verify price * shares is correct
#test_update_price_raises_on_negative() — use pytest.raises(ValueError)
#test_equality() — two stocks with equal position_value() should be ==
#test_less_than() — a lower-value stock should be < a higher-value one

from stock import Stock
import pytest

def test_position_value():
    stock = Stock("AAPL", 10, 100)
    assert stock.position_value() == 1000

def test_update_price_raises_on_negative():
    stock = Stock("AAPL", 10, 150)
    with pytest.raises(ValueError):
        stock.update_price(-100)

def test_equality():
    stock1 = Stock("AAPL", 10, 150)  # position value = 1500
    stock2 = Stock("GOOGL", 5, 300)   # position value = 1500
    assert stock1 == stock2

def test_less_than():
    stock1 = Stock("AAPL", 10, 250)  # position value = 2500
    stock2 = Stock("GOOGL", 5, 400)   # position value = 2000
    assert stock1 < stock2, "Position value of stock1 should be less than stock2"