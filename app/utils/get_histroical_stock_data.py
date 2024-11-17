import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def get_historical_stock_data(ticker_symbol):
    """
    Fetch 1-year historical stock price data for a given stock ticker with validation and error handling.

    Parameters:
        ticker_symbol (str): The stock ticker symbol (e.g., "AAPL" for Apple).

    Returns:
        tuple: A tuple containing the ticker name (str) and a Pandas DataFrame with historical price data.
    """
    try:
        # Validate input
        if not isinstance(ticker_symbol, str) or not ticker_symbol.strip():
            raise ValueError("Invalid ticker symbol. Please provide a valid stock ticker as a string.")

        ticker_symbol = ticker_symbol.strip().upper()  # Normalize ticker input

        # Create Ticker object
        stock = yf.Ticker(ticker_symbol)

        # Check if the Ticker object has valid data
        if stock.info is None or 'regularMarketPrice' not in stock.info:
            raise ValueError("Ticker Not Found on Yahoo Finance Data Platform")

        # Get ticker name
        ticker_name = stock.info.get("shortName", ticker_symbol)

        # Calculate the date range
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=365*3)).strftime('%Y-%m-%d')

        # Fetch historical data
        historical_data = stock.history(start=start_date, end=end_date)

        # Check if data is returned
        if historical_data.empty:
            raise ValueError("No historical data found for the ticker")

        # Format the data
        historical_data.reset_index(inplace=True)
        historical_data = historical_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

        return ticker_name, historical_data

    except ValueError as ve:
        # Handle validation and missing ticker errors
        raise ValueError(str(ve))
    except Exception as e:
        # Catch any unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

