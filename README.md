# Money-Saver-Preditor

## Repository Structure

```
.
├── app/
│ ├── __init__.py
│ ├── main.py
│ ├── routes.py
│ ├── models/
│ │ ├── __init__.py
│ │ └── deploy_model/
│      ├── decision_tree.pkl
│      └── fraud_detection_model.pkl
│ ├── templates/
│ └── utils/
│   ├── __init__.py
    ├── model.py
│   └── data_preprocessing.py
├── data/
│ ├── raw/
│ │ └── transactions.csv
│ ├── processed/
│ │ └── processed_transactions.csv
│ ├── results/
│ │ └── evaluation_results.csv
├── scripts/
│ ├── preprocess_data.py
│ ├── train_model.py
│ └── evaluate_model.py
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/leopers/Money-Saver-Preditor.git
   cd Money-Saver-Preditor
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure your python environment variable is setup correctly

   ```bash
   export PYTHONPATH=$(pwd)
   ```

5. Run the Flask application:
   ```bash
   python app/main.py
   ```

## Usage

- Access the web application at `http://localhost:5000`
- You can either check for fraud on a specific and existent transaction or even add new transactions to our database.

## Dataset description

About the Dataset
This is a simulated credit card transaction dataset containing legitimate and fraud transactions from the duration 1st Jan 2019 - 31st Dec 2020. It covers credit cards of 1000 customers doing transactions with a pool of 800 merchants.

Source of Simulation
This was generated using [Sparkov Data Generation | Github](https://github.com/namebrandon/Sparkov_Data_Generation) tool created by Brandon Harris. This simulation was run for the duration - 1 Jan 2019 to 31 Dec 2020. The files were combined and converted into a standard format.

## Dataset Columns

1. **`trans_date_trans_time`**: The date and time when the transaction occurred.
2. **`cc_num`**: The credit card number used for the transaction.
3. **`merchant`**: The name of the merchant where the transaction took place.
4. **`category`**: The category of the merchant or transaction.
5. **`amt`**: The amount of the transaction.
6. **`first`**: The first name of the cardholder.
7. **`last`**: The last name of the cardholder.
8. **`gender`**: The gender of the cardholder.
9. **`street`**: The street address of the cardholder.
10. **`city`**: The city of the cardholder.
11. **`state`**: The state of the cardholder.
12. **`zip`**: The ZIP code of the cardholder.
13. **`lat`**: The latitude coordinate of the cardholder's address.
14. **`long`**: The longitude coordinate of the cardholder's address.
15. **`city_pop`**: The population of the city where the cardholder resides.
16. **`job`**: The occupation of the cardholder.
17. **`dob`**: The date of birth of the cardholder.
18. **`trans_num`**: A unique identifier for the transaction.
19. **`unix_time`**: The transaction time in Unix time format.
20. **`merch_lat`**: The latitude coordinate of the merchant's location.
21. **`merch_long`**: The longitude coordinate of the merchant's location.
22. **`is_fraud`**: A binary indicator of whether the transaction is fraudulent (1) or not (0).

## License

This project is licensed under the MIT License.
