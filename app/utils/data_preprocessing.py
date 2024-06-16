import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import os

class PreprocPipeline:
    ''''
    A transformer class to preprocess the data
    '''
    def __init__(self):
        self.numerical_features = ['amount(usd)', 'lat', 'long', 'merch_lat', 'merch_long', 'age']
        self.categorical_features = ['merchant', 'job', 'hour_of_day', 'month', 'day_of_week']

        self.scaler = StandardScaler()
        self.encoder = OneHotEncoder(handle_unknown='ignore')

        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.scaler, self.numerical_features),
                ('cat', self.encoder, self.categorical_features)
            ]
        )
        

    def select_features(self, X):
        '''
        Selects the features to be used in the model and prepares the training data
        '''

        X_copy = X.set_index('transaction_id', inplace=False)
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
    
    
    def save_pipeline(self, filepath='model/pipeline.pkl', overwrite=True):
        '''
        Saves the pipeline to disk
        '''
        if not overwrite and os.path.exists(filepath):
            raise FileExistsError(f"The file {filepath} already exists.")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self, filepath)
    
    @staticmethod
    def load_pipeline(filepath='model/pipeline.pkl'):
        '''
        Loads the pipeline from disk
        '''
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        return joblib.load(filepath)