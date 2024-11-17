import argparse
from utils.get_price_data import  get_historical_stock_data
from utils.stock_stats import stock_stats

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compute the average daily return for a stock.")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol (e.g., 'AAPL').")
    args = parser.parse_args()
    ticker_symbol = args.ticker

    # Fetch historical data
    ticker_name, historical_data = get_historical_stock_data(ticker_symbol)

    # Compute statistics
    enhanced_data = stock_stats(historical_data)

    # Compute the average daily return
    avg_daily_return = enhanced_data['Daily Return'].mean()

    # Output the result
    print(f"Average Daily Return for {ticker_name} ({ticker_symbol}): {avg_daily_return:.2f}%")

if __name__ == "__main__":
    main()

