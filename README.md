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

## License

This project is licensed under the MIT License.
