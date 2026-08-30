#Exercise1: Write a function safe_divide(a, b) that returns a / b, but catches ZeroDivisionError and returns None instead of crashing.
#Test with safe_divide(10, 2) and safe_divide(10, 0).

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))

#Exercise2: Given prices = {"AAPL": 227.35, "MSFT": 415.1}, write a function get_price(prices, ticker) that returns the price, or prints f"{ticker} not found" and returns None if the ticker doesn't exist.
#Test with "AAPL" and "TSLA".

prices = {"AAPL": 227.35, "MSFT": 415.1}
def get_price(prices, ticker):
    try:
        return prices[ticker]
    except KeyError:
        print(f"{ticker} not found")
        return None

print(get_price(prices, "TSLA"))
print(get_price(prices, "AAPL"))


#Exercise3: Write a function parse_price(value) that tries to convert value to a float and return it.
#Catch ValueError (e.g. if given "abc") and print "Invalid price format", returning None.
#Test with "150.5", "abc", and None (this last one should raise TypeError — catch that separately and print "Price cannot be None").

def parse_price(value):
    try:
        return float(value)
    except ValueError:
        print("Invalid price format")
        return None
    except TypeError:
        print("Price cannot be None")
        return None

print(parse_price("150.5"))
print(parse_price("abc"))
print(parse_price(None))


#Exercise4: Write a function process_trade(price, quantity) that calculates price * quantity inside a try.
#Use else to print the result only if no error occurred, and finally to print "Trade processing complete" regardless.
# Trigger it with valid inputs, then with price="abc" (which will raise TypeError when multiplied).

def process_trade(price, quantity):
    try:
        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
            raise TypeError
        result = price * quantity
    except TypeError:
        print("Invalid input types for price or quantity")
        return None
    else:
        print(f"Trade value: {result}")
        return result
    finally:
        print("Trade processing complete")


process_trade(10, 5)
process_trade("abc", 5)


#Exercise5: Raising your own exception: Write validate_trade_quantity(quantity) that raises a ValueError with the message "Quantity must be positive" if quantity <= 0.
#Wrap a call to it in a try/except that catches the ValueError and prints the message. Test with quantity=100 and quantity=-5.


def validate_trade_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")

try:
    validate_trade_quantity(100)
    print("Quantity is valid")
except ValueError as e:
    print(e)

try:
    validate_trade_quantity(-5)
    print("Quantity is valid")
except ValueError as e:
    print(e)

#Exercise6: Bug hunt: Identify the issue in the following code and fix it.
"""
def get_stock_price(ticker):
       prices = {"AAPL": 227.35}
       try:
           return prices[ticker]
       except:
           print("Something went wrong")

   print(get_stock_price("AAPL"))
   print(get_stock_price("MSFT"))
"""
#This code "works" without crashing — but explain in a comment why the bare except: is a bad practice here, even though it prevents a crash. Rewrite it using a specific exception type.

#Ficed code:

def get_stock_price(ticker):
    prices = {"AAPL": 227.35}
    try:
        return prices[ticker]
    except KeyError:
        print("Stock ticker not found")
        return None

print(get_stock_price("AAPL"))
print(get_stock_price("MSFT"))

#The explanation for why using a bare except is bad practice is that it catches all exceptions, including those that you might not expect or want to catch (like KeyboardInterrupt, SystemExit, etc.).
#This can make debugging difficult because it hides the actual error and can lead to unexpected behavior. By catching specific exceptions (like KeyError in this case), you can handle only the errors you anticipate and allow other exceptions to propagate normally.
