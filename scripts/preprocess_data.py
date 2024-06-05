import pandas as pd
from datetime import datetime

# Load the raw data
train_data = pd.read_csv('data/raw/fraudTrain.csv')
test_data = pd.read_csv('data/raw/fraudTest.csv')

# Preprocess the data

    #drop first column
train_data.drop(train_data.columns[0], axis=1, inplace=True)
test_data.drop(test_data.columns[0], axis=1, inplace=True)

    #rename columns
train_data.rename(columns={"trans_date_trans_time":"transaction_time",
                         "cc_num":"credit_card_number",
                         "amt":"amount(usd)",
                         "trans_num":"transaction_id"},
                inplace=True)
test_data.rename(columns={"trans_date_trans_time":"transaction_time",
                         "cc_num":"credit_card_number",
                         "amt":"amount(usd)",
                         "trans_num":"transaction_id"},
                inplace=True)

    #convert transaction_time to datetime
train_data["transaction_time"] = pd.to_datetime(train_data["transaction_time"])
test_data["transaction_time"] = pd.to_datetime(test_data["transaction_time"])

    #convert dob to datetime
train_data["dob"] = pd.to_datetime(train_data["dob"])
test_data["dob"] = pd.to_datetime(test_data["dob"])

    #creating hour of the day column and dropping time unix
train_data["hour_of_day"] = train_data["transaction_time"].dt.hour
train_data.drop("unix_time", axis=1, inplace=True)
test_data["hour_of_day"] = test_data["transaction_time"].dt.hour
test_data.drop("unix_time", axis=1, inplace=True)

    #converting dtypes 
train_data.credit_card_number = train_data.credit_card_number.astype('category')
train_data.is_fraud = train_data.is_fraud.astype('category')
train_data.hour_of_day = train_data.hour_of_day.astype('category')
test_data.credit_card_number = test_data.credit_card_number.astype('category')
test_data.is_fraud = test_data.is_fraud.astype('category')
test_data.hour_of_day = test_data.hour_of_day.astype('category')

    # Creating age attribute
train_data["age"] = train_data["transaction_time"].dt.year - train_data["dob"].dt.year
test_data["age"] = test_data["transaction_time"].dt.year - test_data["dob"].dt.year

    # Creating day of the week attribute
train_data["day_of_week"] = train_data["transaction_time"].dt.dayofweek
test_data["day_of_week"] = test_data["transaction_time"].dt.dayofweek

    # Creating month attribute
train_data["month"] = train_data["transaction_time"].dt.month
test_data["month"] = test_data["transaction_time"].dt.month


# Save the processed data
train_data.to_csv('data/processed/processed_train.csv', index=False)
test_data.to_csv('data/processed/processed_test.csv', index=False)