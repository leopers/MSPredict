import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Load the processed data
data = pd.read_csv('data/processed/processed_transactions.csv')

# Define features and target
X = data.drop(columns=['isFraud'])
y = data['isFraud']

# Load the trained model
model = joblib.load('app/models/fraud_detection_model.pkl')

# Make predictions
predictions = model.predict(X)

# Evaluate the model
print("Classification Report:\n", classification_report(y, predictions))
print("ROC-AUC Score:", roc_auc_score(y, predictions))
