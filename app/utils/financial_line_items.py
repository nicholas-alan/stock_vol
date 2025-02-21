import pandas as pd
import get_statements

def financial_line_items(stocks):
    """
    Parameters: stocks = list of 
    """
    ### Fetches Statements of n-number of stocks and stores in two dictionaries of annual and quarterly statements.
    portfolio_statements = get_statements.tickers_statements(stocks)
    portfolio_quarterly_statements = get_statements.tic(stocks)

    balance_sheets = get_statements.tickers_balance_sheets(portfolio_statements)
    income_statements = get_statements.tickers_income_statements(portfolio_statements)
    cash_flow_statements = get_statements.tickers_cash_flow_statements(portfolio_statements)

    quar_balance_sheets = get_statements.tickers_quarterly_balance_sheets(portfolio_quarterly_statements)
    quar_income_statements = get_statements.tickers_quarterly_income_statements(portfolio_quarterly_statements)
    quar_cash_flow_statements = get_statements.tickers_quarterly_cash_flow_statements(portfolio_quarterly_statements)

def return_common_line_items(statement):

    assets = [(x, statement[x].loc['Total Assets']) for x in statement.keys()]
    liabilities = [(x, statement[x].loc['Total Debt']) for x in statement.keys()]
    inventory = [(x, statement[x].loc['Inventory']) for x in statement.keys()]
    current_assets = [(x, statement[x].loc['Current Assets']) for x in statement.keys()]
    current_debt = [(x, statement[x].loc['Current Debt']) for x in statement.keys()]

    return assets, liabilities, inventory, current_assets, current_debt

    