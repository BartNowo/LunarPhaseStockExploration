# Visuals for the moon phases and the volume of each stock starting from 2019-01-01 - current date as a bar graph and line graph respectively
# to look for a correlation between the volume of each stock to the moon phases to see if they relate to each other

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from pathlib import Path
import numpy as np

# File paths of the CSV files
tesla_file = Path(__file__).parent.parent.parent / "data" / "tesla.csv"
spy_file = Path(__file__).parent.parent.parent / "data" / "spy.csv"
nvidia_file = Path(__file__).parent.parent.parent / "data" / "nvidia.csv"
nasdaq_file = Path(__file__).parent.parent.parent / "data" / "nasdaq.csv"
moon_phases_file = Path(__file__).parent.parent.parent / "data" / "moon_phases.csv"
apple_file = Path(__file__).parent.parent.parent / "data" / "apple.csv"

# Read the stock data and moon data CSV files
df_tesla = pd.read_csv(tesla_file)
df_spy = pd.read_csv(spy_file)
df_nvidia = pd.read_csv(nvidia_file)
df_nasdaq = pd.read_csv(nasdaq_file)
df_moon = pd.read_csv(moon_phases_file)
df_apple = pd.read_csv(apple_file)

# Extract the volume data from each stock DataFrame
volume_apple = df_apple['volume']
volume_tesla = df_tesla['volume']
volume_spy = df_spy['volume']
volume_nvidia = df_nvidia['volume']
volume_nasdaq = df_nasdaq['volume']

# Extract the moon phases from the moon DataFrame
moon_phases = df_moon['Moon Phase']

# Extract the date from the moon DataFrame
date_data = df_moon['Date']

# Extract the closing price data from each stock DataFrame
closing_price_apple = df_apple['close']
closing_price_tesla = df_tesla['close']
closing_price_spy = df_spy['close']
closing_price_nvidia = df_nvidia['close']
closing_price_nasdaq = df_nasdaq['close']

