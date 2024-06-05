import pandas as pd
from app.utils.data_preprocessing import PreprocPipeline

# Load the raw data
data = pd.read_csv('data/raw/transactions.csv')

# Preprocess the data
pipeline = PreprocPipeline()
processed_data = pipeline.fit_transform(data)

# Save the processed data
processed_data.to_csv('data/processed/processed_transactions.csv', index=False)