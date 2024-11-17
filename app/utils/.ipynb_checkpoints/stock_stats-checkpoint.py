import pandas as pd

def stock_stats(stock_data):
    """
    Compute statistics on historical stock price data, including daily returns, running averages,
    running standard deviations, daily volatility, and cumulative statistics for volatility.

    Parameters:
        stock_data (pd.DataFrame): The historical stock price data returned by `get_historical_stock_data`.

    Returns:
        pd.DataFrame: A new DataFrame containing the original data with additional columns for computed statistics.
    """
    # Create a copy of the input data to avoid modifying the original
    stock_data_copy = stock_data.copy()

    # Compute Daily Return
    stock_data_copy['Daily Return'] = ((stock_data_copy['Close'] / stock_data_copy['Close'].shift(1)) - 1) * 100

    # Compute Running Average of Daily Returns
    stock_data_copy['Running Avg Return'] = stock_data_copy['Daily Return'].expanding().mean()

    # Compute Running Standard Deviation of Daily Returns
    stock_data_copy['Running Std Dev'] = stock_data_copy['Daily Return'].expanding().std()

    # Compute Daily Volatility
    stock_data_copy['Daily Volatility'] = ((stock_data_copy['High'] - stock_data_copy['Low']) / stock_data_copy['Close']) * 100

    # Compute Running Average of Daily Volatility
    stock_data_copy['Running Avg Volatility'] = stock_data_copy['Daily Volatility'].expanding().mean()

    # Compute Running Standard Deviation of Daily Volatility
    stock_data_copy['Running Std Dev Volatility'] = stock_data_copy['Daily Volatility'].expanding().std()

    return stock_data_copy

