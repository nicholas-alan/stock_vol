import pandas as pd

def stock_stats(stock_data):
    """
    Compute statistics on historical stock price data.

    Parameters:
        stock_data (pd.DataFrame): The historical stock data returned by `get_historical_stock_data`.

    Returns:
        pd.DataFrame: A new DataFrame containing the original data with additional columns for computed statistics.
    """
    # Create a copy of the input data to avoid modifying the original
    stock_data_copy = stock_data.copy()

    # Compute Daily Return
    stock_data_copy['Daily Return'] = ((stock_data_copy['Close'] / stock_data_copy['Close'].shift(1)) - 1) * 100

    # Return the modified DataFrame with new statistics
    return stock_data_copy

