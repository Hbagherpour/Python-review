
import argparse
from pathlib import Path
import logging
from analyzer.loader import load_trades
from analyzer.summary import value_per_ticker, biggest_trade

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to the CSV file containing trade data")
    parser.add_argument("--ticker", help="Filter trades by ticker symbol")
    args = parser.parse_args()

    trades, skipped = load_trades(Path(args.file))
    print(f"Trades loaded: {len(trades)} ({skipped} bad rows skipped)")

    # If args.ticker is given, keep only the trades for that ticker
    if args.ticker:
        trades = [trade for trade in trades if trade['ticker'] == args.ticker.upper()]

    #If no trades are left, print "No trades found for ..." and return

    if not trades:
        if args.ticker:
            print(f"No trades found for {args.ticker.upper()}")
        else:
            print("No valid trades found in the file")
        return

    totals = value_per_ticker(trades)
    biggest = biggest_trade(trades)

    print("Total value per ticker:")
    for ticker, total in totals.items():
        print(f"  {ticker}: ${total:,.2f}")

    print(f"Biggest trade: {biggest['ticker']}, ${biggest['price'] * biggest['quantity']:,.2f}")

if __name__ == "__main__":
    main()