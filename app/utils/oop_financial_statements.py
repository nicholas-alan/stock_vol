import yfinance as yf
import pandas as pd

class TickerFinancials:
    def __init__(self, ticker_symbol):
        """
        Initialize the class with the ticker symbol.
        Fetches quarterly and annual financial statements.
        """
        self.ticker_symbol = ticker_symbol.strip().upper()
        self.stock = yf.Ticker(self.ticker_symbol)
        
        # Fetch quarterly and annual financial statements
        self.quarterly_income_statement = self.stock.quarterly_income_stmt
        self.quarterly_balance_sheet = self.stock.quarterly_balance_sheet
        self.quarterly_cashflow_statement = self.stock.quarterly_cashflow
        self.annual_income_statement = self.stock.income_stmt
        self.annual_balance_sheet = self.stock.balance_sheet
        self.annual_cashflow_statement = self.stock.cashflow

    def get_quarterly_line_item(self, statement_type, line_item):
        """
        Fetches a specific line item from the given quarterly financial statement.
        
        Parameters:
            statement_type (str): The type of statement ('income', 'balance_sheet', 'cashflow').
            line_item (str): The line item (e.g., 'Total Assets', 'Revenue', etc.).
        
        Returns:
            The value for the requested line item from the specific statement.
        """
        # Choose the correct quarterly statement
        statement_map = {
            'income': self.quarterly_income_statement,
            'balance_sheet': self.quarterly_balance_sheet,
            'cashflow': self.quarterly_cashflow_statement
        }
        
        # Check if the statement type is valid
        if statement_type not in statement_map:
            raise ValueError(f"Invalid statement type: {statement_type}. Choose from 'income', 'balance_sheet', or 'cashflow'.")
        
        statement = statement_map[statement_type]
        
        # Check if the line item exists in the statement
        if line_item not in statement.index:
            raise ValueError(f"Line item '{line_item}' not found in {statement_type} statement.")
        
        # Return the line item values (quarterly data)
        return self.ticker_symbol, statement.loc[line_item]
    
    def get_all_quarterly_data(self):
        """
        Returns all quarterly data for income, balance sheet, and cash flow statements.
        """
        return {
            "quarterly_income_statement": self.quarterly_income_statement,
            "quarterly_balance_sheet": self.quarterly_balance_sheet,
            "quarterly_cashflow_statement": self.quarterly_cashflow_statement
        }
    
    def get_annual_line_item(self, statement_type, line_item):
        """
        Fetches a specific line item from the given annual financial statement.
        
        Parameters:
            statement_type (str): The type of statement ('income', 'balance_sheet', 'cashflow').
            line_item (str): The line item (e.g., 'Total Assets', 'Revenue', etc.).
        
        Returns:
            The value for the requested line item from the specific statement.
        """
        # Choose the correct annual statement
        statement_map = {
            'income': self.annual_income_statement,
            'balance_sheet': self.annual_balance_sheet,
            'cashflow': self.annual_cashflow_statement
        }
        
        # Check if the statement type is valid
        if statement_type not in statement_map:
            raise ValueError(f"Invalid statement type: {statement_type}. Choose from 'income', 'balance_sheet', or 'cashflow'.")
        
        statement = statement_map[statement_type]
        
        # Check if the line item exists in the statement
        if line_item not in statement.index:
            raise ValueError(f"Line item '{line_item}' not found in {statement_type} statement.")
        
        # Return the line item values (annual data)
        return statement.loc[line_item]

    def get_all_annual_data(self):
        """
        Returns all annual data for income, balance sheet, and cash flow statements.
        """
        return {
            "annual_income_statement": self.annual_income_statement,
            "annual_balance_sheet": self.annual_balance_sheet,
            "annual_cashflow_statement": self.annual_cashflow_statement
        }
