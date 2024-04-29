import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"

# User input for stock symbol
stock_symbol = input("Enter the stock: (NVIDIA, NASDAQ, SPY, TESLA, or APPLE): ")

# Define paths to CSV files
path_to_moon_csv = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"
path_to_stock_csv = None

# Assign the correct path based on user input
if stock_symbol.lower() == "nvidia":
    path_to_stock_csv = Path(__file__).parent.parent.parent / "data" / "nvidia.csv"
elif stock_symbol.lower() == "nasdaq":
    path_to_stock_csv = Path(__file__).parent.parent.parent / "data" / "nasdaq.csv"
elif stock_symbol.lower() == "spy":
    path_to_stock_csv = Path(__file__).parent.parent.parent / "data" / "spy.csv"
elif stock_symbol.lower() == "apple":
    path_to_stock_csv = Path(__file__).parent.parent.parent / "data" / "apple.csv"
elif stock_symbol.lower() == "tesla":
    path_to_stock_csv = Path(__file__).parent.parent.parent / "data" / "tesla.csv"
else:
    print("Invalid stock symbol. Please enter one of the following: NVIDIA, NASDAQ, SPY, TESLA, or APPLE")
    exit()

# Read stock data from CSV
stock_data_df = pd.read_csv(path_to_stock_csv)

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# depending on the stock, reads in stock data csv file and loads into pandas dataframe
stock_data_df = pd.read_csv(path_to_stock_csv)

# converts the date columns to datetime type
moon_phases_df['Date'] = pd.to_datetime(moon_phases_df['Date']).dt.date
stock_data_df['Date'] = pd.to_datetime(stock_data_df['timestamp']).dt.date

# merges the dataframes on the data column the inner means it will include only dates
# present in both dataframes
merged_stock_df = pd.merge(
    moon_phases_df, stock_data_df, on='Date', how='inner')

merged_stock_df['Date'] = pd.to_datetime(merged_stock_df['Date'])

def filter_and_calculate_returns(merged_stock_df, year):
    stock_year = merged_stock_df[merged_stock_df['Date'].dt.year == year]
    stock_year['Daily_Return'] = stock_year['close'].pct_change() * 100
    return stock_year

# Call the function for each year
stock_2021 = filter_and_calculate_returns(merged_stock_df, 2021)
stock_2022 = filter_and_calculate_returns(merged_stock_df, 2022)
stock_2023 = filter_and_calculate_returns(merged_stock_df, 2023)

def calculate_average_returns(stock_df, year):
    full_moon_avg_return = stock_df[stock_df['Moon Phase'] == 'Full Moon']['Daily_Return'].mean()
    new_moon_avg_return = stock_df[stock_df['Moon Phase'] == 'New Moon']['Daily_Return'].mean()
    print(f"Average Returns during Full Moon ({year}): {full_moon_avg_return:.2f}%")
    print(f"Average Returns during New Moon ({year}): {new_moon_avg_return:.2f}%")

# Calculate average returns for each year
calculate_average_returns(stock_2021, 2021)
calculate_average_returns(stock_2022, 2022)
calculate_average_returns(stock_2023, 2023)


# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
fig.suptitle(stock_symbol.upper() + " Stock New and Full Moon Daily Returns and Volatility (2021-2023)")

# Plot for 2021
axes[0].plot(stock_2021[stock_2021['Moon Phase'] == 'Full Moon']['Date'],
             stock_2021[stock_2021['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[0].plot(stock_2021[stock_2021['Moon Phase'] == 'New Moon']['Date'],
             stock_2021[stock_2021['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[0].set_title("2021")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Daily Return (%)")
axes[0].legend()

# Plot for 2022
axes[1].plot(stock_2022[stock_2022['Moon Phase'] == 'Full Moon']['Date'],
             stock_2022[stock_2022['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[1].plot(stock_2022[stock_2022['Moon Phase'] == 'New Moon']['Date'],
             stock_2022[stock_2022['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[1].set_title("2022")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Daily Return (%)")
axes[1].legend()

# Plot for 2023
axes[2].plot(stock_2023[stock_2023['Moon Phase'] == 'Full Moon']['Date'],
             stock_2023[stock_2023['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[2].plot(stock_2023[stock_2023['Moon Phase'] == 'New Moon']['Date'],
             stock_2023[stock_2023['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[2].set_title("2023")
axes[2].set_xlabel("Date")
axes[2].set_ylabel("Daily Return (%)")
axes[2].legend()


# Show the plots
plt.tight_layout()
plt.show()