from oop_financial_statements import TickerFinancials

def financial_ratios(ticker_thing):
    name = ticker_thing.ticker_symbol

    assets = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Total Assets')
    debt = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Total Debt')
    cur_assets = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Current Assets')
    cur_debt = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Current Debt')
    inventory = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Inventory')
    cur_liab = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Current Liabilities')
    equity = ticker_thing.get_quarterly_line_item(
        'balance_sheet', 'Stockholders Equity')
    net_income = ticker_thing.get_quarterly_line_item(
        'income', 'Net Income')
    operating_income = ticker_thing.get_quarterly_line_item(
        'income', 'Operating Income')
    interest_expense = ticker_thing.get_quarterly_line_item(
        'income', 'Interest Expense')

    acid_test = (cur_assets[1] - inventory[1]) / cur_liab[1]
    current_ratio = cur_assets[1] / cur_liab[1]
    debt_equity = debt[1] / equity[1]
    return_on_assets = net_income[1] / assets[1]
    return_on_equity = net_income[1] / equity[1]
    interest_coverage = operating_income[1] / interest_expense[1]
    
    ratios = {
        'Acid Test':acid_test,
        'Current Ratio':current_ratio,
        'Debt to Equity':debt_equity,
        'Return on Assets':return_on_assets,
        'Return on Equity':return_on_equity,
        'Interest Coverage':interest_coverage
    
    }
    

    return name, ratios