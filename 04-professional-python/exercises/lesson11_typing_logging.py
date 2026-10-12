#exercise1: Add type hints: Rewrite these functions with full type hints:
"""
       def apply_commission(trade_value, rate=0.001):
       return trade_value - trade_value * rate

   def average_price(prices):
       return sum(prices) / len(prices)

   def find_price(prices, ticker):
       return prices.get(ticker)      # returns None if missing
    """

import logging


def apply_commission(trade_value: float, rate: float = 0.001) -> float:
    return trade_value - trade_value * rate
def average_price(prices: list[float]) -> float:
    return sum(prices) / len(prices)
def find_price(prices: dict[str, float], ticker: str) -> float | None:
    return prices.get(ticker)      # returns None if missing


#exercise2: Run mypy: Install it, run mypy lesson10_typing_logging.py, and paste the output.
#Then deliberately call apply_commission("1000") and run mypy again.
#What does it report, and why didn’t Python itself complain until runtime?


#after running mypy on the code, it will report an error for the call apply_commission("1000") because the function expects a float for the trade_value parameter, but a string is being passed instead.
#The reason Python itself doesn't complain until runtime is that Python is a dynamically typed language, meaning it doesn't enforce type checking at compile time. The type hints are mainly for static analysis tools like mypy, which can catch type errors before the code is run.
#apply_commission("1000")  # This will cause a mypy error

"""Traceback (most recent call last):
  File "c:\Hossein\Python\Python-review\04-professional-python\exercises\lesson10_typing_logging.py", line 31, in <module>
    apply_commission("1000")  # This will cause a mypy error
    ~~~~~~~~~~~~~~~~^^^^^^^^
  File "c:\Hossein\Python\Python-review\04-professional-python\exercises\lesson10_typing_logging.py", line 17, in apply_commission
    return trade_value - trade_value * rate
                         ~~~~~~~~~~~~^~~~~~
TypeError: can't multiply sequence by non-int of type 'float'"""

"""
When with the bad call active:
mypy .\lesson10_typing_logging.py
lesson10_typing_logging.py:31: error: Argument 1 to "apply_commission" has incompatible type "str"; expected "float"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

When with the bad call commented out:
 mypy .\lesson10_typing_logging.py
Success: no issues found in 1 source file
"""


#exercise3: Basic logging: Configure logging with a timestamped format at INFO level.
#Write a function load_prices(prices: dict[str, float]) that logs an INFO message with the number of prices loaded,
#and a WARNING for any ticker whose price is <= 0.

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

def load_prices(prices: dict[str, float]) -> None:
    logger.info(f"Loading prices for {len(prices)} tickers.")
    for ticker, price in prices.items():
        if price <= 0:
            logger.warning(f"Invalid price for {ticker}: {price}")

prices = {"AAPL": 150.0, "GOOG": 0.0, "MSFT": -10.0, "AMZN": 3200.0}
load_prices(prices)

"""2026-10-12 10:50:52,511 | INFO | __main__ | Loading prices for 4 tickers.
2026-10-12 10:50:52,512 | WARNING | __main__ | Invalid price for GOOG: 0.0
2026-10-12 10:50:52,512 | WARNING | __main__ | Invalid price for MSFT: -10.0
"""

#exercise4: Log an exception: Write safe_return(open_price: float, close_price: float) -> float | None
#that catches ZeroDivisionError, calls logger.exception(...), and returns None.
#Trigger it with open_price=0 and look at the traceback in the output.
#You’re still calling logging.exception(...), not logger.exception(...). The exercise asked for logger.exception.


logger = logging.getLogger(__name__)

def safe_return(open_price: float, close_price: float) -> float | None:
    try:
        return (close_price - open_price) / open_price * 100
    except ZeroDivisionError:
        logger.exception("Cannot compute return: open_price is zero")
        return None

safe_return(0, 100)  # This will log an exception and return None

print("#### exercise4: Log an exception ####")

"""
logging output:
2026-10-12 10:50:52,512 | ERROR | __main__ | Cannot compute return: open_price is zero"""

"""Traceback (most recent call last):
  File "c:\Hossein\Python\Python-review\04-professional-python\exercises\lesson10_typing_logging.py", line 62, in safe_return
    return (close_price - open_price) / open_price * 100
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
ZeroDivisionError: division by zero"""


#exercise5: Constants and clean code: Refactor this to remove magic numbers and add type hints:

"""   def net_proceeds(value, shares):
       fee = value * 0.001
       tax = value * 0.15
       return value - fee - tax - shares * 0.005
    """

def net_proceeds(value: float, shares: int) -> float:
    FEE_RATE: float = 0.001
    TAX_RATE: float = 0.15
    SHARE_FEE: float = 0.005

    fee: float = value * FEE_RATE
    tax: float = value * TAX_RATE
    return value - fee - tax - shares * SHARE_FEE

print("#### exercise5: Net Proceeds Calculation ####")
print(net_proceeds(1000.0, 10))  # Example usage

#exercise6: bug hunt:
"""   def add_to_watchlist(ticker, watchlist=[]):
       watchlist.append(ticker)
       return watchlist

   print(add_to_watchlist("AAPL"))
   print(add_to_watchlist("MSFT"))
    """
#What gets printed, and why is it surprising? Explain in a comment and fix it.

#The output will be:
#['AAPL']
#['AAPL', 'MSFT']
#This is surprising because the default argument `watchlist=[]` is evaluated only once when the function is defined, not each time it's called. This means that the same list object is used for all calls to the function, leading to unexpected behavior.

def add_to_watchlist(ticker: str, watchlist: list[str] | None = None) -> list[str]:
    if watchlist is None:
        watchlist = []
    watchlist.append(ticker)
    return watchlist

print("#### exercise6: Bug Hunt ####")
print(add_to_watchlist("AAPL"))
print(add_to_watchlist("MSFT"))
