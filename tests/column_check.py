import pandas as pd

# Load the data
data = pd.read_csv('data/processed/processed_train.csv')

# Strip leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Check if 'transaction_id' column exists 
if 'transaction_id' in data.columns:
    print("Column 'transaction_id' exists in the dataset.")
else:
    print("Column 'transaction_id' is missing from the dataset.")  