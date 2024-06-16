from flask import Blueprint, request, redirect,url_for, jsonify, render_template
import joblib
import pandas as pd

main_bp = Blueprint('main_bp', __name__)

USER_DATA = {
    "username": "testuser",
    "password": "testpass"
}

# Load the trained model
#model = joblib.load('app/models/fraud_detection_model.pkl')

# Load the data
#data = pd.read_csv('data/raw/transactions.csv')

# Preprocess data (assuming you have preprocessing steps in a separate module)
#from app.utils.data_preprocessing import preprocess_data
#data = preprocess_data(data)

# @main_bp.route('/query', methods=['GET'])
# def query_transactions():
#     customer_id = request.args.get('customer_id')
#     start_time = int(request.args.get('start_time'))
#     end_time = int(request.args.get('end_time'))
    
#     # Filter transactions for the given customer ID and time interval
#     transactions = data[(data['nameOrig'] == customer_id) & (data['step'] >= start_time) & (data['step'] <= end_time)]
    
#     if transactions.empty:
#         return jsonify({'message': 'No transactions found for the given criteria.'}), 404
    
#     # Predict fraud
#     predictions = model.predict(transactions.drop(columns=['isFraud', 'nameOrig', 'nameDest']))
    
#     # Add predictions to the transactions DataFrame
#     transactions['isFraud'] = predictions
    
#     return jsonify(transactions.to_dict(orient='records'))

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            return redirect(url_for('main_bp.dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/services')
def register():
    return render_template('services.html')