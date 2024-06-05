import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

class PreprocPipeline:
    ''''
    A transformer class to preprocess the data
    '''
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoder = OneHotEncoder(handle_unknown='ignore')

        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.scaler, self.numerical_features),
                ('cat', self.encoder, self.categorical_features)
            ]
        )

        self.numerical_features = ['amount(usd)', 'lat', 'long', 'merch_lat', 'merch_long', 'age']
        self.categorical_features = ['merchant', 'job', 'hour_of_day', 'month', 'day_of_week']


    def select_features(self, X):
        '''
        Selects the features to be used in the model and prepares the training data
        '''

        X.set_index('transaction_id', inplace=True)
        return X[['amount(usd)', 'lat', 'long', 'merch_lat', 'merch_long', 'age', 'merchant', 'job', 'hour_of_day', 'month', 'day_of_week']]
    
    def fit(self, X):
        '''
        Fits the transformer to the data
        '''

        X_copy = self.select_features(X)
        self.preprocessor.fit(X_copy)

    def transform(self, X):
        '''
        Transforms the data
        '''
        X = self.select_features(X)
        return self.preprocessor.transform(X)
    
    def fit_transform(self, X):
        '''
        Fits and transforms the data
        '''
        X = self.select_features(X)
        return self.preprocessor.fit_transform(X)
    
    def save_pipeline(self):
        '''
        Saves the pipeline to disk
        '''
        joblib.dump(self, 'model/pipeline.pkl')
    
    @staticmethod
    def load_pipeline():
        '''
        Loads the pipeline from disk
        '''
        return joblib.load('model/pipeline.pkl')