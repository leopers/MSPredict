import pandas as pd
from app.utils.data_preprocessing import preprocess_data

# Load the raw data
data = pd.read_csv('data/raw/transactions.csv')

# Preprocess the data
processed_data = preprocess_data(data)

# Save the processed data
processed_data.to_csv('data/processed/processed_transactions.csv', index=False)