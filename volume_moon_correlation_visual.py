# Visuals for the moon phases and the volume of each stock starting from 2019-01-01 - current date as a bar graph and line graph respectively
# to look for a correlation between the volume of each stock to the moon phases to see if they relate to each other

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime

# File paths of the CSV files
tesla_file = '../LunarPhaseStockExploration/data/tesla20190101.csv'
spy_file = '../LunarPhaseStockExploration/data/spy20190101.csv'
nvidia_file = '../LunarPhaseStockExploration/data/nvidia20190101.csv'
nasdaq_file = '../LunarPhaseStockExploration/data/nasdaq20190101.csv'
moon_phases_file = '../LunarPhaseStockExploration/data/moon_phases.csv'
apple_file = '../LunarPhaseStockExploration/data/apple20190101.csv'

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
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plotting the line graph (volume data)
ax1.plot(tesla_dates, tesla_volume, label='Tesla')
ax1.plot(spy_dates, spy_volume, label='S&P 500')
ax1.plot(nvidia_dates, nvidia_volume, label='NVIDIA')
ax1.plot(nasdaq_dates, nasdaq_volume, label='NASDAQ')
ax1.plot(apple_dates, apple_volume, label='Apple')
ax1.set_xlabel('Date')
ax1.set_ylabel('Volume (Millions)')
ax1.set_title('Volume Data Over Time (All Stocks)')
ax1.legend()

# Format y-axis labels of the line graph as millions
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))

# Plotting the bar graph
ax2.bar(moon_dates, moon_phases)
ax2.set_xlabel('Date')
ax2.set_ylabel('Moon Phase')
ax2.set_title('Moon Data Over Time')

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5)

# Save the figure
plt.savefig("volume_plot.png")

# Show the figure
plt.show()