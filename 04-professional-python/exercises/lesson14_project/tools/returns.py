
def calculate_return(open_price, close_price):
    """
    Calculate the percentage change between open and close prices.

    Parameters:
    open_price (float): The opening price of the stock.
    close_price (float): The closing price of the stock.

    Returns:
    float: The percentage change from open to close price.
    """
    if open_price == 0:
        raise ValueError("Open price cannot be zero.")
    
    percentage_change = ((close_price - open_price) / open_price) * 100
    return percentage_change