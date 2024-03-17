# Visuals for the moon phases and the volume of each stock starting from 2019-01-01 - current date as a bar graph and line graph respectively
# to look for a correlation between the volume of each stock to the moon phases to see if they relate to each other

# Result from the data of any correlation:
# 
# 
# 
# 
# 
# 
# 
# 
# 

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
import pandas as pd

# File paths of the CSV files
tesla_file = '../LunarPhaseStockExploration/data/tesla20190101.csv'
spy_file = '../LunarPhaseStockExploration/data/spy20190101.csv'
nvidia_file = '../LunarPhaseStockExploration/data/nvidia20190101.csv'
nasdaq_file = '../LunarPhaseStockExploration/data/nasdaq20190101.csv'
moon_phases_file = '../LunarPhaseStockExploration/data/moon_phases.csv'
apple_file = '../LunarPhaseStockExploration/data/apple20190101.csv'

# Read the stock data and moon data CSV files
df_tesla = pd.read_csv(tesla_file)
df_spy = pd.read_csv(spy_file)
df_nvidia = pd.read_csv(nvidia_file)
df_moon = pd.read_csv(moon_phases_file)
df_apple = pd.read_csv(apple_file)

# Extract the volume data from each stock DataFrame
volume_apple = df_apple['volume']
volume_tesla = df_tesla['volume']
volume_spy = df_spy['volume']
volume_nvidia = df_nvidia['volume']

# Extract the moon phases from the moon DataFrame
moon_phases = df_moon['Moon Phase']

# Create a new DataFrame combining the volume data and moon phases
df_combined = pd.DataFrame({
    'Apple Volume': volume_apple,
    'Tesla Volume': volume_tesla,
    'SPY Volume': volume_spy,
    'NVIDIA Volume': volume_nvidia,
    'Moon Phase': moon_phases
})

# Print the combined DataFrame
print(df_combined)

# Function to read the contents of a CSV file for the volume data
def read_volume_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        dates = []
        volume_values = []
        for row in reader:
            date = datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S").date()
            volume = float(row[4])
            dates.append(date)
            volume_values.append(volume)
        return dates, volume_values

# Function to read the contents of a CSV file for the moon phases data
def read_moonphase_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        dates = []
        moon_phases = []
        for row in reader:
            date = datetime.strptime(row[0], "%Y-%m-%d").date()
            moon_phase = row[1]
            dates.append(date)
            moon_phases.append(moon_phase)
        return dates, moon_phases

# Read the contents of each CSV file
tesla_dates, tesla_volume = read_volume_csv_file(tesla_file)
spy_dates, spy_volume = read_volume_csv_file(spy_file)
nvidia_dates, nvidia_volume = read_volume_csv_file(nvidia_file)
nasdaq_dates, nasdaq_volume = read_volume_csv_file(nasdaq_file)
apple_dates, apple_volume = read_volume_csv_file(apple_file)
moon_dates, moon_phases = read_moonphase_csv_file(moon_phases_file)

# Create a figure with two subplots: line graph and bar graph
fig, ([ax1, ax2], [ax3, ax4], [ax5, ax6]) = plt.subplots(3, 2, figsize=(13, 13))

# Plotting the line graph (volume data) for Tesla stock
ax1.plot(tesla_dates, tesla_volume, label='Tesla', linewidth=0.5)
ax1.set_xlabel('Date')
ax1.set_ylabel('Volume (Millions)')
ax1.set_title('Volume of Tesla Stock Over Time')
ax1.legend()

# Plotting the line graph (volume data) for S&P 500 stock
ax2.plot(spy_dates, spy_volume, label='S&P 500', linewidth=0.5)
ax2.set_xlabel('Date')
ax2.set_ylabel('Volume (Millions)')
ax2.set_title('Volume of S&P 500 Over Time')
ax2.legend()

# Plotting the line graph (volume data) for NVIDIA stock
ax3.plot(nvidia_dates, nvidia_volume, label='NVIDIA', linewidth=0.5)
ax3.set_xlabel('Date')
ax3.set_ylabel('Volume (Millions)')
ax3.set_title('Volume of NVIDIA Stock Over Time')
ax3.legend()

# Plotting the line graph (volume data) for NASDAQ stock
ax4.plot(nasdaq_dates, nasdaq_volume, label='NASDAQ', linewidth=0.5)
ax4.set_xlabel('Date')
ax4.set_ylabel('Volume (Millions)')
ax4.set_title('Volume of NASDAQ Stock Over Time')
ax4.legend()

# Plotting the line graph (volume data) for Apple stock
ax5.plot(apple_dates, apple_volume, label='Apple', linewidth=0.5)
ax5.set_xlabel('Date')
ax5.set_ylabel('Volume (Millions)')
ax5.set_title('Volume of Apple Stock Over Time')
ax5.legend()

# Format y-axis labels of the line graph as millions
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))

# Plotting the bar graph
ax6.bar(moon_dates, moon_phases)
ax6.set_xlabel('Date')
ax6.set_ylabel('Moon Phase')
ax6.set_title('Moon Data Over Time')

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=1, wspace=0.4)

# Save the figure
plt.savefig("volume_plot.png")

# Show the figure
plt.show()