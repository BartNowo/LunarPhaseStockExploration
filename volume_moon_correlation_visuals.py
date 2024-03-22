# Visuals for the moon phases and the volume of each stock starting from 2019-01-01 - current date as a bar graph and line graph respectively
# to look for a correlation between the volume of each stock to the moon phases to see if they relate to each other

# Results from the data:
# ----------------------
# 1) The plots in "volume_plots.png" of the volume graphs for each stock and the moon phase over time from a general and full 5-year scope,
#    it shows that they're consistent and are volatile in unision with barely any inconsistencies.
# 2) The plots in "volume_plots_2.png" of the correlation between the volume vs new moon phase, volume vs full moon phase and volume vs all moon phases
#    with the pearson's correlation coefficient as heatwave and scatterplot visuals respectively. The correlation that's within the plots are that
#    at new moon, the volume of all stocks are negatively impacted while at full moon and against all moon phases, volume of Apple and NASDAQ stock have
#    mostly negative correlation with a bit of neutral correlation.
# 3) The plots in "volume_plots_3.png" of cross-correlation visuals between the stocks and the new moon, full moon and all moon phases respectively.
#    show decreasing of volume over time.
# 4) From the sets of graphs and visuals, it seems that it has been a landslide of volume of stocks being negatively impacted.

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

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

# Create a new DataFrame combining the volume data and moon phases
df_combined = pd.DataFrame({
    'Apple Volume': volume_apple,
    'Tesla Volume': volume_tesla,
    'SPY Volume': volume_spy,
    'NVIDIA Volume': volume_nvidia,
    'NASDAQ Volume': volume_nasdaq,
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

# Create a figure with 6 subplots: lines graph and a bar graph
fig, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2, 3, figsize=(40, 20))

def volume_tesla_graph(): # Plotting the line graph (volume data) for Tesla stock
    ax1.plot(tesla_dates, tesla_volume, label='Tesla', linewidth=0.5)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Volume (Millions)')
    ax1.set_title('Volume of Tesla Stock Over Time')
    ax1.legend()
volume_tesla_graph()

def volume_sp500_graph(): # Plotting the line graph (volume data) for S&P 500 stock
    ax2.plot(spy_dates, spy_volume, label='S&P 500', linewidth=0.5)
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Volume (Millions)')
    ax2.set_title('Volume of S&P 500 Over Time')
    ax2.legend()
volume_sp500_graph()

def volume_nvidia_graph(): # Plotting the line graph (volume data) for NVIDIA stock
    ax3.plot(nvidia_dates, nvidia_volume, label='NVIDIA', linewidth=0.5)
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Volume (Millions)')
    ax3.set_title('Volume of NVIDIA Stock Over Time')
    ax3.legend()
volume_nvidia_graph()

def volume_nasdaq_graph(): # Plotting the line graph (volume data) for NASDAQ stock
    ax4.plot(nasdaq_dates, nasdaq_volume, label='NASDAQ', linewidth=0.5)
    ax4.set_xlabel('Date')
    ax4.set_ylabel('Volume (Millions)')
    ax4.set_title('Volume of NASDAQ Stock Over Time')
    ax4.legend()
volume_nasdaq_graph()

def volume_apple_graph(): # Plotting the line graph (volume data) for Apple stock
    ax5.plot(apple_dates, apple_volume, label='Apple', linewidth=0.5)
    ax5.set_xlabel('Date')
    ax5.set_ylabel('Volume (Millions)')
    ax5.set_title('Volume of Apple Stock Over Time')
    ax5.legend()
volume_apple_graph()

def format_y_axis_labels(): # Format y-axis labels of the line graph as millions
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))
    ax3.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))
    ax4.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))
    ax5.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x * 1e-8)))
format_y_axis_labels()

def moon_phase_graph(): # Plotting the bar graph
    ax6.bar(moon_dates, moon_phases)
    ax6.set_xlabel('Date')
    ax6.set_ylabel('Moon Phase')
    ax6.set_title('Moon Data Over Time')
moon_phase_graph()

# Create a figure with 6 subplots: heatwaves and scatterplot visuals
fig2, ([ax7, ax8, ax9], [ax10, ax11, ax12]) = plt.subplots(2, 3, figsize=(20, 20))

def pearson_coorelation_visual_new_moon_heatwave(): # Visualize the correlation between the new moon phase and all stocks with the heatwave visual of Pearson's correlation coefficent
    new_moon_data = df_combined[df_combined['Moon Phase'] == 'New Moon'] # Filter the combined DataFrame for the new moon phase
    correlation_matrix_pearson = new_moon_data[['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume']].corr(method='pearson') # Calculate the correlation matrix for the new moon phase using Pearson's correlation coefficient
    sns.heatmap(correlation_matrix_pearson, annot=True, cmap='coolwarm', ax=ax7) # Plot the correlation matrix as a heatmap
    ax7.set_title("Pearson Correlation: Volume vs New Moon")
