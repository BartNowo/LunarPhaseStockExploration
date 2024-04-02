import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

"""
I would like to see how Nvidia's high share price on each full moon period from November 30, 2021 to 
# November 29, 2022, then after that, plot the peak price of Nvidia everyday from November 30, 2022 to 
# November 30, 2023. So essentially, I have two plots, one for the period of 11-30-2021 to 11-29-2022, and 
# one for the latter. I am plotting peak prices. I am doing this because I am studying how NVIDIA did before and 
# after ChatGPT was live, and seeing if full moon volatility had any effect on ChatGPT's first year of usage, since
# everyone was going crazy over ChatGPT, and seeing if investors saw potential in NVIDIA. I am studying full moon
# periods because many studies back that investors are most aggressive, and prices are more volatile during 
# those times.
"""

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"
path_to_nvidia_csv = Path(__file__).parent.parent.parent / "data" / "nvidia.csv"

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# reads in stock data csv file and loads into pandas dataframe
nvidia_data_df = pd.read_csv(path_to_nvidia_csv)

# converts the date columns to datetime type
moon_phases_df['Date'] = pd.to_datetime(moon_phases_df['Date']).dt.date
nvidia_data_df['Date'] = pd.to_datetime(nvidia_data_df['timestamp']).dt.date

# merges the dataframes on the data column the inner means it will include only dates
# present in both dataframes
merged_nvidia_df = pd.merge(
    moon_phases_df, nvidia_data_df, on='Date', how='inner')

# this is not necessary but you can save the merged df to csv file just change the
# filename and it will create a csv file in the data folder
# merged_nvidia_df.to_csv(Path(__file__).parent / "data" / "__filename.csv___", index=False)

# Filter data for the first period (11/30/2021 to 11/29/2022)
first_period_nvidia = merged_nvidia_df[(merged_nvidia_df['Date'] >= pd.to_datetime('2021-11-30').date()) &
                                        (merged_nvidia_df['Date'] <= pd.to_datetime('2022-11-29').date())]

# Filter data for the second period (11/30/2022 to 11/30/2023)
second_period_nvidia = merged_nvidia_df[(merged_nvidia_df['Date'] >= pd.to_datetime('2022-11-30').date()) &
                                         (merged_nvidia_df['Date'] <= pd.to_datetime('2023-11-30').date())]

# Get full moon dates for the first period
full_moon_dates_first = first_period_nvidia[first_period_nvidia['Moon Phase'] == 'Full Moon']['Date']

# Get peak prices at full moon days for the first period
peak_prices_first = first_period_nvidia.groupby('Date')['close'].max().loc[full_moon_dates_first]

# Get peak prices for everyday for the second period
peak_prices_second = second_period_nvidia.groupby('Date')['close'].max()

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 14))

# Plot for the first period
axs[0].plot(peak_prices_first.index, peak_prices_first.values, label="Peak Prices (Full Moon Period)", color='blue')
axs[0].set_title('Peak Prices of NVIDIA Stock on Full Moon Days (11/30/2021 to 11/29/2022)')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Peak Price')
axs[0].tick_params(axis='x', rotation=45)
axs[0].legend()

# Plot for the second period
axs[1].plot(peak_prices_second.index, peak_prices_second.values, label="Peak Prices (Everyday)", color='green')
axs[1].set_title('Peak Prices of NVIDIA Stock for Everyday (11/30/2022 to 11/30/2023)')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Peak Price')
axs[1].tick_params(axis='x', rotation=45)
axs[1].legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()


