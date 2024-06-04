import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
class PreprocPipeline:
    '''
    Custom transformer for data preprocessing
    '''
    def __init__(self):
        # Our training dataset has only numerical features
        self._scaler = StandardScaler()
        self.drop_columns = ['nameOrig', 'nameDest', 'isFraud', 'isFlaggedFraud']
        self.fitted = False
        #No need for imputers as there are no missing values in the dataset


    def fit(self,  X_train):    
        '''
        Fit the transformer on input data
        '''
        X_copy = X_train.drop(columns=self.drop_columns)
        X_copy = pd.DataFrame(self._scaler.fit_transform(X_train))
        self.fitted = True
        return self
    

    def transform(self, X):
        '''
        Preprocess the input data for model training
        '''
        if not self.fitted:
            raise ValueError('Transformer must be fitted before transforming data')
        data = data.drop(columns=self.drop_columns)
        X = pd.DataFrame(self._scaler.transform(X))
        return X
    

    def encoder(self , y):
        '''
        Encode the target variable
        '''
        y = pd.get_dummies(y, drop_first=True)
        return y
    

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