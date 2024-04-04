from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Define paths to the datasets
current_file_path = Path(__file__)  # Gets the path of the current script
path_to_moon_csv = current_file_path.parent.parent.parent / "data" / "moon_phases.csv"
path_to_apple_csv = current_file_path.parent.parent.parent / "data" / "apple.csv"

# Step 1: Read and preprocess the datasets
moon_phases = pd.read_csv(path_to_moon_csv)
apple_data = pd.read_csv(path_to_apple_csv)

# Convert timestamp columns to datetime format
moon_phases['Date'] = pd.to_datetime(moon_phases['Date'])
apple_data['timestamp'] = pd.to_datetime(apple_data['timestamp'])

# Step 2: Merge datasets based on timestamp
merged_data = pd.merge_asof(apple_data, moon_phases, left_on='timestamp', right_on='Date')

# Step 3: Feature engineering
# Extract features from the timestamp
merged_data['month'] = merged_data['timestamp'].dt.month
merged_data['day'] = merged_data['timestamp'].dt.day
merged_data['hour'] = merged_data['timestamp'].dt.hour

# Step 4: Split dataset into training and testing sets
X = merged_data[['open', 'high', 'low', 'close', 'volume', 'vwap', 'month', 'day', 'hour']]
y = merged_data['Moon Phase']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train an ML model (Random Forest Classifier)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Step 6: Evaluate the model performance
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 7: Baseline comparison
# We can use a simple baseline such as predicting the most frequent class
baseline_accuracy = y_test.value_counts(normalize=True).max()
print("Baseline Accuracy:", baseline_accuracy)

# Step 8: Interpret the results
# Visualize feature importances
feature_importances = pd.Series(rf_classifier.feature_importances_, index=X.columns)
feature_importances.nlargest(5).plot(kind='barh')
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Top 5 Feature Importances')
plt.show()



# Aggregate Stock Price Movements by Moon Phase
avg_prices_by_phase = merged_data.groupby('Moon Phase')['close'].mean().reset_index()

# Visualize Stock Performance by Moon Phase
plt.figure(figsize=(10, 6))
sns.barplot(x='Moon Phase', y='close', data=avg_prices_by_phase.sort_values(by='close', ascending=False))
plt.xticks(rotation=45)
plt.title('Average Closing Price by Moon Phase')
plt.ylabel('Average Closing Price ($)')
plt.xlabel('Moon Phase')
plt.tight_layout()
plt.show()

# For a more detailed analysis, consider the difference between opening and closing prices
merged_data['price_change'] = merged_data['close'] - merged_data['open']
avg_price_change_by_phase = merged_data.groupby('Moon Phase')['price_change'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Moon Phase', y='price_change', data=avg_price_change_by_phase.sort_values(by='price_change', ascending=False))
plt.xticks(rotation=45)
plt.title('Average Daily Price Change by Moon Phase')
plt.ylabel('Average Price Change ($)')
plt.xlabel('Moon Phase')
plt.tight_layout()
plt.show()
