import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# this file is a good template to help you guys get started it
# loads in files in df and merges them and simple plotting

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent / "data" / "moon_phases.csv"
path_to_apple_csv = Path(__file__).parent.parent / "data" / "apple.csv"
path_to_spy_csv = Path(__file__).parent.parent / "data" / "spy.csv"
path_to_nvida_csv = Path(__file__).parent.parent / "data" / "nvida.csv"
path_to_tesla_csv = Path(__file__).parent.parent / "data" / "tesla.csv"
path_to_nasdaq_csv = Path(__file__).parent.parent / "data" / "nasdaq.csv"

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# reads in stock data csv file and loads into pandas dataframe
apple_data_df = pd.read_csv(path_to_apple_csv)

# converts the date columns to datetime type
moon_phases_df['Date'] = pd.to_datetime(moon_phases_df['Date']).dt.date
apple_data_df['Date'] = pd.to_datetime(apple_data_df['timestamp']).dt.date

# merges the dataframes on the data column the inner means it will include only dates
# present in both dataframes
merged_apple_df = pd.merge(
    moon_phases_df, apple_data_df, on='Date', how='inner')

# this is not necessary but you can save the merged df to csv file just change the
# filename and it will create a csv file in the data folder
# merged_apple_df.to_csv(Path(__file__).parent / "data" / "__filename.csv___", index=False)

# creates a new dataframe that filters data for one yeat from jan 1 2020 t0 dec 31 2020
one_year_apple = merged_apple_df[(merged_apple_df['Date'] >= pd.to_datetime('2020-01-01').date()) &
                                 (merged_apple_df['Date'] <= pd.to_datetime('2020-12-31').date())]

full_moon_dates = one_year_apple[one_year_apple['Moon Phase']
                                 == 'Full Moon']['Date']
new_moon_dates = one_year_apple[one_year_apple['Moon Phase']
                                == 'New Moon']['Date']

# plotting x axis date y axis closing price for that date
plt.figure(figsize=(14, 7))
plt.plot(one_year_apple['Date'], one_year_apple['close'],
         label="Closing Price", color='blue')

# adds vlines for full moon
for date in full_moon_dates:
    plt.axvline(x=date, color='red', linestyle='--', linewidth=1,
                label='Full Moon' if date == full_moon_dates.iloc[0] else "")

# Add vertical lines for new moons
for date in new_moon_dates:
    plt.axvline(x=date, color='gray', linestyle='--', linewidth=1,
                label='New Moon' if date == new_moon_dates.iloc[0] else "")

# # styling and labeling
# plt.title('Stock Closing Prices with Moon Phases (2020)')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# plt.xticks(rotation=45)
# plt.legend()
# plt.tight_layout()

# plt.show()

print(full_moon_dates)
