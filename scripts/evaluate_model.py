from unittest import skip
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import make_scorer, f1_score, recall_score

from app.utils.model import Model
from app.utils.data_preprocessing import PreprocPipeline

#load the data
df = pd.read_csv('data/processed/processed_train.csv')

X = df.drop('is_fraud', axis = 1)
y = df['is_fraud']

models = [
    ('Logistic Regression', LogisticRegression(max_iter=10000, random_state=42)),
    ('Decision Tree', DecisionTreeClassifier(random_state=42, max_depth=10)),
    ('Random Forest', RandomForestClassifier(random_state=42, max_depth=10, n_estimators=100)),
    ('SVM', SVC(random_state=42, kernel='rbf', C=1.0, gamma='scale'))
]

#Stratifield KFold (10-fold cross validation)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

def evaluate_model(models, X, y):
    '''
    Evaluates the model using 10-fold cross validation
    '''
    results = {}
    for name, model in models:
        model = Model(model)

        scores = cross_val_score(model, X, y, cv=skf, scoring=make_scorer(recall_score), n_jobs=-1)

        results[name] = scores
        print(f'{name} Recall Score: {np.mean(scores):.4f} (+/- {np.std(scores):.4f})')

    return results

results = evaluate_model(models, X, y)