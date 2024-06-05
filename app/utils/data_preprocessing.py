import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

class PreprocPipeline:
    '''
    Custom transformer for data preprocessing 
    '''
    def __init__(self):
        self.categorical = ['type']
        self.numerical = ['amount', 'step', 'hour']
        self.drop_columns = ['oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud', 'nameOrig', 'nameDest']
        self.scaler = StandardScaler()
        self.fitted = False
        #No need for imputers as there are no missing values in the dataset

    def create_features(self, data):
        '''
        Create new features from the existing ones
        '''
        data_copy = data.copy()
        data_copy['hour'] = np.nan
        data_copy.hour = data.step % 24

        
        return data_copy
    
    def scale_fit(self, data):
        '''
        Scale the numerical features
        '''
        data_copy = data.copy()
        data_copy[self.numerical] = self.scaler.fit_transform(data_copy[self.numerical])
        return data_copy
    
    def scale_tranform(self, data):
        '''
        Scale the numerical features
        '''
        data_copy = data.copy()
        data_copy[self.numerical] = self.scaler.transform(data_copy[self.numerical])
        return data_copy

    def fit(self,  x_train):    
        '''
        Fit the transformer on input data
        '''
        x_copy = self.create_features(x_train)
        x_copy = x_copy.drop(columns=self.drop_columns)
        x_copy = pd.get_dummies(x_copy, columns=self.categorical)
        x_copy = self.scale_fit(x_copy)
        self.fitted = True
        return self

    def transform(self, X):
        '''
        Preprocess the input data for model training
        '''
        if not self.fitted:
            raise ValueError('Transformer must be fitted before transforming data')
        X = self.create_features(X)
        X = X.drop(columns=self.drop_columns)
        X = pd.get_dummies(X, columns=self.categorical)
        X = self.scale_tranform(X)
        return X

    def fit_transform(self, X):
        '''
        Fit and transform the input data
        '''
        self.fit(X)
        return self.transform(X)
    
    def save_pipeline(self):
        '''
        Save the preprocessing pipeline
        '''
        joblib.dump(self, 'models/preprocessing_pipeline.pkl')

    @staticmethod
    def load_pipeline():
        '''
        Load the preprocessing pipeline
        '''
        return joblib.load('models/pipeline/preprocessing_pipeline.pkl')