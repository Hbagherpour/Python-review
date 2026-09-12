Portfolio Tracker

A small object-oriented Python project that models a stock portfolio. It demonstrates core OOP concepts — encapsulation, dunder methods (__str__, __repr__, __eq__, __lt__, __len__), custom exception handling, and using built-ins like max() and sorted() with user-defined comparison logic. Built as a hands-on exercise in designing clean, testable Python classes for a finance-flavored domain.

Project Structure
portfolio-tracker/
├── stock.py        # Stock class — represents a single equity position
├── portfolio.py     # Portfolio class — a collection of Stock holdings
├── main.py          # Demo script showing the classes in action
└── README.md
Features
stock.py — Stock

Represents a single stock holding.

__init__(self, ticker, price, shares) — creates a position
position_value() — returns price * shares
update_price(new_price) — updates the price; raises ValueError if new_price <= 0
__str__ / __repr__ — human-readable and developer-friendly representations
__eq__ — compares two stocks by position_value()
__lt__ — compares two stocks by position_value(), enabling sorting and max()
portfolio.py — Portfolio

Represents a collection of stock holdings.

_holdings — encapsulated internal list of Stock objects
add_stock(stock) — adds a holding
remove_stock(ticker) — removes a holding by ticker; handles a missing ticker gracefully instead of raising
total_value() — sums position_value() across all holdings
best_performer() — returns the highest-value holding using max(), powered by Stock.__lt__
__len__ — number of holdings
__str__ — readable summary, e.g. Portfolio (3 holdings, total value: $12,450.00)
main.py — Demo

Ties the two classes together:

Builds a portfolio with 4–5 realistic holdings
Prints the portfolio summary (__str__)
Prints the holding count (len())
Prints the best performer
Attempts an invalid price update and catches the resulting ValueError
Attempts to remove a non-existent ticker and confirms the program doesn't crash
Sorts the holdings by value with sorted() and prints them in order

