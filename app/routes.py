from flask import Blueprint, request, redirect,url_for, jsonify, render_template, request, session, flash
import joblib
import pandas as pd
import psycopg2
from psycopg2 import sql
from app.database.config import config
import random
from app.utils.model import Model
import csv


main_bp = Blueprint('main_bp', __name__)

#model = joblib.load('../model/pipeline.pkl')

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('main_bp.dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@main_bp.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        flash('Please login first', 'danger')
        return redirect(url_for('main_bp.login'))
    
@main_bp.route('/services')
def services():
    return render_template('services.html')

def get_db_connection():
    params = config()
    return psycopg2.connect(**params)

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieve form data
        transaction_time = request.form['transaction_time']
        credit_card_number = request.form['credit_card_number']
        merchant = request.form['merchant']
        category = request.form['category']
        amount = request.form['amount']  # Get amount as a string
        is_fraud = request.form['is_fraud']
        
        # Convert form data to appropriate types
        try:
            amount = float(amount)
            credit_card_number = int(credit_card_number)
            is_fraud = is_fraud.lower() in ['true', '1', 'yes', 'y']
            is_fraud = bool(is_fraud)  # Ensure is_fraud is a boolean
        except ValueError as e:
            print(f"Value error: {e}")
            return "Invalid input data format."

        # Insert data into PostgreSQL
        connection = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO transaction 
            (transaction_time, credit_card_number, merchant, category, amount, is_fraud) 
            VALUES 
            (%s, %s, %s, %s, %s, %s)
            """
            
            # Log the values being inserted
            print(f"Inserting values: ({transaction_time}, {credit_card_number}, '{merchant}', '{category}', {amount}, {is_fraud})")
            
            cursor.execute(insert_query, (transaction_time, credit_card_number, merchant, category, amount, is_fraud))
            
            # Commit the transaction
            connection.commit()
            
            # Close cursor and connection
            cursor.close()
            connection.close()

            return redirect(url_for('main_bp.success'))
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Database error: {error}")
            if connection:
                connection.rollback()  # Rollback the transaction in case of error
            return "An error occurred while inserting data into the database."
        
        finally:
            # Close connection
            if connection:
                connection.close()
                print("PostgreSQL connection is closed")
    
    return render_template('form.html')


@main_bp.route('/success')
def success():
    return "Data successfully inserted into the database!"

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)
        df_columns = list(df)
        columns = ','.join(df_columns)
        values = "VALUES({})".format(",".join(["%s" for _ in df_columns]))
        insert_stmt = f"INSERT INTO users ({columns}) {values}"

        conn = get_db_connection()
        cur = conn.cursor()

        for _, row in df.iterrows():
            cur.execute(insert_stmt, tuple(row))

        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('main_bp.home'))
    return render_template('upload.html')

def predict_fraud(amount, lat, long, merch_lat, merch_long, age, merchant, job, hour_of_day, month, day_of_week, transaction_id):
    # Load the machine learning model
    model = joblib.load('models/deploy_model/decision_tree.pkl')

    # Assuming you have a pandas DataFrame with columns matching your model's input features
    data = {
        'amount(usd)': [amount],
        'lat': [lat],
        'long': [long],
        'merch_lat': [merch_lat],
        'merch_long': [merch_long],
        'age': [age],
        'merchant': [merchant],
        'job': [job],
        'hour_of_day': [hour_of_day],
        'month': [month],
        'day_of_week': [day_of_week],
        'transaction_id': [transaction_id] 
    }

    df = pd.DataFrame(data)

    # Make predictions
    prediction = model.predict(df)
    
    # Assuming model.predict returns 1 for fraud and 0 for non-fraud
    return prediction[0]

@main_bp.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        try:
            # Retrieve form data from the feedback form
            feedback = request.form['feedback']

            # Retrieve transaction details passed from check_frauds
            transaction_id = request.form['transaction_id']
            transaction_time = request.form['transaction_time']
            credit_card_number = request.form['credit_card_number']
            merchant = request.form['merchant']
            category = request.form['category']
            amount = request.form['amount']


            # Write feedback and transaction info to CSV
            with open('../app/data/feedback.csv', mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([transaction_id, transaction_time, credit_card_number, merchant, category, amount, feedback])

            # Here you can process the feedback (e.g., store it in the database)
            # Example: print feedback to console
            print(f"Feedback for transaction {transaction_id}: {feedback}")

            return redirect(url_for('main_bp.dashboard'))  # Redirect to home or another page after submitting feedback
        
        except Exception as e:
            print(f"Error in submit_feedback: {e}")
            return "An error occurred while submitting feedback."

    return redirect(url_for('main_bp.home')) 

@main_bp.route('/check_frauds', methods=['GET', 'POST'])
def check_frauds():
    if request.method == 'POST':
        try:
            # Retrieve form data
            amount = float(request.form['amount'])
            lat = float(request.form['lat'])
            long = float(request.form['long'])
            merch_lat = float(request.form['merch_lat'])
            merch_long = float(request.form['merch_long'])
            age = int(request.form['age'])
            merchant = request.form['merchant_name']
            job = request.form['job']
            hour_of_day = int(request.form['hour_of_day'])
            month = int(request.form['month'])
            day_of_week = int(request.form['day_of_week'])
            transaction_id = request.form['transaction_id']

            # Prepare data for prediction
            prediction = predict_fraud(amount, lat, long, merch_lat, merch_long, age, merchant, job, hour_of_day, month, day_of_week, transaction_id)

            if prediction == 1:
                fraud_status = 'Fraudulent'
            else:
                fraud_status = 'Not Fraudulent'

            # Generate a fictional transaction ID
        
            return render_template('fraud_result.html', prediction=fraud_status, 
                                   amount=amount, lat=lat, long=long, merch_lat=merch_lat, merch_long=merch_long,
                                   age=age, merchant=merchant, job=job, hour_of_day=hour_of_day, 
                                   month=month, day_of_week=day_of_week, transaction_id=transaction_id)
        
        except Exception as e:
            print(f"Error in check_frauds: {e}")
            return "An error occurred while evaluating fraud."

    return render_template('check_frauds.html')


def load_user_credentials():
    csv_path = '../app/data/users.csv'
    users_df = pd.read_csv(csv_path)
    users_df['password'] = users_df['password'].astype(str)
    users = dict(zip(users_df['username'], users_df['password']))
    return users

def get_db_connection():
    params = config()
    conn = psycopg2.connect(**params)
    return conn

users = load_user_credentials()