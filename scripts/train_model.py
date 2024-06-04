import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the processed data
data = pd.read_csv('data/processed/processed_transactions.csv')

# Define features and target
X = data.drop(columns=['isFraud'])
y = data['isFraud']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Save the trained model
joblib.dump(rf, 'app/models/fraud_detection_model.pkl')