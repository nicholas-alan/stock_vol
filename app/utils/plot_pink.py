
import pandas as pd
import matplotlib.pyplot as plt

def plot_pink(data, x_column, y_column, title="Stock Price Chart", xlabel="Date", ylabel="Price"):
    """
    Create a visually striking line graph with a black background and 'deeppink' color scheme.

    Parameters:
        data (pd.DataFrame): The data to plot.
        x_column (str): The name of the column to use for the x-axis.
        y_column (str): The name of the column to use for the y-axis.
        title (str): The title of the graph.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        Matplotlib figure: The figure object containing the plot.
    """
    # Ensure the x_column is in datetime format if it represents dates
    if pd.api.types.is_datetime64_any_dtype(data[x_column]) == False:
        data[x_column] = pd.to_datetime(data[x_column])

    # Set up the plot with a dark background
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot the data
    ax.plot(data[x_column], data[y_column], color='deeppink', linewidth=2)
    ax.grid(True, color='deeppink', alpha=0.5)

    # Customize the plot with titles and labels
    ax.set_title(title, color='deeppink', fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel, color='deeppink')
    ax.set_ylabel(ylabel, color='deeppink')

    # Customize ticks and spines to match the color scheme
    ax.tick_params(axis='x', colors='deeppink')
    ax.tick_params(axis='y', colors='deeppink')
    for spine in ax.spines.values():
        spine.set_edgecolor('deeppink')

    # Tight layout for better spacing
    plt.tight_layout()

    return fig
