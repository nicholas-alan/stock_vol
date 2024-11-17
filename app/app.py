import streamlit as st
from utils.get_price_data import get_historical_stock_data
from utils.stock_stats import stock_stats
from utils.summary_stats import generate_summary_table
import pandas as pd
import datetime

# Function to process and display results
def go_time(ticker1, ticker2, output_container):
    with output_container:
        # Fetch and process data for both tickers
        ticker1_name, ticker1_data = get_historical_stock_data(ticker1, start_date, end_date)
        ticker2_name, ticker2_data = get_historical_stock_data(ticker2, start_date, end_date)
        # Compute statistics for both stocks
        ticker1_stats = stock_stats(ticker1_data)
        ticker2_stats = stock_stats(ticker2_data)

        # Create a 2-column layout for the outputs
        col_a, col_b, col_c = st.columns(3)

        # Outputs for Ticker 1
        with col_a:
            st.subheader(f"Results for {ticker1_name} ({ticker1})")
            
            # Line Chart for Closing Price
            st.line_chart(data=pd.DataFrame({
                "Date": ticker1_stats['Date'],
                "Close": ticker1_stats['Close']
            }).set_index("Date"))

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker1_stats.head())

        # Outputs for Ticker 2
        with col_c:
            st.subheader(f"Results for {ticker2_name} ({ticker2})")
            
            # Line Chart for Closing Price
            st.line_chart(data=pd.DataFrame({
                "Date": ticker2_stats['Date'],
                "Close": ticker2_stats['Close']
            }).set_index("Date"))

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker2_stats.head())

            # Summary Table in the Middle
            summary_table = generate_summary_table(
                ticker1_stats.iloc[-1],
                ticker2_stats.iloc[-1],
                ticker1_name,
                ticker2_name
            )
            st.table(summary_table)

# Main app layout
st.title("Stock Comparison App")

# First container for inputs
input_container = st.container()
output_container = st.container()

#Input Fields for Date Range Defaults
today = datetime.date.today()
default_start_date = today - datetime.timedelta(days=3*365)  # Three years ago


# Input fields and "GO" button inside the input container
with input_container:
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker1 = st.text_input("Stock Ticker 1 (e.g., AAPL):", value="AAPL")
        start_date = st.date_input("Start Date", value=default_start_date)
    with col3:
        ticker2 = st.text_input("Stock Ticker 2 (e.g., TSLA):", value="TSLA")
        end_date = st.date_input("End Date", value=today)

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

