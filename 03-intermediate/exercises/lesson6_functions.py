#Exercise1: Write calculate_return(open_price, close_price) that returns the percentage change.
# Add a proper docstring. Test it with open_price=150, close_price=157.5.

def calculate_return(open_price, close_price):
    """
    calculate percentage return between two prices.

    Args:
        open_price (float): Starting price
        close_price (float): Ending price

    Returns:
        float: Percentage change
    """
    change = close_price - open_price
    percent = (change / open_price) * 100
    return percent

print(calculate_return(150, 157.5))

#Exercise2: Write apply_commission(trade_value, rate=0.001) that returns the trade value minus commission (trade_value * rate).
#Call it once with the default rate, once overriding it to 0.002.

def apply_commission(trade_value, rate=0.001):
    return trade_value - (trade_value * rate)

print(apply_commission(100))
print(apply_commission(100, 0.002))

#Exercise3: Write analyze_prices(prices) that takes a list and returns three values:
#the minimum, maximum, and average — all in one return statement.
#Unpack the result into three named variables and print them, formatted to 2 decimals.

def analyze_prices(prices):
    return min(prices), max(prices), sum(prices) / len(prices)

low, high, avg = analyze_prices([123.4, 121.6, 432.0, 321.3])
print(f"Low: {low:.2f}, High: {high:.2f}, Average: {avg:.2f}")

#Exercise4: Write execute_trade(ticker, quantity, side, price) that prints a formatted trade confirmation string.
#Call it once using keyword arguments in a different order than the function signature.

def execute_trade(ticker, quantity, side, price):
    print(f"Trade confirmation: {side} {quantity} shares of {ticker} @ ${price:.2f}")

execute_trade(price=430.2, ticker="TSLA", quantity=200, side="BUY")

#Exercise5: Pure vs. side-effect: Write two versions of a "add trade to portfolio" concept:
#   calculate_position_value(shares, price) — a pure function, returns shares * price
#   add_to_portfolio(portfolio_list, ticker) — a side-effect function that appends ticker to portfolio_list (a list passed in) and returns nothing
#Call both, and in a comment explain which one would be easier to unit test and why.

def calculate_position_value(shares, price):
    return shares * price

value=calculate_position_value(2, 50)
print(f"Position value: {value}")


def add_to_portfolio(portfolio_list, ticker):
    portfolio_list.append(ticker)

my_portfolio = []
add_to_portfolio(my_portfolio, "TSLA")
add_to_portfolio(my_portfolio, "GOOG")

print(f"Portfolio: {my_portfolio}")

"""
calculate_position_value is easier to unit test: given the same inputs (shares, price),
it always returns the same output, with no dependency on or modification of anything
outside itself.

add_to_portfolio is harder to test because its "result" isn't a return value — it's a
mutation of external state (the list you passed in). To test it, you have to set up
state before the call (an empty/seeded list), call the function for its side effect,
then inspect that external state afterward to verify it changed correctly.
"""

#Exercise6: Bug hunt:
#def get_price_list():
#       prices = []
#       prices.append(100)
#       prices.append(200)
#
#result = get_price_list()
#print(result[0])

#What happens when you run this, and why? Fix it.

#Fixed version:

def get_price_list():
    prices = []
    prices.append(100)
    prices.append(200)
    return prices          # <- must return the list

result = get_price_list()  # <- consistent 0-space indent, outside the function
print(result[0])

#Bug 1 — Indentation error (why it crashes immediately)
#IndentationError: The function body is indented 7 spaces. Then result = get_price_list() dedents to 3 spaces — but 3 doesn't match any level Python has seen so far

#Bug 2 — Even if indentation were fixed, the function is missing a return
#Without an explicit return, a function returns None by default. So result would be None, and result[0] would raise TypeError