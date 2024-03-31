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

# creates a new dataframe that filters data for one yeat from jan 1 2020 t0 dec 31 2020
one_year_apple = merged_nvidia_df[(merged_nvidia_df['Date'] >= pd.to_datetime('2020-01-01').date()) &
                                 (merged_nvidia_df['Date'] <= pd.to_datetime('2020-12-31').date())]

full_moon_dates = one_year_apple[one_year_apple['Moon Phase']
                                 == 'Full Moon']['Date']
new_moon_dates = one_year_apple[one_year_apple['Moon Phase']
                                == 'New Moon']['Date']

# plotting x axis date y axis closing price for that date
plt.figure(figsize=(14, 7))
plt.plot(one_year_apple['Date'], one_year_apple['close'],
         label="Closing Price", color='green')

# adds vlines for full moon
for date in full_moon_dates:
    plt.axvline(x=date, color='red', linestyle='--', linewidth=1,
                label='Full Moon' if date == full_moon_dates.iloc[0] else "")

# Add vertical lines for new moons
for date in new_moon_dates:
    plt.axvline(x=date, color='gray', linestyle='--', linewidth=1,
                label='New Moon' if date == new_moon_dates.iloc[0] else "")

# styling and labeling
plt.title('NVIDIA Stock Closing Prices with Moon Phases (2020)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
