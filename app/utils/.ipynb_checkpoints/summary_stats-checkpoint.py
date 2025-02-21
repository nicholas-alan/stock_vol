import pandas as pd

def generate_summary_table(bottom_row1, bottom_row2, stock1_name, stock2_name):
    """
    Generate a summary table comparing key statistics for two stocks.

    Parameters:
        bottom_row1 (pd.Series): Last row of statistics for Stock 1.
        bottom_row2 (pd.Series): Last row of statistics for Stock 2.
        stock1_name (str): Name of Stock 1.
        stock2_name (str): Name of Stock 2.

    Returns:
        pd.DataFrame: Summary statistics table.
    """
    summary_data = {
        "Statistic": [
            "Avg. Daily Return",
            "Standard Deviation (Return)",
            "Avg. Daily Volatility",
            "Standard Deviation (Volatility)"
        ],
        stock1_name: [
            bottom_row1['Running Avg Return'],
            bottom_row1['Running Std Dev'],
            bottom_row1['Running Avg Volatility'],
            bottom_row1['Running Std Dev Volatility']
        ],
        stock2_name: [
            bottom_row2['Running Avg Return'],
            bottom_row2['Running Std Dev'],
            bottom_row2['Running Avg Volatility'],
            bottom_row2['Running Std Dev Volatility']
        ]

        
    }
    return pd.DataFrame(summary_data)

