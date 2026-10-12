
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

from stock_with_typing_logging import Stock
from portfolio_with_typing_logging import Portfolio

portfolio = Portfolio()
portfolio.add_stock(Stock("AAPL", 332.00, 10))
portfolio.add_stock(Stock("GOOG", 335.00, 5))
portfolio.add_stock(Stock("MSFT", 495.00, 8))
portfolio.add_stock(Stock("AMZN", 256.00, 3))
portfolio.add_stock(Stock("TSLA", 365.00, 12))

print(portfolio)
print(f"Number of holdings: {len(portfolio)}")
print(f"Best performer: {portfolio.best_performer()}")

try:
    portfolio.get_holdings()[0].update_price(-150.00)
except ValueError as e:
    print(f"Error updating stock price: {e}")


portfolio.remove_stock("NONEXISTENT")

sorted_holdings = sorted(portfolio.get_holdings(), reverse=True)
for stock in sorted_holdings:
    print(f"{stock.ticker}: ${stock.position_value():.2f}")