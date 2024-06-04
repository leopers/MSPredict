# Money-Saver-Preditor

A financial transaction fraud prevention DS project following an agile methodology approach that extends SCRUM to Data Science projects

## Repository Structure

```
.
├── app/
│ ├── init.py
│ ├── main.py
│ ├── routes.py
│ ├── models/
│ │ ├── init.py
│ │ └── fraud_detection_model.pkl
│ ├── static/
│ ├── templates/
│ └── utils/
│   ├── init.py
│   └── data_preprocessing.py
├── data/
│ ├── raw/
│ │ └── transactions.csv
│ ├── processed/
│ │ └── processed_transactions.csv
├── notebooks/
│ ├── EDA.ipynb
│ ├── model_training.ipynb
│ └── model_evaluation.ipynb
├── scripts/
│ ├── preprocess_data.py
│ ├── train_model.py
│ └── evaluate_model.py
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
- Provide customer ID and time interval to query transactions and check for fraud.

## Dataset description

Dataset Description
The PaySim dataset is a synthetic dataset that simulates mobile money transactions based on real financial logs. The dataset is scaled down to 1/4 of the original size for use on Kaggle.

- Column Descriptions
- step: A time unit in the simulation, where 1 step corresponds to 1 hour. The dataset covers a total of 744 steps, equivalent to 30 days.
- type: Type of transaction, including the following categories:
- CASH-IN: Cash deposit into an account.
- CASH-OUT: Cash withdrawal from an account.
- DEBIT: Direct debit transaction.
- PAYMENT: Payment transaction.
- TRANSFER: Transfer of funds from one account to another.
- amount: The amount of money involved in the transaction, in local currency.
- nameOrig: Identifier for the customer who initiated the transaction.
- oldbalanceOrg: The initial balance of the customer's account before the transaction.
- newbalanceOrig: The new balance of the customer's account after the transaction.
- nameDest: Identifier for the recipient of the transaction.
- oldbalanceDest: The initial balance of the recipient's account before the transaction.
- newbalanceDest: The new balance of the recipient's account after the transaction.
- isFraud: A binary indicator (0 or 1) indicating whether the transaction is fraudulent. Fraudulent transactions aim to profit by taking control of customer accounts and attempting to empty funds.
- isFlaggedFraud: A binary indicator (0 or 1) indicating whether the transaction is flagged as a fraud attempt. The business model flags transactions that attempt to transfer more than 200,000 in a single 
  transaction as illegal.
  
Note:

Columns oldbalanceOrg, newbalanceOrig, oldbalanceDest, and newbalanceDest should not be used for fraud detection because transactions detected as fraud are canceled, which affects these balances.



## License

This project is licensed under the MIT License.
