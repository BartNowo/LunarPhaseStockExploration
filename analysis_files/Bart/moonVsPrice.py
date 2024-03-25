import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / \
    "data" / "moon_phases.csv"
path_to_apple_csv = Path(__file__).parent.parent.parent / "data" / "apple.csv"
path_to_spy_csv = Path(__file__).parent.parent.parent / "data" / "spy.csv"
path_to_nvida_csv = Path(__file__).parent.parent.parent / "data" / "nvida.csv"
path_to_tesla_csv = Path(__file__).parent.parent.parent / "data" / "tesla.csv"
path_to_nasdaq_csv = Path(
    __file__).parent.parent.parent / "data" / "nasdaq.csv"

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

# Function to find the first day of each specified moon phase


def find_first_days(df, phase_name):
    # Shift the 'Moon Phase' column to find transition points
    # moves phases over 1 to use to compare against original df to see when moon changes transition
    shifted = df['Moon Phase'].shift(1, fill_value=df['Moon Phase'].iloc[0])
    # Identify rows where the current phase matches phase_name and is different from the row before
    return df[(df['Moon Phase'] == phase_name) & (df['Moon Phase'] != shifted)]['Date']


first_new_moon_dates = find_first_days(one_year_apple, 'New Moon')
first_full_moon_dates = find_first_days(one_year_apple, "Full Moon")

# Pair each new moon with the following full moon so we have the start of a new moon to the start of a full moon
cycle_data = []
for new_moon_date in first_new_moon_dates:
    following_full_moon = first_full_moon_dates[first_full_moon_dates > new_moon_date].min(
    )
    if pd.notnull(following_full_moon):
        # Get start and end prices for the start and end date
        start_price = merged_apple_df.loc[merged_apple_df['Date']
                                          == new_moon_date, 'close']
        end_price = merged_apple_df.loc[merged_apple_df['Date']
                                        == following_full_moon, 'close']

        if not start_price.empty and not end_price.empty:
            start_price = start_price.iloc[0]
            end_price = end_price.iloc[0]

            # Calculates price change and percent change
            price_change = end_price - start_price
            percent_change = (price_change / start_price) * 100

            # Append this cycle's data to the list
            cycle_data.append({
                'Start Date': new_moon_date,
                'End Date': following_full_moon,
                'Start Price': start_price,
                'End Price': end_price,
                'Price Change': price_change,
                'Percent Change': percent_change
            })


cycles_df = pd.DataFrame(cycle_data)


print(cycles_df)
