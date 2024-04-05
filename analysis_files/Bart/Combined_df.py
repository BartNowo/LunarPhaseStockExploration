import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

# this file is a good template to help you guys get started it
# loads in files in df and merges them and simple plotting

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / \
    "data" / "moon_phases.csv"
path_to_apple_csv = Path(__file__).parent.parent.parent / \
    "data" / "apple_df.csv"
path_to_spy_csv = Path(__file__).parent.parent.parent / "data" / "spy_df.csv"
path_to_nvidia_csv = Path(
    __file__).parent.parent.parent / "data" / "nvidia_df.csv"
path_to_tesla_csv = Path(__file__).parent.parent.parent / \
    "data" / "tesla_df.csv"
path_to_nasdaq_csv = Path(
    __file__).parent.parent.parent / "data" / "nasdaq_df.csv"

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# reads in stock data csv file and loads into pandas dataframe
apple_data_df = pd.read_csv(path_to_apple_csv)
nasdaq_data_df = pd.read_csv(path_to_nasdaq_csv)
nvidia_data_df = pd.read_csv(path_to_nvidia_csv)
spy_data_df = pd.read_csv(path_to_spy_csv)
tesla_data_df = pd.read_csv(path_to_tesla_csv)

dataframes = [(apple_data_df, "Apple"), (nasdaq_data_df, "NASDAQ"), (nvidia_data_df, "Nvidia"),
              (spy_data_df, "SPY"), (tesla_data_df, "Tesla")]

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(
    20, 10), sharex=True)  # Share the x-axis for uniform scaling
axes = axes.flatten()

for ax, (df, title) in zip(axes[:-1], dataframes):
    # Ensure date columns are parsed as datetime if not already
    df['Start Date'] = pd.to_datetime(df['Start Date'])
    df['End Date'] = pd.to_datetime(df['End Date'])

    for _, row in df.iterrows():
        color = 'green' if row['Price Change'] > 0 else 'red'
        # Plot a line from the start to the end of the cycle
        ax.plot([row['Start Date'], row['End Date']], [
                row['Start Price'], row['End Price']], '-o', color=color)

    ax.set_title(title + " Positive vs Negative Returns")
    ax.set_ylabel('Stock Price ($)')

    # Set date format on the x-axis
    ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(
        interval=2))  # Adjust the interval as needed
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    fig.autofmt_xdate()  # Rotate date labels to prevent overlap


axes[-1].axis('off')
# Add a common X label
fig.text(0.5, 0.04, 'Date', ha='center', va='center')

# Adjust layout
plt.tight_layout()
plt.savefig(Path(__file__).parent / 'figure1_Bart.png')
plt.show()
