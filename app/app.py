import streamlit as st
from utils.get_price_data import  get_historical_stock_data
from utils.stock_stats import stock_stats
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Stock Comparison App")

# Side-by-side input fields for stock tickers
col1, col2 = st.columns(2)
with col1:
    ticker1 = st.text_input("Stock Ticker 1 (e.g., AAPL):", value="AAPL")
with col2:
    ticker2 = st.text_input("Stock Ticker 2 (e.g., TSLA):", value="TSLA")

# GO button in the center
if st.button("GO"):
    # Fetch and process data for both tickers
    ticker1_name, ticker1_data = get_historical_stock_data(ticker1)
    ticker2_name, ticker2_data = get_historical_stock_data(ticker2)

    # Compute statistics
    ticker1_stats = stock_stats(ticker1_data)
    ticker2_stats = stock_stats(ticker2_data)

    # Average daily return for both tickers
    avg_daily_return_ticker1 = ticker1_stats['Daily Return'].mean()
    avg_daily_return_ticker2 = ticker2_stats['Daily Return'].mean()

    # Display side-by-side figures
    fig_col1, fig_col2 = st.columns(2)

    # Figure for Ticker 1
    with fig_col1:
        st.write(f"Closing Prices for {ticker1_name} ({ticker1})")
        plt.figure(figsize=(5, 4))
        plt.plot(ticker1_data['Date'], ticker1_data['Close'], label=f"{ticker1_name} (Close)", color="blue")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.title(f"{ticker1_name} Closing Prices")
        plt.legend()
        st.pyplot(plt)
        st.write(f"**Average Daily Return for {ticker1_name} ({ticker1}):** {avg_daily_return_ticker1:.2f}%")

    # Figure for Ticker 2
    with fig_col2:
        st.write(f"Closing Prices for {ticker2_name} ({ticker2})")
        plt.figure(figsize=(5, 4))
        plt.plot(ticker2_data['Date'], ticker2_data['Close'], label=f"{ticker2_name} (Close)", color="green")
        plt.xlabel("Date")
        plt.ylabel("Closing Price (USD)")
        plt.title(f"{ticker2_name} Closing Prices")
        plt.legend()
        st.pyplot(plt)
        st.write(f"**Average Daily Return for {ticker2_name} ({ticker2}):** {avg_daily_return_ticker2:.2f}%")

