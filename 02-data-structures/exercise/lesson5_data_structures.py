#exercise1: List manipulation: Start with prices = [150.2, 152.8, 148.5, 155.1].
#Append 149.9, remove 148.5, sort ascending, then print the final list and its length.

prices = [150.2, 152.8, 148.5, 155.1]
prices.append(149.9)
prices.remove(148.5)
prices.sort()
print(prices)
print(len(prices))

#exercise2: Tuple unpacking: Given trade = ("AAPL", 227.35, 100, "BUY") (ticker, price, quantity, side),
#unpack it into 4 named variables and print: "BUY 100 shares of AAPL at $227.35".

trade = ("AAPL", 227.35, 100, "BUY")
ticker, price, volume, side = trade
print(f"{side} {volume} shares of {ticker} at ${price:.2f}")

#exercise3: Dict-based lookup: Given
#prices = {"AAPL": 227.35, "MSFT": 415.1, "GOOG": 178.9}
#Safely print the price for "TSLA" using .get() with a default of "Not found" — don't let it crash.

prices = {"AAPL": 227.35, "MSFT": 415.1, "GOOG": 178.9}
print(prices.get("TSLA", "Not found"))


#exercise4: Set operations: Given nasdaq_watchlist = {"AAPL", "MSFT", "GOOG", "TSLA"} and nyse_watchlist = {"JPM", "GS", "MSFT", "TSLA"},
#print: tickers in both lists (intersection), tickers unique to nasdaq_watchlist only

nasdaq_watchlist = {"AAPL", "MSFT", "GOOG", "TSLA"}
nyse_watchlist = {"JPM", "GS", "MSFT", "TSLA"}

print(nasdaq_watchlist & nyse_watchlist)
print(nasdaq_watchlist - nyse_watchlist)


#exercise5: List comprehension: Given returns = [1.2, -0.5, 3.1, -2.8, 0.4, -1.1],
#use a list comprehension to build a new list containing only the positive returns (no loop + append, no continue).

returns = [1.2, -0.5, 3.1, -2.8, 0.4, -1.1]
positive_returns = [p for p in returns if p > 0]
print(positive_returns)


#exercise6: List of dicts (real-world shape): Given
#   portfolio = [
#       {"ticker": "AAPL", "shares": 10, "price": 227.3},
#       {"ticker": "MSFT", "shares": 5, "price": 415.1},
#       {"ticker": "GOOG", "shares": 8, "price": 178.9},
#   ]

#Loop through and print each holding's total value (shares * price, formatted as currency),
#then print the total portfolio value (sum of all holdings) using an accumulator.


portfolio = [
       {"ticker": "AAPL", "shares": 10, "price": 227.3},
       {"ticker": "MSFT", "shares": 5, "price": 415.1},
       {"ticker": "GOOG", "shares": 8, "price": 178.9},
   ]

total_value = 0

for holding in portfolio:
    value = holding["shares"] * holding["price"]
    print(f"{holding['ticker']}: ${value:,.2f}")
    total_value = total_value + value

print(f"Sum of all holdings is: ${total_value:,.2f}")


#exercise7: Bug hunt:
#ohlc = (100, 105, 98, 103)
#   ohlc[0] = 101
#   print(ohlc)
#What happens and why? Fix it correctly
#(hint: you can't "fix" a tuple in place — what's the right approach when you need to change one value?).

#This raises a TypeError, because tuples are immutable and can not be altered.
#solution can be unpacking to swap out one postion


ohlc = (100, 105, 98, 103)
o, h, l, c = ohlc
ohlc = (101, h, l, c)
print(ohlc)