
def value_per_ticker(trades: list[dict]) -> dict[str, float]:
    ticker_values = {}
    for trade in trades:
        ticker = trade['ticker']
        value = trade['price'] * trade['quantity']
        ticker_values[ticker] = ticker_values.get(ticker, 0) + value
    return ticker_values


def biggest_trade(trades: list[dict]) -> dict | None:
    if not trades:
        return None
    return max(trades, key=lambda trade: trade['price'] * trade['quantity'])

