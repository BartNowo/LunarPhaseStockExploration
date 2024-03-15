import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# File paths of the CSV files
tesla_file = '../LunarPhaseStockExploration/data/tesla20190101.csv'
spy_file = '../LunarPhaseStockExploration/data/spy20190101.csv'
nvidia_file = '../LunarPhaseStockExploration/data/nvidia20190101.csv'
nasdaq_file = '../LunarPhaseStockExploration/data/nasdaq20190101.csv'
moon_phases_file = '../LunarPhaseStockExploration/data/moon_phases.csv'
apple_file = '../LunarPhaseStockExploration/data/apple20190101.csv'

# Function to read the contents of a CSV file
def read_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        volume_values = []
        for row in reader:
            volume = float(row[4])
            volume_values.append(volume)
        return volume_values

# Read the contents of each CSV file
tesla_volume = read_csv_file(tesla_file)
spy_volume = read_csv_file(spy_file)
nvidia_volume = read_csv_file(nvidia_file)
nasdaq_volume = read_csv_file(nasdaq_file)
apple_volume = read_csv_file(apple_file)

# Plotting the volume data
plt.plot(tesla_volume, label='Tesla')
plt.plot(spy_volume, label='S&P 500')
plt.plot(nvidia_volume, label='NVIDIA')
plt.plot(nasdaq_volume, label='NASDAQ')
plt.plot(apple_volume, label='Apple')
plt.xlabel('Days')
plt.ylabel('Volume (Millions)')
plt.title('Volume Data')
plt.legend()

# Format y-axis labels as millions
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))

plt.show()