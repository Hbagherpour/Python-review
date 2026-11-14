# Trade Log Analyzer

A small Python program that reads a CSV file of trades and prints a short summary.

## Project Structure

```
trade-log-analyzer/
├── analyzer/
│   ├── __init__.py
│   ├── loader.py       # reads the CSV
│   └── summary.py      # calculates the numbers
├── tests/
│   └── test_summary.py
├── trades.csv          # sample data
├── main.py
└── README.md
```

## How It Works

- `loader.py` reads the CSV, converts the numbers, skips bad rows, and logs a warning for each skipped row.
- `summary.py` has two functions: `value_per_ticker` (total value per ticker) and `biggest_trade` (the trade with the highest price × quantity).
- `main.py` takes `--file` (required) and `--ticker` (optional), loads the trades, filters by ticker if given, and prints the summary.

## How to Run It

```bash
python main.py --file trades.csv
python main.py --file trades.csv --ticker aapl
```

Example output:

```
Trades loaded: 5 (2 bad rows skipped)
Total value per ticker:
  AAPL: $1,500.00
  GOOGL: $14,000.00
  MSFT: $6,000.00
  TSLA: $10,500.00
  AMZN: $26,400.00
Biggest trade: AMZN, $26,400.00
```

## How to Test It

```bash
python -m pytest
```

The tests check the totals per ticker, the biggest trade, and the empty-list cases.
