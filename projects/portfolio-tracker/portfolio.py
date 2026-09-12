#portfolio.py — a Portfolio class with:

#_holdings list (encapsulated)
#add_stock(stock)
#remove_stock(ticker) — removes a stock by ticker name; if not found, catch the situation gracefully (don't crash) and print a message
#total_value() — sum of all position_value()
#best_performer() — returns the Stock with the highest position_value() (hint: use max(), which works because you defined __lt__)
#__len__ — number of holdings
#__str__ — a readable summary, e.g. "Portfolio (3 holdings, total value: $12,450.00)"

from stock import Stock  # Import the Stock class from stock.py
class Portfolio:
    def __init__(self):
        self._holdings = []
    def add_stock(self, stock):
        if isinstance(stock, Stock):
            self._holdings.append(stock)
        else:
            raise TypeError("Only Stock instances can be added to the portfolio.")
    def remove_stock(self, ticker):
        for stock in self._holdings:
            if stock.ticker == ticker:
                self._holdings.remove(stock)
                return
        print(f"Stock with ticker '{ticker}' not found in the portfolio.")
    def total_value(self):
        return sum(stock.position_value() for stock in self._holdings)
    def best_performer(self):
        if not self._holdings:
            return None
        return max(self._holdings, key=lambda stock: stock.position_value())
    def __len__(self):
        return len(self._holdings)
    def __str__(self):
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
