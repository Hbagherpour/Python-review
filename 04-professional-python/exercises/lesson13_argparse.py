# Exercise 1: Write a program that takes one required argument, ticker, and prints Ticker: AAPL (using whatever was typed).
# Run it with python lesson13_argparse.py AAPL

"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ticker", help="Stock ticker symbol")
args = parser.parse_args()

print(f"Ticker: {args.ticker}")
"""

#Exercise 2: Add an optional argument --price (type float, default 0.0).
#Print AAPL price: $227.35 using two decimals. Run it with and without --price.

"""
parser.add_argument("--price", type=float, default=0.0, help="Stock price")
args = parser.parse_args()  

print(f"{args.ticker} price: ${args.price:.2f}")
"""

#Exercise 3: Add a switch --shout. If it’s used, print the ticker in capital letters; otherwise print it exactly as typed.
#Run it with aapl and with aapl --shout.

"""
parser.add_argument("--shout", action="store_true", help="Print ticker in capital letters")
args = parser.parse_args()

if args.shout:
    print(f"Ticker: {args.ticker.upper()}")
else:
    print(f"Ticker: {args.ticker}")
"""

#add all the arguments first, then call parse_args() once.And comment out the previous parse_args() calls. Then run the program with different combinations of arguments to see how it behaves.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ticker", help="Stock ticker symbol")
parser.add_argument("--price", type=float, default=0.0, help="Stock price")
parser.add_argument("--shout", action="store_true", help="Print ticker in capital letters")
args = parser.parse_args()

print(f"Ticker: {args.ticker}")
print(f"{args.ticker} price: ${args.price:.2f}")

if args.shout:
    print(f"Ticker: {args.ticker.upper()}")
else:
    print(f"Ticker: {args.ticker}")


#Find the bug:

"""
parser.add_argument("--quantity", default=1)
args = parser.parse_args()
print(args.quantity + 5)
"""
#Run it with --quantity 10. What happens, and why? Fix it in one small change.

#The bug occurs because the `--quantity` argument is being treated as a string by default, so when you try to add 5 to it, Python raises a TypeError since you cannot add an integer to a string.
#Correct the bug by specifying the type of the `--quantity` argument as an integer. Here's the fixed code:
"""
parser.add_argument("--quantity", type=int, default=1)
"""


