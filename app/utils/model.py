import os
from random import Random
import joblib
from sklearn.base import BaseEstimator
from app.utils.data_preprocessing import PreprocPipeline
from sklearn.pipeline import Pipeline, make_pipeline
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE

class Model(BaseEstimator):
    def __init__(self, model, resample_rs=42, model_rs = 13):
        super().__init__()

        self.name = 'model'
        self.version = '1.0.0'
        self.resample_rs = resample_rs
        self.model_rs = model_rs
        self.preprocessor = PreprocPipeline()
        self.model = model
        self.undersampler = RandomUnderSampler(sampling_strategy = 0.1 , random_state = self.resample_rs) # type: ignore
        self.oversampler = SMOTE(sampling_strategy= 'auto', random_state = self.resample_rs)

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

    def fit(self, X, y):
        '''
        Trains the model
        '''

        # Preprocess the data  
        X = self.preprocessor.fit_transform(X)
        # Resample the data
        X, y = self.undersampler.fit_resample(X, y) # type: ignore
        X, y = self.oversampler.fit_resample(X, y) # type: ignore
        # Train the model
        self.model.fit(X, y)
        return self


    def predict(self, X):
        '''
        Predicts the target variable
        '''
        X = self.preprocessor.transform(X)
        return self.model.predict(X)
    
    def score(self, X, y):
        '''
        Scores the model
        '''
        X = self.preprocessor.transform(X)
        return self.model.score(X, y)

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
