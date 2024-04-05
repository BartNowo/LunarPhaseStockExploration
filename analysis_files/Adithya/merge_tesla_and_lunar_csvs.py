import pandas as pd

moon_phases_df = pd.read_csv('/workspaces/LunarPhaseStockExploration/data/moon_phases.csv')
tesla_df = pd.read_csv('/workspaces/LunarPhaseStockExploration/data/tesla.csv')

# Extract only the date component from 'timestamp' column
tesla_df['Date'] = tesla_df['timestamp'].str.split(' ').str[0]

# Merge the DataFrames on the 'Date' column
merged_df = pd.merge(moon_phases_df, tesla_df, on='Date')

# Drop the 'timestamp' column from the merged DataFrame
merged_df = merged_df.drop('timestamp', axis=1)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)