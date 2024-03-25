import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / \
    "data" / "moon_phases.csv"
path_to_nvidia_csv = Path(
    __file__).parent.parent.parent / "data" / "nvidia.csv"


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

# creates a new dataframe that filters data for one yeat from jan 1 2020 t0 dec 31 2020
one_year_nvidia = merged_nvidia_df[(merged_nvidia_df['Date'] >= pd.to_datetime('2020-01-01').date()) &
                                   (merged_nvidia_df['Date'] <= pd.to_datetime('2020-12-31').date())]

full_moon_dates = one_year_nvidia[one_year_nvidia['Moon Phase']
                                  == 'Full Moon']['Date']
new_moon_dates = one_year_nvidia[one_year_nvidia['Moon Phase']
                                 == 'New Moon']['Date']

# Function to find the first day of each specified moon phase


def find_first_days(df, phase_name):
    # Shift the 'Moon Phase' column to find transition points
    # moves phases over 1 to use to compare against original df to see when moon changes transition
    shifted = df['Moon Phase'].shift(1, fill_value=df['Moon Phase'].iloc[0])
    # Identify rows where the current phase matches phase_name and is different from the row before
    return df[(df['Moon Phase'] == phase_name) & (df['Moon Phase'] != shifted)]['Date']


first_new_moon_dates = find_first_days(one_year_nvidia, 'New Moon')
first_full_moon_dates = find_first_days(one_year_nvidia, "Full Moon")

# Pair each new moon with the following full moon so we have the start of a new moon to the start of a full moon
cycle_data = []
for new_moon_date in first_new_moon_dates:
    following_full_moon = first_full_moon_dates[first_full_moon_dates > new_moon_date].min(
    )
    if pd.notnull(following_full_moon):
        # Get start and end prices for the start and end date
        start_price = merged_nvidia_df.loc[merged_nvidia_df['Date']
                                           == new_moon_date, 'close']
        end_price = merged_nvidia_df.loc[merged_nvidia_df['Date']
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
avg_price_change = cycles_df['Price Change'].mean()
print("Average Price Change across all cycles:", avg_price_change)