pearson_coorelation_visual_new_moon_heatwave()

def pearson_coorelation_visual_full_moon_heatwave(): # Visualize the correlation between the full moon phase and all stocks with the heatwave visual of Pearson's correlation coefficent
    full_moon_data = df_combined[df_combined['Moon Phase'] == 'Full Moon'] # Filter the combined DataFrame for the new moon phase
    correlation_matrix_pearson = full_moon_data[['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume']].corr(method='pearson') # Calculate the correlation matrix for the new moon phase using Pearson's correlation coefficient
    sns.heatmap(correlation_matrix_pearson, annot=True, cmap='coolwarm', ax=ax8) # Plot the correlation matrix as a heatmap
    ax8.set_title("Pearson Correlation: Volume vs Full Moon")
pearson_coorelation_visual_full_moon_heatwave()

def pearson_correlation_visual_all_moonphases_heatwave(): # Visualize the correlation between all moon phases and all stocks with the heatwave visual of Pearson's correlation coefficent
    # Filter the combined DataFrame for the desired moon phases
    moon_phases_filter = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Last Quarter Moon', 'Waning Crescent Moon']
    filtered_data = df_combined[df_combined['Moon Phase'].isin(moon_phases_filter)]
    correlation_matrix_pearson = filtered_data[['Apple Volume', 'NASDAQ Volume', 'NVIDIA Volume', 'SPY Volume', 'Tesla Volume']].corr(method='pearson') # Calculate the correlation matrix for the new moon phase using Pearson's correlation coefficient
    sns.heatmap(correlation_matrix_pearson, annot=True, cmap='coolwarm', ax=ax9) # Plot the correlation matrix as a heatmap
    ax9.set_title("Pearson Correlation: Volume vs All Moon Phases")
pearson_correlation_visual_all_moonphases_heatwave()

def pearson_coorelation_visual_new_moon_scatter(): # Visualize the correlation between the new moon phase and all stocks with the scatterplot visual of Pearson's correlation coefficent
    new_moon_data = df_combined[df_combined['Moon Phase'] == 'New Moon'] # Filter the combined DataFrame for the new moon phase
    ax10.scatter(new_moon_data['Apple Volume'], new_moon_data['Tesla Volume'], label='Tesla')
    ax10.scatter(new_moon_data['Apple Volume'], new_moon_data['SPY Volume'], label='S&P 500')
    ax10.scatter(new_moon_data['Apple Volume'], new_moon_data['NVIDIA Volume'], label='NVIDIA')
    ax10.scatter(new_moon_data['Apple Volume'], new_moon_data['NASDAQ Volume'], label='NASDAQ')
    ax10.set_xlabel('Apple Volume')
    ax10.set_ylabel('Volume')
    ax10.set_title('New Moon Phase: Volume vs Apple Volume')
    ax10.legend()
pearson_coorelation_visual_new_moon_scatter()

def pearson_coorelation_visual_full_moon_scatter(): # Visualize the correlation between the full moon phase and all stocks with the scatterplot visual of Pearson's correlation coefficent
    full_moon_data = df_combined[df_combined['Moon Phase'] == 'Full Moon'] # Filter the combined DataFrame for the full moon phase
    ax11.scatter(full_moon_data['Apple Volume'], full_moon_data['Tesla Volume'], label='Tesla')
    ax11.scatter(full_moon_data['Apple Volume'], full_moon_data['SPY Volume'], label='S&P 500')
    ax11.scatter(full_moon_data['Apple Volume'], full_moon_data['NVIDIA Volume'], label='NVIDIA')
    ax11.scatter(full_moon_data['Apple Volume'], full_moon_data['NASDAQ Volume'], label='NASDAQ')
    ax11.set_xlabel('Apple Volume')
    ax11.set_ylabel('Volume')
    ax11.set_title('Full Moon Phase: Volume vs Apple Volume')
    ax11.legend()
pearson_coorelation_visual_full_moon_scatter()

