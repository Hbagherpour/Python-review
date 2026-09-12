#stock.py — a Stock class with:

#__init__(self, ticker, price, shares)
#position_value()
#update_price(new_price) — but this time, raise a ValueError if new_price <= 0
#__str__, __repr__, __eq__ (compare by position_value()), __lt__ (compare by position_value())

class Stock:
    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Price must be greater than 0")
        self.price = new_price

    def __str__(self):
        return f"{self.ticker}: {self.shares} shares at ${self.price:.2f} each"

    def __repr__(self):
        return f"Stock(ticker='{self.ticker}', price={self.price}, shares={self.shares})"

    def __eq__(self, other):
        if isinstance(other, Stock):
            return self.position_value() == other.position_value()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Stock):
            return self.position_value() < other.position_value()
        return NotImplemented

APPL = Stock("AAPL", 150.00, 10)
print(APPL)
APPL.update_price(155.00)
print(APPL)

GOOG = Stock("GOOG", 2800.00, 5)
print(GOOG)
GOOG.update_price(2850.00)
print(GOOG)
try:
    GOOG.update_price(-100)
except ValueError as e:
    print(f"Failed to update price: {e}")  # This will raise a ValueError
print(GOOG)
print(APPL == GOOG)  # False
print(APPL < GOOG)   # True
print(APPL > GOOG)   # False
print(APPL == Stock("AAPL", 155.00, 10))  # True
print(APPL < Stock("AAPL", 155.00, 10))   # False
print(APPL > Stock("AAPL", 155.00, 10))   # False
print(APPL.__repr__())  # Stock(ticker='AAPL', price=155.0, shares=10)
