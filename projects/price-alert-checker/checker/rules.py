def is_triggered(rate: float, condition: str, threshold: float) -> bool:
    """
    Determines if the given rate triggers the specified condition against the threshold.

    Parameters:
    - rate (float): The current rate to evaluate.
    - condition (str): The condition to check ('above' or 'below').
    - threshold (float): The threshold value to compare against.

    Returns:
    - bool: True if the condition is met, False otherwise.

    Note: At exactly the threshold value, the function will return False for both 'above' and 'below' conditions.
    """
    if condition == 'above':
        return rate > threshold  # Triggered only if rate is strictly above the threshold
    elif condition == 'below':
        return rate < threshold  # Triggered only if rate is strictly below the threshold
    else:
        raise ValueError("Condition must be either 'above' or 'below'.")