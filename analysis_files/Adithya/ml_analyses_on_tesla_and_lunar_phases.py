import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('merged_data.csv')

# Data preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df['Moon Phase'] = LabelEncoder().fit_transform(df['Moon Phase'])

# Feature engineering
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year

# Splitting the data
train_size = int(0.8 * len(df))
train_data = df[:train_size]
test_data = df[train_size:]

# Baseline Model (Linear Regression without lunar phases)
baseline_model = LinearRegression()
baseline_model.fit(train_data[['Month', 'Day', 'Year']], train_data['close'])

# ML Model (Linear Regression with lunar phases)
ml_model = LinearRegression()
ml_model.fit(train_data[['Month', 'Day', 'Year', 'Moon Phase']], train_data['close'])

# Model evaluation
def evaluate_model(model, X, y):
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)
    return mse, mae, r2

baseline_mse, baseline_mae, baseline_r2 = evaluate_model(baseline_model, test_data[['Month', 'Day', 'Year']], test_data['close'])
ml_mse, ml_mae, ml_r2 = evaluate_model(ml_model, test_data[['Month', 'Day', 'Year', 'Moon Phase']], test_data['close'])

print("Baseline Model Results:")
print("MSE:", baseline_mse)
print("MAE:", baseline_mae)
print("R-squared:", baseline_r2)

print("\nML Model Results:")
print("MSE:", ml_mse)
print("MAE:", ml_mae)
print("R-squared:", ml_r2)

# Correlation Analysis
correlation = df[['Moon Phase', 'close']].corr().iloc[0, 1]
print("\nCorrelation between Tesla stock prices and lunar phases:", correlation)

# Scatter plot of Tesla stock prices and lunar phases
plt.scatter(df['Moon Phase'], df['close'])
plt.xlabel('Moon Phase')
plt.ylabel('Tesla Stock Price')
plt.title('Correlation: Tesla Stock Prices and Lunar Phases')

# Save the plot as a PNG image
plt.savefig('correlation_plot.png')