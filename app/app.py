import streamlit as st
from utils.get_price_data import get_historical_stock_data
from utils.stock_stats import stock_stats
import pandas as pd

# Function to process and display results
def go_time(ticker1, ticker2, output_container):
    with output_container:
        # Fetch and process data for both tickers
        ticker1_name, ticker1_data = get_historical_stock_data(ticker1)
        ticker2_name, ticker2_data = get_historical_stock_data(ticker2)

        # Compute statistics
        ticker1_stats = stock_stats(ticker1_data)
        ticker2_stats = stock_stats(ticker2_data)

        # Average daily return for both tickers
        avg_daily_return_ticker1 = ticker1_stats['Daily Return'].mean()
        avg_daily_return_ticker2 = ticker2_stats['Daily Return'].mean()

        # Create new 2-column layout for the results
        col_a, col_b = st.columns(2)

        # Chart for Ticker 1
        with col_a:
            st.write(f"Closing Prices for {ticker1_name} ({ticker1})")
            st.line_chart(data=pd.DataFrame({
                "Date": ticker1_data['Date'],
                "Close": ticker1_data['Close']
            }).set_index("Date"))
            st.write(f"**Average Daily Return for {ticker1_name} ({ticker1}):** {avg_daily_return_ticker1:.2f}%")

        # Chart for Ticker 2
        with col_b:
            st.write(f"Closing Prices for {ticker2_name} ({ticker2})")
            st.line_chart(data=pd.DataFrame({
                "Date": ticker2_data['Date'],
                "Close": ticker2_data['Close']
            }).set_index("Date"))
            st.write(f"**Average Daily Return for {ticker2_name} ({ticker2}):** {avg_daily_return_ticker2:.2f}%")

# Main app layout
st.title("Stock Comparison App")

# First container for inputs
input_container = st.container()
output_container = st.container()

# Input fields and "GO" button inside the input container
with input_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker1 = st.text_input("Stock Ticker 1 (e.g., AAPL):", value="AAPL")
    with col3:
        ticker2 = st.text_input("Stock Ticker 2 (e.g., TSLA):", value="TSLA")

    # GO button in the center column
    with col2:
        # Inject CSS to center the button
        st.markdown("""
            <style>
            .center-button {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="center-button">', unsafe_allow_html=True)
        if st.button("GO", use_container_width=True):
            # Trigger go_time and pass the output_container for results
            go_time(ticker1, ticker2, output_container)
        st.markdown('</div>', unsafe_allow_html=True)

