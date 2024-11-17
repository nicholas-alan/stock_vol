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

        # Compute statistics for both stocks
        ticker1_stats = stock_stats(ticker1_data)
        ticker2_stats = stock_stats(ticker2_data)

        # Create a 2-column layout for the outputs
        col_a, col_b = st.columns(2)

        # Outputs for Ticker 1
        with col_a:
            st.subheader(f"Results for {ticker1_name} ({ticker1})")
            
            # Line Chart for Closing Price
            st.line_chart(data=pd.DataFrame({
                "Date": ticker1_stats['Date'],
                "Close": ticker1_stats['Close']
            }).set_index("Date"))

            # Display final statistics
            st.write("**Final Statistics:**")
            st.write(f"Total Daily Return: {ticker1_stats['Daily Return'].sum():.2f}%")
            st.write(f"Running Avg Return: {ticker1_stats['Running Avg Return'].iloc[-1]:.2f}%")
            st.write(f"Running Std Dev: {ticker1_stats['Running Std Dev'].iloc[-1]:.2f}%")
            st.write(f"Daily Volatility: {ticker1_stats['Daily Volatility'].iloc[-1]:.2f}%")
            st.write(f"Running Avg Volatility: {ticker1_stats['Running Avg Volatility'].iloc[-1]:.2f}%")
            st.write(f"Running Std Dev Volatility: {ticker1_stats['Running Std Dev Volatility'].iloc[-1]:.2f}%")

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker1_stats.head())

        # Outputs for Ticker 2
        with col_b:
            st.subheader(f"Results for {ticker2_name} ({ticker2})")
            
            # Line Chart for Closing Price
            st.line_chart(data=pd.DataFrame({
                "Date": ticker2_stats['Date'],
                "Close": ticker2_stats['Close']
            }).set_index("Date"))

            # Display final statistics
            st.write("**Final Statistics:**")
            st.write(f"Total Daily Return: {ticker2_stats['Daily Return'].sum():.2f}%")
            st.write(f"Running Avg Return: {ticker2_stats['Running Avg Return'].iloc[-1]:.2f}%")
            st.write(f"Running Std Dev: {ticker2_stats['Running Std Dev'].iloc[-1]:.2f}%")
            st.write(f"Daily Volatility: {ticker2_stats['Daily Volatility'].iloc[-1]:.2f}%")
            st.write(f"Running Avg Volatility: {ticker2_stats['Running Avg Volatility'].iloc[-1]:.2f}%")
            st.write(f"Running Std Dev Volatility: {ticker2_stats['Running Std Dev Volatility'].iloc[-1]:.2f}%")

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker2_stats.head())

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

