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

phase = input('Would you like to study a crescent or gibbous? ')
keywords = []
if phase.lower().startswith("c"):
    keywords.append('Waning Crescent')
    keywords.append('Waxing Crescent')
elif  phase.lower().startswith("g"):
    keywords.append('Waning Gibbous')
    keywords.append('Waxing Gibbous')
else:
    raise ValueError("Invalid phase")

def calculate_average_returns(stock_df, year, keywords):
    avg_return1 = stock_df[stock_df['Moon Phase'] == keywords[0]]['Daily_Return'].mean()
    avg_return2 = stock_df[stock_df['Moon Phase'] == keywords[1]]['Daily_Return'].mean()
    print(f"Average Returns during {keywords[0]} ({year}): {avg_return1:.2f}%")
    print(f"Average Returns during {keywords[1]} ({year}): {avg_return2:.2f}%")

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
    calculate_average_returns(stock_year, year, keywords)

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
fig.suptitle(keywords[0] + " and " + keywords[1] + " Volatility (2021-2023)")

# Plot data for each symbol and year on each subplot
for i, year in enumerate(range(2021, 2024)):
    for symbol, merged_data, color in zip(['NVIDIA', 'NASDAQ', 'SPY', 'TESLA', 'APPLE'], [merged_data_nvidia, merged_data_nasdaq, merged_data_spy, merged_data_tesla, merged_data_apple], ['blue', 'red', 'green', 'orange', 'purple']):
        stock_year = filter_and_calculate_returns(merged_data, year)
        axes[i].plot(stock_year[stock_year['Moon Phase'] == keywords[0]]['Date'],
                     stock_year[stock_year['Moon Phase'] == keywords[0]]['Daily_Return'],
                     label=f'{symbol} - {keywords[0]}', color=color, alpha=0.7)
        axes[i].plot(stock_year[stock_year['Moon Phase'] == keywords[1]]['Date'],
                     stock_year[stock_year['Moon Phase'] == keywords[1]]['Daily_Return'],
                     label=f'{symbol} - {keywords[1]}', color=color, linestyle='dashed', alpha=0.7)
    axes[i].set_title(f"Year {year}")
    axes[i].set_xlabel("Date")
    axes[i].set_ylabel("Volatility/Price Change (%)")
    axes[i].legend(fontsize='6')  # Adjust legend font size here

# Show the plots
plt.tight_layout()
plt.show()
