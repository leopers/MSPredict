import os
import joblib
from sklearn.base import BaseEstimator
from app.utils.data_preprocessing import PreprocPipeline
from sklearn.pipeline import Pipeline

class Model(BaseEstimator, PreprocPipeline):
    def __init__(self, model):
        super().__init__()

        self.name = 'model'
        self.version = '1.0.0'
        self.model = model

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model 

    def set_name(self, name):
        self.name = name

    def set_version(self, version):
        self.version = version
        
    def train(self, X, y):
        '''
        Trains the model
        '''
        X = self.fit_transform(X)
        self.model.fit(X, y)

    def predict(self, X):
        '''
        Predicts the target variable
        '''
        X = self.transform(X)
        return self.model.predict(X)

    def save_model(self, filepath='model/model.pkl', overwrite=True):
        '''
        Saves the model to disk
        '''
        if not overwrite and os.path.exists(filepath):
            raise FileExistsError(f"The file {filepath} already exists.")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self, filepath)
    
    @staticmethod
    def load_model(filepath='model/model.pkl'):
        '''
        Loads the model from disk
        '''
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        return joblib.load(filepath)
