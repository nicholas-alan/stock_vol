import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def get_historical_stock_data(ticker_symbol):
    """
    Fetch 1-year historical stock price data for a given stock ticker.

    Parameters:
        ticker_symbol (str): The stock ticker symbol (e.g., "AAPL").

    Returns:
        tuple: A tuple containing the ticker name (str) and a Pandas DataFrame with historical price data.
    """
    # Normalize the ticker symbol
    ticker_symbol = ticker_symbol.strip().upper()

    # Create a Ticker object and fetch data
    stock = yf.Ticker(ticker_symbol)
    ticker_name = stock.info.get("shortName", ticker_symbol)

    # Calculate the date range
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365*3)).strftime('%Y-%m-%d')

    # Fetch historical data
    historical_data = stock.history(start=start_date, end=end_date)

    # Format the data
    historical_data.reset_index(inplace=True)
    historical_data = historical_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    return ticker_name, historical_data

