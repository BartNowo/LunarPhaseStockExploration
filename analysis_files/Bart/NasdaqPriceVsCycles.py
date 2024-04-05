import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

# This file contains starts off by reading in moon data and Nasdaq stock from csv and loads data into a DataFrme
# Then we merge the two dataframes on Date and we obtain a time frame of 4 years from the merged data starting
# at 01-01-2020 to 01-01-2024. Then we find the full moon dates and new moon dates we use a function to identify
# the first day of the new moon (the start date for a cycle) and the first day of a full moon (end date of cycle)
# Then we go through each cycle obtaining the price change, percent change between cycles and we find the avg % change

# paths to each file
path_to_moon_csv = Path(__file__).parent.parent.parent / \
    "data" / "moon_phases.csv"

path_to_nasdaq_csv = Path(
    __file__).parent.parent.parent / "data" / "nasdaq.csv"

# reads in moon data csv file loads into pandas dataframe
moon_phases_df = pd.read_csv(path_to_moon_csv)

# reads in stock data csv file and loads into pandas dataframe
nasdaq_data_df = pd.read_csv(path_to_nasdaq_csv)

# converts the date columns to datetime type
moon_phases_df['Date'] = pd.to_datetime(moon_phases_df['Date']).dt.date
nasdaq_data_df['Date'] = pd.to_datetime(nasdaq_data_df['timestamp']).dt.date

# merges the dataframes on the data column the inner means it will include only dates
# present in both dataframes
merged_nasdaq_df = pd.merge(
    moon_phases_df, nasdaq_data_df, on='Date', how='inner')

# creates a new dataframe that filters data for one yeat from jan 1 2020 t0 dec 31 2020
one_year_nasdaq = merged_nasdaq_df[(merged_nasdaq_df['Date'] >= pd.to_datetime('2020-01-01').date()) &
                                   (merged_nasdaq_df['Date'] <= pd.to_datetime('2024-01-01').date())]

full_moon_dates = one_year_nasdaq[one_year_nasdaq['Moon Phase']
                                  == 'Full Moon']['Date']
new_moon_dates = one_year_nasdaq[one_year_nasdaq['Moon Phase']
                                 == 'New Moon']['Date']

# Function to find the first day of each specified moon phase


def find_first_days(df, phase_name):
    # Shift the 'Moon Phase' column to find transition points
    # moves phases over 1 to use to compare against original df to see when moon changes transition
    shifted = df['Moon Phase'].shift(1, fill_value=df['Moon Phase'].iloc[0])
    # Identify rows where the current phase matches phase_name and is different from the row before
    return df[(df['Moon Phase'] == phase_name) & (df['Moon Phase'] != shifted)]['Date']


first_new_moon_dates = find_first_days(one_year_nasdaq, 'New Moon')
first_full_moon_dates = find_first_days(one_year_nasdaq, "Full Moon")

# Pair each new moon with the following full moon so we have the start of a new moon to the start of a full moon
cycle_data = []
for new_moon_date in first_new_moon_dates:
    following_full_moon = first_full_moon_dates[first_full_moon_dates > new_moon_date].min(
    )
    if pd.notnull(following_full_moon):
        # Get start and end prices for the start and end date
        start_price = merged_nasdaq_df.loc[merged_nasdaq_df['Date']
                                           == new_moon_date, 'close']
        end_price = merged_nasdaq_df.loc[merged_nasdaq_df['Date']
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
# calculates the return for each cycle
cycles_df['Return'] = 1000 * (cycles_df['Percent Change'] / 100)
# Calculate the total outcome by summing the returns, then subtract the total initial investment
# to find the net profit (or loss).
total_return = cycles_df['Return'].sum()


print(cycles_df)
cycles_df.to_csv(Path(__file__).parent.parent.parent /
                 "data" / "nasdaq_df.csv", index=False)
avg_price_change = cycles_df['Price Change'].mean()
print("Average Price Change across all cycles:", avg_price_change)
# Count of cycles with positive price change
positive_change_count = (cycles_df['Price Change'] > 0).sum()

# Count of cycles with negative price change
negative_change_count = (cycles_df['Price Change'] < 0).sum()

# Total number of cycles analyzed
total_cycles = cycles_df.shape[0]

# Output the counts
print(
    f"Number of cycles with a positive price change: {positive_change_count}")
print(
    f"Number of cycles with a negative price change: {negative_change_count}")
print(f"Total number of cycles analyzed: {total_cycles}")
print(
    f"Percent of the time buying on the new moon and selling on the full moon would produce gains: {positive_change_count / total_cycles}")


print(f"Total return after all cycles: ${total_return:.2f}")


fig, ax = plt.subplots(figsize=(10, 6))

# Plot each cycle with color coding for price direction
for _, row in cycles_df.iterrows():
    color = 'green' if row['Price Change'] > 0 else 'red'
    # Plot a line from the start to the end of the cycle with color based on price change
    plt.plot([row['Start Date'], row['End Date']], [row['Start Price'], row['End Price']], '-o',
             color=color, label=f"{row['Start Date']} to {row['End Date']}")

# Improve readability by rotating date labels
plt.xticks(rotation=45)

# Set the date format on the x-axis to make it clearer
ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))

# Set titles and labels
plt.title('Stock Price Change from New Moon to Full Moon')
plt.xlabel('Date')
plt.ylabel('Stock Price')

# Optional: Adjust the x-axis to display dates better, especially if they are too dense
ax.xaxis.set_major_locator(mdates.MonthLocator(
    interval=1))  # Adjust the interval as needed

# Since we're using color to denote price change, a legend showing each cycle might not be necessary and can clutter the plot.
# Consider custom legends or annotations if specific cycles need highlighting.

plt.tight_layout()
plt.show()
