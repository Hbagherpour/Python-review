
# Project goal:

A small Python project that calculates the percentage return between an opening price and a closing price.

## Project Structure
```
├── tools/
│   ├── __init__.py
│   └── returns.py
├── tests/
│   └── test_returns.py
├── main.py
└── README.md
```
tools/returns.py contains the calculate_return(open_price, close_price) function.
main.py is a simple example that uses the function.
tests/test_returns.py contains the unit tests.

# How it works:
calculate_return(open_price, close_price) returns the percentage change from the open price to the close price:

return (%) = (close_price - open_price) / open_price * 100

# How to run it:

```bash
python main.py
```

# How to test it:

From the project root, run:
python -m pytest

The tests cover two cases:

Price rise: the return is positive.
Price fall: the return is negative.

