from flask import Blueprint, request, redirect,url_for, jsonify, render_template, request, session, flash
import joblib
import pandas as pd

main_bp = Blueprint('main_bp', __name__)

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

# @main_bp.route('/about')
# def load_user_credentials():
#     csv_path = '../app/data/users.csv'
#     users_df = pd.read_csv(csv_path)
#     users_df['password'] = users_df['password'].astype(str)
#     users = dict(zip(users_df['username'], users_df['password']))
#     return users

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('main_bp.home'))
    return render_template('form.html')

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