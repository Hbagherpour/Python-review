
import logging
logger = logging.getLogger(__name__)

class Stock:
    def __init__(self, ticker: str, price: float, shares: int) -> None:
        self.ticker = ticker
        self.price = price
        self.shares = shares
        logger.debug("Created Stock instance: %s", self)

    def position_value(self) -> float:
        return self.price * self.shares

    def update_price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Price must be greater than 0")
        logger.info("%s price updated: %s -> %s", self.ticker, self.price, new_price)
        self.price = new_price
        

    def __str__(self) -> str:
        return f"{self.ticker}: {self.shares} shares at ${self.price:.2f} each"

    def __repr__(self) -> str:
        return f"Stock(ticker='{self.ticker}', price={self.price}, shares={self.shares})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Stock):
            return self.position_value() == other.position_value()
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, Stock):
            return self.position_value() < other.position_value()
        return NotImplemented

AAPL = Stock("AAPL", 150.00, 10)
print(AAPL)
AAPL.update_price(155.00)
print(AAPL)

GOOG = Stock("GOOG", 2800.00, 5)
print(GOOG)
GOOG.update_price(2850.00)
print(GOOG)
try:
    GOOG.update_price(-100)
except ValueError as e:
    print(f"Failed to update price: {e}")  # This will raise a ValueError
print(GOOG)
print(AAPL == GOOG)  # False
print(AAPL < GOOG)   # True
print(AAPL > GOOG)   # False
print(AAPL == Stock("AAPL", 155.00, 10))  # True
print(AAPL < Stock("AAPL", 155.00, 10))   # False
print(AAPL > Stock("AAPL", 155.00, 10))   # False
print(AAPL.__repr__())  # Stock(ticker='AAPL', price=155.0, shares=10)
