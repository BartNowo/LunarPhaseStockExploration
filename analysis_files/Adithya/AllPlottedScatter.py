import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def read_stock_data(stock_symbol, path_to_stock_csv):
    stock_data = pd.read_csv(path_to_stock_csv)
    stock_data['Date'] = pd.to_datetime(stock_data['timestamp']).dt.date
    return stock_data

def merge_data(stock_data, moon_data):
    merged_data = pd.merge(moon_data, stock_data, on='Date', how='inner')
    merged_data['Date'] = pd.to_datetime(merged_data['Date'])
    return merged_data

def filter_and_calculate_returns(merged_stock_df, year):
    stock_year = merged_stock_df[merged_stock_df['Date'].dt.year == year]
    stock_year['Daily_Return'] = stock_year['close'].pct_change() * 100
    return stock_year

def calculate_average_returns(stock_df, year):
    full_moon_avg_return = stock_df[stock_df['Moon Phase'] == 'Full Moon']['Daily_Return'].mean()
    new_moon_avg_return = stock_df[stock_df['Moon Phase'] == 'New Moon']['Daily_Return'].mean()
    print(f"Average Returns during Full Moon ({year}): {full_moon_avg_return:.2f}%")
    print(f"Average Returns during New Moon ({year}): {new_moon_avg_return:.2f}%")

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"
path_to_stock_csv_nvidia = Path(__file__).parent.parent.parent / "data" / "nvidia.csv"
path_to_stock_csv_nasdaq = Path(__file__).parent.parent.parent / "data" / "nasdaq.csv"
path_to_stock_csv_spy = Path(__file__).parent.parent.parent / "data" / "spy.csv"
path_to_stock_csv_tesla = Path(__file__).parent.parent.parent / "data" / "tesla.csv"
path_to_stock_csv_apple = Path(__file__).parent.parent.parent / "data" / "apple.csv"

# Read moon data
moon_data = pd.read_csv(path_to_moon_csv)
moon_data['Date'] = pd.to_datetime(moon_data['Date']).dt.date

# Read stock data for each symbol
stock_data_nvidia = read_stock_data('NVIDIA', path_to_stock_csv_nvidia)
stock_data_nasdaq = read_stock_data('NASDAQ', path_to_stock_csv_nasdaq)
stock_data_spy = read_stock_data('SPY', path_to_stock_csv_spy)
stock_data_tesla = read_stock_data('TESLA', path_to_stock_csv_tesla)
stock_data_apple = read_stock_data('APPLE', path_to_stock_csv_apple)

# Merge moon data with stock data for each symbol
merged_data_nvidia = merge_data(stock_data_nvidia, moon_data)
merged_data_nasdaq = merge_data(stock_data_nasdaq, moon_data)
merged_data_spy = merge_data(stock_data_spy, moon_data)
merged_data_tesla = merge_data(stock_data_tesla, moon_data)
merged_data_apple = merge_data(stock_data_apple, moon_data)

# Calculate and print average returns for each symbol and year
for symbol, merged_data in zip(['NVIDIA', 'NASDAQ', 'SPY', 'TESLA', 'APPLE'], [merged_data_nvidia, merged_data_nasdaq, merged_data_spy, merged_data_tesla, merged_data_apple]):
    for year in range(2021, 2024):
        stock_year = filter_and_calculate_returns(merged_data, year)
        calculate_average_returns(stock_year, year)

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
fig.suptitle("Stocks New and Full Moon Daily Returns Scatter Plot (2021-2023)")

# Plot scatter data for each symbol and year on each subplot
for i, year in enumerate(range(2021, 2024)):
    for symbol, merged_data, color in zip(['NVIDIA', 'NASDAQ', 'SPY', 'TESLA', 'APPLE'], [merged_data_nvidia, merged_data_nasdaq, merged_data_spy, merged_data_tesla, merged_data_apple], ['blue', 'red', 'green', 'orange', 'purple']):
        stock_year = filter_and_calculate_returns(merged_data, year)
        axes[i].scatter(stock_year[stock_year['Moon Phase'] == 'Full Moon']['Date'],
                        stock_year[stock_year['Moon Phase'] == 'Full Moon']['Daily_Return'],
                        label=f'{symbol} - Full Moon', color=color, alpha=0.7)
        axes[i].scatter(stock_year[stock_year['Moon Phase'] == 'New Moon']['Date'],
                        stock_year[stock_year['Moon Phase'] == 'New Moon']['Daily_Return'],
                        label=f'{symbol} - New Moon', color=color, marker='x', alpha=0.7)
    axes[i].set_title(f"Year {year}")
    axes[i].set_xlabel("Date")
    axes[i].set_ylabel("Daily Return (%)")
    axes[i].legend()

# Save the scatter plot as a PNG image
plt.tight_layout()
plt.savefig('stocks_moon_daily_returns.png')
