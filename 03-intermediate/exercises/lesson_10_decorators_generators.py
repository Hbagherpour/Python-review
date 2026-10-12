#exercise 1: Basic decorator: Write a decorator log_call that prints "Calling <function name>" before the function runs and "<function name> returned <result>" after.
#Apply it to a simple function like calculate_return(open_price, close_price). 
#Call the decorated function and observe the output.

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def calculate_return(open_price, close_price):
    return (close_price - open_price) / open_price * 100    
# Call the decorated function
calculate_return(100, 110)  

#Exercise 2: Timer decorator: Write a @timer decorator and apply it to a function that does some busy work (e.g., sums range(1_000_000)).
#Confirm it prints the elapsed time.

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def sum_large_range():
    return sum(range(1_000_000))

# Call the decorated function
sum_large_range()

#Exercise 3: Basic generator: Write a generator function price_stream(prices) that takes a list and yields each price one at a time.
#Loop over it with a for loop and print each value. Then explain in a comment: what would happen differently if you used return prices instead of yielding each one?

def price_stream(prices):
    for price in prices:
        yield price 

# Loop over the generator and print each value
for price in price_stream([100, 101, 102, 103]):
    print(price)    

# If we used return prices instead of yielding each one, the function would return the entire list at once and terminate.
# also , we would not be able to iterate over the values one at a time, and we would lose the memory efficiency that generators provide.


#Exercise 4: Generator with early stop: Write a generator positive_returns(returns) that yields only the positive values from a list one at a time.
#Loop over it, but break after finding the first 2 positive values. Add a print() inside the generator right before each yield, so you can visually confirm that values after the 2nd positive one are never even generated (proving laziness).


def positive_returns(returns):
    for r in returns:
        if r > 0:
            print(f"Yielding positive return: {r}")
            yield r

# Loop over the generator and break after finding the first 2 positive values
count = 0   
for r in positive_returns([1, -2, 3, -4, 5]):
    print(r)
    count += 1
    if count == 2:
        break

#Exercise 5: Context manager (class-based): Write a Timer class (like the example) using __enter__/__exit__.
#Use it in a with block around some computation.


class Timer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Elapsed time: {end - self.start:.4f} seconds")

# Use the Timer context manager in a with block
with Timer():
    total = sum(range(1_000_000))



#Exercise 6: Context manager (contextlib version): Rewrite exercise 5 using @contextmanager from contextlib instead.
#Confirm it produces the same behavior.

from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start:.4f} seconds")

# Use the timer context manager in a with block
with timer():
    total = sum(range(1_000_000))


#Exercise 7: Bug hunt:
    """
   def get_prices():
       yield 100
       yield 200
       yield 300

   prices = get_prices()
   print(prices[0])
  
    """

#What happens when you run this, and why? (Hint: think about what type get_prices() actually returns, and what operations that type does and doesn't support.)
#Fix it to correctly get the first value.

#when you run this code, it raises a TypeError because the object returned by get_prices() is a generator, which does not support indexing. Generators can only be iterated over, and you cannot access their elements using square brackets.
#Fix it to correctly get the first value:
def get_prices():
    yield 100
    yield 200
    yield 300

prices = get_prices()
print(next(prices))
