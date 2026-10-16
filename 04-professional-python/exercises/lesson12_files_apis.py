#exercise1: pathlib: Using Path(__file__).parent, build a path to data/trades.csv.
#Create the data/ folder if it doesn’t exist (mkdir(exist_ok=True)) and print whether the file exists.

from pathlib import Path

BASE_DIR = Path(__file__).parent
data_folder = BASE_DIR / "data"
file_path = data_folder / "trades.csv"
data_folder.mkdir(exist_ok=True)
trades_file = data_folder / "trades.csv"
print(f"File exists: {trades_file.exists()}")

#EXERCISE 2: Write a CSV: Write data/trades.csv with columns ticker, side, price, quantity and at least 5 rows (mix BUY and SELL).
#Use csv.DictWriter with newline="".

import csv

with open(file_path, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['ticker', 'side', 'price', 'quantity']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'ticker': 'AAPL', 'side': 'BUY', 'price': 150.0, 'quantity': 10})
    writer.writerow({'ticker': 'GOOGL', 'side': 'SELL', 'price': 2800.0, 'quantity': 5})
    writer.writerow({'ticker': 'MSFT', 'side': 'BUY', 'price': 300.0, 'quantity': 20})
    writer.writerow({'ticker': 'TSLA', 'side': 'SELL', 'price': 700.0, 'quantity': 8})
    writer.writerow({'ticker': 'AMZN', 'side': 'BUY', 'price': 3500.0, 'quantity': 3})

#exercise 3: Read a CSV: Write load_trades(path: Path) -> list[dict] that reads the file with DictReader and converts price to float and quantity to int.
#If a row has bad data (e.g. price = "abc"), catch the ValueError, log a WARNING with the row, and skip it.
#Test it by temporarily adding one bad row.

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)

def load_trades(path: Path) -> list[dict]:
    trades = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                price = float(row["price"])
                quantity = int(row["quantity"])
            except (ValueError, TypeError):
                logger.warning("Skipping bad row: %s", row)
                continue
            trades.append({
                'ticker': row['ticker'],
                'side': row['side'],
                'price': price,
                'quantity': quantity
            })

    return trades

trades = load_trades(file_path)
print(f"Loaded trades: {trades}")


#Exercise 4: Summarize: Write summarize_trades(trades) -> dict returning the total traded value per ticker (price * quantity), using a loop and a dict.
#Print it formatted as currency.


def summarize_trades(trades) -> dict:
    summary = {}
    for trade in trades:
        ticker = trade['ticker']
        value = trade['price'] * trade['quantity']
        summary[ticker] = summary.get(ticker, 0) + value
    return summary

summary = summarize_trades(trades)
for ticker, value in summary.items():
    print(f"{ticker}: ${value:,.2f}")


#exercise 5: JSON. Create this dictionary:
#watchlist = {"name": "My list", "tickers": ["AAPL", "MSFT", "GOOG"]}
#Save it to data/watchlist.json with json.dump(..., indent=2). Then load it back with json.load and print the name and each ticker.

import json

watchlist = {"name": "My list", "tickers": ["AAPL", "MSFT", "GOOG"]}

file_path1 = data_folder / "watchlist.json"
with open(file_path1, "w") as f:
    json.dump(watchlist, f, indent=2)

with open(file_path1, "r") as f:
    loaded_watchlist = json.load(f)

print(f"Name: {loaded_watchlist['name']}")
print("Tickers:")
for ticker in loaded_watchlist['tickers']:
    print(f"  {ticker}")


#exercise 6: Text file. Write three lines (any text) to data/notes.txt.
#Then add a fourth line using append mode.
#Then read the file and print each line.


file_path2 = data_folder / "notes.txt"

with open(file_path2, "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open(file_path2, "a") as f:
    f.write("Line 4\n")

with open(file_path2, "r") as f:
    for line in f:
        print(line.strip())


#exercise 7: API call:
    """
    import requests

response = requests.get(
    "https://api.frankfurter.dev/v1/latest",
    params={"base": "USD", "symbols": "EUR"},
    timeout=10,
)
response.raise_for_status()
data = response.json()
print(data["rates"]["EUR"])

    """

#Run it and print the rate. Then wrap it in a try/except requests.exceptions.
#RequestException that prints "Could not get the rate" if anything goes wrong. 
#To test the failure, change timeout=10 to timeout=0.001 and confirm your message appears instead of a crash.

try:
    import requests

    response = requests.get(
        "https://api.frankfurter.dev/v1/latest",
        params={"base": "USD", "symbols": "EUR"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    print(data["rates"]["EUR"])
except requests.exceptions.RequestException:
    print("Could not get the rate")

#Exercise 8: Find the bug:

    """
    import csv

with open("prices.csv") as f:
    reader = csv.DictReader(f)
    total = 0
    for row in reader:
        total += row["price"]
    print(total)
    """

#The bug in the provided code is that it attempts to add a string (row["price"]) to an integer (total). The "price" value read from the CSV file is a string, and it needs to be converted to a numeric type (like float) before performing the addition.
##To fix the bug, I should convert row["price"] to a float (or int, depending on the expected data type) before adding it to total. Here's the corrected code:
#also, it is a good practice to handle potential exceptions that may arise during the conversion, such as ValueError if the string cannot be converted to a float.
#also, in opening the file, it is a good practice to specify the encoding (e.g., encoding="utf-8") to avoid potential issues with character encoding.
#corrected code:

import csv

with open("prices.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    total = 0
    for row in reader:
        try:
            total += float(row["price"])
        except ValueError:
            print(f"Skipping row with invalid price: {row}")
    print(total)

