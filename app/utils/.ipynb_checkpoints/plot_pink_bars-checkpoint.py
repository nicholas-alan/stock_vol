import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter, MonthLocator

def plot_pink_bars(data, title="Yearly Reports", xlabel="Date", ylabel="Value", bar_width=120):
    """
    Create a bar chart with a dark background and 'deeppink' color scheme for yearly data.
    Assumes data is a pandas Series with a datetime index.
    
    Parameters:
      data (pd.Series): A datetime-indexed pandas Series.
      title (str): The title for the chart.
      xlabel (str): The label for the x-axis.
      ylabel (str): The label for the y-axis.
      bar_width (int): The width of the bars in days. (Adjust to make the bars wider or narrower.)
    
    Returns:
      Matplotlib figure: The figure object containing the plot.
    """
    # Ensure the index is datetime
    if not pd.api.types.is_datetime64_any_dtype(data.index):
        data.index = pd.to_datetime(data.index)
    
    # Set up the dark-themed plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Plot the bar chart. The bar width is set in days.
    ax.bar(data.index, data.values, color='deeppink', width=bar_width, alpha=0.6)
    
    # Set quarterly tick marks on the x-axis (every 3 months)
    year_locator = YearLocator()
    year_formatter = DateFormatter('%Y')
    ax.xaxis.set_major_locator(year_locator)
    ax.xaxis.set_major_formatter(year_formatter)

    # Set monthly grid-lines
    month_locator = MonthLocator()
    ax.xaxis.set_minor_locator(month_locator)
    ax.grid(True, which='minor', color='deeppink', linestyle='-', alpha=0.3)
    
    # Rotate tick labels for better readability
    ax.tick_params(axis='x', colors='deeppink', rotation=45)
    ax.tick_params(axis='y', colors='deeppink')
    
    # Set title and axis labels
    ax.set_title(title, color='deeppink', fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel, color='deeppink')
    ax.set_ylabel(ylabel, color='deeppink')
    
    # Customize the spines to match the color scheme
    for spine in ax.spines.values():
        spine.set_edgecolor('deeppink')
    
    # Add a grid
    ax.grid(True, color='deeppink', alpha=0.5)
    
    # Add a footer (left-aligned and near the bottom)
    fig.text(0.01, 0.01, "Created on www.NicholasAlan.com, DataSource: YahooFinance", 
             ha='left', color='deeppink', fontsize=10, fontstyle='italic')
    
    plt.tight_layout()
    return fig
