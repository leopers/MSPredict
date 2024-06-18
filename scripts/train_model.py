import pandas as pd
from sklearn.metrics import recall_score, accuracy_score
from sklearn.model_selection import train_test_split
import joblib
from sklearn.tree import DecisionTreeClassifier
from imblearn.metrics import specificity_score

from app.utils.model import Model

data = pd.read_csv('data/processed/processed_train.csv')
test_data = pd.read_csv('data/processed/processed_test.csv')

X = data.drop('is_fraud', axis=1)
y = data['is_fraud']

X_test = test_data.drop('is_fraud', axis=1)
y_test = test_data['is_fraud']

model = Model(DecisionTreeClassifier(random_state=13,max_depth=10, class_weight='balanced'))

model.fit(X, y)

model.save_model('app/models/deploy_model/decision_tree.pkl')

# Load the model
loaded_model = model.load_model('app/models/deploy_model/decision_tree.pkl')

# Predict the target variable

y_pred = loaded_model.predict(X_test)

# Calculate scores
recall = recall_score(y_test, y_pred)
print(f'Recall Score: {recall:.4f}')
accuracy_score = accuracy_score(y_test, y_pred)
print(f'Accuracy Score: {accuracy_score:.4f}')
specificity = specificity_score(y_test, y_pred)
print(f'Specificity Score: {specificity:.4f}')

