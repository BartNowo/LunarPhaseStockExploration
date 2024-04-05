from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Define paths to the datasets
current_file_path = Path(__file__)  # Gets the path of the current script
path_to_moon_csv = current_file_path.parent.parent.parent / "data" / "moon_phases.csv"
path_to_apple_csv = current_file_path.parent.parent.parent / "data" / "apple.csv"

# Step 1: Read and preprocess the datasets for ML analysis
# Read moon phases data
moon_phases = pd.read_csv(path_to_moon_csv)
# Read Apple stock data
apple_data = pd.read_csv(path_to_apple_csv)

# Convert timestamp columns to datetime format
moon_phases['Date'] = pd.to_datetime(moon_phases['Date'])
apple_data['timestamp'] = pd.to_datetime(apple_data['timestamp'])

# Merge datasets based on timestamp
merged_data_ml = pd.merge_asof(apple_data, moon_phases, left_on='timestamp', right_on='Date')

# Feature engineering for ML analysis
merged_data_ml['month'] = merged_data_ml['timestamp'].dt.month
merged_data_ml['day'] = merged_data_ml['timestamp'].dt.day
merged_data_ml['hour'] = merged_data_ml['timestamp'].dt.hour

# Split dataset into training and testing sets for ML analysis
X_ml = merged_data_ml[['open', 'high', 'low', 'close', 'volume', 'vwap', 'month', 'day', 'hour']]
y_ml = merged_data_ml['Moon Phase']
X_train_ml, X_test_ml, y_train_ml, y_test_ml = train_test_split(X_ml, y_ml, test_size=0.2, random_state=42)

# Step 3: Train an ML model (Random Forest Classifier)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_ml, y_train_ml)

# Step 4: Evaluate the model performance
y_pred_ml = rf_classifier.predict(X_test_ml)
accuracy_ml = accuracy_score(y_test_ml, y_pred_ml)
print("Accuracy of ML model:", accuracy_ml)

# Step 5: Baseline comparison for ML model
baseline_accuracy_ml = y_test_ml.value_counts(normalize=True).max()
print("Baseline Accuracy of ML model:", baseline_accuracy_ml)

# Step 6: Visualize feature importances for ML model
feature_importances_ml = pd.Series(rf_classifier.feature_importances_, index=X_ml.columns)
plt.figure(figsize=(10, 6))
feature_importances_ml.nlargest(5).plot(kind='barh')
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Top 5 Feature Importances for ML Model')
plt.tight_layout()

# Step 7: Read and preprocess the datasets for analysis of stock performance by moon phase
# Read moon phases data again
moon_phases = pd.read_csv(path_to_moon_csv)
# Read Apple stock data again
apple_data = pd.read_csv(path_to_apple_csv)

# Convert timestamp columns to datetime format
moon_phases['Date'] = pd.to_datetime(moon_phases['Date'])
apple_data['timestamp'] = pd.to_datetime(apple_data['timestamp'])

# Merge datasets based on timestamp
merged_data_analysis = pd.merge_asof(apple_data.sort_values('timestamp'), moon_phases.sort_values('Date'), left_on='timestamp', right_on='Date')
merged_data_analysis['month'] = merged_data_analysis['timestamp'].dt.month
merged_data_analysis['day'] = merged_data_analysis['timestamp'].dt.day
merged_data_analysis['hour'] = merged_data_analysis['timestamp'].dt.hour

# Step 8: Analyze Stock Performance by Moon Phase

# Calculate average closing price for each moon phase
avg_prices_by_phase = merged_data_analysis.groupby('Moon Phase')['close'].mean().reset_index()

# Visualize Average Closing Price by Moon Phase (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(x='Moon Phase', y='close', data=avg_prices_by_phase.sort_values(by='close', ascending=False))
plt.xticks(rotation=45)
plt.title('Average Closing Price by Moon Phase')
plt.ylabel('Average Closing Price ($)')
plt.xlabel('Moon Phase')
plt.tight_layout()
plt.show()

# Calculate the difference between opening and closing prices
merged_data_analysis['price_change'] = merged_data_analysis['close'] - merged_data_analysis['open']
avg_price_change_by_phase = merged_data_analysis.groupby('Moon Phase')['price_change'].mean().reset_index()

# Visualize Average Daily Price Change by Moon Phase (Column Chart)
plt.figure(figsize=(10, 6))
sns.barplot(x='Moon Phase', y='price_change', data=avg_price_change_by_phase.sort_values(by='price_change', ascending=False))
plt.xticks(rotation=45)
plt.title('Average Daily Price Change by Moon Phase')
plt.ylabel('Average Price Change ($)')
plt.xlabel('Moon Phase')
plt.tight_layout()
plt.show()

# Visualize distribution of the price change (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(merged_data_analysis['price_change'], bins=20)
plt.title('Distribution of Price Change')
plt.xlabel('Price Change ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Visualize line chart for average closing price by moon phase
plt.figure(figsize=(10, 6))
sns.lineplot(x='Moon Phase', y='close', data=avg_prices_by_phase.sort_values(by='close', ascending=False), marker='o')
plt.xticks(rotation=45)
plt.title('Average Closing Price by Moon Phase')
plt.ylabel('Average Closing Price ($)')
plt.xlabel('Moon Phase')
plt.tight_layout()
plt.show()

# Visualize pie chart for distribution of moon phases
plt.figure(figsize=(8, 8))
moon_phase_counts = merged_data_analysis['Moon Phase'].value_counts()
plt.pie(moon_phase_counts, labels=moon_phase_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Moon Phases')
plt.tight_layout()
plt.show()
