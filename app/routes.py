from flask import Blueprint, request, redirect,url_for, jsonify, render_template, request, session, flash
import joblib
import pandas as pd

main_bp = Blueprint('main_bp', __name__)

model = joblib.load('../model/pipeline.pkl')

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

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Retrieve form data
        column1 = request.form['column1']
        column2 = request.form['column2']
        column3 = request.form['column3']
        
        # Insert data into PostgreSQL
        try:
            params = config()
            connection = psycopg2.connect(**params)
            cursor = connection.cursor()

            # Construct the SQL query
            insert_query = "INSERT INTO my_table (column1, column2, column3) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (column1, column2, column3))
            
            # Commit the transaction
            connection.commit()
            
            # Close cursor and connection
            cursor.close()
            connection.close()

            return redirect(url_for('main_bp.success'))
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "An error occurred while inserting data into the database."
    
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

@main_bp.route('/check_frauds')
def check_frauds():
    if request.method == 'POST':
        try:
            # Retrieve form data
            amount = float(request.form['amount'])
            date = pd.to_datetime(request.form['date'])

            # Prepare data for prediction
            transaction_data = pd.DataFrame({'amount': [amount], 'date': [date]})
            
            # Make prediction using the loaded model
            prediction = model.predict(transaction_data)[0]

            if prediction == 1:
                fraud_status = 'Fraudulent'
            else:
                fraud_status = 'Not Fraudulent'

            return render_template('fraud_result.html', prediction=fraud_status, amount=amount, date=date)
        
        except Exception as e:
            print(e)
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