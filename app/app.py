import matplotlib.pyplot as plt
import streamlit as st
from utils.get_price_data import get_historical_stock_data
from utils.stock_stats import stock_stats
from utils.summary_stats import generate_summary_table
import pandas as pd
import datetime

def plot_closing_prices(data, stock_name):
    """
    Create a Matplotlib plot for the closing prices of a stock.

    Parameters:
        data (pd.DataFrame): Stock data containing 'Date' and 'Close' columns.
        stock_name (str): The name of the stock for labeling.

    Returns:
        Matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(data['Date'], data['Close'], label=f'{stock_name} Closing Prices', color='blue', linewidth=2)
    ax.set_title(f'{stock_name} Closing Prices Over Time', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Closing Price (USD)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(fontsize=10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

# Custom CSS to widen the app
def widen_app():
    st.markdown(
        """
        <style>
        /* Adjust the main content width */
        .main {
            max-width: 90%; /* Set to 80-90% of the viewport width */
            margin: 0 auto; /* Center align */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


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
        col_a, col_b = st.columns(2)

        # Outputs for Ticker 1
        with col_a:
            st.subheader(f"Results for {ticker1_name} ({ticker1})")
            
            # Line Chart for Closing Price
                "Date": ticker1_stats['Date'],
                "Close": ticker1_stats['Close']
            }).set_index("Date"))

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker1_stats.head())

        # Outputs for Ticker 2
        with col_b:
            st.subheader(f"Results for {ticker2_name} ({ticker2})")
            
            # Line Chart for Closing Price
                "Date": ticker2_stats['Date'],
                "Close": ticker2_stats['Close']
            }).set_index("Date"))

            # Display DataFrame Head
            st.write("**DataFrame Head:**")
            st.write(ticker2_stats.head())

    with tables_container:
            # Summary Table 
            summary_table = generate_summary_table(
                ticker1_stats.iloc[-1],
                ticker2_stats.iloc[-1],
                ticker1_name,
                ticker2_name
            )
            st.table(summary_table)

# Main app layout
st.title("Stock Comparison App")
widen_app()
# First container for inputs
input_container = st.container()
output_container = st.container()
tables_container = st.container()

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

