import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def get_fin_statements(ticker_symbol, start_date=None, end_date=None):
    """Fetches the 3 financial statements, annual, via YFinance
    Parameters:
        ticker_symbol (str): stock ticker "AAPL"
        start_date (datetime)
        end_date (datetime)

    Returns:
        tuple containing
        ticker_name and a dictionary containing statments.
    """
    ticker_symbol = ticker_symbol.strip().upper()

    stock = yf.Ticker(ticker_symbol)

    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow_statement = stock.cashflow

    statements = {
        "income_statement": income_statement,
        "balance_sheet":balance_sheet,
        "cashflow_statement":cashflow_statement
    }
    return statements

def tickers_statements(tickers):
    if type(tickers) == str: tickers = [tickers]
    tickers = [x.strip().upper() for x in tickers]
    return {x:get_fin_statements(x) for x in tickers}
    #return [get_fin_statements(x) for x in tickers]

def tickers_income_statements(tickers_statements):
    return {
    ticker: data['income_statement']
    for ticker, data in tickers_statements.items()
}

def tickers_balance_sheets(tickers_statements):
    return {
    ticker: data['balance_sheet']
    for ticker, data in tickers_statements.items()
}

def tickers_cash_flow_statements(tickers_statements):
    return {
    ticker: data['cashflow_statement']
    for ticker, data in tickers_statements.items()
}


def get_quarterly_fin_statements(ticker_symbol, start_date=None, end_date=None):
    """Fetches the 3 quarterly financial statements via YFinance
    
    Parameters:
        ticker_symbol (str): stock ticker "AAPL"
        start_date (datetime)
        end_date (datetime)

    Returns:
        tuple containing
        ticker_name and a dictionary containing quarterly statements.
    """
    ticker_symbol = ticker_symbol.strip().upper()

    stock = yf.Ticker(ticker_symbol)

    quarterly_income_statement = stock.quarterly_income_stmt
    quarterly_balance_sheet = stock.quarterly_balance_sheet
    quarterly_cashflow_statement = stock.quarterly_cashflow

    # Create dictionary to hold quarterly data
    quarterly_statements = {
        "quarterly_income_statement": quarterly_income_statement,
        "quarterly_balance_sheet": quarterly_balance_sheet,
        "quarterly_cashflow_statement": quarterly_cashflow_statement
    }
    
    return quarterly_statements

def tickers_quarterly_statements(tickers):
    """Fetches quarterly financial statements for a list of tickers."""
    if type(tickers) == str: tickers = [tickers]
    tickers = [x.strip().upper() for x in tickers]
    return {x:get_quarterly_fin_statements(x) for x in tickers}

def tickers_quarterly_income_statements(tickers_quarterly_statements):
    """Extract quarterly income statements from fetched data."""
    return {
    ticker:data['quarterly_income_statement']
    for ticker, data in tickers_quarterly_statements.items()
}

def tickers_quarterly_balance_sheets(tickers_quarterly_statements):
    """Extract quarterly balance sheets from fetched data."""
    return {
    ticker:data['quarterly_balance_sheet']
    for ticker, data in tickers_quarterly_statements.items()
}

def tickers_quarterly_cash_flow_statements(tickers_quarterly_statements):
    """Extract quarterly cash flow statements from fetched data."""
    return {
    ticker:data['quarterly_cashflow_statement']
    for ticker, data in tickers_quarterly_statements.items()
}

