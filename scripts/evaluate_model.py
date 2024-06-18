import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate, train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import make_scorer, f1_score, recall_score, accuracy_score
from imblearn.metrics import specificity_score

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
]

#Stratifield KFold (10-fold cross validation)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

def evaluate_model(models, X, y):
    '''
    Evaluates the model using 10-fold cross validation
    '''
    results = {}
    scoring = {
        'recall': make_scorer(recall_score),
        'specificity': make_scorer(specificity_score),
        'accuracy': make_scorer(accuracy_score)
    }
    
    for name, model in models:
        model = Model(model)
        cv_results = cross_validate(model, X, y, cv=skf, scoring=scoring)
        
        results[name] = {
            'recall': (cv_results['test_recall'].mean(), cv_results['test_recall'].std()),
            'specificity': (cv_results['test_specificity'].mean(), cv_results['test_specificity'].std()),
            'accuracy': (cv_results['test_accuracy'].mean(), cv_results['test_accuracy'].std())
        }
        
        print(f'{name} Recall Score: {results[name]["recall"][0]:.4f} (+/- {results[name]["recall"][1]:.4f})')
        print(f'{name} Specificity Score: {results[name]["specificity"][0]:.4f} (+/- {results[name]["specificity"][1]:.4f})')
        print(f'{name} Accuracy Score: {results[name]["accuracy"][0]:.4f} (+/- {results[name]["accuracy"][1]:.4f})')

    return results

results = evaluate_model(models, X, y)

# Save the results of evaluation (and its means and standard deviations per model) to a DataFrame

results_df = pd.DataFrame.from_dict(results, orient='index')
results_df.to_csv('data/results/evaluation_results.csv', index=True)