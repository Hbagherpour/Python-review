#Import both classes
#Create a portfolio, add 4-5 stocks with realistic tickers/prices/shares
#Print the portfolio (print(portfolio) should use __str__)
#Print len(portfolio)
#Print the best performer
#Try updating a stock's price to a negative number — catch the ValueError gracefully with a printed message
#Try removing a stock that doesn't exist — should not crash
#Sort your holdings list using sorted() and print them in order of value


from stock import Stock
from portfolio import Portfolio

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
    portfolio._holdings[0].update_price(-150.00)
except ValueError as e:
    print(f"Error updating stock price: {e}")


portfolio.remove_stock("NONEXISTENT")

sorted_holdings = sorted(portfolio._holdings, key=lambda stock: stock.position_value(), reverse=True)
for stock in sorted_holdings:
    print(f"{stock.ticker}: ${stock.position_value():.2f}")