# Create a new DataFrame combining the volume data and moon phases
df_combined = pd.DataFrame({
    'Apple Volume': volume_apple,
    'Tesla Volume': volume_tesla,
    'SPY Volume': volume_spy,
    'NVIDIA Volume': volume_nvidia,
    'NASDAQ Volume': volume_nasdaq,
    'Closing Price Apple': closing_price_apple,
    'Closing Price Tesla': closing_price_tesla,
    'Closing Price SPY': closing_price_spy,
    'Closing Price NVIDIA': closing_price_nvidia,
    'Closing Price NASDAQ': closing_price_nasdaq,
    'Moon Phase': moon_phases,
    'Date': date_data,
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

# Create a figure with 6 subplots: cross-correlation line graphs and a bar graph
fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2, 3, figsize=(40, 20))

def volume_tesla_graph(): # Plotting the line graph (volume data) for Tesla stock
    # Plotting the line graph (volume data) for Tesla stock
    ax1.plot(tesla_dates, tesla_volume, label='Tesla', linewidth=0.5)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_title('Volume of Tesla Stock Over Time')
    # Set y-axis limits
    ax1.set_ylim(0, 1000000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 200000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
volume_tesla_graph()

def volume_spy_graph(): # Plotting the line graph (volume data) for SPY stock
    # Plotting the line graph (volume data) for SPY stock
    ax2.plot(spy_dates, spy_volume, label='SPY', linewidth=0.5)
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Volume (Millions)')
    ax2.set_title('Volume of SPY Over Time')
    # Set y-axis limits
    ax2.set_ylim(0, 400000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 80000000 for tick in range(num_ticks + 1)]
    ax2.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax2.set_yticklabels(tick_labels)
volume_spy_graph()

def volume_nvidia_graph(): # Plotting the line graph (volume data) for NVIDIA stock
    # Plotting the line graph (volume data) for NVIDIA stock
    ax3.plot(nvidia_dates, nvidia_volume, label='NVIDIA', linewidth=0.5)
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Volume (Millions)')
    ax3.set_title('Volume of NVIDIA Stock Over Time')
    # Set y-axis limits
    ax3.set_ylim(0, 160000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 32000000 for tick in range(num_ticks + 1)]
    ax3.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax3.set_yticklabels(tick_labels)
volume_nvidia_graph()

def volume_nasdaq_graph(): # Plotting the line graph (volume data) for NASDAQ stock
    # Plotting the line graph (volume data) for NASDAQ stock
    ax4.plot(nasdaq_dates, nasdaq_volume, label='NASDAQ', linewidth=0.5)
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Volume (Millions)')
    ax4.set_title('Volume of NASDAQ Stock Over Time')
    # Set y-axis limits
    ax4.set_ylim(0, 18000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 3600000 for tick in range(num_ticks + 1)]
    ax4.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax4.set_yticklabels(tick_labels)
volume_nasdaq_graph()

def volume_apple_graph(): # Plotting the line graph (volume data) for Apple stock
    # Plotting the line graph (volume data) for Apple stock
    ax5.plot(apple_dates, apple_volume, label='Apple', linewidth=0.5)
    ax5.set_xlabel('Date')
    ax5.set_ylabel('Volume (Millions)')
    ax5.set_title('Volume of Apple Stock Over Time')
    # Set y-axis limits
    ax5.set_ylim(0, 410000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 82000000 for tick in range(num_ticks + 1)]
    ax5.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax5.set_yticklabels(tick_labels)
volume_apple_graph()

def moon_phase_graph(): # Plotting the bar graph
    ax6.bar(moon_dates, moon_phases)
    ax6.set_xlabel('Date')
    ax6.set_ylabel('Moon Phase')
    ax6.set_title('Moon Data Over Time')
moon_phase_graph()

# Create a figure with 6 subplots: scatterplot visuals and ... 
# fig2, ([ax7, ax8, ax9], [ax10, ax11, ax12]) = plt.subplots(2, 3, figsize=(20, 20))

# def cross_correlation_visual_new_moon(): # Visualize the correlation between the new moon phase and all stocks with the cross-correlation graph
#     def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
#         return data1.corr(data2.shift(lag))
#     new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon'] # Select only the rows with new moon phase
#     new_moon_phase = new_moon_phase.dropna(subset=['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume'])
#     # Calculate cross-correlation between new moon phase and stock volumes
#     cross_corr = {}
#     lags = range(-100, 101)
#     for column in df_combined.columns[:-7]:
#         cross_corr[column] = [crosscorr(new_moon_phase[column], df_combined[column], lag) for lag in lags]
#     # Plot cross-correlation as a line graph
#     for column, values in cross_corr.items():
#         ax7.plot(lags, values, label=column)
#     ax7.axhline(-1, color='black', linestyle='--')
#     ax7.set_xlabel('Lag')
#     ax7.set_ylabel('Correlation')
#     ax7.set_title('Cross-Correlation: Volume vs New Moon Phase')
#     ax7.legend()
# cross_correlation_visual_new_moon()

# def cross_correlation_visual_full_moon(): # Visualize the correlation between the full moon phase and all stocks with the cross-correlation graph
#     def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
#         return data1.corr(data2.shift(lag))
#     full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon'] # Select only the rows with full moon phase
#     full_moon_phase = full_moon_phase.dropna(subset=['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume'])
#     # Calculate cross-correlation between full moon phase and stock volumes
#     cross_corr = {}
#     lags = range(-40, 41)
#     for column in df_combined.columns[:-7]:
#         cross_corr[column] = [crosscorr(full_moon_phase[column], df_combined[column], lag) for lag in lags]
#     # Plot cross-correlation as a line graph
#     for column, values in cross_corr.items():
#         ax8.plot(lags, values, label=column)
#     ax8.axhline(-1, color='black', linestyle='--')
#     ax8.set_xlabel('Lag')
#     ax8.set_ylabel('Correlation')
#     ax8.set_title('Cross-Correlation: Volume vs Full Moon Phase')
#     ax8.legend()
# cross_correlation_visual_full_moon()

# def cross_correlation_visual_all_moonphases(): # Visualize the correlation between all moon phases and all stocks with the cross-correlation graph
#     def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
#         return data1.corr(data2.shift(lag))
#     # Filter the combined DataFrame for the desired moon phases
#     moon_phases_filter = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Last Quarter Moon', 'Waning Crescent Moon']
#     filtered_data = df_combined[df_combined['Moon Phase'].isin(moon_phases_filter)]
#     filtered_data = filtered_data.dropna(subset=['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume'])
#     # Calculate cross-correlation between all moon phases and stock volumes
#     cross_corr = {}
#     lags = range(-40, 41)
#     for column in df_combined.columns[:-7]:
#         cross_corr[column] = [crosscorr(filtered_data[column], df_combined[column], lag) for lag in lags]
#     # Plot cross-correlation as a line graph
#     for column, values in cross_corr.items():
#         ax9.plot(lags, values, label=column)
#     ax9.axhline(-1, color='black', linestyle='--')
#     ax9.set_xlabel('Lag')
#     ax9.set_ylabel('Correlation')
#     ax9.set_title('Cross-Correlation: Volume vs All Moon Phases')
#     ax9.legend()
# cross_correlation_visual_all_moonphases()

# def average_daily_stock_volume_change_percentage_moon_phase(): # Visualize the average daily stock volume change percentage as bar graphs for each stock
#     moon_phases_filter = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Last Quarter Moon', 'Waning Crescent Moon']
#     filtered_data = df_combined[df_combined['Moon Phase'].isin(moon_phases_filter)]
#     filtered_data = filtered_data.dropna(subset=['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume'])
#     # Calculate the average daily value of stock volume for each stock
#     average_volume_apple = filtered_data['Apple Volume'].mean()
#     average_volume_nasdaq = filtered_data['NASDAQ Volume'].mean()
#     average_volume_nvidia = filtered_data['NVIDIA Volume'].mean()
#     average_volume_spy = filtered_data['SPY Volume'].mean()
#     average_volume_tesla = filtered_data['Tesla Volume'].mean()
#     # Calculate the volume change percentage for each stock
#     initial_volumes = [filtered_data['Apple Volume'].iloc[0], filtered_data['NASDAQ Volume'].iloc[0], filtered_data['NVIDIA Volume'].iloc[0], filtered_data['SPY Volume'].iloc[0], filtered_data['Tesla Volume'].iloc[0]]
#     volume_changes = [(average_volume_apple - initial_volumes[0]) / initial_volumes[0] * 100,
#                       (average_volume_nasdaq - initial_volumes[1]) / initial_volumes[1] * 100,
#                       (average_volume_nvidia - initial_volumes[2]) / initial_volumes[2] * 100,
#                       (average_volume_spy - initial_volumes[3]) / initial_volumes[3] * 100,
#                       (average_volume_tesla - initial_volumes[4]) / initial_volumes[4] * 100]
#     # Create a bar graph of the average daily volume change percentage for each stock
#     stocks = ['Apple', 'NASDAQ', 'NVIDIA', 'SPY', 'Tesla']
#     ax10.bar(stocks, volume_changes)
#     ax10.set_xlabel('Stock')
#     ax10.set_ylabel('Average Daily Volume Change (%)')
#     ax10.set_title('Average Daily Stock Volume Change (%) by Stock')
# average_daily_stock_volume_change_percentage_moon_phase()

def apple_volume_vs_price_new_moon():
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon']
    new_moon_phase = new_moon_phase.dropna(subset=['Apple Volume', 'Closing Price Apple'])
    # Create a new figure and axes
    fig3, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot Apple's stock volume
    ax1.scatter(new_moon_phase['Date'], new_moon_phase['Apple Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(new_moon_phase['Apple Volume'].min(), new_moon_phase['Apple Volume'].max())
    # Plot Apple's stock price
    ax2.scatter(new_moon_phase['Date'], new_moon_phase['Closing Price Apple'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(new_moon_phase['Closing Price Apple'].min(), new_moon_phase['Closing Price Apple'].max())
    plt.suptitle("Apple's Stock Volume and Price during New Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 410000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 82000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig3.savefig("emilio_plots_3.png")
apple_volume_vs_price_new_moon()

def apple_volume_vs_price_full_moon():
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon']
    full_moon_phase = full_moon_phase.dropna(subset=['Apple Volume', 'Closing Price Apple'])
    # Create a new figure and axes
    fig4, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot Apple's stock volume
    ax1.scatter(full_moon_phase['Date'], full_moon_phase['Apple Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(full_moon_phase['Apple Volume'].min(), full_moon_phase['Apple Volume'].max())
    # Plot Apple's stock price
    ax2.scatter(full_moon_phase['Date'], full_moon_phase['Closing Price Apple'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(full_moon_phase['Closing Price Apple'].min(), full_moon_phase['Closing Price Apple'].max())
    plt.suptitle("Apple's Stock Volume and Price during Full Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 410000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 82000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig4.savefig("emilio_plots_4.png")
apple_volume_vs_price_full_moon()

def nasdaq_volume_vs_price_new_moon():
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon']
    new_moon_phase = new_moon_phase.dropna(subset=['NASDAQ Volume', 'Closing Price NASDAQ'])
    # Create a new figure and axes
    fig5, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot NASDAQ's stock volume
    ax1.scatter(new_moon_phase['Date'], new_moon_phase['NASDAQ Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(new_moon_phase['NASDAQ Volume'].min(), new_moon_phase['NASDAQ Volume'].max())
    # Plot NASDAQ's stock price
    ax2.scatter(new_moon_phase['Date'], new_moon_phase['Closing Price NASDAQ'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(new_moon_phase['Closing Price NASDAQ'].min(), new_moon_phase['Closing Price NASDAQ'].max())
    plt.suptitle("NASDAQ's Stock Volume and Price during New Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 7000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * (7000000 / 5) for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig5.savefig("emilio_plots_5.png")
nasdaq_volume_vs_price_new_moon()

def nasdaq_volume_vs_price_full_moon():
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon']
    full_moon_phase = full_moon_phase.dropna(subset=['NASDAQ Volume', 'Closing Price NASDAQ'])
    # Create a new figure and axes
    fig6, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot NASDAQ's stock volume
    ax1.scatter(full_moon_phase['Date'], full_moon_phase['NASDAQ Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(full_moon_phase['NASDAQ Volume'].min(), full_moon_phase['NASDAQ Volume'].max())
    # Plot NASDAQ's stock price
    ax2.scatter(full_moon_phase['Date'], full_moon_phase['Closing Price NASDAQ'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(full_moon_phase['Closing Price NASDAQ'].min(), full_moon_phase['Closing Price NASDAQ'].max())
    plt.suptitle("NASDAQ's Stock Volume and Price during Full Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 7000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * (7000000 / 5) for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig6.savefig("emilio_plots_6.png")
nasdaq_volume_vs_price_full_moon()

def nvidia_volume_vs_price_new_moon():
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon']
    new_moon_phase = new_moon_phase.dropna(subset=['NVIDIA Volume', 'Closing Price NVIDIA'])
    # Create a new figure and axes
    fig7, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot NVIDIA's stock volume
    ax1.scatter(new_moon_phase['Date'], new_moon_phase['NVIDIA Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(new_moon_phase['NVIDIA Volume'].min(), new_moon_phase['NVIDIA Volume'].max())
    # Plot NVIDIA's stock price
    ax2.scatter(new_moon_phase['Date'], new_moon_phase['Closing Price NVIDIA'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(new_moon_phase['Closing Price NVIDIA'].min(), new_moon_phase['Closing Price NVIDIA'].max())
    plt.suptitle("NVIDIA's Stock Volume and Price during New Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 160000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 32000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig7.savefig("emilio_plots_7.png")
nvidia_volume_vs_price_new_moon()

def nvidia_volume_vs_price_full_moon():
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon']
    full_moon_phase = full_moon_phase.dropna(subset=['NVIDIA Volume', 'Closing Price NVIDIA'])
    # Create a new figure and axes
    fig8, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot NVIDIA's stock volume
    ax1.scatter(full_moon_phase['Date'], full_moon_phase['NVIDIA Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(full_moon_phase['NVIDIA Volume'].min(), full_moon_phase['NVIDIA Volume'].max())
    # Plot NVIDIA's stock price
    ax2.scatter(full_moon_phase['Date'], full_moon_phase['Closing Price NVIDIA'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(full_moon_phase['Closing Price NVIDIA'].min(), full_moon_phase['Closing Price NVIDIA'].max())
    plt.suptitle("NVIDIA's Stock Volume and Price during Full Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 160000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 32000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig8.savefig("emilio_plots_8.png")
nvidia_volume_vs_price_full_moon()

def spy_volume_vs_price_new_moon():
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon']
    new_moon_phase = new_moon_phase.dropna(subset=['SPY Volume', 'Closing Price SPY'])
    # Create a new figure and axes
    fig9, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot SPY's stock volume
    ax1.scatter(new_moon_phase['Date'], new_moon_phase['SPY Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(new_moon_phase['SPY Volume'].min(), new_moon_phase['SPY Volume'].max())
    # Plot SPY's stock price
    ax2.scatter(new_moon_phase['Date'], new_moon_phase['Closing Price SPY'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(new_moon_phase['Closing Price SPY'].min(), new_moon_phase['Closing Price SPY'].max())
    plt.suptitle("SPY's Stock Volume and Price during New Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 400000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 80000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig9.savefig("emilio_plots_9.png")
spy_volume_vs_price_new_moon()

def spy_volume_vs_price_full_moon():
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon']
    full_moon_phase = full_moon_phase.dropna(subset=['SPY Volume', 'Closing Price SPY'])
    # Create a new figure and axes
    fig10, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot SPY's stock volume
    ax1.scatter(full_moon_phase['Date'], full_moon_phase['SPY Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(full_moon_phase['SPY Volume'].min(), full_moon_phase['SPY Volume'].max())
    # Plot SPY's stock price
    ax2.scatter(full_moon_phase['Date'], full_moon_phase['Closing Price SPY'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(full_moon_phase['Closing Price SPY'].min(), full_moon_phase['Closing Price SPY'].max())
    plt.suptitle("SPY's Stock Volume and Price during Full Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 400000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * 80000000 for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig10.savefig("emilio_plots_10.png")
spy_volume_vs_price_full_moon()

def tesla_volume_vs_price_new_moon():
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon']
    new_moon_phase = new_moon_phase.dropna(subset=['Tesla Volume', 'Closing Price Tesla'])
    # Create a new figure and axes
    fig11, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot Tesla's stock volume
    ax1.scatter(new_moon_phase['Date'], new_moon_phase['Tesla Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(new_moon_phase['Tesla Volume'].min(), new_moon_phase['Tesla Volume'].max())
    # Plot Tesla's stock price
    ax2.scatter(new_moon_phase['Date'], new_moon_phase['Closing Price Tesla'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(new_moon_phase['Closing Price Tesla'].min(), new_moon_phase['Closing Price Tesla'].max())
    plt.suptitle("Tesla's Stock Volume and Price during New Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 500000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * (500000000 / 5) for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig11.savefig("emilio_plots_11.png")
tesla_volume_vs_price_new_moon()

def tesla_volume_vs_price_full_moon():
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon']
    full_moon_phase = full_moon_phase.dropna(subset=['Tesla Volume', 'Closing Price Tesla'])
    # Create a new figure and axes
    fig12, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    # Plot Tesla's stock volume
    ax1.scatter(full_moon_phase['Date'], full_moon_phase['Tesla Volume'], c='blue')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_ylim(full_moon_phase['Tesla Volume'].min(), full_moon_phase['Tesla Volume'].max())
    # Plot Tesla's stock price
    ax2.scatter(full_moon_phase['Date'], full_moon_phase['Closing Price Tesla'], c='red')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Stock Price')
    ax2.set_ylim(full_moon_phase['Closing Price Tesla'].min(), full_moon_phase['Closing Price Tesla'].max())
    plt.suptitle("Tesla's Stock Volume and Price during Full Moon Phase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Set y-axis limits
    ax1.set_ylim(0, 500000000)
    # Set y-axis ticks
    num_ticks = 5
    tick_values = [tick * (500000000 / 5) for tick in range(num_ticks + 1)]
    ax1.set_yticks(tick_values)
    # Format y-axis tick labels
    tick_labels = [f'{tick // 1000000}M' for tick in tick_values]
    ax1.set_yticklabels(tick_labels)
    fig12.savefig("emilio_plots_12.png")
tesla_volume_vs_price_full_moon()

# Adjust the spacing between subplots
fig.subplots_adjust(hspace=0.2, wspace=0.2)
# fig2.subplots_adjust(hspace=0.4, wspace=0.2)

# Save the figures
fig.savefig("emilio_plots.png")
# fig2.savefig("emilio_plots_2.png")

# Show the figures
plt.show()