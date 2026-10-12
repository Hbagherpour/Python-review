
import logging

logger = logging.getLogger(__name__)

from stock_with_typing_logging import Stock  # Import the Stock class from stock.py
class Portfolio:
    def __init__(self) -> None:
        self._holdings = []  # List to hold Stock instances
    def add_stock(self, stock: Stock) -> None:
        if isinstance(stock, Stock):
            self._holdings.append(stock)
        else:
            raise TypeError("Only Stock instances can be added to the portfolio.")
    def remove_stock(self, ticker: str) -> None:
        for stock in self._holdings:
            if stock.ticker == ticker:
                self._holdings.remove(stock)
                return
        logger.warning(f"Stock with ticker '{ticker}' not found in the portfolio.")
    def total_value(self) -> float:
        return sum(stock.position_value() for stock in self._holdings)
    def best_performer(self) -> Stock | None:
        if not self._holdings:
            return None
        return max(self._holdings, key=lambda stock: stock.position_value())
    def get_holdings(self) -> list[Stock]:
        return list(self._holdings)
    def __len__(self) -> int:
        return len(self._holdings)
    def __str__(self) -> str:
        total_value = self.total_value()
        return f"Portfolio ({len(self)} holdings, total value: ${total_value:.2f})"

#some instance tests
portfolio = Portfolio()
portfolio.add_stock(Stock("AAPL", 150.00, 10))
portfolio.add_stock(Stock("GOOG", 2800.00, 5))
print(portfolio)
print(f"Total value: ${portfolio.total_value():.2f}")
print(f"Best performer: {portfolio.best_performer()}")
print(f"Number of holdings: {len(portfolio)}")  
portfolio.remove_stock("AAPL")
print(portfolio)
