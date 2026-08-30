
#Exercise1: finance_utils.py — move your calculate_return and apply_commission functions here from Lesson 6/2 (with docstrings).
#Add an if __name__ == "__main__": block that prints a quick test call when the file is run directly.


def calculate_return(open_price, close_price):
    """
    calculate percentage return between two prices.

    Args:
        open_price (float): Starting price
        close_price (float): Ending price

    Returns:
        float: Percentage change
    """
    change = close_price - open_price
    percent = (change / open_price) * 100
    return percent


def apply_commission(trade_value, rate=0.001):
    return trade_value - (trade_value * rate)


if __name__ == "__main__":
    print(calculate_return(150, 157.5))
    print(apply_commission(100))
    print(apply_commission(100, 0.002))