def pearson_correlation_visual_all_moonphases_scatter(): # Visualize the correlation between all moon phases and all stocks with the scatterplot visual of Pearson's correlation coefficent
    # Filter the combined DataFrame for the desired moon phases
    moon_phases_filter = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Last Quarter Moon', 'Waning Crescent Moon']
    filtered_data = df_combined[df_combined['Moon Phase'].isin(moon_phases_filter)]
    ax12.scatter(filtered_data['Apple Volume'], filtered_data['Tesla Volume'], label='Tesla')
    ax12.scatter(filtered_data['Apple Volume'], filtered_data['SPY Volume'], label='S&P 500')
    ax12.scatter(filtered_data['Apple Volume'], filtered_data['NVIDIA Volume'], label='NVIDIA')
    ax12.scatter(filtered_data['Apple Volume'], filtered_data['NASDAQ Volume'], label='NASDAQ')
    ax12.set_xlabel('Apple Volume')
    ax12.set_ylabel('Volume')
    ax12.set_title('All Moon Phases: Volume vs Apple Volume')
    ax12.legend()
pearson_correlation_visual_all_moonphases_scatter()

# Create a figure with 6 subplots: cross-correlation plots and ...
fig3, ([ax13, ax14, ax15], [ax16, ax17, ax18]) = plt.subplots(2, 3, figsize=(20, 20))

register_matplotlib_converters()

def cross_correlation_visual_new_moon(): # Visualize the correlation between the new moon phase and all stocks with the cross-correlation graph
    def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
        return data1.corr(data2.shift(lag))
    new_moon_phase = df_combined[df_combined['Moon Phase'] == 'New Moon'] # Select only the rows with new moon phase
    # Calculate cross-correlation between new moon phase and stock volumes
    cross_corr = {}
    lags = range(-10, 11)
    for column in df_combined.columns[:-1]:
        cross_corr[column] = [crosscorr(new_moon_phase[column], df_combined[column], lag) for lag in lags]
    # Plot cross-correlation as a line graph
    for column, values in cross_corr.items():
        ax13.plot(lags, values, label=column)
    ax13.axhline(0, color='black', linestyle='--')
    ax13.set_xlabel('Lag')
    ax13.set_ylabel('Correlation')
    ax13.set_title('Cross-Correlation: Volume vs New Moon Phase')
    ax13.legend()
cross_correlation_visual_new_moon()

def cross_correlation_visual_full_moon(): # Visualize the correlation between the full moon phase and all stocks with the cross-correlation graph
    def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
        return data1.corr(data2.shift(lag))
    full_moon_phase = df_combined[df_combined['Moon Phase'] == 'Full Moon'] # Select only the rows with full moon phase
    # Calculate cross-correlation between full moon phase and stock volumes
    cross_corr = {}
    lags = range(-10, 11)
    for column in df_combined.columns[:-1]:
        cross_corr[column] = [crosscorr(full_moon_phase[column], df_combined[column], lag) for lag in lags]
    # Plot cross-correlation as a line graph
    for column, values in cross_corr.items():
        ax14.plot(lags, values, label=column)
    ax14.axhline(0, color='black', linestyle='--')
    ax14.set_xlabel('Lag')
    ax14.set_ylabel('Correlation')
    ax14.set_title('Cross-Correlation: Volume vs Full Moon Phase')
    ax14.legend()
cross_correlation_visual_full_moon()

def cross_correlation_visual_all_moonphases(): # Visualize the correlation between all moon phases and all stocks with the cross-correlation graph
    def crosscorr(data1, data2, lag=0): # Function to calculate cross-correlation between two time series
        return data1.corr(data2.shift(lag))
    # Filter the combined DataFrame for the desired moon phases
    moon_phases_filter = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Last Quarter Moon', 'Waning Crescent Moon']
    filtered_data = df_combined[df_combined['Moon Phase'].isin(moon_phases_filter)]
    # Calculate cross-correlation between all moon phases and stock volumes
    cross_corr = {}
    lags = range(-10, 11)
    for column in df_combined.columns[:-1]:
        cross_corr[column] = [crosscorr(filtered_data[column], df_combined[column], lag) for lag in lags]
    # Plot cross-correlation as a line graph
    for column, values in cross_corr.items():
        ax15.plot(lags, values, label=column)
    ax15.axhline(0, color='black', linestyle='--')
    ax15.set_xlabel('Lag')
    ax15.set_ylabel('Correlation')
    ax15.set_title('Cross-Correlation: Volume vs All Moon Phases')
    ax15.legend()
cross_correlation_visual_all_moonphases()

# Adjust the spacing between subplots
fig.subplots_adjust(hspace=0.2, wspace=0.2)
fig2.subplots_adjust(hspace=0.4, wspace=0.2)
fig3.subplots_adjust(hspace=0.2, wspace=0.2)

# Save the figures
fig.savefig("volume_plots.png")
fig2.savefig("volume_plots_2.png")
fig3.savefig("volume_plots_3.png")

# Show the figures
plt.show()