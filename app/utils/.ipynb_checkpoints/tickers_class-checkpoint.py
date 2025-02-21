class full_financial_statements:
    
    def __init__(self,tickers):
        import get_statements
        self.tickers = self._clean_tickers(tickers)
        self.portfolio_annual = self._fetch_annual(tickers)
        self.portfolio_quarterly = self._fetch_quarterly(tickers)
    def __repr__(self):
        return f"Portfolio Intialized for {self.tickers}"
    def _fetch_annual(self, tickers):
        return get_statements.tickers_statements(tickers)
    def _fetch_quarterly(self, tickers):
        return get_statements.tickers_quarterly_statements(tickers)
    def _clean_tickers(self, tickers):
        if type(tickers) == str: tickers = [tickers]
        return [x.strip().upper() for x in tickers]
    def __getattr__(self, name):
        name = name.split('.')
        ticker = name[0]
        time_period = name[1]
        statement_type = name[2]

        statements = {
            "income_statement": income_statement,
            "balance_sheet":balance_sheet,
            "cashflow_statement":cashflow_statement
        }
        
        if ticker in self.tickers:
            combined_time_statements = {"Annum":self.portfolio_annual[ticker],"Quarter":self.portfolio_quarterly[ticker]}
            return combined_time_statements
        raise AttributeError(f"""
        {name} was not found in Portfolio:
        {self.tickers}
        """)
        
        try: 
            if time_period in combined_time_statements.keys():
                return "hello from nested attribute"
        except:
            None
        try:
            if statement_type in statements:
                return "hello from nested statements"
        except:
            None
    #total_assets = self.x.quarterly.