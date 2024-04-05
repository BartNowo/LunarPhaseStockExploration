import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"
path_to_nvidia_csv = Path(__file__).parent.parent.parent / "data" / "nvidia.csv"
# path_to_nasdaq_csv = Path(__file__).parent.parent.parent / "data" / "nasdaq.csv"
# path_to_spy_csv = Path(__file__).parent.parent.parent / "data" / "spy.csv"
# path_to_apple_csv = Path(__file__).parent.parent.parent / "data" / "apple.csv"

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# depending on the stock, reads in stock data csv file and loads into pandas dataframe
nvidia_data_df = pd.read_csv(path_to_nvidia_csv)

# converts the date columns to datetime type
moon_phases_df['Date'] = pd.to_datetime(moon_phases_df['Date']).dt.date
nvidia_data_df['Date'] = pd.to_datetime(nvidia_data_df['timestamp']).dt.date

# merges the dataframes on the data column the inner means it will include only dates
# present in both dataframes
merged_nvidia_df = pd.merge(
    moon_phases_df, nvidia_data_df, on='Date', how='inner')

merged_nvidia_df['Date'] = pd.to_datetime(merged_nvidia_df['Date'])

# Filter data by year
nvidia_2020 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2020]
nvidia_2021 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2021]
nvidia_2022 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2022]
nvidia_2023 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2023]

# Calculate daily returns
nvidia_2020['Daily_Return'] = nvidia_2020['close'].pct_change() * 100
nvidia_2021['Daily_Return'] = nvidia_2021['close'].pct_change() * 100
nvidia_2022['Daily_Return'] = nvidia_2022['close'].pct_change() * 100
nvidia_2023['Daily_Return'] = nvidia_2023['close'].pct_change() * 100

# Filter data by year
nvidia_2020 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2020]
nvidia_2021 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2021]
nvidia_2022 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2022]
nvidia_2023 = merged_nvidia_df[merged_nvidia_df['Date'].dt.year == 2023]

# Calculate daily returns
nvidia_2020['Daily_Return'] = nvidia_2020['close'].pct_change() * 100
nvidia_2021['Daily_Return'] = nvidia_2021['close'].pct_change() * 100
nvidia_2022['Daily_Return'] = nvidia_2022['close'].pct_change() * 100
nvidia_2023['Daily_Return'] = nvidia_2023['close'].pct_change() * 100

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
fig.suptitle("NVIDIA Stock Daily Returns (2021-2023)")

# Plot for 2021
axes[0].plot(nvidia_2021[nvidia_2021['Moon Phase'] == 'Full Moon']['Date'],
             nvidia_2021[nvidia_2021['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[0].plot(nvidia_2021[nvidia_2021['Moon Phase'] == 'New Moon']['Date'],
             nvidia_2021[nvidia_2021['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[0].set_title("2021")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Daily Return (%)")
axes[0].legend()

# Plot for 2022
axes[1].plot(nvidia_2022[nvidia_2022['Moon Phase'] == 'Full Moon']['Date'],
             nvidia_2022[nvidia_2022['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[1].plot(nvidia_2022[nvidia_2022['Moon Phase'] == 'New Moon']['Date'],
             nvidia_2022[nvidia_2022['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[1].set_title("2022")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Daily Return (%)")
axes[1].legend()

# Plot for 2023
axes[2].plot(nvidia_2023[nvidia_2023['Moon Phase'] == 'Full Moon']['Date'],
             nvidia_2023[nvidia_2023['Moon Phase'] == 'Full Moon']['Daily_Return'],
             label='Full Moon', color='blue')
axes[2].plot(nvidia_2023[nvidia_2023['Moon Phase'] == 'New Moon']['Date'],
             nvidia_2023[nvidia_2023['Moon Phase'] == 'New Moon']['Daily_Return'],
             label='New Moon', color='red')
axes[2].set_title("2023")
axes[2].set_xlabel("Date")
axes[2].set_ylabel("Daily Return (%)")
axes[2].legend()

# Customize axes, legends, etc. as needed

# Calculate average returns during full moon and new moon periods
full_moon_avg_return_2021 = nvidia_2021[nvidia_2021['Moon Phase'] == 'Full Moon']['Daily_Return'].mean()
new_moon_avg_return_2021 = nvidia_2021[nvidia_2021['Moon Phase'] == 'New Moon']['Daily_Return'].mean()

full_moon_avg_return_2022 = nvidia_2022[nvidia_2022['Moon Phase'] == 'Full Moon']['Daily_Return'].mean()
new_moon_avg_return_2022 = nvidia_2022[nvidia_2022['Moon Phase'] == 'New Moon']['Daily_Return'].mean()

full_moon_avg_return_2023 = nvidia_2023[nvidia_2023['Moon Phase'] == 'Full Moon']['Daily_Return'].mean()
new_moon_avg_return_2023 = nvidia_2023[nvidia_2023['Moon Phase'] == 'New Moon']['Daily_Return'].mean()

print("Average Returns during Full Moon (2021): {:.2f}%".format(full_moon_avg_return_2021))
print("Average Returns during New Moon (2021): {:.2f}%".format(new_moon_avg_return_2021))
print("Average Returns during Full Moon (2022): {:.2f}%".format(full_moon_avg_return_2022))
print("Average Returns during New Moon (2022): {:.2f}%".format(new_moon_avg_return_2022))
print("Average Returns during Full Moon (2023): {:.2f}%".format(full_moon_avg_return_2023))
print("Average Returns during New Moon (2023): {:.2f}%".format(new_moon_avg_return_2023))


# Show the plots
plt.tight_layout()
plt.show()

