#In loader.py, write load_trades(path), like in Lesson 14: it converts the numbers, skips bad rows, and logs a warning for each one.

from pathlib import Path
import csv
import logging
import math

logger = logging.getLogger(__name__)

VALID_SIDES = {"BUY", "SELL"}

def load_trades(path: Path) -> tuple[list[dict], int]:
    trades = []
    skipped = 0

    with open(path, 'r', encoding='utf-8', newline="") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2):
            try:
                ticker = row["ticker"].strip().upper()
                side = row["side"].strip().upper()
                price = float(row["price"])
                quantity = int(row["quantity"])
            except (KeyError, AttributeError, ValueError, TypeError):
                logger.warning("Line %d: bad row: %s", line_no, row)
                skipped += 1
                continue

            if not ticker or side not in VALID_SIDES or price <= 0 or quantity <= 0 or math.isnan(price):
                logger.warning("Line %d: invalid values: %s", line_no, row)
                skipped += 1
                continue

            trades.append({
                'ticker': ticker,
                'side': side,
                'price': price,
                'quantity': quantity,
            })
    logger.info("Loaded %d trades, skipped %d", len(trades), skipped)
    return trades, skipped

