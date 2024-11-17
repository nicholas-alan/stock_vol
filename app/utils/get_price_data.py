import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def get_historical_stock_data(ticker_symbol, start_date=None, end_date=None):
    """
    Fetch historical stock price data for a given stock ticker within a specified date range.
    
    Parameters:
        ticker_symbol (str): The stock ticker symbol (e.g., "AAPL").
        start_date (datetime.date, optional): The start date for the data. Defaults to 3 years ago.
        end_date (datetime.date, optional): The end date for the data. Defaults to today.

    Returns:
        tuple: A tuple containing the ticker name (str) and a Pandas DataFrame with historical price data.
    """
    # Normalize the ticker symbol
    ticker_symbol = ticker_symbol.strip().upper()

    # Create a Ticker object and fetch data
    stock = yf.Ticker(ticker_symbol)
    ticker_name = stock.info.get("shortName", ticker_symbol)

    # Default to 3 years back if no start_date is provided
    if not start_date:
        start_date = datetime.now() - timedelta(days=365 * 3)
    if not end_date:
        end_date = datetime.now()

    # Ensure dates are in the correct string format for yfinance
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    # Fetch historical data
    historical_data = stock.history(start=start_date, end=end_date)

    # Format the data
    historical_data.reset_index(inplace=True)
    historical_data = historical_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    return ticker_name, historical_data

